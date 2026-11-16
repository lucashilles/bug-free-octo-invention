# Domain 5 Study Guide — Trust and Security with Google Cloud

> Condensed from the 50-question bank in [`05-trust-and-security.md`](05-trust-and-security.md). Citations look like (Exam N · QM). Many scenarios repeat across exams (phishing, Cloud Armor for DDoS, physical security under the shared responsibility model, default encryption), so look for paired citations. Items marked "see ⚠️" have a shaky or vague key, discussed at the end.

---

## 1. Core security concepts: CIA, posture, resilience

### Key facts
- **The CIA triad** is the base vocabulary of this domain:
  - **Confidentiality**: only approved users can access the data.
  - **Integrity**: data stays correct, complete and dependable.
  - **Availability**: data stays **dependable and accessible when needed** (Exam 1 · Q27).
  - Typical controls: confidentiality comes from IAM, authentication, least privilege and encryption. Integrity means data isn't improperly changed, corrupted or deleted. Availability is supported by reducing downtime and planning for business continuity. Accurate data that nobody can reach is **not** available (Exam 1 · Q27).
- **Compliance** is a separate idea: meeting regulatory and industry standards. The exam uses it as a distractor for CIA questions (Exam 1 · Q27).
- **Security posture** is the **complete view** of an organization's cybersecurity readiness: network design, identity and access controls, monitoring coverage, and how consistently policies are applied (Exam 3 · Q8).
- **Cyber resilience** is the ability to **reduce the chance** of attacks, **keep essential services running** during an incident, **limit business impact** and **recover quickly** (Exam 5 · Q7). In short: anticipate, withstand, recover and adapt. It goes beyond prevention because it **assumes some attacks will still succeed** (Exam 5 · Q7).
- Security posture is something you can measure and manage. In Google Cloud, **Security Command Center** is where posture is defined, assessed and monitored (Exam 3 · Q8).
- **Security is a continuous program, not a product.** A new security platform doesn't stop leaks on its own. Long-term improvement comes from **skilled people and an evolving security plan** (Exam 5 · Q4, see ⚠️). A good plan mixes **people, process and technology**: find the root cause, layer controls (**defense in depth**), monitor, train staff and keep improving (Exam 5 · Q4).
- *(not in the question bank)* **Threat** = a potential danger. **Vulnerability** = a weakness that a threat can exploit. **Risk** = the likelihood and impact of a threat exploiting a vulnerability.

### CIA triad compared

| Term | Plain meaning | Typical exam wording | Source |
|---|---|---|---|
| Confidentiality | Only approved people see it | "limiting data access only to approved users" | (Exam 1 · Q27) |
| Integrity | It stays correct | "correct, complete, and dependable" | (Exam 1 · Q27) |
| Availability | It's there when needed | "accessible when needed" | (Exam 1 · Q27) |
| Compliance (not CIA) | Meets rules and standards | "regulatory and industry standards" | (Exam 1 · Q27) |

### Decision rules
- "Complete view of readiness", "overall state of security" → **security posture** (Exam 3 · Q8).
- "Prevent, keep running, limit impact, recover" → **cyber resilience** (Exam 5 · Q7).
- "Long-term", "improve the security approach" → invest in **expertise and process**, not the most expensive tool (Exam 5 · Q4).

### Traps
- **Threat response** is only one part of posture. It is reacting to incidents, not the whole picture (Exam 3 · Q8).
- **Data masking** hides values. It is not resilience (Exam 5 · Q7).
- **Longer data retention** is not a security fix. Keeping data longer means more data can leak. Retention should follow business, legal and privacy needs (Exam 5 · Q4).
- **IaaS** and **vendor lock-in** are not resilience either. IaaS is a service model and lock-in is a portability concern (Exam 5 · Q7).
- Waiting for a "newer platform" or buying "the most expensive platform" is never the answer (Exam 5 · Q4).

---

## 2. Cybersecurity threats

