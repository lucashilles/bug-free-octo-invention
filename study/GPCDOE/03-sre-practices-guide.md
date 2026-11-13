# Domain 3 Study Guide — Applying Site Reliability Engineering Practices

> Condensed from the 77-question bank in [`03-sre-practices.md`](03-sre-practices.md). Citations look like (Exam N · QM). Some questions appear in more than one exam, so look for the paired citations.

---

## 1. SLIs: what to measure and where to measure it

### Key concepts
- **SLI = good events / valid events.** The denominator must cover the same scope as the SLI. For a home page latency SLI, count home page requests under 100 ms and divide by **home page requests only**, not by all app requests (Exam 1 · Q47).
- An SLI measures **what users get**, not what a backend is doing. Queue size, I/O wait and PD throughput are *causes*. The availability SLI is the share of report requests that return a successful response (Exam 2 · Q38).
- **Availability as a ratio, not a count.** "Successful API calls ÷ attempted API calls" beats "successful uploads per minute", because the per-minute count is throughput (Exam 3 · Q29).
- **Separate SLIs for separate expectations.** "99.9% available and ≤200 ms for 95% of requests" calls for an availability SLO and a latency SLO, each built on its own SLI and monitored in Cloud Monitoring (Exam 3 · Q17).

### SLI type selector

| Scenario wording | SLI type | Source |
|---|---|---|
| Page is served but **some widgets are missing**, or the response is degraded or partial | **Quality**: non-degraded responses / total responses | (Exam 1 · Q25) |
| Requests fail or return 5xx | **Availability**: successful / valid requests | (Exam 2 · Q38), (Exam 3 · Q29) |
| "Fast enough": N ms threshold | **Latency**: requests under threshold / valid requests | (Exam 1 · Q47) |
| Data updated recently enough (pipelines) | **Freshness**. A distractor when the issue is incomplete content | (Exam 1 · Q25) |

### Where to measure

| Requirement | Measure at | Reject | Source |
|---|---|---|---|
| User's view, **no app code changes** | **Synthetic clients** plus **existing request logs** | "Add new metrics" (that needs instrumentation), modifying code, "**only** proxy logs" (too narrow) | (Exam 1 · Q14) |
| Catch **CDN, LB misconfiguration or global network** failures | **Client-side instrumentation** plus a **synthetic client** | Server logs, server metrics and GKE health checks share the LB SLI's blind spot | (Exam 1 · Q34) |

### Decision rules
- If the service returns "something, but incomplete", choose a **quality** SLI (Exam 1 · Q25).
- If an option counts infra health ("healthy microservices / total microservices"), reject it. That is backend health, not user experience (Exam 1 · Q25).
- If an option correlates strongly with failures, such as a queue metric, it can serve as a leading-indicator **alert**. It is still not the SLI (Exam 2 · Q38).
- To extend coverage upstream of your infrastructure, measure **outside** the infrastructure (Exam 1 · Q34).

### Traps
- **Percentile at the threshold** ("calculate the percentile that corresponds to 100 ms") is close in spirit, but it is not the recommended good/valid form. **Median + p90** only describes the shape of the distribution (Exam 1 · Q47).
- **Average latency** hides the tail. A low average does not mean 95% of requests are fast (Exam 3 · Q17), (Exam 4 · Q19).
- Alerting on **average latency > 150 ms** is not an SLO (Exam 3 · Q17).

---

## 2. Setting SLO targets

### Latency SLO from measured percentiles (worked examples)
Rule: **anchor the target to current measured performance, then add a modest margin.** Never set it tighter than current performance. Never set it exactly equal (that leaves zero error budget, a tripwire). Never loosen it so far that it stops reflecting what users are happy with.

| Question | Measured (28-day) | Too tight | Exact match (zero budget) | **Correct** | Too loose |
|---|---|---|---|---|---|
| (Exam 2 · Q49) | p90 120 ms / p95 275 ms | 100 / 250 | 120 / 275 | **150 / 300** | 250 / 400 |
| (Exam 4 · Q11) | p90 160 ms / p95 300 ms | 150 / 290 | 160 / 300 | **190 / 330** | 300 / 450 |

