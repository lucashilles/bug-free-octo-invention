# Domain 2 Study Guide — Building and Testing Applications

> Condensed from the 57-question bank in [`02-building-and-testing.md`](02-building-and-testing.md). Citations look like (Exam N · QM). Several questions repeat across exams with different wording, so look for the paired citations. Many explanations use older product names (Stackdriver, Container Registry, Cloud Debugger); see the questionable-answers section before trusting those.

---

## 1. Developer environments and source control

### Key facts

- **Cloud Shell** runs in a browser and comes with a built-in code editor, Git and integrated access to your project's resources. Source code never lands on the machine you are sitting at (Exam 1 · Q45). It also has `gcloud` preinstalled and already authenticated, needs no local install, and interactive sessions cost nothing (Exam 5 · Q6).
- **Cloud Code** is the IDE extension for VS Code and IntelliJ. It adds Kubernetes-aware completion and snippets, debugging against the cluster, deploy workflows and cluster resource management (Exam 3 · Q18).
- **Cloud Workstations** are managed development environments that can reach resources inside a VPC. They are built from base images that you can extend with custom images (Exam 4 · Q38).
- A **kubeconfig** file holds clusters, users and contexts. `kubectl config` switches between contexts, so one file can cover several GKE clusters (Exam 3 · Q37).
- **Trunk-based development** means small, frequent commits to the main branch. This keeps merge conflicts small when releases are frequent (Exam 4 · Q28).

### Which developer environment?

| Requirement in the stem | Pick | Why not the others |
|---|---|---|
| Emergency fix from a public or non-corporate computer, no local code allowed | **Cloud Shell + its editor**, then open a pull request (Exam 1 · Q45) | A public PC with Git or a VM stores code locally. A mounted Cloud Storage bucket is not a Git workflow. |
| Urgent production workaround script from a personal computer, quickly and cheaply | **Cloud Shell**: clone the repo and run the script there (Exam 5 · Q6) | Cloud Workstations means launching and paying for a VM. Installing VS Code + Cloud Code or the gcloud CLI locally takes setup time. |
| Rich IDE support for GKE in VS Code or IntelliJ | **Cloud Code** (Exam 3 · Q18) | The Cloud Shell editor is for quick edits. Notebooks are for data and ML work. |
| Consistent security controls, access inside VPC-SC or PSC networks, custom tools allowed | **Cloud Workstations with preconfigured base images + custom images rebuilt weekly** (Exam 4 · Q38) | Letting developers build their own images breaks consistency. Cloud Code + VPN or IAP is more complex and less isolated. |

### Decision rules

- No local source code allowed, or a quick one-off fix from a machine with no tools installed: use **Cloud Shell** (Exam 1 · Q45), (Exam 5 · Q6).
- IDE named (VS Code, IntelliJ) and GKE or Cloud Run work: use **Cloud Code** (Exam 3 · Q18).
- Security baseline plus custom tooling: use **centrally managed images that get rebuilt on a schedule**, not images developers create freely (Exam 4 · Q38).
- Multiple clusters: the bank's key is **one shared config file defining clusters, users and contexts + `kubectl config`** (Exam 3 · Q37). This key is debatable; see the questionable-answers section.
- Rapid releases with few merge conflicts: use **trunk-based development** (Exam 4 · Q28).

### Coding fundamentals that show up

- Aggregating a value per key (for example, summing transaction amounts per account number) calls for a **hash table**. It gives near-constant-time lookups. A linked list is O(n), and a 2-D array or a delimited string is a poor fit (Exam 2 · Q3).

### Traps

- "Open three terminals, one per cluster" is never the best practice (Exam 3 · Q37).
- Cloud Storage bucket mounted as a drive "linked to Git" is a distractor (Exam 1 · Q45).
- Cloud Workstations is for long-lived managed dev environments. For a one-off urgent fix it is slower and costlier than Cloud Shell (Exam 5 · Q6).
- Feature-branch options exist alongside trunk-based ones. Exam 4 · Q28 prefers trunk-based, but Exam 4 · Q47 keys feature branches plus CAB approval. Expect conflicting keys (see the questionable-answers section).

