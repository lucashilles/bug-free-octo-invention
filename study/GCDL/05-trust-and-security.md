# Domain 5 — Trust and Security with Google Cloud

50 questions. Answers are collapsed — try each question before expanding it.

## Questions

### Exam 1 · Q10

**FinWell, a digital banking company, stores customer transaction records in cloud regions selected for regulatory reasons. The compliance team wants to understand how the legal idea of data sovereignty affects those records. What does data sovereignty mean for the stored data?**

- A. Data is governed by the laws and regulations of the country where it is stored.
- B. A country automatically has the right to access all data created inside its borders.
- C. A customer has the right to fully control their own personal information.
- D. Data must be encrypted whenever it is stored or transmitted.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Data is governed by the laws and regulations of the country where it is stored.

**Correct answer: A. Data is governed by the laws and regulations of the country where it is stored.**

Data sovereignty means data is subject to the laws of the country (or region) where it physically resides. That is why FinWell picks regions "for regulatory reasons". Where the data sits decides which rules apply to it.

**Why the others are wrong:**
- **B. A country automatically has the right to access all data**: sovereignty means local laws apply, not that a government can access everything automatically.
- **C. A customer has the right to fully control their own personal information**: this describes data privacy and individual rights, not sovereignty.
- **D. Data must be encrypted**: encryption is a security control; it is not the definition of sovereignty.

**Remember:** Sovereignty = whose laws apply. Residency = where the data is stored.

</details>

---

### Exam 1 · Q12

**SkillGrid Analytics, an online learning platform, has hired a new reporting analyst. The administrator wants the analyst to be able to view existing BigQuery datasets for dashboard work, but the analyst must not be allowed to delete datasets or create new datasets. Which Google Cloud service should the administrator use to define and assign the correct access roles?**

- A. Cloud Storage
- B. Identity and Access Management (IAM)
- C. Virtual Private Cloud (VPC)
- D. Cloud Trace

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Identity and Access Management (IAM)

**Correct answer: B. Identity and Access Management (IAM)**

IAM controls who can do what on which resource. The administrator grants the analyst a role that allows viewing BigQuery data but not creating or deleting datasets. This follows the principle of least privilege. The clue is "define and assign the correct access roles".

**Why the others are wrong:**
- **A. Cloud Storage**: Cloud Storage is object storage, not an access control service.
- **C. Virtual Private Cloud (VPC)**: VPC controls network connectivity, not per-user permissions on datasets.
- **D. Cloud Trace**: Cloud Trace measures request latency in applications.

**Remember:** Who can do what on which resource = IAM. Give only the access needed (least privilege).

</details>

---

### Exam 1 · Q17

**NovaInbox, a secure email collaboration platform, receives a file attachment that looks suspicious after being reported by an employee. The security research team wants to compare the file and related URLs against a large global threat intelligence dataset that aggregates results from many antivirus engines, URL scanners, and security community submissions. Which Google Cloud-affiliated tool should the team use?**

- A. Cloud Translation API
- B. Cloud SQL
- C. VirusTotal
- D. BigQuery Omni

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. VirusTotal

**Correct answer: C. VirusTotal**

VirusTotal, part of Google, checks files and URLs against many antivirus engines, URL scanners and community submissions. It holds a large shared threat intelligence dataset. The clue is the exact description: "aggregates results from many antivirus engines, URL scanners, and security community submissions".

**Why the others are wrong:**
- **A. Cloud Translation API**: it translates text between languages and has no security function.
- **B. Cloud SQL**: it is a managed relational database, not a threat intelligence tool.
- **D. BigQuery Omni**: it runs BigQuery analytics on data in other clouds; it is not a malware scanner.

**Remember:** Check a suspicious file or URL against many scanners = VirusTotal. Frontline incident-response intelligence = Mandiant.

</details>

---

### Exam 1 · Q25

**BrightCart, an online grocery delivery app, runs several batch-processing workloads on Compute Engine. The finance team notices that the monthly Compute Engine bill has increased unexpectedly. After reviewing the project, the security team finds that a compromised account created unauthorized VM workloads that are consuming CPU resources to perform hashing calculations and earn cryptocurrency for the attacker. What type of attack is this?**

- A. Cryptomining
- B. Phishing
- C. LLM attack
- D. Distributed Denial-of-Service (DDoS)

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Cryptomining

**Correct answer: A. Cryptomining**

Cryptomining (cryptojacking) is when attackers use someone else's computing resources to mine cryptocurrency. The victim pays the bill. The clues are unauthorized VMs, high CPU use for "hashing calculations" and a surprise rise in the compute bill.

**Why the others are wrong:**
- **B. Phishing**: phishing tricks people into giving away credentials; it may be how the account was compromised, but it is not what the VMs are doing.
- **C. LLM attack**: this targets AI models, such as with prompt injection; no AI model is involved here.
- **D. DDoS**: a DDoS floods a service with traffic to make it unavailable; it does not use the victim's VMs to earn money.

**Remember:** Surprise compute bill + unknown VMs + high CPU = cryptomining.

</details>

---

### Exam 1 · Q26

**MealTrail, a food delivery app, stores order history and customer contact details in a Cloud Storage bucket. During an internal review, the team discovers that a junior administrator accidentally allowed public internet access to the bucket. External users could view the files without exploiting any software flaw or using advanced attack methods. What is the root cause of this security incident?**

- A. Misconfiguration
- B. Advanced Persistent Threat (APT)
- C. Zero-day vulnerability
- D. Ransomware

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Misconfiguration

**Correct answer: A. Misconfiguration**

The bucket was exposed because an administrator set its access incorrectly. No software flaw or advanced attack was involved. Misconfiguration is one of the most common causes of cloud data exposure. The clue is "accidentally allowed public internet access" and "without exploiting any software flaw".

**Why the others are wrong:**
- **B. Advanced Persistent Threat (APT)**: an APT is a skilled attacker staying hidden in a network for a long time, which is not what happened.
- **C. Zero-day vulnerability**: a zero-day is an unknown software flaw; the stem says no flaw was exploited.
- **D. Ransomware**: ransomware encrypts data and demands payment; here files were simply readable.

**Remember:** Human error in settings (like a public bucket) = misconfiguration.

</details>

---

### Exam 1 · Q27

**HealthBridge, a telemedicine provider, stores patient appointment details and consultation records in Google Cloud. The security team is reviewing the core security principles that help protect data. They want to understand how availability strengthens the organization’s overall data security posture. What does availability mean in this context?**

- A. By limiting data access only to approved users
- B. By making sure data follows required regulatory and industry standards
- C. By verifying that data remains correct, complete, and dependable
- D. By making sure data remains dependable and accessible when needed

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. By making sure data remains dependable and accessible when needed

**Correct answer: D. By making sure data remains dependable and accessible when needed**

Availability is the "A" in the CIA triad (confidentiality, integrity, availability). It means authorized users can reach data and systems when they need them. For a telemedicine provider, doctors must be able to open patient records during consultations.

**Why the others are wrong:**
- **A. Limiting access to approved users**: this is confidentiality.
- **B. Following regulatory and industry standards**: this is compliance.
- **C. Data remains correct, complete, and dependable**: this is integrity.

