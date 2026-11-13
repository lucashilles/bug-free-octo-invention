# Domain 1 Study Guide — Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications

> Condensed from the 63-question bank in [`01-designing-cloud-native-apps.md`](01-designing-cloud-native-apps.md). Citations look like (Exam N · QM). Several scenarios repeat across exams, so look for the paired citations.

---

## 1. Choosing a compute platform

### Key facts
- **Cloud Run** is the default answer for a stateless HTTP/gRPC service with unpredictable or bursty traffic. It scales up fast, **scales to zero**, and you pay only while requests are served (Exam 1 · Q29), (Exam 1 · Q60).
- **Cloud Run is built on Knative.** Migrating a container from on-prem Knative, keeping the same deployment strategy, on a fully managed service → Cloud Run (Exam 1 · Q11), (Exam 4 · Q4).
- Cloud Run handles **long-lived, persistent gRPC connections** with surges around specific dates (an IVR backend with 1–30 minute calls) at the lowest cost and effort (Exam 3 · Q44).
- Cloud Run supports **gRPC** natively. A gRPC API that publishes to an async message service → Cloud Run + **Pub/Sub**, not GKE/Compute Engine + self-managed Kafka (Exam 6 · Q5).
- Modernizing a Python 3 web API that needs autoscaling, frequent deployments, low cost and low ops → Cloud Run, not App Engine flexible, a single VM, or a GKE rewrite (Exam 4 · Q54).
- A containerized Python service with daytime traffic and **no traffic at night** → Cloud Run, logging errors to **standard error** so **Error Reporting** picks them up automatically (Exam 6 · Q16).
- **App Engine flexible** keeps a minimum number of instances running, so it costs money while idle (Exam 1 · Q29).
- **GKE** (Standard or Autopilot) and **Compute Engine MIGs** scale, but they add cluster/VM management and cost more for spiky traffic than Cloud Run (Exam 1 · Q60), (Exam 6 · Q16).

### Comparison

| Platform | Scales to zero | Ops overhead | Picked when | Source |
|---|---|---|---|---|
| Cloud Run | Yes | Lowest | Stateless containers, spiky traffic, gRPC, Knative migration | (Exam 1 · Q29), (Exam 4 · Q4), (Exam 6 · Q5) |
| Cloud Functions | Yes | Low | One function per endpoint, put behind an HTTPS LB | (Exam 2 · Q23) |
| App Engine flexible | No (min instances) | Medium | Rarely the best answer in this bank | (Exam 1 · Q29), (Exam 4 · Q54) |
| GKE Autopilot / Standard | No | Medium–high | You need Kubernetes features | (Exam 1 · Q60), (Exam 6 · Q16) |
| Compute Engine / MIG | No | Highest | Legacy VM workloads | (Exam 1 · Q60), (Exam 4 · Q54) |

### Decision rules
- "Unpredictable traffic" + "minimize cost" + "stateless" → **Cloud Run + Firestore** (Exam 1 · Q29), (Exam 1 · Q60).
- "Knative" anywhere in the stem → **Cloud Run** (Exam 1 · Q11), (Exam 4 · Q4).
- An API with several URL paths, each mapped to a different function → **one Cloud Function per path**, each a separate backend service behind an **HTTPS load balancer** with path routing (Exam 2 · Q23).
- Hybrid (cloud + on-prem) microservices with an emphasis on managed services and scalability → **GKE clusters in each environment via Anthos + Cloud Run for Anthos** (Exam 3 · Q17). See the questionable-answers note on product naming.
- Errors must show up in Error Reporting with minimal setup → write them to **stderr**, not to a Cloud Storage bucket (Exam 6 · Q16).

### Traps
- "Deploy on Compute Engine and enable autoscaling" does not fix a monolith's architecture (Exam 1 · Q16).
- GKE Autopilot sounds "managed", but Cloud Run is still cheaper and simpler for intermittent stateless traffic (Exam 1 · Q60), (Exam 6 · Q16).
- Self-managed Kafka on GKE or VMs loses to Pub/Sub whenever the stem says "minimize infrastructure management" (Exam 6 · Q5).

---

## 2. Choosing a database

