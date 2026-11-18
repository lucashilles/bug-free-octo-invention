# Domain 6 Study Guide — Ensuring Solution and Operations Excellence

> Condensed from the 36-question bank in [`06-operations-excellence.md`](06-operations-excellence.md). Citations look like (Exam N · QM). Older questions say "Stackdriver": read it as Cloud Logging, Cloud Monitoring, Cloud Trace and the rest of Google Cloud Observability.

---

## 1. Cloud Logging: collecting, routing and analyzing logs

### Key facts
- **Cloud Audit Logs** are collected automatically. **Admin Activity** audit logs are always on and free. Data Access audit logs are off by default for most services (BigQuery is the exception).
- Compute Engine VMs do **not** send their OS logs (syslog, kernel, application files) on their own. You install an agent **on every VM**: the old question says "Stackdriver Logging agent"; today it is the **Ops Agent**, which collects both logs and metrics (Exam 2 · Q26).
- **GKE** sends container `stdout`/`stderr` to Cloud Logging. Logs survive pod restarts, so a crash-looping deployment is debugged in Logs Explorer filtered on the **`k8s_container`** resource, not on the nodes and not with `kubectl exec` into a container that dies every 2 seconds (Exam 2 · Q6).
- Logging and Monitoring for GKE (once called "Cloud Operations for GKE" or "Stackdriver Kubernetes Engine Monitoring") is on by default for new clusters. If it was turned off, you **enable it on the existing cluster** with `gcloud container clusters update`. No new cluster, no migration (Exam 2 · Q55).
- The **Log Router** sends log entries to sinks. Sink destinations: Cloud Logging buckets, **Cloud Storage**, **BigQuery**, **Pub/Sub**, or another project.
- An **aggregated sink** is created on a **folder** or **organization** with child resources included. A folder-level sink covers every current **and future** project in that folder, and nothing outside it (Exam 3 · Q56).
- **Log Analytics** lets you query a log bucket with **SQL**. You can link the bucket to a **BigQuery linked dataset** and build dashboards on it in **Data Studio** (called Looker Studio from 2022 to 2026) (Exam 5 · Q41).
- A sink to **Pub/Sub** turns a log entry into an event. Pub/Sub can then trigger a **Cloud Run function** (formerly Cloud Functions). This is how you react reliably to "instance deleted" events from a MIG, instead of trusting a shutdown script (Exam 3 · Q62).
- **Firewall Insights** (Network Intelligence Center) needs **Firewall Rules Logging** turned on for each rule it should analyze. VPC Flow Logs are a different feature (Exam 2 · Q48).
- For "how many queries did each user run in BigQuery", query the **`INFORMATION_SCHEMA.JOBS`** views. They already hold the user, job type and time for every job (Exam 2 · Q20).

### Comparison

| Need | Use | Source |
|---|---|---|
| Admin activity across services | Cloud Audit Logs, collected automatically | (Exam 2 · Q26) |
| OS/system logs from VMs | Ops Agent on **each** VM | (Exam 2 · Q26) |
| Logs from a crash-looping GKE pod | Logs Explorer, `k8s_container` resource | (Exam 2 · Q6) |
| All production projects' logs, now and later | Aggregated sink on the Production **folder** | (Exam 3 · Q56) |
| SQL over logs + dashboards | Log Analytics → linked BigQuery dataset → Data Studio | (Exam 5 · Q41) |
| Act on a log event | Sink → Pub/Sub → Cloud Run function | (Exam 3 · Q62) |
| Firewall Insights shows nothing | Enable Firewall Rules Logging | (Exam 2 · Q48) |
| BigQuery queries per user | `INFORMATION_SCHEMA.JOBS` | (Exam 2 · Q20) |

