# Domain 5 Study Guide — Managing Implementation

> Condensed from the 33-question bank in [`05-managing-implementation.md`](05-managing-implementation.md). Covers rollouts, CI/CD and infrastructure as code, API management, data migration tooling, and working with Google Cloud from Cloud Shell and the CLIs. Citations look like (Exam N · QM).

---

## 1. Rolling out new versions safely

### Key facts
- Every managed compute platform has a built-in way to release gradually. The exam wants that built-in way, not an extra load balancer or a new project.
- **GKE**: a Deployment does a **rolling update** whenever its Pod template changes. `kubectl set image deployment/<name> <container>=<image>` (or `kubectl apply` with an edited manifest) replaces Pods a few at a time, governed by `maxSurge` and `maxUnavailable`. `kubectl rollout undo` rolls back (Exam 1 · Q53).
- **App Engine**: deploy the update as a **new version** of the same service, then **split traffic** between versions (by IP, cookie or random) with `gcloud app services set-traffic --splits` (Exam 2 · Q27).
- **Cloud Run** (and Knative serving, once "Cloud Run for Anthos"): each deploy creates a **revision**. Deploy with `--no-traffic` if needed, then send a percentage to the new revision with `gcloud run services update-traffic --to-revisions` (Exam 2 · Q42). Revision **tags** give a test URL that takes no production traffic.
- **Managed instance groups (MIGs)**: you update the group's **instance template**, then choose how instances pick it up (Exam 2 · Q50):
  - **Proactive** update: the MIG actively replaces or restarts existing instances.
  - **Opportunistic** update: nothing changes now; only instances created later (by autoscaling or repair) use the new template.
  - **Rolling restart** restarts instances on the same template. **Rolling replace** recreates them.
- **Schema changes are a separate release.** Keep database migrations in their own pipeline and make them **backward compatible** (expand, then contract later), so the previous app revision still works if you roll back. Combine this with a gradual Cloud Run traffic split (Exam 5 · Q32).

### Comparison

| Platform | Unit of release | Gradual rollout | Source |
|---|---|---|---|
| GKE | Deployment Pod template | Rolling update (`kubectl set image` / `apply`) | (Exam 1 · Q53) |
| App Engine | Version | Traffic splitting between versions | (Exam 2 · Q27) |
| Cloud Run / Knative serving | Revision | Traffic splitting between revisions, tags | (Exam 2 · Q42), (Exam 5 · Q32) |
| Compute Engine MIG | Instance template | Rolling update, proactive or opportunistic; canary with two templates | (Exam 2 · Q50) |

### Decision rules
- "Minimal downtime" on GKE → **`kubectl set image`** on the Deployment (Exam 1 · Q53).
- "Test with production traffic before replacing" on App Engine → **new version + traffic split** (Exam 2 · Q27).
- "Send a subset of traffic to the new version" on Cloud Run → **new revision + traffic split** (Exam 2 · Q42).
- "Don't touch existing instances, new ones should use the new template" → **rolling update, opportunistic mode** (Exam 2 · Q50).
- "Quick rollback" + database schema changes → **separate pipelines for schema and app**, **gradual traffic split** for the app (Exam 5 · Q32).

### Traps
- Deleting and recreating a Deployment or Service causes downtime. The image lives in the **Deployment**, not the Service (Exam 1 · Q53).
- Rolling-updating the **node instance group** under GKE upgrades nodes, not your app (Exam 1 · Q53).
- A new App Engine *application* or a new VPC plus a load balancer is overkill; versions already split traffic (Exam 2 · Q27).
- A new Cloud Run *service* behind a load balancer, or Traffic Director (now Cloud Service Mesh), adds complexity Cloud Run doesn't need. A `TRAFFIC_PERCENTAGE` Cloud Build substitution isn't a real feature (Exam 2 · Q42).
- Proactive mode, rolling restart and rolling replace all disturb existing instances (Exam 2 · Q50).
- Running schema migrations at **container start-up**, deploying `:latest`, or one pipeline that migrates the schema first all make rollback unsafe (Exam 5 · Q32).

---

## 2. Packaging and deploying workloads

