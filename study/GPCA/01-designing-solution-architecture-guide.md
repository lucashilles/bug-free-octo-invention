# Domain 1 Study Guide — Designing and Planning a Cloud Solution Architecture

> Condensed from the 84-question bank in [`01-designing-solution-architecture.md`](01-designing-solution-architecture.md). Citations look like (Exam N · QM). Many older scenarios repeat with newer product names, so look for the paired citations.

---

## 1. Requirements, assessment and migration planning

### Key facts
- An architect's first move is to **understand the requirements**, then evaluate options against them. A team that worries its logging tool is not good enough → work with them to define requirements and evaluate tools, not "install the agent" or "send them links" (Exam 1 · Q4).
- Google's migration path is **assess → plan → deploy → optimize**. Assessment discovers the inventory and dependencies; the plan groups workloads into waves; only then do you move them.
- **Migration Center** is Google's assessment hub. It collects inventory and utilization from your current environment (discovery client or imported data) and produces **TCO and cost estimates** for running those workloads on Google Cloud. For a quick, best-practice cost estimate of on-prem compute and SAP workloads → collect environment details and use Migration Center (Exam 5 · Q42).
- **Migrate to Virtual Machines** (formerly Migrate for Compute Engine) moves VMware, AWS, Azure and physical VMs to Compute Engine. The best-practice sequence for lifting and shifting RHEL VMs from VMware is: **assess the VMs, define a migration plan, prepare a runbook, execute** (Exam 2 · Q39).
- Migrating a J2EE application, the classic best-practice trio is: move to a **managed platform** (App Engine in the question), **automate provisioning with infrastructure as code**, and run **CI with automated tests in staging** (Exam 1 · Q3). Rewriting MySQL to NoSQL or adding Dataflow "for metrics" are not migration best practices.
- **Bring your own license (BYOL) for Windows Server** requires **sole-tenant nodes** (dedicated hardware, to satisfy Microsoft licensing). Import the on-prem image as a BYOL image, then boot a sole-tenant VM from it. A standard Windows image from Google is pay-as-you-go and already includes a license (Exam 4 · Q8).
- A migration plan for analytics includes **evaluating ETL code moving to Dataflow** and a **schema plan to denormalize for BigQuery** (Exam 4 · Q30). Loading 10 TB of analytics into Cloud SQL, or moving to a "MySQL cluster", repeats the old problem.
- A team new to Kubernetes that wants low ops → **assess the app and its dependencies for containerization, then plan a move to GKE Autopilot** (Exam 5 · Q79). Autopilot manages nodes, scaling and security settings for you; Standard leaves node management to you.

### Decision rules
- "First step", "help them choose a tool" → **gather and define requirements** (Exam 1 · Q4).
- "Quick cost estimate for migrating on-prem workloads" → **Migration Center**, not the Pricing Calculator with guessed numbers, Cloud Asset Inventory (which only sees Google Cloud resources), or a full partner engagement (Exam 5 · Q42).
- "Lift and shift VMware VMs, best practice" → **assess, plan, runbook, migrate with Migrate to Virtual Machines** (Exam 2 · Q39).
- "Bring existing Windows Server licenses" → **import as BYOL + sole-tenant node** (Exam 4 · Q8).
- "New to Kubernetes" + "minimize operational overhead" → **GKE Autopilot** after a containerization assessment (Exam 5 · Q79).

### Traps
- Migrating VMs one by one "based on a list of applications" skips the assessment and runbook (Exam 2 · Q39). Manually importing disk images or installing third-party agents is not the recommended path either.
- A standard Windows VM (or attaching your imported disk as a *data* disk) does not use your license (Exam 4 · Q8).
- Stackdriver Debugger (later Cloud Debugger) was shut down in 2023. It was never the right "best practice" answer (Exam 1 · Q3).
- Kubernetes "on Compute Engine" and GKE Standard both leave node operations to a team that can't handle them yet (Exam 5 · Q79).

---

## 2. Modernization strategy and future-proofing

### Key facts
- **Workload disposition**: each workload is rehosted (lift and shift), replatformed (move and improve), refactored or rebuilt, replaced (buy SaaS), or retired. Lift and shift is fast; modernization comes after.
- After a rapid lift and shift, a nine-month plan for auto-scaling, near no-ops compute → **GKE with containers** and **App Engine standard** (Exam 3 · Q50). Today Cloud Run would also fit. Compute Engine with custom machine types or MIGs still leaves you managing VMs.
- A tightly coupled monolith that slows deployments and blocks new ML features → **phased migration to event-driven microservices** with **Pub/Sub** for async communication and models on **Vertex AI endpoints** (Exam 5 · Q64). Just containerizing the monolith, or calling a model from the monolith, does not improve agility.
- A legacy order system that must keep talking to ERP and supply chain systems during a multi-year transition → **build a cloud-native platform with API-based integration and asynchronous messaging** to decouple from legacy (Exam 5 · Q19). This is the strangler pattern: replace pieces gradually behind stable interfaces.
- Open-source, portable stack that autoscales, does continuous delivery, runs isolated copies, uses templates and URL routing → **GKE + Jenkins + Helm** (Exam 1 · Q29). Helm charts are the "dynamic templates"; Kubernetes namespaces give isolated copies; Ingress gives URL routing.
- Outsourced operators must promote staged versions to production themselves, with low ops → **App Engine**, which deploys **versions** side by side and lets you **migrate or split traffic** between them (Exam 2 · Q45). Cloud Run revisions with traffic splitting offer the same model today.
- **Designing for the future**: keep data. Store as much analytics and activity data as is affordable so you can train ML models later, and package backends as **containers on GKE** for elastic scaling (Exam 4 · Q32).
- **Improving an ML model over time** → store predictions (recommendations) and their real **outcomes** in BigQuery and feed them back as training data (Exam 2 · Q29). Faster hardware does not make a model more accurate.

