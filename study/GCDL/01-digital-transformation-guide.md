# Domain 1 Study Guide — Digital Transformation with Google Cloud

> Condensed from the 28-question bank in [`01-digital-transformation.md`](01-digital-transformation.md). Citations look like (Exam N · QM). The bank is small and repeats a few ideas many times (CapEx → OpEx, on-prem scaling pain, IaaS/PaaS/SaaS), so official exam-guide topics that no question tests are covered briefly and marked *(not in the question bank)*. Items marked "see ⚠️" have a shaky key or wording, discussed at the end.

---

## 1. What digital transformation means

### Key facts
- **Digital transformation** = using modern digital technology (cloud, data, analytics, automation, AI) to **redesign how the business works and delivers value**: workflows, collaboration, customer experience and speed of response to demand (Exam 2 · Q39).
- It is **not just a change of hosting location**. Moving to the cloud is a chance to **redesign current business processes and services** (Exam 4 · Q33).
- It is **not only for IT** and **not only for large companies**. It changes the business model, not just the cost line (Exam 4 · Q33).
- The value over time comes from teams spending less effort on running infrastructure and more on **building solutions** that differentiate the business (Exam 1 · Q29), (Exam 4 · Q31).
- **Customer expectations drive it.** The exam's recurring user expectations:
  - Information **simple to access from any device** (hence mobile apps) (Exam 2 · Q7).
  - **Always-on services**: help and service outside business hours (Exam 4 · Q16).
- Cloud gives developers **new tools to innovate and optimize resource usage**: fast provisioning, easy scaling, room to experiment (Exam 4 · Q31).
- **Narrower labels the exam uses as distractors** (Exam 2 · Q39):
  - **Data center migration**: moving workloads and data to another environment. It can be one step of a transformation, but it doesn't redesign processes by itself.
  - **Operations optimization**: making existing operations more efficient, reliable or cheaper. It supports transformation but is only part of it.
  - **User personalization**: tailoring content to each user. It is one possible outcome, not the overall approach.
- Moving the same systems to the cloud without improving processes or services ("lift and shift only") gets the cost benefits at best and **misses most of the value** (Exam 4 · Q33).
- **The cloud as a transformation platform** *(not in the question bank)*: Google frames cloud as an enabler of new business models, data-driven decisions, and faster experimentation. Older IT was a cost center that kept the lights on; modern cloud is a driver of innovation.

### Phrases that map to "digital transformation"

| Scenario wording | Answer | Not this |
|---|---|---|
| Cloud + analytics + automation to redesign workflows and customer experience | ✅ Digital transformation (Exam 2 · Q39) | ❌ Data center migration, operations optimization, user personalization |
| What does adopting cloud mainly represent? | ✅ Chance to redesign processes and services (Exam 4 · Q33) | ❌ "Only IT", "only large orgs", "same business model, lower cost" |
| Why launch a mobile app? | ✅ Customers expect access from any device (Exam 2 · Q7) | ❌ "Only through mobile", "mobile is the only way to secure data" |
| Why extend support to evenings and weekends? | ✅ Users expect always-on services (Exam 4 · Q16) | ❌ Personalization, regional access, professional expertise |

### Decision rules
- If the scenario combines several technologies to change **how the business operates**, the answer is **digital transformation**, not a narrower label (Exam 2 · Q39).
- "Gain value over time" from cloud → **focus on solution development / innovation**, not on maintaining infrastructure (Exam 1 · Q29).
- "Why are customers asking for X?" → pick the **broad modern expectation** (any device, always on), not a narrow technical reason (Exam 2 · Q7), (Exam 4 · Q16).

### Traps
- Words like "only", "exclusively", "never" in options are usually wrong at this level (Exam 2 · Q7), (Exam 4 · Q33).
- A mobile app is not more secure by itself. Security comes from identity and access controls, encryption and secure design across the whole system (Exam 2 · Q7).
- "Always-on" is about **when** a service is available (time of day). "Regional access" is about **where** (geography, language, local markets). "Personalization" is about tailoring to each user (Exam 4 · Q16).
- "Expand internal hosting infrastructure" or "relax on-prem security" are never the cloud benefit (Exam 1 · Q29).
- "Avoid the limitations of serverless" or "optimize on-prem maintenance" don't describe moving to cloud (Exam 4 · Q31).

