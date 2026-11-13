# Professional Cloud DevOps Engineer — Practice Exam 1

60 questions.

## Question 1

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You manage an application that exposes an HTTP endpoint directly, without a load balancer in front of it. HTTP response latency is critical to the user experience, and you want visibility into the latencies that all of your users are experiencing. You use Cloud Monitoring. What should you do?

- [ ] A. In your application, create a metric with `metricKind` set to `DELTA` and `valueType` set to `DOUBLE`. In Cloud Monitoring’s Metrics Explorer, use a Stacked Bar chart to visualize the metric.
- [ ] B. In your application, create a metric with `metricKind` set to `CUMULATIVE` and `valueType` set to `DOUBLE`. In Cloud Monitoring’s Metrics Explorer, use a Line chart to visualize the metric.
- [x] C. In your application, create a metric with `metricKind` set to `GAUGE` and `valueType` set to `DISTRIBUTION`. In Cloud Monitoring’s Metrics Explorer, use a Heatmap chart to visualize the metric.
- [ ] D. In your application, create a metric with `metricKind` set to `METRIC_KIND_UNSPECIFIED` and `valueType` set to `INT64`. In Cloud Monitoring’s Metrics Explorer, use a Stacked Area chart to visualize the metric.

### Explanation

**Correct Answer**

**C. In your application, create a metric with**`**metricKind**`**set to**`**GAUGE**`**and**`**valueType**`**set to**`**DISTRIBUTION**`**. In Cloud Monitoring’s Metrics Explorer, use a Heatmap chart to visualize the metric.**

**Exam Reasoning Explanation**

The hard requirement is understanding the latency experienced by _all_ users — not a single summary number like an average or a total. That rules out any scalar value type (DOUBLE, INT64) up front, because a single DOUBLE or INT64 value per time interval collapses every request’s latency into one number, discarding the shape of the distribution (how many requests were fast, how many were slow, whether there’s a long tail). DISTRIBUTION is the only value type built to preserve that per-request spread as a histogram. Once DISTRIBUTION is established as the required value type, the metric kind must also be a combination Cloud Monitoring actually permits for a custom (`custom.googleapis.com`) metric: DELTA-kind DISTRIBUTION metrics are explicitly disallowed for custom metrics, leaving GAUGE as the valid, practical choice for an application self-reporting a snapshot of recent latencies. The visualization then has to match the data: a Heatmap is purpose-built to render a single distribution-valued time series over time, which is exactly what this metric produces.

**Key Exam Clues**

  * “understand what HTTP latencies all of your users are experiencing” is a hard constraint — it demands the full distribution/spread of latency values, not an aggregate like a sum or average, which immediately rules out scalar value types.

  * “without using a load balancer” is a technical signal — it establishes that no managed load-balancer latency metric is automatically available, so the application itself must create and report this custom metric.

  * The metricKind/valueType pairing in each option is a decisive technical signal on its own: only one pairing (GAUGE + DISTRIBUTION) is both semantically correct for latency data and a permitted combination for a custom metric.

**Why This Is Correct**

A DISTRIBUTION-valued metric lets Cloud Monitoring bucket incoming latency measurements into a histogram, so instead of losing information to averaging, you retain the full shape of the data — letting you later compute arbitrary percentiles (p50, p90, p99) and see multimodal patterns an average would hide. Setting `metricKind` to GAUGE is the correct, custom-metric-compatible choice for an application reporting this distribution as periodic snapshots of recent request latencies (DELTA is not a valid kind for DISTRIBUTION-valued custom metrics). In Metrics Explorer, a Heatmap chart is specifically designed to display one distribution-valued time series, plotting time on the X-axis, latency buckets on the Y-axis, and using color intensity to represent how many requests fell into each bucket — giving you exactly the “latency experienced by all users” view the scenario asks for.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Incorrect:** DOUBLE is a scalar value type, so this metric could only ever report a single number per interval (e.g., a sum or count of latency), not the distribution across users; it can’t show the spread of experienced latencies at all. It’s also a disallowed combination for a custom metric, since DELTA-kind metrics are not permitted with custom.googleapis.com metrics for several value types. A Stacked Bar chart compounds the mismatch by being built for comparing discrete scalar categories, not rendering distribution data.

  * **Option B — Incorrect:** CUMULATIVE + DOUBLE would track something like total accumulated latency or total request count over time, which is a running total, not per-request distribution data — it tells you nothing about the spread of individual latencies. A Line chart reinforces that this option is designed to show a scalar trend over time, not a histogram.

  * **Option D — Incorrect:** `METRIC_KIND_UNSPECIFIED` is not a usable kind for an actual custom metric definition — it’s a placeholder/default value in the API, not a deliberate choice you’d make when creating a metric. INT64 is again a scalar type, incapable of representing a distribution, and a Stacked Area chart is built for comparing multiple scalar series over time, not visualizing one distribution’s bucketed values.

**Exam Trap**

The trap is assuming that any numeric metric type (DOUBLE or INT64) is “good enough” for latency monitoring as long as you’re collecting _something_ — especially since CUMULATIVE/DOUBLE (Option B) sounds plausible for “tracking latency over time.” The decisive distinction the exam is testing is between _aggregate_ numeric reporting (which erases per-request detail) and _distribution-valued_ reporting (which preserves it) — only the latter can answer “what are all my users experiencing,” since an average or sum can look identical whether every user had the same latency or half had near-zero latency and half had extreme outliers.

**Foundation Concept**

When you need to understand the full experience across a population of events (requests, users, transactions) rather than a single rolled-up number, distribution-valued metrics and histogram-style visualization (heatmaps, percentile charts) are the correct tool — averages and simple counters are appropriate for trend-watching a single aggregate quantity, not for characterizing variability or spotting a problematic tail of slow requests hiding behind a healthy-looking mean.

**Real-World Connection**

In practice, teams exposing an HTTP endpoint without a managed load balancer (which would otherwise provide built-in request-latency distribution metrics automatically) instrument the application directly with a DISTRIBUTION-valued custom metric, then build a Heatmap or percentile-based dashboard in Cloud Monitoring to catch latency regressions — a p99 spike that would be completely invisible in a mean-latency line chart often reveals the exact subset of requests (e.g., those hitting a cold cache or a specific downstream dependency) causing real user pain.

**Memory Hook**

“Latency across all users” → DISTRIBUTION value type (never a scalar) → GAUGE kind for a custom metric → Heatmap chart to visualize it.

**30-Second Exam Takeaway**

Whenever a Cloud Monitoring question asks you to understand the full spread or experience of a measurement across many events rather than a single aggregate, reach for a DISTRIBUTION-valued metric (GAUGE kind for custom metrics) visualized with a Heatmap — scalar value types (DOUBLE, INT64) and their matching chart types (Line, Bar, Stacked Area) are built for trend-watching single numbers, not for representing per-event variability.

**Official References**