### Key facts
- **Phishing**: a fake message that looks trusted (support team, salary portal) and pushes urgency ("account disabled in 12 hours") to steal **credentials or bank details**, often via a **look-alike login page**. It is a **social engineering** attack (Exam 1 · Q31), (Exam 2 · Q28), (Exam 2 · Q41).
- **Malware**: malicious software that **secretly steals, alters or damages** information without the user noticing (Exam 2 · Q46).
- **Ransomware**: a type of malware that **encrypts your data and demands payment**, usually in cryptocurrency, for the decryption key (Exam 5 · Q17). Some ransomware also **threatens to publish stolen data** (Exam 5 · Q50).
- Attacks chain together. **Phishing** is often the **entry point** that later leads to cryptomining or ransomware. The exam asks you to name what the scenario **describes**, not how the attacker first got in (Exam 1 · Q25), (Exam 5 · Q17).
- **Cryptomining** (cryptojacking): attackers use a compromised account to create **unauthorized VMs** that burn CPU on **hashing to earn cryptocurrency**. The first sign is often an **unexpected bill** (Exam 1 · Q25).
- **Misconfiguration**: a human error such as making a bucket **public**. No software flaw is exploited. It is one of the most common causes of cloud data exposure (Exam 1 · Q26). Reduce it with tight IAM permissions, Cloud Storage **public access prevention** and **uniform bucket-level access**, and regular posture checks in Security Command Center (Exam 1 · Q26).
- **Advanced Persistent Threat (APT)**: a skilled, well-funded attacker who gets in and **stays hidden for a long time** to spy or steal. **Zero-day vulnerability**: a software flaw that is **unknown to the vendor** and has no fix yet. Both are distractors when the stem says the cause was a simple mistake (Exam 1 · Q26).
- **Unsecured third-party systems**: attackers enter through a **vendor's plugin or component** connected to your delivery process (a supply chain attack). Your own controls can be strong and you are still exposed (Exam 3 · Q20).
- **LLM attack (prompt injection)**: crafted prompts make an AI assistant **ignore its instructions**, leak restricted data or bypass response controls (Exam 5 · Q50). Other LLM risks include data leakage through model answers and unsafe tool use by AI agents (Exam 3 · Q20).
- **DDoS**: a flood of traffic, often from a botnet, meant to **exhaust resources** so real users can't reach the service (Exam 3 · Q10), (Exam 4 · Q2). See Lesson 5 for the defense.

### Threats compared

| Clue in the question | Threat | Source |
|---|---|---|
| Fake email or portal asking for a password or bank details | Phishing | (Exam 1 · Q31), (Exam 2 · Q28), (Exam 2 · Q41) |
| Software that secretly steals, alters or damages data | Malware | (Exam 2 · Q46) |
| Files encrypted, payment demanded for the key | Ransomware | (Exam 5 · Q17) |
| Unauthorized VMs, high CPU, rising bill, crypto rewards | Cryptomining | (Exam 1 · Q25) |
| Bucket accidentally public, no exploit used | Misconfiguration | (Exam 1 · Q26) |
| Entry through a vendor plugin or component | Unsecured third-party systems | (Exam 3 · Q20) |
| Prompts that override an AI assistant's instructions | LLM attack (prompt injection) | (Exam 5 · Q50) |
| Huge volume of fake requests to take a site down | DDoS | (Exam 3 · Q10), (Exam 4 · Q2) |

### Decision rules
- Something **asks the user** for credentials or a click → **phishing**. Something **demands payment** to unlock data → **ransomware**.
- **Billing spike + unknown VMs** → **cryptomining**, not DDoS (Exam 1 · Q25).
- "Without exploiting any software flaw" → **misconfiguration**, not zero-day or APT (Exam 1 · Q26).

### Traps
- **Spamming** is unwanted bulk mail. It doesn't try to steal credentials (Exam 2 · Q28).
- **Ransomware** is a kind of malware, but it is loud (it announces itself). "Without the user noticing" points to generic **malware** (Exam 2 · Q46).
- **Zero trust architecture** is a defense model, not a threat vector (Exam 3 · Q20).
- **SQL injection** is a code attack, not social engineering (Exam 2 · Q41). Social engineering exploits **human trust, fear, urgency or curiosity**, not a technical flaw (Exam 2 · Q41).
- **Physical damage** and **hardware failure** are not cyberattacks. Without a ransom note or an attacker, they are operational risks (Exam 3 · Q20), (Exam 5 · Q17).
- **SLA violations** and **incomplete data input** are service and data quality issues, not threats (Exam 2 · Q46).

---

## 3. The shared responsibility model

### Key facts
- In the cloud, **security is shared**. Google is responsible for **security *of* the cloud**. The customer is responsible for **security *in* the cloud**: what they put on it and how they configure it (Exam 4 · Q20).
- Google calls its version **shared responsibility and shared fate**: Google also gives customers secure defaults, tools and guidance to help them do their part (Exam 4 · Q47).
- **Google always owns physical security**: data center buildings, hardware and facilities. This holds for every service model, including IaaS (Exam 1 · Q49), (Exam 4 · Q20), (Exam 6 · Q42).
- In **IaaS (Compute Engine)** Google manages the physical infrastructure, hardware, network foundation and the **virtualization layer**. The customer keeps everything inside the VM: guest **OS patching and hardening**, installed software, application code, encryption of data inside the app, and application-level user access (Exam 1 · Q49), (Exam 4 · Q20).
- Customers **can't install their own physical security hardware** in Google's data centers. Their security work is configuration: IAM, encryption settings, firewall rules, logging (Exam 4 · Q47).
- Testing the **availability of the customer's own applications** is the customer's job, not Google's (Exam 4 · Q18).
- The **customer defines data access policies**: who can see which datasets and reports. That's the customer's IT team, not Google support and not end users (Exam 5 · Q19).
- The more managed the service (IaaS → PaaS → SaaS), the more Google takes on. **Data and access** always stay with the customer.