### Key facts
- Starting from nothing with a Kubernetes manifest: create the cluster with **`gcloud container clusters create`**, fetch credentials with `gcloud container clusters get-credentials`, then deploy with **`kubectl apply -f`** (Exam 1 · Q58). `kubectl` talks to an existing cluster; it can't create a GKE cluster.
- **Deployment Manager** reached end of support on March 31, 2026; Google points to **Infrastructure Manager** (managed Terraform). It was never the way to apply Kubernetes manifests (Exam 1 · Q58).
- **Containers maximize utilization** for small apps: many 0.1-vCPU Pods share one node, while a VM per copy wastes most of the machine (Exam 2 · Q4).
- Reliable releases need **immutable, versioned image tags** (for example `:v1.4.2`), built from the **production branch**, tested in a **staging namespace**, then promoted. With a fixed tag, `imagePullPolicy: IfNotPresent` is safe (Exam 2 · Q4).
- **Faster image builds and pulls** (Exam 4 · Q51):
  - Use a **small base image** (Alpine, `-slim` or distroless). Smaller images pull and start faster.
  - **Order layers from least to most often changed.** Install OS packages and dependencies first, `COPY` the source last, so code changes don't invalidate the cached dependency layers.
  - Multi-stage builds keep build tools out of the final image.
- A Java `SecurityException: SHA1 digest error` means a JAR's manifest digest doesn't match the class inside it, typically a signed JAR that was modified or corrupted. The keyed fix is to **digitally sign the JARs (correctly) and redeploy** (Exam 4 · Q52). See questionable answers.

### Decision rules
- "No infrastructure yet" + Kubernetes Deployment file → **`gcloud` creates the cluster, `kubectl` creates the Deployment** (Exam 1 · Q58).
- "Small app, maximize utilization, reliable releases" → **GKE + versioned image + staging namespace, then promote** (Exam 2 · Q4).
- "Speed up deployments" from a Dockerfile → **lighter base image + copy source after installing dependencies** (Exam 4 · Q51).

### Traps
- The `latest` tag with `imagePullPolicy: Always` and "restart the Pods to deploy" is not a controlled release (Exam 2 · Q4).
- A startup script that clones the repo on each boot is slow and unrepeatable; a baked image per release wastes resources on oversized VMs (Exam 2 · Q4).
- Bigger nodes don't make image builds or pulls faster. Removing Python after `pip install` breaks the app. Trimming requirements helps little compared with layer caching (Exam 4 · Q51).
- MD5 instead of SHA1, or "clean and rebuild" alone, doesn't fix a JAR signature mismatch (Exam 4 · Q52).
- "Google Container Engine" in old questions means GKE (Exam 4 · Q51).

---

## 3. CI/CD pipelines, infrastructure as code and GitOps

### Key facts
- **Cloud Build** runs builds and tests. **Cloud Deploy** manages promotion through targets (dev → staging → prod) with approvals, canary and rollback. Cloud Deploy executes its rendering and deploy steps in Cloud Build.
- **Private GKE endpoint**: the default Cloud Build workers can't reach it. Create a **Cloud Build private pool** connected (peered) to the **same VPC network as the cluster**, and set it as the Cloud Deploy **execution environment** (Exam 5 · Q43).
- **Terraform in CI/CD** without keys (Exam 5 · Q72):
  - Cloud Build runs as a service account and **impersonates** a narrowly scoped deployer service account. No JSON keys.
  - Run **`terraform plan` on pull requests** so reviewers see the change.
  - Require a **manual approval** step before **`terraform apply`** runs in production. Developers can propose but not apply.
- **Infrastructure Manager** is Google's managed service for running Terraform.
- **Config Connector** is a Kubernetes add-on that manages Google Cloud resources as Kubernetes objects declared in YAML. **Config Controller** is a **hosted** bundle of Config Connector, Config Sync and Policy Controller, so you don't run the control plane yourself (Exam 5 · Q74).
- **Config Sync** keeps clusters in sync with configuration stored in Git (or OCI) repositories. **Policy Controller** (built on OPA Gatekeeper) enforces policies at admission. Together they replace "Anthos Config Management" and work across a fleet, including attached clusters such as Amazon EKS (Exam 5 · Q82).
- **Testing frameworks** belong in the pipeline: fast **unit** tests on every commit, **integration** tests against real or emulated dependencies (see lesson 6), and **load** tests before high-traffic launches.

### Comparison

| Need | Tool | Source |
|---|---|---|
| Deploy to a private GKE cluster from Cloud Deploy | Cloud Build private pool on the cluster's VPC | (Exam 5 · Q43) |
| Terraform with governance, no keys | Impersonation + plan on PR + approval before apply | (Exam 5 · Q72) |
| Declarative IaC for Google Cloud resources, GKE shop, low ops | Config Controller | (Exam 5 · Q74) |
| Consistent config + policy across GKE and EKS | Config Sync + Policy Controller | (Exam 5 · Q82) |