### Key facts
- **Cloud SQL**: managed MySQL/PostgreSQL. Handles backups, replication and updates. Right for an existing relational schema with heavy reads/writes when the team can't run a database full time (Exam 2 · Q14).
- **Spanner**: globally distributed, strongly consistent relational database. Pick it for **global consistency + high availability** (for example, point trading in a multiplayer game migrating from MySQL) (Exam 4 · Q59), and for a SQL schema that must scale with global growth (Exam 2 · Q29).
- **Firestore**: managed document database with a **flexible schema**. Right when a rigid MySQL schema is hard to evolve for user-specific state (Exam 2 · Q40).
- **Firestore in Native mode** gives mobile/web clients **offline persistence**, **real-time listeners**, ACID transactions, semi-structured data, multi-zone replication and direct client access with an optional middle tier (Exam 1 · Q17), (Exam 4 · Q31), (Exam 4 · Q34).
- Firestore Native also meets "immediate access after submission + sort by multiple fields + diverse record formats" for purchase history (Exam 3 · Q15).
- **Bigtable**: wide-column NoSQL for high-throughput workloads. No offline client libraries and no fit for relational schemas (Exam 2 · Q14), (Exam 4 · Q31), (Exam 4 · Q34).
- **BigQuery**: analytics warehouse. Not for transactional, low-latency app data (Exam 4 · Q34), (Exam 4 · Q59).

### Comparison

| Need in the stem | Pick | Not | Source |
|---|---|---|---|
| Existing MySQL schema, minimal DBA effort | Cloud SQL | Spanner (overkill), Marketplace MySQL (self-managed) | (Exam 2 · Q14) |
| Global strong consistency, 99.999% | Spanner | Cloud SQL (regional), Bigtable | (Exam 4 · Q59), (Exam 2 · Q36) |
| Schema evolves per user, flexible fields | Firestore / Datastore | Cloud SQL, Spanner | (Exam 2 · Q40) |
| Mobile offline sync + real-time updates | Firestore Native | Cloud SQL, Bigtable, SQLite + Cloud Storage sync | (Exam 4 · Q31), (Exam 1 · Q17) |
| ACID + semi-structured + offline client libs | Firestore | Bigtable, Cloud SQL, BigQuery | (Exam 4 · Q34) |
| Analytics over PBs | BigQuery | Firestore | (Exam 2 · Q19) |

### Decision rules
- "Offline", "sync across devices", "real-time updates" → **Firestore (Native mode)** (Exam 4 · Q31).
- "Hierarchical data for a mobile app" + least privilege → **Firestore Native + `roles/datastore.user`**. `datastore.viewer` is read-only; `cloudsql.editor` is too broad (Exam 1 · Q17).
- "Global", "consistency", "multi-region" + relational → **Spanner** (Exam 4 · Q59).
- "Team can handle minor admin only" + MySQL → **Cloud SQL** (Exam 2 · Q14).
- "Diverse record formats" → a document database, not Cloud SQL (Exam 3 · Q15).

### Traps
- Firestore in **Datastore mode** is not the answer when offline sync or real-time client features are required (Exam 1 · Q17), (Exam 3 · Q15).
- Spanner is "overkill" for a standard MySQL workload with no global requirement (Exam 2 · Q14).
- A self-managed SQLite + Cloud Storage sync job means writing your own sync logic (Exam 4 · Q31).
- A migration path of "Cloud SQL, then import into Firestore Native" is keyed in one vague item; treat it as weak (Exam 4 · Q42). See questionable answers.

---

## 3. Schema and key design for scale

### Key facts
- **Spanner hotspots**: monotonically increasing primary keys (such as **version 1 UUIDs**, which are timestamp-based) concentrate inserts on one split and make scaling non-linear (Exam 1 · Q35).
- Spanner transaction tables should use **random UUIDs** for the key, not incremental numbers (Exam 2 · Q29).
- To search customers by phone number in Spanner: a **`Phones` child table interleaved in `Customers`**, plus an **index on the phone number** column (Exam 2 · Q30).
- **Bigtable row keys**: concatenating several human-readable attributes (e.g. `<region>_<customerID>_<orderID>`) spreads load and keeps keys readable (Exam 4 · Q19).
- **Firestore**: an unbounded number of child items (comments, posts) belongs in a **subcollection** under the parent document, not in an array field (Exam 2 · Q33), (Exam 4 · Q45).
- Firestore documents have a **1 MB size limit**, so nesting every post inside a profile document doesn't scale (Exam 4 · Q45).