---

## 2. Limits of on-premises infrastructure and why cloud helps

### Key facts
- On-prem capacity is **fixed**. Adding compute means **buying, installing, configuring and maintaining hardware**, which is **time-consuming and costly** (Exam 6 · Q35).
- To survive traffic peaks on-prem, you must **provision hardware for peak usage**, which is expensive and sits idle the rest of the time (Exam 2 · Q3).
- When peak traffic exceeds what you bought, the app goes down: **not enough servers to handle the traffic** (Exam 6 · Q15).
- Both directions hurt: you **over-buy** capacity (waste) or **under-buy** (outages) (Exam 3 · Q29).
- Cloud fixes this with **elastic, on-demand capacity**: scale up for the spike, scale down after, and **pay only for what you use** (Exam 3 · Q29).
- Cloud lets you reach data and compute **without being tied to one physical location** (Exam 1 · Q8).
- Public cloud is **cost-effective for storing and serving data at large scale** (Exam 4 · Q21).
- Slow provisioning and limited experimentation on fixed hardware are solved by cloud's **self-service tools**: on-demand environments, managed databases, automated deployments, monitoring and autoscaling (Exam 4 · Q31).
- **"Agile infrastructure"** on this exam means you can **provision, scale and release resources on demand** instead of buying hardware for the highest expected peak. Combined with consumption pricing, you only pay for what you need, when you need it (Exam 3 · Q29).
- **Cloud availability is high but never 100%.** Providers publish an **SLA (service level agreement)** per service, with targets such as 99.9% or 99.99%. Real uptime still depends on your design: multiple zones, load balancing, backups and disaster recovery (Exam 1 · Q8), (Exam 3 · Q29), (Exam 4 · Q31).
- Cloud also offers managed **backup, replication and disaster recovery** capabilities, so teams build less of this themselves (Exam 1 · Q29).
- **Serverless** services (Cloud Run, Cloud Run functions) scale automatically with demand. That is why "a serverless function can't scale" is never the cause in an on-prem scenario (Exam 2 · Q3), (Exam 4 · Q31), (Exam 6 · Q15).

### Decision rules
- Scenario = "own data center + traffic spikes + struggle/outage" → the cause is **fixed hardware capacity / cost of provisioning for peak** (Exam 2 · Q3), (Exam 6 · Q15), (Exam 6 · Q35).
- Scenario = "over-buy or under-buy for holidays" → benefit is **pay only for what you need, when you need it** (Exam 3 · Q29).
- Public cloud benefit for a distributed company → **access not limited to one physical location** (Exam 1 · Q8).

### Traps
- **Serverless and multicloud distractors**: if the company runs on its own servers, options blaming "serverless functions that can't scale" or "multi-cloud complexity" don't fit the scenario (Exam 2 · Q3), (Exam 6 · Q15), (Exam 6 · Q35).
- "Overreliance on PaaS", "perimeter security makes data inaccessible", "inconsistent customer data", "compliance blocks scaling" are all off-topic (Exam 2 · Q3), (Exam 6 · Q15), (Exam 6 · Q35).
  - PaaS is adopted to **reduce** operational burden, so it can't be the cause of on-prem scaling pain (Exam 2 · Q3).
  - Bad data quality causes wrong reports and logic errors, **not outages at peak traffic**. Failures that happen only at peak point to a **capacity** limit (Exam 6 · Q15).
  - Adding capacity doesn't automatically breach compliance. Compliance depends on how systems are designed, secured and governed (Exam 6 · Q35).