### Decision rules
- "Long-term modernization", "developer agility", "integrate new ML features" → **phased, event-driven microservices + Pub/Sub** (Exam 5 · Q64).
- "Multi-year transition" + "integrate with legacy" → **APIs + async messaging**, never a big-bang replacement (Exam 5 · Q19).
- "Future-proof" in a case study → **keep data for ML** and **containerize** (Exam 4 · Q32).
- "Better model results over time" → **feedback loop of outcomes into training data** (Exam 2 · Q29).

### Traps
- "Replace the whole ERP in one migration" and "move it unchanged to VMs" both fail a multi-year, low-risk transition (Exam 5 · Q19).
- CI/CD with Spinnaker, schema versioning tools and weekly patching are good operations, but they don't "leverage future cloud improvements" (Exam 4 · Q32).
- GPUs → TPUs, or chasing new CPU generations, changes speed or cost, not prediction quality (Exam 2 · Q29).
- GKE + Cloud Load Balancing alone has no CD tool and no templating (Exam 1 · Q29). Deployment Manager is not open source and has been superseded by Infrastructure Manager (Terraform).

---

## 3. Choosing a compute platform

### Key facts
- **Serverless first** when the stem says "minimize ops" and traffic is spiky or idle. Cloud Run, Cloud Run functions and App Engine standard all **scale to zero**.
- An MVP used only during business hours, fully managed and scaling to zero → **Cloud Functions** (now **Cloud Run functions**) (Exam 1 · Q60). App Engine flexible keeps at least one instance running; GKE keeps nodes running.
- A few public APIs with low traffic and occasional spikes, cost-efficient, behind Cloud Load Balancing → **static content in Cloud Storage, APIs on Cloud Functions, user data in Firestore** (Exam 3 · Q5). Cloud CDN is a cache, not a place to store content; Cloud SQL and Spanner bill even when idle.
- Millions of concurrent users and "developers only write code" → **App Engine** (Exam 3 · Q10). An unpredictable HTTP API in Go with low ops → **App Engine standard** (Exam 3 · Q16), which starts instances in seconds; flexible runs VMs and scales slowly.
- Very high request rates (500,000 req/s) with idle periods and exact-match lookups → **Cloud Run + Bigtable** (Exam 3 · Q2). Cloud Run scales to zero; Bigtable handles the writes and key lookups.
- A promo site with 100 to 500,000 click-throughs a day and low ops → **App Engine + Datastore** (Firestore in Datastore mode), or a **MIG + Bigtable** (Exam 3 · Q49). See questionable answers.
- Long C++ test suites on Linux VMs, cut run time with minimal changes → **MIG with autoscaling** to fan tests out over many VMs (Exam 3 · Q32). Dataproc would require rewriting tests as Hadoop jobs.
- A case study that needs a **custom Linux distro** and strong uptime → **Compute Engine MIGs with autoscaling behind a global load balancer, on standard (non-preemptible) VMs** (Exam 4 · Q31). A REST game backend → **instance template, multi-zone MIG per region, L7 (HTTP(S)) load balancer** (Exam 4 · Q36).
- Many small services, multi-region, single public IP for the frontends, immutable artifacts → **container registry (now Artifact Registry) + GKE + global HTTP(S) load balancer** (Exam 4 · Q26). Container image digests are immutable; the global LB gives one anycast IP.
- **Spot VMs** (successor to preemptible VMs) are up to 60–91% cheaper but can be reclaimed at any time. Use them for fault-tolerant batch work, never for latency-sensitive, uptime-critical serving.

### Comparison

| Platform | Scales to zero | Ops | Picked when | Source |
|---|---|---|---|---|
| Cloud Run functions | Yes | Lowest | Event-driven or small APIs, idle most of the time | (Exam 1 · Q60), (Exam 3 · Q5) |
| Cloud Run | Yes | Lowest | Containers, very high or spiky request rates | (Exam 3 · Q2), (Exam 5 · Q62) |
| App Engine standard | Yes | Low | Code-only apps, versions and traffic splitting | (Exam 3 · Q10), (Exam 3 · Q16), (Exam 2 · Q45) |
| GKE Autopilot / Standard | No | Medium | Many microservices, portability, Helm | (Exam 1 · Q29), (Exam 4 · Q26), (Exam 5 · Q79) |
| Compute Engine MIG | No | Highest | Custom OS, legacy apps, parallel VM work | (Exam 3 · Q32), (Exam 4 · Q31), (Exam 4 · Q36) |

