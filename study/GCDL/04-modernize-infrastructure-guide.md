# Domain 4 Study Guide — Modernize Infrastructure and Applications with Google Cloud

> Condensed from the 59-question bank in [`04-modernize-infrastructure.md`](04-modernize-infrastructure.md). Citations look like (Exam N · QM). The source dumps have no explanations, so the reasoning here is ours. Many scenarios repeat across exams (Cloud Run functions for events, GKE Enterprise for multi-environment Kubernetes, APIs for legacy and partner data), so look for paired citations. Items marked "see ⚠️" have a shaky key, discussed at the end.

---

## 1. Why modernize: agility, faster releases and managed services

### Key facts
- **The business driver is speed.** Legacy data-center apps that take **weeks to update and release** lose customers who expect frequent features and quick fixes. That pain is what pushes a company toward cloud-based architecture (Exam 5 · Q45).
- **Modernizing on Google Cloud lets you release updates more quickly**, including bug fixes, which is how it helps meet user expectations (Exam 1 · Q23).
- **Cloud-native apps** let developers **release new features in an agile way**. That is the reason to build cloud-native rather than only move an old app when requirements change often, for example per-user, per-season personalization (Exam 4 · Q36).
- **Managed services** mean Google Cloud takes over routine administration: OS patching, component upgrades, setting up database servers. Developers spend that time on features instead (Exam 2 · Q24).
- The task a managed platform typically handles **automatically** is **patching and upgrades**. Managing user access, deciding what to archive and optimizing cost remain your job (Exam 2 · Q31).
- Cloud shifts spending from **CapEx to OpEx (pay-as-you-go)**, not the other way round (Exam 5 · Q45), (Exam 4 · Q36).

### Decision rules
- "Takes weeks to release", "can't keep up with feature requests": the motive is **agility / faster release cycles** (Exam 5 · Q45), (Exam 1 · Q23).
- "IT team spends its week patching and setting up servers": the answer is **adopting managed services** (Exam 2 · Q24), (Exam 2 · Q31).
- "Why build cloud-native?": **agile feature releases**, not "the provider writes code for you" (Exam 4 · Q36).

### Traps
- "Toil automation helps perform automatic updates" and "DevOps requires market trends to be measured" sound like SRE/DevOps vocabulary but don't answer the question (Exam 1 · Q23).
- "Personalized content from customer data" is an AI/data benefit, not a modernization benefit (Exam 1 · Q23).
- Options that say code "changes by itself", the provider "writes all source code" or that you can "speed up capital expenditure planning" are always wrong (Exam 5 · Q45), (Exam 4 · Q36).
- Managed services do **not** take over **user access management**. Under shared responsibility, IAM decisions stay with the customer (Exam 2 · Q31).

---

## 2. Virtualization, virtual machines and Compute Engine

### Key facts
- A **hypervisor** is the software layer that lets **several operating systems** (for example Linux and Windows) run on **one physical machine**, each in its own virtual machine (Exam 4 · Q15).
- **Virtual machines** each have their **own dedicated OS**. If apps can't share an OS environment, they need VMs, not containers (Exam 6 · Q6).
- **Compute Engine** is Google Cloud's IaaS VM service. Choose it when you need **detailed control** over the VM, OS configuration, networking and machine types. It still supports **autoscaling and automatic rolling updates** through managed instance groups (Exam 3 · Q37).
- **Spot VMs** (successor to **Preemptible VMs**) use spare capacity at a deep discount. Google can **stop them when it needs the capacity back**. They fit batch jobs that **checkpoint, can restart and aren't urgent** (Exam 2 · Q45), (Exam 4 · Q34).
- Pricing options on Compute Engine beyond on-demand: **sustained-use discounts** (automatic for long-running VMs) and **committed-use discounts** (1- or 3-year commitment) *(not in the question bank)*.

### Compute Engine options compared