### Decision rules
- "Private endpoint" + deploys failing → **private pool peered with the cluster's VPC** (Exam 5 · Q43).
- "No long-lived keys" → **service account impersonation** (or Workload Identity Federation for external CI) (Exam 5 · Q72).
- "Developers can propose but not apply" → **plan on PR, approval gate before apply**, still automated (Exam 5 · Q72).
- "Kubernetes-style YAML for Google Cloud resources" + "reduce operational overhead" → **Config Controller** (Exam 5 · Q74).
- "Multi-cluster / multi-cloud configuration and policy, Google-recommended" → **Config Sync + Policy Controller** (Exam 5 · Q82).

### Traps
- VPC Service Controls is about data exfiltration, not network reachability. A private pool on the **default** VPC can't reach a cluster on another network. A Cloud Deploy custom target doesn't add connectivity (Exam 5 · Q43).
- Auto-applying on merge skips the governance gate. Having a human run `terraform apply` from a workstation breaks automation. A privileged JSON key in Secret Manager is still a long-lived key (Exam 5 · Q72).
- Config Sync alone syncs config; it doesn't provision Google Cloud resources. Config Connector is declarative YAML, not Python scripts. A custom operator is maximum ops (Exam 5 · Q74).
- Argo CD, Flux, Crossplane, Kyverno or custom scripts can work, but they aren't the Google-recommended answer (Exam 5 · Q82).

---

## 4. API management and calling Google APIs well

### Key facts
- **Apigee** is Google Cloud's API management platform: proxies, security, quotas, analytics, developer portal and monetization.
- An **API facade** in Apigee decouples consumers from the backend. Consumers call a stable Apigee endpoint while the monolith behind it is refactored or replaced (Exam 5 · Q38).
- **Apigee policies** to know (Exam 5 · Q11):
  - **Quota**: caps the number of calls an app or developer can make over a period (per minute, day, month). Use it to limit total usage and cost.
  - **Spike Arrest**: smooths bursts by limiting the rate per second or minute. It protects the backend; it doesn't count totals.
  - **Verify API Key** and **OAuth v2**: identify and authorize the caller. They don't limit volume.
  - **XML/JSON threat protection**: blocks malicious payloads.
- **Versioning**: put the **major version** in the API (for example `/v1/`, `/v2/`) and **increment it for every backward-incompatible change**. Keep the old version running while clients migrate (Exam 3 · Q11).
- **Retries**: on HTTP **5xx**, **429** (and 408), retry with **truncated exponential backoff with jitter** (wait 1s, 2s, 4s… plus randomness, up to a cap). Google client libraries do this for you by default (Exam 2 · Q31).
- **Pub/Sub publisher latency**: client libraries **batch** messages and wait for a batch to fill or a delay to expire. If latency matters more than throughput, **turn batching off** (or lower the batch delay) (Exam 4 · Q21).
- **Firestore in Datastore mode** (formerly Cloud Datastore): fetch many entities by ID with a **batch get using keys** (`get_multi`). One round trip, and lookups by key are cheaper and faster than queries (Exam 2 · Q1).
- **Browser uploads straight to Cloud Storage** (Exam 4 · Q6):
  - The backend issues a **signed URL** (or signed POST policy), time-limited and scoped to one object.
  - The bucket needs a **CORS** configuration that allows the app's origin, or the browser blocks the cross-origin request.

### Decision rules
- "Limit the total number of API calls" in Apigee → **Quota policy** (Exam 5 · Q11).
- "API design may change later" + many consumers → **Apigee API facade** in front of the backend (Exam 5 · Q38).
- "Don't impact customers with breaking changes" → **new major version per breaking change** (Exam 3 · Q11).
- Intermittent 5xx/429 → **truncated exponential backoff** (Exam 2 · Q31).
- Pub/Sub timeouts, no publish errors, improve publish latency → **disable batching** (Exam 4 · Q21).
- Many entities by identifier → **keys + batch get** (Exam 2 · Q1).
- Browser uploads bypassing the backend → **CORS + signed URL** (Exam 4 · Q6).

