# Domain 3 — Applying Site Reliability Engineering Practices

77 questions. Answers are collapsed — try each question before expanding it.

## Quick-review: memory hooks

- Timeouts from overload + availability goal → scale horizontally across zones with active load balancing, not a bigger box or an idle backup. *(Q1.2)*
- IMAG has exactly three roles: IC, Ops Lead, Comms Lead — if a title isn’t one of those three, it isn’t a canonical incident management role. *(Q1.6)*
- For a request-driven frontend, scale on a real request-volume signal from the load balancer — not on probe timing, not on pod resource usage, and (where a native path exists) not through a self-managed metrics adapter either. *(Q1.9)*
- A good postmortem action item fixes the process (an automated test gating future releases), not the person — blameless means systemic, not individual. *(Q1.12)*
- To measure user-perceived reliability with zero application code changes, look outside the app: simulate the user from the outside (synthetic clients) and read what already happened from the outside (request logs). *(Q1.14)*
- Serving “everyone affected” under incident communications means one scheduled update reaching all audiences, each one promising when the next update lands — not splitting audiences apart or handing part of the job to a role that doesn’t own it. *(Q1.20)*
- Recurring manual delete-and-recreate work is toil — automate it with a managed instance group’s health-check-based auto-healing, not with better alerts or faster human reaction. *(Q1.22)*
- For shared Terraform code, use Git plus reviewed, tested merges into one authoritative main line. Folders and zip snapshots are not version control. *(Q1.23)*
- If the system can still return “something” but it’s incomplete, measure it with a quality SLI, not an availability SLI. *(Q1.25)*
- Stop the bleeding before you study the wound: roll back the likely cause first, then diagnose and document. *(Q1.26)*
- The IC sets up the room, the OL fixes, the CL tells, and the postmortem comes last. *(Q1.27)*
- When the service misses its SLOs, fix the service before handover; do not change the target, skip the target, or push the problem back. *(Q1.29)*
- To catch failures upstream of your infrastructure, measure from upstream of your infrastructure: real client telemetry plus external synthetic probes. *(Q1.34)*
- Detection and frequency come from the existing setup, repair time comes from the failover duration, and impact is one divided by the number of zones. *(Q1.37)*
- Compound the growth, judge headroom against capacity after losing a zone, and pair pod autoscaling with node limits and a load test. *(Q1.40)*
- During the incident you keep a living document, and after it you write a blameless postmortem for stakeholders. *(Q1.44)*
- An SLI is good events over valid events, so count the fast home page requests and divide by home page requests only. *(Q1.47)*
- For prompt notification about a recorded VM lifecycle event, match the event in logs and attach a notification channel. *(Q1.52)*
- A postmortem is blameless and shared widely, with action items for the system and not blame for the people. *(Q1.53)*
- **Shared reliability ownership means shared targets, shared operational feedback, and shared improvement work.** *(Q1.56)*
- When a healthy standby is ready, switch the Service selector to recover while preserving the failing workload. *(Q1.59)*
- Growing backlog plus parallelizable consumers suggests adding workers, even when CPU utilization is modest. *(Q1.60)*
- Postmortems are triggered by failures (data loss, user impact, human intervention, slow fix, monitoring failure) or by a stakeholder request, not by automation doing its job. *(Q2.7)*
- Value of an extra nine = the difference in availability (here 0.09%) × revenue; invest only if that value beats the cost. *(Q2.10)*
- Horizontal for how many Pods, cluster autoscaler for how many nodes, and vertical for how big each Pod is. *(Q2.12)*
- When reliability already exceeds the target and the goals are less debt and lower cost, spend engineering time on removing toil, not on more capacity or more features. *(Q2.23)*
- The SLO sets the budget, and the burn rate shows how fast you are spending it, so alert on the rate. *(Q2.27)*
- Surplus reliability is unspent budget, so spend it on velocity and send spare engineers where reliability is short. *(Q2.31)*
- Meet the SLO without greatly exceeding it, because unspent budget is wasted velocity and a hidden promise. *(Q2.33)*
- Replacement first and shutdown last, with notice before deprecation and outreach before turn-down. *(Q2.34)*
- One owner drives each item, and collaborators help without sharing the accountability. *(Q2.35)*
- Fix the system, not the person, by turning the lesson into an automated release gate. *(Q2.37)*
- An SLI measures what users get, as good over valid events, not what a backend is doing. *(Q2.38)*
- A postmortem explains why it happened and what will change, never who to blame. *(Q2.40)*
- Stop the bleeding first, then find the cause. *(Q2.42)*
- Ask what failed in the system, not who failed. *(Q2.44)*
- A latency SLO should sit a reasonable step above what’s currently measured — never exactly at it, and never so far above it that it stops meaning anything. *(Q2.49)*
- When a problem starts right after a release, mitigate first by rolling it back — don’t investigate further or ship more changes before restoring the known-good state. *(Q2.51)*
- When a question asks what to put in place _before_ an incident to make the reliability-versus-features call automatic, the answer is an error budget policy agreed with stakeholders — not a blanket rule, a fixed release cadence, or a single pipeline gate. *(Q2.53)*
- A safer rollout reduces deployment risk, but it does not lift an error-budget freeze. *(Q3.11)*
- For native Kubernetes Deployments, rollback scope follows the Deployment boundary. *(Q3.13)*
- Measure successful requests and sufficiently fast requests, then set targets and alerts for both. *(Q3.17)*
- Production readiness combines operational visibility, resilience, and early reliability review. *(Q3.19)*
- To measure whether operations work, divide successful attempts by total attempts. *(Q3.29)*
- Budget nearly gone → freeze features, spend the time on reliability — not on a safer release and not on a bigger feature backlog. *(Q3.42)*
- When a canary degrades service, restore traffic to the healthy baseline before pursuing detailed diagnosis. *(Q3.56)*
- Cordon stops arrivals, drain evacuates workloads, and network controls restrict communication. *(Q4.1)*
- Anchor the SLO to current measured performance, then loosen it by a modest margin — never match it exactly (zero error budget) and never loosen it so far that it stops reflecting real user experience. *(Q4.11)*
- Just migrated, peak season coming → load test first; everything else (autoscaling platform, multi-region automation, pre-provisioning) is a decision that load-test data should inform, not precede. *(Q4.15)*
- Preparing for a traffic spike needs two things: enough capacity (review and raise quotas) and good visibility (meaningful metrics and targeted alerts) — not new infrastructure tooling, not averaged latency, and not alerts on every failure. *(Q4.19)*
- Communicate first, analyze capacity before acting, scale only if the analysis shows it’s needed, then drain and remove — never remove the bad node before confirming the rest of the pool can handle the load, and never save communication for last. *(Q4.31)*
- Budget spent means the launch decision goes back to the team: freeze it or knowingly accept worse reliability. Don’t ask for more budget, don’t move budget between SLOs, and don’t treat passing tests as a substitute. *(Q4.34)*
- Choose the metric for what you measure (speed means latency), choose the evaluation method for what you count (requests means request-based), and treat the calendar month as the compliance period. *(Q4.35)*
- Operational problems that come from design are best fixed in the design phase, so review the design early. *(Q4.38)*
- To make postmortems well received: leaders take part, and good postmortem work gets visibly rewarded. Do not centralize them, hand them to newcomers, or open them to critique. *(Q4.39)*
- An instance’s service account only writes telemetry, so give it Logs Writer and Monitoring Metric Writer. *(Q4.40)*
- A good postmortem is blameless in content (cause, how it could have been worse, prevention) and open in process (everyone involved writes it and everyone can read it). *(Q4.43)*
- “Before you scale wide, check what each region will actually let you have.” *(Q4.50)*
- “A container that breaks after a while needs a liveness probe, not a babysitter or a timer job.” *(Q4.52)*
- “Let the trigger be tiny; let the compute be big — and let the big compute turn itself off.” *(Q4.55)*
- “Unpredictable traffic, stateless pods: scale the replica count, not the schedule or the pod’s own size.” *(Q4.57)*

## Questions

### Exam 1 · Q2

You maintain a stateless, web-based API running on a single Compute Engine instance in the `europe-west2-a` zone. The Service Level Indicator (SLI) for availability is falling short of the defined Service Level Objective (SLO). A postmortem determined that requests are timing out because the API receives a high volume of traffic and the instance is running out of memory. You need to improve service availability. What should you do?

- A. Adjust the SLO so that it matches the currently measured SLI.
- B. Migrate the service to a larger Compute Engine instance type with more memory.
- C. Deploy additional service instances across other zones and distribute traffic across all of them using a load balancer.
- D. Deploy additional service instances across other zones and configure them as failover targets to take over if the primary instance becomes unavailable.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Deploy additional service instances across other zones and distribute traffic across all of them using a load balancer.

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

</details>

---

### Exam 1 · Q6

Your organization follows Site Reliability Engineering practices. You are acting as Incident Commander for a new, customer-impacting incident. To run an effective incident response, you need to immediately delegate two other incident management roles. Which two roles should you assign? (Choose two.)

- A. Operations Lead
- B. Engineering Lead
- C. Communications Lead
- D. Customer Impact Assessor
- E. External Customer Communications Lead

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Operations Lead **|** C. Communications Lead

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

</details>

---

### Exam 1 · Q9

Your team has recently deployed an NGINX-based application to Google Kubernetes Engine (GKE) and exposed it to the public through an HTTP(S) Google Cloud Load Balancer (GCLB) Ingress. You want to scale the application’s frontend deployment using an appropriate Service Level Indicator (SLI). What should you do?

- A. Configure the horizontal pod autoscaler (HPA) to scale based on the average response time reported by the Liveness and Readiness probes.
- B. Configure the vertical pod autoscaler (VPA) in GKE, and enable the cluster autoscaler so the cluster grows as pod resource requests expand.
- C. Use GKE’s native custom metrics support for the horizontal pod autoscaler, and configure it to scale based on the request count metric that the GCLB publishes to Cloud Monitoring.
- D. Expose the NGINX stats endpoint, and configure the horizontal pod autoscaler to scale based on the request metrics it reports.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Use GKE’s native custom metrics support for the horizontal pod autoscaler, and configure it to scale based on the request count metric that the GCLB publishes to Cloud Monitoring.

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

</details>

---

### Exam 1 · Q12

Your organization follows Site Reliability Engineering principles. You’re writing the postmortem for an incident, triggered by a software change, that had a severe impact on users. You want to prevent incidents of this severity from recurring. What should you do?

- A. Identify the engineers responsible for the incident, and escalate the matter to their senior management.
- B. Ensure that test cases capable of catching this class of error run successfully as a required step before future software releases.
- C. Follow up individually with the employees who reviewed the change, and prescribe practices they should personally follow going forward.
- D. Create a policy requiring on-call teams to immediately call engineers and management to discuss a plan of action whenever an incident occurs.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Ensure that test cases capable of catching this class of error run successfully as a required step before future software releases.

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

</details>

---

### Exam 1 · Q14

You support a high-traffic web application running on Google Cloud. You need to measure the application’s reliability from the user’s perspective, without making any engineering changes to the application itself. What should you do? (Choose two.)

- A. Review the application’s current metrics, and add new ones as needed.
- B. Modify the application code to capture additional information about user interactions.
- C. Analyze only the web proxy logs, and capture the response time of each request.
- D. Create synthetic clients that simulate a user journey through the application.
- E. Use current and historical request logs to trace customer interactions with the application.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Create synthetic clients that simulate a user journey through the application. **|** E. Use current and historical request logs to trace customer interactions with the application.

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

</details>

---

### Exam 1 · Q20

Your organization follows Site Reliability Engineering practices. You are acting as Communications Lead for a large, ongoing incident affecting customer-facing applications, and there is still no estimated resolution time. You’re receiving emails from internal stakeholders asking for updates, as well as emails from customers asking what’s happening. You want to efficiently keep everyone affected informed. What should you do?

- A. Focus on responding to internal stakeholders at least every 30 minutes, and commit to “next update” times in those communications.
- B. Provide periodic updates to all stakeholders in a timely manner, and commit to a “next update” time in every communication.
- C. Delegate responding to internal stakeholder emails to another member of the incident response team, and focus on providing responses directly to customers.
- D. Forward all internal stakeholder emails to the Incident Commander and let them manage internal communications, while you focus on providing responses directly to customers.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Provide periodic updates to all stakeholders in a timely manner, and commit to a “next update” time in every communication.

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

</details>

---

### Exam 1 · Q22

You support a production service running on a single Compute Engine instance. You regularly spend time recreating the service by deleting the crashing instance and creating a new one from the relevant image. You want to reduce the time spent on this manual work while following Site Reliability Engineering principles. What should you do?

- A. File a bug with the development team so they can find the root cause of the crashing instance.
- B. Create a managed instance group with a single instance, and use health checks to determine the system’s status.
- C. Place a load balancer in front of the Compute Engine instance, and use health checks to determine the system’s status.
- D. Create a Cloud Monitoring dashboard with SMS alerts so you can begin recreating the crashed instance promptly after it crashes.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Create a managed instance group with a single instance, and use health checks to determine the system’s status.

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

</details>

---

### Exam 1 · Q23

You are responsible for writing and updating the Terraform configurations that define your organization’s infrastructure. Two new engineers will soon contribute to the same codebase. You need to choose tooling and establish a workflow that prevents team members from overwriting one another’s changes. You also need to make sure the latest version always contains every update. What should you do?

- A.
    Keep the code in a Git-based version control system.
    Define a workflow in which each developer merges their own changes at the end of the working day.
    Bundle the code and upload it to a versioned Cloud Storage bucket, designating that upload as the current master version.
- B.
    Keep the code in a Git-based version control system.
    Define a workflow that requires peer code review and unit testing to validate integrity and functionality before changes are integrated.
    Define a workflow in which the fully integrated code in the repository is treated as the current master version.
- C.
    Keep the code as plain-text files in Google Drive, arranged in a defined folder hierarchy.
    At the end of each day, verify that every change is reflected in the files within that hierarchy.
    Rename the folder hierarchy using a predefined naming convention that increments the version number.
- D.
    Keep the code as plain-text files in Google Drive, arranged in a defined folder hierarchy.
    At the end of each day, verify that every change is reflected in the files within that hierarchy, then create a new .zip archive using a predefined naming convention.
    Upload the .zip archive to a versioned Cloud Storage bucket and accept it as the latest version.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B.

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

</details>

---

### Exam 1 · Q25

You operate a high-traffic consumer web application built on a microservices architecture. The application’s home page assembles several independent widgets — for example, current weather conditions, live stock quotes, and breaking news headlines. For each widget, the request-handling thread calls a dedicated backend microservice and then renders the home page from the responses it collects. These backend microservices intermittently fail, and when that happens the home page is still served, but with one or more widgets missing. Your users tolerate an occasional missing widget and would rather see a partially populated page than no page at all, but satisfaction drops sharply if this partial-content condition becomes too frequent. You want to define a Service Level Indicator (SLI) that can support a Service Level Objective (SLO) for this experience. Which SLI should you select?

- A. A quality SLI, calculated as the ratio of non-degraded responses to total responses.
- B. An availability SLI, calculated as the ratio of healthy microservices to the total number of microservices.
- C. A freshness SLI, calculated as the proportion of widgets refreshed within the preceding 10 minutes.
- D. A latency SLI, calculated as the ratio of microservice calls completing in under 100 ms to total microservice calls.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. A quality SLI, calculated as the ratio of non-degraded responses to total responses.

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

</details>

---

### Exam 1 · Q26

You are running an experiment to determine whether users respond positively to a new feature in your web application. Soon after you release the feature as a canary, users begin receiving a spike in HTTP 500 errors, and your monitoring reports show higher latency. You want to reduce the impact on users as quickly as possible. What should you do FIRST?

- A. Revert the experimental canary rollout.
- B. Begin tracking latency, traffic, errors, and saturation.
- C. Collect information for the incident’s postmortem document.
- D. Track down where the 500 errors originate and what is causing the latency increase.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Revert the experimental canary rollout.

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

</details>

---

### Exam 1 · Q27

You are the on-call engineer for an infrastructure service that many other systems depend on. An alert tells you the service is failing to serve most of its requests, and every dependent system, which together serve hundreds of thousands of users, is affected. Following your Site Reliability Engineering (SRE) incident management protocol, you declare yourself Incident Commander (IC) and bring in two experienced teammates as Operations Lead (OL) and Communications Lead (CL). What should you do next?

- A. Work out ways to reduce the impact on users and roll the mitigations out to production.
- B. Reach out to the owners of the affected services and give them a status update on the incident.
- C. Set up a shared communication channel for the incident responders and leads to talk to one another.
- D. Open a postmortem document, record the incident details, share the draft internally, and request input from internal stakeholders.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Set up a shared communication channel for the incident responders and leads to talk to one another.

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

</details>

---

### Exam 1 · Q29

Your organization follows SRE principles and practices. You are preparing to assume operational responsibility for a new service built by the Development Team, and you run a Production Readiness Review (PRR) as part of the handover. When the analysis phase ends, you conclude that the service, as it stands, cannot satisfy its Service Level Objectives (SLOs). You want to be confident the service can meet its SLOs once it is running in production. What should you do next?

- A. Lower the SLO targets to values the service can currently achieve so that it can go live.
- B. Inform the development team that they will need to provide ongoing production support for the service.
- C. Determine the reliability improvements to recommend and have them completed before the handover.
- D. Launch the service in production without SLOs and define them later, once operational data has been gathered.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Determine the reliability improvements to recommend and have them completed before the handover.

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

</details>

---

### Exam 1 · Q34

You support a multi-region web service that runs on Google Kubernetes Engine (GKE) behind a global external Application Load Balancer. For legacy reasons, user requests first pass through a third-party Content Delivery Network (CDN), which then forwards traffic to the load balancer. You have already implemented an availability Service Level Indicator (SLI) at the load balancer. You now want broader coverage so that a load balancer misconfiguration, a CDN failure, or another global networking catastrophe would also be detected. Where should you measure this new SLI? (Choose two.)

- A. In your application servers’ logs.
- B. Through instrumentation built directly into the client.
- C. In metrics exported from your application servers.
- D. Through GKE health checks on your application servers.
- E. Using a synthetic client that periodically sends simulated user requests.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Through instrumentation built directly into the client. **|** E. Using a synthetic client that periodically sends simulated user requests.

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

</details>

---

### Exam 1 · Q37

Your application runs across three Google Cloud zones, and its users are split among them. You can fail over from one zone to another, but doing so interrupts service for 10 minutes for the affected users. A database failure occurs about once every quarter, and your monitoring detects it within five minutes. You are documenting the reliability risks of a planned real-time messaging feature. For each risk, you record Mean Time to Detect (MTTD) in minutes, Mean Time to Repair (MTTR) in minutes, Mean Time Between Failures (MTBF) in days, and the percentage of users impacted. The messaging feature relies on a new database system whose zonal failover takes twice as long to complete successfully. You need to capture the risk of this new database failing in a single zone. Which set of values should you record for the new database failover risk?

- A. MTTD: 5 minutes, MTTR: 10 minutes, MTBF: 90 days, User impact: 33%
- B. MTTD: 5 minutes, MTTR: 20 minutes, MTBF: 90 days, User impact: 33%
- C. MTTD: 5 minutes, MTTR: 10 minutes, MTBF: 90 days, User impact: 50%
- D. MTTD: 5 minutes, MTTR: 20 minutes, MTBF: 90 days, User impact: 50%

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. MTTD: 5 minutes, MTTR: 20 minutes, MTBF: 90 days, User impact: 33%

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

</details>

---

### Exam 1 · Q40

You are carrying out a semi-annual capacity planning review for your primary service. You anticipate user growth of 10% month over month for the next six months. The service is fully containerized and runs on a Google Kubernetes Engine (GKE) Standard regional cluster spread across three zones, with the cluster autoscaler enabled. The service currently uses about 30% of its total provisioned CPU capacity, and it must stay resilient if a single zone fails. You want users to see minimal negative impact from either the growth or a zone failure, without paying for capacity you do not need. How should you prepare for the projected growth?

- A. Confirm the maximum node pool size, enable a Horizontal Pod Autoscaler, and then run a load test to validate the expected resource requirements.
- B. Rely on the cluster autoscaler, since a GKE cluster with it enabled scales automatically regardless of the growth rate.
- C. Take no capacity action, since 30% utilization leaves ample headroom for this rate of growth.
- D. Add 60% more node capacity up front to cover six months of 10% growth, and then run a load test to confirm the capacity is sufficient.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Confirm the maximum node pool size, enable a Horizontal Pod Autoscaler, and then run a load test to validate the expected resource requirements.

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

</details>

---

### Exam 1 · Q44

A serious outage prevented every user of your service from accessing it for several hours. After extended incident response, the service recovered and access was restored. You now need to give relevant stakeholders a summary of the incident, following Site Reliability Engineering (SRE) recommended practices. What should you do first?

- A. Phone each stakeholder individually to describe what occurred.
- B. Write a postmortem and distribute it to the stakeholders.
- C. Send the incident state document to every stakeholder.
- D. Ask the engineer responsible to write an apology email to all stakeholders.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Write a postmortem and distribute it to the stakeholders.

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

</details>

---

### Exam 1 · Q47

You support a high-traffic web application and want to make sure the home page loads quickly. As a first step, you decide to define a Service Level Indicator (SLI) for home page request latency, with 100 ms as the acceptable page load time. What is the Google-recommended way to calculate this SLI?

- A. Group request latencies into buckets, and then calculate the percentile that corresponds to 100 ms.
- B. Group request latencies into buckets, and then calculate the median and the 90th percentile.
- C. Count the home page requests that complete in under 100 ms, and then divide that count by the total number of home page requests.
- D. Count the home page requests that complete in under 100 ms, and then divide that count by the total number of requests to the whole web application.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Count the home page requests that complete in under 100 ms, and then divide that count by the total number of home page requests.

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

</details>

---

### Exam 1 · Q52

An application runs on a single Compute Engine VM in one region. Occasional VM shutdowns interrupt users’ ongoing work. You need a solution that can be implemented quickly and reliably notifies you about shutdown events.

Which approach should you choose?

- A. In Logs Explorer, create a log-based alert for VM log entries with `protoPayload.methodName` set to `v1.compute.instances.stop`.
- B. Route the VM logs to BigQuery and schedule hourly queries that find entries with `protoPayload.methodName` set to `v1.compute.instances.stop`.
- C. Modify the application to detect when its host VM is about to shut down and send a notification from the application.
- D. Use Cloud Scheduler to trigger health checks of the VM at randomized intervals, with no more than one hour between checks.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. In Logs Explorer, create a log-based alert for VM log entries with `protoPayload.methodName` set to `v1.compute.instances.stop`.

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

</details>

---

### Exam 1 · Q53

Your organization is adopting Site Reliability Engineering (SRE) culture and principles. A service you support recently suffered a limited outage. A manager on another team asks you for a formal account of what happened so that they can act on remediation work. What should you do?

- A. Write a postmortem covering the root causes, the resolution, lessons learned, and a prioritized list of action items, and share it only with the manager.
- B. Write a postmortem covering the root causes, the resolution, lessons learned, and a prioritized list of action items, and publish it on the engineering organization’s document portal.
- C. Write a postmortem covering the root causes, the resolution, lessons learned, the people responsible, and a list of action items for each person, and share it only with the manager.
- D. Write a postmortem covering the root causes, the resolution, lessons learned, the people responsible, and a list of action items for each person, and publish it on the engineering organization’s document portal.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Write a postmortem covering the root causes, the resolution, lessons learned, and a prioritized list of action items, and publish it on the engineering organization’s document portal.

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

</details>

---

### Exam 1 · Q56

You are leading a DevOps transformation for an organization that operates a production service. The DevOps team maintains the service infrastructure and handles on-call incidents. The Software Development team authors, submits, and reviews application code. Neither team has documented or published service level objectives (SLOs).

You want both teams to share accountability for service reliability. Which assignment of responsibilities best establishes this operating model?

- **A.**
    **DevOps team:** Maintain the infrastructure, handle on-call incidents, and review application code.
    **Software Development team:** Author and submit code for DevOps review, and unilaterally establish and publish SLOs that DevOps is responsible for achieving.
- **B.**
    **DevOps team:** Maintain the infrastructure and review application code.
    **Software Development team:** Author and submit code for DevOps review, assume all on-call responsibilities, and unilaterally establish and publish SLOs that DevOps is responsible for achieving.
- **C.**
    **DevOps team:** Maintain the service infrastructure.
    **Software Development team:** Author and submit application code for review.
    **Both teams:** Review application code, participate in a shared on-call rotation, and collaboratively define, agree to, and publish the service’s SLOs.
- **D.**
    **DevOps team:** Maintain the infrastructure and retain all on-call responsibilities.
    **Software Development team:** Author, submit, and review application code, and establish and publish the service’s SLOs independently.

<details><summary>Answer &amp; explanation</summary>

**Correct:** **C.**

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

</details>

---

### Exam 1 · Q59

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

- **A.** Deploy the failing application version from `app-green` to `app-blue` as well.
- **B.** Revert the application version running in `app-green` to the previous stable release.
- **C.** Broaden the `app-svc` selector by removing `version: green` and retaining only `app: my-app`.
- **D.** Change the `app-svc` selector to require `app: my-app` and `version: blue`.

<details><summary>Answer &amp; explanation</summary>

**Correct:** **D.** Change the `app-svc` selector to require `app: my-app` and `version: blue`.

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

</details>

---

### Exam 1 · Q60

You are responding to an incident affecting an inventory-update microservice deployed on a Google Kubernetes Engine (GKE) Autopilot cluster.

An online retailer publishes order events to Pub/Sub. Multiple replicas of the microservice can consume events from the same pull subscription and process inventory updates concurrently in a warehouse system.

A promotional campaign causes a sudden increase in orders. Inventory updates become delayed, and customers can place orders for products that have already sold out. Monitoring shows these changes from normal operation:

  * **Average Pod CPU utilization:** Normally 20% of the CPU limit; currently 30%.

  * **Average Pod memory utilization:** Normally 10% of the memory limit; currently 10%.

  * **Average oldest unacknowledged message age:** Normally 347 milliseconds; currently 8,074 milliseconds.

  * **Average undelivered message count:** Normally 5 messages; currently 14,705 messages.

  * **Average acknowledgment latency:** Normally 312 milliseconds; currently 354 milliseconds.

Which action should you take to reduce inventory-processing delays while minimizing customer impact?

- **A.** Shorten the Pub/Sub subscription’s acknowledgment deadline.
- **B.** Add a virtual waiting room that limits incoming store traffic to its normal pre-campaign rate.
- **C.** Scale out the inventory-processing microservice by increasing its Pod replica count.
- **D.** Raise the CPU and memory limits configured for each inventory-processing Pod.

<details><summary>Answer &amp; explanation</summary>

**Correct:** **C.** Scale out the inventory-processing microservice by increasing its Pod replica count.

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

</details>

---

### Exam 2 · Q7

Your team is writing a postmortem after an incident on your externally facing application. The team wants to improve its postmortem policy by adding triggers that indicate when an incident requires a postmortem. Based on Site Reliability Engineering (SRE) practices, which triggers should the policy define? (Choose two.)

- A. A request for a postmortem comes from an external stakeholder.
- B. An incident results in data loss.
- C. A request for a postmortem comes from an internal stakeholder.
- D. The monitoring system detects that an instance of your application has failed.
- E. The CD pipeline detects a problem with a release and automatically rolls it back.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. An incident results in data loss. **|** C. A request for a postmortem comes from an internal stakeholder.

**Correct Answer**

**B. An incident results in data loss.**

**C. A request for a postmortem comes from an internal stakeholder.**

**Exam Reasoning Explanation**

The decision method is to separate triggers that are defined in advance and objective from triggers that reflect the system working as designed. Google’s SRE guidance lists objective triggers such as user-visible downtime or degradation beyond a threshold, data loss of any kind, on-call engineer intervention, long resolution time, and a monitoring failure. It adds that any stakeholder may also request a postmortem. Option B matches the objective list directly. Options D and E describe automation succeeding (monitoring detecting a failure, a pipeline catching and reversing a bad release), which is the opposite of a failure that needs organizational learning. That leaves a stakeholder request as the second trigger, and the A versus C split is a scoping judgment explained in the Exam Trap.

**Key Exam Clues**

  * “triggers that indicate whether an incident requires a postmortem” is a hard constraint. You need criteria that can be defined before an incident, not reasons a postmortem would be useful.

  * “Based on Site Reliability Engineering (SRE) practices” is a hard constraint. The answers must align with Google’s published SRE criteria rather than general incident-management folklore.

  * “Choose two” is a cardinality instruction. The stem expects one objective trigger and one request-based trigger.

  * “external facing application” is context only. It describes who uses the application, not who can trigger the team’s own postmortem policy.

**Why This Is Correct**

Option B is the clearest match. Data loss of any kind is an explicit SRE postmortem trigger, because losing data is a serious, often irreversible failure even if the service recovers quickly. Option C reflects the SRE guidance that, beyond the objective triggers, any stakeholder may request a postmortem for an event. The two selections are independent triggers that work together. One is an objective criterion that fires without anyone asking, and the other is a request-based path that catches events the objective criteria miss. Together they cover the two mechanisms the SRE guidance describes: criteria defined before an incident, and stakeholder requests on top of them.

**Why the Other Options Are Not the Best Fit**

**Option A is _Technically Possible but Not Best_. **SRE guidance does say any stakeholder may request a postmortem, so an external request is not absurd. It loses to C because the policy is the team’s internal governance and postmortems are internal documents that contain operational detail. A request from outside the company would normally reach the team through an internal stakeholder such as support or management, who then request the postmortem.

**Option D is _Incorrect_.** The SRE trigger is a monitoring failure, meaning monitoring did not detect the problem and a person had to discover it manually. Here monitoring worked, and a single failed instance is routine in most managed deployments and is typically absorbed by redundancy without user impact.

**Option E is a _Different Use Case_**. The SRE trigger is on-call engineer intervention, such as a manual rollback or traffic reroute. An automated pipeline rollback is a control working as designed with no human intervention and no stated user impact. It is better handled by release-quality review than by a postmortem trigger.

**Exam Trap**

The weak point of this item is A versus C, so it is worth stating plainly. Google’s SRE text says “any stakeholder,” which does not distinguish internal from external, and this item’s key rests on that distinction. The defensible reading is that the policy is internal governance, so an internal stakeholder request is the one that belongs in it. Do not treat this as a rule that external requests are never honored. The stronger exam skill is rejecting D and E, which sound like incident signals but describe automation succeeding. The answer would change if the stem said an on-call engineer manually rolled back a release, because on-call intervention is a listed trigger.

**Foundation Concept**

A postmortem policy has two parts: objective criteria defined before an incident, and discretionary requests from stakeholders. Objective criteria remove debate about whether an incident was “big enough” and keep the practice blameless and consistent. Postmortems cost time, so triggers aim at events that carry learning value, such as user impact, data loss, human intervention, slow resolution, or failures of the detection system itself. Events that the system handled automatically and invisibly usually carry less learning value.

**Real-World Connection**

A team writes a policy that requires a postmortem for any data loss, any user-visible degradation past a set threshold, any manual intervention by on-call, and any incident where monitoring failed to alert, and lets managers or partner teams request one for anything else. The outcome is predictable triage: no one argues about whether to write one, and effort goes to incidents with real lessons. The trade-off is that too many triggers or low thresholds create postmortem fatigue, so teams tune thresholds as they learn what is worth the effort.

**Memory Hook**

Postmortems are triggered by failures (data loss, user impact, human intervention, slow fix, monitoring failure) or by a stakeholder request, not by automation doing its job.

**30-Second Exam Takeaway**

For SRE postmortem-trigger questions, pick the listed objective triggers such as data loss, user-visible impact, on-call intervention, long resolution time and monitoring failure, plus a stakeholder request. Reject options where monitoring or CI/CD automation simply worked as intended.

**Official References**