| Need | Choice | Source |
|---|---|---|
| Full control of OS, network, machine type | ✅ Compute Engine (standard or custom VM) | (Exam 3 · Q37) |
| Each app needs its own OS | ✅ Virtual machines | (Exam 6 · Q6) |
| Cheapest for fault-tolerant, restartable, non-urgent batch | ✅ Spot VMs / Preemptible VMs | (Exam 2 · Q45), (Exam 4 · Q34) |
| Same batch job on standard or custom pay-as-you-go VM | ❌ Works but costs more | (Exam 4 · Q34) |
| Same batch job on Cloud Run functions | ❌ Meant for short event-driven code, not long nightly jobs | (Exam 2 · Q45), (Exam 4 · Q34) |

### Decision rules
- "Run multiple operating systems on one physical server": **hypervisor** (Exam 4 · Q15).
- "Dedicated OS per application" or "cannot share an OS": **virtual machines** (Exam 6 · Q6).
- "Detailed control over VMs, OS and machine types": **Compute Engine** (Exam 3 · Q37).
- "Can be interrupted", "restarts from checkpoints", "cheapest": **Spot VMs** (Exam 2 · Q45), (Exam 4 · Q34).

### Traps
- **Containers share the host OS kernel**, so they don't give each app its own OS (Exam 6 · Q6), (Exam 4 · Q15).
- Cloud Build is a CI/CD build service, not somewhere to run an app. App Engine and Cloud Run hide the VM, so they fail a "detailed VM control" requirement (Exam 3 · Q37).
- "Premium tier virtual machines" isn't a real cost-saving option (Exam 2 · Q45).

---

## 3. Containers, microservices and Google Kubernetes Engine

### Key facts
- **Containerization** bundles application code **with its dependencies** (runtime libraries, package versions), so it behaves the same on a laptop, in test and in production. It fixes "works on my machine" (Exam 5 · Q40).
- Containers are lighter than VMs because they **share the host OS kernel**. They start fast and pack densely.
- **Microservices** split a large app into **small independent services**, each owning one business function, each built, deployed and scaled separately. The opposite is a **monolith** (Exam 2 · Q26).
- Breaking a monolith into microservices (refactoring) makes the app **more efficient and scalable**. It needs code changes and is not the quickest route to the cloud (Exam 2 · Q37).
- **Google Kubernetes Engine (GKE)** is Google's managed **Kubernetes** service for **orchestrating containers**: deploying, scaling and operating many of them, up to thousands (Exam 5 · Q43).
- The exam's stock phrasing of GKE's benefit: it **enables rapid application deployment and testing** and **shortens the time to test and refine fixes** (Exam 1 · Q15), (Exam 3 · Q12).
- **GKE Autopilot** goes further: Google manages **nodes, scaling and cluster operations**, so the team focuses on apps. **GKE Standard** leaves node configuration to you (Exam 2 · Q43).

### GKE modes compared

| | GKE Standard | GKE Autopilot |
|---|---|---|
| Who manages nodes | You | Google |
| Billing | Per node (VM) | Per Pod resource request |
| Pick when | You need node-level control | "Reduce time spent configuring nodes and cluster operations" (Exam 2 · Q43) |

### Decision rules
- "Same code breaks in production because of different libraries": **containerization** (Exam 5 · Q40).
- "Split into independent services, deployed and scaled separately": **microservices** (Exam 2 · Q26).
- "Run and coordinate thousands of containers", "orchestrate containers": **GKE** (Exam 5 · Q43), (Exam 1 · Q15).
- "Kubernetes, but less cluster admin": **GKE Autopilot** (Exam 2 · Q43).
- "Why GKE?": **rapid deployment and testing / faster test-and-refine cycles** (Exam 1 · Q15), (Exam 3 · Q12).

### Traps
- GKE does **not** remove the need to package apps in containers, and it doesn't suggest code redesigns or copy source code between servers (Exam 3 · Q12).
- GKE doesn't "provide pre-written source code", "optimize VM performance" or "connect legacy systems" (that's an API job) (Exam 1 · Q15).
- **Cloud Run** also runs containers and is less work, but it's not Kubernetes. When the stem says "Kubernetes" or "thousands of containers to orchestrate", stay with GKE (Exam 2 · Q43), (Exam 5 · Q43).
- Spot VMs and load balancing don't solve dependency drift (Exam 5 · Q40).