### Who does what (IaaS)

| Responsibility | Google | Customer | Source |
|---|---|---|---|
| Physical data center security | ✅ | ❌ | (Exam 1 · Q49), (Exam 4 · Q20), (Exam 6 · Q42) |
| Hardware and network infrastructure | ✅ | ❌ | (Exam 6 · Q42) |
| Guest OS patching and hardening | ❌ | ✅ | (Exam 1 · Q49), (Exam 4 · Q20) |
| Application code security | ❌ | ✅ | (Exam 4 · Q20) |
| Application-level user access / data access policies | ❌ | ✅ | (Exam 1 · Q49), (Exam 5 · Q19) |
| Encrypting sensitive data inside the app | ❌ | ✅ | (Exam 1 · Q49) |

### Decision rules
- Physical, buildings, hardware, facilities → **Google Cloud alone**, not "shared" (Exam 6 · Q42).
- "Who decides which employees access what" → **the customer's IT team** (Exam 5 · Q19).

### Traps
- "**Customer and Google**" sounds balanced, but physical security is Google's alone (Exam 6 · Q42).
- **Cloud Identity** is a tool the customer uses. It manages users and groups and supplies the identities that IAM policies refer to. It doesn't decide policy (Exam 5 · Q19).
- **Google Cloud Customer Care** and **external security providers** don't decide your access rules or secure Google's data centers (Exam 5 · Q19), (Exam 6 · Q42).
- Assuming security is "fully Google's responsibility" is always wrong (Exam 6 · Q25).

---

## 4. Identity and access management

### Key facts
- **IAM (Identity and Access Management)** defines **who** can do **what** on **which resource**. It's the answer when someone must view BigQuery datasets but not delete or create them (Exam 1 · Q12).
- **Authentication** = proving **who you are** (sign-in). **Authorization** = deciding **what you may do** after that. Authentication always comes **first**, then IAM checks permissions (Exam 5 · Q24).
- **Auditing** records who did what, when and from where, using **audit logs**. It supports investigations and compliance but doesn't verify identity (Exam 5 · Q24).
- **2-Step Verification (2SV) / multi-factor authentication (MFA)**: a password **plus** a second factor such as a phone prompt, a code (SMS or authenticator app) or a **hardware security key**. A stolen password alone is no longer enough (Exam 3 · Q47).
- **Least privilege**: each person gets **only the permissions their job needs**, nothing more. If an account is compromised, the damage is limited to what it can do. In IAM you apply it with **predefined or custom roles** (Exam 6 · Q22), (Exam 1 · Q12).
- **Map roles to job functions.** When several departments share a project, define roles per function or team instead of per person. It's faster and easier to manage. In practice you put users in **groups** by department and grant roles to the groups, at the project, folder or resource level (Exam 3 · Q7).
- **Service accounts** are identities for **applications and automated workloads**, not shared logins for people (Exam 3 · Q7).
- Roles can be granted on a single resource. For example, a **BigQuery viewer role** lets an analyst read datasets without creating or deleting them (Exam 1 · Q12).
- *(not in the question bank)* **Cloud Identity** manages users and groups and supports single sign-on (SSO). Best practice is to **grant roles to groups**, not to individuals.
- IAM role types: **basic** (Owner, Editor, Viewer: broad, across many services), **predefined** (per service, e.g. BigQuery Data Viewer) and **custom** (Exam 3 · Q7), (Exam 6 · Q49). *(not in the question bank)* Policies are **inherited** down the resource hierarchy (organization → folders → projects → resources).

### Identity terms compared

| Term | Question it answers | Source |
|---|---|---|
| Authentication | "Are you really who you claim to be?" | (Exam 5 · Q24) |
| Authorization | "What are you allowed to do?" | (Exam 5 · Q24) |
| Auditing | "What did you do?" (logs) | (Exam 5 · Q24) |
| 2SV / MFA | "Prove it a second way" | (Exam 3 · Q47) |
| Least privilege | "Only what the job needs" | (Exam 6 · Q22) |

