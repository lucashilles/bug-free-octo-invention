# Domain 3 Study Guide — Configuring and Deploying Applications

> Condensed from the 104-question bank in [`03-deploying-applications.md`](03-deploying-applications.md). Citations look like (Exam N · QM). Several scenarios repeat across exams, so look for paired citations. Many explanations still use old names (Stackdriver = Cloud Monitoring / Cloud Logging); see ⚠️ for the items that look outdated or weak.

---

## 1. Choosing where to deploy

### Key facts
- **Container image, no OS dependencies, least ops:** deploy it to **Cloud Run**. GKE Autopilot still means Kubernetes management, GKE Standard means more, and Compute Engine means managing VMs, scaling, health checks and OS updates (Exam 6 · Q12).
- **Microservice in C++ with custom libraries, minimal infrastructure management:** **Cloud Build** builds the container, **Cloud Run** runs it. Cloud Functions suits short, event-driven tasks rather than a continuously running microservice with custom native libraries. A Container-Optimized OS VM or standard GKE adds infrastructure work (Exam 4 · Q51).
- **Static site (HTML, CSS, JS, images) with minimal effort:** upload it to a **Cloud Storage** bucket configured for website hosting. App Engine, a VM with Apache, or a GKE container is overkill (Exam 3 · Q34).
- **Whole website with variants to compare:** App Engine (versions + traffic splitting) or Cloud Run (revisions + traffic splitting). Cloud Functions is the wrong shape for hosting a whole website (Exam 1 · Q34), (Exam 4 · Q5).
- **Custom domain on App Engine** (`www.example.com`): **verify domain ownership**, then create a **CNAME to `ghs.googlehosted.com`**. Don't use an A record to a "single global App Engine IP", and don't use `dispatch.yaml`, which routes requests *within* the app between services (Exam 3 · Q12).

### Platform selector

| Scenario wording | Pick | Reject | Source |
|---|---|---|---|
| Container, "reduce infrastructure management", no OS dependencies | **Cloud Run** | GKE Autopilot/Standard, Compute Engine | (Exam 6 · Q12) |
| Custom native libraries, minimal management | **Cloud Build → Cloud Run** | Cloud Functions, COS VM, GKE | (Exam 4 · Q51) |
| Static content only | **Cloud Storage** website | App Engine, VM, GKE | (Exam 3 · Q34) |
| Needs stable identity + its own disk per replica | **GKE StatefulSet** (see §2) | Deployment | (Exam 2 · Q1) |
| Header-based routing (user-agent, OS) | **GKE + Anthos Service Mesh** (see §6) | Cloud Run tags, App Engine IP split | (Exam 3 · Q3) |
| Legacy .NET app, containers not yet approved | **Compute Engine image built per build by Cloud Build** (see §8) | .NET Core rewrite for Cloud Run, GKE, Web Deploy onto a base image | (Exam 5 · Q31) |

### Decision rules
- When the stem says "minimal management" and the workload is a stateless container, choose **Cloud Run** before any GKE option (Exam 6 · Q12), (Exam 4 · Q51).
- When there is no server-side logic at all, choose **Cloud Storage** (Exam 3 · Q34).
- For an App Engine custom domain, the answer is always **verify + CNAME `ghs.googlehosted.com`** (Exam 3 · Q12).

### Traps
- "GKE Autopilot" sounds managed, but it is still Kubernetes. Cloud Run wins on operational simplicity (Exam 6 · Q12).
- `dispatch.yaml` is not domain mapping (Exam 3 · Q12).
- "Split the site into three services/functions" to test three designs adds complexity. Use **one service with versions/revisions and traffic splitting** (Exam 1 · Q34), (Exam 4 · Q5).

---

## 2. GKE workload objects and in-cluster service discovery

### Key facts
- **Deployment** manages replicas of stateless Pods. Use one Deployment per microservice so each can have its own replica count (Exam 1 · Q43), (Exam 2 · Q47).
- **StatefulSet** gives each Pod a **stable network identity** (persistent hostname/DNS), **its own PersistentVolumeClaim**, and ordered scaling. Pick it when replicas each need "a stable network identity and its own persistent disk" (Exam 2 · Q1).
- **DaemonSet** runs one Pod **on every node**. Node-level agents (third-party logging/monitoring) go here. Don't embed agents in app images, SSH into nodes, or use a Deployment, which doesn't guarantee one per node (Exam 2 · Q10).
- **Service** gives a stable virtual IP plus a cluster DNS name (`name.namespace.svc.cluster.local`) and load-balances across Pods. Clients inside the cluster **use the Service name in the URL** (Exam 1 · Q23), (Exam 1 · Q43), (Exam 2 · Q47).
- **ClusterIP** Service = reachable only inside the cluster. **NodePort** exposes on node ports outside the cluster (Exam 3 · Q14).
- **Ingress** is for **external** HTTP(S) traffic into the cluster. On GKE an Ingress provisions an HTTP(S) load balancer. To serve a second domain on the **same external IP**, **add a host rule to the existing Ingress**. A new Ingress or a new `LoadBalancer` Service provisions a new IP (Exam 2 · Q18).
- **Namespace + Kubernetes RBAC** isolate teams inside one cluster. To let another team **deploy its own workloads without being able to modify yours**, create a **new namespace** and grant that team the **Admin role on the namespace** (a RoleBinding) with Kubernetes RBAC. Project-level IAM Viewer can't deploy, project-level IAM Editor reaches every namespace, and a whole new cluster adds cost and overhead (Exam 5 · Q13).

### Object comparison

| Need | Object | Source |
|---|---|---|
| N interchangeable stateless replicas | Deployment | (Exam 1 · Q43), (Exam 2 · Q47) |
| Stable hostname + own disk per replica | StatefulSet | (Exam 2 · Q1) |
| One agent Pod per node | DaemonSet | (Exam 2 · Q10) |
| Stable internal address for a set of Pods | Service (ClusterIP) + Service DNS name | (Exam 1 · Q23), (Exam 3 · Q14) |
| Several external domains on one LB IP | One Ingress with multiple host rules | (Exam 2 · Q18) |
| Another team deploys into your cluster but can't touch your app | New namespace + Kubernetes RBAC Admin on that namespace | (Exam 5 · Q13) |

### Decision rules
- "Specific number of replicas per microservice + uniform addressing" → **Deployment + Service + Service DNS name** (Exam 1 · Q43), (Exam 2 · Q47).
- "Only other services in the cluster may call it" → **ClusterIP** (Exam 3 · Q14).
- "Install X on every node" → **DaemonSet** (Exam 2 · Q10).
- Permissions scoped to part of a cluster → **Kubernetes RBAC on a namespace**; project-level IAM roles apply to the whole cluster (Exam 5 · Q13).