- Cloud does **not** guarantee 100% availability, does not remove the need for security, and doesn't mean "unlimited storage = no downtime" (Exam 1 · Q8), (Exam 3 · Q29), (Exam 4 · Q31).
- Moving to cloud is never a reason to **relax security protocols**. Under shared responsibility the customer still secures identities, access, data and configuration (Exam 1 · Q29), (Exam 1 · Q8).
- "Schedule physical server repairs after hours" is your problem on-prem, not a cloud benefit (Exam 1 · Q8).

---

## 3. Cloud economics: CapEx, OpEx, TCO and pay-as-you-go

### Key facts
- **CapEx (capital expenditure)**: large upfront purchases of long-lived assets, such as servers and data centers. Paid before you know if you need them.
- **OpEx (operational expenditure)**: ongoing spending for services as you consume them, such as a monthly cloud bill.
- **Moving to cloud shifts spending from CapEx to OpEx.** This is the single most repeated fact in this domain (Exam 2 · Q4), (Exam 4 · Q29), (Exam 4 · Q37).
- On-prem hardware purchases are capital assets, **depreciated over several years**. Cloud services are paid as they are consumed, so they are booked as operating costs (Exam 2 · Q4).
- After migration, the customer must **adjust to a consumption-based, pay-as-you-go spending model** (Exam 3 · Q32).
- **Cost management itself changes.** Spending becomes usage-based and variable, so teams must **monitor billing, set budgets and alerts, label resources, right-size, and remove idle resources** (Exam 2 · Q4). Billing tools are covered in Domain 6.
- TCO is **often but not always lower** in the cloud. It depends on architecture, usage patterns, licensing and how well the environment is optimized. A poorly managed cloud can be expensive (Exam 2 · Q4).
- Cloud **reduces on-prem infrastructure management costs** (hardware upkeep, staff time on racking and patching servers) (Exam 4 · Q27).
- **TCO (total cost of ownership)** = all costs over time: hardware, software licenses, power, cooling, space, staff, maintenance, downtime, and for the cloud option also the **migration effort**. Review TCO before migrating, and compare it with the expected business benefits, to **evaluate return on investment (ROI)** of cloud vs staying on-prem (Exam 4 · Q49).
- Large-scale storage and serving is cheaper in public cloud thanks to economies of scale (Exam 4 · Q21).
- Google Cloud also offers **discounts for steady usage** (sustained use and committed use discounts) *(not in the question bank; billing and cost control are in Domain 6)*.

### CapEx vs OpEx

| | CapEx | OpEx |
|---|---|---|
| Typical example | Buy servers, build a data center | Pay a monthly cloud bill |
| Timing | Upfront | As you go |
| Capacity | Fixed, sized for peak | Elastic, sized for actual use |
| Risk | Over- or under-buying | Bill grows with usage, needs monitoring |
| Cloud migration direction | ❌ Away from | ✅ Toward (Exam 2 · Q4), (Exam 4 · Q29), (Exam 4 · Q37) |

### Decision rules
- Any "how does spending change when moving to cloud?" question → **CapEx → OpEx** (Exam 2 · Q4), (Exam 4 · Q29), (Exam 4 · Q37).
- "Why look at TCO before migration?" → **to evaluate ROI** (Exam 4 · Q49).
- "Effect on operations and personnel costs" → **reduced on-prem infrastructure management costs** (Exam 4 · Q27).

### Traps
- **OpEx → CapEx** is always backwards (Exam 2 · Q4), (Exam 4 · Q29), (Exam 5 · Q28).
- "Cost management stays the same, only TCO changes" is wrong. The spending model itself changes (Exam 2 · Q4).
- Error budget, SLA availability and compute sizing are not why you review TCO (Exam 4 · Q49):
  - **Error budget**: an SRE idea. With an SLO (service level objective), it is how much unreliability is acceptable before teams must prioritize reliability work.
  - **Service level availability**: a reliability target set in SLAs and SLOs, not a financial comparison.
  - **Compute sizing**: technical capacity planning. It feeds cost estimates, but TCO is much broader.