---

## 2. Local development and emulators

### Key facts

- The **Pub/Sub emulator** is installed and started with gcloud, using a project ID. You point the app at it by exporting **`PUBSUB_EMULATOR_HOST`** (Exam 4 · Q21). **`$(gcloud beta emulators pubsub env-init)`** sets that same variable for you automatically (Exam 5 · Q2).
- The **Cloud SQL Auth Proxy** can run on a developer workstation. It authenticates with IAM, encrypts the connection to Cloud SQL, and the app connects to **localhost** (Exam 5 · Q7).
- Emulators avoid cloud costs and give an isolated, predictable environment. Google provides emulators for services such as **Bigtable** and **Pub/Sub** (Exam 4 · Q8), (Exam 2 · Q54).
- The **Functions Framework** runs a Cloud Function on your local machine so you can call it with curl (Exam 3 · Q38).
- **Minikube** gives you a lightweight single-node Kubernetes cluster. **Skaffold** builds, pushes and deploys to it, and rebuilds or redeploys automatically when code changes (Exam 3 · Q60).
- The **Spanner emulator** is good for functional tests but **does not reproduce real performance characteristics** (Exam 4 · Q52).

### Decision rules

- Fast and cheap testing of an MVP built on Cloud Run, Bigtable and Pub/Sub: **emulators locally, then deploy** (Exam 4 · Q8).
- Quick Pub/Sub integration check on every build: **Pub/Sub emulator started with gcloud**, with the app pointed at it through `env-init` or `PUBSUB_EMULATOR_HOST` (Exam 5 · Q2), (Exam 4 · Q21).
- Local tests of an App Engine app against Cloud SQL with encrypted, IAM-authenticated traffic: **run the Cloud SQL Auth Proxy locally and connect to localhost** (Exam 5 · Q7).
- Unit tests that assert Pub/Sub message ordering cheaply and reliably: use the **Pub/Sub emulator**, not mocks, not one topic per tester, and not subscription filters (Exam 2 · Q54).
- Integration test of a subscriber that handles credit card data: run the **emulator + a publishing service that sends a predefined set of test messages**. Don't use random content, and never replay production messages because they contain sensitive data (Exam 2 · Q58).
- Diagnosing production errors in a Cloud Run service that moves Pub/Sub messages from topic A to topic B with mock messages: run the **Pub/Sub and Cloud Run emulators locally**, set the log level to DEBUG or INFO, and publish mock messages to topic A. Don't point production at local topics (Exam 2 · Q26).
- Developing a Cloud Function triggered by Cloud Storage: use the **Functions Framework locally**. Don't rewrite it as an HTTP function, and don't edit a copy in production (Exam 3 · Q38).
- Local container build and run that matches the production GKE deployment, with low resource use: use **Minikube + Skaffold** (Exam 3 · Q60).

### Traps

- `gcloud config set api_endpoint_overrides/pubsub https://pubsubemulator...` is a fake endpoint. The emulator is local and is reached through `PUBSUB_EMULATOR_HOST` (Exam 4 · Q21).
- Cloud Code + calling `pubsub.googleapis.com` still hits the real service, and so does just enabling the Pub/Sub API (Exam 4 · Q21), (Exam 5 · Q2).
- Cloud SQL from a laptop: a local PostgreSQL install skips IAM and doesn't test Cloud SQL. Connecting to the private IP needs VPN or peering and has no IAM auth. Encrypting rows is not the same as encrypting the connection. A Compute Engine VM running HAProxy + the proxy is needless complexity (Exam 5 · Q7).
- Docker Compose doesn't emulate Kubernetes. Terraform + kubeadm provisions infrastructure. kaniko + Tekton is in-cluster CI that is too heavy for a laptop (Exam 3 · Q60).
- An emulator is the wrong answer for **performance** tests (Exam 4 · Q52).

---

## 3. Building container images

### Key facts