### Traps
- Bare **Pods** instead of Deployments: no replica management or self-healing (Exam 1 · Q43), (Exam 2 · Q47).
- **Ingress for service-to-service traffic** inside the cluster is wrong (Exam 1 · Q43), (Exam 2 · Q47).
- "GKE Endpoint" / Cloud DNS A records for in-cluster discovery add pointless layers. Kubernetes DNS already does it (Exam 1 · Q23).
- ReplicaSet and ReplicationController don't give stable identity or per-Pod storage. ReplicationController is legacy (Exam 2 · Q1).
- Converting a stateless Deployment to a StatefulSet just to roll out safely adds complexity (Exam 3 · Q49).
- "New namespace + IAM Editor on the project" looks isolated, but the IAM role isn't namespace-scoped, so the other team could still modify your app (Exam 5 · Q13).

---

## 3. Pod lifecycle: probes, hooks and graceful shutdown

### Key facts
- Kubernetes sends **SIGTERM** before killing a container. To close DB connections cleanly during a Deployment update, **handle SIGTERM in the code** (Exam 2 · Q59).
- `terminationGracePeriodSeconds` only gives *more time*. A **PodDisruptionBudget** only limits voluntary disruptions. A **preStop** hook runs extra logic. None of them fixes code that ignores SIGTERM (Exam 2 · Q59).
- The bank's key for "check DB connectivity and run a graceful shutdown script on failure" is a **livenessProbe that fails without DB connectivity + a preStop handler** for the shutdown script. An initContainer only checks once before start, PostStart runs once after start, and separate Jobs are complex and slow (Exam 1 · Q19, see ⚠️).
- A legacy app whose config lives on NFS: mount it via a **PersistentVolumeClaim** and start the service with an **ENTRYPOINT script** that verifies the config before serving. Baking config into the image forces rebuilds; a node startup script couples config to infrastructure (Exam 2 · Q4).
- **Preemptible VMs** (Compute Engine) get a shutdown script. Make the script send the application a **Linux signal** so it disconnects from the database. Polling a file every 5 minutes is too slow; broadcasting to logged-in users or publishing to Pub/Sub doesn't stop the process cleanly (Exam 3 · Q40).
- **The three probes:** a **readinessProbe** decides whether the Pod is in the Service's endpoints, so it controls **whether the load balancer sends it traffic**; a **livenessProbe** restarts a stuck container; a **startupProbe** holds off liveness (and readiness) checks until the app has started. To use `/healthz` for "should the LB route to this Pod?", configure `readinessProbe: httpGet: {path: /healthz, port: 80}` (Exam 5 · Q20).
- **Slow, variable startup makes the liveness probe fail** → add a **startupProbe**. Lengthening the liveness `initialDelaySeconds` delays detection of real hangs on every start; more CPU or a readiness probe doesn't stop the restarts (Exam 5 · Q49).
- **Pod in `CrashLoopBackOff`:** the container starts and then exits repeatedly. First step: **`kubectl logs POD_NAME`** (add **`--previous`** for the crashed run) to read stdout/stderr. `kubectl exec` usually can't attach to a crashing container and app logs aren't in `/var/log/messages`. Registry permissions show up as **`ImagePullBackOff`**/`ErrImagePull`, not CrashLoopBackOff (Exam 5 · Q36).

### Probe selector

| Need | Probe | Source |
|---|---|---|
| Only send LB/Service traffic when the app can serve | **readinessProbe** | (Exam 5 · Q20) |
| Restart a hung container | **livenessProbe** | (Exam 5 · Q20), (Exam 1 · Q19) |
| Slow start trips the liveness probe | **startupProbe** | (Exam 5 · Q49) |

### Decision rules
- "App crashes/aborts DB connections during rollout" → **SIGTERM handler** first (Exam 2 · Q59).
- "Continuous health check + shutdown script" → **probe + preStop**, not init/PostStart (Exam 1 · Q19).
- "Graceful shutdown on preemption" → **shutdown script → signal to process** (Exam 3 · Q40).
- "Decide whether traffic is routed to the Pod" → **readiness**; "restart if stuck" → **liveness**; "slow to boot" → **startup** (Exam 5 · Q20), (Exam 5 · Q49).
- Troubleshoot by status: `CrashLoopBackOff` → **container logs**; `ImagePullBackOff` → **image name/registry IAM** (Exam 5 · Q36).

### Traps
- Raising `terminationGracePeriodSeconds` looks helpful but doesn't make the app react (Exam 2 · Q59).
- `COPY` config into the image (Exam 2 · Q4) and "one image per environment" (Exam 3 · Q26) are both config-in-image anti-patterns.
- `healthCheck:` and `loadbalancerHealthCheck:` aren't Pod spec fields; on GKE the Ingress load balancer health check is derived from the **readinessProbe** (Exam 5 · Q20).
- Raising `initialDelaySeconds` on the liveness probe is the tempting fix for slow starts, but a **startupProbe** is the purpose-built answer (Exam 5 · Q49).
- Checking Artifact Registry IAM or VPC egress logs for a CrashLoopBackOff: the image already pulled, so look at the app's own logs (Exam 5 · Q36).

---

## 4. Configuration and storage for deployed apps

### Key facts
- **Compute Engine instance metadata** is the built-in way to pass per-instance or per-environment configuration. The app **queries the metadata server** at runtime (Exam 2 · Q7), (Exam 3 · Q26).
- **Golden image across test/staging/prod:** set a metadata key such as `DATABASE` at instance creation and **read it from the metadata server**. Metadata does **not** appear as an environment variable automatically, so the "read the DATABASE env var" option is wrong (Exam 3 · Q26).
- **Same custom image, several MIGs, different config each:** put the values in **each instance template's metadata** (Exam 3 · Q36).
- **Service endpoint/version discovery for new VMs:** endpoint details as **metadata fetched at runtime**. Labels organize resources; they aren't runtime config. A fixed hostname/port is inflexible (Exam 2 · Q7).
- **One project per environment (dev, QA, staging, prod):** set a **project-wide metadata key** such as `environment` once in each project; every instance inherits it and the deployment tool reads it from the metadata server. Setting instance metadata at each launch is repetitive and error-prone, a startup script that derives the environment from the project name is brittle, and a deployment-tool instance per project is overhead (Exam 5 · Q44).
- **Shared read/write config file for many instances, no code rewrite:** **Filestore** mounted as an **NFS PersistentVolume**. This is the answer both when lifting a legacy app and when splitting a monolith into GKE microservices that share the file (Exam 4 · Q25), (Exam 5 · Q59).
- **Expanded a persistent disk but Pods don't see the space:** edit **`spec.resources.requests.storage` on the PVC** and apply it (the StorageClass must allow volume expansion). Don't edit the PV's capacity, redeploy, or run `fdisk` in the Pod (Exam 4 · Q58).

### Storage selector

