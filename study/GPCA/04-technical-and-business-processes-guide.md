# Domain 4 Study Guide — Analyzing and Optimizing Technical and Business Processes

> Condensed from the 38-question bank in [`04-technical-and-business-processes.md`](04-technical-and-business-processes.md). Citations look like (Exam N · QM). This domain is about process, not products: how code gets to production safely, how you prove a system survives failure, how you cut and track cost, and how you bring people along.

---

## 1. CI/CD pipelines and traceability

### Key facts
- The standard Google Cloud pipeline is **Cloud Build trigger → build and test → push image to Artifact Registry → deploy**. Builds start from a **trigger on source changes**, not from a scheduler that polls the repo (Exam 4 · Q48).
- **Tag images with the commit hash.** That links every deployed image to the exact code that produced it, which gives full auditability (Exam 3 · Q15), (Exam 4 · Q48). Dates, comments and `latest` don't do this: `latest` moves with every build and tells you nothing.
- For microservices, build **one image per microservice**, not one big image (Exam 4 · Q48).
- Images belong in a **container registry** (Artifact Registry), not in Cloud Storage (Exam 4 · Q48), (Exam 5 · Q4).
- **Container Registry** was shut down in 2025. Questions that say Container Registry mean **Artifact Registry** today (Exam 2 · Q59), (Exam 4 · Q48).
- To *enforce* that every change to a branch is built, tested and deployed automatically, use a **Cloud Build trigger** plus a **deployment pipeline** that deploys new images, and let **only the deployment tool** hold deploy permissions. Developer hooks and manual deploys can be skipped, so they enforce nothing (Exam 2 · Q59).
- Centralized, secure CI/CD for GKE and Cloud Run: **Cloud Build** with GitHub triggers, **Artifact Registry** (with vulnerability scanning) and **Binary Authorization** to block images that don't meet policy (Exam 5 · Q4). **Cloud Deploy** handles promotion between environments, but not without scanning.
- GitHub repo, deploy to Cloud Run on every merged PR: connect the repo with the **Cloud Build GitHub app** and create a trigger that builds and deploys (Exam 5 · Q69). No keys are stored anywhere.
- A good test order inside the pipeline: **unit tests first** (cheap, before building) → build and push the image → deploy to a **test environment** → **integration and acceptance tests** → deploy to production → **smoke tests** (Exam 5 · Q73).
- Verifying code before production with tags: build **staging tags** into a **staging environment**, test there, then tag for production (Exam 1 · Q42).

### Decision rules
- "Trace a deployment back to the code" → image tag = **commit hash** (Exam 3 · Q15).
- "Automatically build on every change" → **Cloud Build trigger**, never a polling scheduler (Exam 4 · Q48).
- "Enforce the process" → automated pipeline, and only the deploy tool has deploy rights (Exam 2 · Q59).
- "Centralized control + security scanning + consistent deploys" → Cloud Build + Artifact Registry + Binary Authorization (Exam 5 · Q4).
- "Run all tests in the pipeline" → unit → build → integration/acceptance in test env → prod → smoke (Exam 5 · Q73).

### Traps
- **Service account keys committed to a repo** are always wrong. If GitHub Actions must call Google Cloud, use Workload Identity Federation (Exam 5 · Q69).
- A **GitHub Enterprise** trigger is for GitHub Enterprise Server, not GitHub.com (Exam 5 · Q69).
- **Config Sync** syncs Kubernetes configuration from Git. It doesn't deploy Cloud Run services (Exam 5 · Q69).
- Running unit tests "locally" or "before committing" leaves them outside the pipeline, so they can be skipped (Exam 5 · Q73).
- Running acceptance tests *in production* is too late (Exam 5 · Q73).
- Deploying directly to production and testing there, or a red/black rollout with no staging step, doesn't verify the code first (Exam 1 · Q42).
- Vulnerability scanning checks for known CVEs. It doesn't test that the code works (Exam 2 · Q59).

---

## 2. Release strategies and testing

