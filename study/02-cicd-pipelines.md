# Domain 2 — Building and Implementing CI/CD Pipelines

86 questions. Answers are collapsed — try each question before expanding it.

## Quick-review: memory hooks

- “Stop untested images from running” → Binary Authorization with the pipeline as attestor; “control who can act” → RBAC; they solve different problems. *(Q1.7)*
- “Only X can be deployed to the cluster” means enforce it at the cluster’s admission boundary (Binary Authorization), not at the build pipeline or with a convention like tagging. *(Q1.10)*
- “It broke right after a specific change, and that change is in version control” → diff the before/after states first, before reaching for unrelated fixes or abandoning the pipeline. *(Q1.15)*
- Authenticating a GCP CI/CD tool to another GCP service is almost always “grant the existing service account the right IAM role” — not a new service account, not a config-file permission, and not manual credential plumbing. *(Q1.19)*
- Secrets for an automated pipeline belong in a centralized, IAM-controlled, encrypted store — never in source control, encrypted or not — because only a dedicated secret-management approach makes both secure automated access and fast rotation possible. *(Q1.21)*
- Push the image under the release tag in its name, because tags select versions and digests only identify content. *(Q1.35)*
- Sign at build and verify at deploy: Binary Authorization admits only images with a trusted attestation. *(Q1.39)*
- To recover faster, make rollback a traffic switch and make every change pass automated tests before it ships. *(Q1.42)*
- Image changed in the registry means a Pub/Sub event, and the least-effort consumer is the deployment tool’s built-in Pub/Sub trigger. *(Q1.43)*
- Compare the canary to a fresh copy of today’s production, not to the instances that have been running for weeks. *(Q1.45)*
- Build events are already published to Pub/Sub, so a push subscription turns them into webhook calls without code. *(Q1.49)*
- For an immutable resource with live dependents: create its replacement, redirect the dependents, then retire the original. *(Q1.55)*
- “GitHub gates who merges, Cloud Build automates what builds” — approval belongs on the branch protection rule, automation belongs on the push trigger. *(Q2.2)*
- Use a revision tag with zero standard traffic allocation to test before routing customers to it. *(Q2.5)*
- Unproven under load means start small and widen on evidence: a canary through an automated pipeline. *(Q2.19)*
- Gates belong in the pipeline, run fast tests first, build once, and never put customers before acceptance tests. *(Q2.21)*
- Blue/green decides how fast you can undo a release; canary decides how many users you risk while testing it. *(Q2.22)*
- Peer review gates the change and fast feedback catches what slips through, with no external gatekeeper. *(Q2.28)*
- On Cloud Run, deploy with no traffic and a tag, test on the tag’s URL, then shift traffic gradually. *(Q2.29)*
- Instant rollback requires the old version to still be running, and only blue/green guarantees that. *(Q2.30)*
- Route by what the request says and by how much with a mesh virtual service, headers for who and weights for how many. *(Q2.36)*
- The partition sets the line: pods at or above that ordinal get the update, and the rest stay put. *(Q2.39)*
- Encrypt with Cloud KMS, reference it in the build config, and let only the build account decrypt. *(Q2.45)*
- VM vulnerability tools scan installed OS packages on a running machine; Artifact Analysis scans installed OS and language packages inside a container image — same goal, container-native mechanism. *(Q2.50)*
- Jenkins needs a persistent server, not a function, and not a separate network — when the application lives in Google Cloud, put Jenkins in Google Cloud, on a VM. *(Q2.52)*
- Don’t pay more compute to go faster — stop redoing the same work. Cache it. *(Q2.54)*
- Push once, pull often: store the image next to the cluster that pulls it. *(Q2.58)*
- When tags mark deployment readiness, match the release-tag convention in the trigger. *(Q3.1)*
- Match the role to the work and attach its binding to the exact resource requiring access. *(Q3.6)*
- An unreliable supporting dependency and a tight response budget suggest a circuit breaker with a safe fallback. *(Q3.8)*
- Validate in QA first, gate production with approval, and choose rollout strategy separately. *(Q3.12)*
- When Cloud Build needs private API access with minimal infrastructure management, choose a VPC-connected private pool. *(Q3.14)*
- Use Artifact Analysis to understand image risk and audit logs to establish upload accountability. *(Q3.15)*
- Private connectivity reaches the database, while a scoped service identity controls migration access. *(Q3.16)*
- Use Cloud Deploy for release progression and rollback, and Artifact Registry policies for retention. *(Q3.20)*
- Build, scan, enforce, then push; use managed build infrastructure to reduce maintenance. *(Q3.24)*
- For Cloud Run password rotation, mount `latest` and reread the file. *(Q3.28)*
- Debug one Pod → break-glass label; change the rules for everyone → anything else. *(Q3.30)*
- Scanning tells you what’s inside an image; provenance plus Binary Authorization tells you where it came from — traceability needs the second one. *(Q3.31)*
- Caching needs a remote repository; one single address for everything needs a virtual repository on top of it — you typically want both together. *(Q3.34)*
- “Automatically rolls back” means the platform decides and acts — if a human has to notice and run a command, it isn’t automatic. *(Q3.35)*
- The trigger submits, the group approves, and the build service account publishes. *(Q3.38)*
- If Cloud Build built it, let Cloud Build attest it — reach for your own Cloud KMS keyring and attestor only when you need to verify something Cloud Build’s built-in attestor doesn’t already cover. *(Q3.41)*
- A ciphertext embedded in the build config has to be re-embedded every time the secret changes; a Secret Manager reference doesn’t. *(Q3.46)*
- Same manifest everywhere except one small per-environment difference → one shared base plus per-target Kustomize overlays, selected by one profile per target. *(Q3.47)*
- Keys go in Cloud KMS, never in the bucket next to what they protect; recurring container jobs go in Cloud Run jobs, not Cloud Build. *(Q3.48)*
- Slow starts with hardware headroom point toward execution-slot availability; slow running tasks require a different diagnosis. *(Q3.57)*
- Reuse the previous image, and place frequently changing inputs late. *(Q3.60)*
- Use `['-']` to start independently and step IDs to wait for prerequisites. *(Q4.2)*
- For a simple Cloud Run canary, split traffic between revisions of the existing service. *(Q4.4)*
- For economical feature testing, give each branch its own namespace before giving it its own cluster. *(Q4.8)*
- Images plus Helm charts, fully managed, native GKE/Cloud Run/IAM/VPC-SC integration → Artifact Registry; Container Registry never did Helm charts and has been retired. *(Q4.12)*
- A runtime configuration failure needs a test that runs the application with its configuration. *(Q4.17)*
- Full production load, zero user exposure, before launch → shadow testing; canary and A/B both actually serve some real users, so neither is “before launch.” *(Q4.21)*
- 403 on the state bucket during backend init → grant roles/storage.objectAdmin on that bucket specifically, not roles/owner on the whole project and not a workaround like local state. *(Q4.24)*
- Secret rotates, app must always have the latest value, no downtime → mount as a Secret Manager volume (read live on each access); environment variables are resolved once at startup and go stale after rotation. *(Q4.28)*
- Automated gate + Google-recommended key practice → Cloud KMS for the signing key, Workload Identity for authentication; a human signer (personal key or not) breaks automation, and a service account JSON key breaks the keyless-authentication practice. *(Q4.30)*
- To test every change before it is accepted, trigger Cloud Build on each pull request and scope the build to the folder being changed. *(Q4.32)*
- Tagged revision with no traffic is for QA, and a traffic split is for live users in limited numbers. The old revision stays deployed, so rollback is just moving traffic back. *(Q4.36)*
- Tags can move and digests cannot, so roll back to the known-good image by its digest. *(Q4.37)*
- For “only trusted images can be deployed” with low overhead, choose the managed deploy-time enforcer, Binary Authorization, and not registry permissions, custom validators, or a self-run open-source tool. *(Q4.44)*
- “Guardrail means gate, not gauge” — if the requirement is to block deployment, think Binary Authorization; if it’s to measure or report risk, think scanning tools like Artifact Analysis. *(Q4.47)*
- “On a GCP VM, let the VM’s own identity do the work — don’t hand Terraform a key it doesn’t need.” *(Q4.49)*
- “Automate the gate you can remove; page the human for the gate you can’t.” *(Q4.51)*
- “Blue/green rollback is a selector flip, not a rollout undo — the old version never left.” *(Q4.59)*
- “An API key is a secret to store, not a key to manage — reach for Secret Manager, not Cloud KMS.” *(Q4.60)*

## Questions

### Exam 1 · Q7

Your organization has moved to a container-based development model. Your team builds many applications that flow continuously through an automated build pipeline into a Kubernetes cluster running in production. The security auditor is worried that a developer or operator could bypass automated testing and push code changes straight to production without the required approval. What should you do to enforce that approval step?

- A. Configure the build system to use protected branches that require pull request approval before merging.
- B. Use an admission controller to verify that incoming requests to the cluster originate from approved sources.
- C. Use Kubernetes Role-Based Access Control (RBAC) to restrict cluster access to only approved users.
- D. Enable Binary Authorization on the Kubernetes cluster, and configure the build pipeline as an attestor.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Enable Binary Authorization on the Kubernetes cluster, and configure the build pipeline as an attestor.

**Correct Answer**

**D. Enable Binary Authorization on the Kubernetes cluster, and configure the build pipeline as an attestor.**

**Exam Reasoning Explanation**

The must-have constraint is specifically about the deploy-time gate: the auditor’s concern is that someone could circumvent automated testing and push an image to the production cluster without the testing/approval pipeline having actually run on it. That means the control needs to be enforced at the point where workloads are admitted to run in the cluster, and it needs to verify that a specific trusted process (the pipeline) actually vetted the image — not just that a person was authorized to act, or that a process was followed earlier upstream. Binary Authorization is purpose-built for exactly this: it blocks deployment of any container image to the cluster unless it carries a cryptographically verifiable attestation from a designated, trusted attestor (here, the build pipeline), closing the gap between “testing happened” and “the tested artifact is what’s actually running.”

**Key Exam Clues**

  * “circumvent automated testing and push code changes to production without approval” is a hard constraint — it specifically calls out bypassing the pipeline’s own gate, not just unauthorized human access.

  * “enforce approvals” at deploy time, into “a Kubernetes cluster in the production environment,” is a technical signal pointing at an admission-time control over the cluster itself, not a source-control or identity-access control upstream of it.

  * “configured as an attestor” (in the correct option) is the decisive mechanism: it ties the approval cryptographically to the pipeline’s own attestation, which is what actually prevents circumvention rather than merely restricting who can act.

**Why This Is Correct**

Binary Authorization enforces deploy-time policy on a Kubernetes cluster by requiring every container image to carry one or more valid attestations, signed by designated attestors, before the cluster’s admission controller will allow it to run. Configuring the automated build pipeline itself as the attestor means an image can only receive the required signature if it has actually passed through that pipeline’s testing and build steps — so even someone with legitimate `kubectl` access can’t deploy an image that skipped the pipeline, because the cluster will reject any unattested image outright. This directly closes the exact gap the auditor raised: it’s not about restricting who can act, but about guaranteeing what gets admitted to run.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Different Use Case:** Protected branches with required pull request approval is a legitimate control, but it operates on source code merges in the version-control system, not on what gets deployed to the cluster. It does nothing to stop someone from building and pushing a container image directly to the cluster outside the normal pipeline, so it doesn’t close the specific circumvention risk described.

  * **Option B — Technically Possible but Not Best:** A generic admission controller that checks the _source_ of incoming requests (e.g., which service account or IP issued the deployment call) addresses _who_ is making the request, but it doesn’t verify that the image itself was actually built and tested by the approved pipeline. A user with a legitimately “approved” source could still push an untested image; this doesn’t enforce the testing/approval gate itself.

  * **Option C — Different Use Case:** Kubernetes RBAC controls which authenticated users or service accounts can perform which actions against the cluster API (an identity/authorization concern). It’s valuable for least-privilege access but says nothing about whether a given container image passed through automated testing — an authorized user under RBAC could still deploy an image that skipped the pipeline entirely.

**Exam Trap**

The trap is treating this as an access-control problem (who is allowed to deploy) rather than a supply-chain-integrity problem (what is allowed to run). RBAC and source-restricted admission controllers both sound like reasonable “enforce approvals” answers because they gate _actors_ , but the auditor’s concern is about _artifacts_ bypassing testing — which only an attestation-based control like Binary Authorization actually verifies.

**Foundation Concept**

Software supply chain security distinguishes between controlling who can take an action (identity and access management, e.g., RBAC) and verifying that an artifact meets a required provenance or quality bar before it’s trusted to run (attestation-based admission control, e.g., Binary Authorization). When a scenario specifically worries about bypassing automated testing, the answer sits in the second category, because the first category can’t detect or prevent a legitimately authorized actor from deploying an unvetted artifact.

**Real-World Connection**

In practice, teams configure their CI/CD pipeline (e.g., Cloud Build) to run its test and security-scan stages and, only on success, sign the resulting image with an attestor key tied to Binary Authorization policy; the GKE cluster’s policy is then set to reject any image lacking that attestation. The operational payoff is that even a well-intentioned “hotfix” pushed manually during an incident gets blocked unless it goes through the pipeline — trading a small amount of deployment friction for a hard guarantee that production only ever runs tested, approved artifacts.

**Memory Hook**

“Stop untested images from running” → Binary Authorization with the pipeline as attestor; “control who can act” → RBAC; they solve different problems.

**30-Second Exam Takeaway**

When a question frames the risk as bypassing automated testing/approval before something reaches production in Kubernetes, look for an attestation-based admission control (Binary Authorization) rather than an identity/access control (RBAC) or a source-control gate (branch protection) — those control different stages and different risks.

**Official References**

[**Google Cloud — Binary Authorization overview:**](https://cloud.google.com/binary-authorization/docs/overview) Supports: the correct-answer mechanism of blocking unattested images from deployment and configuring a build pipeline as a trusted attestor

</details>

---

### Exam 1 · Q10

Your application services run on Google Kubernetes Engine (GKE). You want to guarantee that only images from your centrally managed Artifact Registry repository in the `altostrat-images` project can be deployed to the cluster, while keeping the development effort required to achieve this to a minimum. What should you do?

- A. Create a custom builder for Cloud Build that only pushes images to the `altostrat-images` Artifact Registry repository.
- B. Configure a Binary Authorization policy that includes an allowlist name pattern matching the `altostrat-images` Artifact Registry repository.
- C. Add logic to the deployment pipeline that checks that every manifest references only images from the `altostrat-images` Artifact Registry repository.
- D. Tag every image in the `altostrat-images` Artifact Registry repository, and verify that tag is present whenever an image is deployed.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Configure a Binary Authorization policy that includes an allowlist name pattern matching the `altostrat-images` Artifact Registry repository.

**Correct Answer**

**B. Configure a Binary Authorization policy that includes an allowlist name pattern matching the**`**altostrat-images**`**Artifact Registry repository.**

**Exam Reasoning Explanation**

The hard requirement is enforcement at the point of deployment — “only images from X can be deployed” is a guarantee about what the cluster will actually admit, not about what a build pipeline happens to produce or what a separate script happens to check. That distinction eliminates any approach that only controls the image-push side (where images get created) or that lives outside the cluster’s own admission path (a pipeline-side check that can be bypassed by anyone with direct `kubectl` access). The second constraint — minimizing development effort — favors a declarative policy configuration over building and maintaining custom tooling, scripts, or tagging conventions. Binary Authorization is the GKE-native admission control mechanism built exactly for this: a short, declarative policy restricts which image name patterns the cluster will admit, with no custom code to write or maintain.

**Key Exam Clues**

  * “only images from your centrally-managed... registry... can be deployed” is a hard constraint — it specifies admission-time enforcement on the cluster, not a build-time convention or a pipeline-side check that a bypass could evade.

  * “to the cluster” is a technical signal — it points toward a Kubernetes/GKE admission control mechanism rather than a CI/CD pipeline step that happens before the cluster is ever involved.

  * “while minimizing development time” is a preference that rules out options requiring custom code, scripts, or manual conventions in favor of a declarative, policy-based control.

**Why This Is Correct**

Binary Authorization enforces its policy at image admission into the GKE cluster: a policy with a default rule set to deny deployment, combined with an allowlist name pattern scoped to the `altostrat-images` repository, means the cluster will only admit images whose registry path matches that pattern, and will block anything else regardless of how someone attempted to deploy it (kubectl, a different pipeline, a compromised CI job). This is implemented as a short YAML policy rather than custom code, satisfying the “minimize development time” goal, and it closes the loop that build-side or pipeline-side controls leave open: it doesn’t matter where an image was built or pushed from — only images matching the approved registry pattern can ever run on the cluster.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Different Use Case:** A custom Cloud Build builder restricted to pushing only to the `altostrat-images` repository controls one path by which images get created, but it does nothing to stop a different image — built elsewhere, pulled from a public registry, or pushed by another pipeline — from being deployed directly to the cluster. It secures the build side, not the deploy side, which is what the requirement actually asks for.

  * **Option C — Technically Possible but Not Best:** Adding manual validation logic to the deployment pipeline that inspects manifests is a workable idea in principle, but it requires writing and maintaining custom checking code, and it only guards deployments that go through that specific pipeline — anyone with direct cluster access can bypass it entirely. It also conflicts with the “minimize development time” goal compared to a declarative policy.

  * **Option D — Technically Possible but Not Best:** Tagging approved images and checking for that tag at deploy time is a weak, convention-based control: tags are mutable and can be applied to any image by anyone with push access, so this doesn’t actually guarantee the image originates from the approved registry. It also requires building and maintaining custom tagging and verification logic rather than relying on built-in enforcement.

**Exam Trap**

The trap is treating Option A (controlling the build pipeline’s push destination) as equivalent to controlling what the cluster will run — but restricting where a trusted pipeline publishes images says nothing about what else might be deployed from outside that pipeline. The scenario’s “only images from X can be deployed” is a cluster-admission guarantee, which only an admission-control mechanism like Binary Authorization can actually provide.

**Foundation Concept**

Restricting _where images can be built or pushed to_ and restricting _what a cluster will admit to run_ are two different controls that address different threat models — the first narrows your trusted build surface, the second guarantees enforcement regardless of how an image arrived. When a requirement is phrased as “only X can be deployed,” it’s asking for the second: an admission-control policy evaluated at deploy time, not a convention enforced earlier in the pipeline.

**Real-World Connection**

Teams commonly layer both controls in production — a locked-down CI/CD pipeline that only pushes trusted images to one or two approved repositories, and a Binary Authorization policy on the cluster restricting admission to exactly those repository paths — so that even a misconfigured or compromised alternate deployment path can’t introduce an unapproved image, because the cluster itself refuses to run anything outside the allowlisted registry pattern.

**Memory Hook**

“Only X can be deployed to the cluster” means enforce it at the cluster’s admission boundary (Binary Authorization), not at the build pipeline or with a convention like tagging.

**30-Second Exam Takeaway**

When a GKE question asks you to guarantee that only images from a specific registry can be deployed — especially with minimal custom engineering — reach for a Binary Authorization policy with a name-pattern restriction rather than a build-pipeline control or a custom pipeline/tagging check, since only admission control actually governs what the cluster will run.

**Official References**

[**Google Cloud — Binary Authorization Policy YAML reference:**](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference) Supports: the correct-answer mechanism of restricting admitted images to a registry path pattern via a declarative policy, and the current “allowlist” terminology for this feature

[**Google Cloud — Container Registry deprecation and transition to Artifact Registry:**](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation) Supports: the terminology update reflecting that Container Registry (GCR) is fully shut down and Artifact Registry is the current, official image registry product

</details>

---

### Exam 1 · Q15

You have a CI/CD pipeline that uses Cloud Build to build Docker images and push them to Docker Hub. Your code is versioned in Git. After making a change to the Cloud Build YAML configuration, you notice that the pipeline is no longer building any new artifacts. Following Site Reliability Engineering practices, what should you do to resolve the issue?

- A. Disable the CI pipeline, and revert to building and pushing the artifacts manually.
- B. Change the CI pipeline to push the artifacts to Artifact Registry instead of Docker Hub.
- C. Upload the configuration YAML file to Cloud Storage, and use Error Reporting to identify and fix the issue.
- D. Run a Git diff between the previous and current versions of the Cloud Build configuration file to find and fix the bug.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Run a Git diff between the previous and current versions of the Cloud Build configuration file to find and fix the bug.

**Correct Answer**

**D. Run a Git diff between the previous and current versions of the Cloud Build configuration file to find and fix the bug.**

**Exam Reasoning Explanation**

The must-have constraint is diagnosing and fixing the actual root cause — the pipeline broke immediately after a configuration change, which is a direct, available clue pointing to exactly where the defect was introduced. SRE troubleshooting practice favors using the evidence closest to the failure before reaching for broader or unrelated remedies: since the code (including the Cloud Build YAML) is already versioned in Git, comparing the last known-working configuration against the current one is the fastest, most direct way to isolate precisely what changed and caused the failure. Every other option either abandons the automation entirely, changes something unrelated to the reported symptom, or applies a tool that doesn’t actually inspect configuration files — none of which engages with the root cause the way a direct diff does.

**Key Exam Clues**

  * “After making a change in the Cloud Build YAML configuration... no new artifacts are being built” is a hard constraint — it establishes a clear before/after causal link between a specific recent change and the failure, which is the strongest available diagnostic signal.

  * “You use Git for code versioning” is a technical signal — it tells you the tooling needed to directly compare the working and broken configuration states is already in place and requires no new setup.

  * “following Site Reliability Engineering practices” is a scope signal — it points toward a root-cause diagnostic approach consistent with blameless, evidence-based troubleshooting, rather than a workaround that sidesteps the problem or discards the automation.

**Why This Is Correct**

Since the pipeline failure began immediately after a specific, identifiable change to the Cloud Build configuration, and that configuration is version-controlled in Git, running a diff between the last working revision and the current one directly surfaces the exact lines that changed — which is almost always where the bug was introduced in a “it broke right after I changed X” scenario. This lets you pinpoint and correct the specific misconfiguration (a malformed step, an incorrect trigger condition, a broken substitution variable, etc.) with minimal guesswork, restoring the pipeline to a working state while preserving the intended change where possible. It’s the most targeted, lowest-effort path to root cause given the information already available.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Disabling the pipeline and reverting to manual builds abandons the automation entirely rather than fixing it — it’s a workaround that sacrifices the benefits of CI/CD (consistency, speed, reduced human error) instead of addressing the actual defect, and it does nothing to prevent the same misconfiguration from recurring once the pipeline is eventually re-enabled.

  * **Option B — Different Use Case:** Switching the artifact destination from Docker Hub to Artifact Registry doesn’t address the reported symptom at all — the pipeline isn’t failing because of where it pushes images, it’s failing to build anything in the first place, almost certainly due to the YAML change itself. This is a distractor that changes something unrelated to the actual failure.

  * **Option C — Incorrect:** Error Reporting is designed to aggregate and surface exceptions and stack traces from running application code, not to analyze static configuration files; uploading a YAML file to Cloud Storage and pointing Error Reporting at it doesn’t correspond to how that service actually works, so this approach can’t meaningfully diagnose a Cloud Build configuration problem.

**Exam Trap**

The trap is reaching for a tool-sounding “observability” answer (Option C) because the scenario involves troubleshooting, without checking whether that tool’s actual function matches the problem — Error Reporting ingests application exceptions, not static config files, so it has no mechanism to inspect or validate YAML syntax or pipeline logic. The fastest, most defensible fix is almost always the one that directly uses the evidence already pointing at the cause (the recent, version-controlled change), rather than introducing a new, mismatched tool.

**Foundation Concept**

When a system breaks immediately following a specific, identifiable change, the most effective troubleshooting first step is to examine that exact change before considering broader remedies — version control is one of the most direct diagnostic tools available precisely because it preserves the before/after state needed to isolate a regression quickly, which is far more targeted than disabling the system, changing unrelated components, or applying a monitoring tool outside its intended scope.

**Real-World Connection**

Teams running CI/CD pipelines routinely rely on this exact pattern when a pipeline regresses after a configuration commit: a quick `git diff` or `git log -p` against the pipeline definition file isolates the change, often revealing a typo, an incorrect step ordering, or a broken trigger condition within minutes — turning what could be an extended outage of the delivery pipeline into a short, well-understood fix, and reinforcing why keeping CI/CD configuration under the same version control as application code is a core DevOps practice.

**Memory Hook**

“It broke right after a specific change, and that change is in version control” → diff the before/after states first, before reaching for unrelated fixes or abandoning the pipeline.

**30-Second Exam Takeaway**

When a CI/CD pipeline fails immediately after a configuration change and that configuration is version-controlled, the SRE-aligned first move is always to compare the before/after states directly (a Git diff) to isolate the root cause — not to disable the pipeline, swap an unrelated component, or apply a monitoring tool that doesn’t inspect configuration files.

**Official References**

[**Google Cloud — Cloud Build configuration overview and troubleshooting builds:**](https://cloud.google.com/build/docs/troubleshooting) Supports: the correct-answer mechanism of diagnosing a Cloud Build YAML regression by examining the configuration change that preceded the failure

[Google Cloud — Professional Cloud DevOps Engineer exam guide, Section 2 (CI/CD pipelines): ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment — diagnosing and resolving CI/CD pipeline failures is explicitly part of building and implementing CI/CD pipelines

</details>

---

### Exam 1 · Q19

Your team uses Cloud Build for all CI/CD pipelines. You want to use the `kubectl` builder in Cloud Build to deploy new images to Google Kubernetes Engine (GKE), and you need to authenticate to GKE while keeping the development effort to a minimum. What should you do?

- A. Grant the Kubernetes Engine Developer role to the Cloud Build service account.
- B. Specify the Kubernetes Engine Developer role for Cloud Build in the `cloudbuild.yaml` file.
- C. Create a new service account with the Kubernetes Engine Developer role, and use it to run Cloud Build.
- D. Add a separate step in Cloud Build that retrieves service account credentials and passes them to `kubectl`.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Grant the Kubernetes Engine Developer role to the Cloud Build service account.

**Correct Answer**

**A. Grant the Kubernetes Engine Developer role to the Cloud Build service account.**

**Exam Reasoning Explanation**

The hard requirement is authenticating Cloud Build’s `kubectl` builder to the GKE cluster while minimizing development effort — meaning the solution should use existing, built-in mechanisms rather than custom scripting or additional infrastructure. Cloud Build already runs every build under its own default service account, and the `kubectl` builder is designed to pick up that identity’s credentials automatically (via the GKE cluster’s environment variables for zone/region and cluster name) with no manual credential handling required. That makes IAM role assignment on the existing Cloud Build service account the single, minimal-effort action needed — every other option either grants the permission in the wrong place (a YAML file isn’t an IAM mechanism), introduces unnecessary new infrastructure (a separate service account to run Cloud Build itself), or adds custom pipeline logic to do something the builder already handles natively.

**Key Exam Clues**

  * “minimizing development effort” is a hard constraint — it rules out any option requiring custom scripting, credential-handling steps, or additional infrastructure beyond what Cloud Build and the `kubectl` builder already provide.

  * “the kubectl builder for Cloud Build” is a technical signal — it specifies a tool that is built to authenticate using the Cloud Build service account’s existing identity, pointing directly at an IAM-role-grant solution rather than a manual credential-passing one.

  * “authenticate to GKE” is a scope signal — it’s specifically an identity/authorization task, which in Google Cloud is solved through IAM role bindings, not through application configuration files like `cloudbuild.yaml`.

**Why This Is Correct**

Every Cloud Build job runs under a Google-managed Cloud Build service account by default, and the `kubectl` builder is specifically designed to authenticate to a GKE cluster using that identity’s IAM permissions — it reads the cluster, zone/region, and project details from environment variables and handles the credential exchange itself. Granting the Kubernetes Engine Developer role (`roles/container.developer`) to that existing service account gives it exactly the permissions needed to interact with Kubernetes API objects in the cluster, which is all that’s required: no new service account, no custom credential-retrieval step, and no configuration-file-level role declaration (which isn’t how IAM permissions are granted in the first place). This is the smallest possible change that fully satisfies the authentication requirement.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Incorrect:** IAM roles are granted through Identity and Access Management policy bindings on a principal (a user, group, or service account) — they are not something you “specify” inside a `cloudbuild.yaml` build configuration file. This option describes a mechanism that doesn’t correspond to how GCP IAM actually works, so it can’t function as described.

  * **Option C — Technically Possible but Not Best:** Creating a new service account and configuring Cloud Build to run under it would work, but it’s unnecessary additional effort and infrastructure when the default Cloud Build service account already exists and only needs an IAM role granted to it. This adds a service-account creation and configuration step that doesn’t improve on simply granting the role to the existing identity.

  * **Option D — Technically Possible but Not Best:** Manually retrieving service account credentials and passing them to `kubectl` in a separate build step duplicates functionality the `kubectl` builder already performs automatically via the Cloud Build service account’s identity. This is significantly more development effort (writing and maintaining custom credential-handling logic) for no functional benefit over simply granting the role.

**Exam Trap**

The trap is Option B, which sounds plausible because `cloudbuild.yaml` is where you configure _what_ a build does — but IAM role grants are an identity/access-management concept entirely separate from build step configuration, and conflating the two is a common misunderstanding of where permissions actually live in Google Cloud. The decisive distinction is that authentication/authorization is an IAM concern (a policy binding on a principal), never something declared inside the pipeline’s own YAML definition.

**Foundation Concept**

When a CI/CD tool needs to interact with another Google Cloud service, the lowest-effort and most maintainable authentication pattern is almost always to grant the pipeline’s existing runtime identity (its default service account) the specific IAM role needed for the target service — rather than creating new service accounts, manually handling credentials, or trying to configure permissions through the pipeline’s own configuration file, which has no authority over IAM.

**Real-World Connection**

Teams running Cloud Build-to-GKE deployment pipelines commonly grant the Cloud Build service account the Kubernetes Engine Developer role exactly once during pipeline setup, after which every subsequent build’s `kubectl` builder step authenticates and deploys without any further credential management — keeping the pipeline simple to maintain and avoiding the security and operational overhead of managing separate service account keys or custom authentication logic.

**Memory Hook**

Authenticating a GCP CI/CD tool to another GCP service is almost always “grant the existing service account the right IAM role” — not a new service account, not a config-file permission, and not manual credential plumbing.

**30-Second Exam Takeaway**

When a Cloud Build question asks how to authenticate a builder (like `kubectl`) to another Google Cloud service with minimal effort, look for the option that grants the appropriate IAM role directly to Cloud Build’s existing default service account — that’s almost always simpler and more correct than creating new service accounts, writing custom credential-handling steps, or trying to set permissions inside the build configuration file itself.

**Official References**

[**Google Cloud — Authenticating to the Kubernetes API server:**](https://cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication) Supports: the correct-answer mechanism of granting `roles/container.developer` to the service account used to authenticate to a GKE cluster

[**Google Cloud — IAM roles for Kubernetes Engine:**](https://cloud.google.com/kubernetes-engine/docs/how-to/iam) Supports: the Kubernetes Engine Developer role’s purpose and scope as the minimal-effort permission grant for deploying to GKE

</details>

---

### Exam 1 · Q21

Your application artifacts are built and deployed through a CI/CD pipeline. You want the pipeline to access application secrets securely, and you also want to be able to rotate those secrets easily in the event of a security breach. What should you do?

- A. Prompt developers for secrets at build time, and instruct them not to store secrets at rest.
- B. Store secrets in a separate configuration file in Git, and give select developers access to that file.
- C. Store secrets in Cloud Storage, encrypted with a key from Cloud KMS, and grant the CI/CD pipeline access to Cloud KMS through IAM.
- D. Encrypt the secrets and store them in the source code repository, store the decryption key in a separate repository, and grant the pipeline access to that repository.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Store secrets in Cloud Storage, encrypted with a key from Cloud KMS, and grant the CI/CD pipeline access to Cloud KMS through IAM.

**Correct Answer**

**C. Store secrets in Cloud Storage, encrypted with a key from Cloud KMS, and grant the CI/CD pipeline access to Cloud KMS through IAM.**

**Exam Reasoning Explanation**

The two must-have requirements are secure, automated access for the pipeline and easy rotation in a breach scenario — which together rule out anything requiring manual human intervention at build time or anything that puts secrets inside version control, where history is hard to fully purge and access can’t be centrally revoked. Each option has to be checked against both requirements independently: automation compatibility, and how cleanly a compromised secret can be rotated. A centralized, encrypted store with IAM-controlled access satisfies both — the pipeline authenticates automatically via its service account, the secret value and the encryption key are managed independently of any code repository, and rotating either the secret or revoking access is a quick operation in a dedicated system built for exactly this.

**Key Exam Clues**

  * “securely access application secrets” is a hard constraint — it requires automated, access-controlled retrieval by the pipeline itself, ruling out any human-in-the-loop step.

  * “more easily rotate secrets in case of a security breach” is a second hard constraint — it demands that updating or revoking a secret be fast and centralized, which disqualifies anything embedding secrets in version-controlled files (where rotation means purging history and redeploying across every clone).

  * “CI/CD pipeline” as the consumer is a technical signal pointing toward IAM-based service-to-service access (the pipeline’s own identity authenticating to a secrets store), rather than developer-managed access controls on a shared file.

**Why This Is Correct**

Storing secrets in Cloud Storage with Cloud KMS encryption keeps the sensitive values out of source control entirely, encrypted at rest with keys that are centrally managed and access-controlled. Granting the CI/CD pipeline’s service account IAM access to the relevant Cloud KMS key and Cloud Storage object lets the pipeline retrieve and decrypt secrets automatically during a build with no manual step, satisfying secure access. For rotation, updating the stored secret value or rotating the KMS key is a contained, centralized operation — and if a breach occurs, revoking IAM access or rotating the key immediately cuts off further use of the compromised secret, without needing to rewrite Git history or coordinate changes across every repository that might reference it.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Prompting developers for secrets at build time breaks automation entirely — a CI/CD pipeline is meant to run unattended, and requiring a human to supply a secret defeats the purpose of continuous delivery while also providing no mechanism for secure storage or rotation at all.

  * **Option B — Violates Requirement:** Storing secrets in a Git configuration file, even with restricted developer access, puts sensitive values into version control history, where they persist indefinitely across clones and forks; rotating a compromised secret would require not just updating the file but scrubbing history everywhere it was ever committed, which is neither secure nor easy.

  * **Option D — Technically Possible but Not Best:** Encrypting secrets and storing them alongside code, with the decryption key in a separate repository, is a workable but weaker pattern than using a dedicated key-management service: both the encrypted secrets and the key end up living in source control systems not purpose-built for secret lifecycle management, lacking the centralized audit logging, fine-grained IAM controls, and key-rotation tooling that Cloud KMS provides natively. Rotation here still means committing new encrypted values and managing key access through repository permissions rather than a dedicated IAM/KMS control plane.

**Exam Trap**

The trap is Option D looking secure at first glance because the secrets are “encrypted” — but encryption alone doesn’t solve the rotation and access-revocation problem if the encrypted blob and its key are still managed through source-control permissions rather than a centralized key-management system built for exactly this lifecycle (issuing, rotating, and revoking access to keys and secrets independently of code history).

**Foundation Concept**

Secrets belong in a system designed around their specific lifecycle — centralized storage, encryption at rest, fine-grained IAM-based access, and the ability to rotate or revoke instantly — never in source control, even encrypted, because version control systems are optimized for code history and collaboration, not for the access-revocation and audit guarantees a compromised secret response actually requires.

**Real-World Connection**

While Cloud Storage encrypted with a Cloud KMS key is a valid and functional pattern, Google Cloud also offers Secret Manager, a service purpose-built for exactly this use case — centralized secret storage, automatic versioning, IAM-based per-secret access control, and built-in audit logging — which many CI/CD pipelines use directly for application secrets precisely because it provides this same security and rotation model with less infrastructure to manage than assembling Cloud Storage and Cloud KMS by hand.

**Memory Hook**

Secrets for an automated pipeline belong in a centralized, IAM-controlled, encrypted store — never in source control, encrypted or not — because only a dedicated secret-management approach makes both secure automated access and fast rotation possible.

**30-Second Exam Takeaway**

When a CI/CD question asks how to securely provide and easily rotate secrets, favor a centralized, encrypted secret store with IAM-based access over anything that puts secrets (even encrypted ones) into source control or requires a human to supply them at build time — the decisive test is whether a compromised secret can be rotated and revoked without touching repository history.

**Official References**

[**Google Cloud — Cloud KMS overview:**](https://cloud.google.com/kms/docs/key-management-service) Supports: the correct-answer mechanism of encrypting secrets with centrally managed, rotatable Cloud KMS keys and controlling access via IAM

[Google Cloud — Secret Manager overview: ](https://cloud.google.com/secret-manager/docs/overview)Supports: the current, purpose-built Google Cloud service for application secret storage, access control, and rotation referenced as the broader best-practice context

</details>

---

### Exam 1 · Q35

Your application images are built with Cloud Build and pushed to Artifact Registry. You want to be able to choose a specific version of your application to deploy, based on the release version tagged in source control. What should you do when you push the image?

- A. Record the image digest in the source control tag.
- B. Pass the source control tag as a parameter in the image name.
- C. Have Cloud Build embed the release version tag in the application image.
- D. Use Artifact Registry digest versioning to match the image to the source control tag.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Pass the source control tag as a parameter in the image name.

**Correct Answer**

**B. Pass the source control tag as a parameter in the image name.**

**Exam Reasoning Explanation**

Start from the deployment side. To deploy “a particular version,” the deployment must be able to name that version in the image reference it uses. The version comes from the source control tag, so that tag has to become part of the image reference at the moment the image is pushed. The push step is where the reference is set, which makes it the only place the link can be created. Test each option against one question: after the push, can I select the image by the Git release tag alone? Only an image published under that tag in its name can be selected that way.

**Key Exam Clues**

  * **“specify a particular version of your application for deployment”** (hard constraint): the image must be addressable by a version identifier at deployment time.

  * **“based on the release version tagged in source control”** (hard constraint): the identifier must come from the Git tag, so that value has to appear in the image reference.

  * **“when you push the image”** (sequence instruction): the action must happen at push time, which is when the image’s name and tag are assigned.

**Why This Is Correct**

A container image is referenced by name plus either a tag or a digest. Image tags are the common human-readable way to refer to different revisions, and Google’s guidance describes tagging images with a version identifier at build time as a common approach. Cloud Build supports this directly. For builds invoked by a trigger, the default substitution $TAG_NAME holds the name of the Git tag, and you can use it in the image name in the build config, so the pushed image carries the release version. For a manual build, you can supply the same value through the substitutions flag. Deployment can then reference the image by that tag, and redeploying an earlier release means pointing back to its tag.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best**. This runs in the wrong direction. A digest is computed by the registry from the image content, so it is only known after the push, and writing it back into source control adds a post-build step. It also sets nothing on the pushed image, so you would have to look up the digest from the Git tag before every deployment instead of simply deploying the tagged image.

**Option C — Technically Possible but Not Best.** Embedding the version inside the image, for example as a label or a file, helps identify what is running. Deployment still resolves an image through its registry reference, so embedded content does not let you select a version. The image must still be pushed under a tag for that to work.

**Option D — Incorrect.** A digest is a content-derived hash, not a versioning scheme you can configure to match a Git tag. There is no digest versioning feature that maps an image to a source control tag.

**Exam Trap**

The strongest distractors are the digest-based options, because digests are immutable and tags are mutable, so deploying by digest is often the better practice for guaranteeing exact content. The resolving distinction is that this question asks how to select a version by its Git release tag, and a digest cannot carry or be matched to that tag. The answer would shift if the requirement were to guarantee the exact bytes deployed even if a tag were later reassigned. In that case you would deploy by digest, ideally in addition to tagging.

**Foundation Concept**

An image has three identifiers. The name locates the repository, a tag is a mutable human-readable pointer to a revision, and the digest is an immutable hash of the content. Tagging at build time with the source control version ties an artifact to the code that produced it, which supports traceability and straightforward rollbacks. Tags can be moved to new images, so strict reproducibility requires resolving to a digest. Google Container Registry has been superseded by Artifact Registry, which also hosts images for the gcr.io domain through gcr.io repositories.

**Real-World Connection**

A team creates a release tag such as v1.4.0 in Git, which fires a Cloud Build trigger on tags. The build config builds the image and pushes it to an Artifact Registry repository under a name ending in the tag value, using the $TAG_NAME substitution. Deployment manifests or a delivery pipeline then reference that exact tag, so promoting or rolling back is a matter of choosing a release tag. The trade-off is that tags can be reassigned, so teams that need stronger guarantees also record or deploy the resulting digest.

**Memory Hook**

Push the image under the release tag in its name, because tags select versions and digests only identify content.

**30-Second Exam Takeaway**

When a question asks how to deploy a specific version identified by a source control tag, tag the image with that release version in its name at push time. Reject digest-based options as the way to match a Git tag, and reject options that bury the version inside the image, since neither makes the version selectable by reference.

**Official References**

[Google Cloud: Substituting variable values (Cloud Build): ](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values)Supports: the correct answer, covering the default $TAG_NAME substitution holding the Git tag name for triggered builds, and using substitutions in image names pushed to Artifact Registry.

[**Google Cloud: About container image digests:**](https://docs.cloud.google.com/architecture/using-container-images) Supports: the option distinctions, covering tagging images with a version identifier at build time, tags as mutable references, and digests as immutable content hashes (Options A and D).

[**Google Cloud: Transition from Container Registry (Artifact Registry):**](https://docs.cloud.google.com/artifact-registry/docs/transition/transition-from-gcr) Supports: the current terminology, covering Artifact Registry as the recommended successor to Container Registry and its support for the gcr.io domain through gcr.io repositories.

[**Google Cloud: Professional Cloud DevOps Engineer exam guide (Section 2.1, Designing pipelines):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with CI/CD of applications and artifact management with Artifact Registry.

</details>

---

### Exam 1 · Q39

You manage production deployments to a set of Google Kubernetes Engine (GKE) clusters. You want to ensure that only images successfully built by your trusted CI/CD pipeline can be deployed to production. What should you do?

- A. Turn on Web Security Scanner for the clusters.
- B. Turn on Artifact Analysis vulnerability scanning in Artifact Registry.
- C. Configure the GKE clusters as private clusters.
- D. Configure the GKE clusters with Binary Authorization.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Configure the GKE clusters with Binary Authorization.

**Correct Answer**

**D. Configure the GKE clusters with Binary Authorization.**

**Exam Reasoning Explanation**

Start from what the requirement demands. It has two parts: the control must establish where an image came from, specifically that your trusted pipeline built it successfully, and it must enforce that fact at deployment by blocking anything that cannot show it. A control that only detects problems, or that only restricts network access, does not tie an image to its build origin or block a deployment. The decision method is to ask of each option whether it records provenance at build time and checks it at deploy time. Only one of the four does both.

**Key Exam Clues**

  * **“only images successfully built by your trusted CI/CD pipeline”** (hard constraint): the control must verify an image’s build origin, not just its contents.

  * **“can be deployed to production”** (hard constraint): enforcement must happen at deployment, which means blocking, not reporting.

  * **“a set of Google Kubernetes Engine (GKE) clusters”** (technical signal): the control must apply on the cluster deployment path, where images are admitted.

**Why This Is Correct**

Binary Authorization is a deploy-time security control that ensures only trusted container images are deployed on GKE. It works by enforcing a policy, and one common policy requires signed attestations. An attestor signs an image after your pipeline builds it, and at deploy time the admission check verifies the attestation, so unsigned images are blocked. Cloud Build integrates directly. When a build produces images, Cloud Build automatically creates the built-by-cloud-build attestor in your project and, once the images are successfully built, signs and creates attestations for them. A production policy that requires that attestation therefore admits only images your pipeline built successfully. That matches the requirement precisely.

**Why the Other Options Are Not the Best Fit**

**Option A — Different Use Case.** Web Security Scanner crawls deployed web applications to identify vulnerabilities such as cross-site scripting and outdated libraries. It evaluates running applications, not the origin of the images, and it cannot stop an image from being deployed.

**Option B — Technically Possible but Not Best.** Artifact Analysis scans images in Artifact Registry for known vulnerabilities and can feed results into a delivery process, so it is tempting as an image trust control. Scanning alone does not show that your pipeline built the image, and it does not block a deployment. It becomes useful here only as an input to an attestation policy.

**Option C — Different Use Case.** Private clusters use nodes with only internal IP addresses, isolating them from the public internet and limiting control plane access. That is a network isolation control. It says nothing about which images are admitted to run on the nodes.

**Exam Trap**

The strongest distractor is Option B, because vulnerability scanning sounds like image trust. The resolving distinction is that scanning finds known vulnerabilities in an image’s contents, whereas the requirement concerns provenance and enforcement. Option B would become part of the answer if the requirement were to block images with serious vulnerabilities. In that case a scan result would be turned into an attestation, and Binary Authorization would require it at deploy time.

**Foundation Concept**

Software supply chain security rests on two steps: produce evidence about an artifact where it is built, and verify that evidence where it is deployed. Evidence takes the form of a signed attestation tied to a specific image, and verification is an admission check that allows or denies the workload. Detection tools and network controls complement this but do not replace it. Policies can also be introduced gradually, for example by first auditing violations before enforcing, and they typically include a break-glass path for emergencies.

**Real-World Connection**

A team builds images in Cloud Build and pushes them to Artifact Registry, and each successful build is automatically attested by the built-by-cloud-build attestor. They then enable Binary Authorization on the production GKE clusters with a policy requiring that attestation, usually trialing it in an audit mode first to see which deployments would have been blocked. An image pushed by hand or built outside the pipeline is rejected at admission. The result is a verifiable chain from source to production, at the cost of maintaining the policy and attestors and planning for emergency exceptions.

**Memory Hook**

Sign at build and verify at deploy: Binary Authorization admits only images with a trusted attestation.

**30-Second Exam Takeaway**

When a question asks to ensure that only images from a trusted pipeline run in GKE, choose Binary Authorization with attestations. Reject vulnerability scanners and network isolation, since scanners report on contents and private clusters restrict network access, and neither enforces build provenance at deployment.

**Official References**

[**Google Cloud: Gating Deployments with Binary Authorization (codelab):**](https://codelabs.developers.google.com/gating-deployments-with-binary-auth) Supports: the correct answer, covering policies requiring signed attestations at deploy time, and Cloud Build automatically creating the built-by-cloud-build attestor and signing attestations for successfully built images.

[**Google Cloud: Artifact Analysis and vulnerability scanning:**](https://docs.cloud.google.com/artifact-registry/docs/analysis) Supports: the elimination of Option B and the current terminology, covering Artifact Analysis (formerly Container Analysis) scanning images automatically when they are pushed to Artifact Registry.

[**Google Cloud: About private clusters (GKE):**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept) Supports: the elimination of Option C, covering private clusters as nodes with only internal IP addresses that are isolated from the public internet.

[**Google Cloud: Overview of Web Security Scanner (Security Command Center):**](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview) Supports: the elimination of Option A, covering Web Security Scanner as a vulnerability scanner for web applications on App Engine, GKE, and Compute Engine.

</details>

---

### Exam 1 · Q42

You release a new version of an internal application during a weekend maintenance window, when user traffic is minimal. After the window closes, you discover that one of the new features does not work as expected in production. The outage lasts a long time before you roll back the release and deploy a fix. You want to change your release process to shorten the mean time to recovery (MTTR) so that future outages are not prolonged. What should you do? (Choose two.)

- A. Require two separate peers to review code changes before they are merged.
- B. Adopt a blue/green deployment strategy when releasing new code through a continuous delivery (CD) server.
- C. Add a code linting tool that checks coding standards before any code is accepted into the repository.
- D. Require developers to run automated integration tests in their local development environments before a release.
- E. Set up a continuous integration (CI) server, add a unit test suite to the code, and have the CI server run the tests on every commit to verify changes.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Adopt a blue/green deployment strategy when releasing new code through a continuous delivery (CD) server. **|** E. Set up a continuous integration (CI) server, add a unit test suite to the code, and have the CI server run the tests on every commit to verify changes.

**Correct Answer**

**B. Adopt a blue/green deployment strategy when releasing new code through a continuous delivery (CD) server.**

**E. Set up a continuous integration (CI) server, add a unit test suite to the code, and have the CI server run the tests on every commit to verify changes.**

**Exam Reasoning Explanation**

Separate the must-have from the framing. The goal is a shorter recovery time after a bad release, and the incident shows two weaknesses: the broken feature reached production, and getting back to a good state took too long. Choose one action for each weakness. For fast recovery, you need a release mechanism that makes returning to the previous version quick and low-risk. For fast detection and repair, you need automated, enforced feedback on every change so defects surface early and a fix can ship through a trusted pipeline. Then eliminate options that improve code hygiene or rely on unenforced manual steps without affecting recovery. Two options remain.

**Key Exam Clues**

  * **“Reduce the mean time to recovery”** is a hard constraint. The chosen actions must shorten recovery, not only prevent problems.

  * **“After an extended outage, you roll back ... and deploy a fix”** is a technical signal. Both rolling back and redeploying took too long, so the release mechanism and the verification of fixes are the targets.

  * **“Choose two”** is a cardinality instruction. Select exactly two options, ideally covering different parts of the problem.

  * **“Release process”** is a scope signal. The change should live in the delivery pipeline, not in individual habits or style rules.

**Why This Is Correct**

Option B addresses recovery directly. In a blue/green deployment, two identical environments exist, and the new version is deployed to the idle one while the current one keeps serving users. Traffic moves to the new version only when it is ready, and if a problem appears, traffic switches back to the previous environment almost instantly. This turns an extended rollback into a quick switch, which is the largest cut to MTTR. Option E strengthens the other half. A CI server that runs unit tests on every commit gives immediate, automated, consistent feedback, so regressions are caught close to where they were introduced. It also verifies a fix quickly and reliably before it is released. The two options work together: E reduces how often bad changes reach production and speeds up fixes, while B limits how long users are affected when one does. They are independent controls, and together they cover both prevention and recovery.

**Why the Other Options Are Not the Best Fit**

**Option A — Different Use Case:** Requiring two peer reviewers improves code quality and shares knowledge. It is tempting because reviews catch defects. It happens before merging, depends on human attention, and does nothing to speed up rollback or fix verification, and it can slow delivery.

**Option C — Different Use Case:** A linting tool enforces style and standards. It is tempting because it is automated and runs before acceptance. It does not detect functional defects such as a feature that fails in production, and it has no effect on recovery speed.

**Option D — Technically Possible but Not Best:** Automated integration tests are valuable, so the idea is sound. It loses because running them in local environments is left to individual developers, is not enforced centrally, and may differ from the production setup. It is also not part of the release mechanism, so it does not make recovery faster the way a pipeline-level control does.

**Exam Trap**

The strongest distractor is option D, because automated integration tests sound more thorough than unit tests. The distinction is where and how they run: tests that depend on each developer’s local environment are inconsistent and unenforced, while a CI server runs them the same way on every commit. The answer would shift toward integration testing only if the option said they run automatically in the pipeline against a production-like environment. A second trap is treating quality gates such as peer review and linting as recovery measures. They are preventive and do not shorten recovery.

**Foundation Concept**

Mean time to recovery improves when you can detect problems fast and restore service fast. Detection improves with automated testing and monitoring, and restoration improves with deployment strategies that make reverting cheap, such as blue/green, canary, or traffic splitting. Prevention reduces how often failures happen, but it does not substitute for recovery speed. Blue/green has costs, including running two environments and handling data or schema compatibility, so it fits best when instant rollback matters more than the duplicated capacity.

**Real-World Connection**

A team routes releases through a pipeline that builds, runs unit tests on each commit, deploys to the idle environment, and only then shifts traffic. When a broken feature appears, an operator shifts traffic back within minutes, and the team fixes the defect with a new commit that passes the same automated tests before redeploying. The result is a short disruption instead of an extended outage, at the cost of keeping a second environment available during releases.

**Memory Hook**

To recover faster, make rollback a traffic switch and make every change pass automated tests before it ships.

**30-Second Exam Takeaway**

For MTTR questions, pick one option that makes reverting instant, such as blue/green, and one that gives automated, enforced feedback, such as CI tests. Reject style rules, peer review, and unenforced local testing, which do not change recovery speed.

**Official References**

[Google Cloud Architecture Center — Application deployment and testing strategies: ](https://cloud.google.com/architecture/application-deployment-and-testing-strategies)Supports: blue/green deployment keeping the previous environment available and allowing a quick switch back, which supports option B.

[**Google Cloud Architecture Center — DevOps capabilities (DORA), including continuous integration, test automation, and continuous delivery:**](https://docs.cloud.google.com/architecture/devops) Supports: running automated tests on each commit through a CI process as a practice that speeds feedback and release reliability, which supports option E.

[Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 2, Building and implementing CI/CD pipelines): ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment with deployment strategies such as blue/green and with troubleshooting and mitigating deployment issues.

</details>

---

### Exam 1 · Q43

Your team builds application container images and pushes them to Artifact Registry. You need an automated pipeline that deploys the application each time a new image is published, and you want to keep the development effort as low as possible. What should you do?

- A. Configure Cloud Build to start a Spinnaker pipeline.
- B. Configure Cloud Pub/Sub to start a Spinnaker pipeline.
- C. Configure a custom builder in Cloud Build to start a Jenkins pipeline.
- D. Configure Cloud Pub/Sub to start a custom deployment service running on Google Kubernetes Engine (GKE).

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Configure Cloud Pub/Sub to start a Spinnaker pipeline.

**Correct Answer**

**B. Configure Cloud Pub/Sub to start a Spinnaker pipeline.**

**Exam Reasoning Explanation**

Separate the must-have from the preference. The must-have is that the trigger is the image update itself, not a source commit or a manual step. The preference is minimal development effort, which favors managed, built-in integrations over anything custom. Work through it as requirement, capability, elimination, decision. The registry already emits an event when an image changes, so you need something that listens to that event, and Spinnaker can start a pipeline directly from a Pub/Sub subscription. That path needs configuration but no new code. Each remaining option adds a build step, a custom builder, or a service you would have to write and run.

**Key Exam Clues**

  * **“Deploys the application when the image is updated”** is a hard constraint. The trigger must be the image publish event, not a code change.

  * **“Minimizing the development effort”** is a preference that works as a tiebreaker. It rules out anything requiring custom code or a custom service.

  * **“Images are built and pushed to the registry”** is a technical signal. The image already exists when the pipeline starts, so a build step is unnecessary for triggering.

  * **“Automated pipeline”** is a technical signal. It points to an event-driven trigger rather than a manual or polling approach.

**Why This Is Correct**

Artifact Registry publishes messages to a Pub/Sub topic named gcr whenever an image is uploaded, tagged, or deleted. Spinnaker supports a Pub/Sub trigger type that subscribes to a Google Pub/Sub subscription and starts a pipeline when a message arrives. Its Google Pub/Sub integration documents registry-originated messages as a supported source. Connecting the two is a configuration task: create a subscription on the topic, enable Google Pub/Sub in Spinnaker, and add a Pub/Sub trigger to the pipeline. The image reference in the message can be used as the artifact to deploy. No custom code is needed, which is why it is the lowest-effort fit. One boundary matters: the topic delivers all registry events, so the pipeline should constrain the trigger to the push events and image it cares about.

**Why the Other Options Are Not the Best Fit**

**Option A — Different Use Case:** Cloud Build starts builds from source events such as commits or tags, and Spinnaker can react to Cloud Build results. That chain is tied to a build happening, not to an image appearing in the registry. It is tempting because Cloud Build is a natural place to produce the image, but it would miss images pushed by other means. It also adds a build dependency the requirement does not call for.

**Option C — Technically Possible but Not Best:** A custom builder in Cloud Build can call Jenkins, so the outcome is achievable. It is tempting because Jenkins is a well-known deployment tool. It loses on effort, because it requires writing and maintaining a custom builder, running a Jenkins server, and still has no direct link to the image update event.

**Option D — Violates Requirement:** Pub/Sub is the right trigger source, and that makes this option look close. However, writing, hosting, securing, and operating your own deployment service on GKE is the highest-effort path. It directly conflicts with minimizing development effort when an existing tool can consume the same event.

**Exam Trap**

The strongest distractor is option A, because Cloud Build feels like the natural pipeline entry point when images are built there. The distinction is that the requirement is event-driven on the image update, not on a source change. The answer would shift toward Cloud Build only if the requirement were to deploy on every source commit. A second trap is option D, which uses the correct Pub/Sub event but ignores the effort constraint. A terminology note: Container Registry has been superseded by Artifact Registry, and Artifact Registry publishes to the same gcr topic, so the Pub/Sub approach is unchanged. Google’s native managed continuous delivery service is Cloud Deploy, but it is not offered here, so the best choice among the given options is B.

**Foundation Concept**

Event-driven pipelines start from a signal that something changed, not from polling or a manual step. A registry publishes change events to a message bus, and a deployment system subscribes to that bus and acts on it. Using a deployment tool’s built-in trigger for that event beats writing glue code, because the integration is already tested and maintained. The pattern holds whenever the source of the change can publish events. It weakens when you need to filter heavily or enforce ordering and approvals, which the deployment tool must then handle.

**Real-World Connection**

A team creates a subscription on the registry’s topic and adds a Pub/Sub trigger to a Spinnaker pipeline with a constraint on the image name. Every new tagged image then starts a deployment with no code to maintain. The operational result is a short, auditable path from image publish to rollout, and the main ongoing cost is managing Spinnaker itself rather than custom services. Because the topic carries all registry events, the team also adds payload filtering so tag deletions do not start deployments.

**Memory Hook**

Image changed in the registry means a Pub/Sub event, and the least-effort consumer is the deployment tool’s built-in Pub/Sub trigger.

**30-Second Exam Takeaway**

When a deployment must start from an artifact update and effort must be minimal, pick the managed event source feeding the tool’s native trigger. Reject options that add build steps, custom builders, or self-written services.

**Official References**

[Google Cloud — Artifact Registry: Configure Pub/Sub notifications: ](https://docs.cloud.google.com/artifact-registry/docs/configure-notifications)Supports: the registry publishing image upload and tag events to the gcr topic, and that Artifact Registry uses the same topic as Container Registry, which makes the Pub/Sub trigger valid for option B.

[**Spinnaker — Google Cloud Pub/Sub triggers:**](https://spinnaker.io/docs/setup/other_config/triggers/google/) Supports: Spinnaker starting pipelines from Pub/Sub messages originating from Google Cloud systems such as the container registry, which separates B from A, C, and D.

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 2, Building and implementing CI/CD pipelines):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with designing pipelines, pipeline triggers, and artifact management with Artifact Registry.

</details>

---

### Exam 1 · Q45

You use Spinnaker to deploy your application, and your pipeline includes a canary deployment stage. The application keeps an in-memory cache that is populated with objects when the application starts. You want to automate the comparison between the canary version and the production version. How should you configure the canary analysis?

- A. Compare the canary against a newly created deployment of the current production version.
- B. Compare the canary against a newly created deployment of the previous production version.
- C. Compare the canary against the already running deployment of the current production version.
- D. Compare the canary against the averaged performance of a sliding window of earlier production versions.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Compare the canary against a newly created deployment of the current production version.

**Correct Answer**

**A. Compare the canary against a newly created deployment of the current production version.**

**Exam Reasoning Explanation**

The must-have is a fair, like-for-like comparison that isolates the effect of the new code. The scenario supplies the key detail: an in-memory cache filled at startup. That means a long-running instance and a freshly started instance behave differently regardless of the code version. Work through requirement, capability, elimination, decision. A valid baseline must run the same code as production while matching the canary in age and conditions. Any comparison target that differs in running time, code version, or traffic period adds noise that cannot be separated from the canary’s real effect. Only one option meets that bar.

**Key Exam Clues**

  * **“In-memory cache that loads objects at start time”** is a decisive technical signal. A freshly started canary has a cold cache, while a long-running instance has a warm one, which skews performance metrics.

  * **“Automate the comparison of the canary version against the production version”** is a hard constraint. The comparison target must produce statistically fair results.

  * **“Canary deployment stage in the pipeline”** is a context signal. Spinnaker’s canary analysis is designed to run a canary and a baseline side by side.

**Why This Is Correct**

Spinnaker’s automated canary analysis, built on Kayenta, compares the canary against a baseline rather than against the live production instances. The baseline is a new deployment of the current production version, started at the same time as the canary, with the same number of instances and configuration. Because both start together, they have the same cache warmup state, so differences in metrics reflect the code change instead of uptime. In this application, the cold cache is the very effect that would distort a comparison against long-running production instances. A boundary to note: the baseline runs the same version production runs, so it tests the new code, not production’s accumulated state.

**Why the Other Options Are Not the Best Fit**

**Option B — Incorrect:** A new deployment of the previous production version is a baseline of the wrong code. It is tempting because it is freshly started, like the canary, which would match cache state. It is not the version users currently run, so the analysis would compare the canary with something that is not production and could miss regressions relative to what is live.

**Option C — Violates Requirement:** Comparing against the existing production deployment is the intuitive approach, and it is tempting for that reason. The existing instances have run for a long time with warm caches, so latency and resource metrics would differ from a freshly started canary for reasons unrelated to the code. This is exactly the unfairness the cache detail points to.

**Option D — Technically Possible but Not Best:** A sliding window of earlier versions provides a long history, which is tempting for statistical stability. It mixes several code versions and different traffic periods, and none of it matches the canary’s start time, so it cannot isolate the effect of the new release.

**Exam Trap**

The strongest distractor is option C, because comparing a canary with the live production deployment is the most natural reading of a canary. The distinction is that the comparison must hold everything constant except the code, and uptime and cache state are not constant. The answer would switch to C only if the application had no warmup or startup effects and the production instances were otherwise comparable. A second trap is option B, which looks fair because it is freshly started but tests the wrong code version.

**Foundation Concept**

A valid experiment changes one variable and controls the rest. In canary analysis, the canary carries the changed code, and the baseline is the control. For the control to be valid, it should match the canary in code version relevant to production, start time, scale, and traffic exposure. Anything that depends on instance age, such as caches, JIT warmup, or connection pools, makes long-running instances a poor control. This model applies to automated comparison of metrics. Where an application has no age-dependent behavior, the difference matters less, but the baseline pattern remains the safer default.

**Real-World Connection**

A pipeline deploys three canary instances with the new image and three baseline instances with the current production image, routes a small share of traffic to each, and runs the analysis on matching metrics for a fixed period. A score above the threshold promotes the release, and a low score stops it. Teams often add a test where the canary runs the same version as production, which should always pass, to confirm the analysis configuration is sound. The cost is temporary extra instances while the analysis runs.

**Memory Hook**

Compare the canary to a fresh copy of today’s production, not to the instances that have been running for weeks.

**30-Second Exam Takeaway**

For canary analysis questions, pick a baseline that runs the current production version and starts alongside the canary. Reject comparisons against long-running instances, older versions, or historical averages.

**Official References**

[**Google Cloud Blog — Canary analysis: Lessons learned and best practices from Google and Waze:**](https://cloud.google.com/blog/products/devops-sre/canary-analysis-lessons-learned-and-best-practices-from-google-and-waze) Supports: comparing the canary against a baseline with the same version and configuration as production rather than against production itself, citing cache warmup as a skewing factor, which supports option A and rules out options C and D.

[**InfoQ — Kayenta: An Open Source Canary Analysis Tool from Netflix and Google:**](https://www.infoq.com/news/2018/04/kayenta) Supports: creating a brand new baseline cluster so metrics are free of effects from long-running processes, which reinforces the elimination of option C.

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 2, Building and implementing CI/CD pipelines):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with deployment strategies such as canary and with defining success metrics based on application telemetry.

</details>

---

### Exam 1 · Q49

Your multi-step Cloud Build pipeline builds your application and deploys it to Google Kubernetes Engine (GKE). You want to connect the pipeline to a third-party monitoring platform by sending the build information to a webhook with an HTTP POST. You also want to keep development effort as low as possible. What should you do?

- A. Add logic to every Cloud Build step that sends the build information to the webhook with an HTTP POST.
- B. Add a final step to the Cloud Build pipeline that sends the build information to the webhook with an HTTP POST.
- C. Use Cloud Logging to create a log-based metric from the Cloud Build logs, and then create an alerting policy that uses a webhook notification channel.
- D. Create a Pub/Sub push subscription on the Cloud Build cloud-builds topic so that the build information is sent to the webhook with an HTTP POST.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Create a Pub/Sub push subscription on the Cloud Build cloud-builds topic so that the build information is sent to the webhook with an HTTP POST.

**Correct Answer**

**D. Create a Pub/Sub push subscription on the Cloud Build cloud-builds topic so that the build information is sent to the webhook with an HTTP POST.**

**Exam Reasoning Explanation**

The must-have is that build information reaches a third-party webhook as an HTTP POST. The preference is minimal development effort. Work through requirement, capability, elimination, decision. Ask which approach already produces the build information and the HTTP POST without new code. Cloud Build already publishes build state changes as messages, and a Pub/Sub push subscription already delivers messages as HTTP POST requests to an endpoint. Joining those two managed pieces is configuration. The other options require writing and maintaining logic inside the pipeline or repurposing a metrics and alerting feature for a job it was not designed to do.

**Key Exam Clues**

  * **“HTTP POST of the build information to a webhook”** is a technical signal. Pub/Sub push delivery is itself an HTTP POST to a webhook endpoint.

  * **“Minimize the development effort”** is a preference that works as a tiebreaker. It favors configuration over custom pipeline code.

  * **“Multiple step pipeline”** is a technical signal. Per-step logic would multiply the work and still miss overall build status events.

  * **“Build information”** is a technical signal. Cloud Build’s own notifications carry the build resource and status, so you do not need to assemble it.

**Why This Is Correct**

Cloud Build publishes a message to the cloud-builds Pub/Sub topic whenever a build’s state changes, such as when it is created, starts working, or completes. Each message carries the build resource and its status. A push subscription on that topic makes Pub/Sub send each message to a configured HTTPS endpoint as a POST request, so the webhook receives build updates with no pipeline code. Setup amounts to creating the topic if needed, granting the required permissions, and creating the subscription. Two boundaries apply. The push request wraps the message in a JSON envelope, with the build data base64-encoded inside, so the receiving platform must accept that format, or you can choose unwrapped delivery to send the raw data. The endpoint must also be an HTTPS address that Pub/Sub can reach and that returns a success code.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** Adding POST logic to every step works. It is tempting because it uses only Cloud Build. It requires the most effort, since the code must be written, kept consistent, and maintained in each step. It also does not capture overall build state changes cleanly.

**Option B — Technically Possible but Not Best:** A final step is less work than adding logic to every step, which makes it tempting. It still requires custom code, and it only runs when earlier steps succeed, so failed builds may never report. It would also need to assemble the build information itself.

**Option C — Different Use Case:** A log-based metric with an alerting policy and a webhook notification channel can notify a webhook. It is tempting because alerting policies support webhooks. It is built to alert on conditions in logs, not to forward build information, so it adds metric and policy configuration and the alert payload would not be the build data the monitoring platform expects.

**Exam Trap**

The strongest distractor is option B, because a final pipeline step seems like the obvious lightweight integration. The distinction is that it still means writing and maintaining code inside the pipeline, and it can miss failed builds, whereas the Pub/Sub notification is managed and fires on every state change. The answer would switch toward B only if Pub/Sub were unavailable or if the webhook needed a custom payload that Pub/Sub could not provide. Option C is the second trap, because log-based alerting sounds like a monitoring integration but delivers alerts, not build records.

**Foundation Concept**

Event-driven integration lets a source publish state changes and any number of consumers react without changing the source. Messaging services decouple producers from consumers, and push delivery turns messages into HTTP calls for webhook-style receivers. Prefer using the event stream a managed service already emits over adding code to the process that generates the events. This model works well for status and lifecycle events. Fine-grained custom data from inside a build step still requires explicit logic in that step.

**Real-World Connection**

A team creates a push subscription on the build topic that targets the monitoring vendor’s HTTPS endpoint with authentication enabled. Every build creation, progress, success, and failure then appears in the monitoring platform, including builds that fail early. The team maintains no scripts, and its main ongoing task is confirming the receiver handles the Pub/Sub message envelope. If the vendor cannot parse it, they can enable unwrapped delivery or place a small relay in front.

**Memory Hook**

Build events are already published to Pub/Sub, so a push subscription turns them into webhook calls without code.

**30-Second Exam Takeaway**

When a managed service already emits events and you need them in an external HTTP endpoint with low effort, choose Pub/Sub with a push subscription. Reject custom code in the pipeline and alerting features that do not carry the data.

**Official References**

[**Google Cloud — Cloud Build: Subscribe to build notifications:**](https://cloud.google.com/build/docs/subscribe-build-notifications) Supports: Cloud Build publishing build state changes to the cloud-builds topic and supporting push subscriptions that deliver messages to an endpoint, which supports option D and rules out options A and B.

[**Google Cloud — Pub/Sub push subscriptions:**](https://docs.cloud.google.com/pubsub/docs/push) Supports: push delivery sending messages to a webhook as an HTTPS POST request, in wrapped or unwrapped form, which supports the mechanism and the format boundary in option D.

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 2, Building and implementing CI/CD pipelines):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment with implementing and managing pipelines, including auditing and tracking deployments with Cloud Build.

</details>

---

### Exam 1 · Q55

Your organization provisions a Compute Engine managed instance group (MIG) through a Terraform-based CI/CD pipeline. The MIG runs an application using an instance template that generates unique names with `name_prefix`. The MIG’s Terraform resource directly references that template resource.

After you modify the machine type in the instance-template configuration, `terraform apply` fails with this error:
    
          1. Error waiting for Deleting Instance Template:
      2. The instance_template resource
      3. 'projects/example-project/global/instanceTemplates/app-template-202610310001'
      4. is already being used by
      5. 'projects/example-project/regions/us-central1/instanceGroupManagers/app-mig'

You must replace the template and update the MIG to reference its replacement while minimizing application disruption and additional pipeline executions.

Which action should you take?

- **A.** Destroy the MIG, replace the instance template with one containing the new machine type, and recreate the MIG using the replacement template.
- **B.** Perform separate pipeline executions to provision another instance template, switch the MIG to that template, and remove the previous template.
- **C.** Temporarily remove the MIG from Terraform state, apply the template replacement, and import the existing MIG back into state afterward.
- **D.** Configure `create_before_destroy = true` inside a `lifecycle` block on the instance-template resource, and run the pipeline again.

<details><summary>Answer &amp; explanation</summary>

**Correct:** **D.** Configure `create_before_destroy = true` inside a `lifecycle` block on the instance-template resource, and run the pipeline again.

**Correct Answer**

**D. Add a**`**lifecycle**`**block to the instance-template resource and set**`**create_before_destroy = true**`**, then rerun the pipeline.**

**Exam Reasoning Explanation**

The error identifies a replacement-ordering problem: Terraform attempts to delete a template that the MIG still references. Preserve the MIG and let Terraform coordinate the replacement within one apply operation. D addresses that ordering directly; A unnecessarily rebuilds the group, B requires additional runs, and C changes state bookkeeping without removing the cloud dependency.

**Key Exam Clues**

  * **“Already being used by” — Technical signal:** The existing MIG reference blocks template deletion.

  * **“**`**name_prefix**`**” — Technical signal:** The original and replacement templates can coexist under different names.

  * **“Directly references the template resource” — Technical signal:** Terraform can track the dependency and update the reference.

  * **“Minimizing application disruption” — Preference:** Avoid tearing down the MIG.

  * **“Number of pipeline runs” — Preference:** Prefer dependency-aware replacement within one apply.

**Why This Is Correct**

Instance templates are immutable, so changing the machine type requires a replacement. Add this block inside the existing instance-template resource:
    
          1. lifecycle {
      2.   create_before_destroy = true
      3. }

With the stated unique naming and direct reference, Terraform can:

  1. Create the replacement template.

  2. Update the MIG to reference it.

  3. Delete the original template after the reference changes.

The Google provider documentation explicitly recommends this configuration for instance templates used by instance group managers. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** Rebuilding the group removes the dependency but unnecessarily disrupts application capacity. Replacing the template does not require destroying the MIG.

  * **Option B — Technically Possible but Not Best:** The sequence is valid, but splitting it across pipeline runs adds coordination and intermediate configurations. D lets Terraform manage the required ordering declaratively.

  * **Option C — Incorrect:** Removing the MIG from state leaves the actual group and its template reference intact. The deletion blocker remains. If the MIG configuration stays present, Terraform can also plan to create another group, potentially encountering an existing-name conflict. 

**Exam Trap**

B describes the right operational sequence but misses that Terraform can execute it within one apply. Separate runs become reasonable when a changed requirement mandates independently approved creation, cutover, and cleanup stages.

Also, `**create_before_destroy**`**does not guarantee a disruption-free rollout of the new machine type to every existing VM** ; that depends on the MIG’s update configuration. 

**Foundation Concept**

Distinguish **replacement ordering** , **resource naming** , and **workload rollout**. Lifecycle rules control replacement ordering; unique names permit old and new resources to coexist; the MIG’s update policy controls how existing VMs adopt the new configuration. A fixed conflicting name could prevent creation even with `create_before_destroy` enabled. 

**Real-World Connection**

Use the lifecycle fix alongside an appropriate proactive MIG update policy when existing VMs must receive the new machine type automatically. Configure surge capacity, availability limits, and health checks to control disruption. Additional surge VMs require available capacity and can temporarily increase compute costs. 

**Memory Hook**

For an immutable resource with live dependents: create its replacement, redirect the dependents, then retire the original.

**30-Second Exam Takeaway**

When Terraform cannot delete an in-use template, look for `create_before_destroy`, compatible unique naming, and a direct resource reference. Resolve the dependency ordering while treating the application’s rolling update as a separate concern.

**Official References**

[**Terraform Google Provider — Instance Templates: Using with Instance Group Manager**](https://github.com/hashicorp/terraform-provider-google/blob/main/website/docs/r/compute_instance_template.html.markdown)

Supports: Template immutability, unique naming, and the create–update–delete sequence.

[**HashiCorp Terraform — Lifecycle Reference**](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle)

Supports: `create_before_destroy` behavior and coexistence constraints.

[**HashiCorp Terraform — terraform state rm**](https://developer.hashicorp.com/terraform/cli/commands/state/rm)

Supports: Why removing state does not remove the actual MIG or its cloud dependencies.

[**Google Compute Engine — Automatically Apply VM Configuration Updates in a MIG**](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups)

Supports: Proactive versus opportunistic updates, disruption controls, and surge-capacity trade-offs.

</details>

---

### Exam 2 · Q2

You’re building a CI/CD pipeline in Cloud Build that produces an application container image, with the source code hosted in GitHub. Company policy requires that production image builds run only against the main branch, and that the change control team must approve every push to the main branch. You also want the build itself to require as little manual intervention as possible. What should you do? (Choose two.)

- A. Create a Cloud Build trigger and set its repository event to Pull request.
- B. Add an OWNERS file to the trigger’s Included files filter.
- C. Create a Cloud Build trigger and set its repository event to Push to a branch, scoped to the main branch.
- D. Configure a branch protection rule on the main branch in the GitHub repository.
- E. Enable the manual Approval option on the Cloud Build trigger.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Create a Cloud Build trigger and set its repository event to Push to a branch, scoped to the main branch. **|** D. Configure a branch protection rule on the main branch in the GitHub repository.

**Correct Answer**

**C. Create a Cloud Build trigger and set its repository event to Push to a branch, scoped to the main branch.**

**D. Configure a branch protection rule on the main branch in the GitHub repository.**

**Exam Reasoning Explanation**

The scenario bundles two separate controls that must each land in the right system. “Builds only run against main” is a Cloud Build trigger-configuration concern — walking requirement → capability, a trigger whose event is Push to a branch, scoped with a branch regex matching only `main`, fires exactly when (and only when) commits land on main, fully automatically. “The change control team approves all pushes to main” is a source-control concern — it’s about gating what’s allowed to reach the main branch in the first place, which is exactly what a GitHub branch protection rule (requiring a pull request plus required approving reviews) enforces. Together, C handles the build-automation half and D handles the human-approval half, each in the system built for it — and neither one duplicates or interferes with the other’s job, which is why both are needed and why no third option is required.

**Key Exam Clues**

  * “production image builds are only run against the main branch” — a hard constraint on trigger scope: points to a Cloud Build trigger event configured for pushes to a specific branch.

  * “the change control team approves all pushes to the main branch” — a hard constraint on who can get code into main: points to a source-control-level gate (GitHub), not a build-level gate.

  * “as automated as possible” — a decisive preference that disqualifies any option that inserts a recurring manual step into the build execution itself.

  * “(Choose two)” — confirms the two requirements are solved by two distinct, complementary mechanisms rather than one option doing double duty.

**Why This Is Correct**

A Cloud Build trigger with the repository event set to Push to a branch starts a build automatically whenever a commit lands on the matched branch (here, main) — once configured, it requires no further human action per build, satisfying “as automated as possible” for the build itself. Separately, GitHub branch protection rules let repository administrators require that changes reach a protected branch only via a pull request, and that the pull request receive a specified number of approving reviews before it can be merged — this is precisely how a “change control team” enforces sign-off on everything that reaches main. Because the approval happens at the merge/PR stage (outside Cloud Build) and the build trigger fires automatically afterward (inside Cloud Build), the two together deliver full automation for the build while still enforcing human approval exactly where the policy requires it — on the path into main.

**Why the Other Options Are Not the Best Fit**

**Option A — _Different Use Case_.** A Pull request event triggers a build when a PR is opened or updated, which is well suited to running checks against proposed changes before merge — but the requirement is that _production_ image builds run against the main branch, which means after code has been approved and merged, not on every PR update against a feature branch.

**Option B — _Incorrect_. **The Included files filter controls whether a trigger fires based on which files changed (commonly used to scope triggers in a monorepo) — it has nothing to do with approvals. Pairing an OWNERS file with this filter doesn’t make Cloud Build enforce code-owner review; that capability (requiring review from code owners) lives in GitHub’s branch protection settings, not in a Cloud Build trigger’s file filter.

**Option E — _Violates Requirement_. **Cloud Build’s trigger-level approval setting pauses every single triggered build until a user with the Cloud Build Approver role manually approves it inside Cloud Build. That’s a real feature, but it adds a recurring manual step to every production build run — directly working against “as automated as possible” — and it approves the act of _building_ , not the act of _pushing to main_ , which is what the change control team is actually meant to govern.

**Exam Trap**

The trap is reaching for Cloud Build’s own approval feature (E) because the word “approve” appears in both the requirement and the Cloud Build UI. But the requirement’s approval is scoped to “pushes to the main branch” — a source-control event — not to build executions. Enabling Cloud Build approval would satisfy a differently-worded requirement (“require sign-off before every production build runs”), and it would do so at the cost of automation; the question explicitly prioritizes automation for the build step while placing the approval burden on the one place it belongs — the gate into main.

**Foundation Concept**

A secure, automated CI/CD pipeline typically separates two layers of control: a _code-governance_ layer (who can change what, and under what review requirements — enforced by the source-control platform, here GitHub) and a _build-automation_ layer (what happens once governed, approved code lands — enforced by the CI/CD tool, here Cloud Build). Approval requirements are usually best enforced as early and as close to the source of truth as possible (the merge gate), leaving the downstream build pipeline free to run without further manual checkpoints.

**Real-World Connection**

A platform team configures GitHub so that main is protected — no direct pushes, pull requests required, and at least one approval from a designated change-control reviewer — while Cloud Build watches main with a push-triggered pipeline that builds and pushes the production image the moment a PR lands. The operational result is a clean audit trail (every production image traces back to an approved, merged PR) with zero added latency in the build step itself. The trade-off is that this design puts all the protection at the merge gate; if someone with sufficient repository permissions could bypass the branch protection rule (for example, an admin with “include administrators” unchecked), the build would faithfully build whatever reaches main, so the strength of this design depends on the branch protection rule being configured to apply to everyone, including admins.

**Memory Hook**

“GitHub gates who merges, Cloud Build automates what builds” — approval belongs on the branch protection rule, automation belongs on the push trigger.

**30-Second Exam Takeaway**

When a question splits “only build from this branch” from “require approval before changes land,” expect two separate answers: a Cloud Build push trigger scoped to the branch for automation, and a GitHub (or equivalent source-control) branch protection/required-review rule for the human approval — never a Cloud Build trigger-level approval setting standing in for source-control governance.

**Official References**

[**Google Cloud — Create and manage GitHub App triggers:**](https://cloud.google.com/build/docs/create-github-app-triggers) Supports: the distinction between the Push to a branch and Pull request trigger events, and how a branch-scoped push trigger automates production builds

[Google Cloud — gcloud builds triggers create manual (--require-approval reference): ](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual)Supports: Cloud Build’s manual approval feature pauses each triggered build until a Cloud Build Approver approves it, clarifying why Option E governs build execution rather than branch access

[**GitHub Docs — About branch protection rules:**](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) Supports: branch protection rules can require a pull request and a specified number of approving reviews before changes reach a protected branch, which is the mechanism behind the correct answer’s change-control requirement

</details>

---

### Exam 2 · Q5

Your company operates a public Cloud Run service named `booking-engine`, accessible through HTTPS at https://booking-engine-abcdef.a.run.app.

Developers need to validate new revisions before those revisions receive customer traffic through the service’s standard URL. What should you do?

- A. Deploy using `gcloud run deploy booking-engine --no-traffic --tag dev` and test the revision at https://dev---booking-engine-abcdef.a.run.app.
- B. Run `gcloud run services update-traffic booking-engine --to-revisions LATEST=1` and test through https://booking-engine-abcdef.a.run.app.
- C. Include the header supplied by `curl -H "Authorization:Bearer $(gcloud auth print-identity-token)"` when requesting https://booking-engine-abcdef.a.run.app to test privately.
- D. Grant developers `roles/run.invoker` on `booking-engine` and test through https://booking-engine-abcdef.private.run.app.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Deploy using `gcloud run deploy booking-engine --no-traffic --tag dev` and test the revision at https://dev---booking-engine-abcdef.a.run.app.

**Correct Answer**

**A. Deploy using**`**gcloud run deploy booking-engine --no-traffic --tag dev**`**and test the revision at**[**https://dev---booking-engine-abcdef.a.run.app**](https://dev---booking-engine-abcdef.a.run.app)**.**

**Exam Reasoning Explanation**

The requirement concerns selecting an unreleased revision while preserving customer routing. Choose revision-specific access with no production traffic allocation. Authentication changes address who may invoke the service; a traffic split deliberately exposes customers to the new revision.

**Key Exam Clues**

  * **“New revisions” — technical signal:** Developers need revision-specific routing.

  * **“Before … customer traffic” — sequence constraint:** Keep the new revision outside the standard traffic allocation during testing.

  * **“Public Cloud Run service” — contextual signal:** Adding authentication headers alone does not select a different revision.

**Why This Is Correct**

`--no-traffic` deploys the revision without assigning it traffic from the standard service URL. `--tag dev` provides a dedicated URL that routes testing requests directly to that revision. Google documents this pattern for validating revisions before migrating customer traffic. 

**URL correction:** The supplied option’s tagged hostname needs **three hyphens** after `dev`: `dev---booking-engine-abcdef.a.run.app`. The revised option includes that correction. 

**Why the Other Options Are Not the Best Fit**

  * **Option B — Violates Requirement:** `LATEST=1` assigns 1% of service traffic to the latest revision. This is a customer-facing canary rollout, so customers can encounter the revision before developer validation finishes. 

  * **Option C — Different Use Case:** An identity token authenticates the caller when authentication is required. It does not change revision routing; requests to the standard URL follow the configured traffic allocation. It also does not make the existing public service private. 

  * **Option D — Incorrect:** Cloud Run Invoker authorizes service invocation. Granting it does not create a `.private.run.app` endpoint or select an unreleased revision. 

**Exam Trap**

**Zero production traffic allocation does not mean private access.** A traffic tag on this public service provides separate routing, without adding developer-only authentication. If the requirement instead called for testing with 1% of real customer traffic, option B would fit. 

**Foundation Concept**

Deployment, routing, and authorization are separate controls: deployment creates a version, routing selects the version that receives a request, and authorization determines whether the caller may invoke it.

**Real-World Connection**

Developers can run smoke tests against the `dev` URL while customers continue using the standard endpoint. After validation, the team can gradually migrate traffic to the tested revision. 

**Memory Hook**

Use a revision tag with zero standard traffic allocation to test before routing customers to it.

**30-Second Exam Takeaway**

Choose **A** , with the corrected three-hyphen URL. Use `--no-traffic` and a revision tag for pre-release testing; configure authentication separately when developer-only access is required.

**Official References**

  * **Google Cloud — Rollbacks, gradual rollouts, and traffic migration**

Supports: Tagged revision testing, `--no-traffic`, URL format, and percentage-based rollouts.

[Official documentation](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration)

  * **Google Cloud — Authenticate developers**

Supports: Cloud Run Invoker permissions and identity-token authentication.

[Official documentation](https://docs.cloud.google.com/run/docs/authenticating/developers)

  * **Google Cloud — Allowing public (unauthenticated) access**

Supports: Service-level public access controls and their distinction from revision routing.

[Official documentation](https://docs.cloud.google.com/run/docs/authenticating/public)

</details>

---

### Exam 2 · Q19

The latest version of your containerized application has passed testing and is ready for production on Google Kubernetes Engine (GKE). You were unable to fully load-test the new version in pre-production, so you need to make sure it does not introduce performance problems once it is deployed. The deployment must also be automated. What should you do?

- A. Deploy through a continuous delivery pipeline that uses a canary deployment, watch for performance issues in Cloud Monitoring, and increase traffic to the new version as the metrics support it.
- B. Deploy through a continuous delivery pipeline that uses a blue/green deployment, move traffic to the new version, and watch for performance issues in Cloud Monitoring.
- C. Deploy with kubectl, use Config Connector to gradually shift traffic between the versions, and watch for performance issues in Cloud Monitoring.
- D. Deploy with kubectl with the spec.updateStrategy.type field set to RollingUpdate, watch for performance issues in Cloud Monitoring, and run the kubectl rollback command if any issues appear.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Deploy through a continuous delivery pipeline that uses a canary deployment, watch for performance issues in Cloud Monitoring, and increase traffic to the new version as the metrics support it.

**Correct Answer**

**A. Deploy through a continuous delivery pipeline that uses a canary deployment, watch for performance issues in Cloud Monitoring, and increase traffic to the new version as the metrics support it.**

**Exam Reasoning Explanation**

Two must-have constraints decide this item: the deployment must be automated, and the release must be safe given that load testing was incomplete. Walking requirement → capability: because performance under real load is unknown, the strategy has to expose the new version to a small share of production traffic first, then widen exposure only when metrics look healthy. That is the canary pattern. Automation points to a continuous delivery pipeline rather than hand-run commands. Options that shift all traffic at once, rely on manual `kubectl`, or use a tool that is not a traffic manager fail one of those two constraints, leaving only option A.

**Key Exam Clues**

  * “could not fully load-test the new version in your pre-production environment” is a hard constraint. Performance risk is unresolved until real traffic hits the new version, so exposure must be limited at first.

  * “ensure that the application does not have performance problems after deployment” is a hard constraint. The strategy must include a metrics-driven check before the rollout widens.

  * “Your deployment must be automated” is a hard constraint. This favors a continuous delivery pipeline over manual `kubectl` steps.

  * “Use Cloud Monitoring to look for performance issues” is a technical signal. Every option monitors; the difference is how much traffic is exposed while you watch.

**Why This Is Correct**

A canary deployment sends a small percentage of traffic to the new version while the current version keeps serving the rest, so any performance regression affects only a fraction of users. You watch Cloud Monitoring, and if latency and resource metrics hold, you raise the percentage in stages until the new version carries all traffic. Cloud Deploy supports this on GKE, where a delivery pipeline stage defines canary phases with percentages and can run verification at each phase, and it manages the underlying Deployment and Service resources during the rollout. The pipeline makes the progression repeatable and automated, while the staged percentages give the real-traffic evidence that pre-production load testing could not.

**Why the Other Options Are Not the Best Fit**

**Option B is _Technically Possible but Not Best_.** Blue/green runs the new version alongside the old one and switches traffic to it. That gives fast rollback, but the option migrates traffic to the new version and only then looks for problems, so every user is exposed to any performance issue at once. It is tempting because it is also automatable and easy to reverse, but it does not limit the blast radius of an untested-under-load release.

**Option C is _Violates Requirement_.** Config Connector lets you manage Google Cloud resources through Kubernetes configuration, so it is not a mechanism for gradually shifting traffic between application versions. Pairing it with manual `kubectl` also fails the requirement for an automated deployment.

**Option D is _Violates Requirement_.** A rolling update replaces Pods gradually, but it does not hold back traffic according to performance metrics, and it starts from a manual `kubectl` deployment rather than an automated pipeline. The option’s details are also off: Kubernetes Deployments set their update strategy under `.spec.strategy.type`, not `spec.updateStrategy.type`, and the rollback command is `kubectl rollout undo`, since `kubectl rollback` is not a command.

**Exam Trap**

The trap is choosing blue/green (B) because it sounds like the safest, most mature strategy. Its safety comes from fast reversal after a problem is seen, whereas this question needs protection before most users are affected. If the stem said the new version had been fully load-tested but you needed zero downtime and an instant switch-back, blue/green would be the better answer. A second trap is treating a rolling update as a canary. It replaces Pods incrementally, but it does not tie the progression to the performance metrics you are watching.

**Foundation Concept**

Progressive delivery limits risk by controlling how much traffic a new version receives and by gating each increase on evidence. The main strategies differ in blast radius and reversal speed: rolling updates replace instances gradually, blue/green swaps whole environments, and canary exposes a slice of real traffic first. When you cannot validate a release under production-like load beforehand, the strategy should turn production itself into the test, in small, observed steps. Automation matters because manual traffic changes are slow and error-prone.

**Real-World Connection**

A team defines a Cloud Deploy pipeline with canary phases such as 10%, then 50%, then 100%, and watches latency and error dashboards in Cloud Monitoring between phases. If a phase shows degraded latency, they stop and roll back while only a small share of users saw the problem. The trade-off is a slower rollout and the need to run two versions side by side, which also requires the application to tolerate mixed versions, for example with compatible database schemas.

**Memory Hook**

Unproven under load means start small and widen on evidence: a canary through an automated pipeline.

**30-Second Exam Takeaway**

When a question says the release could not be fully tested for performance and the deployment must be automated, choose a canary deployment through a continuous delivery pipeline with metrics-gated ramp-up. Blue/green fits when instant switch-back matters more than limiting exposure, and manual `kubectl` options fail the automation requirement.

**Official References**

[**Google Cloud — Canary deployments to GKE and GKE attached clusters using service-based networking (Cloud Deploy):**](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/service-networking) Supports: Cloud Deploy canary strategies define percentage phases in a delivery pipeline stage and can enable verification on each phase, which is the automated, metrics-gated rollout in Option A

[**Google Cloud — Config Connector overview:**](https://docs.cloud.google.com/config-connector/docs/overview) Supports: Config Connector manages Google Cloud resources through Kubernetes tooling and APIs, which is why it is not a traffic-ramping mechanism for application versions (Option C)

[Kubernetes — Update a Deployment Without Downtime: ](https://kubernetes.io/docs/tasks/run-application/update-deployment-rolling/)Supports: rolling updates are configured under `.spec.strategy` on a Deployment and are rolled back with `kubectl rollout undo`, which clarifies the field and command errors in Option D

</details>

---

### Exam 2 · Q21 ❌ *you missed this*

You need to build a CI/CD pipeline in Google Cloud for a containerized application. Your development team practices trunk-based development with a central Git repository. You want every new version of the application to pass through all of your tests in the pipeline so that quality improves. What should you do?

- A. First, install a Git hook that requires developers to run unit tests before pushing code to the central repository. Second, trigger Cloud Build to build the application container, deploy it to a testing environment, and run integration tests. Third, if the integration tests pass, deploy the container to production and run acceptance tests.
- B. First, install a Git hook that requires developers to run unit tests before pushing code to the central repository, and build a container if all tests pass. Second, trigger Cloud Build to deploy the container to a testing environment and run integration tests and acceptance tests. Third, if all tests pass, tag the code as production ready, then trigger Cloud Build to build and deploy the application container to production.
- C. First, trigger Cloud Build to build the application container and run unit tests using that container. Second, if the unit tests pass, deploy the container to a testing environment and run integration tests. Third, if the integration tests pass, have the pipeline deploy the container to production, then run acceptance tests.
- D. First, trigger Cloud Build to run unit tests whenever code is pushed, and if all unit tests pass, build the application container and push it to a central registry. Second, trigger Cloud Build to deploy the container to a testing environment and run integration tests and acceptance tests. Third, if all tests pass, have the pipeline deploy the application to production and run smoke tests.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. First, trigger Cloud Build to run unit tests whenever code is pushed, and if all unit tests pass, build the application container and push it to a central registry. Second, trigger Cloud Build to deploy the container to a testing environment and run integration tests and acceptance tests. Third, if all tests pass, have the pipeline deploy the application to production and run smoke tests.

**Correct Answer**

**D. First, trigger Cloud Build to run unit tests whenever code is pushed, and if all unit tests pass, build the application container and push it to a central registry. Second, trigger Cloud Build to deploy the container to a testing environment and run integration tests and acceptance tests. Third, if all tests pass, have the pipeline deploy the application to production and run smoke tests.**

**Exam Reasoning Explanation**

Two must-have constraints decide this item: all tests must run _in the pipeline_ , and every test must pass before the release reaches production. Walking requirement → capability: a pipeline-run test is enforced for every push, while a developer-side hook is not. Test order should also run from cheapest to most expensive, so a failure stops the pipeline early. Finally, the artifact that passes the test stages should be the one that is deployed. Only option D puts unit tests in the pipeline, builds and stores a container once, runs integration and acceptance tests before production, and limits production to quick post-deploy checks.

**Key Exam Clues**

  * “run all your tests in the pipeline” is a hard constraint. Testing cannot depend on a step outside the pipeline, such as a local developer hook.

  * “trunk-based development” is a technical signal. Commits land frequently on one shared branch, so automated checks must trigger on each push rather than rely on individual discipline.

  * “any new versions of the application” is a hard constraint. Every version must pass the full set of tests, which means testing before production exposure.

  * “improve the quality” is a preference. The order of stages should catch defects early and keep untested code away from customers.

**Why This Is Correct**

Running unit tests in Cloud Build on every push makes the quality gate part of the shared pipeline, so it applies to every commit no matter whose machine produced it. Building the container only after unit tests pass avoids packaging code that already failed. Storing the image in a central registry gives the later stages one artifact to deploy. Deploying that container to a testing environment lets integration tests and acceptance tests exercise it in a production-like setting before any customer is affected. Only if all of those pass does the pipeline deploy to production, where short smoke tests confirm the release started correctly. This matches the shape Google documents for containerized apps: Cloud Build builds and tests, the container goes to Artifact Registry, it is deployed to staging, and then the same container is promoted to production.

**Why the Other Options Are Not the Best Fit**

**Option A is _Violates Requirement_.** It relies on a Git hook for unit tests, so those tests are not run in the pipeline. It also deploys to production before running acceptance tests, so a version that would fail acceptance reaches customers first.

**Option B is _Violates Requirement_.** Its unit-test gate is again a Git hook rather than a pipeline step. It also builds the production container a second time after the tests pass, so the artifact that reaches production is not the artifact that was tested. It is tempting because the test environment stage correctly includes both integration and acceptance tests.

**Option C is _Violates Requirement_.** Unit tests run in Cloud Build and integration tests run in a test environment, which is close to right. The flaw is the final step: it deploys to production and only then runs acceptance tests, so acceptance testing is not a gate for the release. Running unit tests inside the already-built container is also a slower point to catch failures than before the build.

**Exam Trap**

The trap is Option C, which looks nearly identical to D until the last step. Reading quickly, “Cloud Build, test environment, integration tests, production” seems right, but acceptance tests placed after production make customers the test audience. A second trap is treating a Git hook as a pipeline control. Git’s own documentation notes that client-side hooks are not copied when a repository is cloned and can be bypassed (for example with `--no-verify`), and that policy enforcement belongs on the server side. A pre-push hook would be a reasonable add-on if the goal were faster local feedback, but it cannot satisfy “in the pipeline.”

**Foundation Concept**

A trustworthy CI/CD pipeline orders its checks from fast and cheap to slow and broad: unit tests first, then integration tests against a deployed test environment, then acceptance tests, and only then production. Two principles support this. First, quality gates must live where they cannot be skipped, which is the shared pipeline. Second, build the artifact once and promote that same artifact through the environments, so what you tested is exactly what you ship. Post-deploy smoke tests are brief sanity checks, not a replacement for pre-production acceptance testing.

**Real-World Connection**

A team configures a Cloud Build trigger on pushes to the main branch. Unit tests run first; if they pass, the container is built and pushed to Artifact Registry, deployed to a staging cluster, and checked by integration and acceptance suites, with production deployment gated on success. Developers still get a quick local feedback loop, but the guarantee comes from the pipeline. The trade-off is pipeline run time: long acceptance suites delay releases, so teams parallelize tests and keep unit tests fast so that trunk-based commits are not blocked.

**Memory Hook**

Gates belong in the pipeline, run fast tests first, build once, and never put customers before acceptance tests.

**30-Second Exam Takeaway**

For “run all tests in the pipeline” questions, choose the option with CI-triggered unit tests, a single container build stored in a registry, integration and acceptance tests in a test environment, and production last. Reject options that rely on Git hooks or run acceptance tests after production.

**Official References**

[Google Cloud — CI/CD pipeline for developing and delivering containerized apps: ](https://docs.cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke)Supports: the recommended flow in which Cloud Build builds and tests, the container is stored in Artifact Registry and deployed to staging, and the same container is then promoted to production (Option D over A, B, and C)

[**Pro Git — Customizing Git: Git Hooks:**](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) Supports: client-side hooks are not copied when a repository is cloned and can be bypassed, and policy enforcement belongs on the server side, which is why a Git hook is not a pipeline gate (Options A and B)

[**Professional Cloud DevOps Engineer Exam Guide — Section 2.1, Designing pipelines:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment via “CI/CD of applications and infrastructure” and “CI/CD pipeline triggers” within the section on building and implementing CI/CD pipelines including continuous testing

</details>

---

### Exam 2 · Q22

You are defining the deployment and testing approach for a CI/CD pipeline on Google Cloud. The approach you choose must satisfy two requirements:

  * It must simplify release deployments and keep the time needed to roll back a release as short as possible.

  * It must let you validate changes against real production traffic while progressively widening the share of users exposed to the change.

Which deployment strategy and testing strategy should you select?

- A. Recreate deployment combined with canary testing
- B. Blue/green deployment combined with canary testing
- C. Rolling update deployment combined with A/B testing
- D. Rolling update deployment combined with shadow testing

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Blue/green deployment combined with canary testing

**Correct Answer**

**B. Blue/green deployment combined with canary testing**

**Exam Reasoning Explanation**

Treat the item as two independent filters, one per requirement, and keep only the option that passes both. Filter one concerns the deployment strategy: simple releases and the shortest rollback. Filter two concerns the testing strategy: real production traffic with gradually increasing user exposure. Evaluate each half separately, because every option pairs one deployment pattern with one testing pattern, and a single wrong half is enough to eliminate it. Only option B has a deployment half that gives near-instant rollback and a testing half that exposes users incrementally.

**Key Exam Clues**

  * “minimize the duration of deployment rollbacks” — hard constraint on the deployment half: favors a strategy where rollback is a traffic switch rather than a redeployment.

  * “Reduce the complexity of release deployments” — preference on the deployment half: favors a clean cutover between two whole versions over a gradual in-place version mix.

  * “real production traffic” — hard constraint on the testing half: eliminates any approach that relies on simulated or staging traffic only.

  * “gradual increase in the number of affected users” — hard constraint on the testing half: describes progressively widening exposure, which is the defining behavior of canary testing and not of shadow testing (no users affected) or A/B testing (condition-based segments).

**Why This Is Correct**

Blue/green deployment runs two identical environments: the current version (blue) keeps serving traffic while the new version (green) is deployed and verified, and a traffic switch at the load balancer then cuts over. That keeps releases simple, with no mixed-version fleet to reason about, and rollback is just pointing traffic back at the still-running blue environment, which is why it is documented as an instant rollback. Canary testing partially rolls out a change to a small share of live production traffic, compares it with a baseline, and increases exposure step by step, which satisfies the requirement for real traffic with a gradually growing number of affected users. The two strategies are complementary: blue/green provides the clean environments and fast fallback, and canary provides the progressive exposure.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Canary testing satisfies the testing half, but a recreate deployment shuts down the old version before starting the new one, which causes downtime and makes rollback slow because the previous version must be redeployed. It directly conflicts with minimizing rollback duration.

  * **Option C — Violates Requirement:** Rolling updates replace instances gradually in place, so rolling back means rolling forward again through the fleet, which is slower than a traffic switch, and the system runs mixed versions during the process. A/B testing also targets users under specific conditions to compare variants for experimentation, rather than progressively increasing the share of affected users, so both halves are a weaker fit.

  * **Option D — Violates Requirement:** Shadow testing mirrors real production traffic to the new version without affecting users’ responses, so there is no gradual increase in affected users at all, which contradicts the stated testing requirement. Pairing it with a rolling update also leaves rollback slower than a blue/green switch, so neither half matches.

**Exam Trap**

The strongest distractor is option C, because rolling updates are a common default on GKE and managed instance groups and A/B testing sounds like testing on real traffic with partial exposure. The distinction is that the question wants rollback speed (a traffic switch, not a fleet re-roll) and progressive exposure by percentage (canary, not condition-based experiments). If the requirement were instead to compare two variants for a specific user segment, A/B testing would become correct, and if the requirement were to test with no user impact at all, shadow testing would.

**Foundation Concept**

Deployment strategies define how a new version replaces the old one (recreate, rolling, blue/green), while testing strategies define how you gain confidence in it using live traffic (canary, A/B, shadow). They are separate decisions that are often combined. Rollback speed is determined by whether the old version is still running and traffic can be redirected, and risk is controlled by how much real traffic the new version receives. Blue/green’s cost is running duplicate environments, and it requires backward-compatible data and schema changes.

**Real-World Connection**

A team deploys a new release to a green environment behind the same load balancer, then shifts 5 percent of traffic to it, watches error rates and latency against the baseline, and raises the percentage in stages. If a metric degrades, they redirect all traffic to the blue environment within seconds instead of redeploying. The cost is temporarily paying for two environments, which is an acceptable trade-off for fast recovery and lower blast radius.

**Memory Hook**

Blue/green decides how fast you can undo a release; canary decides how many users you risk while testing it.

**30-Second Exam Takeaway**

When a question asks for fast rollback plus gradually increasing exposure to real traffic, evaluate the deployment half and the testing half separately. Blue/green gives the instant rollback, and canary gives the progressive production exposure. Shadow means no user impact, and A/B means condition-based segments.

**Official References**

[**Google Cloud — Application deployment and testing strategies:**](https://docs.cloud.google.com/architecture/application-deployment-and-testing-strategies) Supports: the correct-answer mechanism (blue/green cutover with instant rollback via traffic redirection, and canary testing on live production traffic) and the elimination of the recreate, rolling, A/B, and shadow pairings

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment to Section 2.2, “Implementing and managing pipelines,” which lists deployment strategies (canary, blue/green, rolling, traffic splitting, feature flags)

</details>

---

### Exam 2 · Q28

Your organization requires a change advisory board (CAB) to approve every change made to an existing service. You want to redesign this process so that it no longer has a negative effect on software delivery performance. Which two actions should you take? (Choose two.)

- A. Replace the CAB with a senior manager who provides continuous oversight from development through deployment.
- B. Allow developers to merge their own changes, provided the team’s deployment platform can roll back changes if problems are found.
- C. Adopt a peer-review-based process for individual changes that is enforced at code check-in and backed by automated tests.
- D. Group changes into larger, less frequent software releases.
- E. Make sure the team’s development platform gives developers fast feedback on the impact of their changes.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Adopt a peer-review-based process for individual changes that is enforced at code check-in and backed by automated tests. **|** E. Make sure the team’s development platform gives developers fast feedback on the impact of their changes.

**Correct Answer**

**C. Adopt a peer-review-based process for individual changes that is enforced at code check-in and backed by automated tests.**

**E. Make sure the team’s development platform gives developers fast feedback on the impact of their changes.**

**Exam Reasoning Explanation**

Begin with the hard constraint: whatever replaces the CAB must not slow delivery, so any option that keeps approval in the hands of people outside the team, or that increases risk per release, fails it. Then ask what control the CAB was providing, which is catching bad changes before they cause harm, and look for practices that deliver that control inside the team’s normal workflow. Because two answers are required, look for a complementary pair: one that gates changes at the point of check-in and one that shortens the loop for detecting problems. Only options C and E form that pair.

**Key Exam Clues**

  * “change advisory board (CAB) to approve all changes” — technical signal: an external approval gate, which DORA research associates with worse delivery performance.

  * “eliminate any negative impact on the software delivery performance” — hard constraint: the replacement controls must be lightweight and owned by the team so they do not add waiting time.

  * “(Choose two.)” — cardinality instruction: select a complementary pair of practices, not two alternatives for the same job.

  * “existing service” — context clue: changes are ongoing and incremental, which favors per-change review and automation over scheduled approval meetings.

**Why This Is Correct**

Option C replaces the CAB’s gatekeeping with peer review enforced when code is checked in and supported by automated tests. This keeps a genuine approval step and segregation of duties, since a second person reviews each change, while the review, comments, and approvals are recorded in the team’s development platform. Automated tests then catch many defects before a human spends time on them. Option E supplies the second half: when developers see the effect of their changes quickly, through continuous integration results, monitoring, and observability, bad changes are detected and corrected early instead of waiting for a committee. DORA’s research describes this same combination, peer review supplemented by automation for early detection, visibility, and fast feedback. The two work together rather than independently: C prevents and filters changes at check-in, and E detects and corrects what slips through, so the pair covers both prevention and detection without any external gate.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** A senior manager is another approval step performed by someone outside the team, so it keeps the same bottleneck under a different name. It is tempting because it appears to simplify the process, but DORA found that both CABs and senior-manager approvals have a negative impact on delivery performance.

  * **Option B — Technically Possible but Not Best:** Rollback capability does reduce the cost of mistakes, and self-merging removes waiting time, which makes this option appealing. It loses because it drops peer review, the control DORA identifies as the preferred approval mechanism, and it relies on recovery after problems reach production rather than on catching them at check-in.

  * **Option D — Violates Requirement:** Larger, less frequent releases carry more changes each, which makes defects harder to isolate, raises the risk of every release, and delays feedback. DORA’s guidance points the opposite way, toward working in small batches for shorter lead times and faster feedback loops.

**Exam Trap**

The trap is Option B, because it sounds like modern DevOps: trust developers and rely on rollback. The distinction is that rollback is a recovery mechanism, whereas the question asks for a replacement approval process, and peer review is the practice that serves that role. If the option had said developers merge their own changes after peer approval and passing automated checks, it would align with the recommended approach.

**Foundation Concept**

Change risk is best managed by making changes small, reviewing them close to where they are written, automating detection of problems, and shortening feedback loops, not by adding an approval layer far from the work. The role of risk and compliance functions shifts from gatekeeper to designer of the process and provider of information. Exam framing aside, this also applies in regulated environments, where peer review records in the development platform can serve as audit evidence.

**Real-World Connection**

A team enforces branch protection so that every change needs at least one peer approval and passing automated tests before it can merge. After deployment, dashboards and alerts show the effect of each change within minutes. Approval history lives in the pull request record, which auditors can inspect, and lead time drops from the cycle of a weekly board meeting to hours. The main investment is keeping the test suite reliable, since flaky tests would erode trust in the gate.

**Memory Hook**

Peer review gates the change and fast feedback catches what slips through, with no external gatekeeper.

**30-Second Exam Takeaway**

When asked how to improve on a CAB or other external approval process, choose in-team peer review backed by automated tests, together with fast feedback on change impact. Reject swapping one external approver for another, merging with no review, and batching changes into larger releases.

**Official References**

[**DORA — Streamlining change approval:**](https://dora.dev/capabilities/streamlining-change-approval/) Supports: the correct-answer mechanism for options C and E (peer review enforced at check-in, supported by automation and fast feedback) and the elimination of Option A (CAB and senior-manager approvals hurting delivery performance)

[**Google Cloud — DevOps capabilities (DORA):**](https://docs.cloud.google.com/architecture/devops) Supports: the capability overview, including streamlining change approval through peer review and working in small batches for shorter lead times and faster feedback, which eliminates Option D

</details>

---

### Exam 2 · Q29

Your organization is developing and releasing a microservice on Cloud Run that many internal applications depend on. You are shipping a new release and must test it thoroughly in both the staging and production environments, while keeping the impact on service consumers and on developers as low as possible. What should you do?

- A. Deploy the new release to the staging environment and split traffic so that 1% reaches the latest version. Run your tests against it. If they succeed, progressively roll the latest version out to both the staging and production environments.
- B. Deploy the new release to the staging environment and split traffic so that 50% reaches the latest version. Run your tests against it. If they succeed, route all traffic to the latest version, then repeat the process in the production environment.
- C. Deploy the new release to the staging environment with a new-release tag and no traffic assigned. Run your tests against the tagged version. If they succeed, progressively roll out the tagged version, then repeat the process in the production environment.
- D. Create a new environment tagged green to serve as the staging environment and deploy the new release there for testing. If the tests succeed, route all traffic to the green environment and delete the existing staging environment, then repeat the process in the production environment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Deploy the new release to the staging environment with a new-release tag and no traffic assigned. Run your tests against the tagged version. If they succeed, progressively roll out the tagged version, then repeat the process in the production environment.

**Correct Answer**

**C. Deploy the new release to the staging environment with a new-release tag and no traffic assigned. Run your tests against the tagged version. If they succeed, progressively roll out the tagged version, then repeat the process in the production environment.**

**Exam Reasoning Explanation**

Rank the options by how much real user traffic the new version touches before it has been tested. The requirement to minimize user impact makes that the deciding variable, and the requirement to minimize developer impact penalizes anything that adds rebuilding or environment-management effort. Option C is the only one where testing happens with zero user exposure, and traffic only moves after the tests pass. Options A and B expose users first, and Option D creates heavy rework in the name of safety.

**Key Exam Clues**

  * “minimize user and developer impact” — hard constraint with two sides: no untested exposure for users, and a lightweight workflow for developers.

  * “test the new version extensively” — technical signal: testing needs a stable, directly addressable endpoint, not a sampled share of live traffic.

  * “Cloud Run” — technical signal: revision tags and traffic splitting are native features, so no extra environment is needed.

  * “staging and production environments” — sequence instruction: the same safe pattern must be repeated in each environment, in order.

**Why This Is Correct**

Cloud Run lets you deploy a new revision with no traffic assigned and attach a tag to it. The tag gives that revision its own dedicated URL, so you can run extensive tests against it without any user or consuming application reaching it. After the tests pass, you shift traffic to the tagged revision in increments, watching error and latency signals, and you can send traffic back to the previous revision immediately if something looks wrong. Because this uses built-in revision features on the existing service, developers do not have to build or tear down parallel environments. Repeating the same sequence in production gives the same safety there.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** A 1% split limits blast radius, but real users are still routed to a version that has not been tested yet, which conflicts with minimizing user impact. It also states that the gradual rollout proceeds to both staging and production at once, which skips the separate validation of production. It is tempting because 1% sounds harmless, but “extensive testing” cannot be done reliably on a thin slice of live traffic.

  * **Option B — Violates Requirement:** Sending half of the traffic to an untested version is the highest-risk choice, and the jump from 50% straight to all traffic abandons a gradual rollout. It maximizes user impact, so it contradicts the main requirement.

  * **Option D — Technically Possible but Not Best:** A green environment gives strong isolation and would protect users, which makes it tempting. However, standing up a whole new environment, switching all traffic at once, and deleting the existing staging environment each cycle adds heavy and unnecessary work for developers, and deleting staging eliminates the stable baseline. It is a different pattern than what Cloud Run provides natively through tagged revisions and traffic splitting.

**Exam Trap**

The strongest distractor is Option A, because small-percentage traffic splitting is the textbook “gradual rollout” and the 1% figure looks safe. The subtle point is that the question asks for extensive testing with minimal user impact, which means testing must happen before any traffic is assigned. If the requirement were instead to validate behavior under real production load with limited exposure, a small initial traffic split would become the right first step.

**Foundation Concept**

Separating deploy from release is a core progressive-delivery idea: a new version can exist, be reachable for testing, and receive no user traffic until you decide to release it. Cloud Run implements this with immutable revisions, tags that create direct test URLs, and percentage-based traffic assignment. Testing first through a tag, then shifting traffic gradually, combines the safety of a staging check with the controlled exposure of a canary.

**Real-World Connection**

A platform team deploys each release with no traffic and a tag, then runs integration and load tests against the tag’s URL while consuming applications continue using the stable revision. They then move traffic in steps while watching dashboards, and revert in seconds by sending traffic back to the previous revision if a metric degrades. Developers need only a single command per step rather than provisioning duplicate environments.

**Memory Hook**

On Cloud Run, deploy with no traffic and a tag, test on the tag’s URL, then shift traffic gradually.

**30-Second Exam Takeaway**

When a Cloud Run question asks for extensive testing with minimal user impact, choose a no-traffic revision with a tag, test via its direct URL, and then roll out gradually. Reject options that send untested code to real users, even at small percentages, or that rebuild whole environments.

**Official References**

[**Google Cloud — Rollbacks, gradual rollouts, and traffic migration (Cloud Run):**](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration) Supports: the correct-answer mechanism (deploying a revision with no traffic, tagging it for a dedicated test URL, then gradually shifting traffic) and the elimination of Options A, B, and D

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment to Section 2.2, “Implementing and managing pipelines,” which covers deployment strategies such as canary, blue/green, rolling, and traffic splitting

</details>

---

### Exam 2 · Q30

Your team recently moved an application onto Google Kubernetes Engine (GKE) and is now preparing to ship an updated version. The release approach must let you revert to the earlier version immediately if the update proves faulty. Which deployment model fits best?

- A. Roll out the update with a rolling deployment, then run tests on the new application after the rollout completes.
- B. Use A/B testing, and run tests on the application at regular intervals after the rollout completes.
- C. Use a canary deployment, and test the new application at regular intervals after the new version is live.
- D. Use a blue/green deployment, and test the new application after the rollout completes.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Use a blue/green deployment, and test the new application after the rollout completes.

**Correct Answer**

**D. Use a blue/green deployment, and test the new application after the rollout completes.**

**Exam Reasoning Explanation**

Only one requirement carries weight here: rollback must be instant. Turn that into a mechanical test. For each option, ask whether going back means reversing a process that took time (not instant) or flipping traffic to a version that is still fully running (instant). The testing phrases in each option are secondary, because the question asks which deployment model to use. Applying the test leaves a single option in which the previous version stays intact and live during the release.

**Key Exam Clues**

  * “instantly roll back” — hard constraint: eliminates models where rollback means undoing a gradual replacement or redeploying the old version.

  * “previous version” — technical signal: the old version must still be running and reachable so traffic can be returned to it.

  * “Which deployment model” — scope clue: the question targets how a release replaces the old version, not how it is tested, which separates it from A/B testing and canary testing.

**Why This Is Correct**

Blue/green deployment maintains two identical environments. The current version (blue) keeps serving users while the new version (green) is deployed alongside it, and the release happens by switching traffic from one to the other, usually at the load balancer or Service level. Because blue is left running until you choose to retire it, a rollback is simply a routing change back to blue, which is why Google documents blue/green as offering instant rollback along with zero-downtime cutover. On GKE this typically means two parallel Deployments with a traffic switch between them.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** A rolling deployment swaps Pods in batches, leaving a mix of old and new versions during the process. It is tempting because it is the Kubernetes default and can be reversed, but reversing means rolling back through the same staged replacement, which is neither instant nor clean.

  * **Option B — Different Use Case:** A/B testing sends defined user segments to a variant to compare behavior under specific conditions, so it is an experimentation technique and not a way to release a version with a full-fleet fallback. It is tempting because two versions run simultaneously, but it does not provide the instant, complete revert the question requires.

  * **Option C — Technically Possible but Not Best:** A canary deployment shifts a small share of live traffic to the new version, increasing it over time, and traffic can be moved back quickly, which makes it a close second. It loses because its rollback is described as fast rather than instant, and its design goal is progressive exposure of real users to a version still being evaluated.

**Exam Trap**

The tempting wrong answer is canary (Option C), since it also supports quick reversion and is widely associated with safe releases. The deciding word is “instantly”: blue/green keeps a complete idle copy of the old version, whereas canary is built around gradual user exposure. If the question instead asked for progressively increasing the share of real traffic that reaches the new version, canary would be correct.

**Foundation Concept**

How fast you can roll back depends on whether the prior version is still running and how traffic is directed to it. Blue/green keeps two full environments and swaps traffic between them, trading duplicate capacity cost for the fastest, simplest revert. Rolling and canary approaches conserve resources by replacing or shifting capacity incrementally, so reverting takes longer. Deployment models (how one version replaces another) are separate from testing strategies (how confidence is built), which is why the testing wording in each option does not change the answer. In production practice, you would usually verify the green environment before cutting traffic over, but the exam item turns on the deployment model.

**Real-World Connection**

A team deploys the updated version as a second set of Pods beside the live one, checks it through an internal endpoint, and then repoints the Service or load balancer to it. If an unexpected error appears after cutover, they restore the original routing within moments and investigate without pressure. The cost is paying for duplicate capacity during the release, and data schema changes must stay compatible with both versions so the switch back is safe.

**Memory Hook**

Instant rollback requires the old version to still be running, and only blue/green guarantees that.

**30-Second Exam Takeaway**

If a question stresses an instant revert of a release, choose blue/green. Choose canary when it stresses gradual exposure of real traffic, and remember that A/B testing is a segment-based experimentation technique, not a release model.

**Official References**

[**Google Cloud — Application deployment and testing strategies:**](https://docs.cloud.google.com/architecture/application-deployment-and-testing-strategies) Supports: the correct-answer mechanism (blue/green cutover with instant rollback by redirecting traffic) and the distinctions that eliminate the rolling, A/B, and canary options

[Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide: ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment to Section 2.2, “Implementing and managing pipelines,” which lists deployment strategies such as canary, blue/green, rolling, and traffic splitting

</details>

---

### Exam 2 · Q36

Your organization runs a containerized web application on-premises. As part of its migration to Google Cloud, you must choose a deployment strategy and a platform that satisfy all of the following acceptance criteria:

  1. The platform can route traffic from Android devices to an Android-specific microservice.

  2. The platform supports arbitrary percentage-based traffic splitting.

  3. The deployment strategy supports continuous testing of multiple versions of any microservice.

What should you do?

- A. Release a canary of the application on Cloud Run, and use traffic splitting to send 10% of user traffic to the canary according to the revision tag.
- B. Release a canary of the application on App Engine, and use traffic splitting to send a subset of user traffic to the new version according to the IP address.
- C. Release a canary of the application on Compute Engine, and use Cloud Service Mesh with Compute Engine to send 10% of user traffic to the canary by configuring the virtual service.
- D. Release a canary on Google Kubernetes Engine (GKE) with Cloud Service Mesh, and use traffic splitting to send 10% of user traffic to the new version according to the user-agent header configured in the virtual service.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Release a canary on Google Kubernetes Engine (GKE) with Cloud Service Mesh, and use traffic splitting to send 10% of user traffic to the new version according to the user-agent header configured in the virtual service.

**Correct Answer**

**D. Release a canary on Google Kubernetes Engine (GKE) with Cloud Service Mesh, and use traffic splitting to send 10% of user traffic to the new version according to the user-agent header configured in the virtual service.**

**Exam Reasoning Explanation**

Treat the three acceptance criteria as independent filters and require every option to pass all of them. Criterion 1 is the most discriminating, because it needs routing based on a property of the request, such as the kind of client, which is more than a percentage split. Criterion 2 then requires weighted routing with arbitrary percentages, and criterion 3 requires version-level control for each microservice, not just for the application as a whole. Applying the filters in that order leaves one option that identifies Android clients, applies weights, and works per microservice.

**Key Exam Clues**

  * “direct traffic from Android devices to an Android-specific microservice” — hard constraint: the platform must make routing decisions from request attributes such as the user-agent header.

  * “arbitrary percentage-based traffic splitting” — hard constraint: weighted routing with freely chosen percentages is required, not fixed shards or per-user stickiness.

  * “continuous testing of multiple versions of any microservice” — technical signal: routing control must be available per microservice and per version, which points to a service mesh.

  * “containerized web application” — context clue: a container platform such as GKE is a natural fit and keeps migration effort low.

**Why This Is Correct**

Cloud Service Mesh on GKE uses Istio-style traffic management. A VirtualService can match on request headers, such as the user-agent that identifies Android clients, and route those requests to a specific microservice, which satisfies criterion 1. The same resource assigns weights to destinations, so a canary can receive 10% or any other percentage and be adjusted gradually, which satisfies criterion 2. Because the rules are defined per service and per version subset, any number of microservice versions can run side by side and be tested continuously, which satisfies criterion 3. The routing happens in the mesh’s proxies, so the application code does not need to change.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Cloud Run assigns traffic by percentage across revisions and uses tags to give a revision its own test URL, which is tempting because it handles canaries well. However, its own traffic splitting does not inspect request headers such as user-agent, so it cannot steer Android clients to a dedicated microservice.

  * **Option B — Violates Requirement:** App Engine splits traffic by IP address or cookie, and an IP address does not identify an Android device. Google also documents that IP-based splits are imprecise and that users on mobile networks can shift IP addresses during a session, so it fails criterion 1 and weakens criterion 2.

  * **Option C — Technically Possible but Not Best:** A service mesh with a virtual service is the right family of tool, which is why this is the strongest distractor. It loses because the option configures only a percentage split and gives no rule for identifying Android traffic, and it places a containerized microservice application on VMs, which adds management overhead compared with GKE.

**Exam Trap**

The trap is Option C, because it names the right tool, Cloud Service Mesh with a virtual service, and satisfies the percentage requirement. The subtle point is that criterion 1 asks for attribute-based routing, which only Option D states. If criterion 1 were removed and the question only required a gradual percentage rollout, Cloud Run’s revision-based traffic splitting would become the simpler and defensible answer.

**Foundation Concept**

Platform-native traffic splitting, such as App Engine versions or Cloud Run revisions, operates at the granularity of a service and divides traffic by percentage, cookie, or IP address. A service mesh moves routing into a proxy layer that can inspect request attributes, such as headers and paths, and apply weights per service and version. When requirements combine content-aware routing with fine-grained, per-microservice version control, the mesh is the appropriate layer.

**Real-World Connection**

A retailer moves its containerized storefront to GKE with Cloud Service Mesh. A virtual service routes requests whose user-agent indicates Android to the Android microservice, while a second rule sends 90% of the remaining traffic to the stable version and 10% to the canary. Operators adjust weights over time and run several versions in parallel. The trade-off is added mesh operations and proxy resource overhead, and user-agent values can be spoofed, so they suit routing but not security decisions.

**Memory Hook**

Route by what the request says and by how much with a mesh virtual service, headers for who and weights for how many.

**30-Second Exam Takeaway**

When requirements demand routing by a request attribute, such as device type, together with arbitrary weights per microservice version, choose a service mesh on GKE. Platform-native splitting alone gives percentages, cookies, or IP addresses, not header-aware routing.

**Official References**

[**Google Cloud — Cloud Service Mesh by example: canary deployments:**](https://cloud.google.com/service-mesh/docs/tutorials/canary-deployment) Supports: the correct-answer mechanism, showing canary rollouts with weighted VirtualService routing on GKE using Cloud Service Mesh and Istio APIs

[**Istio — VirtualService reference:**](https://istio.io/latest/docs/reference/config/networking/virtual-service/) Supports: the ability of a VirtualService to match requests on headers such as user-agent and to assign weights to destinations, which satisfies criteria 1 and 2 in option D and distinguishes option C

[**Google Cloud — App Engine splitting traffic:**](https://docs.cloud.google.com/appengine/docs/flexible/splitting-traffic) Supports: the elimination of Option B, since App Engine splits by IP address or cookie and documents the limits of IP-based splitting for mobile users

[**Google Cloud — Cloud Run rollbacks, gradual rollouts, and traffic migration:**](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration) Supports: the elimination of Option A, since Cloud Run splits traffic by percentage across revisions and uses tags for direct test URLs rather than request-header routing

</details>

---

### Exam 2 · Q39

You are ready to release a new feature of a web-based application to production. You want to use Google Kubernetes Engine (GKE) to perform a phased rollout that first reaches half of the web server pods. What should you do?

- A. Use a partitioned rolling update.
- B. Use node taints with the NoExecute effect.
- C. Use a ReplicaSet in the Deployment specification.
- D. Use a StatefulSet with the Parallel pod management policy.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Use a partitioned rolling update.

**Correct Answer**

**A. Use a partitioned rolling update.**

**Exam Reasoning Explanation**

Convert the requirement into a capability: the update must stop partway, after exactly half the pods have the new version, and then be continued deliberately. So look for a native Kubernetes setting that defines a boundary inside a rolling update. Then test each option against what it actually controls. Taints control which pods may run on which nodes, ReplicaSets control how many pods exist, and pod management policy controls how pods are created or deleted when scaling. Only one option controls which subset of pods receives an update.

**Key Exam Clues**

  * “phased rollout” — technical signal: the update must proceed in stages with a deliberate stopping point, not all at once.

  * “half of the web server pods” — hard constraint: the mechanism must let you choose the exact subset that receives the new version.

  * “Google Kubernetes Engine (GKE)” — context clue: the solution should use native Kubernetes workload settings available on GKE, without extra tooling.

**Why This Is Correct**

A StatefulSet’s RollingUpdate strategy accepts a `partition` value. Pods with an ordinal greater than or equal to the partition are updated to the new template, while lower-ordinal pods stay on the previous revision. With N replicas, setting the partition to N/2 updates the upper half and leaves the lower half untouched, and lowering the partition afterwards, finally to 0, continues the rollout to the rest. GKE’s rolling update documentation describes partitioning as useful for staging an update, rolling out a canary, or performing a phased rollout, which is exactly the stated need. One boundary is that partitioning is a feature of StatefulSets, not of Deployments.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Different Use Case:** A NoExecute taint evicts running pods that do not tolerate it from a node. It is tempting because removing pods from some nodes sounds like targeting a subset, but it is node-level scheduling and eviction control and does not deploy a new version to a chosen share of pods.

  * **Option C — Technically Possible but Not Best:** A ReplicaSet keeps a specified number of pod replicas running, and a Deployment uses ReplicaSets to perform rolling updates. Neither offers a setting that halts an update at half the pods. You could approximate a split by running two ReplicaSets with different replica counts, but that is a manual workaround and not a built-in phased rollout control.

  * **Option D — Different Use Case:** The Parallel pod management policy lets a StatefulSet launch or terminate pods without waiting on each other, and Kubernetes documents it as affecting scaling operations. It is tempting because it appears in the same resource type, but it provides no stopping point for an update and does not select a subset of pods.

**Exam Trap**

The strongest distractor is Option D, because it also involves a StatefulSet setting and “parallel” can sound like acting on subsets of pods. The distinction is that pod management policy governs how pods are created and deleted when scaling, whereas partition governs which pods receive an update. If the requirement were to scale a StatefulSet up or down quickly without ordered waiting, Parallel pod management would be the correct choice.

**Foundation Concept**

A rolling update replaces pods incrementally, and a phased rollout adds a controllable pause so that part of the fleet runs the new version while you observe it. Kubernetes expresses that pause through update-strategy parameters such as the StatefulSet partition. Exam framing differs from common production practice here: web servers are usually stateless and run as Deployments, where phased rollouts are typically done with two Deployments behind one Service, traffic splitting in a service mesh, or a delivery tool such as Cloud Deploy, because Deployments have no partition setting.

**Real-World Connection**

A team running a StatefulSet with eight replicas sets the partition to four and applies the new template, so only the upper four pods update. They watch error rate and latency, ideally against an SLO burn-rate alert, then lower the partition to zero to finish the rollout, or revert the template if signals degrade. The blast radius stays limited to half the pods during the observation window, though the traffic share reaching the new version depends on how requests are distributed among pods.

**Memory Hook**

The partition sets the line: pods at or above that ordinal get the update, and the rest stay put.

**30-Second Exam Takeaway**

When a Kubernetes question asks for an update to reach only part of a workload’s pods before continuing, choose a partitioned rolling update. Taints control scheduling and eviction, ReplicaSets control replica counts, and pod management policy controls scaling behavior.

**Official References**

[Kubernetes — StatefulSets (rolling updates, partitions, and pod management policy): ](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)Supports: the correct-answer mechanism (the RollingUpdate partition that updates only pods at or above a given ordinal) and the elimination of Option D (pod management policy documented as affecting scaling operations)

[**Kubernetes — Taints and Tolerations:**](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) Supports: the elimination of Option B, since NoExecute taints evict non-tolerating pods from nodes and are scheduling controls, not rollout controls

[**Kubernetes — ReplicaSet:**](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) Supports: the elimination of Option C, since a ReplicaSet maintains a number of pod replicas and Deployments build rolling updates on top of it without a built-in halfway stop

[Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide: ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment to Section 2.2, “Implementing and managing pipelines,” which lists deployment strategies such as canary, blue/green, rolling, and traffic splitting

</details>

---

### Exam 2 · Q45

You use Cloud Build to build and deploy your application. You want to incorporate database credentials and other application secrets into the build pipeline securely, while keeping development effort to a minimum. What should you do?

- A. Create a Cloud Storage bucket that relies on built-in encryption at rest, store the secrets in it, and grant Cloud Build access to the bucket.
- B. Encrypt the secrets and keep them in the application repository, keep the decryption key in a separate repository, and grant Cloud Build access to that repository.
- C. Encrypt the secrets on the client side and store them in a Cloud Storage bucket, keep the decryption key in the same bucket, and grant Cloud Build access to the bucket.
- D. Use Cloud Key Management Service (Cloud KMS) to encrypt the secrets and reference them in your Cloud Build deployment configuration, and grant Cloud Build access to the key ring.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Use Cloud Key Management Service (Cloud KMS) to encrypt the secrets and reference them in your Cloud Build deployment configuration, and grant Cloud Build access to the key ring.

**Correct Answer**

**D. Use Cloud Key Management Service (Cloud KMS) to encrypt the secrets and reference them in your Cloud Build deployment configuration, and grant Cloud Build access to the key ring.**

**Exam Reasoning Explanation**

There are two hard constraints: the secrets must be protected in a way that holds up under access to the places they are stored, and the solution must need little custom development. Evaluate protection by asking what someone who can read the storage location can see, and evaluate effort by asking whether Cloud Build can consume the secret natively or whether you must write your own retrieval and decryption logic. Options that store keys next to ciphertext, or that rely on default storage encryption, fail the protection test. Options that require hand-built cryptography fail the effort test. One option uses a managed key service that Cloud Build already integrates with.

**Key Exam Clues**

  * “securely incorporate database credentials and other application secrets” — hard constraint: the secrets must never sit in readable form where broad access exists, and decryption must be controlled by access to a key.

  * “minimize the development effort” — hard constraint: the approach should use native Cloud Build integration, not custom encryption and decryption scripts.

  * “Cloud Build” — technical signal: Cloud Build can decrypt Cloud KMS-encrypted values at build time and inject them into build steps.

  * “build pipeline” — context clue: the need is for build-time secret injection into specific steps.

**Why This Is Correct**

Cloud KMS lets you encrypt each secret with a key you control. You place the encrypted value in the Cloud Build configuration under `availableSecrets`, together with the name of the key that decrypts it, and a build step receives the decrypted value as an environment variable through `secretEnv`. Cloud Build decrypts it while the build runs, so the plaintext is not stored in the repository or in a bucket. The build’s service account needs the Cloud KMS CryptoKey Decrypter role on the key, which means access to the secret is governed by IAM on the key and not by who can read a file. The integration is native, so the development effort is a configuration change and not custom code. One boundary is that the ciphertext is only as safe as the key’s access controls, so key permissions must be kept tight.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Cloud Storage encrypts data at rest by default, which makes this sound secure, but that protects the disks and not against anyone authorized to read the bucket, who would see the secrets as plaintext objects. The build would also need custom steps to fetch and handle them.

  * **Option B — Violates Requirement:** Keeping ciphertext in one repository and the key in another is hand-rolled key management. Repositories are not designed as key stores, many developers typically have read access, and the build needs custom decryption code, which adds effort without the controls of a managed key service.

  * **Option C — Violates Requirement:** Storing the decryption key in the same bucket as the encrypted secrets defeats the encryption, because anyone with access to the bucket gets both. Custom client-side cryptography also takes significant effort to build and maintain.

**Exam Trap**

The strongest distractor is Option A, because “built-in encryption at rest” sounds like the secure and low-effort choice. The distinction is that default storage encryption is automatic for all data and does not restrict what authorized readers can see, so it does not make a bucket a secret store. If the bucket held non-sensitive build artifacts, default encryption would be sufficient.

**Foundation Concept**

Encryption protects data only if access to the key is controlled separately from access to the ciphertext. Managed key services, such as Cloud KMS, provide that separation through IAM, and CI/CD systems with native integrations can decrypt at the point of use, a pattern called build-time secret injection. Secrets should never be stored in plaintext in source repositories or general-purpose storage. In practice, Google Cloud also offers Secret Manager as a dedicated store for secrets, and the exam guide lists both Cloud KMS and Secret Manager under pipeline configuration and secrets, so a new design should evaluate both, but Secret Manager is not among the options here.

**Real-World Connection**

A team encrypts the database password with a Cloud KMS key and places the base64 ciphertext in the build configuration under `availableSecrets`. It grants the build service account the CryptoKey Decrypter role on that key, and the deployment step reads the value from an environment variable. Rotating the password means re-encrypting it and updating the configuration. Secrets never appear in plaintext in the repository, and the cost is managing key permissions and keeping the encrypted values current.

**Memory Hook**

Encrypt with Cloud KMS, reference it in the build config, and let only the build account decrypt.

**30-Second Exam Takeaway**

For secrets in a Cloud Build pipeline with minimal effort, use a managed key service that Cloud Build integrates with natively, so that access is controlled by IAM on the key. Reject plaintext in buckets or repositories, keys stored beside their ciphertext, and custom cryptography.

**Official References**

  * [**Google Cloud — Use encrypted credentials from Cloud KMS (Cloud Build):**](https://docs.cloud.google.com/build/docs/securing-builds/use-encrypted-credentials) Supports: the correct-answer mechanism (encrypting values with Cloud KMS, referencing them through availableSecrets with the key name, injecting them via secretEnv, and granting the build service account the CryptoKey Decrypter role) and the elimination of options A, B, and C

  * [**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment to Section 2.3, “Managing pipeline configuration and secrets,” which lists key management with Cloud KMS, secret management, and build versus runtime secret injection

</details>

---

### Exam 2 · Q50

An organization has recently moved to a container-based application development workflow, and the team builds many applications that are deployed continuously through an automated pipeline into production. A recent security audit found that code reaching production could contain vulnerabilities, and that the team’s existing virtual machine (VM) vulnerability tooling no longer applies now that workloads run in containers. The security and patch level of every piece of code moving through the pipeline needs to be assured. What should be done?

- A. Set up Artifact Analysis to scan container images and report Common Vulnerabilities and Exposures (CVEs).
- B. Configure the containers in the build pipeline to automatically update themselves just before release.
- C. Reconfigure the existing operating-system vulnerability scanning software to run inside the containers themselves.
- D. Implement static code analysis tooling that scans the Dockerfiles used to build the containers.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Set up Artifact Analysis to scan container images and report Common Vulnerabilities and Exposures (CVEs).

**Correct Answer**

**A. Set up Artifact Analysis to scan container images and report Common Vulnerabilities and Exposures (CVEs).**

**Exam Reasoning Explanation**

The audit hands over two hard facts: production code may contain vulnerabilities, and the old VM-based vulnerability tooling doesn’t translate to containers. That second fact should immediately rule out any option that tries to reuse or relocate the old tool rather than adopt a container-native replacement. What’s needed is a mechanism that inspects the actual software installed inside each built image — OS packages and language dependencies — against known vulnerability data, and that does so automatically as images flow through the existing continuous pipeline. That’s a different capability than linting build instructions or hoping containers patch themselves, and it’s exactly what a dedicated container vulnerability-scanning service is built to provide.

**Key Exam Clues**

  * “existing tooling around virtual machine (VM) vulnerabilities no longer applies to the containerized environment” — an explicit fact that should disqualify any option built around reusing the old VM-based tool.

  * “ensure the security and patch level of all code running through the pipeline” — the solution needs to inspect the actual components that end up in the built artifact, not just the build instructions or a one-time update step.

  * “deployed continuously through an automated build pipeline” — favors a solution that triggers automatically as part of that pipeline rather than a manual or ad hoc process.

**Why This Is Correct**

Artifact Analysis is Google Cloud’s purpose-built service for scanning container images for known vulnerabilities in both OS packages and language-level dependencies, identified by CVE ID. It triggers automatically whenever a new image is pushed to the registry the build pipeline publishes to, so every image moving through the pipeline is checked without any manual intervention. This directly replaces the VM-vulnerability tooling with its container-native equivalent and gives the team ongoing, automated visibility into the actual patch level of the software shipping in every container.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Incorrect:** “containers updating themselves” before release isn’t a standard or verifiable security control. It provides no visibility into what vulnerabilities exist or existed, and containers are generally meant to be built as immutable artifacts from a known base rather than self-modifying at release time — this gives the team no actual detection or reporting capability, which is what the scenario requires.

  * **Option C — Violates Requirement:** the audit has already explicitly stated that the existing VM vulnerability tooling doesn’t apply to the containerized environment. Trying to reconfigure that same software to run inside containers directly contradicts the constraint the scenario itself provides.

  * **Option D — Technically Possible but Not Best:** static analysis of Dockerfiles can catch certain build-instruction issues (bad practices, risky base images named explicitly), but it doesn’t inspect the OS and language packages that actually end up installed inside the resulting image. It can’t, by itself, tell the team whether a vulnerable package version shipped in a given build.

**Exam Trap**

The trap in Option C is overlooking information the scenario already gave: the audit states outright that the old VM tooling doesn’t work in containers, so picking an option built around that same tool means failing to apply a stated constraint. The trap in Option D is conflating “scanning the instructions used to build something” with “scanning what was actually built” — a Dockerfile check has no visibility into which vulnerable package versions actually got installed in the final image.

**Foundation Concept**

Container-native vulnerability management works by scanning the actual contents of a built image — its OS packages and language dependencies — against known vulnerability sources, rather than relying on agent-based tooling designed for a persistent VM operating system. Automating that scan to trigger on every image push embeds security visibility directly into the CI/CD pipeline instead of treating it as a separate, manual step layered on afterward.

**Real-World Connection**

With Artifact Analysis enabled on the registry the pipeline publishes to, every new image is automatically scanned and any known CVEs in its OS or language packages are surfaced. The team can pair that with a deployment-time policy, such as Binary Authorization, to block images with unresolved critical vulnerabilities from reaching production — giving the organization the same kind of ongoing patch-level assurance for containers that the old tooling once provided for virtual machines.

**Memory Hook**

VM vulnerability tools scan installed OS packages on a running machine; Artifact Analysis scans installed OS and language packages inside a container image — same goal, container-native mechanism.

**30-Second Exam Takeaway**

When VM-era vulnerability tooling stops applying after a move to containers, favor the option that scans the actual contents of the built image for known CVEs and integrates automatically with the registry and pipeline — not one that reuses the old tool, relies on self-updating containers, or only inspects the Dockerfile.

**Official References**

[**Google Cloud — Artifact Analysis overview (formerly Container Analysis):**](https://cloud.google.com/artifact-analysis/docs/container-analysis) Supports: the correct-answer mechanism of automated, pipeline-integrated container image vulnerability scanning.

[**Google Cloud — Vulnerability scanning (Artifact Analysis):**](https://cloud.google.com/artifact-analysis/docs/vulnerability-scanning) Supports: the OS-package and language-package CVE scanning capability that directly matches the correct answer

</details>

---

### Exam 2 · Q52

An application runs entirely on Google Cloud, and the team needs to stand up Jenkins to deploy application releases into that environment. The goals are to streamline the release process, reduce operational toil, and keep user data secure. What should be done?

- A. Run Jenkins on individual local workstations.
- B. Run Jenkins on a Kubernetes cluster hosted on-premises.
- C. Run Jenkins on Cloud Run functions.
- D. Run Jenkins on Compute Engine virtual machines.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Run Jenkins on Compute Engine virtual machines.

**Correct Answer**

**D. Run Jenkins on Compute Engine virtual machines.**

**Exam Reasoning Explanation**

The deployment target is already fully inside Google Cloud, so the natural baseline is to keep the CI/CD tooling in the same environment rather than introduce a second network or infrastructure boundary. From there, the decision narrows to whether the chosen Google Cloud compute option can actually run Jenkins: Jenkins is a persistent, stateful server process, which rules out any execution model built around short-lived, time-boxed invocations. What’s left is a platform that is both inside Google Cloud and capable of hosting a long-running server — which is exactly what Compute Engine is for, and it lets Jenkins use native IAM and private networking to reach its deployment targets without exporting credentials or data outside Google Cloud’s boundary.

**Key Exam Clues**

  * “application runs entirely on Google Cloud” — the deployment target already lives in Google Cloud, favoring keeping Jenkins in that same environment rather than a separate network.

  * “streamline the release process, reduce operational toil, and keep user data secure” — three simultaneous requirements that together disqualify options adding manual maintenance, a second infrastructure environment, or an unsuitable execution model.

  * Single-select “What should be done?” — only one option needs to satisfy all three goals at once.

**Why This Is Correct**

Compute Engine provides a persistent virtual machine, which is the kind of platform Jenkins’s controller process actually needs: a long-running server that keeps job queues, configuration, and plugin state alive between builds. Placing that VM inside the same Google Cloud project and VPC as the application lets Jenkins authenticate to deployment targets through an IAM service account and private networking, rather than external credentials crossing into another network — directly supporting the “keep user data secure” goal. Because everything stays in one managed cloud environment, the team also avoids maintaining a second piece of infrastructure (a local machine fleet or an on-premises cluster), which is what actually lowers operational toil.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** individual local workstations have no centralized management, no consistent security controls, and require ongoing manual upkeep (patching, availability, backup) on every machine — this works directly against both “lower operational toil” and “keep user data secure.”

  * **Option B — Technically Possible but Not Best:** hosting Jenkins on an on-premises Kubernetes cluster, while the application and its data live entirely in Google Cloud, creates a hybrid topology. Deployment credentials now have to cross from the on-premises network into Google Cloud, and the team has to operate and secure two separate environments instead of one — increasing rather than reducing toil and security exposure, even though Kubernetes itself is a perfectly capable orchestrator.

  * **Option C — Incorrect:** Cloud Run functions execute on a per-invocation basis with a hard maximum duration per call, after which the instance is terminated — a model built for short-lived, stateless work. Jenkins requires a continuously running controller process that persists state across builds, which this execution model cannot provide; this option is technically infeasible as described, not merely suboptimal.

**Exam Trap**

The trap is assuming any Google Cloud service is interchangeable as long as it’s “serverless” or “cloud-native” sounding — Cloud Run functions looks appealing for low operational toil, but Jenkins’s architecture as a persistent server is fundamentally incompatible with a time-boxed, per-invocation execution model. A second trap is equating “Kubernetes” with “low toil” without registering that Option B explicitly places it on-premises, which reintroduces the exact hybrid-network toil and security problem the scenario is trying to avoid.

**Foundation Concept**

Jenkins runs as a traditional, stateful controller process, not a short-lived function — it needs a platform that supports long-running execution, persistent storage for configuration and build history, and a stable network identity for reaching deployment targets. A general-purpose VM platform like Compute Engine satisfies that directly, and co-locating it with the application inside the same cloud project lets it rely on native IAM and private networking instead of external credentials or VPN connectivity.

**Real-World Connection**

Running Jenkins on a Compute Engine VM with a narrowly scoped IAM service account lets the team grant Jenkins exactly the deployment permissions it needs on the target Google Cloud resources, avoid storing long-lived static credentials for an external network, and rely on Google Cloud’s own VM image and patching tooling — concretely reducing both the security exposure and the day-to-day operational burden compared to running a separate on-premises CI environment.

**Memory Hook**

Jenkins needs a persistent server, not a function, and not a separate network — when the application lives in Google Cloud, put Jenkins in Google Cloud, on a VM.

**30-Second Exam Takeaway**

For “where should Jenkins run” questions, eliminate FaaS platforms outright on execution-model grounds, and prefer keeping Jenkins inside the same cloud environment as its deployment targets over local workstations or on-premises infrastructure, which add toil and cross-network security risk.

**Official References**

[**Google Cloud — Using Jenkins for distributed builds on Compute Engine:**](https://cloud.google.com/architecture/using-jenkins-for-distributed-builds-on-compute-engine) Supports: the correct-answer pattern of running Jenkins on Compute Engine with an IAM service account for secure deployment access

[**Google Cloud — Cloud Run functions quotas (maximum function duration):**](https://cloud.google.com/functions/quotas) Supports: the technical elimination of Option C, since Jenkins’s persistent controller process cannot run within a bounded per-invocation execution mode.

</details>

---

### Exam 2 · Q54

Cloud Build is used to build an application, and the goal is to shorten the build time while keeping both cost and development effort as low as possible. What should be done?

- A. Cache intermediate build artifacts in Cloud Storage between builds.
- B. Stand up multiple Jenkins agents to run the build in parallel.
- C. Break the build into multiple smaller steps to cut down execution time.
- D. Switch to a larger Cloud Build virtual machine (VM) using the machine-type option.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Cache intermediate build artifacts in Cloud Storage between builds.

**Correct Answer**

**A. Cache intermediate build artifacts in Cloud Storage between builds.**

**Exam Reasoning Explanation**

This question stacks three requirements at once: faster builds, lower cost, and low implementation effort. Any option that trades one of those for another fails the question, even if it technically speeds things up. Scaling to bigger compute or to a second CI system can address speed, but each does so by spending more money or more engineering effort — the opposite of what’s being asked. The option that actually attacks the real source of wasted build time — redoing work that hasn’t changed since the last build — is the one that satisfies all three constraints together, because avoiding redundant work is both cheap (object storage, not more compute) and simple to add (a couple of build steps) within the Cloud Build setup already in place.

**Key Exam Clues**

  * “reduce the build time while minimizing cost and development effort” — a triple, simultaneous constraint; the right answer has to score well on all three, not just speed.

  * “You use Cloud Build” — the scenario has already committed to Cloud Build as the CI tool, which should raise a flag against any option that introduces a separate CI system.

  * Single-select “What should you do?” — only one action needs to satisfy the full compound requirement.

**Why This Is Correct**

Caching intermediate build artifacts — dependencies, compiled objects, or other reusable outputs — in a Cloud Storage bucket between builds is Google’s own documented technique for speeding up Cloud Build. By copying a previous build’s results from the bucket, reusing them, and writing updated results back, each new build only has to redo the work that actually changed rather than starting from scratch. That directly cuts build time. Cloud Storage is inexpensive relative to build compute, so the added cost is minimal, and the implementation is a small, well-documented addition of a few build steps to the existing configuration rather than a redesign — hitting all three goals at once.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Violates Requirement:** standing up multiple Jenkins agents means operating an entirely separate CI system alongside (or instead of) Cloud Build. That’s a significant increase in both development effort — integrating or migrating the pipeline — and ongoing cost — infrastructure to run and maintain Jenkins agents — directly working against two of the three stated goals.

  * **Option C — Incorrect:** simply splitting a build into more, smaller steps doesn’t by itself reduce total execution time. Cloud Build steps run sequentially unless explicitly configured to run in parallel, so breaking work into more steps leaves the total amount of work the same, and can even add overhead from pulling and starting more step containers, rather than solving the actual time cost.

  * **Option D — Technically Possible but Not Best:** a larger machine type can genuinely speed up a CPU- or memory-bound build, but Cloud Build’s own pricing scales build-minute cost sharply with machine size — a high-CPU machine type can cost many times more per minute than the default. That directly conflicts with the “minimizing cost” requirement, even though it helps with raw speed.

**Exam Trap**

Option D is the trap because “bigger machine, faster build” is the most intuitive lever to reach for — but the question explicitly also asks to minimize cost, and Cloud Build’s pricing makes that trade-off concrete and expensive. The question is testing whether the full compound requirement is being weighed, not just the speed half of it.

**Foundation Concept**

Google’s documented Cloud Build performance guidance centers on eliminating redundant work rather than adding more compute to brute-force through it. Techniques like Docker layer caching and caching directories or dependencies via Cloud Storage let each build reuse the results of the previous one, so only genuinely changed work has to be redone — typically both faster and cheaper than scaling up the build machine.

**Real-World Connection**

A build that re-downloads the same unchanged dependencies or recompiles unchanged code on every single commit wastes minutes every time it runs. Caching those results in Cloud Storage turns most builds into fast, incremental runs instead of full rebuilds, compounding savings in both developer wait time and Cloud Build billing as a team ships many times a day.

**Memory Hook**

Don’t pay more compute to go faster — stop redoing the same work. Cache it.

**30-Second Exam Takeaway**

When a build-speed question also asks to minimize cost and effort, favor caching previous build results over scaling up build machines or standing up separate CI infrastructure.

**Official References**

[**Google Cloud — Best practices for speeding up builds (Cloud Build):**](https://cloud.google.com/build/docs/speeding-up-builds) Supports: the correct-answer mechanism of caching directories and artifacts with Cloud Storage between builds

[**Google Cloud — Cloud Build pricing:**](https://cloud.google.com/build/pricing) Supports: the elimination of Option D by showing build-minute cost scaling sharply with machine type

</details>

---

### Exam 2 · Q58

Some of your production services run on Google Kubernetes Engine (GKE) in a Europe region, while your build system runs in a US region. You want to push the container images from the build system to a scalable registry so that the bandwidth available for transferring the images to the cluster is as high as possible. What should you do?

- A. Push the images to Artifact Registry by using the gcr.io hostname.
- B. Push the images to Artifact Registry by using the us.gcr.io hostname.
- C. Push the images to Artifact Registry by using the eu.gcr.io hostname.
- D. Push the images to a private image registry running on a Compute Engine instance in the same Europe region as the cluster.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Push the images to Artifact Registry by using the eu.gcr.io hostname.

**Correct Answer**

**C. Push the images to Artifact Registry by using the eu.gcr.io hostname.**

**Exam Reasoning Explanation**

Two hard constraints define the answer: the registry must be a scalable service, and image transfer bandwidth to the cluster must be maximized. The second constraint tells you which side to optimize. Images are pushed once per build but pulled whenever nodes start or scale, so the pull path to the cluster matters most, which means the images should be stored close to the GKE cluster and not close to the build system. Apply that to each hostname option, then test the self-hosted option against the “scalable” requirement.

**Key Exam Clues**

  * “scalable registry” — hard constraint: the registry must be a managed service that scales without you operating it, which excludes a self-run server.

  * “maximize the bandwidth for transferring the images to the cluster” — hard constraint: the images must be stored near the cluster that pulls them.

  * “production services ... in a Europe region” with a build system in a US region — technical signal: producer and consumer are on different continents, and the optimization targets the consumer side.

  * “gcr.io,” “us.gcr.io,” and “eu.gcr.io” hostnames — technical signal: the hostname determines the multi-region where images are stored.

**Why This Is Correct**

The hostname selects the storage location. Artifact Registry supports the gcr.io domain through gcr.io repositories in multi-regional locations: gcr.io and us.gcr.io map to the us multi-region, eu.gcr.io maps to the europe multi-region, and asia.gcr.io maps to asia. Pushing to eu.gcr.io therefore stores the images in Europe, near the GKE cluster, so every pull travels a short distance with higher throughput and no intercontinental transfer. The build system pays the cross-ocean cost once per push, while the cluster benefits on every pull. Artifact Registry is a fully managed service, which meets the scalability requirement. One prerequisite is IAM: the build identity needs write access to the repository and the cluster’s nodes need read access.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** The gcr.io hostname maps to the US multi-region, so the images would be stored on the wrong continent and every pull would cross it. It is tempting because it is the default hostname, but it works against the bandwidth goal.

  * **Option B — Violates Requirement:** The us.gcr.io hostname is also the US multi-region. It is tempting because the build system is in the US and pushes would be fast, but that optimizes the one-time push and not the repeated pulls the question is about.

  * **Option D — Technically Possible but Not Best:** A registry in the cluster’s region has the right proximity, but a self-run registry on a Compute Engine instance is not a scalable managed service. You would own capacity, availability, storage, patching, and authentication, and a single instance is a throughput bottleneck and a single point of failure.

**Exam Trap**

The strongest distractor is Option B, because “the build system is in the US” makes a US hostname feel natural. The distinction is which transfer matters: pushes happen once per build, and pulls happen on every deployment and scale-out. If the requirement had been to maximize build push speed because pulls were rare, the registry location near the build system would become the better choice.

**Foundation Concept**

Store artifacts close to the systems that consume them most often, since the read path usually dominates the write path for container images. Registry location choice balances latency, availability, and bandwidth cost. Exam framing and current practice differ in two ways. First, Container Registry is deprecated and superseded by Artifact Registry, which serves the gcr.io hostnames through gcr.io repositories, so this item is expressed with Artifact Registry. Second, the supplied region names (eu-west-1 and us-west-1) are not Google Cloud region IDs, so the revised item refers to the Europe and US geographies, which is all the answer depends on. In a new design, Google recommends creating a repository in the same region as your GKE cluster to reduce latency and network egress costs, which a pkg.dev repository allows.

**Real-World Connection**

A US-based build system pushes each image once to the Europe-hosted repository, and GKE nodes in Europe pull from it whenever pods are scheduled or the autoscaler adds nodes. Rollouts and scale-out start faster because pulls stay within Europe. The build pays a single cross-region transfer per image, and the team grants the build service account write access and the cluster’s node service account read access.

**Memory Hook**

Push once, pull often: store the image next to the cluster that pulls it.

**30-Second Exam Takeaway**

When a question asks to maximize image pull bandwidth to a cluster, choose the managed registry location nearest the cluster, not the build system. The hostname prefix (us, eu, asia) sets the storage multi-region, and a self-hosted registry fails the scalability requirement.

**Official References**

[**Google Cloud — Artifact Registry gcr.io repositories (hostname to location mapping and Container Registry transition):**](https://docs.cloud.google.com/artifact-registry/docs/transition/gcr-repositories) Supports: the correct-answer mechanism (gcr.io and us.gcr.io map to the us multi-region, eu.gcr.io maps to europe), the elimination of options A and B, and the terminology update from Container Registry to Artifact Registry

[**Google Cloud — Artifact Registry repository overview (repository location):**](https://docs.cloud.google.com/artifact-registry/docs/repositories) Supports: the guidance that repositories should be located near the GKE clusters and other services that consume them to reduce latency and egress costs, and the managed nature of the service that eliminates option D

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment to Section 2.1, “Designing pipelines,” which lists artifact management with Artifact Registry

</details>

---

### Exam 3 · Q1

You have configured a Cloud Build pipeline to deploy Terraform configurations maintained in a GitHub repository. Developers work in short-lived branches and occasionally create tags during development. When a release is ready for deployment, you assign it a semantic version tag. You need the pipeline to apply the Terraform configuration whenever a new release becomes available, while minimizing operational overhead. What should you do?

- A. Configure a Cloud Build trigger for tag pushes matching `\d+\.\d+\.\d+`.
- B. Configure a Cloud Build trigger for branch pushes matching `\d+\.\d+\.\d+`.
- C. Configure a Cloud Build trigger for tag pushes matching `.*`.
- D. Configure a Cloud Build trigger for branch pushes matching `.*`.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Configure a Cloud Build trigger for tag pushes matching `\d+\.\d+\.\d+`.

**Correct Answer**

**A. Configure a Cloud Build trigger for tag pushes matching**`**\d+\.\d+\.\d+**`**.**

**Exam Reasoning Explanation**

First, identify the event that represents deployment readiness: a release tag. Then distinguish release tags from tags created during development. A tag trigger with a version pattern provides the most selective configuration offered, using Cloud Build’s built-in filtering instead of additional pipeline logic. 

**Key Exam Clues**

  * **“Semantic version tag” — Technical signal:** Release identification depends on tag names.

  * **“Occasionally create tags during development” — Technical signal:** Matching every tag would also invoke the deployment pipeline for development tags.

  * **“Whenever a new release becomes available” — Hard constraint:** The trigger must respond to the release event.

  * **“Minimizing operational overhead” — Preference:** Use native trigger filtering.

**Why This Is Correct**

Cloud Build supports triggers for pushed tags and accepts regular expressions for matching their names. In `\d+\.\d+\.\d+`, each `\d+` matches one or more digits, and each `\.` matches a literal period. The expression therefore matches version strings such as `2.5.1`. 

Associate the trigger with the existing build configuration that applies Terraform. The tag must be pushed to GitHub; creating it locally does not invoke the trigger. 

**Why the Other Options Are Not the Best Fit**

  * **Option B — Violates Requirement:** The version pattern looks appropriate, but it filters branch names. Pushing a release tag does not satisfy a branch-push trigger.

  * **Option C — Technically Possible but Not Best:** It invokes builds for release tags and development tags. Additional filtering would be needed to prevent development tags from reaching the deployment steps.

  * **Option D — Violates Requirement:** It responds to pushes across all branches, including development branches, rather than using release tags as the deployment signal. 

**Exam Trap**

Selecting a tag trigger is only part of the decision: `.*` also includes development tags. Option C would fit if every pushed tag represented an approved deployment release.

**Foundation Concept**

A repository trigger combines an **event type** with a **matching condition**. Both must represent the intended deployment boundary.

The supplied expression assumes development tags do not match the version pattern. Cloud Build performs regex searches, so it can also match a tag such as `test-2.5.1`. For strict release filtering, use anchors and a pattern tailored to your release naming convention; the supplied expression is not a complete semantic-version validator. 

**Real-World Connection**

A team could use development tags such as `experiment-networking` and release tags such as `2.5.1`. Filtering for version tags lets the release push invoke the existing Terraform pipeline automatically, reducing manual deployment work and unnecessary builds.

**Memory Hook**

When tags mark deployment readiness, match the release-tag convention in the trigger.

**30-Second Exam Takeaway**

Identify what declares a release, then configure the corresponding trigger event and filter. Here, version-tag pushes provide the deployment signal, making A the best option.

**Official References**

  * [**Google Cloud — Create and manage build triggers**](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers)

Supports: Tag versus branch events, repository matching, and the requirement to push tags to the remote repository.

  * [**Google Cloud CLI — gcloud builds triggers create github**](https://docs.cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github)

Supports: Separate branch and tag patterns, regex search behavior, and the distinctions among options A–D.

  * [**Google RE2 — Syntax**](https://github.com/google/re2/wiki/Syntax)

Supports: Digit classes, repetition, escaped literal characters, and matching boundaries.

</details>

---

### Exam 3 · Q6

Your company uses several Cloud Deploy delivery pipelines to release applications across different environments. The development team currently has no access to these pipelines. You must grant the team access exclusively to the development delivery pipeline while following Google-recommended access-control practices. What should you do?

- A. Grant the team `roles/clouddeploy.operator` through the Google Cloud console, and configure deny conditions for every pipeline except the development delivery pipeline.
- B. Create a custom IAM role containing all `clouddeploy.automations.*` permissions through the Google Cloud console, and grant it through an allow policy scoped to the development delivery pipeline.
- C. Define a policy file granting the team `roles/clouddeploy.operator`, and apply it to the development target.
- D. Define a policy file granting the team `roles/clouddeploy.developer`, and apply it to the development delivery pipeline.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Define a policy file granting the team `roles/clouddeploy.developer`, and apply it to the development delivery pipeline.

**Correct Answer**

**D. Define a policy file granting the team**`**roles/clouddeploy.developer**`**, and apply it to the development delivery pipeline.**

**Exam Reasoning Explanation**

Select both the appropriate permissions and the correct resource scope. The team needs access to one delivery pipeline, so attach the role binding directly to that pipeline. Google documents this exact approach using `roles/clouddeploy.developer` and a pipeline-level IAM policy. 

**Key Exam Clues**

  * **“Exclusively to the development delivery pipeline” — Hard constraint:** Scope the grant to that pipeline.

  * **“Currently has no access” — Technical signal:** A narrowly scoped grant is sufficient; existing broad access does not need to be counteracted.

  * **“Google-recommended access-control practices” — Preference:** Use a suitable predefined role with the required resource scope.

**Why This Is Correct**

Cloud Deploy supports IAM policies on individual delivery pipelines. Bind the development team’s group to `roles/clouddeploy.developer` in the policy file, then apply it to the development pipeline using `gcloud deploy delivery-pipelines set-iam-policy`. This grant does not extend to sibling pipelines. 

The Developer role provides deployment-configuration and release-related permissions without granting operational target-management permissions. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** A broader grant followed by exclusions adds unnecessary access-control complexity. Since the team starts without access, grant permissions directly on the required pipeline. The Operator role itself is not inherently invalid for pipeline access; the proposed scoping approach is the problem. 

  * **Option B — Incorrect:** `clouddeploy.automations.*` permissions manage automation resources. They do not supply the delivery-pipeline permissions required here. Restricting the policy’s scope cannot compensate for selecting the wrong permissions. 

  * **Option C — Different Use Case:** Applying an Operator binding to a target grants access to configure that target, including updating or deleting it. It does not grant the requested access to the delivery pipeline. 

**Exam Trap**

A **development target** and a **development delivery pipeline** are different resources. Choose the resource named in the requirement. Option C would fit a request to administer the development target.

**Foundation Concept**

An IAM role determines **which actions** a principal can perform; the resource receiving the binding determines **where** those permissions apply. Least privilege requires both an appropriate role and an appropriately narrow scope.

**Real-World Connection**

Bind a developer group to the development pipeline’s IAM policy. Team membership then controls who receives that access, while production pipelines receive no additional grants. This simplifies administration and preserves environment boundaries.

**Memory Hook**

Match the role to the work and attach its binding to the exact resource requiring access.

**30-Second Exam Takeaway**

For access to one Cloud Deploy pipeline, use a pipeline-level IAM binding. Here, select the predefined Developer role and apply the policy to the development delivery pipeline—not its target.

**Official References**

[**Google Cloud — Use IAM to restrict Cloud Deploy access**](https://docs.cloud.google.com/deploy/docs/securing/iam)

Supports: Pipeline-specific Developer bindings, alternative Operator bindings, and the distinction between pipeline and target access.

[**Google Cloud — IAM roles and permissions**](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions)

Supports: Developer and Operator capabilities and the purpose of automation permissions.

[**Google Cloud CLI — gcloud deploy delivery-pipelines set-iam-policy**](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/set-iam-policy)

Supports: Applying a policy file to a specific delivery pipeline.

</details>

---

### Exam 3 · Q8

You operate Service A, a public-facing API with a response-time SLO of 500 ms. Service A synchronously calls Service B, an internal API that collects request information for transactions handled by Service A.

Under heavy load, Service B becomes unreliable, returning HTTP 500 errors or causing connection timeouts. You need to protect Service A’s users from these failures. What should you do?

- A. Increase the capacity of the request queue preceding Service A’s worker thread pool.
- B. Retry failed calls to Service B using exponential backoff.
- C. Implement a circuit breaker with a fallback that stores the request data in a database.
- D. Apply rate limiting in Service A to restrict outbound requests to Service B.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Implement a circuit breaker with a fallback that stores the request data in a database.

**Correct Answer**

**C. Implement a circuit breaker with a fallback that stores the request data in a database.**

**Exam Reasoning Explanation**

Prioritize the public API’s response-time objective. Repeatedly waiting for an unreliable supporting service can consume Service A’s latency budget and processing resources. A circuit breaker interrupts calls likely to fail, while a database fallback preserves the information Service B would normally collect. 

**Key Exam Clues**

  * **“Response-time SLO of 500 ms” — Performance constraint:** Additional waiting and retries must fit a tight latency budget.

  * **“Synchronously calls” — Dependency signal:** Service B’s delays directly affect Service A.

  * **“HTTP 500 errors or … timeouts” — Failure signal:** The dependency requires failure isolation.

  * **“Collects request information” — Functional signal:** A durable alternative can preserve this information while B is unavailable, assuming collection can be deferred.

**Why This Is Correct**

A circuit breaker monitors dependency calls and opens when configured failure or slow-call thresholds are reached. While open, it rejects further calls quickly. After a waiting period, limited calls test whether the dependency has recovered. 

Service A handles rejected or failed calls through a fallback that writes the request information to a database. This allows the primary transaction path to continue without requiring immediate success from Service B.

This solution assumes deferred collection is acceptable. Configure bounded call timeouts and a sufficiently fast fallback; a circuit breaker alone does not guarantee the 500 ms SLO. 

**Why the Other Options Are Not the Best Fit**

**Option A — Incorrect for This Requirement:** A larger queue allows more requests to wait while workers remain occupied. It does not resolve Service B’s failures and can increase latency and memory consumption, working against the response-time objective. 

**Option B — Technically Possible but Not Best:** Exponential backoff helps with transient failures, but synchronous retries introduce additional attempts and waiting within Service A’s limited response budget. Retries can also amplify an overloaded backend’s workload. Bounded retries may complement the solution, particularly during deferred processing. 

**Option D — Technically Possible but Not Best:** Rate limiting can reduce overload and protect backend capacity. However, admitted requests can still encounter timeouts or errors, and rate limiting alone provides no alternative destination for their information. It is a useful complementary control. 

**Exam Trap**

A circuit breaker **does not itself store request data**. Option C must be understood as a breaker combined with application-defined database fallback logic. The breaker detects and isolates failure; the fallback determines how Service A continues operating. 

**Foundation Concept**

Circuit breakers have three principal states: closed permits normal calls, open rejects calls, and half-open permits recovery probes. They isolate unhealthy dependencies. Timeouts bound individual waits, while fallbacks provide acceptable behavior when the dependency cannot be used. 

**Real-World Connection**

When B becomes unhealthy, persist its request records through the fallback and process them later. Use transaction identifiers to prevent duplicate collection during replay, and test fallback latency under load. The alternative path must remain dependable when B fails.

**Memory Hook**

An unreliable supporting dependency and a tight response budget suggest a circuit breaker with a safe fallback.

**30-Second Exam Takeaway**

Choose failure isolation when synchronous dependency failures threaten a public API’s latency. Combine the circuit breaker with bounded timeouts and a valid fallback; larger queues or retries alone do not provide that protection.

**Official References**

  * [**Microsoft Architecture Center — Circuit Breaker pattern**](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker)  
Supports: Failure isolation, fast rejection, fallback handling, and distinction from retries.

  * [**Resilience4j — CircuitBreaker**](https://resilience4j.readme.io/docs/circuitbreaker)  
Supports: Failure thresholds, slow-call detection, and recovery states.

  * [**Google SRE — Addressing Cascading Failures**](https://sre.google/sre-book/addressing-cascading-failures)  
Supports: Queue latency, retry amplification, and deadline management.

  * [**Google SRE — Handling Overload**](https://sre.google/sre-book/handling-overload/)  
Supports: Capacity protection, throttling, and graceful degradation.

</details>

---

### Exam 3 · Q12

Your company is adopting Cloud Deploy to deliver a web service running on Google Kubernetes Engine (GKE). The application currently has no automated tests. The Quality Assurance (QA) team must manually validate each new release before that version handles any production traffic. Which delivery pipeline design should you implement?

- A. Configure a delivery pipeline with one stage and a standard deployment strategy.
- B. Configure a delivery pipeline with one stage and a canary deployment strategy.
- C. Configure a delivery pipeline with two stages and a canary deployment strategy.
- D. Configure a delivery pipeline with two stages and a standard deployment strategy.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Configure a delivery pipeline with two stages and a standard deployment strategy.

**Correct Answer**

**D. Configure a delivery pipeline with two stages and a standard deployment strategy.**

D is the most direct design: deploy to a QA environment, complete manual validation, and then permit production deployment. However, the requirements do not strictly exclude C if the same QA gate precedes its production canary.

**Exam Reasoning Explanation**

The decisive requirement is validation **before any production exposure**. Provide a non-production target where QA can exercise the release, followed by a production target protected by manual approval. Standard deployment supports this progression without introducing percentage-based rollout phases. 

**Key Exam Clues**

  * **“Manually validate each new release” — Hard constraint:** A human decision must control progression to production.

  * **“Before … any production traffic” — Sequence constraint:** QA must complete validation before production exposure begins.

  * **“No automated tests” — Technical signal:** The pipeline must accommodate manual testing rather than depend on an existing automated verification suite.

**Why This Is Correct**

Implement the two stages as follows:

  1. **QA target:** Deploy the release using the standard strategy and perform manual testing.

  2. **Production target:** Set `requireApproval: true`. An authorized reviewer approves the rollout only after QA succeeds.

Cloud Deploy supports ordered target progression and approval before deploying into a target. Two stages alone do not enforce QA completion—the approval gate is essential. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** A single stage can require approval, but it does not provide both a deployed QA environment and a subsequent production target within this pipeline. Testing would need an additional arrangement outside the proposed progression.

  * **Option B — Violates Requirement:** Using a production canary as the initial validation mechanism exposes some production traffic before QA completes. Canary phases do not substitute for a preceding QA environment. 

  * **Option C — Technically Possible but Not Best:** Two stages can provide QA followed by production, and a production canary could begin after QA approval. This is feasible, but adds progressive rollout behavior that the scenario does not request; D directly implements the stated workflow. 

**Exam Trap**

Distinguish **testing before production** from **testing with limited production exposure**. A canary addresses the latter.

The absence of automated tests does not prohibit canary deployment. Consequently, D is the straightforward intended answer, while C remains technically defensible with an appropriate approval gate.

**Foundation Concept**

Pipeline stages describe progression between deployment targets. Deployment strategies describe how a release reaches a target. Approval gates determine whether that deployment may proceed. These are separate controls that can be combined.

**Real-World Connection**

Deploy a release to `qa`, let testers verify its critical workflows, and approve the pending `production` rollout only after acceptance. If QA finds a defect, withhold approval so the existing production version continues serving users.

**Memory Hook**

Validate in QA first, gate production with approval, and choose rollout strategy separately.

**30-Second Exam Takeaway**

Manual QA before any production traffic points to QA and production stages with an approval gate. Standard deployment meets that requirement directly; canary deployment is an additional rollout choice.

**Official References**

  * [**Google Cloud — Configuration schema reference**](https://docs.cloud.google.com/deploy/docs/config-files)

Supports: Ordered stages, deployment targets, and standard versus canary configuration.

  * [**Google Cloud — Promote your release and manage approvals**](https://docs.cloud.google.com/deploy/docs/promote-release)

Supports: Manual approval gates, `requireApproval: true`, and approving or rejecting production rollouts.

[**Google Cloud — Use a deployment strategy**](https://docs.cloud.google.com/deploy/docs/deployment-strategies)

Supports: Standard deployment behavior and canary deployments that progressively expose users to a release.

</details>

---

### Exam 3 · Q14

You are configuring a continuous integration (CI) pipeline whose integration tests require access to APIs hosted in a private Virtual Private Cloud (VPC) network. Your security team requires that API traffic remain private. You need a solution that minimizes operational overhead. What should you do?

- A. Use Cloud Build private pools configured to connect to your private VPC network.
- B. Use Cloud Build to create a Compute Engine VM in your private VPC network, and execute the integration tests through a startup script.
- C. Use Cloud Build to run the pipeline, and configure a cross-region internal Application Load Balancer to provide access to the APIs.
- D. Use Cloud Build to run the pipeline, and configure a global external Application Load Balancer with a Google Cloud Armor security policy to provide access to the APIs.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Use Cloud Build private pools configured to connect to your private VPC network.

**Correct Answer**

**A. Use Cloud Build private pools configured to connect to your private VPC network.**

**Exam Reasoning Explanation**

The solution must provide private connectivity while minimizing infrastructure management. Cloud Build private pools support access to private VPC resources and provide fully managed build workers. 

**Key Exam Clues**

  * **Technical signal:** Integration tests must call APIs inside a private VPC network.

  * **Hard constraint:** API traffic must remain private.

  * **Preference:** Minimize operational overhead.

**Why This Is Correct**

Private pool workers run in a Google-managed service producer network. Configure a private connection between that network and your VPC so the workers can reach the APIs through internal IP addresses. Configure the necessary firewall access and run the integration tests on the private pool. 

Cloud Build manages the worker infrastructure and its scaling, avoiding the need to maintain your own test VMs. 

**Why the Other Options Are Not the Best Fit**

  * **B — Technically Possible but Not Best:** A VM inside the VPC can reach private APIs. However, this approach adds VM provisioning, test execution coordination, result collection, and cleanup to the pipeline.

  * **C — Incorrect as a complete solution:** An internal Application Load Balancer provides an internal endpoint, but creating it does not establish private connectivity from Cloud Build workers to your VPC. Additional networking would still be required.

  * **D — Violates Requirement:** A global external Application Load Balancer exposes an external endpoint. A Cloud Armor policy can restrict requests, but it does not convert that endpoint into private VPC connectivity. 

**Exam Trap**

Creating a private pool alone does not automatically connect it to your VPC. The pool must be configured with the appropriate private network connection. 

**Foundation Concept**

Build execution and network access are separate concerns. Cloud Build runs the tests; the private pool’s network configuration provides a route to the internal APIs.

**Real-World Connection**

For example, integration tests can validate an internal orders API directly through its private address while Cloud Build manages the test workers.

**Memory Hook**

When Cloud Build needs private API access with minimal infrastructure management, choose a VPC-connected private pool.

**30-Second Exam Takeaway**

Choose **A**. Private pools provide managed build execution with private VPC access; a load balancer alone does not establish that connectivity.

**Official References**

  * [**Private pools overview**](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview)  
Supports: Managed build workers, automatic scaling, and access to private network resources.

  * [**Set up environment to use private pools in a VPC network**](https://docs.cloud.google.com/build/docs/private-pools/set-up-private-pool-to-use-in-vpc-network)  
Supports: Private connections that allow communication through internal IP addresses.

  * [**Internal Application Load Balancer overview**](https://docs.cloud.google.com/load-balancing/docs/l7-internal)  
Supports: Internal endpoints and the network scope of cross-region internal load balancing.

  * [**External Application Load Balancer overview**](https://docs.cloud.google.com/load-balancing/docs/https)  
Supports: External frontend IP addresses and Cloud Armor integration.

</details>

---

### Exam 3 · Q15

You store container images built by Cloud Build in Artifact Registry. You need to maintain vulnerability scanning coverage for both existing and newly uploaded images. You also need to identify the principal responsible for pushing each image. What should you do?

- A. Enable automatic vulnerability scanning for newly uploaded images and arrange periodic rescanning of all stored images. Use Cloud Audit Logs to track image uploads and identify the uploading principal.
- B. Export vulnerability scan results to a Cloud Storage bucket, and use a custom script to analyze the results and notify the security team.
- C. Configure automatic daily rescanning of images. Enable Cloud Audit Logs for scan operations, and use Logs Explorer to identify vulnerabilities.
- D. Trigger automatic vulnerability scans when new image tags are created, and review the results. Use Cloud Audit Logs to track tag creation events.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Enable automatic vulnerability scanning for newly uploaded images and arrange periodic rescanning of all stored images. Use Cloud Audit Logs to track image uploads and identify the uploading principal.

**Correct Answer**

**A. Enable automatic vulnerability scanning for newly uploaded images and arrange periodic rescanning of all stored images. Use Cloud Audit Logs to track image uploads and identify the uploading principal.**

**Exam Reasoning Explanation**

A addresses both requirements: vulnerability monitoring and upload attribution. However, its scanning language is shorthand: Artifact Analysis provides on-push scanning and continuous analysis, with additional steps needed to cover previously stored or inactive images. 

**Key Exam Clues**

  * **Coverage requirement:** Include existing images and future uploads.

  * **Ongoing requirement:** Detect newly disclosed vulnerabilities.

  * **Audit requirement:** Identify who performed each image push.

**Why This Is Correct**

Implement A as follows:

  1. **Enable automatic scanning.** Enable the Container Scanning API and ensure scanning is enabled for the relevant repositories.

  2. **Cover existing images.** Push previously unscanned images again; enabling scanning does not automatically scan the existing inventory. 

  3. **Maintain continuous analysis.** Artifact Analysis updates findings as vulnerability information changes. Periodically pull retained images within the 30-day activity window to prevent their findings from becoming stale. 

  4. **Enable upload auditing.** Enable Artifact Registry **Data Write audit logs**. Inspect upload operations such as `Docker-PutManifest` and their caller identity. Data Access logging is generally disabled by default. 

**Why the Other Options Are Not the Best Fit**

  * **B — Different Use Case:** Processing exported findings supports reporting and notifications. It does not establish scanning coverage for every image or identify image uploaders.

  * **C — Incorrect:** Continuous analysis updates vulnerability findings as new information arrives; it is not simply a configurable daily full rescan. Audit logs record operations and identities, while Artifact Analysis maintains vulnerability findings.

  * **D — Incorrect:** Automatic initial scanning is based on the image’s **digest**. Adding or modifying a tag does not trigger a new scan. A tag creator also need not be the principal that originally uploaded the image. 

**Exam Trap**

Do not assume enabling scanning retroactively covers existing images. Similarly, enabling audit logging now cannot recreate upload records that were never collected.

**Foundation Concept**

  * **Artifact Registry** stores images.

  * **Artifact Analysis** maintains vulnerability findings.

  * **Cloud Audit Logs** records resource operations and caller identities.

**Real-World Connection**

When Cloud Build pushes an image, the uploading principal is normally its build service account. To identify the human or source change behind that upload, correlate the registry event with the corresponding build records. 

**Memory Hook**

Use Artifact Analysis to understand image risk and audit logs to establish upload accountability.

**30-Second Exam Takeaway**

Choose **A**. Include existing-image initialization, maintain the continuous-analysis activity window, and explicitly enable Data Write audit logging.

**Official References**

  * [**Types of scanning**](https://docs.cloud.google.com/artifact-analysis/docs/scanning-types)  
Supports: Digest-based scanning, continuous analysis, tag behavior, and the 30-day activity window.

  * [**Scan OS packages automatically**](https://docs.cloud.google.com/artifact-analysis/docs/quickstart-scanning-os-automatically)  
Supports: Enabling scanning and pushing existing images again for initial coverage.

  * [**Artifact Registry audit logging**](https://docs.cloud.google.com/artifact-registry/docs/audit-logging)  
Supports: Upload operations, including `Docker-PutManifest`, and their Data Write classification.

  * [**Cloud Audit Logs overview**](https://docs.cloud.google.com/logging/docs/audit)  
Supports: Caller identities and explicit enablement of Data Access audit logs.

  * [**Connect to Cloud Build**](https://docs.cloud.google.com/artifact-registry/docs/configure-cloud-build)  
Supports: Build service accounts uploading artifacts to Artifact Registry.

</details>

---

### Exam 3 · Q16

Your web application connects to an AlloyDB for PostgreSQL cluster through a private IP address accessible from your default VPC network. Before deploying a new application version, your Cloud Build CI/CD pipeline must execute a database schema migration.

You need to implement this process following Google-recommended security practices. What should you do?

- A. Configure a Cloud Build private pool with a static external IP address. Restrict database connections to that address, and execute the migration script in the private pool.
- B. Create a service account with the required database access permissions. Configure Cloud Build to use this service account, and execute the migration script in a private pool.
- C. Store the database username and password in Secret Manager, and retrieve them when executing the migration script.
- D. Store the database username and encrypted password in the application configuration file, and use these credentials to execute the migration through Cloud Build.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Create a service account with the required database access permissions. Configure Cloud Build to use this service account, and execute the migration script in a private pool.

**Correct Answer**

**B. Create a service account with the required database access permissions. Configure Cloud Build to use this service account, and execute the migration script in a private pool.**

**Exam Reasoning Explanation**

The solution needs both **private network connectivity** and an appropriately authorized **build identity**. B addresses both components: a private pool for database access and a dedicated service account for the migration workload. 

**Key Exam Clues**

  * **Technical signal:** AlloyDB is accessed through a private IP address.

  * **Execution requirement:** The migration runs inside Cloud Build.

  * **Security preference:** Use a dedicated identity with only the necessary permissions.

  * **Sequence requirement:** Complete the migration before deploying the application.

**Why This Is Correct**

Configure the private pool with a supported network path to the AlloyDB private endpoint. Private pools support access to resources in private networks, including databases. 

Configure Cloud Build to run as the dedicated service account. For IAM database authentication, enable that authentication method, register the service account as an AlloyDB database user, and grant the PostgreSQL privileges needed for the schema migration. **Assigning an IAM role alone does not grant all required database privileges.**

**Why the Other Options Are Not the Best Fit**

  * **A — Incorrect:** A static external IP address does not establish connectivity to the database’s private IP address. External address allowlisting does not solve the private network routing requirement. 

  * **C — Technically Possible but Not Best:** Secret Manager is appropriate when using password-based authentication. However, retrieving credentials alone does not provide Cloud Build with connectivity to the private database. It is a supporting component rather than a complete solution.

  * **D — Technically Possible but Not Best:** An encrypted password in a configuration file still requires secure decryption-key management and does not establish private connectivity. Secret Manager provides managed storage for passwords when they are required. 

**Exam Trap**

A private pool is not automatically connected to every private endpoint. If AlloyDB uses private services access, account for **non-transitive VPC peering** : simply chaining the pool’s peering connection through your VPC to another peered network is insufficient. 

**Foundation Concept**

Database access has three separate requirements:

  * **Connectivity:** A network path to the database.

  * **Authentication:** A recognized database identity.

  * **Authorization:** Permission to execute the required SQL operations.

**Real-World Connection**

Run the versioned migration as a pipeline step under the migration service account. Make application deployment depend on successful migration completion, so a failed schema change stops the release.

**Memory Hook**

Private connectivity reaches the database, while a scoped service identity controls migration access.

**30-Second Exam Takeaway**

Choose **B**. Configure the private network path, run Cloud Build under a dedicated service account, and grant the necessary database privileges.

**Official References**

  * [**Using Cloud Build in a private network**](https://docs.cloud.google.com/build/docs/private-pools/use-in-private-network)  
Supports: Private database access and limitations of transitive peering.

  * [**Run builds with a user-managed service account**](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts)  
Supports: Configuring a dedicated build identity.

  * [**Manage**](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth?utm_source=chatgpt.com)[**IAM authentication**](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth)  
Supports: Service account database users, IAM authentication, and PostgreSQL privileges.

  * [**Choose a connectivity option**](https://docs.cloud.google.com/alloydb/docs/choose-alloydb-connectivity)  
Supports: AlloyDB private connectivity requirements and network topology considerations.

  * [**Use secrets from Secret Manager**](https://docs.cloud.google.com/build/docs/securing-builds/use-secrets)  
Supports: Securely providing passwords to Cloud Build when password authentication is used.

</details>

---

### Exam 3 · Q20

Your company uses Cloud Build and Artifact Registry in a CI/CD pipeline that deploys container images to Google Kubernetes Engine (GKE). Images are tagged with their corresponding commit hashes and promoted to production after passing tests in development and pre-production. A recent production release failed because an integration scenario had not been tested, leading to a disruptive manual rollback. During recovery, you also discovered numerous outdated, unused images in Artifact Registry. You need to improve deployment and rollback management and remove unnecessary images. What should you do?

- A. Create a dedicated rollback pipeline in Cloud Build, and configure an Artifact Registry cleanup policy.
- B. Manage application deployments with Cloud Deploy, and configure an Artifact Registry cleanup policy.
- C. Deploy Cloud Service Mesh across the GKE clusters, and manually delete obsolete images from Artifact Registry.
- D. Manage application deployments with Cloud Deploy, and schedule a Cloud Build job to delete obsolete container images.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Manage application deployments with Cloud Deploy, and configure an Artifact Registry cleanup policy.

**Correct Answer**

**B. Manage application deployments with Cloud Deploy, and configure an Artifact Registry cleanup policy.**

**Exam Reasoning Explanation**

Two capabilities are required: controlled release management and automated artifact retention. Cloud Deploy manages deployment progression and rollback, while Artifact Registry cleanup policies manage image removal. B addresses both needs through their dedicated managed capabilities. 

**Key Exam Clues**

  * **“Improve deployment and rollback management” — Hard constraint:** Requires repeatable release promotion and recovery.

  * **“Outdated, unused images” — Hard constraint:** Requires artifact lifecycle management.

  * **“Integration scenario had not been tested” — Diagnostic signal:** Deployment verification must include meaningful integration tests.

  * **“Commit hashes” — Technical signal:** Build traceability already exists; tagging alone does not validate application behavior.

**Why This Is Correct**

Cloud Deploy defines a delivery pipeline across target environments and manages releases and rollouts. A rollback creates another rollout using a previously successful release, providing a consistent recovery mechanism. It integrates with the existing Cloud Build and Artifact Registry workflow. 

Artifact Registry cleanup policies automatically remove versions matching deletion criteria and retain versions matching keep criteria. Configure retention to preserve production and rollback candidates, and preview deletion behavior with a dry run. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** A Cloud Build pipeline can execute rollback commands, and its cleanup policy is appropriate. However, the team must implement and maintain its own release-selection and recovery workflow instead of using Cloud Deploy’s release-management capabilities. 

  * **Option C — Different Use Case:** Cloud Service Mesh provides traffic management and can support canary or blue-green deployments. Those capabilities do not supply the requested release-management workflow, and manual image deletion leaves repository maintenance dependent on operators. 

  * **Option D — Technically Possible but Not Best:** Cloud Deploy is appropriate, but a scheduled cleanup build requires custom deletion logic and job maintenance. Native cleanup policies already provide automated retention and removal. Custom jobs become useful when requirements exceed what policy conditions can express. 

**Exam Trap**

Adopting Cloud Deploy does not automatically create the missing integration tests. Configure deployment verification using tests that exercise the previously uncovered functionality; Cloud Deploy runs the tests you provide.

**Foundation Concept**

Release management and artifact retention must work together. A reproducible rollback needs both the previous deployment configuration and its container image. An image can be old yet still be necessary for recovery.

**Real-World Connection**

Continue building images with Cloud Build, promote releases through Cloud Deploy, and add integration verification to the relevant targets. Combine deletion rules for obsolete builds with keep rules protecting recovery images, then review cleanup results in dry-run mode before enabling deletion. 

**Memory Hook**

Use Cloud Deploy for release progression and rollback, and Artifact Registry policies for retention.

**30-Second Exam Takeaway**

When a scenario combines deployment recovery problems with accumulating images, pair managed delivery with native cleanup policies. Preserve the artifacts needed for rollback and explicitly configure the required tests.

**Official References**

  * [**Google Cloud — Overview of Cloud Deploy:**](https://docs.cloud.google.com/deploy/docs/overview)

Supports: Environment progression, release management, rollback, and integration with Cloud Build and Artifact Registry.

  * [**Google Cloud Deploy — Verify your deployment:**](https://docs.cloud.google.com/deploy/docs/verify-deployment)

Supports: Deployment verification using explicitly configured application tests.

  * [**Google Cloud Artifact Registry — Configure cleanup policies:**](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy)

Supports: Automated deletion, keep rules, retention criteria, and dry-run validation.

  * [**Google Cloud — Cloud Service Mesh overview:**](https://docs.cloud.google.com/service-mesh/docs/overview)

Supports: Traffic management and progressive deployment capabilities; option C’s different operational focus.

</details>

---

### Exam 3 · Q24

You are designing a CI/CD pipeline that packages an application into container images. Images must reach Artifact Registry only after a vulnerability scan confirms there are no critical findings. You also want to minimize ongoing pipeline maintenance. Which approach best satisfies both requirements?

- A. Build and publish the image using a custom script on a VM. Use Artifact Analysis automatic scanning after publication and delete the image if critical vulnerabilities are found.
- B. Build the image with Cloud Build. Run Artifact Analysis On-Demand Scanning before publication and push the image to Artifact Registry only if no critical vulnerabilities are found.
- C. Build the image using Jenkins installed on a VM. Run Artifact Analysis On-Demand Scanning before publication and push the image to Artifact Registry only if no critical vulnerabilities are found.
- D. Build and publish the image using Cloud Build. Use Artifact Analysis automatic scanning after publication and delete the image if critical vulnerabilities are found.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Build the image with Cloud Build. Run Artifact Analysis On-Demand Scanning before publication and push the image to Artifact Registry only if no critical vulnerabilities are found.

**Correct Answer**

**B. Build the image with Cloud Build. Run Artifact Analysis On-Demand Scanning before publication and push the image to Artifact Registry only if no critical vulnerabilities are found.**

**Exam Reasoning Explanation**

First enforce the hard requirement: scanning and approval must precede publication. This eliminates A and D. Both remaining options support that sequence, but Cloud Build removes the need to operate a Jenkins installation and its VM, making B the stronger maintenance fit.

**Key Exam Clues**

  * **“Only after a vulnerability scan confirms” — Sequence constraint:** The security check must complete before pushing the image.

  * **“No critical findings” — Hard constraint:** Explicitly evaluate the scan results for `CRITICAL` severity.

  * **“Minimize ongoing pipeline maintenance” — Preference:** Favor managed build infrastructure over a self-hosted CI server.

**Why This Is Correct**

On-Demand Scanning can inspect a locally built image before it is uploaded to Artifact Registry. Configure the pipeline to build, scan, evaluate severity, and publish only after the check succeeds.

The severity check must fail the build when `CRITICAL` findings exist, preventing the dependent push step from running. Merely running the scanner does not establish this enforcement. Google documents this Cloud Build integration directly. 

Cloud Build provides managed build workers, reducing infrastructure setup, upgrades, and scaling responsibilities. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Automatic scanning examines the image after upload. Deleting it afterward cannot satisfy a requirement that disallows publishing an image with critical vulnerabilities. The custom VM also introduces maintenance responsibilities.

  * **Option C — Technically Possible but Not Best:** Jenkins can implement the required pre-publication scanning sequence. However, hosting it on a VM requires maintaining the CI server and its infrastructure, making it less suitable than Cloud Build for the stated maintenance preference.

  * **Option D — Violates Requirement:** Cloud Build addresses infrastructure maintenance, but the scan occurs too late. Automatic on-push scanning begins when the image is uploaded, so subsequent deletion does not provide a pre-publication gate. 

**Exam Trap**

“Automatic scanning” does not mean “scanning before upload.” If the requirement instead permitted post-upload detection and removal, D could fit. Here, the timing constraint requires an explicit gate before publication.

**Foundation Concept**

The scanner detects findings; the pipeline enforces policy. A successful scan represents the supported vulnerabilities detected at that time. Automatic scanning can complement the initial gate by updating findings as new vulnerability information becomes available. 

**Real-World Connection**

A commit-triggered build can stop at the severity check and retain diagnostic logs for the developer. After the vulnerable dependency is updated, the replacement image is rebuilt and rescanned before publication, avoiding a separate registry cleanup workflow.

**Memory Hook**

Build, scan, enforce, then push; use managed build infrastructure to reduce maintenance.

**30-Second Exam Takeaway**

When vulnerable images must never enter the registry, place the security decision before upload. If multiple options support that sequence, use the operational requirements—such as maintenance effort—to select the best implementation.

**Official References**

  * [**Artifact Analysis — Use On-Demand Scanning in your Cloud Build pipeline:**](https://docs.cloud.google.com/artifact-analysis/docs/ods-cloudbuild)

Supports: Scanning before publication and failing builds based on selected vulnerability severities.

  * [**Artifact Analysis — Types of scanning:**](https://docs.cloud.google.com/artifact-analysis/docs/scanning-types)

Supports: Local on-demand scans, automatic on-push scanning, and continuous analysis.

  * [**Google Cloud — Overview of Cloud Build:**](https://docs.cloud.google.com/build/docs/overview)

Supports: Managed build infrastructure and reduced infrastructure maintenance.

  * [**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)

Supports: Objective 2.4, covering deployment-pipeline security, Artifact Analysis, and vulnerability scanning.

</details>

---

### Exam 3 · Q28

You are deploying a containerized application to Cloud Run. The application requires a password to connect to a database and retrieve data. Your company’s security policy requires the password to be rotated weekly. You need a solution that minimizes the ongoing effort required to manage password rotation. What should you do?

- **A.** Deploy the application to Cloud Run. Each week, build a new container image with the updated database password configured as an environment variable in the Dockerfile. Deploy the image and migrate traffic to the new revision.
- **B.** Store the database password in Secret Manager. Deploy the application to Cloud Run and expose the secret’s `latest` version as an environment variable. Add a new secret version containing the updated password each week.
- **C.** Deploy the application to Cloud Run. Each week, build a new container image and supply the updated database password as a build-time secret. Deploy the image and migrate traffic to the new revision.
- **D.** Store the database password in Secret Manager. Deploy the application to Cloud Run and mount the secret’s `latest` version as a volume. Add a new secret version containing the updated password each week.

<details><summary>Answer &amp; explanation</summary>

**Correct:** **D.** Store the database password in Secret Manager. Deploy the application to Cloud Run and mount the secret’s `latest` version as a volume. Add a new secret version containing the updated password each week.

**Correct Answer**

**D. Store the database password in Secret Manager. Deploy the application to Cloud Run and mount the secret’s**`**latest**`**version as a volume. Add a new secret version containing the updated password each week.**

**Exam Reasoning Explanation**

The deciding factor is how the application receives updated credentials. A mounted secret supports runtime access to rotated values without requiring a weekly container rebuild and deployment.

This question aligns with exam objective 2.3, which covers secret management and build-time versus runtime secret injection. 

**Key Exam Clues**

  * **Weekly password rotation:** Credentials change regularly.

  * **Cloud Run:** Supports Secret Manager integration.

  * **Minimal management effort:** Avoid coupling password changes to image builds and application deployments.

**Why This Is Correct**

Cloud Run retrieves the secret value when the application reads the mounted file. Referencing `latest` therefore lets subsequent reads obtain the updated password. Google explicitly identifies mounted secrets as suitable for rotation. The application must reread the file rather than retain the password indefinitely in memory. 

**Why the Other Options Are Not the Best Fit**

  * **A — Technically Possible but Not Best:** Rebuilding an image, deploying it, and shifting traffic every week adds unnecessary operational work.

  * **B — Technically Possible but Not Best:** Secret-backed environment variables are resolved when an instance starts. Updating `latest` does not refresh the variable in an already running instance. Google recommends selecting a specific secret version for environment variables. 

  * **C — Different Use Case:** Build-time secrets supply credentials to the build process. They do not establish runtime retrieval of the database password, and this option still requires weekly builds and deployments.

**Exam Trap**

The `latest` alias does not make an environment variable refresh dynamically. Secret delivery and application consumption determine when a changed value takes effect.

**Foundation Concept**

A Secret Manager secret contains immutable, numbered versions. Rotation adds a new version, and `latest` refers to the most recently created version. Your application’s access strategy determines how that version reaches running workloads. 

**Real-World Connection**

Coordinate the database credential change with publishing the new secret version, validate the password, and ensure the application reloads it when needed. Adding a version in Secret Manager alone does not update the database password. Google recommends a rotation workflow that updates the external system and Secret Manager together. 

For automation, a Secret Manager rotation schedule sends Pub/Sub notifications; a subscriber must perform the rotation steps. 

**Memory Hook**

For Cloud Run password rotation, mount `latest` and reread the file.

**30-Second Exam Takeaway**

Choose **D**. Mounted secrets support updated values during runtime, while secret-backed environment variables are resolved at instance startup.

**Official References**

[**Configure secrets for services — Cloud Run**](https://docs.cloud.google.com/run/docs/configuring/services/secrets)  
Supports: Mounted secret behavior, environment variable resolution, and rotation suitability.

[**About rotation schedules — Secret Manager**](https://docs.cloud.google.com/secret-manager/docs/rotation-recommendations)  
Supports: Secret versions, the `latest` alias, and coordination with external credential systems.

[**Create rotation schedules in Secret Manager**](https://docs.cloud.google.com/secret-manager/docs/secret-rotation)  
Supports: Pub/Sub rotation notifications and the requirement for a subscriber to execute rotation.

</details>

---

### Exam 3 · Q30

Your team needs to debug a live issue affecting a workload running in a Google Kubernetes Engine (GKE) cluster that has Binary Authorization enabled. To investigate, you want to launch a short-lived diagnostic Pod using an unsigned utility image pulled from Artifact Registry. When you apply the Pod manifest, the Binary Authorization policy blocks the deployment. You need the approach that lets the Pod run while keeping the deployment as secure and auditable as possible. What should you do?

- A. Change the enforcementMode setting in the Binary Authorization policy to ALWAYS_ALLOW.
- B. Add the image-policy.k8s.io/break-glass label to the Pod specification.
- C. Temporarily turn off Binary Authorization on the GKE cluster.
- D. Add the diagnostic image to the admissionWhitelistPatterns entry of the Binary Authorization policy.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Add the image-policy.k8s.io/break-glass label to the Pod specification.

**Correct Answer**

**B. Add the image-policy.k8s.io/break-glass label to the Pod specification.**

**Exam Reasoning Explanation**

Start by separating the hard requirement from the preferences. The hard requirement is: the Pod must deploy despite failing the policy. The preferences are: scope the exception as narrowly as possible, and leave an audit trail. Every option satisfies the hard requirement — all four would get the Pod running. The question is decided entirely by the preferences. Break-glass satisfies both: it is applied per-Pod (not cluster-wide or policy-wide), it requires no edit to the stored policy object, and Google Cloud explicitly logs break-glass usage so security teams can review every emergency bypass after the fact. The other three options all widen the blast radius or remove the audit trail to varying degrees, so the decision collapses to “which option is scoped to exactly this one Pod and still gets logged” — and only break-glass is.

**Key Exam Clues**

  * **“short-lived diagnostic Pod”** — a sequence/cardinality-style signal that the fix should be scoped to one Pod, not the cluster or the policy.

  * **“unsigned utility image”** — confirms the image genuinely fails attestation; this rules out any answer that claims the image would pass normally.

  * **“Binary Authorization policy rejects the deployment”** — tells you the policy is doing its job correctly; the fix should not be “make the policy stop doing its job everywhere.”

  * **“most secure and auditable solution”** — a decisive preference signal (a “BEST”-type qualifier): multiple options can technically work, so you must rank them by scope and logging, not just functionality.

**Why This Is Correct**

The break-glass label is a Binary Authorization-specific override mechanism built for exactly this scenario: a one-off, emergency deployment of an image that would otherwise be denied. Setting `image-policy.k8s.io/break-glass: "true"` on the Pod spec tells the admission webhook to let this single Pod through without touching the policy document itself, and Binary Authorization writes a log entry recording that the override was used. Once you delete the Pod and remove the label, there is nothing left over to clean up in the policy — the exception existed only for the lifetime of that one Pod.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Setting the policy to always allow (regardless of whether this is read as the evaluationMode or enforcementMode field) turns off attestation checking for every deployment the policy covers, not just your one diagnostic Pod. It trades “most secure” for “least secure” and has to be manually reverted, which is also the opposite of auditable-by-default.

  * **Option C — Violates Requirement:** Disabling Binary Authorization on the cluster removes image-signature enforcement for every workload on that cluster for as long as it stays off, including unrelated production Pods. It is the broadest possible exception and the easiest one to forget to re-enable.

  * **Option D — Technically Possible but Not Best:** admissionWhitelistPatterns is a legitimate field, but it is a permanent, policy-level allowlist entry, normally reserved for known infrastructure images (for example, Google system images) that should always bypass checks. Using it for a one-time debug image means the exemption persists in the policy after your troubleshooting is done unless someone remembers to remove the pattern — less scoped and less self-cleaning than a per-Pod break-glass label.

**Exam Trap**

The trap is treating “it will make the Pod deploy” as the only test. A/C/D all work mechanically, so a learner who stops at “does this unblock the deployment?” has no way to pick one. The exam is really testing whether you recognize break-glass as the purpose-built, narrowly scoped, auto-logged mechanism versus the broader, policy-level levers. A secondary trap in option A is the field name itself: ALWAYS_ALLOW is actually a value of a policy’s evaluationMode, not its enforcementMode — conflating the two is a realistic distractor pattern, and recognizing that mismatch is itself a clue that A isn’t describing a real, well-formed configuration.

**Foundation Concept**

Binary Authorization enforces a deploy-time policy (“only run images that meet these attestation requirements”) independent of how the image got into the cluster. Any override mechanism you choose should be evaluated the same way you’d evaluate least-privilege access in IAM: prefer the narrowest, most temporary, most observable exception over a broad or permanent one. Break-glass exists specifically to give you a narrow, logged escape hatch instead of forcing a choice between “can’t debug” and “turn off security.”

**Real-World Connection**

A platform team that standardizes on break-glass for debug Pods can alert on every break-glass log entry and review them weekly, catching both legitimate emergency use and any accidental or malicious misuse quickly. A team that instead reaches for admissionWhitelistPatterns or disabling enforcement tends to accumulate stale exceptions in the policy over time, quietly widening the cluster’s attack surface long after the original incident is resolved.

**Memory Hook**

Debug one Pod → break-glass label; change the rules for everyone → anything else.

**30-Second Exam Takeaway**

When a Binary Authorization question asks for the “most secure and auditable” way to run one noncompliant image, look for the option scoped to a single Pod with built-in logging — that’s break-glass. Any option that edits the policy itself or turns enforcement off is a broader, less reversible change and is rarely the best answer for a temporary, single-use need.

**Official References**

  * [Google Cloud — Use breakglass (GKE, Distributed Cloud): ](https://cloud.google.com/binary-authorization/docs/using-breakglass)Supports: the correct-answer mechanism (the `image-policy.k8s.io/break-glass` label and its audit logging behavior)

  * [Google Cloud — Binary Authorization Policy YAML reference: ](https://cloud.google.com/binary-authorization/docs/policy-yaml-reference)Supports: the admissionWhitelistPatterns, enforcementMode, and evaluationMode field definitions used to eliminate options A and D

</details>

---

### Exam 3 · Q31

Your company is rolling out supply chain security controls for its containerized applications running on Google Kubernetes Engine (GKE). You need the ability to trace a container image running in production back to the exact source and build process that produced it, and your solution needs to follow Google-recommended practice for software supply chain security. What should you do?

- A. Store every build artifact in Artifact Registry, and turn on automatic vulnerability scanning.
- B. Enable the Container Analysis API, configure Cloud Build to use only official base images, and turn on automatic vulnerability scanning.
- C. Run every GKE node pool on Container-Optimized OS, enable Binary Authorization on the cluster, and turn on automatic security updates.
- D. Enable the Container Analysis API, configure Cloud Build to generate and sign build provenance attestations for every build, and configure Binary Authorization to verify those attestations before deployment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Enable the Container Analysis API, configure Cloud Build to generate and sign build provenance attestations for every build, and configure Binary Authorization to verify those attestations before deployment.

**Correct Answer**

**D. Enable the Container Analysis API, configure Cloud Build to generate and sign build provenance attestations for every build, and configure Binary Authorization to verify those attestations before deployment.**

**Exam Reasoning Explanation**

The hard requirement is traceability: proving which source commit and which build process produced a given production image, not just whether that image contains known vulnerabilities or runs on a hardened host. Only one mechanism actually records that chain of custody — build provenance, which Cloud Build can generate and cryptographically sign for every build, storing the metadata via the Container Analysis API. Vulnerability scanning (A, B) and node-level hardening (C) are both legitimate supply chain security practices, but neither one captures or proves where an image came from. Binary Authorization only becomes meaningful for traceability once it’s verifying a real provenance attestation; configured on its own (as in C), it enforces nothing specific about the build’s origin. D is the only option where generation (Cloud Build signs provenance) and enforcement (Binary Authorization verifies it) are both present.

**Key Exam Clues**

  * **“trace container images used in production back to their source and build processes”** — a technical signal pointing specifically at build provenance, not vulnerability data or host configuration.

  * **“supply chain security controls”** — a scope clue broad enough to fit several Google Cloud features, which is why the exam relies on the traceability requirement to pick among them.

  * **“follow Google-recommended practices”** — points at Cloud Build’s documented SLSA-aligned provenance generation combined with Binary Authorization verification, which Google explicitly describes as its software supply chain security approach.

  * **“Google-recommended practices for software supply chain security”** paired with “trace... back to... source and build processes” together rule out any option that stops at scanning or OS hardening without a provenance mechanism.

**Why This Is Correct**

Cloud Build can generate build provenance for the images it produces, meeting SLSA Level 3 assurance, and sign that provenance as an attestation; this metadata (recording the source, build steps, and builder identity) is stored through the Container Analysis API. Configuring Binary Authorization to verify these attestations before deployment means only images with valid, verifiable provenance from your build process can run in GKE — giving you exactly the ability to trace a running production image back to the specific build that created it, and to block anything that lacks that proof.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Different Use Case:** Storing artifacts in Artifact Registry and scanning them for vulnerabilities tells you what known issues exist inside an image’s packages. It says nothing about which source commit or build pipeline produced the image, so it doesn’t satisfy the traceability requirement at all.

  * **Option B — Technically Possible but Not Best:** Enabling the Container Analysis API is a necessary underlying piece (it’s the same metadata store that provenance attestations use), and restricting to official base images improves supply chain hygiene at the base-layer level. But without Cloud Build actually generating and signing provenance, and without Binary Authorization verifying it, there’s no enforced record proving which build process produced a given image — the API is enabled but nothing is using it to establish traceability.

  * **Option C — Different Use Case:** Container-Optimized OS and automatic security updates harden the GKE node/host layer, which is a different part of the supply chain than the container image’s build history. Enabling Binary Authorization without pointing it at a provenance-based attestor enforces nothing specific about where the image came from — the cluster-level controls here address runtime infrastructure security, not image traceability.

**Exam Trap**

The trap is treating “supply chain security” as satisfied by any combination of recognizable security features — vulnerability scanning, official base images, hardened nodes, Binary Authorization by name. The question’s actual requirement is narrower and specific (traceability to source and build process), and only the option that generates and verifies build provenance actually answers that, regardless of how many other legitimate security practices the distractors stack together.

**Foundation Concept**

Software supply chain security has several distinct layers: what’s inside an image (vulnerability scanning), what runs the image (node/OS hardening), and where the image came from (build provenance and attestation). A control from one layer doesn’t substitute for another — proving an image’s origin specifically requires generating verifiable provenance at build time and enforcing its presence at deploy time, which is what the SLSA framework and Binary Authorization’s attestation model are designed to provide together.

**Real-World Connection**

A team that only scans images for vulnerabilities can tell you an image is currently “clean,” but if asked “did this exact image come from our official CI pipeline, built from the commit we think it was,” they have no answer. A team that generates signed build provenance and enforces it with Binary Authorization can answer that question for every image running in production, which is exactly what’s needed during an incident investigation or a supply chain audit.

**Memory Hook**

Scanning tells you what’s inside an image; provenance plus Binary Authorization tells you where it came from — traceability needs the second one.

**30-Second Exam Takeaway**

When a question specifically asks to trace a container image back to its source and build process, look for build provenance generation (Cloud Build) paired with Binary Authorization verification — vulnerability scanning and node-level hardening are supply chain practices too, but they don’t establish or enforce an image’s origin.

**Official References**

[**Google Cloud — Cloud Build overview (build provenance and SLSA)**](https://cloud.google.com/build/docs/overview)**:** Supports: the correct-answer mechanism (Cloud Build generating SLSA Level 3 build provenance and signing it as an attestation)

[**Google Cloud — Securing deployments by only allowing images built by Cloud Build (Binary Authorization):**](https://cloud.google.com/binary-authorization/docs/deploy-cloud-build)Supports: Binary Authorization verifying Cloud Build-signed attestations before deployment, and the elimination of option C’s unconfigured Binary Authorization

</details>

---

### Exam 3 · Q34

You’re designing a containerized CI pipeline and want to reduce how much the pipeline depends on public upstream container registries, while improving build reproducibility and security. You need a design that caches every containerized dependency the pipeline uses, while keeping ongoing manual effort and maintenance to a minimum. What should you do?

- A.
    Create a remote Docker repository in Artifact Registry for each upstream registry you depend on.
    Have the CI pipeline pull container images directly through these remote repositories.
- B.
    Create a standard Docker repository in Artifact Registry for each upstream registry you depend on.
    Upload the container images used by the build pipelines into the appropriate repositories yourself.
- C.
    Create a standard Docker repository in Artifact Registry for each upstream registry you depend on.
    Create a single, central virtual Docker repository that fronts these standard repositories.
    Have the CI pipeline pull container images through the central virtual repository.
- D.
    Create a remote Docker repository in Artifact Registry for each upstream registry you depend on.
    Create a single, central virtual Docker repository that fronts these remote repositories.
    Have the CI pipeline pull container images through the central virtual repository.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D.

**Correct Answer**

**D.**

  1. **Create a remote Docker repository in Artifact Registry for each upstream registry you depend on.**

  2. **Create a single, central virtual Docker repository that fronts these remote repositories.**

  3. **Have the CI pipeline pull container images through the central virtual repository.**

**Exam Reasoning Explanation**

Separate the two things the stem is asking for: caching needs to happen automatically (minimal manual effort), and the CI pipeline needs a simple, low-maintenance way to consume it (minimal ongoing maintenance). A remote repository solves the first part on its own — it’s a proxy that downloads and caches a package from its upstream the first time it’s requested, with no manual upload step. A virtual repository solves the second part — it gives every consumer one single address instead of one address per upstream source, which is what actually keeps maintenance low as the number of upstream registries grows. Only option D combines both: automatic caching per upstream, consolidated behind one endpoint the pipeline references.

**Key Exam Clues**

  * **“minimize reliance on public upstream container registries”** — a technical signal pointing at a caching proxy layer (remote repositories) sitting between the pipeline and the public registries.

  * **“cache all containerized dependencies”** — a scope clue: the mechanism must handle every image automatically, ruling out anything requiring someone to manually populate a repository.

  * **“minimizing the required amount of manual effort and maintenance”** — a decisive preference clue that applies twice: once to rule out manual population (standard repos with manual uploads), and again to favor a single consolidated access point over one per upstream source.

  * **“improve build reproducibility and security”** — reinforces that the goal is a controlled, cached, Google-managed path to every dependency, rather than the pipeline reaching out to each public registry directly every time.

**Why This Is Correct**

A remote Docker repository per upstream registry gives you automatic, no-touch caching: Artifact Registry fetches and stores each image the first time it’s requested, and subsequent requests are served from that cache rather than from the public internet, directly reducing reliance on upstream registries without anyone uploading anything. Layering a virtual Docker repository on top of those remote repositories gives the CI pipeline one single Docker endpoint to reference, regardless of how many different upstream registries are actually behind it — this is the documented pattern Google Cloud itself describes (a virtual repository serving as the single access point in front of remote, caching repositories), and it’s what keeps future maintenance low as upstream sources are added, removed, or reconfigured.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** Remote repositories correctly provide automatic caching, so this option does satisfy the “minimal manual effort to populate the cache” part. But without a virtual repository, the CI pipeline and every Dockerfile or build config has to know and reference the specific remote repository address for each upstream source individually, which is more to configure and maintain as the number of upstream registries grows.

  * **Option B — Violates Requirement:** Standard repositories don’t cache anything automatically; someone has to manually pull each image from its upstream source and push it into the right standard repository, and keep repeating that process every time a new version is needed. That’s the opposite of “minimizing manual effort and maintenance,” and it also means the cache isn’t guaranteed to be complete for every dependency the build actually uses.

  * **Option C — Violates Requirement:** Adding a virtual repository here only solves the “single endpoint” half of the problem. The standard repositories behind it still don’t cache anything on their own, so this design still requires the same manual upload process as option B — it just hides that manual process behind a consolidated address.

**Exam Trap**

The trap is treating “virtual repository” and “remote repository” as interchangeable ways to get caching, when only remote repositories actually proxy and cache an external upstream. A virtual repository is purely a routing/consolidation layer — pairing it with standard repositories (option C) looks like a complete solution but silently reintroduces the manual-upload problem that remote repositories exist to eliminate.

**Foundation Concept**

In Artifact Registry, each repository type serves a distinct purpose: standard repositories hold artifacts you explicitly publish, remote repositories automatically proxy and cache an external upstream, and virtual repositories provide one unified address across any mix of standard and remote repositories. Solving “cache external dependencies with minimal effort” requires remote repositories specifically; solving “give consumers one simple, low-maintenance endpoint” requires a virtual repository on top — and most real designs that need both properties combine the two, exactly as Google’s own documentation illustrates.

**Real-World Connection**

A CI pipeline built directly against several different remote-repository URLs (one per upstream vendor) works, but every new base image source means another endpoint to add to build configs across every repository that uses it. Fronting all of those remote repositories with one virtual repository means onboarding a new upstream source, or swapping which backing repository serves a given namespace, is a change made once in the virtual repository’s configuration, with no changes required in any individual pipeline or Dockerfile.

**Memory Hook**

Caching needs a remote repository; one single address for everything needs a virtual repository on top of it — you typically want both together.

**30-Second Exam Takeaway**

When a question asks to cache public upstream dependencies in Artifact Registry with minimal manual effort and maintenance, look for remote repositories (for the automatic caching) combined with a virtual repository (for the single, low-maintenance access point) — standard repositories alone always imply manual population, no matter what’s layered on top of them.

**Official References**

[**Google Cloud — About remote repositories:**](https://cloud.google.com/artifact-registry/docs/repositories/remote-overview) Supports: the correct-answer mechanism (automatic download-and-cache behavior on first request, with no manual upload step)

[Google Cloud — Repository overview (standard, remote, and virtual repositories): ](https://cloud.google.com/artifact-registry/docs/repositories)Supports: the virtual-repository consolidation pattern (a single access point fronting remote and standard repositories) and the elimination of options B and C, where standard repositories require manual publishing

</details>

---

### Exam 3 · Q35

You manage a critical, high-traffic application running on Google Kubernetes Engine (GKE). You are about to release a new version that makes significant changes to the payment processing workflow. You need a deployment approach that minimizes risk and automatically rolls back the release if it turns out to be unstable. What should you do?

- A. Use Cloud Deploy to run a canary deployment. Configure the delivery pipeline with a multi-phase canary sequence that starts at a 5% traffic split, define success criteria from application telemetry in Cloud Monitoring, and configure Cloud Deploy to automatically roll back the release if the new version fails verification.
- B. Configure your GKE deployment manifest to follow a blue-green pattern: deploy the new version as a “green” deployment next to the existing “blue” one, then, once “green” is live, update the Service selector to gradually move user traffic over to the new version.
- C. Edit the GKE Service manifest to add a selector for the v2 Pods, then create a second GKE Deployment for the new version, and gradually shift traffic by scaling the new Deployment’s replica count up while scaling the old Deployment’s replica count down.
- D. Use the GKE Deployment’s default rolling update strategy, monitor logs and metrics in Cloud Monitoring while it rolls out, and if a problem appears, run kubectl rollout undo to revert the application to the previous stable version.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Use Cloud Deploy to run a canary deployment. Configure the delivery pipeline with a multi-phase canary sequence that starts at a 5% traffic split, define success criteria from application telemetry in Cloud Monitoring, and configure Cloud Deploy to automatically roll back the release if the new version fails verification.

**Correct Answer**

**A. Use Cloud Deploy to run a canary deployment. Configure the delivery pipeline with a multi-phase canary sequence that starts at a 5% traffic split, define success criteria from application telemetry in Cloud Monitoring, and configure Cloud Deploy to automatically roll back the release if the new version fails verification.**

**Exam Reasoning Explanation**

There are two hard requirements stacked in this stem: the release must minimize risk, and it must roll back automatically — not “be rollback-able” or “be rolled back once someone notices.” Every option can plausibly reduce risk through gradual traffic exposure, so the deciding factor is whether rollback is actually automated or depends on a human noticing a problem and taking action. Cloud Deploy’s canary strategy combined with its verification and automation features is the only option where both a defined, telemetry-based pass/fail check and the rollback action itself are handled by the platform rather than by a person — which is exactly what “automatically rolls back” requires.

**Key Exam Clues**

  * **“significant changes to its payment processing workflow”** — signals high blast-radius risk, favoring a small initial exposure (a low traffic percentage) over an all-at-once or coarse-grained cutover.

  * **“minimizes risk”** — favors a progressive, percentage-based rollout over a strategy that exposes 100% of either version at once.

  * **“automatically rolls back if the release proves to be unstable”** — a decisive requirement/exclusion clue: it rules out any option whose rollback step depends on a person detecting the issue and running a command.

  * **“5% traffic split”** paired with **“success criteria using application telemetry”** — technical anchors that map directly to Cloud Deploy’s canary phases and deploy-analysis/verification features.

**Why This Is Correct**

Cloud Deploy’s canary deployment strategy lets you define a sequence of traffic percentages (such as 5%, then larger phases) for a progressive rollout, and its verification (deploy analysis) feature lets you gate each phase on real telemetry, including metrics pulled from Cloud Monitoring. When you pair this with a Cloud Deploy automation rule configured to repair/roll back a failed rollout, a failed verification at any phase triggers rollback to the last known-good release without a human needing to intervene — satisfying both “minimizes risk” (small initial exposure, telemetry-gated progression) and “automatically rolls back” in one coherent, Google-recommended pipeline.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Violates Requirement:** Nothing in this option describes an automated verification step or an automated rollback trigger; “gradually switch” traffic via a Service selector is also not how plain Kubernetes Service selectors behave — a selector matches one set of Pods or another, so the actual traffic cutover here is a discrete switch, not a graduated one, and any rollback would have to be performed manually by reverting the selector.

  * **Option C — Violates Requirement:** This is an entirely manual, hand-rolled approximation of a canary pattern, with no defined success criteria and no automated decision point. Nothing rolls anything back automatically; a person has to watch the rollout and decide when and whether to reverse the replica counts.

  * **Option D — Violates Requirement:** This option explicitly describes a human detecting the issue from logs and metrics and then manually running kubectl rollout undo. That is a manual rollback by definition, directly contradicting the stated requirement that the release roll back automatically.

**Exam Trap**

The trap is that B, C, and D all sound like reasonable progressive-delivery or safety practices in isolation (blue-green, manual traffic shifting, rolling updates with monitoring). A learner who stops at “does this reduce risk somewhat?” can talk themselves into any of them. The question is actually testing whether you notice that only one option ties a defined, telemetry-based success/failure check directly to an automated rollback action, rather than to a person’s judgment call.

**Foundation Concept**

A deployment strategy that “automatically rolls back” needs three pieces working together: a gradual exposure mechanism (so a bad release affects few users), a defined, machine-evaluable success criterion (so “unstable” has a precise meaning), and an automation that acts on that criterion without waiting for a human. Progressive delivery tools like Cloud Deploy are built to wire these three pieces together; hand-built traffic-shifting with manual monitoring only ever provides the first piece.

**Real-World Connection**

A payments team that relies on “watch the dashboards and run rollout undo if something looks wrong” is exposed to detection lag — by the time a person notices elevated error rates and runs the command, a meaningful number of payment transactions may already have hit the broken code path. Wiring verification directly to an automation rule means the bad version is rolled back within the same phase window it was detected in, often before it has reached a large percentage of traffic.

**Memory Hook**

“Automatically rolls back” means the platform decides and acts — if a human has to notice and run a command, it isn’t automatic.

**30-Second Exam Takeaway**

When a question asks for a deployment strategy that “automatically rolls back,” look for the option where both the success/failure check and the rollback action are configured as part of the delivery pipeline (Cloud Deploy verification plus an automation rule) — any option that ends in “a person monitors and then manually intervenes” fails that requirement regardless of how gradual the rollout itself is.

**Official References**

[Google Cloud — Use a canary deployment strategy (Cloud Deploy): ](https://cloud.google.com/deploy/docs/deployment-strategies/canary)Supports: the correct-answer mechanism (percentage-based canary phases and deploy analysis using Cloud Monitoring/Google Cloud Observability metrics)

[Google Cloud — Automate your deployment (Cloud Deploy): ](https://cloud.google.com/deploy/docs/automation)Supports: the automatic-rollback mechanism (a repair-rollout automation rule that acts on a failed verification without manual intervention), used to eliminate options B, C, and D

</details>

---

### Exam 3 · Q38

You need a pipeline that builds a containerized application from GitHub and publishes its image to Artifact Registry. Each new Git tag must automatically submit a build, but execution must wait for approval from a member of the `gcp-developers-admins@mountkirk.com` Google group.

Security policy prohibits static credentials and federation between Google Cloud IAM and external identity providers. Which configuration satisfies these requirements?

- A. Create a GitHub-connected Cloud Build trigger for new tag pushes and enable required approval. Grant `roles/cloudbuild.builds.approver` to `gcp-developers-admins@mountkirk.com` and `roles/artifactregistry.writer` to the service account used to execute the builds.
- B. Create a GitHub Actions workflow that builds and publishes images on new tag pushes. Mirror the Google group’s membership into a GitHub team and require that team’s approval. Create a Google Cloud service account, download its key, and use the key to authenticate the workflow. Grant the service account `roles/artifactregistry.writer`.
- C. Generate an SSH key pair and register its public key as a GitHub repository deploy key. Configure an approval-required Cloud Build trigger that retrieves the repository using this key. Grant `roles/cloudbuild.builds.editor` to `gcp-developers-admins@mountkirk.com` and `roles/artifactregistry.writer` to the build service account.
- D. Create a GitHub Actions workflow that builds and publishes images on new tag pushes. Mirror the Google group’s membership into a GitHub team and require that team’s approval. Configure a Google Cloud workload identity pool that trusts the GitHub workflow identity, and grant the authorized federated principal `roles/artifactregistry.writer`.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Create a GitHub-connected Cloud Build trigger for new tag pushes and enable required approval. Grant `roles/cloudbuild.builds.approver` to `gcp-developers-admins@mountkirk.com` and `roles/artifactregistry.writer` to the service account used to execute the builds.

**Correct Answer**

**A. Create a GitHub-connected Cloud Build trigger for new tag pushes and enable required approval. Grant**`**roles/cloudbuild.builds.approver**`**to**`**gcp-developers-admins@mountkirk.com**`**and**`**roles/artifactregistry.writer**`**to the service account used to execute the builds.**

**Exam Reasoning Explanation**

First eliminate designs using static keys or external identity federation. Then verify that the remaining design provides approval **before execution** , the correct approver permission, and an authorized identity for publishing images. Option A satisfies all these requirements.

**Key Exam Clues**

  * **New tag pushed:** Configure a GitHub tag-push trigger.

  * **Approval before execution:** Enable Cloud Build’s approval gate.

  * **Google group approval:** Grant the group the Cloud Build Approver role.

  * **No static credentials or federation:** Execute within Cloud Build using its configured service account.

**Why This Is Correct**

Cloud Build supports GitHub tag-push triggers with required approval. A matching event creates a **pending build** ; its steps execute only after an authorized approver accepts it. 

Grant the group `roles/cloudbuild.builds.approver` on the build project. Grant the execution service account `roles/artifactregistry.writer`, preferably scoped to the destination repository, so it can publish images. 

Cloud Build runs under the configured Google Cloud service account without requiring an exported service account key or a workload identity pool trusting GitHub. 

**Why the Other Options Are Not the Best Fit**

  * **Option B — Violates Requirement:** The downloaded service account key is a long-lived credential, directly violating the prohibition on static credentials. GitHub team approval does not resolve that authentication issue. 

  * **Option C — Violates Requirement:** The SSH private key introduces a static credential. Additionally, the exact role `roles/cloudbuild.builds.editor` does **not** include `cloudbuild.builds.approve`; the specified group therefore lacks the required approval permission.

  * **Option D — Violates Requirement:** Workload Identity Federation exchanges GitHub’s OIDC identity for short-lived Google Cloud credentials. Although it avoids service account keys, it establishes the external identity trust expressly prohibited here. 

**Exam Trap**

**Keyless authentication can still involve federation.** Option D satisfies one security condition while violating the other. Also, automatic triggering and approval gating coexist: submission is automatic, while execution waits.

**Foundation Concept**

Separate human authorization from workload permissions. Group members authorize execution through the Approver role; the build service account performs operations using its own permissions, including writing artifacts. 

**Real-World Connection**

An accidentally pushed release tag creates a pending build. An authorized group member can reject it before container-building or image-publishing steps execute. 

**Memory Hook**

The trigger submits, the group approves, and the build service account publishes.

**30-Second Exam Takeaway**

Choose **A** : a tag-triggered Cloud Build pipeline with required approval, the group’s Approver role, and the build service account’s Artifact Registry Writer role.

**Official References**

  * **Google Cloud — Gate builds on approval**

Supports: Pending builds, approval before execution, and approval permissions.

[Official documentation](https://docs.cloud.google.com/build/docs/securing-builds/gate-builds-on-approval)

  * **Google Cloud — Cloud Build roles and permissions**

Supports: The permissions in `roles/cloudbuild.builds.approver` and `roles/cloudbuild.builds.editor`.

[Official documentation](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild)

  * **Google Cloud — Store artifacts in Artifact Registry**

Supports: Granting Artifact Registry Writer to the build service account.

[Official documentation](https://docs.cloud.google.com/build/docs/building/store-artifacts-in-artifact-registry)

  * **Google Cloud — Run builds with a user-managed service account**

Supports: Configuring the build execution identity and applying least privilege.

[Official documentation](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts)

</details>

---

### Exam 3 · Q41

You have a CI/CD pipeline in Cloud Build that builds container images, which are stored in Artifact Registry. You need to guarantee that only images built by this Cloud Build pipeline in your production project can be deployed to your Google Kubernetes Engine (GKE) cluster, while keeping the implementation and ongoing maintenance effort as low as possible. What should you do?

- A. Turn on Binary Authorization for the GKE cluster, and build a Cloud Run function that’s triggered by Artifact Registry INSERT events to check that pushed containers carry the projects/PROJECT_ID/attestors/built-by-cloud-build attestor.
- B. Restrict Artifact Registry so that only the Cloud Build service account is permitted to push container images.
- C. Turn on Binary Authorization for the GKE cluster. Create a Cloud Key Management Service (Cloud KMS) keyring and the built-by-cloud-build attestor yourself. After each Cloud Build push, use the key to generate an attestation, and update the Binary Authorization policy to require the projects/PROJECT_ID/attestors/built-by-cloud-build attestor.
- D. Turn on Binary Authorization for the GKE cluster, and set the Binary Authorization policy to require the projects/PROJECT_ID/attestors/built-by-cloud-build attestor.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Turn on Binary Authorization for the GKE cluster, and set the Binary Authorization policy to require the projects/PROJECT_ID/attestors/built-by-cloud-build attestor.

**Correct Answer**

**D. Turn on Binary Authorization for the GKE cluster, and set the Binary Authorization policy to require the projects/PROJECT_ID/attestors/built-by-cloud-build attestor.**

**Exam Reasoning Explanation**

The hard requirement is a hard deployment-time gate: only Cloud-Build-built images may run on the cluster. The preference is minimal setup and upkeep. Binary Authorization is the mechanism that actually enforces a gate at deploy time in GKE, so any option without it (B) is disqualified outright regardless of effort. Among the Binary Authorization options, Cloud Build already has a built-in, Google-managed integration: it automatically creates the built-by-cloud-build attestor in your project and automatically signs an attestation for every image it builds, with Binary Authorization verifying that attestation at deploy time. That means the entire “verify this was built by Cloud Build” problem is solved the moment you point your policy at that attestor — no keys, no custom code, no manual signing step required, which is exactly what makes D the lowest-effort option that still fully satisfies the hard requirement.

**Key Exam Clues**

  * **“only images built by the Cloud Build pipeline in your production project are deployed”** — a technical signal pointing at Binary Authorization’s attestor-verification model, specifically one tied to Cloud Build as the builder.

  * **“deployed to your GKE cluster”** — a scope clue: the control must act at GKE admission/deploy time, not merely at registry-push time.

  * **“minimize the amount of manual effort required for implementation and maintenance”** — a decisive preference clue: it favors whichever option offloads the most setup and ongoing work onto a managed/automatic mechanism.

  * **“built-by-cloud-build attestor”** named explicitly in every option — a technical anchor signaling that the exam wants you to recognize this as Google’s specific, automatically managed attestor rather than something you build yourself.

**Why This Is Correct**

Cloud Build’s integration with Binary Authorization automatically provisions the built-by-cloud-build attestor in your project (created the first time you run a build) and automatically signs an attestation for each successfully built image — all without you creating a Cloud KMS key, managing signing keys, or writing any code. Once Binary Authorization is enabled on the GKE cluster and its policy requires the projects/PROJECT_ID/attestors/built-by-cloud-build attestor, the cluster’s admission controller will refuse to deploy any image that doesn’t carry a valid attestation from that attestor — which only Cloud Build can produce for that project. That delivers the exact guarantee asked for, with the setup reduced to two configuration steps.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** This requires designing, writing, and maintaining a custom Cloud Run function as a permanent piece of infrastructure, which directly conflicts with “minimize manual effort and maintenance.” It’s also the wrong enforcement point: reacting to an Artifact Registry INSERT (push) event checks images after they land in the registry, not at the moment GKE tries to deploy them, so it doesn’t actually function as the deployment-time gate the requirement calls for — Binary Authorization’s native admission control already does this natively.

  * **Option B — Violates Requirement:** Limiting who can push to Artifact Registry controls one storage location, but it does nothing to control what GKE is allowed to pull and run. Without an enforcement mechanism at the cluster itself, there’s no guarantee against deploying images from elsewhere, so this doesn’t satisfy “ensure only images built by the Cloud Build pipeline are deployed to your GKE cluster.”

  * **Option C — Technically Possible but Not Best:** This reaches the same end state as D, but by manually rebuilding what Cloud Build’s integration already automates: creating your own Cloud KMS keyring and attestor, and manually generating an attestation after every build. That’s substantial duplicate setup and an ongoing manual (or custom-scripted) step on every single build, which is exactly the extra effort the requirement asks you to avoid.

**Exam Trap**

The trap is assuming that because Binary Authorization “requires an attestor and attestations,” you must be the one who creates the Cloud KMS key and signs each attestation (option C) — that’s how Binary Authorization works in the general case, but Cloud Build has a specific, documented shortcut that automates exactly that workflow for images it builds, which is what the built-by-cloud-build attestor name is signaling.

**Foundation Concept**

Binary Authorization enforces policy at the point resources are deployed, by requiring one or more attestations — cryptographically signed claims that a specific verification step occurred — before an image is allowed to run. When the entity doing the verifying is also the platform enforcing the policy (here, Google-managed Cloud Build and Binary Authorization working together), the provider can automate both the attestor’s existence and the signing step, removing the key-management burden that a fully custom attestor setup would otherwise require.

**Real-World Connection**

A team that hand-rolls its own KMS keyring, attestor, and per-build signing step takes on key rotation, access control for the signing key, and a scripted or manual signing step that has to run reliably on every single build or the pipeline silently stops producing deployable images. Using the built-by-cloud-build attestor removes all of that: Cloud Build keeps attesting every build automatically, and the only thing the platform team maintains is the one-line policy requirement.

**Memory Hook**

If Cloud Build built it, let Cloud Build attest it — reach for your own Cloud KMS keyring and attestor only when you need to verify something Cloud Build’s built-in attestor doesn’t already cover.

**30-Second Exam Takeaway**

When a question asks to restrict GKE (or Cloud Run) deployments to images built by Cloud Build with minimal setup, look for the option that simply points a Binary Authorization policy at the built-by-cloud-build attestor — any option involving your own Cloud KMS key, a hand-written attestation step, or a custom verification function is doing manual work Cloud Build already automates.

**Official References**

[**Google Cloud — Securing deployments by only allowing images built by Cloud Build (Binary Authorization):**](https://cloud.google.com/binary-authorization/docs/deploy-cloud-build)Supports: the correct-answer mechanism (Cloud Build’s automatic creation of the built-by-cloud-build attestor and automatic attestation signing, verified by Binary Authorization at deploy time)

[**Google Cloud — Securing image deployments to Cloud Run and GKE (Cloud Build docs):**](https://cloud.google.com/build/docs/securing-builds/use-binary-authorization) Supports: the detail that Cloud Build generates and signs attestations automatically, and the multi-project note relevant to “production project,” used to eliminate the manual Cloud KMS approach in option C

</details>

---

### Exam 3 · Q46

You’re designing a secure Cloud Build pipeline for a web application that needs access to a package manager. The package manager credentials are highly sensitive and must be protected from unauthorized access. You need a way to retrieve these credentials securely at build time, following Google-recommended practice, while keeping ongoing maintenance to a minimum. What should you do?

- A. Grant roles/cloudkms.cryptoKeyDecrypter to the Cloud Build service account. Store Cloud KMS-encrypted data in the build config file, specifying the secret under the secrets field.
- B. Grant roles/cloudkms.cryptoKeyDecrypter to the Cloud Build service account. Store Cloud KMS-encrypted data in the build config file, specifying the secret under the availableSecrets.inline field.
- C. Grant roles/secretmanager.secretAccessor to the service account used for the build, and specify the secret under the availableSecrets.secretManager field.
- D. Store base64-encoded data in the web application’s source control repository, and decrypt and use the secret during the build.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Grant roles/secretmanager.secretAccessor to the service account used for the build, and specify the secret under the availableSecrets.secretManager field.

**Correct Answer**

**C. Grant roles/secretmanager.secretAccessor to the service account used for the build, and specify the secret under the availableSecrets.secretManager field.**

**Exam Reasoning Explanation**

Separate the hard requirement from the preference: the hard requirement is real protection against unauthorized access, and the preference is low ongoing maintenance. D fails the hard requirement outright, since base64 is an encoding, not encryption, and provides no actual confidentiality once it’s sitting in source control. That leaves A, B, and C, which all genuinely protect the secret, so the preference decides between them. A and B both require you to manually encrypt the credential with Cloud KMS and embed the resulting ciphertext directly in the build config file — meaning every rotation of the credential requires re-encrypting and updating that file. Secret Manager, referenced through availableSecrets.secretManager, lets Cloud Build pull the current value directly from a dedicated secret store with no ciphertext embedded in the build config at all, which is both Google’s documented, purpose-built mechanism for this and the option with the least ongoing upkeep.

**Key Exam Clues**

  * **“package manager credentials are highly sensitive and need to be protected from unauthorized access”** — a decisive requirement clue that rules out D immediately, since base64 offers no real protection.

  * **“securely retrieve credentials at build time following Google-recommended practices”** — a technical signal pointing at Cloud Build’s documented secret-handling guides, which treat Secret Manager integration as the primary path and the Cloud KMS-based top-level secrets field as legacy.

  * **“keep maintenance overhead to a minimum”** — a decisive preference clue: it favors whichever secret-retrieval mechanism requires the least manual work to keep current, which rules out the two options that embed a static ciphertext in the build config.

  * **“secrets field” vs. “availableSecrets.inline field” vs. “availableSecrets.secretManager field”** — technical anchors distinguishing the legacy mechanism, the current KMS-based mechanism, and the Secret Manager mechanism from one another.

**Why This Is Correct**

Secret Manager is Google Cloud’s dedicated service for storing credentials like API keys and passwords, with built-in versioning and access control. Granting the build’s service account the Secret Manager Secret Accessor role and referencing the secret through the availableSecrets.secretManager field lets Cloud Build fetch the current secret value directly at build time, with the secret’s actual value living only in Secret Manager — never encoded or embedded in the build config. When the credential changes, you add a new version in Secret Manager; there’s no build config file to re-encrypt or edit, which is exactly what keeps maintenance low while still meeting Google’s documented, recommended approach for secret access in Cloud Build.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Outdated:** Specifying the secret under the top-level secrets field is Cloud Build’s legacy mechanism for using Cloud KMS-encrypted data; it works, but it’s the superseded approach, and every credential rotation means manually re-running the Cloud KMS encryption and committing a new ciphertext into the build config.

  * **Option B — Technically Possible but Not Best:** The availableSecrets.inline field is the current (non-legacy) way to use Cloud KMS-encrypted data directly in the build config, so this is a legitimate, secure option. But it still requires manually encrypting the credential and maintaining the resulting ciphertext inside the build config file, which is more ongoing effort than letting Secret Manager hold the live value.

  * **Option D — Violates Requirement:** Base64 is a reversible encoding scheme, not encryption — anyone who can read the repository can trivially decode the “encrypted” value. Storing it in source control also exposes the credential to everyone with repository access, which directly contradicts the requirement to protect it from unauthorized access.

**Exam Trap**

The trap is treating A, B, and C as functionally interchangeable because all three involve granting a role and referencing a field in the build config — on the surface, they look like minor syntax variations. The real distinction the question is testing is between a static, manually-maintained encrypted value living in the build config (A, B) and a live reference to a centrally managed secret store (C), which is where the “minimize maintenance” requirement actually bites.

**Foundation Concept**

When a CI/CD system needs a sensitive value at build time, there are two fundamentally different patterns: encrypt the value once and embed the ciphertext in configuration (requiring you to manage encryption and re-embed ciphertext on every change), or store the value in a dedicated secret-management service and reference it by name and version (letting the service own versioning, rotation, and access control). The second pattern is lower-maintenance by design, because updating the secret never requires touching the pipeline configuration itself.

**Real-World Connection**

A team using inline Cloud KMS-encrypted secrets in its build config has to coordinate a config change across every repository that uses the credential whenever it rotates, and risks builds breaking if that step is missed. A team using Secret Manager rotates the credential once, in one place, and every build referencing “latest” (or the updated version) picks it up automatically, with no pipeline changes required.

**Memory Hook**

A ciphertext embedded in the build config has to be re-embedded every time the secret changes; a Secret Manager reference doesn’t.

**30-Second Exam Takeaway**

When a Cloud Build question asks for secure secret retrieval with minimal maintenance, look for Secret Manager and the secretAccessor role over any option that embeds Cloud KMS-encrypted ciphertext directly in the build config (whether under the legacy secrets field or the newer inline field) — and treat base64 “encryption” as an automatic disqualifier.

**Official References**

[**Google Cloud — Use secrets from Secret Manager (Cloud Build):**](https://cloud.google.com/build/docs/securing-builds/use-secrets) Supports: the correct-answer mechanism (the Secret Manager Secret Accessor role and the availableSecrets.secretManager field)

[**Google Cloud — Use encrypted credentials from Cloud KMS (Cloud Build)**](https://cloud.google.com/build/docs/securing-builds/use-encrypted-credentials)**:** Supports: the distinction between the legacy top-level secrets field and the current inline field, used to classify and eliminate options A and B

</details>

---

### Exam 3 · Q47

You’re setting up a Cloud Deploy pipeline to deploy an application to Google Kubernetes Engine (GKE) as a Deployment. You need the Deployment to run two replicas in the development environment and five replicas in production, while keeping every other configuration parameter identical across both environments. You also want to minimize the ongoing effort of updating the manifests going forward. How should you configure the skaffold.yaml file?

- A. Define multiple profiles, and configure the manifests.kustomize section.
- B. Define a single profile, and configure the manifests.kustomize section.
- C. Define multiple profiles, and configure the manifests.rawYaml section.
- D. Define a single profile, and configure the manifests.rawYaml section.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Define multiple profiles, and configure the manifests.kustomize section.

**Correct Answer**

**A. Define multiple profiles, and configure the manifests.kustomize section.**

**Exam Reasoning Explanation**

There are two separate requirements stacked here: the replica count must differ per environment while everything else stays identical, and future manifest updates should require minimal duplicate effort. Kustomize is built for exactly the first requirement — a shared base manifest plus small, targeted overlay patches (here, just the replica count) — which is what keeps “everything else” automatically consistent, since there’s only ever one copy of the non-varying configuration. The second requirement, differentiating dev from production, needs a profile per target, because Cloud Deploy activates a specific Skaffold profile for each target in the delivery pipeline, and each profile can point to its own Kustomize overlay. A single profile has no way to represent two different overlay paths for two different targets at once, so both “multiple profiles” and “kustomize” are necessary together.

**Key Exam Clues**

  * **“two replicas in the development environment and five replicas in the production environment”** — a technical signal that per-target configuration differs, which requires some mechanism to select different values per target.

  * **“all other configuration parameters are consistent between environments”** — a decisive constraint: it favors a shared base manifest with small overlay patches over separate, independently maintained files per environment.

  * **“minimize developmental overhead when updating the manifests in the future”** — a decisive preference clue: it rules out any approach that requires keeping multiple near-duplicate manifest files in sync by hand.

  * **“skaffold.yaml”** and the explicit manifests.kustomize vs. manifests.rawYaml naming — technical anchors pointing directly at Skaffold’s two distinct manifest-rendering mechanisms, one of which (Kustomize) supports overlay patching and one of which (raw YAML) does not.

**Why This Is Correct**

Cloud Deploy renders manifests through Skaffold, and its documented pattern for per-target variation with Kustomize is to define one profile per target, each with its own manifests.kustomize entry pointing at a target-specific overlay directory (for example, one overlay for development, one for production). Because Kustomize overlays only need to specify the fields that differ — here, just the replica count — the base manifest holding every other setting is defined once and shared, so there’s nothing to keep manually synchronized across environments. Cloud Deploy’s delivery pipeline then references the matching profile for each target, so the dev target renders with two replicas and the production target renders with five, with a single source of truth for everything else.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Violates Requirement:** A single profile can only point to one Kustomize configuration. Since development and production need different replica counts, you need two separate overlay paths active for their respective targets — which requires two profiles. A single profile has no way to represent both outcomes at once.

  * **Option C — Technically Possible but Not Best:** Multiple profiles with raw YAML can technically achieve different replica counts by pointing each profile at an entirely separate manifest file (for example, one full file for development, another for production). But raw YAML has no overlay/patch mechanism, so every other configuration parameter has to be duplicated identically across both files and manually kept in sync — directly working against “all other configuration parameters are consistent” and “minimize overhead when updating manifests in the future.”

  * **Option D — Violates Requirement:** A single profile using raw YAML means exactly one static manifest file with no mechanism to vary anything — including the replica count — between development and production. This configuration can’t actually produce two replicas in one environment and five in the other at all.

**Exam Trap**

The trap is treating “profiles” and “manifest format” as independent choices rather than recognizing they have to work together. A learner might reason “Kustomize handles the differences, so one profile is enough,” missing that Cloud Deploy’s target-to-profile association is itself what selects which overlay applies — the overlay mechanism and the per-target profile selection are two halves of the same solution.

**Foundation Concept**

Kustomize’s core design is a base configuration plus small, composable overlay patches per variant, which is precisely suited to “mostly identical configuration, with a few deliberate per-environment differences.” Pairing that with Skaffold profiles — one profile per Cloud Deploy target, each pointing at its own overlay — is the standard way to let a single pipeline definition serve multiple environments without duplicating the parts that should stay identical.

**Real-World Connection**

A team maintaining separate full raw-YAML manifests per environment often finds that a change meant for every environment (a new label, an updated resource limit, a changed probe setting) gets applied to one file and forgotten in another, causing environments to drift apart silently. A team using a shared Kustomize base with per-environment overlays makes that same change once, in the base, and every environment picks it up automatically on the next render — the overlays only ever need to contain the replica-count difference.

**Memory Hook**

Same manifest everywhere except one small per-environment difference → one shared base plus per-target Kustomize overlays, selected by one profile per target.

**30-Second Exam Takeaway**

When a Cloud Deploy/Skaffold question asks for consistent manifests across environments with one or two deliberate per-environment differences and low future maintenance, look for multiple profiles paired with Kustomize overlays — raw YAML forces full file duplication, and a single profile can’t represent more than one target’s configuration at a time.

**Official References**

[**Google Cloud — Manage manifests in Cloud Deploy (rendering using Kustomize)**](https://cloud.google.com/deploy/docs/skaffold)**:** Supports: the correct-answer mechanism (one profile per target, each pointing to its own Kustomize configuration) and the raw-manifest alternative requiring separate full files per target, used to eliminate options C and D

</details>

---

### Exam 3 · Q48

A third-party application continuously uploads encrypted files to a Cloud Storage bucket. Each file is protected with an HMAC-SHA256 key and contains sensitive data that must be loaded into BigQuery for analysis every day shortly after midnight. You need to design a secure, fully automated pipeline that decrypts these files and loads them into BigQuery, following Google-recommended practices while keeping custom development effort to a minimum. What should you do?

- A. 1. Upload the decryption key into the same Cloud Storage bucket that stores the encrypted files. 2. Build a Cloud Build pipeline that decrypts each file and then loads it into BigQuery. 3. Set up a Cloud Scheduler job that triggers the pipeline daily at the required time.
- B. 1. Create a Cloud Key Management Service (Cloud KMS) key ring and import the decryption key into it. 2. Containerize the decrypt-and-load script, then push the resulting image to an Artifact Registry repository. 3. Create a Cloud Run job that runs the image on a recurring schedule. 4. Grant the Cloud Run service agent the Cloud KMS CryptoKey Encrypter/Decrypter role.
- C. 1. Create a Cloud Key Management Service (Cloud KMS) key ring and import the decryption key into it. 2. Configure a Cloud Build trigger that calls Cloud KMS to decrypt each file before loading it into BigQuery. 3. Set up a Cloud Scheduler job that fires the trigger daily at the required time.
- D. 1. Upload the decryption key into the same Cloud Storage bucket that stores the encrypted files. 2. Write a script that retrieves the key from Cloud Storage and uses it to decrypt each file. 3. Containerize the script and push the resulting image to an Artifact Registry repository. 4. Create a Cloud Run job that runs the image on a recurring schedule.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. 1. Create a Cloud Key Management Service (Cloud KMS) key ring and import the decryption key into it. 2. Containerize the decrypt-and-load script, then push the resulting image to an Artifact Registry repository. 3. Create a Cloud Run job that runs the image on a recurring schedule. 4. Grant the Cloud Run service agent the Cloud KMS CryptoKey Encrypter/Decrypter role.

**Correct Answer**

**B. 1. Create a Cloud Key Management Service (Cloud KMS) key ring and import the decryption key into it. 2. Containerize the decrypt-and-load script, then push the resulting image to an Artifact Registry repository. 3. Create a Cloud Run job that runs the image on a recurring schedule. 4. Grant the Cloud Run service agent the Cloud KMS CryptoKey Encrypter/Decrypter role.**

**Exam Reasoning Explanation**

Must-have constraints: the key has to be managed securely (not just “available”), the job must run unattended on a daily schedule, and the solution should take minimal custom engineering while still following Google’s own recommended pattern. Preference, not requirement: which specific compute product runs the script, as long as it’s a managed, low-maintenance option. Capability: Cloud KMS exists specifically to store and broker cryptographic key material — including imported HMAC-SHA256 key material — without ever exposing the raw key to application code or storage; Cloud Run jobs exist specifically to run a container to completion on a schedule, with a built-in “Add Scheduler Trigger” integration that requires no pipeline authoring. Elimination: any option that puts the decryption key in the same Cloud Storage bucket as the data it protects (A, D) fails the security requirement outright, since anyone with read access to the bucket has both the ciphertext and the key. Any option that repurposes Cloud Build — a CI/CD build tool meant for compiling, testing, and deploying code — as the engine for a recurring data-decrypt-and-load job (A, C) is forcing a tool to do something it isn’t designed or optimized for, which works against “Google-recommended practices” and “minimal development effort.” Decision: Option B is the only one that stores the key correctly (Cloud KMS), runs the job with the purpose-built scheduled-execution service (Cloud Run jobs), and explicitly grants the minimum IAM permission needed to decrypt.

**Key Exam Clues**

  * “HMAC-SHA256 key” and “sensitive data” — a hard constraint that key handling itself is part of what’s being graded, not incidental detail.

  * “secure and automated solution” — a compound hard constraint; an option that is automated but not secure (A, D) or that strains to be secure through an awkward mechanism (C) does not fully satisfy it.

  * “follow Google-recommended practices” — a technical signal pointing toward purpose-built managed services (Cloud KMS for keys, Cloud Run jobs for scheduled containers) over repurposed tooling.

  * “minimizing the required development effort” — an elimination signal favoring the option with the least custom pipeline/trigger configuration, which favors Cloud Run’s native scheduler integration over building a Cloud Build trigger from scratch.

  * “every day after midnight” — a sequence/cardinality instruction confirming a recurring, unattended schedule is required; satisfied by all four options, so it narrows nothing on its own but rules out any manual or ad hoc process.

**Why This Is Correct**

Importing the HMAC-SHA256 key into a Cloud KMS key ring means the raw key material lives inside a service designed to guard it — it can be used to decrypt without ever being readable in plaintext outside of an authorized call, and access is governed by IAM rather than by whoever can read a storage bucket. Packaging the decrypt-and-load logic as a container and publishing it to Artifact Registry is the standard, Google-recommended way to make a piece of automation portable and versioned. A Cloud Run job is purpose-built to execute that container to completion on a schedule — Cloud Run’s own console and CLI offer a one-step “Add Scheduler Trigger” that wires up Cloud Scheduler for you, which is precisely the “minimal development effort” path. Finally, granting the Cloud KMS CryptoKey Encrypter/Decrypter role (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) is the least-privilege grant needed for the executing identity to call Decrypt against that specific key — nothing more, nothing less.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement:** Placing the decryption key in the same bucket as the encrypted files defeats the purpose of encrypting them in the first place — anyone who can read the bucket can read both the ciphertext and the key. Using Cloud Build as the recurring processing engine is also a mismatch: Cloud Build is designed for build/test/deploy steps triggered by source changes, not as a standing daily data-decrypt-and-load job, making this a “Different Use Case” layered on top of the security failure.

**Option C — Technically Possible but Not Best:** This option gets key management right by using Cloud KMS, so it isn’t insecure, but it still drives the daily decrypt-and-load work through a Cloud Build trigger. Cloud Build pipelines are optimized for short-lived build/deploy jobs rather than ongoing scheduled data processing, so while it could be made to work, it isn’t the Google-recommended, lowest-effort fit, and unlike Option B it never grants the executing identity permission to call Cloud KMS, which would leave decryption failing on IAM grounds as described.

**Option D — Violates Requirement:** The execution pattern (containerize the script, publish to Artifact Registry, run as a scheduled Cloud Run job) is structurally identical to the correct answer’s pattern, but it inherits the same flaw as Option A — the decryption key sits in the same Cloud Storage bucket as the data it’s meant to protect, which is the one requirement this question is most directly testing.

**Exam Trap**

The trap is treating “automated and running on a schedule” as sufficient to call a design secure. Two of the four options (A and D) are fully automated and correctly scheduled, yet both fail because of where the key lives, not how the job runs. The question would only reward storing the key in Cloud Storage if it were encrypted there by a separate, properly managed key — simply dropping the raw decryption key next to the ciphertext is never the secure choice, regardless of how clean the rest of the automation looks.

**Foundation Concept**

The transferable idea is separation of secrets from data: a cryptographic key should live in a system designed to broker access to it under IAM control (Cloud KMS), never in the same storage location as the material it protects. Layered on top of that is tool fit: a scheduled, recurring execution engine purpose-built for running a container to completion (Cloud Run jobs) is the Google-recommended, low-effort choice for batch-style automation, while a CI/CD build tool (Cloud Build) is optimized for building and deploying code, not for standing in as a daily ETL engine. One nuance worth flagging: in production, the identity that actually needs the Cloud KMS CryptoKey Encrypter/Decrypter role is the Cloud Run job’s runtime service account — the identity your code executes as and uses to call other Google Cloud APIs — which is distinct from the Google-managed “Cloud Run service agent” that handles internal plumbing like pulling the container image. The exam phrasing uses “service agent” loosely to mean “the identity Cloud Run uses,” so for this question treat the two as the same target; just know the distinction exists if you’re wiring this up for real.

**Real-World Connection**

Teams building scheduled data-ingestion jobs like this one typically standardize on exactly this pattern — Cloud KMS for any key material, a container image in Artifact Registry, and a Cloud Run job on a Cloud Scheduler trigger — because it keeps the security boundary (who can decrypt) and the operational boundary (who can deploy a new version of the script) cleanly separate and auditable through Cloud Audit Logs, while avoiding the ongoing maintenance burden of a standing VM or a misapplied CI/CD pipeline.

**Memory Hook**

Keys go in Cloud KMS, never in the bucket next to what they protect; recurring container jobs go in Cloud Run jobs, not Cloud Build.

**30-Second Exam Takeaway**

Whenever a Google Cloud scenario combines “decrypt a file” with “run it on a schedule,” check two things independently: does the key live in Cloud KMS (not alongside the data), and does the job run on a tool built for scheduled execution (Cloud Run jobs) rather than a CI/CD build tool — an option can get one right and still be wrong on the other.

**Official References**

[**Google Cloud — Import a key into Cloud KMS**](https://cloud.google.com/kms/docs/key-import)**:** Supports: confirms HMAC-SHA256 key material can be imported into Cloud KMS for secure storage and use

[**Google Cloud — Execute Cloud Run jobs on a schedule:**](https://cloud.google.com/run/docs/execute/jobs-on-schedule) Supports: confirms Cloud Run jobs natively integrate with Cloud Scheduler as the low-effort, Google-recommended way to run a container on a recurring schedule

[**Google Cloud — Cloud KMS permissions and roles**](https://cloud.google.com/kms/docs/reference/permissions-and-roles)**:** Supports: confirms the exact name and effect of the Cloud KMS CryptoKey Encrypter/Decrypter role granted in the correct answer

[**Google Cloud — Cloud Build overview:**](https://cloud.google.com/build/docs/overview) Supports: clarifies Cloud Build’s intended CI/CD build/deploy purpose, the basis for eliminating Options A and C as a tool mismatch

</details>

---

### Exam 3 · Q57

Jenkins orchestrates application deployments to Google Kubernetes Engine (GKE) and on-premises VMs. Following an expansion of the on-premises infrastructure, deployments to those VMs take longer to start, although resource utilization remains within normal levels. You need to reduce the delay before on-premises deployments begin. Which change should you make?

- A. Increase the CPU performance and memory capacity of the on-premises VMs.
- B. Adopt blue-green deployments for applications running on the on-premises VMs.
- C. Increase the configured number of Jenkins executors.
- D. Configure Jenkins to retrieve deployment artifacts from an on-premises artifact repository.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Increase the configured number of Jenkins executors.

**Correct Answer**

**C. Increase the configured number of Jenkins executors.**

**Exam Reasoning Explanation**

The requirement concerns deployment **start delay** , while normal utilization provides no evidence that faster hardware is needed. Among the choices, increasing execution capacity most directly addresses tasks waiting to begin. Changing deployment strategy or artifact storage does not increase Jenkins scheduling capacity.

**Key Exam Clues**

  * **“Expansion of the on-premises infrastructure” — Technical signal:** The orchestration configuration might need to accommodate additional deployment work.

  * **“Take longer to start” — Hard constraint:** Focus on initiation and scheduling rather than execution speed.

  * **“Resource utilization remains within normal levels” — Technical signal:** Hardware saturation is not the demonstrated bottleneck.

**Why This Is Correct**

A Jenkins executor is a task-execution slot. Its configured count determines how many tasks can run concurrently on a node. Increasing that count on eligible agents allows additional deployment tasks to begin without waiting for an occupied slot.

This helps when executor availability is the constraint and the agents have sufficient CPU, memory, I/O, and network capacity. Configure execution capacity on agents; Jenkins discourages running deployment work on the controller’s built-in node. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** Faster CPUs and additional memory help resource-bound workloads. They do not directly increase the configured executor count, and the scenario reports normal utilization.

  * **Option B — Different Use Case:** Blue-green deployment maintains alternate application environments and switches traffic between them to support safer releases and rollback. It does not resolve Jenkins tasks waiting for execution capacity. 

  * **Option D — Different Use Case:** An artifact repository changes where deployment packages are stored and retrieved. It does not increase Jenkins execution slots, and the scenario provides no evidence that artifact retrieval causes the delay.

**Exam Trap**

Normal CPU utilization does not guarantee that Jenkins has an available executor: concurrency limits can leave tasks waiting despite hardware headroom. If measurements instead showed CPU or memory saturation during deployment execution, upgrading resources could become appropriate.

**Foundation Concept**

Separate **queue waiting time** from **task execution time**. These symptoms favor an executor-capacity explanation, but normal resource utilization alone does not prove it. In production, inspect the queue reason and eligible-agent availability before tuning concurrency; offline agents or restrictive labels can also delay starts. 

**Real-World Connection**

Increase agent executor capacity gradually, then compare queue waiting time and resource utilization. This can shorten deployment initiation while helping you avoid introducing resource contention through excessive parallelism.

**Memory Hook**

Slow starts with hardware headroom point toward execution-slot availability; slow running tasks require a different diagnosis.

**30-Second Exam Takeaway**

Determine whether work is waiting to start or running slowly. When Jenkins concurrency is the limiting factor, increase eligible-agent executor capacity within the resources available.

**Official References**

  * [**Jenkins — Managing Nodes:**](https://www.jenkins.io/doc/book/managing/nodes/)Supports: Executor semantics, concurrency limits, resource considerations, and separation of agent execution from controller responsibilities.

  * [**Jenkins — Executor Starvation:**](https://www.jenkins.io/doc/book/using/executor-starvation/)

Supports: Queue delays caused by unavailable executors, offline agents, and agent-label restrictions.

</details>

---

### Exam 3 · Q60

Your team builds an application from a Dockerfile using Cloud Build and stores the resulting container images in Artifact Registry. Developers report that builds take too long. You need to reduce build times using Google-recommended practices. What should you do?

- A. Use `--cache-from` to reference a previously built image in Artifact Registry, and copy frequently modified files in later Dockerfile instructions.
- B. Use `--cache-from` to reference a previously built image in Artifact Registry, and copy frequently modified files in earlier Dockerfile instructions.
- C. Store the container-layer cache in Cloud Storage, and copy frequently modified files in earlier Dockerfile instructions.
- D. Store the container-layer cache in Cloud Storage, and copy frequently modified files in later Dockerfile instructions.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Use `--cache-from` to reference a previously built image in Artifact Registry, and copy frequently modified files in later Dockerfile instructions.

**Correct Answer**

**A. Use**`**--cache-from**`**to reference a previously built image in Artifact Registry, and copy frequently modified files in later Dockerfile instructions.**

**Exam Reasoning Explanation**

The solution must combine cache reuse with an instruction order that preserves reusable work. Artifact Registry already holds the images, so use a previous image as the cache source and introduce frequently changing inputs later. A provides both optimizations. 

**Key Exam Clues**

  * **“From a Dockerfile” — Technical signal:** Docker layer caching applies.

  * **“Images in Artifact Registry” — Technical signal:** Previously built images can supply the cache.

  * **“Reduce build times” — Required outcome:** Avoid rebuilding unchanged work.

  * **“Google-recommended practices” — Preference:** Favors the documented Docker-specific caching approach.

**Why This Is Correct**

Google’s documented Cloud Build configuration pulls a previously built image from Artifact Registry and references it through `--cache-from`. An existing cache image must be available for reuse. 

Docker invalidates cached work when relevant instructions or inputs change. Placing frequently modified files later preserves earlier layers, such as dependency installation, when their inputs remain unchanged.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Technically Possible but Not Best:** The registry cache is appropriate, but frequently changing files introduced early invalidate subsequent work. This reduces the benefit of caching.

  * **Option C — Technically Possible but Not Best:** Cloud Storage can preserve build results through a custom save-and-restore process. However, it does not use the documented image-cache approach, and its early placement of changing files further limits reuse. 

  * **Option D — Technically Possible but Not Best:** The instruction order is appropriate. However, a Cloud Storage cache introduces an additional restoration workflow when Google’s Docker-specific guidance already supports using an image from Artifact Registry. 

**Exam Trap**

Choosing a cache source is only half the solution. A cache cannot preserve dependent layers after their inputs change. Copying stable dependency manifests early is useful; copying frequently changing application source before dependency installation is usually inefficient.

**Foundation Concept**

Build caching reuses unchanged work. Order stable, expensive operations before frequently changing inputs wherever dependencies allow. Here, “later” refers to Dockerfile instruction order, rather than requiring a separate multi-stage build.

**Real-World Connection**

Copy dependency manifests and lockfiles, install dependencies, and then copy application source. Routine source edits can then reuse the dependency layer, shortening the feedback cycle for developers. 

**Memory Hook**

Reuse the previous image, and place frequently changing inputs late.

**30-Second Exam Takeaway**

For Docker builds in Cloud Build, combine `--cache-from` with effective layer ordering. Measure the result: retrieving a cache image also takes time, so the benefit depends on how much work is reused. 

**Official References**

  * [**Google Cloud Build — Best practices for speeding up builds:**](https://docs.cloud.google.com/build/docs/optimize-builds/speeding-up-builds)

Supports: Artifact Registry images with `--cache-from`, cache prerequisites, transfer overhead, and Cloud Storage directory caching.

  * [**Docker — Optimize cache usage in builds:**](https://docs.docker.com/build/cache/optimize/)

Supports: Cache invalidation, instruction ordering, and separating dependency installation from frequently changing source files.

</details>

---

### Exam 4 · Q2

You are configuring a continuous integration (CI) pipeline in Cloud Build with the following `cloudbuild.yaml` configuration:
    
          1. steps:
      2. - name: foo
      3.   id: foo
      4. - name: bar
      5.   id: bar
      6. - name: baz
      7.   id: baz

The `foo` and `bar` steps each take five minutes and can run independently. The `baz` step must wait until both have completed successfully. You need to reduce build time by running the independent steps concurrently. What should you do?

- A. Add the following machine configuration:
      
            1. options:
        2.   machineType: 'E2_HIGHCPU_8'
- B. Add the following machine configuration:
      
            1. options:
        2.   machineType: 'E2_HIGHCPU_32'
- C. Configure `foo` to start immediately and make `baz` wait for both preceding steps:
      
            1. steps:
        2. - name: foo
        3.   id: foo
        4.   waitFor: ['-']
        5. - name: bar
        6.   id: bar
        7. - name: baz
        8.   id: baz
        9.   waitFor:
        10.     - foo
        11.     - bar
- D. Configure both independent steps to start immediately and make `baz` wait for their completion.
      
            1. steps:
        2. - name: foo
        3.   id: foo
        4.   waitFor: ['-']
        5. - name: bar
        6.   id: bar
        7.   waitFor: ['-']
        8. - name: baz
        9.   id: baz
        10.   waitFor:
        11.     - foo
        12.     - bar

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Configure both independent steps to start immediately and make `baz` wait for their completion.

**Correct Answer**

**D. Configure both independent steps to start immediately and make**`**baz**`**wait for their completion.**

**Exam Reasoning Explanation**

Cloud Build executes steps sequentially by default. Option D explicitly allows `foo` and `bar` to run concurrently while preserving both dependencies required by `baz`. 

**Key Exam Clues**

  * **Parallelism opportunity:** `foo` and `bar` are independent.

  * **Dependency constraint:** `baz` requires both steps to finish successfully.

  * **Optimization goal:** Reduce elapsed build time through concurrency.

**Why This Is Correct**

  * `waitFor: ['-']` makes each independent step eligible to start when the build begins.

  * `waitFor: ['foo', 'bar']` makes `baz` wait for successful completion of both identified steps. 

**Why the Other Options Are Not the Best Fit**

  * **A — Different Use Case:** More vCPUs can accelerate workloads that benefit from additional CPU capacity. Changing the machine type does not change the step dependencies or enable concurrent execution. 

  * **B — Different Use Case:** A larger machine likewise leaves the sequential execution order unchanged. It does not implement the requested parallelism. 

  * **C — Incorrect:** `bar` has no `waitFor` setting, so it waits for all preceding steps—including `foo`—to finish. The two five-minute steps remain sequential. 

**Exam Trap**

Adding `waitFor: ['-']` only to the first step does not create concurrency. The first step already depends implicitly on the start of the build.

**Foundation Concept**

`id` identifies a build step. `waitFor` references those identifiers to establish dependencies. An omitted or empty `waitFor` waits for all preceding steps; it does **not** mean “no dependencies.” 

**Real-World Connection**

Assuming sufficient resources and unchanged execution times, the prerequisite phase decreases from approximately **10 minutes to 5 minutes**. The complete pipeline still includes the execution time of `baz` and any startup overhead.

**Memory Hook**

Use `['-']` to start independently and step IDs to wait for prerequisites.

**30-Second Exam Takeaway**

Choose **D**. Start `foo` and `bar` concurrently, then let `baz` run only after both succeed.

**Official References**

  * [**Configuring the order of build steps**](https://docs.cloud.google.com/build/docs/configuring-builds/configure-build-step-order)  
Supports: Concurrent execution, `waitFor: ['-']`, and explicit dependencies.

  * [**Build configuration file schema**](https://docs.cloud.google.com/build/docs/build-config-file-schema)  
Supports: Step identifiers, default sequential execution, and omitted `waitFor` behavior.

  * [**Increase vCPU for builds**](https://docs.cloud.google.com/build/docs/optimize-builds/increase-vcpu-for-builds)  
Supports: Machine-size configuration and its distinction from build-step scheduling.

</details>

---

### Exam 4 · Q4

Your application is running in production on Cloud Run. Your team has completed a new version, revision B, and wants to test it with 10% of your clients.

You need to implement this test with the **least operational effort**. What should you do?

- A. Deploy revision B to the existing service without allocating production traffic. Assign it a revision tag and share its tagged URL with 10% of your clients.
- B. Deploy revision B to a separate Cloud Run service. Update the existing application to forward a percentage of incoming requests to the new service.
- C. Deploy revision B to a separate Cloud Run service. Configure a load balancer to distribute traffic between the existing and new services.
- D. Deploy revision B to the existing service without initially allocating traffic. Configure Cloud Run traffic splitting to send 10% of traffic to revision B and 90% to the existing revision.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Deploy revision B to the existing service without initially allocating traffic. Configure Cloud Run traffic splitting to send 10% of traffic to revision B and 90% to the existing revision.

**Correct Answer**

**D. Deploy revision B to the existing service without initially allocating traffic. Configure Cloud Run traffic splitting to send 10% of traffic to revision B and 90% to the existing revision.**

**Exam Reasoning Explanation**

Cloud Run provides native percentage-based routing between revisions of the same service. This supports a canary rollout with minimal configuration and no application routing changes. 

**Key Exam Clues**

  * **Existing platform:** The application already runs on Cloud Run.

  * **Limited exposure:** Test the new revision before a complete rollout.

  * **Primary preference:** Use the least operational effort.

**Why This Is Correct**

  1. Deploy revision B with no initial traffic allocation.

  2. Set the service’s traffic allocation to **90% for the existing revision and 10% for revision B**.

  3. Assess revision B before increasing its allocation.

Cloud Run manages routing through the existing service endpoint. 

**Why the Other Options Are Not the Best Fit**

  * **A — Technically Possible but Not Best:** Tagged URLs support direct testing of a specific revision. However, distributing a different URL requires coordinating client participation instead of automatically allocating traffic through the existing endpoint. 

  * **B — Technically Possible but Not Best:** Application-level forwarding requires code changes and another service. Native revision traffic splitting provides the required rollout mechanism with less work. 

  * **C — Technically Possible but Not Best:** This introduces another service and load-balancing configuration, including serverless backends. Those additional components are unnecessary for splitting traffic between revisions of one service. 

**Exam Trap**

**10% of requests is not necessarily 10% of distinct clients.** D is the intended answer for a percentage-based canary. If the requirement means a fixed, identifiable client cohort, traffic splitting alone does not guarantee that assignment. Session affinity is also best effort. 

**Foundation Concept**

Traffic allocation controls the proportion of requests sent to each revision. A revision tag provides a separate URL that targets a particular revision directly.

**Real-World Connection**

After deploying revision B without traffic, configure the split using actual revision names:
    
          1. gcloud run services update-traffic SERVICE \
      2.   --region=REGION \
      3.   --to-revisions=CURRENT_REVISION=90,REVISION_B=10

The command updates routing without requiring application changes. 

**Memory Hook**

For a simple Cloud Run canary, split traffic between revisions of the existing service.

**30-Second Exam Takeaway**

Choose **D** for the lowest-effort 90/10 canary rollout. Remember that the allocation applies to traffic rather than a guaranteed fixed group of clients.

**Official References**

  * [**Rollbacks, gradual rollouts, and traffic migration**](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration)  
Supports: No-traffic deployment, revision traffic splitting, and tagged testing URLs.

  * [**gcloud run services update-traffic**](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update-traffic)  
Supports: Configuring explicit 90/10 revision allocations.

  * [**Set session affinity for services**](https://docs.cloud.google.com/run/docs/configuring/session-affinity?)  
Supports: Request routing behavior and limitations of client affinity.

  * [**Set up an external Application Load Balancer with serverless backends**](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-serverless)  
Supports: The additional configuration introduced by option C.

</details>

---

### Exam 4 · Q8

Your company runs a GKE application composed of 12 microservices across development (Dev), staging (Staging), and production (Prod) environments. Multiple teams develop features concurrently. Deployments from different feature branches into the shared Dev cluster cause dependency test failures and delay releases.

You need a cost-effective approach that gives developers stable environments for testing their microservice changes independently of other development work. What should you do?

- A. Use Cloud Build to build container images and update Kubernetes manifests from main-branch merge requests. Use Config Sync to deploy the images for testing in dynamically created namespaces within the autoscaling Dev cluster. Delete the namespaces after testing.
- B. Use Cloud Build to build container images and update Kubernetes manifests for each commit. Use Cloud Deploy to progressively deliver changes to the Dev, Staging, and Prod clusters. Use Config Sync to maintain consistent Kubernetes configurations across environments.
- C. Use Cloud Build to build container images and update Kubernetes manifests from feature-branch commits. Use Config Sync to deploy the images for testing in dynamically created namespaces within the autoscaling Dev cluster. Delete the namespaces after testing.
- D. Use Cloud Build to build container images and update Kubernetes manifests from feature-branch commits. Use Config Sync to deploy the images into a separate, dynamically provisioned Dev cluster for each feature branch. Delete the clusters during the merge-request workflow.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Use Cloud Build to build container images and update Kubernetes manifests from feature-branch commits. Use Config Sync to deploy the images for testing in dynamically created namespaces within the autoscaling Dev cluster. Delete the namespaces after testing.

**Correct Answer**

**C. Use Cloud Build to build container images and update Kubernetes manifests from feature-branch commits. Use Config Sync to deploy the images for testing in dynamically created namespaces within the autoscaling Dev cluster. Delete the namespaces after testing.**

**Exam Reasoning Explanation**

C most explicitly combines **feature-branch testing** , **separate test environments** , and **shared infrastructure**. Dedicated namespaces reduce deployment collisions while avoiding a separate cluster for every branch. 

**Key Exam Clues**

  * **Root cause:** Concurrent feature deployments interfere with one another.

  * **Testing requirement:** Developers need stable, independent feature environments.

  * **Cost preference:** Reuse the existing Dev cluster.

  * **Lifecycle requirement:** Remove temporary resources after testing.

**Why This Is Correct**

Configure Cloud Build triggers for feature-branch pushes. Give each feature branch a distinct namespace, and update its manifests with the appropriate images. Config Sync supports namespace-scoped configurations sourced from specified Git branches or revisions. 

Within each environment, use known versions of required dependencies and namespace-specific service endpoints. Apply resource quotas, RBAC, and network policies to reduce resource contention and unintended interactions. Clean up the environment through its GitOps configuration after testing. 

**Why the Other Options Are Not the Best Fit**

  * **A — Technically Possible but Ambiguous:** Its namespace approach is appropriate, but “main-branch merge requests” does not clearly specify the intended feature-branch workflow. Importantly, pre-merge pull-request triggers can also test feature-branch commits, so this wording can overlap with C. 

  * **B — Different Use Case:** This describes promotion through shared environments. It does not establish separate environments for concurrent feature branches, leaving the stated Dev deployment conflicts unresolved.

  * **D — Technically Possible but Not Best:** Separate clusters provide stronger separation, but introduce more provisioning and management overhead. Shared-cluster multi-tenancy reduces resource fragmentation and avoids waiting for new clusters. 

**Exam Trap**

A namespace alone does not guarantee stable dependencies or complete isolation. Dependency versions, service routing, shared test data, resource quotas, and policies must also be scoped appropriately.

For an unambiguous question, A should explicitly distinguish mainline integration from pre-merge feature testing.

**Foundation Concept**

Cloud Build builds images and executes tests. Config Sync reconciles declared Kubernetes configuration. Namespaces provide separate scopes for feature workloads within shared infrastructure.

**Real-World Connection**

A checkout feature can run in `feature-checkout-123` with known versions of its inventory and payment dependencies. Another team’s deployment updates its own namespace without replacing those dependencies.

**Memory Hook**

For economical feature testing, give each branch its own namespace before giving it its own cluster.

**30-Second Exam Takeaway**

Choose **C** as the clearest intended answer: feature-branch triggers, temporary namespaces, stable dependencies, and cleanup. A’s merge-request wording should be clarified because pre-merge testing can implement the same pattern.

**Official References**

  * [**Isolate your workloads using namespaces**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/isolate-workloads-dedicated-namespaces)  
Supports: Reducing naming collisions and applying namespace-scoped quotas, access controls, and network policies.

  * [**Configure syncing from more than one source of truth**](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories)  
Supports: Namespace-scoped configuration and Git branch or revision selection.

  * [**Cluster multi-tenancy**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multitenancy-overview)  
Supports: Shared-cluster isolation, reduced management overhead, and reduced resource fragmentation.

  * [**Create and manage build triggers**](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers)  
Supports: Branch-push and pull-request triggers, including the ambiguity in option A.

</details>

---

### Exam 4 · Q12

Your organization is beginning to containerize its workloads on Google Cloud. You need a fully managed storage solution capable of holding both container images and Helm charts, and it must integrate natively with the Google Cloud services you already rely on — Google Kubernetes Engine (GKE), Cloud Run, VPC Service Controls, and Identity and Access Management (IAM). What should you do?

- A. Configure Docker’s registry storage driver to use a Cloud Storage bucket owned by your organization as the backing store.
- B. Deploy an open source container registry server inside GKE, locked down with a restrictive role-based access control (RBAC) configuration.
- C. Configure Artifact Registry as an OCI-based registry that stores both container images and Helm charts.
- D. Configure Container Registry as an OCI-based registry for container images.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Configure Artifact Registry as an OCI-based registry that stores both container images and Helm charts.

**Correct Answer**

**C. Configure Artifact Registry as an OCI-based registry that stores both container images and Helm charts.**

**Exam Reasoning Explanation**

Three constraints must all be satisfied: the solution has to be fully managed, it has to store both container images and Helm charts, and it has to integrate natively with GKE, Cloud Run, VPC Service Controls, and IAM specifically. Artifact Registry is Google’s fully managed artifact storage service; because it supports the OCI format, a single Docker-format repository can hold both container images and Helm charts, and as a first-party Google Cloud service it is already wired into GKE, Cloud Run, VPC Service Controls, and IAM. The Cloud Storage-backed Docker driver (A) and the self-run open source registry (B) both fail the “fully managed, natively integrated” requirement since they’re assembled or operated by the team itself. Container Registry (D) never supported Helm charts and has been deprecated in favor of Artifact Registry, so it fails the dual-artifact requirement outright.

**Key Exam Clues**

  * “fully managed storage solution” — hard constraint eliminating any option that requires operating or assembling the registry infrastructure yourself

  * “container images and Helm charts” — hard constraint requiring one solution to handle both artifact types, which only an OCI-capable registry provides

  * “native integration into ... GKE, Cloud Run, VPC Service Controls, and ... IAM” — hard constraint pointing to a first-party Google Cloud service rather than a self-hosted or storage-bucket-backed workaround

  * “starting to containerize” — signals the forward-looking, currently recommended choice rather than a legacy service

**Why This Is Correct**

Artifact Registry is Google Cloud’s fully managed artifact storage service. Its Docker-format repositories are OCI-compliant, and because Helm 3.8+ can push and pull charts as OCI artifacts, the same repository type that holds container images can also hold Helm charts — no separate chart-hosting system is needed. As a first-party service, Artifact Registry integrates natively with GKE and Cloud Run for pulling images and charts, with IAM for repository-level access control, and with VPC Service Controls for perimeter protection, covering every integration point the scenario names.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement:** Pointing a Docker storage driver at a Cloud Storage bucket builds a registry backing store out of general-purpose object storage rather than using a purpose-built, managed registry service. It provides none of Artifact Registry’s native IAM repository permissions, VPC Service Controls perimeter support, or Helm chart handling, and leaves the team responsible for assembling and maintaining the registry layer itself.

**Option B — Violates Requirement:** Running an open source container registry server inside GKE, however tightly locked down with RBAC, is a self-operated solution — the organization owns its availability, upgrades, and security, which fails the “fully managed” requirement outright. It also has no built-in integration with VPC Service Controls or Cloud Run, since it isn’t a first-party Google Cloud service.

**Option D — Violates Requirement:** Container Registry only ever stored container images; it never supported Helm charts, so it fails the dual-artifact requirement regardless of its other characteristics. It is also Google’s legacy registry service, deprecated and fully superseded by Artifact Registry, making it the wrong choice for an organization just starting to containerize.

**Exam Trap**

The trap is anchoring on the familiar name “Container Registry” because the scenario mentions container images, while overlooking that the requirement explicitly includes Helm charts — an artifact type Container Registry was never built to store. A second trap is treating any registry-shaped setup (a Cloud Storage-backed Docker driver, or a self-hosted open source registry) as equivalent to a managed service once it technically stores images; “fully managed” and “native integration” are there specifically to rule out anything you’d have to operate, patch, or wire up to IAM and VPC Service Controls yourself.

**Foundation Concept**

The Open Container Initiative (OCI) format standardizes how registries store artifacts, which is why a single OCI-compliant Docker-format repository can hold both container images and Helm charts (pushed and pulled using Helm 3.8+’s native OCI support) rather than needing a separate chart repository. A fully managed, first-party registry service built on this standard — rather than a bucket repurposed as a registry, or a self-run open source registry — is what gives you integration with a cloud provider’s IAM, network security, and compute services without extra engineering effort.

**Real-World Connection**

A platform team standardizing on Artifact Registry stores both its application container images and its internal Helm charts in the same repository type, grants developers push access through IAM roles scoped to individual repositories, and places the registry inside a VPC Service Controls perimeter to prevent exfiltration — all without operating any registry infrastructure themselves. When GKE or Cloud Run deploys a workload, it pulls images and charts directly from Artifact Registry using the same IAM identity and network controls already governing the rest of the environment.

**Memory Hook**

Images plus Helm charts, fully managed, native GKE/Cloud Run/IAM/VPC-SC integration → Artifact Registry; Container Registry never did Helm charts and has been retired.

**30-Second Exam Takeaway**

When a scenario asks for a managed Google Cloud artifact store that must hold both container images and Helm charts, look for OCI-based Artifact Registry — Container Registry is images-only and deprecated, and anything self-hosted or storage-bucket-backed fails the “fully managed, natively integrated” requirement regardless of what it can technically store.

**Official References**

[**Google Cloud — Artifact Registry overview:**](https://docs.cloud.google.com/artifact-registry/docs/overview) Supports: Artifact Registry’s fully managed nature and its native integration with IAM and VPC Service Controls

[**Google Cloud — Transition from Container Registry:**](https://docs.cloud.google.com/artifact-registry/docs/transition-from-gcr) Supports: Container Registry’s deprecation and its lack of support for non-container artifacts, versus Artifact Registry’s expanded, fully managed support for both container images and formats like Helm charts

</details>

---

### Exam 4 · Q17

You are investigating a failed deployment in your CI/CD pipeline. Deployment logs show that the application container could not start because a required environment variable was missing.

You need to identify the configuration error and add a safeguard to the CI/CD workflow to prevent similar failures. What should you do?

- A. Adopt a canary deployment strategy.
- B. Add static code analysis to the CI pipeline.
- C. Add integration tests to the CI pipeline.
- D. Enable Cloud Audit Logs for deployment operations.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Add integration tests to the CI pipeline.

**Correct Answer**

**C. Add integration tests to the CI pipeline.**

**Exam Reasoning Explanation**

The failure occurs when the application starts with its runtime configuration. An integration test that launches the container and validates startup can reproduce this problem before deployment. Google’s SRE guidance specifically recommends integration testing configuration files. 

**Key Exam Clues**

  * **Failure stage:** The container fails during startup.

  * **Root-cause signal:** A required environment variable is missing.

  * **Prevention requirement:** Add validation to the CI/CD workflow.

**Why This Is Correct**

First, trace the missing variable through the deployment configuration and pipeline’s variable mappings, then correct the omission.

Add an integration test that starts the built container with representative deployment configuration and verifies that it becomes ready and handles a basic request. Make successful testing a prerequisite for deployment. Cloud Build supports integration tests as pipeline steps. 

**Why the Other Options Are Not the Best Fit**

  * **A — Different Use Case:** Canary deployments limit exposure to a faulty release and support validation during rollout. They do not, by themselves, detect missing configuration before deployment or correct its source. 

  * **B — Technically Possible but Not Best:** Static checks can catch some configuration mistakes. However, executing the application with its configuration more directly tests the startup behavior that failed here. 

  * **D — Different Use Case:** Audit logs help establish who performed deployment or configuration operations. They do not validate that the application can start or prevent deployment of incomplete configuration. 

**Exam Trap**

Integration tests must cover the relevant configuration. A test that supplies a hardcoded variable can pass even when the deployment template omits that variable. 

**Foundation Concept**

Integration testing checks whether assembled application components work together. For this scenario, that includes the container, its configuration, and its required dependencies.

**Real-World Connection**

For example, if the missing variable is `DATABASE_URL`, correct its deployment mapping and add a startup test using configuration generated from the deployment templates. An omitted mapping should then fail the pipeline before release.

**Memory Hook**

A runtime configuration failure needs a test that runs the application with its configuration.

**30-Second Exam Takeaway**

Choose **C**. Correct the missing configuration and add a startup-focused integration test that blocks deployment when it fails.

**Official References**

  * [**Testing for Reliability — Google SRE**](https://sre.google/sre-book/testing-reliability/)  
Supports: Integration testing, configuration testing, and blocking releases when tests detect failures.

  * [**Overview of Cloud Build**](https://docs.cloud.google.com/build/docs/overview)  
Supports: Running integration tests and static analysis as build steps.

  * [**Use a deployment strategy**](https://docs.cloud.google.com/deploy/docs/deployment-strategies)  
Supports: Canary deployments as a method for reducing rollout risk.

  * [**Cloud Audit Logs overview**](https://docs.cloud.google.com/logging/docs/audit)  
Supports: Audit logs recording administrative operations and caller identities.

</details>

---

### Exam 4 · Q21

You are choosing a deployment approach for your applications on Google Cloud, and as part of that planning you want to gather performance metrics for new application versions using live traffic. The new versions need to be tested against the full production load before they are actually launched. What should you do?

- A. Combine A/B testing with a blue/green deployment.
- B. Combine canary testing with continuous deployment.
- C. Combine canary testing with a rolling updates deployment.
- D. Combine shadow testing with continuous deployment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Combine shadow testing with continuous deployment.

**Correct Answer**

**D. Combine shadow testing with continuous deployment.**

**Exam Reasoning Explanation**

Three constraints must all be satisfied: use live production traffic to gather performance metrics, test against the full production load, and do this before the new version is actually launched. A/B testing (A) and canary testing (B, C) both route real user requests directly to the new version, meaning real users are actually served by it — that’s a form of launch, and canary specifically limits traffic to a fraction, not the full load. Shadow testing (D) mirrors the complete incoming request stream to the new version in parallel with the current version, but only returns the current version’s responses to users — the new version processes the full real traffic volume and pattern without ever being responsible for what a user actually sees, satisfying “full production load” and “before launched” simultaneously. Pairing it with continuous deployment keeps this evaluation a repeatable, automated pipeline step.

**Key Exam Clues**

  * “use live traffic to gather performance metrics” — rules out synthetic load in a staging environment, points toward a technique operating on real production requests

  * “test against the full production load” — a hard constraint eliminating any technique that only exposes the new version to a fraction of traffic (canary) or splits users between versions (A/B)

  * “before your applications are launched” — a hard constraint eliminating any technique where real users are actually served responses from the new version, since that is itself a form of launch

  * “deployment technique” paired with a strategy — signals a combination of a testing technique with a deployment mechanism, matching every option’s paired structure

**Why This Is Correct**

Shadow testing duplicates the full stream of live production requests and sends a copy to the new version at the same time the current version handles the real request, but only the current version’s response is ever returned to the user. The new version is exercised by the complete, real-world volume and pattern of production traffic — exactly what’s needed for meaningful performance metrics — while remaining entirely invisible to users, meaning it has not actually been launched. Running this as part of continuous deployment lets the team evaluate every new version this way automatically and repeatedly, rather than as a manual, one-time test.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement:** A/B testing routes real users to the new version based on some condition, meaning those users are actually served by it — a form of launch to part of the audience, contradicting testing “before” launch. Blue/green’s typical instantaneous full-traffic cutover also doesn’t provide the gradual or mirrored evaluation the scenario implies.

**Option B — Violates Requirement:** Canary testing intentionally limits the new version’s exposure to a small percentage of live traffic to contain risk, so it’s never tested against the full production load — only a deliberately reduced subset. It also serves real responses to the users whose traffic lands on the canary, meaning the new version has effectively been launched to them.

**Option C — Violates Requirement:** This shares Option B’s core issues — only a portion of traffic reaches the new version, so it isn’t validated against the full load, and the users on that portion are actually served by it, meaning it isn’t tested purely “before” launch. Pairing canary with rolling updates doesn’t change canary’s fundamental traffic-splitting behavior.

**Exam Trap**

The trap is treating “canary” as the default answer whenever a question mentions testing new versions with real traffic, since canary is the most commonly discussed technique for this general idea. But canary and A/B testing both expose some real users to the new version, and canary specifically limits traffic volume rather than using the full load — two details this scenario’s wording (“full production load,” “before... launched”) is specifically designed to rule out. Shadow testing is the less commonly reached-for option that actually satisfies both constraints.

**Foundation Concept**

Deployment and release-testing techniques differ along two independent dimensions: how much of the real traffic volume reaches the new version, and whether the new version’s output is ever actually shown to real users. Canary and A/B testing both expose a portion of real users to real responses from the new version. Shadow testing is distinct because it decouples traffic volume from user exposure entirely: the new version can see 100% of the traffic pattern without ever being responsible for a single response a user actually sees.

**Real-World Connection**

A team preparing to replace a core backend service mirrors all production requests to the new version for several days using traffic mirroring on their load balancer, comparing its latency, error rates, and resource usage against the current version under the exact same real-world load — all while users continue to be served exclusively by the existing version. Only after confirming the new version performs acceptably under full production conditions do they begin a separate, gradual rollout to actually expose users to it.

**Memory Hook**

Full production load, zero user exposure, before launch → shadow testing; canary and A/B both actually serve some real users, so neither is “before launch.”

**30-Second Exam Takeaway**

When a scenario wants a new version validated against the complete, real production traffic pattern without any real user ever seeing its response, that’s shadow testing (traffic mirroring) — canary and A/B testing both involve serving at least some real users, and canary specifically limits traffic volume rather than using the full load.

**Official References**

[**Google Cloud — Set up traffic management for global external Application Load Balancers:**](https://cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt) Supports: the traffic-mirroring mechanism underlying shadow testing, described as sending an identical request to a mirror backend without client-facing impact, “useful for testing a new version of a backend service”

[Google Cloud — Cloud Deploy deployment strategies: ](https://cloud.google.com/deploy/docs/deployment-strategies)Supports: canary deployment being a progressive rollout to a portion of infrastructure/traffic rather than the full production load, contrasting with shadow testing’s full-traffic, no-user-exposure approach

</details>

---

### Exam 4 · Q24

You have a Cloud Build job configured to deploy Terraform code whenever a Git branch is updated. During testing, the job fails, and the build logs show the following error:

Initializing the backend...

Error: Failed to get existing workspaces: querying Cloud Storage failed: googleapi: Error 403

You need to resolve this by following Google-recommended practices. What should you do?

- A. Update the Terraform configuration to use local state instead of a remote backend.
- B. Create a Cloud Storage bucket matching the name referenced in the Terraform configuration.
- C. Grant the Cloud Build service account the roles/owner Identity and Access Management (IAM) role on the project.
- D. Grant the Cloud Build service account the roles/storage.objectAdmin Identity and Access Management (IAM) role, scoped to just the state file’s storage bucket.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Grant the Cloud Build service account the roles/storage.objectAdmin Identity and Access Management (IAM) role, scoped to just the state file’s storage bucket.

**Correct Answer**

**D. Grant the Cloud Build service account the roles/storage.objectAdmin Identity and Access Management (IAM) role, scoped to just the state file’s storage bucket.**

**Exam Reasoning Explanation**

The fix must resolve a 403 permission error encountered while Terraform’s GCS backend queries the state bucket, and it must follow Google-recommended, least-privilege practice. The error text — “querying Cloud Storage failed: googleapi: Error 403” — is specifically an authorization failure, not a not-found error, which rules out Option B; creating the bucket addresses a missing-resource scenario, not a permissions one. Option A sidesteps the problem rather than fixing it, and abandoning a shared remote backend for local state contradicts recommended CI/CD practice for team-shared infrastructure as code. Option C would technically resolve the 403 by granting the Cloud Build service account unrestricted project-wide permissions, but this is explicitly against the least-privilege principle Google recommends for automated pipeline service accounts. Option D grants exactly the permissions Terraform’s GCS backend needs — reading, listing, and writing objects — scoped to only the specific bucket holding the state file, resolving the 403 while following least-privilege practice.

**Key Exam Clues**

  * “Error 403” paired with “querying Cloud Storage” — specifically identifies an authorization failure against the GCS backend, not a missing-resource (404) condition

  * “following Google-recommended practices” — a hard constraint ruling out any fix that technically works but over-grants permissions, such as a broad project-level Owner grant

  * “Cloud Build job that deploys Terraform code” — identifies the Cloud Build service account as the identity whose permissions need examining, since that’s the principal executing terraform init

  * “Initializing the backend...” — pinpoints the failure to the backend initialization step, where Terraform first needs to list and read objects in the configured state bucket

**Why This Is Correct**

Terraform’s Google Cloud Storage backend needs to list and read objects in the configured bucket during terraform init to check for existing state, and a 403 at this exact step means the identity running Terraform — the Cloud Build service account — lacks sufficient permissions on that bucket. The roles/storage.objectAdmin role grants the read, write, and list permissions Terraform’s GCS backend needs to manage state objects, and granting it specifically on the state file’s bucket, rather than at the project level, gives Cloud Build exactly the access required without extending broader privileges, matching Google’s recommended least-privilege approach for pipeline service accounts.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement:** Switching to local state avoids the permission error rather than fixing it, and abandons the shared, lockable remote state a team-oriented CI/CD pipeline depends on — contradicting recommended Terraform practice for collaborative infrastructure management generally, not just this one error.

**Option B — Incorrect:** A 403 error means the caller was denied access to a resource it could reach, not that the resource doesn’t exist; a genuinely missing bucket would produce a different, not-found-style error. Creating a new bucket doesn’t address a permissions problem and risks creating confusion or duplicate infrastructure if the intended bucket already exists.

**Option C — Technically Possible but Not Best:** Granting roles/owner at the project level would resolve the 403, since Owner includes every needed Cloud Storage permission, but it also hands the Cloud Build service account unrestricted control over the entire project — a significant over-grant for a pipeline that only needs to read and write objects in one specific bucket, and a clear violation of least-privilege best practice.

**Exam Trap**

The trap is picking the option that would “work” (C) without checking whether it follows the recommended practice the question explicitly asks for — a broad Owner grant does fix the symptom, but the real test is recognizing that scoped, least-privilege access is the Google-recommended way to fix it. A second trap is misreading “403” as if it could mean the resource is missing, which would make creating a bucket (B) seem plausible; distinguishing authorization failures from not-found errors is the key diagnostic skill being tested.

**Foundation Concept**

When a service account hits an authorization error against a specific resource, the Google-recommended remediation is to grant that service account the narrowest IAM role that covers the required permissions, scoped to the smallest resource that makes sense — here, the individual bucket rather than the project — rather than reaching for a broad, predefined role like Owner that happens to include the needed permissions along with many others the task doesn’t require.

**Real-World Connection**

A platform team running Terraform through Cloud Build grants the Cloud Build service account roles/storage.objectAdmin on only the bucket holding their Terraform state, rather than broader project-level access. When a new pipeline later needs similar access for a different state bucket, the precedent of scoping grants to individual buckets makes it easy to extend the same least-privilege pattern, keeping the blast radius of any single service account’s compromise or misconfiguration limited to the specific state files it’s actually responsible for.

**Memory Hook**

403 on the state bucket during backend init → grant roles/storage.objectAdmin on that bucket specifically, not roles/owner on the whole project and not a workaround like local state.

**30-Second Exam Takeaway**

When a Cloud Build/Terraform pipeline fails with a 403 while querying its GCS state bucket, the Google-recommended fix is a least-privilege IAM grant scoped to that bucket — never a project-wide role like Owner, and never abandoning the remote backend to dodge the error.

**Official References**

[Google Cloud — Store Terraform state in a Cloud Storage bucket: ](https://docs.cloud.google.com/docs/terraform/resource-management/store-state)Supports: the object-level permissions Terraform’s GCS backend requires, and the recommendation to control access to the state bucket

[**Google Cloud — Terraform security best practices:**](https://docs.cloud.google.com/docs/terraform/best-practices/security) Supports: applying least-privilege IAM principles to service accounts used for Terraform automation, rather than broad roles like Owner

</details>

---

### Exam 4 · Q28

You are deploying an application to Cloud Run that needs a password to start up. Your organization mandates that every password be rotated every 24 hours, and the application must always be working with the current password. You need to achieve this without any downtime. What should you do?

- A. Store the password in Secret Manager and expose it to the application as an environment variable.
- B. Store the password in Secret Manager and mount it as a volume inside the application’s container.
- C. Have Cloud Build bake the password into the application container image at build time, and make sure Artifact Registry is locked down from public access.
- D. Hard-code the password directly in the application’s source code, and use Cloud Build to rebuild and redeploy the application whenever the password changes.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Store the password in Secret Manager and mount it as a volume inside the application’s container.

**Correct Answer**

**B. Store the password in Secret Manager and mount it as a volume inside the application’s container.**

**Exam Reasoning Explanation**

Three things must hold: the application must always have the current, 24-hour-rotated password, there must be no downtime, and the approach should follow sound secrets-handling practice. Options C and D both bake the password into something static — a container image or the source code itself — meaning every rotation requires a full rebuild-and-redeploy cycle, and D additionally hardcodes a secret in source control, a serious anti-pattern on its own. Option A exposes the secret as an environment variable, which Cloud Run resolves only once, at instance startup; already-running instances keep serving the old password until replaced by a new deployment. Option B mounts the secret as a volume, and Cloud Run reads volume-mounted secrets directly from Secret Manager on each access rather than caching them at startup, so when the secret rotates, currently running instances pick up the new value the next time they read the file — no redeploy, no downtime.

**Key Exam Clues**

  * “your application must have the latest password” — a hard constraint ruling out any mechanism resolved only once at startup, since that leaves running instances holding a stale value after rotation

  * “rotated every 24 hours” — establishes rotation as a recurring, ongoing event the solution must handle automatically

  * “deploy the application with no downtime” — rules out any approach requiring a rebuild-and-redeploy cycle every time the password changes, reintroducing deployment risk every 24 hours

  * “requires a password to start” paired with secret rotation — points toward Cloud Run’s two secret-delivery mechanisms (environment variable vs. volume) as the real decision point

**Why This Is Correct**

Cloud Run reads a volume-mounted secret directly from Secret Manager each time it’s accessed, rather than resolving it once when the instance starts, which is why this method is documented as working well with secret rotation. When the password rotates in Secret Manager, the application’s already-running Cloud Run instances read the new value the next time they access the mounted file — no new revision, no redeploy, no downtime — satisfying both “latest password” and “no downtime” at once.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement:** Cloud Run resolves environment-variable secrets once, at instance startup, and Google explicitly recommends pinning environment-variable secrets to a specific version rather than “latest” for exactly this reason. After a rotation, already-running instances keep the old password until replaced by a new deployment — an additional step the scenario doesn’t call for.

**Option C — Violates Requirement:** Baking the password into the container image at build time makes it a fixed part of that image; picking up a rotated password requires rebuilding and redeploying the container every 24 hours. It also embeds a secret directly in a container image, a weaker practice than referencing it from Secret Manager at runtime, regardless of how well Artifact Registry access is restricted.

**Option D — Violates Requirement:** Hardcoding the password in source code is a severe security anti-pattern on its own — exposed in version control history to anyone with repository access — and compounds the redeployment problem, since every rotation requires a code change, rebuild, and redeploy.

**Exam Trap**

The trap is treating “store the password in Secret Manager” as the whole answer and overlooking that Cloud Run offers two delivery mechanisms with meaningfully different rotation behavior — an environment variable looks like the simpler, more familiar choice, but it’s resolved only at startup and won’t reflect a rotated secret in already-running instances. The decisive detail is “must have the latest password” combined with a 24-hour rotation cadence, which specifically favors the mechanism Cloud Run reads live rather than the one resolved once at startup.

**Foundation Concept**

Cloud Run offers two ways to deliver a Secret Manager secret to a container: as an environment variable, resolved once when the instance starts and fixed for that instance’s lifetime, or as a mounted volume, read directly from Secret Manager on each access. A secret that rotates on a recurring schedule needs the volume-mount approach so running instances stay current without requiring a new deployment every time the value changes.

**Real-World Connection**

A team running a Cloud Run service against a database that rotates its credentials daily mounts the database password as a Secret Manager volume rather than an environment variable, and configures the application to read the password file on each connection attempt rather than caching it once at startup. When the credential rotates at midnight, every running instance seamlessly picks up the new password on its next database connection, with no coordinated redeploy and no window where the service is unavailable or authenticating with an outdated credential.

**Memory Hook**

Secret rotates, app must always have the latest value, no downtime → mount as a Secret Manager volume (read live on each access); environment variables are resolved once at startup and go stale after rotation.

**30-Second Exam Takeaway**

When a Cloud Run application needs a Secret Manager value that rotates and must always reflect the current version without redeploying, mount the secret as a volume rather than exposing it as an environment variable — volumes are read live from Secret Manager on each access, while environment variables are fixed for the life of the instance.

**Official References**

[**Google Cloud — Configure secrets for services (Cloud Run):**](https://cloud.google.com/run/docs/configuring/secrets) Supports: volume-mounted secrets reading live from Secret Manager (“works well with secret rotation”) versus environment-variable secrets being resolved only once, at instance startup

</details>

---

### Exam 4 · Q30

You are building a CI/CD pipeline natively on Google Cloud, and you want every build deployed to a pre-production Google Kubernetes Engine (GKE) environment to be automatically load-tested before it can be promoted to production. Only builds that pass this test should ever reach production, and you want to follow Google-recommended practices for doing this with Binary Authorization. How should you configure the pipeline?

- A. Have the lead quality assurance engineer manually sign the attestation for each passing build, using their own personal private key.
- B. Have the pipeline sign the attestation for each passing build with a private key stored in Cloud Key Management Service (Cloud KMS), authenticating with a service account JSON key stored as a Kubernetes Secret.
- C. Have the pipeline sign the attestation for each passing build with a private key stored in Cloud Key Management Service (Cloud KMS), authenticating through Workload Identity.
- D. Have the lead quality assurance engineer manually sign the attestation for each passing build, using a key stored in Cloud Key Management Service (Cloud KMS).

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Have the pipeline sign the attestation for each passing build with a private key stored in Cloud Key Management Service (Cloud KMS), authenticating through Workload Identity.

**Correct Answer**

**C. Have the pipeline sign the attestation for each passing build with a private key stored in Cloud Key Management Service (Cloud KMS), authenticating through Workload Identity.**

**Exam Reasoning Explanation**

Two things must both hold: the attestation must be created automatically once a build passes the load test, with no manual human gate for every build, and the signing key and its authentication method must follow Google-recommended security practices. Options A and D both require the lead QA engineer to personally sign every attestation, turning an automated pipeline step into a manual approval bottleneck — contradicting the premise that builds are automatically tested and promoted based on that result. A additionally uses a personal private key rather than any centrally managed key, compounding the problem. Option B keeps the signing key in Cloud KMS correctly, but authenticates to it with an exported service account JSON key stored as a Kubernetes Secret — a long-lived credential Google explicitly recommends avoiding when a keyless alternative exists. Option C uses Cloud KMS for the signing key and Workload Identity for authentication, letting the pipeline’s identity securely assume a Google Cloud service account without exported key material, fully automating attestation creation while following Google’s recommended practices.

**Key Exam Clues**

  * “automatically load-tested before being promoted” — establishes that the gate is based on an automated test result, which should flow directly into an automated attestation step rather than requiring human sign-off

  * “only builds that have passed this test are deployed to production” — frames the attestation as the automated proof that gates promotion, not a separate manual approval layered on top

  * “personal private key” versus “a key stored in Cloud Key Management Service” — a direct signal distinguishing an anti-pattern key-management choice from a properly centralized one

  * “service account JSON key stored as a Kubernetes Secret” versus “authenticated through Workload Identity” — the precise detail distinguishing the two Cloud-KMS-based options, determining which follows Google’s recommended keyless authentication practice

**Why This Is Correct**

A fully automated Binary Authorization pipeline has the CI/CD system itself create and sign the attestation as soon as a build passes its load test, using a signing key securely held in Cloud KMS rather than a locally managed or personal key. For a pipeline component running in GKE to authenticate to Cloud KMS and use that key, Workload Identity lets it assume a Google Cloud service account’s permissions without ever exporting or storing a long-lived JSON key — the Google-recommended way to grant Google Cloud API access to GKE-based workloads. Cloud KMS for the key plus Workload Identity for authentication keeps the entire attestation step automated and keyless.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement:** Requiring the lead QA engineer to manually sign every attestation turns an automated gate into a human bottleneck. Signing with a personal private key compounds the problem, since personal keys aren’t centrally managed, rotated, or revocable the way a Cloud KMS key is.

**Option B — Technically Possible but Not Best:** Storing the signing key in Cloud KMS is correct, but authenticating to it with an exported service account JSON key stored as a Kubernetes Secret introduces a long-lived credential that must be stored, rotated, and protected manually — exactly the risk Workload Identity is designed to eliminate when it’s available, as it is here.

**Option D — Violates Requirement:** Moving the signing key into Cloud KMS improves on Option A, but the attestation still depends on the lead QA engineer manually signing every passing build, keeping a human approval step in what should be a fully automated promotion gate driven by the load test’s result.

**Exam Trap**

The trap is treating “the key is now in Cloud KMS” as sufficient to make an option correct, without separately checking whether the attestation process is actually automated and whether the authentication method avoids exported credentials. Option D shows this clearly — a properly managed key paired with a manual human signer is still wrong, because the automation requirement is just as binding as the key-management requirement, and both must be satisfied together.

**Foundation Concept**

An automated Binary Authorization pipeline needs two things working together: a securely managed signing key, typically held in Cloud KMS rather than with any individual or embedded in long-lived files, and a way for the pipeline’s own identity to authenticate to that key without relying on exported credentials. Workload Identity is the mechanism that lets a workload running in GKE securely assume a Google Cloud service account’s permissions for exactly this purpose, completing the fully automated, keyless chain from “test passed” to “attestation created” to “deployment permitted.”

**Real-World Connection**

A platform team wires their CI/CD pipeline so that, immediately after a build passes its automated load test in the pre-production GKE cluster, a pipeline step running under Workload Identity signs an attestation using a Cloud KMS key, and Binary Authorization’s production policy only admits images carrying that attestation. No person reviews individual builds, no service account key ever needs to be generated or rotated, and a bad build simply never accumulates the attestation it needs to reach production.

**Memory Hook**

Automated gate + Google-recommended key practice → Cloud KMS for the signing key, Workload Identity for authentication; a human signer (personal key or not) breaks automation, and a service account JSON key breaks the keyless-authentication practice.

**30-Second Exam Takeaway**

When a Binary Authorization question asks how to attest builds automatically based on a passed test, look for the option pairing a centrally managed key (Cloud KMS) with keyless authentication (Workload Identity) — eliminate anything that inserts a manual human signer, and eliminate anything that authenticates with an exported service account key when Workload Identity is available.

**Official References**

[**Google Cloud — Create attestations (Binary Authorization):**](https://docs.cloud.google.com/binary-authorization/docs/making-attestations) Supports: Cloud KMS as the recommended store for the attestation signing key, used by an automated pipeline step rather than a manual signer

[Google Cloud — About Workload Identity Federation for GKE: ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity)Supports: Workload Identity Federation being the recommended way for GKE workloads to authenticate to Google Cloud services, in place of service account keys stored as Kubernetes Secrets

</details>

---

### Exam 4 · Q32

You are developing reusable infrastructure as code modules. Each module includes integration tests that launch the module in a test project, and your source control is GitHub. You need to test your feature branches continuously and make sure all code is tested before any change is accepted. You need to automate the integration tests. What should you do?

- A. Use a Jenkins server for your CI/CD pipelines, and run all of the tests on the feature branch on a periodic schedule.
- B. Have the pull request reviewers run the integration tests before they approve the code.
- C. Use Cloud Build to run the tests, and trigger the full set of tests after a pull request has been merged.
- D. Use Cloud Build to run the tests in a specific folder, and trigger a Cloud Build run for every GitHub pull request.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Use Cloud Build to run the tests in a specific folder, and trigger a Cloud Build run for every GitHub pull request.

**Correct Answer**

**D. Use Cloud Build to run the tests in a specific folder, and trigger a Cloud Build run for every GitHub pull request.**

**Exam Reasoning Explanation**

Three requirements must hold together. The tests must run automatically, each change must be tested continuously as it is proposed, and the tests must complete before a change is accepted. That makes the pull request the right point to run them, because it sits between the feature branch and the code being accepted. Option D ties an automated Cloud Build run to every pull request, so no change reaches review untested. The other options fail one requirement each: they run on a schedule, depend on a person, or run only after the change has already been accepted.

**Key Exam Clues**

  * “automate the integration tests” is a hard constraint that rules out any option relying on people to run them

  * “continuously test your feature branch” is a hard constraint that rules out scheduled or occasional runs

  * “ensure that all code is tested before changes are accepted” is a hard constraint on timing: the tests must be a gate before merge, not a check afterward

  * “Each module contains integration tests” is a technical signal that tests are organized per module, which suits tests scoped to a specific folder

  * “You are using GitHub for source control” is a technical signal that pull request events can start the pipeline

**Why This Is Correct**

Cloud Build triggers can start a build in response to events on a GitHub repository, including commits to a pull request. A pull request trigger therefore runs the integration tests automatically whenever a change is proposed or updated, and the build result is shown on the pull request so reviewers see it before approving. Because each module keeps its tests in its own folder, the build can run the tests in that folder. A trigger can also be limited with an included-files filter so it starts only when matching files change, which keeps runs focused on the affected module. One prerequisite applies: any shared files that modules depend on must also be covered by the filters, or a change to them could skip the tests it affects.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement:** Running tests on a schedule is not continuous testing of every change, so a change could be reviewed or merged between runs without having been tested. It also means operating and maintaining a Jenkins server when the scenario is already built around GitHub and Google Cloud, which adds management effort without meeting the requirement.

**Option B — Violates Requirement:** Asking reviewers to run the tests by hand is not automation. It also depends on every reviewer running the full tests every time, so coverage is inconsistent and slow, and it makes a human step part of the gate.

**Option C — Violates Requirement:** Cloud Build is the right tool, but triggering the tests after the pull request is merged means the change has already been accepted when the tests run. A failure then lands on the main branch instead of blocking the change, which defeats the requirement that code be tested before it is accepted.

**Exam Trap**

The trap is option C, because it uses the right service and sounds thorough by running all tests. The failure is timing: a post-merge run reports problems after acceptance and can’t act as a gate. Option A is a second trap, since Jenkins is a legitimate CI server, but the option’s periodic schedule is what breaks it. Post-merge builds are still useful for deploying or running a final regression on the main branch, so the answer would favor a post-merge trigger only if the requirement were about what happens after acceptance.

**Foundation Concept**

Continuous integration gates change by running automated tests against each proposed change before it is merged, with results reported on the pull request, so only passing code reaches the main branch. In a repository that holds several independent modules, scoping tests to the changed module’s folder keeps runs short. That matters here because infrastructure integration tests create real resources in a test project, so they are slower and cost money. Because these builds run code against a real project, Cloud Build’s comment control on pull request triggers is relevant: builds from external contributors can be set to run only after an owner or collaborator comments /gcbrun.

**Real-World Connection**

A team that maintains a repository of Terraform modules creates a Cloud Build trigger for each module folder, set to run on pull requests and filtered to that folder’s files. When an engineer opens a pull request that changes one module, Cloud Build runs that module’s integration tests in the test project and reports the result on the pull request. Reviewers see a passing or failing result before they approve, and broken changes never reach the main branch.

**Memory Hook**

To test every change before it is accepted, trigger Cloud Build on each pull request and scope the build to the folder being changed.

**30-Second Exam Takeaway**

When a question asks how to automatically test changes before they are accepted in GitHub, look for a pull request trigger, not a scheduled job, a manual step, or a post-merge build. Scoping the test run to the changed folder keeps it efficient for repositories that contain several modules.

**Official References**

[**Google Cloud Build — Building repositories from GitHub:**](https://docs.cloud.google.com/build/docs/run-builds-on-github) Supports: triggers that run builds in response to GitHub events such as pull requests, comment control for pull request builds, and build results being reported on GitHub

[**Google Cloud Build — REST Resource: projects.locations.triggers:**](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers) Supports: the pull request event filter on triggers and the includedFiles and ignoredFiles filters that limit a trigger to changes in specific paths

[Google Cloud — Professional Cloud DevOps Engineer Certification exam guide (Section 2.1, designing pipelines: CI/CD pipeline triggers; continuous testing): ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain and objective alignment

</details>

---

### Exam 4 · Q36

Your application runs on Cloud Run. You want to test a new version using live production traffic, and at the same time let the quality assurance (QA) team test it manually. You need to limit the potential impact of any problems found during testing, and you must be able to roll back to a previous version of the application if necessary. How should you deploy the new version? (Choose two.)

- A. Deploy the application as a new, separate Cloud Run service.
- B. Deploy a new Cloud Run revision that has a tag, using the --no-traffic option.
- C. Deploy a new Cloud Run revision that has no tag, using the --no-traffic option.
- D. Deploy the new application version using the --no-traffic option, and route production traffic to the revision’s URL.
- E. Deploy the new application version, and split traffic to the new version.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Deploy a new Cloud Run revision that has a tag, using the --no-traffic option. **|** E. Deploy the new application version, and split traffic to the new version.

**Correct Answer**

**B. Deploy a new Cloud Run revision that has a tag, using the --no-traffic option.**

**E. Deploy the new application version, and split traffic to the new version.**

**Exam Reasoning Explanation**

The scenario has two testing needs that call for two separate mechanisms. QA needs to reach the new version directly and manually, without real users being sent to it, and the live-traffic test needs a controlled share of real users on the new version so that any problem affects only a small portion of them. Deploying a tagged revision with --no-traffic gives QA a dedicated URL for the new revision while production traffic stays on the existing revision (B). Splitting traffic then sends a limited percentage of live requests to the new revision (E). The old revision stays deployed throughout, so rollback is a matter of moving traffic back to it. Options A, C, and D each fail one of the needs. A creates a separate service that production traffic never reaches. C leaves QA without a stable URL for the revision. D sends production traffic to a URL meant for direct testing, which doesn’t work as a traffic-splitting mechanism. B and E work together, with B covering QA’s manual testing and E covering the live-traffic test with limited exposure.

**Key Exam Clues**

  * “while you let the quality assurance team perform manual testing” requires a way to reach the new revision directly, which a revision tag provides through a dedicated URL

  * “use live production traffic to test a new version” requires routing real requests to the new revision, which traffic splitting does

  * “limit the potential impact of any issues” favors sending only a fraction of traffic to the new version rather than all of it

  * “roll back to a previous version” favors keeping the earlier revision deployed within the same service so traffic can be moved back

  * “(Choose two.)” with two distinct needs (QA access and live traffic) signals two complementary actions

**Why This Is Correct**

Cloud Run keeps each deployment as a revision and lets you control which revisions receive traffic. Deploying with --no-traffic creates the new revision without sending any requests to it, and adding a tag gives it a dedicated URL that QA can use to test it directly without serving production traffic. Once the revision looks healthy, traffic splitting lets you direct a small percentage of live traffic to the new revision, with the rest still going to the existing one, so any problem reaches only a limited share of users. Because the previous revision remains deployed, you can roll back by routing all traffic to it.

**Why the Other Options Are Not the Best Fit**

**Option A: Technically Possible but Not Best.** A new service gets its own URL and its own traffic configuration, so production traffic never reaches it unless you add other routing in front of the two services. It also gives up the revision history within one service that makes traffic splitting and rollback simple.

**Option C: Violates Requirement.** Without a tag, the new revision has no dedicated URL, so the QA team has no stable address for testing it directly while it receives no traffic. The revision is deployed but effectively unreachable for manual testing.

**Option D: Violates Requirement.** A revision URL created by a tag is meant for direct testing, not for sending production traffic. Pointing production traffic at it is not traffic splitting, and doing so would not limit the impact in a controlled way. It also leaves the main service URL without a defined split, so it does not provide the gradual exposure the scenario requires.

**Exam Trap**

The trap is picking the options that look safe in isolation. A no-traffic deployment (B, C, D) sounds cautious, but the scenario also requires live production traffic to test the new version, which only traffic splitting supplies. The reverse trap is choosing traffic splitting alone (E) and forgetting that QA needs a direct way to reach the revision, which the tag provides. A third trap is reading “tag” as optional. Without it, the revision has no URL of its own, which is what separates B from C.

**Foundation Concept**

Cloud Run services are made up of revisions. Each deployment creates an immutable revision, and a service’s traffic can be assigned to one or more revisions by percentage. A revision tag creates a dedicated URL that reaches that revision directly, even when it is receiving no production traffic. Combining no-traffic deployment, tags, and percentage-based traffic splitting supports gradual rollouts: validate directly, expose a small share of users, then increase or roll back by changing the traffic assignment.

**Real-World Connection**

A team deploys a new version of its API as a tagged, no-traffic revision and gives the QA team the tagged URL for manual testing. After QA signs off, the team sends 5% of production traffic to the new revision and watches error rates and latency. If metrics look healthy, they raise the share in steps. If something goes wrong, they move all traffic back to the previous revision, which was never removed, and affected users see the problem for only a short time.

**Memory Hook**

Tagged revision with no traffic is for QA, and a traffic split is for live users in limited numbers. The old revision stays deployed, so rollback is just moving traffic back.

**30-Second Exam Takeaway**

For a Cloud Run test that needs both direct manual testing and limited live traffic, choose a tagged --no-traffic revision for the direct-access part and traffic splitting for the live-traffic part. Avoid separate services, untagged revisions, and pointing production traffic at a test URL.

**Official References**

[**Google Cloud: Cloud Run gradual rollouts and rollbacks:**](https://cloud.google.com/blog/products/serverless/cloud-run-now-supports-gradual-rollouts-and-rollbacks) Supports: deploying a new revision with --no-traffic and a tag to test it at a specific URL without serving traffic, then migrating traffic gradually and rolling back to an earlier revision

[**Google Codelabs: Using revisions in Cloud Run for traffic splitting, gradual rollouts, and rollbacks:**](https://codelabs.developers.google.com/codelabs/cloud-run/revisions-cloud-run-traffic-splitting-gradual-rollout-rollbacks) Supports: tagging a revision to test it at a dedicated URL without serving traffic, splitting traffic by percentage, and rolling back to a previous revision

</details>

---

### Exam 4 · Q37

You are investigating problems in a production application that runs on Google Kubernetes Engine (GKE). You’ve traced the problem to a recently updated container image, but you haven’t been able to identify which code change caused it. The deployment currently references the image by its latest tag. You need to get the cluster running a version of the container that works as intended. What should you do?

- A. Create a new tag named stable that points to the previously working container image, and change the deployment to reference that new tag.
- B. Change the deployment to reference the sha256 digest of the previously working container image.
- C. Build a new container image from an earlier Git tag, and perform a rolling update of the deployment to that new image.
- D. Reapply the latest tag to the previous container image, and perform a rolling update of the deployment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Change the deployment to reference the sha256 digest of the previously working container image.

**Correct Answer**

**B. Change the deployment to reference the sha256 digest of the previously working container image.**

**Exam Reasoning Explanation**

Two things must hold. The deployment must run exactly the image that was previously working, since the code change that broke it hasn’t been found and there is nothing to fix forward. The reference the deployment uses must also stay unambiguous, so the rollback does not depend on what a registry label happens to point to at the moment a Pod starts. Tags are mutable pointers, so any tag-based reference, whether a new tag or the old latest tag, can later point at a different image. A digest is a cryptographic hash of the image’s contents and cannot be repointed. Pointing the deployment at the digest of the known-good image restores that exact artifact without a rebuild.

**Key Exam Clues**

  * “recently updated container image” identifies the artifact as the cause, which points toward reverting to the earlier artifact

  * “the exact change in code was not identified” is a constraint that rules out fixing forward, since the faulty change isn’t known

  * “currently pointing to the latest tag” highlights the mutable reference that created the ambiguity

  * “a version of the container that functions as intended” means a previously working image exists and should be reused as-is

**Why This Is Correct**

A container image digest uniquely and immutably identifies a container image. Google’s guidance recommends deploying by digest to avoid the downsides of tags. Tags are mutable, and Google notes that deploying by tag in Kubernetes can lead to unexpected results, because new Pods created from the same Deployment spec can end up using either an old or a new image. Referencing the previously working image by its sha256 digest makes the Deployment spec point at exactly that content, and the update to that spec triggers a rolling update that replaces the faulty Pods. No rebuild is needed because the working image is already in the registry.

**Why the Other Options Are Not the Best Fit**

**Option A, Technically Possible but Not Best.** A new stable tag would work until someone moves it, and it adds a mutable label that must be managed. It also repeats the problem that caused the incident. The deployment depends on a pointer that can change, instead of on the image itself.

**Option C, Technically Possible but Not Best.** Rebuilding from an earlier Git tag does not guarantee the same image as before, since base image or dependency versions may have changed since the original build. It is also slower than reusing the existing known-good image, and it produces a new artifact that has never run in production.

**Option D, Violates Requirement.** Moving the latest tag keeps the mutable-reference problem, and it doesn’t change the Deployment spec because the image string is still “:latest”. Kubernetes starts a rolling update only when the Pod template changes, so the rollout may never start, and nodes that already hold a cached latest image may not pull the retagged one.

**Exam Trap**

The trap is treating a tag as a stable name for an image. Options A and D both rely on tags, and D looks tidy because it keeps the deployment unchanged, but that is exactly why it fails. A second trap is that rebuilding from a Git tag (C) sounds like the standard way to roll back code. Here the working artifact already exists, and a rebuild produces a different artifact even if the source is the same. The answer would change to C only if the previous image had been deleted from the registry, so that a rebuild was the only way to recreate it.

**Foundation Concept**

An image tag is a human-readable, mutable label that can be moved to a different image at any time. An image digest is the hash of the image manifest or image index, and it is a content-addressed, immutable identifier. When a rollback has to restore a specific known-good artifact, a digest reference guarantees that Kubernetes pulls that exact image regardless of any retagging in the registry.

**Real-World Connection**

An on-call engineer finds that an incident began right after a new image was pushed under the latest tag. They look up the digest of the last known-good image from the registry or the Cloud Build history, update the Deployment to reference it by digest, and let the rolling update replace the faulty Pods. The deployment then stays pinned to that content, so a later push to latest can’t alter it, and the team can investigate the code change without time pressure.

**Memory Hook**

Tags can move and digests cannot, so roll back to the known-good image by its digest.

**30-Second Exam Takeaway**

When a question asks how to run a specific known-good container image in Kubernetes, choose the immutable digest reference over any tag, and prefer reusing the existing image over rebuilding it. Be wary of options that move or add tags, because a tag can be repointed.

**Official References**

[**Google Cloud: About container image digests (GKE):**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-container-images) Supports: image digests uniquely and immutably identifying an image, tags being mutable, and the downsides of deploying by tag in Kubernetes, including Pods created from the same Deployment spec ending up with different images

[**Google Cloud: Using container image digests in Kubernetes manifests:**](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/using-container-image-digests-in-kubernetes-manifests) Supports: referencing images by digest in Kubernetes manifests as the recommended way to identify container images

</details>

---

### Exam 4 · Q44

Your company operates in a highly regulated industry, and its security team requires that only trusted container images can be deployed to Google Kubernetes Engine (GKE). You need a solution that meets this requirement while keeping management overhead to a minimum. What should you do?

- A. Configure Binary Authorization on your GKE clusters to enforce deploy-time security policies.
- B. Grant the roles/artifactregistry.writer role to the Cloud Build service account, and verify that no employee has write permission on Artifact Registry.
- C. Use Cloud Run to build and deploy a custom validator, and enable an Eventarc trigger so that validation runs whenever a new image is uploaded.
- D. Configure Kritis in your GKE clusters to enforce deploy-time security policies.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Configure Binary Authorization on your GKE clusters to enforce deploy-time security policies.

**Correct Answer**

**A. Configure Binary Authorization on your GKE clusters to enforce deploy-time security policies.**

**Exam Reasoning Explanation**

The requirement is about what can be deployed to GKE, so the control has to act at deploy time, on the path where images enter the cluster. It also has to be a managed capability, because the scenario asks for minimal management overhead. Controlling who can push images, or validating images when they are uploaded, acts earlier in the supply chain and does not stop an untrusted image from reaching the cluster through another route. Between the two deploy-time options, the managed Google Cloud product wins over the open-source tool that you would deploy and operate yourself. Binary Authorization is the only option that meets all of these requirements.

**Key Exam Clues**

  * “only trusted container images can be deployed to GKE” is a hard constraint that places enforcement at the deployment step, not at the registry

  * “minimizing management overhead” is a hard constraint that favors a managed product over custom code or a self-run tool

  * “highly regulated” is a technical signal that favors centrally defined, auditable policy enforcement

  * “enforce deploy-time security policies” appears in both A and D, which signals that the real decision is between Google’s managed product and an open-source implementation

**Why This Is Correct**

Binary Authorization is a Google Cloud product for software supply-chain security. It acts as a deploy-time enforcer that prevents images that violate your policy from being deployed. It integrates with the GKE control plane to allow or block deployment based on policies you define. A policy can require attestations, which are signed statements that an image passed a step such as a build or test, and attestors verify them at deploy time. Policy enforcement events can be viewed in Cloud Audit Logs, and Google describes dry-run support for testing a policy before enforcing it. One prerequisite applies: if the policy requires attestations, you must set up attestors and have your pipeline create the attestations.

**Why the Other Options Are Not the Best Fit**

**Option B — Incorrect:** Restricting who can write to Artifact Registry controls who can publish images, not which images can be deployed. An untrusted image from another registry, or an image pushed through an allowed identity without any checks, could still be deployed to the cluster. Limiting write access is good practice, but it does not enforce trust at deployment.

**Option C — Technically Possible but Not Best:** A custom validator triggered when an image is uploaded checks images at the registry, not at deployment, so it does not block images that arrive another way. It is also custom code you must build, secure, and maintain, which works against the minimal-overhead requirement.

**Option D — Technically Possible but Not Best:** Kritis is an open-source implementation of deploy-time enforcement that uses an admission controller, so it fits the enforcement point. You deploy and operate it yourself in the clusters, though, while Binary Authorization is the Google-managed product natively integrated with GKE and based on the Kritis specification. That makes Kritis the higher-overhead choice.

**Exam Trap**

The trap is option D. Binary Authorization is based on the Kritis specification, so Kritis looks like the same capability. The difference is who runs it: Kritis is an open-source tool you install and maintain, and Binary Authorization is a managed Google Cloud service. Kritis would become a candidate only if the requirement were open-source, vendor-neutral enforcement on Kubernetes clusters that a managed Google Cloud service does not cover, and the team accepted operating it. A second trap is option B, because least-privilege access to the registry is a sound practice, but it addresses publishing and not deployment.

**Foundation Concept**

Container trust can be controlled at three points: build (who builds and signs), registry (who can push), and deploy (what the cluster admits). Only a deploy-time admission control guarantees that what runs matches policy, because images can reach a cluster from any registry. Controls at the earlier points reduce risk but do not enforce. Attestations let earlier stages record that an image passed checks so that the deploy-time check only needs to verify the signature, and least-privilege registry access complements deploy-time enforcement.

**Real-World Connection**

A regulated company’s Cloud Build pipeline builds each image, runs tests and scans, and signs an attestation for images that pass. The GKE clusters have a Binary Authorization policy requiring that attestation. When someone tries to deploy an unsigned image from a public registry, the deployment is blocked and the event is logged to Cloud Audit Logs, which gives the security team evidence for auditors. The team ran the policy in dry-run mode first to see what it would block before turning on enforcement.

**Memory Hook**

For “only trusted images can be deployed” with low overhead, choose the managed deploy-time enforcer, Binary Authorization, and not registry permissions, custom validators, or a self-run open-source tool.

**30-Second Exam Takeaway**

When a question requires that only trusted images be deployed to GKE with minimal management overhead, choose Binary Authorization. Registry write restrictions and upload-time validators act before deployment, and Kritis is an open-source implementation you would have to run yourself.

**Official References**

[**Google Cloud — Binary Authorization overview:**](https://docs.cloud.google.com/binary-authorization/docs/overview) Supports: Binary Authorization as a Google Cloud product for software supply-chain security, the deploy-time policy enforcer, attestations and attestors, its basis in the Kritis specification, and enforcement events in Cloud Audit Logs

[**Google Cloud Blog — Deploy only what you trust: introducing Binary Authorization for Google Kubernetes Engine:**](https://cloud.google.com/blog/products/identity-security/deploy-only-what-you-trust-introducing-binary-authorization-for-google-kubernetes-engine) Supports: Binary Authorization as a policy enforcement point integrated into GKE deployment, and Kritis as an open-source implementation of deployment-time enforcement that uses an admission controller

[**Google Cloud — Professional Cloud DevOps Engineer Certification exam guide (Section 2.4, securing the deployment pipeline: software supply chain security such as Binary Authorization):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain and objective alignment

</details>

---

### Exam 4 · Q47

Your organization’s shift-left security initiative requires every team to add guardrails to their Google Kubernetes Engine (GKE) clusters so that only trusted, approved container images can be deployed. Which approach best satisfies this requirement?

- A. Turn on Artifact Analysis for your Artifact Registry repositories to scan container images for known common vulnerabilities and exposures (CVEs)
- B. Require Binary Authorization to attest container images as part of your CI/CD pipeline before they can be deployed
- C. Set up Identity and Access Management (IAM) policies that enforce a least-privilege model across your GKE clusters
- D. Run Falco or Prisma Cloud on your GKE clusters to monitor running Pods for vulnerabilities

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Require Binary Authorization to attest container images as part of your CI/CD pipeline before they can be deployed

**Correct Answer**

**B. Require Binary Authorization to attest container images as part of your CI/CD pipeline before they can be deployed**

**Exam Reasoning Explanation**

The must-have constraint is that only trusted/approved images may be deployed, enforced as a guardrail — meaning automatically, not advisorially — and “shift left” means the check has to happen before or at deploy time, not after. Detecting CVEs, applying least privilege, and runtime monitoring are all useful, but none of them stop an unapproved image from reaching the cluster. Tracing requirement → capability → elimination → decision: the requirement is “block untrusted images at deploy”; Binary Authorization supplies a deploy-time admission policy requiring attestations; A only scans and reports, C only governs who can act, D only observes after the fact; so B is the only option that gates the deployment itself.

**Key Exam Clues**

  * “guard rails... to only allow the deployment of trusted and approved images” is a hard constraint pointing to an enforcement/admission-control mechanism rather than a detection tool.

  * “shift left on security” is a sequence/timing signal: the control must act before or at deployment, which rules out anything that only observes afterward.

  * “on all the GKE clusters” signals an org-wide, policy-based guardrail rather than a one-off manual check in a single pipeline.

**Why This Is Correct**

Binary Authorization is a deploy-time policy engine for GKE (and other supported platforms) that only allows an image to run if it carries attestations proving it passed required steps, such as a build or vulnerability-scan gate earlier in the CI/CD pipeline. Because the policy is enforced by the admission controller at deploy time, an image lacking the required attestation is rejected before it ever starts — which is precisely what “guardrails to only allow trusted and approved images” is asking for, and it acts at the earliest possible point in the deployment lifecycle, satisfying “shift left.”

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** Artifact Analysis scans images in Artifact Registry and surfaces CVEs, which is valuable input, but scanning by itself does not stop an unapproved image from being deployed; nothing blocks the deployment unless those findings are wired into an enforcement mechanism such as Binary Authorization.

**Option C — Different Use Case:** least-privilege IAM policies control which identities are allowed to perform which actions, such as who may deploy to a cluster. That says nothing about whether a specific image is trusted; a fully authorized engineer could still deploy an unapproved image.

**Option D — Violates Requirement:** Falco and Prisma Cloud are runtime security tools that detect and alert on suspicious behavior in Pods that are already running. By definition this happens after deployment, which satisfies neither “guardrail that prevents deployment” nor “shift left.”

**Exam Trap**

The trap is treating vulnerability scanning (Option A) as equivalent to a deployment guardrail. Scanning answers “is this image risky?” while the question asks for a mechanism that answers “can this image run at all?” The distinction is enforcement versus detection. If the requirement were instead “identify which images contain known CVEs” rather than “only allow approved images to deploy,” Option A would become the correct answer.

**Foundation Concept**

Shift-left security means moving verification earlier in the software delivery lifecycle so problems are caught before production rather than after. In practice this splits into two complementary capabilities: scanning/detection (find issues early, e.g., CVE scanning) and enforcement/admission control (block anything that hasn’t proven it meets policy, e.g., Binary Authorization). A guardrail, by definition, belongs to the enforcement category — it has to be able to say “no.”

**Real-World Connection**

A team configures its CI/CD pipeline so that after a build passes vulnerability scanning and tests, Cloud Build signs an attestation; a Binary Authorization policy on the GKE clusters then requires that attestation before admitting any Pod. The operational result is that an engineer can no longer deploy an untested or unscanned image directly to production even by accident, which reduces the risk of a known-vulnerable or unverified image causing an incident and gives InfoSec an auditable, cluster-wide enforcement point instead of relying on manual review.

**Memory Hook**

“Guardrail means gate, not gauge” — if the requirement is to block deployment, think Binary Authorization; if it’s to measure or report risk, think scanning tools like Artifact Analysis.

**30-Second Exam Takeaway**

When a question asks for a control that only allows trusted/approved artifacts to be deployed, look for an admission-control or attestation mechanism rather than a scanning, IAM, or runtime-monitoring tool — those inform or restrict activity around the deployment but don’t gate the deployment decision itself.

**Official References**

[**Google Cloud — Binary Authorization overview:**](https://cloud.google.com/binary-authorization/docs/overview) Supports: correct-answer mechanism — deploy-time attestation and admission-control enforcement on GKE

[**Google Cloud — Artifact Analysis and vulnerability scanning:**](https://cloud.google.com/artifact-analysis/docs/container-analysis) Supports: why Option A is a scanning/detection capability rather than a deployment guardrail (also confirms the current product name, formerly Container Analysis)

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 2.4, Securing the deployment pipeline):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment — Binary Authorization is explicitly named under securing the deployment pipeline

</details>

---

### Exam 4 · Q49

Your organization runs Jenkins on a Google Cloud Compute Engine VM for CI/CD and wants to extend its pipelines to manage infrastructure as code with Terraform. The Terraform runs that execute on this Jenkins instance need to be authorized to create Google Cloud resources, and you want to follow Google-recommended practices for granting that authorization. What should you do?

- A. Verify that the Jenkins VM has an attached service account granted the appropriate Identity and Access Management (IAM) permissions
- B. Configure a Terraform module that has Secret Manager supply the authentication credentials at runtime
- C. Create a separate service account, download its key file, and set its value in the GOOGLE_CREDENTIALS environment variable on the Jenkins server
- D. Add a gcloud auth application-default login step to the Jenkins job before the Terraform commands run

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Verify that the Jenkins VM has an attached service account granted the appropriate Identity and Access Management (IAM) permissions

**Correct Answer**

**A. Verify that the Jenkins VM has an attached service account granted the appropriate Identity and Access Management (IAM) permissions**

**Exam Reasoning Explanation**

The hard constraint is that the authorization method must follow Google-recommended practice, not merely “work.” Terraform on Google Cloud authenticates through Application Default Credentials (ADC), and when Terraform runs on a Compute Engine VM, ADC automatically picks up the VM’s attached service account via the metadata server — no key file or login step required. Walking the chain: requirement (authorize Terraform to create resources, the Google-recommended way) → capability (ADC + attached service account is Google’s documented preferred method for production code on Google Cloud) → elimination (B adds an unnecessary credential-retrieval layer, C introduces a long-lived downloaded key, D is designed for interactive human sign-in) → decision (A simply confirms the native, keyless mechanism is correctly configured).

**Key Exam Clues**

  * “authorized to create Google Cloud resources” is the core requirement: the solution must grant Terraform an identity with the right permissions, not just make Terraform technically runnable.

  * “follow Google-recommended practices” is an exclusion cue that rules out any option involving a manually downloaded, long-lived key or an interactive login flow.

  * “Jenkins running on Google Cloud VM instances” is a technical signal that the workload already runs on Compute Engine, which is exactly the environment where attached-service-account authentication applies natively.

**Why This Is Correct**

Google documents Application Default Credentials as the recommended way to authenticate Terraform to Google Cloud, and specifically states that attaching a user-managed service account is the preferred way to supply ADC with credentials for production code running on Google Cloud. Because the Jenkins VM is already a Compute Engine instance, Terraform executing there automatically discovers and uses that attached service account’s credentials through the metadata server. Confirming the VM has an attached service account with the correct IAM permissions is therefore all that’s needed — no credential file to create, store, or rotate.

**Why the Other Options Are Not the Best Fit**

**Option B — Technically Possible but Not Best:** having a Terraform module pull credentials from Secret Manager at runtime still means managing a stored secret and the logic to retrieve it, which is more moving parts than necessary when the VM can already supply credentials natively through its attached identity; it doesn’t match Google’s stated preferred method for this exact scenario.

**Option C — Violates Requirement:** downloading a service account key and placing it in the GOOGLE_CREDENTIALS environment variable is a documented authentication method, but Google’s own guidance treats service account keys as the less secure, fallback option for cases where attaching a service account isn’t possible (local development, on-premises, other clouds) — not for a workload already running on a GCE VM, so it fails the “Google-recommended practices” requirement.

**Option D — Incorrect:** gcloud auth application-default login creates local ADC credentials tied to a human user’s sign-in session for development workstations; it isn’t intended for unattended, automated CI/CD execution and doesn’t represent how production workloads on Google Cloud are meant to authenticate.

**Exam Trap**

The trap is assuming that because options B, C, and D all result in Terraform being able to authenticate, they’re equally valid — the question isn’t asking what works, it’s asking what Google recommends. The moment a scenario already places the workload on a GCE VM, that’s the signal to reach for attached-service-account credentials rather than any form of manually managed or interactive credential. If the Jenkins server instead ran outside Google Cloud (on-premises or another cloud), a downloaded key or Workload Identity Federation would become the relevant choice instead.

**Foundation Concept**

Application Default Credentials is Google Cloud’s unified strategy for letting client libraries and tools like Terraform find credentials automatically based on where code is running, without changing application code between environments. On Google Cloud compute resources, the preferred credential source is an attached service account resolved through the instance metadata server; everywhere else (local workstations, on-premises, other clouds), ADC falls back to user credentials, impersonation, downloaded keys, or Workload Identity Federation. Recognizing which environment you’re in tells you which ADC source is “recommended” for that case.

**Real-World Connection**

A platform team migrates their Terraform runs from a developer’s laptop (using a downloaded service account key) to a Jenkins job running on a GCE VM. By removing the key file and instead attaching a purpose-built service account to the VM with only the IAM roles Terraform needs, they eliminate a long-lived credential that could leak through logs, source control, or a compromised laptop, and they gain centralized control: revoking or auditing access now means managing the VM’s service account rather than hunting down who has a copy of the key.

**Memory Hook**

“On a GCP VM, let the VM’s own identity do the work — don’t hand Terraform a key it doesn’t need.”

**30-Second Exam Takeaway**

When a workload authenticating to Google Cloud is already running on a Google Cloud compute resource, the Google-recommended answer is almost always an attached service account with Application Default Credentials — treat downloaded keys and interactive login commands as fallback options reserved for environments outside Google Cloud.

**Official References**

[**Google Cloud — Authentication for Terraform:**](https://cloud.google.com/docs/terraform/authentication) Supports: correct-answer mechanism — ADC as the recommended authentication method and attached service accounts as the preferred credential source for production code on Google Cloud; also clarifies why the downloaded-key and `gcloud auth application-default login` options are not the best fit here

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 2.3, Managing pipeline configuration and secrets):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment — build versus runtime secret injection and configuration/secret management in CI/CD pipelines

</details>

---

### Exam 4 · Q51

While reviewing your delivery pipeline in Google Cloud Deploy, you determine that you need to cut down the toil built into the pipeline and shorten how long an end-to-end deployment takes to complete. What should you do? (Choose two.)

- A. Set up a trigger that notifies the responsible team as soon as a manual intervention step is reached
- B. Break the pipeline’s automation steps down into a larger number of smaller tasks
- C. Write a script that automates how the delivery pipeline itself is created in Google Cloud Deploy
- D. Bring in additional engineers to work through the manual steps
- E. Automate the promotion approval that moves a release from the development environment to the test environment

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Set up a trigger that notifies the responsible team as soon as a manual intervention step is reached **|** E. Automate the promotion approval that moves a release from the development environment to the test environment

**Correct Answer**

**A. Set up a trigger that notifies the responsible team as soon as a manual intervention step is reached**

**E. Automate the promotion approval that moves a release from the development environment to the test environment**

**Exam Reasoning Explanation**

The two hard constraints are that toil must actually be reduced (not redistributed) and that end-to-end deployment time must actually shorten. Walking the chain: requirement (cut toil and wall-clock time together) → capability (Cloud Deploy supports both removing an approval step entirely for low-risk promotions, and notifying a team the instant a still-required manual step is reached) → elimination (B restructures already-automated steps without removing manual work, C automates a different, infrequent activity — pipeline setup, not per-release execution, D keeps the same manual work in place and simply adds people to it) → decision (A and E are the two documented levers that actually shrink either the manual-work surface or the wait time around it).

**Key Exam Clues**

  * “cut down the toil” is a hard constraint that rules out any option that keeps the same manual work in place, however it’s staffed or restructured.

  * “shorten how long an end-to-end deployment takes to complete” is a second hard constraint requiring the chosen actions to reduce actual wall-clock duration, not just configuration effort.

  * “(Choose two)” signals the intended pair should cover two distinct categories of delay: a step that can be removed entirely, and a step that still needs a human but shouldn’t sit waiting.

**Why This Is Correct**

A: notifying the responsible team the moment a manual step is reached closes the gap between “work is ready” and “someone notices,” which is itself a form of toil (the overhead of checking or polling for whether action is needed), and it directly cuts the dead time the pipeline spends waiting for a human to notice — shortening the end-to-end duration even for steps that genuinely still require a person.

E: automating the approval that promotes a release from development to test removes a manual gate entirely for a lower-risk promotion, eliminating both the toil of a person clicking approve and the wait time for that approval to happen — exactly the kind of safe-to-automate step continuous delivery pipelines are designed to remove.

Together, these cover different parts of the pipeline rather than overlapping: E eliminates an entire manual approval step at one promotion stage, while A addresses steps that still require a human (such as a higher-risk later promotion) by minimizing how long the pipeline waits on that person. Between them, the set addresses both the parts of the pipeline that can be automated away and the parts that still need a human but shouldn’t be left idle.

**Why the Other Options Are Not the Best Fit**

**Option B — Incorrect:** subdividing automation steps into smaller tasks doesn’t remove any manual work and doesn’t inherently shorten the pipeline; it can just as easily add coordination overhead between more steps, and nothing about step granularity on its own reduces toil or wall-clock duration.

**Option C — Different Use Case:** scripting the creation of the delivery pipeline automates a setup or configuration activity that typically happens once, or only when the pipeline definition itself changes — not the recurring, per-release toil and delay the question is asking about.

**Option D — Violates Requirement:** adding more engineers to the manual steps keeps the same manual work in place and simply spreads it across more people; it doesn’t eliminate the work itself, so it directly fails the “reduce toil” requirement rather than satisfying it.

**Exam Trap**

The trap is treating “add more people” or “add more granular steps” as if they address toil, when the defining feature of toil is manual, repetitive work that can be automated away — the fix is removing the need for a human, or speeding up the handoff when a human is genuinely unavoidable, not staffing it up or restructuring steps that are already automated. If a step truly can’t be automated yet, such as a production approval requiring a compliance sign-off, the right lever is still minimizing wait time with a notification, not adding people to it.

**Foundation Concept**

Reducing toil in a delivery pipeline means either eliminating a manual step by automating it outright, or, where a human genuinely must be involved, minimizing the delay between “action needed” and “action taken.” Cloud Deploy supports both patterns directly: approval requirements can be automated away for low-risk promotions by driving the next promotion from a Pub/Sub event (such as a successful test run), and for steps that still require a human, Cloud Deploy’s Pub/Sub notifications — including its dedicated approvals topic — let a team be notified the instant action is needed instead of relying on someone to check manually.

**Real-World Connection**

A platform team configures their Cloud Deploy pipeline so that promotion from development to test happens automatically once tests pass, removing a manual approval that used to sit idle overnight waiting for someone to notice. For the still-required production approval, they subscribe their on-call system to the pipeline’s approval notifications so the approver is paged the moment a release is ready, cutting what used to be a multi-hour wait for someone to check their email down to minutes.

**Memory Hook**

“Automate the gate you can remove; page the human for the gate you can’t.”

**30-Second Exam Takeaway**

When a question asks how to cut toil and shorten end-to-end deployment time together, look for one option that removes a manual approval step entirely through automation and another that minimizes the wait time for approvals that still genuinely require a human — adding staff or restructuring already-automated steps addresses neither goal.

**Official References**

[**Google Cloud — Promote a release in Cloud Deploy:**](https://cloud.google.com/deploy/docs/promote-release) Supports: correct-answer mechanism for Option A — the clouddeploy-approvals Pub/Sub topic notifies teams or systems the moment a rollout needs manual approval

[**Google Cloud — Integrating Cloud Deploy with other systems:**](https://cloud.google.com/deploy/docs/integrating) Supports: correct-answer mechanism for Option E — using Pub/Sub notifications (such as successful test results) to automatically promote a release to the next target

[Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 2.1, Designing pipelines): ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment — CI/CD pipeline triggers and configuring deployment processes such as approval flows

</details>

---

### Exam 4 · Q59

You’re building the CI/CD pipeline for an application on Google Kubernetes Engine (GKE), deployed with a Kubernetes Deployment, Service, and Ingress. The application team has asked for blue/green deployments, and you now need to implement the rollback step. What should you do?

- A. Run kubectl rollout undo
- B. Delete the new container image and delete its running Pods
- C. Update the Kubernetes Service’s selector to point back at the previous Deployment
- D. Scale the new Kubernetes Deployment down to zero replicas

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Update the Kubernetes Service’s selector to point back at the previous Deployment

**Correct Answer**

**C. Update the Kubernetes Service’s selector to point back at the previous Deployment**

**Exam Reasoning Explanation**

The hard constraint is that the rollback mechanism has to match the deployment strategy actually in use, and blue/green keeps two independently running Deployments side by side rather than progressively updating one. Walking the chain: requirement (roll back a blue/green deployment) → capability (a Service’s label selector is what decides which Deployment’s Pods receive traffic, and switching it back to the previous Deployment restores service instantly since those Pods never stopped running) → elimination (A reverts a single Deployment’s own revision history, which is the rolling-update model, not two separate Deployments; B and D either remove capacity or fail to redirect traffic without also touching the Service) → decision (C is the one action that matches how blue/green is actually structured).

**Key Exam Clues**

  * “blue/green deployment methodology” is a hard constraint that determines which rollback mechanism applies, since blue/green and rolling updates use fundamentally different rollback mechanics.

  * “Deployment, Service, and Ingress” is a technical signal confirming the Service’s label selector is the layer that actually controls which set of Pods receives traffic — exactly what a blue/green switch manipulates.

  * “implement the rollback actions,” rather than “fix the bug” or “investigate the failure,” is a scope signal: the task is to restore traffic to the known-good version, not to diagnose or rebuild anything.

**Why This Is Correct**

In a blue/green setup, the old (“blue”) and new (“green”) versions run as two separate, independently running Deployments at the same time, and a single Kubernetes Service’s label selector decides which one actually receives traffic. Because both Deployments keep running after the cutover, rolling back is simply a matter of updating the Service’s selector so it matches the previous Deployment’s Pod labels again — traffic returns to the known-good version instantly, with no redeployment, rebuild, or Pod deletion needed, and the problematic new Deployment is left intact for investigation.

**Why the Other Options Are Not the Best Fit**

**Option A — Different Use Case:**`kubectl rollout undo` reverts a single Deployment back to an earlier revision in its own rollout history, which is the rollback mechanism for a rolling-update strategy. In blue/green, the previous version isn’t a prior revision of the same Deployment — it’s a separate, still-running Deployment — so this command doesn’t accomplish the kind of switch blue/green rollback requires.

**Option B — Violates Requirement:** deleting the new image and its running Pods removes the broken version but does nothing to point the Service back at Pods that can actually serve traffic, risking an outage rather than restoring service to the previous version.

**Option D — Technically Possible but Not Best:** scaling the new Deployment to zero stops it from running, but unless the Service’s selector is also switched back to the old Deployment, there’s nothing left for the Service to point at, so this step alone doesn’t complete a working rollback.

**Exam Trap**

The trap is reaching for `kubectl rollout undo` out of habit, since it’s the familiar Kubernetes rollback command — but that command is scoped to a Deployment’s own revision history, which is the rolling-update model, not the two-Deployment, Service-switch model that defines blue/green. The deployment strategy named in the scenario is the signal that determines which rollback mechanism actually applies.

**Foundation Concept**

Blue/green deployments keep two complete, independent environments running side by side and use a single switch — here, a Service’s label selector — to decide which one is “live.” That design is what makes rollback instant and low-risk: because the previous environment was never torn down, reverting is just flipping the switch back, rather than rebuilding or restoring anything.

**Real-World Connection**

A team cuts their Service over to a newly deployed “green” version and immediately starts seeing errors in production. Because the “blue” Deployment’s Pods are still running untouched, they patch the Service’s selector back to the blue labels, and traffic returns to the stable version within seconds — giving the team time to debug the green Deployment without any user-facing downtime or a rushed redeploy.

**Memory Hook**

“Blue/green rollback is a selector flip, not a rollout undo — the old version never left.”

**30-Second Exam Takeaway**

When a question specifies blue/green deployments on Kubernetes and asks how to roll back, look for the option that repoints the Service’s selector to the previous Deployment — `kubectl rollout undo` belongs to rolling updates, not to a strategy built around two independently running Deployments.

**Official References**

[Kubernetes documentation — Service: ](https://kubernetes.io/docs/concepts/services-networking/service/)Supports: correct-answer mechanism — a Service’s label selector determines which Deployment’s Pods receive traffic, and switching it is how blue/green cutover and rollback work

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 2.2, Implementing and managing pipelines):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment — deployment strategies, including blue/green

</details>

---

### Exam 4 · Q60

You’re building a Cloud Run application that needs an API key to call a third-party API, and you want to store and use that key securely, following Google-recommended practices. What should you do?

- A. Store the API key as a secret in Secret Manager, and expose that secret to the Cloud Run service as an environment variable
- B. Store the API key as a secret in Secret Manager, mount it as a file under a custom directory, and have the application decrypt it before use
- C. Store the API key as a key in Cloud Key Management Service (Cloud KMS), and expose it to the Cloud Run service as an environment variable
- D. Encrypt the API key with Cloud Key Management Service (Cloud KMS), pass the resulting ciphertext to Cloud Run as an environment variable, and have the application decrypt it before use

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Store the API key as a secret in Secret Manager, and expose that secret to the Cloud Run service as an environment variable

**Correct Answer**

**A. Store the API key as a secret in Secret Manager, and expose that secret to the Cloud Run service as an environment variable**

**Exam Reasoning Explanation**

The hard constraint is that the storage and retrieval mechanism must be both secure and the one Google specifically documents as recommended for this exact scenario — a Cloud Run workload needing a credential. Walking the chain: requirement (securely store and use an API key in Cloud Run, the Google-recommended way) → capability (Secret Manager is the purpose-built secret store, and Cloud Run has native support for exposing a Secret Manager secret as an environment variable at startup, with no application-level cryptography involved) → elimination (B misdescribes that native integration by adding an unnecessary manual decryption step, C misapplies Cloud KMS as if it were a secret store, D manually rebuilds an encrypt/decrypt flow that Secret Manager’s integration already handles) → decision (A is the simplest path that matches exactly what Google documents).

**Key Exam Clues**

  * “secure way to store and use the API key... following Google-recommended practices” is an exclusion cue pointing to the purpose-built secret-storage service and its native Cloud Run integration, rather than a general-purpose key-management service or a manually engineered encrypt/decrypt flow.

  * “API key” — an arbitrary credential string, not a cryptographic key used to encrypt other data — is a technical signal distinguishing this from what Cloud KMS actually manages.

  * The repeated phrase “decrypt... before use” appearing in two of the four options is worth noticing: Secret Manager’s native Cloud Run integration never requires the application to perform its own decryption step, so any option describing that extra step is describing unnecessary complexity.

**Why This Is Correct**

Google explicitly recommends storing sensitive values like API keys for Cloud Run workloads in Secret Manager, and Cloud Run has built-in, native support for exposing a Secret Manager secret to a service as an environment variable. Cloud Run retrieves the secret’s value securely at instance startup and makes it directly available to the application, while Secret Manager itself handles encryption at rest and access control through IAM. No custom decryption code, encryption key management, or special mount path is required, which makes this the simplest, most secure, and most Google-aligned way to meet the requirement.

**Why the Other Options Are Not the Best Fit**

**Option B — Incorrect:** this starts from the right service, Secret Manager, but misrepresents how the integration works. Cloud Run and Secret Manager already handle secure delivery and decryption of the secret’s value, so an application-level “decrypt the key” step is unnecessary and reflects a misunderstanding of the feature; the described mount path also isn’t a standard, documented convention.

**Option C — Incorrect:** Cloud KMS manages cryptographic keys used to encrypt, decrypt, or sign data — it isn’t designed to store arbitrary secret values such as an API key, so treating an API key as something to “save in Cloud KMS as a key” misapplies the service to a job it isn’t built for.

**Option D — Technically Possible but Not Best:** manually encrypting the API key with Cloud KMS, passing the ciphertext as an environment variable, and decrypting it inside the application is a workable but needlessly complex pattern that duplicates work Secret Manager’s native Cloud Run integration already performs automatically and securely — it isn’t the practice Google documents as recommended for this scenario.

**Exam Trap**

The trap is assuming that because Cloud KMS is an “encryption” service, it must be the more secure or more rigorous choice for protecting an API key. Cloud KMS solves a different problem — managing the keys used to encrypt other data — while Secret Manager is the service purpose-built for storing and retrieving secret values like API keys, passwords, and certificates, with its own encryption and access control handled internally.

**Foundation Concept**

Google Cloud deliberately separates secret storage (Secret Manager, for values an application needs to read, like API keys and credentials) from key management (Cloud KMS, for cryptographic keys used to encrypt, decrypt, or sign data elsewhere). Recognizing which category a piece of sensitive data falls into points directly at which service to use, and Cloud Run’s native integrations with Secret Manager mean the correct choice usually requires no custom cryptography code in the application at all.

**Real-World Connection**

A team deploying a Cloud Run service that calls a paid weather API stores that API key as a Secret Manager secret and references it as an environment variable in the service’s configuration. When the key needs to rotate, they add a new secret version and update the reference; the application code never changes, never handles raw ciphertext, and the service account’s IAM permissions determine exactly who and what can read the key, giving the team both operational simplicity and a clean audit trail.

**Memory Hook**

“An API key is a secret to store, not a key to manage — reach for Secret Manager, not Cloud KMS.”

**30-Second Exam Takeaway**

When a Cloud Run workload needs to securely hold a credential like an API key, the Google-recommended answer is almost always storing it in Secret Manager and exposing it through Cloud Run’s native secret integration — Cloud KMS and manual encrypt/decrypt flows solve a different problem and add unnecessary complexity here.

**Official References**

[**Google Cloud — Configure secrets for Cloud Run services:**](https://cloud.google.com/run/docs/configuring/secrets) Supports: correct-answer mechanism — Google’s recommendation to store sensitive values in Secret Manager and expose them to Cloud Run natively as environment variables

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 2.3, Managing pipeline configuration and secrets):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment — configuration and secret management (Secret Manager) versus key management (Cloud KMS)

</details>

---

### Exam 5 · Q2 ❌ *you missed this*

You use a **multi-step Cloud Build pipeline** to build and deploy your application to **Google Kubernetes Engine (GKE)**. You want to **integrate with a third-party monitoring platform** by performing an **HTTP POST of the build information to a webhook**. You want to **minimize development effort**.

What should you do?

- **A.** Add logic to **each Cloud Build step** to **HTTP POST the build information** to a webhook.
- **B.** Add a **new step at the end of the pipeline** in **Cloud Build** to **HTTP POST the build information** to a webhook.
- **C.** Use **Cloud Logging** to create a **logs-based metric** from the **Cloud Build logs**. Create an **alert** with a **Webhook notification type**.
- **D.** Create a **Cloud Pub/Sub push subscription** to the **Cloud Build**`**cloud-builds**`**Pub/Sub topic** to **HTTP POST the build information** to a webhook.

<details><summary>Answer &amp; explanation</summary>

**Correct:** **D.** Create a **Cloud Pub/Sub push subscription** to the **Cloud Build**`**cloud-builds**`**Pub/Sub topic** to **HTTP POST the build information** to a webhook.

**Correct Answer:**

**D.** Create a **Cloud Pub/Sub push subscription** to the **Cloud Build**`**cloud-builds**`**Pub/Sub topic** to **HTTP POST the build information** to a webhook.

**Explanation:**

Cloud Build **automatically publishes build events** to the `**cloud-builds**`**Pub/Sub topic**.

  * The most efficient approach is to **subscribe to this topic** and trigger an **HTTP POST to the webhook** whenever a build completes.

  * This **decouples** the build pipeline from the monitoring integration, reducing complexity and **minimizing development effort**.

**Steps to implement:**

  1. **Create a Cloud Pub/Sub subscription** for the `cloud-builds` topic.

  2. **Set up a push subscription** that **sends build events** to the **third-party monitoring webhook**.

**Why Other Options Are Incorrect:**

**A. Add logic to each Cloud Build step** – This is inefficient because **each step would need to be modified** , leading to **code duplication and maintenance overhead**.

**B. Add a new step at the end of the pipeline** – While **this works** , it **ties webhook integration to the build process** , making it **less flexible** and **more effort to maintain**.

**C. Use Cloud Logging and logs-based metrics** – This is **not the best approach** because:

  * Cloud Logging metrics are **aggregated over time** and not **real-time event triggers**.

  * It introduces **additional configuration steps** without improving efficiency.

**Reference Documentation:**

[Cloud Build and Cloud Pub/Sub integration](https://cloud.google.com/build/docs/automate-builds-pubsub-events)  
[ Creating a Pub/Sub push subscription](https://cloud.google.com/pubsub/docs/create-push-subscription)

</details>

---

### Exam 5 · Q9

**In managing your CI/CD pipeline for building and deploying application artifacts, ensuring secure access to secrets and simplifying their rotation in the event of a security breach is paramount. What action should you take to address this concern?**

- I. Require developers to input secrets during the build process and emphasize avoiding storage of secrets at rest.
- II. Store secrets in a distinct configuration file within Git, granting specific developers access to this file.
- III. Securely store secrets in Cloud Storage encrypted with a key from Cloud KMS, providing the CI/CD pipeline access via IAM.
- IV. Encrypt the secrets and store them within the source code repository, while safeguarding the decryption key in a separate repository accessible to the pipeline.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Securely store secrets in Cloud Storage encrypted with a key from Cloud KMS, providing the CI/CD pipeline access via IAM.

**III. Securely store secrets in Cloud Storage encrypted with a key from Cloud KMS, providing the CI/CD pipeline access via IAM.**

Here's why this stands out as the most secure and manageable approach:

  * **Centralized Secret Management:** Cloud Storage provides a dedicated location for storing secrets, separate from application code.

  * **Robust Encryption:** Cloud KMS offers strong encryption with granular key management capabilities.

  * **Identity-Based Access Control:** IAM allows fine-grained permissions, ensuring only the CI/CD pipeline has authorized access to secrets.

  * **Secret Isolation:** Separates secret management from source code repositories, reducing the risk of accidental exposure.

  * **Secret Rotation:** Cloud KMS simplifies secret rotation, enhancing security in case of a breach.

Let's analyze the shortcomings of the other options:

  * **I. Require developers to input secrets during the build process...** This introduces potential for human error and makes secret management cumbersome within a CI/CD pipeline.

  * **II. Store secrets in a distinct configuration file within Git...** Storing secrets within version control, even with limited access, increases the risk of accidental exposure in the history or through compromised credentials.

  * **IV. Encrypt the secrets and store them within the source code repository...** Even encrypted, directly storing secrets within the repository presents a greater risk compared to a dedicated secret management system.

**Reference:**

<https://cloud.google.com/security-key-management>

</details>

---

### Exam 5 · Q14

**Your organization recently shifted to a container-based workflow for application development. Within this setup, your team continuously deploys multiple applications via an automated build pipeline to the production environment. However, a recent security audit flagged concerns about potential vulnerabilities in the code deployed to production. The conventional tooling for virtual machine (VM) vulnerabilities is inadequate for the containerized environment. How can you ensure the security and patch level of all code processed through the pipeline?**

- I. Implement Container Analysis to scan and report Common Vulnerabilities and Exposures (CVEs).
- II. Configure the containers within the build pipeline to autonomously update themselves before release.
- III. Adapt existing operating system vulnerability software to function within the containerized environment.
- IV. Integrate static code analysis tooling to scrutinize the Docker files utilized in creating the containers.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Implement Container Analysis to scan and report Common Vulnerabilities and Exposures (CVEs).

**I. Implement Container Analysis to scan and report Common Vulnerabilities and Exposures (CVEs).**

Here's why this stands out:

  * **Container-Focused:** Container Analysis is specifically designed to identify vulnerabilities within container images, offering a more accurate and targeted approach than traditional VM-based tools.

  * **Pipeline Integration:** Seamlessly integrates into your CI/CD pipeline, providing security checks at multiple stages of the development process.

  * **Actionable Insights:** Provides detailed reports on discovered CVEs, enabling timely remediation.

**Why Other Options Are Less Ideal:**

  * **II. Configure the containers within the build pipeline...** While auto-updating can help in some cases, it doesn't guarantee patching of known CVEs and might lead to compatibility issues.

  * **III. Adapt existing operating system vulnerability software...** Adapting VM-focused tools for containers is often cumbersome and may not offer comprehensive coverage.

  * **IV. Integrate static code analysis tooling...** While valuable for overall code quality, static code analysis primarily focuses on custom code, not necessarily external library vulnerabilities.

**Key Points:**

  * **Proactive Security:** Implement vulnerability scanning early in your build pipeline to discover issues before they reach production.

  * **Image Repository Integration:** Consider integrating Container Analysis with your image repository (e.g., Google Container Registry) for continuous monitoring of stored images.

**Additional Considerations:**

  * **Base Images:** Regularly update base images to incorporate OS-level security patches.

  * **Dependency Scanning:** Use tools to scan for outdated dependencies with known vulnerabilities in your container images.

**Reference:**  
<https://cloud.google.com/container-analysis/docs/container-analysis>

</details>

---

### Exam 5 · Q16

**You're responsible for deploying application releases to Google Cloud Platform (GCP) using Jenkins to streamline processes, reduce overhead, and ensure data security. What's the best course of action?**

- I. Deploy Jenkins on local workstations.
- II. Implement Jenkins on an on-premises Kubernetes cluster.
- III. Utilize Jenkins within Google Cloud Functions.
- IV. Set up Jenkins on Compute Engine virtual machines.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Set up Jenkins on Compute Engine virtual machines.

**IV. Set up Jenkins on Compute Engine virtual machines.**

Here's why this choice is optimal:

  * **Resource Control:** Compute Engine provides dedicated VMs, giving you full control over Jenkins' environment, resources, and configuration.

  * **Customization:** VMs offer flexibility for installing plugins, managing dependencies, and integrating with other GCP services.

  * **Security:** You can implement robust security measures on the VMs, aligning with your data security requirements.

  * **Scalability:** If needed, you can adjust the resources allocated to your Jenkins setup as build demands change.

**Why other options are less ideal:**

  * **I. Deploy Jenkins on local workstations.** This lacks scalability, consistency, and is vulnerable to local machine failures.

  * **II. Implement Jenkins on an on-premises Kubernetes cluster.** Managing a hybrid cloud setup adds complexity and might not be necessary if your application already resides in GCP.

  * **III. Utilize Jenkins within Google Cloud Functions.** Cloud Functions are designed for short-lived tasks, not a persistent CI/CD tool like Jenkins.

**Important Considerations:**

  * **High Availability:** For mission-critical pipelines, consider setting up multiple Jenkins instances in a master-agent configuration.

  * **GCP Integration:** Utilize GCP features like Cloud Build for some parts of your pipeline, where appropriate, for cost-efficiency and simplicity.

  * **Security Best Practices:** Harden your Jenkins VMs, implement proper access control, and encrypt sensitive data.

**Reference:**

<https://plugins.jenkins.io/google-compute-engine/>

</details>

---

### Exam 5 · Q19 ❌ *you missed this*

**You're set to deploy a new feature of a web-based application to production and wish to utilize Google Kubernetes Engine (GKE) for a phased rollout to half of the web server pods. What is the optimal course of action?**

- I. Employ a partitioned rolling update method.
- II. Implement Node taints with NoExecute.
- III. Utilize a replica set within the deployment specification.
- IV. Opt for a stateful set with parallel pod management policy.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Employ a partitioned rolling update method.

**Correct Option:**

**I. Employ a partitioned rolling update method.**

**Justification:**

  * **Controlled Rollout:** Partitioned rolling updates allow you to release your new feature in increments. You can update half of your web server pods, validate functionality, and then proceed with the remaining pods if everything looks good.

  * **Kubernetes Native:** This method is directly supported within Kubernetes Deployment objects, ensuring a streamlined process.

  * **Phase Control:** You have granular control over the percentage of pods updated in each phase, enabling the targeted 50% rollout.

**Why Other Options Are Less Suitable:**

  * **II. Implement Node taints with NoExecute.** Node taints are used to control pod scheduling, not for incrementally updating existing pods.

  * **III. Utilize a replica set within the deployment specification.** Replica sets simply control the number of running pods, not the rollout strategy of updates.

  * **IV. Opt for a stateful set with parallel pod management policy.** Stateful sets are used for workloads requiring persistent storage and stable identifiers, not for phased rollouts of web servers.

**Reference:**

<https://cloud.google.com/kubernetes-engine/docs/concepts/statefulset#partitioning_rolling_updates>

<https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#partitions>

</details>

---

### Exam 5 · Q21 ❌ *you missed this*

**During the migration of an on-premises containerized web application to Google Cloud, considering specific traffic direction and testing needs, which deployment strategy and platform should you opt for?**

- I. Implement the canary release on Cloud Run, employing traffic splitting to route 10% of user traffic to the canary release based on the revision tag.
- II. Choose App Engine for deploying the canary release, utilizing traffic splitting to direct a subset of user traffic to the new version based on IP address.
- III. Deploy the canary release on Compute Engine, utilizing Anthos Service Mesh with Compute Engine to direct 10% of user traffic to the canary release via virtual service configuration.
- IV. Opt for Google Kubernetes Engine with Anthos Service Mesh for deploying the canary release, employing traffic splitting to direct 10% of user traffic to the new version based on the user-agent header configured in the virtual service.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Opt for Google Kubernetes Engine with Anthos Service Mesh for deploying the canary release, employing traffic splitting to direct 10% of user traffic to the new version based on the user-agent header configured in the virtual service.

**Correct option: IV**

**Why option IV is correct**

**IV. Opt for Google Kubernetes Engine with Anthos Service Mesh for deploying the canary release, employing traffic splitting to direct 10% of user traffic to the new version based on the user-agent header configured in the virtual service.**

This is the **most appropriate and exam-accurate choice** given all constraints in the question:

  * The application is **containerized** and being migrated from **on-premises** → GKE is the natural target platform.

  * The question explicitly mentions **specific traffic direction and testing needs** , which implies **advanced traffic control** , not just percentage-based splitting.

  * **Anthos Service Mesh (ASM)** provides **Layer-7 traffic management** using Istio, enabling:

    * Header-based routing (such as `User-Agent`)

    * Canary testing for specific client groups (internal testers, beta users, bots, QA devices)

    * Fine-grained control without modifying application code

  * This allows **safe validation of new versions** under real traffic conditions while tightly controlling exposure.

From an SRE and DevOps perspective, this is the **gold standard** for canary deployments requiring deterministic traffic selection rather than random sampling.

**Why the other options are not suitable**

**I. Canary on Cloud Run using revision-based traffic splitting**  
Cloud Run supports **percentage-based traffic splitting only**. It does **not support header-based routing** , so you cannot direct traffic based on user-agent or other request attributes.

**II. App Engine with IP-based traffic splitting**  
IP-based routing is coarse, unreliable (NAT, mobile users), and not suitable for controlled canary testing. Additionally, App Engine is less aligned with migrating an existing **containerized** on-prem application.

**III. Compute Engine with Anthos Service Mesh**  
Anthos Service Mesh is designed for **Kubernetes workloads**. While traffic shaping on Compute Engine is possible, ASM does not manage non-GKE VM workloads for application-level canary routing.

**Final answer:** **IV**

</details>

---

### Exam 5 · Q25

**To facilitate trunk-based development in a central Git repository, how can you establish a robust CI/CD pipeline for a containerized application in Google Cloud, ensuring thorough testing for new versions to enhance its quality**

- I. Enforce a Git hook to mandate developers execute unit tests before pushing code to the central repository. Subsequently, initiate Cloud Build to construct the application container. Upon completion, deploy the container to a testing environment and execute integration tests. If successful, proceed to deploy the application container to the production environment, followed by the execution of acceptance tests.
- II. Implement a Git hook to enforce developers execute unit tests before pushing code to the central repository. Upon successful unit tests, trigger Cloud Build to build a container. Subsequently, deploy the application container to a testing environment, execute integration tests, and acceptance tests. If all tests pass, designate the code as production-ready and deploy the application container to the production environment.
- III. Initiate Cloud Build to build the application container and conduct unit tests within the container. Upon successful completion, deploy the application container to a testing environment and execute integration tests. Following successful integration tests, deploy the application container to the production environment, and execute acceptance tests.
- IV. Trigger Cloud Build to execute unit tests upon code push. If all unit tests pass, proceed to build and push the application container to a central registry. Subsequently, deploy the container to a testing environment, execute integration tests, and acceptance tests. Upon passing all tests, deploy the application to the production environment, and conduct smoke tests.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Trigger Cloud Build to execute unit tests upon code push. If all unit tests pass, proceed to build and push the application container to a central registry. Subsequently, deploy the container to a testing environment, execute integration tests, and acceptance tests. Upon passing all tests, deploy the application to the production environment, and conduct smoke tests.

**The most appropriate approach is:**

**IV. Trigger Cloud Build to execute unit tests upon code push. If all unit tests pass, proceed to build and push the application container to a central registry. Subsequently, deploy the container to a testing environment, execute integration tests, and acceptance tests. Upon passing all tests, deploy the application to the production environment, and conduct smoke tests.**

Explanation:

This approach outlines a well-structured CI/CD pipeline that leverages Cloud Build and ensures the application goes through multiple stages of testing before deployment to production:

  1. **Unit tests upon code push** ensure that basic functionality is verified immediately.

  2. **Building and pushing the container to a central registry** ensures that the built container image is version-controlled and available for subsequent deployments.

  3. **Deploying to a testing environment** for further integration and acceptance testing ensures that the application is thoroughly tested before it reaches production.

  4. **Smoke tests in production** provide an extra layer of verification in the live environment.

This process aligns well with trunk-based development and ensures quality by testing in incremental stages.

**Why the other options are incorrect:**

  * **I. Enforce a Git hook to mandate developers execute unit tests before pushing code to the central repository, then deploy to production after tests:** While this approach does involve unit and integration tests, relying on developers to run unit tests locally before a push is less reliable. Automated testing in CI (via Cloud Build) ensures consistent execution of tests in a controlled environment. Additionally, deploying directly to production before running acceptance tests in the production environment poses a risk.

  * **II. Enforce a Git hook and designate code as production-ready after passing tests:** Like the first option, this relies on local unit tests, which can be inconsistent. Also, labeling code as production-ready without actually deploying to production or running post-deployment tests (like smoke tests) increases risk.

  * **III. Initiate Cloud Build for unit tests and deploy to production before acceptance tests:** Deploying to production before running **acceptance tests** is risky. Acceptance tests should be executed in a controlled pre-production environment to ensure the application is fully functional before impacting production users.

**Documentation:**

[Cloud Build CI/CD Pipelines](https://cloud.google.com/build?hl=en)

</details>

---

### Exam 5 · Q26

**In your organization's multi-cloud setup, you're tasked with setting up a CI/CD pipeline for an application deployed using custom Compute Engine images across various cloud platforms. The solution should enable seamless building and deployment of images in the current environment while remaining adaptable to future changes. Which solution stack should you choose?**

- I. Opt for Cloud Build integrated with Packer.
- II. Choose Cloud Build combined with Google Cloud Deploy.
- III. Implement Google Kubernetes Engine alongside Google Cloud Deploy.
- IV. Utilize Cloud Build integrated with kpt (Kubernetes Package Manager).

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Opt for Cloud Build integrated with Packer.

**I. Opt for Cloud Build integrated with Packer.**

Here's why this choice stands out:

  * **Image Focus:** Packer is specialized in building images across multiple platforms, making it ideal for your multi-cloud setup.

  * **Flexibility:** Cloud Build can orchestrate the image building process using Packer and deploy the resulting images to the various cloud platforms.

  * **Future-Proof:** This combination provides a versatile foundation that can easily adapt as you add more cloud environments or change deployment strategies.

**Why Others Are Less Ideal:**

  * **II. Choose Cloud Build combined with Google Cloud Deploy.** Cloud Deploy is primarily focused on continuous delivery to Kubernetes environments, making it less relevant for a scenario centered around custom Compute Engine images.

  * **III. Implement Google Kubernetes Engine alongside Google Cloud Deploy.** While Kubernetes and Cloud Deploy are powerful, they add complexity if your core need is building and deploying images to VMs across clouds.

  * **IV. Utilize Cloud Build integrated with kpt (Kubernetes Package Manager).** kpt is a great tool for managing Kubernetes configurations but is less relevant to building multi-platform VM images.

**Reference:**

<https://cloud.google.com/build/docs/building/build-vm-images-with-packer>

</details>

---

### Exam 5 · Q29

**While setting up the CI/CD pipeline for an application deployed on Google Kubernetes Engine (GKE) utilizing Kubernetes Deployment, Service, and Ingress, the application team desires deployment using the blue/green methodology. What are the appropriate rollback actions to implement?**

- I. Perform a rollback using the kubectl rollout undo command.
- II. Delete the new container image and subsequently terminate the running Pods.
- III. Update the Kubernetes Service to revert to the previous Kubernetes Deployment.
- IV. Scale down the new Kubernetes Deployment to zero.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Update the Kubernetes Service to revert to the previous Kubernetes Deployment.

**Best Rollback Approach:**

**III. Update the Kubernetes Service to revert to the previous Kubernetes Deployment.**

**Reasons:**

  * **Blue/Green Alignment:** This directly embodies blue/green strategy, where you switch traffic between fully provisioned deployments, allowing for instantaneous rollback.

  * **Simplicity and Speed:** Updating the service selector is efficient and ensures traffic is quickly directed back to the previous, stable version.

  * **Control:** You retain both deployments, giving you the option to investigate the new deployment if needed.

**Why Other Options Are Less Ideal:**

  * **I. Perform a rollback using the kubectl rollout undo command.** While feasible, this mutates the current deployment, deviating from the pure blue/green approach where both versions remain intact.

  * **II. Delete the new container image and subsequently terminate...** This is destructive and can disrupt troubleshooting efforts if issues need to be analyzed in the new deployment.

  * **IV. Scale down the new Kubernetes Deployment to zero.** Scaling down still leaves the new deployment in place, and scaling back up to serve traffic could be slower than simply switching the Service.

</details>

---

### Exam 5 · Q30

**In developing an application on Cloud Run requiring access to a third-party API via an API key, adherence to Google-recommended practices for secure storage and usage of the key is paramount. What's the recommended approach?**

- I. Store the API key securely in Secret Manager as a secret, then reference it as an environment variable within the Cloud Run application.
- II. Save the API key in Secret Manager as a secret key, then mount it under the /sys/api_key directory and decrypt it within the Cloud Run application.
- III. Secure the API key in Cloud Key Management Service (Cloud KMS) as a key, then reference it as an environment variable within the Cloud Run application.
- IV. Encrypt the API key using Cloud Key Management Service (Cloud KMS), pass it as an environment variable to Cloud Run, and decrypt it for usage within the applicationX

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Store the API key securely in Secret Manager as a secret, then reference it as an environment variable within the Cloud Run application.

**Correct option: I**

**Why option I is correct**

**I. Store the API key securely in Secret Manager as a secret, then reference it as an environment variable within the Cloud Run application.**

This is the **Google-recommended and exam-accurate approach** for handling sensitive data such as API keys in **Cloud Run**.

Core security and platform fundamentals:

  * **Secret Manager is purpose-built for secrets** (API keys, tokens, passwords). It provides encryption at rest, fine-grained IAM access control, versioning, and audit logging.

  * **Cloud Run natively integrates with Secret Manager** , allowing secrets to be injected securely as environment variables **without embedding secrets in code or images**.

  * **No custom cryptography required** : Google manages encryption and decryption transparently, reducing operational risk and complexity.

  * **Least privilege** : The Cloud Run service account can be granted access to only the specific secret it needs.

This aligns perfectly with Google’s guidance: _use Secret Manager for application secrets and reference them securely at runtime_.

**Documentation:**  
<https://cloud.google.com/run/docs/configuring/secrets>

**Why the other options are not suitable**

**II. Mount the key under**`**/sys/api_key**`**and decrypt it in the app.**  
Cloud Run does not support arbitrary filesystem secret mounts like this, and manual decryption is unnecessary and error-prone. This is not a supported or recommended pattern.

**III. Store the API key directly in Cloud KMS and reference it as an environment variable.**  
Cloud KMS is designed for **encryption keys** , not for storing application secrets. Google explicitly recommends using **Secret Manager on top of KMS** for secret storage.

**IV. Encrypt the API key with KMS and decrypt it inside the application.**  
This adds needless complexity and increases the attack surface. Application-managed cryptography is discouraged when managed secret services are available.

**Final answer:** **I**

</details>

---

### Exam 5 · Q31

**In optimizing your deployment pipeline with Google Cloud Deploy to minimize toil and reduce deployment time, what steps should you take? (Choose two.)**

- I. Implement a trigger system to alert the relevant team for manual intervention when necessary during the deployment process.
- II. Break down automation tasks into smaller, more manageable components to streamline deployment.
- III. Develop a script to automate the setup of the deployment pipeline within Google Cloud Deploy, reducing manual configuration efforts.
- IV. Increase the number of engineers to expedite completion of manual steps in the deployment process.
- V. Automate approval procedures for promoting deployments from the development environment to the testing environment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Implement a trigger system to alert the relevant team for manual intervention when necessary during the deployment process. **|** V. Automate approval procedures for promoting deployments from the development environment to the testing environment.

**Correct Answers: I and V**

**Explanation**

The goal is explicitly:  
**Minimize toil** \+ **Reduce end-to-end deployment time** in **Google Cloud Deploy**.

The two actions that directly reduce _human bottlenecks_ and optimize _pipeline performance_ are:

**I. Implement a trigger system to alert the relevant team for manual intervention when necessary.**

Why this is correct

Manual approvals introduce **human latency** , which is one of the biggest contributors to long deployment times.

A trigger (Pub/Sub → Slack, email, webhook, PagerDuty, etc.) ensures:

  * The right person is notified immediately

  * The manual step completes as quickly as possible

  * Pipeline idle time is minimized

This **reduces deployment time** and **reduces toil** caused by missed or delayed approvals.

**V. Automate approval procedures for promoting deployments from dev → test.**

Why this is correct

If your pipeline already includes automated quality checks, then automatically approving the promotion:

  * Eliminates a manual step

  * Removes human bottlenecks

  * Reduces toil

  * Speeds up deployment across environments

  * Follows CI/CD best practices (automation + gating via tests)

Google Cloud Deploy supports automated approvals when the risk is low and automated tests ensure safety.

**Why the Other Options Are Incorrect**

**II. Break down automation tasks into smaller pieces — Not impactful**

This improves maintainability but **does not reduce toil or accelerate deployments**.

**III. Script the creation of the pipeline — One-time setup**

Automating _pipeline creation_ does not affect:

  * ongoing deployment time

  * repetitive toil  
It's a setup optimization, not a deployment optimization.

**IV. Add more engineers — Not helpful**

Increasing people does not solve CI/CD delays.  
Automation, not headcount, reduces toil.

**Doc:**[**Google Cloud Deploy – Approvals & Automation**](https://docs.cloud.google.com/deploy/docs/automation)

**Final Answer: I and V**

</details>

---

### Exam 5 · Q34

**In alignment with your company's security strategy to shift left on security, the InfoSec team requires all teams to enforce guardrails on Google Kubernetes Engine (GKE) clusters, allowing only the deployment of trusted and approved images. How can you fulfill this requirement effectively?**

- I. Implement Container Analysis in Artifact Registry to scan container images for common vulnerabilities and exposures (CVEs) during your CI/CD pipeline.
- II. Utilize Binary Authorization to verify and attest images during the CI/CD pipeline, ensuring only approved images are deployed to GKE clusters.
- III. Establish Identity and Access Management (IAM) policies to establish a least privilege model on GKE clusters, restricting image deployments based on predefined permissions.
- IV. Deploy Falco or Twistlock on GKE to actively monitor running Pods for vulnerabilities and security issues.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Utilize Binary Authorization to verify and attest images during the CI/CD pipeline, ensuring only approved images are deployed to GKE clusters.

**Correct option: II**

**Why option II is correct**

**II. Utilize Binary Authorization to verify and attest images during the CI/CD pipeline, ensuring only approved images are deployed to GKE clusters.**

This is the **Google-recommended and exam-correct mechanism** for enforcing **preventive (shift-left) security guardrails** on GKE.

Core security fundamentals:

  * **Binary Authorization is an admission control system** for GKE that enforces **deploy-time policies** , not just detection.

  * It ensures **only container images that are cryptographically attested and explicitly approved** can be deployed to a cluster.

  * Policies can require:

    * Images to come from trusted registries

    * Images to be signed by approved attestors

    * CI/CD pipelines to complete security checks before deployment

  * This directly fulfills the requirement of **allowing only trusted and approved images** , blocking everything else **before it reaches production**.

Binary Authorization is the canonical Google Cloud solution for **shift-left container security on GKE**.

**Authoritative documentation:**  
<https://cloud.google.com/binary-authorization/docs/overview>

**Why the other options are not suitable**

**I. Container Analysis image scanning**  
Image scanning detects vulnerabilities but **does not prevent deployment**. It is advisory, not an enforcement guardrail.

**III. IAM-based restrictions on image deployment**  
IAM controls _who_ can deploy, not _what_ images are deployed. It cannot validate image trust or integrity.

**IV. Runtime security tools (Falco / Twistlock)**  
These tools detect issues **after pods are already running** , which is **shift-right** , not shift-left. They do not prevent untrusted images from being deployed.

**Final answer:** **II**

</details>

---

### Exam 5 · Q43

**Following your organization's recent adoption of a container-based workflow for application development, your team consistently deploys numerous applications to a Kubernetes cluster in the production environment through an automated build pipeline. However, the security auditor has expressed concerns regarding the potential for developers or operators to bypass automated testing and push unauthorized code changes to production. How can you enforce approvals in this scenario?**

- I. Implement protected branches in the build system, mandating approval of pull requests.
- II. Deploy an Admission Controller to validate that incoming requests originate from approved sources.
- III. Utilize Kubernetes Role-Based Access Control (RBAC) to restrict access exclusively to approved users.
- IV. Enable binary authorization within the Kubernetes cluster and configure the build pipeline as an attestor.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Enable binary authorization within the Kubernetes cluster and configure the build pipeline as an attestor.

**IV. Enable binary authorization within the Kubernetes cluster and configure the build pipeline as an attestor.**

Here's why this approach is the strongest:

  * **Image-Level Enforcement:** Binary authorization provides granular control at the container image level. It ensures only images that have passed the required validation and approval steps (automated tests, security scans, human sign-off, etc.) within your build pipeline can be deployed into the Kubernetes cluster.

  * **Build Pipeline Integration:** Configuring the build pipeline as an attestor provides a tamper-resistant mechanism to track the approval state of an image along its creation process.

  * **Security Focus:** This approach is specifically tailored to prevent the deployment of unauthorized code, directly addressing the auditor's concern.

**While other options provide security benefits, they're either too broad or indirect:**

  * **I. Implement protected branches...** Enforces code review but doesn't prevent unauthorized image builds and deployments.

  * **II. Deploy an Admission Controller...** Useful for validating various properties, but would require defining complex rules and doesn't intrinsically track the approval status of an image.

  * **III. Utilize Kubernetes RBAC...** Vital for access control, but it doesn't enforce code approval within the build process.

**Reference:**  
<https://cloud.google.com/binary-authorization>

</details>

---

### Exam 5 · Q50

**What steps should you take to deploy the new versions of your service's API with minimal disruption to third-party developers and end users of third-party installed applications?**

- A. Implement the new API version, announce deprecation of the old version, contact remaining users of the old API, provide best effort support to users, and finally, deactivate the old version.
- B. Announce the old API version deprecation, introduce the new version, contact users still on the old version, deactivate the old version, and offer best effort support to old API users.
- C. Notify the deprecation of the old API version, contact remaining users of the old version, introduce the new version, deactivate the old version, provide best effort support, and finally, turn down the old version.
- D. Introduce the new API version, contact users still on the old API version, announce the deprecation of the old version, deactivate the old version, and provide best effort support to old API users.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Implement the new API version, announce deprecation of the old version, contact remaining users of the old API, provide best effort support to users, and finally, deactivate the old version.

**Correct option: A**

**Why option A is correct**

**A. Implement the new API version, announce deprecation of the old version, contact remaining users of the old API, provide best effort support to users, and finally, deactivate the old version.**

This sequence follows **Google-recommended API lifecycle and SRE best practices** for minimizing disruption to **external developers and dependent applications**.

Core fundamentals behind this approach:

  * **Backward compatibility first:** You must **introduce the new API version before deprecating the old one** , ensuring developers have a working alternative.

  * **Clear deprecation signaling:** Announcing deprecation early gives third-party developers sufficient time to migrate.

  * **Active communication:** Proactively contacting remaining users of the old API reduces surprise outages and helps identify blockers.

  * **Grace period + support:** Providing best-effort support during the deprecation window aligns with reliability and developer-experience principles.

  * **Controlled shutdown:** Only after adoption and communication should the old API be deactivated.

This is the standard **safe rollout → deprecation → migration → retirement** lifecycle.

**Documentation:**  
<https://cloud.google.com/apis/design/versioning>

**Why the other options are not suitable**

**B. Deprecates before introducing the new version.**  
This creates risk because users are warned before a viable replacement exists, increasing disruption and confusion.

**C. Contacts users and deactivates before a clear migration path exists.**  
This violates backward-compatibility expectations and can break third-party applications.

**D. Contacts users before formally announcing deprecation.**  
This leads to inconsistent messaging and does not follow a transparent, documented lifecycle process.

**Final answer:** **A**.

</details>

---

### Exam 5 · Q52

**You oversee an application operating within Google Kubernetes Engine (GKE) and employing the blue/green deployment approach. Portions of the Kubernetes manifests are provided below:**

**apiVersion: apps/v1**

**kind: Deployment**

**metadata:**

**name: green-app**

**labels:**

**app: my-app**

**version: green**

**\---**

**apiVersion: apps/v1**

**kind: Deployment**

**metadata:**

**name: blue-app**

**labels:**

**app: my-app**

**version: blue**

**\---**

**apiVersion: v1**

**kind: Service**

**metadata:**

**name: appservice**

**spec:**

**selector:**

**app: my-app**

**version: green**

**\---**

**apiVersion: networking.k8s.io/v1**

**kind: Ingress**

**metadata:**

**name: ingress-app**

**spec:**

**defaultBackend:**

**service:**

**name: appservice**

**The green-app Deployment was recently updated to incorporate a new application version. However, after the update, a substantial portion of user requests is failing, a behavior not observed during testing. Your task is to minimize the impact on users and facilitate developers in diagnosing the issue. What action should you take?**

- A. Update the Deployment blue-app to revert to the previous version of the application.
- B. Roll back the Deployment green-app to use the prior version of the application.
- C. Modify the selector on the Service appservice to app: my-app.
- D. Adjust the selector on the Service appservice to app: my-app, version: blue.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Adjust the selector on the Service appservice to app: my-app, version: blue.

**Given the scenario, the correct action to minimize the impact on users and facilitate developers in diagnosing the issue is:**

**D. Adjust the selector on the Service appservice to app: my-app, version: blue.**

**Justification:**

Adjusting the selector on the Service to target the blue version specifically would effectively route traffic only to the blue version of the application. Since the green version is experiencing issues after the recent update, directing traffic to the stable blue version ensures that users are not impacted by the failures in the green version. Meanwhile, developers can investigate the issue with the green version without disrupting user experience.

**Explanation for why other options are not suitable:**

**A. Updating the Deployment blue-app to revert to the previous version of the application:**

  * This option doesn't directly address the issue with the failing green version. Reverting the blue version won't resolve the problem with the green version, and it may introduce further complications.

**B. Rolling back the Deployment green-app to use the prior version of the application:**

  * While rolling back the green version would address the immediate issue, it may impact user experience as the application would revert to a potentially outdated version. Additionally, it doesn't provide developers with a controlled environment to diagnose the issue.

**C. Modifying the selector on the Service appservice to app: my-app:**

  * Modifying the selector to a generic value won't effectively route traffic to a specific version of the application. It doesn't address the need to isolate traffic from the failing green version while maintaining user experience with the stable blue version.

**References** :

[https://cloud.google.com/architecture/application-deployment-and-testing-strategies](https://cloud.google.com/architecture/application-deployment-and-testing-strategies  https://blog.devgenius.io/blue-green-deployment-with-kubernetes-b7595b17fe17)

[https://blog.devgenius.io/blue-green-deployment-with-kubernetes-b7595b17fe17](https://cloud.google.com/architecture/application-deployment-and-testing-strategies  https://blog.devgenius.io/blue-green-deployment-with-kubernetes-b7595b17fe17)

</details>

---

### Exam 5 · Q53

**You're managing an application on Google Cloud Platform (GCP) using Terraform. The application leverages a managed instance group for deployment on instances defined by an instance template. Your CI/CD pipeline deploys the Terraform code. When you attempt to update the machine type within the instance template via Terraform, the pipeline fails during the terraform apply stage, encountering the following error message:**

**Error waiting for deleting instance template: The instance_template resource 'project/demo-project/global/instanceTemplates/demo-instance-2024010000010001' is already being used by 'projects/demo-project/regions/us-central1/instanceGroupManagers/demo-mig'**

**Your objective is to update the instance template while minimizing disruptions to both the application and the CI/CD pipeline execution frequency.**

**What's the most appropriate course of action?**

- A. Delete the managed instance group entirely, then recreate it after updating the instance template.
- B. Introduce a new instance template, update the managed instance group to use this new template, and subsequently delete the old instance template.
- C. Eliminate the managed instance group from your Terraform state file, update the instance template, and then re-import the managed instance group.
- D. Employ the create_before_destroy meta-argument within the instance template's lifecycle block, setting it to `true`.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Employ the create_before_destroy meta-argument within the instance template's lifecycle block, setting it to `true`.

The best course of action in this situation is

**D. Employ the create_before_destroy meta-argument within the instance template's lifecycle block, setting it to true.**

Let's break down why this is the most suitable solution and discuss the other options:

**D. Employ the create_before_destroy meta-argument within the instance template's lifecycle block, setting it to true.**

  * **How it works:** create_before_destroy forces Terraform to create a new instance template (with the updated machine type) _before_ destroying the old template. This allows the managed instance group to seamlessly transition to the new resource, avoiding downtime.

  * **Advantages**

    * **Minimizes application disruption:** The managed instance group can continue serving traffic from the old instances while new ones with the updated machine type are spun up.

    * **Maintains CI/CD pipeline consistency:** Your pipeline won't need major modifications, allowing for smooth continuous deployment.

**Incorrect Options:**

  * **A. Delete the managed instance group entirely, then recreate it after updating the instance template.**

    * Too disruptive. This would delete all running instances, leading to significant application downtime.

  * **B. Introduce a new instance template, update the managed instance group to use this new template, and subsequently delete the old instance template.**

    * While less disruptive, it involves more manual steps and could cause temporary inconsistencies due to a mix of instance types.

  * **C. Eliminate the managed instance group from your Terraform state file, update the instance template, and then re-import the managed instance group.**

    * Risky – Managing resources outside of Terraform's control can lead to state inconsistencies. It's best to let Terraform handle resource lifecycles directly.

**Reference:**

<https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle#create_before_destroy>

</details>

---

### Exam 5 · Q56

**In the context of managing a high-priority workload on an autoscaled managed instance group within a single zone, with the need to validate alterations before finalizing changes and ensuring uninterrupted capacity for handling requests during testing, what is the recommended action to achieve this?**

- I. Modify autoscaling settings to "Only scale out" during the modification process.
- II. Transform the managed instance group to function across multiple zones.
- III. Temporarily disable autoscaling while implementing changes.
- IV. Enable predictive autoscaling to anticipate resource requirements.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Modify autoscaling settings to "Only scale out" during the modification process.

The recommended action to achieve uninterrupted capacity for handling requests during testing while validating alterations before finalizing changes on an autoscaled managed instance group within a single zone is:

**I. Modify autoscaling settings to "Only scale out" during the modification process.**

Explanation:

By modifying the autoscaling settings to "Only scale out" during the modification process, the managed instance group will only add new instances as needed to handle increased workload, ensuring uninterrupted capacity for handling requests. This approach allows you to validate alterations before finalizing changes while maintaining the necessary capacity to handle requests without interruption.

**Justification for why other options are not suitable:**

**II. Transform the managed instance group to function across multiple zones.**

  * While spreading instances across multiple zones can improve availability and fault tolerance, it doesn't directly address the need to ensure uninterrupted capacity during testing or the requirement to validate alterations before finalizing changes.

**III. Temporarily disable autoscaling while implementing changes.**

  * Disabling autoscaling may lead to capacity constraints during testing, potentially causing service interruptions or degraded performance. It's crucial to maintain autoscaling functionality to ensure the service can dynamically adjust to workload changes.

**IV. Enable predictive autoscaling to anticipate resource requirements.**

  * Predictive autoscaling can help anticipate resource requirements based on historical data, but it may not be suitable for ensuring uninterrupted capacity during testing or validating alterations before finalizing changes. Predictive autoscaling relies on historical patterns and may not accurately predict resource needs during testing or when making significant alterations to the workload.

**Reference:**

<https://cloud.google.com/compute/docs/autoscaler/managing-autoscalers>

</details>

---

### Exam 5 · Q58

**Your team has been alerted to a critical security vulnerability requiring a patch on Compute Engine instances serving millions of global customers. The goal is to swiftly deploy the security patch while minimizing costs and impact on end customers. What is the recommended course of action?**

- I. Perform a canary rollout of the security patch with a brief duration for testing.
- II. Simultaneously update all Compute Engine instances worldwide.
- III. Conduct a 24-hour rolling update during each region's overnight hours.
- IV. Implement an A/B rollout by duplicating all Compute Engine instances, applying the security patch to one set, and then transitioning users.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Perform a canary rollout of the security patch with a brief duration for testing.

**Choose I — start with a short-lived canary rollout of the patched instance template, verify that the first few VMs stay healthy, and then let the Managed Instance Group (MIG) updater finish rolling the patch out everywhere.**

  * Google Cloud’s MIG updater is designed for exactly this scenario: it lets you **canary a new template on a small slice of instances** (for example, 1-5 %) and, if health checks stay green, automatically continue to a full rollout. This gets the security fix into production much faster than a region-by-region schedule, yet still limits blast radius if something goes wrong. [cloud.google.com](https://cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups?utm_source=chatgpt.com) | [cloud.google.com](https://cloud.google.com/compute/docs/instance-groups?utm_source=chatgpt.com)

  * A canary update is markedly cheaper than running an entire duplicate fleet (the A/B pattern) and avoids the customer-visible risk of a simultaneous global restart. Google’s documentation calls canary deployment a **“progressive rollout that splits traffic between the existing and new versions before ramping up to 100 %.”** [cloud.google.com](https://cloud.google.com/deploy/docs/deployment-strategies/canary?utm_source=chatgpt.com)

  * Because this is a _critical_ vulnerability, waiting until each region’s overnight window (24 h) leaves too large an exposure window; a tight canary followed immediately by an automated rollout closes the gap quickly while still providing a safety valve.

**Why the other options are not ideal**

  * **II — update all instances at once:** fastest, but any unforeseen issue would take the whole service down simultaneously, violating high-availability principles. Google recommends staged rollouts (canary or rolling) rather than “all-at-once” for production MIGs. [cloud.google.com](https://cloud.google.com/compute/docs/release-notes?utm_source=chatgpt.com)

  * **III — 24-hour regional rolling update:** safer than II but too slow for an urgent fix; attackers could exploit the vulnerability in regions that have not yet been patched.

  * **IV — duplicate the fleet and do an A/B cut-over:** provides safety but **doubles VM cost** during the patch window and still requires a traffic switch. Google highlights canary updates as a lighter-weight alternative that meets the same safety goals without the extra spend. [cloud.google.com](https://cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups?utm_source=chatgpt.com)

In short, a brief canary rollout (option I) best balances **speed, safety, and cost** in line with Google’s recommended practices for managed instance groups.

</details>

---

### Exam 5 · Q61

**Your organization conducts numerous builds on Google Cloud daily. To protect against data exfiltration and ensure VMs lack public IP addresses, you aim to implement Google-recommended practices to create a customizable, easily-managed solution for your builds capable of scaling to your organization's needs. What action should you take?**

- A. Deploy private pools in Cloud Build with VPC service control.
- B. Configure and execute the builds in Cloud Build within a default pool to enforce necessary privacy measures.
- C. Create a build environment using Compute Engine VMs within a custom VPC, utilizing Jenkins to execute the builds.
- D. Establish a build environment using Compute Engine Spot VM instances within a custom VPC, employing Jenkins to execute the builds.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Deploy private pools in Cloud Build with VPC service control.

The best way to achieve your goals is 

**A. Deploy private pools in Cloud Build with VPC service control.** Here's why this aligns with Google's recommended practices:

  * **Security:**

    * **Private Pools:** Isolated environments prevent unauthorized access and data exfiltration.

    * **VPC Service Control:** Adds a layer of protection by restricting communication with Google services only within your designated perimeter.

  * **Scalability:** Cloud Build automatically scales worker nodes up and down within your private pool based on demand.

  * **Ease of Management:** Cloud Build's integrated solution reduces the overhead of managing infrastructure compared to custom setups.

  * **Customization:** Private pools offer flexibility for fine-grained configuration and security settings.

**Why Other Options Are Less Ideal:**

  * **B. Default Pools:** Lack the enhanced security and isolation provided by private pools.

  * **C & D. Custom Compute Engine VMs with Jenkins:**

    * **Management Overhead:** You become responsible for setting up, managing, and scaling the underlying infrastructure.

    * **Spot VM Risk:** While cost-effective, Spot VMs are preemptible and might disrupt builds.

**References:**

<https://cloud.google.com/build/docs/private-pools/private-pools-overview>

<https://cloud.google.com/build/docs/private-pools/using-vpc-service-controls>

<https://cloud.google.com/build/docs/private-pools/set-up-private-pool-to-use-in-vpc-network>

</details>

---

### Exam 5 · Q65

**Your code is hosted on GitHub and built using Cloud Build, both manually and via webhooks. Building the code requires accessing confidential information. To adhere to Google-recommended practices and protect the confidentiality of this information, what action should you take?**

- A. Initiate the builds from the command line each time, providing the necessary confidential information as parameters during the build process.
- B. Create an encrypted file within your GitHub repository containing only the confidential information, and reference this encrypted file within your Cloud Build configuration file.
- C. Store the confidential secrets in Secret Manager, specify the URI for the secrets within the Cloud Build configuration file, and reference the secret as parameters in the build steps.
- D. Maintain the code in GitHub and establish a separate repository within Cloud Source Repositories solely for storing confidential information. Reference this new repository within your Cloud Build configuration file.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Store the confidential secrets in Secret Manager, specify the URI for the secrets within the Cloud Build configuration file, and reference the secret as parameters in the build steps.

**The action that aligns with Google-recommended practices to protect the confidentiality of confidential information required during builds hosted on GitHub and built using Cloud Build is:**

**C. Store the confidential secrets in Secret Manager, specify the URI for the secrets within the Cloud Build configuration file, and reference the secret as parameters in the build steps.**

**Explanation:**

**Option C involves storing confidential secrets securely in Google Cloud's Secret Manager. Secret Manager provides a centralized and secure storage solution for sensitive information such as API keys, passwords, and other credentials. By storing confidential information in Secret Manager, you can ensure that it is encrypted at rest and accessible only to authorized users and services.**

In the Cloud Build configuration file, you can specify the URI for the secrets stored in Secret Manager and reference these secrets as parameters in the build steps. This allows Cloud Build to securely access the confidential information during the build process without exposing it in plaintext in the configuration files or build logs.

**Justification for why other options are not suitable:**

**A. Initiating the builds from the command line each time, providing the necessary confidential information as parameters during the build process.**

  * Manually providing confidential information as parameters during the build process introduces potential security risks, as the information may be exposed in plaintext in the command history or build logs. This approach is also not scalable and may not be suitable for automated builds triggered by webhooks.

**B. Creating an encrypted file within your GitHub repository containing only the confidential information, and referencing this encrypted file within your Cloud Build configuration file.**

  * While encrypting sensitive information within the repository can provide some level of protection, managing encryption keys and decryption mechanisms adds complexity and may not offer the same level of security as dedicated secret management solutions like Secret Manager. Additionally, storing encrypted files within the repository may still expose sensitive information to authorized repository users.

**D. Maintaining the code in GitHub and establishing a separate repository within Cloud Source Repositories solely for storing confidential information, referencing this new repository within your Cloud Build configuration file.**

  * While separating code and sensitive information into different repositories may provide some level of isolation, it does not offer the same level of security and centralized management as using Secret Manager. Additionally, managing multiple repositories for different types of information may increase complexity and administrative overhead.

**References:**

<https://cloud.google.com/build/docs/securing-builds/use-secrets>

<https://cloud.google.com/build/docs/configuring-builds/substitute-variable-values>

</details>

---
