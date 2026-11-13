# Domain 4 Study Guide — Integrating Applications with Google Cloud Services

> Condensed from the 63-question bank in [`04-integrating-google-cloud-services.md`](04-integrating-google-cloud-services.md). Citations look like (Exam N · QM). Several scenarios repeat across exams (Private Google Access, Drive OAuth, Workload Identity, stock-price Pub/Sub), so look for paired citations. Items marked "see ⚠️" have a shaky key or explanation, discussed at the end.

---

## 1. Service identity, Application Default Credentials and the metadata server

### Key facts
- **Code runs as a service account, not as you.** When a function's write to another project's bucket fails with 403, the fix is to grant a narrow role (`roles/storage.objectCreator`) **on the bucket** to the identity the function runs as. Granting the role to your user account, or giving yourself `iam.serviceAccountUser`, doesn't change what the function can do. Enabling the API in project B doesn't fix a permissions error (Exam 1 · Q13, see ⚠️ for which service account that really is).
- **Cross-project access = home-project service account + role on the remote resource.** A Compute Engine app in project A that publishes to a topic in project B runs with a **service account from project A**, which is granted publisher **directly on the topic** in project B (Exam 1 · Q47).
- **Application Default Credentials (ADC)** pick up the service account attached to the VM, so no key file has to be distributed. Google manages rotation of those credentials (Exam 2 · Q49), (Exam 1 · Q47).
- **Metadata server:** `http://metadata.google.internal/` with the header `Metadata-Flavor: Google`. It is reachable only from inside the instance and returns live values, such as `computeMetadata/v1/project/project-id` (Exam 2 · Q46).
- **No client library for your language?** Get a short-lived **access token from the metadata server** and send it in the `Authorization` header of your REST calls (Exam 4 · Q32).
- **BigQuery from a script or CLI:** querying needs **BigQuery Data Viewer** (read tables) **plus BigQuery Job User** (create query jobs). Data Editor adds write access you don't need (Exam 3 · Q41).

### Credential options compared

| Option | Verdict | Why | Source |
|---|---|---|---|
| Attached service account + ADC | ✅ Best | No keys to distribute, Google rotates credentials | (Exam 2 · Q49) |
| Metadata-server token in `Authorization` header | ✅ For raw REST | Short-lived, refreshed by the platform | (Exam 4 · Q32) |
| JSON key in source repo / CI package | ❌ | Exposed if the repo leaks | (Exam 2 · Q49) |
| P12 file copied to host | ❌ | Manual transfer, leak risk | (Exam 2 · Q49) |
| API key in the code or in `GOOGLE_APPLICATION_CREDENTIALS` | ❌ | An API key isn't a service-account identity | (Exam 4 · Q32) |
| `gcloud auth application-default print-access-token` at startup, saved to a file | ❌ | The token expires, and you would have to manage refresh yourself | (Exam 4 · Q32) |
| Signed URLs "for authentication" | ❌ | They grant access to objects, not general API auth | (Exam 2 · Q49) |

### Decision rules
- 403 from code calling an API: find the **runtime identity**, then grant the **least-privileged role on the target resource** (Exam 1 · Q13), (Exam 1 · Q47).
- "Securely distribute credentials to VMs": the answer is **don't**. Use the attached service account with ADC (Exam 2 · Q49).
- Need project ID or region at runtime on Cloud Run: query the **metadata server**, not console-copied environment variables or the Cloud Asset Inventory API (Exam 2 · Q46).
- BigQuery permission error when running queries: **Data Viewer + Job User** (Exam 3 · Q41).

### Traps
- Options that use a service account **from the other project** (project B's account used on project A's VMs) create a reverse dependency (Exam 1 · Q47).
- "Use ADC with the private key of a service account" sounds modern, but it still means handling a key file (Exam 1 · Q47).
- Creating a view or copying the table to a new dataset doesn't fix a permission error (Exam 3 · Q41).

---

## 2. Workload Identity on GKE

### Key facts
- **Workload Identity** binds a **Kubernetes service account (KSA)** to a **Google service account (GSA)**. Pods get short-lived tokens, so no keys are stored in the cluster. It is Google's recommended way for GKE workloads to call Google Cloud APIs (Exam 1 · Q51), (Exam 3 · Q27).
- Setup steps: create the GSA with the needed role (BigQuery, Spanner and so on) → create a KSA → **enable Workload Identity on the cluster** → bind KSA to GSA with **`roles/iam.workloadIdentityUser`** → set the KSA in the Deployment spec (Exam 2 · Q37), (Exam 1 · Q57), (Exam 3 · Q31).
- It is a **one-time setup**, and credentials are rotated for you (Exam 3 · Q27).
- It needs minimal code change. Client libraries pick up the identity automatically, for example when accessing Spanner from microservices (Exam 1 · Q44).
- It works **across projects**: grant the GSA roles in whichever project holds the resource (Exam 1 · Q51).