### Traps
- Service Directory or an internal load balancer only gives an address; consumers still call the monolith's API directly and break when it changes. Exposing SQL views couples them to the database (Exam 5 · Q38).
- Notifying clients by mailing list, auto-published docs, or a "DEPRECATED" suffix on the same version number don't protect clients from a breaking change (Exam 3 · Q11).
- gRPC, multi-region buckets or watching the status page don't handle transient errors (Exam 2 · Q31).
- Changing the total timeout, switching subscribers to push, or adding a backup queue doesn't touch publishing latency (Exam 4 · Q21).
- Queries with filters, or one get per entity, cost more round trips than a batch get (Exam 2 · Q1).
- Granting end users an IAM role on the bucket is too broad and needs Google identities. A signed URL without CORS fails in the browser (Exam 4 · Q6).

---

## 5. Data migration and transfer tooling

### Key facts
- Pick the transfer tool by **source**, **size** and **usable bandwidth**. At 1 Gbps fully used, 10 TB takes about a day, 100 TB about 10 days, and 1 PB about three months. Real links are slower, and shared ones much slower.
- **`gcloud storage cp`** (or the legacy `gsutil -m cp`) moves data online in **parallel**. Good for up to tens of TB with a decent link. Compress first to cut transfer time (Exam 3 · Q20), (Exam 4 · Q10), (Exam 4 · Q37).
- **Storage Transfer Service** is a managed service for large or recurring transfers:
  - From **other clouds and object stores** (Amazon S3, Azure Blob Storage, S3-compatible storage, HTTP URL lists) directly into Cloud Storage. No data passes through your own servers (Exam 3 · Q61).
  - From **on-premises file systems** using transfer agents (formerly "Transfer Service for on-premises data"). This still uses your network link.
- **Transfer Appliance** is for **offline** transfer when the network is too slow, shared or expensive. You copy data to the appliance locally, ship it, and Google uploads it to your bucket, encrypted with your Cloud KMS key. Older questions mention a "Rehydrator" step; that was the first-generation process (Exam 1 · Q52), (Exam 4 · Q49), (Exam 5 · Q56), (Exam 5 · Q66).
- **Integrity check after upload**: Cloud Storage stores a **CRC32C** (and MD5 for non-composite objects) for each object. Compute CRC32C locally with **`gsutil hash -c`** (or `gcloud storage hash`) and compare with the hash from **`gsutil ls -L`** (or `gcloud storage objects describe`). No download needed (Exam 3 · Q26).
- **Database Migration Service** migrates MySQL, PostgreSQL, SQL Server and Oracle databases **into Cloud SQL or AlloyDB**, one-time or continuous. Its destinations are Google Cloud databases only.
- **Cloud SQL external replicas**: a MySQL server outside Google Cloud can replicate from a Cloud SQL primary. Use it to distribute one authoritative database to read-only sites (Exam 5 · Q26).
- Related tools: **Datastream** (change data capture into BigQuery and Cloud Storage), **BigQuery Data Transfer Service** (scheduled loads from SaaS and other warehouses), **Migrate to Virtual Machines** (lift-and-shift VMs).

### Comparison

| Scenario | Tool | Source |
|---|---|---|
| 10 TB export, 1 Gbps, minimize time and cost | Compress + parallel `gsutil -m` / `gcloud storage cp` | (Exam 3 · Q20), (Exam 4 · Q10) |
| Batch files staged for ETL | Parallel copy (`gsutil -m cp`) | (Exam 4 · Q37) |
| 10 TB in another provider's object storage | Storage Transfer Service | (Exam 3 · Q61) |
| 75 TB on-prem, best practice | Transfer Appliance | (Exam 1 · Q52) |
| 1 PB, 1 Gbps, within a month | Transfer Appliance | (Exam 4 · Q49) |
| 500 TB, shared 1 Gbps, 60 days, secure | Transfer Appliance | (Exam 5 · Q56) |
| 2 PB in ten weeks | Transfer Appliance | (Exam 5 · Q66) |
| Prove uploaded files match local ones | CRC32C: `gsutil hash -c` vs `gsutil ls -L` | (Exam 3 · Q26) |
| One HQ writer, many read-only plant copies | Cloud SQL + external read replicas | (Exam 5 · Q26) |

