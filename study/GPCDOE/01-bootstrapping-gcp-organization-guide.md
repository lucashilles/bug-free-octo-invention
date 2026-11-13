# Domain 1 Study Guide — Bootstrapping and Maintaining a Google Cloud Organization

> Condensed from the 50-question bank in [`01-bootstrapping-gcp-organization.md`](01-bootstrapping-gcp-organization.md). Citations like (E2 · Q8) mean Exam 2, Question 8.

## Contents

1. [Resource hierarchy, folders & cost grouping](#1-resource-hierarchy-folders--cost-grouping)
2. [Organization policies](#2-organization-policies)
3. [IAM, service accounts & workload identity](#3-iam-service-accounts--workload-identity)
4. [Audit logs & centralized logging access](#4-audit-logs--centralized-logging-access)
5. [Multi-project monitoring (metrics scopes)](#5-multi-project-monitoring-metrics-scopes)
6. [Infrastructure as Code with Terraform](#6-infrastructure-as-code-with-terraform)
7. [Kubernetes-native config: Config Connector, Config Sync, Policy Controller](#7-kubernetes-native-config-config-connector-config-sync-policy-controller)
8. [CI/CD tooling & artifact storage](#8-cicd-tooling--artifact-storage)
9. [Environments & GKE multi-tenancy](#9-environments--gke-multi-tenancy)
10. [Networking between departments](#10-networking-between-departments)
11. [Developer environments: Cloud Workstations](#11-developer-environments-cloud-workstations)
12. [Capacity, quotas, secrets & encryption](#12-capacity-quotas-secrets--encryption)
13. [SRE incident readiness](#13-sre-incident-readiness)
14. [⚠️ Questionable answers](#️-questionable-answers)
15. [Last-minute cheat sheet](#last-minute-cheat-sheet)

---

## 1. Resource hierarchy, folders & cost grouping

**Key facts**
- Folders are the attachment point for IAM and Organization Policy inheritance and a natural boundary for billing/cost aggregation (E3 · Q37).
- Google's landing-zone guidance cautions against mirroring the org chart; prefer **environment-based** (or sensitivity-based) folders when the pain is policy consistency per environment (E3 · Q37).
- **Labels** help filter billing exports but are **not** an IAM/Org Policy attachment point (E3 · Q37).
- A Cloud Billing **budget can be scoped to a folder** and sums spend of every nested project (E3 · Q43).

**Decision rules**
- "Apply security policy consistently to all prod projects" + "track prod vs dev cost" → one **Production** folder + one **Development** folder (E3 · Q37).
- "Visibility into total department spend, alert if department exceeds budget" → department folder + **one budget scoped to the folder** at the full budget (E3 · Q43).
- Only pick per-project budgets when the question asks *which project* overspent (E3 · Q43).

**Traps**
- "20 business units" in the stem tempts BU folders — but the stated problems are environment problems (E3 · Q37).
- Full budget on *each* project → nothing fires until one project alone eats the whole budget; budget ÷ N projects → false/missed alarms (E3 · Q43).
- A "common services project" per BU centralizes shared infra; it is not a policy or cost boundary (E3 · Q37).

| Mechanism | Policy/IAM inheritance? | Cost aggregation? | Use for |
|---|---|---|---|
| Folder | Yes | Yes (folder-scoped budgets/reports) | Environment or department grouping |
| Label | No | Filter in billing export only | Tagging/breakdowns |
| Common-services project | No | No | Shared VPC host, logging, security tooling |

---

## 2. Organization policies

**Key facts**
- Org policies inherit org → folder → project; a lower level can override the parent (E2 · Q8).
- `iam.disableServiceAccountKeyCreation` blocks creating user-managed SA keys; `iam.disableServiceAccountKeyUpload` blocks uploading an externally generated public key — a different action (E4 · Q22). A newer managed variant `iam.managed.disableServiceAccountKeyCreation` exists (E2 · Q8).
- There is no downloadable "default key": Google-managed keys can't be downloaded; only user-managed keys can be created/exported (E2 · Q8, E5 · Q47).
- `gcp.resourceLocations` restricts where resources are created; Secret Manager **automatic replication requires `global`**, so under a US/EU-only policy use **user-managed replication** with every replica in an allowed region (E3 · Q9).
- `compute.restrictXpnProjectLienRemoval` makes lien removal on a Shared VPC host project require `resourcemanager.projects.updateLiens` **at the organization level** (E4 · Q7).

**Decision rules**
- Eliminate JSON key risk org-wide with minimal overhead → enforce `constraints/iam.disableServiceAccountKeyCreation` at the **org** (E4 · Q22).
- A key is unavoidable for a 3rd-party app → override the constraint **on that project only**, then create the key (E2 · Q8, E5 · Q47). Even narrower: tag-based exemption of specific service accounts (E2 · Q8).
- Regulatory "resources only in region X" across the org → org policy with allowed regions in an `in: allowed_values` list (E5 · Q63).
- Org policy blocks a create → first change the *resource configuration* to comply, don't relax the policy (E3 · Q9).
- Teams self-manage project IAM, need lien removal restricted to org level → `compute.restrictXpnProjectLienRemoval` (E4 · Q7).

**Traps**
- Removing the policy at org/folder "fixes the error" but drops the guardrail for everyone (E2 · Q8).
- Custom roles stripping `iam.serviceAccountKeys.*` or restricting `serviceAccountKeyAdmin` to admins only *reduce/concentrate* risk — they don't eliminate it (E4 · Q22).
- Detect-and-delete approaches (log-based alerts, hourly Asset Inventory scans) are reactive, not preventive (E5 · Q63).
- Revoking `updateLiens` at project level doesn't help when teams can re-grant it to themselves; VPC-SC has nothing to do with liens (E4 · Q7).
- Allowing `global` makes secret creation succeed but doesn't keep replicas in-region (E3 · Q9).

| Constraint | Blocks | Typical stem |
|---|---|---|
| `iam.disableServiceAccountKeyCreation` | Creating new SA keys | "Remove JSON key risk" |
| `iam.disableServiceAccountKeyUpload` | Uploading external public keys | Distractor for the above |
| `gcp.resourceLocations` | Resources in non-allowed locations | Data residency / "error … in [global]" |
| `compute.restrictXpnProjectLienRemoval` | Lien removal on Shared VPC host w/o org-level permission | Protect Shared VPC host from deletion |

---

## 3. IAM, service accounts & workload identity

**Key facts**
- Workload Identity Federation for GKE gives each workload (Kubernetes ServiceAccount) its own identity with short-lived credentials — no keys (E2 · Q20, E4 · Q3).
- Impersonation setup: Google SA + KSA, grant KSA `roles/iam.workloadIdentityUser` on the GSA, annotate KSA with `iam.gke.io/gcp-service-account`, run Pods as the KSA (E4 · Q3). Current guidance generally prefers direct IAM grants to federated principals where supported, but if the stem says "impersonation", use this (E4 · Q3).
- Node service accounts are shared by every Pod on the node → violates least privilege (E2 · Q20, E4 · Q3).
- Kubernetes Secrets are only base64-encoded; mounting a key in a Secret still distributes a long-lived credential (E2 · Q20, E4 · Q3).
- For a CI tool on a Compute Engine VM (Jenkins + Terraform), attach a service account with the needed IAM permissions to the VM (E5 · Q33).
- Time-boxed access → **group** + IAM binding with an **IAM Condition** (date/time expression); access ends automatically (E5 · Q62).
- Grant roles to **groups**, not individuals (E4 · Q56, E5 · Q62).
- **Change risk recommendations** (Recommender/Active Assist) surface risk of an IAM policy change *before* applying it (E3 · Q44).

**Decision rules**
- Terraform pipeline in ephemeral GKE Pods → (C) create GSA with needed roles + (A) KSA via Workload Identity Federation (E2 · Q20).
- "Avoid long-lived credentials, per-workload permissions, multi-tenant GKE" → Workload Identity (E4 · Q3).
- "Access only during September" → group + IAM Condition (E5 · Q62).
- "Assess risk of this IAM change before production" → change risk recommendations (E3 · Q44).
- "Restrict a team to its namespace" → Kubernetes **RBAC**, not IAP (E2 · Q47).

**Traps**
- Node SA option looks attractive as the "keyless" choice — but it's shared identity (E2 · Q20). Only defensible if the cluster is dedicated to the one pipeline.
- JSON key in the CI tool's secret store is still a long-lived key (E2 · Q20).
- "Recent change recommendations" = after-the-fact; deprecation/breaking-changes recommender = different risk; Project Owner = no assessment at all (E3 · Q44).
- Firewall rules control traffic, not IAM access; manual role removal or Cloud Scheduler revocation per user is more fragile than conditions (E5 · Q62).

| Need | Pick | Not |
|---|---|---|
| Pod → Google APIs | Workload Identity Federation for GKE | Node SA, JSON key in Secret |
| VM workload → Google APIs | Attached service account | `GOOGLE_CREDENTIALS` key, `gcloud auth application-default login` |
| Temporary human access | Group + IAM Condition | Custom role removed manually |
| Namespace-level access in GKE | Kubernetes RBAC | IAP (HTTP(S) apps only) |

---

## 4. Audit logs & centralized logging access

**Key facts**
- Data Access audit log config inherits downward; a child **cannot disable** a log type a parent enabled — it can only add (E4 · Q5).
- The supported way to narrow an enabled config is **exempted principals** (by identity, not by resource branch) (E4 · Q5).
- Org-level enablement automatically covers future projects; per-project enablement doesn't (E4 · Q5).
- **Log views** slice a single log bucket into IAM-grantable subsets with no data duplication; `_AllLogs` gives full visibility. `_Default` view exists only on the `_Default` bucket and isn't project-scoped (E4 · Q46).
- Data Access audit logs require `roles/logging.privateLogViewer`; `roles/logging.viewer` can't see them (E4 · Q56).

**Decision rules**
- Company-wide Data Access logging except one folder → enable at **org**, add that folder's principals to **exempted principals** (E4 · Q5).
- Central log project, each team sees only its logs, ops sees all, low cost → per-team **log views** + ops on `_AllLogs` (E4 · Q46).
- Security team needs read-only Data Access logs → `privateLogViewer` granted to a **group** (E4 · Q56).

**Traps**
- "Enable everywhere except the folder" (per-resource) is the literal reading but doesn't scale and isn't how exclusion works (E4 · Q5).
- BigQuery export per team duplicates storage; Logs Writer is the wrong direction of permission (E4 · Q46).
- `logging.viewer` "sounds enough" — it isn't for Data Access logs (E4 · Q56).

---

## 5. Multi-project monitoring (metrics scopes)

**Key facts**
- A **scoping project** hosts a **metrics scope** listing monitored projects; it also stores alert policies, dashboards, uptime checks. Metric data stays in the source project (E1 · Q31, E1 · Q57).
- Monitoring Viewer on the scoping project is enough to view all monitored projects' data — no role on workload projects needed (E1 · Q31).
- Google recommends a **new or resource-free** project as the scoping project (E1 · Q31, E1 · Q57).
- Ordinary folders don't auto-populate scope membership (app-enabled folders are a separate mechanism) (E1 · Q57).
- Metrics scopes are what Workspaces became (E1 · Q31).

**Decision rules**
- Prod-only alerting, least privilege → new monitoring project, add only prod projects, grant read on the scope (E1 · Q31).
- Per-environment dashboards → **one dedicated scoping project per environment**, each containing that environment's projects (E1 · Q57).

**Traps**
- Hosting the scope in an existing prod workload project "works" but isn't recommended (E1 · Q31 option C, E1 · Q57 options C/D).
- Per-project scopes fragment the view; Project Viewer is too broad (E1 · Q31).
- One scope with all environments + filters works but isn't the best match (E1 · Q57).

---

## 6. Infrastructure as Code with Terraform

**Key facts**
- Terraform code belongs in a **VCS (Git)** with branches, reviews, merge to main; object versioning, network shares and Drive are not VCS (E1 · Q4, E5 · Q8).
- Peer review + tests (`terraform validate`/`plan`) before merge prevent conflicts; "daily merges" don't (E5 · Q8).
- New stack on every apply = Terraform can't see shared state → use a **remote `gcs` backend** (with locking) (E2 · Q17, E5 · Q45).
- State in source control: no locking, plaintext secrets, documented anti-pattern (E2 · Q17).
- **Cloud Foundation Toolkit** provides Google-maintained Terraform modules for project + foundational resource provisioning (E4 · Q18, E5 · Q40).
- Repo layout: Terraform **one shared repo, directories per env**; Kustomize/Config Sync **one shared repo, overlays per env**; app code **one repo per app, feature branches** (E4 · Q26).

**Decision rules**
- "Version and share IaC with a growing team" → Git + PR/merge workflow (E1 · Q4, E5 · Q8).
- "Duplicate stacks / exactly one stack" → gcs backend (E2 · Q17, E5 · Q45).
- "Fast, reliable, repeatable project provisioning" → CFT modules (E4 · Q18, E5 · Q40).

**Traps**
- Cloud Storage object versioning ≠ code versioning (E1 · Q4).
- Cleanup pipeline treats the symptom; destroy-then-apply causes downtime (E2 · Q17).
- Custom Terraform module from scratch is declarative but slower/riskier than CFT; gcloud scripts are imperative (no state/drift detection) (E4 · Q18).
- Double-encoding environment (repo per env *and* branch per env) breaks single source of truth; separate repos+branches fight Kustomize's base/overlay design (E4 · Q26).

| Storage for… | Right tool | Wrong tool |
|---|---|---|
| `.tf` source | Git + PRs | GCS versioned bucket, Drive, network share |
| `terraform.tfstate` | GCS backend (remote, locked) | Git repo, local disk |

---

## 7. Kubernetes-native config: Config Connector, Config Sync, Policy Controller

**Key facts**
- **Config Connector**: Kubernetes CRDs that represent **Google Cloud resources**; it's a controller with a continuous reconciliation loop (corrects drift); Google-supported (E4 · Q10, E4 · Q27, E5 · Q38).
- **Crossplane**: CRD-based too, but community project → no Google Cloud Support path (E4 · Q10).
- **Config Sync**: continuously syncs/reconciles cluster objects from Git (installs things and keeps them matching) (E2 · Q18, E5 · Q24).
- **Policy Controller** (Gatekeeper-based): admission control + audit of constraints — decides what is *allowed*, doesn't install resources (E2 · Q18, E4 · Q33).
- **Anthos Config Management** = Config Sync + Policy Controller; constraint templates/parameters in Git → synced and enforced across clusters (E4 · Q33, E5 · Q37).
- Pods and Jobs run once; Cloud Build runs on triggers — neither is a reconciler (E4 · Q27).

**Decision rules**
- "CRDs" + "Google Cloud Support" → Config Connector (E4 · Q10).
- "GitOps devs create cloud resources" + "reconcile periodically / prevent drift" → Config Connector (E4 · Q27, E5 · Q38).
- "Git is source of truth, install & keep network policies + DaemonSet consistent across clusters" → Config Sync (E2 · Q18, E5 · Q24).
- "Constraint templates + parameters in GitHub, auto-applied" → ACM (Policy Controller + Config Sync) (E4 · Q33, E5 · Q37).
- "Prevent Pods that violate a security standard" → Policy Controller (E2 · Q18 trap note).

**Traps**
- "Enforce" ≠ Policy Controller automatically — enforcing *existence* is Config Sync (E2 · Q18).
- Config Connector synced to Git still only manages GCP resources, not policy constraints (E4 · Q33).
- Monitoring alerts + Cloud Run functions remediation = custom plumbing duplicating Config Sync (E2 · Q18).
- Anthos Service Mesh is traffic/mTLS, irrelevant to policy sync (E4 · Q33).

| Tool | Manages | Source | Reconciles? |
|---|---|---|---|
| Config Connector | Google Cloud resources (as CRDs) | K8s manifests (often via GitOps) | Yes (controller loop) |
| Config Sync | Any K8s objects in cluster | Git repo | Yes |
| Policy Controller | Constraints (allow/deny + audit) | Constraint templates | Admission + audit |
| Crossplane | Cloud resources (CRDs) | K8s | Yes, but no Google support |
| Terraform via Cloud Build | Cloud resources | `.tf` | No — per trigger |

---

## 8. CI/CD tooling & artifact storage

**Key facts**
- Helm 3 (3.8+) charts can be stored as **OCI artifacts** in Artifact Registry (Docker-format repos); IAM-governed and VPC-SC-supported (E2 · Q1).
- **Packer** builds VM images for multiple clouds from one config; **Cloud Deploy** promotes releases to GKE/Cloud Run/attached clusters; **kpt** manages Kubernetes config packages (E2 · Q14).
- Cloud Build **default pool** runs outside your VPC; **private pools** are managed, peered into your VPC, reach private resources without public exposure (E4 · Q16).

**Decision rules**
- Public + private Helm charts, native access control, VPC-SC → Artifact Registry OCI (E2 · Q1).
- Multi-cloud VM image pipeline → Cloud Build + Packer (E2 · Q14).
- CI build must hit private VPC APIs, no public exposure, low overhead → Cloud Build private pools (E4 · Q16).

**Traps**
- GitHub Enterprise / self-hosted chart server on GKE / GCS bucket repo → not native IAM + VPC-SC (E2 · Q1).
- Cloud Build + Cloud Deploy is the "standard pairing" but builds no VM images (E2 · Q14).
- External LB + Cloud Armor is still public; internal LB doesn't give default-pool workers a path into the VPC; Spinnaker adds overhead (E4 · Q16).

| Need | Tool |
|---|---|
| VM images across clouds | Packer |
| Container release promotion (GKE/Cloud Run) | Cloud Deploy |
| K8s config packages | kpt |
| Helm charts + images, IAM + VPC-SC | Artifact Registry (OCI) |
| Builds reaching private VPC | Cloud Build private pool |

---

## 9. Environments & GKE multi-tenancy

**Key facts**
- Separate **dev** (write/break code), **test/staging** (config changes, experiments, load tests in a production-like env) and **prod** (validated changes only); commonly separate projects under env folders (E1 · Q32, E5 · Q5).
- GKE charges a per-cluster management fee → cluster count drives cost (E2 · Q47).
- Recommended layout: **cluster per environment**, **namespace per application**; namespaces scope policy, RBAC + network policies enforce it (E3 · Q4).
- Release channels: **Stable** = most mature; **Regular** = default balance; **Rapid** = earliest; **Extended** = longer minor-version support, not "extra stable" (E3 · Q52).

**Decision rules**
- Dev/experiments/load tests hurting prod → separate dev env + separate test env (E1 · Q32, E5 · Q5).
- Many teams, dev + prod, minimum cost, team isolation → one shared dev cluster + one shared prod cluster, namespace per team, **RBAC** (E2 · Q47).
- Sensitive data, several apps, low admin overhead → cluster per env, namespace per app (E3 · Q4).
- "Prioritize stability" for staging + prod → **Stable for both**; "balance freshness & stability" → Regular for both (E3 · Q52).

**Traps**
- A single scaled-down dev env shared with testers gives unrepresentative load results (E1 · Q32).
- Freezing prod to one release a year concentrates risk (E1 · Q32).
- Cluster per app/team multiplies fees and overhead (E2 · Q47, E3 · Q4).
- Staging doesn't have to be on a faster channel than prod (E3 · Q52).

---

## 10. Networking between departments

- Many departments, many apps, minimal management, flexibility → **VPC per department + VPC Network Peering** (E2 · Q56).
- **Private Service Connect** exposes one published service at a time — not general VPC-to-VPC connectivity (E2 · Q56).
- **Cloud VPN** encrypts over the public internet, suited to hybrid links, not linking Google Cloud VPCs (E2 · Q56).
- VPC per application = unmanageable at the stated scale (E2 · Q56).
- See ⚠️ section — this answer is option-relative.

---

## 11. Developer environments: Cloud Workstations

**Key facts**
- Workstation **configurations** are templates (image, IDE, machine type, storage) shared with a team; changes apply on next start (E1 · Q58).
- Patching: updated base images, rebuild custom images, `runningTimeout` forces refresh; custom dependencies remain your responsibility (E1 · Q58).
- `idleTimeout` = stop after inactivity (cost); `runningTimeout` = stop after fixed runtime even if active (E3 · Q7).
- Private Workstations cluster keeps environments off public networks (E3 · Q7).
- Code OSS **preview link** gives authenticated browser access to an app on a workstation port — no public IP, bastion, or IAP tunnel to the underlying VM (E3 · Q10).
- Workstations support attached GPUs; grant developers **Cloud Workstations User**. Cloud Shell can't get GPUs (Google-owned VM) (E3 · Q27).

**Decision rules**
- Standardized team env + IDEs + ongoing patching → Cloud Workstations config per team (E1 · Q58, E5 · Q57).
- Same IDE, private, MOST cost-effective → private cluster + `idleTimeout` (E3 · Q7).
- View web app running in workstation → preview link (E3 · Q10).
- Managed Java IDE + GPUs → GPU workstation per developer (E3 · Q27).

**Traps**
- Golden-VM snapshots, checklists/scripts, laptop images → no managed refresh (E1 · Q58).
- Scheduled VM shutdowns ignore developer activity (E3 · Q7).
- Per-dev projects with Editor role = broad permissions + DIY IDE (E3 · Q27).

---

## 12. Capacity, quotas, secrets & encryption

- Quotas are enforced **per project per region** → multi-region capacity planning = verify quota in **each** target region (E1 · Q17).
- Machine-type choice is sizing, not capacity planning; Cloud Trace is latency debugging (E1 · Q17).
- Cloud Run: a **scaling target** (CPU %, concurrency) says *when* to scale; **resource limits / max instances + quotas** say *how far* — verify quotas support the range (E3 · Q58). Request-based scaling uses **concurrent requests**, and Cloud Run CPU targets *are* customizable (E3 · Q58).
- Sensitive data with bounded exposure on breach → keys in **Cloud KMS**, rotated frequently (E2 · Q60). SSO is user auth; per-instance build-time secrets spread secrets into artifacts (E2 · Q60).

---

## 13. SRE incident readiness

- Reduce customer disruption → **current playbooks** + **automation** that analyzes impact and suggests mitigations to on-call (E3 · Q55).
- Everyone modifying prod during incidents = uncoordinated; exclusive unrestricted on-call permissions ≠ least privilege; alerts on internal behavior alone aren't necessarily actionable/symptom-based (E3 · Q55).

---

## ⚠️ Questionable answers

| Q | Issue |
|---|---|
| (E5 · Q33) | Answer (attach SA to Jenkins VM) is fine, but the explanation is wrong in places: it says "Workload Identity is designed for VM-to-Google Cloud communication" (VMs use the attached SA via the metadata server; Workload Identity is a GKE/federation feature), and claims `gcloud auth application-default login` needs "manual key rotation" (it's an interactive *user* credential flow — the real problem is using a human's credentials in automation). Also note the tension with (E2 · Q20): a shared node SA is rejected there because many Pods share it; a dedicated Jenkins VM doesn't have that problem. |
| (E2 · Q60) | KMS key rotation creates a new primary version for **new** encryptions; old versions stay enabled to decrypt existing data, so rotation alone doesn't shrink what a compromised old version exposes unless data is re-encrypted. Treat as "best of the options"; the reasoning overstates rotation. |
| (E2 · Q56) | VPC Peering is non-transitive and has per-network peering limits, so a mesh across "a large number of departments" is not low-maintenance in practice; Google landing-zone guidance commonly points to Shared VPC or hub-and-spoke (e.g., Network Connectivity Center). Correct only relative to the listed options. |
| (E4 · Q5) | Exempted principals are identity-based: those principals become exempt wherever the org-level config applies, not just inside the CustomerService folder. Works only if those principals are used solely by that folder's projects. |
| (E2 · Q18, E5 · Q24) | The "correct" option has Cloud Build *deploy* the resources **and** Config Sync sync them — redundant in pure GitOps (Config Sync applies from Git). E5's explanation reframes Cloud Build as validating/rendering before the repo. Pick it for "Config Sync", not for the Cloud Build deploy step. |
| (E4 · Q26, E4 · Q33, E5 · Q37) | "Anthos Config Management" is legacy branding; the components are now Config Sync and Policy Controller. Concepts still hold. |
| (E1 · Q4) | Cites Cloud Source Repositories as a Git host; CSR is closed to new customers — use GitHub/GitLab/Secure Source Manager. The VCS principle is unaffected. |
| (E4 · Q3) | Explanation itself notes current guidance prefers direct IAM grants to Workload Identity principals over GSA impersonation; the answer is right only because the stem demands impersonation. |

---

## Last-minute cheat sheet

- Policy consistency/cost by environment → **prod & dev folders**, not BU folders or labels.
- Department total budget → **folder + one folder-scoped budget**.
- Kill JSON key risk org-wide → **`iam.disableServiceAccountKeyCreation` at org** (not `…KeyUpload`).
- Key truly required → **override constraint on that project only**; no "default key" exists.
- Data residency → **`gcp.resourceLocations` / `in: allowed_values`**; secrets → **user-managed replication** in allowed regions.
- Shared VPC host lien protection → **`compute.restrictXpnProjectLienRemoval`**.
- Pods → Google APIs → **Workload Identity Federation for GKE** (GSA + KSA + `workloadIdentityUser` + annotation).
- Never: JSON key in K8s Secret, node SA shared by all Pods.
- Temporary access → **group + IAM Condition (date/time)**.
- Pre-change IAM risk → **change risk recommendations**.
- Namespace isolation → **RBAC**; IAP is for HTTP(S) apps.
- Exclude a folder from org-level Data Access logs → **exempted principals**; children can't disable.
- Data Access logs → **`logging.privateLogViewer` to a group**.
- Per-team view of central logs → **log views**; ops → `_AllLogs`.
- Multi-project monitoring → **dedicated resource-free scoping project** per boundary; Monitoring Viewer there.
- Terraform code → **Git + PRs**; state → **GCS backend**; duplicate stacks = missing remote state.
- New projects fast & repeatable → **Cloud Foundation Toolkit modules**.
- Repos: infra shared w/ env dirs/overlays; apps repo-per-app w/ feature branches.
- CRDs + Google support / periodic drift correction for cloud resources → **Config Connector**.
- Install & keep K8s objects matching Git → **Config Sync**; what's allowed → **Policy Controller**.
- Helm charts + VPC-SC → **Artifact Registry (OCI)**; multi-cloud VM images → **Packer**.
- CI needs private VPC → **Cloud Build private pools**.
- GKE: cluster per env, namespace per app/team; stability → **Stable** for staging & prod.
- Dev envs → **Cloud Workstations**; cost → `idleTimeout`; view app → preview link; GPUs → workstation, not Cloud Shell.
- Multi-region capacity → **check quota in every region**; Cloud Run → limits + quotas, not just a scaling target.