| Requirement | Choose | Reject | Source |
|---|---|---|---|
| Many Pods read + write one file, NFS, no code change | **Filestore NFS PV** | Shared PD (complex ReadWriteMany setup, single point of failure), ConfigMap (not built for concurrent modification), GCS FUSE (performance overhead) | (Exam 4 · Q25), (Exam 5 · Q59) |
| Each replica has its own disk | StatefulSet + PVC per Pod | Deployment | (Exam 2 · Q1) |
| Legacy config on existing NFS share | PVC + ENTRYPOINT check | gsutil in container, COPY in image | (Exam 2 · Q4) |
| Grow a volume | Edit **PVC** request | Edit PV, fdisk | (Exam 4 · Q58) |

### Decision rules
- One image, different environments on Compute Engine → **metadata + metadata server** (Exam 3 · Q26), (Exam 3 · Q36).
- Pick the metadata scope that matches what varies: environment = project → **project metadata**; per MIG → **instance template metadata**; per instance → **instance metadata** (Exam 5 · Q44), (Exam 3 · Q36), (Exam 3 · Q26).
- Shared writable file system on GKE → **Filestore** (Exam 4 · Q25), (Exam 5 · Q59).

### Traps
- Instance **tags/labels** for config values (Exam 2 · Q7), (Exam 3 · Q26).
- Startup script with hardcoded values, Bigtable or a PD for small config (Exam 3 · Q36).
- Editing the **PV** instead of the **PVC** (Exam 4 · Q58).
- A ConfigMap volume for a file the app **writes**: ConfigMap volumes are read-only and size-limited (Exam 5 · Q59).

---

## 5. Secrets on GKE

### Key facts
- **Recommended pattern:** store the secret in **Secret Manager**, grant a **Google service account (GSA)** access, run the Pod as a **Kubernetes service account (KSA)**, and bind KSA → GSA with **Workload Identity**. No keys to export, and the secret isn't readable through the Kubernetes API server (Exam 1 · Q41), (Exam 3 · Q25).
- A **Kubernetes Secret** injected as an env var is base64-encoded and is exposed through the Kubernetes API (Exam 1 · Q41), (Exam 3 · Q25).
- **Application-layer Secrets Encryption** (Cloud KMS key) encrypts Secrets at rest in etcd, but they are still served by the API server (Exam 1 · Q41), (Exam 3 · Q25).
- When Secret Manager isn't among the options and the task is "store DB credentials for an on-prem DB with rotation", the bank keys **Kubernetes Secret + Cloud KMS plugin** for encryption (Exam 3 · Q46, see ⚠️).

### Decision rules
- If Secret Manager + Workload Identity is an option, pick it (Exam 1 · Q41), (Exam 3 · Q25).
- Reject any option that **exports a service account key as JSON** (into a ConfigMap or volume) (Exam 1 · Q41), (Exam 3 · Q25).

### Traps
- "Store it in Cloud KMS": KMS manages *keys*, not secrets (Exam 3 · Q25).
- Sidecar proxy, service mesh or an encrypted PVC don't solve credential storage and rotation (Exam 3 · Q46).

---

## 6. Rollout strategies and traffic splitting

### Key facts
- **Canary:** route a **small share of real traffic** to the new version, watch metrics, increase gradually. It minimizes how many users a production-only bug can hit (Exam 1 · Q37). In a **CD pipeline with Cloud Monitoring** it's the automated answer when load testing wasn't possible (Exam 1 · Q26).
- **Blue/green:** two full environments, switch all traffic; the selling point is **fast, complete rollback** (Exam 1 · Q46).
- **Rolling update:** replaces instances sequentially. Zero downtime, but no fine-grained traffic control and an issue can still reach a large share of users (Exam 1 · Q37), (Exam 2 · Q57).
- **Recreate:** downtime (Exam 1 · Q37), (Exam 2 · Q57).
- **Traffic mirroring (shadowing):** copy live traffic to the new version without affecting users, so you can **test against the full production load before launch** (Exam 2 · Q27).
- **A/B test for a business metric** (sales, conversion): split a predetermined percentage between variants and look for a **statistically significant difference** (Exam 2 · Q32). "Randomized" A/B test of a recommendation algorithm → **weighted traffic splitting between versions**; header-based routing targets conditions rather than randomizing, mirroring shows users nothing, and a flag on one instance isn't a controlled split (Exam 5 · Q25). Three designs → one service with **traffic splitting** across versions/revisions (Exam 1 · Q34), (Exam 4 · Q5).
- **Feature flag:** turn new code on for **specific, identified users** (e.g. customers who signed up to test). Cloud Run percentage splitting picks requests at random, so it can't target a named group; blue/green swaps everyone; session affinity only pins a client to an instance (Exam 5 · Q58).
- **Kubernetes RollingUpdate knobs:** `maxSurge` = extra Pods allowed above `replicas`; `maxUnavailable` = Pods allowed below it. **`maxSurge: 1`, `maxUnavailable: 0`** starts one new Pod and removes an old one only after the new one is Ready, so old replicas are kept until the new one is healthy. `maxSurge: 0`, `maxUnavailable: 1` takes an old Pod down first. `Recreate` has no surge/unavailable settings and causes downtime (Exam 5 · Q57).
- **Compute Engine MIG rolling update** uses the same two knobs. To **minimize cost and keep the instance count constant**, use **`maxSurge: 0`, `maxUnavailable: 1`**: no extra VMs are created; one instance at a time is replaced and must pass its health check before the update moves on (Exam 5 · Q10).
- **Cloud Run gradual release:** deploy the new revision with **"Serve this revision immediately" off** (no traffic), give it a small percentage, monitor, then increase (Exam 6 · Q2), (Exam 4 · Q30).
- **GKE + Anthos Service Mesh (Istio):** two Deployments labeled with version names + an **Istio routing rule** sending a small percentage to the new one gives zero-downtime A/B/canary (Exam 2 · Q57). Mesh routing can match **HTTP headers such as `user-agent`**, so "route by operating system" points to ASM (Exam 3 · Q3).

### Strategy selector

| Requirement in the stem | Strategy | Source |
|---|---|---|
| Issues only appear with real users; limit the number affected | **Canary** | (Exam 1 · Q37) |
| Automated, no prior load test, avoid performance glitches | **CD pipeline + canary + Cloud Monitoring** | (Exam 1 · Q26) |
| Swift full rollback | **Blue/green** | (Exam 1 · Q46) |
| Full production load before launch, no user impact | **Traffic mirroring** | (Exam 2 · Q27) |
| Does variant X increase sales? | **A/B split + statistical analysis** | (Exam 2 · Q32) |
| Randomized A/B test of a new algorithm | **Weighted traffic split between versions** | (Exam 5 · Q25) |
| Only customers who signed up see the change | **Feature flag** | (Exam 5 · Q58) |
| GKE: keep old replicas until the new one is healthy | **RollingUpdate, `maxSurge: 1`, `maxUnavailable: 0`** | (Exam 5 · Q57) |
| MIG: minimize cost, constant instance count | **Rolling update, `maxSurge: 0`, `maxUnavailable: 1`** | (Exam 5 · Q10) |
| Segment by OS/user-agent with quick rollback | **GKE + ASM header routing** | (Exam 3 · Q3) |
| Cloud Run, gradual, least config | **No-traffic revision + percentage split** | (Exam 6 · Q2), (Exam 4 · Q30) |