### Decision rules
- "Scale to zero" + "fully managed" → **Cloud Run / Cloud Run functions / App Engine standard** (Exam 1 · Q60), (Exam 3 · Q16).
- "Custom Linux distro" → **Compute Engine**, not a managed platform (Exam 4 · Q31).
- "REST/HTTP API" → **L7 load balancer**; "TCP, non-HTTP" → **network (L4) load balancer** (Exam 4 · Q36), (Exam 2 · Q40).
- "Run many tests or jobs in parallel without code changes" → **autoscaled MIG** (Exam 3 · Q32).
- "Single global IP + multi-region + immutable artifacts" → **Artifact Registry + GKE + global HTTP(S) LB** (Exam 4 · Q26).
- Uptime matters ("downtime is loss of players") → **standard VMs, not preemptible/Spot** (Exam 4 · Q31).

### Traps
- Single-zone MIGs per region and L4 load balancers lose for an HTTP API (Exam 4 · Q36).
- "Cloud Endpoints" is an API gateway, not a place to run code (Exam 3 · Q10).
- App Engine flexible with a custom runtime adds VM start-up time and cost (Exam 3 · Q16).
- A single VM with Cloud SQL, or GKE with persistent disks, fails "scale + low ops" (Exam 3 · Q49).

---

## 4. High availability within a region

### Key facts
- A **zone** is a failure domain; a **region** has three or more zones. Surviving a zone outage means running in at least two zones of one region. Surviving a region outage needs a second region (lesson 5).
- A **regional MIG** spreads instances across zones and recreates failed ones. For a business-critical app that must survive a zone outage at the lowest cost → **regional MIG in one region** (Exam 5 · Q58). Multi-region active-active with Spanner is more than the requirement asks.
- **Regional Persistent Disk** (and Hyperdisk Balanced High Availability) synchronously replicates a disk across two zones. If the zone fails, you **force-attach** it to a standby VM in the other zone with no data loss (Exam 3 · Q21).
- Quick restore in another zone with the latest data → **instance template + regional PD**, start the app in the other zone of the same region and attach the disk (Exam 2 · Q52). Snapshots lose recent writes; a regional PD can't be attached in another region.
- An app that can't scale horizontally, needs exclusive filesystem access over TCP, and tolerates brief downtime → **unmanaged instance group with an active and a standby VM in different zones, a regional PD, and a network load balancer** (Exam 2 · Q40). A MIG would start several copies that share one disk; an HTTP LB doesn't fit raw TCP.
- **Cloud SQL high availability**: a primary and a **standby in another zone of the same region**, with synchronous replication and automatic failover (the `REGIONAL` availability type). Older material calls the standby a "failover replica" (Exam 2 · Q7). **Read replicas** scale reads and do not fail over automatically.
- Cloud SQL HA failover takes about a minute. **Zero downtime** for SQL Server through a zone outage → **Always On availability groups with Windows Server Failover Clustering on Compute Engine, nodes in different zones** (Exam 1 · Q57). Spanner does not run SQL Server.

### Decision rules
- "Survive a zone failure" + "lowest cost" → **regional MIG** (Exam 5 · Q58).
- "Disk data instantly available in another zone" → **regional PD + force-attach** (Exam 3 · Q21), (Exam 2 · Q52).
- "Not horizontally scalable" + "exclusive disk access" → **active/standby in an unmanaged group + regional PD** (Exam 2 · Q40).
- "Cloud SQL HA" → **standby in a different zone, same region** (Exam 2 · Q7).
- "SQL Server, zero downtime on zone outage" → **Always On AGs across zones** (Exam 1 · Q57).

### Traps
- Spot-only MIGs are not high availability: every VM can be reclaimed at once (Exam 5 · Q58).
- "Different subnets" is not the same as "different zones". Subnets are regional, so they don't protect against a zone failure (Exam 1 · Q57).
- Hourly snapshots, gcsfuse mounts and rsync from Local SSD all lose data or add latency on failover (Exam 3 · Q21).
- A replica "in a different region" is DR, not HA (Exam 2 · Q7).

---

## 5. Disaster recovery, backups and multi-region data

### Key facts
- **RTO** is how long recovery may take; **RPO** is how much recent data you may lose. Tighter targets need warmer standbys and continuous replication, and cost more.
- DR patterns, from cheapest to fastest: **cold** (backups, rebuild on demand), **warm** (scaled-down standby running), **hot / active-active** (full capacity in both regions).
- Regional failover for a Compute Engine app → **two instance groups in different regions of the same project, behind HTTP(S) load balancing** that fails over to the standby group (Exam 1 · Q49). Groups, not single instances; separate projects add nothing.
- Cross-region DR for Cloud SQL → a **cross-region read replica** that you **promote** during a regional outage. It replicates asynchronously, so RPO is minutes or less (Exam 5 · Q71). Cloud SQL HA only covers zones.
- RTO 2 hours + RPO 15 minutes for an app on Compute Engine + Cloud SQL → **MIGs already running in both regions behind a global load balancer, plus a cross-region Cloud SQL replica** (Exam 5 · Q55). Building the replica "after the disaster" is impossible once the primary region is down; daily snapshots miss the RPO.
- Minimize data loss for a single Cloud SQL MySQL instance → **automated backups + binary logging**, which together allow **point-in-time recovery** (Exam 2 · Q62).
- Automated, zone-proof disk backups kept 90 days in a separate, restricted project with minimal effort → **Backup and DR Service**: a backup plan with daily backups into a **backup vault** with a 90-day enforced retention (Exam 5 · Q60). Scripts and snapshot-to-bucket copies are manual and not tamper-proof.
- Heavy writes, relational, multi-region HA, low ops → **Cloud Run in several regions behind a global HTTPS load balancer, with Spanner** (Exam 5 · Q62). Cloud SQL is regional; Firestore and Bigtable are not relational.
- **Spanner** reads are strongly consistent by default. Users seeing stale order data across regions → use **strong reads** and place the **leader region** near most users so writes and strong reads stay fast (Exam 4 · Q66). Caching in CDN or Memorystore makes staleness worse; Bigtable replication is eventually consistent.