**Remember:** Confidentiality = only the right people. Integrity = correct and unaltered. Availability = there when needed.

</details>

---

### Exam 1 · Q30

**BrightCart, a retail mobile app company, runs more than 240 Google Cloud projects for payment services, product search, inventory APIs, and analytics workloads. Its security team wants one centralized place to review the organization’s overall security posture, find risky configurations, and detect vulnerabilities across the Google Cloud environment. Which Google Cloud product should BrightCart use?**

- A. Security Command Center
- B. Managed Service for Apache Spark
- C. Cloud Load Balancing
- D. Dataflow

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Security Command Center

**Correct answer: A. Security Command Center**

Security Command Center is Google Cloud's central security and risk management service. It shows the security posture across the whole organization and finds misconfigurations, vulnerabilities and threats. The clues are "240 projects", "one centralized place", "risky configurations" and "vulnerabilities".

**Why the others are wrong:**
- **B. Managed Service for Apache Spark**: it runs Spark and Hadoop data processing jobs, not security reviews.
- **C. Cloud Load Balancing**: it spreads traffic across back ends; it does not assess security posture.
- **D. Dataflow**: Dataflow runs data pipelines, not security scanning.

**Remember:** Central view of security posture, misconfigurations and vulnerabilities across Google Cloud = Security Command Center.

</details>

---

### Exam 1 · Q31

**FinEdge Pay, a digital wallet company, trains employees to recognize common cybersecurity threats. One employee receives a message that looks like it came from the internal support team. The message says the employee’s account access will be disabled in 12 hours unless they click a link and sign in on a look-alike company portal. The portal is fake and is built to capture the employee’s username and password. What type of cybersecurity threat is this?**

- A. DDoS attack
- B. Phishing
- C. Cryptomining
- D. LLM attack

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Phishing

**Correct answer: B. Phishing**

Phishing is a social engineering attack. A fake message pretends to come from a trusted source and tricks people into giving up credentials or clicking malicious links. The clues are the urgent threat (access disabled in 12 hours), a look-alike portal and a fake sign-in page built to capture usernames and passwords.

**Why the others are wrong:**
- **A. DDoS attack**: a DDoS floods a service with traffic; it does not trick employees into sharing passwords.
- **C. Cryptomining**: cryptomining uses stolen computing power to mine cryptocurrency.
- **D. LLM attack**: this targets AI models, such as with prompt injection; no AI model is involved.

**Remember:** Fake message + urgency + fake login page = phishing.

</details>

---

### Exam 1 · Q33

**FitGuide, a fitness coaching mobile app, is launching several public-facing generative AI chat features for workout planning and nutrition guidance. The security team wants a Google Cloud capability that can inspect AI prompts and responses, reduce prompt injection and jailbreak risks, and block harmful or inappropriate model output before it reaches users. Which Google Cloud capability should the team use?**

- A. Cloud Storage Autoclass
- B. Model Armor
- C. Virtual Machine snapshots
- D. Cloud Run functions

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Model Armor

**Correct answer: B. Model Armor**

Model Armor is a Google Cloud service that screens prompts and responses for generative AI apps. It helps detect prompt injection and jailbreak attempts and filters harmful or inappropriate content before it reaches users. The clue is "inspect AI prompts and responses" and "block harmful or inappropriate model output".

**Why the others are wrong:**
- **A. Cloud Storage Autoclass**: it optimizes storage costs; it has nothing to do with AI safety.
- **C. Virtual Machine snapshots**: snapshots back up VM disks; they do not inspect AI traffic.
- **D. Cloud Run functions**: it runs event-driven code, not AI prompt and response screening.

**Remember:** Protect gen AI prompts and responses (prompt injection, jailbreaks, harmful output) = Model Armor.

</details>

---

### Exam 1 · Q40

**MedNova Health, a digital healthcare portal, receives a very large number of security alerts from applications, endpoints, network devices, and cloud services every day. Its security operations team wants a cloud-native platform that can bring security data into one place, use AI and threat intelligence to improve detection, support investigations, and help analysts respond to incidents faster. Which Google Cloud solution should MedNova Health use?**

- A. Google Security Operations
- B. Apigee API Management
- C. Compute Engine
- D. Cloud Spanner

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Google Security Operations

**Correct answer: A. Google Security Operations**

Google Security Operations (formerly Chronicle) is a cloud-native security operations platform (SIEM and SOAR). It collects security data in one place, uses AI and threat intelligence to detect threats, and helps analysts investigate and respond faster. The clues are "a very large number of security alerts", "bring security data into one place" and "respond to incidents faster".

**Why the others are wrong:**
- **B. Apigee API Management**: it manages and secures APIs; it is not a security operations platform.
- **C. Compute Engine**: it provides virtual machines.
- **D. Cloud Spanner**: it is a globally distributed relational database.

**Remember:** Centralize security data, detect, investigate and respond = Google Security Operations.

</details>

---

### Exam 1 · Q46

**BluePeak Insurance is reviewing Google Cloud’s advanced security capabilities after a series of industry-wide cyber incidents. The CISO wants to highlight the organization within Google Cloud that is known for intelligence gathered from hands-on incident response work during major cyberattacks across the world. Which organization provides this type of frontline threat intelligence?**

- A. VirusTotal
- B. Mandiant
- C. Google Distributed Cloud
- D. Looker

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Mandiant

**Correct answer: B. Mandiant**

Mandiant, part of Google Cloud, is known for frontline threat intelligence. It gathers this from hands-on incident response to major cyberattacks around the world. The clue is "intelligence gathered from hands-on incident response work".

**Why the others are wrong:**
- **A. VirusTotal**: VirusTotal provides crowdsourced scanning of files and URLs, not frontline incident-response intelligence.
- **C. Google Distributed Cloud**: it extends Google Cloud infrastructure to edge and on-premises locations; it is not a threat intelligence group.
- **D. Looker**: Looker is a business intelligence tool.

**Remember:** Frontline incident-response experts and intelligence = Mandiant. Crowdsourced file and URL scanning = VirusTotal.

</details>

---

### Exam 1 · Q49

**RiverBox Media, a video streaming company, is migrating several internal applications from its private data center to Google Cloud by using Compute Engine virtual machines. The security team is reviewing the Shared Responsibility Model to understand which security duties will move from RiverBox Media to Google Cloud when using Infrastructure as a Service. Which responsibility is inherently handled by Google Cloud?**

- A. Physical security of the data center facilities
- B. Managing application-level user access
- C. Encrypting sensitive data within the application
- D. Applying operating system patches to virtual machines

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Physical security of the data center facilities

**Correct answer: A. Physical security of the data center facilities**

Under the shared responsibility model, Google always secures the physical infrastructure: buildings, hardware and the underlying network. With IaaS (Compute Engine), the customer still manages the guest OS, applications, data and user access. The clue is "inherently handled by Google Cloud" with IaaS.

**Why the others are wrong:**
- **B. Managing application-level user access**: the customer controls who can use its applications.
- **C. Encrypting sensitive data within the application**: Google encrypts data at rest by default, but application-level encryption is the customer's job.
- **D. Applying OS patches to VMs**: with IaaS the customer manages the guest operating system, including patches.