- "Increased hardware maintenance" or "increased cloud hardware management costs" for the customer is wrong. The provider manages the hardware (Exam 4 · Q27), (Exam 4 · Q37).
- "Reduced cloud software licensing costs" sounds plausible but isn't the point. Licensing may change with the vendor agreement and architecture, but it doesn't automatically go down; the clear saving is on-prem management (Exam 4 · Q27).
- "A shift toward structured data" has nothing to do with migration economics. Cloud supports structured, semi-structured (JSON) and unstructured data (images, video, logs) alike (Exam 4 · Q37).
- "No change to existing responsibilities" is wrong. Infrastructure duties move to the provider; the customer keeps application design, access control, data protection and configuration (Exam 4 · Q37).
- OpEx does not make TCO automatically "more predictable". Usage-based bills can vary (Exam 3 · Q29).

---

## 4. Cloud deployment models: public, private, hybrid, multicloud

### Key facts
- **Public cloud**: shared infrastructure owned and run by a provider (Google Cloud), rented on demand. Benefits: global reach, elasticity, scale economics (Exam 1 · Q8), (Exam 4 · Q21).
- **Private cloud** *(not in the question bank)*: cloud-style infrastructure dedicated to one organization, usually in its own data center.
- **Hybrid cloud** = **private (on-prem) infrastructure + public cloud services** used together. Typical reason: keep sensitive or regulated systems on-prem while using public cloud for analytics, scaling and new services (Exam 3 · Q22).
- The private side of a hybrid cloud can be an **on-prem data center, a private cloud or an edge environment**. The public side adds scalability, analytics, modernization, storage or disaster recovery (Exam 3 · Q22).
- Hybrid and multicloud are **not exclusive**: one organization can be both at once (Exam 3 · Q22).
- **Multicloud**: using **more than one public cloud provider**. Reasons: avoid lock-in, use the best service from each, meet regional or regulatory needs. Hybrid and multicloud products (GKE Enterprise, formerly Anthos) are in Domain 4.
- **On-premises**: everything in your own data center, all managed by you.

### Deployment models compared

| Model | What it combines | Exam signal |
|---|---|---|
| On-premises | Own hardware, own data center | "aging data centers", "fixed capacity" |
| Public cloud | Provider's shared infrastructure | "global access", "pay for what you use" (Exam 1 · Q8) |
| Private cloud | Dedicated cloud-style infrastructure | *(not in the question bank)* |
| Hybrid cloud | ✅ Private/on-prem + public cloud (Exam 3 · Q22) | "keep sensitive systems on-prem, use cloud for the rest" |
| Multicloud | Two or more public providers | "multiple public cloud providers" (the distractor in (Exam 3 · Q22)) |

### Decision rules
- "Own data center + Google Cloud together" → **hybrid** (Exam 3 · Q22).
- "Several public cloud providers" → **multicloud**.

### Traps
- "A combination of multiple public cloud providers" is **multicloud**, not hybrid (Exam 3 · Q22).
- "Serverless + public cloud" and "different virtualized servers" are not deployment models (Exam 3 · Q22). Serverless runs on the provider's public cloud, so that option has no private side. Virtual machines can run anywhere, so virtualization alone doesn't make an architecture hybrid.
- "Hybrid cloud" also shows up as a distractor in service-model questions. It is a deployment model, not IaaS/PaaS/SaaS (Exam 6 · Q11).

---

## 5. Service models: IaaS, PaaS, SaaS and shared responsibility