### Decision rules
- "Minimal configuration" on Cloud Run → use **built-in revision traffic splitting**, not a load balancer or code-level routing (Exam 6 · Q2).
- "Small portion of users first, then everyone" → **traffic splitting / canary**, not "smoke test then 100%" (Exam 4 · Q30).
- For the key **"safest rollout of a new GKE revision"**, the bank's answer is **rolling update + PodDisruptionBudget**, not a StatefulSet conversion or an HPA scale-down policy (Exam 3 · Q49, see ⚠️).
- Surge vs unavailable: "keep capacity / keep old until new is healthy" → **surge 1, unavailable 0**; "no extra cost / no extra instances" → **surge 0, unavailable 1** (Exam 5 · Q57), (Exam 5 · Q10).
- **Random share of users** → traffic split; **named group of users** → feature flag (Exam 5 · Q25), (Exam 5 · Q58).

### Traps
- Blue/green doesn't give gradual exposure; canary doesn't give the fastest complete rollback (Exam 1 · Q37), (Exam 1 · Q46).
- **Feature flag to half of all users** looks like A/B, but the bank rejects it for not giving the clean, predetermined traffic split of the LB option (Exam 2 · Q32). The reverse holds for a hand-picked tester group, where the feature flag wins over percentage splitting (Exam 5 · Q58).
- `Recreate` with `maxSurge`/`maxUnavailable` values is a distractor: those fields belong to `RollingUpdate` only (Exam 5 · Q57).
- Traffic mirroring and HTTP header routing are not randomized A/B tests (Exam 5 · Q25).
- Cloud Run tags/revisions and App Engine IP-based splits can't target an OS (Exam 3 · Q3).
- Separate namespaces don't give traffic control by percentage (Exam 2 · Q57).
- Weekly load tests or local load tests don't reduce the blast radius of a new feature (Exam 4 · Q30).

---

## 7. Autoscaling deployed workloads

### Key facts
- **HPA** changes **Pod count**; **VPA** changes **Pod size** (requests/limits); **Cluster Autoscaler** changes **node count**. For "pods and nodes follow CPU" → **Cluster Autoscaler + HPA on CPU** (Exam 4 · Q29).
- **Stateless service, autoscaling needed urgently with minimal changes** → **HPA on CPU**. A custom-metric HPA or any VPA takes longer to set up (Exam 1 · Q27), (Exam 1 · Q39).
- **Internal service that must scale rapidly** → **HPA + ClusterIP Service** (Exam 3 · Q14).
- **Pub/Sub consumer with bursty publishing** → **HPA on an external metric** such as `pubsub.googleapis.com/subscription/num_undelivered_messages`. CPU may not track backlog (Exam 1 · Q12).
- **Compute Engine MIG latency spikes while scaling on CPU** → **lower the target CPU utilization** (scale out earlier) and **shorten the cooldown/initialization period** (Exam 1 · Q14). Never remove health checks; there is no "AUTOSCALE" label.
- **Right-size Cloud Spanner for cost without hurting reliability:** watch **CPU utilization in Cloud Monitoring** and reduce processing units gradually to the minimum needed. Error logs, Trace RPS and Snapshot Debugger don't measure capacity (Exam 3 · Q24).
- **Cloud Run slows down and returns errors only under a high-load test:** check whether the service hit its **maximum instances** limit and **raise max instances**. Min instances only keeps instances warm against cold starts; splitting traffic to an old revision or disabling Cloud Armor doesn't add capacity (Exam 5 · Q11).
- **Cap App Engine standard at 5 instances:** **`basic_scaling` with `max_instances: 5`** (plus `idle_timeout`, e.g. 10m). **Manual scaling** runs a fixed `instances` count and has no `max_instances`; `min_pending_latency` is an automatic-scaling setting (Exam 5 · Q45, see ⚠️).

### Autoscaler comparison

| Signal / need | Tool | Source |
|---|---|---|
| More Pods under CPU load, fastest to implement | HPA (CPU) | (Exam 1 · Q27), (Exam 1 · Q39) |
| Queue backlog drives work | HPA (external metric) | (Exam 1 · Q12) |
| Nodes as well as Pods | Cluster Autoscaler + HPA | (Exam 4 · Q29) |
| Bigger/smaller Pods | VPA (not for bursts) | (Exam 1 · Q12), (Exam 3 · Q14) |
| VM fleet | MIG autoscaler: lower target, shorter cooldown | (Exam 1 · Q14) |
| Cloud Run errors under peak load | Raise **max instances** | (Exam 5 · Q11) |
| App Engine standard, hard upper bound | **basic_scaling `max_instances`** | (Exam 5 · Q45) |

### Decision rules
- Tight deadline beats elegance: **CPU-based HPA** (Exam 1 · Q39).
- Messages waiting → **external metric**, not resource utilization (Exam 1 · Q12).
- Serverless app fails only at peak → look for a **scaling ceiling** (max instances) before anything else (Exam 5 · Q11).

### Traps
- Enabling **MIG autoscaling on GKE node pools directly** instead of Cluster Autoscaler (Exam 4 · Q29).
- **VPA Recommendation mode** doesn't scale anything (Exam 1 · Q12).
- Raising the CPU target delays scale-out and makes latency worse (Exam 1 · Q14).
- Raising Cloud Run **min** instances to match load-test users: costs money and doesn't lift the ceiling (Exam 5 · Q11).
- "Manual scaling with max instances 5": manual scaling has no maximum, only a fixed count (Exam 5 · Q45).

---

## 8. CI/CD deployment pipelines