[Google SRE Book — Postmortem Culture: Learning from Failure: ](https://sre.google/sre-book/postmortem-culture/)Supports: the list of common postmortem triggers (including data loss of any kind) and the statement that any stakeholder may request a postmortem, which together justify Options B and C and eliminate D and E

[**Google Cloud Architecture Framework — Conduct thorough postmortems:**](https://docs.cloud.google.com/architecture/framework/reliability/conduct-postmortems) Supports: the recommendation to define postmortem criteria before an incident occurs, and the same set of objective triggers, including on-call interventions and monitoring failures

</details>

---

### Exam 2 · Q10

Your organization wants to raise an application’s availability target from 99.9% to 99.99%, and the improvement would cost $2,000. The application currently generates $1,000,000 in revenue. You need to decide whether the higher availability is worth the investment over a single year of use. What should you do?

- A. Calculate the value of the improved availability as $900, and conclude that the improvement is not worth the investment.
- B. Calculate the value of the improved availability as $1,000, and conclude that the improvement is not worth the investment.
- C. Calculate the value of the improved availability as $1,000, and conclude that the improvement is worth the investment.
- D. Calculate the value of the improved availability as $9,000, and conclude that the improvement is worth the investment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Calculate the value of the improved availability as $900, and conclude that the improvement is not worth the investment.

**Correct Answer**

**A. Calculate the value of the improved availability as $900, and conclude that the improvement is not worth the investment.**

**Exam Reasoning Explanation**

This is a two-step decision: first find the value of the extra availability, then compare it with the cost. The value step comes from the SRE method of treating availability as a share of revenue, so the improvement is the difference between the two targets applied to annual revenue. The decision step is a straight comparison: spend more than the value gained and the investment loses money. Computing $900 and comparing it with the $2,000 cost settles the answer, and only option A pairs the correct value with the correct conclusion.

**Key Exam Clues**

  * “from 99.9% to 99.99%” is the calculation input. The improvement is the gap between the two targets, not either target on its own.

  * “current revenue is $1,000,000” is the calculation base. The value of availability is proportional to the revenue the service generates.

  * “for a single year of usage” is a hard constraint. The value ($900) and the cost ($2,000) are compared over the same one-year period.

  * “worth the investment” is the decision rule. Worth it only when the value gained exceeds the cost.

**Why This Is Correct**

Going from 99.9% to 99.99% availability is an improvement of 0.09 percentage points (99.99% − 99.9% = 0.09%). Applied to $1,000,000 of revenue, the incremental value is 0.0009 × $1,000,000 = $900. Google’s SRE guidance frames the same trade-off: if the cost of gaining one more nine is less than the incremental revenue, the investment pays off, and if it costs more, the cost exceeds the projected revenue gain. Here the cost of $2,000 is greater than the $900 value, so the improvement is not worth it for one year.

**Why the Other Options Are Not the Best Fit**

**Option B is _Incorrect_. **The $1,000 figure is a miscalculation, and it comes from treating the gain as 0.1% of revenue, which is the unavailability at the old target rather than the difference between the two targets. Its conclusion (not worth it) happens to be right, but the supporting number is wrong.

**Option C is _Incorrect_. **It combines the same wrong $1,000 value with the wrong conclusion. Even at $1,000, the investment would still cost twice what it returns.

**Option D is _Incorrect_.** The $9,000 figure comes from an order-of-magnitude slip, 0.9% rather than 0.09%, which makes the improvement look worth buying. It is tempting because it flips the decision, but the arithmetic does not support it.

**Exam Trap**

The trap is the decimal placement in the percentage difference. 99.99% − 99.9% is 0.09 percentage points, and it is easy to read as 0.1% ($1,000) or 0.9% ($9,000). If the revenue were $10,000,000 instead, the same improvement would be worth $9,000, which would exceed the $2,000 cost. The decision flips with revenue and cost, so always recompute both.

**Foundation Concept**

Each extra nine of availability costs more than the previous one but protects a smaller slice of revenue, so reliability has diminishing returns. SRE therefore treats availability targets as a business decision, not a technical goal to maximize. The value of an availability improvement is the revenue protected by the difference between the targets, and an investment makes sense only when that value exceeds the cost of reaching the target. The comparison should use the same time period for both sides.

**Real-World Connection**

A team weighing a multi-zone redesign multiplies the availability gain by the service’s annual revenue and compares it with the engineering and infrastructure cost before committing. When the value is smaller than the cost, they keep the current target and spend the error budget on feature work instead. The trade-off is that revenue is only part of the picture, because reputation, contractual penalties, and indirect effects can also matter, so teams use the calculation as a starting point rather than the final word.

**Memory Hook**

Value of an extra nine = the difference in availability (here 0.09%) × revenue; invest only if that value beats the cost.

**30-Second Exam Takeaway**

For availability-versus-cost questions, subtract the two targets, multiply by revenue to get the value, and compare it with the cost over the same period. Watch the decimal placement, because wrong answers are usually off by a factor of 10.

**Official References**

[Google SRE Book — Embracing Risk: ](https://sre.google/sre-book/embracing-risk/)Supports: the framing of availability in nines, the link between availability and revenue, and the principle that reliability investments should be weighed against the value they protect

[**Professional Cloud DevOps Engineer Exam Guide — Section 3.1, Balancing change, velocity, and reliability of the service:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment via “Defining SLIs (e.g., availability, latency), SLOs, and SLAs” and “Opportunity cost of risk and reliability (e.g., number of ‘nines’)”

</details>

---

### Exam 2 · Q12

Your company runs an ecommerce website built from JVM-based applications in a microservice architecture on Google Kubernetes Engine (GKE). Traffic rises during the day and falls overnight. Your operations team currently runs enough Pods to cover the evening peak at all times. You want to automate scaling so that only the Pods and nodes needed for the current load are running. What should you do?

- A. Set up the Vertical Pod Autoscaler and leave the node pool at a fixed size.
- B. Set up the Vertical Pod Autoscaler and turn on the cluster autoscaler.
- C. Set up the Horizontal Pod Autoscaler and leave the node pool at a fixed size.
- D. Set up the Horizontal Pod Autoscaler and turn on the cluster autoscaler.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Set up the Horizontal Pod Autoscaler and turn on the cluster autoscaler.

**Correct Answer**

**D. Set up the Horizontal Pod Autoscaler and turn on the cluster autoscaler.**

**Exam Reasoning Explanation**

The requirement has two layers that both have to flex with the daily load curve: the number of Pods, and the number of nodes that host them. Walking requirement → capability: load that varies with time of day is a replica-count problem, so Pods should scale out and in, which is what the Horizontal Pod Autoscaler does. The cost saving only materializes if the nodes go away when the Pods do, and a fixed node pool keeps paying for peak capacity regardless of Pod count. That requires the cluster autoscaler to shrink and grow the node pool. Only option D covers both layers in the right way.

**Key Exam Clues**

  * “load increases during the day and decreases during the night” is a hard constraint. Demand swings up and down daily, which calls for scaling the number of replicas.

  * “run enough Pods to handle the evening peak load” describes the problem to remove, because capacity is sized for peak and wasted off-peak.

  * “only running enough Pods and nodes for the load” is a hard constraint. Both Pods and nodes must scale, so a static node pool is disqualified.

  * “microservice architecture” supports horizontal scaling, since stateless replicated services are the natural fit for adding and removing Pods.

**Why This Is Correct**

The Horizontal Pod Autoscaler changes the number of Pods in response to CPU or memory consumption or custom metrics, so replicas rise during the day and fall at night. The Horizontal Pod Autoscaler does not change the number of nodes in a GKE cluster, and Google’s documentation points to the cluster autoscaler for that job. The cluster autoscaler resizes a node pool between the minimum and maximum you set: when Pods can’t be scheduled it adds nodes, and when nodes are under-used and their Pods fit elsewhere it removes them. The two work as a chain, where replicas go up, pending Pods trigger new nodes, and the reverse happens as load drops, so you pay for only what the current load needs.

**Why the Other Options Are Not the Best Fit**

**Option A is _Different Use Case_.** The Vertical Pod Autoscaler adjusts the CPU and memory requests of individual Pods, which is aimed at steady-state right-sizing. Google’s guidance says to use the Horizontal Pod Autoscaler for workloads with sudden spikes in demand, and the fixed node pool means off-peak savings would never be realized.

**Option B is _Different Use Case_**. Adding the cluster autoscaler fixes the node side, but the Pod side still uses the Vertical Pod Autoscaler, which resizes Pods rather than changing replica counts. Right-sized Pods are still running around the clock, so the daily swing in load is not followed.

**Option C is _Technically Possible but Not Best_. **The Horizontal Pod Autoscaler reduces the number of running Pods at night, which is the right Pod-side choice. With a static node pool, though, the idle nodes keep running and billing, so you do not meet the requirement to run only the nodes you need.

**Exam Trap**

The trap is stopping after the Pod layer. Option C looks almost complete because the Horizontal Pod Autoscaler is correct, but the stem explicitly asks for “Pods and nodes,” so the node layer has to scale too. A second trap is treating the Vertical Pod Autoscaler as the general-purpose “autoscaling” answer. Vertical autoscaling would be the better fit if the load were steady but the Pods were over- or under-provisioned, and the question would then be about right-sizing rather than following a daily cycle.

**Foundation Concept**

Kubernetes autoscaling works in layers. Horizontal Pod autoscaling changes how many Pods run, vertical Pod autoscaling changes how much CPU and memory each Pod requests, and cluster autoscaling changes how many nodes exist to host them. The cluster autoscaler decides based on the resource requests of Pods, not their live utilization, which is why explicit resource requests on workloads matter. A cost-efficient design for variable load usually pairs Pod-level scaling with node-level scaling.

**Real-World Connection**

An ecommerce team sets a Horizontal Pod Autoscaler on its storefront Deployment and enables the cluster autoscaler on the node pool with sensible minimum and maximum sizes. Overnight the Pod count drops, nodes drain and are removed, and the bill shrinks. The trade-off is that scale-down can briefly disrupt Pods that are rescheduled to other nodes, so replicas should tolerate restarts, and scale-up has a short delay while new nodes start, so some headroom or a higher minimum may be needed for sudden traffic spikes.

**Memory Hook**

Horizontal for how many Pods, cluster autoscaler for how many nodes, and vertical for how big each Pod is.

**30-Second Exam Takeaway**

For GKE workloads whose load rises and falls over time and where both Pod and node costs matter, pick the Horizontal Pod Autoscaler together with the cluster autoscaler. Rule out any option that leaves the node pool static or that relies only on the Vertical Pod Autoscaler.

**Official References**

[**Google Cloud — About horizontal Pod autoscaling:**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) Supports: the Horizontal Pod Autoscaler scales the number of Pods with load, does not change the number of nodes, and relies on the cluster autoscaler for node scaling (Options C and D)

[**Google Cloud — About GKE cluster autoscaling:**](https://docs.cloud.google.com/kubernetes-engine/docs/cluster-autoscaler) Supports: the cluster autoscaler adds nodes when Pods can’t be scheduled and removes under-used nodes down to the node pool minimum, which is the node-layer scaling the question requires

[**Google Cloud — Vertical Pod autoscaling:**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler) Supports: the Vertical Pod Autoscaler is for analyzing and setting CPU and memory resources per Pod and for steady-state right-sizing, with horizontal autoscaling recommended for sudden spikes (Options A and B)

</details>

---

### Exam 2 · Q23

You operate a globally used service that has a 99% availability target, and your team has limited engineering capacity. For the current calendar month, measured availability is 99.5%. You need to keep the service within its defined availability goals while staying able to respond to business changes, including an upcoming launch of new features. You must also reduce technical debt and keep operational costs low, and you want to follow Google-recommended practices. What should you do?

- A. Provide N+1 redundancy for the service by provisioning additional compute capacity.
- B. Identify, quantify, and eliminate toil by automating repetitive operational tasks.
- C. Establish an error budget for the service’s availability target and work to minimize the remaining error budget.
- D. Assign the available engineers to the feature backlog while making sure the service stays within its availability target.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Identify, quantify, and eliminate toil by automating repetitive operational tasks.

**Correct Answer**

**B. Identify, quantify, and eliminate toil by automating repetitive operational tasks.**

**Exam Reasoning Explanation**

Separate the must-haves from the context. The context is that the service already beats its target, so reliability is not the problem. The must-haves are three simultaneous goals: keep meeting the target and absorb upcoming change, reduce technical debt, and minimize operational cost, all with few engineers. Test each option against all three, not just the first. An option that adds cost, or that uses the spare reliability headroom for something other than debt and cost reduction, fails a requirement. Only the option that converts engineering time into lasting automation satisfies all of them together.

**Key Exam Clues**

  * “99% target” versus “99.5% availability” — technical signal: the service is over-delivering, so the problem is not reliability and no new reliability spend is justified.

  * “limited engineering resources” — hard constraint: the chosen work must free capacity, not consume more of it ongoing.

  * “reduce technical debt while minimizing operational costs” — hard constraint: the answer must lower recurring effort and cost, which feature work or added infrastructure does not.

  * “react to business changes, including the upcoming launch” — preference: the team needs spare capacity and headroom for change, which comes from removing manual work.

**Why This Is Correct**

Toil is manual, repetitive, automatable operational work that scales with the service and brings no lasting value. Google SRE practice is to identify it, measure it, and eliminate it with engineering, keeping operational work below about half of each engineer’s time so the rest goes to projects that reduce future toil or add features. Automating toil directly reduces technical debt, lowers operating cost, and frees scarce engineers to support the launch, while the existing availability surplus gives the team room to invest in that automation safely. It satisfies every requirement at once, which none of the other options do.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** It is tempting because redundancy sounds like reliability protection ahead of a launch. But the service already exceeds its target, so extra capacity buys reliability nobody asked for while directly increasing operating cost, the opposite of what the question requires. It also does nothing about technical debt.

  * **Option C — Technically Possible but Not Best:** Error budgets are a core SRE tool, and the 99% target already implies a 1% budget, of which only half a point has been used this month. But the item asks for action on debt and cost, and “minimizing the remaining budget” would mean deliberately burning reliability headroom as an end in itself. Budgets govern how fast you may change things, not how you reduce toil or debt, so this does not solve the stated problem.

  * **Option D — Technically Possible but Not Best:** The surplus budget does permit feature velocity, which is why this is the most tempting distractor. However, it directs scarce engineers to new features and leaves technical debt and operational cost unaddressed, so it meets only the first goal and ignores the other two.

**Exam Trap**

The trap is reading “99.5% against a 99% target” as a signal to spend the error budget on feature work, which leads to Option D. The surplus budget describes what is safe to do, but the question’s explicit requirements are debt reduction and low operational cost, so the best use of limited engineers is toil elimination. If the question dropped those two requirements and asked only how to take advantage of the surplus, Option D would be the right answer.

**Foundation Concept**

An SLO defines acceptable reliability, and the gap between it and 100% is the error budget that can be spent on change and risk. Toil work is a separate lever: automation turns recurring human effort into a one-time engineering investment, which compounds by freeing capacity. Reliability work, feature work, and toil reduction compete for the same limited engineering time, so the right choice depends on which constraint the scenario emphasizes.

**Real-World Connection**

A small team notices it spends hours each week on manual certificate renewals, ad hoc capacity changes, and ticket-driven access grants. By measuring that time and automating those tasks, they cut recurring on-call and ticket load and shrink the manual surface that creates inconsistencies. When the feature launch arrives, they have engineers available and a simpler system to change, without having paid for extra infrastructure.

**Memory Hook**

When reliability already exceeds the target and the goals are less debt and lower cost, spend engineering time on removing toil, not on more capacity or more features.

**30-Second Exam Takeaway**

Read every stated goal in an SRE scenario, since the surplus-error-budget detail is a distraction when the question asks for debt and cost reduction. Choose toil elimination through automation when engineering capacity is limited and recurring manual work is the cost driver.

**Official References**

[**Google SRE Book — Eliminating Toil:**](https://sre.google/sre-book/eliminating-toil/) Supports: the correct-answer mechanism (defining toil, capping operational work at about 50 percent, and using engineering project time to reduce future toil), and the elimination of Options A and D as responses to debt and cost goals

[**Google Cloud Blog — Identifying and tracking toil using SRE principles:**](https://cloud.google.com/blog/products/management-tools/identifying-and-tracking-toil-using-sre-principles) Supports: the link between identifying, measuring, and reducing toil and lower operating costs, and the role of an SLO and error budget in deciding when to invest in automation (distinguishing Option C)

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment to Section 3, “Applying site reliability engineering practices,” covering balancing change, velocity, and reliability and managing the service lifecycle

</details>

---

### Exam 2 · Q27

Your team runs microservices on Google Kubernetes Engine (GKE). You want to detect when your error budget is being consumed so that you can protect customers and establish release policies. What should you do?

- A. Derive SLIs from metrics, and enable alerting policies to fire when the services fail to pass.
- B. Use the metrics from Cloud Service Mesh to gauge the health of the microservices.
- C. Define an SLO, and create an alerting policy on select_slo_burn_rate.
- D. Define an SLO and set up uptime checks for your services, and enable alerting policies to fire when the services fail to pass.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Define an SLO, and create an alerting policy on select_slo_burn_rate.

**Correct Answer**

**C. Define an SLO, and create an alerting policy on select_slo_burn_rate.**

**Exam Reasoning Explanation**

Work through the dependency chain the question implies. An error budget exists only when an SLO sets a target, so the answer must include defining an SLO. Next, “detect consumption” is about how quickly the budget is being used, not whether a single check passed or failed, so the alerting signal must be a rate of consumption. Finally, “protect customers” favors an early warning before the SLO is breached. Apply those three tests in order, and only one option carries an SLO and an alert on the burn rate.

**Key Exam Clues**

  * “error budget” — technical signal: an error budget is derived from an SLO target, so an SLO must be defined and an SLI alone is not enough.

  * “detect consumption” — hard constraint: the alert must measure how fast the budget is being spent, which is the burn rate.

  * “protect customers” — preference: alerting on the rate of consumption warns before the SLO is violated, instead of after.

  * “define release policies” — technical signal: budget status gives an objective basis for deciding when to slow or pause releases.

**Why This Is Correct**

An SLO combines an SLI, a target, and a compliance period, and the error budget is the amount of failure the target permits. The burn rate describes how quickly that budget is being used, and Cloud Monitoring exposes it through the time-series selector `select_slo_burn_rate`, which takes the SLO and a lookback period. A sustained burn rate above one means the service will miss its SLO for that period. An alerting policy on this selector therefore notifies the team while there is still budget left, which protects customers, and the same signal gives an objective basis for release policies, such as slowing rollouts while the budget is burning fast. Google’s guidance recommends pairing a fast-burn alert with a slow-burn alert to cover both sudden and gradual consumption.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** SLIs are measurements, and alerting when services fail to pass reacts to threshold crossings on those measurements. It is tempting because SLIs are the foundation of reliability monitoring. But without an SLO target there is no error budget, so nothing can be detected as being consumed.

  * **Option B — Different Use Case:** Cloud Service Mesh telemetry gives visibility into service health, such as latency, traffic, and error rates, and it can be the data source for an SLI. It is tempting because it is native to GKE microservices. But raw health metrics have no objective or budget attached, so they do not detect consumption or inform release policy.

  * **Option D — Technically Possible but Not Best:** Defining an SLO is correct, but alerting when an uptime check fails is binary failure alerting on probe results. It is the closest distractor because it names both an SLO and alerting. It loses because the alert is not tied to the rate at which the error budget is being spent, so it does not give the early, proportional warning the question asks for.

**Exam Trap**

The trap is Option D, since “SLO plus alerting” looks like a complete answer. The subtle distinction is what the alert evaluates: a failed check says something is down now, while a burn-rate alert says the budget is being used up faster than the SLO can tolerate. If the question had asked to be notified as soon as an endpoint becomes unreachable, uptime-check alerting would be the better fit.

**Foundation Concept**

The reliability chain runs from SLI (what you measure) to SLO (the target for it) to error budget (the permitted failure) to burn rate (how fast that allowance is being used). Alerting on burn rate ties monitoring directly to the objective, rather than to arbitrary thresholds on symptoms, and it lets teams trade release velocity against reliability using a shared measure. This is why error budget status is used to decide when to ship and when to focus on stability.

**Real-World Connection**

A team defines an availability SLO for a checkout microservice over a rolling window, then creates a fast-burn alerting policy that pages on-call and a slow-burn policy that opens a ticket. Their release policy states that non-urgent rollouts pause while the fast-burn alert is active. Customers are protected because the team reacts to rapid budget loss early, and release decisions rest on an agreed measure instead of opinion. The cost is tuning thresholds and lookback windows so alerts stay actionable.

**Memory Hook**

The SLO sets the budget, and the burn rate shows how fast you are spending it, so alert on the rate.

**30-Second Exam Takeaway**

When a question asks how to detect error budget consumption, look for an SLO plus an alerting policy based on burn rate. SLIs alone, raw mesh metrics, and uptime-check failures do not tell you how fast the budget is being used.

**Official References**

[**Google Cloud — Alerting on your burn rate (Cloud Monitoring SLO monitoring):**](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/alerting-on-budget-burn-rate) Supports: the correct-answer mechanism (burn rate of the error budget, the select_slo_burn_rate time-series selector, and fast-burn and slow-burn alert types) and the elimination of Options A and D

[**Google Cloud — Design service level objectives (Cloud Service Mesh):**](https://docs.cloud.google.com/service-mesh/docs/observability/design-slo) Supports: how SLIs, SLO targets, compliance periods, and error budgets fit together for services running on GKE with Cloud Service Mesh, which distinguishes Option B

[Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide: ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment to Section 3.1, “Balancing change, velocity, and reliability of the service,” which covers defining SLIs, SLOs, and SLAs and managing error budgets

</details>

---

### Exam 2 · Q31

You support a service that has a well-defined Service Level Objective (SLO). Over the past six months, the service has consistently met its SLO and customer satisfaction has remained high. Most of its operational tasks are automated, so few repetitive tasks occur often. You want to optimize the balance between reliability and deployment velocity while following site reliability engineering (SRE) best practices. Which two actions should you take? (Choose two.)

- A. Tighten the service’s SLO.
- B. Raise the service’s deployment velocity and/or accepted risk.
- C. Reassign engineering time to other services that need greater reliability.
- D. Persuade the product team to put reliability work ahead of new features.
- E. Revise how the service’s Service Level Indicators (SLIs) are implemented so they cover more of the service.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Raise the service’s deployment velocity and/or accepted risk. **|** C. Reassign engineering time to other services that need greater reliability.

**Correct Answer**

**B. Raise the service’s deployment velocity and/or accepted risk.**

**C. Reassign engineering time to other services that need greater reliability.**

**Exam Reasoning Explanation**

Read the scenario as a set of diagnostic signals, and ask what each says about where effort is needed. The SLO is consistently met, so reliability is sufficient. Customers are consistently happy, so the SLO matches what users need. Toil is low, so operations are not consuming engineering time. None of the signals show a shortfall, which means the service is spending less of its error budget than it is allowed to. The sensible decisions are therefore to spend that surplus on speed and to move scarce engineering capacity to where reliability is lacking. Options that add reliability investment to an already healthy service, or that adjust measurement without a trigger, do not follow from the signals.

**Key Exam Clues**

  * “consistently met its SLO” over six months — technical signal: reliability exceeds what is required, so error budget is going unused.

  * “customer satisfaction has been consistently high” — hard constraint on the answer: the current SLO is adequate for users, so there is no basis for raising the target.

  * “Most of the service’s operational tasks are automated” — technical signal: toil is low, so there is no toil-reduction work to prioritize.

  * “optimize the balance between reliability and deployment velocity” — hard constraint: with reliability in surplus, the balance should move toward velocity.

  * “(Choose two.)” — cardinality instruction: select two complementary actions that together redeploy the surplus.

**Why This Is Correct**

Option B uses the surplus reliability directly. An SLO defines the reliability users need, and the error budget exists so it can be spent on change and risk; consistently leaving it unspent means releases are slower or more cautious than necessary. Releasing faster or accepting more risk converts that headroom into delivery speed while the SLO still defines the safe boundary. Option C addresses the other surplus, people. Engineers are scarce, and their time should go to the most important characteristics of the most important services, so with this service stable and toil low, capacity is better used on services that fall short of their reliability needs. The two actions are complementary and cover both resources the scenario leaves unspent, error budget and engineering time.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** A stricter SLO shrinks the error budget and increases the cost of reliability, yet customers are already happy at the current target. It is tempting because the team is beating the target easily, but it moves the balance toward reliability when the signals call for velocity, and it sets a bar users did not ask for.

  * **Option D — Violates Requirement:** Prioritizing reliability over new features is the right response to a missed SLO or exhausted error budget. Here the SLO is met and customers are satisfied, so this reverses the intended use of the budget and slows delivery with no benefit.

  * **Option E — Different Use Case:** Increasing SLI coverage is valuable when indicators miss important user journeys, for example when customers are unhappy even though the SLO is met. The scenario shows the opposite, so there is no evidence the SLIs are inadequate, and the change does not address the reliability-versus-velocity balance.

**Exam Trap**

The most tempting distractor is Option A, because “we are easily exceeding the target, so raise the bar” feels like continuous improvement. The distinction is that SLOs reflect user needs and cost, not engineering pride, and happy customers indicate the target is already right. If customers had been unhappy while the SLO was being met, tightening the SLO or improving SLI coverage (Option E) would become the correct direction.

**Foundation Concept**

An SLO sets the reliability level at which user happiness and cost are balanced, and the error budget is the tolerated unreliability that can be traded for velocity. Reliability beyond the target has diminishing value and real costs, such as slower releases and engineering time that could go elsewhere. SRE decision making combines three signals: whether the SLO is met, whether customers are happy, and how much toil exists. Different combinations point to different actions, and this combination points toward spending surplus rather than adding investment.

**Real-World Connection**

A team whose service has comfortably exceeded its SLO for two quarters shortens release cycles, reduces canary soak times, and takes on a long-delayed migration while watching error budget burn-rate alerts. They also lend an engineer to a neighboring service that keeps missing its SLO. Feature delivery speeds up and reliability effort is focused where it is needed, with the SLO and burn-rate alerting acting as the guardrail if the added risk causes problems.

**Memory Hook**

Surplus reliability is unspent budget, so spend it on velocity and send spare engineers where reliability is short.

**30-Second Exam Takeaway**

When a service consistently beats its SLO, users are happy, and toil is low, shift the balance toward velocity and move engineering capacity to services that need reliability. Tighten the SLO or prioritize reliability work only when the signals show unhappy users or a missed SLO.

**Official References**

[**Google SRE Workbook — Implementing SLOs:**](https://sre.google/workbook/implementing-slos/) Supports: the correct-answer mechanism for options B and C (SLOs reflect user happiness, engineering time should go to the most important services, and decisions about reliability versus functionality follow from SLO and error budget status), and the elimination of options A, D, and E

[Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide: ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment to Section 3.1, “Balancing change, velocity, and reliability of the service,” which covers SLOs, error budgets, and the opportunity cost of risk and reliability

</details>

---

### Exam 2 · Q33

You support a user-facing web application. When you analyze its error budget for the past six months, you find that it has never used more than 5% of its error budget in any given time window. You hold a Service Level Objective (SLO) review with business stakeholders and confirm that the SLO is set appropriately. You want the application’s SLO to reflect its observed reliability more closely. Which two steps can you take to further that goal while balancing velocity, reliability, and business needs? (Choose two.)

- A. Add more serving capacity to every zone the application runs in.
- B. Make application releases more frequent or potentially riskier.
- C. Tighten the SLO to match the application’s observed reliability.
- D. Implement and measure additional Service Level Indicators (SLIs) for the application.
- E. Announce planned downtime to use up more of the error budget, and make sure users are not depending on a tighter SLO.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Make application releases more frequent or potentially riskier. **|** E. Announce planned downtime to use up more of the error budget, and make sure users are not depending on a tighter SLO.

**Correct Answer**

**B. Make application releases more frequent or potentially riskier.**

**E. Announce planned downtime to use up more of the error budget, and make sure users are not depending on a tighter SLO.**

**Exam Reasoning Explanation**

Identify what is fixed and what can move. The SLO is fixed, because stakeholders just confirmed it matches business needs. What can move is the observed reliability, which is far higher than the SLO requires. The goal of aligning the two therefore has to be met from the observed side, by deliberately using some of the unspent error budget, and not by changing the target. Evaluate each option by asking whether it spends surplus budget safely or whether it adds reliability, changes the agreed target, or only changes measurement. Only two options spend the surplus in ways the business can accept.

**Key Exam Clues**

  * “never consumed more than 5% of its error budget” — technical signal: reliability substantially exceeds the SLO, so most of the budget goes unused.

  * “confirm that the SLO is set appropriately” — hard constraint: the SLO target should stay as it is, so the gap must be closed by moving observed reliability.

  * “SLO to more closely reflect its observed reliability” — goal statement: reduce the over-delivery rather than reinforce it.

  * “balancing velocity, reliability, and business needs” — preference: favor actions that convert surplus reliability into delivery speed without breaking business commitments.

  * “(Choose two.)” — cardinality instruction: pick two complementary ways to spend the budget.

**Why This Is Correct**

Option B spends the unused budget on change. Releases are a major source of outages, so more frequent or somewhat riskier releases use budget in exchange for velocity, and the SLO remains the boundary that limits how far to go. Option E addresses a less obvious risk of over-delivering: users come to depend on the reliability they actually observe, not the reliability promised, so an SLO that is greatly exceeded effectively becomes a tighter implicit SLO. Google describes this with its Chubby lock service, where SRE makes a service meet, but not significantly exceed, its SLO, and introduces planned outages so dependents do not assume it never fails. The two work together: B uses the surplus to speed delivery, and E uses part of it to reset user expectations and expose hidden dependencies. Both lower observed reliability toward the SLO while staying within the agreed budget, which makes the pair complete for the stated goal.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Extra capacity in every zone raises reliability and cost further, which widens the gap between the SLO and observed reliability, the opposite of the goal.

  * **Option C — Violates Requirement:** Matching the SLO to observed performance is tempting because it makes the two numbers agree immediately. But the SLO has just been validated against business needs, and SLOs should reflect what users and the business require, not what the system happens to deliver. Tightening shrinks the error budget, leaving less room for change and slowing velocity, and it commits the team to a level nobody asked for.

  * **Option D — Different Use Case:** More SLIs improve measurement coverage, which is valuable if existing indicators miss important user journeys. Nothing in the scenario suggests the SLIs are inadequate, and extra measurement does not close the gap between a validated SLO and the unused budget.

**Exam Trap**

The most tempting distractor is Option C, because “make the SLO match observed reliability” reads like the literal request. The distinction is that the SLO review confirmed the target, so the question is asking how to bring behavior toward the target. If stakeholders had instead determined that users really needed higher reliability, tightening the SLO would become appropriate, and if the SLIs were found to miss key user journeys, Option D would become relevant.

**Foundation Concept**

An SLO sets the reliability users and the business actually need, and the error budget is the amount of unreliability that can be traded for other benefits. Persistently exceeding the SLO is not free: it slows delivery, raises cost, and teaches users to rely on performance that was never promised, which creates a de facto tighter SLO. SRE therefore treats unused budget as something to spend deliberately. In production, any planned downtime must stay within the budget, be announced in advance, and be coordinated with dependent teams.

**Real-World Connection**

A team that has never used more than a small share of its error budget increases release frequency and shortens canary soak times. It also schedules announced, time-boxed maintenance events sized to use part of the budget, and tells dependent teams so they add retries and fallbacks. Delivery speeds up and downstream services become more resilient, with burn-rate alerting watching that the budget is not overspent.

**Memory Hook**

Meet the SLO without greatly exceeding it, because unspent budget is wasted velocity and a hidden promise.

**30-Second Exam Takeaway**

When a service far outperforms an SLO that stakeholders have confirmed, close the gap by spending budget safely, through faster or riskier releases and announced planned downtime. Do not tighten the SLO, add capacity, or simply measure more.

**Official References**

[**Google SRE Book — Service Level Objectives:**](https://sre.google/sre-book/service-level-objectives/) Supports: the correct-answer mechanism for options B and E (users rely on actual performance, and the Chubby example of meeting but not significantly exceeding an SLO with planned outages), and the elimination of Option C

[Google SRE Workbook — Implementing SLOs: ](https://sre.google/workbook/implementing-slos/)Supports: the use of error budgets to balance reliability against change and velocity, which eliminates Option A and distinguishes Option D

</details>

---

### Exam 2 · Q34

Your development team has built a new version of its service’s API. You need to roll out the new version with the least possible disruption to third-party developers and to the end users of third-party installed applications. What should you do?

- A. Introduce the new API version. Announce the deprecation of the old version. Deprecate the old version. Contact the remaining users of the old version. Provide best-effort support to users of the old version. Turn down the old version.
- B. Announce the deprecation of the old version. Introduce the new API version. Contact the remaining users of the old version. Deprecate the old version. Turn down the old version. Provide best-effort support to users of the old version.
- C. Announce the deprecation of the old version. Contact the remaining users of the old version. Introduce the new API version. Deprecate the old version. Provide best-effort support to users of the old version. Turn down the old version.
- D. Introduce the new API version. Contact the remaining users of the old version. Announce the deprecation of the old version. Deprecate the old version. Turn down the old version. Provide best-effort support to users of the old version.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Introduce the new API version. Announce the deprecation of the old version. Deprecate the old version. Contact the remaining users of the old version. Provide best-effort support to users of the old version. Turn down the old version.

**Correct Answer**

**A. Introduce the new API version. Announce the deprecation of the old version. Deprecate the old version. Contact the remaining users of the old version. Provide best-effort support to users of the old version. Turn down the old version.**

**Exam Reasoning Explanation**

Because every option contains the same six steps, the question is purely about ordering, so derive the ordering rules from the constraint. Third-party developers and their installed applications cannot be upgraded on your schedule, so every step that pressures users must come after something that makes the pressure reasonable, and the only step that breaks clients must come last. That yields four dependencies: the replacement exists before anyone is asked to migrate, notice comes before the deprecation takes effect, outreach to remaining users follows the migration period, and support for stragglers is offered while the old version still runs, before it is turned down. Check each option for violations, and only one has none.

**Key Exam Clues**

  * “least disruption to third-party developers and end users” — hard constraint: clients you do not control must keep working throughout, so the breaking step, turn down, must come last.

  * “third-party installed applications” — technical signal: installed apps update slowly and unpredictably, so a long overlap and direct outreach are needed.

  * “deploy the new versions of the API” — sequence instruction: the new version must be available first so there is something to migrate to.

  * “remaining users” and “best-effort support” — sequence signals: these steps address stragglers after migration has begun and before the old version is removed.

**Why This Is Correct**

Option A follows the dependency order. Introducing the new version first gives users a destination. Announcing the deprecation then gives them notice and a timeline, and deprecating the old version formally marks it as superseded. Contacting the remaining users comes next, because only after the migration period can you identify who has not moved. Providing best-effort support to those users helps them finish migrating while the old version still works, and turning it down last removes the old version only after migration has been supported, which keeps disruption to a minimum. This matches Google’s published API guidance that an older version must go through a reasonable, well-communicated deprecation period before it is shut down.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Violates Requirement:** It announces deprecation before the new version exists, so users are told to leave with nowhere to go. It also provides support after turning the old version down, when the users who needed help have already lost service.

  * **Option C — Violates Requirement:** It announces deprecation and contacts users before introducing the replacement, so the outreach has nothing to offer them. Starting the process this way creates exactly the disruption the question is trying to avoid.

  * **Option D — Violates Requirement:** It starts correctly by introducing the new version, which makes it the most tempting distractor. It then contacts the remaining users before any deprecation announcement, so there is no migration period from which anyone could be “remaining,” and it offers support only after the old version has been turned down.

**Exam Trap**

The trap is Option D, because it shares the correct first step and looks nearly identical to A. The errors are in the middle and end: outreach before announcement, and support after shutdown. Support after turn-down is illogical under any reading, so no single changed requirement would make D correct. As a rule of thumb, scan each sequence for the turn-down step, which must be last.

**Foundation Concept**

When you run an API consumed by clients you do not control, the producer owns the migration timeline but not the clients’ release schedules. Safe lifecycle management therefore follows a pattern: ship the replacement, give notice, keep the old version working during an overlap, identify and help stragglers, and remove the old version last because removal is the only step that breaks clients. The exam’s six-step labels are framing for this pattern; Google’s API guidance (AIP-185) states the general requirement as a reasonable, well-communicated deprecation period before shutdown.

**Real-World Connection**

A team publishes v2 beside v1 behind the same API gateway and announces a deprecation timeline with dates. It marks v1 as deprecated in documentation and responses, then uses request logs and API keys to find the callers who are still on v1 and contacts them directly. After helping those callers migrate, it turns v1 down once traffic is negligible. Partner applications keep working throughout, and the cost is running two versions in parallel during the overlap.

**Memory Hook**

Replacement first and shutdown last, with notice before deprecation and outreach before turn-down.

**30-Second Exam Takeaway**

For API version retirement questions, order the steps by dependency: new version, announcement, deprecation, outreach to remaining users, support, then turn-down. Reject any sequence that asks users to migrate before the replacement exists or that supports users after the old version is gone.

**Official References**

[**Google API Improvement Proposals — AIP-185: API Versioning:**](https://google.aip.dev/185) Supports: Google’s guidance that an older API version must go through a reasonable, well-communicated deprecation period before being shut down, which underpins the ordering in option A

[Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide: ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment to Section 3.2, “Managing service lifecycle,” which covers service management from planning and deployment through maintenance and retirement

</details>

---

### Exam 2 · Q35

You are drafting the action items in a postmortem for an outage and assigning people to them. The outage has ended, but its root causes still need to be fixed, and you want the team to complete the action items promptly and efficiently. What is the best way to assign owners and collaborators to the action items?

- A. Name one owner for each action item, and add collaborators where needed.
- B. Name several owners for each item so the team is guaranteed to complete items quickly.
- C. Name collaborators only, with no individual owner, so the postmortem stays blameless.
- D. Name the team lead as the owner of every action item, because they lead the SRE team.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Name one owner for each action item, and add collaborators where needed.

**Correct Answer**

**A. Name one owner for each action item, and add collaborators where needed.**

**Exam Reasoning Explanation**

Begin with the one hard requirement, which is that corrective work gets finished quickly and efficiently. Then picture each assignment model once the incident pressure has faded and the item competes with feature work. Speed depends on whether someone clearly knows the item is theirs to push, and on whether helpers know whom they are supporting. So separate the two roles in the question: an accountable owner and supporting collaborators. Screen each option for whether it keeps accountability single, present, and close to the work. Only one option meets all three conditions.

**Key Exam Clues**

  * “address the root causes” — technical signal: the action items are corrective work that must be completed, and recording them alone does not reduce risk.

  * “quickly and efficiently” — hard constraint: the assignment model must remove ambiguity about who drives the item and avoid handoff delays.

  * “owners and collaborators” — technical signal: these are separate roles, so the answer must define both and keep them distinct.

  * “The outage is over” — context clue: with no incident urgency, follow-through depends on clear ownership while other priorities compete.

**Why This Is Correct**

One named owner is accountable for moving the item from idea to completion, which means a single person tracks status, chases dependencies, and escalates blockers. Collaborators contribute expertise or access, such as another team’s system, without sharing the accountability. This keeps decisions fast, because one person can proceed without waiting for agreement among several people. It also matches how SRE guidance treats postmortem action items: as prioritized, tracked work that needs a clear accountable person to reach closure. The pair of roles is complete for the question, since it covers who drives the work and who supports it.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Violates Requirement:** Several owners sounds like extra assurance, which is why it is tempting. But shared ownership spreads responsibility, so each person can reasonably assume another is handling the item, and coordination overhead rises. Nothing about it guarantees speed.

  * **Option C — Violates Requirement:** Blameless postmortems avoid assigning fault for what happened. They do not remove accountability for completing the fix. With no individual owner, nobody is answerable for progress, so items tend to stall, which defeats the goal of addressing root causes.

  * **Option D — Technically Possible but Not Best:** The team lead is a single accountable person, so this option does not fail on ambiguity. It loses because routing every item through one person creates a bottleneck, and ownership follows seniority instead of who is best placed to do the work, which slows items that need hands-on expertise.

**Exam Trap**

The strongest distractor is Option C, because it applies the blameless principle to the wrong thing. Blamelessness concerns how the incident’s causes are analyzed and described, whereas ownership of a corrective action is forward-looking accountability. If the question had asked how to write the incident narrative without attributing fault to individuals, then not naming people would be the right approach.

**Foundation Concept**

Accountability and blame are different ideas: blame looks backward at fault, while ownership looks forward at who will deliver the change. Tasks shared among many people are prone to diffusion of responsibility, and the usual remedy is one accountable person supported by contributors, a pattern similar to the accountable and consulted roles in responsibility-assignment models. Good action items are also prioritized, tracked in the team’s normal work system, and reviewed on a regular cadence so they do not fade after the postmortem is published.

**Real-World Connection**

After a memory-exhaustion outage, an action item to add a saturation alert is assigned to one engineer on the owning service team, with the observability team listed as a collaborator. The item has a priority and due date in the issue tracker and is checked in the weekly reliability review. The owner reports status and raises any blocker with the collaborating team, so the fix competes fairly with feature work and gets closed.

**Memory Hook**

One owner drives each item, and collaborators help without sharing the accountability.

**30-Second Exam Takeaway**

For postmortem action items, choose a single accountable owner with collaborators as needed. Eliminate multiple owners, ownerless items justified by blamelessness, and blanket assignment to the team lead.

**Official References**

[**Google SRE Workbook — Postmortem Culture: Learning from Failure:**](https://sre.google/workbook/postmortem-culture/) Supports: the correct-answer mechanism, since it explains what makes postmortem action items actionable for preventing recurrence, including clear priorities, and why options that blur accountability fall short

[**USENIX ;login: — Postmortem Action Items: Plan the Work and Work the Plan (Google SRE):**](https://www.usenix.org/publications/login/spring2017/lunney) Supports: Google’s approach to categorizing, prioritizing, and tracking action items so that they are actually executed

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment to Section 3, “Applying site reliability engineering practices,” whose incident-related objectives (3.3) cover post-incident follow-through

</details>

---

### Exam 2 · Q37

Your company applies Site Reliability Engineering (SRE) principles. You are writing the postmortem for an incident that was triggered by a software change and severely affected users. You want to prevent a severe incident like this from happening again. What should you do?

- A. Identify the engineers responsible for the incident and escalate the matter to senior management.
- B. Make sure that test cases capable of catching errors of this kind pass before new software releases.
- C. Follow up with the employees who reviewed the changes and prescribe the practices they should follow going forward.
- D. Design a policy requiring on-call teams to immediately call engineers and management to agree on a plan of action whenever an incident occurs.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Make sure that test cases capable of catching errors of this kind pass before new software releases.

**Correct Answer**

**B. Make sure that test cases capable of catching errors of this kind pass before new software releases.**

**Exam Reasoning Explanation**

Start from the SRE principle that postmortems look for systemic causes, not culprits, and that their action items should reduce the chance of recurrence. Then ask where the failure entered: a software change reached users, so a control was missing between code and release. Test each option on two questions: does it target the system or specific people, and does it prevent the failure or only react to it? Options that point at individuals fail the first test, an option about response coordination fails the second, and only one option adds a systemic preventive control.

**Key Exam Clues**

  * “follows Site Reliability Engineering principles” — technical signal: postmortems are blameless and focus on contributing causes in the system, not on individuals.

  * “triggered by a software change” — technical signal: the defect passed through the release process, so the fix belongs before release.

  * “prevent severe incident from happening in the future” — hard constraint: the action must lower the likelihood of recurrence, not just improve how the next incident is handled.

  * “writing a postmortem” — context clue: the deliverable is concrete action items that address root causes.

**Why This Is Correct**

The incident shows a gap: a class of error was able to reach users because no release-time check caught it. Adding test cases that detect this kind of error, and requiring them to pass before new releases, converts the lesson into an automated, repeatable control. It works no matter who writes or reviews a change, which is what a systemic fix should do. In Google’s classification of postmortem action items, it is a prevention-type item, the type that aims to stop recurrence or reduce its impact, whereas items that only mitigate or improve response leave the underlying defect path open.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Naming responsible engineers and escalating them is the opposite of blameless practice. It is tempting because it appears to create accountability, but it discourages honest reporting and changes nothing in the system, so the same class of error can recur with a different author.

  * **Option C — Violates Requirement:** Following up with reviewers and prescribing practices sounds like process improvement, which makes it tempting. It still singles out individuals, and it relies on people remembering to apply guidance each time, which is a weaker and less reliable control than an automated test gate.

  * **Option D — Different Use Case:** A call-out policy improves coordination during an incident, which is valid incident management practice. It does not stop a faulty change from reaching users, and it would apply to every incident regardless of severity, so it fails the prevention requirement.

**Exam Trap**

The strongest distractor is Option C, because improving the review process feels like a systemic fix. The distinction is that it targets the people who reviewed the change and depends on their future diligence, while the SRE approach is to fix the system with controls that do not depend on any one person. If the question had asked how to shorten response time to future incidents, Option D would move up, since it addresses coordination rather than prevention.

**Foundation Concept**

A blameless postmortem identifies contributing causes without indicting individuals or teams, because people who fear punishment hide problems and the organization stops learning. The output is a set of concrete, owned, tracked action items, which Google categorizes as investigate, mitigate, repair, detect, and prevent. Prefer automated prevention, such as tests and pipeline gates, over reminders, training, or additional approvals. Google’s SRE Workbook also warns against postmortems whose action items are mostly mitigative and fail to address recurrence.

**Real-World Connection**

After an outage caused by an unvalidated configuration change, a team writes a regression test that reproduces the failure pattern and makes it a required check in its release pipeline. The postmortem records the action item with an owner and a due date and tracks it to closure. Releases that would trigger the same class of failure are now blocked automatically, at the cost of maintaining the test and a slightly longer pipeline.

**Memory Hook**

Fix the system, not the person, by turning the lesson into an automated release gate.

**30-Second Exam Takeaway**

In an SRE postmortem question about preventing recurrence, pick the systemic, automated control that closes the gap the change slipped through. Reject answers that blame or retrain individuals, and answers that only improve incident response.

**Official References**

[**Google SRE Book — Postmortem Culture: Learning from Failure:**](https://sre.google/sre-book/postmortem-culture/) Supports: the blameless-postmortem principle and the focus on contributing causes over individuals, which eliminates Options A and C

[**Google SRE Workbook — Postmortem Culture: Learning from Failure:**](https://sre.google/workbook/postmortem-culture/) Supports: the need for action items that prevent recurrence and not merely mitigate, which supports option B over option D

</details>

---

### Exam 2 · Q38

You are responsible for the reliability of a high-volume enterprise application. Many users report that an important part of its functionality, a data-intensive reporting feature, consistently fails with an HTTP 500 error. When you review the application’s dashboards, you see a strong correlation between the failures and a metric that tracks the size of an internal queue used to generate reports. You trace the failures to a reporting backend with high I/O wait times, and you resolve the problem quickly by resizing the backend’s persistent disk (PD). Now you need to create an availability Service Level Indicator (SLI) for the report generation feature. How should you define it?

- A. As the I/O wait times aggregated across all report generation backends.
- B. As the proportion of report generation requests that result in a successful response.
- C. As the application’s report generation queue size compared with a known-good threshold.
- D. As the reporting backend’s PD throughput capacity compared with a known-good threshold.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. As the proportion of report generation requests that result in a successful response.

**Correct Answer**

**B. As the proportion of report generation requests that result in a successful response.**

**Exam Reasoning Explanation**

Separate the diagnostic story from the actual ask. The troubleshooting details, queue size, I/O wait, and disk capacity, describe what caused one incident, whereas the requirement is an availability indicator for the feature. An availability SLI should answer one question: did users get a successful result when they asked for a report? Test each option on whether it counts successful outcomes against all valid attempts, or whether it measures an internal condition that merely correlated with failure. Only one option is a direct measure of the user-visible outcome, and the rest are cause-side signals.

**Key Exam Clues**

  * “availability Service Level Indicator” — hard constraint: the indicator must express whether requests to the feature succeed, not how a component is behaving.

  * “report generation feature” — scope clue: the SLI should be limited to requests for this feature, not the whole application.

  * “consistently failing with an HTTP 500 error” — technical signal: the user-visible failure is a failed response, so success versus failure of responses is the natural basis for good and bad events.

  * “queue size,” “I/O wait times,” and “persistent disk” — exclusion signals: these are causes found during troubleshooting, and an SLI built on them would track one failure mode instead of availability.

**Why This Is Correct**

An SLI is most useful as a ratio of good events to valid events, and for availability the natural form is the proportion of requests that were served successfully. Defining it as the share of report generation requests that return a successful response measures exactly what users experience, and it moves down whatever the cause of failure is, whether disk I/O, a full queue, a software defect, or something not yet seen. That makes it a stable basis for an SLO and an error budget. One boundary is to define “valid” and “good” explicitly, for example by excluding health checks and by treating 5xx responses as bad events.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Different Use Case:** I/O wait time is a resource saturation signal that is valuable for diagnosing backend performance, and it is tempting because it was the cause here. But it does not say whether requests succeeded: high I/O wait may not break requests, and requests can fail with low I/O wait.

  * **Option C — Technically Possible but Not Best:** Queue size correlated strongly with failures, which makes it attractive as a signal and potentially useful as a leading indicator for alerting. It is still an internal proxy, and a threshold on it describes system state instead of user-visible success, so it can miss failures that have other causes and can fire when users are unaffected.

  * **Option D — Different Use Case:** Disk throughput capacity compared with a threshold is a capacity-planning and configuration measure, and resizing the disk was the fix for this incident. It says nothing directly about whether report requests succeed, and the “known-good” threshold is subjective.

**Exam Trap**

The strongest distractor is Option C, because the dashboard correlation makes the queue metric feel authoritative. The distinction is that SLIs measure the outcome users experience, while queue size is one of several possible causes of a bad outcome. If the question had asked for an early-warning alert that fires before users are affected, a queue-size threshold would be a reasonable leading indicator for that purpose.

**Foundation Concept**

An SLI is a carefully defined measure of an aspect of the service level that users receive, and the preferred form is good events divided by valid events. SLIs and SLOs should reflect user experience, so they track symptoms, while cause-based metrics such as saturation, queue depth, and I/O wait belong on diagnostic dashboards and in supporting alerts. Common SLI types for request-driven features are availability, latency, and quality, and each requires a precise definition of which events count as valid and which count as good.

**Real-World Connection**

A team defines the report feature’s availability SLI as the number of report requests answered with a non-5xx status divided by all report requests, measured at the load balancer or in application metrics. It sets an SLO over a rolling window and alerts on error budget burn rate. I/O wait and queue depth stay on a diagnostic dashboard with warning alerts. The SLI drops no matter what breaks the feature, though it does not explain why, so the diagnostic signals remain necessary for troubleshooting.

**Memory Hook**

An SLI measures what users get, as good over valid events, not what a backend is doing.

**30-Second Exam Takeaway**

When asked to define an availability SLI, choose the ratio of successful requests to valid requests for the feature in question. Do not pick resource, queue, or capacity metrics, which are causes that help diagnose problems but do not measure availability.

**Official References**

[**Google SRE Book — Service Level Objectives:**](https://sre.google/sre-book/service-level-objectives/) Supports: the correct-answer mechanism, including the definition of an SLI as a carefully defined measure of the service level provided and the guidance to build indicators around what users care about, which eliminates options A, C, and D

[**Google SRE Workbook — Implementing SLOs:**](https://sre.google/workbook/implementing-slos/) Supports: the request-based SLI form, the proportion of good requests among all valid requests, and how SLIs feed SLOs and error budgets

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment to Section 3.1, “Balancing change, velocity, and reliability of the service,” which covers defining SLIs such as availability and latency, SLOs, and SLAs

</details>

---

### Exam 2 · Q40

You are writing the postmortem for an incident that had a severe impact on users, and you want to prevent similar incidents in the future. Which two of the following sections should you include in the postmortem? (Choose two.)

- A. An explanation of the incident’s root cause.
- B. A list of the employees responsible for causing the incident.
- C. A list of action items to prevent the incident from recurring.
- D. Your personal assessment of how the incident’s severity compares with past incidents.
- E. Copies of the design documents for every service the incident affected.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. An explanation of the incident’s root cause. **|** C. A list of action items to prevent the incident from recurring.

**Correct Answer**

**A. An explanation of the incident’s root cause.**

**C. A list of action items to prevent the incident from recurring.**

**Exam Reasoning Explanation**

The stated purpose is prevention of similar incidents, so the test for each section is whether it helps the organization understand why the failure happened or change something so it does not happen again. Sections that identify people, offer subjective rankings, or bulk up the document with reference material do not serve that purpose. Because the question asks for two answers, look for a complementary pair: one section that diagnoses and one that prescribes. That pair covers the learning loop, from understanding the cause to acting on it.

**Key Exam Clues**

  * “prevent similar incidents in the future” — hard constraint: every included section must contribute to understanding causes or driving corrective change.

  * “postmortem” — technical signal: SRE postmortems are blameless learning documents, so sections that single out individuals are excluded.

  * “severely affected users” — context clue: a serious incident warrants a thorough causal analysis and concrete follow-up work.

  * “(Choose two.)” — cardinality instruction: pick two sections that together form a diagnosis-and-remediation pair.

**Why This Is Correct**

An explanation of the root cause, or more precisely the contributing causes, records why the incident happened and gives readers the understanding needed to find similar weaknesses elsewhere. A list of action items turns that understanding into work: concrete, prioritized changes with owners that reduce the chance or impact of recurrence. The two sections work together and neither is sufficient alone, since cause analysis without actions leaves the gap open, and actions without a causal explanation risk fixing the wrong thing. Together they are the minimum that delivers the question’s goal.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Violates Requirement:** A list of people responsible turns the postmortem into a blame exercise. It is tempting because accountability sounds useful, but SRE postmortems are blameless, since blaming individuals discourages honest reporting and leaves the underlying system gaps unaddressed.

  * **Option D — Technically Possible but Not Best:** A severity comparison can add context, and teams often record impact and severity in a postmortem. A personal opinion on how it ranks against past incidents is subjective, so it does not explain the cause or lead to a fix, and it is not among the sections that serve the stated prevention goal.

  * **Option E — Different Use Case:** Design documents are reference material for understanding a system, and a postmortem may link to specific relevant ones. Attaching copies for every impacted service adds bulk without analysis, and it does not explain this incident or prescribe changes.

**Exam Trap**

The strongest distractor is Option B, because naming those involved feels like part of an honest account. The distinction is that postmortems analyze the system conditions that allowed the failure, and people appear in the timeline only as actors whose decisions the system made possible. If the question asked for the incident timeline, referring to roles or decisions made at each step would be appropriate, but a list of culprits would still not be.

**Foundation Concept**

A postmortem is a written record of an incident: its impact, the actions taken to resolve it, the contributing causes, and the follow-up actions to prevent recurrence. Blameless practice focuses on those causes without indicting individuals or teams, because people who fear punishment hide problems and organizations stop learning. Good action items are concrete, prioritized, owned, and tracked to completion, and they cover prevention as well as detection and mitigation.

**Real-World Connection**

After an outage caused by a configuration change that overloaded a backend, the team writes a postmortem with a causal analysis that explains why the change passed review and why alerts fired late. The action items add a pre-release load check and a saturation alert, each with an owner and due date. Other teams read it and apply the same checks to their services, so the incident produces systemic improvement instead of a list of names.

**Memory Hook**

A postmortem explains why it happened and what will change, never who to blame.

**30-Second Exam Takeaway**

For postmortem content questions, include the root-cause analysis and the action items that prevent recurrence. Exclude lists of people, subjective opinions, and bulk attachments that do not drive learning or change.

**Official References**

[**Google SRE Book — Postmortem Culture: Learning from Failure:**](https://sre.google/sre-book/postmortem-culture/) Supports: the correct-answer mechanism, since it describes postmortems as documentation of the incident, its root causes, and the follow-up actions to prevent recurrence, and it establishes the blameless principle that eliminates option B

[**Google SRE Workbook — Postmortem Culture: Learning from Failure:**](https://sre.google/workbook/postmortem-culture/) Supports: the need for actionable items that prevent recurrence, which supports option C and distinguishes the other options

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment to Section 3, “Applying site reliability engineering practices,” whose incident-related objectives (3.3) cover post-incident learning

</details>

---

### Exam 2 · Q42

You support a popular mobile game application deployed on Google Kubernetes Engine (GKE) across several Google Cloud regions, and each region has multiple Kubernetes clusters. You receive a report that none of the users in one specific region can connect to the application. You want to resolve the incident in line with Site Reliability Engineering (SRE) practices. What should you do first?

- A. Redirect user traffic from the affected region to the other regions that report no issues.
- B. Use Cloud Monitoring to look for a spike in CPU or memory usage in the affected region.
- C. Add a node pool of high-memory, high-CPU machine type instances to the cluster.
- D. Use Cloud Logging to filter on the affected region’s clusters and inspect the error messages in the logs.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Redirect user traffic from the affected region to the other regions that report no issues.

**Correct Answer**

**A. Redirect user traffic from the affected region to the other regions that report no issues.**

**Exam Reasoning Explanation**

The word “first” makes this a sequencing question, and the SRE rule for incidents is to limit user impact before investigating the cause. Sort the options into two groups: those that restore service for users now, and those that gather information or attempt a fix. Then ask whether a restoring option is available. Multiple healthy regions exist, so redirecting users is possible and fast. Every investigative or speculative action therefore comes later, because users remain unable to connect while you perform it.

**Key Exam Clues**

  * “none of the users in a specific region can connect” — technical signal: total impact confined to one region, which makes the region a clear unit to isolate or drain.

  * “across several Google Cloud regions” with multiple clusters each — technical signal: redundancy exists, so healthy regions can serve the affected users.

  * “following Site Reliability Engineering practices” — hard constraint: mitigation takes priority over root-cause analysis during an incident.

  * “What should you do first?” — sequence instruction: the first action must reduce user impact, and diagnosis belongs after it.

**Why This Is Correct**

Redirecting traffic away from the failing region restores service to users within the time it takes to change routing, without needing to know why the region failed. This follows Google’s SRE guidance that the first response in a major outage should be to make the system work as well as it can under the circumstances, for example by diverting traffic from a broken cluster to others, and not to chase the root cause immediately. It also preserves the failing region intact for investigation afterward. One prerequisite is that the remaining regions must have enough capacity headroom to absorb the redirected load, since overloading them would spread the outage.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Technically Possible but Not Best:** Checking CPU and memory in the affected region is a sound diagnostic step, which is why it is tempting. But it only examines one hypothesis, and users remain unable to connect for as long as the investigation takes, so it belongs after mitigation.

  * **Option C — Violates Requirement:** Adding larger instances assumes the problem is a capacity shortage, which has no supporting evidence. It takes time, adds cost, and may not address a connectivity failure at all, so it is a guess that leaves users down.

  * **Option D — Technically Possible but Not Best:** Inspecting logs is the reflexive first move in troubleshooting, and it will eventually be needed to find the cause. As a first action it delays relief for users, and it can be done more calmly once traffic is flowing to healthy regions.

**Exam Trap**

The strongest distractor is Option D, because looking at logs feels like the natural start of any investigation. The distinction is that SRE separates mitigation from diagnosis, and Google’s guidance explicitly tells responders to resist the instinct to start with root-cause hunting. If the question had asked what to do next, after traffic was moved, then inspecting logs and metrics in the affected region would be the right answer.

**Foundation Concept**

An incident has distinct phases: detect, mitigate, diagnose, fix, and learn. Mitigation reduces user impact using fast, reversible actions such as draining or redirecting traffic, rolling back a change, or adding capacity, and it does not require understanding the cause. Diagnosis and the permanent fix follow once users are protected. Multi-region redundancy exists so that one region’s failure can be absorbed by others, but that only works if capacity and routing controls were prepared in advance.

**Real-World Connection**

An on-call engineer sets the affected region’s weight to zero in the global load balancer or traffic management layer and watches saturation in the healthy regions. Players reconnect within minutes through other regions, at somewhat higher latency. The team then examines logs and metrics in the isolated region, fixes the fault, and shifts traffic back gradually. The main risk is overloading the receiving regions, so their headroom is checked before and during the shift.

**Memory Hook**

Stop the bleeding first, then find the cause.

**30-Second Exam Takeaway**

In “what should you do first” incident questions, choose the fast mitigation that restores user service, such as redirecting traffic or rolling back. Diagnostic steps like checking logs and metrics, and speculative fixes like adding capacity, come after impact is reduced.

**Official References**

[**Google SRE Book — Effective Troubleshooting:**](https://sre.google/sre-book/effective-troubleshooting/) Supports: the correct-answer mechanism, since it advises that the first response to a major outage is to make the system work as well as possible, for example by diverting traffic from a broken cluster, instead of immediately seeking the root cause, which eliminates options B, C, and D as first steps

[Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide: ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment to Section 3.3, “Mitigating incident impact on users,” which lists draining or redirecting traffic, adding capacity, and rollback strategies

</details>

---

### Exam 2 · Q44

You support a service that recently suffered an outage. A new release that exhausted the service’s memory resources caused it, and you successfully rolled the release back to limit the impact on users. You are now responsible for the post-mortem and want to follow Site Reliability Engineering (SRE) practices while developing it. What should you do?

- A. Concentrate on building new features instead of preventing the outage from recurring.
- B. Concentrate on identifying the contributing causes of the incident instead of the individual responsible for it.
- C. Schedule one-on-one meetings with every engineer involved, and establish who approved and pushed the new release to production.
- D. Use the Git history to locate the related code commit, and bar the engineer who made it from working on production services.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Concentrate on identifying the contributing causes of the incident instead of the individual responsible for it.

**Correct Answer**

**B. Concentrate on identifying the contributing causes of the incident instead of the individual responsible for it.**

**Exam Reasoning Explanation**

The impact has already been mitigated by the rollback, so the remaining question is what the post-mortem is for: learning and preventing recurrence. Apply the SRE test to each option by asking what it directs attention toward, systems and processes or individuals. The memory exhaustion reached production because some control failed to catch it, so the useful question is which controls were missing, not which person was involved. Only one option aims the investigation at causes in the system, and the others either drop the prevention goal or hunt for a person.

**Key Exam Clues**

  * “follow Site Reliability Engineering practices when developing the post-mortem” — technical signal: SRE post-mortems are blameless and focus on learning from failure.

  * “new release that exhausted the service memory resources” — technical signal: the defect passed through the release process, so the analysis should examine why existing controls did not catch it.

  * “rolled back the release successfully to mitigate” — context clue: the incident is over, and the remaining work is understanding and preventing recurrence.

**Why This Is Correct**

A blameless post-mortem identifies the contributing causes of an incident without indicting any individual or team for bad or inappropriate behavior. In this case that means asking questions such as why a memory-exhausting change passed testing, why the rollout did not surface the problem before full exposure, and why monitoring did not flag memory pressure sooner. The answers produce systemic action items, such as memory regression tests, resource-limit checks, or longer canary phases, that prevent a similar release from reaching users regardless of who wrote or approved it. Google’s experience is that a truly blameless post-mortem culture produces more reliable systems, partly because people who are not afraid of punishment report problems honestly.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** A post-mortem exists to document what happened and drive actions that reduce the chance or impact of recurrence. Prioritizing new features over that work leaves the underlying gap open, so the same class of outage can return.

  * **Option C — Violates Requirement:** Talking with the engineers involved is a normal way to gather facts, which makes this tempting. But the stated purpose is to establish who approved and pushed the release, which turns the exercise into a search for responsibility and discourages candid accounts.

  * **Option D — Violates Requirement:** Barring the engineer who made the commit is punitive and treats one person as the cause. It teaches others to hide mistakes, and it fixes nothing in the system, so the same change could be made by someone else.

**Exam Trap**

The strongest distractor is Option C, because collecting information from the people involved looks like diligence. The distinction is the objective: reconstructing what happened and why is blameless, while determining who approved and pushed the release is attribution of fault. If the same meetings aimed to rebuild the timeline and the decision context without assigning fault, they would be consistent with SRE practice.

**Foundation Concept**

People respond to incentives, so if reporting a mistake leads to punishment, problems are hidden and the organization stops learning. Blameless post-mortems separate accountability for improving the system from blame for individuals, and they treat human error as a symptom of gaps in tooling, testing, review, or monitoring. A good post-mortem records impact, timeline, contributing causes, and concrete action items that have owners and are tracked to completion.

**Real-World Connection**

After a release exhausts memory and is rolled back, the team writes a post-mortem that lists contributing causes: a leak in a new code path, no soak test, a canary period too short to show growth, and no alert on memory trend. Action items add a memory regression test and a resource-saturation alert and lengthen the canary stage, each with an owner and a due date. The document is shared widely so other teams can learn from it, and engineers continue to report issues honestly.

**Memory Hook**

Ask what failed in the system, not who failed.

**30-Second Exam Takeaway**

For SRE post-mortem questions, pick the blameless answer that analyzes contributing causes and drives systemic fixes. Reject answers that single out, question, or sideline individuals, and answers that skip prevention work.

**Official References**

[Google SRE Book — Postmortem Culture: Learning from Failure: ](https://sre.google/sre-book/postmortem-culture/)Supports: the correct-answer mechanism (blameless post-mortems that focus on contributing causes without indicting individuals or teams) and the elimination of Options C and D

[**Google SRE Workbook — Postmortem Culture: Learning from Failure:**](https://sre.google/workbook/postmortem-culture/) Supports: the link between a blameless post-mortem culture and more reliable systems, and the need for action items that prevent recurrence, which eliminates Option A

</details>

---

### Exam 2 · Q49

A team is defining Service Level Objectives (SLOs) for a high-traffic, multi-region web application whose customers expect the service to be consistently available and fast. Customers are currently satisfied with both availability and performance. Over the trailing 28-day window, measurements show a 90th-percentile latency of 120 ms and a 95th-percentile latency of 275 ms. Which latency SLO should the team publish?

- A. Publish a 90th-percentile latency target of 100 ms and a 95th-percentile latency target of 250 ms.
- B. Publish a 90th-percentile latency target of 120 ms and a 95th-percentile latency target of 275 ms.
- C. Publish a 90th-percentile latency target of 150 ms and a 95th-percentile latency target of 300 ms.
- D. Publish a 90th-percentile latency target of 250 ms and a 95th-percentile latency target of 400 ms.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Publish a 90th-percentile latency target of 150 ms and a 95th-percentile latency target of 300 ms.

**Correct Answer**

**C. Publish a 90th-percentile latency target of 150 ms and a 95th-percentile latency target of 300 ms.**

**Exam Reasoning Explanation**

The must-have constraint is that the published target has to leave room for normal variance — a service that is already running at 120 ms/275 ms cannot publish those exact numbers as its SLO without being perpetually one bad minute away from violating it. The second constraint, equally important, is that “customers are currently happy,” which anchors how much slack is appropriate: the target should stay close enough to today’s real performance that it still reflects what users actually experience, rather than drifting into territory where a real regression could hide behind a technically-met SLO. Evaluate each option against both constraints together, and only the option with a modest, proportionate buffer survives.

**Key Exam Clues**

  * “Customers are currently happy with the application performance and availability” — a signal that the published target should stay close to current measured values, ruling out an excessively loose target.

  * “90th percentile of latency is 120ms and the 95th percentile of latency is 275ms” — the baseline the recommended SLO must be benchmarked against, not copied.

  * “What latency SLO would you recommend to the team to publish” — asks for a target the team will defend going forward, which implies the target needs headroom (an error budget) rather than being a snapshot of current measurement.

**Why This Is Correct**

A target of 150 ms (p90) and 300 ms (p95) sits modestly above the measured 120 ms and 275 ms. That gap is the SLO’s error budget: it absorbs ordinary, expected variance in a high-traffic, multi-region system — traffic spikes, routine releases, minor infrastructure hiccups — without the service falling out of SLO on a routine basis. At the same time, the buffer is small enough that the target still tracks what satisfied customers are actually experiencing today, so a genuine regression (say, p90 latency drifting to 200 ms) would still trip the SLO well before users started noticing a meaningfully worse experience.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** a 100 ms / 250 ms target is tighter than the service’s own currently measured performance (120 ms / 275 ms). The service would already be out of SLO under normal, currently-satisfactory conditions, which makes the target unworkable from day one.

  * **Option B — Incorrect:** this sets the SLO to exactly the currently measured values, leaving zero buffer between achieved performance and the target. Any ordinary fluctuation in a high-traffic system would push the SLI past the SLO, triggering false alarms and unnecessary feature freezes despite customers being happy — this is the specific mistake SRE guidance warns against when it comes to choosing SLO targets.

  * **Option D — Technically Possible but Not Best:** 250 ms / 400 ms is more than double the current p90 and nearly 1.5x the current p95. That much slack would let the service’s real performance degrade substantially — well past the point where “currently happy” customers would stay happy — while still reporting as fully within SLO, defeating the purpose of the SLO as an early-warning signal tied to actual user experience.

**Exam Trap**

The trap in Option B is mistaking precision for rigor: measuring carefully and then publishing exactly what you measured feels disciplined, but it’s the canonical error SRE guidance calls out directly — a target with no buffer isn’t a target, it’s a tripwire. The trap in Option D is overcorrecting in the other direction, assuming “more margin is always safer,” when the stem’s “customers are currently happy” detail is precisely what tells you the margin shouldn’t be that large. The decisive test is always: does this target leave a believable, proportionate buffer over what’s actually being achieved?

**Foundation Concept**

A latency SLO should be set with intentional headroom above currently observed performance — enough to function as a real error budget, but not so much that the target stops reflecting genuine user experience. That buffer is what makes the SLO useful as a decision-making tool: small, expected fluctuations stay within budget, while real regressions still get caught early, and it also gives engineering room to make trade-offs elsewhere (cost, maintainability) that might cost a little latency without breaching the SLO.

**Real-World Connection**

With a 150 ms / 300 ms SLO in place, the team can ship a normal release that nudges p90 latency up a few milliseconds without burning through its error budget or triggering a reliability-first response — but a release or incident that pushes p90 toward 200 ms would still clearly violate the SLO, prompting investigation well before the degradation became severe enough for customers to complain.

**Memory Hook**

A latency SLO should sit a reasonable step above what’s currently measured — never exactly at it, and never so far above it that it stops meaning anything.

**30-Second Exam Takeaway**

When a question gives you current measured percentiles and asks what SLO to publish, eliminate the option that matches those numbers exactly (no error budget) and the option far looser than them (no longer reflects real user experience); the modest-headroom option is almost always correct.

**Official References**

[**Google SRE Book — Service Level Objectives (Choosing Targets):**](https://sre.google/sre-book/service-level-objectives/) Supports: the correct-answer reasoning and the elimination of Option B’s “set the target to current performance” anti-pattern

[**Google SRE Workbook — Implementing SLOs:**](https://sre.google/workbook/implementing-slos/) Supports: practical guidance on setting initial reliability targets and buffers for an error budget

</details>

---

### Exam 2 · Q51

A web application hosted on Compute Engine provides a booking service to thousands of users. Shortly after a new feature is released, the monitoring dashboard shows every user experiencing elevated latency at login. The goal is to limit the impact of this incident on the service’s users. What should be done first?

- A. Roll back the release that was just deployed.
- B. Review the Cloud Monitoring data in more depth.
- C. Increase the size of the virtual machines that run the login service.
- D. Deploy another new release to see whether it resolves the problem.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Roll back the release that was just deployed.

**Correct Answer**

**A. Roll back the release that was just deployed.**

**Exam Reasoning Explanation**

Two things anchor this question: the symptom began shortly after a new release, and the stated goal is to mitigate user impact, not to understand root cause. A tight timing correlation between a deploy and a new, universal symptom is strong evidence the release caused it, and when the likely cause of an incident is a recent change, SRE practice is to restore the last known-good state immediately rather than spend time investigating or risk introducing further change. Rolling back does exactly that: it’s the fastest, lowest-risk way to stop user impact given the evidence already in hand, which is what “what should you do first” is asking for.

**Key Exam Clues**

  * “Shortly after the release of a new feature... all users are experiencing latency” — a strong timing correlation between the deploy and the symptom, pointing to the release as the likely cause.

  * “mitigate the impact of the incident on the users” — the explicit goal is impact reduction, not root-cause diagnosis.

  * “What should you do first?” — a sequencing constraint favoring the fastest, safest corrective action over further investigation or additional risky changes.

**Why This Is Correct**

Rolling back the release immediately restores the application to the state it was in before the latency began, directly addressing the most probable cause without requiring any further diagnosis first. This mitigates the impact on the thousands of affected users as quickly as possible, which is the explicit goal stated in the question — consistent with SRE incident-response priority of restoring service first and investigating root cause afterward, once the system is stable again.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Technically Possible but Not Best:** reviewing monitoring data is a reasonable diagnostic activity, but it doesn’t itself reduce user impact, and the evidence already available — the tight timing correlation with the release — is already strong enough to justify acting. Spending time investigating further before taking the indicated corrective action delays mitigation without a clear need.

  * **Option C — Technically Possible but Not Best:** resizing the VMs assumes the problem is a capacity or resource constraint, but nothing in the scenario points to a load increase — the correlation is specifically with a code release, not traffic growth. Acting on that unverified assumption risks spending time and money without addressing the more probable actual cause.

  * **Option D — Violates Requirement:** deploying another release introduces more unverified change into a system that’s already experiencing an incident, rather than first stabilizing it. This runs directly counter to standard incident practice, which calls for restoring a known-good state before introducing any further changes.

**Exam Trap**

The trap in Option B is that “investigate before acting” sounds like the careful, responsible choice, but the question isn’t asking what’s generally prudent — it’s asking what mitigates user impact first, and the evidence already on hand (the tight timing correlation with a release) is sufficient to justify an immediate rollback. Waiting to confirm what’s already strongly indicated only prolongs the impact the question is asking you to minimize.

**Foundation Concept**

A central tenet of SRE incident management is limiting the disruption of an incident and restoring normal operation as quickly as possible — which is exactly why every rollout is expected to have a well-understood, well-tested rollback mechanism. When a recent change is strongly implicated, rolling it back is the standard fastest path to restoring service; a full root-cause investigation follows afterward, typically through a postmortem, once the immediate user impact has been addressed.

**Real-World Connection**

Rolling back the suspect release the moment users begin experiencing latency right after a deploy stops the impact on thousands of active logins immediately. The team can then investigate what specifically in the new feature caused the regression in a calmer, lower-pressure setting, rather than leaving users degraded while that investigation happens live in production.

**Memory Hook**

When a problem starts right after a release, mitigate first by rolling it back — don’t investigate further or ship more changes before restoring the known-good state.

**30-Second Exam Takeaway**

A strong timing correlation between a deploy and a new symptom, combined with a question asking what to do “first” to mitigate user impact, points to rolling back the suspect change rather than further diagnosis or an additional deployment.

**Official References**

[**Google SRE Book — Chapter 14, Managing Incidents:**](https://sre.google/sre-book/incident-response/) Supports: the core principle that effective incident management limits disruption and restores service as quickly as possible

[**Google Cloud Blog — Adventures in SRE-land: Incident management at Google:**](https://cloud.google.com/blog/products/gcp/incident-management-at-google-adventures-in-sre-land) Supports: rollback as the standard, well-tested mechanism for restoring service once a recent change is implicated in an incident

</details>

---

### Exam 2 · Q53

A team operates a large service governed by a clearly defined Service Level Objective (SLO), and engineers ship new releases of that service several times each week. In the event that a significant incident pushes the service outside its SLO, the goal is for engineering effort to pivot away from feature work and toward restoring reliability. Which action should be taken in advance of any such incident?

- A. Work with every service stakeholder to establish a suitable error budget policy ahead of time.
- B. Negotiate an agreement with the product team that service reliability will always take priority over shipping new features.
- C. Negotiate with the development team to cut the release cadence down to once a week at most.
- D. Introduce a plugin into the Jenkins pipeline that blocks new releases any time the service is outside its SLO.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Work with every service stakeholder to establish a suitable error budget policy ahead of time.

**Correct Answer**

**A. Work with every service stakeholder to establish a suitable error budget policy ahead of time.**

**Exam Reasoning Explanation**

The hard constraint is timing: whatever mechanism makes the reliability-versus-features decision has to be agreed and in place _before_ the incident, so that nobody is negotiating priorities while the service is already broken. The soft constraint is sustainability: the organization still releases multiple times a week under normal conditions, so the mechanism can’t be a permanent brake on velocity — it has to be conditional on an objective trigger. An error budget policy satisfies both: it is written and agreed in advance, and it only forces a reliability-first posture once the budget is actually spent, leaving normal release cadence untouched the rest of the time. Options that either impose a permanent constraint (B, C) or implement only a narrow technical fragment of the policy (D) fail one of these two requirements.

**Key Exam Clues**

  * “deploys new releases of the service multiple times a week” — establishes that high release velocity is the normal, desired state, which rules out any option that permanently throttles releases as the default.

  * “If a major incident causes the service to miss its SLO” — defines an objective, data-driven trigger condition, which is exactly what an error budget policy is built to key off of.

  * “before a major incident occurs” — a hard constraint requiring the mechanism to be pre-agreed rather than negotiated reactively.

**Why This Is Correct**

An error budget policy is a document, agreed in advance by both the team building features and the team(s) accountable for reliability, that spells out exactly what happens as the error budget is consumed — up to and including redirecting engineering effort away from features and onto reliability work once the budget is exhausted. Because it is negotiated and signed off before any incident, it converts what would otherwise be an ad hoc, politically charged argument during a crisis into a pre-agreed, objective consequence that triggers automatically. That directly produces the outcome the scenario asks for: a clean shift in focus from features to reliability precisely when the SLO is missed, and normal behavior the rest of the time.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Violates Requirement:** committing to “always” prioritize reliability over features removes the balancing mechanism SRE is built around. Error budgets exist precisely so that reliability work is prioritized only when the data (budget burn) says it should be, not unconditionally — an absolute rule like this is neither what the scenario needs nor realistic for a product organization to accept.

  * **Option C — Technically Possible but Not Best:** capping release frequency addresses the symptom the question never raised. The stated problem is what happens _after_ a major incident causes an SLO miss, not that releases are currently too frequent; arbitrarily slowing down a healthy, well-functioning release cadence doesn’t target the actual trigger condition and sacrifices velocity even when the service is well within budget.

  * **Option D — Technically Possible but Not Best:** an automated release gate tied to SLO status is a reasonable _implementation detail_ that an error budget policy might eventually include, but introduced on its own it is a unilateral technical control rather than an agreement reached with stakeholders, and it only blocks releases — it does nothing to actually redirect engineering focus onto reliability work, run postmortems, or reallocate sprint capacity, which is the broader shift the scenario is asking for.

**Exam Trap**

The trap options sound protective of reliability but each oversimplifies the SRE balancing act: B swings too far by making reliability win unconditionally, and D swings too narrow by automating only the release-blocking piece without the surrounding stakeholder agreement. The decisive test is whether the option is both collaboratively agreed upon _and_ conditional on an objective trigger — only the error budget policy is both.

**Foundation Concept**

An error budget is the inverse of the SLO (roughly, 1 − SLO) — the quantified amount of unreliability a service is allowed to accumulate over a measurement window. On its own, that number is just a metric; the error budget policy is what gives it consequences, defining in advance what the team does as the budget is spent, including the point at which feature work pauses in favor of reliability work. This is the core SRE mechanism for resolving the structural tension between product development’s incentive to ship and reliability’s incentive to stay within SLO.

**Real-World Connection**

A team that has a signed-off error budget policy going into a major incident can redirect the next sprint’s capacity to reliability fixes immediately and without internal conflict, because the response was already agreed before anyone had a deadline or a launch on the line. Teams that skip this step typically end up re-litigating the reliability-versus-features trade-off incident by incident, which slows the response, breeds inconsistency, and makes recurring SLO misses more likely.

**Memory Hook**

When a question asks what to put in place _before_ an incident to make the reliability-versus-features call automatic, the answer is an error budget policy agreed with stakeholders — not a blanket rule, a fixed release cadence, or a single pipeline gate.

**30-Second Exam Takeaway**

SRE questions about balancing velocity and reliability almost always resolve to establishing an error budget (and its policy) with stakeholders in advance; treat “always prioritize X” absolutes and single-tool technical fixes as the standard distractor pattern.

**Official References**

[**Google SRE Book — Embracing Risk (Motivation for Error Budgets):**](https://sre.google/sre-book/embracing-risk/) Supports: the correct-answer mechanism and the rationale for why reliability work is prioritized conditionally rather than always

[**Google SRE Workbook — Example Error Budget Policy:**](https://sre.google/workbook/error-budget-policy/) Supports: what an error budget policy contains and how it operationalizes the shift from features to reliability work

</details>

---

### Exam 3 · Q11

You are responsible for your company’s main revenue-generating application. Its error budget policy suspends production deployments when the service approaches a breach of its service level objective (SLO). Recent service problems have exhausted the available error budget. A pending release includes a feature urgently needed by your largest customer, and you have been informed that all unit tests have passed. How should you proceed?

- A. Wait for the error budget to be replenished before deploying the feature.
- B. Repeat the unit tests and deploy the feature if they succeed.
- C. Proceed with the feature deployment immediately.
- D. Introduce the feature to a subset of users, then expand the rollout if no errors are reported.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Wait for the error budget to be replenished before deploying the feature.

**Correct Answer**

**A. Wait for the error budget to be replenished before deploying the feature.**

**Exam Reasoning Explanation**

The deployment freeze is the decisive constraint. The service has exhausted its error budget, so the established policy takes precedence over customer urgency and successful testing. Neither repeating tests nor reducing rollout size changes whether this feature release is permitted.

**Key Exam Clues**

  * **“Suspends production deployments” — Hard constraint:** The organization has already defined its response to reliability risk.

  * **“Exhausted the available error budget” — Technical signal:** The service has reached the condition requiring the freeze.

  * **“Feature urgently needed” — Business pressure:** Urgency does not establish an exception to the policy.

  * **“All unit tests have passed” — Supporting evidence:** Testing increases confidence but does not replenish the budget.

**Why This Is Correct**

An error budget policy translates measured reliability into release decisions. When the budget is depleted, postponing feature releases limits additional change risk and creates room for reliability improvements. Google’s guidance freezes changes until sufficient budget becomes available again. 

Google’s example policy permits exceptions for P0 issues and security fixes. The scenario describes a customer feature, with no qualifying exception identified.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Violates Requirement:** Passing the tests again does not lift the deployment freeze. Unit tests also cannot establish that every production interaction will behave correctly; some defects emerge only under real traffic. 

  * **Option C — Violates Requirement:** Immediate deployment disregards the explicit error budget policy. The customer’s importance does not independently authorize bypassing that policy. 

  * **Option D — Violates Requirement:** A canary limits the number of users initially exposed to a change, but it remains a production deployment. It is useful when releases are permitted; it does not override an active freeze. 

**Exam Trap**

A gradual rollout is normally a sound reliability practice, making D tempting. However, rollout safety and release permission are separate decisions. If the error budget had recovered and the freeze were lifted, a monitored canary would be an appropriate deployment strategy.

**Foundation Concept**

An error budget represents the failures permitted by an SLO over its measurement period. Its policy determines how remaining budget affects engineering priorities. Recovery depends on the defined measurement window and release criteria; successful tests do not erase previously observed failures. 

**Real-World Connection**

Keep the tested feature ready while the team addresses the recent reliability problems. Once the policy permits feature releases again, deploy progressively and monitor the result. This protects the application’s existing revenue while preserving the work needed for the customer’s feature.

**Memory Hook**

A safer rollout reduces deployment risk, but it does not lift an error-budget freeze.

**30-Second Exam Takeaway**

An exhausted error budget plus an explicit deployment freeze means postponing feature releases. Customer urgency, passing tests, and canaries do not replace the policy’s release criteria.

**Official References**

  * [**Google SRE Workbook — Example Error Budget Policy**](https://sre.google/workbook/error-budget-policy/)

Supports: Deployment freezes, reliability prioritization, and exceptions for P0 issues or security fixes.

  * [**Google SRE Book — A Collection of Best Practices for Production Services**](https://sre.google/sre-book/service-best-practices/)

Supports: Freezing feature changes when the budget is spent and resuming after budget recovery.

  * [**Google SRE Workbook — Canarying Releases**](https://sre.google/workbook/canarying-releases/)

Supports: Canary risk reduction, production exposure, and limitations of pre-production testing.

</details>

---

### Exam 3 · Q13

You are rolling out a new application version to a Google Kubernetes Engine (GKE) cluster spanning multiple zones. Most of the rollout appears healthy, but some Pods in one zone are showing increased error rates. You need to revert the update only for the affected Pods while minimizing disruption to users. What should you do?

- A. Reduce the number of Pods in the affected zone, then deploy the new application version again.
- B. Drain the affected nodes, then deploy the new application version on the remaining nodes.
- C. Restore the Deployment’s previous Pod template and use a rolling update to replace the Pods in the affected zone.
- D. Run `kubectl rollout undo` for the entire Deployment, then redeploy the new version while excluding the affected zone.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Restore the Deployment’s previous Pod template and use a rolling update to replace the Pods in the affected zone.

**Correct Answer**

**C. Restore the Deployment’s previous Pod template and use a rolling update to replace the Pods in the affected zone.**

However, C requires an unstated prerequisite: **the affected Pods must belong to an independently managed Deployment scoped to that zone**. Changing a Deployment’s template applies to its managed replicas across all zones—not just the zone experiencing errors. 

**Exam Reasoning Explanation**

The decisive requirement is rollback scope. A rolling update controls how Pods are replaced; it does not automatically restrict replacement to a geographic zone. First establish whether the affected zone has a separate Deployment. Without that boundary, C cannot provide the requested selective rollback.

**Key Exam Clues**

  * **“Only for the affected Pods” — Hard constraint:** Healthy portions must remain outside the rollback scope.

  * **“One zone” — Technical signal:** Placement and Deployment ownership must be distinguished.

  * **“Minimizing disruption” — Preference:** Replace affected workloads gradually while preserving sufficient serving capacity.

**Why This Is Correct**

C describes an appropriate rollback mechanism **when the Deployment already manages only the affected zone’s workload**. Restore its previous template and use controlled rolling replacement.

An architecture supporting this can combine separate Deployments with zone-specific node selectors or required node affinity. The conclusion follows from combining independent Deployment management with explicit Pod-placement constraints. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Incorrect:** Scaling down and redeploying the new version does not restore the previous application version. It can reduce capacity without performing the required rollback.

  * **Option B — Different Use Case:** Draining evicts workloads and makes nodes unavailable for new scheduling. It supports node maintenance or evacuation, but does not revert the application version and can affect additional workloads on those nodes. 

  * **Option D — Violates Requirement:** It explicitly rolls back the entire Deployment, including healthy replicas, before introducing another deployment. That exceeds the requested selective scope. Deployment rollback restores the selected Deployment’s previous template. 

**Exam Trap**

**Rolling** describes replacement behavior; it does not mean **zone-selective**. C becomes valid if the question specifies that each zone has its own independently managed Deployment.

**Foundation Concept**

Availability zones determine workload placement. Deployments determine the desired application version for their managed replicas. Selective recovery requires those management boundaries to match the desired recovery scope.

**Real-World Connection**

With separate Deployments for zones A, B, and C, you can restore the previous version only in zone B while preserving the other Deployments. If one Deployment spans all three zones, reverting its template eventually affects its replicas throughout that Deployment.

**Memory Hook**

For native Kubernetes Deployments, rollback scope follows the Deployment boundary.

**30-Second Exam Takeaway**

C is the intended answer only with an independently managed Deployment for the affected zone. A shared Deployment does not gain zone-specific rollback merely by restoring its previous Pod template.

**Official References**

[**Kubernetes — Deployments**](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

Supports: Template-driven rollouts, Deployment-wide reconciliation, rollback behavior, and rolling-update controls.

[**Kubernetes — Assigning Pods to Nodes**](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)

Supports: Node selectors, required node affinity, and zone-based placement constraints.

[**Kubernetes — kubectl drain**](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_drain/)

Supports: Node evacuation, Pod eviction, and why draining is distinct from application rollback.

</details>

---

### Exam 3 · Q17

You manage a critical API deployed on Cloud Run that handles an average of 10,000 requests per minute. Users expect **99.9% availability** and response times of **200 milliseconds or less for at least 95% of requests**.

You need to define service level objectives (SLOs) that reflect these expectations and implement ongoing measurement and monitoring. What should you do?

- A. Configure Cloud Monitoring alerts to trigger when average API latency exceeds 150 milliseconds or the error rate exceeds 0.1%.
- B. Define latency as the only SLO, requiring 99% of requests to complete within 100 milliseconds.
- C. Define an availability SLO of 99% and a latency SLO requiring 90% of requests to complete within 500 milliseconds. Use Cloud Monitoring to measure compliance and alert on violations.
- D. Define availability and latency SLOs using the corresponding service level indicators (SLIs). Use Cloud Monitoring to measure compliance and alert on violations.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Define availability and latency SLOs using the corresponding service level indicators (SLIs). Use Cloud Monitoring to measure compliance and alert on violations.

**Correct Answer**

**D. Define availability and latency SLOs using the corresponding service level indicators (SLIs). Use Cloud Monitoring to measure compliance and alert on violations.**

**Exam Reasoning Explanation**

D connects the user expectations to measurable indicators, explicit objectives, and operational monitoring. An SLO requires an SLI, a target, and a defined compliance period.

**Key Exam Clues**

  * **Availability requirement:** At least 99.9% availability.

  * **Latency requirement:** At least 95% of requests complete within 200 milliseconds.

  * **Operational requirement:** Continuously measure performance and notify the team about problems.

**Why This Is Correct**

Define two request-based SLOs over an agreed compliance period:

  * **Availability:** Successful eligible requests divided by total eligible requests, with a target of **at least 99.9%**.

  * **Latency:** Eligible requests completing within 200 milliseconds divided by total eligible requests, with a target of **at least 95%**. 

Cloud Run automatically supplies request-count and request-latency metrics to Cloud Monitoring. Use suitable metrics to measure the SLIs, track compliance, and configure notification channels with SLO alerting. Burn-rate alerts can warn when the error budget is being consumed too quickly. 

**Why the Other Options Are Not the Best Fit**

  * **A — Technically Possible but Not Best:** These alerts can supplement monitoring, but average latency does not establish whether 95% of requests meet the 200-millisecond threshold. The option also does not explicitly define and measure the requested SLOs. Google’s SRE guidance explains that averages can conceal slow requests. 

  * **B — Violates Requirement:** It omits availability entirely. A stricter latency target does not replace the missing availability objective.

  * **C — Violates Requirement:** Both targets are weaker than required: 99% availability instead of 99.9%, and 90% within 500 milliseconds instead of 95% within 200 milliseconds.

**Exam Trap**

**Average latency and a percentile-based latency requirement are different measurements.** A lower average does not guarantee that the required fraction of requests is fast enough. 

**Foundation Concept**

An **SLI** measures service behavior. An **SLO** sets the acceptable target for that measurement over a specified period. An **alerting policy** determines when the team should respond. 

**Real-World Connection**

Suppose 90% of requests take 50 milliseconds and 10% take 500 milliseconds. Average latency is only **95 milliseconds** , yet just **90%** meet the 200-millisecond threshold—the required latency SLO fails.

**Memory Hook**

Measure successful requests and sufficiently fast requests, then set targets and alerts for both.

**30-Second Exam Takeaway**

Choose **D**. Define separate availability and latency SLIs, apply the required targets over a compliance period, and monitor them with SLO-based alerts.

**Official References**

  * [**Concepts in service monitoring**](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring)  
Supports: Availability and latency SLIs, request-based SLOs, targets, and compliance periods.

  * [**Service Level Objectives — Google SRE**](https://sre.google/sre-book/service-level-objectives/)  
Supports: User-focused objectives and why average latency can conceal poor tail performance.

  * [**Monitor Health and Performance — Cloud Run**](https://docs.cloud.google.com/run/docs/monitoring)  
Supports: Automatic collection of request-count and request-latency metrics.

  * [**Alerting on your burn rate**](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/alerting-on-budget-burn-rate)  
Supports: SLO-based alerting, notification channels, and error-budget burn monitoring.

</details>

---

### Exam 3 · Q19

Your organization is actively developing a new web service and preparing it for production. As the SRE team lead, you **MUST** apply Google-recommended practices throughout productionalization. Which two activities should you prioritize next? **(Choose two.)**

- A. Establish monitoring and alerting for the service.
- B. Begin preparing guidelines for using infrastructure systems.
- C. Collaborate with the product team on the service’s design.
- D. Implement redundant resources within the service environment.
- E. Provide early SRE consultation to review architecture and design decisions in detail.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Establish monitoring and alerting for the service. **|** E. Provide early SRE consultation to review architecture and design decisions in detail.

**Correct Answer**

The supplied answer key selects:

**A. Establish monitoring and alerting for the service.**

**E. Provide early SRE consultation to review architecture and design decisions in detail.**

However, **this pair is not uniquely supported by the wording**. Google’s guidance also directly supports D during active-development productionalization. 

**Exam Reasoning Explanation**

A and E address operational visibility and early identification of architectural risks. Both are recommended practices. However, the scenario specifically identifies active development and productionalization, for which Google also explicitly recommends redundancy. Therefore, the supplied key is plausible, but eliminating D requires additional context. 

**Key Exam Clues**

  * **“Actively developing” — Technical signal:** Identifies the service’s lifecycle stage.

  * **“Preparing it for production” — Required outcome:** Calls for operational readiness work.

  * **“Google-recommended practices” — Hard constraint:** Requires authoritative support for the selected activities.

  * **“Choose two” — Cardinality instruction:** Requires a defensible distinction between the selected pair and the remaining options.

**Why This Is Correct**

  * **A:** Monitoring and alerting provide visibility into service behavior and enable detection of operational problems.

  * **E:** Early consultation identifies architectural risks while design changes are comparatively easier to make. Google’s early-engagement model extends through design and implementation, so this activity remains relevant during development.

These activities complement each other, but their validity does not establish that they are the only appropriate pair. 

**Why the Other Options Are Not the Best Fit**

  * **Option B — Technically Possible but Not Best:** Infrastructure guidelines support consistent engineering decisions. Google associates this activity primarily with architecture and design, making it less directly aligned with the stated productionalization work. 

  * **Option C — Technically Possible but Not Best:** Collaborative design is legitimate SRE work. The stem provides no specific design problem that makes codesign the immediate priority, although it should not be described as an incorrect practice. 

  * **Option D — Best Fit under a phase-specific interpretation:** Google explicitly includes additional resources for redundancy in active-development productionalization. Consequently, D cannot be reliably eliminated, and A/D is another defensible selection. 

**Exam Trap**

Distinguish an intended answer key from a uniquely validated answer. Treating redundancy as unnecessary would introduce an assumption absent from the scenario.

**Foundation Concept**

SRE combines early design influence with operational readiness. Lifecycle phases guide priorities, while consultation, documentation, monitoring, and resilience work can overlap.

**Real-World Connection**

An SRE team could review architectural failure modes, establish actionable alerts, and validate redundant capacity before launch. Actual priorities depend on existing controls, reliability objectives, and identified risks.

**Memory Hook**

Production readiness combines operational visibility, resilience, and early reliability review.

**30-Second Exam Takeaway**

**A/E is the supplied key, while A/D has direct lifecycle-specific support.** This item needs clarification before it can be published as a uniquely graded two-answer question.

**Official References**

  * [**Google SRE Workbook — SRE Engagement Model:**](https://sre.google/workbook/engagement-model/)

Supports: Monitoring, alerting, and redundancy during active development; infrastructure guidance during architecture and design.

  * [**Google SRE Book — The Evolving SRE Engagement Model:**](https://sre.google/sre-book/evolving-sre-engagement-model/)

Supports: Early consultation, collaborative design, and SRE participation during implementation.

  * [**Google Cloud — Professional Cloud DevOps Engineer Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)

Supports: Objective 3.2, managing the service lifecycle.

</details>

---

### Exam 3 · Q29

You manage the reliability of an internally developed, distributed file-storage service that processes thousands of uploads and downloads each day. You need to select a service level indicator (SLI) and use it to support alerts for potential service problems. Which metric best represents the reliability experienced when using the service?

- A. Mean response time of API operations such as `get`, `put`, and `list`.
- B. Count of successfully completed file uploads and downloads per minute.
- C. Mean size of the objects stored by the service.
- D. Number of successful API calls divided by the total number of attempted API calls.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Number of successful API calls divided by the total number of attempted API calls.

**Correct Answer**

**D. Number of successful API calls divided by the total number of attempted API calls.**

**Exam Reasoning Explanation**

The indicator should show whether users can successfully perform operations. A success ratio directly measures that outcome while accounting for changing request volume. Latency measures responsiveness, successful-operation counts measure throughput, and object size describes the workload. D therefore provides the strongest measure of operational availability.

**Key Exam Clues**

  * **“Uploads and downloads” — Technical signal:** Reliability should reflect whether requested operations succeed.

  * **“Thousands … each day” — Technical signal:** Request outcomes provide a useful population of measurable events.

  * **“Reliability experienced when using the service” — Hard constraint:** Prefer a user-outcome measure over workload characteristics.

  * **“Support alerts” — Technical signal:** The indicator should support comparison against a defined reliability objective.

**Why This Is Correct**

Google’s SRE guidance recommends expressing SLIs as good events divided by total events. For request-driven availability:

\\[ \text{Availability SLI} = \frac{\text{Successful API calls}}{\text{Total attempted API calls}} \\]

Both counts must cover the same measurement period and request population. The result is dimensionless and can be expressed as a percentage. For example, \\(9{,}990/10{,}000 \times 100 = 99.9\%\\). 

For implementation, explicitly define eligible requests and successful completion so that the measurement reflects the service contract. Google commonly defines request-based availability using well-formed requests that succeed. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** Latency is a valid SLI for responsiveness, but it does not directly measure successful completion. Requests can fail quickly while average latency remains low. Averages can also conceal slow requests in the distribution’s tail.

  * **Option B — Different Use Case:** Successful operations per minute measures throughput. Without total attempts, it cannot distinguish reduced demand from increased failures or reveal the fraction of users whose operations fail.

  * **Option C — Different Use Case:** Average object size helps characterize storage workloads and capacity needs. It does not indicate whether uploads or downloads complete successfully.

**Exam Trap**

A large number of successful operations can coexist with many failures. The denominator reveals the fraction of attempted work that succeeds. If the requirement instead asked for successful processing volume per minute, B would be appropriate.

**Foundation Concept**

An SLI measures observed service behavior; an SLO sets the target for that behavior. Success ratio measures availability, while latency and durability capture additional aspects of storage reliability. One indicator does not fully describe every user expectation.

**Real-World Connection**

Instrument attempted and successful operations, then define an availability SLO using their ratio. Configure error-budget burn-rate alerts to notify the team when failures threaten that objective. This ties alerts to reliability impact rather than ordinary changes in traffic volume. 

**Memory Hook**

To measure whether operations work, divide successful attempts by total attempts.

**30-Second Exam Takeaway**

For request-based availability, look for a success ratio with a meaningful denominator. Counts describe volume, latency describes speed, and neither alone establishes the proportion of successful operations.

**Official References**

  * [**Google SRE Workbook — Implementing SLOs:**](https://sre.google/workbook/implementing-slos/)

Supports: Good-event ratios, request-based availability, and the relationship between SLIs and SLOs.

  * [**Google SRE Book — Service Level Objectives:**](https://sre.google/sre-book/service-level-objectives/)

Supports: Availability, latency, throughput, durability, and the limitations of averages.

  * [**Google Cloud Observability — Alerting on your burn rate:**](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/alerting-on-budget-burn-rate)

Supports: Using SLO-based error-budget alerts to detect reliability risks.

  * [**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)

Supports: Objective 3.1, covering the definition of SLIs, SLOs, and error budgets.

</details>

---

### Exam 3 · Q42

Your team manages a critical service with a 99.9% availability SLO. The quarterly error budget has nearly run out because of several recent incidents. Your team has a new set of features planned for release next week. You need to avoid exceeding the error budget while following Google-recommended practice. What should you do?

- A. Go ahead with the release, but put an automatic rollback in place in case new errors show up.
- B. Release the features in stages, rolling out to one subset of users at a time to limit the potential impact on the SLO.
- C. Postpone the release and have the team focus on reliability improvements until the error budget replenishes.
- D. Postpone the release and have the team spend the time building up a backlog of features to deploy once the error budget replenishes.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Postpone the release and have the team focus on reliability improvements until the error budget replenishes.

**Correct Answer**

**C. Postpone the release and have the team focus on reliability improvements until the error budget replenishes.**

**Exam Reasoning Explanation**

The error budget exists specifically to govern this trade-off: it’s the amount of unreliability the service can absorb while still meeting its SLO, and it’s meant to be spent deliberately on things like feature launches when it’s healthy. With the budget nearly exhausted, any further risk-bearing change — even a carefully staged one — threatens to push the service out of SLO. Google’s own SRE guidance treats this situation as a trigger for a feature freeze specifically so that engineering effort shifts to reliability work, which is the only one of the four options that both avoids further budget risk and redirects effort toward actually fixing the underlying problem rather than just sitting on hands or stockpiling unrelated work.

**Key Exam Clues**

  * **“error budget for the quarter has been nearly depleted”** — a decisive constraint clue: there is very little room left to absorb any additional errors, which argues against any option that still introduces new risk.

  * **“due to several incidents”** — signals that the service has an active reliability problem, which is the condition Google’s error budget policy explicitly treats as a reason to pause feature work and fix the underlying issues.

  * **“planning on releasing new features next week”** — frames the choice as whether to proceed, in some form, with new risk-bearing change right now.

  * **“following Google-recommended practices”** — points directly at the documented SRE error-budget policy response (a feature freeze focused on reliability), rather than at ad hoc risk-mitigation tactics.

**Why This Is Correct**

Google’s SRE practice treats an exhausted or near-exhausted error budget as the signal to impose a freeze on new feature releases, specifically so that the team can redirect its attention to reliability improvements until the budget is replenished. Postponing the release removes the immediate source of additional risk, and spending that time on reliability work (fixing root causes, improving testing, hardening the release process) is what actually restores headroom in the budget and reduces the odds of repeating the recent incidents, rather than just waiting out the clock or doing unrelated work.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** An automatic rollback limits how long a bad release stays live, but it doesn’t prevent the release from consuming more of an already nearly-exhausted budget before the rollback triggers. Proceeding with a risk-bearing release at all runs directly counter to the recommended response to a strained budget.

  * **Option B — Technically Possible but Not Best:** Staged, subset-based rollout is a reasonable general technique for limiting blast radius, and it reduces risk relative to a full release. But it still introduces new change and new risk onto a service whose budget is nearly gone; Google’s documented guidance for this situation is a full pause on feature releases, not merely a more cautious version of the same release.

  * **Option D — Different Use Case:** This option correctly postpones the risky release, but it spends the freed time on building a feature backlog rather than on reliability work. That addresses a different goal (being ready to ship more features later) and does nothing to reduce the chance of repeating the incidents that burned the budget in the first place — which is the specific purpose Google’s guidance assigns to this kind of pause.

**Exam Trap**

The trap is treating “postpone the release” as the whole answer and picking whichever postponement option is listed, without checking what the team is supposed to do with the freed time. Google’s guidance is explicit that a freeze is meant to create space for reliability work specifically, not simply to delay the release or redirect effort toward unrelated feature planning.

**Foundation Concept**

An error budget converts “how reliable should this service be” into a concrete, spendable quantity, which lets a team make principled trade-offs between shipping new risk-bearing changes and investing in stability. When the budget is nearly spent, the policy response isn’t just “be more careful” — it’s a deliberate, temporary rebalancing of where engineering effort goes, specifically toward the reliability work that restores the budget.

**Real-World Connection**

A team that keeps shipping features, even cautiously, while its error budget is nearly gone tends to keep having the same category of incident recur, because nothing is actually being invested in root-cause fixes or hardening. A team that treats budget depletion as an explicit freeze trigger and spends that time on reliability work typically breaks the cycle and arrives at the next compliance period with both a healthier budget and a more resilient service.

**Memory Hook**

Budget nearly gone → freeze features, spend the time on reliability — not on a safer release and not on a bigger feature backlog.

**30-Second Exam Takeaway**

When an error-budget question asks what to do about an upcoming release while the budget is nearly or fully depleted, the Google-recommended answer is almost always to pause the release and redirect the team to reliability work until the budget refreshes — any option that still ships something, however carefully, or that spends the pause on non-reliability work, is the weaker distractor.

**Official References**

[**Google SRE Workbook — Example Error Budget Policy (Appendix B):**](https://sre.google/workbook/error-budget-policy/) Supports: the correct-answer mechanism (freezing feature releases and dedicating the team to reliability work when the error budget is overspent)

[**Google Cloud Blog — Good housekeeping for error budgets (CRE life lessons)**](https://cloud.google.com/blog/products/devops-sre/good-housekeeping-error-budgetscre-life-lessons)**:** Supports: the canonical response to overspending an error budget being a feature freeze aimed specifically at reliability work, used to eliminate option D’s “build a feature backlog” framing

</details>

---

### Exam 3 · Q56

A new version of your Cloud Run application is being introduced through a canary rollout. An SRE colleague reports that the application is now breaching a service level objective (SLO). Your immediate priority is to restore healthy service as quickly as possible. Which action should you take **FIRST**?

- A. Update the traffic allocation so that the latest revision receives 100% of requests.
- B. Update the traffic allocation so that the previous revision receives 100% of requests.
- C. Deploy a new revision from the application’s last known good version.
- D. Investigate the source of the latency using Cloud Trace.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Update the traffic allocation so that the previous revision receives 100% of requests.

**Correct Answer**

**B. Update the traffic allocation so that the previous revision receives 100% of requests.**

**Exam Reasoning Explanation**

The immediate requirement is service recovery. The recent rollout provides a plausible mitigation target, and traffic reassignment offers a direct way to reverse exposure to that change. Prioritize restoring the previous serving revision over deploying another revision or completing a root-cause investigation. Google’s SRE guidance prioritizes mitigating user impact before investigating the underlying cause. 

**Key Exam Clues**

  * **“Canary rollout” — Technical signal:** Traffic is being introduced to a candidate revision while an earlier revision remains available.

  * **“Breaching a service level objective” — Technical signal:** Reliability has degraded sufficiently to require intervention.

  * **“Restore healthy service as quickly as possible” — Hard constraint:** Favor the shortest available recovery path.

  * **“FIRST” — Sequence instruction:** Choose immediate mitigation before subsequent diagnosis and remediation.

**Why This Is Correct**

Cloud Run supports rolling back by assigning 100% of service traffic to an existing previous revision. Changing traffic allocation does not require deploying the application again.

This answer assumes the previous revision remains a healthy, compatible rollback target. Traffic changes are not instantaneous, and in-flight requests can continue during the transition, so confirm recovery after changing the allocation. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** This completes the rollout to the revision associated with the emerging reliability problem, potentially increasing user impact. It would suit promoting a successfully validated canary rather than responding to the reported degradation.

  * **Option C — Technically Possible but Not Best:** Redeploying a known good application version can restore service, but it introduces another deployment when the existing previous revision can receive traffic directly. The additional deployment work delays the available mitigation. 

  * **Option D — Technically Possible but Not Best:** Cloud Trace helps investigate request latency and performance bottlenecks. However, investigation alone does not redirect traffic or restore service. It is appropriate for diagnosing the problem after mitigation, or in parallel without delaying recovery.

**Exam Trap**

Identifying the exact defect can feel like the necessary first step, but a safe rollback can reduce impact before that investigation finishes. If no usable previous revision remained available, deploying a new revision from the known good application version—option C—could become necessary.

**Foundation Concept**

Canary deployment limits exposure while evaluating a candidate release. Retaining the established baseline makes reversal practical; determining why the candidate failed is a separate task from restoring acceptable service.

**Real-World Connection**

After redirecting traffic, monitor current error rates and latency to confirm that user experience improves. Preserve the unsuccessful revision’s logs and traces for investigation. This approach reduces recovery time while retaining evidence needed to prevent recurrence.

**Memory Hook**

When a canary degrades service, restore traffic to the healthy baseline before pursuing detailed diagnosis.

**30-Second Exam Takeaway**

For **FIRST** -action questions during a rollout incident, look for an available mitigation that reduces user impact with minimal additional change. Prefer traffic rollback to an existing healthy revision over redeployment or extended troubleshooting.

**Official References**

  * [**Google Cloud Run — Rollbacks, gradual rollouts, and traffic migration:**](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration)

Supports: Routing all traffic to a previous revision, changing allocation without redeployment, and transition behavior.

  * [**Google SRE Workbook — Incident Response:**](https://sre.google/workbook/incident-response/)

Supports: Prioritizing mitigation before root-cause analysis and using rollback to reduce incident impact.

  * [**Google Cloud — Cloud Trace overview:**](https://docs.cloud.google.com/trace/docs/overview)

Supports: Cloud Trace’s role in latency analysis and performance troubleshooting.

</details>

---

### Exam 4 · Q1

Cloud Monitoring alerts you to potentially malicious activity on a node in your Google Kubernetes Engine (GKE) cluster. A container running on that node might be compromised.

You need to isolate the affected node while investigating the incident and minimize disruption to applications running in the cluster. What should you do?

- A. Taint the suspicious node to prevent Pods that previously interacted with it from being scheduled on other cluster nodes.
- B. Scale the Deployment associated with the suspected container to zero replicas.
- C. Restart the node to interrupt the malicious activity and force its Pods to be recreated on other nodes.
- D. Cordon the node to prevent new Pod scheduling, then drain it gracefully so controller-managed workloads can be recreated on other nodes.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Cordon the node to prevent new Pod scheduling, then drain it gracefully so controller-managed workloads can be recreated on other nodes.

**Correct Answer**

**D. Cordon the node to prevent new Pod scheduling, then drain it gracefully so controller-managed workloads can be recreated on other nodes.**

**Exam Reasoning Explanation**

D provides controlled evacuation of the affected node while preventing normal scheduling onto it. It is the best available option, although complete incident containment also requires network restrictions. 

**Key Exam Clues**

  * **Security signal:** A container might be compromised.

  * **Containment requirement:** Isolate the affected node during investigation.

  * **Availability preference:** Minimize disruption to other workloads.

**Why This Is Correct**

Cordoning marks the node as unschedulable. Draining gracefully evicts eligible Pods, allowing their controllers to create replacements elsewhere. Normal eviction respects PodDisruptionBudgets, helping limit simultaneous application disruption. 

Successful evacuation depends on suitable workload controllers, healthy replicas, and sufficient capacity on other nodes. It does not guarantee zero downtime.

**Why the Other Options Are Not the Best Fit**

  * **A — Incorrect:** Taints affect scheduling or eviction on the tainted node. They do not track which Pods interacted with it or automatically prevent those Pods from running elsewhere. 

  * **B — Violates Requirement:** Scaling to zero removes every replica of that Deployment, potentially taking the application offline. It also leaves the suspicious node available to other workloads.

  * **C — Incorrect:** Restarting does not establish scheduling or network quarantine. It also does not guarantee that replacement Pods run on different nodes or that the underlying compromise is resolved. 

**Exam Trap**

**Cordon and drain are not complete security isolation.** Google’s incident-response guidance recommends retaining the suspected Pod for investigation, draining the other workloads, and restricting network access to the node’s VM. Do not blindly redeploy the suspected workload elsewhere. 

**Foundation Concept**

These controls serve different purposes:

  * **Cordon:** Prevent normal scheduling onto the node.

  * **Drain:** Gracefully evacuate eligible workloads.

  * **Network quarantine:** Restrict communication involving the suspected node.

**Real-World Connection**

Google documents this selective evacuation pattern:
    
          1. kubectl cordon NODE_NAME
      2. kubectl label pod SUSPECT_POD -n APP_NAMESPACE quarantine=true
      3. kubectl drain NODE_NAME --pod-selector='!quarantine' --ignore-daemonsets

This excludes the quarantined Pod from evacuation. DaemonSet Pods remain, and node-level network restrictions must be configured separately. 

**Memory Hook**

Cordon stops arrivals, drain evacuates workloads, and network controls restrict communication.

**30-Second Exam Takeaway**

Choose **D** for controlled node evacuation with minimal disruption. During an actual compromise investigation, add network quarantine and preserve the suspected workload appropriately.

**Official References**

  * [**Mitigate security incidents — GKE**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/security-mitigations)  
Supports: Selective draining, suspected-Pod quarantine, network restrictions, and incident-response tradeoffs.

  * [**kubectl drain**](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_drain/)  
Supports: Unschedulable nodes, graceful eviction, workload-controller requirements, and DaemonSet exclusions.

  * [**Taints and Tolerations**](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)  
Supports: What node taints control and why option A misrepresents their behavior.

  * [**Disruptions**](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)  
Supports: PodDisruptionBudgets and maintaining availability during voluntary disruptions.

</details>

---

### Exam 4 · Q11

You are defining service level objectives for a high-traffic web application whose customers are currently satisfied with its performance and availability. Over a trailing 28-day measurement window, the application’s 90th-percentile latency is 160 ms and its 95th-percentile latency is 300 ms. Which latency SLO should you publish?

- A. A 90th-percentile latency SLO of 150 ms, paired with a 95th-percentile latency SLO of 290 ms.
- B. A 90th-percentile latency SLO of 160 ms, paired with a 95th-percentile latency SLO of 300 ms.
- C. A 90th-percentile latency SLO of 190 ms, paired with a 95th-percentile latency SLO of 330 ms.
- D. A 90th-percentile latency SLO of 300 ms, paired with a 95th-percentile latency SLO of 450 ms.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. A 90th-percentile latency SLO of 190 ms, paired with a 95th-percentile latency SLO of 330 ms.

**Correct Answer**

**C. A 90th-percentile latency SLO of 190 ms, paired with a 95th-percentile latency SLO of 330 ms.**

**Exam Reasoning Explanation**

The SLO must be achievable — not tighter than what the service already delivers — so the team isn’t immediately out of compliance. It should also stay close enough to what users already experience happily that it remains a meaningful signal rather than a number so loose it lets real degradation go unnoticed. Option A sets targets below current measured performance, which the service hasn’t demonstrated it can meet. Option B matches current performance exactly, leaving zero error budget — any ordinary variance breaches it immediately. Option D loosens the targets so far that the published 90th-percentile figure nearly matches today’s 95th-percentile figure, no longer reflecting real user experience. Option C loosens both figures by a modest, deliberate margin, preserving a workable error budget while staying anchored to today’s actual performance.

**Key Exam Clues**

  * “Customers are currently happy with the application performance” — signals current measured performance is the right anchor point; the published SLO shouldn’t diverge sharply from it in either direction

  * “90th percentile of latency is 160 ms and the 95th percentile of latency is 300 ms” — the baseline both figures in a correct option must sit at or modestly above, eliminating anything below these values

  * “over a 28-day window” — a sustained measurement, not a single data point, making it a credible basis for the target rather than something needing heavy discounting

  * Two coupled thresholds — a correct answer must get both the 90th- and 95th-percentile figures right simultaneously, not just one

**Why This Is Correct**

Publishing an SLO at or below current measured performance leaves no room for ordinary variance in traffic, infrastructure, or dependencies — any normal fluctuation would immediately put the service out of SLO and exhaust the error budget before a genuine problem even occurs. Setting the target a modest amount looser than current performance, as this option does, creates a workable error budget while staying close enough to today’s experience that a real regression will still breach the SLO and trigger a response. This balances defensibility with meaningfulness in a way none of the other options do.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement:** Both figures (150 ms and 290 ms) are tighter than what the service currently delivers (160 ms and 300 ms). Publishing an SLO the service doesn’t already meet puts it out of compliance immediately, with no realistic path to meeting it without first improving the system — contradicting the premise that customers are already happy with current performance.

**Option B — Technically Possible but Not Best:** Matching the SLO exactly to current measured performance looks appealing because the service meets it by construction, but it leaves zero error budget. Any small fluctuation in traffic or dependency behavior pushes the service out of SLO, making the target brittle and difficult to defend operationally.

**Option D — Violates Requirement:** Loosening the targets this far (300 ms and 450 ms) means the published SLO no longer reflects the experience customers are actually happy with — the 90th-percentile target alone is nearly double today’s measured value. A target this loose would let a genuine, user-impacting regression occur without ever breaching the SLO, defeating its purpose as an early warning signal.

**Exam Trap**

The trap is reading “base the SLO on current measurement” as “set the SLO equal to current measurement” (Option B), rather than using the measurement as a starting anchor with deliberate headroom built in. The opposite trap is assuming more headroom is always safer, which makes Option D look reasonable — but excessive headroom turns the SLO into a number that no longer represents genuine user happiness, since real degradations could occur well within the published target. The correct answer sits between these two failure modes; further tightening or loosening comes later, from comparing the SLO against actual user-satisfaction signals, not from guessing a wide margin upfront.

**Foundation Concept**

A sound starting SLO is typically derived from a recent, sustained measurement window and then loosened by a modest, deliberate margin rather than published as an exact match to that measurement. This creates an error budget — the gap between “always meets target” and the published objective — that absorbs ordinary variance and gives engineering teams room to make changes without immediately breaching the SLO, while staying close enough to actual performance to remain a meaningful signal of user happiness. The target is refined further over time by comparing it against real indicators of user satisfaction, such as support tickets or sentiment data.

**Real-World Connection**

A team publishing its first formal SLO for a service users already like takes the current 28-day latency percentiles as a baseline, adds a modest buffer, and publishes that as the objective rather than the raw measured numbers. This gives the on-call team a genuine error budget to absorb routine fluctuations from deploys, traffic spikes, or dependency hiccups without constant SLO-violation alerts, while keeping the target tight enough that a real regression — say, a bad release pushing 90th-percentile latency to 250 ms — still breaches the SLO and triggers the team’s error budget policy.

**Memory Hook**

Anchor the SLO to current measured performance, then loosen it by a modest margin — never match it exactly (zero error budget) and never loosen it so far that it stops reflecting real user experience.

**30-Second Exam Takeaway**

When a question gives current measured performance and asks what SLO to publish, rule out anything tighter than the measurement, rule out an exact match (zero error budget), and rule out an excessively loose target that would stop representing real user experience — the right answer sits a modest, deliberate margin above what’s already being delivered.

**Official References**

[**Google SRE Workbook — Chapter 2: Implementing SLOs:**](https://sre.google/workbook/implementing-slos/) Supports: the methodology of deriving a starting SLO from a recent measurement window and loosening it by a modest margin rather than publishing the exact measured value, illustrated by the book’s own worked example (90th-percentile latency measured at 432 ms, published SLO of 450 ms)

</details>

---

### Exam 4 · Q15

You recently migrated an ecommerce application onto Google Cloud, and you now need to get it ready for the approaching peak shopping season. You want to follow Google-recommended practices for this preparation. What is the first thing you should do to get ready for the high-traffic period?

- A. Re-platform the application onto Cloud Run and rely on its built-in autoscaling.
- B. Write a Terraform configuration for the application’s infrastructure so you can quickly stand it up in additional regions.
- C. Run load tests against the application to profile how it performs and scales.
- D. Pre-provision the same amount of additional compute capacity used during last year’s peak season, on the assumption that this year’s growth will be similar.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Run load tests against the application to profile how it performs and scales.

**Correct Answer**

**C. Run load tests against the application to profile how it performs and scales.**

**Exam Reasoning Explanation**

The “first” step must be the one that generates the data every other decision depends on. Options A, B, and D each commit to a specific architectural or capacity decision — re-platforming to Cloud Run, building multi-region deployment automation, or copying last season’s provisioning numbers — without first knowing how the newly migrated application actually performs or where it breaks under load. Google’s own peak-event preparation guidance places load testing early in the preparation phase, months ahead of the event, precisely because it reveals the bottlenecks and scaling behavior that then inform every subsequent architecture and capacity decision. Only load testing produces that foundational data, making it the correct first action; the other three are plausible later steps that are premature without it.

**Key Exam Clues**

  * “recently migrated” — the application’s behavior on Google Cloud is unproven, so prior performance data (and, by extension, last season’s provisioning figures) can’t be trusted to transfer directly

  * “what should you do first” — signals a sequencing question where several options could eventually be reasonable, but only one belongs at the very start

  * “follow Google-recommended practices” — points to Google’s own documented peak-event methodology, which places load testing in the preparation phase ahead of architecture changes

  * “prepare for the upcoming peak traffic season” — a known, anticipated event, which Google’s guidance treats as something to test for well in advance rather than react to

**Why This Is Correct**

Load testing reveals how the newly migrated application actually behaves under increasing demand — where it bottlenecks, how its components scale, and what capacity it genuinely needs — using real data from the current Google Cloud deployment rather than assumptions carried over from before the migration. That data is the necessary input for every subsequent decision: whether to re-platform a component, how many regions to deploy to, or how much capacity to provision. Doing it first, well ahead of the peak season, is also explicitly how Google’s own peak-event preparation guidance sequences this work.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** Moving to Cloud Run and relying on autoscaling can be a reasonable architectural choice, but committing to it before understanding the application’s current bottlenecks and scaling behavior is premature — you don’t yet know whether the application’s architecture even suits Cloud Run’s execution model, or where its real constraints lie.

**Option B — Technically Possible but Not Best:** Automating infrastructure deployment to additional regions is valuable, but it assumes multi-region expansion is the right response to peak load without first confirming that regional capacity, rather than some other bottleneck entirely, is actually what limits the application under load.

**Option D — Violates Requirement:** Pre-provisioning based on last season’s compute usage assumes the application’s resource needs on its new Google Cloud infrastructure mirror its needs on whatever platform it ran on before migration, and assumes a growth figure without any current data to support it. This is guesswork rather than the data-driven approach Google recommends, and it skips the step that would reveal whether last season’s numbers are even relevant anymore.

**Exam Trap**

The trap is picking an option that sounds like solid peak-season preparation — more autoscaling, more automation, more pre-provisioned capacity — without noticing that each one presupposes knowledge the team doesn’t have yet, since the application was only just migrated. The “first” in the question is the tell: it’s asking which action produces the information the other actions would need to be well-informed, not which action sounds the most proactive in isolation.

**Foundation Concept**

Capacity planning and architectural decisions for a known, high-stakes event should be grounded in current, measured performance data rather than assumptions carried over from a previous environment or a previous season. Load testing supplies that data by simulating expected (and above-expected) traffic against the actual production environment, surfacing bottlenecks and scaling limits before they become customer-facing incidents, and giving every later decision — scaling strategy, regional footprint, provisioned capacity — a factual basis instead of a guess.

**Real-World Connection**

A retailer that just migrated its storefront to Google Cloud runs load tests simulating its expected Black Friday traffic months in advance, discovering that a particular database connection pool, not raw compute capacity, is the actual bottleneck at scale. That finding changes their entire preparation plan — instead of blindly provisioning more VMs or committing to a platform migration, they fix the specific constraint the test revealed, then validate the fix with another round of testing before the season arrives.

**Memory Hook**

Just migrated, peak season coming → load test first; everything else (autoscaling platform, multi-region automation, pre-provisioning) is a decision that load-test data should inform, not precede.

**30-Second Exam Takeaway**

When a scenario asks what to do “first” to prepare a recently migrated or newly deployed application for a known high-traffic event, look for the option that generates performance data — load testing — rather than one that commits to a specific architecture or capacity decision before that data exists.

**Official References**

[**Google Cloud — Prepare for a peak capacity event:**](https://docs.cloud.google.com/support/docs/checklists/plan-peak-capacity-event) Supports: load testing and capacity planning as part of the documented preparation phase for a known high-traffic event, ahead of architecture or capacity commitments

[**Google Cloud — Conduct load testing:**](https://docs.cloud.google.com/support/docs/peak-events/conduct-load-testing) Supports: load testing as an early step (recommended three to five months before the event) that determines whether the system will scale successfully and surfaces bottlenecks before other preparation decisions are made

</details>

---

### Exam 4 · Q19

Your company is planning a major marketing event for an online retail site during the holiday shopping season, and you expect the web application to receive a large volume of traffic in a short window. You need to prepare the application for potential failures during the event. What should you do? (Choose two.)

- A. Set up Anthos Service Mesh on the application so you can spot issues on its topology map.
- B. Confirm that the relevant system metrics are being collected in Cloud Monitoring, and configure alerts at thresholds that matter to you.
- C. Review your expected increase in capacity requirements and plan out the quota management you’ll need to support it.
- D. Track your services’ latency using an average percentile latency measurement.
- E. Configure Cloud Monitoring alerts for every common failure your application experiences.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Confirm that the relevant system metrics are being collected in Cloud Monitoring, and configure alerts at thresholds that matter to you. **|** C. Review your expected increase in capacity requirements and plan out the quota management you’ll need to support it.

**Correct Answer**

**B. Confirm that the relevant system metrics are being collected in Cloud Monitoring, and configure alerts at thresholds that matter to you.**

**C. Review your expected increase in capacity requirements and plan out the quota management you’ll need to support it.**

**Exam Reasoning Explanation**

Preparing for a known, high-stakes traffic event has two independent needs: having enough capacity to absorb the expected load, and having the visibility to detect and respond when something does go wrong. C directly addresses capacity — without reviewing increased needs and planning quota management in advance, the application can be throttled or fail outright no matter how well it’s monitored. B directly addresses observability — meaningful, well-tuned alerts on relevant metrics let the team detect and react to real problems during the event. Option A proposes deploying new infrastructure tooling shortly before a high-stakes event, adding risk rather than readiness. Options D and E each sound like reasonable monitoring practices but describe flawed implementations: averaged latency hides the tail-latency problems that actually hurt users, and alerting on every common failure produces noise rather than actionable signal. B and C work independently — one is a capacity action, the other an observability action — and together they form a complete readiness picture: enough capacity, plus the ability to detect trouble if capacity or anything else still goes wrong.

**Key Exam Clues**

  * “prepare your application for potential failures during the event” — frames this as readiness with two distinct angles: having enough capacity, and being able to detect problems

  * “large volume of traffic in a short period” — signals a capacity/quota concern specifically, since everyday quotas may not cover a sudden spike

  * “alerts at levels of interest” (B) versus “all common failures” (E) — a deliberate contrast between targeted, meaningful alerting and indiscriminate alerting

  * “average percentile latency” (D) — an internally inconsistent phrase signaling a flawed metric choice, since averages and percentiles summarize a distribution in different, non-interchangeable ways

**Why This Is Correct**

Reviewing increased capacity requirements and planning quota management (C) ensures the application has enough underlying resource headroom to actually handle the expected spike — without it, the event could fail regardless of monitoring quality, since requests could be throttled or rejected at the infrastructure or API level. Ensuring relevant metrics are captured with alerts set at meaningful thresholds (B) ensures that if something does go wrong, the team finds out quickly enough to respond rather than discovering it through customer complaints. Together these cover both halves of event readiness — sufficient capacity, and the ability to detect trouble when it happens — and neither one substitutes for the other, which is why both are needed and the set is complete at two.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** Service mesh topology visibility can eventually be useful, but introducing new infrastructure tooling into the application shortly before a known high-stakes event adds operational risk and complexity precisely when stability matters most, rather than directly strengthening readiness for the event itself.

**Option D — Violates Requirement:** Monitoring latency as an “average” obscures the tail latency that actually affects user experience — a service with a low average but a long tail of slow requests can still be delivering a poor experience to a meaningful share of users. SRE practice favors percentile-based latency metrics specifically because they surface this tail behavior that averages hide.

**Option E — Violates Requirement:** Alerting on every common failure generates a high volume of low-value notifications, many of which may be routine or self-correcting. This creates alert fatigue, making it harder, not easier, for the on-call team to notice and act on the alerts that actually matter during a high-traffic event.

**Exam Trap**

The trap is picking any option containing “monitor” or “alert” without checking whether it describes monitoring and alerting done well. D sounds like good observability practice but names an inferior metric; E sounds like proactive readiness but describes a noisy, unfocused alerting strategy. The correct pair requires recognizing that readiness for a known traffic spike needs both adequate capacity and well-targeted detection — not just “more monitoring” or “more infrastructure” in any form.

**Foundation Concept**

Preparing a service for a known period of elevated demand has two largely independent prerequisites: confirming the underlying infrastructure and quotas can absorb the expected load, and ensuring the team has the observability to detect and respond to problems that do occur. Within observability itself, implementation quality matters — percentile-based metrics over averages, and targeted alerts over blanket ones, are what make monitoring actually useful during an incident rather than just noisy or misleading.

**Real-World Connection**

An online retailer preparing for a major holiday sale reviews its expected traffic increase, requests the necessary quota increases for compute, networking, and API calls well ahead of the event, and separately tunes its Cloud Monitoring dashboards to alert on signals like p99 latency and error rate crossing meaningful thresholds — rather than paging engineers for every minor, self-resolving blip. When a backend dependency does slow down during the sale, the team is alerted promptly on a signal that actually reflects degraded user experience, and they already have the quota headroom to scale additional capacity in response.

**Memory Hook**

Preparing for a traffic spike needs two things: enough capacity (review and raise quotas) and good visibility (meaningful metrics and targeted alerts) — not new infrastructure tooling, not averaged latency, and not alerts on every failure.

**30-Second Exam Takeaway**

When a scenario asks how to prepare a service for a known high-traffic event, look for one action that secures adequate capacity/quota headroom and one that ensures well-targeted observability — and be suspicious of any monitoring-sounding option that uses averages instead of percentiles, or alerts on everything instead of what matters.

**Official References**

[**Google Cloud — Prepare for a peak capacity event:**](https://docs.cloud.google.com/support/docs/checklists/plan-peak-capacity-event) Supports: capacity planning and quota review as a core part of preparing for a known high-traffic event

[**Google SRE Book — Chapter 6: Monitoring Distributed Systems:**](https://sre.google/sre-book/monitoring-distributed-systems/) Supports: the four golden signals framework, and latency being tracked as a percentile-based distribution rather than an average, underpinning why targeted, meaningful alerting beats averaged metrics and blanket alerting

</details>

---

### Exam 4 · Q31

You are the Operations Lead handling an ongoing incident on one of your services. The service typically operates at around 70% capacity, and you’ve noticed that one node is returning 5xx errors on every request it receives, along with a noticeable rise in customer support cases. You need to pull the offending node out of the load balancer pool so you can isolate and investigate it, while following Google-recommended practices to manage the incident and limit the impact on users. What should you do?

- A.
    Communicate your intent to the incident team.
    Perform a load analysis to determine whether the remaining nodes can absorb the traffic that would be offloaded from the removed node, and scale the pool if the analysis shows it’s needed.
    Once any new nodes report healthy, drain traffic from the unhealthy node and remove it from service.
- B.
    Communicate your intent to the incident team.
    Add a new node to the pool, and wait for it to report as healthy.
    Once traffic is being served from the new node, drain traffic from the unhealthy node and remove the old node from service.
- C.
    Drain traffic from the unhealthy node and remove it from service.
    Monitor traffic to confirm the error is resolved and that the remaining nodes in the pool are handling the load appropriately.
    Scale the pool as necessary to handle the new load.
    Communicate your actions to the incident team.
- D.
    Drain traffic from the unhealthy node and remove the old node from service.
    Add a new node to the pool, wait for it to report as healthy, and begin serving traffic from it.
    Monitor traffic to confirm the pool is healthy and handling traffic appropriately.
    Communicate your actions to the incident team.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A.

**Correct Answer**

**A.**

  1. Communicate your intent to the incident team.

  2. Perform a load analysis to determine whether the remaining nodes can absorb the traffic that would be offloaded from the removed node, and scale the pool if the analysis shows it’s needed.

  3. Once any new nodes report healthy, drain traffic from the unhealthy node and remove it from service.

**Exam Reasoning Explanation**

Three things must hold: the incident team stays informed as part of coordinated response rather than finding out after the fact; removing the unhealthy node must not leave the remaining pool unable to absorb its traffic, since the service already runs at a substantial 70% baseline; and the node should be removed gracefully, by draining it, rather than abruptly. Options C and D both act first and communicate last, running against coordinated incident response, and both remove the unhealthy node before confirming sufficient remaining capacity, risking a cascading overload in the window before new capacity is added. Option B communicates first and ensures a new node is healthy before removing the bad one, protecting capacity, but it unconditionally adds a new node without first checking whether the existing 30% of spare capacity is actually enough — less analysis-driven than evaluating first. Option A communicates first, performs a load analysis to determine whether scaling is actually needed given the service’s normal 70% utilization, scales only if that analysis shows a genuine gap, and only then drains and removes the unhealthy node — satisfying all three requirements with the most measured, analysis-driven approach.

**Key Exam Clues**

  * “The service usually runs at around 70% capacity” — a deliberately given detail establishing headroom in the system, prompting an analysis of whether that headroom is sufficient rather than an automatic decision to add capacity

  * “follow Google-recommended practices to manage the incident” — points toward structured incident response, including communication to the incident team as coordination happens, not as a final report

  * “remove the offending node... so that you can isolate and investigate” — frames node removal as the goal, but one that still needs to happen safely, which is why the order of operations matters

  * Communication appearing as either the first or last step across the four options — a clear signal that when communication happens is one of the things being tested

**Why This Is Correct**

Communicating intent to the incident team first keeps everyone coordinated before a production-affecting action is taken, core to structured incident response. Performing a load analysis before deciding whether to scale directly uses the fact that the service normally runs at 70% capacity — rather than assuming new capacity is automatically required, the analysis determines whether existing headroom is enough to absorb the unhealthy node’s traffic, scaling only if it isn’t. Waiting until any new nodes report healthy before draining and removing the unhealthy node ensures the pool never dips below the capacity needed to serve current demand, and draining lets in-flight requests complete safely rather than being abruptly cut off.

**Why the Other Options Are Not the Best Fit**

**Option B — Technically Possible but Not Best:** Communicating first and ensuring a new node is healthy before removing the bad one protects capacity, but it skips the load analysis step and always adds a new node regardless of whether the service’s existing spare capacity would have been sufficient on its own — a less deliberate response than evaluating first.

**Option C — Violates Requirement:** Removing the unhealthy node before confirming the remaining nodes can handle the offloaded traffic risks overloading the pool during the gap before scaling happens reactively in step 3, and communicating to the incident team only as the final step means coordination happens after the mitigating action has already been taken.

**Option D — Violates Requirement:** This shares Option C’s core problems — the unhealthy node is removed before any replacement capacity exists, creating a window where the pool may be under-provisioned, and communication again comes last, after the node has already been pulled and a new one added.

**Exam Trap**

The trap is treating “remove the bad node quickly” as the priority, when the real priority is removing it _safely_ , without creating a second, broader problem by overloading the remaining capacity — Options C and D both act first and reason about capacity afterward, reversing the safer order. A second trap is assuming any option that adds a new node before removing the old one is equally good; Option B does this unconditionally, while the specifically called-out 70% baseline capacity detail rewards recognizing that a load analysis might show scaling isn’t even necessary, which only Option A captures.

**Foundation Concept**

Mitigating an incident that involves removing a capacity-serving component from production should follow a sequence that protects users throughout: communicate with the incident team as actions are planned and taken, assess whether remaining capacity is sufficient using the real utilization data already known about the system, scale only if that assessment shows a genuine gap, and perform the actual removal gracefully only once any necessary additional capacity is confirmed healthy. This ordering keeps both the team and the user-facing system in a known-good state at every step.

**Real-World Connection**

An on-call engineer managing a node reporting 5xx errors on all requests tells the incident channel what they’re about to do, checks current utilization against the service’s normal 70% baseline, confirms the remaining nodes have enough headroom to absorb the bad node’s share of traffic without needing to scale, and then drains and removes the unhealthy node — all while the incident team has visibility into each step as it happens, and users experience a smooth transition rather than a second wave of errors from an overloaded remaining pool.

**Memory Hook**

Communicate first, analyze capacity before acting, scale only if the analysis shows it’s needed, then drain and remove — never remove the bad node before confirming the rest of the pool can handle the load, and never save communication for last.

**30-Second Exam Takeaway**

When a question sequences incident mitigation steps around removing a capacity-serving node, look for the option that communicates to the incident team first, performs a capacity/load analysis before deciding whether to scale, and only drains and removes the unhealthy node once sufficient capacity is confirmed — options that act before analyzing or communicate only after acting are the wrong order.

**Official References**

[**Google SRE Workbook — Chapter 9: Incident Response:**](https://sre.google/workbook/incident-response/) Supports: the “3Cs” of incident management (coordinate, communicate, control) that make early communication with the incident team a core part of a well-run mitigation, rather than a final report after action has already been taken

</details>

---

### Exam 4 · Q34

You have just noticed that one of your services has used up its error budget for the current rolling window. Meanwhile, your company’s product team is about to launch a new feature. You want to follow Site Reliability Engineering (SRE) practices. What should you do?

- A. Tell the team there is no error budget left, and make sure all of their tests pass so the launch doesn’t put any further strain on the budget.
- B. Tell the team their error budget is used up. Negotiate with them between a launch freeze and accepting a somewhat worse user experience.
- C. Escalate the situation and ask for additional error budget.
- D. Search the product’s other metrics for SLOs that still have error budget left, reallocate that budget, and let the feature launch proceed.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Tell the team their error budget is used up. Negotiate with them between a launch freeze and accepting a somewhat worse user experience.

**Correct Answer**

**B. Tell the team their error budget is used up. Negotiate with them between a launch freeze and accepting a somewhat worse user experience.**

**Exam Reasoning Explanation**

The error budget exists to give product and SRE teams a shared, data-driven way to trade reliability against feature velocity. Once the budget is spent, the data says reliability should take priority, and the decision about releases is made transparently with the team that wants to launch. Option B does this. It surfaces the fact that the budget is exhausted and puts the actual trade-off on the table: freeze the launch, or knowingly accept a degraded user experience. Options A, C, and D each try to get around the signal instead of acting on it. A assumes passing tests protect the budget, but tests do not stop production errors. C treats the budget as something to request more of, which defeats its purpose. D moves budget between unrelated SLOs, which does not reflect the reliability of the service that has actually exceeded its budget.

**Key Exam Clues**

  * “exceeded the error budget for the current rolling window” is the trigger condition that the SRE error budget policy exists to handle

  * “You want to follow Site Reliability Engineering (SRE) practices” points to the error budget policy and its release-versus-reliability trade-off, not to workarounds

  * “about to launch a new feature” sets up the tension between velocity and reliability that error budgets are designed to arbitrate

  * The options that reallocate or request more budget (C, D) treat the budget as negotiable arithmetic, which should stand out as incompatible with how SLOs work

**Why This Is Correct**

Google’s example error budget policy states that when a service has exceeded its error budget for the preceding four-week window, all changes and releases other than P0 issues or security fixes are halted until the service is back within its SLO. The same policy says it is not meant as a punishment, and that it gives teams permission to focus on reliability when the data indicates it matters more than new features. Notifying the product team and negotiating between a launch freeze and tolerating a slightly worse user experience follows this approach. It treats the exhausted budget as a decision point for the whole organization, to be resolved openly with the team that owns the launch, rather than as something to hide, bypass, or inflate.

**Why the Other Options Are Not the Best Fit**

**Option A: Technically Possible but Not Best.** Passing tests is good practice, but it does not address the situation. The service has already overspent its budget, and tests cannot guarantee that a launch won’t add production errors. It also leaves the trade-off implicit and doesn’t give the product team the information needed to decide about the launch.

**Option C: Violates Requirement.** An error budget is derived directly from the SLO, which is 1 minus the target, so it is not something that can be granted on request. Asking for more budget turns the budget from a decision-making tool into a negotiable allowance and removes the signal that reliability needs attention.

**Option D: Violates Requirement.** Each SLO measures a different aspect of user experience, so spare budget on one SLO does not offset overspending on another. Reallocating budget hides the fact that the affected service is unreliable and lets the launch go ahead while users are already seeing degraded reliability on that dimension.

**Exam Trap**

The trap is choosing an option that sounds cooperative, such as being helpful by ensuring the launch is safe (A), finding more budget (C), or reallocating it (D). All three let the launch proceed without confronting the exhausted budget. The correct answer is the one that surfaces the exhausted budget to the product team and has them decide between a freeze and a worse user experience, because the error budget is meant to inform that decision, not be engineered around. The option wording is also a trap: “tolerate a slightly worse user experience” can look like a poor choice, but it is the honest alternative to a freeze that the policy expects teams to weigh.

**Foundation Concept**

An error budget is the allowed amount of unreliability implied by an SLO, calculated as 100% minus the SLO target. Error budgets give product and SRE teams a shared way to balance reliability against feature velocity. While budget remains, teams can take risks and release features. When it is exhausted, an error budget policy agreed in advance by the stakeholders governs what happens next, typically halting non-critical releases until the service is back within its SLO. Disputes about how the policy applies are escalated to a defined decision maker rather than resolved by changing the budget.

**Real-World Connection**

A team’s checkout service has used all of its four-week error budget after a series of incidents, and the product team plans to ship a promotion feature next week. The SRE lead meets with the product manager, shows that the budget is exhausted and which incidents consumed it, and lays out two options: delay the launch while engineering fixes the causes, or launch on schedule and accept that checkout reliability may stay below target for a while. The product manager decides to slip the launch by two weeks. The decision is made with the data in front of everyone, and nobody has altered the SLO or moved budget around to make the numbers look acceptable.

**Memory Hook**

Budget spent means the launch decision goes back to the team: freeze it or knowingly accept worse reliability. Don’t ask for more budget, don’t move budget between SLOs, and don’t treat passing tests as a substitute.

**30-Second Exam Takeaway**

When a scenario says a service has exhausted its error budget and a launch is coming, choose the answer that communicates the exhausted budget and has the team decide between halting the launch and accepting reduced reliability. Reject any option that creates, requests, or reallocates budget to make the launch possible.

**Official References**

[**Google SRE Workbook, Appendix B: Example Error Budget Policy:**](https://sre.google/workbook/error-budget-policy/) Supports: halting changes and releases other than P0 issues or security fixes once the four-week error budget is exceeded, the policy’s non-goal of punishing teams for missing SLOs, and escalation to a named decision maker when parties disagree

[**Google SRE Workbook, Chapter 2: Implementing SLOs:**](https://sre.google/workbook/implementing-slos/) Supports: the definition of an error budget as 100% minus the SLO, and the use of an error budget policy to decide what to do once the budget is exhausted

</details>

---

### Exam 4 · Q35

You are creating a Cloud Monitoring SLO for a service that will be published soon. You want to verify that requests to the service are handled in under 300 ms at least 90% of the time over each calendar month. You need to choose the metric and the evaluation method. What should you do?

- A. Select a latency metric and use the request-based evaluation method.
- B. Select a latency metric and use the windows-based evaluation method.
- C. Select an availability metric and use the request-based evaluation method.
- D. Select an availability metric and use the windows-based evaluation method.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Select a latency metric and use the request-based evaluation method.

**Correct Answer**

**A. Select a latency metric and use the request-based evaluation method.**

**Exam Reasoning Explanation**

Two independent choices have to be right: which metric measures the thing the SLO is about, and which evaluation method counts the right kind of event. The goal is about how fast requests are served, so the metric must be latency, which removes both availability options. The goal is also stated as a share of requests that meet a threshold (“fewer than 300 ms at least 90% of the time”), so each request is the unit being counted, and that is the request-based method. “Per calendar month” is a separate SLO setting, the compliance period, and does not influence either choice. Only A is correct on both.

**Key Exam Clues**

  * “requests... addressed in fewer than 300 ms” is a technical signal that the SLI is latency, with a 300 ms threshold deciding which requests count as good

  * “at least 90%” is the performance goal, expressed as a proportion of requests that meet the threshold, which is how a request-based SLI is defined

  * “per calendar month” is a compliance-period setting, not a clue about the metric or evaluation method

  * “identify the metric and evaluation method” tells you the answer needs one choice for each, so both must be checked

**Why This Is Correct**

A latency SLI in Cloud Monitoring is the ratio of calls under a latency threshold to all calls. With request-based evaluation, the SLO is met when the fraction of good requests, here those faster than 300 ms, is at or above the goal over the compliance period. Cloud Monitoring’s own example is “Latency is below 100 ms for at least 95% of requests”, which has the same structure as this requirement. You set the 300 ms threshold in the SLI details, the 90% goal as the performance goal, and a calendar month as the compliance period.

**Why the Other Options Are Not the Best Fit**

**Option B, Violates Requirement.** Windows-based evaluation counts time intervals that meet a goodness criterion, for example 10-minute windows in which the 95th-percentile latency is under a threshold. That measures the share of time a service performed well, which is not the share of requests under 300 ms. It also gives a quiet interval the same weight as a busy one, which changes what is being measured.

**Option C, Different Use Case.** Request-based evaluation is the right method, but an availability metric measures the ratio of successful responses to all responses, not how fast they were. A fast failure or a slow success would both be misjudged, so this option cannot verify a latency target.

**Option D, Violates Requirement.** It is wrong on both counts: availability does not measure speed, and windows-based evaluation does not count requests.

**Exam Trap**

The phrase “90% of the time” tempts people toward windows-based evaluation, since “of the time” sounds like time intervals. In this scenario, though, “of the time” is shorthand for “of the requests”, because the subject of the sentence is requests and the threshold applies to each of them. A second trap is treating “per calendar month” as a hint about the evaluation method, when it is only the compliance period. The answer would change to windows-based if the goal were stated per interval, for example “95th-percentile latency under 300 ms in at least 90% of 10-minute windows”, or if the only raw metric available were a latency percentile, since Google’s documentation says a percentile metric requires a windows-based SLO.

**Foundation Concept**

A Cloud Monitoring SLO is built from three parts: an SLI that measures performance, a performance goal, and a compliance period, either calendar-based or rolling. The SLI is chosen in two steps, the metric (such as availability or latency) and the evaluation method. Request-based evaluation treats each request as the event and reports the fraction of good requests. Windows-based evaluation treats each time interval as the event and reports the fraction of good intervals.

**Real-World Connection**

A team preparing to launch an API defines its latency SLO in the Cloud Monitoring console by choosing the latency metric, selecting request-based evaluation, setting the threshold to 300 ms, setting the goal to 90%, and using a calendar month as the compliance period. Once the service is live, the console shows what share of requests came in under 300 ms. The team can also use the remaining error budget to decide whether a risky release is acceptable.

**Memory Hook**

Choose the metric for what you measure (speed means latency), choose the evaluation method for what you count (requests means request-based), and treat the calendar month as the compliance period.

**30-Second Exam Takeaway**

When a Cloud Monitoring SLO is worded as “X% of requests faster than N ms”, use a latency metric with request-based evaluation. Pick windows-based only when the goal is about the share of time intervals that meet a criterion, or when the raw metric is a percentile.

**Official References**

[**Google Cloud Observability: Concepts in service monitoring:**](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring) Supports: the definition of a latency SLI as the ratio of calls below a threshold to all calls, request-based versus windows-based SLO compliance, the example “Latency is below 100 ms for at least 95% of requests”, and calendar-based compliance periods

[**Google Cloud Observability: Creating an SLO:**](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-slo) Supports: the console workflow of choosing a metric, then a request-based or windows-based evaluation method, setting the latency threshold, and choosing a calendar or rolling compliance period

</details>

---

### Exam 4 · Q38

You are the Site Reliability Engineer responsible for your company’s data services and products. You regularly deal with operational challenges, such as unpredictable data volume and high cost, in your company’s data ingestion processes. You have just learned that a new data ingestion product will be developed in Google Cloud. You need to work with the product development team to give them operational input on the new product. What should you do?

- A. Deploy the prototype product to a test environment, run a load test, and share the results with the product development team.
- B. After the initial version passes the quality assurance phase and compliance assessments, deploy the product to a staging environment, and share error logs and performance metrics with the product development team.
- C. Once at least one internal customer is using the new product in production, share error logs and monitoring metrics with the product development team.
- D. Review the product’s design with the product development team, and give feedback early in the design phase.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Review the product’s design with the product development team, and give feedback early in the design phase.

**Correct Answer**

**D. Review the product’s design with the product development team, and give feedback early in the design phase.**

**Exam Reasoning Explanation**

The operational problems named in the scenario, unpredictable data volume and high cost, are largely determined by architecture and design choices. The input you provide is therefore worth the most when it arrives while those choices are still being made. Options A, B, and C each offer evidence and feedback at a later stage of the lifecycle, after the design has been built and more commitments exist. Only D puts operational experience into the design itself, where changes are cheapest. The later options also use test, staging, or production data to describe problems that earlier input could have prevented.

**Key Exam Clues**

  * “unpredictable data volume and high cost” are design-level concerns, such as how the system absorbs bursts and how it uses resources, which are hard to fix after the architecture is set

  * “a new data ingestion product will be developed” means the product is at the start of its lifecycle, so there is still a design phase to influence

  * “collaborate with the product development team to provide operational input” points to working together on the product’s design, not delivering test or monitoring reports

  * Options A, B, and C describe progressively later lifecycle stages (prototype test, staging, production), while D is the only one at the design stage

**Why This Is Correct**

Google’s SRE engagement model describes the architecture and design phase as the first place SRE can contribute, for example by sharing best practices, giving early engagement consulting on architectures and design choices, and helping validate assumptions with targeted prototypes. The SRE Workbook notes that early SRE engagement can help avoid costly redesigns that become necessary once a system meets real-world users and has to scale as the service grows. That is the same set of problems you face with unpredictable volume and cost. Reviewing the design with the development team lets you bring the lessons from your existing ingestion processes into the new product before they are expensive to apply.

**Why the Other Options Are Not the Best Fit**

**Option A, Technically Possible but Not Best.** A prototype load test gives useful evidence, but it comes after a prototype exists, so major design decisions have already been made. Results that show a scaling or cost problem may then force rework that earlier design input could have avoided.

**Option B, Technically Possible but Not Best.** Waiting until the product has passed quality assurance and compliance assessments means the design is largely fixed and changes are expensive. Error logs and performance metrics from staging describe what was built, not what should be built.

**Option C, Technically Possible but Not Best.** Sharing logs and metrics only after an internal customer uses the product in production is the most reactive choice. It treats SRE as a recipient of problems instead of a contributor to the product, and real users are already exposed to any issue before the first piece of input is given.

**Exam Trap**

The trap is picking a hands-on validation step, especially the load test in A, because it sounds concrete and data-driven. A load test is valuable, but it answers whether a design copes after the design exists. The scenario’s cues, unpredictable volume and high cost, are design problems that are best handled before building. The answer would change to A if the product were already built and the question asked how to verify capacity before launch.

**Foundation Concept**

The cost of changing a decision rises as a service moves through its lifecycle. Characteristics such as how a system handles variable load and how efficiently it uses resources are set during architecture and design. Engaging early, sometimes called shifting left, lets operational experience shape those decisions instead of being applied as fixes later. SRE can take part through design reviews, best practices, and consulting, and still engage at later stages when a team arrives late.

**Real-World Connection**

An SRE with experience of bursty ingestion volumes is invited to the new product’s design review. They raise questions about what happens when input spikes, how cost grows with volume, and how operators will see and control both. The development team revises the design before any code is written, and the team avoids discovering the problem later through a failed load test or a production incident.

**Memory Hook**

Operational problems that come from design are best fixed in the design phase, so review the design early.

**30-Second Exam Takeaway**

When a new product is just starting development and SRE wants to contribute operational input, choose early engagement in the design phase over any option that waits for a prototype, staging, or production. Later steps validate or react to design choices, but only early input can change them cheaply.

**Official References**

[**Google SRE Workbook, Chapter 18: SRE Engagement Model:**](https://sre.google/workbook/engagement-model/) Supports: Phase 1 (Architecture and Design) engagement activities, such as early engagement consulting and best practices, and the point that early SRE engagement can help avoid costly redesigns when systems meet real users and need to scale

[**Google SRE Book, Chapter 32: The Evolving SRE Engagement Model:**](https://sre.google/sre-book/evolving-sre-engagement-model/) Supports: the Early Engagement Model and the Production Readiness Review process as ways for SRE to partner with development teams across a service’s lifecycle

</details>

---

### Exam 4 · Q39

You need to introduce postmortems into your organization, and you want the postmortem process to be well received. What should you do? (Choose two.)

- A. Encourage new employees to learn the practice by conducting postmortems for the team.
- B. Set up a dedicated team that is responsible for conducting every postmortem.
- C. Encourage senior leadership to acknowledge and take part in postmortems.
- D. Make sure that writing effective postmortems is a practice that is both rewarded and celebrated.
- E. Give the organization a forum in which to critique earlier postmortems.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Encourage senior leadership to acknowledge and take part in postmortems. **|** D. Make sure that writing effective postmortems is a practice that is both rewarded and celebrated.

**Correct Answer**

**C. Encourage senior leadership to acknowledge and take part in postmortems.**

**D. Make sure that writing effective postmortems is a practice that is both rewarded and celebrated.**

**Exam Reasoning Explanation**

The goal is cultural adoption: people must see the postmortem process as valuable and safe rather than as a burden or a punishment. Two options describe the reinforcement mechanisms that build that perception. Visible senior-leadership participation signals that the practice is important and that the whole organization, including those at the top, takes part in learning from failure (C). Rewarding and celebrating effective postmortem writing gives the people who do the work a positive reason to do it well and to keep doing it (D). The remaining options each undermine the goal. Handing every postmortem to a designated team (B) takes ownership away from the engineers who understand the incident. Assigning new employees to conduct postmortems (A) puts the least-equipped people in charge of the process. Opening earlier postmortems to critique (E) risks making authors feel judged. C and D act independently, one through top-down modeling and the other through bottom-up recognition, and together they cover the two main levers of cultural change.

**Key Exam Clues**

  * “introduce postmortems into your organization” frames this as a culture-change question, not a process-design or staffing question

  * “well received” is the success criterion: the right answers are the ones that build acceptance, not the ones that merely get postmortems written

  * “(Choose two.)” signals two complementary actions, here one leadership-driven and one recognition-driven

  * “designated team that is responsible for conducting all postmortems” is a centralization pattern that conflicts with ownership by the engineers involved

**Why This Is Correct**

Google’s SRE guidance says that introducing a postmortem culture takes continuous cultivation and reinforcement, and it lists specific strategies for winning people over. Two of them are to encourage senior leadership’s acknowledgment and participation in postmortems, and to make sure that writing effective postmortems is a rewarded and celebrated practice, both publicly and through individual and team performance management. Leadership participation shows that postmortems matter. Visible rewards show that the effort is valued, which counters the common objection that postmortems cost too much time for too little benefit.

**Why the Other Options Are Not the Best Fit**

**Option A: Technically Possible but Not Best.** Practice has value for newcomers, but having new employees conduct the team’s postmortems puts the least experienced people in charge of a sensitive process whose goal is to build trust. Google’s guidance instead has new SREs learn through exercises that reenact past postmortems, such as the Wheel of Misfortune, which is practice without ownership of real incidents.

**Option B: Violates Requirement.** A dedicated team that conducts every postmortem separates the analysis from the engineers closest to the incident. It makes the process feel imposed from outside and cuts against the collaborative, engineer-owned approach that Google describes, in which blameless postmortems are ideally the product of engineer self-motivation.

**Option E: Technically Possible but Not Best.** Feedback on the postmortem process is valuable, and Google surveys teams about its effectiveness. A forum to critique previous postmortems, though, invites judgment of individual authors’ work, which can make people reluctant to write them. It is not one of the recommended strategies for building acceptance.

**Exam Trap**

The trap is picking options that sound rigorous or process-oriented, such as a dedicated postmortem team (B) or a critique forum (E), when the question asks what makes the process well received. Acceptance comes from signals of safety and value, namely leadership participation and visible recognition, not from adding oversight or centralizing ownership. Option A is a subtler trap, because training newcomers sounds constructive but gives them a sensitive responsibility they are not yet equipped to carry.

**Foundation Concept**

Introducing postmortems is a cultural change as much as a technical one. Cultures shift through what leaders visibly do and what the organization visibly rewards. If senior people participate and good postmortem work is celebrated, others conclude that the practice is safe, valued, and expected. Mandates, centralized ownership, or critique mechanisms can produce documents without producing the openness that makes postmortems useful.

**Real-World Connection**

A new engineering director starts joining postmortem review sessions and says openly what they learned from each one. The team also starts a monthly newsletter that highlights a well-written postmortem and its author, and managers cite strong postmortem work in performance reviews. Engineers who initially saw postmortems as paperwork begin to see them as a way to gain recognition, and they start volunteering to write them.

**Memory Hook**

To make postmortems well received: leaders take part, and good postmortem work gets visibly rewarded. Do not centralize them, hand them to newcomers, or open them to critique.

**30-Second Exam Takeaway**

When a question asks how to get a postmortem culture accepted, choose the options that build safety and perceived value: visible senior-leadership participation and public and performance-based recognition for writing good postmortems. Avoid options that centralize ownership, assign the process to inexperienced staff, or expose authors to critique.

**Official References**

[**Google SRE Book, Chapter 15: Postmortem Culture: Learning from Failure:**](https://sre.google/sre-book/postmortem-culture/) Supports: the “Introducing a Postmortem Culture” strategies of rewarding and celebrating effective postmortem writing and encouraging senior leadership’s acknowledgment and participation, plus the collaborative, engineer-owned approach that rules out a dedicated postmortem team

[**Google SRE Workbook, Chapter 10: Postmortem Culture: Learning from Failure:**](https://sre.google/workbook/postmortem-culture/) Supports: the framing of introducing postmortems as a cultural change that can start small and be tuned to the organization

</details>

---

### Exam 4 · Q40

You have deployed a fleet of Compute Engine instances in Google Cloud. You need to make sure the instances’ monitoring metrics and logs appear in Cloud Logging and Cloud Monitoring, where your company’s operations and cybersecurity teams can see them. You must grant the required roles to the Compute Engine service account through Identity and Access Management (IAM), following the principle of least privilege. What should you do?

- A. Grant the logging.logWriter and monitoring.metricWriter roles to the Compute Engine service accounts.
- B. Grant the logging.admin and monitoring.editor roles to the Compute Engine service accounts.
- C. Grant the logging.editor and monitoring.metricWriter roles to the Compute Engine service accounts.
- D. Grant the logging.logWriter and monitoring.editor roles to the Compute Engine service accounts.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Grant the logging.logWriter and monitoring.metricWriter roles to the Compute Engine service accounts.

**Correct Answer**

**A. Grant the logging.logWriter and monitoring.metricWriter roles to the Compute Engine service accounts.**

**Exam Reasoning Explanation**

The roles in question go to the service account that the instances run as. That identity only needs to send telemetry, meaning log entries to Cloud Logging and metrics to Cloud Monitoring. The operations and security teams’ ability to view the data depends on their own identities’ access, which this question does not ask you to configure. Because the stated requirement is least privilege, the right choice is the narrowest write-only role for each service. Any role that adds read, edit, or administrative abilities to the service account is wrong. A is the only option made up of two write-only roles.

**Key Exam Clues**

  * “grant the required roles for the Compute Engine service account” is a hard constraint: the identity being configured is the one that sends telemetry, not the people who read it

  * “following the principle of least privilege” is a hard constraint that rules out admin and editor roles when a write-only role exists

  * “monitoring metrics and logs” is a technical signal that two separate write permissions are needed, one for each service

  * Every option pairs one logging role with one monitoring role, so both halves must be checked for excess privilege

**Why This Is Correct**

Google’s Ops Agent authorization guidance names Logs Writer and Monitoring Metric Writer as the roles for the service account the agent uses. The Logs Writer role (logging.logWriter) provides the permissions to write log entries. The Monitoring Metric Writer role (monitoring.metricWriter) is write-only and is intended for service accounts and agents. Together they let the instances send logs and metrics and do nothing beyond that. The same guidance says to grant the service account the least privileged IAM roles possible.

**Why the Other Options Are Not the Best Fit**

**Option B — Violates Requirement:** Logging Admin gives full access to all features of Cloud Logging, and Monitoring Editor gives read-write access to Monitoring, including creating and editing configurations such as dashboards and alerting policies. A service account that only sends telemetry needs neither, so this pair breaks least privilege on both sides.

**Option C — Violates Requirement:** Monitoring Metric Writer is correct, but it is paired with an editor-style logging role, which implies broader access than writing log entries. Google documents Logs Writer as the role that provides the permission to write log entries, so the editor-style role adds privilege without adding capability the agent needs.

**Option D — Violates Requirement:** Logs Writer is correct, but Monitoring Editor grants read-write access to Monitoring and the ability to create and edit configurations. The service account only has to write metrics, which Monitoring Metric Writer already covers.

**Exam Trap**

The trap is choosing a role pair that would certainly make everything work, such as editor or admin roles, instead of the narrowest pair that does the job. Options B, C, and D each contain one plausible role, which makes them look reasonable. Both halves have to be write-only. A second trap is reading “visible by the operations and security teams” as a reason to give the service account viewing roles, when visibility is a matter of the teams’ own access. The answer would change only if the question asked what the teams themselves need to read the data, in which case viewer roles would apply to them and not to the service account.

**Foundation Concept**

A telemetry agent on a VM authenticates as the VM’s attached service account and needs permission only to write data. Cloud Logging and Cloud Monitoring each have a purpose-built write-only role for this, Logs Writer and Monitoring Metric Writer, which are separate from the viewer, editor, and admin roles meant for people. IAM roles are one part of authorization. For VMs that use the default Compute Engine service account, the instance’s access scopes must also permit writing, and Google notes that new VMs usually have adequate scopes but older VMs or VMs with modified scopes might not.

**Real-World Connection**

A platform team builds an instance template for a fleet and attaches a service account that holds only Logs Writer and Monitoring Metric Writer. The Ops Agent on each VM sends logs and metrics, and the operations and security teams read them using their own viewer roles. If an instance were compromised, the service account could do little beyond writing telemetry, so the potential damage is limited.

**Memory Hook**

An instance’s service account only writes telemetry, so give it Logs Writer and Monitoring Metric Writer.

**30-Second Exam Takeaway**

When a question asks which roles an instance’s service account needs for logs and metrics under least privilege, choose the two write-only roles, Logs Writer and Monitoring Metric Writer. Reject admin and editor roles, which add abilities the service account never uses.

**Official References**

[**Google Cloud Observability — Authorize the Ops Agent:**](https://docs.cloud.google.com/logging/docs/agent/ops-agent/authorization) Supports: the Logs Writer and Monitoring Metric Writer roles for the service account the agent uses, the guidance to grant the least privileged roles possible, and the access-scope caveat for older VMs

[**Google Cloud Monitoring — Control access with IAM:**](https://docs.cloud.google.com/monitoring/access-control) Supports: Monitoring Metric Writer as the write-only role for service accounts and agents, Monitoring Editor’s read-write access to configurations, and Logging Admin’s full access to Cloud Logging

[**Google Cloud IAM — Cloud Logging roles and permissions:**](https://docs.cloud.google.com/iam/docs/roles-permissions/logging) Supports: Logs Writer (roles/logging.logWriter) providing the permissions to write log entries

</details>

---

### Exam 4 · Q43

Your CTO has asked you to put a postmortem policy in place for every incident, for internal use. You want to define what a good postmortem looks like so that the policy succeeds at your company. What should you do? (Choose two.)

- A. Require every postmortem to state what caused the incident, name the person or team responsible for causing it, and describe how to prevent it from recurring.
- B. Require every postmortem to state what caused the incident, describe how the incident could have been worse, and describe how to prevent it from recurring.
- C. Require every postmortem to state the severity of the incident, describe how to prevent it from recurring, and describe what caused it without naming internal system components.
- D. Require every postmortem to state how the incident was resolved and what caused it, without naming customer information.
- E. Require every postmortem to involve all incident participants in authoring it, and share postmortems as widely as possible.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Require every postmortem to state what caused the incident, describe how the incident could have been worse, and describe how to prevent it from recurring. **|** E. Require every postmortem to involve all incident participants in authoring it, and share postmortems as widely as possible.

**Correct Answer**

**B. Require every postmortem to state what caused the incident, describe how the incident could have been worse, and describe how to prevent it from recurring.**

**E. Require every postmortem to involve all incident participants in authoring it, and share postmortems as widely as possible.**

**Exam Reasoning Explanation**

A successful postmortem policy needs two things: a clear standard for what a postmortem contains, and a process that keeps postmortems honest and useful. The content standard must produce learning and prevention, which means a real root cause, the near-misses that show hidden risk, and actions that prevent recurrence, without blaming anyone. The process standard must bring in everyone who saw the incident and make the result visible to the people who can learn from it. B supplies the content, and E supplies the process. A, C, and D each contain a flaw that would weaken the policy: blame, withheld technical detail, or missing preventive action. B and E work independently of each other, and together they cover both halves of what the CTO asked for.

**Key Exam Clues**

  * “define what a good postmortem is” is a hard constraint that points to both the content and the practices of a quality postmortem

  * “to ensure that the policy is successful” is a hard constraint favoring practices that build trust and adoption, such as blamelessness and open sharing

  * “for internal use” is a technical signal that postmortems can name specific systems and include specific data, which weighs against options that remove technical detail

  * “(Choose two.)” is a cardinality instruction, so one selected option should cover content and the other process

  * “identify the person or team responsible” is an exclusion, since it describes the blame-oriented pattern the policy needs to avoid

**Why This Is Correct**

Option B matches how Google describes a good postmortem. It identifies the root cause and trigger, it includes a “Where we got lucky” lesson, which records the factors that kept the incident from being worse and exposes latent risk, and it ends in preventive action items. The Workbook states that a postmortem with no action items is ineffective, and it describes root-cause sections that focus on what went wrong, not who caused it. Option E matches the Workbook’s recommendations to include all incident participants in postmortem authoring, because a postmortem written in isolation or by one team can overlook contributing factors, and to share postmortems as widely as possible, because the value of a postmortem is proportional to the learning it creates. The two work independently, since one governs what is written and the other governs how it is written and shared, and together they form a complete definition of a good postmortem.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement:** Naming the person or team responsible is the blame-oriented pattern the Workbook lists as a failure mode. It makes people risk-averse and tempts them to hide facts that are critical to preventing recurrence. It is tempting because it names a cause and a prevention step, but the policy’s success depends on blamelessness.

**Option C — Violates Requirement:** Severity and prevention are useful, but banning internal system component names removes the technical specifics needed to explain the root cause and write measurable action items. Google’s good example names the systems involved and explains unfamiliar terms in a glossary, and a policy for internal use should allow that detail.

**Option D — Technically Possible but Not Best:** Describing resolution and cause is useful, and keeping end-user information out of postmortems matches Google’s practice. The option omits follow-up and preventive actions, though, which Google treats as essential, and it says nothing about collaboration or sharing, so it leaves the policy’s success to chance.

**Exam Trap**

The trap is option A, because identifying who caused an incident feels like accountability. A blameless postmortem pursues accountability through owned, tracked action items and through fixing system gaps, not through naming individuals. Option D is a quieter trap, since protecting customer information is a real concern and the option sounds responsible, but it is incomplete without preventive actions. D would come closer to correct if it added action items, and C would be acceptable if it withheld only end-user details instead of internal components.

**Foundation Concept**

A blameless postmortem is a learning tool that focuses on contributing causes and gaps in systems and processes, assuming people acted with good intentions on the information they had. Its quality has two parts. The content part covers impact, root cause and trigger, resolution, lessons including what went well, what went poorly, and where the team got lucky, and action items that have an owner, a priority, and a measurable end state. The process part covers collaborative authoring, timely publication, and wide sharing. A policy that sets standards for both is more likely to produce postmortems that people trust and learn from.

**Real-World Connection**

A company adopts a postmortem template that requires a root cause, a “where we got lucky” section, and prioritized, owned action items filed as tracked bugs. Each postmortem has one owner and collaborators from every team involved in the incident, and the result is published to all engineering employees within about a week. Engineers outside the incident read the postmortems and fix similar weaknesses in their own systems, so repeat incidents decline and people are willing to share information because nobody is blamed.

**Memory Hook**

A good postmortem is blameless in content (cause, how it could have been worse, prevention) and open in process (everyone involved writes it and everyone can read it).

**30-Second Exam Takeaway**

When a question asks how to define a good postmortem, choose the options that keep the content blameless and focused on cause, near-misses, and prevention, and keep the process collaborative and widely shared. Eliminate options that name individuals, remove technical specifics, or leave out preventive actions.

**Official References**

[**Google SRE Workbook, Chapter 10: Postmortem Culture: Learning from Failure:**](https://sre.google/workbook/postmortem-culture/) Supports: the good-postmortem example with root cause, “Where we got lucky”, and prioritized owned action items, blamelessness, including all incident participants in authoring, and sharing postmortems as widely as possible

[**Google SRE Book, Chapter 15: Postmortem Culture: Learning from Failure:**](https://sre.google/sre-book/postmortem-culture/) Supports: the definition of a postmortem as a record of impact, mitigation, root causes, and follow-up actions, blameless postmortems, sharing to the widest useful audience, and keeping end-user-identifying information out of postmortems

[**Google Cloud — Professional Cloud DevOps Engineer Certification exam guide (Section 3, applying site reliability engineering practices):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment

</details>

---

### Exam 4 · Q50

You’re preparing to launch a new production service that will autoscale through a managed instance group and run across several regions. Each instance will require a substantial amount of resources, and you need to plan for that capacity before launch. What should you do?

- A. Monitor Cloud Trace output over time to determine the right instance sizing
- B. Configure the managed instance group to use the n2-highcpu-96 machine type
- C. Deploy the service across multiple regions behind an internal load balancer that routes traffic between them
- D. Confirm that the instance group’s resource requirements fit within the project’s available quota in each target region

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Confirm that the instance group’s resource requirements fit within the project’s available quota in each target region

**Correct Answer**

**D. Confirm that the instance group’s resource requirements fit within the project’s available quota in each target region**

**Exam Reasoning Explanation**

The hard constraint is that this question is specifically about capacity planning, not architecture choice or sizing methodology. Walking the chain: requirement (plan for capacity for a resource-heavy, autoscaling, multi-region deployment) → capability (Google Cloud enforces allocation quotas — CPU, instances, IP addresses, and the instance-group resources themselves — at the regional level, and scaling cannot exceed what a region’s quota allows) → elimination (A addresses latency monitoring rather than capacity, B picks an implementation detail that was never justified by the scenario and still doesn’t confirm availability, C restates an already-given requirement and adds an unaddressed routing decision) → decision (D is the step that directly verifies the deployment can actually obtain the resources it needs in every target region).

**Key Exam Clues**

  * “need to plan for capacity” is the hard constraint that points directly at capacity-planning practice, not at sizing, routing, or monitoring tooling.

  * “a large number of resources for each instance” combined with “multiple regions” signals that per-region resource consumption could be substantial, making quota exhaustion a realistic risk.

  * “should be deployed across multiple regions” and “automatically scale using a managed instance group” are design decisions the scenario has already made, so any option that simply restates them isn’t answering what’s being asked.

**Why This Is Correct**

Google Cloud enforces allocation quotas at the regional level — CPU quota, instance-group resource quota, IP addresses, and disk are all capped per region, and using an instance group requires having enough available quota for every resource it consumes. Because this service needs a large amount of resources per instance and will autoscale across several regions, the amount of quota consumed in each region could be significant, and an autoscaler that hits a quota ceiling simply stops growing rather than failing loudly. Confirming that each target region’s available quota can support the planned resource requirements before launch is what capacity planning concretely means here, and it’s the one option that directly prevents a silent scaling ceiling in production.

**Why the Other Options Are Not the Best Fit**

**Option A — Different Use Case:** Cloud Trace reports on request latency and the behavior of distributed calls; it has no role in determining machine sizing or confirming quota availability, so monitoring it doesn’t address planning for capacity.

**Option B — Technically Possible but Not Best:** choosing a specific machine type is a real configuration step that has to happen at some point, but nothing in the scenario establishes this workload is specifically CPU-optimized, and selecting a machine type says nothing about whether that scale of resource is actually obtainable in each region — it isn’t capacity planning on its own.

**Option C — Different Use Case:** the scenario already states the service will run across multiple regions, so repeating that isn’t new guidance, and adding an internal load balancer introduces a traffic-routing decision intended for private, internal-only traffic that isn’t established as appropriate here; neither part addresses resource or capacity planning.

**Exam Trap**

The trap is reaching for an architecture or tooling decision — a machine type, a load balancer, a tracing tool — when the question explicitly asks about capacity planning, which in Google Cloud’s documented sense centers on quotas, limits, and reservations. If the scenario instead asked how to pick the right machine shape for a known workload profile, option B’s reasoning would become the relevant one; here, the stated task is specifically to plan for capacity.

**Foundation Concept**

Capacity planning on Google Cloud means confirming, ahead of scaling, that the quotas and limits governing a project in each target region can actually support the resource consumption you expect. Because quotas for things like CPUs, IP addresses, and instance-group resources are enforced per region, a workload that scales smoothly in one region can still stall in another if that region’s quota was never checked or raised in advance.

**Real-World Connection**

A team launches an autoscaling, resource-heavy service into a new region and finds the managed instance group stalls well below its target size during a traffic spike — not because of an application bug, but because the project’s CPU quota in that region was never raised to match the expected scale. After requesting a quota increase ahead of the next regional launch, the same spike is absorbed without incident, which is why checking quota is treated as a pre-launch capacity-planning step rather than something discovered during an outage.

**Memory Hook**

“Before you scale wide, check what each region will actually let you have.”

**30-Second Exam Takeaway**

When a question explicitly asks about planning for capacity for an autoscaling workload spread across multiple regions, look for the option addressing project quotas and limits — that’s Google Cloud’s documented meaning of capacity planning, distinct from sizing, routing, or monitoring decisions.

**Official References**

[**Google Cloud — Resource quotas for Compute Engine:**](https://cloud.google.com/compute/quotas) Supports: correct-answer mechanism — instance groups require available quota for every resource they consume, and quotas are enforced regionally

[Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 3.2, Managing service lifecycle): ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment — capacity planning (quotas, limits, reservations) and autoscaling with managed instance groups

</details>

---

### Exam 4 · Q52

An application running on Google Kubernetes Engine (GKE), made up of several microservices deployed with Deployments and Services, has one microservice whose Pods start returning 403 errors once they’ve been running for more than five hours. Your development team expects it will take about a month to fix the underlying cause, and in the meantime you need to keep the service operating normally, using the fewest steps and following Google-recommended practice. What should you do?

- A. Create a scheduled job that terminates any Pod that has been running for more than five hours
- B. Add an HTTP liveness probe to the microservice’s Deployment
- C. Have someone watch the Pods and manually terminate any that have been running for more than five hours
- D. Set up an alert that notifies you whenever a Pod starts returning 403 errors

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Add an HTTP liveness probe to the microservice’s Deployment

**Correct Answer**

**B. Add an HTTP liveness probe to the microservice’s Deployment**

**Exam Reasoning Explanation**

The hard constraint is that whatever solution is chosen has to keep working automatically, unattended, for about a month, using as little new infrastructure as possible. Walking the chain: requirement (keep a known, time-based failure from affecting operations, with the fewest steps) → capability (Kubernetes’ liveness probe is a built-in mechanism precisely for containers that degrade after running for a while, triggering an automatic restart) → elimination (A duplicates that built-in capability with a separate custom resource, C is unscalable manual toil, D only reports the problem without fixing it) → decision (B is the single, declarative addition that uses Kubernetes’ own self-healing feature exactly as designed).

**Key Exam Clues**

  * “Pod returns 403 errors after... running for more than five hours” is a technical signal describing a container that degrades over time and needs a restart to recover — the exact condition liveness probes exist to detect and fix.

  * “will not be resolved for a month” paired with “ensure continued operations” is a hard constraint requiring the solution to keep working automatically and unattended for weeks, ruling out anything that needs a person to keep intervening.

  * “fewest number of steps” and “Google-recommended practices” together form an exclusion cue favoring Kubernetes’ built-in, declarative self-healing feature over custom external automation.

**Why This Is Correct**

An HTTP liveness probe lets the kubelet periodically check whether a container is still healthy; once the probe starts failing, Kubernetes automatically restarts that container. This matches the documented pattern for long-running processes that work correctly at first but degrade after running for a while and need a periodic restart to keep functioning. Configuring the probe is a single, declarative addition to the existing Deployment’s Pod spec, requiring no new resources, no custom scripts, and no ongoing human attention — giving the service a self-healing cycle that can run unattended for the month it takes the development team to ship the real fix.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** a scheduled job that finds and deletes Pods older than five hours can produce a similar outcome, but it duplicates functionality Kubernetes already provides natively through liveness probes, and it means building and maintaining a separate resource with its own logic and permissions — more steps than the built-in mechanism requires.

**Option C — Incorrect:** manually watching Pods and terminating them is pure human toil that doesn’t scale, and it directly conflicts with both “fewest number of steps” and the month-long duration this workaround would need to survive unattended.

**Option D — Incorrect:** an alert only notifies that the problem occurred; it doesn’t restart anything or restore the Pod to a healthy state, so on its own it doesn’t “ensure continued operations” — someone would still have to manually act on every alert for a month.

**Exam Trap**

The trap is reaching for custom automation, like a scheduled job, or for observability, like an alert, as if either were a complete fix, when Kubernetes already has a built-in, declarative mechanism purpose-built for “a container that degrades after running for a while and needs a restart.” Any option that adds infrastructure Kubernetes doesn’t require, or that only reports on the problem instead of fixing it, misses what “fewest steps” and “Google-recommended practice” are pointing at here.

**Foundation Concept**

Kubernetes’ self-healing model relies on probes to decide when a container needs to be restarted, rather than requiring external tooling to watch and intervene. A liveness probe is specifically designed for processes that run fine initially but can enter a broken state over time, since it keeps checking the container’s health on an ongoing basis and lets the kubelet act the moment the probe starts failing, with no outside system required.

**Real-World Connection**

A team discovers that one of their services develops a slow memory leak and starts returning errors after running for several hours, with a proper fix still weeks away. Adding a liveness probe against a simple health endpoint lets Kubernetes automatically cycle affected Pods before users are impacted, buying the team time to ship the real fix without anyone having to babysit the cluster or build throwaway automation in the meantime.

**Memory Hook**

“A container that breaks after a while needs a liveness probe, not a babysitter or a timer job.”

**30-Second Exam Takeaway**

When a GKE Pod reliably becomes unhealthy after running for a while and a permanent fix is still some time away, the Google-recommended, fewest-steps answer is almost always an HTTP liveness probe — it lets Kubernetes restart the Pod automatically rather than relying on custom jobs, manual monitoring, or alerts that only report the problem.

**Official References**

[**Kubernetes documentation — Configure Liveness, Readiness and Startup Probes:**](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) Supports: correct-answer mechanism — liveness probes automatically restarting containers that become unhealthy after running for a while

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 3.3, Mitigating incident impact on users):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment — keeping a service operating while a known issue’s root cause is still being resolved

</details>

---

### Exam 4 · Q55

Your team is building a service that runs compute-intensive processing on batches of data, where processing speed depends directly on the number and speed of CPUs available. These batches vary in size and can arrive at any time from several third-party sources, which need a secure way to upload their data. You want to keep costs as low as possible while still processing each batch as quickly as possible. What should you do?

- A. Stand up a secure file transfer protocol (SFTP) server on a Compute Engine instance for third parties to upload their batches to, and issue them the appropriate credentials. Create a Cloud Run function with a Cloud Storage trigger on the object-finalized event, and have that function scale up a Compute Engine autoscaling managed instance group. Use an instance image pre-loaded with the processing software that terminates its instances once processing finishes.
- B. Provide a Cloud Storage bucket for third parties to upload their batches to, with Identity and Access Management (IAM) access granted appropriately. Run a Standard Google Kubernetes Engine (GKE) cluster with two services: one that processes the batches and another that watches Cloud Storage for new batches. Stop the processing service whenever there are no batches left to process.
- C. Provide a Cloud Storage bucket for third parties to upload their batches to, with Identity and Access Management (IAM) access granted appropriately. Create a Cloud Run function with a Cloud Storage trigger on the object-finalized event, and have that function scale up a Compute Engine autoscaling managed instance group. Use an instance image pre-loaded with the processing software that terminates its instances once processing finishes.
- D. Provide a Cloud Storage bucket for third parties to upload their batches to, with Identity and Access Management (IAM) access granted appropriately. Use Cloud Monitoring to detect new batches landing in the bucket and have it trigger a Cloud Run function that processes the data directly. Configure that Cloud Run function to use the largest available CPU allocation to minimize its runtime.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Provide a Cloud Storage bucket for third parties to upload their batches to, with Identity and Access Management (IAM) access granted appropriately. Create a Cloud Run function with a Cloud Storage trigger on the object-finalized event, and have that function scale up a Compute Engine autoscaling managed instance group. Use an instance image pre-loaded with the processing software that terminates its instances once processing finishes.

**Correct Answer**

**C. Provide a Cloud Storage bucket for third parties to upload their batches to, with Identity and Access Management (IAM) access granted appropriately. Create a Cloud Run function with a Cloud Storage trigger on the object-finalized event, and have that function scale up a Compute Engine autoscaling managed instance group. Use an instance image pre-loaded with the processing software that terminates its instances once processing finishes.**

**Exam Reasoning Explanation**

The must-have constraints are a secure, low-overhead upload path for outside parties, processing that scales with CPU count and speed, triggering that reacts instantly to unpredictable arrivals, and compute that doesn’t cost anything once the work is done. Walking the chain: requirement (secure upload + CPU-scalable processing + fast reaction + minimal cost) → capability (Cloud Storage with IAM gives secure, serverless uploads; an object-finalized trigger reacts the instant a batch lands; a Compute Engine autoscaling group lets the heavy lifting run on machines sized for real CPU needs; a self-terminating image stops billing once processing ends) → elimination (A adds an unnecessary self-managed SFTP server, B keeps a cluster and a polling service running even when idle, D does the heavy compute inside a resource-capped function and detects uploads indirectly through Monitoring) → decision (C is the only path where every piece matches a stated requirement without adding overhead the scenario didn’t ask for).

**Key Exam Clues**

  * “processed faster based on the speed and number of CPUs” is a technical signal that the heavy computation needs to run on infrastructure you can size with CPUs, not inside a resource-capped serverless function.

  * “vary in size and may arrive at any time” favors an event-driven trigger that reacts the instant a batch appears, over a scheduled or polling-based detection mechanism.

  * “upload their data securely” points toward a native, access-controlled Google Cloud storage destination rather than a self-managed server that has to be secured and maintained.

  * “minimize costs, while... processed as quickly as possible” is a dual constraint requiring both an instant trigger and compute that doesn’t sit running, or idle, once the work is finished.

**Why This Is Correct**

A Cloud Storage bucket with IAM gives third parties a secure, access-controlled upload destination with nothing to patch or operate. The object-finalized Cloud Storage trigger fires a lightweight Cloud Run function the instant an upload completes, with no polling delay, and that function’s only job is to scale up a Compute Engine autoscaling managed instance group — handing the actual compute-heavy work to machines that can be sized with as many, or as fast, CPUs as the workload needs. Because the instance image is pre-loaded with the processing software and configured to terminate once processing completes, the project pays for compute only while a batch is actively being processed, which minimizes cost while keeping the time from “upload finishes” to “processing starts” as short as possible.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** standing up a self-managed SFTP server on a Compute Engine instance means an always-running machine that has to be secured, patched, and paid for continuously, when Cloud Storage with IAM already provides a secure, serverless upload path at lower operational cost and overhead — the rest of the path is identical to the correct answer, so this is purely a worse choice for the upload step.

**Option B — Technically Possible but Not Best:** a Standard GKE cluster running two always-on services — one processing, one watching Cloud Storage — keeps compute (and a polling loop) running even when there’s nothing to process. Stopping the processing service when idle still requires something to be continuously watching and deciding that, which is less efficient and less immediate than a native, push-based event trigger, and it doesn’t scale compute to match genuinely CPU-heavy, variable-sized batches the way a right-sized Compute Engine group can.

**Option D — Violates Requirement:** performing the compute-heavy processing inside the Cloud Run function itself, even with its largest CPU setting, ignores the stated requirement that speed depends on “the number and speed of CPUs on the machine” — serverless functions have bounded CPU and memory ceilings well below what a purpose-sized Compute Engine machine can offer. Using Cloud Monitoring to detect new uploads is also an indirect, less immediate substitute for the native Cloud Storage event trigger used in the correct path.

**Exam Trap**

The trap is assuming any combination of a Cloud Storage bucket with a Cloud Run function is equally good, without checking where the actual heavy computation happens. A function that does the processing itself — even dialed up to its largest CPU allocation — is still bounded by serverless compute ceilings, so it fails a requirement explicitly tied to CPU count and speed. The correct pattern uses the function only as a lightweight trigger that hands off to appropriately sized Compute Engine capacity, never as the processor itself.

**Foundation Concept**

Event-driven architectures separate “detecting that work has arrived” from “doing the work.” A lightweight, serverless function is well suited to the first job — reacting instantly to a storage event — but a compute-heavy workload belongs on infrastructure that can be sized to the job and that scales down to zero cost once the job is done, which is exactly what an autoscaling managed instance group paired with a self-terminating image provides.

**Real-World Connection**

A media-processing service lets outside partners drop large video files into a Cloud Storage bucket; the moment an upload finishes, a lightweight Cloud Run function fires and resizes a Compute Engine instance group to match the batch, with each VM pre-loaded to start transcoding immediately and shut itself down once its job is done. Partners get a simple, secure upload target, transcoding starts within seconds of the upload completing rather than on the next polling cycle, and the team’s bill reflects only the minutes of actual transcoding rather than a cluster or server running around the clock.

**Memory Hook**

“Let the trigger be tiny; let the compute be big — and let the big compute turn itself off.”

**30-Second Exam Takeaway**

For compute-heavy, event-driven batch work with unpredictable arrival, look for the pattern of a lightweight serverless trigger (never doing the heavy lifting itself) handing off to right-sized, autoscaling Compute Engine capacity that terminates when finished — that combination is what actually minimizes processing latency and cost together.

**Official References**

[**Google Cloud — Cloud Storage triggers for Cloud Run functions:**](https://cloud.google.com/functions/docs/calling/storage)Supports: correct-answer mechanism — reacting to the object-finalized event the instant an upload completes

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 3.2, Managing service lifecycle):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment — autoscaling with managed instance groups as part of service lifecycle management

</details>

---

### Exam 4 · Q57

You’ve deployed a stateless application, running as multiple pods at once, on a large Standard Google Kubernetes Engine (GKE) cluster. Traffic to the application is unpredictable, and you need the user experience to stay consistent through those traffic swings while also keeping the cluster’s resource usage efficient. What should you do?

- A. Set up a cron job that scales the deployment on a fixed schedule
- B. Set up a Horizontal Pod Autoscaler for the deployment
- C. Set up a Vertical Pod Autoscaler for the deployment
- D. Enable cluster autoscaling on the node pool

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Set up a Horizontal Pod Autoscaler for the deployment

**Correct Answer**

**B. Set up a Horizontal Pod Autoscaler for the deployment**

**Exam Reasoning Explanation**

The must-have constraint is that the mechanism has to react to actual, unpredictable traffic in real time, while also avoiding wasted capacity — a schedule-based or slow-to-react approach fails the first half, and anything that doesn’t change how much capacity is actually running fails the second. Walking the chain: requirement (keep performance steady under unpredictable load while staying resource-efficient) → capability (the Horizontal Pod Autoscaler continuously tracks live demand signals and adjusts replica count to match) → elimination (A follows a fixed schedule unrelated to real traffic, C reacts too slowly and disruptively for inconsistent load, D only reacts to pod-scheduling pressure that something else has to create first) → decision (B is the single mechanism that directly and continuously ties pod capacity to actual demand).

**Key Exam Clues**

  * “inconsistent traffic” is a hard constraint that rules out any schedule-based approach, since a fixed timetable can’t track unpredictable demand.

  * “stateless... multiple pods run at the same time” is a technical signal that the workload is naturally suited to horizontal (replica-count) scaling rather than resizing individual pods.

  * “user experience... stay consistent” paired with “resource usage... efficient” is a dual requirement: the right mechanism must add capacity under load and shed it when load drops, in the same motion.

**Why This Is Correct**

The Horizontal Pod Autoscaler watches real-time signals such as CPU or memory utilization, or custom and external metrics tied to actual demand like request rate, and adjusts the deployment’s pod replica count accordingly. Adding pods as traffic rises keeps response times and throughput steady for users, while removing pods as traffic falls stops the deployment from holding capacity it no longer needs. Because this responds continuously to the live traffic pattern rather than a predetermined timetable, and operates at exactly the layer that fits a stateless, horizontally scalable application, it’s the mechanism built for this combination of unpredictable load and resource efficiency.

**Why the Other Options Are Not the Best Fit**

**Option A — Incorrect:** a cron job scales on a fixed schedule, which has no way to track traffic that is genuinely inconsistent; the deployment could easily be over-provisioned during a scheduled-up window with little actual demand, or under-provisioned during a scheduled-down window that happens to see a spike, directly undermining a consistent user experience.

**Option C — Different Use Case:** the Vertical Pod Autoscaler adjusts a pod’s own CPU and memory requests and limits based on observed usage over time, which suits workloads with predictable, steadily trending resource needs rather than fast, unpredictable swings. Applying a new recommendation typically requires evicting and recreating the pod, so it reacts too slowly and disruptively for inconsistent traffic, and Google’s own guidance cautions against running it together with the Horizontal Pod Autoscaler on the same resource dimension.

**Option D — Technically Possible but Not Best:** cluster autoscaling adds or removes nodes in response to pods that can’t be scheduled due to insufficient node capacity, which is a valuable complement once something else is changing how many pods need to run. On its own, with a fixed pod count, it has nothing to react to as traffic changes, so by itself it cannot keep the user experience consistent as load fluctuates.

**Exam Trap**

The trap is reading “optimize cluster resource usage” as a cue to reach for cluster-level autoscaling (option D) rather than recognizing that right-sizing the pod replica count is itself what prevents wasted resources at this layer — cluster autoscaling only has something to act on once pod-level scaling, like the Horizontal Pod Autoscaler, changes the demand for nodes. If the scenario instead described pods failing to schedule because a fixed replica count occasionally can’t fit on the available nodes, cluster autoscaling would become directly relevant in its own right.

**Foundation Concept**

Kubernetes offers scaling at different layers for different needs: horizontal scaling changes how many replicas of a stateless workload are running to track changing demand, vertical scaling changes how much CPU and memory a single pod is allocated to match its own resource profile, and cluster-level scaling changes how many nodes exist to host whatever pods are currently scheduled. A stateless application facing unpredictable traffic is the textbook case for horizontal scaling, because adding and removing identical replicas is faster and safer than resizing or rescheduling individual pods.

**Real-World Connection**

A retail team’s stateless checkout service sees large, unpredictable traffic swings around promotions and social-media mentions. Configuring a Horizontal Pod Autoscaler against request-based metrics lets the deployment automatically grow from a handful of replicas to dozens during a surge and shrink back afterward, keeping checkout latency steady for shoppers during the spike while freeing up capacity, and the cost that comes with it, once traffic subsides — without anyone having to predict the next surge in advance.

**Memory Hook**

“Unpredictable traffic, stateless pods: scale the replica count, not the schedule or the pod’s own size.”

**30-Second Exam Takeaway**

When a stateless, horizontally scalable GKE workload faces unpredictable traffic and the goal is both consistent performance and efficient resource use, reach for the Horizontal Pod Autoscaler first — it’s the mechanism built to react to live demand at the replica-count layer, with the Vertical Pod Autoscaler and cluster autoscaling serving more specialized or complementary roles.

**Official References**

[**Google Cloud — Horizontal Pod autoscaling in GKE:**](https://cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) Supports: correct-answer mechanism — reacting to real-time resource/demand signals by adjusting replica count, and why it isn’t combined with VPA on the same resource dimension

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 3.2, Managing service lifecycle):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment — autoscaling (including GKE) as part of service lifecycle management

</details>

---

### Exam 5 · Q6

**You're on-call for an infrastructure service with numerous dependent systems. An alert notifies you of widespread failure in serving requests, impacting all dependent systems with hundreds of thousands of users. Following Site Reliability Engineering (SRE) incident management protocols, you designate yourself as Incident Commander (IC) and assign two experienced team members as Operations Lead (OL) and Communications Lead (CL). What's your immediate next step?**

- I. Initiate actions to mitigate user impact and implement the mitigations in production.
- II. Contact the owners of the affected services and keep them informed about the incident status.
- III. Establish a dedicated communication channel for incident responders and leads to ensure seamless coordination.
- IV. Begin a postmortem process, incorporating incident details, share the draft internally, and solicit input from internal stakeholders.#

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Establish a dedicated communication channel for incident responders and leads to ensure seamless coordination.

**Correct option: III**

**Why option III is correct**

**III. Establish a dedicated communication channel for incident responders and leads to ensure seamless coordination.**

Under **Google SRE incident management** , once an incident is declared and roles are assigned (IC, Operations Lead, Communications Lead), the **very next step** is to **create a single, dedicated communication channel** (for example, a Slack channel or conference bridge).

Core SRE fundamentals behind this step:

  * **Single source of truth:** All responders coordinate in one place, avoiding fragmented updates across emails, chats, or calls.

  * **Clear command structure:** The IC can direct actions efficiently, the OL can report mitigation progress, and the CL can prepare consistent external/internal updates.

  * **Reduced cognitive load:** Responders focus on fixing the issue rather than tracking scattered communications.

  * **Scalability:** As more responders join, they can quickly get context without interrupting mitigation work.

Google SRE explicitly defines this as an _early, mandatory step_ before mitigation actions begin.

**Authoritative documentation:**  
<https://sre.google/sre-book/managing-incidents/>

**Why the other options are not correct**

**I. Initiate actions to mitigate user impact immediately.**  
Mitigation is critical, but acting _before_ establishing a coordination channel leads to duplicated effort, missed context, and confusion—especially in large, multi-team incidents.

**II. Contact owners of affected services right away.**  
Stakeholder communication is important, but it is the responsibility of the **Communications Lead** _after_ coordination mechanisms are in place.

**IV. Begin a postmortem process.**  
Postmortems occur **after incident resolution** , not during active response.

**Final answer:** **III**

</details>

---

### Exam 5 · Q11

**In line with Site Reliability Engineering principles, you're drafting a postmortem for an incident triggered by a software change that significantly impacted users. How can you prevent similar severe incidents in the future?**

- I. Hold the engineers involved accountable and escalate the issue to their senior management.
- II. Ensure that test cases detecting errors of this nature are successfully executed before every new software release.
- III. Conduct follow-up discussions with personnel responsible for reviewing the changes, prescribing best practices for future implementations.
- IV. Implement a policy mandating immediate engagement of on-call teams to convene engineers and management for prompt incident resolution planning.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Ensure that test cases detecting errors of this nature are successfully executed before every new software release.

**Best Option:**

**II. Ensure that test cases detecting errors of this nature are successfully executed before every new software release.** This approach directly targets the root cause and promotes proactive issue prevention.

**Reasoning:**

**Preventing Recurrence:** By focusing on testing, you establish a robust barrier to prevent similar errors from reaching production and impacting users.

**SRE Alignment:** Thorough testing is a core element of SRE, emphasizing a proactive approach to reliability.

**Tangible Improvement:** This action item leads to concrete changes in your development and release processes.

**Why Others Are Less Optimal:**

**I. Hold the engineers involved accountable ...** While understanding the causes is important, focusing solely on accountability fosters a blame culture, which is counterproductive for long-term improvement and contradicts SRE principles.

**III. Conduct follow-up discussions ...** Postmortem discussions are vital for learning from the incident, but they are not a direct preventive measure against future similar failures.

**IV. Implement a policy mandating immediate engagement ...** While incident response speed is crucial, the policy doesn't address the root cause of the issue, making it less effective in preventing similar incidents.

**Important Considerations**

While improving test coverage is a top priority, consider these additional SRE-aligned actions:

**Blameless Culture:** Promote a culture where errors are seen as opportunities for learning and improvement. This encourages open communication and problem-solving rather than fear.

**Code Review:** Strengthen code review processes to enhance the identification of potential issues before deployment.

**Chaos Engineering:** Experiment with deliberate disruptions in testing or staging environments to uncover hidden vulnerabilities and build resilience.

</details>

---

### Exam 5 · Q12

**Your team has recently deployed an NGINX-based application into Google Kubernetes Engine (GKE) and has exposed it to the public via an HTTP Google Cloud Load Balancer (GCLB) ingress.**

**You want to scale the deployment of the application's frontend using an appropriate Service Level Indicator (SLI).**

**What should you do?**

- **A.** Configure the **horizontal pod autoscaler** to use the **average response time** from the **Liveness and Readiness probes**.
- **B.** Configure the **vertical pod autoscaler in GKE** and enable the **cluster autoscaler** to scale the cluster as pods expand.
- **C.** **Install the Cloud Monitoring (formerly Stackdriver) custom metrics adapter** and configure a **horizontal pod autoscaler (HPA) to use the number of requests** provided by the **Google Cloud Load Balancer (GCLB)**.
- **D.** Expose the **NGINX stats endpoint** and configure the **horizontal pod autoscaler** to use the **request metrics** exposed by the **NGINX deployment**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** **C.** **Install the Cloud Monitoring (formerly Stackdriver) custom metrics adapter** and configure a **horizontal pod autoscaler (HPA) to use the number of requests** provided by the **Google Cloud Load Balancer (GCLB)**.

**Correct Answer:**

**C.** **Install the Cloud Monitoring (formerly Stackdriver) custom metrics adapter** and configure a **horizontal pod autoscaler (HPA) to use the number of requests** provided by the **Google Cloud Load Balancer (GCLB)**.

**Explanation:**

  * **Horizontal Pod Autoscaler (HPA) is the best approach for scaling stateless applications** like **NGINX-based frontends** based on real traffic metrics.

  * **Google Cloud Load Balancer (GCLB) provides HTTP request count metrics** , which are **more relevant SLIs** for scaling than CPU/memory alone.

  * The **Cloud Monitoring custom metrics adapter** enables **HPA to use external HTTP request rate metrics** from GCLB, ensuring **demand-based autoscaling**.

**Why Other Options Are Incorrect:**

**A. Using Liveness and Readiness probe response times for HPA** –

  * Liveness and readiness probes are **used for health checks** , not for **measuring real traffic load**.

  * Response time **does not accurately represent the need for scaling**.

**B. Using Vertical Pod Autoscaler (VPA) and Cluster Autoscaler** –

  * **VPA optimizes individual pod resource allocation** , **not the number of replicas**.

  * **Cluster Autoscaler only adjusts node counts** , which is **not sufficient** for handling increasing request loads dynamically.

**D. Using the NGINX stats endpoint for autoscaling** –

  * While **NGINX exposes request metrics** , these **are not natively integrated with Cloud Monitoring or HPA**.

  * **GCLB already provides request count metrics** in **Cloud Monitoring** , making it **a better choice**.

**Recommended Approach:**

  1. **Install the Cloud Monitoring custom metrics adapter for Kubernetes**  
[ Cloud Monitoring Custom Metrics Adapter](https://cloud.google.com/monitoring/custom-metrics/creating-metrics)

  2. **Use GCLB's HTTP request metrics for autoscaling**  
[ Autoscaling with External HTTP Request Metrics](https://cloud.google.com/kubernetes-engine/docs/concepts/custom-and-external-metrics)

  3. **Configure the HPA to use request count per second from GCLB**  
[ Scaling Workloads with HPA](https://cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling)

</details>

---

### Exam 5 · Q15

**You support a web application hosted on Compute Engine that provides a booking service for thousands of users.**

**Shortly after the release of a new feature, your monitoring dashboard shows that all users are experiencing latency at login.**

**You want to mitigate the impact of the incident on the users of your service.**

**What should you do first?**

- **A. Roll back the recent release.**
- **B. Review Cloud Monitoring.**
- **C. Upsize the virtual machines running the login services.**
- **D. Deploy a new release to see whether it fixes the problem.**

<details><summary>Answer &amp; explanation</summary>

**Correct:** **A. Roll back the recent release.**

**Correct Answer:**

**A. Roll back the recent release.**

**Explanation:**

  * The **latency issue started immediately after the new release** , indicating that the **new deployment is likely the root cause**.

  * The **fastest and safest way to mitigate impact** is to **roll back to the previous stable version** while investigating the issue.

  * This follows **Site Reliability Engineering (SRE) best practices** , where a rollback is the **primary mitigation strategy** for post-release incidents.

**Why Other Options Are Incorrect:**

**B. Reviewing Cloud Monitoring logs before rolling back** –

  * While **Cloud Monitoring helps diagnose the issue** , **it does not mitigate user impact immediately**.

  * **Rollback first** to reduce user disruption, then analyze the cause.

**C. Upsizing VMs running the login service** –

  * **Scaling resources does not fix application-level issues**.

  * If the new release introduced **inefficient code or database locks** , **increasing VM size won't resolve the root cause**.

**D. Deploying another release without investigation** –

  * **This is risky** because it might **worsen the issue** or introduce new bugs.

  * **Rollback first** , verify the issue is resolved, then debug and prepare a **proper fix** for a future deployment.

**Recommended Approach:**

  1. **Rollback to the last stable release immediately** to restore service availability.

  2. **Investigate logs in Cloud Logging & Monitoring** to find the root cause.

  3. **Run a post-mortem** to ensure the issue is resolved before the next deployment.

  4. **Test the fix in a staging environment** before rolling out again.

**Reference Documentation:**

[ Google SRE Handbook: Managing Incidents](https://sre.google/resources/practices-and-processes/anatomy-of-an-incident/)  
[ Rolling Back Deployments on Compute Engine](https://cloud.google.com/deploy/docs/roll-back)

</details>

---

### Exam 5 · Q17

**You provide support for a large service with a clearly defined Service Level Objective (SLO). The development team frequently deploys new releases of the service each week. In the event of a significant incident causing the service to miss its SLO, you aim for the development team to pivot their focus from feature development to enhancing service reliability. What action should you take proactively before a major incident arises?**

- I. Collaborate with all service stakeholders to formulate an appropriate error budget policy.
- II. Advocate for prioritizing service reliability over introducing new features in discussions with the product team.
- III. Discuss with the development team to potentially reduce the frequency of releases to once a week or less.
- IV. Implement a plugin within your Jenkins pipeline to halt new releases when the service is out of compliance with its SLO.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Collaborate with all service stakeholders to formulate an appropriate error budget policy.

**I. Collaborate with all service stakeholders to formulate an appropriate error budget policy.**

Let's break down why this is the most effective starting point:

  * **Shared Responsibility:** An error budget policy creates a framework for making decisions around reliability vs. feature development. It aligns stakeholders (development, product, operations) on priorities.

  * **Proactive:** Establishes a clear mechanism for when to shift focus _before_ a major incident disrupts the service.

  * **Data-Driven:** Error budgets are based on your SLO. They translate a reliability goal into tangible terms that everyone can understand.

**Why Other Options Are Less Ideal (Initially):**

  * **II. Advocate for prioritizing service reliability ...** While important, a general prioritization doesn't provide the same specific guidance or shared understanding as an error budget policy.

  * **III. Discuss with the development team ...** Slowing down releases might be a consequence of an error budget policy, but it's a blunt instrument and could hinder necessary fixes or improvements.

  * **IV. Implement a plugin within your Jenkins pipeline ...** Halting releases automatically can be a tool to enforce an error budget policy, but the policy itself needs to be defined first.

**Important Considerations**

  * **Communication:** An error budget policy is only effective if well-communicated and agreed upon across the organization.

  * **Review and Adjust:** The error budget should be reviewed periodically and adjusted based on changing business needs and service performance.

**Reference:**

<https://sre.google/workbook/error-budget-policy/>

</details>

---

### Exam 5 · Q20

**As you craft and allocate action items in a postmortem following an outage, your goal is to efficiently address the root causes. Although the outage has concluded, it's vital to swiftly tackle the action items. How should you designate owners and collaborators for these action items?**

- I. Assign a single owner for each action item, along with any necessary collaborators.
- II. Allocate multiple owners for each item to expedite the team's response.
- III. Assign collaborators to the items without designating individual owners to maintain a blameless postmortem approach.
- IV. Designate the team lead as the owner for all action items, given their oversight of the SRE team.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Assign a single owner for each action item, along with any necessary collaborators.

**I. Assign a single owner for each action item, along with any necessary collaborators.**

**Justification:**

  * **Clarity & Accountability:** A single owner ensures there's no confusion about who is ultimately responsible for driving the action item to completion.

  * **Collaboration:** Collaborators provide support, expertise, and diverse perspectives while maintaining accountability with the designated owner.

  * **Urgency:** Given the need for swift action, having clear ownership fosters a sense of responsibility and helps prioritize tasks.

**Why Other Options Are Less Suitable:**

  * **II. Allocate multiple owners for each item...** While well-intentioned, multiple owners can lead to diffusion of responsibility and potential delays if it's unclear who's driving the resolution.

  * **III. Assign collaborators to the items without designating individual owners...** Collaboration is vital, but without clear ownership, tasks risk falling through the cracks or lacking the necessary drive for quick resolution.

  * **IV. Designate the team lead as the owner for all action items...** This places too much burden on the team lead and may not leverage the specific expertise of other team members who are better suited to own individual action items.

**References:**  
<https://sre.google/sre-book/example-postmortem/>

<https://devops.com/when-it-disaster-strikes-part-3-conducting-a-blameless-post-mortem/>

</details>

---

### Exam 5 · Q23

**As a member of a global organization managing a service with a 99% availability target and limited engineering resources, you've noted a 99.5% availability for the current month. To meet the set availability objectives, adapt to business changes, including forthcoming feature launches, and diminish technical debt while minimizing operational expenses, which Google-endorsed approach should take precedence?**

- I. Bolster service resilience by implementing N+1 redundancy through the incorporation of extra computing resources.
- II. Streamline operations by identifying, quantifying, and automating repetitive tasks to eradicate unnecessary manual effort.
- III. Establish an error budget for service-level availability and actively work to reduce any remaining errors.
- IV. Assign available engineers to feature backlog development, ensuring adherence to the availability target.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Streamline operations by identifying, quantifying, and automating repetitive tasks to eradicate unnecessary manual effort.

**The Priority:**

**II. Streamline operations by identifying, quantifying, and automating repetitive tasks to eradicate unnecessary manual effort.**

**Why this takes precedence:**

  * **Efficiency Optimization:** Google's Site Reliability Engineering (SRE) philosophy prioritizes efficient use of available resources. Automating manual processes reduces the potential for human error and frees up engineers for higher-value tasks.

  * **Addressing Root Issues:** Manual operations are a common source of delays and errors. Automation tackles these problems at their core, leading to inherent reliability improvements.

  * **Resource Maximization:** Reducing manual work allows your limited engineers to focus on proactive improvements, new features, and reducing technical debt, all leading to a better service.

  * **Cost-effectiveness:** Operational streamlining through automation often leads to significant cost savings.

**Why Others are Less Ideal:**

  * **I. Bolster service resilience by implementing N+1 redundancy...** Redundancy is valuable but can be expensive. It doesn't address existing operational inefficiencies, which could still lead to outages.

  * **III. Establish an error budget...** Error budgets are an important SRE tool, but a sole focus on reduction might discourage necessary development work and innovation.

  * **IV. Assign available engineers to feature backlog development...** Features are important, but a service that fails to meet its availability targets due to operational problems won't be useful, regardless of feature additions.

</details>

---

### Exam 5 · Q32

**In preparation for deploying a new service to production, you aim to achieve automatic scalability across multiple regions using a managed instance group. This service requires significant resources per instance, necessitating meticulous capacity planning. What actions should you take?**

- I. Evaluate Cloud Trace insights to determine the most effective resource sizing strategy for the service.
- II. Specify the n2-highcpu-96 machine type within the managed instance group configuration to accommodate the service's resource requirements adequately.
- III. Implement deployment across multiple regions and utilize an internal load balancer to efficiently manage traffic distribution.
- IV. Validate that the resource demands align with the available project quota limits in each region before initiating deployment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Validate that the resource demands align with the available project quota limits in each region before initiating deployment.

**Correct option: IV**

**Why option IV is correct**

**IV. Validate that the resource demands align with the available project quota limits in each region before initiating deployment.**

When deploying a **multi-region managed instance group (MIG)** for a **resource-intensive service** , the most critical prerequisite is **quota validation**.

Core infrastructure fundamentals behind this choice:

  * **Managed instance groups scale automatically** , but **scaling is hard-blocked by quotas** (vCPU, CPU families, memory, IP addresses, regional limits).

  * For **large machine types** and **multi-region deployments** , quota exhaustion is one of the **most common production blockers** , even when configuration is correct.

  * **Capacity planning in Google Cloud is quota-driven**. If quotas are insufficient in _any_ target region, autoscaling will fail silently or partially, breaking availability guarantees.

  * Google explicitly recommends **verifying and increasing quotas before production rollout** , especially for high-resource workloads.

This step ensures:

  * Predictable autoscaling behavior

  * No partial regional failures

  * No last-minute deployment blockers

**Why the other options are not suitable**

**I. Evaluate Cloud Trace insights for resource sizing.**  
Cloud Trace is for **latency analysis and request tracing** , not for determining instance sizing or capacity planning.

**II. Specify a large machine type (n2-highcpu-96).**  
Selecting a machine type alone does not ensure availability. Without confirming **regional quota capacity** , instances may fail to launch entirely.

**III. Deploy across multiple regions using an internal load balancer.**  
Internal load balancers are **regional** , not global. They cannot distribute traffic across regions and are inappropriate for multi-region production access.

**Final answer:** **IV**

</details>

---

### Exam 5 · Q36

**You're tasked with establishing a Cloud Monitoring SLO for an upcoming service launch, aiming to ensure that requests are handled within 300 ms for at least 90% of the time per calendar month. How should you select the metric and evaluation method to meet this objective?**

- I. Opt for a latency metric using a request-based evaluation approach.
- II. Opt for a latency metric using a window-based evaluation approach.
- III. Opt for an availability metric using a request-based evaluation approach.
- IV. Opt for an availability metric using a window-based evaluation approach.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Opt for a latency metric using a request-based evaluation approach.

**Correct Option:**

  * **I. Opt for a latency metric using a request-based evaluation approach.**

**Justification:**

  * **Matches the SLO Requirement:** Directly aligns with the performance goal of requests being handled within 300 ms.

  * **Focus on User Experience:** Request-based evaluation emphasizes the individual user experience with each request, ensuring a majority of users see acceptable performance.

  * **Typical for Latency SLOs:** This combination is commonly used for latency-based SLOs.

**Why Other Options Are Less Suitable:**

  * **II. Opt for a latency metric using a window-based evaluation approach.**

    * **Less User-Centric:** While relevant, window-based SLOs can mask significant latency issues within short time periods, potentially not reflecting the actual user experience.

  * **III. Opt for an availability metric using a request-based evaluation approach.**

    * **Measures a Different Aspect:** Availability deals with whether a service can respond at all, not how fast it responds. It wouldn't accurately measure the desired 300ms performance.

  * **IV. Opt for an availability metric using a window-based evaluation approach.**

    * **Even Less Granular:** This combines the wrong metric type (availability) with the less user-centric evaluation (window-based).

**References:**

<https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring#slo-type-request>

<https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring#slo-types>

</details>

---

### Exam 5 · Q44

**You manage a service with a well-defined Service Level Objective (SLO) that has consistently been achieved for the past 6 months, resulting in high customer satisfaction. With most operational tasks automated and only a few repetitive tasks occurring frequently, you aim to optimize the balance between reliability and deployment velocity while adhering to site reliability engineering best practices. What steps should you take? (Select two.)**

- I. Consider tightening the service's SLO criteria.
- II. Potentially accelerate the service's deployment velocity and/or risk profile.
- III. Allocate engineering resources to other services requiring greater reliability.
- IV. Collaborate with the product team to prioritize reliability improvements over new features.
- V. Adjust the implementation of your Service Level Indicators (SLIs) to broaden coverage.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Potentially accelerate the service's deployment velocity and/or risk profile. **|** III. Allocate engineering resources to other services requiring greater reliability.

**The two best steps for this scenario are:**

  * **II. Potentially accelerate the service's deployment velocity and/or risk profile.** Your service's track record demonstrates the ability to maintain a reliable SLO. This allows for experimentation with quicker iterations and potentially more complex changes to boost innovation.

  * **III. Allocate engineering resources to other services requiring greater reliability.** Capitalize on your current service's success by shifting resources to areas that need attention. This promotes a balanced and efficient approach across your systems.

**Why these options are the most suitable:**

  * **Utilizing Success:** Your service's reliability creates space for focusing efforts on other areas or pushing for greater feature development velocity.

  * **SRE Alignment:** This approach aligns with SRE principles by allocating resources strategically across systems to maximize overall user experience.

**Why other options are less ideal:**

  * **I. Consider tightening the service's SLO criteria.** While a possibility, it might be unnecessary given the consistent success and could even introduce undue pressure.

  * **IV. Collaborate with the product team to prioritize reliability improvements over new features.** With the current service already performing well, this might unnecessarily stifle product development.

  * **V. Adjust the implementation of your Service Level Indicators (SLIs) to broaden coverage.** While always beneficial to improve monitoring, it doesn't directly address the opportunity to balance reliability and velocity.

**Reference:**

<https://sre.google/workbook/implementing-slos/#slo-decision-matrix>

</details>

---

### Exam 5 · Q46

**Your organization aims to elevate the availability target of an application from 99.9% to 99.99% with a $2,000 investment. The current revenue generated by the application is $1,000,000. You need to assess whether the increased availability justifies the investment for a single year of usage. What should you do?**

- I. Evaluate the value of enhanced availability at $900 and conclude that the investment is not justified.
- II. Assess the value of enhanced availability at $1,000 and conclude that the investment is not justified.
- III. Determine the value of enhanced availability at $1,000 and conclude that the investment is justified.
- IV. Calculate the value of enhanced availability at $9,000 and conclude that the investment is justified.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Evaluate the value of enhanced availability at $900 and conclude that the investment is not justified.

**Correct choice — I. “Evaluate the value of enhanced availability at $900 and conclude that the investment is not justified.”**

**Why option I is correct**

  1. **How many outage hours are removed?**

     * 99.9 % (“three-nines”) permits ≈ 8 h 45 m 57 s of downtime per year. [uptime.is](https://uptime.is/)

     * 99.99 % (“four-nines”) permits ≈ 52 m 36 s of downtime per year. [uptime.is](https://uptime.is/99.99)

     * Δ downtime = 8.76 h − 0.876 h ≈ 7.884 h saved.

  2. **How much money does that save?**

     * Annual revenue = $1 000 000.

     * Revenue/hour = $1 000 000 ÷ 8 760 h ≈ $114.16 per hour.

     * Value of avoided downtime = 7.884 h × $114.16 ≈ **$900**.

  3. **Compare benefit to cost.**

     * Benefit ≈ $900 / year < Cost = $2 000 / year → financially **unfavorable**.

Therefore option I, which identifies the benefit as $900 and rejects the $2 000 spend, matches the calculation.

**Why the other options are wrong**

  * **II. “Assess the value at $1 000 and conclude the investment is not justified.”**

    * The conclusion (not justified) is fine, but the _benefit figure_ is wrong. Correct math gives ≈ $900, not $1 000; an extra $100 appears from rounding far beyond two significant digits.

  * **III. “Determine the value at $1 000 and conclude the investment is justified.”**

    * Two errors: the benefit is overstated (should be ≈ $900) **and** even at $1 000 the cost still exceeds the benefit, so calling it “justified” is logically inconsistent.

  * **IV. “Calculate the value at $9 000 and conclude the investment is justified.”**

    * The $9 000 figure is off by an order of magnitude (likely mis-placing a decimal). Because the correct benefit is only about $900, this option both mis-states the savings and reaches an incorrect conclusion.

**Bottom line:** Elevating availability from 99.9 % to 99.99 % yields ~7.9 hours of extra uptime worth roughly **$900** in annual revenue protection—far short of the proposed **$2 000** outlay. Only option I reflects that reality.

</details>

---

### Exam 5 · Q48

**Your company adheres to Site Reliability Engineering principles. Following a severe incident triggered by a software change, you're drafting a postmortem to prevent similar incidents in the future. What steps should you take?**

- A. Identify the engineers accountable for the incident and escalate the matter to senior management.
- B. Ensure that test cases capable of catching errors like this are successfully executed before every new software release.
- C. Conduct follow-ups with the staff who reviewed the changes and establish best practices for future adherence.
- D. Develop a policy mandating that on-call teams promptly engage engineers and management in discussions to devise an action plan upon incident occurrence.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Ensure that test cases capable of catching errors like this are successfully executed before every new software release.

**The best answer here is**

**B. Ensure that test cases capable of catching errors like this are successfully executed before every new software release.**

Here's why and a breakdown of the other options:

**Why Option B is the Best Approach:**

  * **Focus on Prevention:** SRE is about building resilient systems and preventing failures. While other options have value, this option directly addresses the root cause by creating a safety net to catch similar errors before they impact production.

  * **Systems-Based Approach:** It emphasizes improving processes rather than focusing on individuals, aligning with SRE and fostering a blameless culture.

**Why Other Options are Less Ideal:**

  * **A. Identify the engineers accountable for the incident and escalate the matter to senior management.**

    * **Blame Culture:** This promotes a culture of fear and discourages open communication, undermining SRE principles and making it harder to uncover the true systemic causes of failure.

  * **C. Conduct follow-ups with the staff who reviewed the changes and establish best practices for future adherence.**

    * **While valuable, it's reactive:** This option is important for learning from the incident, but it doesn't directly prevent a similar error from happening again.

  * **D. Develop a policy mandating that on-call teams promptly engage engineers and management in discussions to devise an action plan upon incident occurrence.**

    * **Focus on Response, Not Prevention:** This optimizes incident response, which is vital, but the main goal of the postmortem is to proactively avoid repeating the incident.

</details>

---

### Exam 5 · Q49

**You're maintaining a user-facing web application and analyzing its error budget over the past six months. Despite occasional fluctuations, the application has consistently stayed below 5% of its error budget. After a Service Level Objective (SLO) review with stakeholders, you confirm that the current SLO is appropriate. How can you better align the application's SLO with its actual reliability, considering velocity, reliability, and business needs? (Select two.)**

- A. Increase serving capacity across all application zones.
- B. Opt for more frequent or potentially risky application releases.
- C. Adjust the SLO to better match the observed reliability of the application.
- D. Introduce and assess additional Service Level Indicators (SLIs) for the application.
- E. Schedule planned downtime to utilize more of the error budget, ensuring users aren't reliant on a stricter SLO.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Opt for more frequent or potentially risky application releases. **|** D. Introduce and assess additional Service Level Indicators (SLIs) for the application.

**Correct Answers: B and D**

**Reasoning**

Your application has consistently consumed **less than 5%** of its error budget over six months.  
This means:

  * The service is **more reliable than required** by the current SLO.

  * You are **under-utilizing your error budget**.

  * You can afford to **move faster** without hurting users or violating SLOs.

Google SRE guidance states:

  * **If your error budget is consistently under-consumed** , you should **increase the release velocity**.

  * **If your SLO is appropriate and not too strict** , you should **NOT tighten it** , but instead improve value delivery or observability by adding meaningful SLIs.

This leads to the two correct choices.

**Correct Answer 1: B. Opt for more frequent or potentially risky application releases.**

Why this is correct

Underused error budget means:

  * You can ship faster

  * You can take more risk

  * You can accelerate innovation

This is exactly what Google’s **Error Budget Policy** recommends.

**Reference:**  
**Google SRE Book - Error Budget Policy**  
<https://sre.google/sre-book/availability-table/>

**Correct Answer 2: D. Introduce and assess additional Service Level Indicators (SLIs) for the application.**

**Why this is correct**

If your system appears _too reliable_ , you might not be measuring **all** important aspects of user experience.

Adding or refining SLIs can:

  * Improve understanding of real reliability

  * Ensure all critical user interactions are measured

  * Align reliability signals with business needs

This is a standard SRE practice when reliability seems artificially high.

**Reference:**  
**Google SRE Workbook – Implementing SLIs**  
<https://sre.google/workbook/implementing-slos/>

**Why the Other Options Are Incorrect**

**A. Increase serving capacity**

This increases cost and does not improve alignment with SLOs.  
Your system is already exceeding expectations.

**C. Adjust the SLO**

You **already confirmed** the SLO is appropriate.  
Tightening it would reduce error budget artificially and may slow velocity without business need.

**E. Schedule planned downtime**

This is anti-SRE and harmful.  
Never reduce reliability intentionally just to “use up” error budget.

**Final Answer: B and D**

</details>

---

### Exam 5 · Q51

**As the SRE engineer for a microservice deployed to a Google Kubernetes Engine (GKE) Autopilot cluster, you oversee an online store's functionality. The system publishes order messages to Pub/Sub, and a microservice processes these messages to update stock information in the warehousing system. Due to a surge in orders during a sales event, stock updates are lagging, leading to orders being accepted for out-of-stock products. Reviewing the microservice metrics against typical levels reveals:**

**Current Microservice Metrics:**

**A. Average CPU usage across all Pods: 30% of Pod limit (typical state: 20% of Pod limit)**

**B. Average memory usage across all Pods: 10% of Pod limit (typical state: 10% of Pod limit)**

**C. Pub/Sub subscription:A. Average oldest unacknowledged message age: 8074 milliseconds (typical state: 347 milliseconds)**

**D. Average undelivered messages: 14705 messages (typical state: 5 messages)**

**E. Average acknowledgment latency: 354 milliseconds (typical state: 312 milliseconds)**

**Your objective is to ensure accurate inventory representation in the warehouse system during order placement while minimizing customer impact. What course of action should you take to resolve the current situation?**

- I. Decrease the acknowledgment deadline on the subscription.
- II. Introduce a virtual queue to manage typical traffic levels on the online store.
- III. Scale up the number of Pod replicas.
- IV. Increase the Pod CPU and memory limits.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Scale up the number of Pod replicas.

**Correct Answer: III. Increase the number of Pod replicas.**

Reasoning

The metrics clearly indicate a **processing throughput bottleneck** , not a resource constraint on individual Pods.

Key observations from the metrics:

  * **CPU usage:** 30% of Pod limit (only slightly higher than normal 20%)

  * **Memory usage:** 10% of Pod limit (same as normal)

This shows that **individual Pods are not resource-constrained**.

However, Pub/Sub metrics show a **large backlog** :

  * **Oldest unacknowledged message age:** 8074 ms (vs 347 ms normally)

  * **Undelivered messages:** 14,705 (vs 5 normally)

  * **Acknowledgment latency:** slightly increased

These metrics indicate that **messages are accumulating faster than the microservice can process them** , meaning the system **needs more parallel consumers**.

In a Pub/Sub-driven architecture, the standard scaling strategy is:

  * Increase the number of **consumer instances** (Pods)

  * Each Pod pulls messages independently

  * Pub/Sub distributes messages across consumers automatically

In **GKE Autopilot** , scaling Pods increases message processing concurrency without managing nodes manually.

Increasing replicas will:

  * Increase message processing throughput

  * Reduce backlog

  * Ensure inventory updates keep pace with order intake

  * Prevent overselling inventory

This aligns with Google Cloud’s guidance for Pub/Sub consumer scaling.

Reference:  
<https://cloud.google.com/pubsub/docs/pull#scaling_subscribers>

**Why the other options are not the best choice**

**I. Decrease the acknowledgment deadline on the subscription**

The acknowledgment deadline determines **how long the subscriber has to acknowledge a message** before Pub/Sub redelivers it.  
Reducing it would **increase duplicate deliveries** and worsen load rather than increasing processing throughput.

Reference:  
<https://cloud.google.com/pubsub/docs/subscriber#ack_deadline>

**II. Add a virtual queue to the online store that allows typical traffic levels**

Introducing a queue or throttling layer at the store would **delay or reject orders** , negatively impacting customers during a sales event.  
It does not solve the underlying issue of **insufficient consumer throughput**.

**IV. Increase the Pod CPU and memory limits**

Current usage shows:

  * CPU ~30%

  * Memory ~10%

This indicates Pods **are not CPU or memory bound**. Increasing limits would not increase message processing throughput.

Reference:  
<https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview>

**Key Concept to Remember**

When **Pub/Sub backlog increases while CPU/memory usage remains low** , the issue is typically **insufficient consumer parallelism** , not resource exhaustion.

The recommended solution is to **scale horizontally (more subscriber Pods)** rather than vertically scaling Pod resources.

</details>

---

### Exam 5 · Q55

**Your organization is leading a DevOps project. The current responsibilities are as follows:**

  * **The DevOps team manages the service infrastructure and is on-call for incidents.**

  * **The Software Development team writes, submits, and reviews code.**

**Currently, neither team has published Service Level Objectives (SLOs) for the service. You are tasked with designing a new joint-ownership model where both teams share responsibility for the service.**

**How should you allocate the responsibilities between the DevOps team and the Software Development team in this new model?**

- A: Limited Collaboration
    DevOps: Management of service infrastructure and response to incidents.
    Software Development: Code development, submission of code for review, and conducting reviews of code.
    Shared: No shared responsibilities.
- B: Complete Role Reversal
    DevOps: Code development, submission of code for review, and conducting reviews of code.
    Software Development: Management of service infrastructure and response to incidents.
    Shared: No shared responsibilities.
- C: SLO-Focused Collaboration
    DevOps: Management of service infrastructure and response to incidents.
    Software Development: Code development, submission of code for review, and conducting reviews of code.
    Shared: Defining and making public Service Level Objectives (SLOs) for the service.
- D: Expanded Joint Ownership
    DevOps: Management of service infrastructure, response to incidents, definition and publication of SLOs.
    Software Development: Code development, submission of code for review, conducting reviews of code, monitoring of application performance metrics.
    Shared: No explicit shared responsibilities (though collaboration on SLOs is likely).

<details><summary>Answer &amp; explanation</summary>

**Correct:** C: SLO-Focused Collaboration

Out of the provided options, the best approach for the new joint-ownership model is

**C: SLO-Focused Collaboration**. Here's why:

**Why SLOs Matter**

  * **Shared Understanding:** SLOs create a common language around service health and reliability, providing clear targets for both teams to work towards.

  * **Customer Focus:** SLOs directly tie service performance to user experience, ensuring the focus remains on delivering a reliable product.

  * **Proactive Approach:** Monitoring performance against SLOs allows teams to identify and address potential issues before they escalate into major incidents.

**Breakdown of Responsibilities**

  * **DevOps:**

    * **Manage Infrastructure:** DevOps remains responsible for maintaining the underlying infrastructure supporting the service.

    * **Incident Response:** As the specialists in infrastructure and operations, DevOps continues to handle incident resolution.

  * **Software Development:**

    * **Code Ownership:** Software devs focus on writing, submitting, and reviewing code to ensure quality and maintainability.

  * **Shared:**

    * **Defining SLOs:** Both teams collaborate to determine appropriate SLOs based on user expectations, business needs, and the capabilities of the system.

    * **Publishing SLOs:** Making SLOs visible to stakeholders improves transparency and builds trust.

**Advantages of SLO-Focused Collaboration**

  * **Balance:** Maintains core strengths of each team while creating a clear overlap in responsibility around service reliability.

  * **Mutual Accountability:** Both teams are incentivized to work together to meet the agreed-upon SLOs.

  * **Data-Driven Improvement:** SLO monitoring leads to insights that drive improvements across development and operational practices.

**Why Other Options Are Less Ideal**

  * **A: Limited Collaboration:** No shared goals or responsibilities make it hard to drive holistic service improvements.

  * **B: Complete Role Reversal:** Forcing teams into unfamiliar domains is disruptive and inefficient. It's better to leverage existing expertise.

  * **D: Expanded Joint Ownership:** While good in theory, it risks overextending team responsibilities. SLOs provide a more manageable starting point for shared ownership.

</details>

---

### Exam 5 · Q60

**Your company relies on a legacy database hosted on Google Kubernetes Engine (GKE), which experiences significant delays in responding to Pod evictions and rescheduling. Any interruptions to the database's operation are deemed unacceptable. To ensure continuous operation, you need to select an appropriate GKE maintenance strategy. What should you do?**

- I. Set the GKE maintenance channel to "Stable".
- II. Define a node pool upgrade strategy with the max-surge-upgrade parameter set to 0.
- III. Establish a "PodDisruptionBudget" object with maxUnavailable specified as 100%.
- IV. Configure a maintenance exclusion window with a scope of "No minor or node upgrades".

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Configure a maintenance exclusion window with a scope of "No minor or node upgrades".

The most appropriate GKE maintenance strategy to ensure continuous operation of the legacy database hosted on Google Kubernetes Engine is:

**IV. Configure a maintenance exclusion window with a scope of "No minor or node upgrades".**

**Explanation:**

Configuring a maintenance exclusion window with a scope of "No minor or node upgrades" allows you to prevent GKE from performing any minor or node upgrades during the specified window. This ensures that no interruptions occur due to upgrades that may lead to Pod evictions and rescheduling, which could impact the database's operation. By defining this exclusion window, you can maintain continuous operation of the legacy database without the risk of disruptions caused by GKE maintenance activities.

**Justification for why other options are not suitable:**

**I. Setting the GKE maintenance channel to "Stable":**

  * Setting the maintenance channel to "Stable" provides predictability in terms of when upgrades occur, but it doesn't prevent upgrades from happening altogether. It may still lead to interruptions if upgrades occur during critical times.

**II. Defining a node pool upgrade strategy with the max-surge-upgrade parameter set to 0:**

  * While setting max-surge-upgrade to 0 ensures that no additional nodes are added during node pool upgrades, it doesn't prevent the upgrades themselves. Node pool upgrades could still result in Pod evictions and rescheduling, potentially impacting the database's operation.

**III. Establishing a "PodDisruptionBudget" object with maxUnavailable specified as 100%:**

  * Specifying maxUnavailable as 100% in a PodDisruptionBudget would effectively prevent any Pod disruptions during maintenance activities. However, it wouldn't prevent node upgrades or other maintenance tasks that could still impact the database's operation. Additionally, this approach may not align with best practices for managing Pod disruptions.

**References:**

<https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions>

<https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#scope_of_maintenance_to_exclude>

<https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels>

<https://cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters>

<https://www.youtube.com/watch?v=eqJQTANI_RI>

</details>

---