### Option comparison

| Option | Problem | Source |
|---|---|---|
| Node's service account | Every Pod on the node shares it, which breaks least privilege | (Exam 1 · Q51), (Exam 1 · Q57), (Exam 3 · Q31) |
| GSA key in a Kubernetes Secret, exposed as env var or file | A long-lived key you must store and rotate | (Exam 1 · Q44), (Exam 2 · Q37), (Exam 3 · Q27) |
| GSA key in Secret Manager, fetched by an init container or the client lib | Still a key, just stored somewhere else | (Exam 2 · Q37), (Exam 1 · Q57), (Exam 3 · Q31) |
| Key encrypted with Cloud KMS | Adds complexity, and you still handle a decrypted credential | (Exam 1 · Q44) |
| HashiCorp Vault dynamic account | Extra infrastructure to run | (Exam 3 · Q27) |
| GKE RBAC | Controls access **inside** Kubernetes, not to Google APIs | (Exam 1 · Q51) |
| VPC-native routing | That's connectivity, not credentials | (Exam 1 · Q44) |
| Key embedded in source code | Never | (Exam 3 · Q27) |

### Decision rules
- Any "GKE + Google API + best practice" question: pick **Workload Identity**. For "choose two", pick **enable on cluster + bind KSA↔GSA** (Exam 1 · Q57), (Exam 3 · Q31).
- Words like "auto-rotating", "one-time setup" and "no keys" all point to Workload Identity (Exam 3 · Q27).

### Traps
- Anything that mentions a **service account key**, however well protected, is a distractor (Exam 2 · Q37).

---

## 3. OAuth 2.0 for accessing users' data

### Key facts
- When an app acts **on behalf of a user** on that user's own data, such as their Google Drive, it needs an **OAuth 2.0 client ID**. Not an API key (that identifies only the project), not a service account (server-to-server, with no user), and not SAML (SSO) (Exam 2 · Q56).
- **Request a narrow scope**: `https://www.googleapis.com/auth/drive.file` gets a per-user access token limited to files the app works with (Exam 4 · Q20), (Exam 4 · Q56).
- **Authorization-code flow:** redirect to the Google consent screen → user signs in (SSO) and consents → the app receives an **authorization code** → the app **exchanges the code for an access token** → it calls the API with that token (Exam 3 · Q7).
- The app **never sees or stores the user's Google password** (Exam 3 · Q7).

### Decision rules
- "Users' Drive", "on behalf of users", "without domain restrictions" → **OAuth client ID + per-user token + minimal scope** (Exam 4 · Q20), (Exam 4 · Q56).
- **Domain-wide delegation** (with an OAuth client or a service account) gives access to the whole Workspace domain. That is excessive and doesn't fit users outside your domain (Exam 4 · Q20), (Exam 4 · Q56).
- The runtime doesn't change the answer. The same OAuth answer applies on Compute Engine or any other Google Cloud runtime (Exam 4 · Q56).

### Traps
- An option that stops at "receive an authorization code, store it in cookies and use it to authenticate" is missing the **code-for-token exchange** (Exam 3 · Q7).
- "Service account + `drive.file` scope + signed JWT" has the right scope on the wrong identity, since a service account isn't the user (Exam 4 · Q20), (Exam 4 · Q56).
- Collecting usernames and passwords, hashed or forwarded, is always wrong (Exam 3 · Q7).

---

## 4. Securing invocations between services

### Key facts
- **Only authorized services may call a function:** create a service account with the **Cloud Functions Invoker** role and make calls as that account. The **Viewer** role can only read configuration and can't invoke. **IAP** is for users reaching web apps, not service-to-service calls. A separate OAuth client ID adds complexity for no benefit (Exam 1 · Q30).
- **CORS:** if a browser page on `https://www.example.com` posts to a function on `https://fn.example.com`, the function returns **`Access-Control-Allow-Origin: https://www.example.com`**, the exact calling origin. `*` lets any site in, `https://*.example.com` is broader than needed, and the function's own origin blocks the real callers (Exam 3 · Q29).
- **Scheduling calls to an internal-ingress Cloud Run service:** the keyed fix for the 403 is **Cloud Scheduler + Pub/Sub** delivering to Cloud Run. Switching ingress to "Internal and Cloud Load Balancing" exposes the service, a cron VM adds management overhead, and `roles/run.developer` is overly broad (Exam 4 · Q14, see ⚠️).