### Key facts
- **Cloud Build trigger on push** to a branch runs the existing `cloudbuild.yaml` (build + `gcloud run deploy`). Pub/Sub, webhook triggers and cron jobs are extra plumbing (Exam 3 · Q58).
- **Simplest fully managed continuous deployment to Cloud Run** per commit (bank key): **Cloud Build trigger** that builds and deploys. Workstation cron jobs and self-managed Jenkins are rejected (Exam 2 · Q21, see ⚠️).
- **Release only specific commits on the main branch:** trigger on a **Git tag pattern** (e.g. `v*`) with a tag convention (Exam 2 · Q8).
- **Cloud Build deploys Cloud Functions and fails right after code validation:** the **Cloud Build service account lacks the Cloud Functions Developer role**. Instance limits, trigger parameters and retries with backoff don't fix permissions (Exam 1 · Q42).
- **Cloud Deploy Dev → Test auto-promotion** (bank key): a **Cloud Function triggered by SUCCEEDED messages on the `clouddeploy-operations` topic** calls the Cloud Deploy API to promote. The `cloud-builds` topic carries build events, not deploy events (Exam 2 · Q44, see ⚠️).
- **Isolated, automated test environment for Cloud Run system tests:** **Cloud Build runs Terraform** to create a **new project** and deploy the service there. A new revision in the production project lacks isolation; gcloud scripts are less declarative (Exam 4 · Q49).
- **Versioned, auditable infrastructure + Google-managed tooling + serverless app:** keep app **and** infrastructure code in **Git**, have **Cloud Build apply Terraform**, and deploy the app to a serverless target (the key uses **Cloud Functions**) in a pipeline step. Plain `gcloud` commands for infrastructure aren't versioned IaC, self-hosted Jenkins isn't Google-managed, and a container on a Compute Engine VM isn't serverless (Exam 5 · Q32, see ⚠️).
- **Promote one image through Dev → Test → Prod:** reference it by its **digest** (`image@sha256:…`), which is immutable. `latest` and even semantic-version tags are mutable and can be moved to different content; a unique image name doesn't pin content either (Exam 5 · Q18).
- **Copy assets as part of a promotion:** add a **`gcr.io/cloud-builders/gsutil` step** to `cloudbuild.yaml` before the promote step, e.g. `cp -r gs://webphotos-staging gs://webphotos-prod`. Manual copies break automation; a startup script in `app.yaml` mixes data movement into the app runtime (Exam 5 · Q5, see ⚠️).
- **Legacy .NET app, containers not approved, consistent results across environments:** have **Cloud Build bake a new Compute Engine image for every build** and deploy **that same image** to every environment (an immutable golden image). A .NET Core rewrite for Cloud Run is a big change, GKE needs containers, and Web Deploy onto a patched base image lets environments drift (Exam 5 · Q31).

### Decision rules
- Deploy step fails, code is fine → **check the build service account's IAM role** (Exam 1 · Q42).
- "Release commits" → **tags**; "every push to dev" → **branch trigger** (Exam 2 · Q8), (Exam 3 · Q58).
- "Separate from production, fully automated" → **new project via IaC** (Exam 4 · Q49).
- "Same artifact in every environment": containers → **image digest**; VMs → **one image per build reused everywhere** (Exam 5 · Q18), (Exam 5 · Q31).
- "Versioning and auditability of infrastructure" → **Git + Terraform run by Cloud Build** (Exam 5 · Q32).

### Traps
- A second repository just for release builds fragments history (Exam 2 · Q8).
- Cloud Build monitoring Pub/Sub to drive promotion, or the gke-deploy builder, is not the bank's Cloud Deploy answer (Exam 2 · Q44).
- Semantic-version tags feel safe, but tags can be re-pointed; only the digest guarantees identical bits (Exam 5 · Q18).
- An option that deploys to Cloud Run but creates infrastructure with `gcloud` loses on the IaC requirement, even though Cloud Run is serverless (Exam 5 · Q32).

---

## 9. Supply-chain security: Binary Authorization

### Key facts
- **Only images built by the pipeline may run on GKE** → **Cloud Build + Artifact Registry + Binary Authorization**. Cloud Deploy and Cloud Armor (a WAF) don't enforce image policy; Cloud Storage isn't the image repository (Exam 2 · Q15).
- **Only images that passed regression tests:** create an **attestor and a policy**, and add a **Cloud Build step that creates an attestation** for images that pass. Voucher adds needless components; a vulnerability-scan attestation proves a different thing; Pod Security Standards don't verify provenance (Exam 6 · Q14).
- **Only images that passed UAT reach production:** after UAT, **sign the attestation with a key in Cloud KMS** and add a **cluster-specific rule in the production project's** Binary Authorization policy. Keys as Kubernetes Secrets and rules in the UAT project are wrong (Exam 4 · Q18).
- **Block images with known critical vulnerabilities:** enable the **Container Scanning API**, review results **programmatically** in the pipeline, create an **attestation** for clean images, and enforce it with **Binary Authorization**. Web Security Scanner crawls web apps, not images; manual console review doesn't scale (Exam 3 · Q30).
- **Binary Authorization works on Cloud Run too**, not just GKE. "Only tested images reach Cloud Run, minimal overhead" → **enable Binary Authorization on the Cloud Run service** and attest images that pass tests. A no-traffic tagged revision is a manual test step that doesn't block untested images; **build provenance** records how an image was built but doesn't enforce anything by itself (Exam 5 · Q38).
- **Cloud Build → Artifact Registry → Cloud Deploy → Cloud Run, "only secure images":** a **Binary Authorization policy that admits only images signed with a trusted key**. Encrypting the image with KMS, storing it in Secret Manager or putting Cloud Armor in front of Cloud Run doesn't verify images (Exam 5 · Q42).
- **Only pipeline-built images *and* no data exfiltration:** **Cloud Build private worker pool** + **VPC Service Controls** perimeter around the CI/CD services (Cloud Build, Artifact Registry, GKE) + **Binary Authorization** on the cluster. The default worker pool runs outside your network; CMEK protects data at rest and firewall rules don't stop exfiltration through Google APIs (Exam 5 · Q33).

### Decision rules
- The attestation must match the gate in the stem: tests passed → test attestation; UAT passed → UAT attestation; no critical CVEs → scan attestation (Exam 6 · Q14), (Exam 4 · Q18), (Exam 3 · Q30), (Exam 5 · Q38).
- Enforcement lives in the **target (production) project's policy** (Exam 4 · Q18).
- Signing keys live in **Cloud KMS** (Exam 4 · Q18).
- "Which images may *run*" → **Binary Authorization**; "data must not leave the environment" → **VPC Service Controls** (+ private pool for builds) (Exam 5 · Q33), (Exam 5 · Q42).

### Traps
- Cloud Armor in a supply-chain question (Exam 2 · Q15), (Exam 5 · Q42).
- Web Security Scanner for container CVEs (Exam 3 · Q30).
- KMS-encrypting an image or storing it in Secret Manager: neither is how images are secured; images live in Artifact Registry and are *signed* (attested), not encrypted, for deployment control (Exam 5 · Q42).
- Answers that have Binary Authorization but the **default worker pool** miss the exfiltration requirement; CMEK-only answers miss it too (Exam 5 · Q33).

---

## 10. Networking and connectivity for deployed apps

