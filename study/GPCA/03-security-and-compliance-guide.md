# Domain 3 Study Guide — Designing for Security and Compliance

> Condensed from the 79-question bank in [`03-security-and-compliance.md`](03-security-and-compliance.md). Covers about 19% of the exam: identity, the resource hierarchy, IAM, organization policies, VPC Service Controls, secure access, encryption, sensitive data, supply chain, compliance regimes and audit logs. Citations look like (Exam N · QM).

---

## 1. Identity and federation

### Key facts
- Google Cloud authenticates people through **Cloud Identity** or **Google Workspace** accounts. You don't create users inside a project.
- **Google Cloud Directory Sync (GCDS)** copies users and groups from Active Directory or LDAP into Cloud Identity. It is one-way and doesn't copy passwords.
- **SAML 2.0 SSO** lets users sign in with the existing corporate IdP (AD FS, Okta, Ping, Entra ID). Passwords stay in the IdP, so users keep their usual login and the security team keeps password control (Exam 1 · Q10).
- Keep AD as the source of truth → **GCDS to sync accounts + SAML SSO to authenticate** (Exam 2 · Q5).
- **Workforce Identity Federation** lets users from an external IdP reach Google Cloud without being synced into Cloud Identity at all. It is the newer option when you don't want to copy accounts.
- **Domain restricted sharing** (organization policy `iam.allowedPolicyMemberDomains`) stops anyone from granting IAM roles to identities outside your Cloud Identity / Workspace customer ID (Exam 3 · Q58).

### Decision rules
- "Minimize user disruption" + "strict password storage rules" → **federate via SAML with the existing IdP** (Exam 1 · Q10).
- "Keep the on-prem AD domain controller" → **GCDS + SAML SSO** (Exam 2 · Q5).
- "No more grants to users outside our domain, from now on" → **org policy: restrict identities by domain** (Exam 3 · Q58).

### Traps
- Password Sync (formerly G Suite Password Sync) copies password hashes into Google, which is exactly what a strict password policy forbids (Exam 1 · Q10).
- GCDS alone provisions accounts but doesn't solve authentication. Asking users to set a matching Google password is the worst choice (Exam 1 · Q10).
- IAP is not an identity provider bridge to AD, and a domain controller replica on Compute Engine adds work without federating sign-in (Exam 2 · Q5).
- Scheduled scripts or Cloud Functions that strip foreign members after the fact are reactive and fragile. An org policy prevents the grant in the first place (Exam 3 · Q58).

---

## 2. Resource hierarchy and policy inheritance

### Key facts
- Hierarchy: **Organization → Folders → Projects → Resources**. One company normally has **one organization**.
- **Folders** group projects by department, business unit or environment. Grant roles and set policies on a folder and every project under it inherits them, including projects created later (Exam 1 · Q35), (Exam 3 · Q18).
- IAM **allow policies are additive**. The effective allow policy at a node is the **union** of its own policy and its ancestors' (Exam 1 · Q46). A role granted higher up can't be taken away lower down by an allow policy.
- **IAM deny policies** (separate from allow policies) can block specific permissions, and deny is checked first. Older questions assume they don't exist.
- To stop a group that is Owner at the org from acting in one folder, **remove the org-level grant** and re-grant only where needed (Exam 3 · Q8).
- The **project** is the main isolation boundary for IAM, billing and quotas. Dev, staging and prod each get their own project (Exam 4 · Q28).

### Typical layouts

| Requirement | Design | Source |
|---|---|---|
| Central control, departments manage their own policies | One org, one folder per department | (Exam 1 · Q35) |
| Same duties per department, projects come and go | Google Group per department, roles on the department folder | (Exam 3 · Q18) |
| Developers create projects but can't touch prod | `Development` and `Production` folders; Project Creator on Development only; baseline at org, stricter policies on Production | (Exam 3 · Q52) |
| Finance limited to regions, Marketing prod/dev split, R&D isolated, auditors see all | Folder per business unit; location policy on Finance folder; separate mktg-prod and mktg-dev projects; compliance team `roles/viewer` at org | (Exam 5 · Q78) |
| Dev and test can see each other; neither can reach staging or prod | One project each for dev, staging, prod | (Exam 4 · Q28) |

### Decision rules
- "Centralize, but let departments decide" → **single org + folder per department** (Exam 1 · Q35).
- "Minimize admin overhead" + "clear view of permissions" → **groups + folder-level roles** (Exam 3 · Q18).
- Inherited permission is too broad → **remove it at the higher level**; adding a weaker role lower down changes nothing (Exam 3 · Q8).
- Security or audit team needs visibility of everything → **Organization Viewer + Project Viewer** (or `roles/viewer` at the org) (Exam 3 · Q41), (Exam 3 · Q46), (Exam 5 · Q78).