### Decision rules
- "Invoke" means **Invoker** role (`roles/cloudfunctions.invoker` style roles), granted to the **calling** service account (Exam 1 · Q30).
- Restricting browser callers means CORS with the **exact origin of the page** (Exam 3 · Q29).

### Traps
- Viewer vs Invoker: if a role name doesn't say "Invoker", it can't invoke (Exam 1 · Q30).
- The function's own domain in `Access-Control-Allow-Origin` blocks the real callers (Exam 3 · Q29).

---

## 5. API management: Cloud Endpoints and Apigee

### Key facts
- **Authenticate callers + enforce quotas + track metrics** in front of a backend: use an **API management layer**. In the bank this is **Cloud Endpoints**, which sits between Cloud Load Balancing and the app (Exam 1 · Q55).
- **Backward-incompatible API change on Cloud Functions:** leave the original function unchanged, deploy a **second function** with the new API, and expose a **versioned API through Cloud Endpoints**. One function branching on a version field risks breaking old callers. A plain load balancer has no API-management features, and Cloud Functions doesn't route by version automatically (Exam 1 · Q18).
- **Subscription tiers with daily request limits:** put the GKE service behind an **Apigee proxy**, identify client apps with **API keys**, and apply a **Quota policy** per tier (Exam 6 · Q3).
- **Apigee environment isolation by hostname:** attach each environment to its **own environment group** (orders-test → test group, orders-prod → prod group), then add each **hostname to the environment group**. Hostnames belong to environment groups, not to environments (Exam 4 · Q27).

### Apigee policies and API tools