### Key facts
- **Cloud Run → Cloud SQL over private IP** (bank key): configure a **Serverless VPC Access connector** on the Cloud Run service (Exam 3 · Q5). The full managed pattern: Cloud SQL and Cloud Run **in the same project**, Cloud SQL **private IP + private services access**, Cloud Run uses the connector (Exam 3 · Q39).
- **Cloud Run → Memorystore gives 502 Bad Gateway:** the **connector is in a different region** from the Cloud Run service; all components must be in the same region. Memorystore doesn't need a public IP (Exam 4 · Q22).
- **Compute Engine VMs → Cloud SQL without IP allowlisting:** enable **private IP** on the Cloud SQL instance (Exam 3 · Q19).
- **Clients in the same VPC find a VM-hosted API:** Compute Engine **internal DNS**, `https://[INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal/`. External IPs, load balancers and A records are overkill (Exam 3 · Q4).
- **Hybrid microservices crash on latency over Cloud VPN** with fluctuating bandwidth: **add Cloud VPN tunnels** for more bandwidth and redundancy (Exam 2 · Q39). Caching PII in Memorystore conflicts with the compliance reason it stays on-prem.
- **Istio: requests to certain URLs fail, others between the same Pods succeed** → an **AuthorizationPolicy** blocking those **paths**. NetworkPolicy works at L3/L4 (not URLs), a wrong port or an mTLS mismatch would break all requests (Exam 1 · Q4), (Exam 1 · Q32).
- **`kubectl` from Cloud Shell times out silently** against a GKE cluster with a public endpoint, after `get-credentials` succeeded: Cloud Shell's (ephemeral) external IP isn't in the cluster's **authorized networks** (control plane allowlist). Missing IAM rights give an explicit permission error, not a timeout; Cloud Shell doesn't need to be in the cluster's VPC to reach a public endpoint (Exam 5 · Q8, see ⚠️).

### Layer comparison

| Control | Works on | Can fail "only some URLs"? | Source |
|---|---|---|---|
| Kubernetes NetworkPolicy | IP/port (L3/L4) | No | (Exam 1 · Q4), (Exam 1 · Q32) |
| Istio mTLS (PeerAuthentication) | Connection encryption | No, affects all traffic | (Exam 1 · Q4) |
| Istio **AuthorizationPolicy** | HTTP method/path (L7) | **Yes** | (Exam 1 · Q4), (Exam 1 · Q32) |

### Decision rules
- Serverless → private VPC resource: **connector, same region** (Exam 3 · Q5), (Exam 4 · Q22).
- Path-specific failures in a mesh → **AuthorizationPolicy** (Exam 1 · Q32).
- "No allowlisting" for Cloud SQL → **private IP** (Exam 3 · Q19).
- Timeout with no error to a GKE control plane → **authorized networks**; an error message → **IAM/RBAC** (Exam 5 · Q8).

### Traps
- Cross-project VPN between Cloud Run and Cloud SQL, or self-managed PostgreSQL on a VM (Exam 3 · Q39).
- Firewall rules as the cause of a Cloud Run → Memorystore failure (Exam 4 · Q22).
- Lowering the VPN MTU or adding a service mesh for a bandwidth problem (Exam 2 · Q39).
- "Cloud Shell isn't in the same VPC" sounds plausible, but a public endpoint is reachable from anywhere that's allowlisted (Exam 5 · Q8).

---

## 11. Compute Engine deployment operations and troubleshooting

### Key facts
- **Image built (Packer) but won't boot:** read the **serial port output** (also visible in Cloud Logging). Don't rebuild blindly or export and mount the disk first (Exam 1 · Q52).
- **One instance failing and SSH unresponsive:** **enable and inspect serial port output** before restarting or replacing it (Exam 1 · Q56).
- **Broke a low-level Linux config file, VM won't boot normally:** fix it through the **interactive serial console** connection. SSH, scp and RDP need a booted OS and network (Exam 2 · Q50).
- **Instance fails to launch (choose two):** check whether the **boot disk is full** and whether the **file system is corrupted**. Firewall, alternative SSH user and dropped traffic assume the OS booted (Exam 2 · Q43).
- **Copy a local directory to a VM:** `gcloud compute scp --recurse … instance:~/path --zone …`. `gsutil cp` targets Cloud Storage; there's no `gcloud compute mv` for this (Exam 2 · Q35).
- **Slow Cloud Storage reads, data for support:** `gsutil perfdiag -o output.json gs://bucket` (Exam 2 · Q13).
- **GKE upgrade/security bulletin awareness** for release-channel clusters: **cluster notifications to Pub/Sub** (Exam 4 · Q37).
- **`insufficient regional quota … resource "CPUS"`** when creating a 200-node GKE cluster: GKE nodes are Compute Engine VMs, so **increase the Compute Engine CPU quota** for that region (Quotas page in the console). There is no separate "GKE CPU quota" to raise, and a support case or redesigning services for fewer cores is the slow path (Exam 5 · Q27).

### Decision rules
- VM not booting or SSH dead → **serial port** (Exam 1 · Q52), (Exam 1 · Q56), (Exam 2 · Q50).
- Diagnose before you destroy: restart/recreate loses the evidence (Exam 1 · Q56).
- Read the resource name in a quota error: CPUS, IP addresses and disks are **Compute Engine** quotas even when GKE is the caller (Exam 5 · Q27).

### Traps
- `gsutil test` and `gcloud services test` don't exist as performance diagnostics (Exam 2 · Q13).
- RSS feeds, BigQuery release-notes queries or polling the GKE API for upgrade notices (Exam 4 · Q37).
- "Increase the GKE quota" for a CPU shortfall (Exam 5 · Q27).

---

## 12. Production monitoring, logging and alerting

### Key facts
- **Text log files on a VM → Cloud Logging, no code change:** install the logging agent (the bank's "Google-provided fluentd"/Stackdriver Logging Agent) and configure it to collect those files (Exam 2 · Q53), (Exam 3 · Q42). The first step after installing it is to **define the app log file as a custom source** (Exam 2 · Q5).
- **Memory usage of a VM** is not a default hypervisor metric; you need the **monitoring agent** (Exam 3 · Q52).
- **Alert on error rate > 15%** (Cloud Run 500s), on **service degradation**, or on **GKE memory outside 20–80%**: a **Cloud Monitoring alerting policy**. Scheduled Cloud Functions, Composer, console checks and `kubectl top` scripts are all rejected (Exam 3 · Q6), (Exam 3 · Q23), (Exam 4 · Q57).
- **Users can't reach the app behind the LB:** **uptime checks** (the bank's "Stackdriver availability checks") with alerting. LB/MIG health checks protect routing and autohealing; they don't notify you, and functional tests check behavior, not reachability (Exam 4 · Q10), (Exam 5 · Q29).
- **Unix process stopped for 5 minutes, monitoring agent installed, app can't be changed:** the bank gives **two different keys for the same stem**: **metric absence** (Exam 4 · Q23) and **process health** (Exam 5 · Q47). Process health is the condition built for this: it counts matching processes from the agent's process metrics and fires when the count drops to 0. Pick process health when it's offered; see ⚠️.
- **Read stdout logs from every replica of a Deployment across several GKE clusters:** **`gcloud logging read`** with a filter. GKE ships container stdout/stderr to Cloud Logging, which aggregates all clusters. `kubectl logs` is one cluster/Pod at a time; `journalctl` via `exec` or SSH reads node/system logs, not container stdout (Exam 5 · Q28).
- **Count requests to `/api/alpha/*` from logs:** a **logs-based counter metric** with a wildcard path filter. `/api/alpha/` alone misses sub-paths; exporting to GCS or Pub/Sub and counting lines is manual (Exam 4 · Q40).
- **Correlate Prometheus metrics with logs and alert in real time, cheaply:** bring Prometheus metrics into **Cloud Monitoring** and create **log-based metrics** there to correlate and alert. BigQuery/Bigtable exports add cost and latency (Exam 3 · Q55).
- **BigQuery query execution time:** Cloud Monitoring metrics, not Trace or slot usage (Exam 1 · Q53).
- **Legacy on-prem monitoring is slow for cloud apps:** use **Cloud Logging + Cloud Monitoring** for capture and alerting and **forward alerts to the existing platform**, rather than a big-bang replacement (Exam 3 · Q35).
- **Log retention of 1 and 3 years with easy search:** keep the logs in **Cloud Logging with custom retention**, rather than chained buckets (Exam 2 · Q45).