### Hotspot table

| Database | Bad key | Good key | Source |
|---|---|---|---|
| Spanner | UUIDv1, auto-increment | Random UUID (v4) | (Exam 1 · Q35), (Exam 2 · Q29) |
| Bigtable | Sequential integers, epoch timestamps | Concatenated readable attributes | (Exam 4 · Q19) |
| Bigtable | MD5 hash of content | Evenly spread but not human-readable | (Exam 4 · Q19) |

### Decision rules
- Spanner load test scales non-linearly → look for a **monotonically increasing key** first (Exam 1 · Q35).
- "Human-readable" + "even distribution" in Bigtable → **concatenated attributes**, not a hash (Exam 4 · Q19).
- Firestore one-to-many with unbounded children → **root collection for the parent + subcollection for children**: articles → comments (Exam 2 · Q33), users → posts (Exam 4 · Q45).
- Spanner one-to-many that you need to search by the child value → **interleaved child table + secondary index on the child column** (Exam 2 · Q30).

### Traps
- LIKE vs STARTS_WITH, 64-bit vs 32-bit ints, STRING for numerics: none of these explain non-linear Spanner scaling (Exam 1 · Q35).
- Storing comment IDs in an array on the article still needs extra reads and grows unbounded (Exam 2 · Q33).
- "Cloud SQL with UUIDs" fixes uniqueness but not global scale (Exam 2 · Q29).

---

## 4. High availability and resilient architecture

### Key facts
- **GKE regional clusters** replicate the control plane and nodes across zones in a region. They survive a zone failure. **Multi-zonal** clusters spread nodes but keep a **single-zone control plane**, so a zone outage can still take down the GKE API (Exam 2 · Q60).
- **Spanner 99.999% + low global read latency** → a multi-region instance config spanning continents (**`nam-asia-eur1`**) with **at least 3 nodes**, not separate regional instances or Dataflow replication (Exam 2 · Q36).
- **Bigtable app profile with multi-cluster routing** gives automatic failover across clusters. Single-cluster routing with manual failover is the problem to fix (Exam 6 · Q11).
- **Containers on GKE**: one component per container (Apache, PHP, MySQL separate) with **readiness and liveness probes**, so Kubernetes can restart unhealthy containers. Avoid one container running everything under a process manager or bash script (Exam 3 · Q1).
- **Spanner** is the database for global consistency and high availability (Exam 4 · Q59).

### Decision rules
- "Zone failure took down the GKE API" → **regional cluster** (Exam 2 · Q60).
- "Bigtable, more efficient and highly available connectivity" → **multi-cluster routing**, not a cache or a bigger connection pool (Exam 6 · Q11).
- "Worldwide users, five nines" → **multi-continent Spanner config** (Exam 2 · Q36).
- "Best practice for availability when containerizing a LAMP stack" → **separate containers + probes** (Exam 3 · Q1).

### Traps
- Multi-zone ≠ regional for GKE: the control plane is the single point of failure (Exam 2 · Q60).
- A Memcached layer in front of Bigtable improves read latency, not failover (Exam 6 · Q11).
- Two independent Spanner instances in separate regions do not give you the single, consistent, five-nines database a multi-region config gives (Exam 2 · Q36).
- Coordinating container startup with a script is fragile; use Kubernetes' built-in health mechanisms (Exam 3 · Q1).

---

## 5. Storage classes, lifecycle, retention and data governance