### Decision rules
- "Who can view vs. delete/create" → **IAM** (Exam 1 · Q12).
- "Confirm the person is really the claimed user" → **authentication** (Exam 5 · Q24).
- Password + phone/code/key → **2SV/MFA** (Exam 3 · Q47).
- "Only the permissions needed for the role" → **least privilege**, not zero trust (Exam 6 · Q22).
- Several teams, one project, fastest way → **roles mapped to job functions** (Exam 3 · Q7).

### Traps
- **Basic roles** (Owner/Editor/Viewer) for every employee are too broad (Exam 3 · Q7), (Exam 6 · Q49).
- **One shared service account** for all departments breaks accountability and least privilege (Exam 3 · Q7).
- Setting least-privilege roles **separately for each employee** is correct in spirit but slow. The exam wants the scalable option (Exam 3 · Q7).
- **VPC** controls network traffic, not who can delete a dataset (Exam 1 · Q12). **Cloud Storage** has bucket-level access controls, but it isn't the service for BigQuery permissions (Exam 1 · Q12).
- **Security by default** means products ship with protections already on. It is not about how many permissions a user gets (Exam 6 · Q22).
- **Privileged access** is about elevated admin permissions, not about filtering network traffic (Exam 3 · Q27).
- **Zero trust** and **least privilege** are related. Zero trust is the overall model ("verify every request"). Least privilege is about how much access is granted (Exam 6 · Q22).

---

## 5. Network and application protection

### Key facts
- **Firewall rules** define which **incoming (ingress) and outgoing (egress) traffic** is allowed or denied to your resources in a VPC network. Rules match on things like direction, priority, protocol, ports, IP ranges, network tags and service accounts (Exam 3 · Q27).
- **Google Cloud Armor** protects internet-facing apps from **DDoS** and web attacks. It works at Google's edge with the external load balancer, so malicious traffic is filtered before it reaches the back ends (Exam 3 · Q10), (Exam 4 · Q2). It covers both **volumetric floods** and **Layer 7 HTTP floods**, and its **web application firewall (WAF)** rules block attacks such as **SQL injection** and **cross-site scripting (XSS)** (Exam 3 · Q10), (Exam 2 · Q35).
- **Cloud VPN** connects networks through **encrypted IPsec tunnels**. It protects data in transit between your office and Google Cloud. It doesn't block attack traffic to a public site (Exam 4 · Q2).
- **Model Armor** inspects **AI prompts and responses**. It reduces **prompt injection and jailbreak** risk, catches **sensitive data exposure** and blocks harmful output before it reaches users (Exam 1 · Q33). It is the defense against the LLM attacks in Lesson 2 (Exam 5 · Q50).
- **Zero trust** replaces "trust the corporate network" with **verify every identity, device and request, from any location**. Access decisions use identity, **device posture** and context, and are checked continuously (Exam 5 · Q6). Least privilege is usually part of a zero-trust strategy (Exam 6 · Q22). When an organization moves from project-by-project cloud use to broad transformation, the recommended shift is to a **zero-trust model that verifies users, devices and applications** (Exam 6 · Q49).
- *(not in the question bank)* Google's own zero-trust implementation is **BeyondCorp**. Customers get it through **Identity-Aware Proxy (IAP)** and **Chrome Enterprise Premium** (formerly BeyondCorp Enterprise): access to apps based on identity and context, without a VPN.
- *(not in the question bank)* **VPC Service Controls** draw a perimeter around managed services (BigQuery, Cloud Storage) to reduce data exfiltration.

### Which protection?

| Need | Use | Not | Source |
|---|---|---|---|
| Allow/deny traffic in and out | Firewall rules | 2SV, encryption keys | (Exam 3 · Q27) |
| Stop a DDoS / botnet flood on a website | Google Cloud Armor | SCC, IAP, KMS, Cloud VPN | (Exam 3 · Q10), (Exam 4 · Q2) |
| Filter AI prompts and responses | Model Armor | Cloud Run functions, Autoclass | (Exam 1 · Q33) |
| Verify every request regardless of location | Zero trust architecture | VPN, perimeter security | (Exam 5 · Q6), (Exam 6 · Q49) |

### Decision rules
- DDoS on a public site → **Cloud Armor**, every time (Exam 3 · Q10), (Exam 4 · Q2).
- Generative AI safety (prompt injection, jailbreak, harmful output) → **Model Armor** (Exam 1 · Q33).
- "No longer trust the office network" → **zero trust** (Exam 5 · Q6).
- SQL injection or cross-site scripting against a public web app → **Cloud Armor WAF rules** (Exam 3 · Q10), (Exam 2 · Q35).