### Key facts
- **Blue-green** keeps the old version running beside the new one. Traffic switches only after validation, and rollback is a switch back (Exam 1 · Q5).
- **Microservices** shrink the blast radius. Each service deploys alone, so one bad change doesn't force a rollback of the whole platform (Exam 1 · Q5).
- **Canary** (gradual rollout): send a small share of real users to the new version first. It catches problems that only real production traffic shows, such as performance issues that staging never reproduced (Exam 1 · Q21).
- **Unit tests** check one component in isolation. They answer "does this microservice work on its own?" (Exam 5 · Q8). Integration tests check components together, end-to-end tests check whole user flows, and load tests check behavior under traffic.
- Moving to the cloud doesn't remove test types. It means **tests must scale well beyond the old approach**, because the platform scales well beyond it (Exam 4 · Q24).
- Load testing a new backend version: build a **scalable test environment in Google Cloud that emulates production load**, create it on demand and tear it down after (Exam 4 · Q25).
- Testing a mobile app across many Android and iOS devices and configurations: **Firebase Test Lab** runs it on real and virtual devices hosted by Google (Exam 4 · Q43).

### Comparison

| Strategy | What it protects against | Source |
|---|---|---|
| Blue-green | Bad release: instant switch back | (Exam 1 · Q5) |
| Canary | Problems that only appear with real traffic | (Exam 1 · Q21) |
| Microservices | Whole-platform rollbacks for one bad change | (Exam 1 · Q5) |
| Unit tests | Bugs inside one component | (Exam 5 · Q8) |
| Scalable load-test env | Failure at real production scale | (Exam 4 · Q25), (Exam 4 · Q24) |

### Decision rules
- "Fewer rollbacks, QA already improved" → **blue-green + microservices** (Exam 1 · Q5).
- "Prod problems not seen in staging" → **canary to a small subset of users** (Exam 1 · Q21).
- "Each microservice on its own" → **unit tests** (Exam 5 · Q8).
- "Test at scale, cost-effectively" → **ephemeral, scalable environment that emulates production** (Exam 4 · Q25).
- "Many mobile devices" → **Firebase Test Lab** (Exam 4 · Q43).

### Traps
- **Replacing QA with canaries** is wrong. Canaries add to testing; they don't replace it (Exam 1 · Q5).
- Database changes (less relational, move to NoSQL) don't reduce deployment rollbacks (Exam 1 · Q5).
- "Deploy fewer or smaller changes" is good hygiene but doesn't expose code to real load before full rollout (Exam 1 · Q21). "Increase load on staging" still misses real-world behavior.
- Dropping unit tests, testing only after release, or testing Google's infrastructure itself are all wrong (Exam 4 · Q24).
- **Static** high/medium/low environments waste money; **existing on-prem infrastructure** may not reach production scale (Exam 4 · Q25).
- Firebase **Hosting** serves web content. It doesn't test apps. You can't run iOS in VMs or containers on Google Cloud (Exam 4 · Q43).

---

## 3. Resilience testing, chaos engineering and disaster recovery drills

### Key facts
- **Resilience** means the system keeps working when parts fail. You test it by **causing failures on purpose**: shut down all VMs in a zone, kill random resources, inject latency or errors (Exam 2 · Q19), (Exam 1 · Q20).
- Opening a system to many more users while keeping a 99.99% SLA: **expand exposure gradually** (a bigger group each day) until autoscaling triggers on all layers, and at the same time **terminate random resources in both zones** (Exam 1 · Q20). That is load plus chaos, with real traffic.
- A replica that never got promoted during a crash means failover was never exercised. Fix: **routinely scheduled failovers** (Exam 1 · Q23). A failover you never test is a failover you don't have.
- Testing an authentication layer (regional MIG + Cloud SQL): **schedule a disaster simulation that shuts down all VMs in a zone** and watch how the application behaves (Exam 2 · Q19).
- Simulating one microservice failing on GKE: use **fault injection** in the service mesh (Istio, now offered by Google as **Cloud Service Mesh**). It can inject delays or abort requests for one service only (Exam 3 · Q9).
- Testing resilience to **mobile network latency**: **failure injection software** in the platform that adds latency to client traffic. It is controlled and repeatable (Exam 4 · Q33).
- DR test procedures: **automate provisioning** so each test is repeatable, and **monitor and debug** with Cloud Monitoring and Cloud Logging (formerly Stackdriver) (Exam 2 · Q32). The question names Deployment Manager, which reached end of support in March 2026; today use Terraform or **Infrastructure Manager**.
- Hybrid DR connectivity: **Dedicated Interconnect** carries replication, and **Cloud VPN** is the secure backup path if the Interconnect fails (Exam 2 · Q17).
- **Penetration tests** can be automated in the release flow. HRL's weekly pen test runs after each Tuesday release: the **deployment job publishes to Pub/Sub**, which triggers the test function (Exam 4 · Q13). You don't need to ask Google before pen testing your own projects, but you must follow the Acceptable Use Policy.