### Key facts
- **Object Lifecycle Management** moves objects to colder classes declaratively (e.g. Standard → Coldline after 14 days, Standard → Archive after 3 years). It beats a scheduled job or a Cloud Function + Cloud Scheduler doing the same thing (Exam 1 · Q2), (Exam 1 · Q8), (Exam 1 · Q54).
- **Retention policy / Bucket Lock** guarantees objects can't be deleted or modified before the retention period ends. This is how you meet "keep for 7 years" (Exam 1 · Q8), (Exam 1 · Q54), (Exam 1 · Q2).
- Logs reviewed for two weeks then only annually → **Coldline** after 14 days. Nearline costs more than Coldline for this infrequently accessed data (Exam 1 · Q2), (Exam 2 · Q31).
- **Object Versioning** guards against accidental overwrite/delete but does not enforce retention and adds cost. **IAM Conditions** control access, not retention (Exam 1 · Q8), (Exam 1 · Q54).
- **Large read-only dataset shared by a MIG**, fast startup, filesystem access, low cost → **one persistent disk attached read-only to many VMs**. Cloud Storage FUSE adds latency; copying at startup slows boot; per-VM disks from a snapshot cost more (Exam 2 · Q52).
- **Images served fast and cheaply** → **Cloud CDN with a Cloud Storage backend** (Exam 3 · Q33).
- **BigQuery compliance**: EU data residency → a **dataset created in an EU region**; right to delete → **DML `DELETE`/`UPDATE`** statements (Exam 2 · Q19).
- **BigQuery row-level separation by department** → views filtering by department, granted per group, without copying data (Exam 3 · Q20). See questionable answers for where the views should live.

### Comparison: compliance vs cost features

| Feature | Solves | Doesn't solve | Source |
|---|---|---|---|
| Retention policy / Bucket Lock | "Must keep N years", can't delete | Cost | (Exam 1 · Q8), (Exam 1 · Q54) |
| Lifecycle rule (SetStorageClass) | Cost of aging data | Retention guarantee | (Exam 1 · Q2), (Exam 1 · Q54) |
| Object Versioning | Accidental overwrite | Retention, cost | (Exam 1 · Q8) |
| IAM Conditions | Who can read | Retention | (Exam 1 · Q54) |
| JWT for users | Nothing storage-related | — | (Exam 1 · Q2), (Exam 2 · Q31) |

### Decision rules
- "Accessible for at least 7 years" + "rarely accessed after 3 years" → **retention policy 7 years + lifecycle to Archive at 3 years** (Exam 1 · Q8), (Exam 1 · Q54).
- "Review 2 weeks, then auditor yearly" → **lifecycle to Coldline at 14 days + Bucket Lock retention** (Exam 1 · Q2).
- "Choose two" with both a lifecycle rule and a script doing the same transition → prefer the **native lifecycle rule** (Exam 1 · Q54).
- Shared read-only data for many VMs → **read-only multi-attach PD** (Exam 2 · Q52).
- Residency in BigQuery → **regional dataset**; deletion on request → **DML** (Exam 2 · Q19).

### Traps
- A Cloud Function + Cloud Scheduler that moves old objects to another bucket is custom code that native lifecycle already provides (Exam 1 · Q8), (Exam 1 · Q54).
- An EU Cloud Storage bucket or federated queries don't satisfy BigQuery residency or deletion by themselves; a Dataflow re-upload is unnecessary complexity (Exam 2 · Q19).
- Copying data into per-department datasets with pipelines duplicates data and needs syncing (Exam 3 · Q20).
- App Engine or a VM with Persistent Disk serving images loses to CDN + Cloud Storage (Exam 3 · Q33).

---

## 6. Microservices migration and API design

### Key facts
- **Monolith → microservices** should be incremental: replace functionality **gradually over several phases** (Strangler Fig). Big-bang refactors and parallel rewrites are high risk (Exam 1 · Q16).
- **Pick the first service to migrate** by low risk and few dependencies: the **product catalog** (frontend + product DB), not payments, order fulfillment or the shopping cart (Exam 1 · Q10).
- Priorities when designing composable microservices: an **API contract** between caller and implementation, and a **versioning scheme** for future incompatible changes (Exam 2 · Q22).
- Expose versioned REST microservices on GKE through an **Ingress** that routes by URL (e.g. `/api/v1/`, `/api/v2/`), so consumers and third parties aren't disrupted by new releases (Exam 3 · Q54).
- **gRPC** for mobile APIs: HTTP/2, HTTPS, compact Protocol Buffers payloads (less bandwidth than JSON or SOAP XML), and generated client code for Android/iOS (Exam 2 · Q12), (Exam 2 · Q34).
- **Header-based routing** across service implementations on VMs/instance groups in several regions → **Traffic Director** (Exam 2 · Q25).
- **Async decoupling**: publish to a **Pub/Sub topic** so multiple services can consume (Exam 6 · Q5).
- **SPA calling a slow third-party API**: make the request **asynchronous** so it doesn't block rendering, and **hide the widget** on timeout or error (Exam 1 · Q21).