### Traps
- **Security Command Center** finds risks and misconfigurations. It doesn't absorb DDoS traffic (Exam 3 · Q10), (Exam 4 · Q2).
- **IAP** controls who can reach an app based on identity. It's not a DDoS shield (Exam 3 · Q10).
- **Cloud KMS** manages encryption keys. It doesn't inspect or block traffic (Exam 3 · Q10).
- **Cloud Run functions** could call a security service, but they don't screen AI prompts themselves. Model Armor is the purpose-built control (Exam 1 · Q33).
- A **VPN** encrypts a network path but still trusts whoever is inside. It is the opposite of zero trust (Exam 5 · Q6).
- "Strong perimeter and trust everything inside" is the old castle-and-moat model (Exam 6 · Q49).

---

## 6. Encryption, backup and incident readiness

### Key facts
- Google Cloud **encrypts customer data by default, at rest and in transit**. No team has to switch it on per service (Exam 5 · Q23), (Exam 5 · Q30). Data at rest is encrypted **before it is written to disk**, using **Google-managed keys** by default (Exam 4 · Q3), (Exam 5 · Q23).
- Default encryption doesn't depend on **tags or labels**. Those help with organization, policy conditions and cost tracking (Exam 5 · Q30).
- Customers who want more control over keys can use **Cloud KMS** with **customer-managed encryption keys (CMEK)**, or **customer-supplied encryption keys (CSEK)** in supported services. They can control key location, rotation, permissions and lifecycle (Exam 4 · Q18), (Exam 5 · Q23), (Exam 5 · Q30).
- If someone physically got into a data center, the stored data is still protected because it's stored with **strong encryption** (Exam 4 · Q3). This is one layer of **defense in depth**, next to physical security, access controls and monitoring (Exam 4 · Q3).
- **Data location** is controlled by the customer's choice of **regions, zones and multi-regions**. Google doesn't hide data in random places (Exam 4 · Q3).
- To meet data protection expectations in many countries, **encrypting personal data (PII)** is a baseline control (Exam 3 · Q28, see ⚠️).
- Moving to the cloud means you benefit from **built-in security** (default encryption, secured infrastructure) instead of building it all yourself (Exam 4 · Q19, see ⚠️).
- **Regular backups** let you restore to a **known-good state** after device failure, accidental deletion or ransomware. Good practice: scheduled backups, retention policies, protected backup storage and **testing restores**. Google Cloud offers **Backup and DR Service** for this (Exam 6 · Q23).
- An **incident response plan** prepares the company to reduce the impact of a breach. You still need one in the cloud (Exam 6 · Q25). It defines roles, escalation, communication, containment, investigation, recovery, **notification duties** and a post-incident review (Exam 6 · Q25).
- *(not in the question bank)* Key management options, from least to most customer control:
  - **Google default encryption**: Google manages the keys.
  - **CMEK (customer-managed encryption keys)**: keys live in **Cloud KMS**, and the customer controls rotation and access.
  - **Cloud HSM**: keys in certified hardware security modules.
  - **Cloud External Key Manager (EKM)**: keys stay outside Google.
  - **CSEK (customer-supplied encryption keys)**: the customer supplies the key with each request.
- **Sensitive Data Protection** (formerly Cloud DLP) discovers, classifies, masks, tokenizes and de-identifies sensitive data such as credit card numbers. It does not provide default encryption (Exam 5 · Q30). **Data masking** hides or replaces real values, for example in test environments (Exam 5 · Q7), (Exam 3 · Q47).
- *(not in the question bank)* Google designs its own hardware, including the **Titan** security chip that verifies machines boot trusted code.

### Decision rules
- "When is data encrypted by default?" → **at rest and in transit** (Exam 5 · Q23).
- "Why is data protected without anyone enabling it?" → **encrypted by default** (Exam 5 · Q30).
- Physical intrusion scenario → **strong encryption** (Exam 4 · Q3).
- Restore after corruption or ransomware → **regular backups** (Exam 6 · Q23). Prepare for a breach → **incident response plan** (Exam 6 · Q25).
- "Can customers manage or rotate their own keys?" → yes, with **Cloud KMS / CMEK** (Exam 4 · Q18).

