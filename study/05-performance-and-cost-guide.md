# Domain 5 Study Guide — Optimizing Performance and Cost

> Condensed from the question bank: [05-performance-and-cost.md](05-performance-and-cost.md) (23 questions). Citations look like (Exam N · QM).

**Repeated scenarios:** Exam 5 reuses six Exam 1/2/4 scenarios almost word for word. E5 Q4 = E1 Q41, E5 Q7 = E1 Q30, E5 Q18 = E2 Q48, E5 Q22 = E2 Q24, E5 Q27 = E2 Q6, E5 Q41 = E4 Q14. If you know these six, you have covered about a quarter of the bank.

---

## 1. Compute pricing: CUDs, flexible commitments, reservations, Spot VMs

### Key facts
- **Committed use discounts (CUDs)** give lower prices in return for a **1-year or 3-year** commitment. The 3-year term gives the bigger discount. A CUD is a **billing arrangement only**: the VMs run unchanged, so performance is not affected (Exam 1 · Q30, Exam 5 · Q7).
- **Resource-based commitments** cover predictable, steady usage, and they are **tied to one region** (Exam 1 · Q30, Exam 3 · Q45).
- **Compute flexible commitments** commit to a **minimum hourly spend**, not to a number of instances. They apply **across regions and projects within the same Cloud Billing account**, so the discount follows workloads when they move (Exam 3 · Q45).
- **A commitment does not reserve capacity.** Reservations hold capacity in specific zones, unused reserved capacity is still charged, and flexible commitments cannot have reservations attached (you create them separately) (Exam 1 · Q30, Exam 3 · Q45).
- **Spot VMs** replace preemptible VMs. Compute Engine can reclaim them at any time, they are **excluded from the Compute Engine SLA**, and they may not be available again right away. The discount is large (the bank cites 60–90%) (Exam 1 · Q5, Exam 1 · Q30, Exam 3 · Q54).
- **Instance groups (MIG or unmanaged) do not lower prices.** MIGs provide autoscaling, autohealing and updates. Unmanaged groups only let you load balance VMs you manage yourself (Exam 1 · Q30, Exam 5 · Q7).
- Sustained use discounts (SUDs) do not appear in any question in this bank.

### Decision rules
- If the workload is stable, fixed in size, business-critical, and "no performance impact" is required → choose **CUDs** (Exam 1 · Q30, Exam 5 · Q7).
- If total demand is steady or growing but instances will **move between regions**, on a multi-year horizon → choose a **3-year compute flexible commitment** (Exam 3 · Q45).
- If the question also needs **assured capacity in specific zones** → add **reservations** (Exam 3 · Q45, option B becomes correct).
- If the work can be interrupted (resumable or checkpointed, no completion-time SLO) and must stay on VMs → choose **Spot VMs** (Exam 3 · Q54).
- If the architecture survives losing a node (quorum, replication, stateless with external coordination) → it is a **Spot candidate** (Exam 1 · Q5).
- If the workload is "unsuitable for containerization" → rule out **Cloud Run and GKE**, which both run containers (Exam 3 · Q54).

### Comparison

| Lever | Lowers price? | Interruption risk | Scope | Best for |
|---|---|---|---|---|
| Resource-based CUD | Yes | None | One region | Steady, predictable usage in one region |
| Compute flexible CUD | Yes | None | All regions and projects in the billing account | Steady spend that moves between regions |
| Reservation | No (unused capacity is still billed) | None | Specific zone(s) | Guaranteed capacity |
| Spot VM | Yes, the biggest discount | Can be reclaimed at any time, no SLA | n/a | Fault-tolerant or resumable batch work |
| MIG / unmanaged group | No | n/a | n/a | Operations and load balancing, not cost |

### Traps
- **Spot VMs for a business-critical workload.** It is the most tempting distractor, but the discount comes from accepting interruption (Exam 1 · Q30).
- **"The data is in durable storage, so Spot is fine."** Durable inputs and outputs do not protect work in progress. A GPU render job with no checkpoint loses its progress when preempted (Exam 1 · Q5). See ⚠️ below.
- **"Scalable" is not the same as "tolerates losing a node."** A scalable cache is not necessarily safe on Spot (Exam 1 · Q5).
- **Treating a commitment as a capacity guarantee,** or adding reservations the question never asked for (Exam 3 · Q45).
- **A 3-year CUD for a resumable job with no SLO.** It works, but Spot VMs are cheaper (Exam 3 · Q54).
- **Picking Spot does not make the application recoverable.** The application still needs its own retry and resume logic (Exam 3 · Q54).

---

## 2. Network Service Tiers and load balancer scope