The cue in both questions is "customers are currently satisfied". That makes the current measurement the anchor.

### Cloud Monitoring SLO configuration (Exam 4 · Q35), (Exam 5 · Q36)
Goal: "requests handled in under 300 ms at least 90% of the time per calendar month."
- **Metric:** speed means **latency**. Availability measures success, not speed.
- **Evaluation:** "X% of requests faster than N ms" means **request-based** evaluation.
- **Calendar month** is the **compliance period**. It says nothing about the evaluation method.

| Evaluation method | Counts | Use when |
|---|---|---|
| **Request-based** | Good requests / total requests | The goal is stated per request: "90% of requests < 300 ms" |
| **Windows-based** | Good time windows / total windows | The goal is stated per interval ("p95 < 300 ms in 90% of 10-min windows"), or the raw metric is already a percentile |

- Trap: "90% **of the time**" pulls toward windows-based evaluation, but the subject of the sentence is requests (Exam 4 · Q35).

### Don't over-deliver on the SLO
- **Meet the SLO, but don't greatly exceed it.** Users depend on the reliability they actually *observe*, which creates a hidden, tighter implicit SLO. The source cites Google's Chubby example: planned outages keep dependents from assuming the service never fails (Exam 2 · Q33).
- SLO consistently met, customers happy, toil low: **raise deployment velocity or accepted risk**, and **move engineers to services that need reliability** (Exam 2 · Q31), (Exam 5 · Q44).
- Under 5% of the budget used for 6 months, and stakeholders confirmed the SLO is right: **release more often or take more risk**, and **announce planned downtime** (Exam 2 · Q33). Exam 5 · Q49 keys this differently (see ⚠️).

| Situation | Do | Don't |
|---|---|---|
| SLO met, users happy, low toil | Raise velocity, reassign engineers (Exam 2 · Q31) | Tighten the SLO, put reliability ahead of features, rework SLIs without a trigger |
| SLO greatly exceeded, SLO confirmed appropriate | Riskier or faster releases, planned downtime (Exam 2 · Q33) | Tighten the SLO to match observed reliability, add capacity |
| SLO met but **users unhappy** | Tighten the SLO or improve SLI coverage (Exam 2 · Q31 trap note) | — |
| SLI falls short of the SLO | Fix the service (Exam 1 · Q2) | Lower the SLO to match the SLI |

### Cost of an extra nine (worked math) (Exam 2 · Q10), (Exam 5 · Q46)
- 99.9% → 99.99% on $1,000,000 revenue, at a cost of $2,000:
  - Difference = 99.99 − 99.9 = **0.09 percentage points**.
  - Value = 0.0009 × $1,000,000 = **$900** < $2,000, so **not worth it**.
  - Alternative path (Exam 5 · Q46): 99.9% allows about 8.76 h of downtime a year and 99.99% about 0.876 h. That saves about 7.88 h, and at $1M ÷ 8,760 h ≈ $114/h, 7.88 h is worth about $900.
- Distractors are off by a factor of 10: **$1,000** treats the gain as 0.1%, the full unavailability at the old target. **$9,000** treats it as 0.9%.
- The decision flips with the inputs. At $10M revenue the same gain is worth $9,000, which exceeds $2,000 (Exam 2 · Q10).

---

## 3. Error budgets, burn rate and error budget policy

### Key concepts
- **Error budget = 1 − SLO target.** You cannot request or grant budget on demand (Exam 4 · Q34).
- **Each SLO has its own budget.** Spare budget on one SLO cannot be moved to another (Exam 4 · Q34).
- A 99% target means a 1% budget. Measured 99.5% means half the budget has been used this month (Exam 2 · Q23).
- **Chain:** SLI (what you measure) → SLO (target + compliance period) → error budget (permitted failure) → **burn rate** (how fast the budget is being spent) (Exam 2 · Q27).

### Detecting budget consumption (Exam 2 · Q27)
- **Define an SLO and alert on `select_slo_burn_rate`.** A sustained burn rate above 1 means the service will miss the SLO for the period. The source recommends pairing a **fast-burn** and a **slow-burn** alert.
- Reject SLI threshold alerts, raw service mesh metrics and uptime-check failure alerts. An uptime-check alert says something is down *now*. It does not say how fast the budget is going.
- If the question asks to be notified **as soon as an endpoint is unreachable**, uptime-check alerting fits.