### Traps
- Multiple organizations per department break central policy management (Exam 1 · Q35), (Exam 5 · Q78). So does a second Workspace account or letting developers build projects outside the org (Exam 3 · Q52).
- Granting Viewer on the Finance folder doesn't cancel Owner inherited from the org; the union still includes Owner (Exam 3 · Q8), (Exam 1 · Q46).
- Effective policy is not the intersection, and lower nodes don't restrict their ancestors (Exam 1 · Q46).
- Assigning roles to individuals, or per project, doesn't scale (Exam 3 · Q18).
- Splitting environments by network or subnet doesn't separate IAM; only projects do (Exam 4 · Q28).
- Project Owner and Organization Administrator are far beyond "visibility" (Exam 3 · Q41), (Exam 3 · Q46).

---

## 3. IAM roles, service accounts and least privilege

### Key facts
- Grant roles to **groups**, not individuals. Prefer **predefined** roles at the **lowest level** that works.
- **BigQuery split**: `bigquery.jobUser` (run jobs, billed to *that* project) on the billing project; `bigquery.dataViewer` on the data. Queries bill to the project where the job runs (Exam 1 · Q54).
- Per-country datasets: one group per country with dataset-level read access, and a parent group holding `jobUser` (Exam 2 · Q22).
- Workloads authenticate as **service accounts**. A VM uses its **attached service account** with the right IAM roles; no stored tokens or keys (Exam 2 · Q13).
- A VM call to an API can fail because the SA lacks a role **or** because the VM's **access scopes** exclude that API. Best practice: a dedicated SA with least-privilege roles and the `cloud-platform` scope (Exam 1 · Q9).
- **Service account impersonation**: a principal with `roles/iam.serviceAccountTokenCreator` gets short-lived tokens for an SA. No keys are downloaded.
- **Workload Identity Federation for GKE** maps a Kubernetes service account to an IAM service account, so pods never handle keys (Exam 4 · Q42).
- **Workload Identity Federation** does the same for workloads outside Google Cloud (AWS, Azure, GitHub Actions, on-prem OIDC/SAML).
- Service-to-service calls (Cloud Run / Cloud Run functions): turn on **require authentication**, give the caller's dedicated SA the **Invoker** role on the callee, and send a Google-signed **ID token** (Exam 4 · Q44).
- Cross-project access: create the SA where the data lives and grant it on both projects (Exam 4 · Q38).
- **IAM Conditions** can make a grant expire: a date/time condition gives temporary access with no clean-up job, and every access stays attributable to the user (Exam 5 · Q68).
- **Signed URLs** give time-limited access to one object for people with no Google account (Exam 1 · Q55).

### Separation of duties (SoD)
- Give different teams roles in **different projects** so one team can't do the other's job.
- **Shared VPC**: the networking team holds Network Admin in the **host project**; developers hold Compute Admin in a **service project** that uses the shared network. Network admins can't touch the VMs and developers can't change the network (Exam 3 · Q4).

### Decision rules
- "Billed to one project, read-only on the data" → **jobUser on billing project + dataViewer on data projects** (Exam 1 · Q54).
- Each country sees only its data → **dataset-level view access per country group** (Exam 2 · Q22).
- VMs pushing to Pub/Sub → **VM service account with Pub/Sub roles** (Exam 2 · Q13).
- GKE pods calling Google APIs → **Workload Identity** (Exam 4 · Q42).
- "Only function X may call function Y" → **IAM invoker + ID token** (Exam 4 · Q44).
- "Temporary access for a known period" → **IAM Condition with an expiry** on a group binding (Exam 5 · Q68).
- External users, no Google account, time-limited upload → **signed URL** (Exam 1 · Q55).
- Network team owns networking, devs own VMs, neither sees the other's data → **Shared VPC host + service project** (Exam 3 · Q4).