---

## 4. Serverless: Cloud Run, Cloud Run functions and App Engine

### Key facts
- **Serverless computing** means you write code and Google Cloud handles **server provisioning, scaling, patching and runtime infrastructure** (Exam 2 · Q9).
- The headline serverless benefit is **scalability**: it scales from a few users to tens of thousands and **down to zero**, so you don't pay for idle capacity (Exam 2 · Q16).
- **Cloud Run** runs **container images** serverlessly: autoscaling, **scale to zero**, no clusters or servers to manage, any language or tool you can put in a container (Exam 1 · Q47), (Exam 5 · Q12), (Exam 5 · Q35).
- **Cloud Run functions** (formerly Cloud Functions) run **small pieces of code in response to events**: a form submission, a file upload to Cloud Storage, a price crossing a threshold, an event from another service (Exam 1 · Q16), (Exam 2 · Q18), (Exam 6 · Q31).
- **App Engine** is Google's original PaaS for **web apps**. You deploy code, it handles the infrastructure and **scales automatically** (Exam 2 · Q50).
- App Engine **versions and traffic splitting** let you run **different versions for different users**, for example to A/B test a redesigned home page before full release (Exam 2 · Q32).

### Serverless options compared

| Clue in the stem | Choice | Source |
|---|---|---|
| "Packaged as a container image", "scale to zero", "no clusters" | ✅ Cloud Run | (Exam 1 · Q47), (Exam 5 · Q12) |
| "Preferred languages and tools" + "less server management" | ✅ Cloud Run | (Exam 5 · Q35) |
| "Small piece of code" + "whenever X happens" (upload, form, event) | ✅ Cloud Run functions | (Exam 1 · Q16), (Exam 2 · Q18), (Exam 6 · Q31) |
| "Write the function code, Google handles servers" (generic) | ✅ Serverless computing | (Exam 2 · Q9) |
| Web app, auto-scaling, focus on code | ✅ App Engine | (Exam 2 · Q50) |
| Different app versions for different users | ✅ App Engine traffic splitting | (Exam 2 · Q32) |
| Need VM/OS control | ❌ Serverless. Use Compute Engine | (Exam 3 · Q37) |

### Decision rules
- Event-driven + small code + no servers: **Cloud Run functions** (Exam 1 · Q16), (Exam 2 · Q18), (Exam 6 · Q31).
- One container + serverless + autoscaling: **Cloud Run** (Exam 1 · Q47), (Exam 5 · Q12).
- Unpredictable launch traffic + don't pay when idle: **scalability** benefit of serverless (Exam 2 · Q16).
- A/B or canary of an app version for a subset of users: **App Engine** versions (Exam 2 · Q32).

### Traps
- **App Engine is a valid distractor for Cloud Run** questions. When the stem says "packaged as one container image", pick Cloud Run (Exam 1 · Q47).
- App Engine traffic splitting serves **different versions to different users**, not different versions to the same user (Exam 2 · Q32).
- Artifact Registry stores images. It doesn't run them (Exam 2 · Q9).
- Managed Service for Apache Spark (formerly Dataproc) and Pub/Sub are data services, not app hosting (Exam 5 · Q35).
- AlloyDB Omni is a database. Bare Metal Solution is the opposite of serverless (Exam 5 · Q12), (Exam 1 · Q16).
- Disaster recovery and built-in security are real cloud benefits, but they don't answer "unknown traffic, no idle cost" (Exam 2 · Q16).

---

## 5. Migration paths: rehost, replatform, refactor, reimagine