**Remember:** IaaS: Google secures the physical layer; you secure the OS, apps, data and access.

</details>

---

### Exam 2 · Q28

**A payroll assistant at MetroKart receives an email that appears to come from the company’s salary portal. The message says their account will be suspended unless they reply with their bank account number and login password. Which cybersecurity threat is this?**

- A. Ransomware
- B. Distributed Denial of Service
- C. Spamming
- D. Phishing

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Phishing

**Correct answer: D. Phishing**

Phishing is a fake message that pretends to come from a trusted source to trick people into giving away sensitive data like passwords or bank details. The clues are an email that "appears to come from the company’s salary portal" and a request to reply with login and bank details.

**Why the others are wrong:**
- **A. Ransomware**: Ransomware encrypts files and demands payment to unlock them.
- **B. Distributed Denial of Service**: DDoS floods a service with traffic to knock it offline.
- **C. Spamming**: Spam is unwanted bulk email; this message is a targeted attempt to steal credentials.

**Remember:** Fake trusted message asking for passwords or financial data → phishing.

</details>

---

### Exam 2 · Q35

**FinSurely, a financial planning mobile app, runs workloads on Google Cloud and needs a central way to discover security weaknesses across its cloud resources and applications. The security team wants to identify risks, prioritize findings, and take remediation actions. Which Google Cloud service should FinSurely use?**

- A. Security Command Center
- B. Google Cloud Armor
- C. Cloud Storage
- D. VPC networks

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Security Command Center

**Correct answer: A. Security Command Center**

Security Command Center is Google Cloud's central security and risk management service. It finds vulnerabilities and misconfigurations across your resources, helps prioritize findings, and supports remediation. The clues are "central way to discover security weaknesses" and "prioritize findings".

**Why the others are wrong:**
- **B. Google Cloud Armor**: Cloud Armor protects web apps from DDoS and web attacks; it does not inventory risks across resources.
- **C. Cloud Storage**: Cloud Storage stores objects; it is not a security tool.
- **D. VPC networks**: VPCs are private networks for your resources, not a risk discovery tool.

**Remember:** One central view of security risks and findings in Google Cloud → Security Command Center.

</details>

---

### Exam 2 · Q41

**SkyTrail Logistics uses Google Cloud to host its shipment tracking portal. The security team is reviewing common cyber threats and is especially worried about attackers tricking employees into revealing passwords or clicking malicious links. Which type of attack best represents this social engineering risk?**

- A. SQL injection attacks
- B. Physical damage to hardware
- C. Phishing emails
- D. Distributed denial-of-service attacks

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Phishing emails

**Correct answer: C. Phishing emails**

Phishing is a social engineering attack. Attackers send messages that look legitimate to trick people into revealing passwords or clicking malicious links. The clues are "tricking employees" and "social engineering".

**Why the others are wrong:**
- **A. SQL injection attacks**: SQL injection targets application code by sending malicious database queries, not people.
- **B. Physical damage to hardware**: This is a physical threat, not trickery of employees.
- **D. Distributed denial-of-service attacks**: DDoS overwhelms services with traffic; it does not trick people.

**Remember:** Tricking people into giving secrets or clicking links → phishing (social engineering).

</details>

---

### Exam 2 · Q46

**NovaCart, an online shopping platform, wants to improve its security awareness training for employees. The training team asks which type of cybersecurity threat can secretly steal, alter, or damage information on a device or system without the user noticing. Which cybersecurity threat does this describe?**

- A. SLA policy violation
- B. Malware attack
- C. Ransomware attack
- D. Incomplete data input

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Malware attack

**Correct answer: B. Malware attack**

Malware is any malicious software, such as viruses, spyware, or trojans, that can secretly steal, change, or damage data. The broad description "steal, alter, or damage information … without the user noticing" fits malware in general.

**Why the others are wrong:**
- **A. SLA policy violation**: An SLA violation is a missed service promise, not a cyber threat.
- **C. Ransomware attack**: Ransomware is one type of malware; it locks data and demands payment, which users notice right away.
- **D. Incomplete data input**: This is a data quality issue, not an attack.

**Remember:** Malicious software that secretly harms data → malware; locks data for payment → ransomware.

</details>

---

### Exam 3 · Q7

**PixelHive Media is building a shared analytics environment on Google Cloud. Its marketing, finance, and engineering teams all need access to the same project, but each team needs different permissions based on the work they perform. What is the fastest and most efficient way to manage access?**

- A. Map IAM roles to job functions for each department.
- B. Assign IAM basic roles to each employee.
- C. Apply least-privilege roles separately for each employee.
- D. Create one shared service account for all departments.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Map IAM roles to job functions for each department.

**Correct answer: A. Map IAM roles to job functions for each department.**

Each team needs different permissions, so define roles by what each job requires and grant them per department. This is far easier to manage than handling every person one by one. In practice you put each team in a group and grant the roles to the group.

**Why the others are wrong:**
- **B. Assign basic roles to each employee**: Basic roles (Owner, Editor, Viewer) are too broad and per-person grants don't scale.
- **C. Least-privilege roles separately for each employee**: Least privilege is right, but per-employee management is slow and error-prone.
- **D. One shared service account for all departments**: It removes accountability and gives everyone the same access.

**Remember:** Grant roles by job function to groups, not to individuals.

**⚠️ Note:** Google's stated best practice is to grant roles to groups. Read "map roles to job functions for each department" as the group-based answer. It is the best option here.

</details>

---

### Exam 3 · Q8

**BrightPath Finance is preparing for a Google Cloud compliance review. The audit team is evaluating the company’s network design, identity and access controls, monitoring coverage, and whether security policies are consistently applied across projects and resources. What term best describes this complete view of the company’s cybersecurity readiness?**

- A. Threat response
- B. Security posture
- C. Cryptomining
- D. Digital transformation

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Security posture

**Correct answer: B. Security posture**

Security posture is the overall state of an organization's security: its network design, access controls, monitoring and how consistently policies are applied. The stem asks for a "complete view of cybersecurity readiness", which is the definition of posture.

**Why the others are wrong:**
- **A. Threat response**: That is how you react to an incident, only one part of the picture.
- **C. Cryptomining**: That is an attack type where stolen compute mines cryptocurrency.
- **D. Digital transformation**: That is using technology to change how a business works, not a security term.

**Remember:** Overall security readiness across the environment = security posture.

</details>

---

### Exam 3 · Q10

**TrailCart Market runs an online shopping platform on Google Cloud. During a holiday sale, a malicious botnet starts sending a huge volume of fake HTTP requests to the application, trying to exhaust resources and prevent real shoppers from accessing the site. Which Google Cloud service should TrailCart Market use to help protect the application from Distributed Denial-of-Service attacks?**

- A. Security Command Center
- B. Google Cloud Armor
- C. Identity-Aware Proxy (IAP)
- D. Cloud Key Management Service (KMS)

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Google Cloud Armor

**Correct answer: B. Google Cloud Armor**

Google Cloud Armor protects applications behind Google's load balancers from DDoS attacks and web attacks. It can filter and rate-limit malicious traffic before it reaches the app. The clues are "botnet", "huge volume of fake HTTP requests" and "DDoS".

