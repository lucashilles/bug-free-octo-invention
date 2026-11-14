# Domain 5 Study Guide — Trust and Security with Google Cloud

> Condensed from the 50-question bank in [`05-trust-and-security.md`](05-trust-and-security.md). Citations look like (Exam N · QM). Many scenarios repeat across exams (phishing, Cloud Armor for DDoS, physical security under the shared responsibility model, default encryption), so look for paired citations. Items marked "see ⚠️" have a shaky or vague key, discussed at the end.

---

## 1. Core security concepts: CIA, posture, resilience

### Key facts
- **The CIA triad** is the base vocabulary of this domain:
  - **Confidentiality**: only approved users can access the data.
  - **Integrity**: data stays correct, complete and dependable.
  - **Availability**: data stays **dependable and accessible when needed** (Exam 1 · Q27).
- **Compliance** is a separate idea: meeting regulatory and industry standards. The exam uses it as a distractor for CIA questions (Exam 1 · Q27).
- **Security posture** is the **complete view** of an organization's cybersecurity readiness: network design, identity and access controls, monitoring coverage, and how consistently policies are applied (Exam 3 · Q8).
- **Cyber resilience** is the ability to **reduce the chance** of attacks, **keep essential services running** during an incident, **limit business impact** and **recover quickly** (Exam 5 · Q7).
- **Security is a continuous program, not a product.** A new security platform doesn't stop leaks on its own. Long-term improvement comes from **skilled people and an evolving security plan** (Exam 5 · Q4, see ⚠️).
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
- Waiting for a "newer platform" or buying "the most expensive platform" is never the answer (Exam 5 · Q4).

---

## 2. Cybersecurity threats

### Key facts
- **Phishing**: a fake message that looks trusted (support team, salary portal) and pushes urgency ("account disabled in 12 hours") to steal **credentials or bank details**, often via a **look-alike login page**. It is a **social engineering** attack (Exam 1 · Q31), (Exam 2 · Q28), (Exam 2 · Q41).
- **Malware**: malicious software that **secretly steals, alters or damages** information without the user noticing (Exam 2 · Q46).
- **Ransomware**: a type of malware that **encrypts your data and demands payment**, usually in cryptocurrency, for the decryption key (Exam 5 · Q17).
- **Cryptomining** (cryptojacking): attackers use a compromised account to create **unauthorized VMs** that burn CPU on **hashing to earn cryptocurrency**. The first sign is often an **unexpected bill** (Exam 1 · Q25).
- **Misconfiguration**: a human error such as making a bucket **public**. No software flaw is exploited. It is one of the most common causes of cloud data exposure (Exam 1 · Q26).
- **Unsecured third-party systems**: attackers enter through a **vendor's plugin or component** connected to your delivery process (a supply chain attack). Your own controls can be strong and you are still exposed (Exam 3 · Q20).
- **LLM attack (prompt injection)**: crafted prompts make an AI assistant **ignore its instructions**, leak restricted data or bypass response controls (Exam 5 · Q50).
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
- **SQL injection** is a code attack, not social engineering (Exam 2 · Q41).

---

## 3. The shared responsibility model

### Key facts
- In the cloud, **security is shared**. Google secures the platform. The customer secures what they put on it and how they configure it.
- **Google always owns physical security**: data center buildings, hardware and facilities. This holds for every service model, including IaaS (Exam 1 · Q49), (Exam 4 · Q20), (Exam 6 · Q42).
- In **IaaS (Compute Engine)** the customer keeps: guest **OS patching and hardening**, application code, encryption of data inside the app, and application-level user access (Exam 1 · Q49), (Exam 4 · Q20).
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
- **Cloud Identity** is a tool the customer uses. It doesn't decide policy (Exam 5 · Q19).
- Assuming security is "fully Google's responsibility" is always wrong (Exam 6 · Q25).

---

## 4. Identity and access management