### Signal selector

| Question asks | Answer | Source |
|---|---|---|
| "Is it reachable from outside?" | Uptime check | (Exam 4 · Q10), (Exam 5 · Q29) |
| "Has this Unix process stopped running?" | Process-health condition (bank also keys metric absence) | (Exam 5 · Q47), (Exam 4 · Q23) |
| "Has metric X stopped reporting?" | Metric-absence condition | (Exam 4 · Q23) |
| "Logs from all replicas in all clusters" | `gcloud logging read` / Logs Explorer | (Exam 5 · Q28) |
| "Threshold on error rate / memory" | Metric-threshold alerting policy | (Exam 3 · Q6), (Exam 4 · Q57) |
| "Count log lines matching a pattern" | Logs-based counter metric | (Exam 4 · Q40) |
| "VM memory" | Monitoring agent | (Exam 3 · Q52) |
| "Log files from disk" | Logging agent + custom source | (Exam 2 · Q5), (Exam 3 · Q42) |

### Decision rules
- "Minimal development time" for alerts → **native Cloud Monitoring**, never a custom function (Exam 3 · Q23), (Exam 3 · Q6).
- "No code change" for logs → **agent**, not a client library (Exam 3 · Q42).
- "Across all clusters/replicas" → **Cloud Logging** (`gcloud logging read`), not per-cluster `kubectl` (Exam 5 · Q28).

### Traps
- Error Reporting is for exception analysis, not resource alerting (Exam 3 · Q23).
- collectd is for metrics; syslog alone doesn't ship to Cloud Logging (Exam 2 · Q53).
- Giving the VM "full access to all Cloud APIs" is never the first step (Exam 2 · Q5).
- "Write logs to /var/log and they'll be shipped automatically" (Exam 3 · Q42).
- `journalctl` (inside the Pod or over SSH to nodes) for container stdout (Exam 5 · Q28).
- Load-balancer health probes and MIG health evaluations for "alert me when users can't reach it" (Exam 5 · Q29).

---

## ⚠️ Questionable answers