### Decision rules
- "Minimize risk during migration" → move the **least coupled, least critical** feature first (Exam 1 · Q10).
- "Minimize business impact" → **phased replacement** (Exam 1 · Q16).
- "Choose two design aspects" for microservices → **contract + versioning**, not "same language", "always async" or "enough instances" (Exam 2 · Q22).
- "HTTPS + minimal bandwidth + mobile" → **gRPC** (Exam 2 · Q12), (Exam 2 · Q34).
- "Don't break API consumers on new releases" on GKE → **Ingress with URL-based versioned routing** (Exam 3 · Q54).
- "Route by HTTP header" across regions, loosely coupled → **Traffic Director** (Exam 2 · Q25).
- "Third-party data is less important; don't let it block rendering" → **async + hide the widget** (Exam 1 · Q21).

### Traps
- MQTT is pub/sub for IoT, not a request/response mobile API; SOAP is verbose XML (Exam 2 · Q12), (Exam 2 · Q34).
- Retrying with backoff "until success" in a UI widget adds load and keeps the user waiting (Exam 1 · Q21).
- Putting the API version in the POST body, or using multiple clusters with DNS per version, is worse than URL-routed Ingress (Exam 3 · Q54).
- Service Directory does discovery, not content-based routing (Exam 2 · Q25).
- One Cloud Function handling all paths, or directly exposed functions without a load balancer, is not the keyed design (Exam 2 · Q23).

---

## 7. Service identity, IAM and least privilege

### Key facts
- Every workload gets a **dedicated user-managed service account** with only the permissions it needs. Don't use the Compute Engine or App Engine **default service accounts** (Exam 3 · Q2), (Exam 3 · Q22), (Exam 4 · Q12).
- Cloud Function calling other services → a new service account with a **custom role**, and grant the deployer **permission to act as** that SA, not permission to obtain its access token (Exam 1 · Q25).
- Cloud Run reading/writing one bucket → user-managed SA with a **custom role** (e.g. only `storage.objects.get`/`create`), not Storage Admin or Project Editor (Exam 3 · Q2).
- Cloud Run reading images from a **private** bucket → enable **public access prevention**, run the service as a user-managed SA, grant **Storage Object Viewer**. Signed URLs are for temporary access, not routine service access (Exam 3 · Q22).
- **Cross-project**: function in Project A writing to a bucket in Project B → create the SA **in Project A**, grant it **`roles/storage.objectCreator` on the bucket in Project B** (Exam 4 · Q12).
- **Cloud SQL**: an app connecting from Compute Engine or through the **Cloud SQL Auth Proxy on GKE** needs the **Cloud SQL Client** role, not Cloud SQL Editor, Project Editor or Owner (Exam 2 · Q38), (Exam 4 · Q36).
- **Firestore from a mobile backend** → `roles/datastore.user` (Exam 1 · Q17).
- **Developer access per team** → put users in **groups**, grant roles to groups, and give them the **Project ID** (Exam 3 · Q10).
- **Workforce Identity Federation** lets employees from an external IdP sign in to the Google Cloud console, with **attribute mapping** for name/photo. **Workload** Identity Federation is for workloads, not people (Exam 6 · Q4).

### Role picker

| Scenario | Role | Reject | Source |
|---|---|---|---|
| App → Cloud SQL (VM or Auth Proxy on GKE) | `roles/cloudsql.client` | Editor, Owner, `cloudsql.editor` | (Exam 2 · Q38), (Exam 4 · Q36) |
| Function writes into another project's bucket | `roles/storage.objectCreator` on that bucket | Default App Engine SA | (Exam 4 · Q12) |
| Read images from private bucket | Storage Object Viewer | Default Compute SA, signed URLs | (Exam 3 · Q22) |
| Read + write a bucket | Custom role | Storage Admin, Project Editor | (Exam 3 · Q2) |
| Firestore read/write | `roles/datastore.user` | `datastore.viewer` (read-only) | (Exam 1 · Q17) |