**Why the others are wrong:**
- **A. Security Command Center**: It gives visibility into security risks and findings; it doesn't block attack traffic.
- **C. Identity-Aware Proxy (IAP)**: It controls who can reach an app based on identity, not volumetric attacks on a public site.
- **D. Cloud KMS**: It manages encryption keys.

**Remember:** DDoS or web attack protection = Cloud Armor.

</details>

---

### Exam 3 · Q19

**LogiNest Retail uses Google Security Operations to strengthen its Cloud SecOps program. The security team depends on analyzed information about attacker goals, common targets, malware campaigns, tactics, techniques, and procedures so they can detect risks earlier and defend the environment proactively. What is this type of cybersecurity information called?**

- A. Threat intelligence
- B. Threat response
- C. Compliance auditing
- D. Identity management

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Threat intelligence

**Correct answer: A. Threat intelligence**

Threat intelligence is analyzed information about attackers: their goals, targets, malware campaigns and tactics, techniques and procedures (TTPs). Security teams use it to detect and stop threats earlier. Google Security Operations includes threat intelligence from Google and Mandiant.

**Why the others are wrong:**
- **B. Threat response**: That is acting on an incident, not the information used to anticipate it.
- **C. Compliance auditing**: That checks controls against regulations or standards.
- **D. Identity management**: That controls user identities and access.

**Remember:** Knowledge about attackers and their methods = threat intelligence.

</details>

---

### Exam 3 · Q20

**MedNest Health has strong internal security controls for its Google Cloud environment, but it recently experienced a data exposure incident. The investigation found that attackers entered through a small appointment-booking plugin from an outside vendor that was connected to MedNest Health’s software delivery process. Which modern cybersecurity threat vector does this situation demonstrate?**

- A. Unsecured third-party systems
- B. Physical damage
- C. LLM attacks
- D. Zero trust architecture

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Unsecured third-party systems

**Correct answer: A. Unsecured third-party systems**

The attackers came in through an outside vendor's plugin connected to the software delivery process. That is a supply chain risk from an unsecured third-party system. Your security is only as strong as the vendors and components you connect to.

**Why the others are wrong:**
- **B. Physical damage**: Nothing physical happened; this was a software entry point.
- **C. LLM attacks**: No AI model or prompt was involved.
- **D. Zero trust architecture**: Zero trust is a security model, not a threat vector.

**Remember:** Breach through a vendor's plugin or library = third-party / supply chain risk.

</details>

---

### Exam 3 · Q27

**ParcelPilot, a delivery tracking website, is hosting its application on Google Cloud. The security team wants to define which incoming and outgoing network traffic should be allowed or denied before users and systems can reach the application. Which security measure should ParcelPilot use?**

- A. 2-Step Verification
- B. Privileged access
- C. Encryption keys
- D. Firewall rules

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Firewall rules

**Correct answer: D. Firewall rules**

Firewall rules define which incoming and outgoing network traffic is allowed or denied for your resources. The clue is "incoming and outgoing network traffic should be allowed or denied".

**Why the others are wrong:**
- **A. 2-Step Verification**: It confirms a user's identity at sign-in; it doesn't filter network traffic.
- **B. Privileged access**: That is about elevated permissions for users.
- **C. Encryption keys**: They protect data confidentiality, not traffic flow.

**Remember:** Allow or deny network traffic = firewall rules.

</details>

---

### Exam 3 · Q28

**StreamWave, a video streaming platform, plans to expand its service to viewers in multiple countries. The company wants to use cloud capabilities to help meet global compliance and data protection expectations for customer information. What should StreamWave do?**

- A. Automatically encrypt personally identifiable information.
- B. Obtain a business license before launching in each new market.
- C. Allow users to turn off two-factor authentication.
- D. Follow only the data policies of the country where the company headquarters is registered.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Automatically encrypt personally identifiable information.

**Correct answer: A. Automatically encrypt personally identifiable information.**

Protecting personal data is a key part of data protection rules in many countries. Encrypting PII protects it if it is accessed without permission. It is the only option that uses cloud capabilities to protect customer data.

**Why the others are wrong:**
- **B. Obtain a business license**: A legal step, but it doesn't protect customer data.
- **C. Let users turn off two-factor authentication**: This weakens security.
- **D. Follow only headquarters' data policies**: Companies must respect the laws of every country where they serve users.

**Remember:** Global data protection starts with protecting PII; ignoring local laws or weakening auth is always wrong.

**⚠️ Note:** Encryption alone doesn't meet global compliance. Data residency, consent and local rules matter too, and Google Cloud already encrypts all data at rest by default. Pick the keyed answer because the other options are clearly worse.

</details>

---

### Exam 3 · Q47

**QuickCart Labs is rolling out stricter access controls for employees who sign in to Google Cloud. The security team wants every user to enter their password and then prove their identity again by using a phone prompt, verification code, or hardware security key. Which security practice is being implemented?**

- A. Distributed Denial-of-Service protection
- B. Data masking
- C. Two-step verification (2SV) / Multi-factor authentication
- D. Threat intelligence sharing

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Two-step verification (2SV) / Multi-factor authentication

**Correct answer: C. Two-step verification (2SV) / Multi-factor authentication**

Two-step verification, a form of multi-factor authentication, requires a password plus a second proof such as a phone prompt, code or security key. This blocks attackers who only have a stolen password.

**Why the others are wrong:**
- **A. DDoS protection**: Protects against floods of traffic, not user sign-in.
- **B. Data masking**: Hides sensitive values in data.
- **D. Threat intelligence sharing**: Shares information about attackers; it doesn't verify identity.

**Remember:** Password + second proof = 2SV / MFA.

</details>

---

### Exam 4 · Q2

**HealthWave Portal hosts a public appointment-booking website on Google Cloud. The security team wants to protect the website from distributed denial-of-service attacks that could overwhelm the application with malicious traffic. Which Google Cloud service should HealthWave Portal use?**

- A. Google Cloud Armor
- B. Cloud Build
- C. Cloud VPN
- D. Security Command Center

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Google Cloud Armor

**Correct answer: A. Google Cloud Armor**

Google Cloud Armor protects internet-facing apps from DDoS attacks and common web attacks. It sits at the edge of Google's network in front of the load balancer and filters malicious traffic before it reaches the app. The clue is "distributed denial-of-service attacks" against a public website.

**Why the others are wrong:**
- **B. Cloud Build**: It is a CI/CD service that builds and tests code, not a traffic filter.
- **C. Cloud VPN**: It creates an encrypted tunnel between networks, it doesn't block attack traffic to a public site.
- **D. Security Command Center**: It gives a central view of security risks and findings, but it doesn't filter incoming DDoS traffic.

**Remember:** DDoS or web attacks on a public site → Cloud Armor.

</details>

---

### Exam 4 · Q3

**StreamSure Media, a video streaming company, stores customer profiles, watch history, and billing-related records in Google Cloud. The security team is concerned about a rare situation where someone with malicious intent might physically access Google Cloud infrastructure. How does Google Cloud help protect stored customer data in this situation?**