### Comparison

| Need | Answer | Source |
|---|---|---|
| Zone failure, Cloud SQL | HA standby in another zone | (Exam 2 · Q7) |
| Region failure, Cloud SQL, RPO minutes | Cross-region replica, promote | (Exam 5 · Q71), (Exam 5 · Q55) |
| Point-in-time recovery | Automated backups + binary logs | (Exam 2 · Q62) |
| Region failure, Compute Engine | Instance groups in two regions + global LB | (Exam 1 · Q49), (Exam 5 · Q55) |
| Retained, isolated backups | Backup and DR backup vault | (Exam 5 · Q60) |
| Global relational, write-heavy | Spanner multi-region | (Exam 5 · Q62), (Exam 4 · Q66) |

### Decision rules
- "Regional outage" → **second region**, pre-provisioned when the RTO is short (Exam 1 · Q49), (Exam 5 · Q55).
- "RPO in minutes" for Cloud SQL → **cross-region replica**; "RPO hours" → backups may do (Exam 5 · Q71).
- "Backups retained N days in a separate project, automated" → **Backup and DR backup vault** (Exam 5 · Q60).
- "Strong consistency across regions" → **Spanner** with strong reads (Exam 4 · Q66), (Exam 5 · Q62).

### Traps
- Cloud SQL HA does not survive a regional outage (Exam 5 · Q71).
- Database Migration Service is for migrations, not ongoing DR replication (Exam 5 · Q71).
- "Rely on the regional SLA" is not a DR plan (Exam 5 · Q55).
- Sharding, read replicas and semisynchronous replication don't give point-in-time recovery for a single instance (Exam 2 · Q62).

---

## 6. Global performance, latency and caching

### Key facts
- The **global external Application Load Balancer** (HTTP(S) LB) has one anycast IP, ends connections at Google's edge, and routes each user to the **nearest healthy backend region**. It is the standard front door for global web apps and APIs (Exam 5 · Q47).
- **Cloud CDN** caches content at Google's edge. It is enabled on a backend service or **backend bucket** of an external Application Load Balancer (Exam 5 · Q75), (Exam 5 · Q61). It can also cache from an **external origin** such as another cloud's storage, so HRL can reach new regions without moving its video library first (Exam 4 · Q62).
- **Media CDN** is Google's CDN for large media and **video streaming**. **Cloud CDN** is the usual answer for web static assets (CSS, JS, images) (Exam 5 · Q47).
- Static assets slow for distant users → **Cloud CDN on the global LB**, and to cut latency for dynamic pages too → **frontend MIGs in Europe and Asia behind the global LB** (Exam 5 · Q75).
- Songs in Cloud Storage failing under load from fixed VMs → **MIG + global HTTP(S) LB with two backends (the MIG and a backend bucket) and Cloud CDN on the bucket** (Exam 3 · Q53).
- Speed up page loads for an e-commerce site → **Cloud CDN for media** and **Memorystore** to cache database results and sessions (Exam 5 · Q61).
- Reduce latency for a GKE API in a new continent → **second GKE cluster in that region + one global HTTP(S) LB across both clusters**. The question uses kubemci; today it's **Multi Cluster Ingress** or the **multi-cluster Gateway** (Exam 3 · Q28). CDN doesn't help a dynamic, computed API.
- Public site suffering DDoS from known IP ranges plus latency → **external HTTP(S) LB + Cloud Armor** (Exam 4 · Q54). Cloud Armor enforces IP deny lists and DDoS protection at the edge; VPC firewall rules act only after traffic reaches your network.
- Downloads served worldwide → one **multi-region Cloud Storage bucket** (Exam 2 · Q33). Buckets are not per-zone.
- **Read-through caching**: hash the query into a cache key, check the cache, and query the database only on a miss. The App Engine question uses **dedicated memcache** (reserved capacity) (Exam 2 · Q35); outside App Engine's legacy runtimes, use **Memorystore**.

### Decision rules
- "Global users" + "API latency" → **global external Application Load Balancer** with backends in several regions (Exam 5 · Q47), (Exam 5 · Q75).
- "Static assets slow far away" → **Cloud CDN** (Exam 5 · Q75). "Video streaming at scale" → **Media CDN**.
- "Content stays at another cloud for now" → **Cloud CDN with an external origin** (Exam 4 · Q62).
- "DDoS + IP ranges" → **Cloud Armor** on the external LB (Exam 4 · Q54).
- "Fewer DB queries" → **cache keyed by query hash**, check before querying (Exam 2 · Q35), (Exam 5 · Q61).