### Key facts
- **IaaS (Infrastructure as a service)**: rent **VMs, storage and networking**; you build and configure the servers, OS and everything above. Example: Compute Engine (Exam 6 · Q11).
- **PaaS (Platform as a service)**: you deploy **your own code**; the provider runs servers, OS and scaling. Examples: App Engine, Cloud Run (Exam 6 · Q13).
- **SaaS (Software as a service)**: a **finished application** delivered over the internet; you only use it and manage your data/content. Examples: Google Workspace, an online payroll app (Exam 2 · Q1).
- **Shared responsibility**: the more managed the model, the less you manage. In SaaS, you are left responsible mainly for **your content, data and users** (Exam 2 · Q22).
- Whatever the model, after migrating you never manage Google's network, physical storage or data centers. You do adapt to **pay-as-you-go** spending (Exam 3 · Q32).
- **SaaS provider duties**: the provider manages the application, platform, infrastructure, updates and availability. Users reach it through a browser, mobile app or client (Exam 2 · Q1).
- **Serverless / FaaS (functions as a service)**: you write small pieces of **event-driven code** and define the events that trigger them; the provider runs and scales them. Example: Cloud Run functions (formerly Cloud Functions). You still write code, so FaaS is never the answer for "use a finished app" (Exam 2 · Q1).
- **App Engine** is Google's classic PaaS: a fully managed, serverless platform where Google handles provisioning and scaling (Exam 6 · Q13).
- **NaaS (network as a service)**: managed networking such as connectivity, routing and network security functions. It doesn't host applications (Exam 6 · Q13).
- **Security of vs in the cloud**: the provider secures **the cloud** (data centers, hardware, its network). The customer secures what it puts **in the cloud**: identities, access, data, configurations and workloads (Exam 1 · Q29), (Exam 1 · Q8). Google extends this idea as **shared fate**: it also provides secure defaults, blueprints and guidance to help customers do their part *(not in the question bank; security is Domain 5)*.

### Who manages what

| Layer | On-prem | IaaS | PaaS | SaaS |
|---|---|---|---|---|
| Physical data center, network, hardware | You | Google | Google | Google |
| OS, runtime, scaling | You | You | Google | Google |
| Application code | You | You | You | Provider |
| Data, content, user access | You | You | You | ✅ You (Exam 2 · Q22) |

### Decision rules
- "Rent VMs, storage, networking; build custom servers; pay per use" → **IaaS** (Exam 6 · Q11).
- "Deploy our own app, it should scale, we don't want to manage servers or OS" → **PaaS** (Exam 6 · Q13).
- "Use a vendor's ready-made app; no servers, no platform, no code" → **SaaS** (Exam 2 · Q1).
- "What is the SaaS customer exclusively responsible for?" → **customer-facing content** (Exam 2 · Q22).

### Traps
- "Network as a service" and "Functions as a service" are distractors (Exam 6 · Q13), (Exam 2 · Q1).
- In SaaS, keeping the platform running and monitoring servers and networks are the **provider's** job (Exam 2 · Q22). The customer may still handle its own local network connectivity, allowed settings and who gets access (Exam 2 · Q22).
- Shared responsibility is about **who secures and operates what**. It doesn't give you "visibility during traffic spikes"; that comes from monitoring and logging tools (Exam 3 · Q29).
- The customer does not get paid compensation for outages as a "responsibility", and does not manage Google's network or storage hardware (Exam 3 · Q32).

---

## 6. Google Cloud infrastructure: regions, zones, latency and custom hardware

### Key facts
- **Region** = an independent geographic area (for example `europe-west3`, Frankfurt). **Zone** = an isolated deployment area inside a region. Multiple zones protect against a single-zone failure; multiple regions put the app **closer to users** and survive a regional outage.
- **Network latency** = the delay for data to travel between user and server; it grows with **physical distance**. **Bandwidth** = how much data can move per second. Users far from the region can have **high bandwidth but high latency** (Exam 4 · Q32).
- To cut latency for users on another continent, **deploy a replica of the app in a region near them** (Exam 4 · Q41). A **global load balancer** then sends each user to the nearest healthy backend, and **Cloud CDN** caches content at the edge (Exam 4 · Q32), (Exam 4 · Q41).
- **Zones** protect against a **zonal failure** (availability). They don't change the distance to users, so they don't fix latency for far-away users (Exam 4 · Q41).
- Capacity or configuration problems hit **all users**. A slowdown that hits only distant users points to latency (Exam 4 · Q32).
- Google designs **purpose-built (custom) servers** optimized for specific workloads, which makes them **more efficient** than off-the-shelf hardware. Google tunes hardware, networking, storage, power and cooling together for its scale (Exam 4 · Q44).
- **Edge network and points of presence** *(not in the question bank)*: Google's private global fiber network plus edge locations and Cloud CDN cache content close to users, lowering latency further.
- **Google's global network** *(not in the question bank)*: traffic can enter Google's network close to the user and travel on Google's backbone rather than the public internet.

