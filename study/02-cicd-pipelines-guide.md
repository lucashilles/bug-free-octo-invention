# Domain 2 Study Guide — Building and Implementing CI/CD Pipelines

> Condensed from the 86-question bank in [`02-cicd-pipelines.md`](02-cicd-pipelines.md). Citations look like (Exam N · QM). ❌ marks a question you missed.

## Contents

1. [Cloud Build: triggers, config, performance](#1-cloud-build-triggers-config-performance)
2. [Pipeline identity and IAM](#2-pipeline-identity-and-iam)
3. [Pipeline design, testing stages and delivery process](#3-pipeline-design-testing-stages-and-delivery-process)
4. [Cloud Deploy](#4-cloud-deploy)
5. [Artifact Registry and image references](#5-artifact-registry-and-image-references)
6. [Deployment strategies](#6-deployment-strategies)
7. [Cloud Run revisions and traffic](#7-cloud-run-revisions-and-traffic)
8. [Secrets management](#8-secrets-management)
9. [Supply-chain security: Binary Authorization and Artifact Analysis](#9-supply-chain-security-binary-authorization-and-artifact-analysis)
10. [Terraform and IaC in pipelines](#10-terraform-and-iac-in-pipelines)
11. [Jenkins, Spinnaker and other third-party tools](#11-jenkins-spinnaker-and-other-third-party-tools)
12. [⚠️ Questionable answers](#️-questionable-answers)
13. [Last-minute cheat sheet](#last-minute-cheat-sheet)

---

## 1. Cloud Build: triggers, config, performance

### Key facts

- **Trigger event types** you need to tell apart:
  - **Push to a branch**: runs automatically when a commit lands on the matching branch, such as `main`. (Exam 2 · Q2)
  - **Push new tag**: takes a regex on the tag name, so `\d+\.\d+\.\d+` matches only semver release tags. `.*` would also match dev tags. The tag has to be *pushed* to GitHub, because a local tag does not fire the trigger. (Exam 3 · Q1)
  - **Pull request**: runs on every PR open or update, and the result shows on the PR before reviewers approve. That makes it the gate for "test every change before it is accepted". (Exam 4 · Q32)
  - **Included files filter**: limits which changed files fire the trigger (monorepo or per-module scoping). It has **nothing to do with approval**. (Exam 2 · Q2, Exam 4 · Q32)
  - **Trigger approval**: the build is *submitted* automatically but stays pending until a principal with `roles/cloudbuild.builds.approver` approves it. `roles/cloudbuild.builds.editor` does **not** include the approve permission. (Exam 3 · Q38)
- **Substitutions**: `$TAG_NAME` holds the Git tag on trigger-invoked builds, so you can put it in the image name. (Exam 1 · Q35)
- **Parallel steps (`waitFor`)**: a step with no `waitFor` waits for *all previous steps*. To run steps concurrently, give **every** independent step `waitFor: ['-']`, and give the dependent step `waitFor: [foo, bar]`. Putting `['-']` on the first step only changes nothing. (Exam 4 · Q2)
- **Build notifications**: Cloud Build publishes every build state change to the **`cloud-builds` Pub/Sub topic**. A **push subscription** POSTs those messages to a webhook with no code. (Exam 1 · Q49, Exam 5 · Q2 ❌)
- **Speeding up builds**:
  - Docker builds: pull the previous image from Artifact Registry and pass it with `--cache-from`. Put frequently changing files (app source) **late** in the Dockerfile and stable inputs (dependency manifests) early. (Exam 3 · Q60)
  - Other intermediate artifacts: cache them in **Cloud Storage** between builds. It is cheap and low effort. (Exam 2 · Q54)
- **Private pools**:
  - Use a private pool **connected to your VPC** when tests must reach private APIs and the traffic must stay private. Creating the pool alone does *not* connect it to your VPC. (Exam 3 · Q14)
  - Use a private pool plus a dedicated service account for schema migrations against a private-IP AlloyDB. Watch for **non-transitive VPC peering**. (Exam 3 · Q16)
  - Use private pools with **VPC Service Controls** to prevent data exfiltration and keep builds off public IPs at scale. (Exam 5 · Q61)
- **Cloud Build is for builds, not recurring batch jobs.** A scheduled decrypt-and-load job belongs in a **Cloud Run job** with a scheduler. (Exam 3 · Q48)
- **The pipeline broke right after a YAML change that is in Git**: `git diff` the previous and current config. Do not abandon CI, switch registries, or point Error Reporting at a YAML file, because Error Reporting only handles app exceptions. (Exam 1 · Q15)

### Decision rules

| If the question says… | Choose |
|---|---|
| "Build automatically on main, and a change-control team must approve pushes to main" | Push-to-branch trigger on `main` **plus GitHub branch protection** (Exam 2 · Q2) |
| "Every new tag builds automatically, but execution waits for group X" | Tag trigger with **required approval**, give group X `cloudbuild.builds.approver`, give the build SA `artifactregistry.writer` (Exam 3 · Q38) |
| "Apply Terraform when a release (semver tag) is ready" | **Tag** trigger with regex `\d+\.\d+\.\d+` (Exam 3 · Q1) |
| "Test every change before it's accepted / feature branches continuously" | **PR trigger**, scoped to the module folder (Exam 4 · Q32) |
| "Send build info to a 3rd-party webhook, minimal effort" | Pub/Sub **push subscription on `cloud-builds`** (Exam 1 · Q49, Exam 5 · Q2) |
| "Faster builds, low cost/effort" | **Caching** (`--cache-from` for Docker, GCS for other artifacts), not a bigger machine (Exam 2 · Q54, Exam 3 · Q60) |
| "Two independent steps should run concurrently" | `waitFor: ['-']` on **both**, and the dependent step waits on their ids (Exam 4 · Q2) |
| "Tests must reach private VPC APIs privately, low ops" | **Private pool** peered to the VPC (Exam 3 · Q14) |

### Traps

- **"Approve" in the stem does not always mean Cloud Build approval.** If the approval is about *pushes to a branch*, it belongs to source control (branch protection). Cloud Build approval adds a manual step to *every build*. (Exam 2 · Q2)
- **A bigger `machineType` is the speed trap.** It costs much more per minute and does not parallelize sequential steps. (Exam 2 · Q54, Exam 4 · Q2)
- **Splitting work into more steps does not reduce total time,** because steps run sequentially by default. (Exam 2 · Q54)
- **A "final step that POSTs to the webhook" still means writing custom code,** and it never runs for failed builds. (Exam 1 · Q49)
- **Branch-push triggers with a semver regex match *branch* names, not tags.** (Exam 3 · Q1)

---

## 2. Pipeline identity and IAM

### Key facts

- **`kubectl` builder deploying to GKE**: grant `roles/container.developer` to the **existing Cloud Build service account**. You cannot "specify a role in `cloudbuild.yaml`", and you don't need a new SA or a credential-fetch step. (Exam 1 · Q19)
- **Cloud Deploy access to one pipeline only**: apply a policy file binding `roles/clouddeploy.developer` **on that delivery pipeline** (`gcloud deploy delivery-pipelines set-iam-policy`). Don't grant broadly and then deny, don't use `automations.*` permissions, and remember that a *target* is not a *pipeline*. (Exam 3 · Q6)
- **Terraform state bucket 403 during `init`**: grant `roles/storage.objectAdmin` **on that bucket only**. Not project Owner, not local state, and don't create a new bucket, because a 403 means access was denied, not that the bucket is missing. (Exam 4 · Q24)
- **Terraform running on Jenkins on a GCE VM**: use the VM's **attached service account** through ADC and the metadata server. No JSON key in `GOOGLE_CREDENTIALS`, and no `gcloud auth application-default login`, which is for humans. (Exam 4 · Q49)
- **Pipeline component in GKE that signs with a KMS key**: use **Workload Identity**, not an SA JSON key stored as a Kubernetes Secret. (Exam 4 · Q30)
- **"No static credentials and no federation with external IdPs"**: use Cloud Build's own SA. That rules out GitHub Actions with an SA key, an SSH deploy key, *and* Workload Identity Federation for GitHub. (Exam 3 · Q38)
- **AlloyDB migration**: use a dedicated SA registered as an IAM database user, with the needed PostgreSQL grants. An IAM role alone does not grant DB privileges. (Exam 3 · Q16)

### Decision rules

- **On Google Cloud:** use the workload's attached or managed identity, scoped to the exact resource, with a role that matches the work.
- **Least privilege:** a **resource-scoped** role always beats `roles/owner`, even though Owner "works". (Exam 4 · Q24)
- **"Keyless" can still mean federation.** Read the constraints carefully. (Exam 3 · Q38)

---

## 3. Pipeline design, testing stages and delivery process

### Key facts

- **Canonical container pipeline for trunk-based development**:
  1. Cloud Build runs **unit tests on push**.
  2. Build the image **once** and push it to a central registry.
  3. Deploy *that* image to a test environment and run **integration and acceptance tests**.
  4. Deploy to prod and run **smoke tests**. (Exam 2 · Q21 ❌, Exam 5 · Q25)
- **Git hooks are not a pipeline gate.** Client-side hooks aren't cloned and can be bypassed. (Exam 2 · Q21)
- **Rebuilding for prod after the tests** means the artifact you ship is not the one you tested. (Exam 2 · Q21)
- **Shortening MTTR** (choose two): **blue/green** through a CD server (rollback becomes a traffic switch) plus a **CI server running unit tests on every commit**. Local integration tests are not enforced. (Exam 1 · Q42)
- **Replacing a CAB without hurting delivery** (DORA): **peer review at check-in backed by automated tests** plus **fast feedback** to developers. A senior manager approver, self-merge without review, or bigger batches all lose. (Exam 2 · Q28)
- **A runtime config failure** (missing env var) needs an **integration test that starts the container with its real config**. Canary, static analysis and audit logs don't catch it. (Exam 4 · Q17)
- **Concurrent feature branches breaking a shared Dev cluster**: build per feature branch and deploy into a **dynamic namespace per branch** (Config Sync) in the autoscaling Dev cluster, then delete it afterwards. A cluster per branch is costlier. (Exam 4 · Q8)
- **Reducing toil and duration in Cloud Deploy** (choose two):
  - **Automate the low-risk dev→test promotion approval.**
  - **Notify the team the moment a manual step is reached.**
  - Not: scripting pipeline creation (a one-time task), more engineers, or smaller steps. (Exam 4 · Q51, Exam 5 · Q31)
- **API versioning lifecycle**: introduce the new version, announce deprecation, contact the remaining users, give best-effort support, then deactivate. (Exam 5 · Q50)
- **Unreliable synchronous dependency with a tight SLO**: a **circuit breaker plus fallback** (store the data in a DB). Retries eat the latency budget, and a bigger queue just adds latency. (Exam 3 · Q8)

### Traps

- **Acceptance tests *after* the production deploy** make customers the test audience. Option C in Exam 2 · Q21 differs from D only in that last step.
- **Rollback capability is recovery, not an approval process.** (Exam 2 · Q28)
- **Post-merge tests can't gate acceptance.** (Exam 4 · Q32)

---

## 4. Cloud Deploy

### Key facts

- **What it does**: models a **delivery pipeline** across ordered **targets** and manages releases and rollouts. A **rollback** is a new rollout of a previously successful release. (Exam 3 · Q20)
- **Manual QA before any prod traffic, no automated tests**: **two stages (QA, then Prod) with the standard strategy**, and `requireApproval: true` on the prod target. The approval is what enforces "QA done". (Exam 3 · Q12)
- **Risky release with automatic rollback**: a **canary strategy** with phases (for example 5%, then more), **verification / deploy analysis on Cloud Monitoring telemetry**, and an automation rule that **rolls back on failed verification**. "Automatic" means no human runs `rollout undo`. (Exam 3 · Q35)
- **Per-environment differences with otherwise identical manifests** (2 vs 5 replicas): in `skaffold.yaml`, use **multiple profiles (one per target)**, each pointing at a **Kustomize overlay** over a shared base. (Exam 3 · Q47)
- **Canary on GKE through a CD pipeline** is the answer when load testing was incomplete. Cloud Deploy manages the Deployment and Service during the canary. (Exam 2 · Q19)
- **Retention**: use **Artifact Registry cleanup policies** (with dry run), not a scheduled Cloud Build delete job or manual deletion. (Exam 3 · Q20)
- **Not for VM images across clouds**: for custom Compute Engine images in a multi-cloud setup, use **Cloud Build + Packer**. Cloud Deploy and kpt are Kubernetes and serverless oriented. (Exam 5 · Q26)

### Decision table: Skaffold manifests for per-target variation (Exam 3 · Q47)

| Option | Result |
|---|---|
| Multiple profiles + `manifests.kustomize` | ✅ Shared base, tiny overlays, one profile per target |
| Single profile + kustomize | ❌ Only one overlay can be active |
| Multiple profiles + `rawYaml` | ⚠️ Works, but duplicates full manifests |
| Single profile + `rawYaml` | ❌ No variation possible |

### Traps

- **Canary is not a substitute for a preceding QA environment.** It still exposes production users. (Exam 3 · Q12)
- **Cloud Deploy does not create the missing tests.** You supply the verification. (Exam 3 · Q20)
- **A dedicated rollback pipeline in Cloud Build** means hand-rolling what Cloud Deploy provides. (Exam 3 · Q20)

---

## 5. Artifact Registry and image references

### Key facts

- **Artifact Registry is the managed registry.** Container Registry is **retired** and **never stored Helm charts**. Artifact Registry Docker repositories are OCI, so they hold images *and* Helm 3.8+ charts, with native GKE, Cloud Run, IAM and VPC-SC integration. (Exam 4 · Q12, Exam 1 · Q10)
- **Repository modes** (Exam 3 · Q34):

| Mode | What it does | Caches upstream? |
|---|---|---|
| Standard | You push artifacts | No, uploads are manual |
| **Remote** | Proxies an upstream (Docker Hub and so on) and caches on first pull | **Yes** |
| **Virtual** | One endpoint fronting several repos (routing only) | No, not by itself |

  "Cache every dependency + single endpoint + low effort" → **remote repos fronted by one virtual repo**.
- **Location matters for pulls**: `gcr.io` and `us.gcr.io` map to the US multi-region, `eu.gcr.io` to Europe, and `asia.gcr.io` to Asia. Store images **near the cluster that pulls them** (push once, pull often). (Exam 2 · Q58)
- **Tags vs digests**:

| | Tag | Digest (`sha256:…`) |
|---|---|---|
| Mutable? | Yes, it can be moved | No, content-derived |
| Use it to… | **Select a release version** (put `$TAG_NAME` in the image name) (Exam 1 · Q35) | **Pin or roll back to exact bytes** (Exam 4 · Q37) |
| Gotcha | Re-pointing `latest` doesn't change the Pod spec, so no rollout happens (Exam 4 · Q37) | Known only after the push, so you can't match it to a Git tag (Exam 1 · Q35) |

- **Roll back to a known-good image** by referencing its **digest**. Rebuilding from an old Git tag gives a *different* artifact. (Exam 4 · Q37)
- **Registry events**: Artifact Registry publishes to the **`gcr` Pub/Sub topic** on upload, tag and delete. A deploy tool's **native Pub/Sub trigger** (Spinnaker) is the low-effort "deploy on new image". (Exam 1 · Q43)
- **Who pushed an image?** Enable Artifact Registry **Data Write audit logs** and look at `Docker-PutManifest` and the caller identity. (Exam 3 · Q15)

---

## 6. Deployment strategies

### Comparison table

| Strategy | Real users exposed? | Rollback | Use it when the stem says… | Cite |
|---|---|---|---|---|
| **Recreate** | All, with downtime | Slow redeploy | (almost never the answer) | Exam 2 · Q22 |
| **Rolling update** | Gradually all | Roll back through the fleet (`kubectl rollout undo`), mixed versions | Default K8s, no special need | Exam 2 · Q22, Q30 |
| **Partitioned rolling update** (StatefulSet `partition`) | Pods with ordinal ≥ partition | Raise or lower the partition | "Phased rollout to **half the pods**" | Exam 2 · Q39, Exam 5 · Q19 ❌ |
| **Blue/green** | All, at cutover | **Instant**: switch traffic back, the old version is still running | "**Instant** rollback", "simplify releases", "shortest rollback" | Exam 2 · Q22, Q30, Exam 1 · Q42 |
| **Canary** | **Small %**, growing on evidence | Shift traffic back | "Not fully load-tested", "progressively widen exposure", "limit blast radius" | Exam 2 · Q19, Q22, Exam 5 · Q58 |
| **A/B testing** | A defined segment, by condition | — | Comparing variants for user segments (experimentation) | Exam 2 · Q22, Q30 |
| **Shadow** | **None**, a mirrored copy of full traffic | N/A | "**Full production load before launch**" | Exam 4 · Q21 |

### Key facts and rules

- **Blue/green answers *how fast you can undo*; canary answers *how many users you risk*.** You can combine them, for example blue/green deployment with canary testing. (Exam 2 · Q22)
- **Blue/green on GKE** = two Deployments plus one Service.
  - **Rollback = change the Service selector back** to the old version (for example `version: blue`). This also keeps the failing Deployment intact for debugging.
  - Not `kubectl rollout undo` (that's for rolling updates), not scaling green to zero, and not deleting the image. (Exam 4 · Q59, Exam 5 · Q29, Exam 5 · Q52)
- **Canary analysis baseline** (Spinnaker/Kayenta): compare against a **freshly created deployment of the *current* production version**, started at the same time. Long-running prod has warm caches, which skews the comparison. (Exam 1 · Q45)
- **Header- or attribute-based routing plus arbitrary % splits** (Android user-agent → Android microservice): **GKE + Cloud Service Mesh VirtualService** (headers decide *who*, weights decide *how many*). (Exam 2 · Q36, Exam 5 · Q21 ❌)
  - Cloud Run splits only by revision %.
  - App Engine splits by IP or cookie.
- **Urgent security patch on a global GCE fleet**: a **short canary in the MIG updater, then a full rollout**. All-at-once is too risky, overnight regional rolls are too slow, and duplicating the fleet costs too much. (Exam 5 · Q58)
- **Validate MIG changes without losing capacity**: set autoscaling to **"Only scale out"** during the change. (Exam 5 · Q56)

### Traps

- **"Instantly revert" means blue/green, not canary.** Canary is about gradual exposure. (Exam 2 · Q30)
- **Blue/green that switches *all* traffic and only then watches metrics** exposes everyone. Untested load means canary. (Exam 2 · Q19)
- **A rolling update is not a canary.** It does not hold traffic back based on metrics. (Exam 2 · Q19)
- **Pod management policy `Parallel`** controls scaling order, not updates. A **ReplicaSet** can't stop at 50%. **NoExecute taints** evict Pods. (Exam 2 · Q39)
- **Plain Service selectors can't split traffic by percentage.** "Gradually move traffic via the selector" is wrong. (Exam 3 · Q35)

---

## 7. Cloud Run revisions and traffic

| Goal | Command or pattern | Cite |
|---|---|---|
| Developers/QA test a revision **before any customer traffic** | `gcloud run deploy SVC --no-traffic --tag dev`, then test at `https://dev---SVC-xxx.a.run.app` (three hyphens) | Exam 2 · Q5 |
| Test thoroughly in staging *and* prod with minimal consumer impact | Tagged revision with no traffic, test it, then shift traffic progressively. Repeat in prod | Exam 2 · Q29 |
| Canary to ~10% of clients, least effort | Deploy with no traffic, then **traffic split 90/10 between revisions of the same service** | Exam 4 · Q4 |
| Live-traffic test **and** manual QA, with rollback (choose two) | **Tagged `--no-traffic` revision** (QA URL) + **traffic split** (live %). The old revision stays deployed, so rollback is moving traffic back | Exam 4 · Q36 |

**Traps**

- **`--to-revisions LATEST=1`** sends 1% of *customers* to an untested revision. (Exam 2 · Q5)
- **Identity tokens and `run.invoker` don't change routing,** and there is no `.private.run.app` URL. (Exam 2 · Q5)
- **A tag with zero traffic is not private access.** The tagged URL is public if the service is public. (Exam 2 · Q5)
- **10% of requests ≠ 10% of distinct clients.** Session affinity is best effort. (Exam 4 · Q4)
- **A separate service plus a load balancer or app-level forwarding** is extra work for no gain. (Exam 4 · Q4, Q36)

---

## 8. Secrets management

### Cloud KMS vs Secret Manager

| | **Secret Manager** | **Cloud KMS** |
|---|---|---|
| Stores | Secret *values* (API keys, passwords, certs) with versions | Cryptographic *keys* (encrypt, decrypt, sign) |
| Rotation of a secret | Add a new version, with no config to touch | You must re-encrypt and re-embed the ciphertext |
| Use for | Cloud Build `availableSecrets.secretManager`, Cloud Run secrets | Signing keys for attestations (Exam 4 · Q30), imported decryption keys (Exam 3 · Q48) |
| Mnemonic | "An API key is a secret to *store*" (Exam 4 · Q60) | "A key to *manage*" |

### Cloud Build secrets: evolution seen in the bank

1. **Legacy**: Cloud Storage + KMS-encrypted secrets, pipeline granted access via IAM. This was the answer when no Secret Manager option existed. (Exam 1 · Q21, Exam 5 · Q9; see ⚠️)
2. **KMS ciphertext in the build config**: `availableSecrets.inline` plus `secretEnv`, with the build SA granted `cloudkms.cryptoKeyDecrypter`. The top-level `secrets` field is the older legacy form. (Exam 2 · Q45, Exam 3 · Q46)
3. **Recommended**: **Secret Manager**. Grant `roles/secretmanager.secretAccessor` to the build SA and reference the secret under **`availableSecrets.secretManager`**. Rotation needs no config change. (Exam 3 · Q46, Exam 5 · Q65)

### Cloud Run: env var vs volume

| Delivery | When the value is read | Pick it when… |
|---|---|---|
| **Environment variable** | **Once, at instance start**. Google recommends pinning a specific version | Static secret, simplest integration ("store an API key securely") (Exam 4 · Q60, Exam 5 · Q30) |
| **Volume mount (`latest`)** | **On each file read** | Secret **rotates** and the app must always see the current value without redeploying. The app must re-read the file (Exam 3 · Q28, Exam 4 · Q28) |

### Never / traps

- **Never store secrets in Git**, whether plaintext, base64 ("encoding ≠ encryption"), or encrypted with the key in another repo. (Exam 1 · Q21, Exam 3 · Q46, Exam 5 · Q65)
- **Never store the decryption key in the same bucket as the ciphertext.** (Exam 2 · Q45, Exam 3 · Q48)
- **Never prompt humans for secrets at build time,** because it breaks automation. (Exam 1 · Q21, Exam 5 · Q65)
- **Never bake secrets into images or source.** (Exam 4 · Q28)
- **Default GCS encryption at rest ≠ a secret store.** Any authorized reader sees plaintext. (Exam 2 · Q45)
- **The `latest` alias does not make an env var refresh.** (Exam 3 · Q28)
- **Cloud Run already decrypts Secret Manager values,** so "mount, then decrypt in the app" is wrong. (Exam 4 · Q60)
- **Build-time secrets don't provide runtime secrets.** (Exam 3 · Q28)

---

## 9. Supply-chain security: Binary Authorization and Artifact Analysis

### Which control answers which question

| Requirement wording | Control | Why not the others |
|---|---|---|
| "Only trusted/approved images can be **deployed**", "guardrail", "can't bypass testing" | **Binary Authorization** (deploy-time admission) | — (Exam 1 · Q7, Q39, Exam 4 · Q44, Q47, Exam 5 · Q34, Q43) |
| "Only images **from repo X**" | BinAuthz policy with an **allowlist name pattern** (`admissionWhitelistPatterns`) and default deny | Custom builder, manifest checks and tags are bypassable or custom (Exam 1 · Q10) |
| "Only images **built by our Cloud Build**", low effort | Require the **`built-by-cloud-build`** attestor, which Cloud Build creates and signs automatically | Your own KMS keyring and attestor duplicates this (Exam 3 · Q41) |
| "Only images that **passed the load test**" (custom gate) | Pipeline signs an attestation with a **Cloud KMS** key, authenticated via **Workload Identity** | A human signer breaks automation; an SA JSON key breaks keyless auth (Exam 4 · Q30) |
| "**Trace** a running image to source/build" | Cloud Build **signed build provenance** (SLSA L3) stored via Container Analysis API, **verified by BinAuthz** | Scanning ≠ provenance (Exam 3 · Q31) |
| "Find/report **CVEs**", replace VM vuln tools | **Artifact Analysis** (Container Analysis) scanning | Dockerfile linting doesn't see installed packages (Exam 2 · Q50, Exam 5 · Q14) |
| "No critical vulns may **reach the registry**" | Cloud Build + **On-Demand Scanning before push**, failing the build on CRITICAL | Automatic scanning runs *after* push, too late (Exam 3 · Q24) |
| "**Who** can deploy" | IAM / K8s RBAC | Doesn't check *what* runs (Exam 1 · Q7, Exam 4 · Q47) |
| Detect bad behavior in running pods | Falco / Prisma / Twistlock (runtime) | That's shift-right, not a guardrail (Exam 4 · Q47, Exam 5 · Q34) |

### Key facts

- **Binary Authorization is managed and based on the Kritis spec.** Kritis itself is open source and self-operated, so with "low overhead" pick BinAuthz. (Exam 4 · Q44)
- **Supports dry-run, and enforcement events go to Cloud Audit Logs.** (Exam 4 · Q44)
- **Emergency or debug Pod with an unsigned image**: add the label **`image-policy.k8s.io/break-glass: "true"`** to that Pod. It is scoped to one Pod and automatically logged.
  - Not `ALWAYS_ALLOW`, not disabling BinAuthz, and not a permanent allowlist entry. (Exam 3 · Q30)
- **Artifact Analysis behavior** (Exam 3 · Q15):
  - It scans on **push, by digest**. Adding a tag does not rescan.
  - Enabling scanning does **not** retroactively scan existing images. Re-push them.
  - Continuous analysis updates findings, but images must be pulled within **30 days** to stay fresh.
  - Audit logs can't recreate upload records that were never collected.
- **Scanning detects; Binary Authorization enforces.** A scan result can become an attestation that BinAuthz then requires. (Exam 1 · Q39, Exam 4 · Q47)

### Traps

- **Treating an *artifact* problem as an *access* problem** (RBAC, branch protection, a source-IP admission controller). (Exam 1 · Q7)
- **Restricting who can push to Artifact Registry** does not control what GKE runs. (Exam 3 · Q41, Exam 4 · Q44)
- **Web Security Scanner and private clusters** are not image-trust controls. (Exam 1 · Q39)
- **COS nodes and auto-upgrades harden hosts,** not image provenance. (Exam 3 · Q31)

---

## 10. Terraform and IaC in pipelines

- **Replacing an immutable instance template that a MIG uses** (error "already being used by"): add **`lifecycle { create_before_destroy = true }`** on the template, which needs unique names via `name_prefix`. Terraform then creates the new template, repoints the MIG and deletes the old one in **one apply**. (Exam 1 · Q55, Exam 5 · Q53)
  - Wrong answers: destroying the MIG (disruptive), separate pipeline runs (extra executions), and state rm/import (doesn't remove the blocker).
  - `create_before_destroy` does not by itself roll the new machine type out to existing VMs. That depends on the MIG update policy. (Exam 1 · Q55)
- **State backend 403**: give the build SA bucket-scoped `roles/storage.objectAdmin`. Keep remote state, which is shared and lockable. (Exam 4 · Q24)
- **Authentication**: on GCE, use the attached SA through ADC. Avoid SA keys and avoid user ADC login. (Exam 4 · Q49)
- **Triggering**: a semver **tag** trigger to apply releases (Exam 3 · Q1). Run IaC module integration tests on **every PR**, scoped per folder (Exam 4 · Q32).
- **Multi-cloud VM images**: use **Packer** orchestrated by Cloud Build. (Exam 5 · Q26)

---

## 11. Jenkins, Spinnaker and other third-party tools

- **Hosting Jenkins for an app that is entirely on GCP**: use **Compute Engine VMs**. Jenkins needs a persistent controller; Cloud Run functions are time-boxed; on-prem K8s adds a hybrid credential path; workstations are unmanaged. (Exam 2 · Q52, Exam 5 · Q16)
- **Jenkins deployments are slow to *start* while CPU and memory look normal**: **increase the executors** (execution slots) on the agents, not on the controller. (Exam 3 · Q57)
- **Build fleet that must avoid public IPs and exfiltration at scale**: use Cloud Build private pools + VPC-SC rather than Jenkins on VMs (managed, autoscaling). Spot VMs can be preempted. (Exam 5 · Q61)
- **Spinnaker**: a **Pub/Sub trigger** on the `gcr` topic to deploy on each new image (Exam 1 · Q43). **Kayenta** canary analysis against a fresh baseline (Exam 1 · Q45).
- **Kritis vs Binary Authorization**: same idea, but BinAuthz is managed. (Exam 4 · Q44)

---

## ⚠️ Questionable answers

These are graded "correct" in the bank but conflict with other questions or current Google guidance. Know the graded answer, but don't generalize from it.

1. **Exam 1 · Q21 and Exam 5 · Q9: Cloud Storage + Cloud KMS for pipeline secrets.**
   - The answer is the best of the four options offered, but none of them is Secret Manager. Secret Manager is the current recommended store (Exam 3 · Q46, Exam 5 · Q65).
   - Exam 5 · Q9's claim that "Cloud KMS simplifies **secret** rotation" confuses rotating a key with rotating a secret value.
   - Pick GCS+KMS only when Secret Manager isn't offered.
2. **Exam 2 · Q45: KMS-encrypted secrets inline in the build config.**
   - This is valid among its options, but Exam 3 · Q46 calls it higher-maintenance than Secret Manager, because every rotation needs a re-encrypt and re-embed.
   - It is a dated pattern, not the preferred one.
3. **Exam 5 · Q19 ❌: the explanation says partitioned rolling updates are "directly supported within Kubernetes Deployment objects".**
   - That is wrong. `partition` is a **StatefulSet** RollingUpdate field (Exam 2 · Q39 says so explicitly).
   - It also dismisses StatefulSets as "not for phased rollouts", which contradicts where the feature actually lives.
   - The answer letter is right; the reasoning is wrong.
4. **Exam 5 · Q21 ❌: the explanation claims Anthos Service Mesh "does not manage non-GKE VM workloads".**
   - The parallel question (Exam 2 · Q36) rejects the Compute Engine option for a different reason: the option only configures a % split and has no user-agent rule.
   - Rely on the Exam 2 · Q36 reasoning: header routing is the deciding criterion.
5. **Exam 5 · Q30: the explanation says "Cloud Run does not support arbitrary filesystem secret mounts".**
   - Cloud Run *does* mount Secret Manager secrets as volumes (Exam 3 · Q28, Exam 4 · Q28 depend on it).
   - Option II is wrong because of the needless app-side "decrypt" step (Exam 4 · Q60), not because of mounting.
6. **Exam 5 · Q14: the explanation recommends integrating with "Google Container Registry".**
   - Container Registry is retired (Exam 4 · Q12, Exam 1 · Q10).
   - Read "Container Analysis" as today's **Artifact Analysis** on Artifact Registry.
7. **Exam 5 · Q53: the explanation says `create_before_destroy` lets "new ones with the updated machine type spin up", avoiding downtime.**
   - Exam 1 · Q55 explicitly notes that it does **not** guarantee rollout to existing VMs, which depends on the MIG update configuration.
   - It also faults option B for "mixing instance types", which is not the real reason. The real reason is extra pipeline runs.
8. **Exam 5 · Q52: the reasoning against option B ("roll back green") is weak.**
   - It says this "reverts to an outdated version". The stronger reason, consistent with Exam 4 · Q59, is that switching the selector to blue is instant and leaves green intact for developers to debug.
9. **Exam 3 · Q12 and Exam 4 · Q8: the bank's own explanations admit ambiguity.**
   - Exam 3 · Q12: option C (two stages plus canary) is "technically defensible".
   - Exam 4 · Q8: option A's "main-branch merge requests" wording is ambiguous.
   - Choose the simplest option that literally matches the stem.

---

## Last-minute cheat sheet

- "Only trusted/approved/tested images can **deploy**" → **Binary Authorization**. Scanning only *reports*, and IAM/RBAC only controls *who*.
- Images built by Cloud Build → require the **`built-by-cloud-build`** attestor. No custom KMS needed.
- Custom gate attestation → the **pipeline** signs with a **Cloud KMS** key via **Workload Identity**. No humans, no JSON keys.
- Only images from repo X → BinAuthz **allowlist name pattern**.
- Debug Pod with an unsigned image → **break-glass label** on that Pod only.
- Trace an image to source/build → **signed build provenance + BinAuthz verification**.
- Block vulns *before* push → **On-Demand Scanning** in Cloud Build. Automatic scanning runs after push. Enabling it doesn't scan old images, and tags don't trigger rescans.
- Secrets in builds → **Secret Manager** + `availableSecrets.secretManager` + `secretAccessor`. Never Git, base64, or the key next to the ciphertext.
- Cloud Run secret that **rotates** → **volume mount** of `latest`. Static API key → env var is fine.
- API key → **Secret Manager**, not KMS. KMS manages *keys*.
- Webhook on build events → Pub/Sub **push subscription on `cloud-builds`**. Deploy on new image → Pub/Sub **`gcr`** topic.
- Faster builds → **cache** (`--cache-from` + changing files late, or GCS). Not a bigger machine.
- Parallel steps → `waitFor: ['-']` on **every** independent step.
- Release on semver → **tag** trigger `\d+\.\d+\.\d+`. Test before accept → **PR** trigger. Approval of merges → **GitHub branch protection**.
- Auto-submit but wait for a human → trigger **approval** + `cloudbuild.builds.approver`.
- Private VPC APIs, private DBs, or no public IPs → Cloud Build **private pool** (+ VPC peering / VPC-SC).
- Pin or roll back exact content → **digest**. Select a version → **tag** in the image name.
- Cache upstream images through one endpoint → **remote repos + virtual repo**. Retention → **cleanup policies**. Helm + images → **Artifact Registry**.
- Push once, pull often → registry **near the cluster** (`eu.gcr.io` for Europe).
- Instant rollback → **blue/green**. On GKE, rollback = **flip the Service selector**, not `rollout undo`.
- Unproven under load / widen gradually → **canary**. Full prod load with zero users exposed → **shadow**. Half the pods → StatefulSet **partition**.
- Header-based routing + % split → **GKE + Cloud Service Mesh VirtualService**.
- Cloud Run: QA first → `--no-traffic --tag` (URL `tag---svc`). Live % → **traffic split**. Rollback → move traffic back.
- Cloud Deploy: QA then prod → **two stages + `requireApproval`**. Auto rollback → **canary + verification + automation**. Per-env diffs → **profiles + Kustomize overlays**. Access → `clouddeploy.developer` **on the pipeline**.
- Terraform: template in use → **`create_before_destroy`**. State 403 → bucket-scoped **`storage.objectAdmin`**. On a GCE VM → **attached SA** (ADC).
- Jenkins for a GCP app → **Compute Engine VM**. Slow to start with idle CPU → **more executors**.
- Pipeline order: unit tests in CI → build once → push → test env (integration + acceptance) → prod + smoke tests. Git hooks are not gates.
- Replace a CAB → **peer review + automated tests + fast feedback**. Reduce Cloud Deploy toil → **auto-approve dev→test + notify on manual steps**.