### Decision rules
- "Resilience test" → **break something on purpose** (zone shutdown, random termination, fault injection), not security tooling (Exam 2 · Q19).
- "Replica wasn't promoted" → **scheduled failover drills** (Exam 1 · Q23).
- "Simulate a microservice failure on GKE" → **Istio / Cloud Service Mesh fault injection** (Exam 3 · Q9).
- "Resilience to latency" → **inject latency** (Exam 4 · Q33).
- "Secure backup for Interconnect" → **Cloud VPN** (Exam 2 · Q17).
- "Run something after every release" → have the **release pipeline publish an event** (Exam 4 · Q13).

### Traps
- **Intrusion detection** and **dark-web scraping** are security controls, not resilience tests (Exam 2 · Q19).
- A **read replica in another zone** with a manual failover tests the database, not the whole auth layer. Cloud SQL HA uses a standby instance, not a read replica (Exam 2 · Q19).
- Bigger instances, more snapshots or a different database don't fix an untested failover (Exam 1 · Q23).
- **Direct Peering** reaches Google public services and isn't a private, encrypted backup path. **Transfer Appliance** is an offline device for bulk moves, not replication (Exam 2 · Q17).
- **Taints/anti-affinity** move pods; **deleting a node** tests node loss; **traffic shifting** avoids the failure instead of simulating it (Exam 3 · Q9).
- Replaying recorded load and over-provisioning to 200% doesn't test failure at all (Exam 1 · Q20). Killing a whole zone while also scaling up is a different test from the one asked.
- A delay before processing uploaded files tests the wrong thing; an opt-in beta measures latency but can't control it (Exam 4 · Q33).
- Activity (Audit) Logs record who did what. They aren't the tool to monitor and debug a DR test (Exam 2 · Q32).

---

## 4. Cutting compute costs

### Key facts
- **Stop what's idle.** Dev and test VMs used only in office hours should be stopped outside them. A stopped VM bills nothing for vCPU and memory; its persistent disks still bill (Exam 5 · Q57), (Exam 2 · Q46).
- Compute Engine has built-in **instance schedules** that start and stop VMs on a cron-like schedule (Exam 5 · Q57). An older pattern is **Cloud Scheduler → Cloud Run function → stop/start** (Exam 2 · Q46). Both are correct answers.
- Dev VMs that start and stop many times a day and need state: keep state on **persistent disks** and **stop** the VM rather than delete it. `--no-auto-delete` keeps a disk even if the VM is deleted (Exam 1 · Q6), (Exam 2 · Q60).
- **Rightsizing**: start with a machine like the on-prem one, install the **Ops Agent** (the question says "Cloud Monitoring agent") so memory is measured, run **normal** traffic, and follow the **machine type (rightsizing) recommendations** (Exam 3 · Q29). Recommendations need about 8 days of data.
- **Idle VM recommender** finds zombie VMs: `gcloud recommender recommendations list --recommender=google.compute.instance.IdleResourceRecommender` (Exam 4 · Q16).
- GKE costs: **HorizontalPodAutoscaler** for stateless (and compatible stateful) workloads plus **cluster autoscaler** removes unneeded nodes without losing availability (Exam 3 · Q36).
- Discounts: **sustained use discounts** apply automatically with no commitment, so they suit **uncertain demand**. **Committed use discounts** need a 1- or 3-year commitment and suit steady, predictable use (Exam 1 · Q41). SUDs cover only some machine families (N1, N2, N2D, C2 and a few others), not E2 or newer series.
- For a startup with uncertain demand: **free tier + sustained use discounts + cost management training** for the whole team, rather than one dedicated cost person (Exam 1 · Q41).