### Key facts
- **IAM (Identity and Access Management)** defines **who** can do **what** on **which resource**. It's the answer when someone must view BigQuery datasets but not delete or create them (Exam 1 · Q12).
- **Authentication** = proving **who you are** (sign-in). **Authorization** = deciding **what you may do** after that (Exam 5 · Q24).
- **2-Step Verification (2SV) / multi-factor authentication (MFA)**: a password **plus** a second factor such as a phone prompt, a code or a **hardware security key** (Exam 3 · Q47).
- **Least privilege**: each person gets **only the permissions their job needs**, nothing more (Exam 6 · Q22).
- **Map roles to job functions.** When several departments share a project, define roles per function or team instead of per person. It's faster and easier to manage (Exam 3 · Q7).
- *(not in the question bank)* **Cloud Identity** manages users and groups and supports single sign-on (SSO). Best practice is to **grant roles to groups**, not to individuals.
- *(not in the question bank)* IAM role types: **basic** (Owner, Editor, Viewer: too broad), **predefined** (per service, e.g. BigQuery Data Viewer) and **custom**. Policies are **inherited** down the resource hierarchy (organization → folders → projects → resources).

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
- **VPC** controls network traffic, not who can delete a dataset (Exam 1 · Q12).
- **Zero trust** and **least privilege** are related. Zero trust is the overall model ("verify every request"). Least privilege is about how much access is granted (Exam 6 · Q22).

---

## 5. Network and application protection

### Key facts
- **Firewall rules** define which **incoming and outgoing traffic** is allowed or denied to your resources (Exam 3 · Q27).
- **Google Cloud Armor** protects internet-facing apps from **DDoS** and web attacks. It works at Google's edge with the external load balancer (Exam 3 · Q10), (Exam 4 · Q2).
- **Model Armor** inspects **AI prompts and responses**. It reduces **prompt injection and jailbreak** risk and blocks harmful output before it reaches users (Exam 1 · Q33). It is the defense against the LLM attacks in Lesson 2 (Exam 5 · Q50).
- **Zero trust** replaces "trust the corporate network" with **verify every identity, device and request, from any location** (Exam 5 · Q6). When an organization moves from project-by-project cloud use to broad transformation, the recommended shift is to a **zero-trust model that verifies users, devices and applications** (Exam 6 · Q49).
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

### Traps
- **Security Command Center** finds risks and misconfigurations. It doesn't absorb DDoS traffic (Exam 3 · Q10), (Exam 4 · Q2).
- **IAP** controls who can reach an app. It's not a DDoS shield (Exam 3 · Q10).
- A **VPN** encrypts a network path but still trusts whoever is inside. It is the opposite of zero trust (Exam 5 · Q6).
- "Strong perimeter and trust everything inside" is the old castle-and-moat model (Exam 6 · Q49).

---

## 6. Encryption, backup and incident readiness

### Key facts
- Google Cloud **encrypts customer data by default, at rest and in transit**. No team has to switch it on per service (Exam 5 · Q23), (Exam 5 · Q30).
- If someone physically got into a data center, the stored data is still protected because it's stored with **strong encryption** (Exam 4 · Q3).
- To meet data protection expectations in many countries, **encrypting personal data (PII)** is a baseline control (Exam 3 · Q28, see ⚠️).
- Moving to the cloud means you benefit from **built-in security** (default encryption, secured infrastructure) instead of building it all yourself (Exam 4 · Q19, see ⚠️).
- **Regular backups** let you restore to a **known-good state** after device failure or ransomware (Exam 6 · Q23).
- An **incident response plan** prepares the company to reduce the impact of a breach. You still need one in the cloud (Exam 6 · Q25).
- *(not in the question bank)* Key management options, from least to most customer control:
  - **Google default encryption**: Google manages the keys.
  - **CMEK (customer-managed encryption keys)**: keys live in **Cloud KMS**, and the customer controls rotation and access.
  - **Cloud HSM**: keys in certified hardware security modules.
  - **Cloud External Key Manager (EKM)**: keys stay outside Google.
  - **CSEK (customer-supplied encryption keys)**: the customer supplies the key with each request.