### Traps
- **Security Command Center** and **Sensitive Data Protection** don't do the default encryption (Exam 5 · Q30).
- "Quantum computers", "unpredictable locations" and "instant deletion" are fantasy options (Exam 4 · Q3).
- **SLOs, Cloud Monitoring and autoscaling** don't restore lost data. Monitoring tells you something is wrong, and autoscaling adds instances that still depend on the damaged data (Exam 6 · Q23).
- **Reducing MFA** or **improving the physical perimeter of your own data center** doesn't prepare a cloud-only company for a breach (Exam 6 · Q25).
- "Replace perimeter security with encryption keys" is wrong. Encryption is one layer, not a replacement. You still need IAM, network security, logging, monitoring and vulnerability management (Exam 4 · Q19).
- "Built-in security" doesn't mean "nothing left to do". Plan your own part (identities, access, data permissions, app settings) from the start of the migration (Exam 4 · Q19).

---

## 7. Security operations and threat intelligence

### Key facts
- **Security Command Center (SCC)** is the **central place** to see security posture across many projects, find **misconfigurations and vulnerabilities**, prioritize findings and act on them (Exam 1 · Q30), (Exam 2 · Q35). It also gives **asset visibility**, **threat detection** and attack surface views, and it flags compliance issues **in your own resources** (Exam 1 · Q30), (Exam 6 · Q38).
- *(not in the question bank)* SCC can also **detect cryptomining** on your VMs, which links back to the threat in Lesson 2.
- **Google Security Operations** (Google SecOps, formerly Chronicle) is a cloud-native **SIEM/SOAR** platform. It brings security data from apps, endpoints, networks and clouds into one place, uses AI and threat intelligence for detection, and speeds up **investigation and response** (Exam 1 · Q40).
  - **SIEM** (security information and event management) collects, normalizes and correlates security data to detect threats.
  - **SOAR** (security orchestration, automation and response) runs **playbooks** that automate response steps (Exam 1 · Q40).
- **Threat intelligence** is analyzed information about attackers: their **goals, targets, malware campaigns and tactics, techniques and procedures (TTPs)**, plus **indicators of compromise (IoCs)** such as malicious IPs, domains and file hashes. Teams use it to detect earlier and defend proactively (Exam 3 · Q19).
- **Threat response** is what you do after something is detected: investigate, contain, remove the threat, recover and improve. It uses threat intelligence but isn't the intelligence itself (Exam 3 · Q19), (Exam 3 · Q8).
- **Mandiant** is Google Cloud's incident response and consulting organization. It is known for **frontline intelligence** from hands-on response to major attacks and breach investigations (Exam 1 · Q46).
- **VirusTotal** checks **files, URLs, domains and IP addresses** against **many antivirus engines, URL scanners and community submissions**. It is a crowdsourced malware intelligence source (Exam 1 · Q17).
- **Google Threat Intelligence** combines **Mandiant** frontline knowledge, **VirusTotal** crowdsourced data, Google's own visibility and **AI (Gemini)** analysis in one offering (Exam 5 · Q10).

### Security tools compared

| Product | What it does | Clue words | Source |
|---|---|---|---|
| Security Command Center | Posture, misconfigurations, vulnerabilities across projects | "centralized", "posture", "risky configurations", "prioritize findings" | (Exam 1 · Q30), (Exam 2 · Q35) |
| Google Security Operations | SIEM/SOAR: collect, detect, investigate, respond | "many alerts", "one place", "respond faster" | (Exam 1 · Q40) |
| Mandiant | Incident response experts, frontline intelligence | "hands-on incident response" | (Exam 1 · Q46) |
| VirusTotal | Scan files/URLs against many engines | "suspicious file", "many antivirus engines" | (Exam 1 · Q17) |
| Google Threat Intelligence | Mandiant + VirusTotal + Google visibility + AI | lists several sources together | (Exam 5 · Q10) |

### Decision rules
- Find weaknesses / misconfigurations across projects → **SCC** (Exam 1 · Q30), (Exam 2 · Q35).
- Too many alerts, need detection and response workflow → **Google SecOps** (Exam 1 · Q40).
- Single suspicious file or URL → **VirusTotal** (Exam 1 · Q17).
- Question lists Mandiant **and** VirusTotal **and** AI → **Google Threat Intelligence** (Exam 5 · Q10).

### Traps
- **Cloud Armor** blocks attacks at the edge. It doesn't give you a posture view (Exam 2 · Q35).
- **Threat response** is acting on an incident. **Threat intelligence** is the knowledge that informs it (Exam 3 · Q19).
- **IAM** and **GKE** show up as filler distractors in threat-intel questions (Exam 5 · Q10).
- **Apigee** manages and secures APIs. It is not a security operations platform (Exam 1 · Q40).
- **Compliance auditing** checks controls against standards. It isn't knowledge about attackers (Exam 3 · Q19).

---

## 8. Privacy, data ownership, sovereignty and compliance

