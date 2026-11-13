# Domain 5 — Optimizing Performance and Cost

23 questions. Answers are collapsed — try each question before expanding it.

## Quick-review: memory hooks

- If a workload’s architecture already assumes nodes can vanish without breaking it (quorum, replication, statelessness with external coordination), it’s a Spot VM candidate; if losing a node loses real work or breaks an SLA, it isn’t. *(Q1.5)*
- Steady, predictable, must-not-fail capacity means commit for a discount; interruptible capacity means Spot VMs; groups manage instances but do not discount them. *(Q1.30)*
- For cheaper user-facing egress, change the network tier, not the network layout. *(Q1.41)*
- “Resource utilization, no setup needed” — Cloud Run’s CPU/memory metrics are already in Cloud Monitoring by default; reach for Trace or Profiler only when the question is about latency or code hotspots instead. *(Q2.6)*
- One region and local users mean Standard Tier with a regional load balancer, because global load balancers require Premium Tier. *(Q2.24)*
- Label the resource, export the bill, and group the cost by label. *(Q2.48)*
- Before tuning autoscaling, pre-provisioning compute, or updating a DR runbook — measure first. Load test to find out how the system actually scales. *(Q2.59)*
- Stable demand with changing regions favors flexible commitments; add reservations when capacity assurance is required. *(Q3.45)*
- Resumable processing with flexible deadlines is a strong candidate for Spot VMs. *(Q3.54)*
- Bandwidth caps are per-instance (vCPU-based), not per-NIC — to raise the ceiling, scale the machine type, not the interface count. *(Q4.14)*
- Profiler shows memory, not CPU, climbing until restart → raise the container’s own memory limit; more node memory or a tracing tool doesn’t touch the limit that’s actually triggering the kill. *(Q4.29)*
- For slow code paths in production with minimal overhead, use Cloud Profiler, because metrics show that a resource is busy and profiles show which code is using it. *(Q4.42)*
- “Big gap, give it CPU. Small gap plus a shrinking budget, fix the code.” *(Q4.45)*
- “Before you build your own dashboard-and-judgment process, check whether a recommender already does the sizing for you.” *(Q4.58)*

## Questions

### Exam 1 · Q5

Your organization wants to lower Compute Engine spend, and after evaluating the options, you decide to use Spot VMs for part of the workload. Which of the following applications is best suited to run on Spot VMs?

- A. A horizontally scalable in-memory caching system.
- B. The organization’s public-facing website.
- C. A distributed, eventually consistent NoSQL database cluster with sufficient quorum.
- D. A GPU-accelerated video-rendering platform that reads source files from and writes rendered output to a storage bucket.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. A distributed, eventually consistent NoSQL database cluster with sufficient quorum.

**Correct Answer**

**C. A distributed, eventually consistent NoSQL database cluster with sufficient quorum.**

**Exam Reasoning Explanation**

The hard constraint behind every Spot VM decision is fault tolerance: Spot VMs can be reclaimed by Google Cloud at any time with minimal notice, so the workload must be able to absorb the sudden loss of one or more nodes without an interruption in service or loss of data. Each option needs to be evaluated against that bar. A quorum-based, eventually consistent distributed database is explicitly designed for this: it tolerates the loss of individual nodes as long as enough replicas remain to satisfy quorum, and the remaining nodes keep serving reads/writes while the cluster heals. That property — architected redundancy that absorbs node loss gracefully — is exactly what Spot VM eligibility requires, and it’s the one option here that has it built in by design (“sufficient quorum” is stated explicitly).

**Key Exam Clues**

  * “distributed, eventually consistent... with sufficient quorum” is the decisive technical signal — it states outright that the architecture tolerates losing individual nodes without breaking availability or consistency guarantees.

  * “scalable in-memory caching system” is a preference/ambiguous signal, not a hard constraint — scalability alone says nothing about whether losing a cache node causes a correctness problem or just a performance dip, so it needs more information than is given to be confidently fault-tolerant.

  * “public-facing website” and “retrieves and stores videos in a storage bucket” are both exclusion signals once examined: a public-facing site typically needs continuous availability (ruling out unannounced interruption), and a GPU render job mid-frame has in-progress compute state that external bucket storage doesn’t protect unless the job is explicitly checkpointed — which isn’t stated.

**Why This Is Correct**

Spot VMs are intended for workloads that are interruption-tolerant: batch processing, fault-tolerant distributed systems, and horizontally scalable services where losing an individual instance doesn’t jeopardize the overall system’s correctness or availability. A NoSQL cluster built with quorum-based replication is the textbook example — losing a node (because it was preempted) simply means the cluster operates with one fewer replica until a new node rejoins, while quorum ensures reads and writes remain consistent and available throughout. This makes it uniquely well-matched to Spot VMs’ core trade-off: significant cost savings in exchange for the possibility of sudden, uncoordinated instance termination.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** A caching system being “scalable” doesn’t by itself guarantee it tolerates node loss safely — many caching layers treat a lost node as cache data loss requiring expensive cache-miss recomputation or even serving stale/absent data to the application, and the question gives no indication the cache has quorum, replication, or warm-standby behavior equivalent to the NoSQL cluster’s explicit quorum guarantee. Without that stated property, it’s a weaker fit than C.

  * **Option B — Violates Requirement:** A production-facing website generally has an availability expectation that directly conflicts with Spot VMs’ lack of an SLA and the possibility of simultaneous, uncoordinated preemption across instances — user-facing traffic shouldn’t be exposed to that risk as the primary serving layer.

  * **Option D — Violates Requirement:** Reading inputs from and writing outputs to a storage bucket protects data-at-rest, but it does nothing for an in-progress GPU render job: if the instance is preempted mid-render, that render’s progress is lost and must restart from the beginning (GPUs attached to preemptible/Spot instances only persist for the life of the instance), making this workload interruption-costly unless the question specified checkpoint/resume logic, which it doesn’t.

**Exam Trap**

The trap is assuming “stores data in durable storage” is sufficient for Spot VM eligibility (Option D) — durability of inputs/outputs is not the same as fault tolerance of in-flight compute work. The distinguishing signal the exam wants you to catch is whether the _in-progress state of the workload itself_ survives a node being pulled out from under it, which only the quorum-based database explicitly guarantees here.

**Foundation Concept**

Spot VM suitability hinges on one question: if this instance disappears right now, does the system keep working correctly? Workloads with built-in redundancy and graceful degradation (quorum-based clusters, horizontally scalable stateless services, restartable batch jobs) say yes; workloads with irreplaceable in-flight state or hard availability requirements (user-facing production traffic, long-running unsaved compute) say no.

**Real-World Connection**

Teams commonly run distributed data stores’ replica nodes on Spot VMs specifically because the replication/quorum layer already exists to handle planned maintenance and hardware failures — Spot preemption is just another instance of the same failure mode the system was built to tolerate — turning an existing resilience investment directly into cost savings, often in the 60-90% range versus standard VM pricing.

**Memory Hook**

If a workload’s architecture already assumes nodes can vanish without breaking it (quorum, replication, statelessness with external coordination), it’s a Spot VM candidate; if losing a node loses real work or breaks an SLA, it isn’t.

**30-Second Exam Takeaway**

When matching workloads to Spot VMs, look past “has durable storage” or “is scalable” and ask specifically whether the stated architecture tolerates losing an individual node mid-operation without data loss or availability impact — a quorum-based distributed system states that tolerance explicitly and is the strongest match.

**Official References**