### Decision rules
- "Admin logs **and** VM system logs" → admin logs are automatic; the agent goes on **every** instance (Exam 2 · Q26).
- "Current and future projects" in one folder, "exclude non-production" → **folder-level aggregated sink**, not the organization and not one sink per project (Exam 3 · Q56).
- "Team prefers SQL" + "dashboards" + "Well-Architected" → **Log Analytics** with the linked BigQuery dataset, no extra export pipeline (Exam 5 · Q41).
- "Shutdown script doesn't run reliably" → drive cleanup from the **instance-removal log entry** through a sink, outside the VM (Exam 3 · Q62).
- "No logging enabled" + "minimal disruption" → turn it on **in place** (Exam 2 · Q55).

### Traps
- "All admin and VM logs are collected automatically" is false for VM OS logs. "Install the agent on one VM to collect everything" is also false: an agent only reads its own VM (Exam 2 · Q26).
- Serial-port logs and node logs are the wrong layer for an application writing to stdout in GKE (Exam 2 · Q6).
- An organization-level sink over-collects non-production logs. Per-project sinks don't pick up new projects (Exam 3 · Q56).
- A shutdown script that waits 30 seconds, retries or publishes to Pub/Sub still depends on the VM living long enough (Exam 3 · Q62).
- Cloud Audit Logs filters or `bq ls`/`bq show` loops are clumsy ways to count queries per user. Data Studio needs a data source first (Exam 2 · Q20).
- VPC Flow Logs don't feed Firewall Insights, and the networkAdmin role doesn't create missing logs (Exam 2 · Q48).

---

## 2. Cloud Monitoring: metrics, dashboards and alerting