- **Cloud Native Buildpacks** detect the language and framework and build an image without a Dockerfile. `pack build` can push straight to Artifact Registry (Exam 1 · Q59).
- **`gcloud run deploy --source`** runs Cloud Build behind the scenes with Buildpacks and stores the image in a registry (Exam 1 · Q59).
- **Jib** builds Docker or OCI images for Java from Maven or Gradle, with no Dockerfile and no Docker daemon (Exam 3 · Q51).
- **Build and push with Cloud Build:** write a `cloudbuild.yaml` with a `docker build -t <registry path>` step and a `docker push` step, then run **`gcloud builds submit`** in the source directory (Exam 5 · Q37).
- **Custom builder:** if Cloud Build lacks a tool, package the tool in your own builder image and reference it in a build step (Exam 2 · Q20).

### Build speed

| Option | Faster build? |
|---|---|
| Higher-CPU machine type for Cloud Build | **Yes** (Exam 1 · Q7), (Exam 3 · Q50) |
| `--cache-from` a previous image in the build config | **Yes**, layers are reused (Exam 1 · Q7), (Exam 3 · Q50), (Exam 5 · Q56) |
| Remove the `docker push` step before `gcloud run deploy` | No, it breaks the deploy because Cloud Run pulls from a registry (Exam 5 · Q56) |
| Store images in a Cloud Storage bucket, or run your own registry in a VPC with private worker pools | No, Cloud Storage isn't a registry and a private registry adds work (Exam 5 · Q56) |
| Switch `python:3.7-alpine` to `ubuntu:latest` + apt-installed Python | No, the image becomes much larger |
| Self-hosted registry on a Compute Engine VM | No, and it adds maintenance |
| Put source on Cloud Storage and fetch it with gsutil | No, it doesn't reduce build time |

### Decision rules

- Cloud Run, no Dockerfile, central registry required: use **`pack build`** or **`gcloud run deploy --source`** (Exam 1 · Q59).
- Containerize a standalone Java app instead of lifting and shifting the VM: use **Jib → Artifact Registry → GKE** (Exam 3 · Q51).
- Missing build tool: use a **custom cloud builder image** (Exam 2 · Q20).
- Build an image for a Compute Engine → GKE migration with Cloud Build: **`cloudbuild.yaml` with docker build + push steps, run with `gcloud builds submit`** (Exam 5 · Q37).
- Shorten a Cloud Build → Cloud Run pipeline: add **`--cache-from`** to the docker build step. Keep the push step (Exam 5 · Q56).

### Traps

- "Upload source code to Artifact Registry" doesn't build anything. "A Cloud Build job to push" assumes an image already exists. `--platform=kubernetes` has nothing to do with building (Exam 1 · Q59).
- Downloading the binary during the build hurts security and reproducibility. Committing it to the repo bloats the repo. A feature request gives you no control (Exam 2 · Q20).
- `gcloud run deploy --image` deploys an existing image, `gcloud container images add-tag` only retags, and a `cloudbuild.yaml` that runs `app deploy` targets App Engine. None of them builds and pushes an image (Exam 5 · Q37).
- Migrate for Anthos and Migrate for Compute Engine are VM migration tools. A raw disk import is lift-and-shift (Exam 3 · Q51).

---

## 4. Cloud Build CI pipelines

### Key facts

- Cloud Build is a **managed** CI service with **triggers** on source commits. It needs far less operational work than Jenkins or a CI server on a VM (Exam 3 · Q48).
- Every step shares the **`/workspace`** directory, which holds the checked-out source (Exam 1 · Q1). Writing a file there is the recommended way to pass data from one step to the next (Exam 5 · Q23).
- Each step in the build config shows up **separately in the build history**, so you can see exactly which stage failed (Exam 3 · Q8).
- The Cloud Build **service account** can be given permissions in other projects (Exam 1 · Q40), (Exam 1 · Q3).

### Decision rules