### Error budget policy, agreed in advance (Exam 2 · Q53), (Exam 5 · Q17)
- To make engineering pivot from features to reliability automatically after an SLO miss, **work with all stakeholders to establish an error budget policy ahead of time**.
- Reject "reliability **always** beats features": the absolute removes the balancing mechanism. Reject "cap releases to once a week": that treats a symptom. Reject "a Jenkins plugin that blocks releases": it can implement a policy, but it is unilateral and only blocks.
- Pattern: **absolutes ("always X") and single-tool fixes are the standard distractors.**

### Budget exhausted or nearly exhausted

| Scenario | Correct | Why the distractors fail | Source |
|---|---|---|---|
| Policy freezes deploys, budget exhausted, the biggest customer urgently wants a feature, tests pass | **Wait for the budget to replenish** | Rerunning tests, deploying now, or a **canary** are all still production deployments. Rollout safety ≠ release permission | (Exam 3 · Q11) |
| 99.9% SLO, quarterly budget nearly gone, features due next week | **Postpone and work on reliability** until the budget replenishes | Auto-rollback still burns budget. A staged rollout still ships. Postponing to build a *feature backlog* wastes the freeze | (Exam 3 · Q42) |
| Budget used up for the rolling window, product team about to launch | **Tell the team, then negotiate: launch freeze vs. knowingly accepting worse UX** | "Make sure tests pass", "escalate for more budget", "reallocate from other SLOs" | (Exam 4 · Q34) |

### Budget surplus plus other goals
- 99% target, 99.5% measured, limited engineers, goals are **reduce technical debt and keep ops costs low**: **identify, quantify and eliminate toil through automation** (Exam 2 · Q23), (Exam 5 · Q23).
- Trap: the surplus budget tempts you toward "assign engineers to the feature backlog". That would be right only if the debt and cost goals were removed (Exam 2 · Q23).
- N+1 redundancy adds cost. Working to "minimize the remaining error budget" pushes the wrong way.

### Shared ownership of reliability (Exam 1 · Q56), (Exam 5 · Q55)
- Joint ownership means **both teams collaboratively define, agree on and publish the SLOs**. In Exam 1 · Q56 it also means shared code review and a **shared on-call rotation**.
- Reject options where one team *unilaterally* sets SLOs for another to meet. Reject handing *all* on-call to developers: "transferring the pager is not sharing ownership" (Exam 1 · Q56).
- In Exam 5 · Q55 the best available option is "SLO-Focused Collaboration": shared SLO definition and publication.

---

## 4. Incident management (IMAG)

### Roles

| Role | Owns | Does not |
|---|---|---|
| **Incident Commander (IC)** | Overall command and coordination. Holds every role not yet delegated. Sets up the "room" | Hands-on mitigation once an OL exists. Answering stakeholder email |
| **Operations Lead (OL)** | Hands-on technical response: diagnose, mitigate, change the system | — |
| **Communications Lead (CL)** | All stakeholder updates, **internal and external** | Splitting audiences, or pushing internal updates onto the IC |

- IMAG has **exactly three** roles. "Engineering Lead", "Customer Impact Assessor" and "External Customer Communications Lead" are distractors (Exam 1 · Q6).

### Sequence after roles are assigned
- IC has declared the incident and assigned an OL and a CL. **Next step: set up a dedicated, shared communication channel** for responders and leads (Exam 1 · Q27), (Exam 5 · Q6).
  - Mitigation belongs to the OL and stakeholder updates to the CL. The postmortem comes after resolution.
  - If **no OL had been assigned**, the IC holds that role and would work on mitigation directly (Exam 1 · Q27 trap note).
- Memory hook: *the IC sets up the room, the OL fixes, the CL tells, and the postmortem comes last.*

### Communications Lead (Exam 1 · Q20)
- Large incident, no ETA, both internal stakeholders and customers emailing: send **periodic updates to all stakeholders, each committing to a "next update" time**.
- Reject serving only one audience, delegating internal emails to someone else, or forwarding them to the IC.