### Decision rules
- "Idle outside office hours" → **schedule stop/start** (Exam 5 · Q57), (Exam 2 · Q46).
- "Unsure of the right size, steady usage" → **one similar VM + agent + normal load + rightsizing recommendations** (Exam 3 · Q29).
- "Find idle VMs fast" → **`gcloud recommender`** (Exam 4 · Q16).
- "Cut GKE cost, keep availability" → **HPA + cluster autoscaler** (Exam 3 · Q36).
- "Uncertain demand" → **SUDs, not CUDs** (Exam 1 · Q41).

### Traps
- **3-year CUDs** on idle machines lock in waste; a newer machine series doesn't remove idle time; a **MIG with autoscaling** doesn't scale to zero for a single dev workstation (Exam 5 · Q57).
- A **script on a production instance** couples dev cost control to prod; **preemptible VMs** can be reclaimed during office hours (Exam 2 · Q46).
- **Auto-delete** disks or **local SSD** lose state; snapshot-and-terminate cycles add needless work (Exam 1 · Q6), (Exam 2 · Q60).
- Rightsizing from **high-traffic** load tests over-sizes the machine; the **smallest machine + autoscaling** isn't rightsizing (Exam 3 · Q29).
- An `idle: true` **label** doesn't exist unless someone set it; health checks show unhealthy VMs, not idle ones (Exam 4 · Q16).
- **Preemptible/Spot node pools** for stateful workloads lose availability; namespace limits alone don't reduce cost; splitting into two clusters adds overhead (Exam 3 · Q36).

---

## 5. Cost visibility and FinOps decisions

### Key facts
- **Labels** (and tags) on resources + **Cloud Billing export to BigQuery** = cost reports by team, environment or app with SQL (Exam 1 · Q6), (Exam 2 · Q60).
- Labels are fixed key/value metadata such as `env=dev` or `team=payments`. A "CPU utilization label" is not a thing (Exam 1 · Q6).
- Planning a migration with cost control in mind: **consistent labels and tags** on everything, and **infrastructure as code** so every resource is created the same way, reviewed and labeled (Exam 5 · Q46).
- BigQuery on-demand cost **per user and per query** in near real time: a **Cloud Logging sink** that exports **BigQuery Data Access logs to BigQuery**, then query them with SQL (Exam 4 · Q1). The billing export doesn't show which user ran which query. (The `INFORMATION_SCHEMA.JOBS` views also show bytes billed per user.)
- Engineers want Spanner, FinOps says it's too expensive: build a **total cost of ownership (TCO)** analysis that includes the operational effort of running a database yourself, and review it together in a workshop (Exam 5 · Q33). Data settles disagreements; the architect facilitates.
- **CapEx vs OpEx**: on-prem hardware is capital spend up front; cloud is operating spend that follows use. That's why stopping idle resources saves money in the cloud.

### Decision rules
- "Finance needs cost by group" → **labels + billing export to BigQuery** (Exam 1 · Q6), (Exam 2 · Q60).
- "Track and control costs after migration" → **labels/tags + IaC** (Exam 5 · Q46).
- "Which BigQuery users cost the most" → **Data Access logs sink → BigQuery** (Exam 4 · Q1).
- "Teams disagree about cost vs managed service" → **TCO + workshop** (Exam 5 · Q33).