### Key facts
- **Privacy** in the cloud = **restrictions on how personal data is accessed and shared** (Exam 6 · Q27). Privacy and security overlap but differ: **security** protects systems and data from threats, **privacy** is about proper handling of personal data. A breach of personal data becomes a privacy incident (Exam 6 · Q27).
- **Data sovereignty**: data is governed by the **laws of the country where it is stored**. Those laws can cover protection, access, privacy, retention and auditability (Exam 1 · Q10).
- **Data residency** is the choice of **where** data is physically stored (region selection). Sovereignty is the legal consequence of that choice. Companies pick regions and use **data residency controls** to meet sovereignty duties (Exam 1 · Q10). *(not in the question bank)* **Assured Workloads** and sovereign cloud offerings help meet location and personnel controls for regulated industries.
- **Google Distributed Cloud** extends Google Cloud to customer data centers and edge sites for strict **locality, regulatory, latency or survivability** needs. It is not a threat intelligence group (Exam 1 · Q46).
- Individual rights to **access, correct or delete** their personal data come from **privacy** laws, not sovereignty (Exam 1 · Q10).
- **The customer owns its data**, not Google, not a third party, not shared ownership. Google **processes** it to provide the service, under the customer's instructions. The customer decides what to upload, who can access it, how long to keep it and when to delete it (Exam 4 · Q4).
- Customers **control their data and can export or move it** whenever they want, with each service's export tools, transfer services or APIs. No support ticket or special activation is needed. Normal network charges and the customer's own IAM and network settings still apply (Exam 4 · Q6).
- Google **does not use customer data for advertising** (Exam 4 · Q18).
- Google has its privacy practices **independently audited against industry standards** (for example ISO/IEC 27001, 27017, 27018, SOC reports) (Exam 4 · Q12, see ⚠️).
- **Compliance Reports Manager** gives customers **certificates, audit reports and compliance documents** such as ISO 27001 certificates and SOC reports, on demand (Exam 6 · Q38). SCC checks **your** resources. Compliance Reports Manager proves **Google's** certifications (Exam 6 · Q38).
- *(not in the question bank)* The **Compliance resource center** lists certifications and regulations Google supports (GDPR, HIPAA, PCI DSS and more). **Access Transparency** logs Google staff access to your content, and **Access Approval** lets you approve that access first.
- Security spending under the **OpEx** model means **no large upfront capital investment** in security hardware. You still configure your own settings, and Google doesn't "guarantee security for every workload" (Exam 4 · Q47).

### Google's trust commitments

| Statement | True? | Source |
|---|---|---|
| The customer owns its data | ✅ | (Exam 4 · Q4) |
| Customer can export/transfer data at any time | ✅ | (Exam 4 · Q6) |
| Google doesn't use customer data for ads | ✅ | (Exam 4 · Q18) |
| Privacy practices audited against industry standards | ✅ | (Exam 4 · Q12) |
| Data can't leave Google Cloud / needs a ticket | ❌ | (Exam 4 · Q6) |
| Google and the customer share ownership | ❌ | (Exam 4 · Q4) |
| Google doesn't let customers change encryption keys | ❌ | (Exam 4 · Q18) |
| OpEx means you don't configure security | ❌ | (Exam 4 · Q47) |

### Decision rules
- "Laws of the country where data is stored" → **data sovereignty** (Exam 1 · Q10).
- "Restrictions on access and sharing" → **privacy** (Exam 6 · Q27).
- Need ISO 27001 certificate or audit report → **Compliance Reports Manager** (Exam 6 · Q38).
- Expanding to many countries → protect PII and follow **each market's** rules, not only the home country's (Exam 3 · Q28).