### Traps
- A regional network LB in one region doesn't help users on other continents; neither do bigger machines (Exam 5 · Q75).
- Cloud SQL read replicas abroad don't speed up static assets (Exam 5 · Q75).
- DNS round robin across two `LoadBalancer` Services has no health-aware, latency-based routing (Exam 3 · Q28).
- A multi-region bucket can't "host the entire web application" with dynamic APIs (Exam 5 · Q47).
- One cache key for "all queries", or a cron job refilling the cache, serves stale or wrong data (Exam 2 · Q35).
- Replicating video into GKE clusters, or serving through Apigee, is not a CDN (Exam 4 · Q62).

---

## 7. Choosing storage: object, file and block

### Key facts
- **Cloud Storage** (object): unlimited, cheap, durable. Classes are Standard, Nearline (30-day minimum), Coldline (90-day) and Archive (365-day); **lifecycle rules** move or delete objects automatically. Locations are region, dual-region or multi-region.
- **Persistent Disk / Hyperdisk** (block): disks attached to VMs. Zonal or regional. **Local SSD** is fast but ephemeral.
- **Filestore** (file): managed NFS. Many instances writing to the **same POSIX filesystem** at up to 100 MB/s → **Filestore mounted on each instance** (Exam 2 · Q56). gcsfuse isn't a full POSIX filesystem; PDs can't be shared for writing.
- Cost-effective storage for a mixed SAN workload → **lifecycle-managed Cloud Storage** for log archives, thumbnails and VM images/templates, and a **cache backed by Datastore** for multi-day session state (Exam 2 · Q23). Local SSD loses data; Cloud SQL and PD-SSD cost more for simple sessions.
- **Data lake rule**: land data **raw and unprocessed in Cloud Storage**, then let pipelines read from there, so you can reprocess when the schema changes (Exam 3 · Q17).
- Low-risk first cloud project: archive 100 TB of logs for DR and try analytics → **Cloud Storage for the archive + BigQuery for analysis** (Exam 1 · Q33), (Exam 3 · Q37).
- High-volume uploads to one bucket (3,000 objects/s, mixed sizes) → **one bucket, metadata in the file, compress each file, random name prefixes** (Exam 3 · Q34). Random prefixes spread load over Cloud Storage's index ranges; sequential names (timestamps, sequence numbers) create hotspots. Creating new buckets every hour or day is an anti-pattern.

### Decision rules
- "Shared POSIX filesystem" → **Filestore** (Exam 2 · Q56).
- "Archive / long-term / DR copy" → **Cloud Storage** with lifecycle rules (Exam 2 · Q23), (Exam 1 · Q33).
- "Store exactly as received, reprocess later" → **raw files in Cloud Storage** (Exam 3 · Q17).
- "High object write rate" → **random prefixes, single bucket** (Exam 3 · Q34).

### Traps
- Storing only processed output (in BigQuery or Cloud Storage) loses the original data you need for reprocessing (Exam 3 · Q17).
- Bigtable, Cloud SQL and Cloud Logging are the wrong home for 100 TB of archived log files (Exam 1 · Q33), (Exam 3 · Q37).
- Batching 10,000 events per archive raises the risk of losing data before upload (Exam 3 · Q34).

---

## 8. Choosing a database

### Key facts
- **BigQuery**: serverless data warehouse. SQL over terabytes to petabytes. Multi-petabyte data for SQL-savvy analysts → BigQuery (Exam 1 · Q2). An OLAP reporting tool over hundreds of TB, "relational" → BigQuery, not Cloud SQL or Spanner (Exam 2 · Q11).
- BigQuery **partitioning** (for example by season) cuts scanned data and cost, and BigQuery supports **adding columns** as data evolves. Cheap race telemetry kept forever, with training on only last season → **BigQuery partitioned by season** (Exam 4 · Q15).
- **Bigtable**: wide-column NoSQL for **high-throughput, low-latency** reads and writes, **time series**, IoT and clickstream. Clickstream spiking to 8,500 events/s → Bigtable (Exam 1 · Q15). 50,000 sensors × 10 readings/s for real-time charts → Bigtable (Exam 1 · Q19). Sensor status every second from 1,000 rooms → **NoSQL** (Exam 1 · Q7).
- Game activity in a "time series database service" → **Bigtable** (Exam 4 · Q35). Mountkirk's full database split: **Bigtable for time series, Spanner for transactions, BigQuery for historical queries** (Exam 4 · Q34).
- **Bigtable row keys** decide performance. Rows sort by key, and queries are fast only as prefix or range scans. Put the most-filtered fields first and the **timestamp last**: `vehicleID#eventID#timestamp`, with a column family per sensor category (Exam 5 · Q23). Hotspots come from **monotonically increasing or poorly distributed keys**; the fix is to **redesign the row key** so writes spread evenly. Adding nodes only hides the problem (Exam 3 · Q59).
- **Cloud SQL**: managed MySQL, PostgreSQL and SQL Server, regional, up to 64 TB. **Spanner**: relational, horizontally scalable, strongly consistent, regional or multi-region. **Firestore**: serverless document database (Native mode, or Datastore mode for the older Datastore API).