### Latency vs bandwidth

| Symptom | Cause | Fix |
|---|---|---|
| Far-away users see slow pages, but their speed tests are fast | ✅ Network latency (Exam 4 · Q32) | Deploy closer: a region near them (Exam 4 · Q41), CDN |
| Large transfers are slow for everyone | Insufficient bandwidth | More bandwidth / better connectivity |
| Slow everywhere under load | Too few or misconfigured servers | Scale out / fix config |

### Decision rules
- "Users in another continent + slow + good internet speed" → **latency** (Exam 4 · Q32).
- "Improve experience for users in country X" → **deploy in a region in country X** (Exam 4 · Q41).
- "Why purpose-built servers?" → **optimized for specific tasks, more efficient** (Exam 4 · Q44).

### Traps
- More **zones in the same region** or more regions **on the same continent** don't help users far away (Exam 4 · Q41).
- A separate billing account changes nothing about performance. Billing accounts handle payment, invoicing and cost tracking, not where the app runs (Exam 4 · Q41).
- Custom servers don't run "software that can't run elsewhere". The same software runs elsewhere, just less efficiently at Google's scale (Exam 4 · Q44).
- "Cheaper to build", "backward compatible with legacy disks", "run software that can't run elsewhere" are wrong reasons for custom servers (Exam 4 · Q44).
- Don't pick "insufficient bandwidth" when the scenario says speed tests are fine (Exam 4 · Q32).

---

## 7. Leading cloud adoption: culture, skills and sponsorship

### Key facts
- Moving from a few cost-saving migrations to a **company-wide transformation** needs **visible top-down executive sponsorship** and a **blameless culture** where teams can experiment and learn from failure (Exam 5 · Q28).
- Building cloud skills: create **a culture of continuous peer-to-peer learning using official training materials**. Learning is shared across teams, not done in isolation (Exam 3 · Q2).
- The right mix is to **upskill existing staff** while hiring where needed. Relying on contractors with elevated access is a security and knowledge risk (Exam 3 · Q2).
- **Google Cloud Adoption Framework (CAF)**: measures cloud maturity on four themes — **Learn** (upskilling staff, plus help from experienced partners), **Lead** (top-down sponsorship plus bottom-up, cross-functional teams), **Scale** (cloud-native, managed services and automation), **Secure** (identity-centric, multilayered security) — across three phases. The bank doesn't name the CAF, but its wrong options in (Exam 3 · Q2) and (Exam 5 · Q28) are the CAF's **tactical** behaviors and the keys are its **transformational** ones.
  - **Tactical**: individual workloads, no overall plan. Goal: cut costs fast with little disruption (short term).
  - **Strategic**: a broader vision guides workloads; people and processes start to change (mid term).
  - **Transformational**: IT becomes an **engine of innovation and a partner to the business** (long term).
- **Cross-functional teams and change management** *(not in the question bank)*: transformation fails when it is treated as an IT-only project. Business, finance and security must be involved from the start (see also (Exam 4 · Q33)).
- Sustainability and cost governance are often part of the business case (carbon-free energy goals, FinOps) *(not in the question bank; covered in Domain 6)*.

### Cloud Adoption Framework: Learn and Lead by phase

| Phase | Learn (skills) | Lead (sponsorship and teams) |
|---|---|---|
| Tactical | Best-effort, self-motivated learning. Contractors do essential work with **wide privileged access**. No hiring of cloud-experienced staff (Exam 3 · Q2) | Sponsorship from one line of business. Adoption **driven by individual contributors** (Exam 5 · Q28) |
| Strategic | Managed training program, certifications. Partners fill narrow gaps. **Hire** cloud-experienced people | Sponsorship up to the C-level. A dedicated cross-functional team (Cloud Center of Excellence) drives adoption |
| Transformational | ✅ **Continuous, collaborative learning**: formal training plus hackathons and tech talks. Contractors have no privileged access (Exam 3 · Q2) | ✅ Sponsorship across the **whole C-level**, a **culture of blameless postmortems**, autonomous cross-functional teams (Exam 5 · Q28) |