- A. Data is instantly deleted whenever physical intrusion is detected.
- B. Data is stored on quantum computers using encryption that cannot be broken.
- C. Data is stored using strong encryption mechanisms.
- D. Data is stored in unpredictable global locations so attackers cannot locate it.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Data is stored using strong encryption mechanisms.

**Correct answer: C. Data is stored using strong encryption mechanisms.**

Google Cloud encrypts all customer data at rest by default. If someone physically stole a disk, they would only get encrypted data that is useless without the keys, which are managed separately. This is one layer of Google's defense-in-depth model, alongside strict physical data center security.

**Why the others are wrong:**
- **A. Instantly deleted on intrusion**: Google doesn't wipe customer data when an intrusion is detected; that would destroy customers' data.
- **B. Quantum computers**: Customer data isn't stored on quantum computers, and no encryption is "unbreakable" by marketing claim.
- **D. Unpredictable global locations**: Data stays in the locations the customer chooses; hiding it is not the protection model.

**Remember:** Physical theft of a disk → encryption at rest makes the data unreadable.

</details>

---

### Exam 4 · Q4

**MediVault, a healthcare records platform, is moving encrypted patient files and application data into Google Cloud. The compliance team wants to confirm who retains ownership of the customer data after it is uploaded to Google Cloud. Who owns the data?**

- A. A third party
- B. The customer and Google share ownership
- C. Google
- D. The customer

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. The customer

**Correct answer: D. The customer**

Under Google Cloud's terms, customers own their data. Google only processes it to provide the services the customer asked for, under the customer's instructions. Moving data into the cloud does not transfer ownership.

**Why the others are wrong:**
- **A. A third party**: No third party gains ownership of data just because it is stored in Google Cloud.
- **B. Shared ownership**: Responsibility for security is shared, but ownership of the data is not.
- **C. Google**: Google is the processor of the data, not its owner.

**Remember:** Your data stays yours. Google processes it, never owns it.

</details>

---

### Exam 4 · Q6

**TrailBite, a meal-planning mobile app, stores recipe photos and analytics files in Google Cloud. The company plans to move a portion of this data to another cloud provider for a new reporting workflow. Which statement is true?**

- A. Customer data cannot be transferred out of Google Cloud.
- B. Customers control their own data and can export or transfer it when needed.
- C. Outgoing data transfer must first be activated in the Google Cloud console.
- D. The customer must open a technical support ticket with the appropriate Google Cloud team.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Customers control their own data and can export or transfer it when needed.

**Correct answer: B. Customers control their own data and can export or transfer it when needed.**

Google Cloud's privacy commitments say the customer owns and controls its data. That includes the right to take it out at any time, for example to another provider. Google supports open standards and data portability to avoid vendor lock-in.

**Why the others are wrong:**
- **A. Cannot be transferred out**: Customers can always export their data; lock-in is something Google explicitly says it avoids.
- **C. Must activate outgoing transfer**: There's no special switch to "enable" exports; customers can move data whenever they want, paying normal network charges.
- **D. Open a support ticket**: Customers don't need Google's permission or a ticket to move their own data.

**Remember:** Customer owns the data → customer can move it out anytime.

</details>

---

### Exam 4 · Q12

**PixelHarbor, a photo-sharing startup, stores user albums and profile information in Google Cloud. Its security team wants assurance that customer information stored in the platform is protected and handled according to recognized privacy expectations. How does Google Cloud help ensure customer data remains secure and private when stored?**

- A. By aggregating training data for customers within each industry
- B. By automatically locking files containing suspicious code
- C. By auditing platform privacy practices against industry standards
- D. By providing privacy reviews for critical customer applications

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. By auditing platform privacy practices against industry standards

**Correct answer: C. By auditing platform privacy practices against industry standards**

Google Cloud's privacy controls are checked by independent third-party audits against recognized standards and certifications, such as ISO/IEC 27018 for protecting personal data in the cloud. The audit reports give customers outside evidence that their data is handled as promised. The clue is "recognized privacy expectations".

**Why the others are wrong:**
- **A. Aggregating training data**: Google does not pool customer data by industry; that would break its privacy commitments.
- **B. Locking suspicious files**: This describes malware handling, not how privacy is assured against standards.
- **D. Privacy reviews for customer applications**: Google doesn't review the privacy of each customer's own applications; that is the customer's job.

**Remember:** Proof of privacy and security → independent audits and certifications (ISO, SOC).

**⚠️ Note:** The idea is right (third-party audits against standards such as ISO 27018), but the wording is loose and D can sound plausible. C is still the best option; pick it on this exam.

</details>

---

### Exam 4 · Q18

**TicketNest, an online event booking platform, is moving sensitive customer information such as names, email addresses, booking history, and payment-related records to Google Cloud. The security team wants to know which Google Cloud privacy policy helps protect customer data from being used outside the purpose of providing cloud services. Which policy supports this requirement?**

- A. Google tests the service availability of customer applications.
- B. Google does not use customer data for advertising purposes.
- C. Google migrates customer data to an offline server when a threat is detected.
- D. Google does not allow customers to change encryption keys.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Google does not use customer data for advertising purposes.

**Correct answer: B. Google does not use customer data for advertising purposes.**

Google Cloud commits that it doesn't use customer data for ads. Customer data is processed only to provide the cloud services the customer contracted for. This is the policy that keeps data from being used "outside the purpose of providing cloud services".

**Why the others are wrong:**
- **A. Tests availability of customer applications**: Testing uptime is unrelated to how customer data is used.
- **C. Migrates data to an offline server**: This is not a real Google Cloud policy and has nothing to do with data use.
- **D. Doesn't allow changing encryption keys**: False: customers can manage and rotate their own keys with Cloud KMS.

**Remember:** Google Cloud privacy commitment: your data is not used for ads.

</details>

---

### Exam 4 · Q19

**BrightWave Journal, a digital publishing company, is shutting down its private data center. The company wants its editors, designers, and partners to create, access, and share content through cloud-based services instead of local infrastructure. What should BrightWave Journal consider during this move?**

- A. Built-in security when moving their data to the cloud
- B. Replacing their perimeter security with data encryption keys
- C. Optimizing cost management with a capital expenditure model
- D. Increasing physical hardware capacity when moving their data to the cloud

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Built-in security when moving their data to the cloud

**Correct answer: A. Built-in security when moving their data to the cloud**

Moving to Google Cloud means relying on security that is built into the platform: a secure global infrastructure, encryption by default, and identity-based access. When the company leaves its own data center, these default protections become part of how its content stays safe. The company still configures access and protects its own data.

**Why the others are wrong:**
- **B. Replace perimeter security with keys**: Encryption keys are one control, not a replacement for a full security approach.
- **C. Cost management with CapEx**: Cloud moves spending toward OpEx, not CapEx.
- **D. Increase physical hardware capacity**: In the cloud the provider manages hardware; the company doesn't buy more.

**Remember:** Moving to Google Cloud → you gain built-in, default security layers.

**⚠️ Note:** The keyed wording is vague. It means Google's default protections (encryption, secure infrastructure). The other options are plainly wrong, so pick A on this exam.

</details>

---

### Exam 4 · Q20