### Key facts
- **Rehost (lift and shift):** move the app as-is, **no code changes, no redesign**. Same OS images, settings and configs, only the minimum changes to run on Compute Engine. Fastest path, typical when a data-center contract is ending (Exam 1 · Q5), (Exam 5 · Q13).
- **Replatform (move and improve):** keep the app logic mostly unchanged but swap a component for a managed one, for example a self-managed database for **Cloud SQL** (Exam 2 · Q34).
- **Refactor:** change the code, often splitting a monolith into microservices. Result: **more efficient and scalable**, but slower and more work (Exam 2 · Q37).
- **Reimagine / rebuild:** design a new cloud-native app from scratch.
- Google also frames modernization as **"invent in greenfield"** and **"invent in brownfield"**:
  - **Greenfield**: no existing app. You build everything new on Google Cloud (Exam 3 · Q44).
  - **Brownfield**: you build a **new cloud-native app that will replace an existing legacy system** (Exam 3 · Q30).
- While building cloud-native apps, companies also **move selected legacy workloads to the cloud**. Modernization runs in parallel with migration, not instead of it (Exam 5 · Q33).
- **Retain** (leave on-premises for now) and **retire** (switch off) are the other "R" options in a migration plan *(not in the question bank)*.
- Google's migration tooling: **Migration Center** for discovery and TCO assessment, **Migrate to Virtual Machines** for moving VMs into Compute Engine, **Migrate to Containers** for turning VMs into containers *(not in the question bank)*.

### Migration strategies compared

| Strategy | Code changes | Speed | Example | Source |
|---|---|---|---|---|
| Rehost (lift and shift) | None | Fastest | Copy VMs to Compute Engine unchanged | (Exam 1 · Q5), (Exam 5 · Q13) |
| Replatform (move and improve) | Small | Fast | Self-managed DB → Cloud SQL | (Exam 2 · Q34) |
| Refactor | Significant | Slower | Monolith → microservices | (Exam 2 · Q37) |
| Invent in greenfield | New app | Depends | No existing app to move | (Exam 3 · Q44) |
| Invent in brownfield | New app, replaces old | Depends | Cloud-native replacement for on-prem claims system | (Exam 3 · Q30) |

### Decision rules
- "No changes to code or architecture" / "same images and configs": **rehost** (Exam 1 · Q5), (Exam 5 · Q13).
- "Replace one self-managed layer with a managed service, logic unchanged": **replatform** (Exam 2 · Q34).
- "Benefit of refactoring into microservices": **more efficient and scalable** (Exam 2 · Q37).
- "No existing application": **greenfield**. "New app that will replace an existing one": **brownfield** (Exam 3 · Q44), (Exam 3 · Q30).

### Traps
- Refactoring is **not** the quickest path and does **not** avoid code changes. No migration makes an app "automatically PCI-DSS compliant" (Exam 2 · Q37).
- "Move then change" and "change then move" describe rehost-then-modernize and modernize-then-rehost. They aren't the answer when the stem stresses building a **new** app (Exam 3 · Q30), (Exam 3 · Q44).
- Rehost vs replatform: if **anything** is swapped for a managed service, it's no longer pure lift and shift (Exam 2 · Q34).

---

## 6. Specialized migration targets: VMware, bare metal and databases

### Key facts
- **Google Cloud VMware Engine** runs your **VMware stack natively** on Google Cloud. Admins keep using **familiar VMware tools and procedures**. It's the low-change path for a large VMware estate (Exam 2 · Q47).
- **Bare Metal Solution** gives dedicated physical servers in Google-run facilities, close to Google Cloud. Use it for workloads with **strict third-party licensing**, **low-level server access** or architectures that **can't be virtualized** (classic case: Oracle databases) (Exam 1 · Q42).
- **Database Migration Service** moves databases (including **SQL Server**, MySQL and PostgreSQL) into **Cloud SQL** with minimal downtime. It's the fast way to get a **managed** database **without changing database engine** (Exam 4 · Q38).

### Decision rules
- "VMware estate, keep VMware tools": **Google Cloud VMware Engine** (Exam 2 · Q47).
- "Licensing terms, low-level/hardware access, can't run on VMs": **Bare Metal Solution** (Exam 1 · Q42).
- "Move quickly to a managed service, keep SQL Server": **Database Migration Service → Cloud SQL** (Exam 4 · Q38).