### Traps
- Labels on a **dataset** don't attribute query cost to users; the billing export has no per-user breakdown (Exam 4 · Q1).
- Logs to **Cloud Storage + Dataflow** works but is heavier than querying them in BigQuery (Exam 4 · Q1).
- **Billing export to Cloud SQL** isn't a supported destination; Backup and DR and service alerts don't track cost (Exam 5 · Q46).
- Picking a side (a PostgreSQL MIG design, a Cloud SQL "middle ground", or citing the Well-Architected Framework to justify Spanner) skips the decision process the question asks for (Exam 5 · Q33).

---

## 6. Stakeholders, skills and change

### Key facts
- **Business risks** of moving to a new tool are about people and the vendor: the team **doesn't know it yet**, and it **could be deprecated** (Exam 1 · Q28). That risk came true: Deployment Manager reached end of support in March 2026; Terraform and **Infrastructure Manager** replace it.
- **Skills gaps**: when the goal is cost optimization and the team already has some experience, **budget for training** and a **role-based certification roadmap**. Consultants cost more and leave no skills behind; deadlines don't close gaps (Exam 1 · Q59).
- **Safe experimentation**: a request process that creates a **sandbox project** per technology, with **only the needed APIs**, **lower quotas**, **narrow IAM roles**, and **automatic deletion** after a set time (Exam 5 · Q30). Guardrails stop sandboxes from becoming shadow production.
- **Justifying a re-architecture to leadership**: talk about outcomes. Microservices on managed services **decouple infrastructure from the app**, ship features faster, make CI/CD easier, enable **A/B testing** and **scale on demand** (Exam 3 · Q12).
- **Facilitation**: when a developer says the app uses **WebSockets** and **sessions stored on each server**, it can still run on Google Cloud. Load balancers support WebSockets, and **session affinity** keeps a user on one backend. Set up a talk between the developer and the **cloud operations team** about load balancing options rather than forcing a redesign (Exam 3 · Q33).
- **Root cause from code**: an app on App Engine that keeps sessions in a **global in-memory variable** works with one instance, then breaks under load when autoscaling adds instances, because each instance has its own copy. Users see old articles again. Store session state in a shared service such as **Memorystore** or **Firestore** (Exam 4 · Q50).

### Decision rules
- "Business risk of adopting tool X" → **unfamiliar to staff** + **vendor may deprecate it** (Exam 1 · Q28).
- "Skills gap, cost goal" → **training budget + certification roadmap** (Exam 1 · Q59).
- "Let teams experiment safely" → **automated, scoped, time-limited sandbox projects** (Exam 5 · Q30).
- "Convince leadership" → **business outcomes** (speed, scale, A/B testing), not technical steps (Exam 3 · Q12).
- "Developer worried about compatibility" → **bring in the right team and discuss options** (Exam 3 · Q33).
- "Works at low load, wrong data at peak" → **per-instance state** (Exam 4 · Q50).

### Traps
- "Uses Python", "needs a service account", "can delete resources" or "only manages Google Cloud" are technical facts, not business risks (Exam 1 · Q28).
- **Full permissions** in a sandbox with a polite request to stay in scope is no guardrail; Project Creator for everyone on a shared billing account invites shadow IT; a **separate organization** with full access per person is the same problem (Exam 5 · Q30).
- "We can containerize it" or "Migrate to Virtual Machines can automate it" are *how*, not *why* (Exam 3 · Q12). Claiming it will be cheaper is not guaranteed.
- Rewriting WebSockets to HTTP streaming, or forcing distributed sessions, is unnecessary work (Exam 3 · Q33).
- Caching headers or URL changes don't explain per-user repeated content; nothing in the code writes to Datastore (Exam 4 · Q50).

---

## ⚠️ Questionable answers