### Key facts
- **Premium Tier** is the default. Traffic rides Google's global backbone, which gives better performance and costs more. **Standard Tier** hands traffic to ordinary ISP transit networks, which costs less but has lower performance and availability, and it is **regional** (Exam 1 · Q41, Exam 2 · Q24).
- **Global external IP addresses and the global (Envoy-based) external Application Load Balancer require Premium Tier.** The **regional** external Application Load Balancer (also Envoy-based) works in either tier and needs a **proxy-only subnet** (Exam 2 · Q24).
- Standard Tier with a regional load balancer gives up the global anycast IP and **Cloud CDN** (Exam 2 · Q24).

### Decision rules
- If the goal is to **lower network cost** for internet-facing traffic (for example, a game backend serving players) → choose **Standard Tier** (Exam 1 · Q41, Exam 5 · Q4).
- If the backends are in one region and the users are local (europe-west2, UK only) → choose **Standard Tier with a regional load balancer** (Exam 2 · Q24, Exam 5 · Q22).
- If users are worldwide, backends are in several regions, or you need Cloud CDN → choose **Premium Tier with a global load balancer** (Exam 2 · Q24).

### Comparison: what each "network" option actually does

| Option | What it solves | Lowers egress cost? |
|---|---|---|
| Standard Tier | Pricing and routing of internet traffic | **Yes** |
| Shared VPC host project | Central network administration and IAM | No |
| Private GKE cluster | Security (nodes get internal IPs only) | No, and NAT can add cost |
| External Application Load Balancer as Ingress | Distributing HTTP traffic | No, and it has its own charges |
| Cloud NAT | Outbound internet access for private VMs | No, and it does not raise bandwidth |

(Exam 1 · Q41, Exam 5 · Q4, Exam 4 · Q14)

### Traps
- **"Standard Tier + global load balancer."** It looks like the best of both, but the combination is invalid (Exam 2 · Q24, option C).
- **"Premium + regional."** The scope is right but the tier is the expensive one (Exam 2 · Q24, option B).
- **"HTTP load balancer as Ingress."** It improves traffic distribution, not the price per GB (Exam 1 · Q41).

---

## 3. Global serving for latency (Cloud Run)

- If users are worldwide and should reach the **nearest region** → **deploy the service to every region**, behind **one global anycast IP on a global external HTTP(S) load balancer** (Exam 5 · Q59).
- A single region behind a global load balancer is not enough. Neither is Cloud Armor, which is a security control, not a latency tool (Exam 5 · Q59).
- This is the opposite of the cost rule in section 2: when **latency for global users** is the goal, choose global + Premium; when **cost for local users** is the goal, choose regional + Standard.

---

## 4. VM network throughput

- The **bandwidth cap applies to the whole instance**, not to each vNIC. It scales with the **vCPU count** (the bank cites about 2 Gbps per vCPU) up to a limit set by the machine series. **Tier_1 networking** on qualifying machine types also raises the cap (Exam 4 · Q14).
- If monitoring shows a VM is pinned at its maximum throughput → **resize to a larger machine type** (n2-standard-2 → n2-standard-8) (Exam 4 · Q14, Exam 5 · Q41).

| Distractor | Why it fails |
|---|---|
| Add more vNICs | Bandwidth is counted per instance, so extra NICs do not add bandwidth |
| Cloud NAT | Provides outbound connectivity for private VMs, not throughput |
| Ops Agent | Adds observability only, not capacity |

---

## 5. Cost attribution: labels + billing export to BigQuery

- **Labels** are key/value pairs that are **forwarded to Cloud Billing**. **Billing export to BigQuery** writes cost line items, including their labels, into a dataset you can query (Exam 2 · Q48, Exam 5 · Q18).
- If several systems share **one project** → the project cannot separate them. **Label each system's resources, export billing to BigQuery, and group cost by label** (Exam 2 · Q48).
- **Not billing dimensions:** instance **metadata**, **Cloud Logging exports** (they contain log entries, not charges) and **VM names** (Exam 2 · Q48, Exam 5 · Q18).
- The console billing reports *can* group by label, **but only after the labels exist**. Without labels, a "cost breakdown report" cannot split costs by system (Exam 2 · Q48, option A).
- Good practice: apply labels at provisioning time (through IaC), keep watching for unlabeled spend, and use a separate allocation rule for shared costs such as networking (Exam 2 · Q48).

---

## 6. Rightsizing and resource utilization