- Build and test on every commit with the least overhead: use a **Cloud Build trigger per commit** (Exam 3 · Q48).
- Unit tests that gate a Cloud Function deploy: run **tests in Cloud Build and deploy automatically from the same build when they pass**, using a dedicated service account. Don't add manual approval, test after deploy, or deploy by hand (Exam 1 · Q3).
- Unit and integration tests whose failures must be easy to identify: use **distinct build steps**. Don't put RUN commands in the Dockerfile, a single combined step, or a separate pipeline (Exam 3 · Q8).
- A file produced in one build step must be read by later steps: **write it to `/workspace`**. Don't use Cloud Storage, Compute Engine metadata or an external web server (Exam 5 · Q23).
- A custom step that adds copyright headers on every commit: a **container that edits files in `/workspace` and commits the changes back** to the repo (Exam 1 · Q1).
- Ops wants one central, secure image registry: use a **registry in a dedicated ops project + IAM for each team's Cloud Build service account**. Never store keys or passwords in the repo (Exam 1 · Q40).
- A test resource must be cleaned up even if the test fails: the **test step writes results to a file and exits 0, the cleanup step runs, and a final step checks the file and fails the build** (Exam 4 · Q6).
- Per-commit performance tests against Spanner that can run concurrently: **create a new Spanner instance per build, load data, run the tests, delete the instance** (Exam 4 · Q52).
- Catch bugs before production with automated feedback: the key is **Cloud Build triggered by Git tags**, not Spinnaker. Spinnaker is for CD (Exam 2 · Q51).

### Traps

- Environment variables don't carry over between Cloud Build steps, so "set `result` in an env var and check it later" fails (Exam 4 · Q6).
- Deleting the function before the test, or adding `waitFor`, doesn't fix cleanup after a failure (Exam 4 · Q6).
- Copying files to or from Cloud Storage for a source-editing step adds overhead and sync problems (Exam 1 · Q1), (Exam 5 · Q23).
- Instance metadata is for small configuration values, and a curl POST/GET to a separate web server is pointless complexity (Exam 5 · Q23).
- A new project per build is slow and hits quota and org-permission problems. One shared Spanner instance causes race conditions. The emulator doesn't measure performance (Exam 4 · Q52).
- Pub/Sub → App Engine "build service" chains are extra moving parts (Exam 3 · Q48).

---

## 5. Vulnerability and security scanning

### Key facts

- **Artifact Registry + the Container Scanning API (Container Analysis)** scans images automatically when they are pushed for OS-package CVEs. It is managed and doesn't slow developers down (Exam 1 · Q6), (Exam 1 · Q49), (Exam 2 · Q11).
- Older items name **Container Registry vulnerability scanning** for the same need (Exam 2 · Q6).
- **Web Security Scanner** (older name: Cloud Security Scanner) scans running web apps on App Engine, GKE or Compute Engine for XSS and outdated or vulnerable libraries (Exam 1 · Q20), (Exam 1 · Q58).

### Which security tool?

| Tool | What it does | Is it a scanner? |
|---|---|---|
| Container Scanning / Artifact Analysis | CVEs in container image packages | Yes, for images |
| Web Security Scanner | XSS, injection and vulnerable libraries in a deployed web app | Yes, for apps |
| Cloud Armor | WAF and DDoS protection, IP allow/deny | No (Exam 1 · Q20), (Exam 1 · Q58) |
| Binary Authorization | Enforces attestations at deploy time | No, it consumes scan results (Exam 2 · Q11) |
| Error Reporting / Debugger | Error aggregation and debugging | No |

### Decision rules

- Scan images inside the pipeline without disrupting other teams: **enable Container Scanning in Artifact Registry**. Don't use Docker Hub, an external Aqua instance, or Binary Authorization alone (Exam 2 · Q11).
- Know about OS vulnerabilities before each daily deploy: **enable Container Analysis, store images in Artifact Registry, review the results before deploying** (Exam 1 · Q6).
- Check a web app for XSS or known-vulnerable libraries: use **Web Security Scanner** (Exam 1 · Q58).

### Traps

- A Cloud Run service or Cloud Function that scans *code* on check-in misses vulnerabilities in the image's dependencies (Exam 1 · Q49), (Exam 2 · Q6).
- Banning non-commercial base images is policy, not scanning. Cloud Monitoring on Cloud Build output is not CVE scanning (Exam 1 · Q49), (Exam 2 · Q6).
- Calling the scanner through gcloud or REST for each image is less integrated than automatic scanning on push (Exam 1 · Q6).