- *(not in the question bank)* **Sensitive Data Protection** (formerly Cloud DLP) discovers, classifies and masks sensitive data such as credit card numbers. It does not provide default encryption.
- *(not in the question bank)* Google designs its own hardware, including the **Titan** security chip that verifies machines boot trusted code.

### Decision rules
- "When is data encrypted by default?" → **at rest and in transit** (Exam 5 · Q23).
- "Why is data protected without anyone enabling it?" → **encrypted by default** (Exam 5 · Q30).
- Physical intrusion scenario → **strong encryption** (Exam 4 · Q3).
- Restore after corruption or ransomware → **regular backups** (Exam 6 · Q23). Prepare for a breach → **incident response plan** (Exam 6 · Q25).

### Traps
- **Security Command Center** and **Sensitive Data Protection** don't do the default encryption (Exam 5 · Q30).
- "Quantum computers", "unpredictable locations" and "instant deletion" are fantasy options (Exam 4 · Q3).
- **SLOs, Cloud Monitoring and autoscaling** don't restore lost data (Exam 6 · Q23).
- "Replace perimeter security with encryption keys" is wrong. Encryption is one layer, not a replacement (Exam 4 · Q19).

---

## 7. Security operations and threat intelligence

### Key facts
- **Security Command Center (SCC)** is the **central place** to see security posture across many projects, find **misconfigurations and vulnerabilities**, prioritize findings and act on them (Exam 1 · Q30), (Exam 2 · Q35).
- **Google Security Operations** (Google SecOps, formerly Chronicle) is a cloud-native **SIEM/SOAR** platform. It brings security data from apps, endpoints, networks and clouds into one place, uses AI and threat intelligence for detection, and speeds up **investigation and response** (Exam 1 · Q40).
- **Threat intelligence** is analyzed information about attackers: their **goals, targets, malware campaigns and tactics, techniques and procedures (TTPs)**. Teams use it to detect earlier and defend proactively (Exam 3 · Q19).
- **Mandiant** is Google Cloud's incident response and consulting organization. It is known for **frontline intelligence** from hands-on response to major attacks (Exam 1 · Q46).
- **VirusTotal** checks files and URLs against **many antivirus engines, URL scanners and community submissions**. It is a crowdsourced malware intelligence source (Exam 1 · Q17).
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

---

## 8. Privacy, data ownership, sovereignty and compliance

### Key facts
- **Privacy** in the cloud = **restrictions on how personal data is accessed and shared** (Exam 6 · Q27).
- **Data sovereignty**: data is governed by the **laws of the country where it is stored** (Exam 1 · Q10).
- *(not in the question bank)* **Data residency** is the choice of **where** data is physically stored (region selection). Sovereignty is the legal consequence of that choice. **Assured Workloads** and sovereign cloud offerings help meet location and personnel controls for regulated industries.
- **The customer owns its data**, not Google, not a third party, not shared ownership (Exam 4 · Q4).
- Customers **control their data and can export or move it** whenever they want. No support ticket or special activation is needed (Exam 4 · Q6).
- Google **does not use customer data for advertising** (Exam 4 · Q18).
- Google has its privacy practices **independently audited against industry standards** (for example ISO/IEC 27001, 27017, 27018, SOC reports) (Exam 4 · Q12, see ⚠️).
- **Compliance Reports Manager** gives customers **certificates, audit reports and compliance documents** such as ISO 27001 (Exam 6 · Q38).
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
- **SCC** and **Cloud Monitoring** don't hold audit reports (Exam 6 · Q38).
- Following only the **headquarters country's** policies ignores where the data and users actually are (Exam 3 · Q28).

---

## ⚠️ Questionable answers