### Decision rules
- Do the arithmetic. If the network transfer fits comfortably in the deadline → **online copy in parallel**. If it doesn't, or the link is shared with production → **Transfer Appliance** (Exam 3 · Q20), (Exam 5 · Q56).
- Source is **another cloud's object storage** → **Storage Transfer Service**, never download and re-upload (Exam 3 · Q61).
- Hundreds of TB to PBs on-prem with a ~1 Gbps link → **Transfer Appliance** (Exam 4 · Q49), (Exam 5 · Q66).
- Verify integrity cheaply → **compare CRC32C hashes**, don't download (Exam 3 · Q26).
- HQ-only writes, plants need exact copies, prove they're in sync → **Cloud SQL primary + standardized schema + external read replicas** (Exam 5 · Q26).

### Traps
- Transfer Appliance for only 10 TB on a 1 Gbps link is slower and costlier than uploading (Exam 3 · Q20), (Exam 4 · Q10). Dataflow or a third-party ETL tool adds cost and load for a simple file copy (Exam 3 · Q20).
- Sequential `gsutil mv` is slow. Using gsutil to "extract" or "load" isn't an ETL step (Exam 4 · Q37), (Exam 3 · Q61).
- Storage Transfer Service from on-prem still runs over the 1 Gbps link, so it can't move 1 PB in a month (Exam 4 · Q49). A faster Interconnect takes weeks to provision. "Ship your own USB or portable disks" isn't a Google service (Exam 4 · Q49), (Exam 5 · Q66).
- A 1 Gbps VPN or Dedicated Interconnect can't move 2 PB in ten weeks (Exam 5 · Q66).
- Cloud Dataprep doesn't decrypt or upload appliance data. Streaming uploads of 75 TB have no resume (Exam 1 · Q52).
- Downloading files again to diff or `shasum` them doubles the transfer. A custom Java hasher is unnecessary effort (Exam 3 · Q26).
- Database Migration Service can't replicate **out** of Cloud SQL to on-prem databases. Pub/Sub topics per supplier rebuild replication by hand (Exam 5 · Q26).

---

## 6. Cloud Shell, the CLIs and emulators

### Key facts
- **Cloud Shell** is a browser-based shell on a temporary VM with `gcloud`, `kubectl`, `bq`, `gsutil`, Terraform and common languages preinstalled and already authenticated. Nothing to install or update on your own machines (Exam 3 · Q63).
- Only the **5 GB home directory** (`$HOME`) persists between sessions. The rest of the VM resets, and the home directory is deleted after 120 days without use. Put personal tools in **`~/bin`**, which is on the default `PATH` (Exam 1 · Q39).
- **Cloud Shell Editor** is the built-in code editor. **Cloud Code** is the IDE plugin (VS Code, JetBrains) for building, running and debugging Kubernetes and Cloud Run apps, with Gemini Code Assist built in.
- **Gemini Cloud Assist** is the AI assistant in the console: it helps design, troubleshoot (logs, errors) and optimize cost of Google Cloud resources.
- **The CLIs**:
  - `gcloud`: most services, including `gcloud container clusters create` (Exam 1 · Q58) and `gcloud storage` (Exam 4 · Q10).
  - `gsutil`: legacy Cloud Storage CLI. Google now recommends `gcloud storage`, which is parallel by default (Exam 3 · Q20).
  - `bq`: BigQuery. `kubectl`: Kubernetes workloads. `cbt`: Bigtable.
- **Datastore-mode indexes**: composite indexes live in `index.yaml`. Deploy them with **`gcloud datastore indexes create index.yaml`** (older form: `gcloud datastore create-indexes`) (Exam 1 · Q48).
- **Emulators** let you develop and test locally without cost: `gcloud emulators` (some under `gcloud beta emulators`) for **Bigtable, Datastore, Firestore, Pub/Sub and Spanner**. `env-init` prints the environment variables (such as `PUBSUB_EMULATOR_HOST`) that point client libraries at the emulator.
- **Client libraries** (Cloud Client Libraries) are the recommended way to call Google APIs from code. They handle authentication through **Application Default Credentials**, retries and batching (Exam 2 · Q1), (Exam 2 · Q31).

### Decision rules
- "Switch workstations, don't manage the gcloud install" → **Cloud Shell** (Exam 3 · Q63).
- "Custom tool in PATH that persists in Cloud Shell" → **`~/bin`** (Exam 1 · Q39).
- "Deploy new Datastore indexes from a YAML file" → **`gcloud datastore indexes create`** (Exam 1 · Q48).
- Local tests against Pub/Sub, Spanner, Bigtable or Firestore without touching production → **emulators**.