---

## 6. Load and performance testing

### Key facts

- Google's reference pattern is **distributed load testing on GKE**: Locust or JMeter in pods, scaled out by adding pods (Exam 1 · Q9), (Exam 2 · Q2).
- During a load test, **Cloud Trace** shows where time goes across services and databases (Exam 1 · Q9), (Exam 6 · Q10).
- For JMeter results analysis, the bank keys **log sink → BigQuery → Looker Studio** (Exam 4 · Q48).

### Decision rules

- Load test that must autoscale to thousands of reads and writes per second and find bottlenecks: **GKE + Locust or JMeter, analyzed in Cloud Trace** (Exam 1 · Q9).
- REST APIs on Cloud Run, Google best practice: a **distributed load-testing framework on a private GKE cluster, scaled with more pods** (Exam 2 · Q2).
- Bottlenecks across several microservices on Cloud Run under load: **enable Cloud Trace and review request timings** (Exam 6 · Q10).
- JMeter orchestration with a Compute Engine instance as the only load generator: **sink to BigQuery, visualize in Looker Studio**. Cloud Storage and Looker are distractors (Exam 4 · Q48).
- Performance tests against Spanner: use a **real, ephemeral instance per build** (Exam 4 · Q52).

### Traps

- cURL on managed or unmanaged instance groups scales poorly. Load generators launched one after another in Cloud Shell are resource-limited (Exam 2 · Q2).
- Cloud Tasks with Cloud Scheduler is not a load-testing tool. VPC Flow Logs are too coarse. Apache Bench on a LAMP VM is limited (Exam 1 · Q9).
- Building custom timing into responses or logs, or Prometheus latency metrics, is weaker than tracing for end-to-end bottlenecks (Exam 6 · Q10).

---

## 7. Logging, Error Reporting and live debugging

### Key facts

- On **Cloud Run, anything written to stdout or stderr goes to Cloud Logging automatically**. Use your language's normal logger. No client library or log files are needed (Exam 4 · Q3).
- On **GKE**, writing **single-line JSON to stdout** makes the logging agent ingest each line as a **structured log** (`jsonPayload`), with no Logging API code needed (Exam 5 · Q24).
- A **log sink to BigQuery** exports logs for SQL analytics (Exam 5 · Q24).
- **Error Reporting** reads from Cloud Logging. For Cloud Run, make sure errors are written to **stderr** (Exam 4 · Q55).
- Raising the **log level to DEBUG or INFO** during local reproduction gives the most diagnostic detail (Exam 2 · Q26).
- **Logpoints** (the legacy Stackdriver or Cloud Debugger feature) inject log statements into running code without redeploying. **Snapshots** capture state and variables at a single moment (Exam 4 · Q9).

### Decision rules