[Google Cloud — About distribution-valued metrics: ](https://docs.cloud.google.com/monitoring/charts/charting-distribution-metrics)Supports: the correct-answer mechanism of using DISTRIBUTION-valued metrics to capture HTTP latency spread, and Heatmap charts as the designed visualization for a single distribution-valued time series

[**Google Cloud — Metric kinds and value types (custom metrics):**](https://cloud.google.com/monitoring/api/v3/kinds-and-types) Supports: the valid metricKind/valueType combinations, including that DELTA-kind DISTRIBUTION metrics are not permitted for custom (`custom.googleapis.com`) metrics, making GAUGE the correct kind here

---

## Question 2

*Domain 3: Applying Site Reliability Engineering Practices*

You maintain a stateless, web-based API running on a single Compute Engine instance in the `europe-west2-a` zone. The Service Level Indicator (SLI) for availability is falling short of the defined Service Level Objective (SLO). A postmortem determined that requests are timing out because the API receives a high volume of traffic and the instance is running out of memory. You need to improve service availability. What should you do?

- [ ] A. Adjust the SLO so that it matches the currently measured SLI.
- [ ] B. Migrate the service to a larger Compute Engine instance type with more memory.
- [x] C. Deploy additional service instances across other zones and distribute traffic across all of them using a load balancer.
- [ ] D. Deploy additional service instances across other zones and configure them as failover targets to take over if the primary instance becomes unavailable.

### Explanation

**Correct Answer**

**C. Deploy additional service instances across other zones and distribute traffic across all of them using a load balancer.**

**Exam Reasoning Explanation**

The must-have constraints are: the root cause is resource exhaustion under high request volume (out-of-memory timeouts), and the goal is improved _availability_ specifically — not just fixing one symptom. A single instance, however large, remains a single point of failure tied to one zone; if that zone has an outage, the service goes down regardless of its spec. The only option that addresses both the capacity problem (spreading request load across multiple instances relieves per-instance memory pressure) and the availability problem (removing the single-zone, single-instance dependency) is horizontal scaling across zones combined with active load balancing, since all instances share the traffic continuously rather than sitting idle waiting for a failure.

**Key Exam Clues**

  * “stateless” is a hard enabler — it’s a technical signal that the service can safely run on multiple concurrent instances with no session-affinity or shared-state concerns, which is what makes load-balanced horizontal scaling viable.

  * “running out of memory” under “high number of requests” is the root cause — it points toward a capacity/scaling fix, not merely a redundancy fix.

  * “improve service availability” is the stated objective — it’s a sequence/scope instruction that the chosen fix must raise the measured SLI, not just paper over the gap or address only half the problem (capacity or resilience alone).

**Why This Is Correct**

Running multiple stateless instances across different zones behind a load balancer accomplishes two things simultaneously: it distributes incoming requests so no single instance is overwhelmed to the point of exhausting memory (directly fixing the postmortem’s identified cause of the timeouts), and it removes the single-zone, single-instance fragility, so a zonal failure no longer takes the whole service down. Because load balancing is active (all instances serve traffic all the time), this also means capacity scales with demand rather than sitting unused until disaster strikes — which is what actually raises the measured availability SLI toward the SLO.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Lowering the SLO to match the current SLI doesn’t improve availability at all — it just redefines the target downward to make the problem disappear on paper. This conflicts directly with the stated goal of improving service availability and ignores the user-facing timeout issue entirely.

  * **Option B — Technically Possible but Not Best:** A bigger instance with more memory would likely reduce or eliminate the out-of-memory timeouts, addressing the capacity symptom. However, it leaves the service as a single instance in a single zone — a zonal outage still causes a full availability loss, so it doesn’t resolve the broader availability objective as completely as distributing across zones does.

  * **Option D — Technically Possible but Not Best:** Adding failover instances in other zones does remove the single-zone dependency, but a passive failover instance sits idle until the primary fails — it does nothing to relieve the primary instance’s memory pressure under normal high-traffic conditions, so the root-cause timeouts identified in the postmortem would persist until an actual failover event occurs. This would be the better choice only if the postmortem’s root cause were purely a zonal-outage risk rather than sustained resource exhaustion under normal load.

**Exam Trap**

The trap is picking D because “failover in case the primary instance is unavailable” sounds like the textbook high-availability pattern. But the postmortem’s root cause here isn’t an unavailable primary instance — it’s an overloaded one. A passive failover design doesn’t touch that root cause at all; only active load distribution does. If the scenario instead described a hardware/zone failure with no capacity issue, D would become the stronger answer.

**Foundation Concept**

For a stateless service experiencing availability loss from resource exhaustion, the SRE-aligned fix is horizontal scaling with active load balancing, not vertical scaling (bigger instance) or passive redundancy (failover) alone — those each solve only one dimension (capacity or resilience) of a two-dimensional availability problem.

**Real-World Connection**

Teams facing this pattern typically deploy a managed instance group spanning multiple zones behind an external or internal load balancer, paired with autoscaling based on CPU/memory or request-based signals, so capacity grows automatically with demand and a single zone’s failure only removes a fraction of total capacity rather than the entire service — directly improving the measured SLI against the error-budget-driven SLO.

**Memory Hook**

Timeouts from overload + availability goal → scale horizontally across zones with active load balancing, not a bigger box or an idle backup.

**30-Second Exam Takeaway**

When a postmortem ties availability loss to resource exhaustion under load, look for the option that both multiplies capacity and spreads it across failure domains with active traffic distribution — vertical scaling and passive failover each only solve half the problem.

**Official References**

[**Google Cloud — Managed instance groups for highly available, scalable applications:**](https://cloud.google.com/compute/docs/instance-groups) Supports: the correct-answer mechanism of distributing stateless workloads across multiple zones with active load balancing to address both capacity and availability

[**Google Cloud Architecture Framework — Reliability pillar:**](https://cloud.google.com/architecture/framework/reliability) Supports: why horizontal scaling plus load balancing is preferred over vertical scaling or passive failover for improving availability against an SLO

---

## Question 3

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You support an application running on Google Cloud and want to configure SMS notifications for your team for the most critical alerts in Cloud Monitoring. You have already identified which alerting policies should trigger these notifications. What should you do?

- [ ] A. Download and configure a third-party integration between Cloud Monitoring and an SMS gateway. Have your team members add their phone numbers to the external tool.
- [ ] B. Select the Webhook notification option for each alerting policy, and configure it to call a third-party integration tool. Have your team members add their phone numbers to the external tool.
- [x] C. Have your team members add and verify their phone numbers as SMS notification channels in Cloud Monitoring. Select the SMS notification type for each alerting policy, and choose the appropriate verified phone numbers from the list.
- [ ] D. Configure a Slack notification for each alerting policy. Set up a Slack-to-SMS integration to forward Slack messages as SMS. Have your team members add their phone numbers to the external integration.

### Explanation

**Correct Answer**

**C. Have your team members add and verify their phone numbers as SMS notification channels in Cloud Monitoring. Select the SMS notification type for each alerting policy, and choose the appropriate verified phone numbers from the list.**

**Exam Reasoning Explanation**

The must-have constraint is getting SMS notifications working for specific, already-identified alerting policies with the least unnecessary complexity. Cloud Monitoring natively supports SMS as a first-class notification channel type: you verify a phone number as a notification channel, then attach that channel directly to an alerting policy. Since this native capability exists and directly satisfies the requirement, any option that introduces a third-party gateway, a webhook relay, or a chained Slack-to-SMS bridge is solving the same problem with more moving parts, more external dependencies, and more points of failure than necessary — none of which the scenario calls for.

**Key Exam Clues**

  * “SMS notifications... in Cloud Monitoring” is a hard constraint — it specifies the notification medium and the platform, pointing toward checking whether that platform has native support before reaching for an external tool.

  * “You have already identified the alerting policies you want to configure this for” is a scope/sequence signal — the task is purely about wiring up notification delivery to existing policies, not building new infrastructure or integrations.

  * “most critical alerts” implies reliability matters — an extra external hop (webhook → third-party tool → SMS, or Slack → SMS bridge) introduces more failure points between the alert firing and the message reaching someone’s phone than a direct, native channel does.

**Why This Is Correct**

Cloud Monitoring lets you add SMS as a notification channel directly in the Alerting section of the console: each team member’s phone number is entered and verified there, after which it appears as a selectable SMS channel. When creating or editing an alerting policy, you choose the SMS notification type and select the relevant verified phone numbers from that list, and Cloud Monitoring delivers the SMS itself when the policy fires — no external gateway, webhook, or chat-platform bridge required. This is the simplest path that fully satisfies the stated need, using functionality Cloud Monitoring already provides out of the box.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** A third-party SMS gateway integration could technically deliver text messages, but it duplicates a capability Cloud Monitoring already provides natively, adding an unnecessary external dependency, additional configuration and account management outside Google Cloud, and another potential point of failure for critical alerts — with no corresponding benefit given the requirement as stated.

  * **Option B — Different Use Case:** Webhook notifications are the correct tool when you need to push alert data into a system that doesn’t have a purpose-built Cloud Monitoring integration (a custom incident-management tool, for example), triggering custom logic on receipt. Using a webhook here to reach a third-party SMS relay solves a problem that native SMS support already solves more directly, so it’s solving the right kind of problem with the wrong tool for this scenario.

  * **Option D — Different Use Case:** Slack notifications are well suited for team-visible, non-urgent alert awareness, and Slack itself has a native Cloud Monitoring integration. But chaining a Slack-to-SMS bridge on top adds two additional integration layers (Cloud Monitoring → Slack → external SMS bridge) purely to reach a destination (SMS) that Cloud Monitoring can already notify directly — this is unnecessary complexity for the stated goal.

**Exam Trap**

The trap is assuming that because Options A, B, and D all plausibly end in an SMS being delivered, they’re all “valid” answers that differ only in implementation detail — when the real test is whether you know Cloud Monitoring has native SMS support at all. Engineers unfamiliar with that native capability are prone to reach for an external integration pattern (webhook, Slack bridge, third-party gateway) by habit, when the simplest and most reliable answer is already built into the product.

**Foundation Concept**

Before reaching for a webhook, custom integration, or a chained notification path through another platform, check whether the target notification channel is natively supported — Cloud Monitoring supports several channel types out of the box (email, SMS, mobile app push, PagerDuty, Slack, and more), and using the native channel is almost always preferable to replicating that functionality through an indirect integration, since it reduces operational surface area and failure points for alerts that matter.

**Real-World Connection**

Teams running critical production services typically configure multiple native notification channels for their highest-severity alerting policies — for example, both a PagerDuty channel for on-call paging and an SMS channel as a backup — specifically because Google’s own guidance notes SMS isn’t a fully reliable channel type on its own and recommends pairing it with another channel type, which is only a realistic practice once you’re using the native, directly configurable channels rather than a chain of external integrations.

**Memory Hook**

Before building a custom path to a notification medium, check whether Cloud Monitoring already supports it natively — SMS, like email and Slack, is a built-in notification channel type, not something you need to bridge to.

**30-Second Exam Takeaway**

When a Cloud Monitoring alerting question describes a notification requirement, first ask whether that channel type is natively supported before considering webhooks or third-party integrations — native channels (email, SMS, PagerDuty, Slack, mobile push) are simpler, more reliable, and the expected answer whenever they directly satisfy the stated need.

**Official References**

[Google Cloud — Create and manage notification channels: ](https://docs.cloud.google.com/monitoring/support/notification-options)Supports: the correct-answer mechanism of adding and verifying an SMS phone number as a native notification channel, then selecting it when configuring an alerting policy

---

## Question 4

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

Your DevOps team is growing, and you have recently adopted Terraform to manage your cloud infrastructure. You need a way to version your Terraform configuration files and share them with the rest of the team. What should you do?

- [x] A. Store the Terraform configuration files in a version-control system, and establish procedures for committing new changes and merging them into the main branch.
- [ ] B. Store the Terraform configuration files in a shared network drive with a separate subfolder for each release, and have each team member work on a different set of files.
- [ ] C. Store the Terraform configuration files in a Cloud Storage bucket with object versioning enabled, and grant every team member access so they can download the files.
- [ ] D. Store the Terraform configuration files in a shared Google Drive folder that syncs automatically to each team member’s machine, and use a file-naming convention to track each new version.

### Explanation

**Correct Answer**

**A. Store the Terraform configuration files in a version-control system, and establish procedures for committing new changes and merging them into the main branch.**

**Exam Reasoning Explanation**

The hard requirement here is two-fold: true code _versioning_ (a history of changes, who made them, and the ability to diff/revert) and controlled _collaboration_ among multiple engineers editing the same codebase. A version-control system (VCS) such as Git is purpose-built for both: it tracks every change as a commit, supports branching, and uses merge workflows (pull/merge requests, code review) to reconcile concurrent edits safely. The other three options each substitute a generic file-storage or file-sync mechanism for an actual VCS, which satisfies “a copy of the files exists somewhere shared” but not “versioned, collaboratively editable code” — the distinction the question is testing.

**Key Exam Clues**

  * “implement code versioning” is a hard constraint — it demands real revision history, not just file storage.

  * “share code with other team members” is a collaboration requirement — it implies concurrent, multi-author editing, not read-only distribution.

  * “team of Infrastructure DevOps Engineers is growing” signals scale — the solution must hold up as more people edit the same code, favoring conflict-resolution tooling over manual coordination.

**Why This Is Correct**

A VCS (Git, typically hosted on Cloud Source Repositories, GitHub, or GitLab) stores every change as a discrete, reversible commit tied to an author and timestamp, which is the textbook definition of “code versioning.” Branching and merge workflows let multiple engineers work in parallel on the same Terraform configuration without overwriting each other’s changes, and establishing a push/merge procedure (e.g., feature branches plus pull requests into `main`) adds the review gate needed to keep shared infrastructure code trustworthy as the team scales. This is also the foundation Google Cloud’s own recommended practices build on: CI/CD pipelines for Terraform (via Cloud Build or similar) are triggered from VCS commits, so starting with a VCS is the prerequisite for everything that follows in a mature IaC workflow.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Violates Requirement:** A network shared folder with per-release subfolders provides no real diff/merge capability and no commit history; “everyone works on different files” is a manual, error-prone substitute for concurrency control, and it doesn’t scale as the team grows — it directly fails the versioning requirement.

  * **Option C — Technically Possible but Not Best:** Cloud Storage object versioning does preserve prior versions of an object, so it has a surface-level resemblance to “versioning.” But it has no concept of commits, authorship, diffs, branches, or merges — it’s built for object/blob storage, not collaborative source-code management, so it can’t support the “sharing and working together” half of the requirement.

  * **Option D — Different Use Case:** Google Drive sync plus a file-naming convention is a document-collaboration pattern, not a code-collaboration one. Simultaneous edits to the same `.tf` file risk silent overwrites or sync conflicts, and naming conventions are a manual, unenforceable stand-in for real version history.

**Exam Trap**

The trap is conflating _object/file versioning_ (Option C) with _source-code versioning_ (Option A) because both use the word “version.” Cloud Storage versioning would only become the right tool if the question were about retaining historical copies of a single uploaded artifact (e.g., a state file backup), not about a team collaboratively authoring and merging code.

**Foundation Concept**

Infrastructure as Code should be treated exactly like application code: it belongs in a VCS with branching, code review, and merge policies, because infrastructure changes carry the same risk of conflicting or regressive edits as application changes do. “Storage with history” (object versioning, file shares) is not a substitute for “collaboration with history” (a VCS), which is the broader principle this question is probing.

**Real-World Connection**

Teams that skip a VCS for Terraform typically discover the cost later: untracked manual edits to shared `.tf` files cause state drift, nobody can tell who changed a security group rule or why, and rolling back a bad change means hand-reconstructing it from memory. Adopting Git from day one with a merge-request workflow turns every infrastructure change into a reviewable, auditable, revertible unit — which is also what lets you later wire Terraform into a CI/CD pipeline (plan on pull request, apply on merge).

**Memory Hook**

If the question is about _collaboratively versioning code_ (not just storing file copies), the answer is a version-control system — full stop.

**30-Second Exam Takeaway**

Whenever a DevOps scenario mentions a growing team needing to version and share _code_ (including Terraform/IaC), look for the option describing a VCS with branch/merge procedures — file shares, Drive sync, and object-storage versioning are all distractors dressed up as “versioning” but lack collaborative merge capability.

**Official References**

[**Google Cloud — Infrastructure as Code with Terraform (best practices):**](https://cloud.google.com/docs/terraform/best-practices/general-style-structure) Supports: why Terraform configurations should live in a VCS with branching/merge workflows as the basis for IaC management

[**Google Cloud — Cloud Source Repositories overview:**](https://cloud.google.com/source-repositories/docs) Supports: Google Cloud’s own recommended Git-based version-control service for storing and collaborating on infrastructure code

---

## Question 5

*Domain 5: Optimizing Performance and Cost*

Your organization wants to lower Compute Engine spend, and after evaluating the options, you decide to use Spot VMs for part of the workload. Which of the following applications is best suited to run on Spot VMs?

- [ ] A. A horizontally scalable in-memory caching system.
- [ ] B. The organization’s public-facing website.
- [x] C. A distributed, eventually consistent NoSQL database cluster with sufficient quorum.
- [ ] D. A GPU-accelerated video-rendering platform that reads source files from and writes rendered output to a storage bucket.

### Explanation

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

---

## Question 6

*Domain 3: Applying Site Reliability Engineering Practices*

Your organization follows Site Reliability Engineering practices. You are acting as Incident Commander for a new, customer-impacting incident. To run an effective incident response, you need to immediately delegate two other incident management roles. Which two roles should you assign? (Choose two.)

- [x] A. Operations Lead
- [ ] B. Engineering Lead
- [x] C. Communications Lead
- [ ] D. Customer Impact Assessor
- [ ] E. External Customer Communications Lead

### Explanation

**Correct Answer**

**A. Operations Lead**

**C. Communications Lead**

**Exam Reasoning Explanation**

Google’s Incident Management at Google (IMAG) framework, which formalizes SRE incident response, defines exactly three core roles for a well-run incident: Incident Commander (IC), Operations Lead (OL), and Communications Lead (CL). The scenario already assigns you the IC role, so the question is really asking which of the framework’s other canonical roles exist to delegate — and only Operations Lead and Communications Lead are part of that defined structure. Everything else in the option list is a plausible-sounding but non-canonical title: delegating to roles the framework doesn’t define would leave you without the specific, well-understood division of labor the IMAG structure is designed to provide during the time-pressured opening minutes of an incident.

**Key Exam Clues**

  * “immediately assign two incident management roles” is a hard constraint signaling a two-answer MSQ drawn from a known, named set of roles rather than an open-ended staffing decision.

  * “Site Reliability Engineering practices” is a technical signal that points specifically to Google’s IMAG role taxonomy as the authoritative framework to apply, not a generic or company-specific incident-response structure.

  * “to assist you” (the IC) in “effective incident response” implies the two roles must report to and relieve the IC of defined categories of work — technical mitigation and stakeholder communication — which is precisely the IC/OL/CL hierarchy’s design.

**Why This Is Correct**

In IMAG, the IC retains overall authority and, by default, personally holds any role not yet delegated — so the first priority in a growing incident is to hand off the two other defined roles so the IC can focus on coordination and decision-making rather than execution. The Operations Lead takes ownership of the hands-on technical response: diagnosing the problem, applying mitigations, and directing the team actually modifying the system. The Communications Lead takes ownership of keeping stakeholders — internal teams, leadership, and (when needed) customers — informed with accurate, timely updates, which both frees the IC from fielding status questions and ensures messaging stays consistent. Together, these two delegated roles cover the two major categories of work an incident generates (fixing it, and communicating about it), which is exactly why IMAG defines no more and no fewer than these three roles for a standard incident.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Incorrect:** “Engineering Lead” is not a defined role in Google’s IMAG framework. It’s the kind of title that sounds plausible by analogy to common organizational roles, but it doesn’t correspond to a specific, recognized incident-management responsibility within this framework — the technical mitigation function it might suggest is already owned by the Operations Lead.

  * **Option D — Incorrect:** “Customer Impact Assessor” is not one of the IMAG roles. Assessing customer impact is something that naturally falls under the Communications Lead’s remit (to inform accurate messaging) or the Operations Lead’s technical assessment, rather than being split out as its own formally defined role.

  * **Option E — Incorrect:** “External Customer Communications Lead” is a plausible-sounding but non-canonical variant of the Communications Lead role. IMAG’s Communications Lead already covers both internal and external communications as a single unified role; splitting external customer communications into a separate title isn’t part of the standard framework.

**Exam Trap**

The trap is being pulled toward option titles that sound organizationally reasonable — “Engineering Lead,” “Customer Impact Assessor” — because they resemble roles you might see in a generic corporate incident process. The exam is specifically testing recall of IMAG’s precise, minimal three-role structure (IC, OL, CL); any title outside that exact set should be treated as a distractor, however sensible it sounds in isolation.

**Foundation Concept**

IMAG deliberately keeps its core role set small — Incident Commander, Operations Lead, Communications Lead — because during an active incident, clarity about who owns what (and who to report to) matters more than granular role specialization. The IC can further delegate sub-tasks or pull in subject matter experts as needed, but those are informal extensions of the OL’s technical work, not separately named roles in the framework itself.

**Real-World Connection**

In practice, a growing on-call team typically keeps IC, OL, and CL as separate rotations so that a single person isn’t trying to simultaneously fix the problem, coordinate the team, and answer stakeholder questions during a high-pressure incident — splitting these concerns early (exactly as this question describes doing “immediately”) is what lets each function operate without one bottlenecking the others, directly improving time-to-mitigation.

**Memory Hook**

IMAG has exactly three roles: IC, Ops Lead, Comms Lead — if a title isn’t one of those three, it isn’t a canonical incident management role.

**30-Second Exam Takeaway**

Whenever a question asks which roles an Incident Commander should delegate under SRE/IMAG practices, the answer set is always drawn from Operations Lead and Communications Lead — any other-sounding title (Engineering Lead, Impact Assessor, etc.) is a distractor built to sound plausible without being part of the defined framework.

**Official References**

[**Google SRE — Incident Management Guide:**](https://sre.google/static/pdf/IncidentManagementGuide.pdf) Supports: the correct-answer mechanism — IMAG’s three core roles (Incident Commander, Operations Lead, Communications Lead) and their reporting relationship to the IC

[Google SRE Workbook — Chapter 9, Incident Response: ](https://sre.google/workbook/incident-response/)Supports: the detailed responsibilities of the Operations Lead and Communications Lead roles within an active incident

---

## Question 7

*Domain 2: Building and Implementing CI/CD Pipelines*

Your organization has moved to a container-based development model. Your team builds many applications that flow continuously through an automated build pipeline into a Kubernetes cluster running in production. The security auditor is worried that a developer or operator could bypass automated testing and push code changes straight to production without the required approval. What should you do to enforce that approval step?

- [ ] A. Configure the build system to use protected branches that require pull request approval before merging.
- [ ] B. Use an admission controller to verify that incoming requests to the cluster originate from approved sources.
- [ ] C. Use Kubernetes Role-Based Access Control (RBAC) to restrict cluster access to only approved users.
- [x] D. Enable Binary Authorization on the Kubernetes cluster, and configure the build pipeline as an attestor.

### Explanation

**Correct Answer**

**D. Enable Binary Authorization on the Kubernetes cluster, and configure the build pipeline as an attestor.**

**Exam Reasoning Explanation**

The must-have constraint is specifically about the deploy-time gate: the auditor’s concern is that someone could circumvent automated testing and push an image to the production cluster without the testing/approval pipeline having actually run on it. That means the control needs to be enforced at the point where workloads are admitted to run in the cluster, and it needs to verify that a specific trusted process (the pipeline) actually vetted the image — not just that a person was authorized to act, or that a process was followed earlier upstream. Binary Authorization is purpose-built for exactly this: it blocks deployment of any container image to the cluster unless it carries a cryptographically verifiable attestation from a designated, trusted attestor (here, the build pipeline), closing the gap between “testing happened” and “the tested artifact is what’s actually running.”

**Key Exam Clues**

  * “circumvent automated testing and push code changes to production without approval” is a hard constraint — it specifically calls out bypassing the pipeline’s own gate, not just unauthorized human access.

  * “enforce approvals” at deploy time, into “a Kubernetes cluster in the production environment,” is a technical signal pointing at an admission-time control over the cluster itself, not a source-control or identity-access control upstream of it.

  * “configured as an attestor” (in the correct option) is the decisive mechanism: it ties the approval cryptographically to the pipeline’s own attestation, which is what actually prevents circumvention rather than merely restricting who can act.

**Why This Is Correct**

Binary Authorization enforces deploy-time policy on a Kubernetes cluster by requiring every container image to carry one or more valid attestations, signed by designated attestors, before the cluster’s admission controller will allow it to run. Configuring the automated build pipeline itself as the attestor means an image can only receive the required signature if it has actually passed through that pipeline’s testing and build steps — so even someone with legitimate `kubectl` access can’t deploy an image that skipped the pipeline, because the cluster will reject any unattested image outright. This directly closes the exact gap the auditor raised: it’s not about restricting who can act, but about guaranteeing what gets admitted to run.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Different Use Case:** Protected branches with required pull request approval is a legitimate control, but it operates on source code merges in the version-control system, not on what gets deployed to the cluster. It does nothing to stop someone from building and pushing a container image directly to the cluster outside the normal pipeline, so it doesn’t close the specific circumvention risk described.

  * **Option B — Technically Possible but Not Best:** A generic admission controller that checks the _source_ of incoming requests (e.g., which service account or IP issued the deployment call) addresses _who_ is making the request, but it doesn’t verify that the image itself was actually built and tested by the approved pipeline. A user with a legitimately “approved” source could still push an untested image; this doesn’t enforce the testing/approval gate itself.

  * **Option C — Different Use Case:** Kubernetes RBAC controls which authenticated users or service accounts can perform which actions against the cluster API (an identity/authorization concern). It’s valuable for least-privilege access but says nothing about whether a given container image passed through automated testing — an authorized user under RBAC could still deploy an image that skipped the pipeline entirely.

**Exam Trap**

The trap is treating this as an access-control problem (who is allowed to deploy) rather than a supply-chain-integrity problem (what is allowed to run). RBAC and source-restricted admission controllers both sound like reasonable “enforce approvals” answers because they gate _actors_ , but the auditor’s concern is about _artifacts_ bypassing testing — which only an attestation-based control like Binary Authorization actually verifies.

**Foundation Concept**

Software supply chain security distinguishes between controlling who can take an action (identity and access management, e.g., RBAC) and verifying that an artifact meets a required provenance or quality bar before it’s trusted to run (attestation-based admission control, e.g., Binary Authorization). When a scenario specifically worries about bypassing automated testing, the answer sits in the second category, because the first category can’t detect or prevent a legitimately authorized actor from deploying an unvetted artifact.

**Real-World Connection**

In practice, teams configure their CI/CD pipeline (e.g., Cloud Build) to run its test and security-scan stages and, only on success, sign the resulting image with an attestor key tied to Binary Authorization policy; the GKE cluster’s policy is then set to reject any image lacking that attestation. The operational payoff is that even a well-intentioned “hotfix” pushed manually during an incident gets blocked unless it goes through the pipeline — trading a small amount of deployment friction for a hard guarantee that production only ever runs tested, approved artifacts.

**Memory Hook**

“Stop untested images from running” → Binary Authorization with the pipeline as attestor; “control who can act” → RBAC; they solve different problems.

**30-Second Exam Takeaway**

When a question frames the risk as bypassing automated testing/approval before something reaches production in Kubernetes, look for an attestation-based admission control (Binary Authorization) rather than an identity/access control (RBAC) or a source-control gate (branch protection) — those control different stages and different risks.

**Official References**

[**Google Cloud — Binary Authorization overview:**](https://cloud.google.com/binary-authorization/docs/overview) Supports: the correct-answer mechanism of blocking unattested images from deployment and configuring a build pipeline as a trusted attestor

---

## Question 8

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your team is designing a new application that will be deployed both inside and outside Google Cloud. You need to collect detailed metrics, such as system resource utilization, and you want to rely on a centralized Google Cloud service while keeping the setup work required to a minimum. What should you do?

- [x] A. Import the Cloud Profiler client library into the application, and configure it to report CPU and memory profiling data to Cloud Profiler for analysis.
- [ ] B. Import the Cloud Debugger client library into the application, and configure it to emit debug log messages that include timing information.
- [ ] C. Instrument the application code with a custom timing library, and publish the resulting metrics through a health-check endpoint that Cloud Monitoring scrapes.
- [ ] D. Deploy a third-party Application Performance Monitoring (APM) tool at both locations, and configure it to export the collected data to a central data store for analysis.

### Explanation

**Correct Answer**

**A. Import the Cloud Profiler client library into the application, and configure it to report CPU and memory profiling data to Cloud Profiler for analysis.**

**Exam Reasoning Explanation**

The must-have constraints are threefold: the solution must work for a hybrid deployment (both inside and outside Google Cloud), it must funnel data into a _centralized Google Cloud service_ , and it must require _minimal setup work_. Testing each option against all three in sequence narrows the field fast. A custom timing library with a scraped health-check endpoint (C) and a third-party APM tool with a hand-built export pipeline (D) both satisfy the hybrid and centralization requirements only at the cost of significant custom engineering — which directly violates the “minimize work” constraint. A Debugger-based approach (B) fails on a more fundamental level: it targets the wrong kind of telemetry (application state inspection, not resource metrics) and, as of this writing, the underlying service no longer exists to send data to. Cloud Profiler is the only option that is a lightweight library import, works identically whether the host is a GCP VM or an external server, and reports directly into a centralized Google Cloud service — satisfying all three constraints simultaneously.

**Key Exam Clues**

  * “both inside and outside Google Cloud Platform” is a hard constraint — it rules out any approach that depends on being hosted on GCP infrastructure to work.

  * “centralized GCP services while minimizing the amount of work” is a dual hard constraint — it eliminates any option requiring custom instrumentation, a hand-rolled scrape/export pipeline, or installing and maintaining separate tooling.

  * “detailed metrics such as system resource utilization” is a technical signal pointing toward resource-consumption data (CPU, memory) rather than application logic/state data, which is what distinguishes a profiling tool from a debugging tool.

**Why This Is Correct**

Cloud Profiler is a statistical, low-overhead continuous profiler: you add its client library to the application, and it samples CPU time, heap (memory) allocation, and other resource-consumption data directly from the running process, then reports that data to a centralized Cloud Profiler backend in Google Cloud. Because the profiling agent lives inside the application process itself rather than depending on GCP-specific host infrastructure, it works the same way whether the application is deployed on Compute Engine, GKE, or a server outside Google Cloud entirely — satisfying the hybrid-deployment requirement. Setup is limited to importing the library and enabling it (typically a few lines of initialization code), which is about as little work as instrumentation gets, and the reporting destination is natively a centralized Google Cloud service, with no custom export pipeline to build or maintain.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Outdated:** Cloud Debugger (formerly Stackdriver Debugger) was deprecated in May 2022 and the service was fully shut down in May 2023; it no longer exists to import or configure. Even setting aside its retirement, Debugger was never designed for metrics collection — it’s a snapshot-based tool for inspecting application state at a code location without stopping execution, not a system for aggregating resource-utilization data. “Emit debug messages with timing information” describes manual log instrumentation, which is also a distinct, heavier-effort pattern than what the question is asking for.

  * **Option C — Technically Possible but Not Best:** This is a legitimate pattern in principle (expose a metrics endpoint for scraping), but it requires writing and maintaining custom timing instrumentation, building and exposing an endpoint, and configuring a scrape/collection pipeline into Cloud Monitoring — none of which is “minimal work” compared to simply importing a managed profiling library.

  * **Option D — Different Use Case:** Deploying and maintaining a separate third-party APM tool at every location, plus building a custom export process into centralized storage, is the most labor-intensive of the four options. It’s a reasonable architecture if you specifically need APM-style distributed tracing or vendor-specific features unavailable in GCP, but it directly conflicts with the stated goal of minimizing setup work while using centralized GCP services natively.

**Exam Trap**

The trap is pattern-matching “needs timing/debug-style instrumentation” to the Debugger product purely because of its name, without checking (a) whether Debugger actually collects system resource metrics (it doesn’t — it inspects application state) and (b) whether the service is still current (it isn’t — it was retired in 2023). Exam questions referencing legacy Stackdriver sub-products should always be checked against current product status before being treated as a viable answer.

**Foundation Concept**

Google Cloud’s observability tooling splits cleanly by data type: Cloud Monitoring handles metrics, Cloud Logging handles logs, Cloud Trace handles distributed request latency, and Cloud Profiler handles continuous code-level CPU/memory profiling — all under the Google Cloud Observability umbrella (formerly Stackdriver). When a question asks for “resource utilization” metrics with minimal setup across hybrid environments, the profiling or monitoring-agent tools (which run as lightweight in-process or host-level agents reporting to a managed backend) are almost always a better fit than custom scrape pipelines or third-party tools requiring manual central aggregation.

**Real-World Connection**

Teams running hybrid workloads commonly pair Cloud Profiler (for in-process CPU/memory profiling) with the Ops Agent (for host-level OS metrics like disk and network) on both GCP and non-GCP hosts, giving them a single centralized view in Google Cloud Observability without building or operating any custom collection infrastructure — freeing engineering time for the application itself rather than observability plumbing.

**Memory Hook**

Need resource-utilization metrics, minimal setup, hybrid deployment, centralized in GCP → Cloud Profiler (or the Ops/Monitoring agent), not a deprecated Debugger, custom scrape pipeline, or third-party APM tool.

**30-Second Exam Takeaway**

When a question asks for low-effort, centralized collection of resource-utilization metrics across GCP and non-GCP hosts, favor the managed, library-based Google Cloud Observability tool (Profiler or the Monitoring/Ops agent) over any option requiring custom instrumentation, a hand-built export pipeline, or a separate third-party tool — and always sanity-check any legacy-sounding Stackdriver sub-product name against current service status.

**Official References**

[Google Cloud — Cloud Profiler overview: ](https://cloud.google.com/profiler/docs/about-profiler)Supports: the correct-answer mechanism (lightweight client library reporting CPU/memory profiling data to a centralized Google Cloud service, usable from any deployment location)

[**Google Cloud — Cloud Debugger deprecation notice:**](https://docs.cloud.google.com/stackdriver/docs/deprecations/debugger-deprecation) Supports: the elimination of Option B as both an outdated and now-nonexistent service

---

## Question 9

*Domain 3: Applying Site Reliability Engineering Practices*

Your team has recently deployed an NGINX-based application to Google Kubernetes Engine (GKE) and exposed it to the public through an HTTP(S) Google Cloud Load Balancer (GCLB) Ingress. You want to scale the application’s frontend deployment using an appropriate Service Level Indicator (SLI). What should you do?

- [ ] A. Configure the horizontal pod autoscaler (HPA) to scale based on the average response time reported by the Liveness and Readiness probes.
- [ ] B. Configure the vertical pod autoscaler (VPA) in GKE, and enable the cluster autoscaler so the cluster grows as pod resource requests expand.
- [x] C. Use GKE’s native custom metrics support for the horizontal pod autoscaler, and configure it to scale based on the request count metric that the GCLB publishes to Cloud Monitoring.
- [ ] D. Expose the NGINX stats endpoint, and configure the horizontal pod autoscaler to scale based on the request metrics it reports.

### Explanation

**Correct Answer**

**C. Use GKE’s native custom metrics support for the horizontal pod autoscaler, and configure it to scale based on the request count metric that the GCLB publishes to Cloud Monitoring.**

**Exam Reasoning Explanation**

The decisive constraint is “appropriate SLI” for a user-facing frontend sitting behind a load balancer. SRE practice treats request-driven services as best measured by signals tied directly to actual user traffic — request volume, latency, error rate — rather than proxy signals internal to the pod (CPU/memory via VPA) or health-check mechanics never designed to represent load (Liveness/Readiness probe timing). The GCLB’s request-count metric is the authoritative, end-to-end signal of real traffic hitting the frontend, published automatically to Cloud Monitoring with no extra instrumentation. GKE’s native custom metrics support lets the HPA consume that metric directly, without standing up and maintaining a separate adapter — making it the option that is simultaneously the most accurate SLI and the least operationally burdensome to implement.

**Key Exam Clues**

  * “appropriate Service Level Indicator (SLI)” is a hard constraint — it requires the chosen signal to genuinely represent user-facing load/experience, immediately disqualifying any metric that only indirectly correlates with it.

  * “HTTP Google Cloud Load Balancer (GCLB) ingress” is a technical signal — it establishes that a load-balancer-level request metric already exists and is the natural source of truth for traffic volume to the frontend.

  * “scale the deployment of the application’s frontend” is a scope signal pointing toward horizontal scaling (more replicas serving more concurrent requests) rather than vertical scaling (bigger pods), since request-driven frontends typically scale by replica count, not per-pod resources.

**Why This Is Correct**

A horizontal pod autoscaler driven by the GCLB’s request-count metric scales replica count in direct proportion to real incoming traffic — exactly the SLI that matters for a public-facing frontend’s user experience. GKE’s native custom metrics support lets the HPA read this metric straight from Cloud Monitoring, eliminating the previously required middleman (the custom-metrics-stackdriver-adapter) along with its service accounts, Workload Identity bindings, and ongoing maintenance burden; Google has stated this also reduces metric-read latency so the HPA reacts to real traffic bursts faster. The result is a scaling signal that is both technically accurate (tied to actual request volume) and operationally simple to set up and keep running.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Liveness and Readiness probe response times measure whether a pod is alive and ready to serve traffic, not how much traffic it’s currently handling. A pod can report fast, healthy probe responses while still being overwhelmed by concurrent user requests, so this signal doesn’t represent the SLI the scenario actually cares about.

  * **Option B — Different Use Case:** VPA with cluster autoscaler addresses a different problem — right-sizing each pod’s CPU/memory requests and growing cluster capacity to accommodate that — not scaling the number of frontend replicas in response to request volume. It would be the better choice if the issue were individual pods being under-provisioned for their per-request resource needs, not a need to handle more concurrent requests.

  * **Option D — Technically Possible but Not Best:** Exposing NGINX’s own stats endpoint and scaling on self-reported request metrics is workable, but it duplicates a signal the GCLB already provides upstream, adds instrumentation and metric-exporting work to maintain, and reflects only what reaches NGINX rather than the full picture the load balancer sees (including, for example, requests the load balancer handles before reaching any pod). It’s a reasonable fallback only when no load-balancer-level metric is available — which isn’t the case here.

**Exam Trap**

The trap is treating “Liveness/Readiness probe timing” as a legitimate load signal because it sounds “metric-like” and is already built into the deployment — but probe latency measures pod health, not request volume, and conflating the two is a common misunderstanding of what an SLI for a request-driven service should actually represent. A second trap is assuming the Stackdriver/Prometheus adapter is still a required step for custom-metric autoscaling in GKE; that operational overhead has since been removed by native custom metrics support, which is the current correct mechanism to cite.

**Foundation Concept**

For request-driven services, the right SLI is almost always something derived from the request path itself — request rate, latency, or error rate — captured as close to the real user-facing boundary as possible (here, the load balancer). Scaling decisions should be driven by that SLI directly rather than by proxy signals (resource utilization, health-check timing) that can diverge from actual user-facing load.

**Real-World Connection**

Teams running public HTTP frontends on GKE commonly scale on load-balancer request-rate metrics specifically because it lets capacity track real traffic patterns (diurnal cycles, marketing-driven spikes) more faithfully than CPU-based scaling alone, which can lag behind or misrepresent load for I/O-bound or request-queuing workloads; native custom metrics support further reduces the operational risk of that setup by removing a previously-required adapter component from the critical scaling path.

**Memory Hook**

For a request-driven frontend, scale on a real request-volume signal from the load balancer — not on probe timing, not on pod resource usage, and (where a native path exists) not through a self-managed metrics adapter either.

**30-Second Exam Takeaway**

When asked to pick an “appropriate SLI” to drive autoscaling for a user-facing, request-driven service, favor a traffic-based metric sourced as close to the user-facing boundary as possible (load-balancer request count) over resource-utilization or health-check-derived signals — and prefer GKE’s native metrics path over a manually maintained adapter wherever the native option covers the required metric source.

**Official References**

[**Google Cloud — GKE native support for custom metrics (Horizontal Pod Autoscaler):**](https://cloud.google.com/blog/products/containers-kubernetes/gke-now-supports-custom-metrics-natively) Supports: the correct-answer mechanism of scaling HPA on Cloud Monitoring/load-balancer metrics without deploying a separate custom-metrics adapter

[**Google Cloud — Configuring horizontal Pod autoscaling in GKE:**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling) Supports: autoscaling based on load balancer traffic and external/custom metrics as the appropriate signal for request-driven frontend workloads

---

## Question 10

*Domain 2: Building and Implementing CI/CD Pipelines*

Your application services run on Google Kubernetes Engine (GKE). You want to guarantee that only images from your centrally managed Artifact Registry repository in the `altostrat-images` project can be deployed to the cluster, while keeping the development effort required to achieve this to a minimum. What should you do?

- [ ] A. Create a custom builder for Cloud Build that only pushes images to the `altostrat-images` Artifact Registry repository.
- [x] B. Configure a Binary Authorization policy that includes an allowlist name pattern matching the `altostrat-images` Artifact Registry repository.
- [ ] C. Add logic to the deployment pipeline that checks that every manifest references only images from the `altostrat-images` Artifact Registry repository.
- [ ] D. Tag every image in the `altostrat-images` Artifact Registry repository, and verify that tag is present whenever an image is deployed.

### Explanation

**Correct Answer**

**B. Configure a Binary Authorization policy that includes an allowlist name pattern matching the**`**altostrat-images**`**Artifact Registry repository.**

**Exam Reasoning Explanation**

The hard requirement is enforcement at the point of deployment — “only images from X can be deployed” is a guarantee about what the cluster will actually admit, not about what a build pipeline happens to produce or what a separate script happens to check. That distinction eliminates any approach that only controls the image-push side (where images get created) or that lives outside the cluster’s own admission path (a pipeline-side check that can be bypassed by anyone with direct `kubectl` access). The second constraint — minimizing development effort — favors a declarative policy configuration over building and maintaining custom tooling, scripts, or tagging conventions. Binary Authorization is the GKE-native admission control mechanism built exactly for this: a short, declarative policy restricts which image name patterns the cluster will admit, with no custom code to write or maintain.

**Key Exam Clues**

  * “only images from your centrally-managed... registry... can be deployed” is a hard constraint — it specifies admission-time enforcement on the cluster, not a build-time convention or a pipeline-side check that a bypass could evade.

  * “to the cluster” is a technical signal — it points toward a Kubernetes/GKE admission control mechanism rather than a CI/CD pipeline step that happens before the cluster is ever involved.

  * “while minimizing development time” is a preference that rules out options requiring custom code, scripts, or manual conventions in favor of a declarative, policy-based control.

**Why This Is Correct**

Binary Authorization enforces its policy at image admission into the GKE cluster: a policy with a default rule set to deny deployment, combined with an allowlist name pattern scoped to the `altostrat-images` repository, means the cluster will only admit images whose registry path matches that pattern, and will block anything else regardless of how someone attempted to deploy it (kubectl, a different pipeline, a compromised CI job). This is implemented as a short YAML policy rather than custom code, satisfying the “minimize development time” goal, and it closes the loop that build-side or pipeline-side controls leave open: it doesn’t matter where an image was built or pushed from — only images matching the approved registry pattern can ever run on the cluster.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Different Use Case:** A custom Cloud Build builder restricted to pushing only to the `altostrat-images` repository controls one path by which images get created, but it does nothing to stop a different image — built elsewhere, pulled from a public registry, or pushed by another pipeline — from being deployed directly to the cluster. It secures the build side, not the deploy side, which is what the requirement actually asks for.

  * **Option C — Technically Possible but Not Best:** Adding manual validation logic to the deployment pipeline that inspects manifests is a workable idea in principle, but it requires writing and maintaining custom checking code, and it only guards deployments that go through that specific pipeline — anyone with direct cluster access can bypass it entirely. It also conflicts with the “minimize development time” goal compared to a declarative policy.

  * **Option D — Technically Possible but Not Best:** Tagging approved images and checking for that tag at deploy time is a weak, convention-based control: tags are mutable and can be applied to any image by anyone with push access, so this doesn’t actually guarantee the image originates from the approved registry. It also requires building and maintaining custom tagging and verification logic rather than relying on built-in enforcement.

**Exam Trap**

The trap is treating Option A (controlling the build pipeline’s push destination) as equivalent to controlling what the cluster will run — but restricting where a trusted pipeline publishes images says nothing about what else might be deployed from outside that pipeline. The scenario’s “only images from X can be deployed” is a cluster-admission guarantee, which only an admission-control mechanism like Binary Authorization can actually provide.

**Foundation Concept**

Restricting _where images can be built or pushed to_ and restricting _what a cluster will admit to run_ are two different controls that address different threat models — the first narrows your trusted build surface, the second guarantees enforcement regardless of how an image arrived. When a requirement is phrased as “only X can be deployed,” it’s asking for the second: an admission-control policy evaluated at deploy time, not a convention enforced earlier in the pipeline.

**Real-World Connection**

Teams commonly layer both controls in production — a locked-down CI/CD pipeline that only pushes trusted images to one or two approved repositories, and a Binary Authorization policy on the cluster restricting admission to exactly those repository paths — so that even a misconfigured or compromised alternate deployment path can’t introduce an unapproved image, because the cluster itself refuses to run anything outside the allowlisted registry pattern.

**Memory Hook**

“Only X can be deployed to the cluster” means enforce it at the cluster’s admission boundary (Binary Authorization), not at the build pipeline or with a convention like tagging.

**30-Second Exam Takeaway**

When a GKE question asks you to guarantee that only images from a specific registry can be deployed — especially with minimal custom engineering — reach for a Binary Authorization policy with a name-pattern restriction rather than a build-pipeline control or a custom pipeline/tagging check, since only admission control actually governs what the cluster will run.

**Official References**

[**Google Cloud — Binary Authorization Policy YAML reference:**](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference) Supports: the correct-answer mechanism of restricting admitted images to a registry path pattern via a declarative policy, and the current “allowlist” terminology for this feature

[**Google Cloud — Container Registry deprecation and transition to Artifact Registry:**](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation) Supports: the terminology update reflecting that Container Registry (GCR) is fully shut down and Artifact Registry is the current, official image registry product

---

## Question 11

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You operate a real-time multiplayer gaming workload on Compute Engine, with separate production and testing environments, each in its own VPC network. Within each VPC, the frontend and backend servers sit on distinct subnets. You suspect a malicious process is periodically communicating from your production frontend instances, and you need to capture network traffic so you can investigate. What should you do?

- [ ] A. Enable VPC Flow Logs on the frontend and backend subnets of the production VPC network only, with a sampling rate of 0.5.
- [x] B. Enable VPC Flow Logs on the frontend and backend subnets of the production VPC network only, with a sampling rate of 1.0.
- [ ] C. Enable VPC Flow Logs on the frontend and backend subnets of both the testing and production VPC networks, with a sampling rate of 0.5. Roll the change out to testing before production.
- [ ] D. Enable VPC Flow Logs on the frontend and backend subnets of both the testing and production VPC networks, with a sampling rate of 1.0. Roll the change out to testing before production.

### Explanation

**Correct Answer**

**B. Enable VPC Flow Logs on the frontend and backend subnets of the production VPC network only, with a sampling rate of 1.0.**

**Exam Reasoning Explanation**

Two decisions drive this question: _where_ to enable Flow Logs and _at what sampling rate_. Scope is a must-have constraint — the suspected malicious activity is specifically in production, so that’s the environment that needs instrumenting; testing is unaffected and enabling logging there adds cost and noise without investigative value. Both the frontend and backend subnets need coverage because a compromised frontend instance could be communicating laterally to the backend tier, or the backend could be the actual source/destination of interest — restricting to frontend alone would blind you to that path. Rate is the second decision: this is a forensic investigation of an intermittent, low-frequency malicious process, so you need every relevant flow captured, not a statistical sample that could simply miss the event. That requires a sampling rate of 1.0 (100%), not a reduced rate chosen for cost/volume optimization.

**Key Exam Clues**

  * “suspect there is a malicious process communicating intermittently” — a security-investigation/forensic scenario, not routine capacity monitoring; intermittent/low-frequency activity is a hard constraint favoring full sampling, since a partial sample could simply miss the event.

  * “production frontend servers” — identifies where the suspicious activity is observed, but doesn’t by itself prove the backend is irrelevant; the question’s broader setup (two tiers in one VPC) is a technical signal that traffic could cross tiers.

  * “ensure that network traffic is captured for analysis” — “ensure” is a completeness directive, ruling out any sampled (less-than-100%) approach as insufficiently reliable for analysis.

**Why This Is Correct**

VPC Flow Logs record metadata about IP traffic sent from and received by VM instances, and the sampling rate parameter controls what fraction of eligible flows are actually logged — a setting of 1.0 logs 100% of flows, which is what a security investigation needs to avoid missing the very traffic you’re hunting for. Scoping the logs to the production VPC’s frontend and backend subnets targets exactly the environment and both tiers where the suspicious communication could be occurring, without burdening the unrelated testing environment with unnecessary logging overhead and cost.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Correct scope (production frontend and backend only) but a 0.5 sampling rate captures only half of flows on average. For an intermittent, suspected-malicious process, that’s a coin flip on whether the relevant traffic is even recorded — it directly undermines “ensure traffic is captured.”

  * **Option C — Different Use Case:** Enabling Flow Logs across both testing and production is scope creep; the incident is confined to production, and testing isn’t implicated in the scenario. The 0.5 sampling rate repeats the same flaw as Option A — incomplete capture for a forensic use case — and “roll out to testing before production” is a standard safe-change-management practice that is irrelevant and even counterproductive here, since it delays instrumenting the one environment that actually needs it.

  * **Option D — Technically Possible but Not Best:** This does get the sampling rate right (1.0), but it unnecessarily expands scope to the testing VPC, which adds cost and log volume with no investigative benefit, and again inserts a testing-first rollout that delays getting visibility into the actual incident in production. It would only be the better choice if the scenario indicated the testing environment might also be compromised or that the source of the malicious traffic was unclear across environments — neither of which is stated here.

**Exam Trap**

The trap is treating “capture traffic for analysis” as if it just means “turn on Flow Logs” and then picking the default or cost-conscious sampling rate (0.5) out of habit, since 0.5 is a common middle-ground choice in cost-optimization scenarios. For a security/forensic scenario with intermittent activity, the correct instinct flips: you prioritize capture completeness over cost, which is the deciding detail between A/B and the rate-pairing in C/D.

**Foundation Concept**

VPC Flow Logs sampling rate is a cost-vs-completeness lever: lower rates (e.g., 0.5 or lower) reduce log volume and expense for routine monitoring or capacity analysis, where a representative sample is good enough, while a rate of 1.0 is reserved for cases — security investigations, compliance, incident forensics — where missing even one flow could mean missing the thing you’re looking for. The mental model is: sample for trends, capture fully for investigations.

**Real-World Connection**

In practice, a team investigating a suspected compromise would enable full-rate Flow Logs on the implicated VPC’s subnets, route the logs to Cloud Logging (or export to BigQuery/Cloud Storage for deeper analysis), and correlate flow metadata with other signals (firewall logs, IDS alerts) to identify the destination IPs and ports the malicious process is talking to — then use that to scope containment (firewall rule changes, instance isolation) without having wasted logging spend instrumenting the unrelated testing environment.

**Memory Hook**

Security/forensic investigation → sampling rate 1.0, scoped only to the implicated environment and every subnet traffic could cross.

**30-Second Exam Takeaway**

When a DevOps Engineer question frames a scenario as “suspected malicious activity, need to capture traffic for analysis,” default to full (1.0) VPC Flow Logs sampling and scope it to exactly the environment/subnets involved — reduced sampling rates and broadened scope are both classic distractors built for cost-optimization scenarios, not security investigations.

**Official References**

[**Google Cloud — VPC Flow Logs overview:**](https://cloud.google.com/vpc/docs/flow-logs) Supports: the correct-answer mechanism (sampling rate controls the fraction of flows logged; 1.0 logs all flows) and the rationale for full capture during investigation

[**Google Cloud — Using VPC Flow Logs for network monitoring, forensics, and security:**](https://cloud.google.com/architecture/validating-filtering-network-traffic-flow-logs) Supports: the use case of enabling Flow Logs specifically for security investigation and traffic analysis, including scoping guidance

---

## Question 12

*Domain 3: Applying Site Reliability Engineering Practices*

Your organization follows Site Reliability Engineering principles. You’re writing the postmortem for an incident, triggered by a software change, that had a severe impact on users. You want to prevent incidents of this severity from recurring. What should you do?

- [ ] A. Identify the engineers responsible for the incident, and escalate the matter to their senior management.
- [x] B. Ensure that test cases capable of catching this class of error run successfully as a required step before future software releases.
- [ ] C. Follow up individually with the employees who reviewed the change, and prescribe practices they should personally follow going forward.
- [ ] D. Create a policy requiring on-call teams to immediately call engineers and management to discuss a plan of action whenever an incident occurs.

### Explanation

**Correct Answer**

**B. Ensure that test cases capable of catching this class of error run successfully as a required step before future software releases.**

**Exam Reasoning Explanation**

The hard requirement is a _systemic_ fix that prevents the same class of incident from recurring, consistent with SRE’s blameless-postmortem culture, which treats incidents as failures of process and tooling rather than failures of individuals. That constraint immediately filters out any remedy aimed at specific people (assigning blame, individually retraining reviewers) in favor of a remedy embedded in the engineering process itself. Among the remaining candidates, the real distinguishing question is whether the fix addresses _prevention_ (stopping the defect from reaching production) or merely improves _response_ (how quickly the team reacts once an incident is already happening). Since the incident was triggered by a software change, a prevention mechanism gated into the release process — automated tests that specifically catch this error type — directly closes the gap that let the defect ship, which is the strongest and most durable fix available.

**Key Exam Clues**

  * “triggered by a software change” is a technical signal — it points the remediation toward the software delivery pipeline (testing, release gating) rather than toward incident communication or escalation processes.

  * “prevent severe incidents from happening in the future” is a hard constraint — it demands a preventive fix, not merely a faster or better-coordinated response after an incident starts.

  * “Site Reliability Engineering principles” and the postmortem context are a technical/cultural signal — SRE postmortems are explicitly blameless, which disqualifies any option centered on identifying or penalizing individuals.

**Why This Is Correct**

Adding automated test cases that specifically catch this error type, and requiring them to pass before any future release, closes the exact gap that allowed the triggering defect to reach production in the first place — it converts a one-time painful lesson into a permanent, automated guardrail that every future change must clear. This is systemic and durable: it doesn’t depend on any individual remembering a lesson or following a manual practice, and it directly targets prevention (stopping the defect class from shipping) rather than response (how the team reacts once something has already gone wrong), which is precisely what “prevent severe incidents from happening” calls for.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Identifying and escalating individual engineers to senior management is the definition of a blame-oriented response, which directly conflicts with SRE’s blameless-postmortem principle. It also does nothing systemic — it neither fixes the underlying defect class nor prevents a different engineer from introducing a similar one later.

  * **Option C — Violates Requirement:** Prescribing personal practices to specific reviewers individually is still people-focused rather than process-focused, and it doesn’t scale or persist: it depends on those particular individuals remembering and consistently applying the guidance, with no systemic enforcement if they don’t, and it implicitly singles out specific people in a way blameless postmortems avoid.

  * **Option D — Different Use Case:** A policy for immediate incident-response escalation improves how quickly the organization reacts and coordinates once an incident is already underway — a legitimate and valuable practice, but one addressing incident _response_ , not _prevention_. It would be the better choice if the goal were reducing time-to-mitigation or improving coordination during incidents, not stopping this class of incident from occurring in the first place.

**Exam Trap**

The trap is that Options A and C can look like reasonable “accountability” measures on first read, especially since the incident was caused by a change someone wrote and someone else reviewed — but SRE postmortems are explicitly designed to resist that instinct, because blaming or individually retraining people doesn’t fix the process gap that let the defect through, and it discourages the open, honest incident reporting that effective postmortems depend on.

**Foundation Concept**

A blameless postmortem’s value lies in converting an incident into a systemic, durable improvement — typically a change to tooling, process, or automated gating — rather than a judgment about who was at fault. The decisive test for any proposed postmortem action item is whether it would have prevented this specific incident (or its class) regardless of which individuals were involved, which is exactly what an automated, release-gating test case achieves and people-focused remedies do not.

**Real-World Connection**

Teams following this practice typically add a regression test derived directly from the incident’s root cause to their CI pipeline, so every subsequent release is automatically checked against the exact failure mode that caused the outage — turning a costly, user-impacting incident into a permanent improvement to release safety, with far more leverage than any one-off conversation or escalation could provide.

**Memory Hook**

A good postmortem action item fixes the process (an automated test gating future releases), not the person — blameless means systemic, not individual.

**30-Second Exam Takeaway**

When an SRE postmortem question asks how to prevent a recurrence, favor action items that are systemic, automated, and embedded in the delivery pipeline (like release-gating tests) over anything aimed at identifying, escalating, or individually retraining specific people — and distinguish prevention-focused fixes from response/coordination-focused ones, since only prevention stops the incident class from recurring.

**Official References**

[**Google SRE Book — Postmortem Culture: Learning from Failure:**](https://sre.google/sre-book/postmortem-culture/) Supports: the correct-answer mechanism of blameless, systemic action items (such as adding regression tests) as the proper output of a postmortem, and the exclusion of individual-blame remedies

[**Google Cloud — Professional Cloud DevOps Engineer exam guide, Section 3 (SRE practices):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment — conducting blameless postmortems and applying their lessons is explicitly part of applying site reliability engineering practices

---

## Question 13

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You manage an application that writes its logs to Cloud Logging. You need to grant some team members the ability to export logs. What should you do?

- [x] A. Grant the team members the IAM role Logs Configuration Writer (`roles/logging.configWriter`).
- [ ] B. Configure Access Context Manager to allow only these members to export logs.
- [ ] C. Create and grant a custom IAM role that includes the `logging.sinks.list` and `logging.sinks.get` permissions.
- [ ] D. Create an Organization Policy in IAM that allows only these members to create log exports.

### Explanation

**Correct Answer**

**A. Grant the team members the IAM role Logs Configuration Writer (**`**roles/logging.configWriter**`**).**

**Exam Reasoning Explanation**

The hard requirement is granting specific individuals the ability to perform one well-defined action: create and manage log exports (sinks) in Cloud Logging. Google Cloud’s IAM model favors predefined roles scoped to exactly this kind of capability over building custom mechanisms, so the first question is whether a predefined role already covers it — and it does. The Logs Configuration Writer role is purpose-built to grant read/write access to sink (export) and log-based metric configurations, which is precisely “the ability to export logs.” That makes every other option either the wrong IAM mechanism (Access Context Manager, Organization Policy) or an under-permissioned attempt to replicate what the predefined role already does more simply.

**Key Exam Clues**

  * “give some team members the ability to export logs” is a hard constraint — it specifies a particular IAM capability (creating/managing log sinks) for a defined set of individuals, pointing toward standard IAM role assignment rather than organization-wide policy or network/context-based controls.

  * “some team members” (not all, not a blanket rule) is a scope signal — it indicates principal-level role binding is the right granularity, not a project- or org-wide policy mechanism.

  * The permissions named in the custom-role option, `logging.sinks.list` and `logging.sinks.get`, are a decisive technical signal: these are read-only permissions (viewing existing sinks), not the `logging.sinks.create` permission actually required to export logs.

**Why This Is Correct**

The Logs Configuration Writer predefined role grants the permissions needed to create, update, delete, get, and list log sinks — sinks being the mechanism Cloud Logging uses to export logs to destinations like Cloud Storage, BigQuery, or Pub/Sub. Granting this role to the specific team members directly satisfies “the ability to export logs” using Google’s own purpose-built, maintained role, with no custom role definition or additional infrastructure to build and keep in sync as Cloud Logging’s permission set evolves.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Different Use Case:** Access Context Manager defines context-aware access perimeters (e.g., restricting access based on IP range, device policy, or identity context) for resources within VPC Service Controls. It isn’t an IAM role-granting mechanism and isn’t designed to control which principals can perform a specific Cloud Logging action like creating a sink — it solves a network/context-boundary problem, not a permissions-granting one.

  * **Option C — Violates Requirement:** `logging.sinks.list` and `logging.sinks.get` only allow viewing existing sinks’ names and configurations — they do not include `logging.sinks.create`, so a principal with only these permissions cannot actually create a log export. Building a custom role here also means manually maintaining a permission set that the predefined role already covers and keeps current.

  * **Option D — Different Use Case:** Organization Policy constraints govern resource configuration guardrails across an organization (e.g., restricting which services or regions can be used) — they are not an IAM mechanism for granting specific principals permission to perform an action like creating a log sink. This misapplies a governance/constraint tool to what is fundamentally an access-grant problem.

**Exam Trap**

The trap is Option C’s apparent precision — naming specific `logging.sinks.*` permissions makes it look like the more deliberate, least-privilege choice. But listing and getting sinks only lets you view configuration that already exists; the actual verb needed is `create`, which neither listed permission provides. Spotting that the named permissions are read-only, not write/create, is the key to eliminating this distractor.

**Foundation Concept**

When a requirement maps cleanly to “grant specific people a specific capability,” the IAM-first instinct should be to check whether a predefined role already covers exactly that capability before reaching for a custom role, and well before considering governance tools like Organization Policy or network/context tools like Access Context Manager — those solve different classes of problems (configuration guardrails and context-aware network access, respectively) than principal-level permission grants.

**Real-World Connection**

Teams commonly grant Logs Configuration Writer narrowly — to a platform or observability team responsible for setting up log routing to BigQuery for analysis or to Cloud Storage for long-term retention — while keeping broader Logging Admin or Owner-level access restricted, since the predefined role’s scope (sinks and log-based metrics) is exactly the surface area that export-configuration work touches, without granting unrelated capabilities like managing log buckets or viewing private logs.

**Memory Hook**

“Give someone the ability to export logs” maps directly to the Logs Configuration Writer role — not a custom role missing the `create` permission, and not a network- or org-level policy tool.

**30-Second Exam Takeaway**

When an IAM question asks how to grant a specific capability to specific people, check for a predefined role that matches the capability by name and permission set before considering a custom role, Organization Policy, or Access Context Manager — and when a custom-role option is offered, verify it actually includes the create/write permission the scenario requires, not just read permissions.

**Official References**

[**Google Cloud — Cloud Logging roles and permissions:**](https://cloud.google.com/iam/docs/roles-permissions/logging) Supports: the correct-answer mechanism — the Logs Configuration Writer role’s permissions for creating and managing log sinks (exports), and the elimination of Option C’s read-only permission set

---

## Question 14

*Domain 3: Applying Site Reliability Engineering Practices*

You support a high-traffic web application running on Google Cloud. You need to measure the application’s reliability from the user’s perspective, without making any engineering changes to the application itself. What should you do? (Choose two.)

- [ ] A. Review the application’s current metrics, and add new ones as needed.
- [ ] B. Modify the application code to capture additional information about user interactions.
- [ ] C. Analyze only the web proxy logs, and capture the response time of each request.
- [x] D. Create synthetic clients that simulate a user journey through the application.
- [x] E. Use current and historical request logs to trace customer interactions with the application.

### Explanation

**Correct Answer**

**D. Create synthetic clients that simulate a user journey through the application.**

**E. Use current and historical request logs to trace customer interactions with the application.**

**Exam Reasoning Explanation**

The hard constraint that filters every option is “without making any engineering changes to it” — any approach that requires touching the application’s code is immediately disqualified, regardless of how good the resulting data would be. Against that filter, synthetic clients and request-log analysis both operate entirely outside the application: synthetic clients are external callers that exercise the live application exactly as a real user would, and request logs are already generated by the existing infrastructure (load balancer, proxy, or web server) without any instrumentation added to the app. Both independently produce a user-perspective view of reliability — synthetic clients proactively, by simulating real journeys on a schedule, and request logs retrospectively, by revealing how actual users experienced the system — which is why they work together as a complete answer rather than overlapping redundantly.

**Key Exam Clues**

  * “without making any engineering changes to it” is a hard constraint — it eliminates any option that requires modifying, instrumenting, or redeploying the application’s own code.

  * “from a user perspective” is a technical signal — it requires the measurement to reflect the actual experience of someone using the application (end-to-end journeys, real request outcomes), not internal system metrics alone.

  * “Choose two” with “only” appearing in one distractor (Option C) is a cardinality/scope signal — it flags that option as artificially narrowed in a way that should be checked against the other candidates before being accepted.

**Why This Is Correct**

Synthetic clients simulate real user journeys — logging in, navigating, completing a transaction — against the live, unmodified application, producing proactive, repeatable measurements of whether the application behaves correctly and performantly from an end-user’s point of view, entirely from outside the app. Historical and current request logs, which the infrastructure already generates as requests flow through it, let you trace what actually happened to real customer requests over time — successes, failures, latencies — giving a retrospective, ground-truth view of user-experienced reliability without adding any logging or instrumentation to the application code. Together, these two approaches cover both proactive (synthetic) and observed (historical) measurement of user-facing reliability, satisfying the requirement comprehensively while respecting the no-engineering-changes constraint.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** “Add new [metrics] as needed” implies instrumenting the application to emit additional metrics it doesn’t currently produce, which is itself an engineering change to the app — directly conflicting with the stated constraint, however useful it might be if that constraint weren’t present.

  * **Option B — Violates Requirement:** This explicitly states modifying the application code, which is the most direct possible violation of “without making any engineering changes to it.”

  * **Option C — Technically Possible but Not Best:** Analyzing web proxy logs for response time doesn’t require any code changes, so it clears the hard constraint, but the word “only” artificially narrows the approach to a single data source and a single dimension (response time), omitting other reliability signals like error rates or full request outcomes that the available request logs already capture more completely — making it a weaker, incomplete choice next to Option E.

**Exam Trap**

The trap is Option A, which sounds like sound SRE practice (“review your metrics, add what’s missing”) but quietly smuggles in an engineering change via “add new ones as needed” — a reminder to check every clause in a distractor against the stated constraints, not just its opening phrase. A second trap is treating Option C as acceptable because it avoids code changes, while missing that its own wording (“only,” single metric) makes it a narrower, inferior version of the broader request-log analysis in Option E.

**Foundation Concept**

Measuring user-perceived reliability without modifying the system under test is the defining feature of black-box observability techniques: synthetic monitoring (proactively exercising the system from outside) and analysis of existing infrastructure-level logs (retrospectively observing real traffic) are the two canonical black-box approaches, as opposed to white-box techniques (custom application metrics, code-level instrumentation) that require the engineering changes this scenario rules out.

**Real-World Connection**

SRE teams commonly pair these two techniques in practice: synthetic checks catch availability or journey-breaking regressions proactively, often before real users are affected, while mining request logs for success/failure rates and latency distributions establishes the actual SLI used to track an SLO against real traffic — giving both an early-warning signal and a ground-truth reliability measurement, without ever touching the application’s own codebase.

**Memory Hook**

To measure user-perceived reliability with zero application code changes, look outside the app: simulate the user from the outside (synthetic clients) and read what already happened from the outside (request logs).

**30-Second Exam Takeaway**

When a scenario rules out engineering/code changes but asks for user-perspective reliability measurement, favor black-box techniques — synthetic monitoring and existing infrastructure/request logs — over any option that mentions adding, modifying, or instrumenting application code, however reasonable that option sounds in isolation.

**Official References**

[**Google Cloud — Monitoring overview and Uptime checks (synthetic monitoring):**](https://cloud.google.com/monitoring/uptime-checks) Supports: the correct-answer mechanism of using external synthetic clients to measure application reliability from a user perspective without application code changes

[**Google Cloud — HTTP(S) Load Balancing logging and monitoring:**](https://cloud.google.com/load-balancing/docs/https/https-logging-monitoring) Supports: the use of existing load balancer/proxy request logs to trace historical customer interactions and reliability without instrumenting the application

---

## Question 15

*Domain 2: Building and Implementing CI/CD Pipelines*

You have a CI/CD pipeline that uses Cloud Build to build Docker images and push them to Docker Hub. Your code is versioned in Git. After making a change to the Cloud Build YAML configuration, you notice that the pipeline is no longer building any new artifacts. Following Site Reliability Engineering practices, what should you do to resolve the issue?

- [ ] A. Disable the CI pipeline, and revert to building and pushing the artifacts manually.
- [ ] B. Change the CI pipeline to push the artifacts to Artifact Registry instead of Docker Hub.
- [ ] C. Upload the configuration YAML file to Cloud Storage, and use Error Reporting to identify and fix the issue.
- [x] D. Run a Git diff between the previous and current versions of the Cloud Build configuration file to find and fix the bug.

### Explanation

**Correct Answer**

**D. Run a Git diff between the previous and current versions of the Cloud Build configuration file to find and fix the bug.**

**Exam Reasoning Explanation**

The must-have constraint is diagnosing and fixing the actual root cause — the pipeline broke immediately after a configuration change, which is a direct, available clue pointing to exactly where the defect was introduced. SRE troubleshooting practice favors using the evidence closest to the failure before reaching for broader or unrelated remedies: since the code (including the Cloud Build YAML) is already versioned in Git, comparing the last known-working configuration against the current one is the fastest, most direct way to isolate precisely what changed and caused the failure. Every other option either abandons the automation entirely, changes something unrelated to the reported symptom, or applies a tool that doesn’t actually inspect configuration files — none of which engages with the root cause the way a direct diff does.

**Key Exam Clues**

  * “After making a change in the Cloud Build YAML configuration... no new artifacts are being built” is a hard constraint — it establishes a clear before/after causal link between a specific recent change and the failure, which is the strongest available diagnostic signal.

  * “You use Git for code versioning” is a technical signal — it tells you the tooling needed to directly compare the working and broken configuration states is already in place and requires no new setup.

  * “following Site Reliability Engineering practices” is a scope signal — it points toward a root-cause diagnostic approach consistent with blameless, evidence-based troubleshooting, rather than a workaround that sidesteps the problem or discards the automation.

**Why This Is Correct**

Since the pipeline failure began immediately after a specific, identifiable change to the Cloud Build configuration, and that configuration is version-controlled in Git, running a diff between the last working revision and the current one directly surfaces the exact lines that changed — which is almost always where the bug was introduced in a “it broke right after I changed X” scenario. This lets you pinpoint and correct the specific misconfiguration (a malformed step, an incorrect trigger condition, a broken substitution variable, etc.) with minimal guesswork, restoring the pipeline to a working state while preserving the intended change where possible. It’s the most targeted, lowest-effort path to root cause given the information already available.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Disabling the pipeline and reverting to manual builds abandons the automation entirely rather than fixing it — it’s a workaround that sacrifices the benefits of CI/CD (consistency, speed, reduced human error) instead of addressing the actual defect, and it does nothing to prevent the same misconfiguration from recurring once the pipeline is eventually re-enabled.

  * **Option B — Different Use Case:** Switching the artifact destination from Docker Hub to Artifact Registry doesn’t address the reported symptom at all — the pipeline isn’t failing because of where it pushes images, it’s failing to build anything in the first place, almost certainly due to the YAML change itself. This is a distractor that changes something unrelated to the actual failure.

  * **Option C — Incorrect:** Error Reporting is designed to aggregate and surface exceptions and stack traces from running application code, not to analyze static configuration files; uploading a YAML file to Cloud Storage and pointing Error Reporting at it doesn’t correspond to how that service actually works, so this approach can’t meaningfully diagnose a Cloud Build configuration problem.

**Exam Trap**

The trap is reaching for a tool-sounding “observability” answer (Option C) because the scenario involves troubleshooting, without checking whether that tool’s actual function matches the problem — Error Reporting ingests application exceptions, not static config files, so it has no mechanism to inspect or validate YAML syntax or pipeline logic. The fastest, most defensible fix is almost always the one that directly uses the evidence already pointing at the cause (the recent, version-controlled change), rather than introducing a new, mismatched tool.

**Foundation Concept**

When a system breaks immediately following a specific, identifiable change, the most effective troubleshooting first step is to examine that exact change before considering broader remedies — version control is one of the most direct diagnostic tools available precisely because it preserves the before/after state needed to isolate a regression quickly, which is far more targeted than disabling the system, changing unrelated components, or applying a monitoring tool outside its intended scope.

**Real-World Connection**

Teams running CI/CD pipelines routinely rely on this exact pattern when a pipeline regresses after a configuration commit: a quick `git diff` or `git log -p` against the pipeline definition file isolates the change, often revealing a typo, an incorrect step ordering, or a broken trigger condition within minutes — turning what could be an extended outage of the delivery pipeline into a short, well-understood fix, and reinforcing why keeping CI/CD configuration under the same version control as application code is a core DevOps practice.

**Memory Hook**

“It broke right after a specific change, and that change is in version control” → diff the before/after states first, before reaching for unrelated fixes or abandoning the pipeline.

**30-Second Exam Takeaway**

When a CI/CD pipeline fails immediately after a configuration change and that configuration is version-controlled, the SRE-aligned first move is always to compare the before/after states directly (a Git diff) to isolate the root cause — not to disable the pipeline, swap an unrelated component, or apply a monitoring tool that doesn’t inspect configuration files.

**Official References**

[**Google Cloud — Cloud Build configuration overview and troubleshooting builds:**](https://cloud.google.com/build/docs/troubleshooting) Supports: the correct-answer mechanism of diagnosing a Cloud Build YAML regression by examining the configuration change that preceded the failure

[Google Cloud — Professional Cloud DevOps Engineer exam guide, Section 2 (CI/CD pipelines): ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment — diagnosing and resolving CI/CD pipeline failures is explicitly part of building and implementing CI/CD pipelines

---

## Question 16

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You run an application on Compute Engine and collect its logs through Cloud Logging. You discover that some personally identifiable information (PII) is leaking into certain log entry fields, and every affected entry begins with the text `userinfo`. You need to capture these entries in a secure location for later review while preventing them from being retained in Cloud Logging. What should you do?

- [ ] A. Create a basic log filter matching `userinfo`, and then configure a log export in the Google Cloud console with Cloud Storage as the sink.
- [ ] B. Use a Fluentd filter plugin with the logging agent to strip log entries containing `userinfo`, and then copy those entries to a Cloud Storage bucket.
- [x] C. Create an advanced log filter matching `userinfo`, configure a log export in the Google Cloud console with Cloud Storage as the sink, and then configure a log exclusion using `userinfo` as the filter.
- [ ] D. Use a Fluentd filter plugin with the logging agent to strip log entries containing `userinfo`, create an advanced log filter matching `userinfo`, and then configure a log export in the Google Cloud console with Cloud Storage as the sink.

### Explanation

**Correct Answer**

**C. Create an advanced log filter matching**`**userinfo**`**, configure a log export in the Google Cloud console with Cloud Storage as the sink, and then configure a log exclusion using**`**userinfo**`**as the filter.**

**Exam Reasoning Explanation**

The scenario has two distinct, must-have requirements: capture the matching entries somewhere secure for later review, and stop them from being retained in Cloud Logging. Cloud Logging’s architecture provides a dedicated mechanism for each: a sink with a filter routes matching entries to an external destination like Cloud Storage (satisfying capture), while a log exclusion independently stops matching entries from being written into Cloud Logging’s own storage (satisfying prevention). Because these are two separate, purpose-built controls operating at the log-routing layer, the correct approach configures both of them together — and because the filter needs to match text appearing within a specific field rather than a simple resource-type or severity match, it must be an advanced filter, not a basic one.

**Key Exam Clues**

  * “capture these log entries in a secure location for later review” is a hard constraint — it requires the matching entries to still exist somewhere accessible, ruling out any approach that simply discards them.

  * “prevent them from leaking to [Cloud Logging]” is a second, independent hard constraint — it requires suppressing retention specifically within Cloud Logging’s own storage, which is a distinct action from exporting a copy elsewhere.

  * “All PII entries begin with the text userinfo” is a technical signal pointing toward a text-pattern match on log content, which requires an advanced log filter (capable of matching on field content) rather than a basic filter (typically limited to simpler criteria like resource type or severity).

**Why This Is Correct**

An advanced log filter matching `userinfo` precisely targets the affected entries based on their content. Configuring a sink with that filter and Cloud Storage as the destination exports a copy of every matching entry to a secure, access-controlled bucket for later review, satisfying the capture requirement. Separately configuring a log exclusion with the same `userinfo` filter tells Cloud Logging not to ingest and store matching entries in its own log storage going forward, directly satisfying the leak-prevention requirement. Because sinks and exclusions are independent, complementary mechanisms within the same log-routing pipeline, applying both together achieves exactly what the scenario asks for — a secure copy retained outside Cloud Logging, and no retention of the sensitive data inside it.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** A basic log filter and export sink would capture matching entries in Cloud Storage, partially satisfying the first requirement, but a basic filter isn’t built to reliably match arbitrary text patterns within log entry fields, and — critically — this option includes no exclusion step at all, so the PII would continue to be retained in Cloud Logging’s own storage, failing the leak-prevention requirement entirely.

  * **Option B — Different Use Case:** Modifying the logging agent’s pipeline to strip matching entries via a Fluentd filter addresses prevention at the collection layer rather than within Cloud Logging’s routing controls, which is a heavier, host-level change requiring agent configuration management across every instance, and it isn’t the mechanism Cloud Logging itself provides for this exact use case. It also doesn’t by itself establish a clean, Cloud Logging-native secure copy — the “copy the entries” step is left vague and disconnected from the filtering logic.

  * **Option D — Different Use Case:** This combines the agent-side Fluentd filtering of Option B with the filter-and-export logic of Option A, but still doesn’t configure a log exclusion — so even with the entries removed at the agent before shipping, there’s no guarantee within Cloud Logging’s own routing that a similar future leak would be suppressed, and it layers unnecessary agent-side complexity on top of controls Cloud Logging already provides natively.

**Exam Trap**

The trap is assuming that exporting matching entries to Cloud Storage (Option A) is sufficient on its own, since “capture them in Cloud Storage” sounds like it solves the whole problem — but exporting a copy via a sink does not stop the original entries from also being retained in Cloud Logging’s default storage. Export and exclusion are separate, additive controls, and missing the exclusion step leaves the leak-prevention half of the requirement completely unaddressed.

**Foundation Concept**

In Cloud Logging’s routing model, a sink determines where a copy of matching log entries is sent (which can include external destinations like Cloud Storage, BigQuery, or Pub/Sub), while an exclusion filter determines what is withheld from being written into Cloud Logging’s own log storage. These are independent levers: you can export without excluding (keeping entries in both places), exclude without exporting (discarding entries entirely), or do both together — which is the pattern needed whenever sensitive data must be preserved somewhere secure while being kept out of the general logging system.

**Real-World Connection**

Teams handling accidental PII leaks in logs commonly use exactly this sink-plus-exclusion pattern: route the sensitive entries to a tightly access-controlled Cloud Storage bucket (often with additional encryption, retention, and audit controls) for compliance review and root-cause analysis, while excluding them from the organization’s general-purpose log buckets so they aren’t visible to the broader set of engineers who have standard log-viewing access — addressing both the operational need to investigate and the compliance need to minimize exposure.

**Memory Hook**

Capture sensitive logs elsewhere with a sink; stop them from staying in Cloud Logging with an exclusion — you need both, not just one.

**30-Second Exam Takeaway**

Whenever a Cloud Logging question asks you to both preserve certain log entries somewhere secure and stop them from being retained in Cloud Logging itself, look for the option that pairs an advanced filter plus export sink (capture) with a matching log exclusion (prevention) — an export alone never stops the data from also sitting in Cloud Logging’s own storage.

**Official References**

[Google Cloud — Configure log sinks: ](https://docs.cloud.google.com/logging/docs/export/configure_export_v2)Supports: the correct-answer mechanism of using an advanced log filter and a Cloud Storage sink to export matching PII entries to a secure location

[**Google Cloud — Configure log exclusions:**](https://docs.cloud.google.com/logging/docs/exclusions) Supports: the correct-answer mechanism of using a log exclusion filter to prevent matching entries from being retained in Cloud Logging’s own storage

---

## Question 17

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

You need to deploy a new production service that will scale automatically using a Managed Instance Group (MIG) and that must run across multiple regions. Each instance requires a large amount of resources, and you need to plan for capacity ahead of the deployment. What should you do?

- [ ] A. Use the `n1-highcpu-96` machine type in the MIG’s instance configuration.
- [ ] B. Monitor Cloud Trace results to determine how many resources are required.
- [x] C. Confirm that the resource requirements fall within the available quota limits in each target region.
- [ ] D. Deploy the service in a single region, and use a global load balancer to route traffic to that region.

### Explanation

**Correct Answer**

**C. Confirm that the resource requirements fall within the available quota limits in each target region.**

**Exam Reasoning Explanation**

The decisive requirement is capacity planning specifically for a multi-region deployment of resource-heavy instances — and Google Cloud resource quotas (CPUs, specific machine-type families, IP addresses, and similar) are allocated and enforced per project per region. That means a deployment plan is incomplete, and genuinely at risk of failing partway through rollout, until you’ve confirmed each target region actually has enough available quota to support the planned instance sizes and counts. None of the other options engages with this region-specific capacity constraint: picking a machine type addresses sizing but not whether that sizing is actually obtainable in every region, monitoring request latency data addresses a completely different concern, and consolidating to one region directly contradicts the multi-region requirement rather than solving the planning problem.

**Key Exam Clues**

  * “plan for capacity” is a hard constraint — it specifically calls for a capacity-planning action, not a sizing choice, a monitoring tool, or an architectural simplification.

  * “deployed over multiple regions” is a hard constraint — it rules out any option that collapses the deployment into a single region, since quotas and capacity must be confirmed independently in each of several regions.

  * “needs a large number of resources for each instance” is a technical signal — it raises the real risk of hitting regional quota ceilings (CPU quotas, specific machine-type quotas) precisely because large instances consume quota quickly, making quota validation materially important here.

**Why This Is Correct**

Google Cloud quotas are enforced at the project-and-region level, so a MIG configured to scale instances with large resource footprints across several regions can succeed in one region and fail to provision in another purely because that region’s quota hasn’t been raised to accommodate the planned instance count and size. Confirming available quota in every target region before deployment is the direct, necessary capacity-planning step: it surfaces where a quota increase request is needed ahead of time, preventing a scaling event or initial rollout from silently failing or being capped well below the intended capacity in one or more regions.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** Choosing a specific machine type like `n1-highcpu-96` is a sizing decision that might suit a high-CPU workload, but selecting a machine type says nothing about whether enough of that machine type’s resources are actually available under quota in each target region — it addresses “what to request” without addressing “can you actually get it,” which is the core of capacity planning here.

  * **Option B — Different Use Case:** Cloud Trace captures distributed request latency data to help diagnose where time is spent across a request’s lifecycle — it’s a performance-debugging and observability tool, not a capacity-planning or quota-forecasting tool. It provides no information about CPU/resource quota availability in a given region.

  * **Option D — Violates Requirement:** Deploying in a single region behind a global load balancer directly abandons the stated requirement to run the service across multiple regions. It might simplify quota management by concentrating everything in one place, but it does so by ignoring an explicit constraint of the scenario rather than solving the capacity-planning problem within it.

**Exam Trap**

The trap is treating machine-type selection (Option A) as equivalent to capacity planning, since picking “enough CPU per instance” feels like it addresses “a large number of resources for each instance.” But sizing an individual instance and confirming that your project can actually obtain that many instances of that size, in every region you’re deploying to, are two different steps — quota validation is the one capacity planning specifically requires.

**Foundation Concept**

Capacity planning for a multi-region deployment must account for the fact that cloud resource quotas are regional and finite: successfully designing an architecture (machine type, autoscaling policy, region selection) is necessary but not sufficient — you must also confirm the underlying capacity is actually allocated and available in every region the architecture depends on, requesting quota increases ahead of deployment wherever a gap exists.

**Real-World Connection**

Teams rolling out a resource-intensive service across several regions routinely check (and often pre-request increases to) CPU and machine-family quotas in each region as part of their launch checklist, specifically because discovering a quota shortfall during a live scaling event — rather than during planning — turns a routine autoscaling action into a production incident where the MIG simply can’t add the instances it needs.

**Memory Hook**

Multi-region capacity planning always includes a region-by-region quota check — architecture and sizing decisions alone don’t guarantee the capacity is actually available where you need it.

**30-Second Exam Takeaway**

Whenever a question asks about capacity planning for a deployment spanning multiple regions or projects, look for the option that validates available resource quota in each target location — quotas are regional, so a plan isn’t complete until you’ve confirmed the numbers actually fit.

**Official References**

[**Google Cloud — Resource quotas overview:**](https://cloud.google.com/docs/quotas/overview) Supports: the correct-answer mechanism of quotas being enforced per project and region, and the need to validate and request increases ahead of a multi-region deployment

[**Google Cloud — Managed instance groups (MIGs) overview:**](https://cloud.google.com/compute/docs/instance-groups) Supports: the architectural context of autoscaling MIGs across multiple regions and why per-region resource availability directly affects scaling outcomes

---

## Question 18

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You support an application that stores product information in a cache. For every cache miss, an entry is logged in Cloud Logging. You want to visualize how often cache misses occur over time. What should you do?

- [ ] A. Link Cloud Logging as a data source in Data Studio, and filter the report on the cache-miss entries.
- [ ] B. Configure Cloud Profiler to identify and visualize when the cache misses occur, based on the logs.
- [x] C. Create a logs-based metric in Cloud Logging, and build a dashboard for that metric in Cloud Monitoring.
- [ ] D. Configure BigQuery as a sink for Cloud Logging, and create a scheduled query that filters the cache-miss logs and writes them to a separate table.

### Explanation

**Correct Answer**

**C. Create a logs-based metric in Cloud Logging, and build a dashboard for that metric in Cloud Monitoring.**

**Exam Reasoning Explanation**

The must-have requirement is a time-series visualization of how often a specific, filterable log event occurs — this is exactly the use case Cloud Logging and Cloud Monitoring were designed to handle together natively, with no custom pipeline or external BI tool required. A logs-based metric converts a log filter (matching the cache-miss entries) into a countable, time-series metric directly within Cloud Logging, and Cloud Monitoring can then chart that metric on a dashboard with essentially no additional setup. Every other option either uses a tool built for a different purpose (code profiling) or routes the data through a heavier, more indirect pipeline (BigQuery scheduled queries, an external BI connector) to arrive at a visualization Cloud Monitoring already provides directly.

**Key Exam Clues**

  * “visualize how often a cache miss happens over time” is a hard constraint — it specifically calls for a time-series count visualization, which logs-based metrics plus Cloud Monitoring dashboards are purpose-built to deliver.

  * “an entry is logged” for every cache miss is a technical signal — it establishes that the event is already captured as a discrete, filterable log entry, meaning no new application instrumentation is needed, only a filter on existing logs.

  * The absence of any stated requirement for long-term archival, complex cross-dataset analysis, or external reporting is an exclusion signal — it rules out heavier options (BigQuery pipelines, external BI tools) built for needs beyond simple frequency visualization.

**Why This Is Correct**

A logs-based metric lets you define a filter (matching the cache-miss log entries) directly in Cloud Logging and have it automatically counted as a time-series metric, with no code changes, data export jobs, or external tooling required. Because that metric now exists as a standard Cloud Monitoring metric, you can immediately chart it on a Cloud Monitoring dashboard to see cache-miss frequency over time, set up alerting on it if desired, and correlate it with other operational metrics — all using the native, tightly integrated path between Cloud Logging and Cloud Monitoring that exists specifically for this kind of “turn a log event into a trend line” use case.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Different Use Case:** Data Studio is a general-purpose reporting and dashboarding tool, but it has no native connector that reads directly from Cloud Logging — getting log data into it typically requires an intermediate step (such as exporting to BigQuery first), making “link Cloud Logging as a source” not a straightforward or native path, and introducing more setup than the logs-based metric approach for what is fundamentally a simple frequency chart.

  * **Option B — Incorrect:** Cloud Profiler is a continuous code-level profiling tool that samples CPU and memory usage within a running application to show where execution time and resources are spent — it has no capability to ingest or visualize arbitrary Cloud Logging entries, so it cannot address this requirement at all.

  * **Option D — Technically Possible but Not Best:** Routing logs to BigQuery via a sink and running scheduled queries to isolate cache-miss entries into a separate table is a viable data pipeline, but it’s considerably more infrastructure than the question calls for — it requires building and maintaining a sink, a scheduled query, and a separate visualization layer on top of the resulting table, when a logs-based metric and Cloud Monitoring dashboard deliver the same time-series visualization with built-in, native tooling and far less setup.

**Exam Trap**

The trap is reaching for a heavier data-engineering solution (BigQuery sink plus scheduled queries, Option D) because it sounds thorough and “production-grade,” when the actual requirement — visualize frequency over time — is already a first-class, built-in capability of Cloud Logging and Cloud Monitoring together. When a log-based count-over-time visualization is all that’s needed, the native logs-based metric path is almost always the better-fit answer over building a custom data pipeline.

**Foundation Concept**

Cloud Logging and Cloud Monitoring are designed to interoperate directly: any log event that can be isolated with a filter can be promoted to a logs-based metric and immediately visualized, alerted on, or combined with other metrics in Cloud Monitoring, without needing to export the data elsewhere first. Reaching for an external pipeline or BI tool is appropriate only when the need goes beyond what this native integration provides — richer cross-dataset analysis, long-term structured querying, or reporting formats Cloud Monitoring doesn’t support.

**Real-World Connection**

Teams commonly use logs-based metrics for exactly this kind of operational signal — cache misses, specific error codes, retry events — because it turns an existing log line into an actionable, chartable, alertable metric in minutes, letting them set an alert if cache-miss frequency crosses a threshold (signaling a caching layer problem) without having to build and maintain any additional data infrastructure.

**Memory Hook**

“How often does a specific log event happen over time?” → logs-based metric in Cloud Logging, charted in Cloud Monitoring — not a profiler, not an external BI tool, not a custom BigQuery pipeline.

**30-Second Exam Takeaway**

When a question asks to visualize the frequency of a specific, filterable log event over time, default to a Cloud Logging logs-based metric paired with a Cloud Monitoring dashboard — it’s the native, lowest-effort path, and heavier options (BigQuery pipelines, external BI tools, profiling tools) are usually distractors solving a different or larger problem than what’s actually being asked.

**Official References**

[Google Cloud — Logs-based metrics overview: ](https://docs.cloud.google.com/logging/docs/logs-based-metrics)Supports: the correct-answer mechanism of converting a log filter into a time-series metric directly within Cloud Logging

[**Google Cloud — Create and manage dashboards in Cloud Monitoring:**](https://docs.cloud.google.com/monitoring/dashboards) Supports: visualizing a logs-based metric’s frequency over time on a Cloud Monitoring dashboard

---

## Question 19

*Domain 2: Building and Implementing CI/CD Pipelines*

Your team uses Cloud Build for all CI/CD pipelines. You want to use the `kubectl` builder in Cloud Build to deploy new images to Google Kubernetes Engine (GKE), and you need to authenticate to GKE while keeping the development effort to a minimum. What should you do?

- [x] A. Grant the Kubernetes Engine Developer role to the Cloud Build service account.
- [ ] B. Specify the Kubernetes Engine Developer role for Cloud Build in the `cloudbuild.yaml` file.
- [ ] C. Create a new service account with the Kubernetes Engine Developer role, and use it to run Cloud Build.
- [ ] D. Add a separate step in Cloud Build that retrieves service account credentials and passes them to `kubectl`.

### Explanation

**Correct Answer**

**A. Grant the Kubernetes Engine Developer role to the Cloud Build service account.**

**Exam Reasoning Explanation**

The hard requirement is authenticating Cloud Build’s `kubectl` builder to the GKE cluster while minimizing development effort — meaning the solution should use existing, built-in mechanisms rather than custom scripting or additional infrastructure. Cloud Build already runs every build under its own default service account, and the `kubectl` builder is designed to pick up that identity’s credentials automatically (via the GKE cluster’s environment variables for zone/region and cluster name) with no manual credential handling required. That makes IAM role assignment on the existing Cloud Build service account the single, minimal-effort action needed — every other option either grants the permission in the wrong place (a YAML file isn’t an IAM mechanism), introduces unnecessary new infrastructure (a separate service account to run Cloud Build itself), or adds custom pipeline logic to do something the builder already handles natively.

**Key Exam Clues**

  * “minimizing development effort” is a hard constraint — it rules out any option requiring custom scripting, credential-handling steps, or additional infrastructure beyond what Cloud Build and the `kubectl` builder already provide.

  * “the kubectl builder for Cloud Build” is a technical signal — it specifies a tool that is built to authenticate using the Cloud Build service account’s existing identity, pointing directly at an IAM-role-grant solution rather than a manual credential-passing one.

  * “authenticate to GKE” is a scope signal — it’s specifically an identity/authorization task, which in Google Cloud is solved through IAM role bindings, not through application configuration files like `cloudbuild.yaml`.

**Why This Is Correct**

Every Cloud Build job runs under a Google-managed Cloud Build service account by default, and the `kubectl` builder is specifically designed to authenticate to a GKE cluster using that identity’s IAM permissions — it reads the cluster, zone/region, and project details from environment variables and handles the credential exchange itself. Granting the Kubernetes Engine Developer role (`roles/container.developer`) to that existing service account gives it exactly the permissions needed to interact with Kubernetes API objects in the cluster, which is all that’s required: no new service account, no custom credential-retrieval step, and no configuration-file-level role declaration (which isn’t how IAM permissions are granted in the first place). This is the smallest possible change that fully satisfies the authentication requirement.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Incorrect:** IAM roles are granted through Identity and Access Management policy bindings on a principal (a user, group, or service account) — they are not something you “specify” inside a `cloudbuild.yaml` build configuration file. This option describes a mechanism that doesn’t correspond to how GCP IAM actually works, so it can’t function as described.

  * **Option C — Technically Possible but Not Best:** Creating a new service account and configuring Cloud Build to run under it would work, but it’s unnecessary additional effort and infrastructure when the default Cloud Build service account already exists and only needs an IAM role granted to it. This adds a service-account creation and configuration step that doesn’t improve on simply granting the role to the existing identity.

  * **Option D — Technically Possible but Not Best:** Manually retrieving service account credentials and passing them to `kubectl` in a separate build step duplicates functionality the `kubectl` builder already performs automatically via the Cloud Build service account’s identity. This is significantly more development effort (writing and maintaining custom credential-handling logic) for no functional benefit over simply granting the role.

**Exam Trap**

The trap is Option B, which sounds plausible because `cloudbuild.yaml` is where you configure _what_ a build does — but IAM role grants are an identity/access-management concept entirely separate from build step configuration, and conflating the two is a common misunderstanding of where permissions actually live in Google Cloud. The decisive distinction is that authentication/authorization is an IAM concern (a policy binding on a principal), never something declared inside the pipeline’s own YAML definition.

**Foundation Concept**

When a CI/CD tool needs to interact with another Google Cloud service, the lowest-effort and most maintainable authentication pattern is almost always to grant the pipeline’s existing runtime identity (its default service account) the specific IAM role needed for the target service — rather than creating new service accounts, manually handling credentials, or trying to configure permissions through the pipeline’s own configuration file, which has no authority over IAM.

**Real-World Connection**

Teams running Cloud Build-to-GKE deployment pipelines commonly grant the Cloud Build service account the Kubernetes Engine Developer role exactly once during pipeline setup, after which every subsequent build’s `kubectl` builder step authenticates and deploys without any further credential management — keeping the pipeline simple to maintain and avoiding the security and operational overhead of managing separate service account keys or custom authentication logic.

**Memory Hook**

Authenticating a GCP CI/CD tool to another GCP service is almost always “grant the existing service account the right IAM role” — not a new service account, not a config-file permission, and not manual credential plumbing.

**30-Second Exam Takeaway**

When a Cloud Build question asks how to authenticate a builder (like `kubectl`) to another Google Cloud service with minimal effort, look for the option that grants the appropriate IAM role directly to Cloud Build’s existing default service account — that’s almost always simpler and more correct than creating new service accounts, writing custom credential-handling steps, or trying to set permissions inside the build configuration file itself.

**Official References**

[**Google Cloud — Authenticating to the Kubernetes API server:**](https://cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication) Supports: the correct-answer mechanism of granting `roles/container.developer` to the service account used to authenticate to a GKE cluster

[**Google Cloud — IAM roles for Kubernetes Engine:**](https://cloud.google.com/kubernetes-engine/docs/how-to/iam) Supports: the Kubernetes Engine Developer role’s purpose and scope as the minimal-effort permission grant for deploying to GKE

---

## Question 20

*Domain 3: Applying Site Reliability Engineering Practices*

Your organization follows Site Reliability Engineering practices. You are acting as Communications Lead for a large, ongoing incident affecting customer-facing applications, and there is still no estimated resolution time. You’re receiving emails from internal stakeholders asking for updates, as well as emails from customers asking what’s happening. You want to efficiently keep everyone affected informed. What should you do?

- [ ] A. Focus on responding to internal stakeholders at least every 30 minutes, and commit to “next update” times in those communications.
- [x] B. Provide periodic updates to all stakeholders in a timely manner, and commit to a “next update” time in every communication.
- [ ] C. Delegate responding to internal stakeholder emails to another member of the incident response team, and focus on providing responses directly to customers.
- [ ] D. Forward all internal stakeholder emails to the Incident Commander and let them manage internal communications, while you focus on providing responses directly to customers.

### Explanation

**Correct Answer**

**B. Provide periodic updates to all stakeholders in a timely manner, and commit to a “next update” time in every communication.**

**Exam Reasoning Explanation**

The must-have constraint is efficiently keeping _everyone affected_ informed — both internal stakeholders and customers are named explicitly, so any approach that serves one audience while ignoring or offloading the other fails to meet the stated scope. The role described (handling communications for the incident) is exactly the Communications Lead function in Google’s incident management framework, whose core responsibility is managing information flow to all audiences, not just one. Given “no estimated time for a resolution,” the efficient and expectation-setting move for every audience is a predictable cadence of periodic updates, each one committing to when the next update will arrive — this single practice scales naturally across however many stakeholders are asking, replacing a flood of one-off replies with a structured broadcast rhythm.

**Key Exam Clues**

  * “efficiently provide updates to everyone affected by the outage” is a hard constraint — it names both audiences (internal stakeholders and customers) and requires covering both, ruling out any option that narrows focus to just one.

  * “no estimated time for a resolution” is a technical signal — it specifically calls for a practice that manages expectations under uncertainty, which is exactly what committing to a “next update” time accomplishes regardless of whether the underlying issue is resolved yet.

  * “in charge of Communications” is a scope/role signal — it identifies this as the Communications Lead function, whose defined responsibility spans all stakeholder communications, not a narrower subset.

**Why This Is Correct**

Periodic, scheduled updates replace a reactive, one-off-reply approach (which doesn’t scale as email volume grows) with a predictable broadcast cadence that efficiently reaches both internal stakeholders and customers from a single communications effort. Committing to a “next update” time in every communication is the specific technique that manages expectations when there’s no resolution ETA — it tells every recipient exactly when they’ll hear more, reducing the anxious, repeated “any updates?” follow-ups that consume further Communications Lead time, and keeping both audiences appropriately informed throughout a prolonged incident without requiring a reply to be drafted for every individual email received.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** This narrows focus to internal stakeholders only, leaving customers without updates entirely — directly conflicting with “everyone affected by the outage,” which explicitly includes customers as well as internal stakeholders.

  * **Option C — Violates Requirement:** Delegating internal communications away and focusing solely on customers still results in only one audience receiving direct attention from the person responsible for Communications; more fundamentally, it abandons the periodic-update structure in favor of ad hoc delegation, which doesn’t establish the predictable update cadence the uncertain-ETA situation calls for.

  * **Option D — Violates Requirement:** Handing internal stakeholder communications to the Incident Commander pulls that person away from their actual role — commanding and coordinating the incident response — to handle a function that belongs to Communications. It also still results in only customers receiving direct attention from the Communications Lead, again failing to cover both named audiences from the role actually responsible for them.

**Exam Trap**

The trap is assuming that splitting the two audiences between different people (Options C and D) is a reasonable division of labor under high email volume — but IMAG’s Communications Lead role exists precisely so that one role owns messaging across all audiences, and reassigning audience-specific communications to the Incident Commander or another unspecified team member either misuses a different role’s time or abandons the stated requirement to serve “everyone affected.” The efficient fix for volume isn’t reassignment — it’s switching from one-off replies to scheduled, scalable periodic broadcasts.

**Foundation Concept**

Under prolonged uncertainty (no ETA), the single highest-leverage communications practice is a predictable update cadence with an explicit commitment to the next update time — it substitutes structure for individualized responses, scales to any number of recipients without added effort per person, and directly reduces stakeholder anxiety by replacing silence (or reactive, inconsistent replies) with a reliable rhythm of information.

**Real-World Connection**

Teams running a major incident commonly post status-page or broadcast updates on a fixed interval (e.g., “next update in 30 minutes”) to both internal channels and public status pages simultaneously, which lets the Communications Lead spend their limited time crafting one accurate, well-reviewed update rather than fielding a growing queue of individual emails — directly reducing the operational load that incident communications would otherwise place on the broader response effort.

**Memory Hook**

Serving “everyone affected” under incident communications means one scheduled update reaching all audiences, each one promising when the next update lands — not splitting audiences apart or handing part of the job to a role that doesn’t own it.

**30-Second Exam Takeaway**

When an SRE incident-communications question describes multiple stakeholder groups and an uncertain resolution time, favor the option that delivers periodic updates to all named audiences with an explicit “next update” commitment — options that narrow focus to one audience or reassign communications to an unrelated role (like the Incident Commander) are distractors that fail the “everyone affected” requirement.

**Official References**

[**Google SRE — Incident Management Guide:**](https://sre.google/static/pdf/IncidentManagementGuide.pdf) Supports: the Communications Lead role’s responsibility for managing information flow to all stakeholders, and the practice of periodic, scheduled updates during a prolonged incident

[Google SRE Workbook — Chapter 9, Incident Response: ](https://sre.google/workbook/incident-response/)Supports: the rationale for committing to a next-update cadence as a core communications practice when an incident’s resolution time is unknown

---

## Question 21

*Domain 2: Building and Implementing CI/CD Pipelines*

Your application artifacts are built and deployed through a CI/CD pipeline. You want the pipeline to access application secrets securely, and you also want to be able to rotate those secrets easily in the event of a security breach. What should you do?

- [ ] A. Prompt developers for secrets at build time, and instruct them not to store secrets at rest.
- [ ] B. Store secrets in a separate configuration file in Git, and give select developers access to that file.
- [x] C. Store secrets in Cloud Storage, encrypted with a key from Cloud KMS, and grant the CI/CD pipeline access to Cloud KMS through IAM.
- [ ] D. Encrypt the secrets and store them in the source code repository, store the decryption key in a separate repository, and grant the pipeline access to that repository.

### Explanation

**Correct Answer**

**C. Store secrets in Cloud Storage, encrypted with a key from Cloud KMS, and grant the CI/CD pipeline access to Cloud KMS through IAM.**

**Exam Reasoning Explanation**

The two must-have requirements are secure, automated access for the pipeline and easy rotation in a breach scenario — which together rule out anything requiring manual human intervention at build time or anything that puts secrets inside version control, where history is hard to fully purge and access can’t be centrally revoked. Each option has to be checked against both requirements independently: automation compatibility, and how cleanly a compromised secret can be rotated. A centralized, encrypted store with IAM-controlled access satisfies both — the pipeline authenticates automatically via its service account, the secret value and the encryption key are managed independently of any code repository, and rotating either the secret or revoking access is a quick operation in a dedicated system built for exactly this.

**Key Exam Clues**

  * “securely access application secrets” is a hard constraint — it requires automated, access-controlled retrieval by the pipeline itself, ruling out any human-in-the-loop step.

  * “more easily rotate secrets in case of a security breach” is a second hard constraint — it demands that updating or revoking a secret be fast and centralized, which disqualifies anything embedding secrets in version-controlled files (where rotation means purging history and redeploying across every clone).

  * “CI/CD pipeline” as the consumer is a technical signal pointing toward IAM-based service-to-service access (the pipeline’s own identity authenticating to a secrets store), rather than developer-managed access controls on a shared file.

**Why This Is Correct**

Storing secrets in Cloud Storage with Cloud KMS encryption keeps the sensitive values out of source control entirely, encrypted at rest with keys that are centrally managed and access-controlled. Granting the CI/CD pipeline’s service account IAM access to the relevant Cloud KMS key and Cloud Storage object lets the pipeline retrieve and decrypt secrets automatically during a build with no manual step, satisfying secure access. For rotation, updating the stored secret value or rotating the KMS key is a contained, centralized operation — and if a breach occurs, revoking IAM access or rotating the key immediately cuts off further use of the compromised secret, without needing to rewrite Git history or coordinate changes across every repository that might reference it.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Prompting developers for secrets at build time breaks automation entirely — a CI/CD pipeline is meant to run unattended, and requiring a human to supply a secret defeats the purpose of continuous delivery while also providing no mechanism for secure storage or rotation at all.

  * **Option B — Violates Requirement:** Storing secrets in a Git configuration file, even with restricted developer access, puts sensitive values into version control history, where they persist indefinitely across clones and forks; rotating a compromised secret would require not just updating the file but scrubbing history everywhere it was ever committed, which is neither secure nor easy.

  * **Option D — Technically Possible but Not Best:** Encrypting secrets and storing them alongside code, with the decryption key in a separate repository, is a workable but weaker pattern than using a dedicated key-management service: both the encrypted secrets and the key end up living in source control systems not purpose-built for secret lifecycle management, lacking the centralized audit logging, fine-grained IAM controls, and key-rotation tooling that Cloud KMS provides natively. Rotation here still means committing new encrypted values and managing key access through repository permissions rather than a dedicated IAM/KMS control plane.

**Exam Trap**

The trap is Option D looking secure at first glance because the secrets are “encrypted” — but encryption alone doesn’t solve the rotation and access-revocation problem if the encrypted blob and its key are still managed through source-control permissions rather than a centralized key-management system built for exactly this lifecycle (issuing, rotating, and revoking access to keys and secrets independently of code history).

**Foundation Concept**

Secrets belong in a system designed around their specific lifecycle — centralized storage, encryption at rest, fine-grained IAM-based access, and the ability to rotate or revoke instantly — never in source control, even encrypted, because version control systems are optimized for code history and collaboration, not for the access-revocation and audit guarantees a compromised secret response actually requires.

**Real-World Connection**

While Cloud Storage encrypted with a Cloud KMS key is a valid and functional pattern, Google Cloud also offers Secret Manager, a service purpose-built for exactly this use case — centralized secret storage, automatic versioning, IAM-based per-secret access control, and built-in audit logging — which many CI/CD pipelines use directly for application secrets precisely because it provides this same security and rotation model with less infrastructure to manage than assembling Cloud Storage and Cloud KMS by hand.

**Memory Hook**

Secrets for an automated pipeline belong in a centralized, IAM-controlled, encrypted store — never in source control, encrypted or not — because only a dedicated secret-management approach makes both secure automated access and fast rotation possible.

**30-Second Exam Takeaway**

When a CI/CD question asks how to securely provide and easily rotate secrets, favor a centralized, encrypted secret store with IAM-based access over anything that puts secrets (even encrypted ones) into source control or requires a human to supply them at build time — the decisive test is whether a compromised secret can be rotated and revoked without touching repository history.

**Official References**

[**Google Cloud — Cloud KMS overview:**](https://cloud.google.com/kms/docs/key-management-service) Supports: the correct-answer mechanism of encrypting secrets with centrally managed, rotatable Cloud KMS keys and controlling access via IAM

[Google Cloud — Secret Manager overview: ](https://cloud.google.com/secret-manager/docs/overview)Supports: the current, purpose-built Google Cloud service for application secret storage, access control, and rotation referenced as the broader best-practice context

---

## Question 22

*Domain 3: Applying Site Reliability Engineering Practices*

You support a production service running on a single Compute Engine instance. You regularly spend time recreating the service by deleting the crashing instance and creating a new one from the relevant image. You want to reduce the time spent on this manual work while following Site Reliability Engineering principles. What should you do?

- [ ] A. File a bug with the development team so they can find the root cause of the crashing instance.
- [x] B. Create a managed instance group with a single instance, and use health checks to determine the system’s status.
- [ ] C. Place a load balancer in front of the Compute Engine instance, and use health checks to determine the system’s status.
- [ ] D. Create a Cloud Monitoring dashboard with SMS alerts so you can begin recreating the crashed instance promptly after it crashes.

### Explanation

**Correct Answer**

**B. Create a managed instance group with a single instance, and use health checks to determine the system’s status.**

**Exam Reasoning Explanation**

The hard requirement is eliminating manual, repetitive toil — specifically the recurring human effort of deleting a crashed instance and recreating it from an image — which is exactly the kind of work SRE principles define as toil to be automated away. That immediately rules out anything that still requires a person to notice the crash and act (filing a bug, watching a dashboard and reacting to an alert) in favor of a mechanism that performs the recreation automatically. A managed instance group (MIG) is Google Cloud’s native automation for exactly this: it continuously monitors instance health and automatically recreates any instance that fails its health check, even when the group size is just one, turning a manual recovery procedure into a fully automated self-healing loop.

**Key Exam Clues**

  * “reduce the time spent performing manual operations” is a hard constraint — it specifically targets reducing human toil, not just detecting or being notified of failures faster.

  * “following Site Reliability Engineering principles” is a technical signal — SRE explicitly treats recurring manual recovery work as toil to be eliminated through automation, pointing toward a self-healing mechanism rather than better alerting.

  * “deleting the crashing instance and creating a new instance based on the relevant image” describes a repeatable, mechanical recovery procedure — a technical signal that this is precisely the kind of task a managed instance group’s auto-healing is built to automate.

**Why This Is Correct**

A managed instance group, even with a target size of one, continuously applies health checks to its member instance and automatically deletes and recreates that instance from the configured instance template whenever it fails its health check — this is functionally identical to the manual recreate-from-image procedure described in the scenario, except performed automatically by the platform with no human action required. This directly and completely eliminates the recurring manual toil the question identifies, replacing a human-driven recovery loop with a system-driven one, which is the core SRE objective of reducing time spent on repetitive operational work.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Different Use Case:** Filing a bug to investigate the root cause of the crashes is a legitimate and valuable parallel action (and good SRE postmortem practice), but it does nothing to reduce the manual recreation work happening in the meantime — the instance will keep crashing and still require manual recreation until the underlying bug is found and fixed, which could take considerable time.

  * **Option C — Technically Possible but Not Best:** A load balancer with health checks can detect that an unhealthy instance shouldn’t receive traffic and can route around it, but a load balancer does not recreate or replace the failed instance itself — the crashed instance still needs to be manually deleted and recreated. This addresses traffic routing, not the automated recovery the scenario actually needs.

  * **Option D — Technically Possible but Not Best:** A monitoring dashboard with SMS alerts speeds up human awareness of a crash, letting you react faster, but it still requires a person to receive the alert and manually perform the same delete-and-recreate steps — it reduces detection latency, not the manual operational work itself, which is the specific time sink the question asks you to reduce.

**Exam Trap**

The trap is Option D, which looks like it addresses “reduce time spent” because faster notification does shorten the overall incident timeline — but faster awareness of a problem is not the same as eliminating the manual labor of fixing it. The distinguishing requirement is toil reduction through automation, not faster human response, which only the managed instance group’s self-healing actually provides.

**Foundation Concept**

SRE treats manual, repetitive, automatable operational work as toil, and the standard response to toil is not to detect it faster or notify about it sooner, but to automate it away entirely. When a scenario describes a human repeatedly performing the same mechanical recovery steps, the SRE-aligned answer is almost always the platform feature that performs that exact recovery automatically — here, a managed instance group’s health-check-driven auto-healing — rather than any improvement to alerting or escalation around the manual process.

**Real-World Connection**

Teams running even single-instance production services commonly wrap them in a managed instance group specifically to gain this auto-healing behavior at essentially no architectural cost — the group still runs just one instance, but a crashed or unresponsive instance is automatically replaced from the same instance template within minutes, freeing the on-call engineer from being paged for routine instance failures and letting their attention go toward investigating recurring root causes instead of performing the recovery itself.

**Memory Hook**

Recurring manual delete-and-recreate work is toil — automate it with a managed instance group’s health-check-based auto-healing, not with better alerts or faster human reaction.

**30-Second Exam Takeaway**

When a question describes an engineer regularly performing the same manual recovery steps and asks how to reduce that time under SRE principles, look for the option that automates the recovery itself (a managed instance group with health checks) rather than options that only improve detection, notification, or routing around the problem.

**Official References**

[**Google Cloud — Autohealing instances in a managed instance group:**](https://cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) Supports: the correct-answer mechanism of automatic, health-check-driven instance recreation, including for a single-instance managed instance group

[**Google SRE Book — Eliminating Toil:**](https://sre.google/sre-book/eliminating-toil/) Supports: the SRE principle of automating recurring manual operational work rather than improving detection or response speed around it

---

## Question 23

*Domain 3: Applying Site Reliability Engineering Practices*

You are responsible for writing and updating the Terraform configurations that define your organization’s infrastructure. Two new engineers will soon contribute to the same codebase. You need to choose tooling and establish a workflow that prevents team members from overwriting one another’s changes. You also need to make sure the latest version always contains every update. What should you do?

- [ ] A.
    Keep the code in a Git-based version control system.
    Define a workflow in which each developer merges their own changes at the end of the working day.
    Bundle the code and upload it to a versioned Cloud Storage bucket, designating that upload as the current master version.
- [x] B.
    Keep the code in a Git-based version control system.
    Define a workflow that requires peer code review and unit testing to validate integrity and functionality before changes are integrated.
    Define a workflow in which the fully integrated code in the repository is treated as the current master version.
- [ ] C.
    Keep the code as plain-text files in Google Drive, arranged in a defined folder hierarchy.
    At the end of each day, verify that every change is reflected in the files within that hierarchy.
    Rename the folder hierarchy using a predefined naming convention that increments the version number.
- [ ] D.
    Keep the code as plain-text files in Google Drive, arranged in a defined folder hierarchy.
    At the end of each day, verify that every change is reflected in the files within that hierarchy, then create a new .zip archive using a predefined naming convention.
    Upload the .zip archive to a versioned Cloud Storage bucket and accept it as the latest version.

### Explanation

**Correct Answer**

**B. Keep the code in a Git-based version control system; define a workflow that requires peer code review and unit testing to validate integrity and functionality before changes are integrated; define a workflow in which the fully integrated code in the repository is treated as the current master version.**

**Exam Reasoning Explanation**

Separate the two must-haves from the quality measures. The must-haves are that concurrent contributors cannot silently overwrite each other, and that the latest version reliably contains every update. Peer review and testing before integration are the quality measures that make the shared codebase trustworthy. Work through each requirement. Preventing overwrites requires a tool with branching, merging, and conflict detection. Capturing all updates requires a single integration point that every change flows through. Only a Git-based repository with a gated merge process and one authoritative main line meets both. File shares and zip snapshots fail the first requirement, so they are eliminated. Option A has the right tool but a weak process and a second source of truth, so it loses to B.

**Key Exam Clues**

  * **“prevent you from overwriting each other’s code”** (hard constraint): this calls for version control with branch, merge, and conflict-detection semantics, not folders or file copies.

  * **“capture all updates in the latest version”** (hard constraint): it needs one authoritative integration line, which means the integrated repository itself must be the master.

  * **“Terraform templates that define your infrastructure”** (technical signal): infrastructure code should be handled with the same review-and-test discipline as application code.

  * **“two new engineers”** (technical signal): with several contributors, the integration process matters as much as the tool.

**Why This Is Correct**

Git gives every engineer an isolated working copy and records each change as a commit. Concurrent edits are reconciled through merges, and conflicting edits to the same lines are surfaced explicitly instead of silently replacing one another. Adding peer review and unit testing before integration means only reviewed, validated changes reach the shared line. Treating the fully integrated repository as the master means the latest version is by definition the sum of everything merged. No separate packaging step can drift out of sync with it. This matches Google’s guidance for Terraform on Google Cloud. Infrastructure code lives in version control, development happens on short-lived branches, changes return to a protected main branch through pull requests, and main represents the latest approved code.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best.** Git is the right tool, and the daily merge does give some integration cadence, so it is tempting. It loses on two points. Each developer merging their own work at the end of the day has no review or test gate, so untested infrastructure changes can enter the shared line. Packaging code into a bucket and declaring that upload the master creates a second source of truth that can lag behind or diverge from the repository.

**Option C — Violates Requirement.** A shared Drive folder offers no branching, merge, or conflict-detection mechanism. Renaming a folder to increment a version is a naming convention, not version control. It does nothing to stop two engineers from editing the same file at once and overwriting each other, which is the core requirement.

**Option D — Violates Requirement.** It has the same underlying weakness as C. A versioned bucket keeps older zip snapshots, but a daily snapshot of a shared folder cannot reconcile concurrent edits or show which change came from whom. It adds manual packaging steps without solving the overwrite problem.

**Exam Trap**

The strongest distractor is Option A, because both A and B use Git and it is easy to stop reading at “Git-based.” The resolving distinction is that the tool alone is not the answer. The process decides whether changes are reviewed and validated before integration, and whether the repository is the single source of truth. If Option A required reviewed, tested merges into a protected main branch, it would converge on Option B. Its bucket upload would still be an unnecessary second source of truth.

**Foundation Concept**

Version control exists to solve concurrent change. Each contributor works in isolation, integration happens through explicit merges, and the history is a complete, attributable record that supports rollback. Treating infrastructure as code means applying the same practices used for application code: review, automated validation, and one authoritative branch. Version control tracks the source code, and file storage or archive snapshots do not substitute for it.

**Real-World Connection**

In practice, the team hosts the Terraform repository on a Git host, such as GitHub, GitLab, or Secure Source Manager. They protect the main branch and require pull requests with at least one reviewer. A CI pipeline, for example in Cloud Build, runs validation and a plan on each pull request, so reviewers see the proposed infrastructure impact before merging. The result is fewer conflicting or untested changes reaching production, and every infrastructure change is auditable and reversible. A Cloud Storage bucket does appear in Terraform workflows, but as the remote location for Terraform state, not as the home of the source code.

**Memory Hook**

For shared Terraform code, use Git plus reviewed, tested merges into one authoritative main line. Folders and zip snapshots are not version control.

**30-Second Exam Takeaway**

When a question asks how several engineers can safely share and evolve infrastructure code without overwriting each other, choose Git-based version control with peer review and testing before integration, and treat the integrated repository as the single source of truth. Reject any option that relies on file shares, folder renaming, or manually packaged archives as the source of truth.

**Official References**

[**Google Cloud: Best practices for version control (Terraform for Google Cloud):**](https://cloud.google.com/docs/terraform/best-practices/version-control) Supports: the correct answer, covering infrastructure code in version control, a protected main branch as the latest approved code, branch-and-pull-request workflow, and Option A’s lack of review gating.

[**Google Cloud: Managing infrastructure as code with Terraform, Cloud Build, and GitOps:**](https://docs.cloud.google.com/solutions/managing-infrastructure-as-code) Supports: reviewing proposed infrastructure changes before merging, and the distinct role of a Cloud Storage bucket as Terraform state storage rather than source-code storage (Options A and D).

[Google Cloud: Professional Cloud DevOps Engineer exam guide (Section 1.2, Managing infrastructure): ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment with infrastructure-as-code tooling, GitOps, Terraform, and Google-recommended practices for making infrastructure changes.

---

## Question 24

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your team is designing a new application for deployment to Google Kubernetes Engine (GKE). You need to set up monitoring that collects and aggregates various application-level metrics in a centralized location, using Google Cloud services while keeping the setup effort to a minimum. What should you do?

- [ ] A. Publish the various metrics from the application directly to the Cloud Monitoring API, and then view these custom metrics in Cloud Monitoring.
- [ ] B. Install the Pub/Sub client libraries, push the various metrics from the application to Pub/Sub topics, and then view the aggregated metrics in Cloud Monitoring.
- [x] C. Install the OpenTelemetry client libraries in the application, configure Cloud Monitoring as the export destination for the metrics, and then view the application’s metrics in Cloud Monitoring.
- [ ] D. Emit all metrics as application-specific log messages, route these messages from the containers to the Cloud Logging collector, and then view the metrics in Cloud Monitoring.

### Explanation

**Correct Answer**

**C. Install the OpenTelemetry client libraries in the application, configure Cloud Monitoring as the export destination for the metrics, and then view the application’s metrics in Cloud Monitoring.**

**Exam Reasoning Explanation**

The two must-have requirements are centralization in a Google Cloud service and minimal setup effort. Each option needs to be judged on how much custom engineering it demands before metrics actually show up, aggregated, in a central place. Writing directly against the raw Cloud Monitoring API (Option A) means building and maintaining your own instrumentation, batching, and labeling logic by hand. Routing metrics through Pub/Sub (Option B) introduces a messaging layer with no built-in aggregation or metrics semantics, requiring a custom consumer to actually get the data into Monitoring. Emitting metrics as log lines and relying on log-based metrics (Option D) works for simple counters but is an indirect, limited path for richer metric types. OpenTelemetry is the one option that provides standardized instrumentation APIs plus a ready-made, officially supported exporter to Cloud Monitoring — meaning the “collect and centralize” work is handled by existing, maintained tooling rather than custom code.

**Key Exam Clues**

  * “collect and aggregate various application-level metrics in a centralized location” is a hard constraint — it requires both breadth of metric types and a single centralized destination, favoring a general-purpose instrumentation standard over narrow, single-purpose mechanisms.

  * “while minimizing the amount of work required to set up monitoring” is a hard constraint — it rules out any option requiring you to build custom plumbing (direct API calls, a Pub/Sub consumer, custom log-parsing rules) when an existing, maintained library and exporter already does the job.

  * “use Google Cloud Platform services” is a technical signal — it points toward an option with a direct, native integration into a GCP observability service, which the OpenTelemetry-to-Cloud-Monitoring exporter provides out of the box.

**Why This Is Correct**

OpenTelemetry provides a vendor-neutral, standardized set of client libraries for instrumenting an application’s metrics (counters, gauges, histograms, and more), and Google Cloud provides an officially supported exporter that sends that telemetry directly to Cloud Monitoring. Installing the OpenTelemetry libraries and configuring the Cloud Monitoring exporter means the application code only needs to call standard OpenTelemetry APIs to record metrics — all the work of formatting, batching, and shipping that data to a centralized Google Cloud service is handled by existing, maintained libraries rather than custom integration code, directly satisfying both the centralization and minimal-effort requirements.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** Publishing metrics directly to the Cloud Monitoring API does centralize the data in the right place, but it requires writing and maintaining custom code to construct time series, handle labels and resource types, manage batching, and deal with API quirks — considerably more setup effort than using an existing instrumentation library with a ready-made exporter.

  * **Option B — Different Use Case:** Pub/Sub is a messaging and event-delivery service, not a metrics aggregation or storage system — pushing metrics into Pub/Sub topics doesn’t by itself get them into Cloud Monitoring or aggregate them in any way. A separate consumer would still need to be built to read from Pub/Sub and write into Monitoring, which is strictly more work than instrumenting directly with a metrics-aware library.

  * **Option D — Technically Possible but Not Best:** Emitting metrics as log messages and relying on log-based metrics can work for simple event counts, but it’s an indirect path for anything beyond basic counters (histograms, gauges with multiple dimensions are awkward or impossible to represent cleanly this way), and it requires designing consistent log formats and filter expressions rather than using a purpose-built metrics API.

**Exam Trap**

The trap is treating Option A as the “most direct” answer because it names the Cloud Monitoring API explicitly — but direct API access isn’t the same as low-effort setup; it actually represents the most manual-integration-heavy path of the four. The real signal to follow is which option offloads the integration work to existing, maintained tooling (an instrumentation library with a built-in exporter) rather than which option sounds most literally tied to the target service.

**Foundation Concept**

When minimizing setup effort for application metrics is a stated goal, favor a standardized instrumentation library with a maintained, purpose-built exporter over hand-rolled API integration, a repurposed messaging system, or an indirect channel like log parsing — the library-plus-exporter pattern concentrates the integration complexity in code you don’t have to write or maintain yourself.

**Real-World Connection**

Teams instrumenting new GKE workloads commonly standardize on OpenTelemetry specifically because it decouples the application’s instrumentation code from any particular backend — the same OpenTelemetry-instrumented code can export to Cloud Monitoring today and, with only an exporter configuration change, to a different observability backend later, which is a meaningful advantage over metrics logic tightly coupled to one vendor’s raw API.

**Memory Hook**

For centralized application metrics with minimal setup, reach for a standardized instrumentation library with a built-in exporter (OpenTelemetry → Cloud Monitoring) — not a raw API integration, a messaging system, or log-based metrics.

**30-Second Exam Takeaway**

When a question asks for centralized application-level metrics in a Google Cloud service with minimal setup effort, favor OpenTelemetry (or another maintained instrumentation library) with its native exporter over direct API calls, messaging-system detours, or log-based metric extraction — those alternatives all shift integration work onto you that the instrumentation library already handles.

**Official References**

[**Google Cloud — Choose an approach to application instrumentation:**](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach) Supports: the correct-answer mechanism of using OpenTelemetry client libraries with Cloud Monitoring as the export destination for application metrics

[**Google Cloud — OpenTelemetry and Cloud Monitoring:**](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry) Supports: the native, officially supported integration between OpenTelemetry-instrumented applications and Cloud Monitoring as a centralized metrics destination

---

## Question 25

*Domain 3: Applying Site Reliability Engineering Practices*

You operate a high-traffic consumer web application built on a microservices architecture. The application’s home page assembles several independent widgets — for example, current weather conditions, live stock quotes, and breaking news headlines. For each widget, the request-handling thread calls a dedicated backend microservice and then renders the home page from the responses it collects. These backend microservices intermittently fail, and when that happens the home page is still served, but with one or more widgets missing. Your users tolerate an occasional missing widget and would rather see a partially populated page than no page at all, but satisfaction drops sharply if this partial-content condition becomes too frequent. You want to define a Service Level Indicator (SLI) that can support a Service Level Objective (SLO) for this experience. Which SLI should you select?

- [x] A. A quality SLI, calculated as the ratio of non-degraded responses to total responses.
- [ ] B. An availability SLI, calculated as the ratio of healthy microservices to the total number of microservices.
- [ ] C. A freshness SLI, calculated as the proportion of widgets refreshed within the preceding 10 minutes.
- [ ] D. A latency SLI, calculated as the ratio of microservice calls completing in under 100 ms to total microservice calls.

### Explanation

**Correct Answer**

**A. A quality SLI, calculated as the ratio of non-degraded responses to total responses.**

**Exam Reasoning Explanation**

Start from the hard requirement: the SLO must track user-perceived experience, specifically how often the home page is served in a degraded (partial-content) state. A quality SLI is purpose-built for exactly this: it measures the proportion of responses that are complete and correct versus those that are “good enough but downgraded.” Every other option measures a different layer of the system (infrastructure health, data staleness, or response speed), none of which directly capture “how often did the user see missing content.”

**Key Exam Clues**

  * “serves the homepage with some missing content” — a technical signal pointing to degraded-response measurement, not a binary up/down signal.

  * “users would rather have some content served instead of no content at all” — a preference clue ruling out a strict availability definition (success vs. failure), since the response is still technically “successful.”

  * “unhappy if this degraded mode occurs too frequently” — a cardinality/threshold clue: the SLO needs a metric that can quantify frequency of degradation, which is exactly what a quality SLI’s good/total ratio provides.

  * No mention of response time anywhere in the scenario — an exclusion clue against latency.

**Why This Is Correct**

A quality SLI is defined as the ratio of responses that meet the full, non-degraded bar to the total number of responses served. In this scenario, a “good” event is a home-page response where all widgets loaded successfully, and a “bad” (but still-served) event is a response where one or more widgets are missing. This directly operationalizes “degraded mode occurring too frequently” as a percentage, which is exactly what an SLO needs: a target like “99% of home-page loads should be non-degraded.”

**Why the Other Options Are Not the Best Fit**

**Option B — Possible but not best.** An availability SLI measured as “healthy microservices / total microservices” describes the health of backend infrastructure, not the experience of the end user viewing the home page. A single unhealthy weather microservice would disproportionately swing this ratio even though 99% of users might still get a fully populated page if that microservice recovers quickly, so it doesn’t correlate well with the thing users actually notice.

**Option C — Different use case.** Freshness SLIs measure whether data was updated recently enough (a data-processing/pipeline concern), not whether a request returned complete content. Even if every widget’s underlying data were perfectly fresh, a failed microservice call would still produce a degraded page, which freshness would never capture.

**Option D — Different use case.** A latency SLI measures how fast calls complete, not whether they succeeded or returned complete content. The scenario describes failures that produce missing content, not slow responses; a microservice could fail instantly (well under 100 ms) and still cause degradation, so latency would show “healthy” even during a degraded user experience.

**Exam Trap**

The strongest distractor is the availability SLI (Option B), because “microservices occasionally fail” sounds like a classic availability problem. The resolving distinction is that availability in SRE is normally scoped to the end-to-end user-facing request (the home-page response itself succeeded), not to the fleet of backend dependencies behind it. If the scenario instead asked you to track whether individual backend microservices were reachable for an internal health dashboard, Option B would become defensible.

**Foundation Concept**

In the SRE SLI taxonomy, request/response services are typically measured with three complementary SLI types: availability (did the request get a response at all), latency (was it fast enough), and quality (was the response complete/correct, as opposed to degraded). A system can be “available” while still being degraded — which is precisely why quality exists as its own SLI category rather than being folded into availability.

**Real-World Connection**

Choosing a quality SLI here means engineering teams get paged or review dashboards based on the rate of degraded home-page loads, not on transient individual-microservice blips. This keeps the error budget aligned with real user pain, avoids false alarms when a non-critical microservice has a brief hiccup that self-heals before affecting many users, and lets the team prioritize fixing whichever widget microservice contributes the most to degraded-response volume.

**Memory Hook**

If the system can still return “something” but it’s incomplete, measure it with a quality SLI, not an availability SLI.

**30-Second Exam Takeaway**

Whenever a question describes a service that returns a technically successful but incomplete or lower-fidelity response, reach for a quality SLI (good/total non-degraded ratio) rather than availability, latency, or freshness — those measure whether a response happened, how fast it was, or how current the data was, not whether the response itself was whole.

**Official References**

[**Google — The Site Reliability Workbook: Implementing SLOs (SLI menu, including the quality/degraded-response SLI type)**](https://sre.google/workbook/implementing-slos/) Supports: the correct-answer mechanism (quality SLI as the ratio of non-degraded to total responses)

[**Google Cloud — Concepts in service monitoring (definitions of availability SLI and latency SLI used to eliminate Options B and D)**](https://docs.cloud.google.com/monitoring/service-monitoring) Supports: option elimination for availability and latency SLI definitions

---

## Question 26

*Domain 3: Applying Site Reliability Engineering Practices*

You are running an experiment to determine whether users respond positively to a new feature in your web application. Soon after you release the feature as a canary, users begin receiving a spike in HTTP 500 errors, and your monitoring reports show higher latency. You want to reduce the impact on users as quickly as possible. What should you do FIRST?

- [x] A. Revert the experimental canary rollout.
- [ ] B. Begin tracking latency, traffic, errors, and saturation.
- [ ] C. Collect information for the incident’s postmortem document.
- [ ] D. Track down where the 500 errors originate and what is causing the latency increase.

### Explanation

**Correct Answer**

**A. Revert the experimental canary rollout.**

**Exam Reasoning Explanation**

The stem sets one governing constraint, which is to reduce user impact as quickly as possible, and one sequencing instruction, which is FIRST. A recent change, the canary, is the obvious suspect because the errors and latency appeared shortly after it shipped. Work backward from the constraint. Which action stops the harm fastest and with the least uncertainty? Reverting the canary removes the suspect change right away. Monitoring, evidence gathering, and diagnosis all leave users affected while they run. They are valid incident activities, but they are premature as the first step. The decision method is to mitigate first, then investigate and document.

**Key Exam Clues**

  * **“Shortly after deploying the feature as a canary release”** (technical signal): the timing correlates the degradation with a recent, easily reversible change.

  * **“spike in the number of 500 errors” and “increased latency”** (technical signal): users are being harmed right now, and monitoring has already detected the problem.

  * **“quickly minimize the negative impact on users”** (hard constraint): the priority is mitigation speed, not understanding.

  * **“first”** (sequence instruction): it asks for the opening action only, which must be the one that stops the impact.

**Why This Is Correct**

A canary release is designed to expose a new version to a small portion of traffic so problems can be caught early with limited impact. The standard response when that canary misbehaves is to roll it back, which restores the known-good version and removes the faulty change from the user path. Google’s SRE guidance on incidents follows the same pattern. Once a recent change is identified as the likely cause, reversing it is the fastest mitigation, and the rollback is the “undo button” for a progressive rollout. It does not require a diagnosis, and a rollback is low-risk because it returns the system to a state that was previously stable. Cloud Deploy’s canary strategy also supports rollback, so this mitigation is built into the tooling.

**Why the Other Options Are Not the Best Fit**

**Option B — Technically Possible but Not Best.** The four golden signals (latency, traffic, errors, and saturation) are sound monitoring practice, and it is tempting because the stem mentions latency and errors. It loses on two counts. Monitoring already detected the problem, so “begin” tracking adds little, and watching signals does nothing to stop users from receiving errors.

**Option C — Violates Requirement.** Postmortem data collection is a necessary follow-up activity, but it happens during or after mitigation, not instead of it. Doing it first prolongs the user impact, which directly conflicts with the requirement to reduce it quickly.

**Option D — Technically Possible but Not Best.** Root-cause investigation is valuable and will be needed, but it is slower and its outcome is uncertain. Users keep experiencing errors during that work. Because the canary can be rolled back without knowing the exact failing component, diagnosis is deferred until after mitigation.

**Exam Trap**

The strongest distractor is Option D, because engineers instinctively want to understand a failure before acting, and “find the root cause” sounds like the rigorous answer. The resolving distinction is that mitigation and root-cause analysis are separate tasks with separate priorities. Mitigation comes first, and the diagnosis can be done safely after the canary is out of the user path. If the rollback were not possible, for example because there was no previous version to return to, then targeted diagnosis or another mitigation such as shifting traffic would become the first step.

**Foundation Concept**

Incident response has a standard order: detect, mitigate, investigate, and then learn. Mitigation reduces or removes user impact using the fastest safe action, such as rolling back a recent change, redirecting traffic, or adding capacity. Root-cause analysis and postmortems come after impact has stopped. A mitigation does not need to explain the failure; it only needs to restore healthy service reliably. Progressive rollouts such as canaries exist precisely so that a rollback can limit the blast radius.

**Real-World Connection**

In practice, an on-call engineer who sees error and latency alerts correlated with a canary stage reverts the canary through the delivery tooling, for example by rolling back the rollout in Cloud Deploy or shifting traffic fully back to the stable revision. Error rate and latency return toward baseline, and the incident is contained within minutes. The team then preserves logs, metrics, and traces from the failed canary for diagnosis and records the timeline for a blameless postmortem. The cost of this approach is a delayed feature experiment, which is far cheaper than prolonged user-facing errors.

**Memory Hook**

Stop the bleeding before you study the wound: roll back the likely cause first, then diagnose and document.

**30-Second Exam Takeaway**

When a question describes user-facing degradation right after a recent release and asks what to do first, pick the fastest safe mitigation, usually a rollback. Monitoring, root-cause tracing, and postmortem notes are real work, but they come after impact is contained.

**Official References**

[**Google Cloud Blog: Incident management at Google, Adventures in SRE-land:**](https://cloud.google.com/blog/products/gcp/incident-management-at-google-adventures-in-sre-land) Supports: the correct answer, covering rollback as the SRE’s mitigation for a bad change in a progressive rollout and the principle of stopping impact before root-cause work (Options B, C, and D).

[Google Cloud: Use a canary deployment strategy (Cloud Deploy): ](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary)Supports: the canary release concept as a progressive rollout that limits user exposure, and rollback support within Cloud Deploy deployment strategies.

[**Google Cloud: Professional Cloud DevOps Engineer exam guide (Section 3.3, Mitigating incident impact on users):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with rollback strategies, draining or redirecting traffic, and adding capacity as incident-mitigation actions.

---

## Question 27

*Domain 3: Applying Site Reliability Engineering Practices*

You are the on-call engineer for an infrastructure service that many other systems depend on. An alert tells you the service is failing to serve most of its requests, and every dependent system, which together serve hundreds of thousands of users, is affected. Following your Site Reliability Engineering (SRE) incident management protocol, you declare yourself Incident Commander (IC) and bring in two experienced teammates as Operations Lead (OL) and Communications Lead (CL). What should you do next?

- [ ] A. Work out ways to reduce the impact on users and roll the mitigations out to production.
- [ ] B. Reach out to the owners of the affected services and give them a status update on the incident.
- [x] C. Set up a shared communication channel for the incident responders and leads to talk to one another.
- [ ] D. Open a postmortem document, record the incident details, share the draft internally, and request input from internal stakeholders.

### Explanation

**Correct Answer**

**C. Set up a shared communication channel for the incident responders and leads to talk to one another.**

**Exam Reasoning Explanation**

This is a sequencing question, so first identify what has already happened and who owns each remaining task. The IC has declared the incident and assigned the OL and CL, so the command structure exists. The remaining tasks belong to different roles: system changes belong to the OL, stakeholder updates belong to the CL, and the postmortem belongs to the aftermath. The IC’s own job is coordination, and coordination needs a shared place where the leads and responders can talk. That makes establishing the channel the IC’s next action, and it enables everything else.

**Key Exam Clues**

  * **“declare yourself Incident Commander ... Operations Lead ... Communications Lead”** (technical signal): the roles are already delegated, so the open item is enabling coordination, not doing the delegated work yourself.

  * **“What should you do next?”** (sequence instruction): the answer must be the step that follows role assignment, not a later-phase or delegated activity.

  * **“hundreds of thousands of users” and “all of its dependent systems”** (technical signal): this is a major incident that calls for structured command and a single coordination point, not ad hoc responses.

**Why This Is Correct**

Google’s incident management model separates duties. The IC leads, and the CL and OL report to the IC, whose job is to coordinate the response, communicate, and stay in control. For coordination to work, interested parties need to know where to interact with the IC, so a recognized command post, such as a war room, is part of the protocol. A shared channel or call is that command post. With it in place, the OL can report mitigation work, the CL can gather facts for updates, and the IC can make decisions from one source of truth. Without it, delegated work is scattered and conflicting changes become more likely.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best.** Mitigation is the right priority for the incident, so this is tempting. However, applying mitigations is the Operations Lead’s responsibility, and the IC delegates instead of working hands-on. The operations team should be the only group changing the system, and its work needs to be coordinated through the command post. If the IC dives into mitigation first, command and control are lost.

**Option B — Different Use Case.** Updating affected service owners is valuable, but it belongs to the Communications Lead. Doing it yourself defeats the point of having delegated that role, and the CL needs the coordination channel to obtain accurate information anyway.

**Option D — Violates Requirement.** A postmortem is a post-incident activity. The service is still failing for hundreds of thousands of users, so drafting and circulating a postmortem now is out of sequence and diverts attention from the response. Only a working record of events should be kept at this stage, so it is available later.

**Exam Trap**

The strongest distractor is Option A, because “stop the user impact first” is a core SRE principle and the stem describes a severe outage. The resolving distinction is that the principle governs what the response team does, while the IC’s role is to enable that response through delegation and coordination. If no OL had been assigned, the IC would absorb the undelegated roles by default, and then working on mitigation directly would become the right next step.

**Foundation Concept**

Structured incident management rests on three ideas: coordinate the response, communicate between responders, the organization, and the outside world, and keep control of the incident. A single leader assigns roles, and people in those roles work to the leader instead of freelancing. A recognized command post gives everyone one place to coordinate. The structure matters because unmanaged incidents suffer from unclear roles, uncoordinated changes, and poor communication, all of which prolong impact.

**Real-World Connection**

In practice, the IC opens a dedicated incident channel or call, invites the OL, the CL, and responders, and states who holds each role. The OL then runs mitigation, such as rolling back a recent change or redirecting traffic, and reports each action in the channel. The CL pulls verified status from the same place and updates affected service owners. Everything done in the channel also forms the record used later for the postmortem. The result is faster mitigation with fewer conflicting changes and clearer messages to dependent teams.

**Memory Hook**

The IC sets up the room, the OL fixes, the CL tells, and the postmortem comes last.

**30-Second Exam Takeaway**

When an IC has already declared an incident and assigned the OL and CL, the next step is to establish the shared command post or channel where the team coordinates. Mitigation belongs to the OL, outbound updates belong to the CL, and postmortems come after resolution, so reject options that have the IC doing those tasks or jump ahead of the response.

**Official References**

[**Google SRE Book: Chapter 14, Managing Incidents:**](https://sre.google/sre-book/managing-incidents/) Supports: the correct answer, covering the separation of incident roles, the operations team as the only group modifying the system, and the recognized command post where parties interact with the incident commander (Options A and B).

[**Google SRE Workbook: Chapter 9, Incident Response:**](https://sre.google/workbook/incident-response/) Supports: the IC, CL, and OL hierarchy, the IC delegating roles and assuming undelegated ones by default, and the principles of coordinating, communicating, and controlling an incident (the answer-switch condition in Exam Trap).

[**Google Cloud: Professional Cloud DevOps Engineer exam guide (Section 3, Applying site reliability engineering practices, including 3.3 Mitigating incident impact on users):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with SRE practices for managing and mitigating incidents.

---

## Question 28

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your VM utilization logs are currently stored in Cloud Logging. You need to provide an interactive, easy-to-share dashboard that updates in real time and presents the data aggregated by quarter. You want to use Google Cloud solutions. What should you do?

- [x] A.
    Route the VM utilization logs from Cloud Logging to BigQuery.
    Build a dashboard in Data Studio.
    Share the dashboard with your stakeholders.
- [ ] B.
    Route the VM utilization logs from Cloud Logging to Pub/Sub.
    Forward the logs from Pub/Sub to a Security Information and Event Management (SIEM) system.
    Build the dashboards in the SIEM system and share them with your stakeholders.
- [ ] C.
    Route the VM utilization logs from Cloud Logging to BigQuery.
    Export the logs from BigQuery to a CSV file.
    Import the CSV file into Google Sheets.
    Build a dashboard in Google Sheets and share it with your stakeholders.
- [ ] D.
    Route the VM utilization logs from Cloud Logging to a Cloud Storage bucket.
    Enable the Cloud Storage API so the logs can be pulled programmatically.
    Build a custom data visualization application.
    Display the pulled logs on a custom dashboard.

### Explanation

**Correct Answer**

**A. 1. Route the VM utilization logs from Cloud Logging to BigQuery. 2. Build a dashboard in Data Studio. 3. Share the dashboard with your stakeholders.**

**Exam Reasoning Explanation**

Separate the must-haves from the preference. The must-haves are an interactive, easily shared dashboard, a continuously updated data path, and quarterly aggregation over log data. The preference is to stay within Google Cloud solutions. Work through the pipeline: the logs need a destination that can aggregate large volumes by period, and the dashboard needs a tool that reads from that destination live and can be shared. BigQuery with Data Studio does both. Each other option breaks the chain somewhere. One uses a security system for a utilization dashboard, one takes a static snapshot, and one requires building a custom application.

**Key Exam Clues**

  * **“easy-to-share interactive ... dashboard”** (hard constraint): this calls for a visualization tool built for sharing reports, not a spreadsheet or a hand-built application.

  * **“updated in real time”** (hard constraint): the data path must stay live end to end, so a streaming log sink and a live connector fit and a one-time export does not.

  * **“aggregated on a quarterly basis”** (technical signal): this needs an analytical engine that can group large log volumes by period, which points to BigQuery.

  * **“use Google Cloud Platform solutions”** (preference): it favors native Google Cloud services over an external third-party system.

**Why This Is Correct**

Cloud Logging uses log sinks to route entries to supported destinations, including BigQuery. Sinks stream log data into BigQuery in small batches, and entries are typically visible there within about a minute, so the data stays near real time. Once in BigQuery, the logs can be aggregated by quarter with SQL, for example in a view that groups utilization by quarter. Data Studio connects directly to BigQuery as a data source, so the dashboard queries live data instead of a copy. It also lets you tune how fresh that data is, from every minute up to every few hours. Stakeholders can then be given access to the same interactive report, which satisfies the sharing requirement.

**Why the Other Options Are Not the Best Fit**

**Option B — Different Use Case.** Routing logs through Pub/Sub is designed for streaming to external or third-party systems, such as SIEM tools like Splunk. A SIEM targets security event analysis, so it is a heavy, tangential fit for a utilization dashboard. It also moves the logs off Google Cloud, which conflicts with the stated preference.

**Option C — Violates Requirement.** It starts correctly by routing logs to BigQuery, which makes it tempting. The CSV export then turns the data into a static snapshot, so the dashboard cannot update in real time. Google Sheets also refreshes connected data no more often than every 15 minutes, and the manual export and import steps make the process fragile.

**Option D — Technically Possible but Not Best.** Cloud Storage is intended for long-term archival of logs. New sinks to Cloud Storage can take hours to begin routing, and these sinks are processed hourly, so this path is poorly suited to real-time needs. A custom visualization application also has to be built, secured, and maintained. That is far more effort than a managed tool that already offers interactive, shareable dashboards.

**Exam Trap**

The strongest distractor is Option C, because it shares its first step with the correct answer and Google Sheets feels familiar for sharing. The resolving distinction is the CSV hop. It breaks the live connection between the logs and the dashboard, so it can only produce a snapshot. Option C would become defensible only if the stakeholders wanted a static, point-in-time quarterly report instead of a continuously updated dashboard.

**Foundation Concept**

Observability dashboards follow a standard pipeline: telemetry is collected, routed to an analytical store, and visualized through a tool that reads from that store. The routing destination should match the purpose. Analytics and aggregation go to BigQuery, archival goes to Cloud Storage, and streaming to external systems goes through Pub/Sub. Freshness depends on keeping every hop live, so any manual export or file hand-off turns a live pipeline into a snapshot.

**Real-World Connection**

In practice, you create a log sink with a filter for the relevant VM utilization logs and send it to a write-enabled BigQuery dataset. You then define a view or query that aggregates utilization by quarter and point a Data Studio data source at it. Data Studio’s default BigQuery refresh interval is several hours, so you would lower the data freshness setting to a few minutes to approach real time. The trade-off is that shorter refresh intervals mean more BigQuery queries, and the data freshness setting exists precisely to balance up-to-date data against cost and performance.

**Memory Hook**

Logs that must be queried, aggregated, and shown live go through a sink to BigQuery and then to a Data Studio dashboard, with no snapshot exports in between.

**30-Second Exam Takeaway**

When a question asks for an interactive, shareable, continuously updated dashboard over Cloud Logging data, route the logs to BigQuery and visualize them in Data Studio. Reject options that pass through a CSV file, a security-focused SIEM, or a custom-built application.

**Official References**

[**Google Cloud: Route logs to supported destinations (Cloud Logging):**](https://docs.cloud.google.com/logging/docs/install/logs_export) Supports: the correct answer’s routing step, and the elimination of Options B and D, covering BigQuery for analysis, Pub/Sub for third-party integrations such as Splunk, and Cloud Storage for long-term storage with hourly sink processing.

[**Google Cloud: View logs routed to BigQuery (Cloud Logging):**](https://docs.cloud.google.com/logging/docs/export/bigquery) Supports: the real-time requirement, covering log sinks that stream data into BigQuery in small batches with entries typically visible within one minute.

[**Google Cloud: Manage data freshness (Data Studio):**](https://docs.cloud.google.com/data-studio/manage-data-freshness) Supports: the live-dashboard requirement and the elimination of Option C, covering configurable BigQuery refresh intervals and the slower refresh rates of Google Sheets.

[**Google Cloud: Professional Cloud DevOps Engineer exam guide (Section 4.2, Managing and analyzing logs):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with exporting and retaining logs by routing to BigQuery, Pub/Sub, and Cloud Storage.

---

## Question 29

*Domain 3: Applying Site Reliability Engineering Practices*

Your organization follows SRE principles and practices. You are preparing to assume operational responsibility for a new service built by the Development Team, and you run a Production Readiness Review (PRR) as part of the handover. When the analysis phase ends, you conclude that the service, as it stands, cannot satisfy its Service Level Objectives (SLOs). You want to be confident the service can meet its SLOs once it is running in production. What should you do next?

- [ ] A. Lower the SLO targets to values the service can currently achieve so that it can go live.
- [ ] B. Inform the development team that they will need to provide ongoing production support for the service.
- [x] C. Determine the reliability improvements to recommend and have them completed before the handover.
- [ ] D. Launch the service in production without SLOs and define them later, once operational data has been gathered.

### Explanation

**Correct Answer**

**C. Determine the reliability improvements to recommend and have them completed before the handover.**

**Exam Reasoning Explanation**

Treat the requirement as fixed: the service must be able to meet its SLOs in production. The SLOs reflect what users need, and the PRR analysis shows the service falls short of them. That leaves the service as the thing to change. Requirement to capability to elimination gives a clear path. The only capability that closes the gap between the service and its SLOs is improving the service’s reliability. Lowering the target, dropping SLOs, or pushing support back to developers each leaves the service unchanged and the gap open. The correct next step is to turn the analysis findings into recommended improvements and complete them before the SRE team takes over.

**Key Exam Clues**

  * **“the service cannot currently meet its SLOs”** (technical signal): the PRR analysis has found a reliability gap, so the next phase is to fix the service, not to move forward as is.

  * **“ensure that the service can meet its SLOs in production”** (hard constraint): the SLOs stay fixed and the service must become capable of meeting them.

  * **“What should you do next?”** (sequence instruction): it follows the analysis phase of the PRR, which in the SRE engagement model leads into improvements and refactoring.

  * **“taking over the management of a new service”** (technical signal): SRE accepts responsibility only after the service is deemed ready, so improvements come before handover.

**Why This Is Correct**

A PRR is meant to verify that a service meets accepted standards of production setup and operational readiness, and to improve its reliability before the SRE team takes responsibility for it. After the analysis phase surfaces gaps, the next phase is improvements and refactoring. SRE identifies the changes needed, such as bug fixes, reliability and design changes, automation, and monitoring and alerting, and works with the development team to get them done. Only after sufficient improvements are made and the service is deemed ready does SRE assume production responsibilities. This directly serves the goal, because it makes the service capable of meeting the SLOs instead of changing what the SLOs say.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement.** Weakening the SLO targets to match current performance is tempting because it makes the gap disappear on paper. It does not make the service more reliable, and it disconnects the SLO from what users need. The requirement was to ensure the service can meet its SLOs, not to redefine them.

**Option B — Technically Possible but Not Best.** Having developers keep supporting the service is a legitimate outcome in some engagements, since SRE does not take on every service. It is not the next step after a failed analysis, though. It sets aside the SLO gap instead of resolving it, and it does not make the service able to meet its SLOs in production.

**Option D — Violates Requirement.** Launching with no SLOs removes the measure of success instead of improving the service. It gives up the reliability target the organization defined and exposes users to an unreliable service with no objective to hold it to. Collecting data is useful, but data collection does not itself raise reliability.

**Exam Trap**

The strongest distractor is Option B, because it sounds like a sensible SRE decision. SRE teams do decline to take on services that are not ready, and developer-led support is a recognized fallback. The resolving distinction is that the stem asks what to do to ensure the service meets its SLOs, which calls for improving the service, not deciding who runs it. Option B would become the better answer if the stem said the development team could not make the needed improvements and SRE had to decide on support responsibility.

**Foundation Concept**

An SRE engagement is gated by readiness. A review analyzes a service against production standards, and the findings drive concrete improvements. Support is handed over only after those improvements make the service ready. SLOs are a fixed expression of required reliability during this process, and the service is adjusted to meet them. They are revisited through the normal SLO review cycle, not rewritten to fit a service that falls short.

**Real-World Connection**

In practice, the SRE team writes up the findings from the analysis, such as missing monitoring, weak failure handling, or manual operational steps, as a prioritized list of improvements for the development team. The teams agree on which items must be finished before handover and which can follow afterward. Once those are done, the service is re-assessed and taken into production support. This costs development time up front but avoids launching a service that predictably exhausts its error budget and generates incidents and toil for the on-call team.

**Memory Hook**

When the service misses its SLOs, fix the service before handover; do not change the target, skip the target, or push the problem back.

**30-Second Exam Takeaway**

If a readiness review shows a service cannot meet its SLOs, the next step is to define and complete reliability improvements before SRE takes over. Reject options that weaken or remove the SLOs, or that sidestep the gap by shifting support responsibility.

**Official References**

[**Google SRE Book: Chapter 32, The Evolving SRE Engagement Model:**](https://sre.google/sre-book/evolving-sre-engagement-model/) Supports: the correct answer, covering PRR objectives, improvement before handover, and SRE assuming responsibility only after the service is deemed ready (Options A, B, and D).

[Google Cloud Blog: How SREs find the landmines in a service (CRE life lessons): ](https://cloud.google.com/blog/products/gcp/how-sres-find-the-landmines-in-a-service-cre-life-lessons)Supports: the SRE entrance review (PRR) identifying bug fixes, process changes, and needed service behavior before onboarding, and the four improvement axes of bugs, reliability, automation, and monitoring and alerting.

---

## Question 30

*Domain 5: Optimizing Performance and Cost*

You need to run a business-critical workload on a fixed set of Compute Engine instances for the next several months. The workload is stable, and the instances are provisioned with exactly the resources it needs. You want to reduce the cost of running this workload without affecting its performance. What should you do?

- [x] A. Buy committed use discounts for the instances.
- [ ] B. Move the instances into a managed instance group.
- [ ] C. Convert the instances to Spot VMs.
- [ ] D. Place the instances in an unmanaged instance group.

### Explanation

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

---

## Question 31

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

You are designing a strategy for monitoring your production Google Cloud projects with Cloud Monitoring metrics scopes. One requirement is to identify and respond to production issues quickly, without false alerts coming from development and staging projects. You also want to follow the principle of least privilege when you give the relevant team members access to the monitoring setup. What should you do?

- [ ] A. Give the relevant team members read access to every production project. Set up a separate metrics scope inside each project.
- [ ] B. Assign the relevant team members the Project Viewer IAM role on every production project. Set up a separate metrics scope inside each project.
- [ ] C. Select an existing production project to host the metrics scope. Add the production projects to this metrics scope. Give the relevant team members read access to the metrics scope.
- [x] D. Create a new Google Cloud project for monitoring and host a metrics scope in it. Add the production projects to this metrics scope. Give the relevant team members read access to the metrics scope.

### Explanation

**Correct Answer**

**D. Create a new Google Cloud project for monitoring and host a metrics scope in it. Add the production projects to this metrics scope. Give the relevant team members read access to the metrics scope.**

**Exam Reasoning Explanation**

Separate the requirements by what they force. Two are must-haves. Monitoring must show only production, so a single metrics scope should contain only the production projects, which also keeps development and staging out of alerting. Access must follow least privilege, so team members should receive read-level monitoring access, not broad roles on production projects. A third consideration shapes the best choice: where the scope is hosted. The decision path is as follows. A single production-only scope removes the per-project options. Of the two single-scope options, the one hosted in a dedicated monitoring project keeps monitoring configuration and access separate from production workloads, so it is the best fit.

**Key Exam Clues**

  * **“without false alerts from development and staging projects”** (hard constraint): the scope must list only production projects, because alerting policies query the projects in the metrics scope.

  * **“quickly identify and react to production environment issues”** (technical signal): this calls for one consolidated production view instead of checking each project separately.

  * **“principle of least privilege”** (hard constraint): grant only read-level monitoring access, at the place where monitoring is configured, not broad access to each production project.

  * **“relevant team members”** (technical signal): access should go to a defined group, scoped narrowly to what they need.

**Why This Is Correct**

A metrics scope lets one project, called the scoping project, chart and monitor time-series data stored in other projects. The scoping project also stores the alerting policies, dashboards, and uptime checks you create. Adding only the production projects to the scope gives a single production view and ensures alerts evaluate only production data. Access control follows the scoping project. A team member with the Monitoring Viewer role on the scoping project can view the time-series data of every project in the scope without needing any other permissions. That means no role on any production project is required, which is least privilege in practice. Google also recommends using a new project, or one without resources, as the scoping project when monitoring multiple projects. A dedicated project stores no time-series data of its own, so no filtering is needed to separate it from monitored data.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement.** Separate metrics scopes in each project leave production fragmented, so there is no single view for fast detection. Read access to every production project is also broader than monitoring needs, since the team only needs to see monitoring data.

**Option B — Violates Requirement.** It has the same fragmentation problem as Option A. The Project Viewer role is a broad basic role that grants read access across a project’s resources, which is far more than monitoring requires and contradicts least privilege.

**Option C — Technically Possible but Not Best.** It does provide a single production-only view and grants read access to the scope, which makes it tempting. However, it hosts the scope in a project that runs production resources. That mixes monitoring configuration with workloads, and the host project’s own time-series data must be filtered when you want to separate it from monitored data. Google’s recommended practice is a new or resource-free scoping project.

**Exam Trap**

The strongest distractor is Option C, because it differs from the correct answer only in where the scoping project lives. The resolving distinction is that a dedicated project cleanly separates monitoring from production workloads. Option C would become acceptable if an organizational policy prevented creating additional projects, but even then it would be a compromise, not the best design.

**Foundation Concept**

A metrics scope is a read-time construct. Metric data always stays in the project where it originates, and the scope only defines which projects a scoping project can query. Every project hosts a metrics scope by default, and metrics scopes are what Workspaces became in Cloud Monitoring. A scope can be shared by many viewers, but anyone viewing through the scoping project sees data from all projects in it. A permission granted on a scoping project can therefore reach the metrics of every monitored project, so scope membership should be designed deliberately.

**Real-World Connection**

An SRE organization creates a monitoring project, and an administrator adds the production projects to its metrics scope, which requires administrative rights on both the scoping project and each added project. Alerting policies and dashboards are created in that project, so they evaluate production data only. On-call engineers receive a read role on the monitoring project and see production health in one place, without gaining access to production workloads. Development teams can have their own separate scoping projects, which keeps the two audiences isolated from each other.

**Memory Hook**

For multi-project monitoring, use one dedicated scoping project that contains only the projects you want to watch, and grant viewer access on that project alone.

**30-Second Exam Takeaway**

When a question asks how to monitor several projects together under least privilege, choose a dedicated monitoring project whose metrics scope contains only the target projects, with read-only access granted on that project. Reject options that fragment the view across per-project scopes or hand out broad roles on the workload projects.

**Official References**

[**Google Cloud: Metrics scopes overview (Cloud Monitoring):**](https://docs.cloud.google.com/monitoring/settings) Supports: the correct answer, covering scoping and monitored projects, the Monitoring Viewer role on the scoping project as sufficient to view monitored data, and the recommendation to use a new or resource-free project as the scoping project (Options A, B, and C).

[**Google Cloud: Configure a metrics scope (Cloud Monitoring):**](https://docs.cloud.google.com/monitoring/settings/multiple-projects) Supports: adding projects to a metrics scope, the administrative role required to modify it, and read roles on the scoping project letting principals view data from projects in the scope.

[**Google Cloud Blog: Multi-project Cloud Monitoring made easier:**](https://cloud.google.com/blog/products/operations/multi-project-cloud-monitoring-made-easier/) Supports: the current terminology, covering Workspaces converted to metrics scopes and the scoping project concept.

[**Google Cloud: Professional Cloud DevOps Engineer exam guide (Section 1.1, Designing the overall resource hierarchy):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with multi-project monitoring and logging and IAM roles.

---

## Question 32

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

Your company is experiencing bugs, outages, and slowness in its production systems. Developers build new features and fix bugs directly in the production environment, and configuration changes and experiments are also carried out there, which causes outages for users. Testers run load tests in production as well, which frequently slows the production systems. You need to redesign the environment so that production has fewer bugs and outages and testers can load test new features. What should you do?

- [ ] A. Add an automated test script that runs in production to detect failures as soon as they occur.
- [ ] B. Build a development environment with reduced server capacity and restrict access to developers and testers.
- [ ] C. Lock down the production environment so developers cannot modify it, and set up a single controlled update each year.
- [x] D. Create a development environment for writing code and a test environment for configuration changes, experiments, and load testing.

### Explanation

**Correct Answer**

**D. Create a development environment for writing code and a test environment for configuration changes, experiments, and load testing.**

**Exam Reasoning Explanation**

List the causes the stem gives, then match each to the change that removes it. Development work, configuration changes, and experiments in production cause the bugs and outages. Load testing in production causes the slowness. The redesign must also give testers a place to load test new features. The decision method is to move each risky activity out of production and into an environment suited to it. Only the option that provides separate non-production environments for coding and for configuration, experiments, and load testing satisfies all of these. Options that only detect problems, share one thin environment, or freeze production each fail at least one requirement.

**Key Exam Clues**

  * **“Developers build new features and fix bugs directly in the production environment” and “configuration changes and experiments are also carried out there”** (technical signals): these activities are the root cause of the outages, so they must move out of production.

  * **“testers run load tests in production” and “enable testers to load test new features”** (hard constraint): testers need an environment of their own for load testing, so the solution cannot simply forbid changes.

  * **“reduce the number of bugs and outages in production”** (hard constraint): the fix must prevent problems from reaching production, not merely detect them after the fact.

**Why This Is Correct**

Separating environments isolates the blast radius of risky work. In a development environment, developers can write and break code without affecting users. In a test environment, configuration changes, experiments, and load tests run without competing with production traffic or slowing it down. Changes are promoted to production only after they have been exercised elsewhere, which cuts the bugs and outages that reach users. This also follows Google’s guidance on structuring environments, where development, testing, and production can carry different policies and access controls, with stricter controls in production.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best.** Automated tests or probes in production can detect failures quickly, and that has value. It is reactive, though, so users still experience every failure. It also leaves development, experiments, configuration changes, and load testing running in production, which are the causes of the problems.

**Option B — Technically Possible but Not Best.** Moving development out of production helps, which makes this tempting. But a single environment with reduced capacity has to serve coding, configuration experiments, and load tests together, so load tests would disturb developers. A smaller environment also produces load results that do not represent production capacity. The option does not say where configuration work and experiments should happen either.

**Option C — Violates Requirement.** Locking down production stops direct changes, but it gives developers and testers nowhere to work and offers testers no way to load test new features. A single update per year also bundles a year of changes into one release, which concentrates risk instead of reducing it.

**Exam Trap**

The strongest distractor is Option B, because it also moves development out of production and restricts access. The resolving distinction is that development and testing have different needs. Coding needs a place that can be broken freely, while load testing needs a production-like environment and must not interfere with other work. Option B would be adequate only if the stem asked solely to move development out of production, with no need for load testing or for rehearsing configuration changes.

**Foundation Concept**

Environment separation is a basic delivery practice. Development is where code changes quickly, test or staging is where changes are validated under conditions resembling production, and production is changed in a controlled way. Each environment can have its own access rules and policies, with the strictest controls in production. In Google Cloud, environments are commonly isolated using separate projects, often grouped under environment folders, so that IAM and organization policies can differ by environment. A test environment is most useful when it mirrors production closely enough for its results to carry over.

**Real-World Connection**

A team creates development, test (non-production), and production projects, grouped under environment folders in the organization. Developers have broad rights in development, narrower rights in test, and no direct changes in production. Changes reach production through a pipeline after passing tests, and load tests run in a test environment that resembles production. Outages from experiments and slowdowns from load tests disappear from production. The trade-off is the cost and upkeep of the extra environments, which can be reduced by creating test environments only when needed.

**Memory Hook**

Build in development, break things safely in test, and let only validated changes reach production.

**30-Second Exam Takeaway**

When a question describes development, experiments, or load tests disrupting production, the fix is to separate environments by purpose and keep production for validated changes. Reject options that only detect failures in production, squeeze all non-production work into one shared environment, or freeze production with no place to test.

**Official References**

[**Google Cloud: Decide a resource hierarchy for your Google Cloud landing zone:**](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy) Supports: the correct answer, covering hierarchies based on application environments such as development, production, and testing, with separate and stricter policies and access for production.

[**Google Cloud: Create and manage folders:**](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders) Supports: using folders to group projects by environment, such as development, production, and test, and to apply environment-specific policies.

[**Google Cloud: Enterprise foundations blueprint, organization structure:**](https://docs.cloud.google.com/architecture/blueprints/security-foundations/organization-structure) Supports: the foundation concept and Option B’s weakness, covering separate production, nonproduction, and development environments, with nonproduction holding a copy of production for testing workloads before promotion.

[**Google Cloud: Professional Cloud DevOps Engineer exam guide (Section 1.4, Managing multiple environments):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with managing multiple environments such as staging and production, including ephemeral environments and configuration and policy management.

---

## Question 33

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You support an application running on App Engine that is used worldwide and accessed from many different types of devices. You want to measure the number of connections, and you are using Cloud Monitoring for App Engine. Which metric should you use?

- [x] A. flex/connections/current
- [ ] B. tcp_ssl_proxy/new_connections
- [ ] C. tcp_ssl_proxy/open_connections
- [ ] D. flex/instance/connections/current

### Explanation

**Correct Answer**

**A. flex/connections/current**

**Exam Reasoning Explanation**

Work through three filters. First, the metric must come from App Engine, because the stem says you are using Cloud Monitoring for App Engine. Second, it must report the number of connections as a current count, not a rate of connections being created. Third, the stem describes the application as a whole, so the metric should describe the application and not a single instance. The first filter removes the load balancer metrics, and the third separates the two remaining App Engine candidates.

**Key Exam Clues**

  * **“Cloud Monitoring for App Engine”** (hard constraint): the metric must be an App Engine metric, which excludes metrics owned by other services such as Cloud Load Balancing.

  * **“the number of connections”** (technical signal): this calls for a current connection count (a gauge), not a count of newly created connections.

  * **“an application ... used globally and accessed from various device types”** (technical signal): the scope is the application overall, not one instance, so a version-level metric fits better than a per-instance metric.

**Why This Is Correct**

The metric appengine.googleapis.com/flex/connections/current reports the number of currently active connections per App Engine flexible environment version. It is recorded against the application-level monitored resource (gae_app), so it gives one figure for the application across its instances. That matches a question about how many connections the application is handling. The metric is a gauge, so it reflects connections open now, which is what “the number of connections” asks for.

**Why the Other Options Are Not the Best Fit**

**Option B — Different Use Case.** tcp_ssl_proxy/new_connections is a Cloud Load Balancing metric for TCP and SSL proxy load balancers, and it counts connections created. It therefore belongs to a different service and measures creations, not the current number of connections.

**Option C — Different Use Case.** tcp_ssl_proxy/open_connections reports the current number of outstanding connections through a TCP or SSL proxy load balancer. It is the right kind of measure, so it is tempting, but it describes the load balancer, not App Engine, and the question asks about App Engine metrics.

**Option D — Technically Possible but Not Best.** flex/instance/connections/current is an App Engine metric for current active connections, but it is reported per instance. Getting an application-level number from it means aggregating across instances. It fits only when you need to see how connections are spread across individual instances.

**Exam Trap**

The strongest distractor is Option D, because its name differs from the correct answer only by the word “instance,” and both metrics appear with the display name “Connections” in the metric reference. The resolving distinction is scope: the metric without “instance” is version-level, and the one with it is instance-level. Option D would become correct if the question asked which instance is carrying the most connections or how load is distributed across instances.

**Foundation Concept**

A Google Cloud metric type has the form of a service domain followed by a metric path, and the service domain tells you which product emits the metric. Choosing the right metric means matching three things: the owning service, the kind of measurement, and the level it is recorded at. A gauge describes the current state, whereas a count of new events is a different measurement. A metric recorded at the application or version level is a different series from one recorded per instance, even when the names are similar. The flex/ prefix in the metric path marks metrics of App Engine’s flexible environment.

**Real-World Connection**

In Metrics Explorer, you pick the App Engine application resource and the connections metric, then group or filter by version to chart connection counts over time. You can place that chart on a dashboard or base an alerting policy on sustained high values. If the aggregate looks unhealthy, you then switch to the instance-level metric to see whether load is concentrated on specific instances. Starting from the aggregate keeps the first view simple and uses the finer-grained metric only for drill-down.

**Memory Hook**

Match the service, then the measure, then the scope: App Engine, current count, whole application.

**30-Second Exam Takeaway**

When asked which monitoring metric to use, first match the metric’s service domain to the product in the stem, then check whether it is a current count or a rate, and finally match its scope to the question. Reject load balancer metrics for App Engine questions, and prefer the version-level metric over its per-instance twin when the question concerns the application as a whole.

**Official References**

[**Google Cloud: Google Cloud metrics, A or B (Cloud Monitoring):**](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b) Supports: the correct answer and Option D, covering the App Engine metric types, including the version-level and instance-level flexible environment connection metrics.

[**Google Cloud: Google Cloud metrics, I to O (Cloud Monitoring):**](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o) Supports: the elimination of Options B and C, covering Cloud Load Balancing, including its TCP and SSL proxy metrics, as metrics owned by a different service domain.

[**Google Cloud: Google Cloud metrics overview (Cloud Monitoring):**](https://docs.cloud.google.com/monitoring/api/metrics_gcp) Supports: the foundation concept, covering the metric type format and the service domain identifying which product emits a metric.

[**Google Cloud: Professional Cloud DevOps Engineer exam guide (Section 4.3, Managing metrics, dashboards, and alerts):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with collecting metrics from platforms and analyzing metrics using the Metrics Explorer.

---

## Question 34

*Domain 3: Applying Site Reliability Engineering Practices*

You support a multi-region web service that runs on Google Kubernetes Engine (GKE) behind a global external Application Load Balancer. For legacy reasons, user requests first pass through a third-party Content Delivery Network (CDN), which then forwards traffic to the load balancer. You have already implemented an availability Service Level Indicator (SLI) at the load balancer. You now want broader coverage so that a load balancer misconfiguration, a CDN failure, or another global networking catastrophe would also be detected. Where should you measure this new SLI? (Choose two.)

- [ ] A. In your application servers’ logs.
- [x] B. Through instrumentation built directly into the client.
- [ ] C. In metrics exported from your application servers.
- [ ] D. Through GKE health checks on your application servers.
- [x] E. Using a synthetic client that periodically sends simulated user requests.

### Explanation

**Correct Answer**

**B. Through instrumentation built directly into the client.**

**E. Using a synthetic client that periodically sends simulated user requests.**

**Exam Reasoning Explanation**

The decisive constraint is where the new SLI sits in the request path. The failure modes named in the question are a CDN failure, a load balancer misconfiguration, and a global networking catastrophe. All of them happen before a request reaches the application tier, and the existing SLI at the load balancer cannot see the CDN hop at all. Any new measurement point at or behind the load balancer repeats the same blind spot. Only a vantage point outside Google Cloud, at the user’s edge of the path, can observe the whole chain. That leaves two candidates: real client-side telemetry, and a synthetic client that sends probe requests along the same public path. They are complementary rather than redundant. One reports what real users experience, and the other probes on a schedule even when real traffic is low.

**Key Exam Clues**

  * “load balancer misconfiguration, CDN failure, or other global networking catastrophe” is a hard constraint. It names failures upstream of the application tier, so the measurement point has to sit upstream too.

  * “requests first pass through a third-party CDN” is a technical signal. It shows the CDN hop lies outside your infrastructure and outside the current load balancer SLI, so only an external vantage point can observe it.

  * “already implemented... at the load balancer” together with “increase coverage” is an exclusion signal. A new SLI measured at or behind that point adds no coverage for the named failure modes.

  * “Choose two” is a cardinality instruction. It points to two complementary external vantage points, not two variations of a downstream signal.

**Why This Is Correct**

Client-side instrumentation records the outcome of each request from the user’s own device. If the CDN is down or the load balancer is misconfigured, the client records the failure directly, even though no server ever saw the request. A synthetic client sends simulated user requests on a schedule across the full public path (CDN, then load balancer, then GKE). It detects an outage even during quiet traffic periods and gives a consistent, controlled signal that does not depend on real users encountering the problem first. Used together, they give a real-user view and a proactive view of the same end-to-end path, which together cover the failure modes that no server-side signal can reveal.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Application server logs only record requests that actually arrived. In a CDN failure or load balancer misconfiguration, requests never reach the servers, so the logs stay quiet during exactly the outages in question. It is tempting because logs are detailed, but the detail is irrelevant when the failure happens upstream.

  * **Option C — Violates Requirement:** Metrics exported from application servers share the same blind spot. They reflect only traffic that reached the application, so they would look healthy during a CDN or load balancer failure. They are tempting as a richer signal than logs, but they sit behind the failure points.

  * **Option D — Violates Requirement:** GKE health checks assess whether pods and nodes are healthy inside the cluster. They have no visibility into the third-party CDN or the load balancer’s configuration, so a global networking failure upstream would not change their results. They are tempting because they sound like availability measurement, but they measure the cluster, not the user’s path.

**Exam Trap**

The trap is assuming that any additional availability signal increases coverage. Options A, C, and D are all real, useful signals, but each sits at or behind the same point in the request path as the load balancer SLI, so none extends visibility upstream. The test is whether the measurement point lies upstream of the failure modes named in the stem, not whether the signal is a different type. If the question had asked about detecting application-level errors for requests that did reach the servers, the server-side options would become strong candidates.

**Foundation Concept**

An SLI is only as trustworthy as its vantage point. A signal measured downstream of a failure point cannot detect failures upstream of it, however detailed it is. SRE practice therefore recommends measuring as close to the user’s experience as practical. For paths that include infrastructure you do not control, such as a third-party CDN, this means measuring from outside your own infrastructure through real client telemetry and external synthetic probing.

**Real-World Connection**

A team that puts a third-party CDN in front of its own load balancer can pair client-side reporting of request outcomes with external synthetic checks that traverse the full public path. During a CDN outage, server dashboards, logs, and cluster health checks all stay green, while the client telemetry and the synthetic probes flag the failure within minutes. This lets the team declare the incident and engage the CDN vendor sooner, and it keeps the reported availability SLI honest.

**Memory Hook**

To catch failures upstream of your infrastructure, measure from upstream of your infrastructure: real client telemetry plus external synthetic probes.

**30-Second Exam Takeaway**

When a question asks how to extend SLI coverage to failures in a CDN, a load balancer, or global networking, look for measurement points outside your own infrastructure, meaning client-side instrumentation and synthetic probing. Eliminate server logs, server metrics, and cluster health checks, because they share the blind spot of the SLI you already have.

**Official References**

[**Google SRE Workbook — Implementing SLOs:**](https://sre.google/workbook/implementing-slos/) Supports: the principle that SLIs should be measured as close to the user’s experience as practical, and the trade-offs of each measurement point (server-side logs and metrics, load balancer, client-side instrumentation, synthetic probing)

[**Google Cloud — Uptime checks:**](https://cloud.google.com/monitoring/uptime-checks) Supports: the correct-answer mechanism of using an external synthetic client to probe the full public request path

---

## Question 35

*Domain 2: Building and Implementing CI/CD Pipelines*

Your application images are built with Cloud Build and pushed to Artifact Registry. You want to be able to choose a specific version of your application to deploy, based on the release version tagged in source control. What should you do when you push the image?

- [ ] A. Record the image digest in the source control tag.
- [x] B. Pass the source control tag as a parameter in the image name.
- [ ] C. Have Cloud Build embed the release version tag in the application image.
- [ ] D. Use Artifact Registry digest versioning to match the image to the source control tag.

### Explanation

**Correct Answer**

**B. Pass the source control tag as a parameter in the image name.**

**Exam Reasoning Explanation**

Start from the deployment side. To deploy “a particular version,” the deployment must be able to name that version in the image reference it uses. The version comes from the source control tag, so that tag has to become part of the image reference at the moment the image is pushed. The push step is where the reference is set, which makes it the only place the link can be created. Test each option against one question: after the push, can I select the image by the Git release tag alone? Only an image published under that tag in its name can be selected that way.

**Key Exam Clues**

  * **“specify a particular version of your application for deployment”** (hard constraint): the image must be addressable by a version identifier at deployment time.

  * **“based on the release version tagged in source control”** (hard constraint): the identifier must come from the Git tag, so that value has to appear in the image reference.

  * **“when you push the image”** (sequence instruction): the action must happen at push time, which is when the image’s name and tag are assigned.

**Why This Is Correct**

A container image is referenced by name plus either a tag or a digest. Image tags are the common human-readable way to refer to different revisions, and Google’s guidance describes tagging images with a version identifier at build time as a common approach. Cloud Build supports this directly. For builds invoked by a trigger, the default substitution $TAG_NAME holds the name of the Git tag, and you can use it in the image name in the build config, so the pushed image carries the release version. For a manual build, you can supply the same value through the substitutions flag. Deployment can then reference the image by that tag, and redeploying an earlier release means pointing back to its tag.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best**. This runs in the wrong direction. A digest is computed by the registry from the image content, so it is only known after the push, and writing it back into source control adds a post-build step. It also sets nothing on the pushed image, so you would have to look up the digest from the Git tag before every deployment instead of simply deploying the tagged image.

**Option C — Technically Possible but Not Best.** Embedding the version inside the image, for example as a label or a file, helps identify what is running. Deployment still resolves an image through its registry reference, so embedded content does not let you select a version. The image must still be pushed under a tag for that to work.

**Option D — Incorrect.** A digest is a content-derived hash, not a versioning scheme you can configure to match a Git tag. There is no digest versioning feature that maps an image to a source control tag.

**Exam Trap**

The strongest distractors are the digest-based options, because digests are immutable and tags are mutable, so deploying by digest is often the better practice for guaranteeing exact content. The resolving distinction is that this question asks how to select a version by its Git release tag, and a digest cannot carry or be matched to that tag. The answer would shift if the requirement were to guarantee the exact bytes deployed even if a tag were later reassigned. In that case you would deploy by digest, ideally in addition to tagging.

**Foundation Concept**

An image has three identifiers. The name locates the repository, a tag is a mutable human-readable pointer to a revision, and the digest is an immutable hash of the content. Tagging at build time with the source control version ties an artifact to the code that produced it, which supports traceability and straightforward rollbacks. Tags can be moved to new images, so strict reproducibility requires resolving to a digest. Google Container Registry has been superseded by Artifact Registry, which also hosts images for the gcr.io domain through gcr.io repositories.

**Real-World Connection**

A team creates a release tag such as v1.4.0 in Git, which fires a Cloud Build trigger on tags. The build config builds the image and pushes it to an Artifact Registry repository under a name ending in the tag value, using the $TAG_NAME substitution. Deployment manifests or a delivery pipeline then reference that exact tag, so promoting or rolling back is a matter of choosing a release tag. The trade-off is that tags can be reassigned, so teams that need stronger guarantees also record or deploy the resulting digest.

**Memory Hook**

Push the image under the release tag in its name, because tags select versions and digests only identify content.

**30-Second Exam Takeaway**

When a question asks how to deploy a specific version identified by a source control tag, tag the image with that release version in its name at push time. Reject digest-based options as the way to match a Git tag, and reject options that bury the version inside the image, since neither makes the version selectable by reference.

**Official References**

[Google Cloud: Substituting variable values (Cloud Build): ](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values)Supports: the correct answer, covering the default $TAG_NAME substitution holding the Git tag name for triggered builds, and using substitutions in image names pushed to Artifact Registry.

[**Google Cloud: About container image digests:**](https://docs.cloud.google.com/architecture/using-container-images) Supports: the option distinctions, covering tagging images with a version identifier at build time, tags as mutable references, and digests as immutable content hashes (Options A and D).

[**Google Cloud: Transition from Container Registry (Artifact Registry):**](https://docs.cloud.google.com/artifact-registry/docs/transition/transition-from-gcr) Supports: the current terminology, covering Artifact Registry as the recommended successor to Container Registry and its support for the gcr.io domain through gcr.io repositories.

[**Google Cloud: Professional Cloud DevOps Engineer exam guide (Section 2.1, Designing pipelines):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with CI/CD of applications and artifact management with Artifact Registry.

---

## Question 36

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You support an application running on Compute Engine that uses a Cloud SQL instance to store and retrieve data. Following an update to the application, users report errors containing database timeout messages. The number of concurrent active users has not changed. You need to determine the MOST probable cause of the database timeouts. What should you do?

- [ ] A. Examine the serial port logs of the Compute Engine instance.
- [ ] B. Use Cloud Profiler to visualize resource utilization across the application.
- [x] C. Check whether the number of connections to the Cloud SQL instance has increased.
- [ ] D. Use Web Security Scanner to determine whether the Cloud SQL instance is under a Distributed Denial of Service (DDoS) attack.

### Explanation

**Correct Answer**

**C. Check whether the number of connections to the Cloud SQL instance has increased.**

**Exam Reasoning Explanation**

Build the diagnosis from the evidence. The symptom is database timeouts, the trigger is an application update, and the user load is unchanged. With load constant, the most probable cause is a change in how the application uses the database. The next question is which database resource an application consumes per request and can exhaust. That resource is connections. So check the signal closest to the symptom, the connection count on the Cloud SQL instance. The other options inspect different layers, such as the VM’s operating system, code-level CPU and memory, or web vulnerabilities, and none of them speaks to the database boundary where the timeouts occur.

**Key Exam Clues**

  * **“Following an update to the application”** (technical signal): the problem began with a change, which points to the application’s new behavior as the trigger.

  * **“The number of concurrent active users has not changed”** (exclusion): this rules out load growth and also makes an external attack an unlikely explanation.

  * **“database timeout messages”** (technical signal): the failure sits on the path between the application and the database, which makes connection availability a prime suspect.

  * **“MOST probable cause”** (decision word): choose the check best supported by the evidence, not merely a possible one.

**Why This Is Correct**

Every database connection consumes client-side and server-side resources, and Cloud SQL imposes overall connection limits that cannot be exceeded. An application update can change connection behavior, for example by opening a new connection per request, leaking connections, or enlarging connection pools across instances. That can push the instance toward its limit even though the number of users is the same. Requests then wait for a connection or fail, which users see as timeouts. Comparing the instance’s connection count before and after the update directly confirms or rules out this cause. Google’s guidance is that creating and using fewer connections reduces overhead and helps you stay under the limit.

**Why the Other Options Are Not the Best Fit**

**Option A — Different Use Case.** Serial port output captures operating system, BIOS, and other system-level messages and is useful for crashes, failed boots, and startup or shutdown problems. Here the VM is running and serving users, and the error is at the database layer, so these logs are unlikely to explain the timeouts.

**Option B — Technically Possible but Not Best.** Cloud Profiler continuously gathers CPU usage and memory-allocation information and attributes it to code. It could expose an inefficient code path, which makes it tempting after an update. It does not show how many connections the application holds against Cloud SQL, so it is less likely to reveal the cause of connection-related timeouts.

**Option D — Incorrect.** Web Security Scanner scans web applications for vulnerabilities such as cross-site scripting and outdated libraries, so it cannot tell you whether a DDoS attack is underway. A stable user count and onset right after an application update also point away from an attack.

**Exam Trap**

The strongest distractor is Option B, because profiling tools sound like the natural answer to a performance problem after a deployment. The resolving distinction is where each tool looks. A profiler measures resource use inside the application process, whereas the symptom appears at the database boundary, where connection exhaustion cannot be seen from a CPU or memory profile. Option B would become the better first step if the symptom were high CPU on the application VM or slow responses without any database error.

**Foundation Concept**

Effective troubleshooting correlates a change with a symptom and then inspects the metric nearest to that symptom. A database connection limit is a finite shared resource, and many concurrent application instances multiply whatever each one holds. A constant user count does not mean constant connection usage, since connection handling is application behavior and can change independently of load. Each diagnostic tool answers a different question: profilers cover code-level CPU and memory, serial output covers VM system behavior, vulnerability scanners cover security flaws, and database connection metrics cover the application-to-database path.

**Real-World Connection**

In practice, you open the Cloud SQL instance’s monitoring and compare connection counts before and after the release. If counts climbed, you review how the new code obtains and releases connections and how large each pool is relative to the number of application instances. Typical fixes include closing connections reliably, right-sizing pools, and using connection pooling. A rollback is the fastest mitigation if impact is severe. The cost of skipping this check is chasing code or infrastructure suspects while users keep hitting the limit.

**Memory Hook**

When the load stays flat but database timeouts appear after a release, check connections first.

**30-Second Exam Takeaway**

When a question describes database timeouts that begin after an application change with unchanged user load, look for what the change did to the application’s database usage, and connection count is the classic answer. Match each tool to its layer, and reject profilers, VM boot logs, and security scanners for a connection-level symptom.

**Official References**

[**Google Cloud: Manage database connections (Cloud SQL):**](https://cloud.google.com/sql/docs/mysql/manage-connections) Supports: the correct answer, covering the resources each connection consumes, Cloud SQL’s connection limits that cannot be exceeded, and using fewer connections to stay under the limit.

[**Google Cloud: Cloud Profiler overview:**](https://docs.cloud.google.com/profiler/docs/about-profiler) Supports: the elimination of Option B, covering Cloud Profiler as a low-overhead profiler for CPU usage and memory allocation in production applications.

[**Google Cloud: Overview of Web Security Scanner (Security Command Center):**](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview) Supports: the elimination of Option D, covering Web Security Scanner as a scanner for web application vulnerabilities such as cross-site scripting and outdated libraries.

[**Google Cloud: Viewing serial port output (Compute Engine):**](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output) Supports: the elimination of Option A, covering serial port output as system-level output for troubleshooting crashes, failed boots, and startup or shutdown issues.

[Google Cloud: Professional Cloud DevOps Engineer exam guide (Section 4.5, Troubleshooting issues): ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment with troubleshooting application, infrastructure, and performance and latency issues.

---

## Question 37

*Domain 3: Applying Site Reliability Engineering Practices*

Your application runs across three Google Cloud zones, and its users are split among them. You can fail over from one zone to another, but doing so interrupts service for 10 minutes for the affected users. A database failure occurs about once every quarter, and your monitoring detects it within five minutes. You are documenting the reliability risks of a planned real-time messaging feature. For each risk, you record Mean Time to Detect (MTTD) in minutes, Mean Time to Repair (MTTR) in minutes, Mean Time Between Failures (MTBF) in days, and the percentage of users impacted. The messaging feature relies on a new database system whose zonal failover takes twice as long to complete successfully. You need to capture the risk of this new database failing in a single zone. Which set of values should you record for the new database failover risk?

- [ ] A. MTTD: 5 minutes, MTTR: 10 minutes, MTBF: 90 days, User impact: 33%
- [x] B. MTTD: 5 minutes, MTTR: 20 minutes, MTBF: 90 days, User impact: 33%
- [ ] C. MTTD: 5 minutes, MTTR: 10 minutes, MTBF: 90 days, User impact: 50%
- [ ] D. MTTD: 5 minutes, MTTR: 20 minutes, MTBF: 90 days, User impact: 50%

### Explanation

**Correct Answer**

**B. MTTD: 5 minutes, MTTR: 20 minutes, MTBF: 90 days, User impact: 33%**

**Exam Reasoning Explanation**

Start by separating what the scenario states from what it changes. The detection time, failure frequency, and zone layout are stated as facts about the existing setup. The only thing the new system changes is how long failover takes. Test each of the four fields against that change. Detection time depends on monitoring, not on failover, so it stays at 5. Failure frequency has no stated change, so the quarterly cadence carries over. Repair time is the failover duration, so it doubles. User impact depends on how many users sit in the failing zone, which the zone layout fixes. Only the repair time and the layout-derived impact need calculating, and the result leaves one option.

**Key Exam Clues**

  * **“Twice as long to successfully fail over”** is a technical signal. It scales only the repair component, taking MTTR from 10 to 20 minutes.

  * **“Once per quarter”** is a technical signal. A quarter is about 90 days, so MTBF is 90.

  * **“Detect it within five minutes”** is a hard constraint. MTTD stays at 5 because nothing about the new database changes detection.

  * **“Three zones” with “users divided between the zones”** is a hard constraint. One zone failing affects one of three equal groups, about 33%.

  * **“Failing in one zone”** is a scoping instruction. It limits the impact to a single zone’s share of users, not all users.

**Why This Is Correct**

In a reliability risk catalog, each risk is described by how long it takes to detect, how long it takes to repair, how often it occurs, and what share of users it affects. For a database failure handled by zonal failover, repair is the failover itself. The current failover takes 10 minutes, so a system that takes twice as long gives an MTTR of 20 minutes. Detection is unchanged at 5 minutes, and failures are assumed to keep their quarterly cadence of roughly 90 days. Users are split across three zones, so a single-zone failure affects about one third of them, or 33%. Option B is the only one with all four values consistent with this reasoning.

**Why the Other Options Are Not the Best Fit**

**Option A — Incorrect:** It keeps MTTR at 10 minutes, which is the old system’s failover time. It is tempting because the other three values are right, but it ignores the stated doubling of failover time.

**Option C — Incorrect:** It makes two errors. It leaves MTTR at 10 minutes and sets impact to 50%. The 50% figure fits a two-zone split, not the three zones in the scenario, which makes it a tempting but wrong calculation.

**Option D — Violates Requirement:** It gets MTTR right at 20 minutes but sets impact to 50%. With users divided across three zones, one zone’s failure affects about 33% of them. The 50% figure ignores the stated zone count.

**Exam Trap**

The strongest distractor is option D, because it gets the doubled repair time right and fails only on the impact percentage. The distinction is that impact is a function of how many zones users are divided across, not of how severe the outage is. The answer would switch to D only if the product were deployed across two zones instead of three. A second trap is assuming that a slower failover also changes detection time or failure frequency, which it does not.

**Foundation Concept**

A reliability risk can be scored by how long it takes to detect, how long it takes to repair, how often it recurs, and what share of users it hurts. Together, these determine the expected user-facing unavailability the risk contributes. For a failure with a fixed recovery procedure, the recovery procedure’s duration sets repair time, and the failure’s blast radius sets impact. This model applies when failures are independent and users are evenly distributed. If users were unevenly distributed across zones, the impact would be the affected zone’s actual share, not a simple equal split.

**Real-World Connection**

Suppose your team adds a database with a slower failover. Recording MTTR as 20 minutes instead of 10 doubles the expected downtime each time that failure occurs. Over a quarterly failure cycle, that can push the feature’s expected unavailability past its availability target. This lets you decide, before launch, whether to invest in faster failover, add zones to shrink per-zone impact, or negotiate a looser objective for the feature.

**Memory Hook**

Detection and frequency come from the existing setup, repair time comes from the failover duration, and impact is one divided by the number of zones.

**30-Second Exam Takeaway**

When a risk-catalog question changes one property, change only the field it drives and leave the rest alone. For zonal failover, repair time equals failover duration and impact equals one over the number of zones.

**Official References**

[Google SRE Workbook — Implementing SLOs (risk catalog with time to detect, time to repair, time between failures, and impact): ](https://sre.google/workbook/implementing-slos/)Supports: how detection time, repair time, failure frequency, and user impact are combined to evaluate reliability risks, which is the basis for the correct values and for rejecting the other options.

[**Google SRE Book — Embracing Risk:**](https://sre.google/sre-book/embracing-risk) Supports: the underlying principle that reliability risk is weighed by the expected impact and duration of failures against availability targets.

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 3, Applying site reliability engineering practices):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with balancing change, velocity, and reliability, and with mitigating incident impact on users.

---

## Question 38

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You support an e-commerce application that runs on a large Google Kubernetes Engine (GKE) cluster deployed both on-premises and on Google Cloud. The application consists of microservices running in containers. You want to identify the containers that consume the most CPU and memory. What should you do?

- [x] A. Use Cloud Monitoring’s Kubernetes Engine monitoring.
- [ ] B. Use Prometheus to gather and aggregate per-container logs, then analyze the results in Grafana.
- [ ] C. Use the Cloud Monitoring API to create custom metrics, then organize the containers into groups.
- [ ] D. Use Cloud Logging to export application logs to BigQuery, aggregate the logs per container, and then analyze CPU and memory consumption.

### Explanation

**Correct Answer**

**A. Use Cloud Monitoring’s Kubernetes Engine monitoring.**

**Exam Reasoning Explanation**

Separate what the task needs from how it could be built. The task needs per-container CPU and memory consumption, and it must work across both on-premises and Google Cloud deployments. CPU and memory consumption are numeric measurements over time, so they are metrics, not log content. The decision path is therefore to look for a solution that already produces container-level resource metrics for Kubernetes in both locations. If one exists as a built-in capability, it beats any option that requires building a collection pipeline. The options built on logs or custom instrumentation each require extra work to approximate what built-in Kubernetes monitoring already provides.

**Key Exam Clues**

  * **“identify the containers that consume the most CPU and memory”** (hard constraint): the solution must expose per-container resource utilization that can be compared across containers.

  * **“deployed both on-premises and on Google Cloud”** (technical signal): the monitoring must cover both locations, so a solution that works across them with little extra setup fits best.

  * **“CPU and memory”** (technical signal): these are resource metrics, which makes log-based approaches indirect.

**Why This Is Correct**

By default, GKE clusters send system metrics to Cloud Monitoring, and those system metrics describe low-level resources such as CPU, memory, and storage for containers, pods, and nodes. Google Distributed Cloud clusters, the on-premises counterpart, are also configured by default to monitor system and container metrics in Cloud Monitoring. Its predefined dashboards chart container CPU usage and memory usage per container. That gives one place to rank containers by consumption across both environments, with no pipeline to build. Google also does not charge for ingesting GKE system metrics, which lowers the cost of this approach.

**Why the Other Options Are Not the Best Fit**

**Option B — Incorrect.** Prometheus is a systems monitoring and alerting toolkit that collects and stores metrics as time series, not logs. The option misdescribes what Prometheus does. Even if reworded to collect metrics, you would be deploying and operating your own Prometheus and Grafana stack across both environments, when built-in monitoring already provides the metrics.

**Option C — Technically Possible but Not Best.** Custom metrics are meant for measurements Cloud Monitoring does not already collect, and container CPU and memory are already available as system metrics. Groups help organize resources for viewing, but they do not rank containers by consumption, so this adds work without adding capability.

**Option D — Technically Possible but Not Best.** Application logs record events and messages, not measurements of resource usage. CPU and memory consumption would appear in them only if the application logged those figures itself. Exporting logs to BigQuery and aggregating them per container would be a heavy, indirect substitute for metrics that already exist.

**Exam Trap**

The strongest distractor is Option B, because Prometheus with Grafana is the well-known Kubernetes monitoring stack and it feels like the natural answer. The resolving distinction is that the option says Prometheus collects logs, which it does not, and that it requires operating a separate stack to get data Cloud Monitoring already provides. Option B would become reasonable if the requirement were to use open-source tooling or to collect application-specific custom metrics, and Google Cloud Managed Service for Prometheus can feed such metrics into Cloud Monitoring.

**Foundation Concept**

Observability data comes in three kinds: metrics, logs, and traces. Resource consumption is a metric, meaning a numeric measurement recorded over time, whereas logs record discrete events. The preferred approach is to use built-in managed telemetry first and add custom collection only for gaps. Terminology has also changed. The Stackdriver brand was replaced by Google Cloud’s operations suite, and its monitoring product is now Cloud Monitoring, with GKE integration documented as observability for GKE. Cloud Monitoring can show Kubernetes metrics from both GKE and on-premises clusters in one place.

**Real-World Connection**

An SRE team opens the Kubernetes dashboards in Cloud Monitoring, charts per-container CPU and memory usage, and sorts or groups by container, namespace, or cluster to find the heaviest consumers. They then use those findings to right-size container requests and limits and to set alerts on utilization approaching limits. The built-in system metrics add no ingestion charge on GKE, while additional collection, such as application or Prometheus metrics, is charged by samples. This avoids the operational burden of running and scaling a separate monitoring stack in two environments.

**Memory Hook**

Resource usage is a metric, so use the built-in Kubernetes metrics in Cloud Monitoring before building logs or custom pipelines.

**30-Second Exam Takeaway**

When asked how to find which containers use the most CPU and memory in GKE, including hybrid deployments, use Cloud Monitoring’s built-in Kubernetes metrics. Reject logs-based answers, since logs are events and not resource measurements, and reject custom-metric or self-managed stack answers when the built-in metrics already cover the need.

**Official References**

[**Google Cloud: Observability for GKE:**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/observability) Supports: the correct answer, covering GKE sending system metrics to Cloud Monitoring and logs to Cloud Logging by default, and Managed Service for Prometheus as an option for user-defined metrics (Options B and C).

[Google Cloud: Configure metrics collection (GKE): ](https://docs.cloud.google.com/monitoring/kubernetes-engine/installing)Supports: GKE system metrics covering low-level resources such as CPU, memory, and storage, being sent to Cloud Monitoring, and no charge for their ingestion.

[**Google Cloud: Use predefined dashboards (Google Distributed Cloud clusters):**](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/reference/predefined-dashboards) Supports: the on-premises coverage, covering predefined dashboards that chart container CPU usage and memory usage per container for Google Distributed Cloud clusters in Cloud Monitoring.

[Prometheus: Overview: ](https://prometheus.io/docs/introduction/overview/)Supports: the elimination of Option B, covering Prometheus as a monitoring and alerting toolkit that collects and stores metrics as time series data.

---

## Question 39

*Domain 2: Building and Implementing CI/CD Pipelines*

You manage production deployments to a set of Google Kubernetes Engine (GKE) clusters. You want to ensure that only images successfully built by your trusted CI/CD pipeline can be deployed to production. What should you do?

- [ ] A. Turn on Web Security Scanner for the clusters.
- [ ] B. Turn on Artifact Analysis vulnerability scanning in Artifact Registry.
- [ ] C. Configure the GKE clusters as private clusters.
- [x] D. Configure the GKE clusters with Binary Authorization.

### Explanation

**Correct Answer**

**D. Configure the GKE clusters with Binary Authorization.**

**Exam Reasoning Explanation**

Start from what the requirement demands. It has two parts: the control must establish where an image came from, specifically that your trusted pipeline built it successfully, and it must enforce that fact at deployment by blocking anything that cannot show it. A control that only detects problems, or that only restricts network access, does not tie an image to its build origin or block a deployment. The decision method is to ask of each option whether it records provenance at build time and checks it at deploy time. Only one of the four does both.

**Key Exam Clues**

  * **“only images successfully built by your trusted CI/CD pipeline”** (hard constraint): the control must verify an image’s build origin, not just its contents.

  * **“can be deployed to production”** (hard constraint): enforcement must happen at deployment, which means blocking, not reporting.

  * **“a set of Google Kubernetes Engine (GKE) clusters”** (technical signal): the control must apply on the cluster deployment path, where images are admitted.

**Why This Is Correct**

Binary Authorization is a deploy-time security control that ensures only trusted container images are deployed on GKE. It works by enforcing a policy, and one common policy requires signed attestations. An attestor signs an image after your pipeline builds it, and at deploy time the admission check verifies the attestation, so unsigned images are blocked. Cloud Build integrates directly. When a build produces images, Cloud Build automatically creates the built-by-cloud-build attestor in your project and, once the images are successfully built, signs and creates attestations for them. A production policy that requires that attestation therefore admits only images your pipeline built successfully. That matches the requirement precisely.

**Why the Other Options Are Not the Best Fit**

**Option A — Different Use Case.** Web Security Scanner crawls deployed web applications to identify vulnerabilities such as cross-site scripting and outdated libraries. It evaluates running applications, not the origin of the images, and it cannot stop an image from being deployed.

**Option B — Technically Possible but Not Best.** Artifact Analysis scans images in Artifact Registry for known vulnerabilities and can feed results into a delivery process, so it is tempting as an image trust control. Scanning alone does not show that your pipeline built the image, and it does not block a deployment. It becomes useful here only as an input to an attestation policy.

**Option C — Different Use Case.** Private clusters use nodes with only internal IP addresses, isolating them from the public internet and limiting control plane access. That is a network isolation control. It says nothing about which images are admitted to run on the nodes.

**Exam Trap**

The strongest distractor is Option B, because vulnerability scanning sounds like image trust. The resolving distinction is that scanning finds known vulnerabilities in an image’s contents, whereas the requirement concerns provenance and enforcement. Option B would become part of the answer if the requirement were to block images with serious vulnerabilities. In that case a scan result would be turned into an attestation, and Binary Authorization would require it at deploy time.

**Foundation Concept**

Software supply chain security rests on two steps: produce evidence about an artifact where it is built, and verify that evidence where it is deployed. Evidence takes the form of a signed attestation tied to a specific image, and verification is an admission check that allows or denies the workload. Detection tools and network controls complement this but do not replace it. Policies can also be introduced gradually, for example by first auditing violations before enforcing, and they typically include a break-glass path for emergencies.

**Real-World Connection**

A team builds images in Cloud Build and pushes them to Artifact Registry, and each successful build is automatically attested by the built-by-cloud-build attestor. They then enable Binary Authorization on the production GKE clusters with a policy requiring that attestation, usually trialing it in an audit mode first to see which deployments would have been blocked. An image pushed by hand or built outside the pipeline is rejected at admission. The result is a verifiable chain from source to production, at the cost of maintaining the policy and attestors and planning for emergency exceptions.

**Memory Hook**

Sign at build and verify at deploy: Binary Authorization admits only images with a trusted attestation.

**30-Second Exam Takeaway**

When a question asks to ensure that only images from a trusted pipeline run in GKE, choose Binary Authorization with attestations. Reject vulnerability scanners and network isolation, since scanners report on contents and private clusters restrict network access, and neither enforces build provenance at deployment.

**Official References**

[**Google Cloud: Gating Deployments with Binary Authorization (codelab):**](https://codelabs.developers.google.com/gating-deployments-with-binary-auth) Supports: the correct answer, covering policies requiring signed attestations at deploy time, and Cloud Build automatically creating the built-by-cloud-build attestor and signing attestations for successfully built images.

[**Google Cloud: Artifact Analysis and vulnerability scanning:**](https://docs.cloud.google.com/artifact-registry/docs/analysis) Supports: the elimination of Option B and the current terminology, covering Artifact Analysis (formerly Container Analysis) scanning images automatically when they are pushed to Artifact Registry.

[**Google Cloud: About private clusters (GKE):**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept) Supports: the elimination of Option C, covering private clusters as nodes with only internal IP addresses that are isolated from the public internet.

[**Google Cloud: Overview of Web Security Scanner (Security Command Center):**](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview) Supports: the elimination of Option A, covering Web Security Scanner as a vulnerability scanner for web applications on App Engine, GKE, and Compute Engine.

---

## Question 40

*Domain 3: Applying Site Reliability Engineering Practices*

You are carrying out a semi-annual capacity planning review for your primary service. You anticipate user growth of 10% month over month for the next six months. The service is fully containerized and runs on a Google Kubernetes Engine (GKE) Standard regional cluster spread across three zones, with the cluster autoscaler enabled. The service currently uses about 30% of its total provisioned CPU capacity, and it must stay resilient if a single zone fails. You want users to see minimal negative impact from either the growth or a zone failure, without paying for capacity you do not need. How should you prepare for the projected growth?

- [x] A. Confirm the maximum node pool size, enable a Horizontal Pod Autoscaler, and then run a load test to validate the expected resource requirements.
- [ ] B. Rely on the cluster autoscaler, since a GKE cluster with it enabled scales automatically regardless of the growth rate.
- [ ] C. Take no capacity action, since 30% utilization leaves ample headroom for this rate of growth.
- [ ] D. Add 60% more node capacity up front to cover six months of 10% growth, and then run a load test to confirm the capacity is sufficient.

### Explanation

**Correct Answer**

**A. Confirm the maximum node pool size, enable a Horizontal Pod Autoscaler, and then run a load test to validate the expected resource requirements.**

**Exam Reasoning Explanation**

Separate the must-haves from the preference. The must-haves are surviving a zone failure and keeping user impact minimal as load grows. The preference is avoiding unnecessary cost. Start with the arithmetic. Growth of 10% per month compounds to 1.1^6, about 1.77 times current load, so 30% utilization becomes about 53% of today’s capacity. If one of three zones fails, only two thirds of capacity remains, so that load would run at about 80% utilization. That is workable but not roomy, so headroom is not guaranteed and must be validated. This points away from doing nothing and away from guessing a fixed number. The remaining decision is between trusting automation blindly and configuring and testing it.

**Key Exam Clues**

  * **“10% month-over-month for six months”** is a technical signal. It compounds to about 77% growth, not 60%.

  * **“Regional cluster on three zones” and “resilience against the failure of a zone”** is a hard constraint. After a zone loss only two thirds of capacity remains, so planned utilization must be judged against that reduced capacity.

  * **“Cluster autoscaler enabled”** is a technical signal. Nodes are added only within configured limits and only when pods cannot be scheduled.

  * **“Minimal negative impact” while “avoiding unnecessary costs”** is a hard constraint paired with a preference. Capacity should be elastic and validated, not over-provisioned in advance.

**Why This Is Correct**

The cluster autoscaler adds nodes only when pods are pending because no node has room, and it stops at the node pool maximum, so you must confirm that maximum covers peak demand including a zone failure. For a regional cluster, node limits can apply per zone or across zones depending on how they are set, which is worth checking. Pod counts must also rise with load, and a Horizontal Pod Autoscaler does that by scaling replicas on observed utilization, which in turn creates the pending pods the cluster autoscaler responds to. A load test then checks that the expected resource needs, including the reduced capacity during a zone loss, are met. Together these steps keep capacity elastic, which avoids paying for idle nodes while protecting users.

**Why the Other Options Are Not the Best Fit**

**Option B — Incorrect:** It is tempting because the cluster autoscaler does add nodes automatically. The claim fails because it only reacts to unschedulable pods, so it cannot scale if pod counts do not grow, and it cannot exceed the configured maximum node pool size. Quotas can also limit it. Saying it works regardless of growth rate is false.

**Option C — Violates Requirement:** It is tempting because 30% looks low. It ignores both compounding growth and the zone-failure requirement. Load reaches about 53% of current capacity, and a zone loss leaves roughly 80% utilization, so calling this significant headroom is not supported and nothing is validated.

**Option D — Technically Possible but Not Best:** Adding capacity and load testing could keep users safe. It loses on two points. The 60% figure comes from adding 10% six times, which understates compounding growth of about 77%. It also pays for six months of unused capacity now, which conflicts with avoiding unnecessary costs when autoscaling can add it only as needed.

**Exam Trap**

The strongest distractor is option B, because enabling the cluster autoscaler feels like it settles capacity. The distinction is that the autoscaler is bounded by configured limits and driven by pending pods, so it needs the maximum checked and pod autoscaling in place. The answer would shift toward option D only if demand were sudden and unforecastable enough that scale-up delay could hurt users, which is not the case with a steady, predicted growth rate. Another trap is the simple-interest error in option D: six months at 10% is not 60%.

**Foundation Concept**

Capacity planning combines forecast demand, a failure-tolerance requirement, and elasticity. Growth rates compound, so forecasts multiply rather than add. Resilience to losing one of N zones means usable capacity is reduced to N minus 1 over N of the total, and headroom must be judged against that reduced capacity. Autoscaling should be layered, with pod-level scaling creating demand for node-level scaling, and both bounded by limits that must be checked. Load testing turns assumptions into evidence. This model works for steady growth. Spiky or bursty demand needs additional buffer because scale-up takes time.

**Real-World Connection**

A team confirms the node pool maximum covers about 1.8 times current load with one zone down, enables a Horizontal Pod Autoscaler on the main workloads, and runs a load test with a simulated zone loss. The result is that nodes are added gradually as users grow, with cost tracking real demand. The load test surfaces any gap, such as a quota or a limit that is too low, before users feel it rather than during an outage.

**Memory Hook**

Compound the growth, judge headroom against capacity after losing a zone, and pair pod autoscaling with node limits and a load test.

**30-Second Exam Takeaway**

When a capacity question combines growth, zone resilience, and cost, choose elastic autoscaling with verified limits and a load test. Reject answers that assume automation has no limits, ignore failure capacity, or provision everything up front.

**Official References**

[**Google Cloud — GKE cluster autoscaler:**](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) Supports: the autoscaler adding nodes only for unschedulable pods and staying within configured node pool limits, which rules out option B and supports checking the maximum in option A.

[**Google Cloud — GKE Horizontal Pod Autoscaler:**](https://cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) Supports: scaling replica counts based on observed utilization, which is the pod-level scaling that drives node scaling in option A.

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 3, Applying site reliability engineering practices):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with managing the service lifecycle, including capacity planning and autoscaling.

---

## Question 41

*Domain 5: Optimizing Performance and Cost*

You are responsible for the backend of a mobile game that runs on a Google Kubernetes Engine (GKE) cluster, and the application serves HTTP requests from players. You need to put a solution in place that lowers the network cost. What should you do?

- [ ] A. Set up the VPC network as a Shared VPC host project.
- [x] B. Set up your network services to use the Standard Network Service Tier.
- [ ] C. Set up your Kubernetes cluster as a private cluster.
- [ ] D. Set up an external Application Load Balancer as the Ingress.

### Explanation

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

---

## Question 42

*Domain 2: Building and Implementing CI/CD Pipelines*

You release a new version of an internal application during a weekend maintenance window, when user traffic is minimal. After the window closes, you discover that one of the new features does not work as expected in production. The outage lasts a long time before you roll back the release and deploy a fix. You want to change your release process to shorten the mean time to recovery (MTTR) so that future outages are not prolonged. What should you do? (Choose two.)

- [ ] A. Require two separate peers to review code changes before they are merged.
- [x] B. Adopt a blue/green deployment strategy when releasing new code through a continuous delivery (CD) server.
- [ ] C. Add a code linting tool that checks coding standards before any code is accepted into the repository.
- [ ] D. Require developers to run automated integration tests in their local development environments before a release.
- [x] E. Set up a continuous integration (CI) server, add a unit test suite to the code, and have the CI server run the tests on every commit to verify changes.

### Explanation

**Correct Answer**

**B. Adopt a blue/green deployment strategy when releasing new code through a continuous delivery (CD) server.**

**E. Set up a continuous integration (CI) server, add a unit test suite to the code, and have the CI server run the tests on every commit to verify changes.**

**Exam Reasoning Explanation**

Separate the must-have from the framing. The goal is a shorter recovery time after a bad release, and the incident shows two weaknesses: the broken feature reached production, and getting back to a good state took too long. Choose one action for each weakness. For fast recovery, you need a release mechanism that makes returning to the previous version quick and low-risk. For fast detection and repair, you need automated, enforced feedback on every change so defects surface early and a fix can ship through a trusted pipeline. Then eliminate options that improve code hygiene or rely on unenforced manual steps without affecting recovery. Two options remain.

**Key Exam Clues**

  * **“Reduce the mean time to recovery”** is a hard constraint. The chosen actions must shorten recovery, not only prevent problems.

  * **“After an extended outage, you roll back ... and deploy a fix”** is a technical signal. Both rolling back and redeploying took too long, so the release mechanism and the verification of fixes are the targets.

  * **“Choose two”** is a cardinality instruction. Select exactly two options, ideally covering different parts of the problem.

  * **“Release process”** is a scope signal. The change should live in the delivery pipeline, not in individual habits or style rules.

**Why This Is Correct**

Option B addresses recovery directly. In a blue/green deployment, two identical environments exist, and the new version is deployed to the idle one while the current one keeps serving users. Traffic moves to the new version only when it is ready, and if a problem appears, traffic switches back to the previous environment almost instantly. This turns an extended rollback into a quick switch, which is the largest cut to MTTR. Option E strengthens the other half. A CI server that runs unit tests on every commit gives immediate, automated, consistent feedback, so regressions are caught close to where they were introduced. It also verifies a fix quickly and reliably before it is released. The two options work together: E reduces how often bad changes reach production and speeds up fixes, while B limits how long users are affected when one does. They are independent controls, and together they cover both prevention and recovery.

**Why the Other Options Are Not the Best Fit**

**Option A — Different Use Case:** Requiring two peer reviewers improves code quality and shares knowledge. It is tempting because reviews catch defects. It happens before merging, depends on human attention, and does nothing to speed up rollback or fix verification, and it can slow delivery.

**Option C — Different Use Case:** A linting tool enforces style and standards. It is tempting because it is automated and runs before acceptance. It does not detect functional defects such as a feature that fails in production, and it has no effect on recovery speed.

**Option D — Technically Possible but Not Best:** Automated integration tests are valuable, so the idea is sound. It loses because running them in local environments is left to individual developers, is not enforced centrally, and may differ from the production setup. It is also not part of the release mechanism, so it does not make recovery faster the way a pipeline-level control does.

**Exam Trap**

The strongest distractor is option D, because automated integration tests sound more thorough than unit tests. The distinction is where and how they run: tests that depend on each developer’s local environment are inconsistent and unenforced, while a CI server runs them the same way on every commit. The answer would shift toward integration testing only if the option said they run automatically in the pipeline against a production-like environment. A second trap is treating quality gates such as peer review and linting as recovery measures. They are preventive and do not shorten recovery.

**Foundation Concept**

Mean time to recovery improves when you can detect problems fast and restore service fast. Detection improves with automated testing and monitoring, and restoration improves with deployment strategies that make reverting cheap, such as blue/green, canary, or traffic splitting. Prevention reduces how often failures happen, but it does not substitute for recovery speed. Blue/green has costs, including running two environments and handling data or schema compatibility, so it fits best when instant rollback matters more than the duplicated capacity.

**Real-World Connection**

A team routes releases through a pipeline that builds, runs unit tests on each commit, deploys to the idle environment, and only then shifts traffic. When a broken feature appears, an operator shifts traffic back within minutes, and the team fixes the defect with a new commit that passes the same automated tests before redeploying. The result is a short disruption instead of an extended outage, at the cost of keeping a second environment available during releases.

**Memory Hook**

To recover faster, make rollback a traffic switch and make every change pass automated tests before it ships.

**30-Second Exam Takeaway**

For MTTR questions, pick one option that makes reverting instant, such as blue/green, and one that gives automated, enforced feedback, such as CI tests. Reject style rules, peer review, and unenforced local testing, which do not change recovery speed.

**Official References**

[Google Cloud Architecture Center — Application deployment and testing strategies: ](https://cloud.google.com/architecture/application-deployment-and-testing-strategies)Supports: blue/green deployment keeping the previous environment available and allowing a quick switch back, which supports option B.

[**Google Cloud Architecture Center — DevOps capabilities (DORA), including continuous integration, test automation, and continuous delivery:**](https://docs.cloud.google.com/architecture/devops) Supports: running automated tests on each commit through a CI process as a practice that speeds feedback and release reliability, which supports option E.

[Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 2, Building and implementing CI/CD pipelines): ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment with deployment strategies such as blue/green and with troubleshooting and mitigating deployment issues.

---

## Question 43

*Domain 2: Building and Implementing CI/CD Pipelines*

Your team builds application container images and pushes them to Artifact Registry. You need an automated pipeline that deploys the application each time a new image is published, and you want to keep the development effort as low as possible. What should you do?

- [ ] A. Configure Cloud Build to start a Spinnaker pipeline.
- [x] B. Configure Cloud Pub/Sub to start a Spinnaker pipeline.
- [ ] C. Configure a custom builder in Cloud Build to start a Jenkins pipeline.
- [ ] D. Configure Cloud Pub/Sub to start a custom deployment service running on Google Kubernetes Engine (GKE).

### Explanation

**Correct Answer**

**B. Configure Cloud Pub/Sub to start a Spinnaker pipeline.**

**Exam Reasoning Explanation**

Separate the must-have from the preference. The must-have is that the trigger is the image update itself, not a source commit or a manual step. The preference is minimal development effort, which favors managed, built-in integrations over anything custom. Work through it as requirement, capability, elimination, decision. The registry already emits an event when an image changes, so you need something that listens to that event, and Spinnaker can start a pipeline directly from a Pub/Sub subscription. That path needs configuration but no new code. Each remaining option adds a build step, a custom builder, or a service you would have to write and run.

**Key Exam Clues**

  * **“Deploys the application when the image is updated”** is a hard constraint. The trigger must be the image publish event, not a code change.

  * **“Minimizing the development effort”** is a preference that works as a tiebreaker. It rules out anything requiring custom code or a custom service.

  * **“Images are built and pushed to the registry”** is a technical signal. The image already exists when the pipeline starts, so a build step is unnecessary for triggering.

  * **“Automated pipeline”** is a technical signal. It points to an event-driven trigger rather than a manual or polling approach.

**Why This Is Correct**

Artifact Registry publishes messages to a Pub/Sub topic named gcr whenever an image is uploaded, tagged, or deleted. Spinnaker supports a Pub/Sub trigger type that subscribes to a Google Pub/Sub subscription and starts a pipeline when a message arrives. Its Google Pub/Sub integration documents registry-originated messages as a supported source. Connecting the two is a configuration task: create a subscription on the topic, enable Google Pub/Sub in Spinnaker, and add a Pub/Sub trigger to the pipeline. The image reference in the message can be used as the artifact to deploy. No custom code is needed, which is why it is the lowest-effort fit. One boundary matters: the topic delivers all registry events, so the pipeline should constrain the trigger to the push events and image it cares about.

**Why the Other Options Are Not the Best Fit**

**Option A — Different Use Case:** Cloud Build starts builds from source events such as commits or tags, and Spinnaker can react to Cloud Build results. That chain is tied to a build happening, not to an image appearing in the registry. It is tempting because Cloud Build is a natural place to produce the image, but it would miss images pushed by other means. It also adds a build dependency the requirement does not call for.

**Option C — Technically Possible but Not Best:** A custom builder in Cloud Build can call Jenkins, so the outcome is achievable. It is tempting because Jenkins is a well-known deployment tool. It loses on effort, because it requires writing and maintaining a custom builder, running a Jenkins server, and still has no direct link to the image update event.

**Option D — Violates Requirement:** Pub/Sub is the right trigger source, and that makes this option look close. However, writing, hosting, securing, and operating your own deployment service on GKE is the highest-effort path. It directly conflicts with minimizing development effort when an existing tool can consume the same event.

**Exam Trap**

The strongest distractor is option A, because Cloud Build feels like the natural pipeline entry point when images are built there. The distinction is that the requirement is event-driven on the image update, not on a source change. The answer would shift toward Cloud Build only if the requirement were to deploy on every source commit. A second trap is option D, which uses the correct Pub/Sub event but ignores the effort constraint. A terminology note: Container Registry has been superseded by Artifact Registry, and Artifact Registry publishes to the same gcr topic, so the Pub/Sub approach is unchanged. Google’s native managed continuous delivery service is Cloud Deploy, but it is not offered here, so the best choice among the given options is B.

**Foundation Concept**

Event-driven pipelines start from a signal that something changed, not from polling or a manual step. A registry publishes change events to a message bus, and a deployment system subscribes to that bus and acts on it. Using a deployment tool’s built-in trigger for that event beats writing glue code, because the integration is already tested and maintained. The pattern holds whenever the source of the change can publish events. It weakens when you need to filter heavily or enforce ordering and approvals, which the deployment tool must then handle.

**Real-World Connection**

A team creates a subscription on the registry’s topic and adds a Pub/Sub trigger to a Spinnaker pipeline with a constraint on the image name. Every new tagged image then starts a deployment with no code to maintain. The operational result is a short, auditable path from image publish to rollout, and the main ongoing cost is managing Spinnaker itself rather than custom services. Because the topic carries all registry events, the team also adds payload filtering so tag deletions do not start deployments.

**Memory Hook**

Image changed in the registry means a Pub/Sub event, and the least-effort consumer is the deployment tool’s built-in Pub/Sub trigger.

**30-Second Exam Takeaway**

When a deployment must start from an artifact update and effort must be minimal, pick the managed event source feeding the tool’s native trigger. Reject options that add build steps, custom builders, or self-written services.

**Official References**

[Google Cloud — Artifact Registry: Configure Pub/Sub notifications: ](https://docs.cloud.google.com/artifact-registry/docs/configure-notifications)Supports: the registry publishing image upload and tag events to the gcr topic, and that Artifact Registry uses the same topic as Container Registry, which makes the Pub/Sub trigger valid for option B.

[**Spinnaker — Google Cloud Pub/Sub triggers:**](https://spinnaker.io/docs/setup/other_config/triggers/google/) Supports: Spinnaker starting pipelines from Pub/Sub messages originating from Google Cloud systems such as the container registry, which separates B from A, C, and D.

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 2, Building and implementing CI/CD pipelines):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with designing pipelines, pipeline triggers, and artifact management with Artifact Registry.

---

## Question 44

*Domain 3: Applying Site Reliability Engineering Practices*

A serious outage prevented every user of your service from accessing it for several hours. After extended incident response, the service recovered and access was restored. You now need to give relevant stakeholders a summary of the incident, following Site Reliability Engineering (SRE) recommended practices. What should you do first?

- [ ] A. Phone each stakeholder individually to describe what occurred.
- [x] B. Write a postmortem and distribute it to the stakeholders.
- [ ] C. Send the incident state document to every stakeholder.
- [ ] D. Ask the engineer responsible to write an apology email to all stakeholders.

### Explanation

**Correct Answer**

**B. Write a postmortem and distribute it to the stakeholders.**

**Exam Reasoning Explanation**

Separate what is required from what is tempting. The requirement is a stakeholder-facing incident summary that follows SRE practice, and the word “first” asks for the opening step after recovery. The preference implied by SRE practice is a blameless, documented, learning-focused record. Work from requirement to capability to elimination. The SRE artifact that summarizes an incident for stakeholders and captures cause, impact, response, and follow-up actions is the postmortem. Each other option either skips documentation, uses a document meant for a different audience and moment, or assigns blame. That leaves one decision.

**Key Exam Clues**

  * **“Following Site Reliability Engineering recommended practices”** is a hard constraint. It points to blameless postmortems rather than informal or punitive communication.

  * **“After several hours of incident management, the service returned to normal”** is a sequence signal. Response is over, so the next step is the after-action write-up, not more live coordination.

  * **“Incident summary to relevant stakeholders”** is a technical signal. The deliverable is a written, shareable summary of the incident.

  * **“First”** is a sequence instruction. It asks for the initial step toward the summary, which is producing the document before distributing or discussing it.

**Why This Is Correct**

SRE practice treats a postmortem as the standard written record of an incident. It describes impact, root causes, the timeline, what went well and badly, and action items to prevent recurrence. A postmortem is written once the incident is resolved and the facts are understood, then shared so stakeholders get a consistent, accurate account and the organization learns from it. It is blameless, focusing on systems and processes rather than individuals. Writing it first means every later communication, whether a meeting, a call, or an update, draws on one agreed source of truth.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** Calling stakeholders does communicate, and it is tempting because it feels personal and quick. It produces no durable record, delivers inconsistent accounts to different people, and happens before the facts and causes are analyzed. It does not match the SRE expectation of a written summary.

**Option C — Different Use Case:** The incident state document, also called the living incident document, is a working record that the incident team updates in real time during the response. It is valid for coordinating responders. It is tempting because it already exists and contains incident detail. It is raw, in-progress, and written for responders, so it is not a polished summary for stakeholders and does not include analysis or follow-up actions.

**Option D — Violates Requirement:** Making one engineer apologize contradicts the blameless culture SRE recommends. Outages come from system and process weaknesses, and punishing or singling out an individual discourages honest reporting and does not address root causes.

**Exam Trap**

The strongest distractor is option C, because the incident state document is a real SRE artifact and holds all the incident details. The distinction is audience and timing. It is a live working tool for responders, while the postmortem is the after-action summary for stakeholders. The answer would shift to C only if the question asked what to maintain during the incident. Option A is the other trap, since talking to people feels responsible but skips the documentation step.

**Foundation Concept**

Incident handling has two phases with different artifacts. During the incident, a living document tracks status and coordinates the response. After resolution, a blameless postmortem analyzes what happened and drives preventive actions. Blamelessness matters because people report problems openly only when they are not punished for them, which improves learning. This model applies to significant incidents. Minor events may warrant a lighter review, but the principle of documenting and learning remains the same.

**Real-World Connection**

After a multi-hour outage, the incident commander gathers the timeline from the incident document, the team writes a postmortem with impact, root cause, and tracked action items, and it is shared with stakeholders and reviewed. The result is one consistent explanation, assigned follow-up work, and fewer repeat incidents. Leadership gets a clear account without relying on side conversations, and engineers stay willing to report problems.

**Memory Hook**

During the incident you keep a living document, and after it you write a blameless postmortem for stakeholders.

**30-Second Exam Takeaway**

When a question asks what to do after an incident is resolved under SRE practice, choose the blameless postmortem. Reject ad hoc communication, live incident documents, and blame-based actions.

**Official References**

[Google SRE Book — Postmortem Culture: Learning from Failure: ](https://sre.google/sre-book/postmortem-culture/)Supports: the postmortem as the standard written record after an incident and the principle of blamelessness, which supports option B and rules out option D.

[**Google SRE Book — Managing Incidents:**](https://sre.google/sre-book/managing-incidents/) Supports: the living incident document as a real-time coordination tool used during the response, which distinguishes option C as a different use case.

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 3, Applying site reliability engineering practices):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with mitigating incident impact on users and applying SRE practices.

---

## Question 45

*Domain 2: Building and Implementing CI/CD Pipelines*

You use Spinnaker to deploy your application, and your pipeline includes a canary deployment stage. The application keeps an in-memory cache that is populated with objects when the application starts. You want to automate the comparison between the canary version and the production version. How should you configure the canary analysis?

- [x] A. Compare the canary against a newly created deployment of the current production version.
- [ ] B. Compare the canary against a newly created deployment of the previous production version.
- [ ] C. Compare the canary against the already running deployment of the current production version.
- [ ] D. Compare the canary against the averaged performance of a sliding window of earlier production versions.

### Explanation

**Correct Answer**

**A. Compare the canary against a newly created deployment of the current production version.**

**Exam Reasoning Explanation**

The must-have is a fair, like-for-like comparison that isolates the effect of the new code. The scenario supplies the key detail: an in-memory cache filled at startup. That means a long-running instance and a freshly started instance behave differently regardless of the code version. Work through requirement, capability, elimination, decision. A valid baseline must run the same code as production while matching the canary in age and conditions. Any comparison target that differs in running time, code version, or traffic period adds noise that cannot be separated from the canary’s real effect. Only one option meets that bar.

**Key Exam Clues**

  * **“In-memory cache that loads objects at start time”** is a decisive technical signal. A freshly started canary has a cold cache, while a long-running instance has a warm one, which skews performance metrics.

  * **“Automate the comparison of the canary version against the production version”** is a hard constraint. The comparison target must produce statistically fair results.

  * **“Canary deployment stage in the pipeline”** is a context signal. Spinnaker’s canary analysis is designed to run a canary and a baseline side by side.

**Why This Is Correct**

Spinnaker’s automated canary analysis, built on Kayenta, compares the canary against a baseline rather than against the live production instances. The baseline is a new deployment of the current production version, started at the same time as the canary, with the same number of instances and configuration. Because both start together, they have the same cache warmup state, so differences in metrics reflect the code change instead of uptime. In this application, the cold cache is the very effect that would distort a comparison against long-running production instances. A boundary to note: the baseline runs the same version production runs, so it tests the new code, not production’s accumulated state.

**Why the Other Options Are Not the Best Fit**

**Option B — Incorrect:** A new deployment of the previous production version is a baseline of the wrong code. It is tempting because it is freshly started, like the canary, which would match cache state. It is not the version users currently run, so the analysis would compare the canary with something that is not production and could miss regressions relative to what is live.

**Option C — Violates Requirement:** Comparing against the existing production deployment is the intuitive approach, and it is tempting for that reason. The existing instances have run for a long time with warm caches, so latency and resource metrics would differ from a freshly started canary for reasons unrelated to the code. This is exactly the unfairness the cache detail points to.

**Option D — Technically Possible but Not Best:** A sliding window of earlier versions provides a long history, which is tempting for statistical stability. It mixes several code versions and different traffic periods, and none of it matches the canary’s start time, so it cannot isolate the effect of the new release.

**Exam Trap**

The strongest distractor is option C, because comparing a canary with the live production deployment is the most natural reading of a canary. The distinction is that the comparison must hold everything constant except the code, and uptime and cache state are not constant. The answer would switch to C only if the application had no warmup or startup effects and the production instances were otherwise comparable. A second trap is option B, which looks fair because it is freshly started but tests the wrong code version.

**Foundation Concept**

A valid experiment changes one variable and controls the rest. In canary analysis, the canary carries the changed code, and the baseline is the control. For the control to be valid, it should match the canary in code version relevant to production, start time, scale, and traffic exposure. Anything that depends on instance age, such as caches, JIT warmup, or connection pools, makes long-running instances a poor control. This model applies to automated comparison of metrics. Where an application has no age-dependent behavior, the difference matters less, but the baseline pattern remains the safer default.

**Real-World Connection**

A pipeline deploys three canary instances with the new image and three baseline instances with the current production image, routes a small share of traffic to each, and runs the analysis on matching metrics for a fixed period. A score above the threshold promotes the release, and a low score stops it. Teams often add a test where the canary runs the same version as production, which should always pass, to confirm the analysis configuration is sound. The cost is temporary extra instances while the analysis runs.

**Memory Hook**

Compare the canary to a fresh copy of today’s production, not to the instances that have been running for weeks.

**30-Second Exam Takeaway**

For canary analysis questions, pick a baseline that runs the current production version and starts alongside the canary. Reject comparisons against long-running instances, older versions, or historical averages.

**Official References**

[**Google Cloud Blog — Canary analysis: Lessons learned and best practices from Google and Waze:**](https://cloud.google.com/blog/products/devops-sre/canary-analysis-lessons-learned-and-best-practices-from-google-and-waze) Supports: comparing the canary against a baseline with the same version and configuration as production rather than against production itself, citing cache warmup as a skewing factor, which supports option A and rules out options C and D.

[**InfoQ — Kayenta: An Open Source Canary Analysis Tool from Netflix and Google:**](https://www.infoq.com/news/2018/04/kayenta) Supports: creating a brand new baseline cluster so metrics are free of effects from long-running processes, which reinforces the elimination of option C.

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 2, Building and implementing CI/CD pipelines):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with deployment strategies such as canary and with defining success metrics based on application telemetry.

---

## Question 46

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

A group of application servers runs on Compute Engine. You need a secure approach that requires the LEAST configuration and lets developers easily reach application logs for troubleshooting. How should you implement this on Google Cloud?

- [x] A. Install the Cloud Logging agent on the application servers. Grant the developers the Logs Viewer IAM role so they can read the logs in Cloud Logging.
- [ ] B. Install the Cloud Logging agent on the application servers. Grant the developers the Private Logs Viewer IAM role so they can read the logs in Cloud Logging.
- [ ] C. Install the Cloud Monitoring agent on the application servers. Grant the developers the Monitoring Viewer IAM role so they can read the metrics in Cloud Monitoring.
- [ ] D. Install the gsutil tool on the application servers and write a script that uploads the application logs to a Cloud Storage bucket, scheduled with cron every five minutes. Grant the developers the Storage Object Viewer IAM role on the bucket so they can read the logs.

### Explanation

**Correct Answer**

**A. Install the Cloud Logging agent on the application servers. Grant the developers the Logs Viewer IAM role so they can read the logs in Cloud Logging.**

**Exam Reasoning Explanation**

Separate the must-haves from the preference. The must-haves are that developers can read application logs and that access stays secure. The preference is the least configuration. Work through requirement, capability, elimination, decision. Application logs on a VM need an agent to reach Cloud Logging, so the choice must include a logging collector. Access should follow least privilege, so the role should grant only what developers need to read ordinary logs. Option C collects the wrong data type, and option D replaces managed collection with custom scripting. Of the two remaining logging options, the one with the narrower role is the secure fit.

**Key Exam Clues**

  * **“Application logs”** is a technical signal. The goal is logs, not metrics, so a metrics-oriented agent and role do not meet it.

  * **“Secure”** is a hard constraint. It calls for the narrowest role that still lets developers read the logs.

  * **“LEAST amount of configuration”** is a preference. A managed agent and a predefined role beat custom scripts and schedules.

  * **“Easily access ... for troubleshooting”** is a technical signal. Developers should use the Logs Explorer rather than fetch files from a bucket.

**Why This Is Correct**

A logging agent running on each VM collects application logs and sends them to Cloud Logging, which stores and indexes them without extra infrastructure. The Logs Viewer role gives read access to the log data in the default log buckets, except Data Access audit logs, which is what developers need for troubleshooting. Granting it at the project level takes a single IAM binding, and developers browse and query logs in the Logs Explorer. This combines managed collection with least-privilege access and almost no custom configuration. One boundary: the VMs must be allowed to write logs, so their service account needs permission to do so, which is typically a default setup step.

**Why the Other Options Are Not the Best Fit**

**Option B — Technically Possible but Not Best:** It collects logs the same way, so it works for troubleshooting. The Private Logs Viewer role adds access to private logs such as Data Access audit logs, which developers do not need. It is tempting because it sounds more complete, but it grants more than necessary and weakens least privilege.

**Option C — Different Use Case:** The monitoring agent collects metrics, and the Monitoring Viewer role shows metrics and dashboards. It is a valid combination for performance monitoring. It is tempting because the two products share a brand and an observability goal. It does not deliver application logs, so it fails the core requirement.

**Option D — Technically Possible but Not Best:** Scripted uploads to Cloud Storage can make logs available. It is tempting because Storage roles are simple. It requires writing, scheduling, and maintaining scripts, introduces a five-minute delay, and gives developers files to download instead of searchable logs. That is the opposite of least configuration and easy troubleshooting.

**Exam Trap**

The strongest distractor is option B, because it is identical to the answer except for the role, and a broader role can look like the safer way to ensure access. The distinction is least privilege: Logs Viewer already covers ordinary application logs, and Private Logs Viewer adds sensitive log types. The answer would switch to B only if developers needed to read Data Access audit logs. A terminology note: the legacy logging and monitoring agents have reached end of support, and the Ops Agent is the current agent that collects both logs and metrics. The item keeps the separate agent names so the distinction between logs and metrics in option C stays meaningful. Today’s equivalent of the answer is the Ops Agent with the Logs Viewer role.

**Foundation Concept**

Centralized logging separates collection, storage, and access. An agent collects and ships logs, a managed service stores and indexes them, and IAM roles control who can read them. Least privilege means granting the narrowest role that satisfies the task. Logs and metrics are different telemetry types with different tools and roles, so matching the data type to the task comes first. This model fits routine application troubleshooting. Regulated or sensitive logs may need stricter role separation or restricted log views.

**Real-World Connection**

A team installs the agent through its VM image or instance configuration, so every server in the pool ships logs automatically. The developers group receives the Logs Viewer role on the project, and engineers filter by service and severity in the Logs Explorer during an incident. The result is faster troubleshooting with no scripts to maintain. Sensitive audit data stays restricted to the smaller group that holds the private log role.

**Memory Hook**

Logs need a logging agent and the Logs Viewer role, while metrics belong to monitoring and private logs belong to audit needs.

**30-Second Exam Takeaway**

When a question asks for developer access to application logs with minimal setup, choose the managed logging agent plus the narrowest viewer role. Reject metrics tools, broader roles than needed, and custom upload scripts.

**Official References**

[**Google Cloud — Cloud Logging access control with IAM:**](https://docs.cloud.google.com/logging/docs/access-control) Supports: Logs Viewer covering log data except Data Access logs and Private Logs Viewer adding private logs, which separates option A from option B.

[**Google Cloud Observability — Legacy Monitoring and Logging agents end of support:**](https://docs.cloud.google.com/stackdriver/docs/deprecations/logging-agent) Supports: the legacy agents having reached end of support and the Ops Agent being the supported alternative, which explains the terminology note.

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 4, Implementing observability practices and troubleshooting issues):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with collecting logs using the Ops Agent and managing and analyzing logs.

---

## Question 47

*Domain 3: Applying Site Reliability Engineering Practices*

You support a high-traffic web application and want to make sure the home page loads quickly. As a first step, you decide to define a Service Level Indicator (SLI) for home page request latency, with 100 ms as the acceptable page load time. What is the Google-recommended way to calculate this SLI?

- [ ] A. Group request latencies into buckets, and then calculate the percentile that corresponds to 100 ms.
- [ ] B. Group request latencies into buckets, and then calculate the median and the 90th percentile.
- [x] C. Count the home page requests that complete in under 100 ms, and then divide that count by the total number of home page requests.
- [ ] D. Count the home page requests that complete in under 100 ms, and then divide that count by the total number of requests to the whole web application.

### Explanation

**Correct Answer**

**C. Count the home page requests that complete in under 100 ms, and then divide that count by the total number of home page requests.**

**Exam Reasoning Explanation**

Start with the requirement: an SLI for home page latency with a stated threshold of 100 ms. Then ask what shape a Google-recommended SLI takes. It is a ratio of good events to valid events, expressed as a percentage, so it can later be compared with an objective. Apply that shape in two steps. First, define good: a home page request faster than 100 ms. Second, define valid: only home page requests, because the SLI describes the home page. Check each option against both steps. Two options fail on the threshold or the formula, one fails on the denominator, and one satisfies both.

**Key Exam Clues**

  * **“Acceptable page load time set to 100 ms”** is a hard constraint. The calculation must classify each request against this threshold.

  * **“Home page request latency”** is a scoping instruction. The SLI covers home page requests only, so the denominator must exclude other traffic.

  * **“Google-recommended way of calculating”** is a technical signal. It points to the standard SLI equation of good events divided by valid events.

  * **“As a first step”** is a context signal. It suggests a simple, well-defined indicator to be paired with an objective later.

**Why This Is Correct**

Google’s SRE guidance defines an SLI as the proportion of valid events that were good, which yields a value between 0 and 100 percent. For latency, a good event is a request served faster than the threshold, and valid events are the requests the SLI is meant to describe. Counting home page requests under 100 ms and dividing by all home page requests gives exactly that ratio. The result is directly usable as the basis for a service level objective, such as a target percentage of fast requests, and it maps naturally to error budgets. It also reads in plain terms: the share of home page loads that met the target.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** Looking up the percentile at 100 ms is close in spirit, because it approximates the share of requests at or below the threshold. It is tempting for that reason. It is not the recommended calculation, because bucketing limits precision to bucket boundaries, a percentile is a summary of the distribution rather than a good-over-valid ratio, and it is harder to tie to a percentage-based objective.

**Option B — Incorrect:** The median and the 90th percentile describe the shape of the latency distribution. It is tempting because percentiles are common in latency reporting. Neither value is compared with the 100 ms threshold, so the calculation never classifies requests as good or bad and does not produce an SLI in the required form.

**Option D — Violates Requirement:** The numerator is correct, but the denominator includes all web application requests. It is tempting because it differs from the answer by only one phrase. It dilutes the home page measurement with unrelated traffic, so the result no longer represents home page latency.

**Exam Trap**

The strongest distractor is option D, because it looks nearly identical to the answer and differs only in the denominator. The distinction is that valid events must match what the SLI describes, which here is home page requests. The answer would switch to D only if the SLI were defined for the whole application’s request latency. Option A is the second trap, since a percentile at the threshold seems equivalent but is not the recommended form of the calculation.

**Foundation Concept**

A good SLI is expressed as a ratio of good events to valid events. This lets one definition work across latency, availability, and quality, and it maps directly to a percentage objective and an error budget. Thresholds turn a continuous measurement such as latency into a good or bad classification for each event. Scoping matters: the valid event set should match the user journey being measured, so unrelated traffic does not mask problems. This approach works for request-driven services. Other workloads, such as batch jobs, use different event definitions but keep the same ratio shape.

**Real-World Connection**

A team counts home page requests served under 100 ms from its load balancer or application metrics and divides by all home page requests. It then sets an objective such as 99 percent of home page loads under the threshold over a rolling window. If the ratio drops below the objective, the error budget burns and the team prioritizes reliability work. Excluding other pages keeps a slow checkout flow from hiding a healthy home page, and the reverse.

**Memory Hook**

An SLI is good events over valid events, so count the fast home page requests and divide by home page requests only.

**30-Second Exam Takeaway**

When asked how to calculate an SLI, answer with good events divided by valid events, and check that the denominator matches the scope the SLI describes. Reject answers that report distribution summaries or use a broader denominator.

**Official References**

[**Google SRE Workbook — Implementing SLOs:**](https://sre.google/workbook/implementing-slos/) Supports: the SLI equation of good events divided by valid events and its use for latency, which supports option C and rules out options B and D.

[**Google SRE Book — Service Level Objectives:**](https://sre.google/sre-book/service-level-objectives/) Supports: the definition of an SLI as a measure of service level, with latency thresholds and percentiles discussed as indicators and objectives, which clarifies why option A and option B are not the recommended calculation.

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 3, Applying site reliability engineering practices):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with defining SLIs, SLOs, and SLAs under balancing change, velocity, and reliability.

---

## Question 48

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Several applications run on a Google Kubernetes Engine (GKE) cluster, and you use GKE’s built-in integration with Cloud Logging and Cloud Monitoring. You are about to put a new containerized application into production that a third party wrote and that cannot be modified or reconfigured. The application writes its log output to /var/log/app_messages.log, and you want those entries to appear in Cloud Logging. What should you do?

- [ ] A. Rely on the default GKE logging agent configuration.
- [ ] B. Deploy a Fluentd DaemonSet to the GKE cluster, and then define a custom input and output configuration that tails the log file in the application’s pods and writes to Cloud Logging.
- [ ] C. Install Kubernetes on Compute Engine and redeploy your applications, and then customize the built-in logging configuration to tail the log file in the application’s pods and write to Cloud Logging.
- [x] D. Write a script that tails the log file inside the pod and writes the entries to standard output, run it as a sidecar container in the application’s pod, and configure a volume shared between the containers so the script can read /var/log in the application container.

### Explanation

**Correct Answer**

**D. Write a script that tails the log file inside the pod and writes the entries to standard output, run it as a sidecar container in the application’s pod, and configure a volume shared between the containers so the script can read /var/log in the application container.**

**Exam Reasoning Explanation**

The must-haves are that the application stays untouched and that its file-based logs reach Cloud Logging. Start from how GKE collects logs. The built-in node agent picks up what containers write to standard output and standard error, and nothing else. The application writes to a file inside its own container, so the managed agent never sees it. The decision then becomes how to turn that file into a stream the managed agent already handles, or how to add a separate collector that can reach the file. A file inside one container is not visible to other containers or to the node unless a volume is shared. That favors changing the pod around the application, not the application itself.

**Key Exam Clues**

  * **“Written by a third party and cannot be modified or reconfigured”** is a hard constraint. The solution must work around the application, for example with a companion container.

  * **“Writes its log information to /var/log/app_messages.log”** is a technical signal. The logs are in a file, not on standard output, so default collection misses them.

  * **“Using GKE’s built-in logging integration”** is a technical signal. The managed agent already ships standard output and standard error, so converting the file into that stream reuses it.

  * **“Containerized application”** is a scoping signal. The file lives in the container’s filesystem and is isolated unless a volume is shared.

**Why This Is Correct**

Kubernetes documents a streaming sidecar pattern for applications that cannot write to standard output. The application container writes to a file on a shared volume, and a sidecar container in the same pod reads that file and prints it to its own standard output. The kubelet and the existing node-level logging agent then collect the sidecar’s output like any other container log, so the entries reach Cloud Logging with no new collector to operate. The script is essentially a single tail command. The application’s code and configuration are unchanged, and only the pod specification gains a sidecar and a shared volume. One boundary: mounting a shared volume at /var/log hides anything already at that path in the application image, and the sidecar adds some resource use to each pod.

**Why the Other Options Are Not the Best Fit**

**Option A — Incorrect:** The default configuration collects container standard output and standard error plus system logs. It does not read arbitrary files inside a container, so the application’s file never reaches Cloud Logging. It is tempting because the managed integration is already in place.

**Option B — Technically Possible but Not Best:** A custom Fluentd DaemonSet can be made to read files, which is why it is tempting, and Google publishes guidance on customizing Fluentd for GKE. A node-level agent reads files that exist on the node, and the container’s log file is not visible there unless a host-mounted volume exposes it, which means changing the pod specification anyway. It also adds a second logging agent to maintain and configure beside the managed one, so it is more work for the same pod change.

**Option C — Violates Requirement:** Moving to self-managed Kubernetes on Compute Engine abandons the GKE environment that is already in use, and the logging challenge remains because a file inside a pod still needs a shared volume or sidecar. It is tempting only because custom configuration is possible there. The effort and operational burden are far out of proportion.

**Exam Trap**

The strongest distractor is option B, because a Fluentd DaemonSet is the familiar way to customize logging on GKE and is the answer some practice sources list. The distinction is that a node-level agent only works on what is visible at the node, which for containers means standard output and standard error, so a file inside the container needs a shared volume or a sidecar to be reachable. The answer would switch to B if the application’s file were already on a host-mounted path that the DaemonSet could read. The word “script” in option D is also a trap, because it looks like development effort, but it is a one-line tail command and a sidecar in the pod specification.

**Foundation Concept**

Container platforms are designed around logs as streams written to standard output and standard error, which a node-level agent collects without touching the application. When an application writes to files instead, you must either bridge the file to a stream or run a collector that can see the file. A sidecar shares the pod’s volumes and network, so it is the natural place to bridge. This model works for any file, socket, or journal source. A sidecar that runs its own logging agent is an alternative when you need parsing or custom routing, at the cost of more resources and configuration.

**Real-World Connection**

A team adds an emptyDir volume mounted at /var/log in the application container and the sidecar, and the sidecar runs a tail command on the log file. The entries appear in Cloud Logging under the sidecar container’s name, can be filtered like any other container logs, and the vendor’s application is untouched. The operational costs are a little extra CPU and memory per pod, and care that log rotation does not leave the shared volume growing without bound.

**Memory Hook**

If the app writes to a file and cannot change, add a sidecar that streams the file to standard output.

**30-Second Exam Takeaway**

For file-based logs from an unchangeable app on GKE, choose a sidecar that tails the file to standard output through a shared volume. Reject answers that rely on default collection or on a node agent that cannot see inside the container.

**Official References**

[**Kubernetes — Logging Architecture:**](https://kubernetes.io/docs/concepts/cluster-administration/logging/) Supports: node-level logging agents handling container standard output and standard error, and the sidecar pattern in which a container streams application logs to its own standard output so the existing agent collects them, which supports option D and the elimination of options A and B.

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 4, Implementing observability practices and troubleshooting issues):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with collecting and importing logs and optimizing logs by source.

---

## Question 49

*Domain 2: Building and Implementing CI/CD Pipelines*

Your multi-step Cloud Build pipeline builds your application and deploys it to Google Kubernetes Engine (GKE). You want to connect the pipeline to a third-party monitoring platform by sending the build information to a webhook with an HTTP POST. You also want to keep development effort as low as possible. What should you do?

- [ ] A. Add logic to every Cloud Build step that sends the build information to the webhook with an HTTP POST.
- [ ] B. Add a final step to the Cloud Build pipeline that sends the build information to the webhook with an HTTP POST.
- [ ] C. Use Cloud Logging to create a log-based metric from the Cloud Build logs, and then create an alerting policy that uses a webhook notification channel.
- [x] D. Create a Pub/Sub push subscription on the Cloud Build cloud-builds topic so that the build information is sent to the webhook with an HTTP POST.

### Explanation

**Correct Answer**

**D. Create a Pub/Sub push subscription on the Cloud Build cloud-builds topic so that the build information is sent to the webhook with an HTTP POST.**

**Exam Reasoning Explanation**

The must-have is that build information reaches a third-party webhook as an HTTP POST. The preference is minimal development effort. Work through requirement, capability, elimination, decision. Ask which approach already produces the build information and the HTTP POST without new code. Cloud Build already publishes build state changes as messages, and a Pub/Sub push subscription already delivers messages as HTTP POST requests to an endpoint. Joining those two managed pieces is configuration. The other options require writing and maintaining logic inside the pipeline or repurposing a metrics and alerting feature for a job it was not designed to do.

**Key Exam Clues**

  * **“HTTP POST of the build information to a webhook”** is a technical signal. Pub/Sub push delivery is itself an HTTP POST to a webhook endpoint.

  * **“Minimize the development effort”** is a preference that works as a tiebreaker. It favors configuration over custom pipeline code.

  * **“Multiple step pipeline”** is a technical signal. Per-step logic would multiply the work and still miss overall build status events.

  * **“Build information”** is a technical signal. Cloud Build’s own notifications carry the build resource and status, so you do not need to assemble it.

**Why This Is Correct**

Cloud Build publishes a message to the cloud-builds Pub/Sub topic whenever a build’s state changes, such as when it is created, starts working, or completes. Each message carries the build resource and its status. A push subscription on that topic makes Pub/Sub send each message to a configured HTTPS endpoint as a POST request, so the webhook receives build updates with no pipeline code. Setup amounts to creating the topic if needed, granting the required permissions, and creating the subscription. Two boundaries apply. The push request wraps the message in a JSON envelope, with the build data base64-encoded inside, so the receiving platform must accept that format, or you can choose unwrapped delivery to send the raw data. The endpoint must also be an HTTPS address that Pub/Sub can reach and that returns a success code.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** Adding POST logic to every step works. It is tempting because it uses only Cloud Build. It requires the most effort, since the code must be written, kept consistent, and maintained in each step. It also does not capture overall build state changes cleanly.

**Option B — Technically Possible but Not Best:** A final step is less work than adding logic to every step, which makes it tempting. It still requires custom code, and it only runs when earlier steps succeed, so failed builds may never report. It would also need to assemble the build information itself.

**Option C — Different Use Case:** A log-based metric with an alerting policy and a webhook notification channel can notify a webhook. It is tempting because alerting policies support webhooks. It is built to alert on conditions in logs, not to forward build information, so it adds metric and policy configuration and the alert payload would not be the build data the monitoring platform expects.

**Exam Trap**

The strongest distractor is option B, because a final pipeline step seems like the obvious lightweight integration. The distinction is that it still means writing and maintaining code inside the pipeline, and it can miss failed builds, whereas the Pub/Sub notification is managed and fires on every state change. The answer would switch toward B only if Pub/Sub were unavailable or if the webhook needed a custom payload that Pub/Sub could not provide. Option C is the second trap, because log-based alerting sounds like a monitoring integration but delivers alerts, not build records.

**Foundation Concept**

Event-driven integration lets a source publish state changes and any number of consumers react without changing the source. Messaging services decouple producers from consumers, and push delivery turns messages into HTTP calls for webhook-style receivers. Prefer using the event stream a managed service already emits over adding code to the process that generates the events. This model works well for status and lifecycle events. Fine-grained custom data from inside a build step still requires explicit logic in that step.

**Real-World Connection**

A team creates a push subscription on the build topic that targets the monitoring vendor’s HTTPS endpoint with authentication enabled. Every build creation, progress, success, and failure then appears in the monitoring platform, including builds that fail early. The team maintains no scripts, and its main ongoing task is confirming the receiver handles the Pub/Sub message envelope. If the vendor cannot parse it, they can enable unwrapped delivery or place a small relay in front.

**Memory Hook**

Build events are already published to Pub/Sub, so a push subscription turns them into webhook calls without code.

**30-Second Exam Takeaway**

When a managed service already emits events and you need them in an external HTTP endpoint with low effort, choose Pub/Sub with a push subscription. Reject custom code in the pipeline and alerting features that do not carry the data.

**Official References**

[**Google Cloud — Cloud Build: Subscribe to build notifications:**](https://cloud.google.com/build/docs/subscribe-build-notifications) Supports: Cloud Build publishing build state changes to the cloud-builds topic and supporting push subscriptions that deliver messages to an endpoint, which supports option D and rules out options A and B.

[**Google Cloud — Pub/Sub push subscriptions:**](https://docs.cloud.google.com/pubsub/docs/push) Supports: push delivery sending messages to a webhook as an HTTPS POST request, in wrapped or unwrapped form, which supports the mechanism and the format boundary in option D.

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 2, Building and implementing CI/CD pipelines):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with implementing and managing pipelines, including auditing and tracking deployments with Cloud Build.

---

## Question 50

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You built a Cloud Monitoring chart for CPU utilization on a dashboard in the scoping project of your metrics scope. You want to share the chart with your Site Reliability Engineering (SRE) team and nobody else, and you must follow the principle of LEAST privilege. What should you do?

- [ ] A. Give the SRE team the scoping project’s project ID, and grant the team the Monitoring Viewer IAM role on that project.
- [ ] B. Give the SRE team the scoping project’s project ID, and grant the team the Monitoring Dashboard Configuration Viewer IAM role on that project.
- [x] C. Use the chart’s share-by-URL option and send the link to the SRE team, and grant the team the Monitoring Viewer IAM role on the scoping project.
- [ ] D. Use the chart’s share-by-URL option and send the link to the SRE team, and grant the team the Monitoring Dashboard Configuration Viewer IAM role on the scoping project.

### Explanation

**Correct Answer**

**C. Use the chart’s share-by-URL option and send the link to the SRE team, and grant the team the Monitoring Viewer IAM role on the scoping project.**

**Exam Reasoning Explanation**

Two separate things must happen for the SRE team to see the chart: they need a way to reach that specific chart, and they need permission to read what it displays. Treat these as two requirements and check each option against both. A link delivers the chart, but a link alone grants no access. A role grants access, and least privilege asks for the narrowest role that still lets the chart render its data. A chart shows metric data, so a role limited to dashboard configuration may not be enough. Work through requirement, capability, elimination, decision, and only one option meets both parts without extra privilege or a missing piece.

**Key Exam Clues**

  * **“Share the chart with the SRE team only”** is a scoping instruction. The sharing method should deliver the specific chart and the access should be limited to that group.

  * **“Principle of LEAST privilege”** is a hard constraint. The role must be the narrowest one that still allows the chart to display data.

  * **“Chart ... CPU utilization”** is a technical signal. A chart displays metric data, so the viewer needs permission to read metrics, not only the dashboard’s definition.

  * **“Dashboard within your scoping project”** is a technical signal. Permissions are granted on the project that holds the metrics scope.

**Why This Is Correct**

Sharing the chart’s URL gives the team a direct link to the exact chart they need. Access is a separate control, because a link does not by itself grant permission to view the data behind it. The Monitoring Viewer role gives read-only access to Cloud Monitoring data and configuration, including custom dashboards, and it is the narrow predefined role that lets the chart show its metric data. It does not allow editing or administration, so it respects least privilege among the options offered. Granting it to a group for the SRE team keeps the access limited to those people. One boundary: Monitoring Viewer applies to the whole project’s monitoring data, not only this chart, so a tighter scope would require a custom role.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** The role is correct, and the team could eventually find the chart, which is why it is tempting. A project ID does not deliver the chart. The team would have to navigate to the project and locate the dashboard themselves, so the specific sharing requirement is not met cleanly.

**Option B — Violates Requirement:** The Monitoring Dashboard Configuration Viewer role grants read-only access to dashboard configurations. It is narrower, which makes it attractive for least privilege. It does not provide the permissions to read the underlying metric data, so the chart would not display what the team needs. The project ID also does not deliver the chart.

**Option D — Violates Requirement:** It delivers the chart with a link, which is right, but pairs it with the configuration-only role. The SRE team could open the dashboard definition but not see the CPU data. Least privilege is not satisfied by a role that is too narrow to do the job.

**Exam Trap**

The strongest distractor is option D, because the dashboard-specific role looks like the most precise least-privilege choice. The distinction is that least privilege means the minimum needed to accomplish the task, and viewing a chart’s data requires metric read permission that the configuration role lacks. The answer would switch to D only if the team needed to see dashboard definitions without viewing any metric values. Option A is the second trap, because the role is right and the sharing method only looks equivalent. A terminology note: workspaces have been replaced by metrics scopes, and the project that hosts the scope is the scoping project. The old Dashboard Viewer role corresponds to the Monitoring Dashboard Configuration Viewer role, which is how the options name it.

**Foundation Concept**

Sharing involves two layers: delivery, which tells people where something is, and authorization, which decides whether they may see it. Least privilege picks the narrowest role that still allows the task to succeed, not the narrowest role in existence. Granting roles to a group rather than individuals keeps access manageable as team membership changes. Predefined roles are broad by design, and when even the narrowest predefined role is too wide, a custom role with specific permissions is the fix.

**Real-World Connection**

An engineer adds the SRE team’s Google group to the scoping project with the Monitoring Viewer role, then pastes the chart link into the team’s channel. Anyone in the group can open the chart and see live CPU data but cannot change dashboards or alerting. If the link is forwarded to someone outside the group, that person still sees a permission error, so the data stays limited to the team.

**Memory Hook**

A link delivers the chart and a role authorizes the data, so send the link and grant the narrowest role that can read metrics.

**30-Second Exam Takeaway**

For sharing monitoring content with least privilege, deliver it with a direct link and grant the narrowest role that can read the underlying data. Reject answers that skip the link or choose a role too narrow to display the data.

**Official References**

[**Google Cloud — Cloud Monitoring: Control access with IAM:**](https://docs.cloud.google.com/monitoring/access-control) Supports: Monitoring Viewer granting read-only access to Monitoring data and configuration including custom dashboards, and the dashboard configuration viewer role being limited to dashboard configurations, which supports option C and rules out options B and D.

[**Google Cloud — Cloud Monitoring: Share a custom dashboard:**](https://docs.cloud.google.com/monitoring/charts/share-dashboards) Supports: shared links requiring the recipient to have permission to view the dashboard, which explains why a link and a role are both needed.

[Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 4, Implementing observability practices and troubleshooting issues): ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment with managing dashboards, including creating, filtering, and sharing them.

---

## Question 51

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You run an application on a virtual machine (VM) created from a custom Debian image that has the Cloud Logging agent installed. The VM has the cloud-platform access scope, and the application writes its log output through syslog. You want to view these logs in the Logs Explorer in the Google Cloud console, but syslog does not appear in the “All logs” list. What should you do first?

- [ ] A. Look in the Logs Explorer for the agent’s test log entry.
- [ ] B. Install the latest version of the Cloud Logging agent.
- [ ] C. Confirm that the VM’s service account access scopes include the monitoring.write scope.
- [x] D. Connect to the VM over SSH and run the command: ps ax | grep fluentd.

### Explanation

**Correct Answer**

**D. Connect to the VM over SSH and run the command: ps ax | grep fluentd.**

**Exam Reasoning Explanation**

The symptom is that a log stream that should exist is missing, and the agent is the component responsible for delivering it. The first troubleshooting step should be the cheapest check that splits the problem in half: is the collector running at all? Work through requirement, capability, elimination, decision. If the agent process is not running, nothing else matters yet. If it is running, move on to credentials, scopes, or configuration. The remaining options either look at downstream results that depend on the agent running, change the installation before diagnosing it, or check a scope that does not apply to the problem.

**Key Exam Clues**

  * **“Syslog is not showing up”** is a technical signal. Something between the application and Cloud Logging is broken, and the agent is the first suspect.

  * **“Image has the agent installed”** is a technical signal. Installed does not mean running, so the process state is the next thing to verify.

  * **“Cloud-platform scope”** is a hard constraint that eliminates scope problems. This scope already allows writing logs.

  * **“First”** is a sequence instruction. It calls for the quickest, lowest-impact diagnostic before any change.

**Why This Is Correct**

On a Linux VM, the legacy Cloud Logging agent runs as a fluentd-based process. Running ps ax | grep fluentd on the VM shows immediately whether that process exists. Google’s troubleshooting guidance says that if you suspect the agent is not working, you should check that it is running and then try to send a test message. A missing process points to a stopped or disabled agent, which you can then restart or investigate, for example through the service status and the agent’s own log file. If the process is present, you know to look at credentials, scopes, or configuration next. The command is read-only, fast, and gives a clear branching result.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** The agent’s test log entry is a real verification method, and it is tempting because it uses the console you are already in. Google lists it as a way to verify a new installation. Here you already know the log is missing, and an absent test entry would not explain why. Checking the process directly is the more informative and more direct first step.

**Option B — Technically Possible but Not Best:** Reinstalling or upgrading can fix some agent problems, which makes it tempting. It is a change made before any diagnosis, takes more effort, and could simply reinstall the same configuration problem. Diagnostics should come before changes.

**Option C — Incorrect:** The monitoring.write scope is for the Monitoring agent. Writing logs requires logging.write, and the cloud-platform scope already covers it. Checking this scope would not reveal the cause and is based on the wrong agent.

**Exam Trap**

The strongest distractor is option A, because it appears in the official guidance and feels like a verification step. The distinction is purpose and order. It confirms that a fresh installation worked, while the process check answers whether the agent is running now, which is the question behind the symptom. The answer would switch to A if the scenario said the agent had just been installed and you needed to confirm the installation. Option C is a second trap because a scope problem is a common cause of missing telemetry, but here the scope is already broad and the named scope belongs to a different agent. A terminology note: the legacy logging and monitoring agents have reached end of support, and the Ops Agent is their supported successor. This item keeps the legacy agent because the fluentd process check is specific to it.

**Foundation Concept**

When telemetry is missing, troubleshoot along the path from source to destination: the application writes the log, the agent collects and ships it, the credentials and permissions allow the write, and the backend stores and displays it. Start with the cheapest check that eliminates the largest part of the path, which is usually whether the collector process is running. Make changes only after diagnosis. This approach works for most agent-based pipelines. Once the agent is confirmed running, the next checks follow the path: agent logs, scopes, and service account permissions.

**Real-World Connection**

An engineer connects to the VM, runs the process check, and finds no agent process. They check the service status and the agent’s log file, see that the agent was disabled by instance metadata on a copied image, and re-enable it. Logs begin to appear within minutes. Had the process been running, the engineer would have moved on to credentials and scopes, saving a needless reinstall.

**Memory Hook**

Missing logs mean check whether the agent process is running before you check anything else.

**30-Second Exam Takeaway**

For missing telemetry questions, choose the least invasive diagnostic that tests the collector first, such as confirming the agent process is running. Reject reinstalls, unrelated scopes, and checks that only make sense after the agent is known to work.

**Official References**

[Google Cloud — Troubleshoot the Logging agent: ](https://docs.cloud.google.com/logging/docs/agent/troubleshooting)Supports: checking that the agent is running with ps ax | grep fluentd when you suspect it is not working, the test log entry being a separate installation check, and the scope guidance showing logging.write for the Logging agent and monitoring.write for the Monitoring agent, which supports option D and rules out options A and C as first steps.

[**Google Cloud Observability — Legacy Monitoring and Logging agents end of support:**](https://docs.cloud.google.com/stackdriver/docs/deprecations/logging-agent) Supports: the legacy agents having reached end of support, which explains the terminology note.

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 4, Implementing observability practices and troubleshooting issues):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with collecting logs and troubleshooting observability issues.

---

## Question 52

*Domain 3: Applying Site Reliability Engineering Practices*

An application runs on a single Compute Engine VM in one region. Occasional VM shutdowns interrupt users’ ongoing work. You need a solution that can be implemented quickly and reliably notifies you about shutdown events.

Which approach should you choose?

- [x] A. In Logs Explorer, create a log-based alert for VM log entries with `protoPayload.methodName` set to `v1.compute.instances.stop`.
- [ ] B. Route the VM logs to BigQuery and schedule hourly queries that find entries with `protoPayload.methodName` set to `v1.compute.instances.stop`.
- [ ] C. Modify the application to detect when its host VM is about to shut down and send a notification from the application.
- [ ] D. Use Cloud Scheduler to trigger health checks of the VM at randomized intervals, with no more than one hour between checks.

### Explanation

**Correct Answer**

**A. In Logs Explorer, create a log-based alert for VM log entries with**`**protoPayload.methodName**`**set to**`**v1.compute.instances.stop**`**.**

**Exam Reasoning Explanation**

The requirements are prompt notification and reliable detection; quick implementation favors an existing managed capability. A directly connects matching VM audit events to alert notifications. B and D introduce polling delays, while C depends on the affected application anticipating its host’s shutdown.

**Key Exam Clues**

  * **“Shutdown events” — Technical signal:** Look for VM lifecycle events in audit logs.

  * **“Reliably notifies you” — Hard constraint:** Finding records alone is insufficient; the solution needs an alerting policy and notification channel.

  * **“Implemented quickly” — Preference:** A managed alerting capability avoids application changes and custom checking logic.

**Why This Is Correct**

Google documents `v1.compute.instances.stop` as a Compute Engine stop operation. A log-based alert can match its audit entries and send notifications through configured channels. Logs Explorer provides the workflow to create this policy directly. 

The essential filter is:
    
          1. resource.type="gce_instance"
      2. protoPayload.methodName="v1.compute.instances.stop"

Configure a notification channel and scope the filter to the relevant VM. This is the strongest listed approach for detecting the specified stop operation.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Technically Possible but Not Best:** Hourly queries can identify matching historical records, making this tempting for analysis. However, detection can wait until the next query execution, and the option does not configure notifications. It fits periodic reporting better than prompt operational alerting.

  * **Option C — Incorrect:** Application logic might recognize some graceful shutdown signals, but it cannot reliably anticipate every unexpected VM termination or guarantee that it can send a notification before execution stops. It also requires development and deployment work.

  * **Option D — Technically Possible but Not Best:** Cloud Scheduler can invoke a target that performs a custom check. However, intervals approaching one hour delay detection and can miss outages that resolve between checks. Scheduler invokes work on a schedule; checking health and sending notifications require additional logic. 

**Exam Trap**

BigQuery can find the same log records, but scheduled analysis introduces a waiting period. If the requirement changed to an **hourly historical report of stop operations** , B would become appropriate.

**Foundation Concept**

Event-based monitoring reacts to recorded events; polling observes state at intervals and can miss changes between observations.

Coverage depends on the event filter. `**v1.compute.instances.stop**`**does not represent every possible VM shutdown cause.** Guest OS terminations, host errors, and maintenance terminations use other event names. Production coverage should include the relevant additional events.

**Real-World Connection**

An operations team scopes the alert to the application VM and routes notifications to its on-call channel. This reduces manual log inspection and speeds investigation of stop operations. Alerting improves detection; restoring availability still requires a separate recovery action.

**Memory Hook**

For prompt notification about a recorded VM lifecycle event, match the event in logs and attach a notification channel.

**30-Second Exam Takeaway**

When an operational event already appears in logs, prefer a managed log-based alert over hourly queries or application-based prediction. Check that the filter covers the failure causes you need to detect.

**Official References**

  * **Google Cloud Logging — Configure log-based alerting policies**

Supports: Creating alerts in Logs Explorer, matching log entries, and configuring notification channels.

[Official documentation](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts)

  * **Google Cloud Monitoring — Event types: Virtual machine terminations**

Supports: The stop-event filter and the distinction between stop operations and other termination causes.

[Official documentation](https://docs.cloud.google.com/monitoring/dashboards/event-types#vm-terminations)

  * **Google Cloud Scheduler — About Cloud Scheduler**

Supports: Scheduled target invocation and why custom health-check logic is required.

[Official documentation](https://docs.cloud.google.com/scheduler/docs/overview)

  * **Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide**

Supports: Objective 4.3, configuring alerting and alerting policies.

---

## Question 53

*Domain 3: Applying Site Reliability Engineering Practices*

Your organization is adopting Site Reliability Engineering (SRE) culture and principles. A service you support recently suffered a limited outage. A manager on another team asks you for a formal account of what happened so that they can act on remediation work. What should you do?

- [ ] A. Write a postmortem covering the root causes, the resolution, lessons learned, and a prioritized list of action items, and share it only with the manager.
- [x] B. Write a postmortem covering the root causes, the resolution, lessons learned, and a prioritized list of action items, and publish it on the engineering organization’s document portal.
- [ ] C. Write a postmortem covering the root causes, the resolution, lessons learned, the people responsible, and a list of action items for each person, and share it only with the manager.
- [ ] D. Write a postmortem covering the root causes, the resolution, lessons learned, the people responsible, and a list of action items for each person, and publish it on the engineering organization’s document portal.

### Explanation

**Correct Answer**

**B. Write a postmortem covering the root causes, the resolution, lessons learned, and a prioritized list of action items, and publish it on the engineering organization’s document portal.**

**Exam Reasoning Explanation**

Two decisions separate the four options, and SRE practice settles both. The first is content: whether the postmortem assigns blame to individuals or focuses on systems and process. The second is audience: whether it goes to one requester or is shared widely so the organization can learn from it. Work through requirement, capability, elimination, decision. The stated context is adopting SRE culture, so blamelessness and shared learning are the standards to apply. Naming people responsible and assigning actions per person fails the first test. Sending it to only one manager fails the second. Only one combination passes both.

**Key Exam Clues**

  * **“Implement SRE culture and principles”** is a hard constraint. It points to blameless postmortems that are shared for learning.

  * **“Formal explanation of what happened”** is a technical signal. The artifact is a postmortem with causes, resolution, lessons learned, and action items.

  * **“Another team ... so they can action remediations”** is a technical signal. The action items must be clear, prioritized, and visible to those who will act.

  * **“The people responsible” and “action items for each person”** is an exclusion signal. It frames the outcome around individuals, which conflicts with blamelessness.

  * **“Share with the manager only” versus “document portal”** is a scoping instruction. It decides whether the learning stays private or is shared broadly.

**Why This Is Correct**

SRE postmortems are written to record impact, causes, the response, what went well and badly, and follow-up actions, and they are blameless. They focus on contributing factors in systems and processes rather than on individuals, because people report problems openly only when they are not punished for them. They are also shared widely, so other teams can learn from the incident and avoid repeating it. A prioritized list of action items tells the receiving team where to start. Publishing on an organization-wide portal gives the requesting manager access while making the learning available to everyone. Option B has the right content and the right audience.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** The content is correct, which makes it tempting, and it does serve the manager’s request. Sending it to one person keeps the lessons from the rest of the organization. SRE treats postmortems as shared learning artifacts, so limiting the audience wastes most of their value.

**Option C — Violates Requirement:** It names the people responsible and assigns actions per person, which makes the document about blame instead of system causes. It also restricts the audience to one manager. It fails on both content and sharing.

**Option D — Violates Requirement:** The audience is right because it is published widely, but naming responsible individuals and assigning per-person actions contradicts blamelessness. It is tempting because it looks accountable and thorough. The effect is that people become less willing to surface problems honestly, which weakens future reliability.

**Exam Trap**

The strongest distractor is option D, because publishing widely is correct and per-person action items look like accountability. The distinction is that SRE places accountability on fixing systems with owned action items, not on assigning fault to people. The answer would switch to D only if the culture were blame-oriented, which contradicts the stated goal. Option A is the second trap, since it satisfies the requester but ignores the shared-learning purpose.

**Foundation Concept**

A blameless postmortem assumes that people acted reasonably on the information they had and that failures reflect gaps in systems, tooling, or process. This encourages honest reporting, which in turn produces better fixes. Wide sharing converts a single team’s incident into organizational knowledge. Action items should be specific, prioritized, and tracked, with owners assigned to the work, not to the fault. This model fits incidents of any size. Genuinely sensitive information, such as security details, may need redaction or restricted sharing, but the default is open and blameless.

**Real-World Connection**

The on-call engineer writes the postmortem with a timeline, root causes, and prioritized actions, and posts it on the engineering portal. The manager’s team picks up the actions relevant to them and tracks them to completion. Other teams read it and check whether they share the same weakness. Over time, engineers report near misses more readily because past postmortems have focused on fixing systems, not on faulting individuals.

**Memory Hook**

A postmortem is blameless and shared widely, with action items for the system and not blame for the people.

**30-Second Exam Takeaway**

When a question asks how to communicate an incident under SRE principles, choose the blameless postmortem shared broadly. Reject versions that name people responsible or keep the document private.

**Official References**

[Google SRE Book — Postmortem Culture: Learning from Failure: ](https://sre.google/sre-book/postmortem-culture/)Supports: blameless postmortems focused on systems and process, with wide sharing for organizational learning, which supports option B and rules out options A, C, and D.

[Google SRE Workbook — Postmortem Culture: Learning from Failure: ](https://sre.google/workbook/postmortem-culture/)Supports: postmortem content such as root causes, impact, lessons learned, and action items, and the practice of sharing them openly.

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 3, Applying site reliability engineering practices):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with managing the service lifecycle and mitigating incident impact on users.

---

## Question 54

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You support a Node.js application that runs in production on Google Kubernetes Engine (GKE). The application sends several HTTP requests to other applications that it depends on. You want to anticipate which of those dependencies could cause performance problems. What should you do?

- [ ] A. Instrument all of the applications with Cloud Profiler.
- [x] B. Instrument all of the applications with Cloud Trace, and review the HTTP requests between services.
- [ ] C. Use Cloud Debugger to examine how the logic runs inside each application, and instrument all of the applications.
- [ ] D. Modify the Node.js application to log the time of each HTTP request and response to its dependencies, and use Cloud Logging to find the dependencies that perform poorly.

### Explanation

**Correct Answer**

**B. Instrument all of the applications with Cloud Trace, and review the HTTP requests between services.**

**Exam Reasoning Explanation**

The goal is to see which dependencies are slow, which is a question about time spent across service boundaries. Start by naming the signal you need: the latency of each call between services, attributed to the service that handled it. Then match each option to the signal it produces. Some tools look inside a single process, one produces partial and manual data from only one side, and one is built to follow a request across services and show where time goes. Work through requirement, capability, elimination, decision, and the cross-service tool is the only one that answers the question directly.

**Key Exam Clues**

  * **“Several HTTP requests to dependent applications”** is a technical signal. The performance risk sits in calls between services, so the data must follow requests across them.

  * **“Anticipate which dependent applications might cause performance issues”** is a hard constraint. You need comparative latency by dependency, not a single application’s internals.

  * **“Instrument all applications”** is a technical signal in the options. Tracing the full chain requires every service to participate so spans connect into one trace.

  * **“Running in production on GKE”** is a context signal. The solution must work on live traffic with low overhead and without code stepping.

**Why This Is Correct**

Cloud Trace is a distributed tracing system that records how long a request takes and how long each operation within it takes, including calls to other services. When each application is instrumented, the spans from each service join into a single trace, and the trace view shows which downstream call consumed the time. You can compare latency by dependency and see changes over time, which lets you spot dependencies that are getting slower before they cause outages. Node.js is supported, and OpenTelemetry libraries with a Cloud Trace exporter are the common way to instrument. One boundary: tracing shows where time is spent but not why a function is slow, so a profiler is the follow-up tool for in-process causes.

**Why the Other Options Are Not the Best Fit**

**Option A — Different Use Case:** A profiler samples CPU and memory use of the code within a single application. It is tempting because it is a performance tool that can be added to every application. It shows which functions consume resources, not how long calls between services take, so it cannot rank dependencies by latency.

**Option C — Outdated:** Cloud Debugger inspected the state of a running application at selected code locations. It is tempting because it appears to show what each application is doing. It is a debugging tool for application state, not a measure of inter-service latency, and the service was shut down in May 2023, so it is no longer available.

**Option D — Technically Possible but Not Best:** Logging request and response times can show how long the Node.js application waits for each dependency, so it can work. It is tempting because it uses a familiar tool. It requires modifying the application and measures only the caller’s view, so you have no breakdown of where time goes inside the dependencies. Correlating logs across services is manual and does not give a request-level, end-to-end picture.

**Exam Trap**

The strongest distractor is option D, because logging call durations feels like a direct way to rank dependencies. The distinction is that it gives one side of each call, requires code changes, and needs manual correlation, while tracing is built for end-to-end request paths. The answer would switch to D only if tracing instrumentation were not possible for the application. Option A is the second trap, since profiling sounds like performance analysis but looks inside one process. A terminology note: Cloud Debugger has been shut down, and the open source Snapshot Debugger is an archived alternative, so option C is outdated as well as a different use case.

**Foundation Concept**

Distributed tracing follows a request through every service it touches and records a span for each operation, linked by a shared trace identifier propagated in request headers. This lets you see the critical path and attribute latency to specific services. Profiling, logging, and debugging each answer different questions: profiling shows resource use in code, logging records discrete events, and debugging inspects state. Tracing is the right tool when the question is where time goes across a chain of calls. It requires instrumentation in each service, or the trace breaks at the uninstrumented hop.

**Real-World Connection**

A team adds the OpenTelemetry SDK with the Cloud Trace exporter to each service, deploys it, and reviews the trace heatmap and the slowest traces in the console. They notice that one dependency’s latency creeps up during peak hours, and they raise it with its owner and add capacity before it breaches the service objective. Sampling keeps the overhead small in production, and linking trace identifiers to logs helps with root-cause analysis.

**Memory Hook**

To find which dependency is slow, trace the request across services, and use a profiler only for what happens inside one service.

**30-Second Exam Takeaway**

When a question asks which service in a call chain is slow, choose distributed tracing across all services. Reject profilers, debuggers, and one-sided logging that cannot give an end-to-end latency breakdown.

**Official References**

[**Google Cloud — Cloud Trace overview:**](https://docs.cloud.google.com/trace/docs/overview) Supports: Trace recording how long requests and operations such as calls to other services take, the Node.js and OpenTelemetry support, and trace and span analysis for latency, which supports option B.

[**Google Cloud Observability — Cloud Debugger deprecation:**](https://docs.cloud.google.com/stackdriver/docs/deprecations/debugger-deprecation) Supports: Cloud Debugger having been deprecated and shut down on May 31, 2023, which marks option C as outdated.

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 4, Implementing observability practices and troubleshooting issues):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with capturing and analyzing distributed traces using tracing frameworks such as OpenTelemetry.

---

## Question 55

*Domain 2: Building and Implementing CI/CD Pipelines*

Your organization provisions a Compute Engine managed instance group (MIG) through a Terraform-based CI/CD pipeline. The MIG runs an application using an instance template that generates unique names with `name_prefix`. The MIG’s Terraform resource directly references that template resource.

After you modify the machine type in the instance-template configuration, `terraform apply` fails with this error:
    
          1. Error waiting for Deleting Instance Template:
      2. The instance_template resource
      3. 'projects/example-project/global/instanceTemplates/app-template-202610310001'
      4. is already being used by
      5. 'projects/example-project/regions/us-central1/instanceGroupManagers/app-mig'

You must replace the template and update the MIG to reference its replacement while minimizing application disruption and additional pipeline executions.

Which action should you take?

- [ ] **A.** Destroy the MIG, replace the instance template with one containing the new machine type, and recreate the MIG using the replacement template.
- [ ] **B.** Perform separate pipeline executions to provision another instance template, switch the MIG to that template, and remove the previous template.
- [ ] **C.** Temporarily remove the MIG from Terraform state, apply the template replacement, and import the existing MIG back into state afterward.
- [x] **D.** Configure `create_before_destroy = true` inside a `lifecycle` block on the instance-template resource, and run the pipeline again.

### Explanation

**Correct Answer**

**D. Add a**`**lifecycle**`**block to the instance-template resource and set**`**create_before_destroy = true**`**, then rerun the pipeline.**

**Exam Reasoning Explanation**

The error identifies a replacement-ordering problem: Terraform attempts to delete a template that the MIG still references. Preserve the MIG and let Terraform coordinate the replacement within one apply operation. D addresses that ordering directly; A unnecessarily rebuilds the group, B requires additional runs, and C changes state bookkeeping without removing the cloud dependency.

**Key Exam Clues**

  * **“Already being used by” — Technical signal:** The existing MIG reference blocks template deletion.

  * **“**`**name_prefix**`**” — Technical signal:** The original and replacement templates can coexist under different names.

  * **“Directly references the template resource” — Technical signal:** Terraform can track the dependency and update the reference.

  * **“Minimizing application disruption” — Preference:** Avoid tearing down the MIG.

  * **“Number of pipeline runs” — Preference:** Prefer dependency-aware replacement within one apply.

**Why This Is Correct**

Instance templates are immutable, so changing the machine type requires a replacement. Add this block inside the existing instance-template resource:
    
          1. lifecycle {
      2.   create_before_destroy = true
      3. }

With the stated unique naming and direct reference, Terraform can:

  1. Create the replacement template.

  2. Update the MIG to reference it.

  3. Delete the original template after the reference changes.

The Google provider documentation explicitly recommends this configuration for instance templates used by instance group managers. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** Rebuilding the group removes the dependency but unnecessarily disrupts application capacity. Replacing the template does not require destroying the MIG.

  * **Option B — Technically Possible but Not Best:** The sequence is valid, but splitting it across pipeline runs adds coordination and intermediate configurations. D lets Terraform manage the required ordering declaratively.

  * **Option C — Incorrect:** Removing the MIG from state leaves the actual group and its template reference intact. The deletion blocker remains. If the MIG configuration stays present, Terraform can also plan to create another group, potentially encountering an existing-name conflict. 

**Exam Trap**

B describes the right operational sequence but misses that Terraform can execute it within one apply. Separate runs become reasonable when a changed requirement mandates independently approved creation, cutover, and cleanup stages.

Also, `**create_before_destroy**`**does not guarantee a disruption-free rollout of the new machine type to every existing VM** ; that depends on the MIG’s update configuration. 

**Foundation Concept**

Distinguish **replacement ordering** , **resource naming** , and **workload rollout**. Lifecycle rules control replacement ordering; unique names permit old and new resources to coexist; the MIG’s update policy controls how existing VMs adopt the new configuration. A fixed conflicting name could prevent creation even with `create_before_destroy` enabled. 

**Real-World Connection**

Use the lifecycle fix alongside an appropriate proactive MIG update policy when existing VMs must receive the new machine type automatically. Configure surge capacity, availability limits, and health checks to control disruption. Additional surge VMs require available capacity and can temporarily increase compute costs. 

**Memory Hook**

For an immutable resource with live dependents: create its replacement, redirect the dependents, then retire the original.

**30-Second Exam Takeaway**

When Terraform cannot delete an in-use template, look for `create_before_destroy`, compatible unique naming, and a direct resource reference. Resolve the dependency ordering while treating the application’s rolling update as a separate concern.

**Official References**

[**Terraform Google Provider — Instance Templates: Using with Instance Group Manager**](https://github.com/hashicorp/terraform-provider-google/blob/main/website/docs/r/compute_instance_template.html.markdown)

Supports: Template immutability, unique naming, and the create–update–delete sequence.

[**HashiCorp Terraform — Lifecycle Reference**](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle)

Supports: `create_before_destroy` behavior and coexistence constraints.

[**HashiCorp Terraform — terraform state rm**](https://developer.hashicorp.com/terraform/cli/commands/state/rm)

Supports: Why removing state does not remove the actual MIG or its cloud dependencies.

[**Google Compute Engine — Automatically Apply VM Configuration Updates in a MIG**](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups)

Supports: Proactive versus opportunistic updates, disruption controls, and surge-capacity trade-offs.

---

## Question 56

*Domain 3: Applying Site Reliability Engineering Practices*

You are leading a DevOps transformation for an organization that operates a production service. The DevOps team maintains the service infrastructure and handles on-call incidents. The Software Development team authors, submits, and reviews application code. Neither team has documented or published service level objectives (SLOs).

You want both teams to share accountability for service reliability. Which assignment of responsibilities best establishes this operating model?

- [ ] **A.**
    **DevOps team:** Maintain the infrastructure, handle on-call incidents, and review application code.
    **Software Development team:** Author and submit code for DevOps review, and unilaterally establish and publish SLOs that DevOps is responsible for achieving.
- [ ] **B.**
    **DevOps team:** Maintain the infrastructure and review application code.
    **Software Development team:** Author and submit code for DevOps review, assume all on-call responsibilities, and unilaterally establish and publish SLOs that DevOps is responsible for achieving.
- [x] **C.**
    **DevOps team:** Maintain the service infrastructure.
    **Software Development team:** Author and submit application code for review.
    **Both teams:** Review application code, participate in a shared on-call rotation, and collaboratively define, agree to, and publish the service’s SLOs.
- [ ] **D.**
    **DevOps team:** Maintain the infrastructure and retain all on-call responsibilities.
    **Software Development team:** Author, submit, and review application code, and establish and publish the service’s SLOs independently.

### Explanation

**Correct Answer**

**C.**

  * **DevOps team: Manage the service infrastructure.**

  * **Software Development team: Write and submit application code for review.**

  * **Both teams: Participate in code reviews, share on-call incident support through a rotation, and jointly agree on, adopt, and publish SLOs for the service.**

**Exam Reasoning Explanation**

The decisive requirement is **shared accountability for reliability**. Look for collaboration across preventive work, incident response, and reliability targets. C addresses all three; A, B, and D retain unilateral SLO decisions and assign incident support exclusively to one team.

**Key Exam Clues**

  * **“Joint-ownership model” — Hard constraint:** Both teams must participate in reliability responsibilities and decisions.

  * **“Neither team has published…SLOs” — Technical signal:** The model must establish explicit, agreed reliability targets.

  * **“Both teams…take responsibility” — Hard constraint:** Moving operational duties entirely from one team to the other is insufficient.

**Why This Is Correct**

C connects development decisions with production outcomes. Shared reviews bring application and operational knowledge into changes; shared on-call participation exposes both teams to production problems; jointly accepted SLOs establish a common reliability goal. Google’s SRE guidance explicitly supports shared service ownership between development and SRE teams. 

The rotation should include appropriate training, runbooks, and escalation paths so participants can respond effectively and sustainably. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Adding operational expertise to code review is useful, but developers remain outside on-call support and impose targets on DevOps without joint agreement. Collaboration in one activity does not establish the requested ownership model.

  * **Option B — Violates Requirement:** Developer on-call participation is valuable, but this option transfers **all** incident support to developers while leaving SLO achievement assigned to DevOps. It redistributes duties without establishing shared reliability decisions.

  * **Option D — Violates Requirement:** This preserves the existing separation between application development and production support. Publishing SLOs adds documentation, but unilateral target setting leaves the teams without a jointly accepted reliability commitment.

Google’s SLO guidance calls for agreement among product stakeholders, developers, and the team responsible for production reliability. That directly distinguishes C from all three distractors. 

**Exam Trap**

**Transferring the pager is not the same as sharing ownership.** Developer-only on-call can be appropriate for a developer-operated service, but B still retains unilateral SLO decisions and divided accountability. Its operational reassignment does not satisfy this scenario.

**Foundation Concept**

Shared ownership combines **common outcomes, agreed decision rules, and participation in maintaining the service**. Teams can retain specialist responsibilities—such as infrastructure administration—while sharing reliability accountability. An SLO defines the reliability target; an agreed error-budget policy helps translate that target into decisions about feature delivery and reliability work. 

**Real-World Connection**

A service team can introduce a trained rotation spanning developers and DevOps, review production incidents together, and prioritize corrective work using agreed reliability goals. This gives developers direct operational feedback and creates a path for recurring incidents to become engineering improvements rather than repeated support work. 

**Memory Hook**

**Shared reliability ownership means shared targets, shared operational feedback, and shared improvement work.**

**30-Second Exam Takeaway**

For joint-ownership questions, select the model that combines collaborative engineering, shared incident responsibility, and mutually accepted SLOs. Specialist duties can remain separate while accountability for the service is shared.

**Official References**

[**Google SRE Workbook — How SRE Relates to DevOps**](https://sre.google/workbook/how-sre-relates/)

Supports: Shared service ownership, collaboration, and reducing organizational silos.

[**Google SRE Workbook — Implementing SLOs**](https://sre.google/workbook/implementing-slos/)

Supports: Stakeholder agreement, documented SLOs, and error-budget policies; explains why unilateral target setting weakens the alternatives.

[**Google SRE Workbook — On-Call**](https://sre.google/workbook/on-call/)

Supports: Developer participation in production support, sustainable rotations, training, and escalation procedures.

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)

Supports: Domain alignment with “Applying site reliability engineering practices,” particularly objective 3.1 concerning reliability and SLOs.

---

## Question 57

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

An organization operates two applications in separate Google Cloud projects for development, staging, and production. The projects are grouped by environment:

  * **Development folder:** `app-one-dev` and `app-two-dev`

  * **Staging folder:** `app-one-staging` and `app-two-staging`

  * **Production folder:** `app-one-prod` and `app-two-prod`

You must provide dashboards for each environment that show metrics from both projects in that environment and omit metrics from the other environments.

Which configuration of scoping projects and metrics scopes best follows Google’s recommended practices?

- [ ] **A.** Provision a single dedicated monitoring project, include all six workload projects in its metrics scope, and store every environment’s dashboards in that project.
- [x] **B.** Provision a dedicated monitoring project for each environment folder. Include only that environment’s two workload projects in its metrics scope, and store the environment’s dashboards in the corresponding monitoring project.
- [ ] **C.** Designate `app-one-prod` as the organization’s central scoping project. Add the remaining five workload projects to its metrics scope, and store all environment dashboards there.
- [ ] **D.** Designate `app-one-dev`, `app-one-staging`, and `app-one-prod` as their environments’ scoping projects. Add the matching `app-two` project to each metrics scope, and store the dashboards in those existing workload projects.

### Explanation

**Correct Answer**

**B. Create a new, dedicated scoping project for each folder. Add only that folder’s two workload projects to the corresponding metrics scope, and create its dashboards in that scoping project.**

**Exam Reasoning Explanation**

First identify the required grouping: **both applications together, with separate views for each environment**. Then apply the architectural preference: Google recommends a new project, or one without resources, as the scoping project for cross-project monitoring. B combines the intended grouping with that recommendation. 

**Key Exam Clues**

  * **“Both projects in the corresponding folder” — Hard constraint:** Each environment’s view must cover both applications.

  * **“Exclude metrics…in the other folders” — Hard constraint:** Dashboards must avoid mixing environments.

  * **“Google-recommended practices” — Selection criterion:** Distinguish a technically functional configuration from the recommended scoping-project design.

**Why This Is Correct**

B creates three dedicated monitoring hosts, each with the appropriate workload membership:

  * **Development:** Add `app-one-dev` and `app-two-dev`.

  * **Staging:** Add `app-one-staging` and `app-two-staging`.

  * **Production:** Add `app-one-prod` and `app-two-prod`.

Dashboard configurations reside in their respective scoping projects. Each scope also includes its own scoping project; the two workload projects are its additional monitored projects. Keeping these hosts free of application workloads follows Google’s documented recommendation. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** A central dedicated project supports cross-project monitoring. However, its scope includes every environment, so environment-specific charts require appropriate filtering. It would better fit a requirement for consolidated visibility across all environments.

  * **Option C — Technically Possible but Not Best:** This also permits centralized monitoring with filters, but additionally uses an application’s production project as the monitoring host instead of a dedicated project.

  * **Option D — Technically Possible but Not Best:** This can satisfy the environment-specific display requirement. Existing workload projects can host metrics scopes, but this choice does not follow the recommendation to use new or resource-free scoping projects. **Its weakness is the architectural preference, not technical impossibility.**

**Exam Trap**

Do not assume that an existing project cannot be a scoping project. D works technically. Also, A can produce environment-specific dashboards with filters; **B is the best match to the stated recommendation, rather than the only functional design**. Google does not require one metrics scope per folder universally.

**Foundation Concept**

A **scoping project** hosts monitoring configuration; its **metrics scope** determines which projects’ metrics are available for charting. Chart filters further narrow that available data.

Ordinary folder organization does not automatically configure scope membership. **App-enabled folders** have a separate management-project mechanism that can synchronize membership; the question does not specify that setup. 

**Real-World Connection**

Create a dedicated production monitoring project, add the two production workload projects, and save the production dashboards there. When another production workload project is introduced, explicitly update the scope so its metrics become available. This makes the monitoring membership an intentional configuration choice. 

**Memory Hook**

Use dedicated scoping projects and match monitored-project membership to the intended monitoring boundary.

**30-Second Exam Takeaway**

For cross-project monitoring questions, distinguish **scope membership** , **dashboard filtering** , and **the choice of monitoring host**. Here, dedicated hosts with environment-specific membership make B the strongest answer.

**Official References**

[**Google Cloud Monitoring — Metrics scopes overview**](https://docs.cloud.google.com/monitoring/settings)

Supports: Scoping-project behavior, dashboard ownership, filtering, and the recommendation for new or resource-free scoping projects.

[**Google Cloud Monitoring — Configure a metrics scope**](https://docs.cloud.google.com/monitoring/settings/multiple-projects)

Supports: Explicitly adding monitored projects and controlling which projects’ metrics are available.

[**Google Cloud Monitoring — Metrics scopes for app-enabled folders**](https://docs.cloud.google.com/monitoring/settings/metrics-scope-app-enabled-folders)

Supports: The distinction between ordinary folders and automatically managed scopes for app-enabled folders.

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)

Supports: Domain alignment with objective 1.1, which explicitly includes multi-project monitoring and logging.

---

## Question 58

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

Your organization requires developers on the same team to use a standardized development environment that supports commonly used integrated development environments (IDEs). You are responsible for maintaining software updates and security patches for these environments.

Which Google-recommended approach should you use to provide a consistent development environment for each team?

- [ ] A. Take daily Compute Engine snapshots of a fully patched “golden” VM and make them available for developers to update their machines.
- [ ] B. Publish a software-update checklist and supporting scripts, and have developers apply the updates to their machines.
- [ ] C. Build an image containing the latest dependencies and install it on developers’ laptops.
- [x] D. Define a Cloud Workstations configuration for each development team.

### Explanation

**Correct Answer**

**D. Define a Cloud Workstations configuration for each development team.**

**Exam Reasoning Explanation**

The requirements combine a shared environment template, IDE support, and ongoing maintenance. The appropriate solution must provide a reproducible baseline and a reliable way to distribute changes. D provides managed workstation templates; A, B, and C leave environment adoption or subsequent maintenance dependent on individual machine-update workflows.

**Key Exam Clues**

  * **“Developers on the same team” — Hard constraint:** Standardization must support team-specific requirements.

  * **“Standardized development environment” — Technical signal:** Look for a reusable configuration that defines the environment.

  * **“Commonly used … IDEs” — Hard constraint:** The solution must support developer tooling.

  * **“Maintaining software updates and security patches” — Hard constraint:** Initial provisioning alone does not satisfy the full lifecycle requirement.

**Why This Is Correct**

Cloud Workstations configurations act as templates. They define the container image, IDE, machine settings, and storage used by developers’ workstations. Administrators share a configuration with a team, and developers create their individual workstations from that common definition. Configuration changes apply when the workstations next start. 

For patch maintenance, use updated base images, regularly rebuild custom images, and configure a running timeout to support refreshes between sessions. **Custom packages and dependencies remain the organization’s responsibility** ; selecting Cloud Workstations does not automatically maintain every added dependency. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Different Use Case:** Snapshots capture disk contents and support restoration. A snapshot of a patched machine preserves a useful baseline, which makes this approach tempting. However, publishing snapshots does not ensure that developers adopt them or keep their environments synchronized. Snapshots primarily address disk backup and recovery. 

  * **Option B — Technically Possible but Not Best:** Checklists and scripts can document and automate updates. However, the proposed process relies on developers executing them correctly and consistently. It provides no managed provisioning or refresh mechanism to maintain the required team baseline.

  * **Option C — Technically Possible but Not Best:** A common laptop image can standardize the initial installation. However, the option does not establish an ongoing process for distributing patches and maintaining consistency after installation. Laptop imaging would require additional endpoint-management processes.

**Exam Trap**

A common image can establish consistency at installation time, but ongoing consistency also requires a maintained update process. If the task were limited to provisioning an initial software baseline on laptops, C would fit.

**Foundation Concept**

A reproducible development environment combines an approved template with a controlled lifecycle: define the tools and dependencies, provision environments from that definition, update it, and refresh the environments. A shared starting point alone does not prevent configuration drift.

**Real-World Connection**

A platform team maintains a Java development image containing the approved JDK, IDE, and build tools. After validating a security update, it publishes the revised image and updates the team’s workstation configuration. Refreshing workstations through this process reduces individual setup work and machine-specific build differences.

**Memory Hook**

Team-wide development consistency requires a shared template and a managed refresh process.

**30-Second Exam Takeaway**

When a question combines standardized developer environments, IDE support, and ongoing updates, look for Cloud Workstations configurations. Remember that updates require workstation refreshes and that custom dependencies still need maintenance.

**Official References**

  * **Google Cloud — Cloud Workstations overview**

Supports: Configuration templates, IDE access, team provisioning, and application of configuration changes.

[Official documentation](https://docs.cloud.google.com/workstations/docs/overview)

  * **Google Cloud — Cloud Workstations security best practices**

Supports: Updated base images, running timeouts, custom-image rebuilds, and responsibility for added dependencies.

[Official documentation](https://docs.cloud.google.com/workstations/docs/set-up-security-best-practices)

  * **Google Cloud — About archive and standard disk snapshots**

Supports: Snapshot backup and restoration capabilities and the distinction relevant to option A.

[Official documentation](https://docs.cloud.google.com/compute/docs/disks/snapshots)

  * **Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide**

Supports: Objective 1.5, enabling secure cloud development environments using tools such as Cloud Workstations. [services.google.com](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)

---

## Question 59

*Domain 3: Applying Site Reliability Engineering Practices*

An application running on Google Kubernetes Engine (GKE) uses separate blue and green Deployments in the same namespace. Production traffic reaches the application through an Ingress and a Service. The relevant manifest excerpts are:
    
          1. apiVersion: apps/v1
      2. kind: Deployment
      3. metadata:
      4.   name: app-green
      5. spec:
      6.   selector:
      7.     matchLabels:
      8.       app: my-app
      9.       version: green
      10.   template:
      11.     metadata:
      12.       labels:
      13.         app: my-app
      14.         version: green
      15.     # Container configuration omitted.
      16. ---
      17. apiVersion: apps/v1
      18. kind: Deployment
      19. metadata:
      20.   name: app-blue
      21. spec:
      22.   selector:
      23.     matchLabels:
      24.       app: my-app
      25.       version: blue
      26.   template:
      27.     metadata:
      28.       labels:
      29.         app: my-app
      30.         version: blue
      31.     # Container configuration omitted.
      32. ---
      33. apiVersion: v1
      34. kind: Service
      35. metadata:
      36.   name: app-svc
      37. spec:
      38.   selector:
      39.     app: my-app
      40.     version: green
      41.   ports:
      42.     - port: 80
      43.       targetPort: 8080
      44. ---
      45. apiVersion: networking.k8s.io/v1
      46. kind: Ingress
      47. metadata:
      48.   name: app-ingress
      49. spec:
      50.   defaultBackend:
      51.     service:
      52.       name: app-svc
      53.       port:
      54.         number: 80

The green Deployment is serving a newly released application version. Monitoring now indicates widespread request failures that were not observed during testing. The blue Deployment continues to run the previous stable version, is healthy, and already has enough capacity to serve production traffic.

You must restore service promptly while keeping the failing release running for developer investigation.

Which action best meets these requirements?

- [ ] **A.** Deploy the failing application version from `app-green` to `app-blue` as well.
- [ ] **B.** Revert the application version running in `app-green` to the previous stable release.
- [ ] **C.** Broaden the `app-svc` selector by removing `version: green` and retaining only `app: my-app`.
- [x] **D.** Change the `app-svc` selector to require `app: my-app` and `version: blue`.

### Explanation

**Correct Answer**

**D. Update the**`**app-svc**`**selector to match both**`**app: my-app**`**and**`**version: blue**`**.**

**Exam Reasoning Explanation**

Recovery must satisfy two constraints: use the already healthy release and preserve the failing release for investigation. Changing the Service selector redirects production traffic without requiring an application rollout. D satisfies both constraints; replacing either Deployment or admitting both versions into the backend pool does not.

**Key Exam Clues**

  * **“Blue/green deployment strategy” — Technical signal:** A separate release environment is available for traffic switching.

  * **“Previous stable release…healthy…sufficient capacity” — Technical signal:** Blue can accept production traffic without first being rebuilt or scaled.

  * **“Restore service quickly” — Preference:** Reuse the prepared environment.

  * **“Preserving the failing release” — Hard constraint:** Keep the green workload available for investigation.

  * **The Service selects**`**version: green**`**— Technical signal:** This selector is the relevant traffic-switching control.

**Why This Is Correct**

Change the Service’s selector to:
    
          1. spec:
      2.   selector:
      3.     app: my-app
      4.     version: blue

Both requirements must match, selecting blue Pods and excluding green Pods. Kubernetes reconciles the Service’s EndpointSlices with the matching Pods. The Ingress still references `app-svc` on port `80`, while neither Deployment’s Pod template changes. Green therefore remains available for investigation.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Incorrect:** Updating blue to the failing version removes the prepared stable fallback. It also leaves the production Service selecting green, so it does not perform the required recovery.

  * **Option B — Violates Requirement:** A Deployment rollback can restore an earlier Pod template, but it changes the failing workload and can replace its running Pods. That conflicts with preserving the running release for investigation and requires a rollout that D avoids. 

  * **Option C — Violates Requirement:** Both Deployments’ Pods have `app: my-app`. Removing the version requirement makes both colors eligible backends, so requests can continue reaching the failing green release. This does not establish an exclusive switch to stable blue. 

**Exam Trap**

Distinguish **rolling back traffic** from **rolling back a Deployment**. D switches traffic to an existing stable environment. B modifies the failing environment itself. Keeping the failing workload running makes the traffic switch the stronger recovery action.

**Foundation Concept**

A Deployment controls the desired workload; a Service selector determines which Pods belong to its backend set. These controls are separate: changing Service membership does not trigger a Deployment rollout. Blue and green are labels—their operational roles come from the deployed versions and current routing configuration. 

**Real-World Connection**

After applying the selector change, verify that `app-svc` resolves to blue backends and that production error rates recover. Developers can investigate green without rebuilding it. Allow for controller and load-balancer reconciliation rather than assuming the cutover completes instantaneously.

**Memory Hook**

When a healthy standby is ready, switch the Service selector to recover while preserving the failing workload.

**30-Second Exam Takeaway**

For blue/green incident recovery, identify the healthy environment and the object selecting production backends. Switch routing to the stable version while keeping the failing Deployment intact; broadening a selector admits additional versions rather than replacing the failing backend set.

**Official References**

[**Kubernetes — Service**](https://kubernetes.io/docs/concepts/services-networking/service/)

Supports: Pod selection and automatic reconciliation of Service EndpointSlices.

[**Kubernetes — Labels and Selectors**](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)

Supports: AND semantics across selector requirements and why removing the version requirement admits both colors.

[**Kubernetes — Deployments**](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

Supports: Pod-template rollouts and the distinction between Deployment rollback and Service traffic switching.

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)

Supports: Objective 3.3, mitigating incident impact through traffic redirection and rollback strategies.

---

## Question 60

*Domain 3: Applying Site Reliability Engineering Practices*

You are responding to an incident affecting an inventory-update microservice deployed on a Google Kubernetes Engine (GKE) Autopilot cluster.

An online retailer publishes order events to Pub/Sub. Multiple replicas of the microservice can consume events from the same pull subscription and process inventory updates concurrently in a warehouse system.

A promotional campaign causes a sudden increase in orders. Inventory updates become delayed, and customers can place orders for products that have already sold out. Monitoring shows these changes from normal operation:

  * **Average Pod CPU utilization:** Normally 20% of the CPU limit; currently 30%.

  * **Average Pod memory utilization:** Normally 10% of the memory limit; currently 10%.

  * **Average oldest unacknowledged message age:** Normally 347 milliseconds; currently 8,074 milliseconds.

  * **Average undelivered message count:** Normally 5 messages; currently 14,705 messages.

  * **Average acknowledgment latency:** Normally 312 milliseconds; currently 354 milliseconds.

Which action should you take to reduce inventory-processing delays while minimizing customer impact?

- [ ] **A.** Shorten the Pub/Sub subscription’s acknowledgment deadline.
- [ ] **B.** Add a virtual waiting room that limits incoming store traffic to its normal pre-campaign rate.
- [x] **C.** Scale out the inventory-processing microservice by increasing its Pod replica count.
- [ ] **D.** Raise the CPU and memory limits configured for each inventory-processing Pod.

### Explanation

**Correct Answer**

**C. Increase the number of Pod replicas running the inventory-processing microservice.**

**Exam Reasoning Explanation**

The sharp increases in backlog size and message age indicate that aggregate consumer throughput is insufficient for the increased order volume. CPU and memory measurements do not show corresponding pressure against their reported limits.

Because processing can be distributed across replicas, increasing the number of consumers directly addresses the throughput shortfall while allowing customers to continue shopping. Google recommends adding subscriber processes or containers when backlog count and age increase together. 

**Key Exam Clues**

  * **“Shared pull subscription” — Technical signal:** Additional subscriber replicas can participate in processing the same backlog.

  * **“Distributed across multiple Pod replicas” — Technical signal:** Horizontal scaling is explicitly supported.

  * **Backlog count and oldest-message age increase sharply — Technical signal:** Consumers are falling behind incoming work.

  * **CPU reaches only 30%; memory remains at 10% — Technical signal:** Increasing per-Pod resource limits is not supported by the reported averages.

  * **“Minimize…impact on customers” — Preference:** Increase processing capacity before introducing customer-facing admission restrictions.

**Why This Is Correct**

Additional Pods provide more subscriber workers, increasing potential concurrent message processing. This can increase inventory-update throughput and drain the backlog.

The important boundary is downstream capacity: the warehouse system, connection pools, and other shared dependencies must accommodate the additional concurrency. Scale and verify that completed processing increases and backlog age falls; these measurements do not establish an exact replica count. GKE supports horizontal Pod autoscaling on Autopilot, including scaling from external metrics. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Incorrect:** The acknowledgment deadline governs when an unacknowledged message becomes eligible for redelivery. Shortening it does not add processing capacity and can increase redelivery and repeated work if messages are still being processed. 

  * **Option B — Technically Possible but Not Best:** Admission control can reduce incoming demand, but it delays customers and does not increase consumer throughput. It becomes more appropriate if a hard downstream capacity limit prevents effective scaling.

  * **Option D — Technically Possible but Not Best:** More resources per Pod can help resource-constrained workers. Here, reported utilization is well below the limits, while the workload explicitly supports additional replicas. Raising limits alone does not necessarily increase subscriber concurrency.

**Exam Trap**

**Low CPU utilization does not imply sufficient application throughput.** Consumers can fall behind because concurrency is limited or workers spend time waiting for I/O.

Conversely, averages do not conclusively rule out individual overloaded Pods or downstream bottlenecks. C is the strongest action from the supplied evidence, followed by verification that scaling improves throughput.

**Foundation Concept**

Horizontal scaling adds workers; vertical scaling increases resources available to each worker. A backlog shrinks when aggregate successful processing exceeds incoming work long enough to catch up.

Also, the question reports CPU utilization relative to **limits**. Percentage-based CPU targets in an HPA use **requests** , so the reported 30% should not be treated as an HPA target measurement.

**Real-World Connection**

Increase consumer replicas during the incident, then configure HPA using backlog signals alongside a complementary signal such as resource utilization. Google recommends multiple scaling signals and regional Pub/Sub backlog metrics for resilience. Bound scaling by tested downstream capacity to avoid moving the bottleneck into the warehouse system. 

**Memory Hook**

Growing backlog plus parallelizable consumers suggests adding workers, even when CPU utilization is modest.

**30-Second Exam Takeaway**

When backlog size and age rise together, compare consumer throughput with demand. If processing can run across replicas and per-Pod resource exhaustion is not evident, scale consumers horizontally and confirm that the backlog begins draining.

**Official References**

[**Google Cloud Pub/Sub — Monitor Pub/Sub in Cloud Monitoring**](https://docs.cloud.google.com/pubsub/docs/monitoring)

Supports: Backlog diagnosis, adding subscriber containers, and acknowledgment-deadline redelivery behavior.

[**Google Kubernetes Engine — Horizontal Pod Autoscaling**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler)

Supports: Autopilot workload scaling, external metrics, and request-based utilization targets.

[**Google Cloud Pub/Sub — Best Practices for Using Pub/Sub Metrics as a Scaling Signal**](https://docs.cloud.google.com/pubsub/docs/metrics-autoscaling-best-practices)

Supports: Multiple scaling signals and recommended regional backlog metrics.

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)

Supports: Objective 3.3, mitigating incident impact by adding capacity, and objective 3.2 on autoscaling.

---