### Decision rules
- "Least privilege" + broad predefined role in the options → pick the narrowest role or a **custom role** (Exam 1 · Q25), (Exam 3 · Q2).
- "Deployer" in the stem → grant **act-as** on the runtime SA (Exam 1 · Q25).
- "External IdP" + "console access for employees" → **Workforce** Identity Federation (Exam 6 · Q4).
- Many developers across projects → **groups**, never per-user bindings (Exam 3 · Q10).
- A Windows VM using the Cloud SQL Auth Proxy: the keyed answer is a custom role with `cloudsql.instances.connect` plus the instance connection name in the proxy command, and `--unix-socket` is wrong on Windows (Exam 6 · Q6). See questionable answers.

### Traps
- Basic roles (Owner, Editor) are always wrong in least-privilege questions (Exam 1 · Q25), (Exam 2 · Q38), (Exam 4 · Q36).
- `roles/cloudsql.viewer` doesn't let the proxy connect (Exam 6 · Q6).
- One service account per employee, impersonated by each user, is not identity federation (Exam 6 · Q4).
- A service account created in the *bucket's* project and used from another project's function is the distractor (Exam 4 · Q12).

---

## 8. Network security, exposure and connectivity

### Key facts
- **Public, unauthenticated, but encrypted** access to a dashboard on Compute Engine → **external HTTP(S) load balancer + Google-managed SSL certificate** (auto-renewing). IAP would force authentication (Exam 1 · Q36), (Exam 4 · Q15).
- **Employees-only internal app** reachable from anywhere with Google Workspace accounts → **HTTP(S) load balancer + Identity-Aware Proxy**, allowing the company domain. No VPN, no IP allowlists, no obscure URLs (Exam 2 · Q55).
- **SSH for maintenance** without public IPs → **IAP TCP forwarding for SSH**, web servers on **private IPs behind an HTTP(S) load balancer**. Better than a bastion host or public IPs (Exam 3 · Q53).
- **Encrypt pod-to-pod traffic in GKE** with minimal app changes → a **service mesh (Istio) with sidecar injection and mutual TLS**. Network Policies restrict traffic but don't encrypt it (Exam 2 · Q41).
- **Lowest TTFB** for thousands of devices calling a single-region REST backend on Premium Tier → **MIG behind an external Application Load Balancer**, not DNS round-robin or a passthrough Network Load Balancer (Exam 6 · Q8).
- **App in one project, AlloyDB in another, keep projects isolated** → keyed answer is a **Shared VPC** with both as service projects (Exam 6 · Q15).

### Comparison: who can reach the app

| Requirement | Front end | Source |
|---|---|---|
| Anyone, no login, encrypted | HTTPS LB + Google-managed cert | (Exam 1 · Q36), (Exam 4 · Q15) |
| Only company Workspace users, anywhere | HTTPS LB + IAP | (Exam 2 · Q55) |
| Admin SSH, no public IPs | IAP for TCP/SSH | (Exam 3 · Q53) |
| Service-to-service encryption in GKE | Istio mTLS | (Exam 2 · Q41) |

### Decision rules
- "Without authentication" → **not IAP**; use TLS on the load balancer (Exam 1 · Q36).
- "Company employees", "Google Workspace", "from anywhere" → **IAP** (Exam 2 · Q55).
- "Encrypt traffic, minimize app changes, Google-supported" → **mesh + mTLS** (Exam 2 · Q41).
- "Minimize latency / TTFB" for HTTP clients → **global external Application LB** (Exam 6 · Q8).

### Traps
- A service account key can't encrypt web traffic (Exam 1 · Q36), (Exam 4 · Q15).
- Exporting reports hourly to a public bucket breaks "real-time" (Exam 1 · Q36), (Exam 4 · Q15).
- Let's Encrypt certificates baked into every app = lots of app changes (Exam 2 · Q41).
- Weighted or plain round-robin Cloud DNS gives no proximity optimization (Exam 6 · Q8).
- A service account JSON key passed as `--credentials-file` doesn't solve network connectivity and adds key-management risk (Exam 6 · Q15).