### Traps
- `/usr/local/bin` and other system paths are reset when the Cloud Shell VM is recycled. `/google/scripts` is Google-managed. Cloud Storage isn't an execution path (Exam 1 · Q39).
- A jump VM with gcloud, package managers or `gcloud components auto-update` on every machine all still mean managing installs (Exam 3 · Q63).
- Indexes aren't picked up from a Cloud Storage bucket, an HTTP call to a Python module, or by deleting and re-uploading in the console (Exam 1 · Q48).

---

## ⚠️ Questionable answers

| Item | Issue |
|---|---|
| **(Exam 5 · Q26)** | **Key changed from D to C.** Database Migration Service only writes into Cloud SQL and AlloyDB, so it can't replicate from Cloud SQL to on-prem plant databases. Cloud SQL for MySQL documents external replicas for exactly this pattern, and option C standardizes the schema first. |
| **(Exam 4 · Q52)** | A "SHA1 digest error" means a signed JAR's manifest doesn't match its contents. "Sign all JAR files and redeploy" is the accepted key, but the real fix is to rebuild and re-sign correctly (or strip stale signatures). Answer B. |
| **(Exam 1 · Q52)** | The "Transfer Appliance Rehydrator" step is from the first-generation appliance; Google now uploads the data for you. The key (Transfer Appliance) still stands. |
| **(Exam 1 · Q48)** | The option says `gcloud datastore create-indexes`, the explanation says `gcloud datastore indexes create`. Same action; the second is the current command. |
| **(Exam 2 · Q42)** | "Cloud Run for Anthos" is now Knative serving on GKE Enterprise, and Traffic Director is Cloud Service Mesh. The answer (revision + traffic split) is unchanged. |

---

## Last-minute cheat sheet

- GKE update, minimal downtime → **`kubectl set image`** (rolling update) (Exam 1 · Q53).
- App Engine canary → **new version + split traffic** (Exam 2 · Q27). Cloud Run canary → **new revision + split traffic** (Exam 2 · Q42).
- New template only for new MIG instances → **opportunistic** rolling update (Exam 2 · Q50).
- Fast rollback with DB changes → **separate schema pipeline + gradual traffic split** (Exam 5 · Q32).
- No infra + K8s manifest → **`gcloud` cluster, `kubectl` deploy** (Exam 1 · Q58).
- Small app, high utilization → **GKE + versioned image + staging namespace** (Exam 2 · Q4).
- Faster Docker builds → **small base image + copy source last** (Exam 4 · Q51). JAR SHA1 digest error → **sign JARs, redeploy** (Exam 4 · Q52).
- Cloud Deploy to private GKE → **private pool peered to the cluster VPC** (Exam 5 · Q43).
- Terraform governance → **impersonation, plan on PR, approval before apply** (Exam 5 · Q72).
- YAML IaC, low ops → **Config Controller** (Exam 5 · Q74). GKE + EKS config and policy → **Config Sync + Policy Controller** (Exam 5 · Q82).
- Limit total API calls → **Apigee Quota** (Exam 5 · Q11). Stable API in front of a changing backend → **Apigee facade** (Exam 5 · Q38).
- Breaking change → **new major version** (Exam 3 · Q11).
- 5xx / 429 → **truncated exponential backoff** (Exam 2 · Q31). Pub/Sub publish latency → **disable batching** (Exam 4 · Q21).
- Many entities by ID → **batch get with keys** (Exam 2 · Q1). Browser upload → **CORS + signed URL** (Exam 4 · Q6).
- ~10 TB, 1 Gbps → **compress + parallel copy** (Exam 3 · Q20), (Exam 4 · Q10), (Exam 4 · Q37).
- Other cloud → **Storage Transfer Service** (Exam 3 · Q61).
- 75 TB+ on-prem or slow/shared link → **Transfer Appliance** (Exam 1 · Q52), (Exam 4 · Q49), (Exam 5 · Q56), (Exam 5 · Q66).
- Verify uploads → **CRC32C compare, no download** (Exam 3 · Q26).
- One writer, many read-only on-prem copies → **Cloud SQL + external replicas** (Exam 5 · Q26).
- No local installs → **Cloud Shell** (Exam 3 · Q63). Persistent tool → **`~/bin`** (Exam 1 · Q39).
- Datastore indexes → **`gcloud datastore indexes create index.yaml`** (Exam 1 · Q48).
