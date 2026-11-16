# Domain 6 Study Guide — Scaling with Google Cloud Operations

> Condensed from the 43-question bank in [`06-scaling-operations.md`](06-scaling-operations.md). Citations look like (Exam N · QM). Several ideas repeat across exams (SLO definition, Cloud Logging, the golden signals), so look for paired citations. Items marked "see ⚠️" have a shaky key, discussed at the end.

---

## 1. Cloud financial governance (FinOps)

### Key facts
- **Cloud spending is decentralized and variable.** Many teams can create resources on demand, and the bill follows actual usage. On-premises spending was centralized (one procurement team) and fixed (hardware bought up front) (Exam 2 · Q11).
- That shift is why cloud needs **financial governance**: shared rules, visibility and accountability for who spends what. Google calls the practice **FinOps** (cloud financial management), where finance, technology and business teams work together on cost decisions.
- **Accountability comes from visibility.** When teams overspend because they can't see how their usage hits the bill, **share cost views with each department** (Exam 3 · Q25).
- Cost visibility per team depends on structure: separate projects or folders per team, and **labels** on resources (for example `team=finance`) so the bill can be broken down. One identical tag on every resource gives no breakdown at all (Exam 3 · Q25).
- Labels only help when they are meaningful **key-value pairs** that differ by department, application, environment, cost center or owner. Billing reports, budgets and billing export can then group spend by those labels (Exam 3 · Q25).
- Accountability also needs **clear ownership**: someone who approves changes, deletes unused resources and answers for overruns. "Everyone owns everything" means nobody does (Exam 3 · Q36).
- Cloud costs are **OpEx**, not CapEx. Moving back to CapEx or buying physical servers is never the cloud cost answer (Exam 3 · Q25), (Exam 3 · Q36).
- **Unpredictable demand + hard-to-control costs:** apply **intelligent recommendations** (Active Assist / Recommender), such as rightsizing idle or oversized VMs and deleting unused resources. Cost recommendations are also gathered in the **FinOps hub** in Cloud Billing (Exam 3 · Q36).

### Decision rules
- "Teams don't see how their usage affects the bill" → **share cost views / reports per team** (Exam 3 · Q25).
- "Costs vary month to month, optimize resource use" → **intelligent recommendations** (Exam 3 · Q36).
- "What is cloud spending like?" → **decentralized and variable** (Exam 2 · Q11).

### Traps
- "Centralized and fixed" describes the old on-premises model (Exam 2 · Q11).
- "Decentralize financial decisions" or "share project ownership across all teams" sounds collaborative but removes accountability (Exam 3 · Q36).
- "Increase capital expenditure" or "improve physical server purchasing" are on-premises answers (Exam 3 · Q25), (Exam 3 · Q36).

---

## 2. Cost-control tools: budgets, estimates and discounts

### Key facts
- **Budgets and budget alerts** (Cloud Billing): set a budget amount, add **threshold rules** (for example 50%, 90%, 100% of the budget, actual or forecasted), and get notified by email or Pub/Sub. It warns before the invoice arrives (Exam 1 · Q11).
  - A budget alert **notifies**. It does not stop spending by itself. Automatic action (like disabling billing) needs extra automation through Pub/Sub.
- **Google Cloud Pricing Calculator:** the tool for a reliable estimate of monthly cost **before** you deploy (Exam 2 · Q36).
- **Sustained use discounts (SUDs):** applied **automatically** to eligible Compute Engine VMs once they run for **more than 25% of the billing month**. The discount grows the longer they run. No sign-up, no setting and no commitment (Exam 6 · Q1).
  - Only some machine series are eligible (for example N1, N2, N2D, C2, M1, M2). E2 and most newer series get no SUDs.
  - SUDs don't stack with CUDs: usage already covered by a commitment gets no SUD (Exam 6 · Q1).
- **Committed use discounts (CUDs):** you commit to a **1-year or 3-year** level of usage (a minimum amount of resources or of spend) in exchange for a bigger discount. That is a different product from SUDs (Exam 6 · Q1).
- **Spot VMs:** deep discount for interruptible capacity. Good for fault-tolerant batch work, not a way to get SUDs (Exam 6 · Q1).
- **Quotas** limit how much of a resource a project can use (CPUs, API calls). They protect against runaway usage, but they are not a spend alert, and costs can still climb inside the quota (Exam 1 · Q11).
- The Pricing Calculator accounts for region, machine size, storage class, network egress, discounts and usage hours, which is why manual math from pricing pages is slow and error-prone (Exam 2 · Q36).
- *(not in the question bank)* **Cloud Billing reports** and **billing export to BigQuery** let you analyze spend by project, service and label. Billing accounts are linked to projects, and IAM billing roles control who can see or change them.