---

## 9. Caching, sessions and backend performance

### Key facts
- **Sessions** → **Memorystore** (Redis or Memcached), which supports expiry for idle-timeout logouts. **Shopping carts** that must survive logout → **Firestore** (Exam 1 · Q5), (Exam 3 · Q59).
- Session data in local memory with cookie-based affinity on the LB is not the recommended pattern (Exam 1 · Q5).
- **Overloaded Cloud SQL behind an API** → expose the API through **Apigee**, cache hot data in **Memorystore for Redis**, and retry failures with **exponential backoff** (Exam 6 · Q1).
- **Cloud CDN** caches static content such as images in front of Cloud Storage. It is not the tool for dynamic, database-backed API responses (Exam 3 · Q33), (Exam 6 · Q1).
- Don't let a slow non-critical dependency block the UI: async call + graceful hiding (Exam 1 · Q21).

### Decision rules
- "Session" + "expire after N minutes" → **Memorystore**; "persist cart across logins" → **Firestore** (Exam 3 · Q59).
- "Database overwhelmed by repeat reads" → **in-memory cache (Redis)** in front of it (Exam 6 · Q1).
- "Static images, fast, cheap" → **CDN + Cloud Storage** (Exam 3 · Q33).

### Traps
- Pub/Sub is not a session store; Cloud Storage files keyed by session ID are not a cart database; BigQuery is not for session data (Exam 3 · Q59), (Exam 1 · Q5).
- Queuing synchronous API calls through Pub/Sub doesn't reduce request latency (Exam 6 · Q1).
- Just adding memory to Cloud SQL plus a home-grown rate limiter is the distractor (Exam 6 · Q1).

---

## ⚠️ Questionable answers

| Item | Issue |
|---|---|
| **(Exam 2 · Q31)** | Keys **II + IV** (scheduled job *and* lifecycle rule, which do the same thing) and rejects Bucket Lock as "expensive". Bucket Lock has no extra charge, and the stem requires 7-year retention. The same scenario in (Exam 1 · Q2) keys **Bucket Lock + Coldline lifecycle**. **Prefer I + IV.** |
| **(Exam 3 · Q20)** | Keys "views inside the Master dataset". Google's **authorized view** pattern puts the views in a **separate dataset** that users can access, then authorizes those views on the source dataset (option I). Granting dataset-level access inside "Master" risks exposing the base tables. |
| **(Exam 6 · Q6)** | Keys a custom role with only `cloudsql.instances.connect`. Google's documentation recommends **`roles/cloudsql.client`** for the Auth Proxy (as in (Exam 2 · Q38) and (Exam 4 · Q36)), and the proxy also needs `cloudsql.instances.get`. The real eliminator for option B is that `--unix-socket` doesn't apply on Windows. |
| **(Exam 1 · Q29)** | The answer (Cloud Run) is right, but the explanation says App Engine **standard** doesn't scale to zero. It does; only flexible keeps minimum instances. |
| **(Exam 2 · Q36)** | The key is fine, but the explanation calls `nam3` a "regional" config. `nam3` is a **multi-region** config limited to North America. "3 nodes so one can fail" also misdescribes Spanner: replication comes from the instance configuration, not the node count. |
| **(Exam 2 · Q25)** | Traffic Director is now part of **Cloud Service Mesh**. The claim that internal HTTP(S) load balancing can't route on headers is wrong; internal Application LBs support header-based routing. |
| **(Exam 2 · Q41)** | The "Istio on GKE" add-on the references point to is deprecated. Today the Google-supported route is **Cloud Service Mesh** (managed Istio). The mTLS-via-sidecar idea still holds. |
| **(Exam 3 · Q17)** | "Anthos" is now **GKE Enterprise**, and "Cloud Run for Anthos" became **Knative serving**, which is no longer offered as a managed add-on. Learn the key, but expect newer wording. |
| **(Exam 4 · Q42)** | The stem has no scenario (no current database, no workload) and the key ("migrate to Cloud SQL, then import into Firestore Native") isn't justified. Don't build rules from it. |
| **(Exam 3 · Q53)** | The key is fine, but the explanation says one HTTP(S) LB "handles both web traffic and SSH". IAP TCP forwarding for SSH is separate from the load balancer. |
| **(Exam 6 · Q8)** | The key (external Application LB) is fine, but the reasoning is off. The backend is in one region, so the gain comes from terminating connections at Google's edge on Premium Tier, not from "routing to the closest backend". |
| **(Exam 6 · Q15)** | Shared VPC is keyed, but it puts both projects on one network, which weakens the "keep projects isolated" requirement. Private Service Connect is the newer cross-project option for AlloyDB. Answer the key if PSC isn't offered. |
| **(Exam 3 · Q15)** | Firestore Native is right (real-time). The claim that Datastore mode is "less performant" is not the real difference: Datastore mode lacks the real-time and offline client features. |
| **(Exam 2 · Q12)** | "REST uses HTTP/1.1" is an overgeneralization. The bandwidth argument for gRPC rests on Protobuf, not on REST being limited to HTTP/1.1. |