- App writes logs to local files on Cloud Run: **switch to stdout and stderr**. Don't use the logging library, cron jobs that copy to Cloud Storage, or public URLs (Exam 4 · Q3).
- Java errors missing from Error Reporting on Cloud Run: **check that they go to stderr** (Exam 4 · Q55).
- Standardize log data across GKE services: **single-line JSON on stdout as structured logs**, plus (per the bank's key) **a log export to BigQuery** for analytics (Exam 5 · Q24).
- Ongoing code-level diagnosis with no redeploy: the bank's key is **Debugger logpoints** (Exam 4 · Q9). The product has been retired; see the questionable-answers section.

### Traps

- The Cloud Logging client library works, but it is "more code to maintain" than stdout (Exam 4 · Q3), (Exam 5 · Q24).
- Pub/Sub + Dataflow pipelines to standardize logs are overbuilt. Exporting to Cloud Storage is for archiving, not analytics (Exam 5 · Q24).
- Cloud Monitoring client libraries and storage buckets have nothing to do with Error Reporting (Exam 4 · Q55).
- Trace and Monitoring show latency and health, not why the code misbehaves (Exam 4 · Q9).

---

## 8. Distributed tracing with Cloud Trace

### Key facts

- Instrument microservices with **OpenTelemetry**, export spans to **Cloud Trace**, and use Trace analysis reports to find slow HTTP requests (Exam 3 · Q11).
- OpenTelemetry instruments the **application code** itself, producing traces, metrics and logs, including timing for calls to **third-party APIs** (Exam 5 · Q51).
- Trace samples requests. Sending the **`X-Cloud-Trace-Context` header with the right parameters** forces a specific request to be traced (Exam 2 · Q28).
- For backends spread across clouds, a **Zipkin collector** gathers spans and **Cloud Trace** (the old Stackdriver Trace) produces latency reports (Exam 2 · Q48).
- Trace measures **request latency**. It doesn't show CPU or memory per function (Exam 3 · Q16), (Exam 2 · Q17).

### Decision rules

- Slow URLs in a GKE microservices app: use **OpenTelemetry → Cloud Trace → analysis report**. Don't use workload metrics dashboards, STDOUT log filters, or tcpdump with Wireshark (Exam 3 · Q11).
- A specific request must always be traced: **add the `X-Cloud-Trace-Context` header**. Don't wait, run a script, or add custom attributes (Exam 2 · Q28).
- Intermittent slowness in an app with **no metrics** that calls third-party APIs: **add the OpenTelemetry library** to the code. Don't pick the Ops Agent, Managed Service for Prometheus, or header propagation alone (Exam 5 · Q51).
- Network latency across clouds: use **Zipkin collector + Trace**, not Fluentd, Debugger or Profiler (Exam 2 · Q48).

### Traps

- Custom attributes add context but **don't guarantee** that a request is sampled (Exam 2 · Q28).
- Fluentd is for logs, not traces (Exam 2 · Q48).
- Propagating `X-Cloud-Trace-Context` only links spans. It doesn't instrument an app that has no telemetry. The Ops Agent and Prometheus collect metrics but don't explain per-call latency in the code (Exam 5 · Q51).

---

## 9. Profiling with Cloud Profiler

### Key facts

- **Cloud Profiler** continuously samples CPU and memory (heap) in production with low overhead. It shows **flame graphs** at function or method level (Exam 1 · Q28), (Exam 2 · Q17), (Exam 4 · Q53).
- Enabling it means adding the Profiler package or agent and starting it. The code changes are minimal (Exam 4 · Q46), (Exam 1 · Q33).

### Profiler vs Trace vs Debugger vs Logging

| Question in the stem | Tool |
|---|---|
| "Which **functions** use the most CPU or memory?" | **Profiler** (Exam 1 · Q28), (Exam 2 · Q17), (Exam 4 · Q53) |
| "Slower in production than locally; find the time-consuming functions" | **Profiler** (Exam 1 · Q33), (Exam 4 · Q46) |
| "**Performance and resource utilization** of a Java microservice" | **Profiler** (Exam 3 · Q16) |
| "Which **request or service hop** is slow?" | **Trace** (Exam 3 · Q11), (Exam 6 · Q10) |
| "Inspect variables or state at a point in the code" | Debugger snapshot (legacy) (Exam 4 · Q9) |

### Decision rules

- The word "function", "method", "CPU", "memory" or "flame graph" in the stem points to **Profiler** (Exam 2 · Q17), (Exam 4 · Q53).
- Performance gap between local and Compute Engine: **Profiler first**, before Debugger, extra logging or a support ticket (Exam 1 · Q33), (Exam 4 · Q46).

### Traps

- SSH + `top` shows processes, not functions. Monitoring dashboards are too high-level. A Fluent Bit daemonset plus log analysis is indirect (Exam 1 · Q28).
- Print statements or log-timestamp scripts are manual and imprecise (Exam 4 · Q53), (Exam 2 · Q17).
- OpenTelemetry tracing or OpenCensus metrics measure latency, not resource use per method (Exam 3 · Q16), (Exam 4 · Q53).

---

## ⚠️ Questionable answers

| Item | Issue |
|---|---|
| **(Exam 4 · Q47)** | Keys feature branches + **change advisory board** approval as "Google-recommended". Google's DORA research recommends **trunk-based development** with small daily merges and finds heavyweight CAB approval slows delivery without improving stability. Option III (daily merge to main) fits DORA better. The key also contradicts (Exam 4 · Q28). |
| **(Exam 4 · Q9)** | Keys **Stackdriver Debugger logpoints**. Cloud Debugger was shut down in 2023, and its successor Snapshot Debugger is archived and unsupported. On today's exam, prefer structured logging or Trace/Profiler options. Treat Debugger answers (also Exam 2 · Q17 option I) as legacy. |
| **(Exam 2 · Q6)**, **(Exam 1 · Q40)** | Key on **Container Registry**. Container Registry is deprecated and replaced by **Artifact Registry**, which also covers scanning (Exam 2 · Q11) and central repositories. If both appear, choose Artifact Registry. |
| **(Exam 3 · Q37)** | Keys "hand out a kubeconfig file". GKE docs recommend each developer run `gcloud container clusters get-credentials` (which writes contexts to their own kubeconfig) and switch with `kubectl config use-context`. Sharing a credentials file is weaker practice. The claim that gcloud is an "extra dependency" is also wrong, because GKE authentication uses the gcloud auth plugin. |
| **(Exam 2 · Q51)** | "Swiftly pinpoint bugs" with fast developer feedback usually means building and testing on **every commit or push**. Git tags usually mark releases. The real lesson is Cloud Build (CI) over Spinnaker (CD). |
| **(Exam 4 · Q48)** vs **(Exam 2 · Q2)**, **(Exam 1 · Q9)** | Exam 4 calls JMeter on a single Compute Engine VM "recommended practice", but the other two items key distributed load generation on GKE as the Google pattern. The explanation's claim that Looker Studio is preferred over Looker "for BigQuery integration" is also unsupported. |
| **(Exam 4 · Q6)** | The answer is fine, but the explanation's reasoning is muddled. The actual reason IV fails is that env vars don't persist across steps. Cloud Build also has `allowFailure` and `allowExitCodes` on steps today, which would be a cleaner design if offered. |
| **(Exam 4 · Q55)** | stderr routing is necessary, but Error Reporting also needs the **stack trace or error format** to group an error. Rejecting "log exceptions properly instead of System.out.println" (D) as irrelevant overstates the case. |
| **(Exam 2 · Q48)**, **(Exam 3 · Q16)** | Old names: Stackdriver Trace is now **Cloud Trace**, and OpenCensus has been merged into **OpenTelemetry**, which is the current instrumentation path. Zipkin ingestion is legacy. |
| **(Exam 1 · Q20)**, **(Exam 3 · Q51)**, **(Exam 1 · Q6)** | Renamed products: Cloud Security Scanner is now **Web Security Scanner**, Migrate for Anthos is now **Migrate to Containers**, and Container Analysis is now **Artifact Analysis**. Also, (Exam 1 · Q6)'s explanation says option III lacks review "before each deployment" when it clearly includes that review. The difference between options is trivial. |
| **(Exam 5 · Q2)** | Keys `$(gcloud beta emulators pubsub env-init)` and rejects option IV (export `PUBSUB_EMULATOR_HOST`) with a false claim that IV "doesn't mention" the variable. `env-init` only prints the `export PUBSUB_EMULATOR_HOST=...` line, so both options are valid and (Exam 4 · Q21) keys IV. Either works on the exam; pick whichever is offered. |
| **(Exam 5 · Q24)** | "Select two" for *standardizing* logs, but exporting to BigQuery (I) is analytics, not standardization. The structured-JSON-on-stdout part (III) is solid. Expect I as the bank's second answer, but don't treat "BigQuery export standardizes logs" as a rule. |
| **(Exam 5 · Q37)** | Says it pushes to **Artifact Registry**, but every image path is `gcr.io/...` (Container Registry style). Real Artifact Registry paths look like `REGION-docker.pkg.dev/PROJECT/REPO/IMAGE`. The `cloudbuild.yaml` + `gcloud builds submit` pattern is right; `gcloud builds submit --tag` (or an `images:` field) would also work. |
| **(Exam 5 · Q56)** | The stem asks to "eliminate unnecessary steps", but no option removes one. `--cache-from` speeds up the build, but only works if the cached image is pulled first (or BuildKit inline cache is used). The explanation's example skips the pull. |
| **(Exam 4 · Q28)**, **(Exam 3 · Q48)** | They justify **Cloud Source Repositories** as the IAM-auditable choice. CSR is closed to new customers. Current guidance is GitHub, GitLab or Bitbucket connected to Cloud Build (or Secure Source Manager). |

---

## Last-minute cheat sheet

- No local code on a public PC: **Cloud Shell + editor + PR** (Exam 1 · Q45).
- VS Code or IntelliJ with GKE: **Cloud Code**. Secure VPC dev environments with custom tools: **Cloud Workstations + centrally managed images rebuilt weekly** (Exam 3 · Q18), (Exam 4 · Q38).
- Trunk-based development means fewer merge conflicts (Exam 4 · Q28).
- Pub/Sub local testing: gcloud emulator + **`PUBSUB_EMULATOR_HOST`** (or `env-init`, which sets it) (Exam 4 · Q21), (Exam 5 · Q2).
- Local app to Cloud SQL, encrypted + IAM: **Cloud SQL Auth Proxy locally, connect to localhost** (Exam 5 · Q7).
- Pub/Sub ordering unit tests: **emulator**, not mocks (Exam 2 · Q54). Sensitive data: **predefined test messages**, never production replay (Exam 2 · Q58).
- Cheap and fast MVP testing: **emulators locally, then deploy** (Exam 4 · Q8).
- Cloud Function with a Storage trigger: **Functions Framework locally** (Exam 3 · Q38).
- Local K8s that mirrors prod with auto-rebuild: **Minikube + Skaffold** (Exam 3 · Q60).
- No Dockerfile: **`pack build`** or **`gcloud run deploy --source`**. Java: **Jib** (Exam 1 · Q59), (Exam 3 · Q51).
- Faster Cloud Build: **higher-CPU machine type + `--cache-from`** (Exam 1 · Q7), (Exam 3 · Q50), (Exam 5 · Q56).
- Missing tool in Cloud Build: **custom builder image** (Exam 2 · Q20).
- CI on every commit with minimal ops: **Cloud Build trigger** (Exam 3 · Q48).
- Tests then auto-deploy in the same Cloud Build run (Exam 1 · Q3). **Separate steps** per test type (Exam 3 · Q8).
- Steps share **`/workspace`**: pass files between steps there. Commit generated changes back to the repo (Exam 1 · Q1), (Exam 5 · Q23).
- Cleanup even on failure: write results to a **file**, exit 0, clean up, then a final step checks the file (Exam 4 · Q6).
- Concurrent Spanner perf tests: an **ephemeral Spanner instance per build**. The emulator ≠ performance (Exam 4 · Q52).
- Central registry: **ops project + IAM grant to the Cloud Build SA**, no keys in the repo (Exam 1 · Q40).
- Image CVEs: **Artifact Registry + Container Scanning API** (Exam 2 · Q11), (Exam 1 · Q49).
- XSS or vulnerable libraries in a running app: **Web Security Scanner**. Cloud Armor is a WAF, not a scanner (Exam 1 · Q58), (Exam 1 · Q20).
- Load test: **Locust or JMeter on GKE, scaled with pods**, analyzed in **Cloud Trace** (Exam 1 · Q9), (Exam 2 · Q2), (Exam 6 · Q10).
- Cloud Run logs: **stdout/stderr**. Errors in Error Reporting: **stderr**. GKE structured logs: **single-line JSON on stdout** (Exam 4 · Q3), (Exam 4 · Q55), (Exam 5 · Q24).
- Force a trace: **`X-Cloud-Trace-Context` header** (Exam 2 · Q28). Slow URLs across microservices, or an uninstrumented app: **OpenTelemetry → Trace** (Exam 3 · Q11), (Exam 5 · Q51).
- Which function burns CPU or memory: **Cloud Profiler flame graph** (Exam 2 · Q17), (Exam 4 · Q53), (Exam 1 · Q28).
- Slower in the cloud than locally: **Profiler** first (Exam 1 · Q33), (Exam 4 · Q46).