### Traps
- **VMware vSphere** is VMware's own product, not a Google Cloud service. Compute Engine would mean converting the VMs (Exam 2 · Q47).
- Compute Engine and serverless options fail the "low-level server access + licensing" requirement (Exam 1 · Q42).
- Moving SQL Server data to **Firestore** (redesign), **BigQuery** (analytics warehouse) or **Cloud Storage** exports doesn't keep the SQL Server approach (Exam 4 · Q38).

---

## 7. Hybrid cloud, multicloud, GKE Enterprise and open standards

### Key facts
- **Hybrid cloud** = on-premises (or private cloud) **plus** a public cloud. Typical reasons: some data must stay in your data center by regulation or choice, while you still use Google Cloud services such as BigQuery or ML (Exam 6 · Q12), (Exam 6 · Q44).
- **Multicloud** = **more than one public cloud provider**, for example running Kubernetes apps across three clouds for more locations (Exam 4 · Q5).
- **GKE Enterprise** (formerly Anthos) is Google's platform for managing **Kubernetes clusters consistently across Google Cloud, on-premises and other public clouds**: one control point, consistent security policies, modernizing old apps and building new container services (Exam 1 · Q24), (Exam 2 · Q20), (Exam 3 · Q31), (Exam 5 · Q25).
- **Openness and interoperability** guide strategy when leaders fear **vendor lock-in** and want freedom to run across public, private and on-prem environments (Exam 5 · Q18).
- **Open standards** reduce the risk that one provider makes future migration hard (Exam 6 · Q21).
- **Open source** = source code is public, so anyone can study, change and contribute to it. Kubernetes is Google's best-known open-source contribution (Exam 5 · Q44).
- **BigQuery Omni** lets BigQuery query data stored in other clouds (AWS, Azure) without moving it. It is analytics, not workload management (Exam 2 · Q20).
- **Google Distributed Cloud** extends Google Cloud infrastructure to edge locations and customer data centers, including air-gapped options for strict sovereignty needs *(not in the question bank)*.

### Environment types compared

| Environment | What it is | Exam clue | Source |
|---|---|---|---|
| Hybrid cloud | On-prem + public cloud | "Keep part of data in our data center", "regulation requires on-prem" | (Exam 6 · Q12), (Exam 6 · Q44) |
| Multicloud | 2+ public clouds | "Three public cloud providers" | (Exam 4 · Q5) |
| Private cloud | Cloud-style infra dedicated to one org | Rarely the answer when Google services must be used | (Exam 6 · Q44) |
| Public cloud only | Everything in one provider | Fails "data must stay on-prem" | (Exam 6 · Q44) |

### Decision rules
- Kubernetes across **Google Cloud + on-prem and/or another cloud**, one management plane: **GKE Enterprise** (Exam 1 · Q24), (Exam 2 · Q20), (Exam 3 · Q31), (Exam 5 · Q25).
- Use Google Cloud services but **keep data on-prem**: **hybrid** (Exam 6 · Q12), (Exam 6 · Q44).
- Several **public** clouds: **multicloud** (Exam 4 · Q5).
- "Worried about lock-in": **openness, interoperability, open standards** (Exam 5 · Q18), (Exam 6 · Q21).
- "Source code public, anyone can contribute": **open source** (Exam 5 · Q44).
- Data spread across Google Cloud and other public cloud providers, brought together for analysis: **multicloud** (Exam 6 · Q48).

### Traps
- A stem can mention **GKE Enterprise** and still ask for the deployment type. Three public clouds = **multicloud**, not hybrid (Exam 4 · Q5).
- **Apigee hybrid** manages APIs across environments, not Kubernetes workloads (Exam 1 · Q24).
- Cloud Run, Cloud Run functions, App Engine and Compute Engine run only in Google Cloud, so none is a cross-environment management answer (Exam 3 · Q31), (Exam 5 · Q25).
- Proprietary databases, single private cloud or "SaaS only" increase dependence rather than reduce it (Exam 5 · Q18). SLAs and scalable infrastructure don't address portability (Exam 6 · Q21).
- PaaS and "closed standard" are distractors for open source (Exam 5 · Q44).