### Living document vs. postmortem (Exam 1 · Q44)

| Artifact | When | Audience |
|---|---|---|
| **Incident state ("living") document** | **During** the incident, updated in real time | Responders |
| **Postmortem** | **After** resolution | Stakeholders and the wider org |

- After a multi-hour outage, the first step in summarizing for stakeholders is to **write a postmortem and distribute it**. Phoning people or asking the "responsible engineer" for an apology are wrong.

### Mitigate first, diagnose later
Rule: **stop the bleeding before you study the wound.** If the symptom started right after a change, roll the change back.

| Scenario | First action | Source |
|---|---|---|
| Canary experiment → spike in 500s and latency | **Revert the canary** | (Exam 1 · Q26) |
| New release → all users see login latency | **Roll back the release**. Not more monitoring, not bigger VMs, not another release | (Exam 2 · Q51), (Exam 5 · Q15) |
| Users in one region can't connect (multi-region GKE) | **Redirect traffic to healthy regions**. Logs and metrics come next | (Exam 2 · Q42) |
| Cloud Run canary breaching the SLO | **Send 100% of traffic to the previous revision**. Not a redeploy, not Cloud Trace first | (Exam 3 · Q56) |
| Blue/green on GKE, green failing, blue healthy, keep green running for investigation | **Change the Service selector to `version: blue`** | (Exam 1 · Q59) |
| Some Pods in one zone erroring after a rollout | Key: restore the previous Pod template and roll the affected Pods (see ⚠️) | (Exam 3 · Q13) |

- Blue/green trap: **rolling back traffic ≠ rolling back a Deployment.** A Deployment rollback changes the failing workload. Removing `version: green` from the selector *broadens* it to both versions (Exam 1 · Q59).
- Exceptions: if no previous version or revision exists, diagnosis or a redeploy of the known-good version becomes the first step (Exam 1 · Q26), (Exam 3 · Q56).

### OL removing a bad node from the LB pool (Exam 4 · Q31)
Pool runs at about 70% capacity and one node returns 5xx on every request. The order is:
1. **Communicate your intent** to the incident team.
2. **Run a load analysis** to see whether the rest of the pool can absorb the traffic, and **scale only if needed**.
3. Once any new nodes are healthy, **drain the bad node and remove it**.

- Reject "always add a node first" (it skips the analysis). Reject removing the node first and scaling reactively. Reject communicating last.

### Suspected compromised GKE node (Exam 4 · Q1)
- **Cordon** (stop new scheduling), then **drain** gracefully. Controller-managed Pods get recreated on other nodes.
- Per the explanation, cordon and drain is *not* full security isolation. Google's guidance also restricts the node VM's network access and **preserves the suspected Pod** for investigation.
- Reject a taint that blocks scheduling elsewhere, scaling the Deployment to 0 (loses evidence), or restarting the node.
- Hook: *cordon stops arrivals, drain evacuates workloads, and network controls restrict communication.*

---

## 5. Postmortems

### When to write one: triggers (Exam 2 · Q7)
- Objective triggers: **data loss**, user-visible impact, on-call intervention (rollback, rerouting), resolution time above a threshold, and **monitoring failure** (a human had to discover the problem).
- A **stakeholder request** is also a trigger. This item keyed *internal* (see ⚠️).
- **Not** triggers: monitoring detecting a failed instance, or CD automatically rolling back a bad release. Those are automation working as intended.

### What goes in it

| Include | Exclude |
|---|---|
| Root cause or contributing causes (Exam 2 · Q40), (Exam 2 · Q44) | A list of people responsible (Exam 2 · Q40), (Exam 1 · Q53) |
| Action items to prevent recurrence (Exam 2 · Q40) | Personal opinion comparing severity with past incidents (Exam 2 · Q40) |
| **How it could have been worse** (near misses) (Exam 4 · Q43) | Copies of every affected design doc (Exam 2 · Q40) |
| Resolution and lessons learned (Exam 1 · Q53) | Banning internal component names. You need the technical specifics (Exam 4 · Q43) |
| — | End-user or customer data. Keeping it out matches Google practice, but that rule alone is incomplete (Exam 4 · Q43) |