### Traps
- `bigquery.user` lets users create datasets; swapping jobUser and dataViewer bills the wrong project (Exam 1 · Q54).
- Granting `dataViewer` project-wide to all analysts lets every country read every dataset; table-by-table sharing is more work (Exam 2 · Q22).
- Access scopes are not IAM roles; you can't "grant Pub/Sub roles through scopes" (Exam 2 · Q13). Encrypted OAuth tokens in a bucket, or a Cloud Function gateway, are needless work.
- Kubernetes Secrets are only base64-encoded. Encrypting them with KMS or running Vault still leaves a long-lived key to protect (Exam 4 · Q42).
- Shared tokens in env vars, or VPC/firewall rules, don't prove which caller is calling. Two functions sharing one SA defeats least privilege (Exam 4 · Q44).
- Organization Admin for a database client is never least privilege (Exam 4 · Q38).
- Scheduled functions that add and remove bindings, signed URLs from a shared SA (not attributable), and Workforce session length (that's not an access window) all lose to an IAM Condition (Exam 5 · Q68).
- Cloud Storage has no "bucket password" (Exam 1 · Q55).
- One project with both teams, or separate VPCs joined by VPN or peering, doesn't put the network under one team's control (Exam 3 · Q4).

---

## 4. Organization policies and network guardrails

### Key facts
- **Organization Policy Service** sets constraints on *what* can be configured, regardless of who has IAM permission. Policies inherit down the hierarchy.
- `compute.vmExternalIpAccess`: list the instances allowed to have external IPs; everything else is blocked (Exam 2 · Q47), (Exam 4 · Q22).
- `gcp.resourceLocations` (**Resource Location Restriction**): limit the regions where resources can be created (Exam 4 · Q39), (Exam 5 · Q25), (Exam 5 · Q78).
- `iam.allowedPolicyMemberDomains`: domain restricted sharing (Exam 3 · Q58).
- **Hierarchical firewall policies** attach to the org or a folder and are evaluated before VPC firewall rules. Project teams can't override them. Apply them on the **production folder** to cover current and future prod projects only (Exam 5 · Q35).
- **Cloud Armor** is the WAF and DDoS layer on external Application Load Balancers. It gives L3/L4 DDoS protection and L7 rules (preconfigured WAF rules, rate limits, custom rules) (Exam 5 · Q10).
- Cloud Armor **named IP address lists** hold a CDN's published ranges (e.g. `sourceiplist-fastly`). Allow them with `evaluatePreconfiguredExpr('sourceiplist-fastly')` in a security policy rule (Exam 4 · Q12).
- **GKE private cluster with a private endpoint + authorized networks** gives the smallest attack surface: nodes have no public IPs and the control plane has no public endpoint (Exam 4 · Q23).

### Decision rules
- "Only approved VMs may have public IPs, across all VPCs" → **org policy `vmExternalIpAccess` with an allow list** (Exam 2 · Q47), (Exam 4 · Q22).
- "Resources only in these regions" → **Resource Location Restriction** at the org or folder (Exam 4 · Q39), (Exam 5 · Q25).
- "Block ingress in prod, allow HTTPS to tagged VMs, teams can't override" → **hierarchical firewall policy on each production folder** (Exam 5 · Q35).
- Multi-layer DDoS on a streaming service → **Cloud Armor** with preconfigured and custom rules (Exam 5 · Q10).
- Only traffic from a CDN's IP ranges → **Cloud Armor rule using the named IP list** (Exam 4 · Q12).
- Minimize GKE attack surface → **private cluster, private endpoint, authorized networks** (Exam 4 · Q23).

### Traps
- Removing default routes, building custom VPCs or using Cloud NAT doesn't *enforce* anything across all VPCs (Exam 2 · Q47).
- IAM roles control who can act, not what values are allowed. Removing `networkAdmin` or creating a custom role doesn't stop a misconfigured IP (Exam 4 · Q22).
- IAM Conditions, quotas of zero, alerts, Terraform defaults and Asset Inventory reports are not enforcement (Exam 4 · Q39), (Exam 5 · Q25).
- A hierarchical policy at the org root also hits dev and staging. Per-project Terraform can be changed by the teams. Blocking all external IPs is a different control (Exam 5 · Q35).
- VPC firewall rules behind an external Application Load Balancer see the proxy addresses, not the client IPs, so filtering by client source range belongs in Cloud Armor (Exam 4 · Q12).
- VPC Service Controls, Cloud NGFW and Security Command Center don't stop DDoS (Exam 5 · Q10).
- A public endpoint, even with authorized networks, is a larger surface than a private one (Exam 4 · Q23).

---

## 5. VPC Service Controls and data exfiltration

### Key facts
- **VPC Service Controls (VPC-SC)** draws a **service perimeter** around projects and restricts which Google APIs (Cloud Storage, BigQuery, Vertex AI...) can move data in or out. It stops exfiltration even by someone with valid IAM credentials.
- **Access levels** (Access Context Manager) allow requests from outside the perimeter based on IP range, device or identity, e.g. only the office CIDR (Exam 2 · Q49).
- On-prem hosts reach a perimeter over VPN/Interconnect with **Private Google Access for on-premises hosts** (`restricted.googleapis.com`) (Exam 3 · Q30), (Exam 5 · Q50).
- Protect the right **service names**: for Vertex AI and Workbench that's `aiplatform.googleapis.com` and `notebooks.googleapis.com` (Exam 5 · Q53).
- Developers who need Cloud Shell can't work inside a perimeter (Cloud Shell runs outside it), so put the perimeter **only around sensitive projects** and keep developers out of it (Exam 4 · Q60).
- To keep sensitive bucket data from leaving a protected boundary (e.g. a `europe-west2` bucket for a hospital), VPC-SC is the keyed control (Exam 4 · Q56).

### Decision rules
- "Prevent exfiltration by insiders, compromised code or oversharing" + BigQuery + VPN → **VPC-SC + Private Google Access for on-prem hosts** (Exam 3 · Q30), (Exam 5 · Q50).
- "Analysts may read only from the office network" → **perimeter + access level on the office CIDR** (Exam 2 · Q49).
- Harden Vertex AI against exfiltration → **perimeter on aiplatform + notebooks APIs** (Exam 5 · Q53).

### Traps
- Private Google Access alone is a routing feature; it doesn't stop data leaving (Exam 3 · Q30), (Exam 5 · Q50), (Exam 5 · Q53).
- Locking the project down to one SA breaks every user and still doesn't block exfiltration (Exam 3 · Q30), (Exam 5 · Q50).
- Private Service Connect is about private endpoints, not exfiltration control (Exam 5 · Q50).
- `ml.googleapis.com` is the retired AI Platform API, and `document.googleapis.com` is Document AI (Exam 5 · Q53).
- Firewall rules don't govern access to Google APIs; scheduled IAM changes aren't location-based (Exam 2 · Q49).
- IAM roles and ACLs control *who*, not *where data may go* (Exam 4 · Q56). Flow Logs only observe (Exam 5 · Q53).
- Putting developers in an access level that admits Cloud Shell punches a hole in the perimeter (Exam 4 · Q60).

---

## 6. Zero trust and secure remote access

### Key facts
- **Zero trust (BeyondCorp)**: no implicit trust for being "on the network". Every request is checked on identity, device and context. Combine IAM, workload identity, central logging and automated controls across cloud and on-prem (Exam 5 · Q21).
- **Identity-Aware Proxy (IAP)** puts Google sign-in and IAM checks in front of web apps (`roles/iap.httpsResourceAccessor`). It works for apps behind a Google load balancer and, via the **IAP on-premises connector** (or a hybrid NEG), for apps in your own data center (Exam 4 · Q57).
- **IAP TCP forwarding** lets you SSH/RDP to VMs with no external IP and no VPN. You need `roles/iap.tunnelResourceAccessor` (IAP-secured Tunnel User) and a firewall rule allowing `35.235.240.0/20` (Exam 3 · Q7).
- **Chrome Enterprise Premium** (formerly BeyondCorp Enterprise) adds context-aware access, device posture and threat protection on top of IAP.

### Decision rules
- Replace VPN with BeyondCorp for an on-prem web app, users on Workspace SSO → **IAP connector to the app** (Exam 4 · Q57).
- SSH to a VM with no public IP and no VPN → **IAP TCP forwarding + IAP-secured Tunnel User + `gcloud compute ssh`** (Exam 3 · Q7).
- After breaches, hybrid estate, EU rules, incident readiness → **zero trust: IAM, workload identity, central logging, automated controls** (Exam 5 · Q21).

### Traps
- Cloud NAT is outbound only; you can't SSH to it (Exam 3 · Q7). A TCP proxy LB exposes the VM publicly; a bastion host needs a public IP and patching.
- Cloud Armor filters traffic but doesn't authenticate users (Exam 4 · Q57). App Engine Viewer is unrelated to an on-prem app.
- Perimeter firewalls alone, encryption at rest alone, or outsourcing security are not a framework (Exam 5 · Q21).

---

## 7. Encryption, key management and secrets

### Key facts
- Everything is encrypted at rest by default with **Google-managed keys**.
- **CMEK** (customer-managed encryption keys): keys in **Cloud KMS** that you own, rotate, disable and audit. Set a CMEK as a bucket's or dataset's **default key** and services use it transparently (Exam 3 · Q23), (Exam 5 · Q6).
- **Cloud KMS protection levels**: `SOFTWARE`, `HSM` (Cloud HSM, FIPS 140-2 Level 3, keys generated and kept inside Google's HSMs), `EXTERNAL` (Cloud EKM, key stays in your external key manager) (Exam 5 · Q70).
- **Key import**: bring key material generated outside Google into Cloud KMS. The imported key is then a normal CMEK (Exam 3 · Q22).
- **CSEK** (customer-supplied keys): you send the raw AES-256 key with each request. Only Cloud Storage and Compute Engine support it. With gsutil you set it in the `.boto` file; with `gcloud storage cp` use `--encryption-key` (Exam 2 · Q2).
- BigQuery supports Google-managed keys and CMEK, **not CSEK** (Exam 3 · Q22).
- **Secret Manager** stores credentials, API keys and certificates with IAM, versions, rotation and audit logs. Use it for database credentials in many microservices (Exam 1 · Q27), (Exam 3 · Q40).
- **Digital signatures** prove who sent something and that it wasn't changed. Sign with the sender's **private key**, verify with the public key (Exam 1 · Q36). Sign each log entry with its timestamp to make logs verifiable (Exam 3 · Q51).

### Which key option?

| Requirement | Pick | Source |
|---|---|---|
| Must rotate the key; data processed later by Dataproc | CMEK as bucket default key | (Exam 3 · Q23) |
| Ownership, control and audit of keys, easy integration | CMEK on sensitive buckets + fine-grained IAM | (Exam 5 · Q6) |
| Keys generated and stored only in a certified HSM, fully managed | Cloud KMS key with `HSM` protection level | (Exam 5 · Q70) |
| Key must be generated outside Google Cloud | Import the key into Cloud KMS, use it as CMEK | (Exam 3 · Q22) |
| Upload from on-prem with your own raw key | CSEK (`.boto` for gsutil) | (Exam 2 · Q2) |

### Decision rules
- "Rotate keys" + "best practice" → **CMEK default key on the bucket**, not manual encryption (Exam 3 · Q23).
- "Ownership, control, audit visibility" → **CMEK** (Exam 5 · Q6).
- "Generated and stored in an HSM" + "fully managed" → **Cloud HSM** (Exam 5 · Q70).
- "Generated externally" → **imported key** in Cloud KMS (Exam 3 · Q22).
- Credentials for many services → **Secret Manager** (Exam 1 · Q27), (Exam 3 · Q40).
- Prevent spoofed messages → **sign with the sender's private key** (Exam 1 · Q36).

### Traps
- Default Google-managed encryption gives you no key control (Exam 5 · Q6). Vault on GKE is self-managed work.
- Manual KMS `encrypt` calls, GPG or CSEK mean Dataproc can't read the data transparently (Exam 3 · Q23).
- CSEK keeps the key outside Google; EKM keeps it in *your* HSM, not Google's; importing into a `SOFTWARE` key isn't HSM-protected (Exam 5 · Q70).
- Keys generated in Cloud KMS fail "generated externally" (Exam 3 · Q22). See questionable answers.
- `gcloud config` has no CSEK setting, and older gsutil has no `--encryption-key` flag (Exam 2 · Q2).
- Source code, environment variables and ACL-protected config files are not secret stores (Exam 1 · Q27), (Exam 3 · Q40).
- Client-side tags can be forged; TLS protects the channel, not authorship; a shared key can't tell users apart (Exam 1 · Q36).
- Dual-writing logs or locking down a SQL table doesn't prove a log entry is authentic (Exam 3 · Q51).

---

## 8. Sensitive data, PII and securing AI

### Key facts
- **Sensitive Data Protection** (formerly Cloud DLP; the API is still the DLP API) discovers, classifies and **de-identifies** PII and card data: redaction, masking, tokenization, format-preserving encryption (Exam 1 · Q38).
- Run de-identification **in the ingest pipeline** (e.g. Dataflow calling the DLP API) so PII never lands in storage (Exam 3 · Q55).
- Feed de-identified data to downstream services such as a recommendation engine (Exam 4 · Q63).
- **Tokenization** reduces PCI scope: only the token vault holds card numbers, so analytics systems stay out of scope (Exam 1 · Q14). **Deterministic** encryption gives the same token for the same card, which allows duplicate detection (Exam 4 · Q11).
- **BigQuery authorized views**: put views that exclude PII columns in a **separate dataset**, grant the team access to that dataset, and authorize the views to read the source (Exam 3 · Q60).
- **Right to erasure**: keep a unique ID per person and **delete their rows** on request; hashing or hiding them in a view is not deletion (Exam 2 · Q44).
- Audit logs in BigQuery with partition expiration support anonymized reporting and timed deletion at low cost (Exam 4 · Q58).
- **Confidential Computing** (Confidential VMs, Confidential GKE Nodes) encrypts data **in use**. With column-level encryption at rest, it protects PII through model training without de-identifying it, so model quality is kept (Exam 5 · Q27).
- **Model Armor** screens LLM prompts and responses for prompt injection, jailbreaks, sensitive data leaks, malicious URLs and harmful content.
- For Vertex AI, the exfiltration control is a **VPC-SC perimeter** around its APIs (Exam 5 · Q53).

### Decision rules
- Strip PII/PCI before storing → **DLP API de-identification** (Exam 1 · Q38), (Exam 3 · Q55).
- "Reduce PCI scope, keep analytics" → **tokenization** (Exam 1 · Q14).
- PII columns for one team, the rest for another, low cost → **authorized views in a separate dataset** (Exam 3 · Q60).
- "Delete personal data on request" → **unique ID + delete rows** (Exam 2 · Q44).
- Protect PII during training **without losing model quality** → **column-level encryption + Confidential GKE Nodes** (Exam 5 · Q27).
- Personalization with PII → **DLP API before the recommendation service** (Exam 4 · Q63).

### Traps
- SHA-256 hashing everything destroys useful data; ECC encryption doesn't remove PII; regexes miss cases (Exam 1 · Q38).
- Separate projects or subnets for card data isolate it but don't shrink PCI scope; labels and log exports don't either (Exam 1 · Q14).
- Storing PII anywhere (a retention bucket, a locked bucket, partner-loaded tables) fails "without retaining any PII" (Exam 3 · Q55).
- Views in the source dataset can't be shared without exposing the source; materialized views cost more (Exam 3 · Q60).
- Tokenizing PII before training hides signal, so it fails "without reducing model quality". CMEK protects data at rest, not in use (Exam 5 · Q27).
- Processing PII on-prem or using AutoML doesn't de-identify anything (Exam 4 · Q63).
- Secret Manager and Memorystore are not token stores (Exam 4 · Q11).

---

## 9. Software supply chain and workload hardening

### Key facts
- **Artifact Registry** stores images; **Artifact Analysis** (formerly Container Analysis) scans them for vulnerabilities, generates **SBOMs** (dependency inventories) and stores metadata. **Cloud Build** produces signed, verifiable **build provenance** (SLSA) (Exam 5 · Q44).
- **Binary Authorization** admits an image to GKE or Cloud Run only if it has the required **attestations** (e.g. "built by CI", "passed tests in staging"). Per-cluster policies enforce dev → staging → prod promotion (Exam 3 · Q19), (Exam 4 · Q18).
- Shift left: put **static analysis (SAST)** and **vulnerability scanning** into CI/CD so checks are automated and don't slow releases (Exam 3 · Q47).
- Block vulnerable images: **scan early, use Google-maintained base images**, and **fail the deployment on critical findings** (Exam 5 · Q83).
- GKE hardening: **no privileged containers**, and use the native Cloud Logging / Monitoring integration for metrics (Exam 4 · Q59).
- Understand a CVE's impact on Google Cloud → **Security Bulletins** and a **support case** (Exam 4 · Q46).

### Decision rules
- "Scan images + verifiable build metadata + dependency inventory" → **Cloud Build + Artifact Registry + Artifact Analysis** (Exam 5 · Q44).
- "Images skip dev/staging and go straight to prod" → **Binary Authorization + attestations from CI** (Exam 3 · Q19).
- Secure deployments for EHR → **Binary Authorization with CI signing + registry vulnerability scanning** (Exam 4 · Q18).
- DevSecOps without slowing releases → **SAST + vulnerability scanning in the pipeline** (Exam 3 · Q47).

### Traps
- Lifecycle hooks, custom admission controllers or written policy are slower or unenforced (Exam 3 · Q19).
- Kritis is the open-source basis of Binary Authorization, not the managed choice; Container Registry is shut down, replaced by Artifact Registry (Exam 4 · Q18).
- Security Command Center and Cloud Asset Inventory don't produce SBOMs or provenance (Exam 5 · Q44).
- Manual security review of every commit or every report doesn't scale with fast releases (Exam 3 · Q47), (Exam 5 · Q83).
- Shielded GKE Nodes protect node boot integrity; they don't block vulnerable images (Exam 5 · Q83).
- The Status Dashboard reports outages, not CVEs; forums aren't authoritative (Exam 4 · Q46).

---

## 10. Compliance regimes and shared responsibility

### Key facts
- Google's certifications (ISO 27001, SOC 2, PCI DSS, HIPAA support) cover the **platform**. You're still responsible for configuring your workload compliantly. There's no "GDPR switch" (Exam 1 · Q56).
- **PCI DSS**: GKE and Google Cloud provide the controls to build a compliant environment; nothing is compliant automatically, and GKE isn't excluded (Exam 1 · Q44).
- **HIPAA**: sign a **Business Associate Agreement (BAA)** with Google and use only services covered by it, checking against the compliance page (Exam 4 · Q17), (Exam 2 · Q18).
- **GDPR**: design the security architecture for it (encryption, residency, least privilege, logging, deletion) (Exam 1 · Q56), (Exam 2 · Q44).
- **Compliance Reports Manager** (in the console) is where you download Google's official ISO, SOC and PCI reports and attestations (Exam 5 · Q84).
- Cost and compliance together: interruptible (**Spot**, formerly preemptible) VMs for non-urgent batch, and stop using non-HIPAA services (Exam 2 · Q18).

### Decision rules
- Privacy audit for a healthcare company → **check services against the compliance list + sign a BAA** (Exam 4 · Q17).
- "Meet GDPR" → **design the architecture for it** (Exam 1 · Q56).
- Need Google's ISO 27001 evidence → **Compliance Reports Manager** (Exam 5 · Q84).
- PCI on GKE → **possible, with the right configuration** (Exam 1 · Q44).

### Traps
- "Using only native services gives pass-on compliance" and "enable the GDPR setting" are both false (Exam 1 · Q56).
- "All of Google Cloud is PCI compliant" and "only App Engine is certified" are both wrong (Exam 1 · Q44).
- Firebase Auth, Prometheus or private clusters are fine practices but don't answer a privacy compliance audit (Exam 4 · Q17).
- Cloud Audit Logs record your activity; they aren't ISO reports. Downloads from the internet aren't official (Exam 5 · Q84).

---

## 11. Audit logging, monitoring and retention

### Key facts
- **Cloud Audit Logs**: **Admin Activity** (always on, free, 400 days), **Data Access** (off by default except BigQuery), **System Event**, **Policy Denied**. Creating a network or a VM is Admin Activity.
- Find who created a resource → **Logs Explorer**, filter the resource type (e.g. `gce_network`) and the method (`compute.networks.insert` for a network) (Exam 3 · Q42).
- **GKE audit logging** sends Kubernetes API server audit logs (deployments, config changes, `kubectl exec`, Secret reads) into Cloud Logging alongside Cloud Audit Logs (Exam 5 · Q34).
- **Log sinks** route logs to Cloud Storage (cheap long-term retention), BigQuery (SQL analysis), Pub/Sub (real-time processing) or another log bucket.
- Long retention → sink to **Cloud Storage** (Exam 3 · Q54). For cost, add a lifecycle rule to Coldline and lock the retention period (Exam 3 · Q57).
- Metrics retention in Cloud Monitoring is limited (24 months), so for 5 years export them to Cloud Storage (Exam 1 · Q24).
- Audit analysis → sink to **BigQuery** with views/dataset access for the auditors (Exam 1 · Q26).
- Real-time response to security events → sink to **Pub/Sub** triggering a function (Exam 3 · Q6).
- **Bucket Lock** (locked retention policy): objects can't be deleted or overwritten until the period ends, by anyone, and the lock can't be undone (Exam 2 · Q58), (Exam 5 · Q52). Add **Object Versioning** to recover overwritten or deleted objects quickly (Exam 5 · Q67).

### Destination by need

| Need | Sink to | Source |
|---|---|---|
| Keep for years, cheaply | Cloud Storage (+ lifecycle, + Bucket Lock) | (Exam 3 · Q54), (Exam 3 · Q57), (Exam 1 · Q24) |
| Query/analyze, auditor access | BigQuery | (Exam 1 · Q26), (Exam 4 · Q58) |
| React within seconds | Pub/Sub → function | (Exam 3 · Q6) |

### Decision rules
- "Who created X and when" → **Admin Activity audit logs in Logs Explorer** (Exam 3 · Q42).
- Full audit trail of GKE admin actions from day one → **GKE audit logging + Cloud Audit Logs** (Exam 5 · Q34).
- WORM for N years → **retention policy + lock** (Exam 2 · Q58), (Exam 5 · Q52). Plus fast recovery → **+ Object Versioning** (Exam 5 · Q67).
- 30 days queryable, 2 years retained, 1 TB/day → **sink to Cloud Storage, lifecycle to Coldline, locked retention** (Exam 3 · Q57).

### Traps
- Monitoring alerts and the console Activity page aren't the audit trail; network creation isn't a Data Access entry (Exam 3 · Q42).
- Binary Authorization, a logging DaemonSet (container stdout) and SCC don't record who did what to the API (Exam 5 · Q34).
- Default retention doesn't reach 5 years; granting access doesn't extend retention (Exam 1 · Q24).
- Alerts don't produce an audit record; Cloud SQL via functions or a plain bucket is slower to analyze than BigQuery (Exam 1 · Q26).
- Cron jobs polling logs, or scheduled BigQuery queries, are slow to react (Exam 3 · Q6).
- Dashboards and Pub/Sub don't store logs; firewall logging is a different log (Exam 3 · Q54).
- BigQuery with 30-day partition expiration deletes data needed for two years; cron uploads skip the agent (Exam 3 · Q57).
- CMEK rotation, IAM roles and ACL modes don't prevent deletion. The `storage.retentionPolicySeconds` org constraint sets *allowed* retention values; it doesn't apply or lock a policy on a bucket (Exam 2 · Q58), (Exam 5 · Q52).
- Lifecycle rules delete or move objects; they don't protect them. Replication copies deletions too (Exam 5 · Q67).

---

## ⚠️ Questionable answers

| Item | Issue |
|---|---|
| **(Exam 1 · Q9)** | A VM may fail to reach BigQuery because of missing IAM roles *or* missing access scopes. The key ("new service account with BigQuery access") is defensible, but option B (enable the BigQuery scope) is often argued. Best practice is a dedicated SA with least-privilege roles and the `cloud-platform` scope, not a downloaded key. |
| **(Exam 1 · Q46)** | The original explanation said IAM has no deny policies. IAM deny policies exist and override allows. The answer (union of allow policies) is unchanged. |
| **(Exam 2 · Q18)** | Options A and B differ only in "disable and then discontinue". Learn the substance: Spot VMs for non-urgent batch, HIPAA-covered services only. |
| **(Exam 3 · Q22)** | BigQuery CMEK accepts imported Cloud KMS keys, so the cleanest design is "import the key, set it as the dataset's CMEK". That isn't offered; C is the best of the four. The original explanation wrongly said BigQuery can't use imported keys. |
| **(Exam 3 · Q42)** | Option C names `compute.instances.insert` (VM creation), but the question asks who created the network (`compute.networks.insert`). The method in C is still the right one. |
| **(Exam 4 · Q11)** | Legacy case study. Deterministic encryption explains duplicate detection; choosing Firestore in Datastore mode over Cloud SQL is weakly argued. |
| **(Exam 4 · Q38)** | Firebase Admin is broader than needed; it's "most restrictive" only among the options. |
| **(Exam 4 · Q58)** | The options barely address PII deletion. BigQuery wins because it holds logs cheaply, expires partitions and feeds Data Studio (called Looker Studio from 2022 to 2026) reports. |

---

## Last-minute cheat sheet

- Keep AD → **GCDS + SAML SSO**; strict password rules → **federate, don't sync passwords** (Exam 2 · Q5), (Exam 1 · Q10).
- No grants outside your domain → **domain restricted sharing org policy** (Exam 3 · Q58).
- One org, **folders per department/environment**, **groups** get roles on folders (Exam 1 · Q35), (Exam 3 · Q18), (Exam 3 · Q52).
- Effective allow policy = **union** with ancestors; remove a too-broad grant **where it was made** (Exam 1 · Q46), (Exam 3 · Q8).
- Security/audit team visibility → **Org Viewer + Project Viewer** (Exam 3 · Q41).
- One project per environment (Exam 4 · Q28). Network team vs app team → **Shared VPC host + service project** (Exam 3 · Q4).
- BigQuery: **jobUser on billing project, dataViewer on data** (Exam 1 · Q54); PII split → **authorized views in a separate dataset** (Exam 3 · Q60).
- Workloads: **attached SA** on VMs, **Workload Identity** on GKE, **invoker + ID token** between functions (Exam 2 · Q13), (Exam 4 · Q42), (Exam 4 · Q44).
- Temporary access → **IAM Condition with expiry** (Exam 5 · Q68). No Google account → **signed URL** (Exam 1 · Q55).
- Public IPs only on approved VMs → **`vmExternalIpAccess`**; regions → **resource location restriction** (Exam 2 · Q47), (Exam 5 · Q25).
- Prod ingress rules teams can't override → **hierarchical firewall policy on prod folders** (Exam 5 · Q35).
- DDoS / CDN allow list → **Cloud Armor** (Exam 5 · Q10), (Exam 4 · Q12). GKE → **private cluster, private endpoint** (Exam 4 · Q23).
- Exfiltration → **VPC-SC (+ PGA for on-prem)**; office-only → **access level** (Exam 5 · Q50), (Exam 2 · Q49).
- Vertex AI perimeter → **aiplatform + notebooks** APIs (Exam 5 · Q53).
- SSH with no public IP → **IAP TCP forwarding**; replace VPN for web apps → **IAP** (Exam 3 · Q7), (Exam 4 · Q57).
- Key control → **CMEK**; HSM-only keys → **Cloud HSM**; external keys → **import**; gsutil CSEK → **.boto** (Exam 5 · Q6), (Exam 5 · Q70), (Exam 3 · Q22), (Exam 2 · Q2).
- Credentials → **Secret Manager**; authenticity → **digital signatures** (Exam 1 · Q27), (Exam 3 · Q51).
- PII out → **DLP API de-identification**; PCI scope → **tokenization**; erasure → **delete rows by ID** (Exam 3 · Q55), (Exam 1 · Q14), (Exam 2 · Q44).
- Protect PII during training → **Confidential GKE Nodes** (Exam 5 · Q27).
- Supply chain → **Artifact Analysis, Binary Authorization, scanning in CI** (Exam 5 · Q44), (Exam 3 · Q19), (Exam 5 · Q83).
- HIPAA → **BAA + covered services**; ISO reports → **Compliance Reports Manager** (Exam 4 · Q17), (Exam 5 · Q84).
- Who did it → **Admin Activity logs**; GKE → **GKE audit logging** (Exam 3 · Q42), (Exam 5 · Q34).
- Long retention → **sink to Cloud Storage + Bucket Lock**; analysis → **BigQuery**; real time → **Pub/Sub** (Exam 3 · Q57), (Exam 1 · Q26), (Exam 3 · Q6).
- Can't delete for N years + quick recovery → **locked retention + versioning** (Exam 5 · Q67).