- **VM rightsizing:** the **VM instance rightsizing recommender** (Active Assist, available through the **Recommender API**) analyzes CPU and memory over the **last 8 days**, using data Compute Engine already collects. **No agent is needed** for a CPU-based recommendation. Query it and apply the result (Exam 4 · Q58).
  - Installing the Ops Agent, by hand or through an Agent Policy, is optional. It only becomes necessary when you need finer guest or memory metrics (Exam 4 · Q58).
  - Picking a machine type by reading a dashboard yourself is subjective, takes more steps, and is not Google's recommended practice (Exam 4 · Q58).
- **Cloud Run utilization:** **Cloud Monitoring** already has built-in container CPU and memory utilization metrics, with no setup. There is no VM, so the Ops Agent cannot be installed (Exam 2 · Q6, Exam 5 · Q27).
  - Look at **peak** utilization, not just the average, before you resize (Exam 2 · Q6).
- **Rule:** if Google already collects the data and a recommender exists → use the recommender or the built-in metric, not your own pipeline (Exam 4 · Q58, Exam 2 · Q6).

---

## 7. Logging cost control (GKE)

- Scenario: a dev cluster has verbose application logs, developers read them with `kubectl logs` (not Cloud Logging), and GKE operational logs must be kept. The bank's answer is an **exclusion filter on the `_Default` sink** for `k8s_container` logs (Exam 5 · Q35).
- What each option does, per the bank's explanation:

| Option | Effect |
|---|---|
| `--logging=SYSTEM` | Sends system logs only; workload logs no longer go to Cloud Logging |
| `--logging=WORKLOAD` | Does not reduce verbosity |
| Disable the `_Default` sink | Too broad: GKE operational logs are lost too |
| Exclusion filter on `_Default` | Targeted cut in log volume, which lowers cost |

- ⚠️ The bank's answer is questionable. See the final section.

---

## 8. Performance tools: Monitoring vs Profiler vs Trace vs logs

| Question asked | Tool | Source |
|---|---|---|
| How much CPU or memory is the service using? (cost/sizing) | **Cloud Monitoring** built-in metrics | Exam 2 · Q6 |
| Which **code path or function** is hot or slow, in production? | **Cloud Profiler** | Exam 4 · Q42, Exam 5 · Q64 |
| Where does latency go across a request or downstream calls? | **Cloud Trace** | Exam 2 · Q6, Exam 4 · Q29 |
| A custom aggregate that is only found in log content | **Logs-based metric** | Exam 2 · Q6 |
| Is the resource saturated? Alert on it | Resource metric (e.g., CPU utilization) | Exam 4 · Q42 |

### Cloud Profiler facts
- Profiler is a **statistical (sampling)** profiler that runs **continuously** and **attributes CPU and heap to source code**. Overhead is under 5% at collection time and commonly under 0.5% amortized, so it is safe to leave on in production (Exam 4 · Q42).
- It is managed by Google. In Go, call `profiler.Start` from `cloud.google.com/go/profiler` early in `main`. On App Engine standard, the service name and version are inferred automatically (Exam 4 · Q42).
- Results are viewed as **flame graphs**. Use Profiler to compare different algorithms in staging and production (Exam 5 · Q64).
- Profiler needs a **language-specific agent or library inside the application**. It is **not** paired with the Ops Agent (Exam 2 · Q6).

### Decision rules
- If the problem is intermittent, only at peak, cannot be reproduced locally, and both overhead and management must be minimal → choose **Cloud Profiler**. A self-hosted profiler on Compute Engine adds management work, and running `go tool pprof` by hand is not continuous (Exam 4 · Q42).
- If Profiler shows the **heap climbing until each restart** on GKE → **raise the container's memory limit in the deployment**. Adding bigger nodes does not change the limit that triggers the OOM kill, raising the CPU limit targets the wrong resource, and Trace measures latency, not memory (Exam 4 · Q29).
- **Wall-clock vs CPU time** (Exam 4 · Q45, choose two), as the bank teaches it:
  - A **large gap** → increase the **CPU** allocation (not memory or disk).
  - A **small gap** plus latency **burning the error budget** (from Trace) → the code is CPU-bound, so **mark the application for code optimization**.
  - "Low heap usage" is **not** a signal that the application needs tuning.
  - ⚠️ See the final section.

---

## 9. Capacity planning: measure first

- If the question asks what to do **"first"** to prepare for a peak or busy season → **run a load test** to learn how the system scales and where it bottlenecks. Autoscaling thresholds, pre-provisioning and DR sizing should all be based on those results (Exam 2 · Q59).
- Traps: doubling last season's capacity is an arbitrary multiplier; turning on autoscaling before you know the right metric and thresholds; a DR runbook is a different concern from normal peak traffic (Exam 2 · Q59).
- Google's peak-event guidance says to start load testing **3–5 months** before the event (Exam 2 · Q59).

---

## ⚠️ Questionable answers