### Blameless means fixing the system, not the person
- Preventing a severe incident caused by a software change: **make tests that catch this class of error a required gate before every release** (Exam 1 · Q12), (Exam 2 · Q37), (Exam 5 · Q11), (Exam 5 · Q48).
  - Reject escalating the engineers to management (blame). Reject following up with reviewers and prescribing personal practices (people-focused, doesn't persist). Reject an on-call call-out policy (that improves *response*, not *prevention*).
- **Ask what failed in the system, not who failed.** One-on-ones to find "who approved and pushed" are attribution. Barring the committing engineer is punitive (Exam 2 · Q44).
- Interviewing people to **rebuild the timeline** without assigning fault is fine (Exam 2 · Q44 trap note).

### Action item ownership (Exam 2 · Q35), (Exam 5 · Q20)
- **Exactly one owner per action item, with collaborators as needed.**
- Reject multiple owners (diffused responsibility), "collaborators only, to stay blameless" (that misapplies blamelessness, which governs the analysis of causes, not forward-looking accountability), and making the team lead own everything.

### Sharing and culture
- Postmortem for another team's manager: write a blameless one with root causes, resolution, lessons and **prioritized** action items, and **publish it on the org-wide portal**, not just to the manager (Exam 1 · Q53).
- A good postmortem policy is **blameless in content** (cause, how it could have been worse, prevention) and **open in process** (all participants author it and it is shared as widely as possible) (Exam 4 · Q43).
- To make postmortems well received: **senior leadership acknowledges and takes part**, and **good postmortems are rewarded and celebrated** (Exam 4 · Q39).
  - Reject a dedicated postmortem team (separates the analysis from the people closest to the incident), new hires running them, or a forum for critiquing past postmortems.

---

## 6. Toil and automation

- **Toil:** recurring manual work, such as deleting and recreating a crashing VM by hand. **Fix:** a **managed instance group of size 1 with health-check autohealing** (Exam 1 · Q22).
  - Reject a load balancer with health checks (routes around the failure but doesn't recreate the VM), SMS alerts (faster *awareness*, same manual work) and a bug filing (useful in parallel, but not a toil reducer).
- A GKE Pod goes bad (403s) after about 5 h and the fix is a month away: **add an HTTP liveness probe**. Reject a cron job that kills old Pods (duplicates a built-in feature), a human babysitter, or an alert only (Exam 4 · Q52).
- Toil removal is the right spend when the goals are less debt and lower cost (Exam 2 · Q23), (Exam 5 · Q23).
- **Fast notification of a VM shutdown:** create a **log-based alert** on `protoPayload.methodName = v1.compute.instances.stop` with a notification channel. Reject hourly BigQuery queries (lag), app-side detection (can't anticipate abrupt termination) and randomized Scheduler health checks (Exam 1 · Q52).
- **Shared Terraform code:** use Git with **peer review and unit tests before integration**, and treat the integrated repo as the single source of truth. Reject daily self-merges plus a bucket upload as "master", and Drive folders or zip archives (Exam 1 · Q23).
- **VM telemetry IAM, least privilege:** grant the service account **`logging.logWriter` + `monitoring.metricWriter`** and nothing broader. Viewer access for the ops and security teams is a separate grant to *them* (Exam 4 · Q40).

---

## 7. Capacity planning and scaling

### Availability through horizontal scale (Exam 1 · Q2)
- A stateless API on one VM runs out of memory under load, the SLI misses the SLO, and the goal is availability: **add instances across zones behind a load balancer that actively distributes traffic**.
- A bigger VM fixes capacity but stays a single-zone SPOF. **Passive failover** removes the zone SPOF, but the idle standby doesn't relieve load on the primary. Lowering the SLO changes nothing.
- Passive failover would be the better answer only if the root cause were a zone or hardware failure with no capacity problem.

### Compounding growth and zone-loss headroom (worked math) (Exam 1 · Q40)
- 10% month-over-month for 6 months: 1.1⁶ ≈ **1.77×**, which is about **77% growth, not 60%** (the simple-interest trap).
- 30% CPU today × 1.77 ≈ **53%** of today's capacity.
- With 3 zones and one lost, **2/3 of capacity remains**, so 53% ÷ 0.667 ≈ **80% utilization**. That works but isn't roomy, so validate it.
- **Answer:** confirm the **max node pool size**, enable **HPA**, then **load test**.
  - Reject "the cluster autoscaler handles it regardless" (it is bounded by max limits and only reacts to pending pods), "30% is plenty", and "+60% up front" (wrong math and over-provisioning).

### Risk catalog values (worked math) (Exam 1 · Q37)
Setup: 3 zones with users split evenly, existing failover takes 10 min, DB failure about once a quarter, detection in 5 min. The new DB's failover takes **twice as long**.

| Field | Value | Reasoning |
|---|---|---|
| MTTD | **5 min** | The detection setup is unchanged |
| MTTR | **20 min** | Equals failover duration (10 × 2) |
| MTBF | **90 days** | Once per quarter, unchanged |
| User impact | **33%** | 1 ÷ number of zones (3). It would be 50% only with 2 zones |

Rule: change only the field the new property drives.

### Autoscaler selection

| Need | Tool | Source |
|---|---|---|
| How many Pods (load rises and falls, unpredictable traffic, stateless) | **HPA** | (Exam 4 · Q57) |
| How many nodes | **Cluster autoscaler** | (Exam 2 · Q12) |
| How big each Pod is (steady load, mis-sized requests) | **VPA** | (Exam 2 · Q12), (Exam 4 · Q57) |
| Daily cycle, want "only the Pods **and nodes** needed" | **HPA + cluster autoscaler** | (Exam 2 · Q12) |
| Unpredictable traffic, consistent UX, efficient cluster | **HPA** (CA only matters once something changes pod demand) | (Exam 4 · Q57) |

- Trap: a cron job scaling on a fixed schedule can't track unpredictable traffic (Exam 4 · Q57).

### Scaling signal for an LB-fronted GKE frontend (Exam 1 · Q9), (Exam 5 · Q12)
- **HPA on the GCLB request-count metric** from Cloud Monitoring.
- Reject probe response times (they measure health, not load), VPA + CA (that is right-sizing, not replica count), and NGINX stats (they duplicate the LB signal and add maintenance).
- Exam 1 · Q9 says to use GKE's **native** custom metrics support. Exam 5 · Q12 says to install the custom metrics adapter (see ⚠️).

### Pub/Sub consumer backlog (Exam 1 · Q60), (Exam 5 · Q51)
- Oldest unacked age went from 347 ms to 8,074 ms and undelivered messages from 5 to 14,705, while CPU went from 20% to 30% and memory stayed at 10%. Answer: **scale out Pod replicas**.
- Low CPU does not mean enough throughput. Reject a shorter ack deadline (redeliveries), a virtual waiting room (delays customers) and bigger Pod limits (Pods aren't resource-bound).

### Preparing for peak or launch

| Scenario | First or best action | Source |
|---|---|---|
| Just migrated, peak season coming, "what **first**?" | **Load test** to profile performance and scaling. Re-platforming to Cloud Run, multi-region Terraform and pre-provisioning should come *after* the data | (Exam 4 · Q15) |
| Big marketing event, prepare for failures (choose 2) | **Collect the right metrics and alert at meaningful thresholds** + **review capacity needs and plan quotas** | (Exam 4 · Q19) |
| New multi-region autoscaling MIG with large instances, plan capacity | **Verify resource needs fit project quota in each region** | (Exam 4 · Q50), (Exam 5 · Q32) |

- Exam 4 · Q19 rejects adding service mesh just before the event (new risk), **average** latency (hides the tail) and alerting on **every** failure (noise).
- Exam 4 · Q50 rejects Cloud Trace for sizing, a hard-coded `n2-highcpu-96`, and an internal LB.

### Cost-efficient bursty batch compute (Exam 4 · Q55)
- **Cloud Storage bucket + IAM** for third-party uploads. A **Cloud Run function on the object-finalized trigger** scales up an **autoscaling MIG** whose image **terminates instances when processing is done**.
- Reject a self-managed SFTP VM (always on), an always-on GKE watcher, and doing heavy CPU work inside the function (bounded CPU).
- Hook: *tiny trigger, big compute, and the big compute turns itself off.*

### GKE maintenance for an interruption-intolerant legacy DB (Exam 5 · Q60)
- Use a **maintenance exclusion** with scope **"No minor or node upgrades"**.
- The Stable channel still upgrades. `max-surge-upgrade=0` still upgrades. The PDB option is rejected (see ⚠️ for the explanation's error).

---

## 8. Production readiness and the SRE engagement model

- **PRR finds the service can't meet its SLOs:** decide on reliability improvements and **get them done before handover**. Reject lowering the SLOs, launching without SLOs, and sending support back to developers. That last one is legitimate only if dev can't make the fixes (Exam 1 · Q29).
- **Early operational input on a new product** (data ingestion with unpredictable volume and high cost): **review the design with the product team early in the design phase**. Prototype load tests, staging metrics and production logs all come after design is fixed (Exam 4 · Q38).
- **Service in active development, productionalization (choose 2):** keyed **monitoring/alerting + early SRE design consultation** (Exam 3 · Q19, see ⚠️).
- **API version retirement** (least disruption): **introduce the new version → announce deprecation → deprecate → contact remaining users → best-effort support → turn down** (Exam 2 · Q34).
  - Rules: the replacement exists before any announcement, outreach comes after the announcement, and **turn-down is always last**. Support after turn-down is illogical.

---

## ⚠️ Questionable answers

| Item | Issue |
|---|---|
| **(Exam 5 · Q49)** vs **(Exam 2 · Q33)** | Same scenario, different keys. Exam 2 keys **B + E** (riskier releases + announced planned downtime) and cites the SRE book's Chubby planned-outage practice. Exam 5 keys **B + D** (add SLIs) and calls planned downtime "anti-SRE", which contradicts the Chubby example its counterpart cites. Exam 2 · Q33's own explanation says D (more SLIs) fits only when SLIs miss user journeys, which the stem doesn't say. **Prefer B + E**, but expect either key to show up. |
| **(Exam 5 · Q60)** | Answer IV (maintenance exclusion) is fine, but the explanation says a PDB with `maxUnavailable: 100%` "would effectively prevent any Pod disruptions." That is backwards: 100% max unavailable permits all Pods to be disrupted. |
| **(Exam 5 · Q12)** vs **(Exam 1 · Q9)** | Exam 5 keys "install the Stackdriver custom metrics adapter". Exam 1 · Q9 says that adapter step has been superseded by GKE's native custom metrics support and treats self-managed adapters as extra overhead. Pick the option with the LB request-count metric. If both adapter and native versions appear, choose native. |
| **(Exam 3 · Q13)** | The bank's own trap and takeaway say restoring the Pod template on a *shared* Deployment can't roll back just one zone. C is valid only if each zone has its own Deployment, which the stem doesn't state. Learn the key, but know that it is shaky. |
| **(Exam 3 · Q19)** | The bank flags it: the key is **A + E**, but Google's lifecycle guidance directly supports **A + D** (redundancy during active development). The item is ambiguous. |
| **(Exam 2 · Q7)** | The key is internal-stakeholder request (C) over external (A). Google's SRE text says "any stakeholder", and the bank admits the internal/external split is the item's weak point. The solid lesson is rejecting D and E (automation working is not a trigger). |
| **(Exam 5 · Q46)** | The answer ($900) is right, but the explanation says the $1,000 distractor comes from "rounding". The real error is using 0.1% (the old unavailability) instead of the 0.09-point difference (Exam 2 · Q10). |
| **(Exam 5 · Q32)** | The answer (verify quota) is right, but the claim that internal load balancers are strictly regional and can't span regions is presented without qualification. Don't rely on it as a general fact. The rejection of option III holds anyway because it doesn't address quota or capacity. |
| **(Exam 5 · Q6)** | The answer (dedicated channel) matches Exam 1 · Q27. The claim that Google "explicitly defines this as an early, mandatory step before mitigation actions begin" overstates the source. The reasoning in Exam 1 · Q27 is that mitigation belongs to the OL. |

---

## Last-minute cheat sheet

- SLI = **good / valid** events, with the denominator scoped to the same thing as the numerator (Exam 1 · Q47).
- Partial or degraded responses call for a **quality** SLI. Failed responses call for **availability**. Speed calls for **latency** (Exam 1 · Q25).
- SLIs measure user outcomes. Queue size, I/O wait and disk throughput are causes, not SLIs (Exam 2 · Q38).
- No code changes allowed: use **synthetic probes + existing request logs**. To cover CDN and LB failures: **client instrumentation + synthetic probes** (Exam 1 · Q14), (Exam 1 · Q34).
- Latency SLO = measured value **+ modest margin**: 120/275 → 150/300, and 160/300 → 190/330 (Exam 2 · Q49), (Exam 4 · Q11).
- "X% of requests < N ms" means a **latency metric + request-based** evaluation. The calendar month is the compliance period (Exam 4 · Q35).
- Extra nine: value = **Δ availability × revenue**. 0.09% × $1M = $900 < $2K, so no (Exam 2 · Q10).
- Detect budget consumption with **SLO + `select_slo_burn_rate` alert**, fast-burn and slow-burn (Exam 2 · Q27).
- Set up an **error budget policy with all stakeholders in advance**. "Always", cadence caps and lone pipeline plugins are distractors (Exam 2 · Q53).
- Budget exhausted and the policy says freeze: **wait**. Canaries and passing tests don't lift a freeze (Exam 3 · Q11).
- Budget nearly gone: postpone the release and **do reliability work**, not feature-backlog work (Exam 3 · Q42).
- Budget gone and a launch pending: **tell the team and let them choose freeze vs. worse UX**. No borrowing or reallocating budget (Exam 4 · Q34).
- SLO beaten by a wide margin with happy users: **ship faster or riskier, move engineers elsewhere**, don't tighten the SLO (Exam 2 · Q31).
- Surplus budget but the goals are debt and cost: **eliminate toil** (Exam 2 · Q23).
- IMAG roles are exactly **IC, OL, CL**. After assigning them, the IC **opens the shared comms channel** (Exam 1 · Q6), (Exam 1 · Q27).
- CL sends **periodic updates to everyone**, each with a **"next update" time** (Exam 1 · Q20).
- **Mitigate first**: roll back the release or canary, shift traffic to the previous revision, region or blue env, then diagnose (Exam 1 · Q26), (Exam 2 · Q42), (Exam 3 · Q56).
- Blue/green: **flip the Service selector** to keep the failing env for investigation (Exam 1 · Q59).
- Bad node in a pool: **communicate → load analysis → scale if needed → drain/remove** (Exam 4 · Q31).
- Living doc **during** the incident, **blameless postmortem after**, published widely (Exam 1 · Q44), (Exam 1 · Q53).
- Postmortem prevention action = an **automated test gate before release**, not people-focused fixes (Exam 1 · Q12).
- Postmortem content: **root cause + action items + how it could have been worse**, never a list of culprits (Exam 2 · Q40), (Exam 4 · Q43).
- **One owner per action item** plus collaborators. Culture comes from **leadership participation + rewarding good postmortems** (Exam 2 · Q35), (Exam 4 · Q39).
- Toil fixes: **MIG autohealing** for crashing VMs, a **liveness probe** for Pods that degrade over time (Exam 1 · Q22), (Exam 4 · Q52).
- Scaling: **HPA** for Pod count, **CA** for nodes, **VPA** for Pod size. Daily cycles need HPA + CA (Exam 2 · Q12).
- Growth compounds: 1.1⁶ ≈ 1.77. Judge headroom **after losing a zone** (×1.5 for 3 zones) (Exam 1 · Q40).
- Risk catalog: MTTR = failover time, impact = **1/zones** (Exam 1 · Q37).
- Capacity planning for a multi-region MIG means **checking quota per region**. For a new or just-migrated app, **load test first** (Exam 4 · Q50), (Exam 4 · Q15).
- PRR shows SLOs can't be met: **fix the service before handover**. Give SRE input **early, at design** (Exam 1 · Q29), (Exam 4 · Q38).