| Item | Issue |
|---|---|
| **(Exam 3 · Q28)** | Keyed "automatically encrypt PII". Encryption helps, but it doesn't by itself meet global compliance. Data residency, consent and local regulations matter too. Also, Google already encrypts all data at rest by default, so this isn't a special action. Pick it because the other options are clearly worse. |
| **(Exam 5 · Q4)** | Keyed "hire cybersecurity experts". Reasonable but vague. The real lesson is that security needs ongoing expertise and process, not a one-time tool purchase. |
| **(Exam 4 · Q12)** | Keyed "auditing platform privacy practices against industry standards". The idea is right (third-party audits such as ISO 27018/27701), but the phrasing is loose and option D ("privacy reviews for critical customer applications") sounds plausible to a newcomer. |
| **(Exam 4 · Q19)** | Keyed "built-in security". Very vague. It means Google's default protections (encryption, secure infrastructure). The other options are plainly wrong (CapEx, more hardware, replacing perimeter security with keys). |
| **(Exam 3 · Q7)** | Keyed "map IAM roles to job functions for each department". Fine, but Google's stated best practice is to grant roles to **groups**. Treat "map to job functions" as the group-based answer. |

---

## Last-minute cheat sheet

- **Availability** = accessible when needed. Confidentiality = approved users only. Integrity = correct and complete (Exam 1 · Q27).
- **Security posture** = full readiness picture. **Cyber resilience** = prevent, keep running, recover (Exam 3 · Q8), (Exam 5 · Q7).
- Long-term security = **expertise and an evolving plan**, not a pricier tool (Exam 5 · Q4).
- Fake message asking for credentials → **phishing** (Exam 1 · Q31), (Exam 2 · Q28), (Exam 2 · Q41).
- Secret theft or damage → **malware**. Encrypted files + payment demand → **ransomware** (Exam 2 · Q46), (Exam 5 · Q17).
- Rogue VMs + bill spike → **cryptomining**. Public bucket by mistake → **misconfiguration** (Exam 1 · Q25), (Exam 1 · Q26).
- Vendor plugin breach → **unsecured third-party systems**. Prompt override → **LLM attack** (Exam 3 · Q20), (Exam 5 · Q50).
- Physical data center security → **Google alone**, in every model (Exam 1 · Q49), (Exam 4 · Q20), (Exam 6 · Q42).
- Data access policies → **the customer's IT team** (Exam 5 · Q19).
- Who can view vs delete → **IAM**. Prove identity → **authentication**. Second factor → **2SV/MFA** (Exam 1 · Q12), (Exam 5 · Q24), (Exam 3 · Q47).
- Only what the job needs → **least privilege**. Many teams → **roles by job function** (Exam 6 · Q22), (Exam 3 · Q7).
- Traffic allow/deny → **firewall rules**. DDoS → **Cloud Armor**. AI prompts → **Model Armor** (Exam 3 · Q27), (Exam 3 · Q10), (Exam 4 · Q2), (Exam 1 · Q33).
- Verify every request from anywhere → **zero trust** (Exam 5 · Q6), (Exam 6 · Q49).
- Default encryption → **at rest and in transit**, no setup needed (Exam 5 · Q23), (Exam 5 · Q30), (Exam 4 · Q3).
- Encrypt PII, rely on **built-in security** (Exam 3 · Q28), (Exam 4 · Q19).
- Restore → **backups**. Prepare for breach → **incident response plan** (Exam 6 · Q23), (Exam 6 · Q25).
- Posture across projects → **SCC**. Alert overload → **Google SecOps** (Exam 1 · Q30), (Exam 2 · Q35), (Exam 1 · Q40).
- TTP knowledge → **threat intelligence**. Frontline IR → **Mandiant**. File scan → **VirusTotal**. All combined → **Google Threat Intelligence** (Exam 3 · Q19), (Exam 1 · Q46), (Exam 1 · Q17), (Exam 5 · Q10).
- Laws of the storage country → **data sovereignty**. Privacy → **limits on access and sharing** (Exam 1 · Q10), (Exam 6 · Q27).
- Customer **owns** and can **export** its data. **No ads** use. **Audited** privacy (Exam 4 · Q4), (Exam 4 · Q6), (Exam 4 · Q18), (Exam 4 · Q12).
- ISO 27001 certificates → **Compliance Reports Manager** (Exam 6 · Q38).
- OpEx security → **no big upfront investment**, but you still configure (Exam 4 · Q47).