**PixelloApps is moving several web servers for its image-sharing platform to Google Cloud by using an infrastructure as a service model. The team wants to understand the shared responsibility model before deploying its virtual machines. In this model, which security responsibility belongs to the cloud provider?**

- A. Defining user permissions for application data
- B. Hardening and patching the guest operating system
- C. Securing the custom application code
- D. Protecting the physical data center facilities

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Protecting the physical data center facilities

**Correct answer: D. Protecting the physical data center facilities**

In the shared responsibility model, Google always secures the physical layer: buildings, hardware and the global network. With IaaS (Compute Engine VMs), the customer keeps more duties than with PaaS or SaaS. The clue is "infrastructure as a service", which leaves only the lowest layers to Google.

**Why the others are wrong:**
- **A. Defining user permissions**: Access to application data is always the customer's job.
- **B. Patching the guest OS**: In IaaS the customer manages and patches the operating system on its VMs.
- **C. Securing custom application code**: The customer owns and secures its own code.

**Remember:** Google always owns physical security. In IaaS, the customer owns the OS and everything above it.

</details>

---

### Exam 4 · Q47

**FinPeak Wallet is moving its payment platform security controls to Google Cloud. The finance team wants to understand how the OpEx model affects cloud security spending. What is one benefit of this model?**

- A. The company does not need to make large upfront capital investments in cloud security.
- B. The company can install and operate custom physical security hardware in Google Cloud data centers.
- C. The company does not need to configure security settings for its cloud resources.
- D. Google Cloud fully guarantees security for every workload.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. The company does not need to make large upfront capital investments in cloud security.

**Correct answer: A. The company does not need to make large upfront capital investments in cloud security.**

With OpEx, security is consumed as a service and paid for as it's used. The company doesn't buy security hardware or build its own facilities upfront. It benefits from Google's investment in secure infrastructure.

**Why the others are wrong:**
- **B. Install custom physical hardware**: Customers can't place their own security hardware in Google's data centers.
- **C. No need to configure security**: Under shared responsibility, customers still configure access and settings.
- **D. Google guarantees all security**: Security is shared; Google doesn't guarantee every workload is secure.

**Remember:** OpEx security = pay as you use, no big upfront investment.

</details>

---

### Exam 5 · Q4

**GreenNest Finance, a small digital banking company, experiences a serious customer data leak only eight months after installing a newer security platform. The leadership team wants to reduce the chance of similar incidents over time and improve its overall security approach. What should GreenNest Finance do to support long-term security?**

- A. Increase data retention periods to at least eight years.
- B. Spend more money to buy the most expensive security platform available.
- C. Hire cybersecurity experts to improve and expand the data security plan.
- D. Wait until a newer and more advanced security platform becomes available.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Hire cybersecurity experts to improve and expand the data security plan.

**Correct answer: C. Hire cybersecurity experts to improve and expand the data security plan.**

A leak soon after buying a new platform shows that tools alone don't create security. Long-term protection needs skilled people who keep improving policies, processes and controls as threats change. The clue is "over time" and "improve its overall security approach".

**Why the others are wrong:**
- **A. Increase data retention**: keeping data longer increases what can leak, it doesn't protect it.
- **B. Buy the most expensive platform**: price doesn't fix gaps in process and expertise, which just failed.
- **D. Wait for a newer platform**: waiting leaves the company exposed and again relies only on tools.

**Remember:** Security is ongoing expertise and process, not a one-time product purchase.

**⚠️ Note:** "Hire cybersecurity experts" is vague. The real lesson is that security needs ongoing expertise and process. It is still clearly the best of the four options, so pick it.

</details>

---

### Exam 5 · Q6

**ClearGate Apps, a multinational SaaS company, is redesigning how employees and partners access its internal systems. The company no longer wants to assume that traffic from an office location or corporate network is automatically trusted. Instead, every identity, endpoint, and application request must be verified, authenticated, and authorized before access is granted, whether the request comes from headquarters, a branch office, or a remote location. Which security model is being described?**

- A. Zero trust architecture
- B. Virtual Private Network (VPN)
- C. Shared Responsibility Model
- D. Capital Expenditure (CapEx) model

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Zero trust architecture

**Correct answer: A. Zero trust architecture**

Zero trust means no request is trusted because of where it comes from. Every user, device and request is verified, authenticated and authorized each time, whether it is from the office or from home. The clue is "no longer wants to assume that traffic from... corporate network is automatically trusted". Google's version of this is BeyondCorp.

**Why the others are wrong:**
- **B. VPN**: a VPN extends the trusted network, which is the perimeter model zero trust replaces.
- **C. Shared Responsibility Model**: it splits security duties between provider and customer, not an access model.
- **D. CapEx model**: it is a spending model, not a security model.

**Remember:** "Never trust, always verify", regardless of location = zero trust.

</details>

---

### Exam 5 · Q7

**MetroLedger, a digital banking platform, recently suffered a security incident that temporarily disrupted a few customer-facing services. The leadership team now wants the company to improve its ability to reduce the chance of future attacks, continue running essential services during an incident, limit business impact, and restore normal operations quickly after disruption. Which concept best describes this capability?**

- A. Data masking
- B. Cyber resilience
- C. Infrastructure as a Service
- D. Vendor lock-in

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Cyber resilience

**Correct answer: B. Cyber resilience**

Cyber resilience is the ability to prevent attacks where possible, keep essential services running during an incident, limit the damage and recover quickly. The stem lists exactly these parts: reduce the chance, continue running, limit impact, restore operations.

**Why the others are wrong:**
- **A. Data masking**: it hides sensitive values in data, a single control, not overall resilience.
- **C. Infrastructure as a Service**: it is a cloud service model, not a security capability.
- **D. Vendor lock-in**: it is a risk of depending on one provider, unrelated to recovering from attacks.

**Remember:** Prevent, withstand, recover = cyber resilience.

</details>

---

### Exam 5 · Q10

**AsterBay Retail, an international ecommerce company, wants its Security Operations team to improve how it detects and investigates advanced attackers. The team needs a Google Cloud security solution that brings together Mandiant frontline incident response knowledge, VirusTotal crowdsourced malware intelligence, Google’s broad visibility, and AI-assisted analysis so analysts can better understand threats and act before attacks cause damage. Which Google Cloud security offering best fits this requirement?**

- A. Google Threat Intelligence
- B. Google Kubernetes Engine (GKE)
- C. Cloud Load Balancing
- D. Identity and Access Management (IAM)

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Google Threat Intelligence

**Correct answer: A. Google Threat Intelligence**

Google Threat Intelligence combines Mandiant's frontline incident response knowledge, VirusTotal's crowdsourced malware data and Google's own visibility, with Gemini-powered analysis. It helps security teams understand who is attacking and act early. The stem names these exact sources, so the match is direct.

**Why the others are wrong:**
- **B. GKE**: it runs containers, it is not a threat intelligence service.
- **C. Cloud Load Balancing**: it distributes traffic across backends.
- **D. IAM**: it controls who can access which resources, not threat research.

**Remember:** Mandiant + VirusTotal + Google visibility = Google Threat Intelligence.

</details>

---