---

## 8. APIs and Apigee: unlocking legacy systems and partner value

### Key facts
- An **API (application programming interface)** is a **defined set of rules and methods that lets software applications communicate** with each other through requests and responses (Exam 2 · Q42).
- **Unlock legacy systems without replacing them.** An API in front of an old system exposes selected data to modern apps and partners, so you **don't have to rewrite the legacy platform** (Exam 1 · Q18), (Exam 4 · Q8).
- APIs make existing capabilities **reusable** across mobile apps, portals and cloud services, which gives **long-term operational flexibility** (Exam 1 · Q21).
- APIs **connect systems programmatically**, so data stays current: live store inventory on a website, live product availability in a partner app, loyalty points across partner locations (Exam 4 · Q11), (Exam 1 · Q9), (Exam 5 · Q3).
- APIs **create new business value and revenue**: a **paid API** to monetize data, content shared with partner sites, a booking system connected to a catering partner's order form (Exam 5 · Q2), (Exam 5 · Q38), (Exam 5 · Q42).
- **Apigee** is Google Cloud's **API management** platform. It helps **expose, secure, manage and reuse** APIs, and adds **traffic analytics, access control, security policies and monetization (pricing plans)** for external developers (Exam 2 · Q2), (Exam 5 · Q47).

### API benefit patterns

| Scenario | API value | Source |
|---|---|---|
| Legacy core system, no budget to modernize, partner needs data | Expose selected data securely | (Exam 1 · Q18) |
| Old reservation platform, new mobile app | No rewrite of the legacy platform | (Exam 4 · Q8) |
| Website shows stale inventory | Programmatic, live connection | (Exam 4 · Q11) |
| Real-time availability in, orders out to partner stores | Two-way exchange between systems | (Exam 1 · Q9) |
| Loyalty points across partners | Keep details current across systems | (Exam 5 · Q3) |
| Valuable data, new income stream | Paid API | (Exam 5 · Q2) |
| Share content with partner sites | API | (Exam 5 · Q38) |
| Booking + catering partner | Connect the two systems | (Exam 5 · Q42) |
| Reuse old capabilities everywhere | Long-term operational flexibility | (Exam 1 · Q21) |
| Track traffic, secure, charge developers | Apigee API Management | (Exam 5 · Q47), (Exam 2 · Q2) |

### Decision rules
- "Systems need to exchange data", "partners", "legacy system + modern app": **API** (Exam 1 · Q9), (Exam 1 · Q18), (Exam 5 · Q38).
- "Manage, secure, analyze, monetize APIs": **Apigee** (Exam 2 · Q2), (Exam 5 · Q47).
- When asked *how* an API creates value, pick the option that **connects specific systems** over vague "discover opportunities" or ML options (Exam 5 · Q42), (Exam 5 · Q3).

### Traps
- APIs expose **selected** capabilities under control. "Reveal every backend record so partners can change it directly" or "add partner users directly to the database" is wrong (Exam 1 · Q21), (Exam 5 · Q2).
- An API doesn't fix the legacy system's stability, retire it immediately, convert it to cloud-native or build the mobile app for you (Exam 4 · Q8), (Exam 4 · Q11).
- "Manually connecting each source one at a time" is the opposite of an API (Exam 4 · Q11).
- Personalized offers, charts and ML demand forecasts are AI/analytics answers (Exam 5 · Q3), (Exam 5 · Q42), (Exam 4 · Q11).
- Pay-as-you-go is a cloud benefit, not an API benefit (Exam 1 · Q21).
- AppSheet is no-code app building, and "App Engine flexible" is hosting. Neither manages APIs (Exam 2 · Q2). Config Sync and NoSQL databases don't share content with partners (Exam 5 · Q38).
- SRE, custom ML and multi-regional databases don't connect apps to stores (Exam 1 · Q9).

---