### Traps
- Sovereignty is **not** "a country can access all data in its borders", **not** individual control of personal data (that's privacy), and **not** encryption (Exam 1 · Q10).
- "Verifying a user's identity" is **authentication**, not privacy. "Meeting standards" is **compliance** (Exam 6 · Q27).
- **SCC**, **Network Intelligence Center** and **Cloud Monitoring** don't hold audit reports (Exam 6 · Q38).
- **Aggregating customer data by industry** or **migrating data to an offline server when a threat appears** are made-up policies (Exam 4 · Q12), (Exam 4 · Q18).
- A **business license** may be needed to operate in a market, but it doesn't protect customer data (Exam 3 · Q28).
- Following only the **headquarters country's** policies ignores where the data and users actually are (Exam 3 · Q28).

---

## ⚠️ Questionable answers

| Item | Issue |
|---|---|
| **(Exam 3 · Q28)** | Keyed "automatically encrypt PII". Encryption helps, but it doesn't by itself meet global compliance. Data residency, consent and local regulations matter too. Also, Google already encrypts all data at rest by default, so this isn't a special action. Pick it because the other options are clearly worse. |
| **(Exam 5 · Q4)** | Keyed "hire cybersecurity experts". Reasonable but vague. The real lesson is that security needs ongoing expertise and process, not a one-time tool purchase. |
| **(Exam 4 · Q12)** | Keyed "auditing platform privacy practices against industry standards". The idea is right (third-party audits such as ISO 27018/27701), but the phrasing is loose and option D ("privacy reviews for critical customer applications") sounds plausible to a newcomer. |
| **(Exam 4 · Q19)** | Keyed "built-in security". Very vague. It means Google's default protections (encryption, IAM, secure infrastructure, logging) plus planning your own share of the work from the start. The other options are plainly wrong (CapEx, more hardware, replacing perimeter security with keys). |
| **(Exam 3 · Q7)** | Keyed "map IAM roles to job functions for each department". Fine, but Google's stated best practice is to grant roles to **groups**. Treat "map to job functions" as the group-based answer. |

---

## Last-minute cheat sheet

- **Availability** = accessible when needed. Confidentiality = approved users only. Integrity = correct and complete (Exam 1 · Q27).
- **Security posture** = full readiness picture. **Cyber resilience** = prevent, keep running, recover (Exam 3 · Q8), (Exam 5 · Q7).
- Long-term security = **expertise and an evolving plan**, not a pricier tool (Exam 5 · Q4).
- Fake message asking for credentials → **phishing** (Exam 1 · Q31), (Exam 2 · Q28), (Exam 2 · Q41).
- Secret theft or damage → **malware**. Encrypted files + payment demand → **ransomware** (Exam 2 · Q46), (Exam 5 · Q17).
- Rogue VMs + bill spike → **cryptomining**. Public bucket by mistake → **misconfiguration**, not APT or zero-day (Exam 1 · Q25), (Exam 1 · Q26).
- Vendor plugin breach → **unsecured third-party systems**. Prompt override → **LLM attack** (Exam 3 · Q20), (Exam 5 · Q50).
- Physical data center security → **Google alone**, in every model (Exam 1 · Q49), (Exam 4 · Q20), (Exam 6 · Q42).
- Data access policies → **the customer's IT team** (Exam 5 · Q19).
- Who can view vs delete → **IAM**. Prove identity → **authentication** (first), then **authorization**. Second factor → **2SV/MFA** (Exam 1 · Q12), (Exam 5 · Q24), (Exam 3 · Q47).
- Service accounts are for **workloads**, not shared human logins (Exam 3 · Q7).
- Only what the job needs → **least privilege**. Many teams → **roles by job function** (Exam 6 · Q22), (Exam 3 · Q7).
- Traffic allow/deny → **firewall rules**. DDoS → **Cloud Armor**. AI prompts → **Model Armor** (Exam 3 · Q27), (Exam 3 · Q10), (Exam 4 · Q2), (Exam 1 · Q33).
- Verify every request from anywhere → **zero trust** (Exam 5 · Q6), (Exam 6 · Q49).
- Default encryption → **at rest and in transit**, no setup needed. More key control → **Cloud KMS / CMEK** (Exam 5 · Q23), (Exam 5 · Q30), (Exam 4 · Q3), (Exam 4 · Q18).
- Encrypt PII, rely on **built-in security** (Exam 3 · Q28), (Exam 4 · Q19).
- Restore → **backups**. Prepare for breach → **incident response plan** (Exam 6 · Q23), (Exam 6 · Q25).
- Posture across projects → **SCC**. Alert overload → **Google SecOps** (Exam 1 · Q30), (Exam 2 · Q35), (Exam 1 · Q40).
- TTP knowledge → **threat intelligence**. Frontline IR → **Mandiant**. File scan → **VirusTotal**. All combined → **Google Threat Intelligence** (Exam 3 · Q19), (Exam 1 · Q46), (Exam 1 · Q17), (Exam 5 · Q10).
- Laws of the storage country → **data sovereignty**. Privacy → **limits on access and sharing** (Exam 1 · Q10), (Exam 6 · Q27).
- Customer **owns** and can **export** its data. **No ads** use. **Audited** privacy (Exam 4 · Q4), (Exam 4 · Q6), (Exam 4 · Q18), (Exam 4 · Q12).
- ISO 27001 certificates → **Compliance Reports Manager** (Exam 6 · Q38).
- OpEx security → **no big upfront investment**, but you still configure (Exam 4 · Q47).