### Key facts
- Cloud Monitoring collects built-in metrics for Google Cloud services. Applications can write **custom metrics** (user-defined metrics) through the API or OpenTelemetry. Dashboards and alerting policies work on both (Exam 2 · Q3).
- Real-time KPIs from game servers with low latency → **custom metrics + a Monitoring dashboard**. Bigtable plus Data Studio, BigQuery load jobs every 10 minutes, or Datastore plus Cloud Datalab (retired) are analytics paths, not live monitoring (Exam 2 · Q3).
- Monitoring ships **predefined dashboards** for GKE and many other services. To triage quickly, start from them, add the metrics you need and create **alerting policies** (Exam 2 · Q43), (Exam 5 · Q85). The old "Monitoring workspace" is now a **metrics scope**.
- An **alerting policy** has a condition (metric threshold, absence, log match, or SLO burn rate) and **notification channels** (email, SMS, PagerDuty, Slack, webhooks, Pub/Sub).
- **Uptime checks** probe a public URL, TCP port or internal endpoint from several locations. Pair one with an alerting policy whose notification channel is **Pub/Sub**, and a **Cloud Run function** can react automatically, for example by switching DNS to a "site unavailable" page and notifying Ops (Exam 4 · Q47).
- Cloud SQL: turn on **automatic storage increase** instead of alerting and resizing by hand. Alert on **CPU utilization** and **replication lag**, then act: a bigger machine type for CPU, less load per instance (the bank's answer is sharding) for lag (Exam 2 · Q10).
- **Google Cloud Managed Service for Prometheus** is a managed, global Prometheus backend built into Cloud Monitoring. It keeps PromQL, scales on its own and accepts metrics from GKE, other Kubernetes clusters, other clouds and on-premises (Exam 5 · Q81).
- For "how long a request takes from start to finish", the metric is **request latency**. QPS and throughput measure traffic; request size measures payload (Exam 5 · Q54). Latency, traffic, errors and saturation are the four **golden signals**.

### Decision rules
- Live operational KPIs → **custom metrics + Monitoring dashboard + alerts** (Exam 2 · Q3).
- "Triage incidents quickly" on GKE → **predefined dashboards + extra metrics + alerting policies**, set up before incidents (Exam 2 · Q43), (Exam 5 · Q85).
- "Detect downtime and react automatically" without managing servers → **uptime check → alert → Pub/Sub → function** (Exam 4 · Q47).
- "Developers rely on Prometheus/PromQL" + "managed" + "multi-cloud" → **Managed Service for Prometheus** (Exam 5 · Q81).
- Storage that must never fill → **auto-increase**, not "alert at 75% and resize manually" (Exam 2 · Q10).

### Traps
- A custom dashboard built **per incident** is too late. A shell script exporting node metrics to Pub/Sub, BigQuery and Data Studio is slow and over-built (Exam 2 · Q43), (Exam 5 · Q85).
- Alerting software installed on your own VM duplicates Cloud Monitoring and adds maintenance (Exam 2 · Q43), (Exam 5 · Q85).
- A cron job on a VM or a scheduled Cloud Run job polling a URL is more to run than an uptime check. Error Reporting groups application exceptions; it doesn't probe URLs (Exam 4 · Q47).
- Running the Prometheus Operator yourself in every cloud, or building your own Prometheus-compatible SaaS, is the opposite of "minimal maintenance" (Exam 5 · Q81).
- Memcached and a 32-core machine don't fix replication lag (Exam 2 · Q10).

---

## 3. SLIs, SLOs, error budgets and alerting strategy

### Key facts
- An **SLI** measures what users experience. For request-driven services the standard SLIs are **availability** (good requests / total requests) and **latency** (share of requests faster than a threshold).
- A **user-centric SLI** for a game on GKE is **request latency + error rate**. CPU, memory and server uptime describe the infrastructure, not the player (Exam 4 · Q41).
- A good **SLO** is a ratio over requests with a target: "99% of HTTP requests return 2xx" and "99% of requests complete within 100 ms". Server uptime per week, mean response time, or "whatever Google Cloud's SLA is" are weak SLOs. Means hide the slow tail; percentiles and ratios don't (Exam 4 · Q61).
- The **error budget** is 100% minus the SLO. At 99.9% availability you may fail 0.1% of requests in the window.
- **Burn rate** is how fast you spend the budget. Page only when the burn rate says the budget will run out soon (for example within 24 hours), and send slower burns to a ticket. This cuts noisy alerts on CPU, memory or every WARN log (Exam 5 · Q80).
- An **error budget policy** says what happens when the budget is spent, typically freezing feature releases to work on reliability (Exam 5 · Q80).
- Cloud Monitoring can define **SLOs** on a service and alert on them. With **Cloud Service Mesh** (formerly Anthos Service Mesh) on the cluster, services and their latency and error metrics show up automatically, so you set a latency SLO and an SLO alerting policy in the console (Exam 3 · Q27).

### Decision rules
- "From the user's viewpoint" → **latency + errors** (Exam 4 · Q41).
- "Meaningful SLOs before GA" → **percentage of requests** meeting a success or latency threshold (Exam 4 · Q61).
- "Too many low-value alerts" + an SLO exists → **symptom-based burn-rate alerting** on the error budget (Exam 5 · Q80).
- "Alert when request latency exceeds a threshold for a duration" on a mesh-enabled cluster → **service mesh + SLO + alerting policy on the SLO** (Exam 3 · Q27).

### Traps
- **Cause-based alerts** (CPU, memory, disk, instance count) page people for things users may never notice (Exam 5 · Q80).
- Log-based alerts on every WARN and ERROR line make the noise worse (Exam 5 · Q80).
- Cloud Profiler measures CPU and memory inside the code; it is not a source for latency alerting. Cloud Trace samples requests and isn't the tool for SLO alerts. Anthos Config Management (now Config Sync + Policy Controller) syncs configuration; it doesn't define SLOs (Exam 3 · Q27).
- A 99.9% "game server availability" SLO counts servers, not user requests (Exam 4 · Q61).

---

## 4. Finding the slow part: Trace, Profiler, service mesh and model monitoring

### Key facts
- **Cloud Trace** follows one request across services and shows how long each hop took. It is the tool for "a small percentage of requests are slow and pass through several microservices" (Exam 1 · Q22).
- **Cloud Profiler** samples CPU and heap usage of running code continuously, with low overhead, and shows which functions use the most. It supports Java, Go, Node.js and Python. Use it to **evaluate the performance** of a Java pipeline (Exam 5 · Q9).
- **Cloud Debugger** was shut down in 2023. Its open-source successor, Snapshot Debugger, captures variables at a line of code. Both are for debugging, not for performance analysis (Exam 5 · Q9), (Exam 3 · Q13).
- With **Cloud Service Mesh** (formerly Anthos Service Mesh), the console shows a **service topology** with request rate, error rate and latency between services. You find the slow microservice there, without reinstalling Istio or touching configuration management (Exam 2 · Q57).
- **Vertex AI Model Monitoring** watches deployed models. **Training-serving skew**: production inputs differ from the **training data**. **Prediction drift**: production inputs **change over time**. Gradually changing customer preferences → enable **prediction drift detection** (Exam 5 · Q31).
- Data quality scans in Dataplex (the catalog part is now **Knowledge Catalog**) check rows and aggregates for validity. They don't detect model drift (Exam 5 · Q31).

### Comparison

| Question in the stem | Tool | Source |
|---|---|---|
| Which service in a request chain adds the latency? | Cloud Trace | (Exam 1 · Q22) |
| Which code uses the CPU/memory? | Cloud Profiler | (Exam 5 · Q9) |
| Which microservice is slow, mesh already installed? | Cloud Service Mesh topology/telemetry | (Exam 2 · Q57) |
| What happened, with which error? | Cloud Logging | (Exam 1 · Q12) |
| Has live model input shifted over time? | Vertex AI Model Monitoring, prediction drift | (Exam 5 · Q31) |

### Decision rules
- "Microservices" + "which service is causing the delay" → **Trace**, or the **mesh dashboard** if a mesh is installed (Exam 1 · Q22), (Exam 2 · Q57).
- "Performance of the code", "CPU", "memory", "hot spots" → **Profiler** (Exam 5 · Q9).
- "Gradual change in real-world behavior" → **drift**; "training vs serving mismatch" → **skew** (Exam 5 · Q31).

### Traps
- Timeouts that fail slow requests faster hide the problem. Custom metrics per request, or looking at Monitoring alone, won't show which hop is slow (Exam 1 · Q22).
- Adding Trace instrumentation answers latency questions, not CPU hot spots. Logs don't show hot code paths (Exam 5 · Q9).
- ClusterSelectors and NamespaceSelectors in Anthos Config Management choose where config applies; they show no telemetry. Reinstalling Istio is disruptive and unnecessary (Exam 2 · Q57).
- Skew detection compares against the training data, so it isn't the tool for slow changes in the world (Exam 5 · Q31).

---

## 5. Supporting deployed solutions: incident response and troubleshooting

### Key facts
- **Mitigate first, then investigate.** If a release broke production, roll back to the last good version, then find the cause with Trace and Logging in a dev, test or staging environment. Don't redeploy the bad build to production to "watch it fail" (Exam 1 · Q12).
- With a deployment pipeline and self-healing instance groups, **revert the commit and rerun the pipeline**. Hand-edited servers get replaced by the instance template, and swapping the template by hand bypasses the pipeline (Exam 1 · Q34).
- When you don't know the cause, **look first**: Cloud Logging and Cloud Monitoring for the affected instances, before upgrading machines, restoring backups or re-architecting (Exam 3 · Q65).
- A **post-mortem** starts from evidence. For GKE pods that can't reach Cloud SQL through the Cloud SQL Auth Proxy, review the **GKE and Cloud SQL logs** before restarting or restoring anything (Exam 2 · Q12). The proxy's service account needs **Cloud SQL Client**, not Cloud Build Editor.
- To debug a VM failure: search **Cloud Logging** for related entries, read the **serial console/serial port output** (it captures kernel panics even when SSH is gone), and line up the Monitoring **metrics** with the failure time (Exam 1 · Q32).
- A **MIG with autohealing** recreates any VM that fails its health check. If every VM restarts every few seconds, nobody can log in. **Remove the health check (autohealing)** for now, then give the helper SSH access, for example a project-wide SSH key (Exam 1 · Q43). Project Viewer can't SSH; a rolling restart changes nothing.
- When autoscaling has reached its **maximum** and CPU is pinned at 100% while dependencies are healthy, the quickest way to restore traffic is to **raise the autoscaler's maximum instance count** (Exam 3 · Q1).
- When autoscaling suddenly stops keeping up after a popular launch, with 503s and slow responses, check **project quotas** first. A quota on CPUs, IPs or instances stops the autoscaler from adding capacity (Exam 4 · Q27).

### Decision rules
- "Started after an update" → **roll back first**, investigate off production (Exam 1 · Q12), (Exam 1 · Q34).
- "Root cause unknown, could take a week" → **revert through the pipeline**, never hand-patch servers (Exam 1 · Q34).
- "First step" for slowness with no known cause → **Logging + Monitoring** (Exam 3 · Q65).
- "Post-mortem" → **logs of every component involved** (Exam 2 · Q12).
- "Autoscaler at max" + "CPU at 100%" + "restore quickly" → **raise max instances** (Exam 3 · Q1).
- "Autoscaling not keeping up" + 503s after growth → **check quotas** (Exam 4 · Q27).

### Traps
- The ISP or a support ticket for packet captures is not the first move for a regression that started with a release (Exam 1 · Q12).
- Exporting a VM image to run on a local server, or checking the activity log for live migration, won't explain a kernel module crash (Exam 1 · Q32).
- Disabling autoscaling doesn't stop autohealing; the health check is what kills the VMs (Exam 1 · Q43).
- Switching the autoscaling metric to memory, or restarting VMs one by one, doesn't add capacity (Exam 3 · Q1).
- Restoring a database backup or adding a load balancer before you know the cause can lose data or add cost for nothing (Exam 3 · Q65), (Exam 2 · Q12).

---

## 6. Release management, patching, quality and reliability testing

### Key facts
- The Well-Architected Framework's **operational excellence pillar** covers operational readiness (observability, SLOs), incident and problem management, managing and optimizing resources, **automating and managing change**, and continuous improvement. The answers in this domain apply it: automate, observe, change in small reversible steps, and learn from incidents.
- **Readiness probes** keep a pod out of the Service until it reports ready. During a rolling update, a new pod with a bad production-only setting never gets traffic and the rollout stalls instead of causing an outage. **Liveness probes** restart stuck containers (Exam 3 · Q35).
- Safer release strategies: **blue/green** (switch all traffic to a fully tested copy, switch back to roll back) (Exam 1 · Q5); **canary** (a small share of traffic first); **rolling** (replace instances a few at a time). Smaller, independent services also make each release smaller (Exam 1 · Q5).
- A release pipeline can trigger checks: for example, the deployment job publishes to **Pub/Sub**, which triggers a function that runs a penetration test against each new release (Exam 4 · Q13).
- Test types: **unit** tests check one service alone (Exam 5 · Q8); integration and end-to-end tests check services together; **load** tests check behaviour at scale.
- **Load testing** simulates the expected number of concurrent users and requests and measures latency against your threshold. Locust, JMeter, k6 and Gatling are common tools. `curl` isn't a load test (Exam 3 · Q13).
- A load-test rollout plan: run in a **separate project**, measure the backend you care about (for example **Bigtable** throughput and latency), and add **logging and metrics** to both the load generator and the system under test (Exam 3 · Q45).
- **Chaos engineering** injects failures (kill instances, a zone, a dependency) under controlled conditions to prove the system recovers.
- **OS patching** at scale on Compute Engine: **VM Manager** (OS Config). The **OS Config agent** runs on each VM (preinstalled on most Google-provided images), and **patch jobs** or scheduled **patch deployments** apply updates across Debian, Ubuntu, RHEL and Windows fleets (Exam 2 · Q54), (Exam 5 · Q49).

### Decision rules
- "Outages during rolling deployments" in GKE → **readiness (and liveness) probes** (Exam 3 · Q35).
- "Fewer rollbacks" → **blue/green**, smaller services (Exam 1 · Q5).
- "Validate latency under expected load before launch" → **load test** at the expected concurrency (Exam 3 · Q13).
- Load tests → **separate project, real backends measured, full observability**, never against production (Exam 3 · Q45).
- "Debian updates with minimal manual intervention", or "patch hundreds of Linux VMs securely" → **OS patch management / VM Manager patch jobs** (Exam 2 · Q54), (Exam 5 · Q49).

### Traps
- MIG health checks act on nodes, not pods. Uptime checks and scheduled availability tasks only **detect** an outage; they don't prevent one (Exam 3 · Q35).
- Turning on autoscaling and sending a few `curl` requests, or deploying to every region, doesn't measure latency under load. Cloud Debugger is retired and never was a load tool (Exam 3 · Q13).
- Load tests run periodically against production, or production changed to log every transaction for replay, put production at risk. In an isolated test project, third-party services are stubbed out rather than load-tested (Exam 3 · Q45).
- Rebuilding instances whenever a new image ships, or SSH-ing in to patch by hand, is manual toil. A container is the wrong fit when the stem says Debian VM (Exam 2 · Q54).
- Cloud Scheduler + SSH scripts don't scale or report compliance. Config Sync is for Kubernetes config, the Ops Agent is for telemetry, and Cloud Deploy is for app releases to GKE/Cloud Run, not OS patching (Exam 5 · Q49).
- Replacing QA with canary releases removes a safety net instead of adding one (Exam 1 · Q5).

---

## ⚠️ Questionable answers

| Item | Issue |
|---|---|
| (Exam 2 · Q10) | Keyed A says to shard the database to reduce replication lag. Sharding is a large redesign; current Cloud SQL guidance usually tries a bigger replica, parallel replication or less write load first. A is still the only option that uses auto-increase storage, so the key stands. |
| (Exam 3 · Q62) | The keyed option says "Cloud Monitoring log-based alert or sink". The working design is a **Cloud Logging sink** to Pub/Sub (or an Eventarc trigger on the audit log) that triggers the function. The idea is right; the product name is loose. |
| (Exam 4 · Q27) | "Check project quota first" is the bank's answer. It fits because the stem stresses autoscaling failures after growth, but a code regression in the new feature (C) is also plausible. Learn the key. |

---

## Last-minute cheat sheet

- Stackdriver = Cloud Logging + Cloud Monitoring + Trace + Profiler + Error Reporting.
- Admin Activity audit logs: automatic. VM OS logs: **Ops Agent on every VM**.
- GKE pod logs: Logs Explorer, `k8s_container`. Logging off? **Enable on the existing cluster.**
- Logs from a whole folder, including future projects → **folder aggregated sink**.
- SQL on logs + dashboards → **Log Analytics → linked BigQuery dataset → Data Studio**.
- React to a log event → **sink → Pub/Sub → Cloud Run function**.
- Firewall Insights empty → **Firewall Rules Logging**.
- BigQuery queries per user → **`INFORMATION_SCHEMA.JOBS`**.
- Live KPIs → **custom metrics + Monitoring dashboard**. GKE triage → **predefined dashboards + alerts**.
- Site down → **uptime check → alert → Pub/Sub → function**.
- PromQL, managed, multi-cloud → **Managed Service for Prometheus**.
- SLIs from the user's view: **latency + error rate**. SLOs: **% of requests** that succeed or are fast.
- Noisy alerts → **error-budget burn-rate alerts** tied to the SLO.
- Mesh on the cluster → SLOs and latency per service from **Cloud Service Mesh**.
- Slow hop across microservices → **Trace**. Slow code (CPU/heap) → **Profiler**. Debugger is gone.
- Model inputs shifting over time → **prediction drift**; vs training data → **skew**.
- Broke after a release → **roll back first**, debug off production, revert through the pipeline.
- Unknown slowness → **Logging + Monitoring first**. VM crash → logs + **serial console** + metrics.
- MIG instances restart in a loop → **remove the health check**, then grant SSH.
- Autoscaler at max, CPU 100% → **raise max**. Autoscaling stuck after growth → **quotas**.
- Rolling-update outages in GKE → **readiness/liveness probes**.
- Load test → expected concurrency, **separate project**, metrics on both sides, never production.
- Patch VM fleets → **VM Manager + OS Config agent + patch jobs**.