| Item | Issue |
|---|---|
| **(Exam 3 · Q49)** | Keys "rolling update with a PodDisruptionBudget at 80%". A PDB limits **voluntary evictions** (node drains, upgrades); it does not govern a Deployment rollout, which is controlled by `maxSurge`/`maxUnavailable`. The explanation's claim that the PDB keeps 80% of Pods up during the update is wrong. Pick it among these options, but don't learn it as how rollouts are protected. |
| **(Exam 3 · Q46)** vs **(Exam 1 · Q41)**, **(Exam 3 · Q25)** | Keys Kubernetes Secret + KMS plugin for credentials that need **rotation**. The other two items (and Google's guidance) prefer **Secret Manager + Workload Identity**, which also handles versioning/rotation. Q46 only wins because Secret Manager isn't offered. |
| **(Exam 1 · Q19)** | Keys a **livenessProbe that fails when the DB is unreachable**. Liveness probes that check external dependencies are a known anti-pattern: a DB outage makes every Pod restart in a loop. A readiness probe is the usual tool for dependency checks. The explanation's line that "a PreStop hook doesn't automatically trigger if a liveness probe fails" is also inaccurate: kubelet runs preStop before killing a container for a failed liveness probe. |
| **(Exam 2 · Q44)** | Cloud Function on `clouddeploy-operations` to auto-promote. Cloud Deploy now has **built-in automation (promote-release rules)**, which is the simpler current answer if offered. |
| **(Exam 1 · Q14)** | Answers are fine, but the explanation says a shorter cooldown lets new VMs "handle traffic sooner". The cooldown/initialization period controls when the **autoscaler trusts the new VM's metrics**; it doesn't change when the VM serves traffic. |
| **(Exam 2 · Q27)** | Calls traffic **mirroring** "A/B testing". Mirroring is shadow testing (users never see the new version); A/B testing exposes users to variants (Exam 2 · Q32). Learn the cue "full production load before launch → mirroring". |
| **(Exam 2 · Q21)** | Dismisses Cloud Run's **continuous deployment from a repository with buildpacks**, which is a built-in, fully managed option (it creates a Cloud Build trigger for you) and arguably simpler. Expect either; the bank keys the explicit Cloud Build trigger. |
| **(Exam 3 · Q5)**, **(Exam 3 · Q39)**, **(Exam 4 · Q22)** | Serverless VPC Access connectors are still valid, but Cloud Run now also supports **Direct VPC egress** without a connector. Q5's claim that the Cloud SQL connector/Cloud Run Cloud SQL connection "won't solve" private IP overstates it; they can use private IP once a VPC path exists. |
| **Stackdriver / legacy agents**: (Exam 2 · Q5), (Exam 2 · Q53), (Exam 3 · Q42), (Exam 3 · Q52), (Exam 1 · Q53), (Exam 3 · Q23), (Exam 4 · Q10), (Exam 4 · Q23), (Exam 4 · Q40), (Exam 5 · Q29), (Exam 5 · Q47) | "Stackdriver" is now Cloud Logging/Monitoring, and the separate fluentd logging agent and collectd monitoring agent are replaced by the **Ops Agent**. The concepts hold; the product names are outdated. |
| **(Exam 3 · Q30)** | Uses **Container Registry**, which is deprecated in favor of **Artifact Registry**; vulnerability scanning now sits under **Artifact Analysis**. The attestation + Binary Authorization logic still holds. |
| **(Exam 2 · Q8)**, **(Exam 2 · Q21)**, **(Exam 3 · Q58)** | Built around **Cloud Source Repositories**, which is closed to new customers. The trigger logic (tag vs branch vs push) carries over to GitHub/GitLab-connected Cloud Build triggers. |
| **(Exam 4 · Q58)** | Resizing the PD first and then editing the PVC is backwards from the normal flow (edit the PVC and let the CSI driver grow the disk), and it only works when the StorageClass has `allowVolumeExpansion: true`. With a manually created PV, as in the stem, expansion may not apply at all. |
| **(Exam 3 · Q12)** | "Webmaster Central" is now **Search Console**. The CNAME to `ghs.googlehosted.com` remains the answer. |
| **(Exam 2 · Q4)** | The explanation says gsutil in the container means "embedding credentials"; with Workload Identity it doesn't. Also, the Kubernetes-native way to hold traffic until config is present is a **readiness probe**. Learn the key, not the reasoning. |
| **(Exam 2 · Q45)** | A Cloud Logging bucket has **one** retention value; you'd set 3 years (which also covers the 1-year need). The explanation implies setting two retention periods. |
| **(Exam 5 · Q47)** vs **(Exam 4 · Q23)** | Same stem (Unix process not running for 5 minutes, agent installed, app can't be changed), different keys: Q47 = **process health**, Q23 = **metric absence**. Q23's explanation says process health needs the app to emit custom metrics, which is wrong: the agent reports process metrics itself. Process health is the condition designed for this and the safer pick when offered; metric absence only fits when the choice is "a metric stopped arriving". |
| **(Exam 5 · Q5)** | The key (gsutil `cp -r` build step) is fine, but the explanation gets both flags wrong. `waitFor: ['-']` makes the step **start immediately at the beginning of the build, in parallel**; it does not make later steps wait. To run the copy before promotion, the promote step should `waitFor` the copy step's `id`. In `gsutil cp`, `-a` sets a **canned ACL**, not "archive mode", so D is wrong because it's missing `-r`, not because `-a` is merely less direct. `gsutil` is also superseded by `gcloud storage`. |
| **(Exam 5 · Q45)** | The explanation says App Engine standard has "two scaling types: basic and automatic". There are three (**automatic, basic, manual**), and automatic scaling also supports `max_instances`. The key (basic scaling, `max_instances: 5`) is still the only option that caps instances. |
| **(Exam 5 · Q32)** | The key (Git + Cloud Build + Terraform + Cloud Functions) is right because of **IaC**. The explanation's claims that App Engine is "less serverless" than Cloud Functions and that Cloud Functions is "the ideal" serverless target are wrong: Cloud Run and App Engine are serverless too. Don't learn "serverless means Cloud Functions". |
| **(Exam 5 · Q8)** | The explanation says public-endpoint clusters restrict access to authorized IPs "by default". **Authorized networks are opt-in** on a public cluster; the key assumes they were enabled. GKE now also offers a DNS-based control plane endpoint, which avoids IP allowlisting for Cloud Shell. |

---

## Last-minute cheat sheet

- Stateless container + least ops → **Cloud Run**; static site → **Cloud Storage** (Exam 6 · Q12), (Exam 3 · Q34).
- App Engine custom domain → **verify + CNAME `ghs.googlehosted.com`** (Exam 3 · Q12).
- Deployment = replicas; **StatefulSet** = stable identity + own disk; **DaemonSet** = one per node (Exam 2 · Q1), (Exam 2 · Q10).
- In-cluster calls → **Service DNS name**; internal only → **ClusterIP**; new domain on same IP → **host rule on existing Ingress** (Exam 1 · Q23), (Exam 3 · Q14), (Exam 2 · Q18).
- Graceful shutdown → **handle SIGTERM**; preemptible VM → **shutdown script sends a signal** (Exam 2 · Q59), (Exam 3 · Q40).
- LB traffic gate → **readinessProbe**; slow start kills it → **startupProbe**; `CrashLoopBackOff` → **`kubectl logs --previous`** (Exam 5 · Q20), (Exam 5 · Q49), (Exam 5 · Q36).
- Golden image + per-env config → **instance metadata read from the metadata server** (Exam 3 · Q26), (Exam 3 · Q36).
- Shared writable file for many Pods → **Filestore NFS PV**; grow a volume → **edit the PVC** (Exam 4 · Q25), (Exam 4 · Q58).
- Secrets → **Secret Manager + Workload Identity**, never exported SA keys (Exam 1 · Q41), (Exam 3 · Q25).
- Limit users hit by a bad release → **canary**; swift full rollback → **blue/green** (Exam 1 · Q37), (Exam 1 · Q46).
- Full production load before launch → **traffic mirroring**; sales impact → **A/B split + statistics** (Exam 2 · Q27), (Exam 2 · Q32).
- Cloud Run gradual → **no-traffic revision, then percentage split** (Exam 6 · Q2), (Exam 4 · Q30).
- Route by OS/user-agent → **GKE + Anthos Service Mesh** (Exam 3 · Q3), (Exam 2 · Q57).
- Named tester group → **feature flag**; random A/B → **weighted split** (Exam 5 · Q58), (Exam 5 · Q25).
- Keep old Pods until new is healthy → **`maxSurge: 1`, `maxUnavailable: 0`**; MIG at no extra cost → **`maxSurge: 0`, `maxUnavailable: 1`** (Exam 5 · Q57), (Exam 5 · Q10).
- Urgent autoscaling → **HPA on CPU**; Pub/Sub backlog → **HPA external metric**; nodes too → **+ Cluster Autoscaler** (Exam 1 · Q39), (Exam 1 · Q12), (Exam 4 · Q29).
- MIG latency during scale-out → **lower CPU target + shorter cooldown** (Exam 1 · Q14).
- Release specific commits → **Git tag trigger**; deploy fails after validation → **Cloud Build SA role** (Exam 2 · Q8), (Exam 1 · Q42).
- Isolated test env → **Cloud Build runs Terraform to create a new project** (Exam 4 · Q49).
- Same image in every environment → reference it by **digest** (Exam 5 · Q18).
- Only trusted images → **Cloud Build + Artifact Registry + Binary Authorization**; attestation step after tests; KMS key; rule in **prod** policy (Exam 2 · Q15), (Exam 6 · Q14), (Exam 4 · Q18).
- No exfiltration from the pipeline → **private worker pool + VPC Service Controls** (+ Binary Authorization, also on Cloud Run) (Exam 5 · Q33), (Exam 5 · Q38).
- Cloud Run → private Cloud SQL/Memorystore → **Serverless VPC Access connector in the same region** (Exam 3 · Q39), (Exam 4 · Q22).
- Istio, only some URLs fail → **AuthorizationPolicy** (Exam 1 · Q4).
- VM won't boot / SSH dead → **serial port** (Exam 1 · Q56), (Exam 2 · Q50).
- Alerts → **Cloud Monitoring alerting policy**; reachability → **uptime check**; process gone → **process health** (bank also keys metric absence, see ⚠️) (Exam 3 · Q6), (Exam 4 · Q10), (Exam 5 · Q47), (Exam 4 · Q23).
- Count matching log entries → **logs-based counter metric** with wildcard path (Exam 4 · Q40).
- Logs from files without code change → **logging agent**; VM memory → **monitoring agent** (Exam 3 · Q42), (Exam 3 · Q52).