### Exam 5 · Q17

**CarePulse Clinics, a healthcare services company, finds that an attacker has locked access to its appointment records and patient history database by encrypting the files. The attacker sends a message demanding payment in cryptocurrency before providing the decryption key needed to restore the data. What type of cybersecurity threat does this describe?**

- A. Phishing
- B. Ransomware
- C. Cryptomining
- D. Hardware failure

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Ransomware

**Correct answer: B. Ransomware**

Ransomware encrypts a victim's data and demands payment, often in cryptocurrency, for the decryption key. The clues are "encrypting the files" and "demanding payment" to restore access.

**Why the others are wrong:**
- **A. Phishing**: it tricks people into giving away credentials or clicking malicious links. It may deliver ransomware, but it isn't the lockout itself.
- **C. Cryptomining**: attackers secretly use your computing power to mine cryptocurrency; they don't lock your data.
- **D. Hardware failure**: it is an accident, not an attack with a ransom demand.

**Remember:** Data locked + payment demanded = ransomware. Mention of crypto doesn't mean cryptomining.

</details>

---

### Exam 5 · Q19

**BrightCart, a retail mobile app company, stores customer purchase analytics in Google Cloud. The operations manager wants to understand who should decide which employees can access different company datasets and reports. Who is responsible for defining data access policies?**

- A. Cloud Identity
- B. Google Cloud Customer Care team
- C. BrightCart’s IT team
- D. BrightCart’s app users

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. BrightCart’s IT team

**Correct answer: C. BrightCart’s IT team**

Under the shared responsibility model, the customer owns its data and decides who can access it. Google secures the underlying infrastructure, but the customer's IT team defines access policies and grants roles through IAM. The clue is "who should decide which employees can access".

**Why the others are wrong:**
- **A. Cloud Identity**: it is a tool for managing users and groups, not the party who sets policy.
- **B. Google Cloud Customer Care**: support helps with issues but doesn't decide your access rules.
- **D. App users**: end customers don't control internal employee access.

**Remember:** Google secures the cloud; the customer secures data and access in the cloud.

</details>

---

### Exam 5 · Q23

**PixelNest Media stores application files and customer activity records in Google Cloud and also sends data between services for processing. The security team wants to know when Google Cloud automatically encrypts customer data by default. When is data automatically encrypted in Google Cloud?**

- A. When it is in transit only.
- B. When it is at rest and in transit.
- C. Data is not automatically encrypted by default.
- D. When it is at rest only.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. When it is at rest and in transit.

**Correct answer: B. When it is at rest and in transit.**

Google Cloud encrypts all customer data at rest by default, with no action needed. Data moving between Google's facilities and services is also encrypted in transit. The stem mentions both stored files and data "sent between services", which points to both states.

**Why the others are wrong:**
- **A. In transit only**: stored data is also encrypted by default.
- **C. Not encrypted by default**: default encryption is a core Google Cloud security feature.
- **D. At rest only**: data in transit is encrypted as well.

**Remember:** Google Cloud default = encrypted at rest and in transit.

</details>

---

### Exam 5 · Q24

**TrailBee Travel uses Google Cloud to host its booking platform. Before a user can open the internal support dashboard, the platform must confirm that the person signing in is really the claimed user. Which aspect of cloud identity management does this action describe?**

- A. Authorization
- B. Authentication
- C. Auditing
- D. Encrypting

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Authentication

**Correct answer: B. Authentication**

Authentication confirms that users are who they claim to be, for example with a password plus 2-step verification. The clue is "confirm that the person signing in is really the claimed user".

**Why the others are wrong:**
- **A. Authorization**: it decides what an authenticated user is allowed to do, which comes after identity is confirmed.
- **C. Auditing**: it records who did what, for later review.
- **D. Encrypting**: it protects data from being read, it doesn't verify identity.

**Remember:** Authentication = who are you? Authorization = what can you do?

</details>

---

### Exam 5 · Q30

**ClearPath Analytics stores customer reports and transaction files in Google Cloud. The security team asks why stored data in Google Cloud is protected without every application team manually enabling encryption for each service. What is the main reason?**

- A. Data is encrypted by Security Command Center
- B. Data is encrypted by Sensitive Data Protection
- C. Data is encrypted by default
- D. Data is encrypted when an appropriate tag is applied

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Data is encrypted by default

**Correct answer: C. Data is encrypted by default**

Google Cloud automatically encrypts all customer data at rest, with no setup by application teams. That is why stored data is protected without anyone turning encryption on per service. The clue is "without every application team manually enabling encryption".

**Why the others are wrong:**
- **A. Security Command Center**: it finds misconfigurations and threats, it doesn't encrypt data.
- **B. Sensitive Data Protection**: it discovers, classifies and masks sensitive data, it isn't the default encryption layer.
- **D. When a tag is applied**: encryption doesn't depend on tags; it is always on.

**Remember:** Google Cloud encryption at rest = automatic, on by default.

</details>

---

### Exam 5 · Q50

**FinBridgeIQ, a fintech website, uses an internal LLM-based assistant to help employees search payment reports and customer billing summaries. Security teams discover that an attacker could submit cleverly written prompts that cause the assistant to ignore its original instructions, reveal restricted financial records, or bypass built-in response controls. Which modern cybersecurity threat best describes this risk?**

- A. Cryptomining
- B. Distributed Denial-of-Service (DDoS)
- C. LLM attack (prompt injection)
- D. Ransomware

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. LLM attack (prompt injection)

**Correct answer: C. LLM attack (prompt injection)**

Prompt injection is when an attacker writes inputs that trick a large language model into ignoring its instructions, revealing restricted data or bypassing its safety controls. The stem describes exactly that: "cleverly written prompts" that make the assistant "ignore its original instructions".

**Why the others are wrong:**
- **A. Cryptomining**: attackers secretly use your compute to mine cryptocurrency.
- **B. DDoS**: it floods a service with traffic to make it unavailable.
- **D. Ransomware**: it encrypts data and demands payment.

**Remember:** Malicious prompts that hijack an AI model = prompt injection.

</details>

---

### Exam 6 · Q22

**ShieldWorks Labs, a healthcare software company, is configuring access to its Google Cloud resources. The security team wants each employee to receive only the specific permissions needed for their role, such as viewing logs, managing billing, or deploying applications, and nothing beyond those job responsibilities. Which security principle describes this approach?**

- A. Cyber resilience
- B. Zero-trust
- C. Least privilege
- D. Security by default

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Least privilege

**Correct answer: C. Least privilege**

The principle of least privilege means giving each user only the permissions they need to do their job, and nothing more. This limits damage from mistakes or compromised accounts. The clue is "only the specific permissions needed for their role... and nothing beyond." In Google Cloud, this is applied with IAM roles.

**Why the others are wrong:**
- **A. Cyber resilience**: This is the ability to withstand and recover from attacks, not a rule for assigning permissions.
- **B. Zero-trust**: Zero trust means verifying every request and trusting no network by default. It is related but broader than limiting permissions.
- **D. Security by default**: This means systems ship with secure settings already turned on.

**Remember:** Only what the job needs → least privilege.

</details>

---

### Exam 6 · Q23

