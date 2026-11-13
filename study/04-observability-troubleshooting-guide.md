# Domain 4 Study Guide — Implementing Observability Practices and Troubleshooting Issues

> Condensed from the question bank in [04-observability-troubleshooting.md](04-observability-troubleshooting.md) (69 questions, Exams 1–5). Citations look like (Exam N · QM). Some questions appear twice across exams, and both are cited.

---

## Contents

1. [Cloud Logging: sinks, aggregated sinks and destinations](#1-cloud-logging-sinks-aggregated-sinks-and-destinations)
2. [Cloud Logging: exclusions, log buckets, retention and cost](#2-cloud-logging-exclusions-log-buckets-retention-and-cost)
3. [Sensitive data / PII in logs](#3-sensitive-data--pii-in-logs)
4. [Log-based metrics](#4-log-based-metrics)
5. [Log collection: Ops Agent, GKE, Cloud Run](#5-log-collection-ops-agent-gke-cloud-run)
6. [Cloud Monitoring metrics: kinds, types and built-in metrics](#6-cloud-monitoring-metrics-kinds-types-and-built-in-metrics)
7. [Prometheus on GKE and hybrid metrics (GMP, OpenTelemetry, Bindplane)](#7-prometheus-on-gke-and-hybrid-metrics)
8. [Metrics scopes, dashboards and sharing](#8-metrics-scopes-dashboards-and-sharing)
9. [Alerting, notification channels, uptime checks and synthetic monitors](#9-alerting-notification-channels-uptime-checks-and-synthetic-monitors)
10. [Trace, Profiler and Error Reporting](#10-trace-profiler-and-error-reporting)
11. [Network observability and troubleshooting](#11-network-observability-and-troubleshooting)
12. [Troubleshooting performance and resource problems](#12-troubleshooting-performance-and-resource-problems)
13. [IAM roles for observability](#13-iam-roles-for-observability)
14. [⚠️ Questionable answers](#️-questionable-answers)
15. [Last-minute cheat sheet](#last-minute-cheat-sheet)

---

## 1. Cloud Logging: sinks, aggregated sinks and destinations

### Key facts
- A **sink** routes log entries that match a filter to **one destination**. Two destinations need at least two sinks (Exam 2 · Q16).
- An **aggregated sink** on a **folder** or **organization** covers all child projects, **including projects created later**. A project-level sink covers only its own project (Exam 2 · Q9, Exam 2 · Q16, Exam 4 · Q9).
- Filtering an org-level sink by project ID does **not** follow future projects, and filters are limited to 20,000 characters (Exam 2 · Q16).
- The Log Router itself costs nothing extra, but you still pay for storage at the destination (Exam 3 · Q25).
- New sinks to Cloud Storage can take hours to start routing and are processed hourly, so they are a poor fit for real-time needs (Exam 1 · Q28).

### Destination comparison

| Destination | Use it when the question says… | Don't use it for… | Source |
|---|---|---|---|
| **Cloud Storage bucket** | "archive", "cheapest", "years", "immutable" (add a **retention policy + Bucket Lock**) | real-time dashboards (it is processed hourly) | Exam 2 · Q9, Exam 2 · Q43, Exam 1 · Q28 |
| **BigQuery dataset** | SQL analysis, live dashboard in Data Studio/Looker Studio, "central repository for analysis" | locked retention (BigQuery expiration can be changed) or the cheapest cold archive | Exam 1 · Q28, Exam 3 · Q25, Exam 2 · Q9 |
| **Pub/Sub topic** | an external **SIEM** or third-party tool that "ingests via Pub/Sub", or streaming to another system | storage: retention is only weeks (31 days max) | Exam 4 · Q9, Exam 2 · Q43, Exam 4 · Q53 |
| **Cloud Logging (log) bucket** | centralize logs and still query and alert natively in Cloud Logging, or set custom retention (for example, 365 days) | consumers that can read only Pub/Sub | Exam 2 · Q25, Exam 4 · Q53 |

### Decision rules
- "Every current **and future** project in the org" → **org-level aggregated sink** (Exam 4 · Q9, Exam 2 · Q9).
- "Only projects in the Prod folder" → **folder-level aggregated sink** (Exam 2 · Q25).
- "Dev logs → dev_dataset, Prod logs → prod_dataset, fewest sinks, future projects" → **one aggregated sink per folder** (Exam 2 · Q16).
- "7-year regulatory retention, guard against human error" → **org aggregated sink → Cloud Storage + locked retention policy** (Exam 2 · Q9).
- "Archive 7 years at lowest cost" → **named sink → Cloud Storage bucket** (Exam 2 · Q43).
- "Security team wants alerting plus near-real-time analysis on the logs" (no external SIEM) → **folder sink → Cloud Logging bucket**, not Pub/Sub (Exam 2 · Q25).
- "SIEM ingests only through Pub/Sub" → **org sink → Pub/Sub topic** (Exam 4 · Q9).
- "Interactive, shareable, real-time dashboard with quarterly aggregation" → **sink → BigQuery → Data Studio** (Exam 1 · Q28).
- "GKE + Cloud Run logs into BigQuery, low cost and complexity" → **native Cloud Logging collection + sink to BigQuery** (Exam 3 · Q25).

### Traps
- Check **scope** and **destination** separately. Each distractor usually gets one of them right (Exam 2 · Q9, Exam 4 · Q9).
- "Repeat for each folder" still misses folders created later. The organization level is the only fully automatic scope (Exam 4 · Q9).
- Pub/Sub *can* be a sink destination, but it is transport, not storage (Exam 2 · Q43, Exam 2 · Q25).
- Exporting to BigQuery and then to CSV and Google Sheets gives a **static snapshot**, not a live dashboard. Sheets also refreshes no more often than every 15 minutes (Exam 1 · Q28).
- Avoid custom apps that write logs directly to BigQuery or Cloud Storage, App Engine "pullers", Datadog relays and manual uploads. Use native collection plus a sink (Exam 2 · Q43, Exam 3 · Q25).

---

## 2. Cloud Logging: exclusions, log buckets, retention and cost

### Key facts
- An **exclusion filter** stops matching entries from being ingested and stored. It is **not** an access control (Exam 4 · Q6).
- A sink's **export** sends a *copy* and does not stop the original from being kept in `_Default`. To capture entries elsewhere *and* keep them out of Cloud Logging, you need **sink + exclusion** (Exam 1 · Q16).
- For high-volume workloads, the cost driver is **ingestion volume**, not retention length (Exam 3 · Q33).
- Log-based metrics are still evaluated on entries that exclusions drop, so metrics recover visibility into excluded logs (Exam 3 · Q33).
- A custom log bucket can have its retention set (for example, **365 days**). Combine it with a sink, then give the consumer access (Exam 4 · Q53).
- Disabling the `_Default` sink (`gcloud logging sinks update _Default --disabled`) stops **all** routing into `_Default` for the project, including system logs (Exam 4 · Q41).

### Decision rules
- "Cut cost of terabytes/day, keep critical ops/security info" → **exclude all non-ERROR logs + build log-based metrics for key indicators** (Exam 3 · Q33).
- "GKE dev cluster: drop app logs (devs use `kubectl logs`), keep operational logs" → `gcloud container clusters update --logging=SYSTEM` (Exam 4 · Q41).
- "Keep logs 1 year for client to import, minimal code changes" (Cloud Run) → **custom log bucket with 365-day retention + sink + client access** (Exam 4 · Q53).
- "Retention and sharing" → a bucket-and-sink problem, not a code problem (Exam 4 · Q53).

### Traps
| Distractor | Why it's wrong | Source |
|---|---|---|
| Exclude only DEBUG | INFO (the bulk of the volume) is still ingested | Exam 3 · Q33 |
| Shorten `_Default` retention to 15 days | Doesn't reduce ingestion, and you lose investigation data | Exam 3 · Q33 |
| Sample across all severities | Drops ERROR/security entries too | Exam 3 · Q33 |
| `--logging=WORKLOAD` | That is the app-log source, the opposite of the goal. `SYSTEM` is required on all cluster types | Exam 4 · Q41 |
| Exclusion `resource.type="k8s_container"` | Also matches system Pods and filters after collection. Excluding GKE logs can leave nothing to share with Support | Exam 4 · Q41 |
| Pub/Sub for 1-year retention | 31-day maximum | Exam 4 · Q53 |

> Answer flip: use an exclusion filter (instead of `--logging=SYSTEM`) if you must keep *part* of the app logs, or on **Autopilot** (Exam 4 · Q41).

---

## 3. Sensitive data / PII in logs

| Goal in the stem | Mechanism | Source |
|---|---|---|
| Capture the PII entries securely **and** stop retaining them in Cloud Logging | **Advanced filter → sink to Cloud Storage + exclusion with the same filter** | Exam 1 · Q16 |
| Stop specific fields from being written to *new* entries **as fast as possible** (Compute Engine, logging agent) | Agent-side Fluentd **`filter_record_transformer`** (built-in filter, `remove_keys`) | Exam 2 · Q41 |
| Keep the log, hide **one field** from most people, let one group see it | Mark `jsonPayload.<field>` as a **restricted field** on the log bucket + grant **Log Field Accessor** (`roles/logging.fieldAccessor`) to that group | Exam 4 · Q6 |
| Collect GKE app logs but never expose PII | **Sensitive Data Protection** inspection/redaction *before* storing (a preprocessing integration, not a built-in Cloud Logging toggle) | Exam 3 · Q2 |

### Traps
- **Encryption ≠ redaction.** An encrypted bucket still shows PII to authorized readers (Exam 3 · Q2).
- **Sampling** reduces volume but does not remove PII, and **disabling logging** breaks the "must collect" requirement (Exam 3 · Q2).
- **Exclusion** to hide a field drops the whole entry and breaks mandatory capture (Exam 4 · Q6).
- A conditional IAM binding (`resource.name.extract(".../buckets/{bucket}/") == "_Default"`) is real syntax, but on its own it hides nothing (Exam 4 · Q6).
- `fluent-plugin-record-reformer` is an add-on gem framed as an output plugin. The built-in filter is the answer (Exam 2 · Q41).
- "Wait for developers to patch" is the long-term root-cause fix, not the *fastest* one (Exam 2 · Q41).
- Gating a field behind an environment variable plus CODEOWNERS controls *whether* data is written, not *who can view* it (Exam 4 · Q6).

---

## 4. Log-based metrics

### Key facts
- Log-based metrics turn a log filter into a time series that you can chart and alert on in Cloud Monitoring (Exam 1 · Q18, Exam 5 · Q10).
- User-defined log-based metric types are **counter** and **distribution**. **Boolean is not a supported metric type** (a Boolean *label* is) (Exam 3 · Q59).
- You can **extract a field as a label** (for example, `matchedFieldName`) and group charts by it (Exam 3 · Q59).

### Decision rules
- "How often does log event X happen over time" (cache misses) → **log-based metric + Cloud Monitoring dashboard** (Exam 1 · Q18, Exam 5 · Q10).
- "Requests from a specific IP" with Ops Agent installed → **Ops Agent logging receiver (access logs) + log-based metric** (Exam 2 · Q3, Exam 5 · Q28).
- "Cloud Armor blocked requests for `/api` prefix, broken down by parameter name" → **counter metric filtered on `configuredAction="DENY"` + `requestUrl` prefix, label = `matchedFieldName`** (Exam 3 · Q59).

### Traps
- A Data Studio/Looker Studio link to Cloud Logging is not a native path (it typically needs a BigQuery export first) (Exam 1 · Q18).
- Profiler cannot read logs (Exam 1 · Q18).
- A BigQuery sink plus scheduled queries is overkill for a simple frequency chart (Exam 1 · Q18).
- An Ops Agent **metrics receiver** reports fixed metric sets and **can't break traffic down by client IP** (Exam 2 · Q3).
- `networksecurity.googleapis.com/https/request_count` with `blocked=true` gives totals only, with no URL or parameter dimension (Exam 3 · Q59).
- Filtering on `configuredAction="ALLOW"` selects permitted traffic, which is the wrong half (Exam 3 · Q59).
- A log-based metric + alert tells you **that** requests are slow, not **where** they are slow (Exam 3 · Q18).

---

## 5. Log collection: Ops Agent, GKE, Cloud Run

### Compute Engine
- VMs **do not** have the agent by default. "New app's logs missing" → first confirm the **Ops Agent is installed** (Exam 2 · Q55).
- "Logs missing, legacy agent" → first check whether the agent **process is running** (`ps ax | grep fluentd`) before reinstalling or checking scopes (Exam 1 · Q51).
- Writing logs requires the `logging.write` scope, which `cloud-platform` already covers. `monitoring.write` belongs to the monitoring agent (Exam 1 · Q51).
- "Agent running + public IP + no logs + user-managed SA" → grant the SA **Logs Writer** (`roles/logging.logWriter`). Don't export keys, switch to the default SA, or enable Private Google Access (PGA only matters for VMs with no external IP) (Exam 4 · Q25).
- "Every current **and future** VM, keep agent **up to date**" → **agent policy** via gcloud. A one-off install from the dashboard, a script over an Asset Inventory snapshot, or baking the agent into an image won't keep it current (Exam 2 · Q26).
- Developers need app logs with least config and least privilege → logging agent (today: **Ops Agent**) + **Logs Viewer** (Exam 1 · Q46, Exam 5 · Q3).
- The legacy logging and monitoring agents are end-of-support. The **Ops Agent** collects both logs and metrics (Exam 1 · Q46, Exam 1 · Q51).

**Troubleshooting order for missing VM logs** (synthesized from Exam 2 · Q55, Exam 1 · Q51 and Exam 4 · Q25): agent installed? → agent process running? → service account has Logs Writer? → (only if no external IP) network path / PGA.

### GKE
- The built-in node agent collects only **stdout/stderr** + system logs, not files inside containers (Exam 1 · Q48).
- "Third-party app writes to `/var/log/app_messages.log`, can't be modified" → **sidecar that tails the file to stdout + shared volume** (Exam 1 · Q48).
  - Trap: a custom Fluentd DaemonSet can't see a file inside a container without a host-mounted volume, and it adds a second agent to maintain. Pick it only if the file is already on a host path (Exam 1 · Q48).
- `--logging=SYSTEM` = operational logs only. `WORKLOAD` = application logs (Exam 4 · Q41).

### Cloud Run
- stdout/stderr capture is automatic, and there is **no customer-installable agent**. A line becomes `jsonPayload` only if it is written as a single valid JSON object (Exam 4 · Q20).
- "Make logs structured JSON" → change the app to use the **Cloud Logging client library and emit JSON**. A Fluent Bit sidecar or "agent converts text to JSON" are wrong (Exam 4 · Q20).

---

## 6. Cloud Monitoring metrics: kinds, types and built-in metrics

### Metric kind / value type
| Need | Choice | Source |
|---|---|---|
| Latency experienced by **all** users (spread, percentiles, tail) | `valueType=DISTRIBUTION`, `metricKind=GAUGE` (custom metric), **Heatmap** chart | Exam 1 · Q1, Exam 5 · Q13 |
| Running total | CUMULATIVE (scalar, shown as a Line chart), which is *not* a distribution | Exam 1 · Q1 |
| `METRIC_KIND_UNSPECIFIED` | API placeholder, never a valid choice | Exam 1 · Q1, Exam 5 · Q13 |

- Scalar types (DOUBLE, INT64) collapse each interval into one number and hide the tail (Exam 1 · Q1).
- "No load balancer" means there are no managed LB latency metrics, so the app must emit its own custom metric (Exam 1 · Q1).

### Built-in metrics that were tested
| Question asks | Metric | Distractor | Source |
|---|---|---|---|
| App Engine (flex) current connections, whole app | `flex/connections/current` | `flex/instance/connections/current` (per instance); `tcp_ssl_proxy/*` (load balancer metrics) | Exam 1 · Q33 |
| Which **Pods** cause node DiskPressure (no exec) | `container/ephemeral_storage/used_bytes` in Metrics Explorer, grouped by pod | `node/ephemeral_storage/used_bytes` (shows which nodes, not which Pods); `df` (needs exec) | Exam 4 · Q23, Exam 5 · Q39 |
| Containers using the most CPU/memory (hybrid GKE) | Built-in **Kubernetes Engine monitoring** (Cloud Operations for GKE) | Prometheus "collecting logs", custom metrics + groups, logs → BigQuery | Exam 1 · Q38, Exam 5 · Q42 |

### Getting app metrics in
- New GKE app, centralized app-level metrics, minimal setup → **OpenTelemetry client libraries with a Cloud Monitoring exporter**. Writing directly to the Monitoring API is the *most* manual path. Pub/Sub has no metric semantics, and log-based metrics are awkward for histograms or gauges (Exam 1 · Q24).
- Custom metrics are for data Cloud Monitoring does **not** already collect. Container CPU and memory are already system metrics (Exam 1 · Q38).

---

## 7. Prometheus on GKE and hybrid metrics

### Key facts
- **Google Cloud Managed Service for Prometheus (GMP)** with **managed collection** stores data in Cloud Monitoring's backend (global, highly available). You query it with **PromQL** in Metrics Explorer (or Grafana pointed at it), and it covers custom workload metrics **and** GKE default metrics (Exam 2 · Q15, Exam 3 · Q22, Exam 3 · Q32, Exam 4 · Q13).
- The Ops Agent's Prometheus receiver is for **Compute Engine VMs**. For GKE, Google recommends managed collection (Exam 3 · Q22).
- GMP data is **not** queried from BigQuery (Exam 4 · Q13).
- **Bindplane** is Google's documented OpenTelemetry pipeline that brings on-prem/hybrid telemetry into Cloud Monitoring, at no extra cost to Cloud Observability customers (Exam 3 · Q50).

### Decision rules
- "Already emit Prometheus metrics on GKE, least maintenance" → **enable GMP managed collection** (Exam 3 · Q32).
- "Many clusters, global PromQL view, low overhead" → **GMP**, not hierarchical or cross-service federation (Exam 2 · Q15).
- "Multi-project GKE Prometheus + flexible query" → **GMP managed collection + Metrics Explorer, with a metrics scope for cross-project** (Exam 3 · Q22).
- "HA, custom + default GKE metrics, all clusters" → **managed collection + query in Cloud Monitoring** (Exam 4 · Q13).
- "On-prem K8s + several GCP projects, OpenTelemetry, one place, easy to support" → **scoping project + Bindplane** (Exam 3 · Q50).
- "GMP managed collection, metrics missing, **no errors**" → validate the **port in the `PodMonitoring` resource** (exporter/scrape config). Check the write quota only if you see HTTP **429** errors (Exam 3 · Q21).

### Traps
| Distractor | Why not | Source |
|---|---|---|
| Self-run Prometheus / Prometheus Operator + remote-write / Thanos / Grafana | You operate every tier, so overhead is not minimized | Exam 4 · Q13, Exam 3 · Q32, Exam 3 · Q50 |
| Hierarchical federation | Works, but self-managed. Correct only if a managed service is forbidden | Exam 2 · Q15 |
| Cross-service federation | Combines one service's metrics with another's; it is not a global roll-up | Exam 2 · Q15 |
| "Workload metrics within Cloud Observability for GKE" | Not the Prometheus-compatible PromQL/Grafana path the team relies on | Exam 2 · Q15 |
| Self-deployed OTel Collector for Prometheus metrics on GKE | Valid, but it is extra infrastructure. GMP is the primary recommendation | Exam 3 · Q32 |
| `roles/monitoring.servicesViewer` | SLO/service read-only. Ingestion needs Monitoring Metric Writer | Exam 3 · Q21 |
| Installing Grafana | Optional UI that fixes nothing about scraping | Exam 3 · Q21 |

---

## 8. Metrics scopes, dashboards and sharing

### Key facts
- A **metrics scope** lets a **scoping project** view metrics from multiple monitored projects. "Workspaces" are the legacy name (Exam 1 · Q50, Exam 2 · Q25).
- A metrics scope consolidates **metrics, not logs** (Exam 2 · Q25).
- Dashboards are project-scoped and governed by that project's IAM (Exam 4 · Q54).

### Decision rules
- "Dashboards showing only one folder's projects (Dev/Staging/Prod)" → **a new scoping project per folder** (don't reuse an app project) (Exam 5 · Q54).
- "Share one chart with the SRE team only, least privilege" → **share chart by URL + `roles/monitoring.viewer`** on the scoping project (Exam 1 · Q50, Exam 5 · Q1).
- "Dev team should keep using *the same live* dashboard" → **`roles/monitoring.viewer` + dashboard URL**, not `roles/viewer` (too broad) and not a JSON/CSV export (Exam 3 · Q51).
- "Share a dashboard with a **partner team**" (no access to your project) → **export the dashboard JSON** so they can import their own copy (Exam 4 · Q54).

### Sharing comparison
| Situation | Answer | Why the others lose |
|---|---|---|
| Internal team, same project, live data | URL + Monitoring Viewer | Dashboard Configuration Viewer can't read metric data (charts error out); a project ID alone doesn't deliver the chart (Exam 1 · Q50, Exam 5 · Q1) |
| Internal team continues an investigation | URL + Monitoring Viewer | `roles/viewer` is a broad basic role; exports are static (Exam 3 · Q51) |
| External/partner team | Export JSON definition | The URL needs project access; a single MQL query is only a fragment; Data Studio is a rebuild (Exam 4 · Q54) |

---

## 9. Alerting, notification channels, uptime checks and synthetic monitors

### Notification channels
- **Native channels**: email, **SMS**, mobile app push, PagerDuty, Slack, webhooks, Pub/Sub. "SMS for critical alerts" → team members **add and verify phone numbers as SMS channels**, then attach them to the policies (Exam 1 · Q3).
- Webhooks are for systems with no purpose-built integration. Don't chain Slack→SMS or a webhook→SMS gateway (Exam 1 · Q3).
- **Webhook channels require public endpoints.** For an alerting platform reachable **only inside the VPC** → **Pub/Sub channel + pull subscription** consumed from inside the VPC. A push subscription can't reach a private address. A Cloud Run function with Direct VPC egress works but is not the recommended pattern (Exam 3 · Q53).

### SLO / alert design
- "Notify before the error budget runs out" → **SLO error-budget burn-rate alert**, not a latency threshold, log-anomaly alert or daily emailed report (Exam 3 · Q39).
- "Alerts for self-healing restarts (recover in under a minute) are burning out staff" → **stop alerting on conditions that need no human action**. Don't change the SLO, spread pages across time zones, or file an incident report per alert (Exam 4 · Q48).

### Probing
| Need | Tool | Source |
|---|---|---|
| Recurring test of a **multi-step business journey** (checkout) + alert on failure | **Synthetic monitor** (a Cloud Run function) + alerting policy | Exam 3 · Q26 |
| Endpoint availability / response check | Uptime check (stateless, independent requests) | Exam 3 · Q26 |
| Availability of **internal-only** APIs in a private VPC | **Private uptime checks** (they use Service Directory). No relay function or VPN needed | Exam 3 · Q40 |
| Detect logged errors (passive) | Log-based alert (doesn't execute any test) | Exam 3 · Q26 |

- Traps: Workflows + Cloud Tasks (Cloud Tasks isn't a cron scheduler) (Exam 3 · Q26). Liveness/readiness probes are kubelet restart/routing signals, not an alertable availability metric (Exam 3 · Q40, Exam 2 · Q32).

### Service Health
- "Dashboard must distinguish our failures from Google Cloud incidents" → enable **Personalized Service Health event annotations** on the dashboard (Exam 3 · Q5).

---

## 10. Trace, Profiler and Error Reporting

### Comparison
| Tool | Answers | Choose when the stem says… | Source |
|---|---|---|---|
| **Cloud Trace** (OpenTelemetry) | **Where** time goes across services: per-request spans and waterfall | "downstream dependencies", "which service is slow", "root cause of latency" across microservices | Exam 1 · Q54, Exam 2 · Q11, Exam 2 · Q32, Exam 3 · Q18 |
| **Cloud Profiler** | Which **code inside one process** burns CPU/memory | "CPU spiked after release", "which function allocates most memory" | Exam 2 · Q11, Exam 1 · Q36 |
| **Error Reporting** | Groups failures and exceptions | "failed requests increased", "exceptions" | Exam 2 · Q11 |
| **Metrics / Prometheus** | **That** something is slow (aggregate numbers) | trends, alerting | Exam 2 · Q11, Exam 2 · Q32 |
| **Cloud Debugger** | — | **Never.** Deprecated in 2022 and shut down in May 2023 | Exam 1 · Q8, Exam 1 · Q54 |

- Rule of thumb: **metrics say that it's slow, traces say where, Profiler says which code, Error Reporting says what failed** (Exam 2 · Q11, Exam 2 · Q32).
- Time spent waiting on a dependency is mostly idle time, so a CPU profile misses it (Exam 2 · Q11).
- VPC Flow Logs, health probes and a Dataflow metrics pipeline can't attribute per-request latency (Exam 2 · Q32).
- Logging call durations yourself gives only the caller's side, needs code changes and needs manual correlation (Exam 1 · Q54).
- Scaling up (HPA) or rolling back are actions to take *after* the root cause is known. They are not diagnosis (Exam 3 · Q18).

### Trace specifics
- **Correlate logs with a slow trace**: make sure the logging config writes the **trace ID from the OTel context into each structured log entry**, then use **"Show logs"** in the Cloud Trace details view. Querying Logs Explorer by trace ID or joining in BigQuery assumes the correlation already exists and is slower (Exam 3 · Q36).
- **Apigee**: trace only the affected proxy with a **proxy-scoped trace configuration override**. An environment-wide trace adds overhead to every proxy (Exam 3 · Q49).
- **Cloud Run + OTel agent, inconsistent traces** → **instance-based billing (CPU always allocated)**, because request-based billing throttles CPU after the response. Adding vCPUs adds capacity, not availability (Exam 3 · Q3).

### Error Reporting
- It is enabled automatically on App Engine flexible. To **customize** error details → build **`ReportedErrorEvent`** objects yourself through the Error Reporting API (or as matching log entries). Installing the library gives only default capture, and moving to GCE or GKE is irrelevant (Exam 2 · Q46).

---

## 11. Network observability and troubleshooting

| Need | Tool | Source |
|---|---|---|
| Forensic capture of an intermittent malicious process | **VPC Flow Logs, sampling 1.0**, on the **implicated env only** (prod frontend + backend subnets), no test-first rollout | Exam 1 · Q11 |
| Record **each** source IP hitting a port an existing firewall rule allows, fewest steps | **Enable firewall rules logging** on that rule (a passthrough NLB keeps client IPs) | Exam 2 · Q13 |
| Which **layer** of a cross-VPC path is broken, **no exec access** | **Connectivity Tests** (Network *Intelligence* Center): simulates routes, firewalls, forwarding rules and peering | Exam 2 · Q4 |
| Full packet payload inspection | Packet Mirroring (needs collectors behind an internal NLB; doesn't write to Cloud Logging) | Exam 2 · Q13 |

- VPC Flow Logs sample packets and aggregate them per connection, are enabled per subnet, and don't explain *why* traffic was denied. Firewall rules logging covers denials (Exam 2 · Q4, Exam 2 · Q13).
- Toolbox or debug containers and `traceroute` violate a "no exec" constraint (Exam 2 · Q4).
- The answer flips to Flow Logs for broad analysis (volume trends, top talkers) (Exam 2 · Q13).

---

## 12. Troubleshooting performance and resource problems

| Symptom | Most probable cause / action | Distractors | Source |
|---|---|---|---|
| Cloud SQL timeouts after an app update, **same user count** | Check whether **Cloud SQL connections increased** | Serial port logs (boot/OS), Profiler (in-process), Web Security Scanner (vuln scanner, not DDoS) | Exam 1 · Q36 |
| After a spike, latency stays high; **Cloud SQL and Cloud Storage requests equally slow**; no errors | Shared layer = App Engine instances → **keep more idle instances** | Multi-region GCS, Cloud SQL HA (that's availability, not latency), migrate to GCE | Exam 2 · Q57 |
| Half the Pods `OOMKilled`, HPA at minimum replicas | **Raise the container memory limit** | Bigger nodes, more nodes, higher HPA max (it doesn't trigger scaling) | Exam 3 · Q23 |
| Node DiskPressure, which Pods, no exec | `container/ephemeral_storage/used_bytes` | node metric, `df` | Exam 4 · Q23, Exam 5 · Q39 |
| Need CPU/memory utilization for an app inside and outside GCP, minimal setup | Cloud Profiler library (keyed answer; see ⚠️) | Debugger (dead), custom scrape endpoint, third-party APM | Exam 1 · Q8 |

- Method: start with the signal closest to the symptom, run diagnostics before making changes, and match the fix to the resource boundary that is failing (Exam 1 · Q36, Exam 1 · Q51, Exam 3 · Q23).
- `OOMKilled` can also be node-level memory exhaustion. Confirm which boundary was exceeded (Exam 3 · Q23).

---

## 13. IAM roles for observability

| Role | Grants | Use when | Source |
|---|---|---|---|
| `roles/logging.configWriter` (Logs Configuration Writer) | Create and manage sinks + log-based metric configs | "Let team members **export logs**" | Exam 1 · Q13 |
| `roles/logging.viewer` (Logs Viewer) | Read ordinary logs | Developers troubleshoot app logs | Exam 1 · Q46, Exam 5 · Q3 |
| `roles/logging.privateLogViewer` (Private Logs Viewer) | + private logs such as **Data Access audit logs** | Only if they need Data Access logs | Exam 1 · Q46 |
| `roles/logging.logWriter` (Logs Writer) | Write log entries | VM service account whose agent can't write | Exam 4 · Q25 |
| `roles/logging.fieldAccessor` (Log Field Accessor) | See **restricted fields** on a bucket | PII field visible only to the security team | Exam 4 · Q6 |
| `roles/monitoring.viewer` (Monitoring Viewer) | Read metric data + dashboards | Share a chart or dashboard (least privilege) | Exam 1 · Q50, Exam 3 · Q51, Exam 5 · Q1 |
| Monitoring Dashboard Configuration Viewer | Dashboard **definitions only**, no metric data | Almost never (charts won't render) | Exam 1 · Q50 |
| `roles/monitoring.servicesViewer` | Read services/SLOs | Not for ingestion problems | Exam 3 · Q21 |
| Monitoring Metric Writer | Write metrics | Ingestion identity | Exam 3 · Q21 |

### Traps
- A custom role with `logging.sinks.list` + `logging.sinks.get` is read-only and can't **create** a sink (Exam 1 · Q13).
- Access Context Manager (context perimeters) and Organization Policy (resource constraints) don't grant permission for an action (Exam 1 · Q13).
- `roles/viewer` works but is too broad (Exam 3 · Q51).
- Don't export service account keys, and don't fall back to the default Compute Engine SA. Grant the missing role to the attached SA (Exam 4 · Q25).

---

## ⚠️ Questionable answers

| Question | Issue |
|---|---|
| **Exam 1 · Q8** (Cloud Profiler for "system resource utilization" metrics, hybrid) | Profiler is code-level CPU/heap profiling attributed to functions. Other explanations in this bank say so (Exam 1 · Q18, Exam 2 · Q11, Exam 1 · Q36), and it does not produce system resource-utilization metrics. The bank's own memory hook adds "(or the Ops/Monitoring agent)". Profiler is the least-bad option listed, but on a real exam an **Ops Agent / Cloud Monitoring** option would beat it. |
| **Exam 5 · Q3** explanation | Says Private Logs Viewer is for "admin activity and system logs". In fact, private logs are mainly **Data Access audit logs**, as Exam 1 · Q46 correctly states, and Admin Activity logs are readable with Logs Viewer. The answer (A) is right; the reasoning is wrong. |
| **Exam 5 · Q13** explanation | Rejects INT64 because latency is "floating-point" and calls DELTA "rate-based". These are weak reasons. The stronger reasoning in Exam 1 · Q1 is that any scalar loses the distribution. The keyed answer (GAUGE + DISTRIBUTION + Heatmap) stands. The claim in Exam 1 · Q1 that DELTA-kind DISTRIBUTION is disallowed for custom metrics is stated without detail, so don't lean on it beyond this question. |
| **Exam 5 · Q28** explanation | Rejects the Ops Agent metrics receiver only because it "likely requires more configuration". The real reason, given in Exam 2 · Q3, is that a metrics receiver **can't break down by client IP** at all. |
| **Exam 2 · Q4** option text | The keyed option says "Network **Connectivity** Center" runs Connectivity Tests. Connectivity Tests belong to **Network Intelligence Center**, as the explanation itself admits. Pick it by capability, but know the real product name. |
| **Exam 1 · Q11** vs **Exam 2 · Q13** | Exam 1 · Q11 treats Flow Logs at sampling 1.0 as capturing every flow. Exam 2 · Q13 says Flow Logs have a dynamic, non-adjustable primary sampling and can't guarantee every IP. Both keyed answers are defensible in context. Know that "sampling 1.0" is the most complete Flow Logs setting, not a guarantee of every packet. |
| **Exam 2 · Q41**, **Exam 1 · Q16**, **Exam 1 · Q51** | These are built on the **legacy Fluentd-based logging agent**, which is end-of-support per Exam 1 · Q46. Learn the principle (scrub at the agent; check that the agent process is running) rather than the Fluentd plugin and process names. |
| **Exam 3 · Q2** | The keyed answer describes Sensitive Data Protection redacting "before storing in Cloud Logging". The explanation admits this is a custom preprocessing integration, not a Cloud Logging setting. If a question offers native options such as restricted fields (Exam 4 · Q6) or agent-side removal (Exam 2 · Q41), prefer those when they fit. |
| **Exam 5 · Q1** explanation | Says Monitoring Viewer via a project ID "shares all dashboards", while via a URL it doesn't. The role grants the same access either way; the URL only *delivers* the chart. The answer is right; the over-sharing argument is not. |

---

## Last-minute cheat sheet

- **One sink = one destination**; folder or org **aggregated sinks** cover future projects.
- Archive cheaply for years → sink → **Cloud Storage**; immutable → **retention policy + Bucket Lock**.
- External SIEM → **Pub/Sub** (it is transport, with ≤31-day retention, never an archive).
- Keep querying and alerting in Logging → sink to a **Cloud Logging bucket**; 1-year retention → custom log bucket with 365 days.
- Live, shareable SQL dashboard on logs → sink → **BigQuery → Data Studio/Looker Studio**, with no CSV step.
- Capture elsewhere **and** keep out of Logging → **sink + exclusion**.
- Cut cost → **exclude non-ERROR + log-based metrics**; retention length isn't the cost driver.
- GKE: drop app logs but keep ops logs → `--logging=SYSTEM`.
- Hide one PII field → **restricted field + Log Field Accessor**; strip at the source fast → filter in the agent.
- "How often does log X happen" or "requests by IP" → **log-based metric** (counter/distribution, not Boolean).
- Latency for all users → **DISTRIBUTION + GAUGE + Heatmap**.
- Missing VM logs → agent installed? → running? → SA has **Logs Writer**?
- Current + future VMs, agent kept current → **Ops Agent agent policy**.
- GKE file logs from an unmodifiable app → **sidecar tail to stdout + shared volume**.
- Cloud Run structured logs → **client library emitting JSON** (no agent on Cloud Run).
- Prometheus on GKE, low ops, global PromQL → **Managed Service for Prometheus**; missing metrics with no errors → check the `PodMonitoring` port.
- On-prem OTel + multiple projects → **scoping project + Bindplane**.
- Slow across services → **Trace**; hot code → **Profiler**; exceptions → **Error Reporting**; Debugger is dead.
- Logs ↔ trace → put the **trace ID in structured logs**, then **"Show logs"** in Trace.
- Cloud Run OTel background export → **instance-based billing (CPU always allocated)**.
- Share a dashboard internally → **URL + `roles/monitoring.viewer`**; partner team → **export JSON**.
- Folder-only dashboards → **one scoping project per folder**.
- SMS alerts → native **SMS channel**; private webhook → **Pub/Sub channel + pull subscription**.
- "Before the error budget runs out" → **burn-rate alert**; self-healing, non-actionable → **don't page**.
- Business journey → **synthetic monitor**; private endpoint → **private uptime check**; GCP incident context → **Service Health annotations**.
- Each source IP on an allowed port → **firewall rules logging**; broken path with no exec → **Connectivity Tests**.
- Which Pods cause DiskPressure → `container/ephemeral_storage/used_bytes`; `OOMKilled` at min replicas → raise the **memory limit**.
- DB timeouts with flat load after a release → check **Cloud SQL connections**; equal slowness across backends → the **shared serving layer** (App Engine idle instances).