### Decision rules
- "Make adoption company-wide / support innovation" → **top-down sponsorship + blameless culture** (Exam 5 · Q28).
- "Build long-term cloud skills, share knowledge" → **continuous peer-to-peer learning with official training** (Exam 3 · Q2).

### Traps
- "Adoption driven primarily by individual contributors" is the CAF's **tactical** phase: it doesn't scale across the company (Exam 5 · Q28).
- "Move funding to CapEx" and "invest in on-prem infrastructure" go backwards (Exam 5 · Q28).
- "Self-directed, separate learning" misses the **sharing** part: knowledge stays scattered. "Train existing staff instead of hiring" is the CAF's tactical stance; mature organizations upskill **and** hire. "Give contractors elevated access" builds dependency, not internal skills, and breaks least privilege (Exam 3 · Q2).

---

## ⚠️ Questionable answers

No open items. (Exam 3 · Q29) was listed here for its loose "agile infrastructure" wording. The dump's explanation reads "agile" as provisioning, scaling and releasing resources on demand, which makes the keyed answer sound; see lesson 2.

---

## Last-minute cheat sheet

- Cloud + analytics + automation to redesign the business = **digital transformation** (Exam 2 · Q39).
- Cloud adoption = **chance to redesign processes and services**, not only IT, not only cost (Exam 4 · Q33).
- Value over time = **focus on solution development** (Exam 1 · Q29). Developers get **tools to innovate** (Exam 4 · Q31).
- Customers expect **any-device access** (Exam 2 · Q7) and **always-on services** (Exam 4 · Q16).
- On-prem scaling pain = **cost of provisioning for peak**, **not enough servers**, **slow and costly to add capacity** (Exam 2 · Q3), (Exam 6 · Q15), (Exam 6 · Q35).
- Holiday spikes → cloud lets you **pay only for what you need, when you need it** (Exam 3 · Q29).
- Public cloud = access **not tied to one location** (Exam 1 · Q8), **cost-effective at scale** (Exam 4 · Q21).
- Spending moves **CapEx → OpEx** (Exam 2 · Q4), (Exam 4 · Q29), (Exam 4 · Q37). Adapt to **pay-as-you-go** (Exam 3 · Q32).
- Cloud **reduces on-prem infrastructure management costs** (Exam 4 · Q27).
- Review TCO to **evaluate ROI** (Exam 4 · Q49).
- **Hybrid** = private/on-prem + public cloud. **Multicloud** = several public clouds (Exam 3 · Q22).
- **IaaS** = rent VMs/storage/network (Exam 6 · Q11). **PaaS** = deploy your code, no servers (Exam 6 · Q13). **SaaS** = ready-made app (Exam 2 · Q1).
- SaaS customer owns **content and data** (Exam 2 · Q22).
- Far users slow, fast speed test → **latency** (Exam 4 · Q32) → **deploy in a region near them** (Exam 4 · Q41).
- Google's **purpose-built servers** are **optimized for specific tasks** (Exam 4 · Q44).
- Company-wide adoption → **top-down sponsorship + blameless culture** (Exam 5 · Q28).
- Skills → **continuous peer-to-peer learning with official training** (Exam 3 · Q2).
- CAF: individual contributors, isolated self-study, contractors with privileged access = **tactical**. Blameless culture, C-level sponsorship, shared learning = **transformational** (Exam 3 · Q2), (Exam 5 · Q28).
- Cloud SLAs are 99.9%–99.99%, **never 100%** (Exam 1 · Q8). Cost management **changes** after migration: budgets, alerts, right-sizing (Exam 2 · Q4).
- Zones = availability, not latency. Global load balancing + Cloud CDN + a nearby region = lower latency (Exam 4 · Q41).