**GlowCart, an ecommerce mobile app, is worried that its order database and application files could be lost or corrupted because of a storage device failure or a ransomware attack. The operations team wants a way to return the environment to an earlier known-good state after such an incident. What should GlowCart do?**

- A. Define service level objectives (SLOs).
- B. Use Cloud Monitoring.
- C. Back up data regularly.
- D. Enable autoscaling.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Back up data regularly.

**Correct answer: C. Back up data regularly.**

Backups are copies of data saved at points in time. If storage fails or ransomware encrypts or corrupts files, the team can restore from a backup to an earlier known-good state. The clue is "return the environment to an earlier known-good state."

**Why the others are wrong:**
- **A. Define SLOs**: Service level objectives set reliability targets but do not protect or restore data.
- **B. Use Cloud Monitoring**: Monitoring can alert you to a problem but cannot restore lost or corrupted data.
- **D. Enable autoscaling**: Autoscaling adjusts capacity to traffic. It does nothing for data loss.

**Remember:** Need to restore after loss or ransomware → backups.

</details>

---

### Exam 6 · Q25

**ClearFunds, a digital payments company, runs all of its applications and databases on Google Cloud. The security team wants to be ready in case sensitive customer data is exposed or accessed without authorization. What should the company do to prepare for this type of event?**

- A. Reduce the use of multi-factor authentication
- B. Assume data security is fully Google’s responsibility, so very little preparation is needed
- C. Create an incident response plan to reduce the impact
- D. Improve physical perimeter security around its own data center

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Create an incident response plan to reduce the impact

**Correct answer: C. Create an incident response plan to reduce the impact**

An incident response plan defines in advance who does what when a security event happens: how to detect, contain, investigate, communicate, and recover. Having it ready reduces damage and recovery time. The clue is "be ready in case sensitive customer data is exposed."

**Why the others are wrong:**
- **A. Reduce MFA use**: Multi-factor authentication protects accounts. Reducing it increases risk.
- **B. Assume security is fully Google's responsibility**: Under the shared responsibility model, the customer still owns its data, access controls, and response.
- **D. Improve physical security of its own data center**: ClearFunds runs everything on Google Cloud, and Google secures the physical data centers.

**Remember:** Restore data → backups. Prepare for a breach → incident response plan.

</details>

---

### Exam 6 · Q27

**CareLoop Wellness, a healthcare appointment mobile app, is moving patient scheduling and profile data to Google Cloud. The team wants to understand what privacy means when users’ personal information is stored, accessed, and shared through cloud services. How is privacy defined in the context of cloud technology?**

- A. Restrictions on data access and sharing
- B. Processes used to verify a user’s identity
- C. Exposure to data breaches and cyber attacks
- D. Meeting required regulatory and industry standards

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Restrictions on data access and sharing

**Correct answer: A. Restrictions on data access and sharing**

In cloud technology, privacy is about controlling who can access personal data and how it is used and shared. It gives individuals and organizations control over their information. The clue is "personal information is stored, accessed, and shared."

**Why the others are wrong:**
- **B. Processes to verify identity**: That is authentication, one security control, not the definition of privacy.
- **C. Exposure to breaches and attacks**: This describes security risk or threats, not privacy itself.
- **D. Meeting regulatory and industry standards**: That is compliance. Compliance can support privacy, but it is a different concept.

**Remember:** Privacy = limits on access and sharing. Authentication = verifying identity. Compliance = meeting standards.

</details>

---

### Exam 6 · Q38

**MedLedger, a healthcare records platform, needs to verify that its cloud service provider has ISO 27001 certification before storing sensitive customer data. The compliance team also needs access to audit reports, certificates, and supporting compliance documents. Which Google Cloud tool should MedLedger use?**

- A. Compliance Reports Manager
- B. Security Command Center
- C. Network Intelligence Center
- D. Cloud Monitoring

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Compliance Reports Manager

**Correct answer: A. Compliance Reports Manager**

Compliance Reports Manager gives customers self-service access to Google Cloud's compliance documents, such as ISO 27001 certificates, SOC reports, and audit reports. Compliance teams use it to verify the provider's certifications. The clues are "ISO 27001 certification" and "audit reports, certificates, and supporting compliance documents."

**Why the others are wrong:**
- **B. Security Command Center**: It finds security risks and misconfigurations in your own cloud resources. It does not provide Google's certificates.
- **C. Network Intelligence Center**: It monitors and troubleshoots network performance and connectivity.
- **D. Cloud Monitoring**: It tracks metrics, uptime, and alerts for applications and infrastructure.

**Remember:** Need Google's certificates and audit reports → Compliance Reports Manager.

</details>

---

### Exam 6 · Q42

**FitCart, a retail mobile app company, has moved its order processing, analytics, and customer-facing services from its own server room to Google Cloud. During a quarterly security review, the security lead wants to confirm who is responsible for protecting the physical buildings, hardware, and facilities where the cloud resources run. Who is responsible for securing the physical infrastructure of the data centers?**

- A. FitCart and Google Cloud
- B. External managed security service providers
- C. Google Cloud
- D. FitCart

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Google Cloud

**Correct answer: C. Google Cloud**

Under the shared responsibility model, the cloud provider always secures the physical layer: data center buildings, hardware, power, and facilities. This is true for IaaS, PaaS, and SaaS alike. The customer is responsible for things like its data, access settings, and how it configures services. The clue is "physical buildings, hardware, and facilities."

**Why the others are wrong:**
- **A. FitCart and Google Cloud**: Many layers are shared, but physical data center security is not. FitCart has no access to Google's buildings.
- **B. External managed security providers**: Third parties may help with the customer's side, but they do not secure Google's data centers.
- **D. FitCart**: FitCart left its own server room. It no longer owns the physical infrastructure.

**Remember:** Physical data center security → Google alone, in every service model.

</details>

---

### Exam 6 · Q49

**NovaRetail Bank is expanding its cloud adoption from a small project-by-project approach to a broader business transformation approach. The security team wants to modernize access control and protect users, applications, and data across different environments. How should NovaRetail Bank change its cloud security?**

- A. Provide employee identities using only Google Cloud authentication.
- B. Adopt a zero-trust model that verifies users, devices and applications.
- C. Focus on strong perimeter security and trust resources inside the private network.
- D. Focus mainly on three Identity and Access Management IAM basic roles: owner, editor, and viewer.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Adopt a zero-trust model that verifies users, devices and applications.

**Correct answer: B. Adopt a zero-trust model that verifies users, devices and applications.**

Zero trust means no user or device is trusted just because it is inside the corporate network. Every request is checked based on identity, device and context, wherever it comes from. This fits a bank that wants to protect users, apps and data "across different environments" as it moves beyond a project-by-project approach. The clue is "modernize access control".

**Why the others are wrong:**
- **A. Only Google Cloud authentication**: Limiting identity to one method doesn't modernize the security model and may not cover every environment.
- **C. Strong perimeter, trust the inside**: This is the old castle-and-moat model that zero trust replaces.
- **D. Mainly the three basic roles**: Owner, editor and viewer are too broad and go against least privilege.

**Remember:** Verify every request from anywhere → zero trust.

</details>

---