### Comparison

| Product | Model | Sweet spot | Source |
|---|---|---|---|
| BigQuery | Columnar warehouse | SQL analytics, TB–PB, historical queries | (Exam 1 · Q2), (Exam 2 · Q11), (Exam 4 · Q15) |
| Bigtable | Wide-column NoSQL | Time series, IoT, clickstream, key lookups | (Exam 1 · Q15), (Exam 1 · Q19), (Exam 4 · Q35) |
| Spanner | Relational, global | Global transactions, strong consistency | (Exam 4 · Q34), (Exam 5 · Q62) |
| Cloud SQL | Relational, regional | Existing MySQL/PostgreSQL/SQL Server apps | (Exam 2 · Q7), (Exam 5 · Q71) |
| Firestore | Document NoSQL | User data, sessions, serverless apps | (Exam 3 · Q5), (Exam 3 · Q49) |

### Decision rules
- "Analysts + SQL + huge data" or "OLAP" → **BigQuery** (Exam 1 · Q2), (Exam 2 · Q11).
- "Sensor / time series / clickstream / millions of writes" → **Bigtable** (Exam 1 · Q19), (Exam 1 · Q15).
- "Bigtable hotspot" → **fix the row key** (Exam 3 · Q59).
- "Query by vehicle and event over a time range" → key **vehicle#event#timestamp** (Exam 5 · Q23).

### Traps
- "Relational" in an OLAP stem tempts you to Cloud SQL or Spanner; at hundreds of TB for analytics, BigQuery wins (Exam 2 · Q11).
- BigQuery isn't a low-latency serving store for high-rate writes (Exam 1 · Q19), (Exam 3 · Q2).
- Leading a Bigtable key with a timestamp hotspots one node; relying on cell versions for time loses range scans (Exam 5 · Q23).
- One Cloud SQL instance per season, or Spanner keyed by season, is costly and hotspots (Exam 4 · Q15).

---

## 9. Data processing and analytics pipelines

### Key facts
- **Dataflow** (Apache Beam) runs **batch and streaming** with one programming model, serverless and autoscaling. New analysis code, hourly batch + real time → Dataflow (Exam 1 · Q11). Real-time fraud stream → **Dataflow**, daily reports → **BigQuery** (Exam 5 · Q59).
- **Dataproc** runs Spark and Hadoop with little code change. Growing on-prem Spark/Hadoop jobs → Dataproc (Exam 1 · Q17). Cheaper → add **preemptible (now Spot) secondary workers** (Exam 2 · Q53). Hadoop on raw Compute Engine means managing the cluster yourself.
- The classic streaming analytics stack: **Pub/Sub → Dataflow → BigQuery**, with **Cloud Storage** for uploaded files. Mountkirk's fully managed analytics (late data, files from devices, SQL on 10 TB) → **Dataflow, Cloud Storage, Pub/Sub, BigQuery** (Exam 4 · Q29). Dataflow's event-time windows and watermarks handle late data.
- Strict order with no duplicates into a legacy API → **Pub/Sub + Dataflow**, which deduplicates and orders by event time (Exam 2 · Q38). Pub/Sub alone now offers **ordering keys** and **exactly-once delivery** (pull subscriptions, within a region), but the bank expects Dataflow.
- Profile, detect anomalies in and clean degraded data → **upload to Cloud Storage, then use Dataprep** (a visual, no-code wrangling partner service) (Exam 1 · Q45). Dataprep can't connect straight to on-prem systems; Cloud Datalab (retired, replaced by Vertex AI Workbench) is a notebook, not a cleaning tool.
- Siloed ERP, plant and telemetry data, EU compliance → **one BigQuery analytics platform** with **regional data residency, IAM access and CMEK** (Exam 5 · Q18).

### Decision rules
- "Batch + streaming", "no existing code" → **Dataflow** (Exam 1 · Q11).
- "Existing Spark/Hadoop", "minimal code change" → **Dataproc**; "+ cheaper" → **Spot/preemptible secondary workers** (Exam 1 · Q17), (Exam 2 · Q53).
- "Process on the fly + late data + SQL on history + managed only" → **Pub/Sub, Dataflow, Cloud Storage, BigQuery** (Exam 4 · Q29), (Exam 5 · Q59).
- "Clean / profile data visually" → **Dataprep** on files in Cloud Storage (Exam 1 · Q45).

### Traps
- Dataproc for both streaming and batch adds cluster management when the stem says "minimize ops" (Exam 5 · Q59).
- Cloud SQL in a "fully managed analytics at 10 TB+" answer is a red flag (Exam 4 · Q29).
- Firestore and Dataprep are not stream processors (Exam 5 · Q59).
- Spot/preemptible VMs are fine for Dataproc **secondary** workers, not for the whole cluster's primary nodes.

---

## 10. Integration, hybrid connectivity and data movement