- **Exam 5 · Q35 (logging).** The bank's answer is weak in two ways.
  - The filter `severity >= DEBUG` matches essentially **all** container logs at DEBUG or above. It does not, as the explanation claims, exclude only "DEBUG and lower." The explanation misreads the filter.
  - Developers read logs with `kubectl logs`, which does not depend on Cloud Logging. GKE operational logs must be kept. That fits **`--logging=SYSTEM`** (option I), which many sources treat as the intended answer.
  - Disabling `_Default` also does not remove *all* logging, because the `_Required` sink still keeps audit logs.
  - On the exam, prefer **SYSTEM** for this exact scenario.
- **Exam 4 · Q45, option A (large wall-clock/CPU gap → add CPU).** Cloud Profiler's own concepts describe wall time much larger than CPU time as time spent **waiting** (I/O, locks, downstream calls). Adding CPU usually does not fix that.
  - The bank's answer matches the published sample question, so remember it for the exam.
  - It is not a general rule for real diagnosis.
- **Exam 4 · Q29 (heap grows until restart → raise the memory limit).** A heap that grows steadily after a new release suggests a **memory leak**. Raising the limit only delays the OOM kill.
  - It is the expected exam answer. The explanation itself mentions a parallel effort to fix the code.
  - Treat it as a stopgap, not a fix.
- **Exam 1 · Q5 (Spot VM workload).** Google's Spot documentation lists batch and **rendering / media-processing** jobs as typical Spot workloads. Rejecting option D (a GPU render job that reads from and writes to a bucket) because "checkpointing isn't stated" is a stretch.
  - Compare Exam 3 · Q54, where resumable processing makes Spot correct.
  - Learn the exam's decisive cue: "sufficient quorum" is stated explicitly. Do not conclude that rendering is a poor fit for Spot.
- **Exam 5 · Q59, reasoning for option III.** The real reason option III fails is that **regional external load balancers cannot share one global anycast IP**; global IPs require the global, Premium-Tier load balancer (Exam 2 · Q24). The explanation's "latency within continents" argument is not the real reason. The answer itself (II) is fine.
- **Exam 5 · Q18, sample SQL.** In the billing export, `labels` is a repeated key/value field. You need `UNNEST(labels)` and a filter on `key = 'system'`. Selecting `labels.system` directly will not work. The answer (B) is still correct.
- **Exam 5 · Q4, option IV.** "The HTTP load balancer is Premium-only and therefore more expensive" is an overstatement. A regional external Application Load Balancer can run in Standard Tier (Exam 2 · Q24). The correct reason to reject option IV is that it solves traffic distribution, not cost (Exam 1 · Q41).

---

## Last-minute cheat sheet

- Stable, fixed, business-critical, and "no performance impact" → **CUD**. Never Spot.
- Steady total usage but instances move between regions → **compute flexible CUD**; a longer horizon → **3 years**.
- A CUD is a discount, not capacity. You need guaranteed capacity → **add a reservation**.
- Interruptible or resumable work, no SLO, VM-only (no containers) → **Spot VMs**.
- Spot needs the system to survive losing a node (e.g., **quorum**); durable storage alone is not enough.
- MIGs and unmanaged groups do **not** lower prices.
- Cut internet egress cost → **Standard Tier**. Not Shared VPC, a private cluster, or a load balancer Ingress.
- One region and local users → **Standard Tier + regional load balancer**. A global load balancer or global IP needs **Premium**.
- Global users routed to the nearest region → **deploy to each region + global HTTP(S) load balancer with an anycast IP**.
- VM pinned at its throughput limit → **larger machine type** (bandwidth scales with vCPUs). Not NICs, NAT or Ops Agent.
- Cost per system in one project → **labels + billing export to BigQuery + GROUP BY label**.
- VM rightsizing → **Recommender API (rightsizing recommender)**, which needs no agent and uses the last 8 days of data.
- Cloud Run CPU or memory use → **Cloud Monitoring built-in metrics**. No setup, no Ops Agent.
- Hot code paths in production, low overhead → **Cloud Profiler** (`profiler.Start`), viewed as flame graphs.
- Latency across services → **Trace**; code hotspots → **Profiler**; utilization → **Monitoring**.
- Heap climbs until restart on GKE → **raise the container memory limit** (not node size, CPU or Trace).
- Wall-clock vs CPU time: big gap → add CPU (exam answer); small gap + error budget burning → optimize the code.
- Prepare for a busy season: **load test first**, then size autoscaling and capacity.
- Dev GKE logs read with `kubectl logs`, system logs must be kept → prefer `--logging=SYSTEM` (the bank says exclusion filter; see ⚠️).