---

## Last-minute cheat sheet

- Spiky or unpredictable stateless traffic + low cost → **Cloud Run + Firestore** (Exam 1 · Q29), (Exam 1 · Q60).
- "Knative" → **Cloud Run** (Exam 1 · Q11), (Exam 4 · Q4).
- gRPC API + async fan-out → **Cloud Run + Pub/Sub** (Exam 6 · Q5).
- Errors into Error Reporting → log to **stderr** (Exam 6 · Q16).
- Existing MySQL, little DBA capacity → **Cloud SQL**. Global consistency + five nines → **Spanner** (Exam 2 · Q14), (Exam 4 · Q59).
- Offline + real-time mobile sync → **Firestore Native** with `roles/datastore.user` (Exam 4 · Q31), (Exam 1 · Q17).
- Spanner keys: **random UUIDs**, never UUIDv1 or sequences (Exam 1 · Q35), (Exam 2 · Q29).
- Spanner search on child values → **interleaved child table + index** (Exam 2 · Q30).
- Bigtable readable + even keys → **concatenated attributes** (Exam 4 · Q19).
- Firestore unbounded children → **subcollection** (Exam 2 · Q33), (Exam 4 · Q45).
- Zone-proof GKE → **regional cluster** (Exam 2 · Q60). Bigtable HA → **multi-cluster routing** (Exam 6 · Q11).
- Keep N years → **retention policy / Bucket Lock**. Cut cost → **lifecycle rule** (Exam 1 · Q54), (Exam 1 · Q2).
- BigQuery residency → **regional dataset**; right to erasure → **DML** (Exam 2 · Q19).
- Shared read-only data for a MIG → **read-only multi-attach PD** (Exam 2 · Q52).
- Monolith migration → **phased (Strangler Fig)**, start with the **product catalog** (Exam 1 · Q16), (Exam 1 · Q10).
- Microservice design → **API contract + versioning**; expose versions via **Ingress URL routing** (Exam 2 · Q22), (Exam 3 · Q54).
- Mobile API, low bandwidth → **gRPC** (Exam 2 · Q12).
- Header-based routing across regions → **Traffic Director** (Exam 2 · Q25).
- Dedicated **user-managed SA**, narrowest role; deployer gets **act-as** (Exam 1 · Q25), (Exam 3 · Q2).
- Cross-project write → SA in the **function's** project + `objectCreator` on the **other** bucket (Exam 4 · Q12).
- Cloud SQL from apps → **Cloud SQL Client** (Exam 2 · Q38), (Exam 4 · Q36).
- Public, no login, encrypted → **LB + Google-managed cert**. Employees only → **LB + IAP** (Exam 1 · Q36), (Exam 2 · Q55).
- SSH without public IPs → **IAP TCP forwarding** (Exam 3 · Q53). Pod traffic encryption → **mesh mTLS** (Exam 2 · Q41).
- Sessions → **Memorystore**; carts → **Firestore** (Exam 3 · Q59).
- Overloaded Cloud SQL API → **Apigee + Redis cache + exponential backoff** (Exam 6 · Q1).