### Key facts
- **Moving large data**: rule of thumb, 1 TB takes about 30 hours at 100 Mbps. 900 TB of archives over 100 Mbps → **Transfer Appliance**; a 10 TB/day ongoing feed → **Dedicated Interconnect** (or Direct Peering) (Exam 2 · Q37). VPN over a 100 Mbps link can't carry 10 TB a day.
- Modernize SFTP files, cron-driven batch ETL and many databases across hybrid systems → **Dedicated Interconnect with Cloud Router**, **Pub/Sub** for event-driven ingestion, and **Dataflow** for central processing (Exam 5 · Q14).
- **Pub/Sub** decouples producers from consumers and buffers when consumers or connections fail. Devices with patchy connectivity → **check connectivity and publish to a shared Pub/Sub topic** (Exam 4 · Q65). One table or VM connection per device doesn't scale.
- Reliable scheduled work → **a scheduler publishes to Pub/Sub, and workers subscribe**. The question uses App Engine cron; today's managed scheduler is **Cloud Scheduler** (Exam 2 · Q36). Pub/Sub retries and buffers if workers are down; direct calls don't.
- Connecting SaaS apps (Salesforce, ServiceNow) and Cloud SQL with mapping, transformation and near real-time sync → **Application Integration**, Google's iPaaS with prebuilt connectors and a data mapper (Exam 5 · Q48). **Workflows** orchestrates API calls but has no connectors or data mapping; Datastream only replicates databases.
- Legacy systems during a long transition → **APIs + asynchronous messaging** (Exam 5 · Q19).

### Comparison

| Tool | Does | Source |
|---|---|---|
| Transfer Appliance | Ships 100s of TB offline | (Exam 2 · Q37) |
| Dedicated Interconnect | Private 10/100 Gbps link to Google | (Exam 2 · Q37), (Exam 5 · Q14) |
| Pub/Sub | Async messaging and buffering | (Exam 4 · Q65), (Exam 2 · Q36), (Exam 5 · Q14) |
| Application Integration | SaaS/app integration with mapping | (Exam 5 · Q48) |
| Cloud Scheduler | Managed cron | (Exam 2 · Q36) |

### Decision rules
- "Hundreds of TB" + "slow link" → **Transfer Appliance**; "many TB every day" → **Interconnect** (Exam 2 · Q37).
- "Unreliable connectivity" or "decouple" → **Pub/Sub** (Exam 4 · Q65), (Exam 2 · Q36).
- "Integrate Salesforce / ServiceNow / databases with transformations" → **Application Integration** (Exam 5 · Q48).
- "Replace SFTP and cron ETL" → **Pub/Sub + Dataflow over Interconnect** (Exam 5 · Q14).

### Traps
- Compressing and uploading with `gsutil -m` over 100 Mbps can't move 900 TB in reasonable time (Exam 2 · Q37).
- Keeping SFTP and adding alerts, or swapping it for Storage Transfer Service with cron ETL, doesn't modernize the flow (Exam 5 · Q14).
- Cron jobs calling a service directly lose work when the service is down (Exam 2 · Q36).

---

## 11. AI and ML solutions

### Key facts
- **Vertex AI** is Google Cloud's ML platform: training, pipelines, Model Registry, endpoints, Model Garden, and Gemini models. **Vertex AI Pipelines** orchestrate repeatable ML workflows at scale.
- **Vertex Explainable AI** gives feature attributions that explain individual predictions. "Help people understand and interpret predictions" → **Explainable AI** (Exam 4 · Q14). **Model Monitoring** watches for skew and drift; it doesn't explain decisions.
- Scalable, auditable, explainable content moderation over media in Cloud Storage → **Vertex AI pipeline with pre-trained multimodal models, results in BigQuery** (for audit) (Exam 5 · Q1).
- Generate product attributes, descriptions and images for millions of products with human review → **Vertex AI generative models in Vertex AI Pipelines, output to BigQuery, and a Cloud Run review UI** before writing to the catalog (Exam 5 · Q12). The **human-in-the-loop review app** → **Cloud Run secured with IAM and Identity-Aware Proxy**, storing review states in a managed database (Exam 5 · Q15).
- **Conversational agents**: **Dialogflow CX** (now part of Conversational Agents) builds virtual agents and can call **Gemini** for generative answers. LLM self-service grounded in BigQuery data → **Dialogflow CX + Vertex AI Gemini + BigQuery** (Exam 5 · Q5). Replace an IVR securely → **Dialogflow CX with secure backend APIs, IAM and data access controls** (Exam 5 · Q16).
- Natural-language product discovery tied to the catalog → **Dialogflow CX + Discovery AI for Retail** (later Vertex AI Search for retail, then for commerce) over the catalog (Exam 5 · Q13).
- Large-scale simulation and training with regional compliance → **Vertex AI training pipelines, managed datasets and region-specific deployments** (Exam 5 · Q20).
- Vehicles with unreliable connectivity → **hybrid: edge inference for latency-sensitive features, cloud training, model updates over intermittent links** (Exam 5 · Q17).

### Decision rules
- "Explain / interpret predictions" → **Explainable AI** (Exam 4 · Q14).
- "Generate content at scale + human review" → **Vertex AI Pipelines + review app on Cloud Run with IAP** (Exam 5 · Q12), (Exam 5 · Q15).
- "Chatbot / virtual agent / replace IVR" → **Dialogflow CX** (+ Gemini) (Exam 5 · Q5), (Exam 5 · Q16).
- "Product search in natural language" → **Dialogflow CX + Vertex AI Search for commerce** (Exam 5 · Q13).
- "Intermittent connectivity" + "low latency" → **edge inference, cloud training** (Exam 5 · Q17).