## ⚠️ Questionable answers

| Item | Issue |
|---|---|
| **(Exam 1 · Q15)**, **(Exam 3 · Q12)** | Correct but vague. "Rapid deployment and testing" and "shortens the time to test and refine fixes" are generic benefits of containers and CI/CD, not things GKE uniquely provides. They are keyed because every other option is clearly false. |
| **(Exam 2 · Q16)** | "Scalability" is keyed, but "avoid paying when no users are active" is really a cost (pay-per-use, scale-to-zero) benefit. Scalability is still the best of the four options. |
| **(Exam 2 · Q50)** | App Engine is right among the options, but for a new web app today Google usually steers toward **Cloud Run**. Option "Anthos" is the old name of GKE Enterprise. |

---

## Last-minute cheat sheet

- Legacy apps take weeks to release → modernize for **agility and faster updates** (Exam 5 · Q45), (Exam 1 · Q23), (Exam 4 · Q36).
- Managed services take over **patching and upgrades**, not user access (Exam 2 · Q24), (Exam 2 · Q31).
- **Hypervisor** = many OSes on one server. **VMs** = dedicated OS per app (Exam 4 · Q15), (Exam 6 · Q6).
- Need full VM/OS/network control → **Compute Engine** (Exam 3 · Q37).
- Restartable, non-urgent, cheapest → **Spot VMs** (Exam 2 · Q45), (Exam 4 · Q34).
- Code + dependencies bundled for consistency → **containers** (Exam 5 · Q40).
- Independent services, deployed separately → **microservices** (Exam 2 · Q26), (Exam 2 · Q37).
- Orchestrate many containers → **GKE**. Less cluster admin → **GKE Autopilot** (Exam 5 · Q43), (Exam 1 · Q15), (Exam 3 · Q12), (Exam 2 · Q43).
- One container, serverless, scale to zero → **Cloud Run** (Exam 1 · Q47), (Exam 5 · Q12), (Exam 5 · Q35).
- Small code triggered by events → **Cloud Run functions** (Exam 1 · Q16), (Exam 2 · Q18), (Exam 6 · Q31).
- Serverless = Google runs the servers. Key benefit = **scalability** (Exam 2 · Q9), (Exam 2 · Q16).
- **App Engine**: web apps that autoscale, versions for **different users** (Exam 2 · Q50), (Exam 2 · Q32).
- No changes → **rehost**. Swap in Cloud SQL → **replatform**. Microservices → **refactor** (Exam 1 · Q5), (Exam 5 · Q13), (Exam 2 · Q34), (Exam 2 · Q37).
- No existing app → **greenfield**. New app replacing old → **brownfield**. Also move selected legacy workloads (Exam 3 · Q44), (Exam 3 · Q30), (Exam 5 · Q33).
- VMware tools → **VMware Engine**. Licensing/low-level access → **Bare Metal Solution**. SQL Server to managed → **DMS → Cloud SQL** (Exam 2 · Q47), (Exam 1 · Q42), (Exam 4 · Q38).
- Kubernetes across clouds and on-prem → **GKE Enterprise** (Exam 1 · Q24), (Exam 2 · Q20), (Exam 3 · Q31), (Exam 5 · Q25).
- Data on-prem + Google services → **hybrid**. Several public clouds → **multicloud** (Exam 6 · Q12), (Exam 6 · Q44), (Exam 4 · Q5), (Exam 6 · Q48).
- Avoid lock-in → **openness, open standards, open source** (Exam 5 · Q18), (Exam 6 · Q21), (Exam 5 · Q44).
- Connect systems, unlock legacy, earn from data → **API** (Exam 2 · Q42), (Exam 1 · Q18), (Exam 4 · Q8), (Exam 1 · Q21), (Exam 4 · Q11), (Exam 1 · Q9), (Exam 5 · Q3), (Exam 5 · Q2), (Exam 5 · Q38), (Exam 5 · Q42).
- Secure, track, monetize APIs → **Apigee** (Exam 2 · Q2), (Exam 5 · Q47).