[**Google Cloud — Spot VMs overview:**](https://cloud.google.com/compute/docs/instances/spot) Supports: the correct-answer mechanism (Spot VMs can be reclaimed at any time, making fault-tolerant/interruption-tolerant workloads the right fit) and the terminology update from the legacy Preemptible VM model

[**Google Cloud — Preemptible VM instances (legacy) and GPU preemption behavior:**](https://docs.cloud.google.com/compute/docs/instances/preemptible) Supports: the distractor elimination for Option D — GPUs on preemptible/Spot instances persist only for the life of the instance, so in-progress render work is lost on preemption

</details>

---

### Exam 1 · Q30

You need to run a business-critical workload on a fixed set of Compute Engine instances for the next several months. The workload is stable, and the instances are provisioned with exactly the resources it needs. You want to reduce the cost of running this workload without affecting its performance. What should you do?

- A. Buy committed use discounts for the instances.
- B. Move the instances into a managed instance group.
- C. Convert the instances to Spot VMs.
- D. Place the instances in an unmanaged instance group.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Buy committed use discounts for the instances.

**Correct Answer**

**A. Buy committed use discounts for the instances.**

**Exam Reasoning Explanation**

Start with the two hard constraints: the cost must go down, and performance must not change. The workload is also described as business-critical, stable, and fixed in size, so interruption and resizing are both unwanted. Now test each option on one question: does it change the price, and does it leave the VMs running exactly as they are? Only a committed use discount changes the price while leaving the running instances untouched. The group options change how instances are organized, not what they cost, and Spot VMs lower the price by accepting interruption, which this workload cannot tolerate.

**Key Exam Clues**

  * **“lower the costs”** (hard constraint): the chosen action must change pricing, not just management.

  * **“without any performance implications”** (hard constraint): the instances must keep running as they do today, with no interruption risk.

  * **“business-critical”** (exclusion): it rules out any capacity that Compute Engine can reclaim at any time.

  * **“stable with the exact amount of resources allocated” and “fixed set of instances”** (technical signal): steady, predictable usage is the exact profile that committed use discounts are designed to reward.

**Why This Is Correct**

Committed use discounts (CUDs) trade a commitment for lower prices on Compute Engine usage. Resource-based commitments are described as ideal for predictable, steady-state usage, which matches this workload. Because the instances need exactly the resources already allocated, the commitment can be sized to match them. A commitment is a pricing arrangement applied to usage, so the instances themselves are unchanged and performance is unaffected. The discount comes from the billing side alone.

**Why the Other Options Are Not the Best Fit**

**Option B — Different Use Case.** Managed instance groups provide autoscaling, autohealing, and automated updates for groups of identical VMs built from an instance template. That is valuable for scalable or self-healing workloads. It is tempting because MIGs are a recommended practice. It lowers no price, though, and migrating a fixed, stable fleet into a MIG adds change without a cost benefit.

**Option C — Violates Requirement.** Spot VMs offer large discounts, and they are the current successor to preemptible VMs, which makes this option attractive for a pure cost goal. Compute Engine can preempt Spot VMs at any time, and they are excluded from the Compute Engine SLA. That directly conflicts with a business-critical workload and the “no performance implications” requirement.

**Option D — Different Use Case.** An unmanaged instance group only collects VMs you manage yourself so they can be load balanced as a unit. It has no effect on pricing, so it does not address the goal.

**Exam Trap**

The strongest distractor is Option C, because Spot VMs are the best-known way to cut Compute Engine costs steeply. The resolving distinction is that the discount comes from accepting interruption, which this workload cannot afford. Spot VMs would become the right answer if the workload were fault-tolerant, such as a restartable batch job. One production caveat: CUD terms are 1 year or 3 years, with the longer term giving the bigger discount, so before buying you would confirm the workload will run for the commitment term. The exam treats the stable, fixed profile as the deciding signal.

**Foundation Concept**

Cloud cost optimization separates two levers. Pricing models change what you pay for the same capacity, and architecture or operations choices change how capacity is organized and managed. Steady, predictable capacity suits commitment-based pricing. Interruptible capacity such as Spot VMs suits fault-tolerant work. Grouping constructs like managed and unmanaged instance groups address availability and operations, not price. Spot VMs are the current successor to preemptible VMs, so the same trade-off of low cost for reclaim risk applies.

**Real-World Connection**

A team running a long-lived, always-on service on a fixed fleet reviews its steady usage, then purchases a resource-based commitment that matches the vCPU and memory it consistently uses in a region and project. The discount applies automatically to matching usage, the VMs keep running unchanged, and the monthly bill drops. The trade-off is the commitment itself, which is why it is sized to the stable baseline rather than to peak or uncertain demand. A commitment alone does not reserve capacity in a zone; reservations can be attached if guaranteed capacity is also needed.

**Memory Hook**

Steady, predictable, must-not-fail capacity means commit for a discount; interruptible capacity means Spot VMs; groups manage instances but do not discount them.

**30-Second Exam Takeaway**

When a question asks how to lower Compute Engine cost for a stable, always-on, business-critical workload without risking performance, choose committed use discounts. Reject Spot VMs for anything that cannot tolerate interruption, and reject instance-group options because they change management, not price.

**Official References**

[Google Cloud: Committed use discounts overview (Compute Engine): ](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)Supports: the correct answer, covering CUDs as discounted prices in return for 1-year or 3-year commitments, and commitments as a pricing agreement that does not by itself reserve capacity.

[Google Cloud: Spot VMs: ](https://docs.cloud.google.com/compute/docs/instances/spot)Supports: the elimination of Option C, covering Spot VMs as the latest version of preemptible VMs, preemptible at any time, and excluded from the Compute Engine SLA.

[Google Cloud: Instance groups (managed and unmanaged): ](https://docs.cloud.google.com/compute/docs/instance-groups)Supports: the elimination of Options B and D, covering MIGs as autoscaling, autohealing, and update tooling for identical VMs, and unmanaged groups as a way to load balance VMs you manage yourself.

</details>

---

### Exam 1 · Q41

You are responsible for the backend of a mobile game that runs on a Google Kubernetes Engine (GKE) cluster, and the application serves HTTP requests from players. You need to put a solution in place that lowers the network cost. What should you do?

- A. Set up the VPC network as a Shared VPC host project.
- B. Set up your network services to use the Standard Network Service Tier.
- C. Set up your Kubernetes cluster as a private cluster.
- D. Set up an external Application Load Balancer as the Ingress.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Set up your network services to use the Standard Network Service Tier.

**Correct Answer**

**B. Set up your network services to use the Standard Network Service Tier.**

**Exam Reasoning Explanation**

The single requirement is lower network cost for a workload that serves HTTP traffic to internet users. Treat the options as levers and ask which one changes what you pay for traffic between your service and the internet. Shared VPC, private clusters, and a load balancer Ingress each solve a different problem, such as administration, isolation, or traffic distribution, and none of them is priced as a cost reduction on user-facing traffic. Network Service Tiers is the one lever whose purpose is to trade performance for cheaper egress. That elimination leaves one decision.

**Key Exam Clues**

  * **“Reduce the network cost”** is a hard constraint. It is the only goal, so the answer must change how traffic is priced.

  * **“Serving HTTP requests from users”** is a technical signal. Responses to users leave Google Cloud as internet egress, which is where tier pricing applies.

  * **“Mobile phone game”** is a context signal. It implies user traffic over the internet, not internal service-to-service traffic.

**Why This Is Correct**

Network Service Tiers lets you choose how traffic between the internet and your Google Cloud resources is carried. Premium Tier, the default, uses Google’s global backbone and costs more. Standard Tier routes traffic over regular ISP transit networks, which is priced lower. Because the game’s backend sends responses to players as internet egress, moving to Standard Tier directly reduces that cost. Two boundaries apply. Standard Tier gives lower performance and availability than Premium, and it is regional, so it fits workloads where higher latency is tolerable. Premium is used by default unless you choose otherwise.

**Why the Other Options Are Not the Best Fit**

**Option A — Different Use Case:** A Shared VPC host project lets multiple projects share one network for centralized administration and policy. It is tempting because it is a networking feature in an organizational setting. It changes how networks are managed, not how internet egress is priced, so it does not reduce this cost.

**Option C — Different Use Case:** A private cluster gives nodes internal IP addresses only, which improves security by reducing exposure. It is tempting because it sounds like a network configuration choice. It does not lower the price of egress to users, and it can add cost, for example for NAT to reach the internet.

**Option D — Different Use Case:** An external Application Load Balancer as Ingress distributes HTTP traffic and gives routing and scaling features. It is tempting because the workload serves HTTP. It does not make egress cheaper and has its own charges, so it is a traffic management choice rather than a cost reduction.

**Exam Trap**

The strongest distractor is option D, because an HTTP load balancer is the standard front door for HTTP workloads on GKE and feels like an optimization. The distinction is that it improves distribution and availability, not the price per gigabyte of egress. The answer would switch only if the question asked about balancing traffic or global routing. A second trap is assuming Standard Tier is free of trade-offs. It reduces cost by giving up the performance of Google’s backbone, which is acceptable here because cost is the stated priority.

**Foundation Concept**

Cloud network cost is driven mostly by egress to the internet, and the route traffic takes determines the price. Carrying traffic over a provider’s private backbone costs more than handing it to the public internet early. A cost question about user-facing traffic therefore points to routing and pricing choices, not to access control or administration. This model applies to internet egress. Internal traffic between services in the same region follows different pricing, and security or organizational features rarely change any of it.

**Real-World Connection**

A team running a regional game backend switches its external addresses and load balancing to Standard Tier. Egress charges to players drop, and the team accepts slightly higher latency and lower availability targets in exchange. If players are spread worldwide and latency matters for gameplay, they would measure the effect first and might keep Premium for latency-sensitive paths while using Standard elsewhere.

**Memory Hook**

For cheaper user-facing egress, change the network tier, not the network layout.

**30-Second Exam Takeaway**

When a question asks to cut network cost for internet-facing traffic, look for the routing and pricing option, which is Standard Tier. Reject features that solve administration, isolation, or traffic distribution.

**Official References**

[**Google Cloud — Network Service Tiers overview:**](https://docs.cloud.google.com/network-tiers/docs/overview) Supports: Premium Tier optimizing for performance and Standard Tier optimizing for cost, which supports option B and its performance trade-off.

[**Google Cloud — Network Service Tiers pricing:**](https://cloud.google.com/network-tiers/pricing) Supports: Standard Tier egress being priced differently from Premium Tier egress, which is the cost mechanism behind option B.

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 5, Optimizing performance and cost):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with infrastructure cost planning that explicitly names network tiers.

</details>

---

### Exam 2 · Q6

You’ve built a serverless application on Cloud Run and deployed it to production. You want to understand the application’s resource utilization so you can make cost-optimization decisions. What should you do?

- A. Use Cloud Trace’s distributed tracing capability to monitor the application’s resource utilization.
- B. Use Cloud Profiler together with Ops Agent to monitor the application’s CPU and memory utilization.
- C. Use Cloud Monitoring to track the application’s container-level CPU and memory utilization.
- D. Use Google Cloud Observability to create logs-based metrics that monitor the application’s resource utilization.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Use Cloud Monitoring to track the application’s container-level CPU and memory utilization.

**Correct Answer**

**C. Use Cloud Monitoring to track the application’s container-level CPU and memory utilization.**

**Exam Reasoning Explanation**

The requirement is to see _resource utilization_ (CPU and memory) for a _Cloud Run_ service, in order to drive cost decisions, with the implicit preference of using what’s already available rather than adding tooling. Walking requirement → capability: Cloud Run is automatically and natively integrated with Cloud Monitoring, which already collects container CPU utilization and container memory utilization for every revision with zero setup. That single fact resolves the question — no agent to install, no code to instrument, no custom metric to build. The other three options each reach for a tool built for a different job (request-path latency, code-level hotspot profiling, or log-derived custom metrics) when the data needed is already a standard, built-in metric.

**Key Exam Clues**

  * “serverless application... Cloud Run” — a setup constraint: the solution should fit a fully managed environment where you don’t control or access underlying VMs.

  * “identify the resource utilization... for cost optimization” — a hard constraint: the goal is CPU/memory usage data specifically, not latency breakdowns or code-level hotspots.

  * “deployed to your production environment” — implies a solution that works passively, without modifying running application code.

  * Each distractor names a real Google Cloud tool, but tied to the wrong kind of signal (trace = latency, profiler = code hotspots, logs-based metrics = custom/derived data) rather than the native utilization metric itself.

**Why This Is Correct**

Cloud Run ships with built-in integration into Cloud Monitoring: as soon as a service or revision runs, metrics including container CPU utilization and container memory utilization are captured automatically and are visible both on the Cloud Run console pages and in Cloud Monitoring’s Metrics Explorer, with no agent installation or code changes required (since Cloud Run is fully managed, there’s no VM to install an agent on in the first place). Those exact metrics are what’s needed to judge whether a service’s configured CPU/memory allocation is over- or under-provisioned — the foundation of a cost-optimization decision for a serverless workload.

**Why the Other Options Are Not the Best Fit**

**Option A — _Different Use Case_.** Cloud Trace’s distributed tracing captures request latency as it flows through a request’s call graph — it tells you _where time goes_ , not how much CPU or memory a container is consuming. It’s the right tool for diagnosing slow requests, not for sizing compute resources.

**Option B — _Incorrect / Violates Requirement_. **Cloud Profiler is a continuous, statistical profiler that attributes CPU and memory _allocation_ to specific lines of application code, and it requires a language-specific profiling agent built into the application itself — not Ops Agent, which is a host-level telemetry agent installed on Compute Engine VMs (or similar hosts) to collect system logs and metrics. Cloud Run doesn’t expose the underlying VM for you to install Ops Agent on, so this pairing doesn’t apply to the scenario. Even where Cloud Profiler is used with Cloud Run, it’s aimed at code-level optimization, not service-level cost sizing.

**Option D — _Technically Possible but Not Best_.** Logs-based metrics are the documented way to derive _custom_ metrics from log content when the data you need isn’t already captured as a metric. CPU and memory utilization for Cloud Run are already first-class, built-in Cloud Monitoring metrics, so manufacturing them from logs would be redundant extra engineering effort for data that’s already available directly.

**Exam Trap**

The trap is picking a tool because it’s plausible for “observability” in general, without checking whether it produces the _specific_ data type asked for. Trace, Profiler, and logs-based metrics are all legitimate, frequently-correct answers in other Cloud Run observability scenarios — but here the question asks specifically for CPU/memory resource utilization, which is a metric Cloud Run already reports natively. If the question instead asked “which function in your code is consuming the most CPU,” Cloud Profiler would become the right answer; if it asked “where is latency being introduced across downstream calls,” Cloud Trace would be correct.

**Foundation Concept**

Think of Cloud Run’s observability stack as layered by question type: “is my service healthy and how much is it costing me to run” → built-in Cloud Monitoring metrics (CPU, memory, instance count, billable instance time); “where is time being spent across a request” → Cloud Trace; “which code path is hot” → Cloud Profiler; “what happened, in detail, for this one request” → Cloud Logging (and logs-based metrics when you need a custom aggregate from that detail). Resource-utilization-for-cost questions point straight at the first layer.

**Real-World Connection**

A team notices rising Cloud Run bills and opens the service’s Cloud Monitoring CPU and memory utilization charts; seeing memory consistently sitting far below the configured limit, they reduce the memory allocation per instance, which lowers the billable resource cost per request without touching application code. The trade-off to watch is under-provisioning: cutting CPU or memory too aggressively based on average utilization can cause cold-start slowdowns or out-of-memory errors under traffic spikes, so teams typically look at peak (not just average) utilization before resizing.

**Memory Hook**

“Resource utilization, no setup needed” — Cloud Run’s CPU/memory metrics are already in Cloud Monitoring by default; reach for Trace or Profiler only when the question is about latency or code hotspots instead.

**30-Second Exam Takeaway**

When a Cloud Run question asks for CPU/memory resource utilization — especially for cost decisions — default to Cloud Monitoring’s built-in container metrics; it requires no agent and no code changes, which beats any option that proposes extra tooling (Profiler, Trace, or custom logs-based metrics) to recreate data that’s already being collected.

**Official References**

[**Google Cloud — Monitor Cloud Run:**](https://cloud.google.com/run/docs/monitoring) Supports: Cloud Run is automatically integrated with Cloud Monitoring, and container CPU utilization and container memory utilization are built-in metrics requiring no setup

[**Google Cloud — Cloud Profiler documentation:**](https://cloud.google.com/profiler/docs) Supports: Cloud Profiler continuously attributes CPU usage and memory allocation to application source code via a language-specific profiling agent, distinguishing its code-level purpose (and agent model) from Ops Agent and from service-level resource-utilization monitoring

</details>

---

### Exam 2 · Q24

You are setting up the frontend tier of an application on Google Cloud. The frontend runs nginx on a managed instance group and sits behind an Envoy-based external Application Load Balancer. The entire application is deployed in the europe-west2 region and serves only users located in the United Kingdom. You need to pick the network tier and load balancing scope that minimize cost. Which combination should you choose?

- A. Premium Tier with a global load balancer
- B. Premium Tier with a regional load balancer
- C. Standard Tier with a global load balancer
- D. Standard Tier with a regional load balancer

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Standard Tier with a regional load balancer

**Correct Answer**

**D. Standard Tier with a regional load balancer**

**Exam Reasoning Explanation**

Start with the requirement that drives cost: users and backends are all in one region, so nothing in the scenario needs global reach or Google’s global backbone. Then work through the two decisions in order. First, decide which tier is cheapest while still workable: Standard. Second, check which load balancer scope is actually available in that tier. Because the question specifies an Envoy-based load balancer, the global option is eliminated by tier compatibility, which leaves the regional option as the only valid cheapest combination.

**Key Exam Clues**

  * “most cost-effective” — hard constraint: the answer must optimize cost, which favors Standard Tier over Premium Tier.

  * “deployed entirely within the europe-west2 region” — technical signal: all backends are in a single region, so a global load balancer adds no value.

  * “only serves users based in the United Kingdom” — technical signal: there is no need for global anycast IPs or worldwide backbone ingress, and users are close to the region.

  * “Envoy-based external ... load balancer” — technical signal: the Envoy-based global external Application Load Balancer runs only in Premium Tier, which constrains valid pairings.

**Why This Is Correct**

Standard Tier is the cost-optimized tier: traffic enters and leaves Google’s network at a peering point near the region where the load balancer is configured, instead of riding Google’s global backbone. The regional external Application Load Balancer, which is Envoy-based, can be configured in either Premium or Standard Tier, and it serves backends from a single region, which matches this deployment exactly. Pairing it with Standard Tier gives the lowest-cost valid design for UK-only users in one region. One prerequisite to remember is that the regional external Application Load Balancer needs a proxy-only subnet in the region.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** A global external Application Load Balancer in Premium Tier works and would serve these users, which makes it tempting as the “default” choice. It loses because you would pay for global capabilities, such as anycast IPs and worldwide backbone ingress, that a single-region, UK-only application never uses.

  * **Option B — Technically Possible but Not Best:** A regional load balancer is the right scope, and it does run in Premium Tier, so it is a close second. It loses on the cost requirement because Standard Tier is available for the same load balancer and is the lower-cost tier, and nothing in the scenario requires Premium Tier’s performance.

  * **Option C — Incorrect:** This combination is not available for an Envoy-based global load balancer. Global external Application Load Balancers use global external IP addresses and global forwarding rules, which require Premium Tier, so it cannot be built even though it sounds cheapest. The classic Application Load Balancer can operate regionally in Standard Tier, but then it is not functioning as a global load balancer and is not the Envoy-based type the question describes.

**Exam Trap**

The trap is Option C, because “Standard Tier” pairs with the cost requirement and “global” pairs with the load balancer type, so the combination looks like the best of both. The distinction is that Standard Tier is regional only, so a global Envoy-based load balancer cannot use it. If the users were spread worldwide, had backends in multiple regions, or needed Cloud CDN, Premium Tier with a global load balancer would become the correct choice.

**Foundation Concept**

Network Service Tiers decide how traffic travels between the internet and your resources: Premium Tier uses Google’s global backbone for performance, while Standard Tier uses regular ISP networks to reduce cost. The tier also constrains which resources you can use, since global IP addresses and global load balancing require Premium Tier, whereas regional resources can use either. The general design rule is to buy global capability only when users or backends are actually global. Standard Tier trades some routing performance and feature breadth for lower cost, which is an acceptable trade when users sit near a single region.

**Real-World Connection**

A UK-focused retail site runs its nginx frontend in europe-west2 and creates a regional external Application Load Balancer using a Standard Tier regional IP address, plus the required proxy-only subnet. Because traffic enters near the London region and no global features are needed, networking costs stay low without changing the application. The team accepts that it has no global anycast address and cannot attach Cloud CDN, and it would move to Premium Tier only if the audience expanded internationally.

**Memory Hook**

One region and local users mean Standard Tier with a regional load balancer, because global load balancers require Premium Tier.

**30-Second Exam Takeaway**

When a question asks for the cheapest network tier and the workload and users are in a single region, choose Standard Tier with a regional load balancer. Check pairing validity first: any global load balancer or global IP in the Envoy-based family forces Premium Tier.

**Official References**

[**Google Cloud — Network Service Tiers overview:**](https://docs.cloud.google.com/network-tiers/docs/overview) Supports: the cost-versus-performance distinction between tiers and the fact that global external IP addresses and the global external Application Load Balancer require Premium Tier while regional resources can use Standard Tier (eliminating Option C and justifying D over B)

[**Google Cloud — External Application Load Balancer overview:**](https://docs.cloud.google.com/load-balancing/docs/https) Supports: the regional external Application Load Balancer being configurable in Premium or Standard Tier and serving a single region, and the global mode being Premium only (supporting D and eliminating A)

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment to Section 5.2, “Implementing FinOps practices for optimizing resource utilization and costs,” which lists infrastructure cost planning including network tiers

</details>

---

### Exam 2 · Q48

You manage several production systems that run on Compute Engine in the same Google Cloud project. Each system uses its own dedicated set of Compute Engine instances. You want to know how much it costs to run each system. What should you do?

- A. In the Google Cloud console, use the cost breakdown report to visualize costs for each system.
- B. Apply a label specific to its system to every instance, enable Cloud Billing export to BigQuery, and query costs by label.
- C. Add metadata specific to its system to every instance, export Cloud Logging to BigQuery, and query costs based on the metadata.
- D. Name each virtual machine (VM) after its system, export usage reports to a Cloud Storage bucket, and configure the bucket as a BigQuery source to query costs by VM name.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Apply a label specific to its system to every instance, enable Cloud Billing export to BigQuery, and query costs by label.

**Correct Answer**

**B. Apply a label specific to its system to every instance, enable Cloud Billing export to BigQuery, and query costs by label.**

**Exam Reasoning Explanation**

Cost reporting needs two things: billing data that contains the costs, and an attribute on each cost line that identifies the system. Work from that. First ask where cost data lives, which rules out options that rely on logs or other non-billing data. Then ask whether the billing data can distinguish the systems, given that all of them share one project and so project-level grouping cannot separate them. The answer must therefore add a per-system attribute that Cloud Billing carries through to its cost records, and then provide a way to aggregate by it.

**Key Exam Clues**

  * “in the same Google Cloud project” — technical signal: project is not a usable grouping dimension, so a resource-level attribute is required.

  * “its own set of dedicated Compute Engine instances” — technical signal: each system maps cleanly onto a set of resources that can carry a system-specific label.

  * “how much it costs to run each of the systems” — hard constraint: the data source must be actual billed cost data, not usage or operational telemetry.

**Why This Is Correct**

A label is a key-value pair that you attach to a resource, and Google Cloud forwards label information to the billing system so charges can be broken down by label. Labeling every instance with a value that identifies its system, such as `system=<name>`, adds the missing dimension. Enabling Cloud Billing export to BigQuery then writes billing line items, including their labels, into a dataset, and a query that sums cost grouped by the label gives the cost of each system. Google’s labels documentation describes this exact use, finding the cost of a particular service by exporting usage and labels to BigQuery. One boundary is that only consistently labeled resources can be attributed, so unlabeled spend will appear separately and should be monitored.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** The built-in billing reports are valuable, which makes this tempting. As stated, though, there is nothing in the data that identifies a system, because everything shares a project and no label has been applied, so the report cannot split costs per system.

  * **Option C — Incorrect:** Instance metadata describes configuration and is not part of billing data, and Cloud Logging exports contain log entries, not charges. Querying that data cannot produce costs.

  * **Option D — Technically Possible but Not Best:** Naming VMs after systems and exporting usage reports builds an unusual pipeline around a naming convention. VM names are not how Cloud Billing attributes cost, and this path would require you to derive costs yourself, when Cloud Billing already exports cost data with labels to BigQuery.

**Exam Trap**

The strongest distractor is Option A, because the console’s billing reports are the quickest place to look at costs. The distinction is that a report can only group by dimensions present in the data, so the systems must be labeled first. If the instances were already labeled by system, the built-in billing reports, which can filter and group costs by resource label, would be a fast alternative to a BigQuery query.

**Foundation Concept**

Cost attribution works by attaching a dimension to each cost line item. Project, service, and SKU come with the billing data, while labels add custom dimensions such as system, team, or environment. Billing export to BigQuery makes those line items queryable at full detail, which supports custom grouping, dashboards, and chargeback or showback. Good practice is to define a consistent labeling scheme, apply it at provisioning time, and track unlabeled spend.

**Real-World Connection**

A team sets a `system` label on every instance through its infrastructure-as-code templates and enables Cloud Billing export to BigQuery. A scheduled query sums monthly cost by label and feeds a dashboard, so each system’s owner can see their spend. Shared costs, such as networking, need a separate allocation rule, and a periodic check for unlabeled resources keeps the data trustworthy.

**Memory Hook**

Label the resource, export the bill, and group the cost by label.

**30-Second Exam Takeaway**

To find costs per system within one project, apply system-specific labels to the resources, export Cloud Billing data to BigQuery, and query by label. Logs, metadata, and VM names are not billing dimensions, and built-in reports can only group by attributes that already exist.

**Official References**

[Google Cloud — Labels overview (Resource Manager): ](https://docs.cloud.google.com/resource-manager/docs/labels-overview)Supports: the correct-answer mechanism (labels are forwarded to billing, can be exported to BigQuery with usage, and are used to find the cost of a particular service), and the note that built-in billing reports can group by labels

[**Google Cloud — Export Cloud Billing data to BigQuery:**](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) Supports: how billing export writes cost data, including labels, to BigQuery so costs can be queried by label, which distinguishes options C and D

</details>

---

### Exam 2 · Q59

An e-commerce application has recently been migrated to Google Cloud, and the team wants to get it ready for the upcoming busy season. What is the first thing that should be done to prepare?

- A. Run load tests against the application to profile how its performance behaves under scaling.
- B. Turn on autoscaling for the production clusters in anticipation of traffic growth.
- C. Pre-provision twice the compute capacity that was used during last season, anticipating growth.
- D. Write a runbook describing how to scale up the disaster recovery (DR) environment if growth occurs.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Run load tests against the application to profile how its performance behaves under scaling.

**Correct Answer**

**A. Run load tests against the application to profile how its performance behaves under scaling.**

**Exam Reasoning Explanation**

The decisive word in the question is “first.” Every one of the four options is a plausible activity somewhere in a busy-season readiness plan, so the question isn’t testing whether each is a good idea in isolation — it’s testing sequencing. Autoscaling thresholds, how much capacity to pre-provision, and how far a DR environment needs to scale are all decisions that should be derived from data about how the application actually behaves under load: where it bottlenecks, at what traffic level, and in which component. Until that data exists, any of those decisions is a guess. Load testing is the step that produces the data, so it has to come before the others, not alongside or after them.

**Key Exam Clues**

  * “What is the first thing that should be done to prepare?” — a sequencing constraint; the correct option must be the foundational step everything else depends on, not merely a reasonable preparation activity.

  * “recently been migrated to Google Cloud” — the application’s scaling behavior in this environment hasn’t necessarily been characterized yet, reinforcing the need to establish a performance baseline before making capacity commitments.

  * Options B, C, and D are each specific infrastructure or process decisions, none of which states that performance data already exists to base that decision on.

**Why This Is Correct**

Load testing reveals the application’s actual scaling characteristics and bottlenecks under simulated peak conditions — whether the constraint is compute, a database connection pool, a downstream API quota, or something else entirely. That information is a precondition for making every other preparation decision well: it tells you what signal and thresholds to configure for autoscaling, how much capacity actually needs to be reserved or pre-provisioned, and whether DR capacity needs to scale differently than production. Running it first means every subsequent decision is grounded in evidence rather than assumption.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Technically Possible but Not Best:** enabling autoscaling is a sound long-term practice, but configuring it effectively requires knowing which metric to scale on and what thresholds and instance limits actually match the application’s real behavior under load — exactly what a load test reveals. Turning it on without that information risks thresholds that are poorly matched to the application’s actual bottlenecks.

  * **Option C — Technically Possible but Not Best:** doubling last season’s compute is an arbitrary multiplier with no basis in measured need. It assumes growth will be linear and that compute is the binding constraint, when the real bottleneck could just as easily be a database, a third-party integration, or application code — something more compute alone wouldn’t fix, and something a load test would surface.

  * **Option D — Different Use Case:** a runbook for scaling the DR environment addresses disaster recovery — restoring service after a catastrophic failure — which is a related but separate concern from preparing production capacity for an expected, non-catastrophic increase in ordinary traffic. It doesn’t speak to the busy-season capacity question the scenario is actually asking about.

**Exam Trap**

The trap is evaluating each option only on “is this a sensible thing to do,” which makes B, C, and D all look reasonable. The question isn’t asking which options are valid preparation activities — it’s asking which one has to happen first so the others can be done well. Skipping past the diagnostic step straight to a specific infrastructure decision is the exact ordering mistake the question is testing for.

**Foundation Concept**

Capacity planning for an anticipated demand increase starts with establishing, through load testing under realistic simulated peak conditions, how the system actually scales and where its real limits are. Every subsequent decision — autoscaling configuration, capacity reservations, redundancy planning, DR sizing — should be derived from that evidence rather than assumed ahead of time.

**Real-World Connection**

Running load tests well ahead of a peak event — Google Cloud’s own peak-event guidance recommends starting three to five months out — surfaces bottlenecks like a saturated connection pool or an undersized API quota while there’s still time to fix them, and gives the team the concrete numbers needed to correctly size autoscaling policies and capacity reservations, instead of discovering those limits for the first time during the actual busy season.

**Memory Hook**

Before tuning autoscaling, pre-provisioning compute, or updating a DR runbook — measure first. Load test to find out how the system actually scales.

**30-Second Exam Takeaway**

When a question asks what to do “first” to prepare for anticipated higher demand, favor the step that produces the data every other decision should be based on — load testing — over any specific capacity or configuration action taken without it.

**Official References**

[**Google Cloud — Conduct load testing (peak capacity event preparation):**](https://cloud.google.com/support/docs/peak-events/conduct-load-testing) Supports: the correct-answer reasoning that load testing is a foundational, early preparation step that surfaces scaling bottlenecks before an event

[**Google Cloud — Manage traffic and load for your workloads in Google Cloud:**](https://cloud.google.com/architecture/infra-reliability-guide/traffic-load) Supports: why capacity decisions such as autoscaling configuration and provisioning should be derived from load-test results rather than assumed in advance

</details>

---

### Exam 3 · Q45

A newly created Google Cloud project will host several applications on Compute Engine VM instances distributed across multiple regions. You expect the total instance count to remain steady or increase, although you might redistribute instances among regions over time. Which approach best minimizes compute costs for this multi-year project?

- A. Purchase a three-year resource-based commitment.
- B. Purchase a three-year compute flexible commitment and create capacity reservations.
- C. Purchase a three-year compute flexible commitment.
- D. Purchase a one-year resource-based commitment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Purchase a three-year compute flexible commitment.

**Correct Answer**

**C. Purchase a three-year compute flexible commitment.**

**Exam Reasoning Explanation**

The solution must accommodate changes in regional allocation. The stable overall demand supports committing to ongoing usage, while the multi-year horizon favors the longer term. Resource-based commitments introduce regional restrictions. Between the flexible options, reservations add capacity assurance that the scenario does not request, making C the best fit.

**Key Exam Clues**

  * **“Distributed across multiple regions” — Technical signal:** Evaluate the geographical scope of each commitment.

  * **“Total instance count to remain steady or increase” — Technical signal:** Indicates an ongoing consumption baseline.

  * **“Redistribute instances among regions” — Hard constraint:** Savings must remain applicable as regional placement changes.

  * **“Minimizes compute costs” — Optimization objective:** Avoid adding capacity arrangements without a corresponding requirement.

  * **“Multi-year project” — Technical signal:** Supports considering a three-year commitment.

**Why This Is Correct**

Compute flexible commitments apply to eligible spending across regions and projects within the same Cloud Billing account. Their coverage can therefore follow eligible workloads as the regional distribution changes. A three-year term provides greater discounts than a one-year term for eligible Compute Engine resources.

The commitment covers a minimum **hourly spend** , rather than a fixed number of instances. Actual savings depend on maintaining sufficient eligible consumption.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** A three-year resource-based commitment can provide substantial savings for predictable regional usage. However, its coverage remains tied to the specified region. Moving workloads elsewhere can leave paid commitments underutilized.

  * **Option B — Technically Possible but Not Best:** Flexible commitments can cover eligible usage that consumes separately created reservations. Reservations hold capacity in specified zones; they do not independently increase the commitment discount. Unused reserved resources can incur charges, so this option introduces unnecessary cost exposure for the stated objective. Consuming a reservation does **not** create duplicate resource charges for the same VM usage. 

  * **Option D — Technically Possible but Not Best:** A one-year resource-based commitment reduces the commitment duration but retains the regional restriction. It also provides a smaller discount than the corresponding three-year resource-based plan. It would be more appropriate for predictable regional demand with only a one-year commitment horizon. 

**Exam Trap**

Do not confuse a **pricing commitment** with a **capacity reservation**. Option B becomes appropriate if the requirements additionally include assured capacity for particular VM configurations in specified zones. Compute flexible commitments do not support attached reservations; any required reservations are created separately. 

**Foundation Concept**

Evaluate commitment scope, duration, and capacity assurance separately. A favorable discount rate only produces useful savings when actual consumption continues to match the commitment’s eligibility and scope.

**Real-World Connection**

An application team could redistribute eligible VMs between two regions while continuing to consume the same billing account’s flexible commitment. Before purchasing, it should forecast minimum hourly eligible spending: unchanged instance counts alone do not guarantee unchanged spending when VM sizes or regional prices differ.

**Memory Hook**

Stable demand with changing regions favors flexible commitments; add reservations when capacity assurance is required.

**30-Second Exam Takeaway**

Identify what remains predictable: total consumption or consumption within a particular region. For ongoing eligible compute usage whose regional distribution may change, prefer a compute flexible commitment and select the term supported by the workload horizon.

**Official References**

  * [**Google Cloud — Committed use discounts for Compute Engine:**](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)

Supports: Cross-region flexible coverage, regional resource-based restrictions, commitment duration, and hourly spending obligations.

  * [**Google Cloud — Combine reservations with committed use discounts:**](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments)

Supports: The distinction between discounts and capacity assurance, including separate reservations with compute flexible commitments.

[**Google Cloud — About reservations:**](https://docs.cloud.google.com/compute/docs/instances/reservations-overview)

Supports: Zonal capacity assurance, charges for unused reserved resources, and the absence of duplicate resource charges when reservations are consumed.

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)

Supports: Alignment with “Optimizing performance and cost,” objective 5.2, which includes infrastructure cost planning and committed-use discounts. [English](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf?utm_source=chatgpt.com)

</details>

---

### Exam 3 · Q54

Your company offers a free photo-processing application. You are selecting compute infrastructure for its backend processing service, which:

  * Stores original and processed photos in Cloud Storage.

  * Can resume processing after a failure.

  * Is unsuitable for containerization.

There is no service level objective (SLO) for photo-processing completion time. You need to minimize compute costs. What should you do?

- A. Deploy the service on Cloud Run.
- B. Deploy the service on standard Compute Engine VMs covered by a three-year committed use discount.
- C. Deploy the service on Google Kubernetes Engine (GKE).
- D. Deploy the service on Compute Engine Spot VMs.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Deploy the service on Compute Engine Spot VMs.

**Correct Answer**

**D. Deploy the service on Compute Engine Spot VMs.**

**Exam Reasoning Explanation**

The workload tolerates interruptions, has flexible completion times, and requires a VM-based execution environment. These characteristics make Spot VMs the best fit among the available options. 

**Key Exam Clues**

  * **Recovery capability:** Processing can resume after a failure.

  * **Scheduling flexibility:** There is no processing-time SLO.

  * **Hard constraint:** The service is unsuitable for containerization.

  * **Primary objective:** Minimize costs.

**Why This Is Correct**

Google recommends Spot VMs for fault-tolerant workloads such as batch processing. They offer substantially discounted compute capacity in exchange for accepting possible interruption when Google reclaims resources. 

The service can run directly on the VM without containerization. Its recovery capability and flexible completion time accommodate the interruptions and capacity delays associated with Spot VMs.

**Why the Other Options Are Not the Best Fit**

  * **A — Violates Requirement:** Cloud Run executes workloads in containers. The service’s containerization constraint makes it unsuitable, even though Cloud Run supports batch jobs. 

  * **B — Technically Possible but Not Best:** Standard VMs can run the service, and committed use discounts benefit predictable usage. However, this option requires a three-year commitment and does not exploit the workload’s suitability for discounted interruptible capacity. 

  * **C — Violates Requirement:** GKE is a container orchestration platform designed to deploy and operate containerized applications. It does not match the stated execution constraint. 

**Exam Trap**

Spot VMs can be interrupted and might not be immediately available again. The processing system must implement recovery and retry behavior; selecting Spot VMs does not provide application recovery automatically. 

**Foundation Concept**

Spot pricing exchanges interruption tolerance for lower compute costs. Committed use discounts exchange a minimum usage or spending commitment for discounted prices. 

**Real-World Connection**

Keep processing progress in durable storage and make retries safe. A replacement worker can then resume unfinished work without corrupting or unnecessarily duplicating completed outputs.

**Memory Hook**

Resumable processing with flexible deadlines is a strong candidate for Spot VMs.

**30-Second Exam Takeaway**

Choose **D**. The service can tolerate interruptions and delays, making Spot VMs the appropriate cost-saving option.

**Official References**

  * [**Spot VMs**](https://docs.cloud.google.com/compute/docs/instances/spot)  
Supports: Discounted capacity, preemption, availability limitations, and suitability for fault-tolerant batch workloads.

  * [**Committed use discounts for Compute Engine**](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)  
Supports: Commitment requirements and suitability for predictable usage.

  * [**Cloud Run container runtime contract**](https://docs.cloud.google.com/run/docs/container-contract)  
Supports: Cloud Run’s container execution requirements.

  * [**GKE overview**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)  
Supports: GKE’s role as a platform for containerized applications.

</details>

---

### Exam 4 · Q14

You monitor a service built on n2-standard-2 Compute Engine instances that serve large files to end users, and customers have been reporting slow downloads. Your Cloud Monitoring dashboard confirms the VMs are consistently hitting their maximum network throughput. You need to raise the network throughput ceiling for these instances. What should you do?

- A. Attach additional virtual network interface controllers (vNICs) to each VM.
- B. Deploy a Cloud NAT gateway and attach it to the VMs’ subnet.
- C. Resize the VMs to the n2-standard-8 machine type.
- D. Install the Ops Agent on the VMs to export additional monitoring metrics.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Resize the VMs to the n2-standard-8 machine type.

**Correct Answer**

**C. Resize the VMs to the n2-standard-8 machine type.**

**Exam Reasoning Explanation**

The fix has to raise the actual network throughput ceiling, since the dashboard confirms the VMs are already saturating their current cap. Google Cloud enforces network bandwidth limits per compute instance based on machine type and vCPU count, not per network interface, so adding vNICs (A) does nothing to raise the cap. Cloud NAT (B) solves an unrelated problem — outbound internet access for instances without external IPs — and has no effect on bandwidth ceilings. The Ops Agent (D) only adds observability, not capacity. Increasing the vCPU count by moving to a larger machine type (C) directly raises the per-instance maximum egress bandwidth, since that limit scales with vCPU count up to the machine series’ cap, making it the only option that actually increases available throughput.

**Key Exam Clues**

  * “running at peak network throughput” — the decisive signal that the bottleneck is the instance’s bandwidth cap, not an unrelated connectivity or configuration issue

  * “n2-standard-2” — a small vCPU count, implying real headroom to grow within the N2 series before hitting its bandwidth ceiling

  * “serve large files” / “downloads are slow” — frames this as a sustained egress-bandwidth problem rather than a one-off latency or routing issue

  * “improve the network throughput performance” — specifically asks for a capacity fix, ruling out anything that only adds visibility (Ops Agent) or addresses outbound internet access for private instances (Cloud NAT)

**Why This Is Correct**

Google Cloud’s per-instance maximum egress bandwidth is generally around 2 Gbps per vCPU, up to a cap defined by the machine series. Moving from n2-standard-2 (2 vCPUs) to n2-standard-8 (8 vCPUs) quadruples the vCPU count, directly raising the per-instance bandwidth ceiling within the N2 family’s limits. Since the VMs are already measured at their current peak, this change actually gives them room to serve files faster rather than leaving them capped where they already sit.

**Why the Other Options Are Not the Best Fit**

**Option A — Incorrect:** Google Cloud accounts for network bandwidth per compute instance, not per virtual network interface. Adding more vNICs does not raise a VM’s aggregate egress or ingress bandwidth limit — the instance remains capped at the same total throughput regardless of how many interfaces that traffic is split across.

**Option B — Different Use Case:** Cloud NAT provides outbound internet connectivity for instances without external IP addresses; it has no effect on an instance’s network bandwidth ceiling. Since the VMs here are already serving traffic — just slowly — the problem isn’t connectivity, it’s throughput capacity, which Cloud NAT doesn’t address.

**Option D — Violates Requirement:** The Ops Agent exports additional monitoring and logging metrics; it’s an observability tool, not a performance capability. Deploying it would give more visibility into the problem but do nothing to raise the network throughput ceiling the scenario asks you to improve.

**Exam Trap**

The trap is assuming that because traffic flows through NICs, adding more NICs must increase available bandwidth — but Google Cloud explicitly caps bandwidth at the instance level based on machine type, not per interface, so Option A looks intuitively correct while being technically wrong. A secondary trap is reaching for Cloud NAT whenever “network” and “VM” appear together, without noticing that NAT addresses outbound connectivity for private instances, not throughput capacity for instances that are already reachable and transferring data.

**Foundation Concept**

Compute Engine enforces a maximum egress (and roughly similar ingress) bandwidth per instance, derived primarily from vCPU count and machine series — generally around 2 Gbps per vCPU up to a series-specific ceiling. This limit applies to the instance as a whole regardless of how many network interfaces or IP addresses it has, which is why scaling vCPUs — by resizing to a larger machine type, or enabling a high-bandwidth Tier_1 networking configuration on qualifying machine types — are the mechanisms that actually raise available throughput.

**Real-World Connection**

A team serving large media or software downloads from Compute Engine VMs notices download speeds plateauing as demand grows, and monitoring confirms the VMs are pinned at their network bandwidth cap. Rather than adding more interfaces or spinning up unrelated networking components, they resize the instances to a larger machine type (or enable Tier_1 networking on a qualifying series) to raise the per-instance throughput ceiling, directly improving the download experience without re-architecting the service.

**Memory Hook**

Bandwidth caps are per-instance (vCPU-based), not per-NIC — to raise the ceiling, scale the machine type, not the interface count.

**30-Second Exam Takeaway**

When a VM is confirmed to be at its network throughput ceiling, look for a fix that raises the per-instance bandwidth cap — typically a larger machine type or Tier_1 networking — and rule out adding NICs, which Google Cloud explicitly does not credit toward instance bandwidth, along with unrelated tools like Cloud NAT or monitoring agents.

**Official References**

[**Google Cloud — Network bandwidth:**](https://docs.cloud.google.com/compute/docs/network-bandwidth) Supports: bandwidth being accounted per compute instance rather than per vNIC, vCPU-based scaling of the per-instance egress cap, and the N2 machine series bandwidth limits

</details>

---

### Exam 4 · Q29

As a Site Reliability Engineer, you support a Go application running in production on Google Kubernetes Engine (GKE). After a new release, you notice the application runs for roughly 15 minutes before restarting. You add Cloud Profiler to the application and observe that heap usage climbs steadily until each restart. What should you do?

- A. Raise the CPU limit configured on the application’s deployment.
- B. Add nodes with more memory to the cluster’s node pool.
- C. Raise the memory limit configured on the application’s deployment.
- D. Instrument the application with Cloud Trace, and redeploy it.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Raise the memory limit configured on the application’s deployment.

**Correct Answer**

**C. Raise the memory limit configured on the application’s deployment.**

**Exam Reasoning Explanation**

The fix must address the memory-growth-then-restart pattern Cloud Profiler has already confirmed, and it must actually change what determines whether the container gets OOMKilled. Option A targets CPU, a different resource than the one Profiler identified as the problem, so it can’t affect a memory-driven restart. Option D adds Cloud Trace, a distributed-tracing tool for request latency and call paths, not a memory-diagnostic tool — Profiler has already supplied the relevant heap data, and Trace adds nothing toward solving a memory problem. Option B adds nodes with more physical memory, but a container’s OOMKill is governed by its own configured memory limit, not by how much memory is available on the node it runs on — more node capacity doesn’t change when that specific container gets killed. Option C directly raises the limit the container is actually measured against, giving the application room to run without hitting that ceiling — the mechanism that determines restart behavior.

**Key Exam Clues**

  * “heap usage grows constantly until the application restarts” — identifies this specifically as a memory-consumption problem, ruling out any fix targeting a different resource (CPU)

  * “runs for about 15 minutes and then restarts” — a classic OOMKill/crash-loop pattern, pointing toward resource limits as the mechanism to examine

  * “add Cloud Profiler... and now notice” — establishes profiling has already successfully diagnosed the issue, so the next step should act on that finding rather than add a different, unrelated diagnostic tool

  * “application deployment” appears in two of the four options — signals the decision is about which deployment-level resource setting to change, not whether to change one at all

**Why This Is Correct**

Cloud Profiler’s heap data has already identified memory, not CPU, as the resource driving the restarts, and in Kubernetes a container is terminated with an out-of-memory kill specifically when it exceeds the memory limit configured for that container in its deployment spec — regardless of how much memory the underlying node has available. Raising the memory limit directly changes that ceiling, giving the application room to operate without triggering a restart, targeting the exact mechanism responsible for the crash-loop behavior Profiler has already diagnosed.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement:** Profiler specifically showed heap (memory) usage climbing, not CPU usage. Raising the CPU limit changes a resource unrelated to the diagnosed problem and would have no effect on when the container gets OOMKilled.

**Option B — Technically Possible but Not Best:** A container’s OOM kill is triggered by its own configured memory limit, not the physical memory available on its node. Adding higher-memory nodes increases cluster capacity in general, but without also raising the container’s own memory limit, that same container is still killed at the same threshold regardless of how much memory the surrounding node has.

**Option D — Violates Requirement:** Cloud Trace captures distributed request latency and call-path data, not memory allocation information, so it contributes nothing new toward diagnosing or resolving a heap-growth problem Cloud Profiler has already clearly identified. Redeploying with an unrelated diagnostic tool also doesn’t address the restarts themselves.

**Exam Trap**

The trap is treating “add more resources somewhere in the cluster” (B) as equivalent to “fix the container’s resource limit” (C) — they sound similar but operate at different layers: node capacity versus the cgroup-enforced limit on the individual container, and only the latter determines whether that specific container gets OOMKilled. A second trap is reaching for a familiar observability tool (Cloud Trace) just because the scenario already involves observability, without checking whether that specific tool measures the resource in question; Trace addresses latency and request flow, not memory.

**Foundation Concept**

In Kubernetes, a container’s memory limit is enforced independently of the node’s total memory capacity: the container is killed once its own usage crosses its configured limit, even if the node still has free memory elsewhere, and adding memory to the node doesn’t raise that container-specific ceiling. This is why diagnosing a memory-related restart requires checking not just whether there’s “enough memory in the cluster,” but specifically whether the container’s own configured limit is appropriate for how much memory the application actually needs.

**Real-World Connection**

An SRE investigating a Go service that restarts every 15 minutes adds Cloud Profiler, confirms the heap grows continuously rather than plateauing, and raises the container’s memory limit in the deployment manifest so it has enough headroom to run without hitting its ceiling — buying stability immediately while a parallel workstream uses the same profiler data to track down and fix whatever code change in the new release caused the excess allocation in the first place.

**Memory Hook**

Profiler shows memory, not CPU, climbing until restart → raise the container’s own memory limit; more node memory or a tracing tool doesn’t touch the limit that’s actually triggering the kill.

**30-Second Exam Takeaway**

When profiling data shows a container’s heap climbing until an OOM-style restart, fix the resource limit Kubernetes actually enforces against that container — its configured memory limit — rather than adding node-level capacity (which doesn’t change the container’s own ceiling) or reaching for a tool, like Cloud Trace, that measures a different kind of problem entirely.

**Official References**

[Google Cloud — Put it all together: Example GKE troubleshooting scenario: ](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-example)Supports: the exact diagnostic pattern of climbing container memory usage leading to an OOMKilled restart, and raising the container’s configured memory limit as a documented response

</details>

---

### Exam 4 · Q42

Your company processes IoT data at scale using Pub/Sub, the App Engine standard environment, and an application written in Go. You have noticed that performance degrades intermittently at peak load, and you could not reproduce the problem on your workstation. You need to monitor the application continuously in production to find the slow paths in the code, while keeping both performance impact and management overhead to a minimum. What should you do?

- A. Use Cloud Monitoring to review the App Engine CPU utilization metric.
- B. Install a continuous profiling tool on Compute Engine, and configure the application to send its profiling data to that tool.
- C. Periodically run the go tool pprof command against the application instance, and analyze the output by using flame graphs.
- D. Set up Cloud Profiler, and initialize the cloud.google.com/go/profiler library in the application.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Set up Cloud Profiler, and initialize the cloud.google.com/go/profiler library in the application.

**Correct Answer**

**D. Set up Cloud Profiler, and initialize the cloud.google.com/go/profiler library in the application.**

**Exam Reasoning Explanation**

Three requirements must hold together. The problem can’t be reproduced locally and appears only intermittently under peak load, so the monitoring has to run continuously in production. You need to find slow paths in the code, so the data must be attributed to functions in the source, not just to resource totals. Finally, both performance impact and management overhead must be minimal, which favors a managed, low-overhead tool over anything you operate yourself. A metric only shows that a resource is busy, and the self-managed and manual profiling options fail the overhead or continuity requirement. Cloud Profiler is the only option that meets all three.

**Key Exam Clues**

  * “could not reproduce this issue on your workstation” is a technical signal that profiling has to happen in production

  * “continuously monitor the application in production” is a hard constraint that rules out occasional manual captures

  * “identify slow paths in the code” is a technical signal that code-level attribution is needed, not infrastructure metrics

  * “minimize performance impact and management overhead” is a hard constraint that favors a managed, low-overhead service

  * “App Engine standard environment” and “written in Go” together point to a supported Cloud Profiler configuration

**Why This Is Correct**

Cloud Profiler is a statistical, low-overhead profiler that continuously gathers CPU usage and memory-allocation information from production applications and attributes it to the source code that generated it. Google states that the overhead of CPU and heap profiling at collection time is under 5 percent, and amortized across the execution time and replicas of a service it is commonly under 0.5 percent, which makes it suitable for always-on use in production. Go on the App Engine standard environment is a supported configuration. You enable it by calling profiler.Start from the cloud.google.com/go/profiler package early in main, and on App Engine the service name and version are inferred from the environment. Google manages the backend and the interface, so you don’t run profiling infrastructure.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** CPU utilization shows how busy the instances are at peak load, which fits the symptom, but it does not show which functions or code paths consume the CPU. It tells you that something is slow, not where in the code.

**Option B — Technically Possible but Not Best:** A continuous profiling tool does fit the continuity requirement, but installing and running it on Compute Engine means provisioning, operating, and securing your own profiling infrastructure and wiring the application to it. That is the management overhead the scenario asks you to avoid, when a managed service already supports this environment.

**Option C — Violates Requirement:** Running go tool pprof periodically is manual and point-in-time, so it can miss an intermittent problem that appears only at peak load, and it is not continuous monitoring. Collecting and analyzing samples by hand is also ongoing operational work.

**Exam Trap**

The trap is picking option A because the symptom appears at peak load and CPU is the obvious resource to check. A resource metric can confirm saturation, but it can’t tell you which code is responsible, which is the actual goal. Option C is a second trap, since pprof is a real Go profiling tool, but it is manual and not continuous. The answer would change to option A only if the goal were to confirm resource saturation or alert on it, and different tooling again (distributed tracing) if the goal were to find which downstream call in a request is slow.

**Foundation Concept**

Metrics and profiles answer different questions. Metrics such as CPU utilization show that a service is slow or saturated, while profiles show where in the code the CPU time or memory goes. Statistical (sampling) profiling takes brief samples at intervals instead of tracing every operation, which keeps overhead low enough to leave on permanently in production. That is what makes it suitable for problems that are intermittent, load-dependent, and impossible to reproduce on a workstation.

**Real-World Connection**

A team adds a single profiler.Start call to its Go service’s main function and deploys to App Engine. After the next peak-load slowdown, they open Profiler, look at the profile data for the period when the degradation occurred, and find that one message-handling function dominates CPU time. They fix that function and redeploy. They never provisioned profiling servers, and the overhead stayed small enough to leave profiling on for good.

**Memory Hook**

For slow code paths in production with minimal overhead, use Cloud Profiler, because metrics show that a resource is busy and profiles show which code is using it.

**30-Second Exam Takeaway**

When a question needs continuous, low-overhead, code-level performance analysis of a production application, choose Cloud Profiler. Reject resource metrics, which don’t point to code, and reject self-hosted or manual profiling, which adds management effort or misses intermittent problems.

**Official References**

[**Google Cloud Profiler — Cloud Profiler overview:**](https://docs.cloud.google.com/profiler/docs/about-profiler) Supports: Cloud Profiler as a statistical, low-overhead continuous profiler for production applications, the overhead figures (under 5 percent at collection, commonly under 0.5 percent amortized), and Go on the App Engine standard environment as a supported configuration

[**Google Cloud Profiler — Profiling Go applications:**](https://docs.cloud.google.com/profiler/docs/profiling-go) Supports: initializing the cloud.google.com/go/profiler library with profiler.Start and App Engine inferring the service name and version

[**Google Cloud — Professional Cloud DevOps Engineer Certification exam guide (Section 5.1, collecting performance information: application performance monitoring):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain and objective alignment

</details>

---

### Exam 4 · Q45

You support a set of Java applications running in production, and every application already has Cloud Profiler and Cloud Trace enabled by default. You need a way to identify which of these applications actually require performance tuning. What should you do? (Choose two.)

- A. Compare the application’s wall-clock time with its CPU time; if the gap between them is large, increase its CPU resource allocation
- B. Compare the application’s wall-clock time with its CPU time; if the gap between them is large, increase its memory resource allocation
- C. Compare the application’s wall-clock time with its CPU time; if the gap between them is large, increase its local disk storage allocation
- D. Compare the application’s latency, wall-clock time, and CPU time together; if latency is steadily consuming the error budget while the gap between wall-clock time and CPU time is small, mark the application for optimization
- E. Check the application’s heap usage; if usage is low, mark the application for optimization

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Compare the application’s wall-clock time with its CPU time; if the gap between them is large, increase its CPU resource allocation **|** D. Compare the application’s latency, wall-clock time, and CPU time together; if latency is steadily consuming the error budget while the gap between wall-clock time and CPU time is small, mark the application for optimization

**Correct Answer**

**A. Compare the application’s wall-clock time with its CPU time; if the gap between them is large, increase its CPU resource allocation**

**D. Compare the application’s latency, wall-clock time, and CPU time together; if latency is steadily consuming the error budget while the gap between wall-clock time and CPU time is small, mark the application for optimization**

**Exam Reasoning Explanation**

Cloud Profiler reports CPU time (time actually executing on a CPU) and wall-clock time (total elapsed time, including everything the thread wasn’t executing) separately, so comparing the two tells you something different depending on which way the gap points. A must-have constraint is that the chosen signals have to actually distinguish “needs tuning” from “doesn’t,” rather than pointing to an unrelated resource. Working the chain: requirement (use Profiler/Trace data to flag applications that genuinely need tuning) → capability (the wall-clock/CPU gap reveals two distinct conditions depending on its size, and Trace’s latency/error-budget data adds the user-impact dimension) → elimination (B and C swap in resources that have no causal link to CPU/wall-time accounting, and E’s “low heap usage” has no established link to a performance problem) → decision (A and D are the two conditions where the Profiler/Trace signals actually justify action, each addressing a different root cause).

**Key Exam Clues**

  * “the gap between them is large” (A) is a technical signal that a large share of elapsed time was not spent executing on CPU, which is consistent with the application not getting enough CPU time to run when it has work ready to do.

  * “latency... steadily consuming the error budget” combined with “the gap... is small” (D) is a compound hard constraint: the small wall-clock/CPU gap shows the thread is genuinely CPU-bound (actively computing nearly the whole time), and the error-budget erosion confirms that this CPU-bound behavior is measurably hurting users — together these justify flagging the app.

  * “(Choose two.)” signals the answer set should cover two distinct, non-overlapping diagnostic conditions rather than two phrasings of the same one.

**Why This Is Correct**

For A: when wall-clock time is much larger than CPU time, the thread spent most of its elapsed duration not actively running on a CPU core. One concrete cause of this pattern is that the application isn’t being allocated enough CPU capacity to run as often as it’s ready to — it’s sitting ready but not scheduled. In that situation, giving the application more CPU resource allocation directly closes the gap, because the limiting factor is CPU availability, not the code itself.

For D: when wall-clock time and CPU time are close together, the thread is spending nearly all of its elapsed time actively executing — it is genuinely CPU-bound, not waiting on anything. Pairing that with Cloud Trace data showing latency is steadily burning the error budget confirms this CPU-bound behavior is a real, user-facing reliability problem rather than a harmless inefficiency. That combination is exactly the signal that should mark an application for optimization work (such as algorithmic or code-level tuning), since simply adding more of the same resource won’t change code that’s already fully using what it has.

**Why the Other Options Are Not the Best Fit**

**Option B — Incorrect:** a wall-clock/CPU time gap reflects how much of an application’s elapsed time was spent executing versus not, which has no causal connection to how much memory it has. Increasing memory allocation changes how much data the application can hold, not how promptly its threads get CPU time, so it doesn’t address what the gap is actually showing.

**Option C — Incorrect:** the same reasoning applies to local disk storage. Disk capacity governs how much data can be stored and accessed on disk, not whether a thread is executing or waiting, so it has no logical relationship to a wall-clock/CPU time comparison.

**Option E — Incorrect:** heap usage reflects how much memory is currently allocated to live objects, not how efficiently or how slowly the application is running. Low heap usage simply means the application isn’t using much memory — on its own that says nothing about latency, throughput, or CPU behavior, so it isn’t a reliable signal that an application needs performance tuning.

**Exam Trap**

The trap is assuming that any “substantial difference” between wall-clock and CPU time always means the same thing, or that it can be fixed the same way regardless of direction. A large gap and a small gap point to opposite conditions — one suggests the application isn’t getting enough CPU, the other confirms it’s already fully using the CPU it has — so the correct response depends entirely on which direction the comparison points, and in the small-gap case, the fix is code-level optimization rather than scaling a resource at all.

**Foundation Concept**

Application performance monitoring works by correlating multiple signals rather than reading any single metric in isolation. CPU time versus wall-clock time tells you how much of an operation’s duration was spent actively computing, which separates “waiting for a resource” problems from “genuinely compute-intensive” ones; latency and error-budget trends from distributed tracing tell you whether that behavior is actually affecting users enough to matter. Combining both is what turns raw profiling data into an actionable judgment about which applications deserve tuning effort.

**Real-World Connection**

A team notices one service’s wall-clock time is consistently far above its CPU time and finds the service is capped at a low CPU limit even though demand has grown; raising that limit lets the service actually use the CPU time it needs, and the gap closes. A different service shows wall-clock and CPU time nearly identical, and its latency has been quietly eating into its SLO’s error budget for weeks; because the code is already fully CPU-bound, the team profiles the hot path and optimizes an inefficient algorithm rather than scaling resources, which is what actually reduces latency and stops the budget burn.

**Memory Hook**

“Big gap, give it CPU. Small gap plus a shrinking budget, fix the code.”

**30-Second Exam Takeaway**

When a question pairs Cloud Profiler’s CPU-time-versus-wall-time comparison with Cloud Trace’s latency/error-budget data, read the size and direction of the gap as the diagnosis: a large gap points toward insufficient CPU allocation, while a small gap combined with budget-burning latency points toward genuinely CPU-bound code that needs optimization rather than more resources.

**Official References**

[**Google Cloud — Cloud Profiler concepts (CPU time and wall time definitions):**](https://cloud.google.com/profiler/docs/concept) Supports: correct-answer mechanism — what CPU time versus wall time measure and why their gap is diagnostic

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 5.1, Collecting performance information in Google Cloud):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment — application performance monitoring as the basis for identifying optimization candidates

</details>

---

### Exam 4 · Q58

Your organization runs a monolithic application on Compute Engine, and you need to choose a machine type that optimizes CPU utilization, basing that choice on historical system metrics and reaching it in as few steps as possible. You want to follow Google-recommended practices. What should you do?

- A. Query the Recommender API for the VM’s machine type recommendation and apply what it suggests
- B. Set up an Agent Policy that automatically installs the Ops Agent on every VM
- C. Manually install the Ops Agent across the fleet of VMs using the gcloud CLI
- D. Inspect the VM’s Cloud Monitoring dashboard yourself and pick a machine type based on its lowest observed CPU utilization

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Query the Recommender API for the VM’s machine type recommendation and apply what it suggests

**Correct Answer**

**A. Query the Recommender API for the VM’s machine type recommendation and apply what it suggests**

**Exam Reasoning Explanation**

The must-have constraints are using historical metrics, reaching a decision in the fewest steps, and following Google-recommended practice — all three have to be satisfied together, not traded off against each other. Walking the chain: requirement (pick an optimal machine type from historical CPU data with minimal effort) → capability (the VM instance rightsizing recommender already monitors CPU and memory utilization automatically and surfaces a ready-to-apply suggestion through the Recommender API) → elimination (B and C both add agent-installation steps that aren’t required for a base CPU recommendation, D substitutes manual review and judgment for an automated calculation) → decision (A is the single call that goes directly from existing historical data to an actionable recommendation).

**Key Exam Clues**

  * “fewest number of steps” is a hard constraint that rules out any option requiring setup or configuration work before a recommendation exists.

  * “historical system metrics” is a technical signal pointing to a feature that already analyzes a window of past utilization automatically, rather than one requiring manual interpretation.

  * “follow Google-recommended practices” is an exclusion cue favoring the documented, purpose-built mechanism over an ad hoc or tangential configuration task.

**Why This Is Correct**

The VM instance rightsizing recommender, accessed through the Recommender API, automatically monitors a Compute Engine instance’s CPU and memory utilization over the trailing eight days and produces a specific, ready-to-apply recommendation for a better-fitting machine type — no manual configuration or agent installation is required to get this CPU-based recommendation, since Compute Engine already collects the underlying utilization data by default. Querying the Recommender API and applying its suggestion is the single, documented, lowest-step path from historical metrics to a chosen machine type, satisfying every constraint in the scenario at once.

**Why the Other Options Are Not the Best Fit**

**Option B — Technically Possible but Not Best:** an Agent Policy that installs the Ops Agent fleet-wide can improve recommendation accuracy or provide richer guest-level telemetry, but it’s an optional enhancement rather than a prerequisite for a base CPU-utilization recommendation, and it adds setup steps the scenario explicitly asks to avoid.

**Option C — Technically Possible but Not Best:** manually installing the Ops Agent through the gcloud CLI has the same issue as B — it’s an extra configuration step that doesn’t by itself identify a machine type, and it isn’t necessary for CPU-based rightsizing, which Compute Engine already monitors without it.

**Option D — Violates Requirement:** manually reviewing a dashboard and selecting a machine type by eye is a multi-step, subjective process rather than Google’s documented, repeatable mechanism, and it substitutes a vague heuristic (“lowest observed CPU utilization”) for the recommender’s actual sizing calculation — which can lead to choosing a machine type that doesn’t actually fit the workload.

**Exam Trap**

The trap is assuming that better recommendations must start with manually installing an agent, since Compute Engine already collects the CPU (and memory) utilization used for rightsizing by default — the Ops Agent steps look relevant but are an unnecessary detour for this specific, already-available CPU-based recommendation. If the scenario instead needed more granular guest-OS or application-level metrics to sharpen a memory-based recommendation, installing the Ops Agent would become a genuinely necessary step.

**Foundation Concept**

Google Cloud’s Active Assist recommenders continuously analyze operational telemetry Google already collects and turn it into specific, actionable suggestions exposed through the Recommender API, console, or gcloud CLI, removing the need for an operator to manually collect, graph, and interpret metrics before making an infrastructure decision. Recognizing that a recommender already exists for a given optimization goal is usually the fastest, most Google-aligned path, compared to building the same analysis by hand.

**Real-World Connection**

A platform team managing hundreds of Compute Engine VMs across a global organization uses the VM instance rightsizing recommender to surface overprovisioned and underprovisioned machines automatically, instead of having an engineer manually chart CPU usage for each VM. Applying the suggested machine type changes directly from the recommendation reduces wasted spend on oversized VMs and protects performance on undersized ones, without a separate metrics-collection effort to design and maintain.

**Memory Hook**

“Before you build your own dashboard-and-judgment process, check whether a recommender already does the sizing for you.”

**30-Second Exam Takeaway**

When a question asks for the fastest, Google-recommended way to pick a resource size or configuration based on data Google already collects, look first for the matching Active Assist recommender exposed through the Recommender API, rather than agent installation or manual dashboard analysis.

**Official References**

[**Google Cloud — Apply machine type recommendations to VM instances (VM instance rightsizing recommender):**](https://cloud.google.com/recommender/docs/vm-instance-rightsizing-recommender) Supports: correct-answer mechanism — automatic CPU/memory utilization analysis over the trailing 8 days and ready-to-apply recommendations via the Recommender API

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 5.1, Collecting performance information in Google Cloud):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment — Active Assist insights and recommendations

</details>

---

### Exam 5 · Q4

**You manage the backend infrastructure of a mobile game running on a Google Kubernetes Engine (GKE) cluster, serving HTTP requests from users. To optimize network expenses, what step should you take?**

- I. Establish the VPC as a Shared VPC Host project.
- II. Set up your network services on the Standard Tier.
- III. Configure your Kubernetes cluster as a Private Cluster.
- IV. Implement a Google Cloud HTTP Load Balancer as Ingress.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Set up your network services on the Standard Tier.

**Correct option: II**

**Why option II is correct**

**II. Set up your network services on the Standard Tier.**

When the explicit goal is to **optimize network expenses** , the most direct and impactful lever in Google Cloud is the **Network Service Tier** selection.

  * **Standard Tier** is priced lower than Premium Tier because traffic is routed over the public internet instead of Google’s global private backbone.

  * For a **mobile game backend** where traffic is typically **regional** and ultra-low global latency is not the primary requirement, Standard Tier provides **significant cost savings** on:

    * Network egress

    * Load-balancing data processing

  * This choice requires **no changes to application code or cluster design** , making it the cleanest cost-optimization step.

This is a classic **exam signal** : when cost optimization is the focus (not latency, availability, or security), **Standard Tier** is the expected answer.

Authoritative documentation:  
<https://cloud.google.com/network-tiers/docs/overview>

**Why the other options are not correct**

**I. Establish the VPC as a Shared VPC Host project.**  
Shared VPC improves **network governance and IAM separation** , not runtime network costs. It does not reduce egress or traffic processing charges.

**III. Configure your Kubernetes cluster as a Private Cluster.**  
Private clusters improve **security** by removing public node IPs. They do not reduce inbound HTTP traffic costs and may even introduce additional NAT costs.

**IV. Implement a Google Cloud HTTP Load Balancer as Ingress.**  
While this is architecturally recommended for HTTP workloads, **external HTTP(S) Load Balancing runs on Premium Tier by default** , which is **more expensive** , not cheaper. It optimizes performance, not cost.

**Final answer:** **II**

</details>

---

### Exam 5 · Q7

**To diminish costs for a stable, business-critical workload running on a fixed set of Compute Engine instances over several months, without compromising performance, what's the recommended approach?**

- I. Opt for Committed Use Discounts to avail discounted pricing.
- II. Transition the instances to a Managed Instance Group for enhanced management and potential cost efficiencies.
- III. Convert the instances to preemptible virtual machines to benefit from lower pricing for non-essential workloads.
- IV. Set up an Unmanaged Instance Group dedicated to running the workload on instances.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Opt for Committed Use Discounts to avail discounted pricing.

**Correct option: I**

**Why option I is correct**

**I. Opt for Committed Use Discounts to avail discounted pricing.**

For a **stable, business-critical workload** running on a **fixed set of Compute Engine instances over several months** , **Committed Use Discounts (CUDs)** are the **recommended and exam-correct approach**.

Core cost-optimization principles:

  * **Designed for predictable workloads:** CUDs provide significant discounts (up to ~55–70%) in exchange for a **1-year or 3-year commitment** on vCPU, memory, or specific machine types.

  * **No performance impact:** Unlike preemptible/Spot VMs, committed instances **retain full availability and performance guarantees**.

  * **No architectural changes required:** You continue running the same instance types; the discount is applied automatically to matching usage.

  * **SRE-aligned:** Reduces cost while maintaining reliability for business-critical services.

This exactly matches the scenario: _long-running, stable, fixed capacity, performance-sensitive workload_.

Authoritative documentation:  
<https://cloud.google.com/compute/docs/instances/committed-use-discounts-overview>

**Why the other options are not suitable**

**II. Transition the instances to a Managed Instance Group (MIG).**  
MIGs improve **availability, scaling, and lifecycle management** , but they **do not reduce compute pricing** by themselves. Cost savings come from discounts, not grouping.

**III. Convert the instances to preemptible virtual machines.**  
Preemptible (Spot) VMs are **not suitable for business-critical workloads** because they can be terminated at any time. This violates the “without compromising performance” requirement.

**IV. Set up an Unmanaged Instance Group.**  
Unmanaged instance groups offer **no cost benefits** and add operational complexity. They are not a pricing optimization mechanism.

**Final answer:** **I**

</details>

---

### Exam 5 · Q18

You manage **several production systems** that run on **Compute Engine** in the same **Google Cloud Platform (GCP) project**.

Each system has its **own set of dedicated Compute Engine instances**.

You want to know **how much it costs to run each system**.

What should you do?

- **A.** In the **Google Cloud Console** , use the **Cost Breakdown section** to visualize the **costs per system**.
- **B.** **Assign all instances a label specific to the system they run**. Configure **BigQuery billing export** and query **costs per label**.
- **C.** **Enrich all instances with metadata** specific to the system they run. Configure **Cloud Logging (formerly Stackdriver Logging) to export to BigQuery** , and query **costs based on the metadata**.
- **D.** **Name each virtual machine (VM) after the system it runs**. Set up a **usage report export** to a **Cloud Storage bucket**. Configure the bucket as a source in **BigQuery** to **query costs based on VM name**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** **B.** **Assign all instances a label specific to the system they run**. Configure **BigQuery billing export** and query **costs per label**.

**Correct Answer:**

**B.** **Assign all instances a label specific to the system they run**. Configure **BigQuery billing export** and **query costs per label**.

**Explanation:**

  * **Google Cloud billing supports resource labels** that allow you to **track costs based on specific attributes** like **which system a VM belongs to**.

  * **BigQuery billing export** provides **detailed billing data** , which can be queried **by labels to determine per-system costs**.

  * This approach **follows Google Cloud best practices for cost allocation** and allows for **granular cost analysis**.

**Steps to Implement:**

  1. **Assign labels to Compute Engine instances** for each system:
        
                    1. bash
            2. CopyEditgcloud compute instances add-labels instance-name --labels=system=my-system

  2. **Enable BigQuery billing export** to **store billing data**.

  3. **Query costs per system using BigQuery** :
        
                    1. sql
            2. CopyEditSELECT service.description, labels.system, SUM(cost) AS total_cost
            3. FROM `billing_dataset.gcp_billing_export`
            4. WHERE usage_start_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
            5. GROUP BY service.description, labels.system
            6. ORDER BY total_cost DESC;

**Why Other Options Are Incorrect:**

**A. Using the Cost Breakdown section in Google Cloud Console** –

  * **The Cost Breakdown section does not provide detailed per-system costs**.

  * **It is not as granular as querying BigQuery exports with labels**.

**C. Exporting logs to BigQuery and querying based on metadata** –

  * **Cloud Logging does not track cost-related data**.

  * **Billing data is stored in Cloud Billing, not Cloud Logging** , so this approach **won't provide accurate cost breakdowns**.

**D. Naming VMs after the system and using usage report exports** –

  * **VM names are not included in detailed billing exports**.

  * **Labels are the recommended approach for cost allocation**.

**Reference Documentation:**

[ Using Labels for Cost Allocation](https://cloud.google.com/blog/topics/cost-management/use-labels-to-gain-visibility-into-gcp-resource-usage-and-spending)  
[ Exporting Cloud Billing Data to BigQuery](https://cloud.google.com/billing/docs/how-to/export-data-bigquery)

</details>

---

### Exam 5 · Q22

**When configuring the frontend tier of an application deployed in Google Cloud, which serves only users from the United Kingdom within the europe-west2 region, utilizing nginx and a managed instance group with an Envoy-based external HTTP(S) load balancer, what network tier and load balancing setup offer the most cost-effective solution?**

- I. Premium Tier with a global load balancer
- II. Premium Tier with a regional load balancer
- III. Standard Tier with a global load balancer
- IV. Standard Tier with a regional load balancer

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Standard Tier with a regional load balancer

**Correct option: IV**

**Why option IV is correct**

**IV. Standard Tier with a regional load balancer**

Your users are **only in the UK** and the application is served from **a single region (europe-west2)**. In this case, the most cost-effective design is to use a **regional external Application Load Balancer** (Envoy-based external HTTP(S) load balancer) with the **Standard Network Service Tier** :

  * In **Standard Tier** , the external Application Load Balancer is intended for **single-region** delivery (it distributes traffic to backends in a single region).

  * Google’s pricing guidance explicitly calls out the **regional external Application Load Balancer** as a cost-effective option for single-region workloads because it uses **Standard Tier** , which has lower outbound data transfer charges.

  * Since you are not serving global users, paying for global premium backbone/edge features is unnecessary for the requirement.

**Documentation:** <https://cloud.google.com/network-tiers/docs/overview>

**Why the other options are not suitable**

**I. Premium Tier with a global load balancer**  
Premium Tier is optimized for global users and multi-region/backbone performance. For a UK-only, single-region serving model, it is typically **more expensive than needed**.

**II. Premium Tier with a regional load balancer**  
Even though regional is correct for the geography constraint, choosing **Premium** defeats the cost goal when **Standard Tier regional** is available and intended for single-region delivery.

**III. Standard Tier with a global load balancer**  
For Envoy-based external HTTP(S) / external Application Load Balancing, **Standard Tier effectively operates in a single region** (not true global multi-region Anycast behavior). If you want global external Application Load Balancing behavior, it requires Premium Tier.

**Final answer: IV**

</details>

---

### Exam 5 · Q27

**To optimize costs, you've deployed a serverless application on Cloud Run in your production environment. How can you effectively identify the application's resource utilization?**

- I. Utilize Cloud Trace with distributed tracing to monitor the application's resource utilization.
- II. Use Cloud Profiler with Ops Agent to track the CPU and memory utilization of the application.
- III. Monitor the container CPU and memory utilization of the application using Cloud Monitoring.
- IV. Employ Cloud Ops to establish logs-based metrics for monitoring the resource utilization of the application.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Monitor the container CPU and memory utilization of the application using Cloud Monitoring.

**III. Monitor the container CPU and memory utilization of the application using Cloud Monitoring.**

Here's why this is the most direct and effective approach:

  * **Container-Level Metrics:** Cloud Run resources are allocated at the container level, making container-specific metrics essential for understanding utilization.

  * **Cloud Monitoring Integration:** Cloud Monitoring provides built-in metrics for tracking CPU, memory, and other resources for Cloud Run instances.

  * **Optimization Focus:** Monitoring container resource usage directly helps you make informed decisions about right-sizing your Cloud Run instances to reduce costs.

**Why Others Are Less Ideal:**

  * **I. Utilize Cloud Trace with distributed tracing...** Cloud Trace is primarily for investigating latency and performance issues in distributed systems, less so for granular resource monitoring.

  * **II. Use Cloud Profiler with Ops Agent...** Cloud Profiler is designed for code-level profiling, which might be less relevant than container-level resource tracking in a pure serverless context.

  * **IV. Employ Cloud Ops to establish logs-based metrics...** While logs hold valuable information, extracting detailed resource metrics from them can be complex compared to using Cloud Monitoring's pre-built metrics.

**Reference:**

<https://cloud.google.com/run/docs/monitoring?hl=ja>

</details>

---

### Exam 5 · Q35

**In your company's Google Kubernetes Engine (GKE) setup, the development environment's clusters are logging applications with verbosity, accessed by developers via kubectl logs without utilizing Cloud Logging. Additionally, there's no standardized logging structure across applications. To minimize logging-related costs while retaining GKE operational logs, what's the optimal approach?**

- I. Update the development cluster using the command: gcloud container clusters update --logging=SYSTEM.
- II. Modify the logging configuration for the development cluster with: gcloud container clusters update --logging=WORKLOAD.
- III. Disable the default logging sink within the project associated with the development environment using: gcloud logging sinks update _Default --disabled.
- IV. Implement an exclusion filter on the default logging sink within the project tied to the development environment with: severity >= DEBUG resource.type = "k8s_container".

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Implement an exclusion filter on the default logging sink within the project tied to the development environment with: severity >= DEBUG resource.type = "k8s_container".

**Correct Option:**

**IV. Implement an exclusion filter on the default logging sink within the project tied to the development environment with: severity >= DEBUG resource.type = "k8s_container".**

**Justification:**

  * **Targeted Filtering:** Directly addresses the verbose application logs by filtering out DEBUG and lower severity log entries from Kubernetes containers, significantly reducing log volume.

  * **Retains Operational Logs:** Keeps essential GKE system logs flowing to Cloud Logging for operational visibility.

  * **Minimal Change:** Minimizes disruption, requiring just a filter update on the existing logging sink.

  * **Cost-Effective:** Reduces the volume of ingested logs, directly impacting logging costs.

**Why Other Options Are Less Suitable:**

  * **I. Update the development cluster using the command: gcloud container clusters update --logging=SYSTEM.**

    * **Too Broad:** Disables application logging entirely, potentially hindering necessary debugging for developers.

    * **Loses Valuable Developer Insights:** May eliminate useful troubleshooting logs generated by developer-side applications.

  * **II. Modify the logging configuration for the development cluster with: gcloud container clusters update --logging=WORKLOAD.**

    * **No Filtering:** Doesn't address the verbosity issue. Logs would still be sent to Cloud Logging, incurring costs.

  * **III. Disable the default logging sink within the project associated with the development environment using: gcloud logging sinks update _Default --disabled.**

    * **Extreme Measure:** Completely disables all logging, including crucial GKE operational logs, hindering monitoring and troubleshooting.

</details>

---

### Exam 5 · Q41

**As you monitor a service employing n2-standard-2 Compute Engine instances for delivering large files, users complain of slow download speeds. Cloud Monitoring indicates that VMs are operating at maximum network throughput. How can you improve network throughput performance?**

- I. Enhance the VMs by adding more network interface controllers (NICs).
- II. Implement a Cloud NAT gateway and link it to the VMs' subnet.
- III. Upgrade the VMs' machine type to n2-standard-8.
- IV. Deploy the Ops Agent to access supplementary monitoring metrics.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Upgrade the VMs' machine type to n2-standard-8.

**Correct option: III**

**Why option III is correct**

**III. Upgrade the VMs' machine type to n2-standard-8.**

In Google Compute Engine, **network throughput scales with machine type size**. When Cloud Monitoring shows that VMs are already operating at **maximum network throughput** , it means the instances have hit their **per-VM network bandwidth ceiling** , not a software or configuration issue.

Key fundamental concepts:

  * **Network performance is tied to vCPU count** : Larger machine types provide higher **egress and ingress bandwidth caps**.

  * **n2-standard-2** instances have relatively low maximum network throughput, which is insufficient for serving **large file downloads** at high speed.

  * By upgrading to **n2-standard-8** , you significantly increase:

    * Available network bandwidth

    * Packet processing capacity

    * Sustained throughput per VM

  * This improves download speeds **without changing application logic or architecture** , making it the most direct and effective fix.

This is a classic **capacity scaling** scenario where vertical scaling is the correct response.

**Relevant documentation:**  
<https://cloud.google.com/compute/docs/network-bandwidth>

**Why the other options are not suitable**

**I. Add more network interface controllers (NICs).**  
Multiple NICs are used for **network isolation or multi-network connectivity** , not for increasing outbound throughput of a single workload. They do not aggregate bandwidth for standard traffic flows.

**II. Implement a Cloud NAT gateway.**  
Cloud NAT provides **outbound internet access** for private VMs. It does not increase VM network throughput and can actually introduce additional limits.

**IV. Deploy the Ops Agent.**  
The Ops Agent improves observability only. It does not affect performance and does not remove network bandwidth limits.

**Final answer:** **III**

</details>

---

### Exam 5 · Q59

**Your Cloud Run-deployed application caters to users worldwide, and the goal is to configure Cloud Run to direct users to their nearest region for optimal response times. What is the recommended approach?**

- I. Deploy the application to a single region and serve it from a global anycast IP address routed behind a global external HTTP(S) load balancer.
- II. Deploy the application to each region and serve it from a global anycast IP address routed behind a global external HTTP(S) load balancer.
- III. Deploy the application to one region per continent, utilizing a regional external HTTP(S) load balancer in each region, and assign the same global IP address to all regional load balancers.
- IV. Deploy the application to a single region and configure Google Cloud Armor in the frontend to permit traffic from all IP addresses.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Deploy the application to each region and serve it from a global anycast IP address routed behind a global external HTTP(S) load balancer.

**The recommended approach to configure Cloud Run to direct users to their nearest region for optimal response times is:**

**II. Deploy the application to each region and serve it from a global anycast IP address routed behind a global external HTTP(S) load balancer.**

**Explanation:**

Deploying the application to each region and serving it from a global anycast IP address routed behind a global external HTTP(S) load balancer allows users to be directed to their nearest region based on latency, ensuring optimal response times. This approach leverages Google's global network infrastructure to route traffic efficiently to the closest region, minimizing latency and improving user experience.

**Justification for why other options are not suitable:**

**I. Deploy the application to a single region and serve it from a global anycast IP address routed behind a global external HTTP(S) load balancer.**

  * This approach does not utilize the benefits of deploying the application to multiple regions to minimize latency and improve response times for users worldwide.

**III. Deploy the application to one region per continent, utilizing a regional external HTTP(S) load balancer in each region, and assign the same global IP address to all regional load balancers.**

  * While deploying the application to one region per continent can improve latency compared to a single region deployment, it may not provide the most optimal response times as users within continents may still experience latency due to regional distances.

**IV. Deploy the application to a single region and configure Google Cloud Armor in the frontend to permit traffic from all IP addresses.**

  * This approach does not optimize response times by directing users to their nearest region. Instead, it allows traffic from all IP addresses, which may not necessarily result in the best user experience in terms of latency.

**References:**

<https://cloud.google.com/run/docs/multiple-regions>

<https://cloud.google.com/run/docs/container-contract>

</details>

---

### Exam 5 · Q64

**Your application contains a module responsible for executing a computationally intensive task. The development team aims to optimize this module by experimenting with different algorithms. To facilitate testing, the team wants to evaluate the performance of each algorithm in both staging and production environments, gathering detailed performance data. What action should you take?**

- A. Integrate the code with profiling libraries to collect detailed performance data. Visualize the data using Cloud Profiler, presenting it as flame graphs for analysis.
- B. Implement code instrumentation to track the flow of requests and responses. Analyze request latencies using Cloud Trace to assess algorithm performance.
- C. Integrate the code with log statements at various algorithmic stages. Utilize log-based notifications to capture data on algorithm execution.
- D. Embed log statements within the code at various algorithmic stages. Use log-metric-based notifications to capture data when specific control structures are invoked multiple times.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Integrate the code with profiling libraries to collect detailed performance data. Visualize the data using Cloud Profiler, presenting it as flame graphs for analysis.

**The best course of action to achieve this goal is**

**A. Integrate the code with profiling libraries to collect detailed performance data. Visualize the data using Cloud Profiler, presenting it as flame graphs for analysis.**

Here's why this approach is ideal:

  * **Focused on performance:** Profiling libraries are specifically designed to gather in-depth performance metrics about code execution, such as function call times, memory usage, and CPU consumption.

  * **Cloud Profiler Integration:** Cloud Profiler seamlessly integrates with GCP, collecting profiling data from your running application in both staging and production.

  * **Visual Analysis with Flame Graphs:** Flame graphs provide an intuitive, hierarchical visualization of where the code spends the most time, making bottlenecks easily identifiable.

  * **Algorithm-Specific Insights:** Profiling allows fine-grained analysis within your algorithms, helping compare their performance characteristics.

**Why Other Options are Less Suitable:**

  * **B. Cloud Trace:** Cloud Trace is primarily for tracing distributed requests and identifying latency issues across services, less focused on algorithmic performance within a module.

  * **C & D. Log statements & notifications:** While logging can provide some information, it's less efficient and accurate than profiling for detailed performance analysis. This approach can also become overly verbose.

**References:**

<https://cloud.google.com/profiler/docs/concepts-profiling>

<https://cloud.google.com/profiler/docs/measure-app-performance>

<https://cloud.google.com/profiler/docs/concepts-flame>

<https://codelabs.developers.google.com/codelabs/otel-cloudtrace-go#0>

</details>

---