### Cost tools compared

| Need | Use | Not | Source |
|---|---|---|---|
| Be told when spend crosses a limit | ✅ Budget + threshold alert | ❌ Quotas, past billing reports, stopping VMs | (Exam 1 · Q11) |
| Estimate cost before deploying | ✅ Pricing Calculator | ❌ Deploying a test workload, manual math from pricing pages, historical costs | (Exam 2 · Q36) |
| Discount for VMs that run most of the month | ✅ SUDs, automatic | ❌ 1/3-year commitment (that's CUDs), Spot VMs, smaller machines | (Exam 6 · Q1) |
| Lower cost on predictable long-term usage | ✅ CUDs | | (Exam 6 · Q1) |
| Optimize resources when demand varies | ✅ Intelligent recommendations | ❌ More CapEx | (Exam 3 · Q36) |

### Decision rules
- "Notify when costs cross X" → **budget threshold rule and alert** (Exam 1 · Q11).
- "Estimate before deploying" → **Pricing Calculator** (Exam 2 · Q36).
- "How do we get sustained use discounts?" → **do nothing, they are automatic** (Exam 6 · Q1).

### Traps
- Reviewing past bills looks backward. The question wants a proactive alert (Exam 1 · Q11).
- Stopping VMs outside peak hours is cost **optimization**. It does not notify anyone when spend crosses a limit (Exam 1 · Q11).
- Historical costs of a "similar" workload are only a rough guide. The new workload may use different services, regions or sizes (Exam 2 · Q36).
- Deploying a test environment "to observe costs" spends money to get an estimate the calculator gives for free (Exam 2 · Q36).
- A 1- or 3-year commitment is the **CUD** answer, not the SUD answer (Exam 6 · Q1).

---

## 3. Resource hierarchy and policy inheritance

### Key facts
- Hierarchy: **Organization → Folders → Projects → Resources**. Folders usually map to departments or teams.
- **Policies set on a folder are inherited** by every project in the folder, including projects created later (Exam 2 · Q19).
- Inheritance goes all the way down: a folder-level access policy applies to the **projects and to their resources** (Exam 3 · Q42).
- Two kinds of policy flow down the hierarchy: **IAM allow policies** (who can do what) and **organization policies** (constraints on what can be configured, such as allowed regions). Both are inherited by child folders, projects and resources (Exam 2 · Q19), (Exam 3 · Q42).
- Folders can contain projects **or other folders**, so a department folder can hold environment sub-folders. Folders can group projects by department, environment, application or business unit (Exam 2 · Q19), (Exam 3 · Q42).
- Inherited access applies unless something blocks it, such as an **IAM deny policy** or an organization policy constraint (Exam 3 · Q42).
- Policies are not limited to one level. They can be set at organization, folder, project or (for many services) resource level. The effective policy is the union of the policy at that level and everything inherited from above.
- The hierarchy also supports cost governance: projects and folders give a natural way to group spend by team (Exam 3 · Q25).

### Decision rules
- "Apply rules once for a team and have them apply to every project" → **set the policy on the team's folder** (Exam 2 · Q19).
- "What happens to a folder-level policy?" → **inherited by the projects and their resources** (Exam 3 · Q42).

### Traps
- "Policies can only be applied at the organization level" or "only to individual projects" are both false (Exam 2 · Q19).
- "Inherited by projects but not their resources" stops inheritance one level too early (Exam 3 · Q42).
- A folder policy does not spread sideways to other folders in the organization (Exam 3 · Q42).

---

## 4. Measuring reliability: availability, SLIs, SLOs and SLAs

### Key facts
- **Availability** is expressed as a **percentage of uptime** (or of successful requests) over a period, such as a monthly uptime percentage in an SLA (Exam 4 · Q22).
- A count of incidents is not a measure of availability: one long outage and several short ones can cost very different amounts of uptime (Exam 4 · Q22).
- **SLI (service-level indicator):** the **direct measurement** of how the service is actually performing, such as the share of successful requests or request latency (Exam 2 · Q10).
- SLIs can measure availability, latency, error rate or throughput (Exam 2 · Q10).
- **SLO (service-level objective):** the **target** value for an SLI that the team wants to meet, over a set period. It can be an availability target ("99.9% of requests succeed over 30 days") or a latency target ("95% of requests complete within 300 ms") (Exam 4 · Q9), (Exam 4 · Q10).
- **SLA (service-level agreement):** a **contract** with customers that promises a level of service and states the consequence (usually service credits) when it is missed (Exam 2 · Q48).
- Order of strictness: **SLO is stricter than the SLA**. The internal target is set above the contractual promise so the team reacts before customers are owed anything (Exam 5 · Q20).
- **Nines to downtime per year:** 99.999% ("five nines") allows about **5 minutes** a year (Exam 1 · Q50).

### Allowed downtime

| Availability | Per year | Per month (approx.) |
|---|---|---|
| 99% | ~3.65 days | ~7.3 hours |
| 99.9% | ~8.8 hours | ~44 minutes |
| 99.95% | ~4.4 hours | ~22 minutes |
| 99.99% | ~53 minutes | ~4.4 minutes |
| 99.999% | ~5.3 minutes (Exam 1 · Q50) | ~26 seconds |

### SLI vs SLO vs SLA

| Term | What it is | Keyword in the question | Source |
|---|---|---|---|
| SLI | A measurement | "direct measurement of how it is performing" | (Exam 2 · Q10) |
| SLO | An internal target | "desired reliability and performance target" | (Exam 4 · Q9), (Exam 4 · Q10) |
| SLA | A contract with penalties | "promised to customers", "service credit" | (Exam 2 · Q48), (Exam 1 · Q7) |

### Decision rules
- "Measure" → SLI. "Target" → SLO. "Contract / promise / credit" → SLA (Exam 2 · Q10), (Exam 4 · Q9), (Exam 2 · Q48).
- Availability questions → **percentage of uptime**, not number of regions or incidents (Exam 4 · Q22).

### Traps
- "Enhanced support" and "scalable infrastructure" are filler distractors in the SLO questions (Exam 4 · Q9), (Exam 4 · Q10).
- "Error reporting" is a tool, not an SLI (Exam 2 · Q10).
- Response time is **latency**, one possible SLI. It is not how availability is expressed. A service can be available but slow (Exam 4 · Q22).
- More regions can **improve** availability, but the number of regions is not how availability is **measured** (Exam 4 · Q22).

---

## 5. Error budgets and missed targets

### Key facts
- **Error budget = 100% − SLO.** With a 99.9% SLO, the service may be unavailable 0.1% of the time. That budget can be "spent" on risky releases and experiments.
- **Budget left → innovate.** Ship features and take reasonable risks (Exam 4 · Q25).
- **Below the SLO → focus on reliability.** Slow down feature releases and fix stability first. Being below the SLO but above the SLA means customers are not owed credits yet, but the team must react (Exam 5 · Q20).
- **Provider misses its SLA → the customer typically gets a service credit.** Fees don't go up, the service isn't shut down, and the provider's SLA has nothing to do with your internal error budget (Exam 2 · Q48).
  - Google Cloud SLAs call these **Financial Credits**. They are applied to future bills for the affected service, not paid as cash, and the customer must claim them under the SLA's terms (Exam 2 · Q48).
- Below the SLO but above the SLA is a **warning sign**: the team is burning its reliability margin and must act before it breaches the contract (Exam 5 · Q20).
- **Business impact of a missed SLA:** unplanned downtime can make **customers leave**. Credits rarely cover lost revenue or trust (Exam 1 · Q7).
- The sensible response to a provider's missed SLA is to review your own architecture, redundancy and support terms, not to weaken the SLA (Exam 1 · Q7).

### Decision rules
- Error budget remaining → prioritize **innovation / feature velocity** (Exam 4 · Q25).
- Below SLO (budget exhausted) → prioritize **reliability** (Exam 5 · Q20).
- Provider breaks SLA → **service credit** for you, **customer churn** risk for your business (Exam 2 · Q48), (Exam 1 · Q7).

### Traps
- "Automatic expansion of the error budget" mixes up a provider's contract with your internal target (Exam 2 · Q48).
- "Renegotiate the SLA so uptime matters less" and "data automatically deleted" are nonsense distractors (Exam 1 · Q7).
- Dropping below the SLO does not mean customers see outages or lower latency. It means the team should shift effort to reliability. If latency is the SLI, missing the SLO means latency went **up** (Exam 5 · Q20).
- A missed **availability** SLA does not mean data is deleted. Outages make data unreachable for a while. Data loss is a **durability** question (Exam 1 · Q7).
- Service credits usually have to be **claimed** under the SLA's terms. "Automatic" is not a safe assumption, but the exam still keys "service credit" (Exam 2 · Q48).

---

## 6. DevOps and SRE culture

### Key facts
- **DevOps** brings development and operations together with shared tools and automation. It fixes **repetitive manual tasks that slow down workflows** (Exam 2 · Q49).
- **Breaking silos** works through **shared responsibility for business results**, not blame or merging everyone into one identical job (Exam 6 · Q43).
- The automation behind DevOps is **CI/CD pipelines** and **automated testing**: build, test and deploy steps run the same way every time, with less human error (Exam 2 · Q49), (Exam 3 · Q17).
- **Small, incremental changes** reduce recovery time when bugs appear. Small releases are easier to test, review and roll back, and fewer changes means the cause is found faster (Exam 3 · Q17).
- **Gradual rollout (canary):** release a new feature to a **small group first**, watch it, then expand. This limits the **blast radius** (how many users a failure can hit) (Exam 3 · Q49).
- Security or privacy concerns about a new feature call for review, testing and a limited rollout, not refusing to launch (Exam 3 · Q49).
- **Automate toil.** Toil is manual, repetitive, automatable operational work. SRE prioritizes automating it (Exam 3 · Q35).
- **Failure is normal.** SRE accepts that some failure will happen, so the team learns from bugs and incidents instead of ignoring or punishing them (Exam 6 · Q50).
- **Blameless postmortems:** after an incident, document what happened, why, and how to prevent it. The goal is learning, not reprimand (Exam 6 · Q50).
- SRE is data-driven: use metrics, logs, traces, SLOs and incident data, and measure the impact of outages to decide what to fix first (Exam 3 · Q35).
- Shared responsibility does not mean identical jobs. Developers and operations keep their skills but share goals and context (Exam 6 · Q43).

### Decision rules
- "Reduce manual work" → **automate toil** (Exam 3 · Q35), (Exam 2 · Q49).
- "Reduce disruption when bugs appear after a release" → **small incremental changes** (Exam 3 · Q17).
- "Release a new system with less risk" → **roll out to a small group first** (Exam 3 · Q49).
- "Minor bug after launch" → **accept and learn from it** (Exam 6 · Q50).
- "Dev and ops work in silos" → **shared responsibility** (Exam 6 · Q43).

### Traps
- "Pause production until all bugs are gone" and "eliminate all future bugs" ignore that failure is normal (Exam 3 · Q17), (Exam 6 · Q50).
- "Large changes together make rollback easier" is the opposite of the truth (Exam 3 · Q17).
- Bug priority follows user and business impact, not bug size. Large bugs are not "easier to review" (Exam 3 · Q17).
- "Reduce the effort spent understanding the impact of outages" is wrong. Outage impact drives SLO and error budget decisions (Exam 3 · Q35).
- "Accept and **ignore**" is wrong. The SRE answer is accept and **learn** (Exam 6 · Q50).
- "Postmortem to reprimand" breaks the blameless rule (Exam 6 · Q50). "Identify who caused each incident and apply penalties" fails for the same reason (Exam 6 · Q43).
- "Give developers sole responsibility for production" and "rely less on operational data" are not SRE practices (Exam 3 · Q35).
- "Roll out to everyone immediately for maximum data" maximizes risk. Refusing to roll out at all is also wrong (Exam 3 · Q49).

---

## 7. Observability, monitoring, logging and the Four Golden Signals

### Key facts
- **Observability** means having visibility into the health, performance and behavior of systems, using **metrics, logs and traces**. "Out-of-the-box observability" means **monitoring IT infrastructure and applications** with built-in tooling you don't have to build yourself (Exam 1 · Q14).
- **Monitoring** = **collecting predefined and custom metrics** (CPU, latency, request count, app-specific values) from applications and infrastructure. Predefined (system) metrics come from Google Cloud services. Custom (user-defined) metrics come from your own code (Exam 3 · Q11).
- **Logging** = **recording application and operating system events as timestamped entries** (plain text or structured), so you can review what happened later (Exam 6 · Q19).
- **Four Golden Signals** (from Google's SRE book):

| Signal | Measures | Exam wording | Source |
|---|---|---|---|
| **Latency** | Time to serve a request | "users wait a long time", "time between request and response" | (Exam 1 · Q45), (Exam 3 · Q18) |
| **Traffic** | Demand on the system | requests or transactions per second, active users | (Exam 1 · Q45), (Exam 3 · Q13) |
| **Errors** | Rate of failed requests | HTTP 5xx, failed calls, timeouts, wrong responses | (Exam 1 · Q45), (Exam 3 · Q18) |
| **Saturation** | How full the system is | "how much capacity is used", CPU, memory or I/O constrained | (Exam 3 · Q13) |

### Decision rules
- "Wait time" / "response time" → **latency** (Exam 1 · Q45), (Exam 3 · Q18).
- "Capacity used" / "resources constrained" → **saturation** (Exam 3 · Q13).
- "Collect metrics" → monitoring (Exam 3 · Q11). "Record events" → logging (Exam 6 · Q19).

### Traps
- Monitoring billing charges, release schedules or customer ratings is not what cloud observability means (Exam 1 · Q14).
- Watching spend in real time is a budget task, not "monitoring" in the ops sense (Exam 3 · Q11).
- "Monitoring network and resource limitations" describes monitoring/saturation, not logging (Exam 6 · Q19).
- Traffic is volume of demand, not how long one request takes. A service can have high traffic with low latency, or the reverse (Exam 1 · Q45).
- Errors means requests **fail**. A slow request that still returns a result is a latency problem (Exam 1 · Q45).
- Saturation can be high while the service still responds. It warns that the system is close to overload (Exam 3 · Q13).
- Recording user actions for compliance is **audit logging** (Cloud Audit Logs), not monitoring (Exam 3 · Q11).

---

## 8. Google Cloud Observability tools

### Key facts
- **Cloud Monitoring:** the managed place for **metrics, dashboards, alerting and uptime checks**. Also collects resource metadata for those views (Exam 1 · Q43), (Exam 5 · Q15).
- **Cloud Logging:** **collect, store, search, analyze and route logs** from GKE, VMs, managed services and custom app entries in one central place (Exam 3 · Q43), (Exam 4 · Q7), (Exam 5 · Q27). It speeds up troubleshooting by letting you analyze logs (Exam 6 · Q10).
  - GKE sends container logs to Cloud Logging by default. VMs send logs through the **Ops Agent** (Exam 3 · Q43).
  - You search and filter logs (by resource, container, severity, time, text) in **Logs Explorer**, which you open from the Console (Exam 4 · Q7), (Exam 6 · Q10).
  - Monitoring shows **that** something is wrong. Logging shows **what happened** (Exam 4 · Q7).
- **Cloud Audit Logs** (inside Cloud Logging) record admin activity and data access, for "who did what" and compliance questions (Exam 3 · Q11).
- **Cloud Trace:** follows **one request across microservices** and shows the time spent at each step (distributed tracing, latency). A trace is made of **spans**, one per unit of work such as a service call or database query (Exam 3 · Q14).
- **Error Reporting:** automatically **collects, groups and shows crashes and exceptions**, with stack traces, counts and first/last-seen times, so developers don't dig through raw logs (Exam 3 · Q48).
- **Cloud Profiler:** continuously collects **CPU and memory-allocation** data from production code with low overhead, and shows **which functions consume the most resources** (often as flame graphs). It is the tool when one service is driving up cloud costs and you need the code responsible (Exam 3 · Q50).
- **Cloud Debugger:** let developers **inspect the state of running code in real time without stopping it** or causing user downtime (Exam 3 · Q1), (Exam 5 · Q26). Google shut Cloud Debugger down in 2023. Its open-source successor is Snapshot Debugger (see ⚠️).
- These tools are grouped under **Google Cloud Observability** (formerly the "operations suite", and before that Stackdriver).

### Which tool?

| Question says | Answer | Common distractor | Source |
|---|---|---|---|
| Dashboards, alerts, uptime checks, metrics | ✅ Cloud Monitoring | ❌ Logging, Trace, Profiler | (Exam 1 · Q43), (Exam 5 · Q15) |
| Collect, store, search logs in one place | ✅ Cloud Logging | ❌ Monitoring, Cloud SDK, Data Catalog, Console | (Exam 3 · Q43), (Exam 4 · Q7), (Exam 5 · Q27), (Exam 6 · Q10) |
| One request across many microservices | ✅ Cloud Trace | ❌ Profiler, Logging | (Exam 3 · Q14) |
| Group crashes and exceptions automatically | ✅ Error Reporting | ❌ Profiler, Trace, Monitoring | (Exam 3 · Q48) |
| Which code function burns CPU/memory | ✅ Cloud Profiler | ❌ Trace, Logging | (Exam 3 · Q50) |
| Inspect live code state without downtime | ✅ Cloud Debugger (retired) | ❌ Profiler, Trace | (Exam 3 · Q1), (Exam 5 · Q26) |
| Who did what, for compliance | ✅ Cloud Audit Logs | ❌ Monitoring | (Exam 3 · Q11) |

### Decision rules
- Keyword → tool: **metrics/dashboards/alerts** = Monitoring, **logs** = Logging, **request path/latency across services** = Trace, **exceptions** = Error Reporting, **CPU/memory by function** = Profiler, **live code state** = Debugger.

### Traps
- Trace vs Profiler: Trace is about **time across services** for a request. Profiler is about **resource use inside the code** (Exam 3 · Q14), (Exam 3 · Q50).
- "Search log entries across containers" is Logging, even though it's GKE. GKE itself and the Console are not log tools (Exam 4 · Q7), (Exam 3 · Q14).
- Cloud Logging does not "analyze live source code", deploy infrastructure (that's Terraform or Infrastructure Manager) or store VM images (that's Compute Engine) (Exam 6 · Q10).
- Off-topic distractors for logging: **Dialogflow** builds chatbots, **Cloud SDK** is the `gcloud` command-line tooling, **Data Catalog** is metadata and data discovery (Exam 3 · Q43).
- Trying to follow one request by correlating logs from every service by hand is the slow way. That's what Trace is for (Exam 3 · Q14).
- Debugger never changed code in production or required taking the app offline (Exam 3 · Q1).

---

## 9. Resilience, scaling and sustainability

### Key facts
- **Redundancy** = copies of important components across multiple resources so the system keeps running when one fails. The goal is **no single point of failure**: for example, several instances behind a load balancer, spread over more than one zone (Exam 4 · Q40).
- Redundancy vs **backups**: backups let you **restore** data after a loss. Redundancy keeps the service **running** during a failure (Exam 4 · Q40).
- **Availability vs durability:** availability is whether the service is reachable. Durability is whether stored data survives. An outage does not delete data. Backups, replication and disaster recovery protect against data loss (Exam 1 · Q7).
- *(not in the question bank)* Resilience patterns: spread workloads across **zones and regions**, use managed instance groups with **autoscaling** and load balancing, replicate data, and plan **disaster recovery** with recovery time and recovery point objectives (RTO/RPO).
- **Scaling sustainably:** move bursty demand to a **public cloud provider with energy-efficient data centers**. You get fast capacity and a lower carbon footprint at once (Exam 6 · Q32).
- *(not in the question bank)* Google has been carbon neutral for its operations since 2007, matches its electricity use with renewable energy, and aims to run on 24/7 carbon-free energy by 2030. The **Carbon Footprint** tool reports emissions from your Google Cloud usage, and the region picker marks lower-carbon regions.

### Decision rules
- "Keep operating if one component fails" → **redundancy** (Exam 4 · Q40).
- "Scale fast + sustainability goals" → **cloud provider with energy-efficient data centers** (Exam 6 · Q32).

### Traps
- Buying efficient servers or switching the on-premises energy supplier doesn't solve the "scale quickly" half. You're still limited by your own space, power, cooling and procurement time (Exam 6 · Q32).
- Rewriting code to use less energy is slow and doesn't add capacity (Exam 6 · Q32).
- Latency and security are not resilience design choices in this question (Exam 4 · Q40).

---

## 10. Google Cloud Customer Care

### Key facts
- **Premium Support** is the tier with the **fastest response for critical (P1) issues** and a **dedicated Technical Account Manager (TAM)** (Exam 3 · Q21).
- *(not in the question bank)* Tiers in order:

| Tier | Typical fit | Notable features |
|---|---|---|
| Basic | Everyone, free | Billing support, docs, community. No technical cases |
| Standard | Dev/test workloads | Technical support during business hours, about 4-hour response for P2 |
| Enhanced | Production workloads | 24/7 for high-impact issues, about 1-hour response for P1 |
| Premium | Business-critical workloads | About 15-minute P1 response, **Technical Account Manager**, proactive guidance (Exam 3 · Q21) |

- *(not in the question bank)* Support cases use **priority levels** (P1 critical to P4 low). Set the priority by business impact. Cases can be escalated if the response doesn't match the impact.

### Decision rules
- "Fastest response" + "dedicated TAM" → **Premium** (Exam 3 · Q21).

### Traps
- Enhanced is production-grade but has **no TAM** (Exam 3 · Q21).

---

## ⚠️ Questionable answers

| Item | Issue |
|---|---|
| **(Exam 3 · Q1)**, **(Exam 5 · Q26)** | Cloud Debugger was deprecated in 2022 and shut down in May 2023 (successor: open-source Snapshot Debugger). The answers describe what it did correctly, but the product no longer exists, and (Exam 5 · Q26) asks which tool "should" be used today. |
| **(Exam 2 · Q48)** | Service credits under Google Cloud SLAs usually must be **requested** by the customer within a time window. "Service credit" is the right answer, but it is not automatic. |
| **(Exam 1 · Q7)** | Keys churn risk (C), which is right. Option A ("use up its internal error budget") is not absurd either, since provider downtime does count against your own SLO. C is the best "business impact" answer. |

---

## Last-minute cheat sheet

- Cloud spending is **decentralized and variable** (Exam 2 · Q11).
- Teams overspend without knowing → **share cost views per department** (Exam 3 · Q25).
- Variable demand, optimize resources → **intelligent recommendations** (Exam 3 · Q36).
- Alert when spend crosses a limit → **budget + threshold rule** (Exam 1 · Q11).
- Estimate before deploying → **Pricing Calculator** (Exam 2 · Q36).
- SUDs are **automatic** after 25% of the month. 1/3-year commitments are CUDs (Exam 6 · Q1).
- Folder policy → inherited by **projects and their resources** (Exam 2 · Q19), (Exam 3 · Q42).
- Availability = **% uptime**. Five nines ≈ **5 minutes/year** (Exam 4 · Q22), (Exam 1 · Q50).
- SLI = measurement, SLO = target, SLA = contract (Exam 2 · Q10), (Exam 4 · Q9), (Exam 4 · Q10).
- Budget left → innovate. Below SLO → reliability (Exam 4 · Q25), (Exam 5 · Q20).
- Provider misses SLA → **service credit**, your risk is **customer churn** (Exam 2 · Q48), (Exam 1 · Q7).
- DevOps removes **repetitive manual tasks**. Silos fixed by **shared responsibility** (Exam 2 · Q49), (Exam 6 · Q43).
- **Small incremental changes**, **roll out to a small group first** (Exam 3 · Q17), (Exam 3 · Q49).
- **Automate toil**. Failure is normal: **accept and learn**, blameless postmortems (Exam 3 · Q35), (Exam 6 · Q50).
- Observability = monitoring **infrastructure and applications**. Monitoring = **metrics**. Logging = **events recorded** (Exam 1 · Q14), (Exam 3 · Q11), (Exam 6 · Q19).
- Wait time = **latency**, capacity used = **saturation** (Exam 1 · Q45), (Exam 3 · Q18), (Exam 3 · Q13).
- Dashboards/alerts/uptime checks → **Cloud Monitoring** (Exam 1 · Q43), (Exam 5 · Q15).
- Logs in one place → **Cloud Logging** (Exam 3 · Q43), (Exam 4 · Q7), (Exam 5 · Q27), (Exam 6 · Q10). Who did what → **Cloud Audit Logs** (Exam 3 · Q11).
- Request across microservices → **Trace**. Exceptions grouped → **Error Reporting**. CPU/memory per function → **Profiler** (Exam 3 · Q14), (Exam 3 · Q48), (Exam 3 · Q50).
- Live code state without downtime → **Debugger** (retired) (Exam 3 · Q1), (Exam 5 · Q26).
- Keep running if a component fails → **redundancy**, no single point of failure (Exam 4 · Q40). Outage ≠ data loss (Exam 1 · Q7).
- Scale fast + sustainability → **cloud provider with energy-efficient data centers** (Exam 6 · Q32).
- Fastest response + TAM → **Premium** support (Exam 3 · Q21).