### Traps
- BigQuery ML is for SQL-based models on tabular data, not for generating chat replies or moderating video (Exam 5 · Q1), (Exam 5 · Q5), (Exam 5 · Q12), (Exam 5 · Q13).
- Self-hosting open-source LLMs or chatbots on GKE adds ops without meeting audit and iteration needs (Exam 5 · Q5), (Exam 5 · Q16).
- Bypassing human review, editing files through signed URLs, or approving in Sheets fails auditability and RBAC (Exam 5 · Q12), (Exam 5 · Q15).
- Fixed GPU VMs with manual scaling, or on-prem-only training, fail "scale globally and optimize cost" (Exam 5 · Q20).
- Cloud-only inference fails when the network drops (Exam 5 · Q17).

---

## ⚠️ Questionable answers

| Item | Issue |
|---|---|
| (Exam 2 · Q23) | Option B puts "VM boot/data volumes" in Cloud Storage. VMs boot from Persistent Disk; Cloud Storage only holds the images and templates. App Engine memcache is also a legacy service. B is still the least-wrong option, so the key stays. |
| (Exam 2 · Q38) | Pub/Sub alone now supports ordering keys and exactly-once delivery (pull, single region). The keyed Pub/Sub + Dataflow is still a safe answer, especially when deduplication and global scale are involved. |
| (Exam 3 · Q49) | Bigtable for "basic user details" is overkill and has a fixed node cost; it is keyed only because GKE + PD and a single VM are worse. |
| (Exam 4 · Q8) | The option's import flag `--os=windows-2022-dc-v` doesn't exist; corrected to the BYOL value `windows-2022-byol`. `gcloud compute images import` is itself deprecated in favour of Migrate to Virtual Machines image imports. |
| (Exam 5 · Q1) | The keyed option says explanations come from Vertex AI Model Monitoring. Explanations come from Vertex Explainable AI; Model Monitoring tracks skew and drift. B is still the best option. |

## Last-minute cheat sheet

- First step → **define requirements** (Exam 1 · Q4). Cost estimate for migration → **Migration Center** (Exam 5 · Q42).
- VMware lift and shift → **assess, plan, runbook, Migrate to Virtual Machines** (Exam 2 · Q39). Windows BYOL → **sole-tenant** (Exam 4 · Q8).
- New to Kubernetes → **Autopilot** (Exam 5 · Q79). Monolith → **phased event-driven microservices** (Exam 5 · Q64).
- Legacy during transition → **APIs + async messaging** (Exam 5 · Q19). Future-proof → **keep data, containerize** (Exam 4 · Q32).
- Scale to zero → **Cloud Run / Cloud Run functions / App Engine standard** (Exam 1 · Q60), (Exam 3 · Q16).
- Custom OS + uptime → **MIGs, standard VMs, global LB** (Exam 4 · Q31). HTTP API → **L7 LB**; TCP → **L4** (Exam 4 · Q36), (Exam 2 · Q40).
- Zone failure, cheap → **regional MIG** (Exam 5 · Q58). Disk survives zone loss → **regional PD + force-attach** (Exam 3 · Q21).
- Cloud SQL HA → **standby in another zone** (Exam 2 · Q7). Region failure → **cross-region replica, promote** (Exam 5 · Q71).
- PITR → **backups + binary logs** (Exam 2 · Q62). 90-day isolated backups → **Backup and DR vault** (Exam 5 · Q60).
- SQL Server zero downtime → **Always On AGs across zones** (Exam 1 · Q57).
- Global relational writes → **Cloud Run multi-region + Spanner** (Exam 5 · Q62).
- Static assets far away → **Cloud CDN on global LB** (Exam 5 · Q75). Video → **Media CDN**. DDoS → **Cloud Armor** (Exam 4 · Q54).
- Shared POSIX → **Filestore** (Exam 2 · Q56). Raw data lake → **Cloud Storage** (Exam 3 · Q17). Many uploads → **random prefixes** (Exam 3 · Q34).
- OLAP / analysts / PB → **BigQuery** (Exam 2 · Q11), (Exam 1 · Q2). Time series / IoT → **Bigtable** (Exam 1 · Q19).
- Bigtable hotspot → **fix the row key** (Exam 3 · Q59); timestamp goes **last** (Exam 5 · Q23).
- Batch + stream → **Dataflow** (Exam 1 · Q11). Spark/Hadoop → **Dataproc + Spot workers** (Exam 2 · Q53).
- 900 TB over a slow link → **Transfer Appliance**; daily TB → **Interconnect** (Exam 2 · Q37).
- Flaky devices → **Pub/Sub** (Exam 4 · Q65). SaaS integration → **Application Integration** (Exam 5 · Q48).
- Explain predictions → **Explainable AI** (Exam 4 · Q14). Chatbot → **Dialogflow CX + Gemini** (Exam 5 · Q5).
- GenAI content with review → **Vertex AI Pipelines + Cloud Run/IAP review app** (Exam 5 · Q12), (Exam 5 · Q15).