| Need | Use | Not | Source |
|---|---|---|---|
| N requests **per day** per client | **Quota** policy | SpikeArrest (it smooths bursts and isn't a daily quota) | (Exam 6 · Q3) |
| Identify client apps | **API keys** | One cluster or project per tier | (Exam 6 · Q3) |
| Auth + quotas + metrics in front of an app | **Cloud Endpoints** / API management | IAP (user identity), GKE Ingress (routing only), Cloud Run (a runtime) | (Exam 1 · Q55) |
| Serve v1 and v2 side by side | Two backends + **versioned API in Endpoints** | LB split, one function with a version switch | (Exam 1 · Q18) |

### Traps
- Duplicating infrastructure per tier (two GKE clusters, two projects with their own load balancers) is never the recommended way to implement quotas (Exam 6 · Q3).
- Putting both Apigee environments in one environment group lets both hostnames reach both environments (Exam 4 · Q27).

---

## 6. Pub/Sub messaging patterns

### Key facts
- **Fan-out:** one topic per event type, with **one subscription per consumer**. Each subscription gets its own copy of every message. New downstream steps add a subscription without changing the publisher (Exam 2 · Q42).
- **Every message must go to two sinks** (Cloud Storage and BigQuery) with low operational overhead: **one topic, 2 subscriptions, 2 Cloud Run services** (Exam 4 · Q44).
- **Competing consumers / load sharing:** a pool of audit-service VMs that should split the work uses **one topic + one pull subscription** that all instances share. A subscription per instance would duplicate every message (Exam 4 · Q50).
- **Durability against downstream failure:** if a function that sends emails throws 500s, have the sender **publish to Pub/Sub** and let the function consume the topic. Messages persist until processed. A longer timeout, aggressive one-second retries or a Memorystore hand-off don't give you durability (Exam 4 · Q7).
- **Ordering:** to keep updates per stock symbol in order in an in-memory DB, use a **pull subscription with message ordering enabled and the stock symbol as the ordering key** (Exam 4 · Q13).
- **Serverless consumer that costs nothing when idle:** a **Cloud Function with a Pub/Sub trigger**. You don't need to also create a pull subscription in code. Compute Engine and GKE cost money even when no messages arrive (Exam 2 · Q9).
- **Several processes analyzing logs in near real time:** a **Cloud Logging sink → Pub/Sub topic**, with each process subscribing. Polling the Logging API doesn't scale, and a Cloud Storage sink isn't near real time (Exam 4 · Q24).

### Subscription design selector

| Goal | Topology | Source |
|---|---|---|
| Each team or step gets every event | 1 topic, **N subscriptions** | (Exam 2 · Q42) |
| Same message to Cloud Storage **and** BigQuery | 1 topic, **2 subs**, 2 services | (Exam 4 · Q44) |
| N worker instances share the load | 1 topic, **1 pull sub** shared by all | (Exam 4 · Q50) |
| Per-key ordering | Pull sub, **ordering key** = entity ID | (Exam 4 · Q13) |

### Decision rules
- Copies or duplicates: a **subscription** is the unit of fan-out. A **topic per publisher instance** makes subscribers listen to everything (Exam 4 · Q50).
- Two subscribers attached to **one** subscription split the messages between them. They don't each get every message (Exam 4 · Q44), (Exam 4 · Q50).
- Per-entity order matters (prices, balances): use an **ordering key** (Exam 4 · Q13).
- "Avoid losing emails, orders or events" → put **Pub/Sub** between producer and consumer (Exam 4 · Q7).

### Traps
- Bank explanations disagree on push vs pull for high volume. (Exam 4 · Q50) says push is less suited to large volumes, and (Exam 4 · Q26) claims the opposite and keys "push + exactly-once" (see ⚠️).
- One Cloud Run service writing to both sinks via push couples both writes into one handler (Exam 4 · Q44).
- A separate topic for each processing step (Exam 2 · Q42) makes the publisher know about every step.

---

## 7. Event-driven triggers and orchestration

### Key facts
- **Object uploaded → message on a topic, minimal effort:** configure **Cloud Storage Pub/Sub notifications** on the bucket. That needs no code, unlike a function, App Engine app or GKE app that publishes for you (Exam 3 · Q47).
- **Flexible, team-maintainable triggers that route to Cloud Run:** an **Eventarc trigger** on Cloud Storage events with **Cloud Run as the target**. Pub/Sub → Cloud Build misuses a CI tool as a runtime, and Firebase functions are aimed at Firebase-based apps (Exam 4 · Q16, see ⚠️ about filename filtering).
- **React to resource creation without changing how resources are provisioned:** a **Cloud Audit Logs-based trigger** fires a **Cloud Function** each time a VM is created, and the function adds missing labels. Periodic Cloud Scheduler scripts leave gaps between runs, and `gcloud terraform vet` only covers Terraform-provisioned resources (Exam 6 · Q9).
- **Orchestrating Cloud Functions where each output drives the next step, with low latency:** use **Workflows with conditional jumps** (`switch`/`next`). **Cloud Composer** (Airflow) is heavier and adds latency. Callbacks are for waiting on external events, not for branching (Exam 4 · Q1).
- **Scheduling:** use **Cloud Scheduler** rather than cron on VMs (Exam 4 · Q14, see ⚠️).
- **Ticket seat reservation:** the bank keys **Pub/Sub + Eventarc → GKE** over Cloud Tasks + Workflows, a Cloud Storage drop or a load balancer + MIG (Exam 6 · Q13, see ⚠️).

### Orchestration vs choreography

| Need | Service | Source |
|---|---|---|
| Ordered serverless steps with branching on results, low latency | **Workflows** (conditional jumps) | (Exam 4 · Q1) |
| Heavy, long-running ETL DAGs | Cloud Composer (Airflow) | (Exam 4 · Q1) |
| Broadcast an event to independent consumers | **Pub/Sub** topic + subscriptions | (Exam 2 · Q42) |
| Route Google Cloud events to Cloud Run with filters | **Eventarc** | (Exam 4 · Q16) |
| Bucket change → message on a topic, no code | **Cloud Storage Pub/Sub notifications** | (Exam 3 · Q47) |
| Act when someone creates a resource | **Audit-log trigger → function** | (Exam 6 · Q9) |
| Time-based invocation | **Cloud Scheduler** | (Exam 4 · Q14) |

### Decision rules
- "Minimal implementation effort" + Cloud Storage → Pub/Sub: use the **built-in notification**, not code (Exam 3 · Q47).
- "Each function's output guides the workflow": use **Workflows**, not Composer (Exam 4 · Q1).
- "Automatically correct …", "without altering the current process" → an **event trigger on audit logs**, not a poller (Exam 6 · Q9).

### Traps
- Cloud Build is CI/CD, not an application runtime (Exam 4 · Q16).
- Workflows **callbacks** are a distractor when the branching logic only depends on the step results (Exam 4 · Q1).

---

## 8. Cloud Storage from application code

### Key facts
- **Signed URLs** give **time-limited access to a single object** to anyone holding the URL, **without a Google account**. Your app authenticates users first and then hands out the URL (Exam 3 · Q45), (Exam 6 · Q7).
  - Downloads for a limited period → signed URL. Email attachments, temporary buckets and expiring cookies are all distractors (Exam 1 · Q15).
  - Large uploads (2 MB–1 GB) with minimal infrastructure → clients **upload directly to Cloud Storage via signed URLs**, not through your web server, file store or database (Exam 2 · Q24).
  - Share with outsiders with a **customizable expiry** → a signed URL per document. ACLs don't expire, `allAuthenticatedUsers` Viewer is far too broad, and **signed policy documents** are aimed at uploads (Exam 6 · Q7).
- **Request-rate ramp-up:** a cold bucket hit with thousands of requests per second returns 429/5xx. **Ramp up gradually** by throttling clients. Switching to the XML API or relaying error codes doesn't help (Exam 1 · Q22).
- **429/503 handling:** **retry with truncated exponential backoff**, meaning increasing intervals up to a maximum number of attempts. Fixed or decreasing intervals and batch retries are wrong (Exam 1 · Q24), (Exam 3 · Q32).
- **Read only some metadata properties:** use the JSON API **`fields` request parameter** on `objects.get`. `patch` updates metadata, `compose` concatenates objects, and `copy` duplicates them (Exam 3 · Q21).
- **Empty "folder":** create a zero-byte object whose name ends in a **trailing slash** (`user123/`). There is no special content type for folders (Exam 3 · Q56).
- **Copy local files to a bucket from the command line:** `gsutil cp LOCAL gs://BUCKET/` (Exam 1 · Q48, see ⚠️ for the current CLI).

### Access options for private objects

| Option | Verdict | Source |
|---|---|---|
| Signed URL issued after your app authenticates the user | ✅ Anonymous users, time-limited, per object | (Exam 3 · Q45), (Exam 6 · Q7) |
| `allUsers` / `allAuthenticatedUsers` + Object Viewer | ❌ Public to the internet | (Exam 3 · Q45), (Exam 6 · Q7) |
| IAP | ❌ Needs Google identities, gates apps not objects | (Exam 3 · Q45) |
| Cloud Armor IP allowlist | ❌ IPs are shared or change | (Exam 3 · Q45) |
| Per-user buckets + per-bucket service accounts handed to clients | ❌ Complex, leaks credentials | (Exam 2 · Q24) |

### Decision rules
- "Limited time", "external users", "no Google account", "large upload without servers" → **signed URL** (Exam 1 · Q15), (Exam 2 · Q24), (Exam 6 · Q7).
- Spike on a dormant bucket → **ramp up**. Throttling during peaks → **exponential backoff** (Exam 1 · Q22), (Exam 1 · Q24).
- 429 at peak: **backoff** is the immediate fix. A quota increase is slow, caching misses on a cold cache, and a multi-regional class doesn't change request quotas (Exam 1 · Q24).

### Traps
- Spreading uploads over many buckets isn't the keyed fix for a ramp-up problem (Exam 1 · Q22).
- (Exam 3 · Q43) keys "multipart upload API" over signed URLs for 500 MB uploads to App Engine, which contradicts (Exam 2 · Q24) (see ⚠️).

---

## 9. Operational databases from code: Spanner, Firestore, SQL

### Key facts
- **Spanner, latency over consistency:** use **stale reads with single-read methods**. Strong reads and read-only transactions may coordinate with the leader. Read-write transactions are for reads and writes together (Exam 1 · Q50).
- **Spanner performance from Go (or any language):** use the **Cloud Client Libraries**. They handle connections, retries and errors idiomatically, unlike the generic Google API Client Libraries or a custom gRPC/HTTP client (Exam 2 · Q16).
- **Spanner credentials from GKE:** use Workload Identity (Exam 1 · Q44). See section 2.
- **Firestore (Datastore mode) memory blow-ups on large lists:** paginate with **query cursors**. Integer offsets still scan the skipped entities, adding latency and cost. A bare limit doesn't page through the rest, and more memory only hides the problem (Exam 3 · Q57).
- **Firestore 429 RESOURCE_EXHAUSTED before a traffic surge:** **optimize queries to cut reads and writes, and retry with exponential backoff**. A quota increase alone or fixed backoff isn't enough (Exam 4 · Q2).
- **Your API's write to Datastore failed with a 5xx:** return **HTTP 500** to your caller so the failure is visible. 204 looks like success, and 406 is about content negotiation (Exam 4 · Q41, see ⚠️).
- **SQL: combine two tables with matching columns and remove duplicates:** use **`UNION`**. `UNION ALL` keeps duplicates, and `JOIN` combines columns, not rows (Exam 3 · Q13).

### Spanner read types

| Read | Freshness | Latency | Use when | Source |
|---|---|---|---|---|
| **Stale read, single-read method** | Slightly old | Lowest | Latency > consistency | (Exam 1 · Q50) |
| Strong read | Latest | Higher | Must see latest data | (Exam 1 · Q50) |
| Read-only transaction | Consistent snapshot | Higher | Several consistent reads | (Exam 1 · Q50) |
| Read-write transaction | Locks | Highest | Read-then-write | (Exam 1 · Q50) |

### Decision rules
- Large result sets cause memory or latency problems → use **cursors**, not offsets (Exam 3 · Q57).
- 429 from a database API → **reduce the load + exponential backoff**. "Fixed backoff" is always a distractor (Exam 4 · Q2).
- "Recommended way to call service X from code" → **Cloud Client Libraries** (Exam 2 · Q16).

### Traps
- Raising Cloud Run memory treats the symptom (Exam 3 · Q57).
- `UNION ALL` vs `UNION`: "eliminate duplicates" means `UNION` (Exam 3 · Q13).

---

## 10. BigQuery and streaming analytics pipelines

### Key facts
- **Flat JSON from an HTTP function that many users need to analyze right away:** **stream it into BigQuery**. Datastore is for entity lookups, Cloud SQL isn't built for that analytics load, and one file per request in Cloud Storage makes querying hard (Exam 1 · Q38).
- **Near real-time SQL analytics at growing scale, managed services only:** **Pub/Sub → Dataflow → BigQuery**. Cloud Storage or Firestore as the sink doesn't give SQL analytics, and self-managed Kafka adds operational load (Exam 4 · Q17).
- **High-volume voting in 30-minute windows, counted and stored for reporting:** **Pub/Sub → Dataflow** (counts plus raw votes) **→ BigQuery**, visualized in Data Studio (Exam 4 · Q39).
- **BigQuery Storage Write API without duplicates:** create a write stream of **committed type** (Exam 4 · Q11, see ⚠️ for the explanation's mistakes).
- **A user who doesn't care about job duration and mustn't impede critical work:** run their queries as **batch** jobs, which start when resources are free. You don't need a separate project or manual timing, and `jobUser` alone doesn't set a priority (Exam 4 · Q43, see ⚠️).
- **Query permissions:** Data Viewer + Job User (Exam 3 · Q41).

### Analytics sink selector

| Requirement | Pipeline | Source |
|---|---|---|
| Per-request JSON, immediate ad-hoc analytics | Function → **BigQuery streaming** | (Exam 1 · Q38) |
| Event stream, near real-time SQL, rapid growth | **Pub/Sub → Dataflow → BigQuery** | (Exam 4 · Q17) |
| High-volume windowed counts + history | **Pub/Sub → Dataflow → BigQuery** + dashboard | (Exam 4 · Q39) |
| Real-time log analysis by several consumers | **Logging sink → Pub/Sub** | (Exam 4 · Q24) |

### Decision rules
- "Analysts", "SQL", "aggregate" → land the data in **BigQuery** (Exam 1 · Q38), (Exam 4 · Q17).
- "High volume stream + transform or count" → **Dataflow** between Pub/Sub and BigQuery, rather than Cloud Functions (Exam 4 · Q39).
- "Don't impede other workloads, duration irrelevant" → **batch priority** (Exam 4 · Q43).

### Traps
- Memorystore as the store for high-volume event capture, or a CSV export to Sheets for reporting, are both distractors (Exam 4 · Q39).
- Building your own dedup layer (Kafka with UUIDs, Pub/Sub + Functions) when the Write API stream type handles it (Exam 4 · Q11).

---

## 11. Client tooling, private connectivity and service discovery

### Key facts
- **Listing Bigtable, Memorystore and Cloud SQL resources with user-defined filters:** run `gcloud bigtable instances list`, `gcloud redis instances list` and `gcloud sql databases list` **with `--filter`**, so filtering happens at the source. Data-plane APIs (HBase, Redis, MySQL) are for data, not inventory (Exam 1 · Q31).
- **Calling Google APIs from code:** prefer **Cloud Client Libraries** (Exam 2 · Q16).
- **A VM with no external IP calling the Cloud Storage API:** enable **Private Google Access** on the subnet. Carrier Peering connects on-prem to Google, VPC Peering connects VPCs, and Shared VPC shares networks across projects. None of those give access to Google APIs (Exam 3 · Q9), (Exam 4 · Q33).
- **Dynamic discovery between Cloud Run services and functions:** use a **Service Directory** namespace. Services register at deploy time and are looked up at runtime. That beats hand-maintained environment variables, naming conventions, querying the Admin APIs, or Consul on a single VM (Exam 3 · Q28).
- **Resilient connection to a legacy REST service running in two regional GKE clusters, with probe-based health checks on a separate port:** the key is **Traffic Director with a sidecar proxy**, plus a firewall rule that allows the health checks (Exam 4 · Q35, see ⚠️ on where health checks really come from).

### Decision rules
- "No public IP" + "Google API" → **Private Google Access** (Exam 3 · Q9), (Exam 4 · Q33).
- "Service registry", "register at deploy, query at runtime" → **Service Directory** (Exam 3 · Q28).
- "Filter results" with gcloud → the **`--filter`** flag, not filtering in the app (Exam 1 · Q31).

### Traps
- Peering products (Carrier, VPC) sound like connectivity fixes, but they don't reach Google APIs (Exam 4 · Q33).
- Self-managed Consul on one VM is both overhead and a single point of failure (Exam 3 · Q28).
- `gcloud dataproc cp` doesn't exist, and `hadoop fs` needs the connector (Exam 1 · Q48).

---

## ⚠️ Questionable answers

| Item | Issue |
|---|---|
| **(Exam 4 · Q26)** | Keys **push + exactly-once delivery** and says push suits high volume better. Pub/Sub exactly-once delivery is a **pull**-subscription feature, and (Exam 4 · Q50) says push is *less* suited to large volumes. The same scenario in (Exam 4 · Q13) keys **pull + ordering key**. Expect the pull answer to be the defensible one. |
| **(Exam 1 · Q13)** | `service-PROJECTA@gcf-admin-robot.iam.gserviceaccount.com` is the Cloud Functions **service agent** (used by Google to manage the function), not the **runtime** service account your code executes as. The principle (grant `objectCreator` on the bucket to the function's identity) is right, but in practice the grant goes to the function's runtime service account. |
| **(Exam 3 · Q43)** | Keys "multipart upload API" for 500 MB uploads to App Engine and rejects signed URLs as "unnecessary complexity". App Engine request sizes are limited far below 500 MB, and Google's pattern (taught in (Exam 2 · Q24)) is direct-to-Cloud Storage uploads via **signed URLs**. Learn the key, but expect signed URLs elsewhere. |
| **(Exam 6 · Q13)** | Keys asynchronous Pub/Sub + Eventarc for "**immediate confirmation** of a specific seat". Publishing only confirms that the message was received, not that the seat was reserved. The rejection of the load-balancer option ("relies on polling the load balancer") is technically wrong. |
| **(Exam 4 · Q11)** | The answer (committed type) is right, but the explanation says the default stream is "buffered". The default stream gives at-least-once semantics, and buffered is a separate type. Committed-type streams avoid duplicates through **stream offsets**, not some automatic dedup. |
| **(Exam 4 · Q14)** | A 403 calling Cloud Run usually means the caller lacks **`roles/run.invoker`**. The explanation says Cloud Run "subscribes" to Pub/Sub, but delivery is a push subscription to the service. Treat the key as "use managed Scheduler, not VM cron or loosened ingress". |
| **(Exam 4 · Q16)** | The explanation says Eventarc Cloud Storage triggers filter by object name and that Cloud Functions can't. Direct Cloud Storage events filter by bucket, and Cloud Functions (2nd gen) triggers are themselves Eventarc triggers. Learn "Eventarc → Cloud Run for flexible triggers" but not the filtering claims. |
| **(Exam 4 · Q35)** | Keys health checks "initiated from the sidecar proxy". For Traffic Director (now Cloud Service Mesh), backend health checks come from **Google Cloud health-check probers**, and firewall rules normally allow those ranges. Know the key, but it's shaky. |
| **(Exam 4 · Q43)** | The answer (batch queries) is fine, but the explanation says batch jobs are "less expensive". Batch priority changes scheduling, not on-demand price, and the cited link is for Google Cloud *Batch*, a different product. |
| **(Exam 4 · Q41)** | Keys C (return 500), but its own explanation recommends "C **and** D" (retry with backoff, then report). In practice, retrying transient 5xx with bounded backoff and then surfacing a 5xx is best. Pick C if you must pick one. |
| **(Exam 1 · Q57)**, **(Exam 3 · Q31)** | Option V describes itself as "not as endorsed" yet is keyed correct. (Exam 3 · Q31) writes the role as `roles/iam.workloadIdentity`, but the real role is **`roles/iam.workloadIdentityUser`**. The feature is now called *Workload Identity Federation for GKE*. |
| **(Exam 1 · Q48)** | `gsutil` is legacy. Google now recommends **`gcloud storage cp`**. The explanation also wrongly says `gcloud` has a general `cp` command. |
| **(Exam 2 · Q46)** | The explanation says to read the region from `instance/zone`. Cloud Run's metadata server exposes `instance/region` for that. |
| **(Exam 1 · Q18)**, **(Exam 1 · Q55)**, **(Exam 4 · Q39)** | Older product framing. Cloud Endpoints still exists, but API Gateway and Apigee are the current API-management options. Data Studio is now **Looker Studio**. |

---

## Last-minute cheat sheet

- Code runs as a **service account**: on a 403, grant a **narrow role on the target resource** to the runtime identity (Exam 1 · Q13), (Exam 1 · Q47).
- On VMs and Cloud Run, use **ADC / metadata server tokens**, never key files, P12s or API keys (Exam 2 · Q49), (Exam 4 · Q32).
- Metadata server: `metadata.google.internal` + `Metadata-Flavor: Google` (Exam 2 · Q46).
- GKE → Google APIs = **Workload Identity**: enable on the cluster + bind KSA↔GSA with `workloadIdentityUser` (Exam 1 · Q57), (Exam 3 · Q31), (Exam 2 · Q37).
- Users' Drive = **OAuth client ID + `drive.file` scope + per-user token**. No domain-wide delegation (Exam 4 · Q20), (Exam 4 · Q56).
- OAuth flow: consent → **auth code → exchange for access token** → call API (Exam 3 · Q7).
- Service-to-service: **Invoker** role on the caller's service account. IAP is for users (Exam 1 · Q30).
- CORS: `Access-Control-Allow-Origin` = the **exact page origin** (Exam 3 · Q29).
- Auth + quotas + metrics → **API management** (Endpoints). Daily tier limits → **Apigee Quota policy + API keys** (Exam 1 · Q55), (Exam 6 · Q3).
- Apigee: **hostnames go on environment groups**, one group per environment (Exam 4 · Q27).
- Breaking API change: keep v1, deploy v2, **version through the gateway** (Exam 1 · Q18).
- Pub/Sub fan-out = **one subscription per consumer**. Load sharing = **one shared pull subscription** (Exam 2 · Q42), (Exam 4 · Q44), (Exam 4 · Q50).
- Per-key order → **ordering key** on a pull subscription (Exam 4 · Q13).
- Don't lose work when a consumer fails → **put Pub/Sub in between** (Exam 4 · Q7).
- Pay only when messages arrive → **function with a Pub/Sub trigger** (Exam 2 · Q9).
- Bucket change → topic, no code: **Cloud Storage Pub/Sub notifications** (Exam 3 · Q47).
- Flexible event routing to Cloud Run → **Eventarc**. React to resource creation → **audit-log trigger** (Exam 4 · Q16), (Exam 6 · Q9).
- Branching orchestration of functions → **Workflows conditional jumps**, not Composer (Exam 4 · Q1).
- Temporary or external object access, big direct uploads → **signed URLs** (Exam 1 · Q15), (Exam 2 · Q24), (Exam 6 · Q7).
- 429/503 → **truncated exponential backoff**. Cold bucket spike → **ramp up gradually** (Exam 1 · Q24), (Exam 3 · Q32), (Exam 1 · Q22).
- Partial metadata → `fields` parameter. Empty folder → object name ending in `/` (Exam 3 · Q21), (Exam 3 · Q56).
- Spanner latency first → **stale single reads**. Use Cloud Client Libraries (Exam 1 · Q50), (Exam 2 · Q16).
- Firestore big lists → **cursors**. Firestore 429 → **optimize + exponential backoff** (Exam 3 · Q57), (Exam 4 · Q2).
- Analytics: **Pub/Sub → Dataflow → BigQuery**. Dedup with the Write API → **committed stream**. Low-priority queries → **batch** (Exam 4 · Q17), (Exam 4 · Q11), (Exam 4 · Q43).
- No external IP → **Private Google Access**. Runtime discovery → **Service Directory** (Exam 4 · Q33), (Exam 3 · Q28).