| Item | Issue |
|---|---|
| **(Exam 2 · Q32)** | The key uses **Deployment Manager**, which reached end of support in March 2026, and **Stackdriver**, now Cloud Monitoring and Cloud Logging. The principle (automated provisioning + observability) still holds. Pick the IaC tool + Cloud Monitoring answer. |
| **(Exam 1 · Q28)** | Written when deprecation was hypothetical. It has since happened, which makes the key stronger, but newer versions may ask about Terraform or Infrastructure Manager instead. |
| **(Exam 4 · Q13)** | "Weekly" could also be met with Cloud Scheduler. The key ties the test to the Tuesday release via Pub/Sub, so the test always runs on the new version. Answer the key. HRL is a legacy case study. |
| **(Exam 4 · Q33)** | Option B (test clients across regions) also simulates latency. The key prefers failure injection because it controls the latency precisely. Answer the key. |
| **(Exam 2 · Q46)** | Compute Engine instance schedules now start and stop VMs without code; Cloud Scheduler + a function is the older pattern. Either is right if offered. |

---

## Last-minute cheat sheet

- Trace deploy → code: **image tag = commit hash** (Exam 3 · Q15), (Exam 4 · Q48).
- CI: **Cloud Build trigger**, not a polling scheduler; images in **Artifact Registry** (formerly Container Registry) (Exam 4 · Q48), (Exam 2 · Q59).
- Enforce the process: automated pipeline, **only the deploy tool can deploy** (Exam 2 · Q59).
- Secure CI/CD: **Cloud Build + Artifact Registry + Binary Authorization** (Exam 5 · Q4).
- GitHub → Cloud Run on merge: **Cloud Build GitHub app + trigger**; never commit keys (Exam 5 · Q69).
- Test order: **unit → build → integration/acceptance → prod → smoke** (Exam 5 · Q73).
- Verify before prod: **staging tag → staging env → production tag** (Exam 1 · Q42).
- Fewer rollbacks: **blue-green + microservices** (Exam 1 · Q5). Prod-only issues: **canary** (Exam 1 · Q21).
- One microservice alone: **unit test** (Exam 5 · Q8). Many devices: **Firebase Test Lab** (Exam 4 · Q43).
- Load test: **scalable, prod-like env in Google Cloud**; tests must scale beyond the old ones (Exam 4 · Q25), (Exam 4 · Q24).
- Resilience: **gradual exposure + random termination** (Exam 1 · Q20); **zone shutdown drill** (Exam 2 · Q19).
- Replica not promoted: **scheduled failovers** (Exam 1 · Q23).
- GKE microservice failure: **Istio / Cloud Service Mesh fault injection** (Exam 3 · Q9). Latency: **inject latency** (Exam 4 · Q33).
- DR tests: **IaC provisioning + Cloud Monitoring/Logging** (Exam 2 · Q32). Interconnect backup: **Cloud VPN** (Exam 2 · Q17).
- Pen test after each release: **deploy job → Pub/Sub → function** (Exam 4 · Q13).
- Idle off-hours: **schedule stop/start** (Exam 5 · Q57), (Exam 2 · Q46). Keep state: **persistent disk + stop** (Exam 1 · Q6), (Exam 2 · Q60).
- Right size: **similar VM + agent + normal load + recommendations** (Exam 3 · Q29). Zombies: **idle VM recommender** (Exam 4 · Q16).
- GKE cost: **HPA + cluster autoscaler** (Exam 3 · Q36). Uncertain demand: **SUDs + training** (Exam 1 · Q41).
- Cost by group: **labels + billing export to BigQuery** (Exam 1 · Q6), (Exam 2 · Q60); migration: **labels/tags + IaC** (Exam 5 · Q46).
- BigQuery cost per user: **Data Access logs sink → BigQuery** (Exam 4 · Q1).
- Cost disagreement: **TCO + workshop** (Exam 5 · Q33).
- Tool business risk: **unfamiliar + deprecation** (Exam 1 · Q28). Skills gap: **training + cert roadmap** (Exam 1 · Q59).
- Sandboxes: **scoped APIs, low quotas, narrow IAM, auto-delete** (Exam 5 · Q30).
- Pitch to leadership: **speed, A/B tests, scale on demand** (Exam 3 · Q12). Developer concern: **meet with cloud ops about LB options** (Exam 3 · Q33).
- Wrong data under load: **in-memory state per instance** → shared store (Exam 4 · Q50).
