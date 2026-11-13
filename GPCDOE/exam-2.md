# Professional Cloud DevOps Engineer — Practice Exam 2

60 questions.

## Question 1

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

Your organization packages its containerized applications using Helm, and your deployments depend on a mix of publicly hosted and internally maintained charts. Your security team has raised a concern that depending directly on a public Helm chart repository introduces risk. You want a single, uniform way to manage every chart that provides built-in access control and works with VPC Service Controls. What should you do?

- [x] A. Store both the public and private charts as OCI artifacts in Artifact Registry.
- [ ] B. Store both the public and private charts in GitHub Enterprise, using Google Workspace as the identity provider for authentication.
- [ ] C. Store both the public and private charts in a Git repository, use Cloud Build to synchronize the repository’s contents into a Cloud Storage bucket, and point Helm at that bucket as a chart repository using the https://[bucket].storage-googleapis.com/[helmchart] URL.
- [ ] D. Deploy a self-managed Helm chart repository server on Google Kubernetes Engine (GKE), using a Cloud Storage bucket as its storage backend.

### Explanation

**Correct Answer**

**A. Store both the public and private charts as OCI artifacts in Artifact Registry.**

**Exam Reasoning Explanation**

The must-have constraints are threefold: one uniform store for both chart types, _native_ (platform-managed) access control, and VPC Service Controls support. Walking requirement → capability: Helm 3+ can push and pull charts as OCI artifacts, and Artifact Registry’s Docker-format repositories natively store OCI artifacts — including Helm charts — so one repository type covers both public (re-hosted/mirrored) and private charts. Artifact Registry access is governed entirely through IAM, satisfying “native access control” without any extra identity layer. And Artifact Registry is a fully supported VPC Service Controls product, so the repository can sit inside a service perimeter. No other option satisfies all three constraints with a Google-managed, IAM-integrated, VPC-SC-eligible service.

**Key Exam Clues**

  * “references both public and private charts” — a hard constraint that the solution must handle both chart sources through one mechanism.

  * “using a public Helm repository as a dependency is a risk” — signals the fix should bring external dependencies under organizational control, not simply re-point to another external SaaS.

  * “manage all charts uniformly” — preference for a single, consistent storage model rather than a mix of tools.

  * “native access control” — excludes solutions that require bolting on a custom or third-party authentication/authorization layer.

  * “VPC Service Controls” — a hard technical signal: the destination must be a Google Cloud service with documented VPC-SC support, not a self-hosted workload or external SaaS product.

**Why This Is Correct**

Since Helm 3.8, Helm charts can be packaged and distributed as OCI artifacts, and Artifact Registry’s Docker-format repositories implement the OCI Distribution Specification, so they can store Helm charts the same way they store container images. Access to an Artifact Registry repository is controlled entirely by IAM roles and bindings — no separate auth system to build or maintain — which is exactly what “native access control” calls for. Artifact Registry is also one of the Google Cloud services with full VPC Service Controls integration, so the repository (and the organization’s private and locally-cached public charts inside it) can be placed behind a service perimeter to prevent unauthorized data exfiltration. This combination directly removes the security team’s concern: instead of pulling from a public Helm repository at deploy time, charts are pulled from a single governed, perimeter-protected registry.

**Why the Other Options Are Not the Best Fit**

**Option B — _Violates Requirement_**. GitHub Enterprise is a third-party SaaS product, not a Google Cloud resource, so it falls outside what VPC Service Controls can protect — service perimeters govern Google Cloud API access, not external platforms. Using Google Workspace as an identity provider addresses authentication, but that’s a federated-identity layer bolted on top of a third-party tool, not “native” access control on a Google Cloud artifact store, and it does nothing to satisfy the VPC-SC requirement.

**Option C — _Outdated / Technically Possible but Not Best_.** This is the classic pre-OCI Helm chart repository pattern (an index.yaml-based repo served over plain HTTPS from a public bucket URL). It adds a Cloud Build synchronization pipeline as extra moving parts (working against “manage uniformly”), and because Helm’s classic chart-repository protocol just performs HTTP GETs against that URL, access control isn’t natively enforced through IAM in the way Helm-to-Artifact-Registry authentication is — the bucket URL shown is a public-style endpoint, not an IAM-gated pull path.

**Option D — _Technically Possible but Not Best_.** Running your own chart repository server (e.g., ChartMuseum-style) on GKE means you now own patching, scaling, and — critically — building your own access-control layer in front of it, which is the opposite of “native access control.” A self-managed workload on GKE isn’t itself a VPC-SC-protected API resource the way a managed Artifact Registry repository is, so the security requirement isn’t met natively either.

**Exam Trap**

The trap is treating “native access control” and “VPC Service Controls” as if any Google Cloud-adjacent service (GKE, Cloud Storage via Cloud Build) automatically qualifies. Running infrastructure _on_ Google Cloud (Option D) or storing files _in_ a Cloud Storage bucket (Option C) is not the same as using a service with first-class IAM integration and documented VPC Service Controls support. If the question had not mentioned VPC Service Controls at all, Option C’s bucket-based approach might be a reasonable lower-effort answer for simple public/private separation — but the explicit VPC-SC requirement rules it out as written.

**Foundation Concept**

Since Helm 3, any OCI-compliant registry can serve as a Helm chart repository, which is why “Docker format” repositories in Artifact Registry can hold Helm charts alongside container images — OCI is a shared distribution protocol for both. When a Google Cloud exam question asks for “native” access control plus VPC Service Controls, read that as a cue to choose a managed Google Cloud service that is explicitly on the VPC-SC supported-products list, rather than a self-hosted workload or an external SaaS tool, however well-integrated that tool appears.

**Real-World Connection**

A platform team consolidates all Helm charts — including re-hosted copies of commonly used public charts — into one or more Artifact Registry repositories inside a service perimeter. The operational result is that every deployment pulls from a single, audited, IAM-governed source, eliminating the supply-chain risk of pulling directly from the public internet at deploy time, and giving security a single control point for access reviews and data-exfiltration prevention. The trade-off is an added step in the chart lifecycle: public charts must be deliberately mirrored into the registry (and kept up to date) rather than consumed live from upstream.

**Memory Hook**

“Helm 3 + OCI + Artifact Registry” = one managed, IAM-governed, VPC-SC-eligible home for every chart, public or private.

**30-Second Exam Takeaway**

When a question pairs “uniform chart/artifact management” with “native access control” and “VPC Service Controls,” look for the managed Google Cloud artifact store (Artifact Registry) over any self-hosted server or third-party SaaS — only a native, VPC-SC-supported service satisfies both the access-control and perimeter requirements at once.

**Official References**

[**Google Cloud — Manage Helm charts in Artifact Registry:**](https://docs.cloud.google.com/artifact-registry/docs/helm/manage-charts) Supports: Artifact Registry’s Docker-format repositories natively store Helm 3 charts as OCI artifacts, which is the mechanism behind the correct answer

[**Google Cloud — Protect Artifact Registry repositories in a service perimeter:**](https://docs.cloud.google.com/artifact-registry/docs/securing-with-vpc-sc) Supports: Artifact Registry’s full VPC Service Controls integration, which eliminates Options B and D

[Professional Cloud DevOps Engineer Exam Guide — Section 1.3, Designing a CI/CD architecture stack: ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment via the “Artifact Registry configuration” and “Security of CI/CD tooling” considerations

---

## Question 2

*Domain 2: Building and Implementing CI/CD Pipelines*

You’re building a CI/CD pipeline in Cloud Build that produces an application container image, with the source code hosted in GitHub. Company policy requires that production image builds run only against the main branch, and that the change control team must approve every push to the main branch. You also want the build itself to require as little manual intervention as possible. What should you do? (Choose two.)

- [ ] A. Create a Cloud Build trigger and set its repository event to Pull request.
- [ ] B. Add an OWNERS file to the trigger’s Included files filter.
- [x] C. Create a Cloud Build trigger and set its repository event to Push to a branch, scoped to the main branch.
- [x] D. Configure a branch protection rule on the main branch in the GitHub repository.
- [ ] E. Enable the manual Approval option on the Cloud Build trigger.

### Explanation

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

---

## Question 3

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You’re running a web application on a Compute Engine managed instance group, and Ops Agent is already installed on every instance. You’ve noticed suspicious activity coming from one particular IP address and need a way to see, in Cloud Monitoring, how many requests that IP address is generating — while keeping the operational overhead of the solution as low as possible. What should you do?

- [x] A. Add a logging receiver to the Ops Agent configuration to collect the web server’s access logs, then create a logs-based metric to count requests from the IP address.
- [ ] B. Write a custom script that scrapes the web server’s log files and pushes IP-address request counts to the Cloud Monitoring API.
- [ ] C. Modify the application code so it reports IP-address request counts directly to the Cloud Monitoring API.
- [ ] D. Add a metrics receiver to the Ops Agent configuration to collect web server metrics.

### Explanation

**Correct Answer**

**A. Add a logging receiver to the Ops Agent configuration to collect the web server’s access logs, then create a logs-based metric to count requests from the IP address.**

**Exam Reasoning Explanation**

The hard requirement is visibility into requests **from one specific IP address** , and the preference is **minimal operational overhead**. The decisive fact is that client IP addresses live in the web server’s access log entries, not in a predefined metric. Walking requirement → capability: to turn log content into something chartable in Cloud Monitoring, you need a logs-based metric, and to get the access logs into Cloud Logging in the first place without writing or running anything custom, you need Ops Agent’s logging receiver (a configuration change, not code or scripting). A metrics receiver, by contrast, only reports predefined metric sets (like connection counts) and has no concept of “count requests matching this IP.” That eliminates D on capability grounds and B/C on overhead grounds.

**Key Exam Clues**

  * “suspicious activity from a specific IP address” — a hard constraint: the solution must be able to isolate and count by an arbitrary field value (client IP) buried in log content.

  * “view the number of requests... in Cloud Monitoring” — the output must land in Monitoring as a chartable/alertable metric, not just remain as raw log entries.

  * “minimal operational overhead” — a decisive preference that eliminates any option requiring custom code, scripts, or ongoing maintenance.

  * “Ops Agent is installed on all instances” — a setup clue: the agent is already present, so the lowest-overhead path is a configuration change to that agent, not a new tool.

**Why This Is Correct**

Ops Agent’s logging receivers collect log files (such as a web server’s access log, which records the client IP for every request) and ship them to Cloud Logging. Once those log entries are in Cloud Logging, a user-defined logs-based metric can be created with a filter that matches the specific IP address; Cloud Logging then automatically maintains a counter-type time series from matching log entries, and that time series is directly visible and chartable in Cloud Monitoring. The entire solution is two configuration/filter changes — no code to write, deploy, or maintain, which is exactly what “minimal operational overhead” is asking for.

**Why the Other Options Are Not the Best Fit**

**Option B — _Technically Possible but Not Best_.** A custom scraping script could eventually get IP-level counts into Cloud Monitoring, but it means writing, deploying, scheduling, and maintaining a bespoke tool — the opposite of minimal operational overhead, and it duplicates functionality Ops Agent and Cloud Logging already provide natively.

**Option C — _Technically Possible but Not Best_.** Changing the application to self-report metrics works for data the app doesn’t already expose elsewhere, but here the needed data (client IP per request) is already captured passively in the access log. Modifying, testing, and redeploying application code to duplicate that is unnecessary effort and ongoing maintenance burden compared to a log-based metric.

**Option D — _Violates Requirement_.** A metrics receiver collects a fixed set of metrics exposed by the host or a supported application (for example, general request/connection counts), not an arbitrary dimension like “requests from IP X.” There’s no way to configure a metrics receiver to break down traffic by client IP, so it can’t satisfy the core requirement regardless of overhead.

**Exam Trap**

The trap is conflating “metrics receiver” with “a way to get request metrics.” Both A and D mention Ops Agent and both sound metric-related, but only logs carry the per-request client IP detail needed here — metrics receivers report aggregated, predefined values, not arbitrary field-level breakdowns from request data. Seeing “Ops Agent” and “metrics” in the same answer can tempt a quick read into D; the question’s real pivot word is “specific IP address,” which only log content (and therefore a logs-based metric) can filter on.

**Foundation Concept**

In Google Cloud’s observability stack, logs and metrics serve different purposes: metrics are numeric time series optimized for trends and alerting but are limited to whatever dimensions were defined in advance, while logs carry arbitrary structured or unstructured detail about each individual event. Logs-based metrics are the bridge between the two — they let you mine log content for a pattern (like a specific IP, error code, or user ID) and turn matches into a proper Cloud Monitoring time series, without having to predict that need when metrics were first designed.

**Real-World Connection**

A security or SRE team facing a suspected scraping or abuse pattern adds a filter-based logs-based metric for the offending IP, gets a chartable, alertable signal within minutes, and can later promote that same technique into a broader rate-limiting or WAF rule once the pattern is confirmed. The main trade-off is cost and scale: logs-based metrics are calculated from log volume, so a very high-traffic log stream with many ad hoc filters can add to logging ingestion costs — which is why they’re best used for targeted, investigative queries like this one rather than as a permanent high-cardinality metrics pipeline.

**Memory Hook**

“IP in the logs, not in the metrics” — when you need to slice by something only visible in raw log content, reach for a logs-based metric, not a metrics receiver.

**30-Second Exam Takeaway**

When a question asks to surface a value buried inside log content (an IP, a status code, a username) as a Cloud Monitoring metric with minimal effort, the answer is almost always “ingest the logs (via Ops Agent’s logging receiver) + create a logs-based metric” — never a metrics receiver, and never custom code unless the data literally doesn’t exist anywhere else.

**Official References**

[Google Cloud — Log-based metrics overview: ](https://docs.cloud.google.com/logging/docs/logs-based-metrics)Supports: how a logs-based metric filters log entries (such as those matching a specific IP) into a counter time series visible in Cloud Monitoring

[**Google Cloud — Configure the Ops Agent:**](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration) Supports: the distinction between logging receivers (which collect log files like web server access logs) and metrics receivers (which collect predefined metric sets), explaining why Option D cannot satisfy the requirement

---

## Question 4

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You’re setting up connectivity between Google Kubernetes Engine (GKE) clusters that live in separate VPCs, and you’ve found that nodes in Cluster A cannot reach nodes in Cluster B. You suspect the root cause is a network misconfiguration rather than an application issue. You need to pinpoint exactly which layer of the network path is failing, but you don’t have execute access into any workloads or nodes to run commands directly. What should you do?

- [ ] A. Install a toolbox container on a node in Cluster A, and use it to confirm that the routes to Cluster B are configured correctly.
- [x] B. Use Network Connectivity Center to run a Connectivity Test from a Cluster A endpoint to a Cluster B endpoint.
- [ ] C. Attach a debug container and run the traceroute command in both directions — from Cluster A to Cluster B and from Cluster B to Cluster A — to identify the point where the paths fail in common.
- [ ] D. Enable VPC Flow Logs in both VPCs and monitor the logs for packet drops.

### Explanation

**Correct Answer**

**B. Use Network Connectivity Center to run a Connectivity Test from a Cluster A endpoint to a Cluster B endpoint.**

**Exam Reasoning Explanation**

Two constraints decide this question: you need to identify the _specific layer_ where the path breaks (routing? firewall? forwarding rule?), and you explicitly cannot exec into any workload or node. Walking requirement → capability: anything requiring you to install, attach, or run something inside a container or on a node (A and C) fails the no-exec constraint outright, regardless of how useful the output would be. That leaves a choice between a static, hop-by-hop configuration analysis tool (B) and raw traffic telemetry (D). A Connectivity Test simulates the packet’s path through every relevant configuration layer — routes, firewall rules, forwarding rules, peering — and reports exactly which hop blocks it, without touching a single VM or pod. VPC Flow Logs, by contrast, record accepted-connection flow statistics at the NIC level and don’t inherently capture _why_ or _where_ a blocked packet was dropped, so they can’t reliably answer “which layer is broken” on their own.

**Key Exam Clues**

  * “identify the layer at which the network connectivity is broken” — a hard constraint requiring a tool that decomposes the path into discrete configuration layers, not just overall reachability.

  * “do not have execute access to workloads and nodes” — a hard exclusion constraint that eliminates any answer requiring exec, attach, SSH, or a debug/toolbox container running inside the cluster’s compute.

  * “suspect... due to the network configuration” — signals the tool should analyze configuration (routes, firewalls), not application behavior.

  * “different VPCs” — a technical anchor indicating the path likely crosses VPC boundaries (peering, routing, or a connectivity hub), which is exactly the kind of multi-hop scenario a path-analysis tool is built to evaluate.

**Why This Is Correct**

A Connectivity Test performs static (and, where applicable, dynamic) analysis of the configured network path between a source and destination, examining routes, firewall rules (VPC, hierarchical, and regional network firewall policies), and forwarding rules at each hop, then reports the specific point of failure — for example, “blocked by firewall rule X in VPC B” or “no valid route beyond this point.” None of this requires logging into a VM, exec’ing into a pod, or installing any tooling on the cluster’s nodes; it’s entirely a control-plane, configuration-level analysis. That makes it the only option that satisfies both the “identify the layer” requirement and the “no execute access” constraint at the same time.

**Why the Other Options Are Not the Best Fit**

**Option A — _Violates Requirement_. **Installing a toolbox container on a node and inspecting routes from inside it requires exactly the kind of node-level execute access the question says you don’t have. The approach might work technically, but it’s disqualified by the stated constraint before its usefulness is even relevant.

**Option C — _Violates Requirement_.** A debug container (whether attached to a pod or run against a node) still requires creating and executing a process within the cluster’s compute context to run `traceroute`. That’s execute-level interaction with workloads/nodes in all but name, so it fails the same constraint as Option A — and running it in both directions only adds more of exactly the access the scenario rules out.

**Option D — _Technically Possible but Not Best_. **VPC Flow Logs don’t require exec access, so they clear that bar, but they’re the wrong tool for the job as described. Flow Logs primarily report metadata about connections that were established (bytes, packets, 5-tuple) at the VM network interface; capturing why traffic was denied is the job of a separate feature, VPC firewall rules logging. Even with both enabled, you’d be inferring the failure layer indirectly from traffic patterns across two VPCs, rather than getting a direct, authoritative answer the way a Connectivity Test provides in a single targeted check.

**Exam Trap**

The sharpest trap in this question is the product name itself: the Connectivity Test capability actually lives under **Network Intelligence Center** , not **Network Connectivity Center** — the latter is a separate Google Cloud product for building hub-and-spoke connectivity (VPC spokes, VPN, Interconnect, router-appliance spokes) between networks. The two names are easy to swap under exam pressure. Learn to recognize the capability by what it does — simulate a path and report the failing configuration layer without touching any compute resource — rather than by memorizing the exact product name, since official practice material (and even real exam distractors) can blur the two.

**Foundation Concept**

Google Cloud networking troubleshooting splits into two broad approaches: configuration analysis (reasoning about what the network _should_ do, based on routes, firewall rules, and peering/hub configuration) and traffic observation (recording what actually happened to real packets, via Flow Logs or firewall rule logging). When you can’t execute commands inside the environment, configuration-analysis tools like Connectivity Tests become the primary diagnostic path, because they work entirely from the control plane’s view of how traffic _would_ flow, hop by hop, layer by layer.

**Real-World Connection**

A platform team with strict least-privilege policies — no engineer has SSH or `kubectl exec` rights into production nodes — runs a Connectivity Test the moment cross-cluster traffic breaks, gets an immediate answer such as “blocked by a firewall rule in the destination VPC,” and hands that to the owning team to fix, all without ever touching a live workload. The trade-off is that a Connectivity Test reasons about configuration and, in many cases, synthetic probe packets — it won’t catch an application-layer bug (like a misbehaving service inside a healthy, correctly-routed network path), so it complements rather than replaces application-level troubleshooting.

**Memory Hook**

No exec access + “which layer broke” = Connectivity Test (Network Intelligence Center), not Flow Logs and not a debug/toolbox container.

**30-Second Exam Takeaway**

Whenever a GKE or VPC networking question pairs “identify where in the path connectivity fails” with “no access to exec into VMs or pods,” the answer is a configuration-analysis path test — functionally, a Connectivity Test — never a debug container, toolbox pod, or raw flow-log monitoring.

**Official References**

[**Google Cloud — Network Intelligence Center overview:**](https://docs.cloud.google.com/network-intelligence-center/docs/overview) Supports: Connectivity Tests is described as a diagnostics tool for checking connectivity between network endpoints, and it is organized under Network Intelligence Center (clarifying the naming distinction flagged in the Exam Trap)

[Google Cloud — Connectivity Tests overview: ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview)Supports: the mechanism behind the correct answer — Connectivity Tests analyzes routes, VPC firewall rules, and regional/hierarchical firewall policies to assess reachability without requiring access to the endpoints themselves

[**Google Cloud — VPC firewall rules logging overview:**](https://docs.cloud.google.com/firewall/docs/vpc-firewall-rules-logging-overview) Supports: why Option D’s VPC Flow Logs alone are not the direct tool for identifying denied/dropped traffic, since logging denied connections is a distinct feature from Flow Logs

---

## Question 5

*Domain 2: Building and Implementing CI/CD Pipelines*

Your company operates a public Cloud Run service named `booking-engine`, accessible through HTTPS at https://booking-engine-abcdef.a.run.app.

Developers need to validate new revisions before those revisions receive customer traffic through the service’s standard URL. What should you do?

- [x] A. Deploy using `gcloud run deploy booking-engine --no-traffic --tag dev` and test the revision at https://dev---booking-engine-abcdef.a.run.app.
- [ ] B. Run `gcloud run services update-traffic booking-engine --to-revisions LATEST=1` and test through https://booking-engine-abcdef.a.run.app.
- [ ] C. Include the header supplied by `curl -H "Authorization:Bearer $(gcloud auth print-identity-token)"` when requesting https://booking-engine-abcdef.a.run.app to test privately.
- [ ] D. Grant developers `roles/run.invoker` on `booking-engine` and test through https://booking-engine-abcdef.private.run.app.

### Explanation

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

---

## Question 6

*Domain 5: Optimizing Performance and Cost*

You’ve built a serverless application on Cloud Run and deployed it to production. You want to understand the application’s resource utilization so you can make cost-optimization decisions. What should you do?

- [ ] A. Use Cloud Trace’s distributed tracing capability to monitor the application’s resource utilization.
- [ ] B. Use Cloud Profiler together with Ops Agent to monitor the application’s CPU and memory utilization.
- [x] C. Use Cloud Monitoring to track the application’s container-level CPU and memory utilization.
- [ ] D. Use Google Cloud Observability to create logs-based metrics that monitor the application’s resource utilization.

### Explanation

**Correct Answer**

**C. Use Cloud Monitoring to track the application’s container-level CPU and memory utilization.**

**Exam Reasoning Explanation**

The requirement is to see _resource utilization_ (CPU and memory) for a _Cloud Run_ service, in order to drive cost decisions, with the implicit preference of using what’s already available rather than adding tooling. Walking requirement → capability: Cloud Run is automatically and natively integrated with Cloud Monitoring, which already collects container CPU utilization and container memory utilization for every revision with zero setup. That single fact resolves the question — no agent to install, no code to instrument, no custom metric to build. The other three options each reach for a tool built for a different job (request-path latency, code-level hotspot profiling, or log-derived custom metrics) when the data needed is already a standard, built-in metric.

**Key Exam Clues**

  * “serverless application... Cloud Run” — a setup constraint: the solution should fit a fully managed environment where you don’t control or access underlying VMs.

  * “identify the resource utilization... for cost optimization” — a hard constraint: the goal is CPU/memory usage data specifically, not latency breakdowns or code-level hotspots.

  * “deployed to your production environment” — implies a solution that works passively, without modifying running application code.

  * Each distractor names a real Google Cloud tool, but tied to the wrong kind of signal (trace = latency, profiler = code hotspots, logs-based metrics = custom/derived data) rather than the native utilization metric itself.

**Why This Is Correct**

Cloud Run ships with built-in integration into Cloud Monitoring: as soon as a service or revision runs, metrics including container CPU utilization and container memory utilization are captured automatically and are visible both on the Cloud Run console pages and in Cloud Monitoring’s Metrics Explorer, with no agent installation or code changes required (since Cloud Run is fully managed, there’s no VM to install an agent on in the first place). Those exact metrics are what’s needed to judge whether a service’s configured CPU/memory allocation is over- or under-provisioned — the foundation of a cost-optimization decision for a serverless workload.

**Why the Other Options Are Not the Best Fit**

**Option A — _Different Use Case_.** Cloud Trace’s distributed tracing captures request latency as it flows through a request’s call graph — it tells you _where time goes_ , not how much CPU or memory a container is consuming. It’s the right tool for diagnosing slow requests, not for sizing compute resources.

**Option B — _Incorrect / Violates Requirement_. **Cloud Profiler is a continuous, statistical profiler that attributes CPU and memory _allocation_ to specific lines of application code, and it requires a language-specific profiling agent built into the application itself — not Ops Agent, which is a host-level telemetry agent installed on Compute Engine VMs (or similar hosts) to collect system logs and metrics. Cloud Run doesn’t expose the underlying VM for you to install Ops Agent on, so this pairing doesn’t apply to the scenario. Even where Cloud Profiler is used with Cloud Run, it’s aimed at code-level optimization, not service-level cost sizing.

**Option D — _Technically Possible but Not Best_.** Logs-based metrics are the documented way to derive _custom_ metrics from log content when the data you need isn’t already captured as a metric. CPU and memory utilization for Cloud Run are already first-class, built-in Cloud Monitoring metrics, so manufacturing them from logs would be redundant extra engineering effort for data that’s already available directly.

**Exam Trap**

The trap is picking a tool because it’s plausible for “observability” in general, without checking whether it produces the _specific_ data type asked for. Trace, Profiler, and logs-based metrics are all legitimate, frequently-correct answers in other Cloud Run observability scenarios — but here the question asks specifically for CPU/memory resource utilization, which is a metric Cloud Run already reports natively. If the question instead asked “which function in your code is consuming the most CPU,” Cloud Profiler would become the right answer; if it asked “where is latency being introduced across downstream calls,” Cloud Trace would be correct.

**Foundation Concept**

Think of Cloud Run’s observability stack as layered by question type: “is my service healthy and how much is it costing me to run” → built-in Cloud Monitoring metrics (CPU, memory, instance count, billable instance time); “where is time being spent across a request” → Cloud Trace; “which code path is hot” → Cloud Profiler; “what happened, in detail, for this one request” → Cloud Logging (and logs-based metrics when you need a custom aggregate from that detail). Resource-utilization-for-cost questions point straight at the first layer.

**Real-World Connection**

A team notices rising Cloud Run bills and opens the service’s Cloud Monitoring CPU and memory utilization charts; seeing memory consistently sitting far below the configured limit, they reduce the memory allocation per instance, which lowers the billable resource cost per request without touching application code. The trade-off to watch is under-provisioning: cutting CPU or memory too aggressively based on average utilization can cause cold-start slowdowns or out-of-memory errors under traffic spikes, so teams typically look at peak (not just average) utilization before resizing.

**Memory Hook**

“Resource utilization, no setup needed” — Cloud Run’s CPU/memory metrics are already in Cloud Monitoring by default; reach for Trace or Profiler only when the question is about latency or code hotspots instead.

**30-Second Exam Takeaway**

When a Cloud Run question asks for CPU/memory resource utilization — especially for cost decisions — default to Cloud Monitoring’s built-in container metrics; it requires no agent and no code changes, which beats any option that proposes extra tooling (Profiler, Trace, or custom logs-based metrics) to recreate data that’s already being collected.

**Official References**

[**Google Cloud — Monitor Cloud Run:**](https://cloud.google.com/run/docs/monitoring) Supports: Cloud Run is automatically integrated with Cloud Monitoring, and container CPU utilization and container memory utilization are built-in metrics requiring no setup

[**Google Cloud — Cloud Profiler documentation:**](https://cloud.google.com/profiler/docs) Supports: Cloud Profiler continuously attributes CPU usage and memory allocation to application source code via a language-specific profiling agent, distinguishing its code-level purpose (and agent model) from Ops Agent and from service-level resource-utilization monitoring

---

## Question 7

*Domain 3: Applying Site Reliability Engineering Practices*

Your team is writing a postmortem after an incident on your externally facing application. The team wants to improve its postmortem policy by adding triggers that indicate when an incident requires a postmortem. Based on Site Reliability Engineering (SRE) practices, which triggers should the policy define? (Choose two.)

- [ ] A. A request for a postmortem comes from an external stakeholder.
- [x] B. An incident results in data loss.
- [x] C. A request for a postmortem comes from an internal stakeholder.
- [ ] D. The monitoring system detects that an instance of your application has failed.
- [ ] E. The CD pipeline detects a problem with a release and automatically rolls it back.

### Explanation

**Correct Answer**

**B. An incident results in data loss.**

**C. A request for a postmortem comes from an internal stakeholder.**

**Exam Reasoning Explanation**

The decision method is to separate triggers that are defined in advance and objective from triggers that reflect the system working as designed. Google’s SRE guidance lists objective triggers such as user-visible downtime or degradation beyond a threshold, data loss of any kind, on-call engineer intervention, long resolution time, and a monitoring failure. It adds that any stakeholder may also request a postmortem. Option B matches the objective list directly. Options D and E describe automation succeeding (monitoring detecting a failure, a pipeline catching and reversing a bad release), which is the opposite of a failure that needs organizational learning. That leaves a stakeholder request as the second trigger, and the A versus C split is a scoping judgment explained in the Exam Trap.

**Key Exam Clues**

  * “triggers that indicate whether an incident requires a postmortem” is a hard constraint. You need criteria that can be defined before an incident, not reasons a postmortem would be useful.

  * “Based on Site Reliability Engineering (SRE) practices” is a hard constraint. The answers must align with Google’s published SRE criteria rather than general incident-management folklore.

  * “Choose two” is a cardinality instruction. The stem expects one objective trigger and one request-based trigger.

  * “external facing application” is context only. It describes who uses the application, not who can trigger the team’s own postmortem policy.

**Why This Is Correct**

Option B is the clearest match. Data loss of any kind is an explicit SRE postmortem trigger, because losing data is a serious, often irreversible failure even if the service recovers quickly. Option C reflects the SRE guidance that, beyond the objective triggers, any stakeholder may request a postmortem for an event. The two selections are independent triggers that work together. One is an objective criterion that fires without anyone asking, and the other is a request-based path that catches events the objective criteria miss. Together they cover the two mechanisms the SRE guidance describes: criteria defined before an incident, and stakeholder requests on top of them.

**Why the Other Options Are Not the Best Fit**

**Option A is _Technically Possible but Not Best_. **SRE guidance does say any stakeholder may request a postmortem, so an external request is not absurd. It loses to C because the policy is the team’s internal governance and postmortems are internal documents that contain operational detail. A request from outside the company would normally reach the team through an internal stakeholder such as support or management, who then request the postmortem.

**Option D is _Incorrect_.** The SRE trigger is a monitoring failure, meaning monitoring did not detect the problem and a person had to discover it manually. Here monitoring worked, and a single failed instance is routine in most managed deployments and is typically absorbed by redundancy without user impact.

**Option E is a _Different Use Case_**. The SRE trigger is on-call engineer intervention, such as a manual rollback or traffic reroute. An automated pipeline rollback is a control working as designed with no human intervention and no stated user impact. It is better handled by release-quality review than by a postmortem trigger.

**Exam Trap**

The weak point of this item is A versus C, so it is worth stating plainly. Google’s SRE text says “any stakeholder,” which does not distinguish internal from external, and this item’s key rests on that distinction. The defensible reading is that the policy is internal governance, so an internal stakeholder request is the one that belongs in it. Do not treat this as a rule that external requests are never honored. The stronger exam skill is rejecting D and E, which sound like incident signals but describe automation succeeding. The answer would change if the stem said an on-call engineer manually rolled back a release, because on-call intervention is a listed trigger.

**Foundation Concept**

A postmortem policy has two parts: objective criteria defined before an incident, and discretionary requests from stakeholders. Objective criteria remove debate about whether an incident was “big enough” and keep the practice blameless and consistent. Postmortems cost time, so triggers aim at events that carry learning value, such as user impact, data loss, human intervention, slow resolution, or failures of the detection system itself. Events that the system handled automatically and invisibly usually carry less learning value.

**Real-World Connection**

A team writes a policy that requires a postmortem for any data loss, any user-visible degradation past a set threshold, any manual intervention by on-call, and any incident where monitoring failed to alert, and lets managers or partner teams request one for anything else. The outcome is predictable triage: no one argues about whether to write one, and effort goes to incidents with real lessons. The trade-off is that too many triggers or low thresholds create postmortem fatigue, so teams tune thresholds as they learn what is worth the effort.

**Memory Hook**

Postmortems are triggered by failures (data loss, user impact, human intervention, slow fix, monitoring failure) or by a stakeholder request, not by automation doing its job.

**30-Second Exam Takeaway**

For SRE postmortem-trigger questions, pick the listed objective triggers such as data loss, user-visible impact, on-call intervention, long resolution time and monitoring failure, plus a stakeholder request. Reject options where monitoring or CI/CD automation simply worked as intended.

**Official References**

[Google SRE Book — Postmortem Culture: Learning from Failure: ](https://sre.google/sre-book/postmortem-culture/)Supports: the list of common postmortem triggers (including data loss of any kind) and the statement that any stakeholder may request a postmortem, which together justify Options B and C and eliminate D and E

[**Google Cloud Architecture Framework — Conduct thorough postmortems:**](https://docs.cloud.google.com/architecture/framework/reliability/conduct-postmortems) Supports: the recommendation to define postmortem criteria before an incident occurs, and the same set of objective triggers, including on-call interventions and monitoring failures

---

## Question 8

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

A third-party application requires a service account key in order to work. When you try to create the key in your project, you get an error saying the organization policy constraint iam.disableServiceAccountKeyCreation is enforced. You need to get the third-party application working while following Google-recommended security practices. What should you do?

- [ ] A. Enable the default service account key and download it.
- [ ] B. Remove the iam.disableServiceAccountKeyCreation policy at the organization level, then create a key.
- [ ] C. Turn off the service account key creation policy on the project’s parent folder, then download the default key.
- [x] D. Add a rule to the project’s organization policy that turns off the iam.disableServiceAccountKeyCreation constraint, then create a key.

### Explanation

**Correct Answer**

**D. Add a rule to the project’s organization policy that turns off the iam.disableServiceAccountKeyCreation constraint, then create a key.**

**Exam Reasoning Explanation**

There are two requirements in tension: the application needs a key, and the fix must follow Google-recommended security practice. Walking requirement → capability: the constraint blocks key creation, so something has to change before a key can exist, but the recommended practice is to treat keys as an exception and limit which projects can create them. The answer is therefore the narrowest exemption that still unblocks you, which is the single project that needs the key. Organization-wide and folder-wide changes lift the guardrail for many projects that never asked for it. Options A and C also rely on a “default key” that you cannot simply download.

**Key Exam Clues**

  * “needs to have a service account key to work properly” is a hard constraint. A keyless alternative is not available here, so a key must be created.

  * “following Google-recommended security practices” is a hard constraint. It points to the narrowest-scope, exception-based approach.

  * “when you try to export the key from your cloud project” is a scoping signal. The project is the unit that needs the exemption.

  * “organization policy constraint... is enforced” is a technical signal. The fix is to change that policy’s scope, not to work around it.

**Why This Is Correct**

Google’s guidance says to use organization policy constraints to limit which projects can create service account keys, and to treat key use as the exception rather than the norm. Organization policies inherit down the resource hierarchy and can be overridden at a lower level. Google’s own troubleshooting guidance for this exact error says that if a key is needed, you can disable the constraint for your project. Adding a rule to the project’s policy that turns off enforcement lets the one project create the key while every other project in the organization stays protected. Once the exemption exists, you can create the key, ideally with the gcloud CLI writing it directly to a secure location rather than leaving a copy in a downloads folder.

**Why the Other Options Are Not the Best Fit**

**Option A is _Incorrect_. **Service accounts have user-managed keys that you create and Google-managed keys that you cannot download, so there is no “default key” to enable and download. Nothing in this option changes the enforced constraint either, so key creation would still be blocked.

**Option B is _Violates Requirement_. **Removing the policy at the organization level would unblock you, but it removes the guardrail for every project in the company, which is the opposite of limiting key creation to the projects that need it. It is tempting because it is the most direct way to make the error disappear.

**Option C is _Incorrect_ on two counts. **Turning the policy off at the parent folder is wider than necessary and affects every project in that folder, and “download the default key” repeats the false premise of Option A. A key still has to be created after the policy allows it.

**Exam Trap**

The trap is choosing the most direct way to make the error go away (removing the constraint, Option B) instead of the narrowest compliant exception. The deciding word is “recommended”: Google prefers avoiding keys entirely, and when a key is unavoidable, exempting only the project that needs it. If the application could use workload identity federation, an attached service account, or impersonation instead, the better answer would be to avoid keys altogether, but the stem states a key is required. One further detail: the supplied error text had a typo in the constraint name, so the revised item uses the correct name, iam.disableServiceAccountKeyCreation. Google’s documentation also describes a newer managed variant, iam.managed.disableServiceAccountKeyCreation, and the legacy constraint name used here remains valid.

**Foundation Concept**

Organization policy constraints are inherited from organization to folder to project, and a policy set at a lower level can override the one above it. That makes scope the main design choice: apply restrictions broadly by default, then grant narrowly scoped exceptions with clear ownership. Google also supports finer exemptions using resource tags on individual service accounts, which is narrower than a project-level exemption. Service account keys are long-lived credentials that can leak, which is why they are restricted by default.

**Real-World Connection**

A security team enforces the key-creation constraint across the organization and handles each legitimate exception by exempting only the requesting project, then tracking that key’s owner and lifetime. The result is a small, auditable set of keys instead of keys scattered across every project. The trade-off is operational work, because each exception needs review, and the exempted project stays open to key creation until someone narrows it again. Teams usually pair exceptions with Cloud Audit Logs monitoring of key creation and with a plan to migrate to keyless authentication later.

**Memory Hook**

Need a key despite the constraint? Exempt the smallest scope that works, the project and not the organization or folder.

**30-Second Exam Takeaway**

When an organization policy blocks something you legitimately need, pick the narrowest-scope override on the resource that needs it. For service account keys specifically, Google’s order of preference is to avoid keys first, and when that is impossible, to exempt only the requesting project.

**Official References**

[Google Cloud — Best practices for managing service account keys: ](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys)Supports: using organization policy constraints to limit which projects can create service account keys, and treating key use as an exception, which is the reasoning behind Option D over B and C

[**Google Cloud — Troubleshoot organization policy errors for service accounts:**](https://docs.cloud.google.com/iam/docs/troubleshoot-org-policies) Supports: the exact error message in the stem, and the options to turn off enforcement for the organization or exempt a single project (or tagged service accounts), with the project-level exemption being the narrower choice

---

## Question 9

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your organization operates under strict regulatory requirements that mandate retaining all logs generated across the company for a period of seven years. You want to keep the logging architecture as simple as possible by relying on fully managed services, and you need to guard against any future gaps in log collection or accidental loss of stored logs caused by misconfiguration or human error. What should you do?

- [ ] A. Configure an aggregated Cloud Logging sink at the organization level that routes all logs to a BigQuery dataset.
- [x] B. Configure an aggregated Cloud Logging sink at the organization level that routes all logs to a Cloud Storage bucket governed by a seven-year retention policy with Bucket Lock enabled.
- [ ] C. Configure an individual Cloud Logging export sink in each project that routes that project’s logs to a BigQuery dataset.
- [ ] D. Configure an individual Cloud Logging export sink in each project that routes that project’s logs to a Cloud Storage bucket governed by a seven-year retention policy with Bucket Lock enabled.

### Explanation

**Correct Answer**

**B. Configure an aggregated Cloud Logging sink at the organization level that routes all logs to a Cloud Storage bucket governed by a seven-year retention policy with Bucket Lock enabled.**

**Exam Reasoning Explanation**

Two separate requirements are stacked here, and each one eliminates half the option set. The must-have constraint on _capture_ is “never miss future logs with minimal effort” — that points to sink **scope**. The must-have constraint on _storage_ is “logs cannot be deleted early, even by mistake, for seven years” — that points to storage **destination**. Walking it through: an organization-level aggregated sink automatically captures every current and future project under that node, so there’s no per-project step to forget (eliminates C and D). A Cloud Storage bucket with a locked retention policy makes the seven-year retention a property of the bucket itself, enforced by the platform rather than by a person remembering not to delete something (eliminates A and C again). Only B satisfies both constraints simultaneously.

**Key Exam Clues**

  * “store all organization logs” + “seven years” — a hard constraint on retention duration and scope (org-wide, not per-project).

  * “minimize logging infrastructure complexity by using managed services” — a preference that rules out hand-rolled or per-resource solutions in favor of a single managed construct.

  * “avoid any future loss of log capture... due to misconfiguration or human error” — this is the decisive phrase. It signals that the design must be self-enforcing (platform-guaranteed), not dependent on someone configuring things correctly every time.

  * “What should you do?” with four single-sentence options — single-select, best-fit question.

**Why This Is Correct**

An aggregated sink created at the organization level (with the “include children” behavior) automatically pulls in log entries from every project in the resource hierarchy, including projects created after the sink exists. That directly satisfies “avoid future loss of log capture” — there’s no manual step tied to onboarding a new project. Pointing that sink at a Cloud Storage bucket with a locked retention policy then satisfies the storage side: once the policy is locked, the retention period can only be increased, never reduced or removed, and the bucket itself cannot be deleted until every object has satisfied its retention period. That turns “seven years, guaranteed” into an enforced platform property rather than a process everyone has to follow correctly.

**Why the Other Options Are Not the Best Fit**

**Option A — _Technically Possible but Not Best_. **The organization-level aggregated sink correctly solves the capture problem, but BigQuery datasets don’t offer an equivalent of Bucket Lock: a dataset or table’s expiration settings can be changed or removed by anyone with the right permissions, so the “immune to misconfiguration or human error” requirement for the stored data is not met.

**Option C — _Violates Requirement_.** Per-project sinks require someone to remember to add a sink every time a new project is created; forgetting even one project means silent log loss, which is precisely the failure mode the question asks you to eliminate. It also inherits BigQuery’s lack of a retention lock.

**Option D — _Violates Requirement_.** The storage destination here is correct (Cloud Storage with a locked seven-year policy), but the sink scope is still per-project, so it carries the same capture-gap risk as Option C. A good storage choice doesn’t compensate for an architecture that can silently miss entire projects.

**Exam Trap**

The trap is evaluating the sink location and the storage destination independently instead of together. A candidate who only reads for “seven-year retention and Bucket Lock” might pick D because it has the right storage half; a candidate who only reads for “minimize complexity, avoid missing new projects” might pick A because it has the right scope half. The question requires both halves to be correct at once. If the requirement dropped “avoid future loss of log capture due to... human error” and only asked about immutable storage, a project-level sink (D) could become defensible for a single-project scope — but as written, org-wide guarantees are explicit.

**Foundation Concept**

Think of this as two independent axes: _where logs are collected from_ (sink scope: project vs. folder/organization, aggregated vs. per-resource) and _how logs are protected once stored_ (destination type and its immutability guarantees). Cloud Logging sinks solve the first axis; Cloud Storage retention policies plus Bucket Lock solve the second. BigQuery and Pub/Sub are valid sink destinations for analytics or streaming use cases, but neither offers an immutable, lockable retention guarantee comparable to Bucket Lock — so when a question emphasizes tamper-proof long-term retention, Cloud Storage with Bucket Lock is the Google-recommended pattern.

**Real-World Connection**

A compliance team configures exactly this pattern (org-level aggregated sink → Cloud Storage with a locked retention policy) once, centrally. The operational result is that no engineer anywhere in the company can shorten the retention window or delete the archive, intentionally or by mistake, and no new team can “forget” to wire up logging when they spin up a new project. The trade-off is reduced flexibility: once locked, the organization cannot even shorten retention later if a regulation changes, so the retention period is typically set conservatively and reviewed carefully before locking.

**Memory Hook**

“Org-wide capture, Storage for the lock” — aggregated sink at the org/folder level for guaranteed scope, Cloud Storage with Bucket Lock for guaranteed immutability.

**30-Second Exam Takeaway**

When a question combines “don’t miss future resources” with “don’t let anyone alter/delete this later,” look for an aggregated (org/folder-level) sink paired with a destination that offers a lockable retention guarantee — that’s Cloud Storage with Bucket Lock, not BigQuery or Pub/Sub.

**Official References**

[**Google Cloud — Aggregated sinks:**](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks) Supports: organization-level aggregated sinks automatically capture current and future child-resource logs, eliminating the per-project configuration risk in Options C and D

[**Google Cloud — Bucket Lock:**](https://docs.cloud.google.com/storage/docs/bucket-lock) Supports: locked retention policies cannot be reduced or removed and the bucket cannot be deleted until all objects meet the retention period, which is why Cloud Storage (Option B) is correct over BigQuery (Option A)

---

## Question 10

*Domain 3: Applying Site Reliability Engineering Practices*

Your organization wants to raise an application’s availability target from 99.9% to 99.99%, and the improvement would cost $2,000. The application currently generates $1,000,000 in revenue. You need to decide whether the higher availability is worth the investment over a single year of use. What should you do?

- [x] A. Calculate the value of the improved availability as $900, and conclude that the improvement is not worth the investment.
- [ ] B. Calculate the value of the improved availability as $1,000, and conclude that the improvement is not worth the investment.
- [ ] C. Calculate the value of the improved availability as $1,000, and conclude that the improvement is worth the investment.
- [ ] D. Calculate the value of the improved availability as $9,000, and conclude that the improvement is worth the investment.

### Explanation

**Correct Answer**

**A. Calculate the value of the improved availability as $900, and conclude that the improvement is not worth the investment.**

**Exam Reasoning Explanation**

This is a two-step decision: first find the value of the extra availability, then compare it with the cost. The value step comes from the SRE method of treating availability as a share of revenue, so the improvement is the difference between the two targets applied to annual revenue. The decision step is a straight comparison: spend more than the value gained and the investment loses money. Computing $900 and comparing it with the $2,000 cost settles the answer, and only option A pairs the correct value with the correct conclusion.

**Key Exam Clues**

  * “from 99.9% to 99.99%” is the calculation input. The improvement is the gap between the two targets, not either target on its own.

  * “current revenue is $1,000,000” is the calculation base. The value of availability is proportional to the revenue the service generates.

  * “for a single year of usage” is a hard constraint. The value ($900) and the cost ($2,000) are compared over the same one-year period.

  * “worth the investment” is the decision rule. Worth it only when the value gained exceeds the cost.

**Why This Is Correct**

Going from 99.9% to 99.99% availability is an improvement of 0.09 percentage points (99.99% − 99.9% = 0.09%). Applied to $1,000,000 of revenue, the incremental value is 0.0009 × $1,000,000 = $900. Google’s SRE guidance frames the same trade-off: if the cost of gaining one more nine is less than the incremental revenue, the investment pays off, and if it costs more, the cost exceeds the projected revenue gain. Here the cost of $2,000 is greater than the $900 value, so the improvement is not worth it for one year.

**Why the Other Options Are Not the Best Fit**

**Option B is _Incorrect_. **The $1,000 figure is a miscalculation, and it comes from treating the gain as 0.1% of revenue, which is the unavailability at the old target rather than the difference between the two targets. Its conclusion (not worth it) happens to be right, but the supporting number is wrong.

**Option C is _Incorrect_. **It combines the same wrong $1,000 value with the wrong conclusion. Even at $1,000, the investment would still cost twice what it returns.

**Option D is _Incorrect_.** The $9,000 figure comes from an order-of-magnitude slip, 0.9% rather than 0.09%, which makes the improvement look worth buying. It is tempting because it flips the decision, but the arithmetic does not support it.

**Exam Trap**

The trap is the decimal placement in the percentage difference. 99.99% − 99.9% is 0.09 percentage points, and it is easy to read as 0.1% ($1,000) or 0.9% ($9,000). If the revenue were $10,000,000 instead, the same improvement would be worth $9,000, which would exceed the $2,000 cost. The decision flips with revenue and cost, so always recompute both.

**Foundation Concept**

Each extra nine of availability costs more than the previous one but protects a smaller slice of revenue, so reliability has diminishing returns. SRE therefore treats availability targets as a business decision, not a technical goal to maximize. The value of an availability improvement is the revenue protected by the difference between the targets, and an investment makes sense only when that value exceeds the cost of reaching the target. The comparison should use the same time period for both sides.

**Real-World Connection**

A team weighing a multi-zone redesign multiplies the availability gain by the service’s annual revenue and compares it with the engineering and infrastructure cost before committing. When the value is smaller than the cost, they keep the current target and spend the error budget on feature work instead. The trade-off is that revenue is only part of the picture, because reputation, contractual penalties, and indirect effects can also matter, so teams use the calculation as a starting point rather than the final word.

**Memory Hook**

Value of an extra nine = the difference in availability (here 0.09%) × revenue; invest only if that value beats the cost.

**30-Second Exam Takeaway**

For availability-versus-cost questions, subtract the two targets, multiply by revenue to get the value, and compare it with the cost over the same period. Watch the decimal placement, because wrong answers are usually off by a factor of 10.

**Official References**

[Google SRE Book — Embracing Risk: ](https://sre.google/sre-book/embracing-risk/)Supports: the framing of availability in nines, the link between availability and revenue, and the principle that reliability investments should be weighed against the value they protect

[**Professional Cloud DevOps Engineer Exam Guide — Section 3.1, Balancing change, velocity, and reliability of the service:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment via “Defining SLIs (e.g., availability, latency), SLOs, and SLAs” and “Opportunity cost of risk and reliability (e.g., number of ‘nines’)”

---

## Question 11

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your application’s performance on Google Cloud has declined since the most recent release. You suspect that calls to downstream dependencies are making some requests take longer to complete, and you need to investigate the application to find the cause. What should you do?

- [ ] A. Set up Error Reporting in your application.
- [ ] B. Set up Google Cloud Managed Service for Prometheus in your application.
- [ ] C. Set up Cloud Profiler in your application.
- [x] D. Set up Cloud Trace in your application.

### Explanation

**Correct Answer**

**D. Set up Cloud Trace in your application.**

**Exam Reasoning Explanation**

The must-have constraint is diagnosing _slow requests_ caused by _downstream dependencies_ , which means the evidence needed is per-request timing broken down by the calls a request makes. Walking requirement → capability: only distributed tracing records a request as a tree of timed spans across service and dependency boundaries, so you can see which hop consumed the time. Error Reporting groups failures, Prometheus aggregates numeric metrics, and Profiler samples resource use inside a single process, so none of them attributes latency to a specific downstream call. That leaves Cloud Trace as the only tool built for this question.

**Key Exam Clues**

  * “performance... has degraded” and “take longer to complete” — a hard constraint pointing to latency, not errors or resource consumption.

  * “downstream dependencies” — a technical signal that the investigation must follow a request across service boundaries, which is the defining use case of distributed tracing.

  * “since the last release” — a contextual clue that you want to compare latency before and after the change, which trace data supports over time.

  * “investigate the issue with your application” — implies per-request, root-cause-level detail rather than an aggregate trend.

**Why This Is Correct**

Cloud Trace is a distributed tracing system that tracks request latency and helps you find performance bottlenecks across services. It records each request as a trace made of spans, so you can measure end-to-end latency, compare latency trends over time, and pinpoint which downstream dependency is causing delays. Instrumenting the application (OpenTelemetry is the recommended approach) lets Trace show where a slow request spent its time, such as waiting on a database call or another service, which is exactly the evidence needed to confirm or rule out the suspected dependency.

**Why the Other Options Are Not the Best Fit**

**Option A — _Different Use Case_. **Error Reporting aggregates and groups application error events by root cause, usually from stack traces or reported errors. A request can be slow without throwing any error, so a latency regression caused by a sluggish dependency may never show up there.

**Option B — _Technically Possible but Not Best_.** Managed Service for Prometheus collects and stores numeric metrics that you query with PromQL. If you had already exposed a latency histogram per dependency, it could show that something is slow, but it gives aggregate numbers rather than per-request, per-hop timing, and it requires you to define and emit those metrics yourself. It tells you that latency rose, not which call within a request caused it.

**Option C — _Different Use Case_. **Cloud Profiler continuously gathers CPU usage and memory-allocation data and attributes it to source code. That finds hot code inside your own process. Time spent waiting on a downstream dependency is mostly idle time, not CPU work, so a CPU or heap profile would largely miss it.

**Exam Trap**

The trap is treating every observability product as interchangeable “performance tooling.” Profiler sounds like the right fit for “performance degraded,” but it answers “which of my code consumes CPU or memory,” while the stem points to waiting on other services. If the question had said “CPU usage spiked after the release” or “which function is allocating the most memory,” Profiler would be correct; if it had said “the number of failed requests increased,” Error Reporting would fit better.

**Foundation Concept**

Match the telemetry signal to the question. Metrics tell you how much and how often (rates, utilization, aggregate latency), logs tell you what happened in a specific event, errors tell you what failed, profiles tell you where your own code spends CPU and memory, and traces tell you where a single request spent its time across components. A latency problem involving dependencies is a trace-shaped question because the answer is a timeline of calls.

**Real-World Connection**

After a release, an engineer opens Trace Explorer, filters to slow requests, and sees that most of the added time sits in one span for a call to an internal pricing service. That points the investigation at that dependency (or at how the new release calls it) instead of the application’s own code. The trade-off is that tracing needs instrumentation and context propagation through every service, and sampling means rare slow requests might not always be captured.

**Memory Hook**

Slow requests across dependencies means Trace; hot code means Profiler; failures means Error Reporting; numeric trends means metrics.

**30-Second Exam Takeaway**

When a question describes a latency regression and suspects downstream or dependent services, choose distributed tracing (Cloud Trace). Reserve Profiler for CPU and memory in your own code, Error Reporting for exceptions, and metrics services for aggregate numeric trends.

**Official References**

[**Google Cloud — Cloud Trace overview:**](https://docs.cloud.google.com/trace/docs/overview) Supports: Trace tracks request latency across services and helps pinpoint which downstream dependencies cause delays, which is why Option D is correct

[**Google Cloud — Error Reporting overview:**](https://docs.cloud.google.com/error-reporting) Supports: Error Reporting aggregates and groups error events by root cause, which distinguishes it from latency analysis (Option A)

[**Google Cloud — Cloud Profiler documentation:**](https://docs.cloud.google.com/profiler/docs) Supports: Profiler gathers CPU usage and memory-allocation data attributed to source code, which makes it a different use case from dependency latency (Option C)

---

## Question 12

*Domain 3: Applying Site Reliability Engineering Practices*

Your company runs an ecommerce website built from JVM-based applications in a microservice architecture on Google Kubernetes Engine (GKE). Traffic rises during the day and falls overnight. Your operations team currently runs enough Pods to cover the evening peak at all times. You want to automate scaling so that only the Pods and nodes needed for the current load are running. What should you do?

- [ ] A. Set up the Vertical Pod Autoscaler and leave the node pool at a fixed size.
- [ ] B. Set up the Vertical Pod Autoscaler and turn on the cluster autoscaler.
- [ ] C. Set up the Horizontal Pod Autoscaler and leave the node pool at a fixed size.
- [x] D. Set up the Horizontal Pod Autoscaler and turn on the cluster autoscaler.

### Explanation

**Correct Answer**

**D. Set up the Horizontal Pod Autoscaler and turn on the cluster autoscaler.**

**Exam Reasoning Explanation**

The requirement has two layers that both have to flex with the daily load curve: the number of Pods, and the number of nodes that host them. Walking requirement → capability: load that varies with time of day is a replica-count problem, so Pods should scale out and in, which is what the Horizontal Pod Autoscaler does. The cost saving only materializes if the nodes go away when the Pods do, and a fixed node pool keeps paying for peak capacity regardless of Pod count. That requires the cluster autoscaler to shrink and grow the node pool. Only option D covers both layers in the right way.

**Key Exam Clues**

  * “load increases during the day and decreases during the night” is a hard constraint. Demand swings up and down daily, which calls for scaling the number of replicas.

  * “run enough Pods to handle the evening peak load” describes the problem to remove, because capacity is sized for peak and wasted off-peak.

  * “only running enough Pods and nodes for the load” is a hard constraint. Both Pods and nodes must scale, so a static node pool is disqualified.

  * “microservice architecture” supports horizontal scaling, since stateless replicated services are the natural fit for adding and removing Pods.

**Why This Is Correct**

The Horizontal Pod Autoscaler changes the number of Pods in response to CPU or memory consumption or custom metrics, so replicas rise during the day and fall at night. The Horizontal Pod Autoscaler does not change the number of nodes in a GKE cluster, and Google’s documentation points to the cluster autoscaler for that job. The cluster autoscaler resizes a node pool between the minimum and maximum you set: when Pods can’t be scheduled it adds nodes, and when nodes are under-used and their Pods fit elsewhere it removes them. The two work as a chain, where replicas go up, pending Pods trigger new nodes, and the reverse happens as load drops, so you pay for only what the current load needs.

**Why the Other Options Are Not the Best Fit**

**Option A is _Different Use Case_.** The Vertical Pod Autoscaler adjusts the CPU and memory requests of individual Pods, which is aimed at steady-state right-sizing. Google’s guidance says to use the Horizontal Pod Autoscaler for workloads with sudden spikes in demand, and the fixed node pool means off-peak savings would never be realized.

**Option B is _Different Use Case_**. Adding the cluster autoscaler fixes the node side, but the Pod side still uses the Vertical Pod Autoscaler, which resizes Pods rather than changing replica counts. Right-sized Pods are still running around the clock, so the daily swing in load is not followed.

**Option C is _Technically Possible but Not Best_. **The Horizontal Pod Autoscaler reduces the number of running Pods at night, which is the right Pod-side choice. With a static node pool, though, the idle nodes keep running and billing, so you do not meet the requirement to run only the nodes you need.

**Exam Trap**

The trap is stopping after the Pod layer. Option C looks almost complete because the Horizontal Pod Autoscaler is correct, but the stem explicitly asks for “Pods and nodes,” so the node layer has to scale too. A second trap is treating the Vertical Pod Autoscaler as the general-purpose “autoscaling” answer. Vertical autoscaling would be the better fit if the load were steady but the Pods were over- or under-provisioned, and the question would then be about right-sizing rather than following a daily cycle.

**Foundation Concept**

Kubernetes autoscaling works in layers. Horizontal Pod autoscaling changes how many Pods run, vertical Pod autoscaling changes how much CPU and memory each Pod requests, and cluster autoscaling changes how many nodes exist to host them. The cluster autoscaler decides based on the resource requests of Pods, not their live utilization, which is why explicit resource requests on workloads matter. A cost-efficient design for variable load usually pairs Pod-level scaling with node-level scaling.

**Real-World Connection**

An ecommerce team sets a Horizontal Pod Autoscaler on its storefront Deployment and enables the cluster autoscaler on the node pool with sensible minimum and maximum sizes. Overnight the Pod count drops, nodes drain and are removed, and the bill shrinks. The trade-off is that scale-down can briefly disrupt Pods that are rescheduled to other nodes, so replicas should tolerate restarts, and scale-up has a short delay while new nodes start, so some headroom or a higher minimum may be needed for sudden traffic spikes.

**Memory Hook**

Horizontal for how many Pods, cluster autoscaler for how many nodes, and vertical for how big each Pod is.

**30-Second Exam Takeaway**

For GKE workloads whose load rises and falls over time and where both Pod and node costs matter, pick the Horizontal Pod Autoscaler together with the cluster autoscaler. Rule out any option that leaves the node pool static or that relies only on the Vertical Pod Autoscaler.

**Official References**

[**Google Cloud — About horizontal Pod autoscaling:**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) Supports: the Horizontal Pod Autoscaler scales the number of Pods with load, does not change the number of nodes, and relies on the cluster autoscaler for node scaling (Options C and D)

[**Google Cloud — About GKE cluster autoscaling:**](https://docs.cloud.google.com/kubernetes-engine/docs/cluster-autoscaler) Supports: the cluster autoscaler adds nodes when Pods can’t be scheduled and removes under-used nodes down to the node pool minimum, which is the node-layer scaling the question requires

[**Google Cloud — Vertical Pod autoscaling:**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler) Supports: the Vertical Pod Autoscaler is for analyzing and setting CPU and memory resources per Pod and for steady-state right-sizing, with horizontal autoscaling recommended for sudden spikes (Options A and B)

---

## Question 13

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You manage an application that runs on Compute Engine. The application uses a custom HTTP server to expose an API, and other applications reach that API through an internal passthrough Network Load Balancer. A firewall rule permits traffic to the API port from 0.0.0.0/0. You need Cloud Logging to record each IP address that accesses the API, using as few steps as possible. What should you do first?

- [ ] A. Enable Packet Mirroring on the VPC network.
- [ ] B. Install the Ops Agent on the Compute Engine instances.
- [x] C. Enable logging on the firewall rule.
- [ ] D. Enable VPC Flow Logs on the subnet.

### Explanation

**Correct Answer**

**C. Enable logging on the firewall rule.**

**Exam Reasoning Explanation**

The hard requirement is a record of every client IP that reaches the API, delivered to Cloud Logging. The preference is the fewest steps, and the stem asks what to do _first_. Walking requirement → capability: the API traffic already passes an ingress firewall rule, and a connection record from that rule contains the source IP and lands in Cloud Logging. The load balancer is a passthrough type, so backend VMs receive packets with the client’s original source address intact, which means the rule sees real client IPs. Turning on logging for that existing rule is one setting. The other options add infrastructure, depend on application behavior, or lose the “each IP” guarantee.

**Key Exam Clues**

  * “log each IP address that accesses the API” is a hard constraint. The record must carry the source IP of every accessing client, not a sampled view.

  * “fewest number of steps” is a hard preference. A single setting on an existing resource beats installing or deploying anything.

  * “A firewall rule permits traffic to the API port from 0.0.0.0/0” is a technical signal. An existing allow rule already matches this traffic, so logging can be switched on for it.

  * “internal passthrough Network Load Balancer” is a technical signal. Passthrough balancing leaves the client source IP unchanged at the backend, so the logged IP is the real client.

  * “custom HTTP server” is a technical signal. Nothing says it writes access logs, so you cannot rely on application logs for client IPs.

**Why This Is Correct**

When logging is enabled on a VPC firewall rule, Google Cloud creates a connection record each time the rule allows or denies traffic. Each record includes the source and destination IP addresses, protocol and ports, the connection time, and a reference to the rule that handled it. Those records are written to Cloud Logging, which is exactly the destination required. Because the existing rule allows the API port from 0.0.0.0/0, enabling logging on it captures each new client connection to the API. Internal passthrough Network Load Balancers deliver packets to backends with the original source and destination IP addresses unchanged, so the recorded source is the actual client. One boundary to keep in mind: firewall rules logging is connection-based and records only TCP and UDP connections, which is sufficient for an HTTP API.

**Why the Other Options Are Not the Best Fit**

**Option A is a _Different Use Case_.** Packet Mirroring clones full packets (headers and payloads) from instances and forwards them to collector instances behind an internal passthrough Network Load Balancer for inspection by security or monitoring tools. It requires a collector deployment and a policy, and it does not write IP records to Cloud Logging by itself. It is tempting because it can see every packet, but it is far more than “fewest steps.”

**Option B is _Technically Possible but Not Best_. **The Ops Agent can ship log files to Cloud Logging, but it only forwards what the application writes. The stem describes a custom HTTP server with no mention of access logging, so you would also have to make the server log client IPs and configure a logging receiver for that file, across every instance. That is many steps, and it depends on application behavior.

**Option D is _Technically Possible but Not Best_.** VPC Flow Logs also record IP addresses and write to Cloud Logging, but they sample packets (the primary sampling rate is dynamic and cannot be adjusted) and aggregate sampled packets over an interval into one entry per connection. That does not guarantee a record of each IP, and it is enabled per subnet, which covers far more traffic than the API port.

**Exam Trap**

The trap is choosing VPC Flow Logs (D) because “log IP addresses” sounds like its textbook use. The words “each” and “fewest steps” push away from a sampled, aggregated, subnet-wide feed and toward a connection record from the rule that already governs this traffic. The answer would change to D if the requirement were broader network analysis, such as traffic volume trends, top talkers, or visibility into protocols beyond TCP and UDP. It would change to B if the stem said the application already wrote access logs and you also needed request details such as paths or status codes.

**Foundation Concept**

Google Cloud gives several network visibility tools that answer different questions. Firewall rules logging records what a specific rule allowed or denied per connection. VPC Flow Logs provides sampled, aggregated flow statistics for subnets and other resources. Packet Mirroring copies full traffic to an analysis tool. Agent-based logging captures what applications write. Choosing among them means matching the evidence you need to the tool’s granularity, scope, and setup effort. Load balancer type also matters here, because passthrough balancing preserves the client address while proxy-based balancing would replace it.

**Real-World Connection**

A team investigating who is calling an internal API turns on logging for the ingress allow rule, then filters the resulting records in Logs Explorer by destination port to list the distinct client IPs. The result is immediate visibility with no deployment. The cost consideration is volume: logging a rule open to 0.0.0.0/0 on a busy port can generate many records and increase Cloud Logging charges, so teams review retention and exclusions. Existing long-lived connections that were already active when logging was enabled do not produce a new entry until they are re-established.

**Memory Hook**

Need the source IPs hitting a port you already allow? Turn on logging for the firewall rule that allows it.

**30-Second Exam Takeaway**

When a question asks for each client IP reaching a service with minimal effort, look for logging on the existing firewall rule rather than flow logs (sampled), Packet Mirroring (collector required), or agents (depends on application logging). Choose the broader tools only when the stem asks for network-wide analysis or other protocols.

**Official References**

[**Google Cloud — VPC firewall rules logging overview:**](https://docs.cloud.google.com/firewall/docs/vpc-firewall-rules-logging-overview) Supports: logging is enabled per firewall rule, records are connection records containing source and destination IPs, only TCP and UDP connections are logged, and records are viewed in Cloud Logging (Option C)

[**Google Cloud — VPC Flow Logs:**](https://docs.cloud.google.com/vpc/docs/flow-logs) Supports: flow logs sample packets, aggregate them by connection over an interval, and are enabled per subnet or wider scope, which is why they do not guarantee a record of each IP (Option D)

[**Google Cloud — Passthrough Network Load Balancer overview:**](https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer) Supports: backend VMs receive load-balanced packets with the original source and destination IP addresses unchanged, so logged source addresses are the real clients

[**Google Cloud — Packet Mirroring:**](https://docs.cloud.google.com/vpc/docs/packet-mirroring) Supports: Packet Mirroring clones traffic to collector instances behind an internal passthrough Network Load Balancer for inspection, which makes it a different use case from simple client-IP logging (Option A)

---

## Question 14

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

You’re building a CI/CD pipeline for an application that runs in your company’s multi-cloud environment. The application is deployed from custom Compute Engine images, and from the equivalent image types on the other cloud providers. You need a solution that can build these images and make them available in your current environment, and that will still work as your environment changes. Which solution stack should you use?

- [x] A. Cloud Build together with Packer.
- [ ] B. Cloud Build together with Cloud Deploy.
- [ ] C. Google Kubernetes Engine (GKE) together with Cloud Deploy.
- [ ] D. Cloud Build together with kpt.

### Explanation

**Correct Answer**

**A. Cloud Build together with Packer.**

**Exam Reasoning Explanation**

Two hard requirements decide this item: the deployable artifact is a custom VM image, and the same approach must work across several cloud providers and stay adaptable. Walking requirement → capability: you need an automation engine to run the pipeline and an image builder that targets many platforms from one definition. Cloud Build is the managed pipeline runner. Packer is the open source tool built to produce VM images for multiple platforms from a single source configuration, with a separate builder per cloud. Only option A has a component that actually builds VM images, so B, C and D fail on the first requirement.

**Key Exam Clues**

  * “custom Compute Engine images and the equivalent in other cloud providers” is a hard constraint. The artifact is a VM image, not a container image or Kubernetes manifest.

  * “multi-cloud environment” is a hard constraint. The tool must not be tied to a single provider’s image format.

  * “adaptable to future changes” is a preference. A vendor-neutral builder with per-cloud plugins fits better than a Kubernetes- or Google Cloud-specific tool.

  * “build and deploy the images” signals that the stack needs an image-building tool, since a pure delivery service would only cover the second half.

**Why This Is Correct**

Packer defines an image once in a template and uses platform-specific builders to produce matching images on each cloud. For Google Cloud, the googlecompute builder creates a Compute Engine image, and for other providers you add the corresponding builders to the same workflow. Cloud Build documents this pairing: a Packer community builder image runs `packer build` as a build step, and the resulting image appears in the Compute Engine Images page. Cloud Build supplies the triggers, managed execution and automation, and Packer supplies the multi-cloud image logic. If the company later adds or changes a provider, you add or swap a Packer builder rather than redesigning the pipeline. One prerequisite applies: the build service account needs permissions such as Compute Engine Instance Admin, plus Artifact Registry Writer if you store the Packer builder image there.

**Why the Other Options Are Not the Best Fit**

**Option B** , Cloud Build with Cloud Deploy, is a _Different Use Case_. Cloud Deploy is a continuous delivery service that promotes releases across targets, and its supported target types are GKE, Cloud Run and GKE Enterprise or attached clusters. It can be extended through custom targets, but that means writing your own deployment logic, and nothing in this pairing creates VM images for multiple clouds. It is tempting because Cloud Build plus Cloud Deploy is the standard Google Cloud CI/CD pairing.

**Option C,** GKE with Cloud Deploy, is _Violates Requirement_. GKE is a container orchestration platform, and the application here is deployed from VM images. This stack contains no image builder at all, and it ties the solution to Kubernetes rather than the multi-cloud VM-image workflow described.

**Option D,** Cloud Build with kpt, is a _Different Use Case_. kpt is a toolchain for managing, customizing and applying Kubernetes resource configuration packages, so it operates on Kubernetes manifests rather than VM images. It would be a sensible pairing for managing Kubernetes configuration, but not for producing Compute Engine images or their equivalents elsewhere.

**Exam Trap**

The trap is that Cloud Deploy, kpt and Packer all appear together in the exam guide’s CI/CD architecture objective, so any of them can sound plausible under time pressure. Cloud Deploy and kpt are Kubernetes- and Cloud Run-oriented, while Packer is the one that builds VM images across clouds. The answer would switch to B if the application were containerized and delivered through staged promotion across GKE or Cloud Run targets. It would switch toward kpt if the problem were managing and customizing Kubernetes configuration packages.

**Foundation Concept**

An image-based deployment pipeline has two separate jobs: _build the immutable artifact_ (a baked VM image) and _deliver it to an environment_. Different tools own each job, and the artifact type decides which tools apply. Container images and Kubernetes manifests point to Kubernetes-centric delivery tools, while baked VM images point to an image builder such as Packer. A vendor-neutral builder with per-cloud plugins is also what keeps a multi-cloud pipeline adaptable.

**Real-World Connection**

A platform team keeps one Packer template per application image in Git. A Cloud Build trigger runs the Packer build on each merge and publishes a new Compute Engine image to the current environment. When the company later adds another cloud, the team adds that provider’s builder to the same workflow rather than creating a second pipeline. The trade-off is operating the Packer builder yourself, because it is a community builder image that you build and store in Artifact Registry, and each additional cloud needs its own credentials and permissions.

**Memory Hook**

VM images across clouds means Packer, containers on Kubernetes means Cloud Deploy, and Kubernetes configuration packages means kpt.

**30-Second Exam Takeaway**

When a question describes baked VM images in a multi-cloud environment, choose Cloud Build running Packer. Cloud Deploy and kpt are the answers when the artifacts are containers or Kubernetes configuration.

**Official References**

[**Google Cloud — Building VM images using Packer:**](https://docs.cloud.google.com/build/docs/building/build-vm-images-with-packer) Supports: Packer creates identical VM images for multiple platforms from a single source configuration, and Cloud Build runs it through a Packer builder to produce Compute Engine images (Option A)

[**Google Cloud — Deploy to custom target types (Cloud Deploy):**](https://docs.cloud.google.com/deploy/docs/deploy-to-custom-targets) Supports: Cloud Deploy’s standard targets are GKE, Cloud Run and GKE attached clusters, with custom targets for anything else, which is why Options B and C do not fit a VM-image workflow

[**CNCF — Reintroducing kpt, your toolchain for infrastructure automation:**](https://cncf.io/blog/2026/07/02/reintroducing-kpt-your-toolchain-for-infrastructure-automation) Supports: kpt works on packages of Kubernetes Resource Model files, which is why Option D addresses Kubernetes configuration rather than VM images

---

## Question 15

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your company runs its services on multiple, globally distributed Google Kubernetes Engine (GKE) clusters. Your operations team has built workload monitoring on Prometheus-based tooling for metrics, alerts, and dashboards, but that setup has no way to view metrics across all clusters at once. You need a scalable solution that supports global Prometheus querying and keeps management overhead low. What should you do?

- [ ] A. Set up Prometheus cross-service federation to centralize data access.
- [ ] B. Set up workload metrics collection within Google Cloud Observability for GKE.
- [ ] C. Set up Prometheus hierarchical federation to centralize data access.
- [x] D. Set up Google Cloud Managed Service for Prometheus.

### Explanation

**Correct Answer**

**D. Set up Google Cloud Managed Service for Prometheus.**

**Exam Reasoning Explanation**

Three requirements decide this item. The solution must keep Prometheus-style tooling, give a single global query view across clusters, and cost little to operate. Walking requirement → capability: federation can aggregate data, but you still run and scale the Prometheus servers at every tier yourself. A managed Prometheus-compatible service removes that burden and exposes one global query endpoint, so existing Prometheus workflows keep working. Options that are self-operated or not built for cross-cluster querying fail the overhead or the global-view requirement.

**Key Exam Clues**

  * “global Prometheus querying” is a hard constraint. The answer must keep Prometheus-style querying (PromQL) and apply it across all clusters at once.

  * “minimize management overhead” is a hard preference. A managed service beats any design where your team runs and scales Prometheus servers.

  * “scalable” is a hard constraint. The design has to handle many clusters without redesign as the fleet grows.

  * “Prometheus-based tooling for metrics, alerts, and dashboards” is a technical signal. The existing tooling should carry over rather than be rebuilt.

**Why This Is Correct**

Google Cloud Managed Service for Prometheus gives you Prometheus with the global, multi-cloud, cross-project infrastructure of Cloud Monitoring behind it. Data lands in Monarch, the same globally scalable datastore Google uses for its own monitoring, so metrics from every cluster can be queried together with PromQL in Cloud Monitoring, Grafana, or any tool that calls the Prometheus query API. Collection is handled by managed collectors on GKE, which are automatically deployed, scaled, sharded, and maintained, and existing Grafana dashboards and PromQL-based alerts continue to work. That combination delivers the global view and low operational burden the stem asks for.

**Why the Other Options Are Not the Best Fit**

**Option A is a _Different Use Case_.** Cross-service federation lets one service’s Prometheus server pull selected series from another service’s server, so both datasets can be used together in a single server, for example combining service metrics with the cluster metrics of the platform they run on. It is not a design for rolling up many clusters into one global view, and it still leaves you running the servers.

**Option B is _Technically Possible but Not Best_.** Workload metrics collection within Google Cloud Observability for GKE sends metrics into Cloud Monitoring, which is globally scoped. It does not by itself give you the Prometheus-compatible collection and query path (PromQL through the Prometheus API, Grafana, rule evaluation) that the team’s existing tooling depends on, so it is a different and larger migration than the managed Prometheus service.

**Option C is _Technically Possible but Not Best_. **Hierarchical federation is the Prometheus project’s own pattern for scale: local servers hold detailed data and higher-level global servers pull aggregated series from them, which gives an aggregate global view. It meets the global-view and scale requirements, but you still deploy, size, secure, and operate every tier of Prometheus servers, which contradicts “minimize management overhead.”

**Exam Trap**

The trap is Option C, because hierarchical federation is the textbook open-source answer to “global view across many Prometheus servers” and it genuinely works. The deciding phrase is “minimize management overhead”: federation scales, but you operate it. The answer would flip to C if the requirement were to stay fully self-managed, for example for a policy against managed telemetry services. A second trap is picking B because “workload metrics” and “Google Cloud” sound native, when the question is specifically about keeping Prometheus-based querying and tooling.

**Foundation Concept**

Prometheus on its own is a per-server, local-storage system, so global views require either federation (pulling aggregated series upward through tiers) or a shared backend that all collectors write to. Federation keeps you in the operations business, while a managed backend moves storage, scaling, and cross-cluster querying to the provider and leaves you with collection and queries. Google Cloud Observability is the current name for the former operations suite, and Managed Service for Prometheus sits within it, using the same backend and APIs as Cloud Monitoring.

**Real-World Connection**

A platform team enables managed collection on each regional GKE cluster, points Grafana at the managed query endpoint, and reuses the PromQL dashboards and alert rules it already had. An SRE can then chart request rates across all regions in one query instead of logging into separate Prometheus servers. The trade-off is that cost shifts from running servers to per-sample ingestion charges, so teams watch metric cardinality and use filters or sampling intervals to control spend.

**Memory Hook**

Many clusters, one PromQL view, no servers to run: managed Prometheus beats federation.

**30-Second Exam Takeaway**

When a question asks for global Prometheus querying across clusters with minimal overhead, choose Google Cloud Managed Service for Prometheus. Federation (hierarchical for scale, cross-service for correlating services) is the self-managed alternative and carries operational burden.

**Official References**

[**Google Cloud — Google Cloud Managed Service for Prometheus:**](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) Supports: managed Prometheus built on the global Monarch datastore, with managed collection and global PromQL querying across clusters (Option D)

[**Prometheus — Federation:**](https://prometheus.io/docs/prometheus/latest/federation/) Supports: hierarchical federation scales Prometheus with higher-level servers pulling aggregated data from local servers, and cross-service federation lets one service’s server pull selected data from another’s, which distinguishes Options C and A

[**Google Cloud — Observability for GKE:**](https://docs.cloud.google.com/kubernetes-engine/docs/monitoring) Supports: GKE clusters send system metrics to Cloud Monitoring by default and can enable Google Cloud Managed Service for Prometheus, which frames the role of Option B relative to Option D

[**Professional Cloud DevOps Engineer Exam Guide — Section 4.1, Instrumenting and collecting telemetry:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment via “Collecting metrics (e.g., from applications, platforms, networking, Cloud Service Mesh, Google Cloud Managed Service for Prometheus, hybrid/multi-cloud environments)”

---

## Question 16

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You are creating Cloud Logging sinks that export log entries to BigQuery for later analysis. Your organization has a folder named Dev that contains development projects and a folder named Prod that contains production projects. Log entries from development projects must be exported to dev_dataset, and log entries from production projects must be exported to prod_dataset. You want to create as few log sinks as possible, and you want the sinks to apply to projects created in the future. What should you do?

- [ ] A. Create a single aggregated log sink at the organization level.
- [ ] B. Create a log sink in every project.
- [ ] C. Create two aggregated log sinks at the organization level, each filtering by project ID.
- [x] D. Create an aggregated log sink in each of the Dev and Prod folders.

### Explanation

**Correct Answer**

**D. Create an aggregated log sink in each of the Dev and Prod folders.**

**Exam Reasoning Explanation**

Three constraints work together. The logs must be split into two different datasets, the number of sinks must be minimal, and the sinks must automatically cover projects that do not exist yet. Walking requirement → capability: a sink routes to one destination, so two destinations require at least two sinks. The scope of each sink should follow how projects are already grouped, which is the folder. An aggregated sink attached to a folder routes the logs of the folder’s child projects, so new projects placed in that folder are covered without further configuration. That gives the minimum of two sinks with no maintenance, and only option D meets all three.

**Key Exam Clues**

  * “Dev... must be exported to dev_dataset, and Prod... to prod_dataset” is a hard constraint. Two destinations mean a single sink cannot do the job.

  * “minimize the number of log sinks” is a hard preference. A per-project design is ruled out, and two sinks is the floor.

  * “apply to future projects” is a hard constraint. Scope must be defined by hierarchy placement, not by a fixed list of project names.

  * “folder named Dev... folder named Prod” is a technical signal. The folders are the natural attachment points for aggregated sinks.

**Why This Is Correct**

Aggregated sinks let you combine and route logs generated by resources in an organization or folder to a central location. You create one with the folder as the parent and with children included, so log entries from projects inside the folder flow to the sink’s destination, and a BigQuery dataset is a supported destination. One sink on Dev pointing at dev_dataset and one on Prod pointing at prod_dataset yields exactly two sinks. A project created later inside either folder is a child of that folder, so its logs are routed without anyone touching the sink. Remember the prerequisites: the datasets must exist and be write-enabled, and each sink’s writer identity needs permission to write to its dataset.

**Why the Other Options Are Not the Best Fit**

**Option A is _Violates Requirement_. **A sink has a single destination, so one organization-level sink would send everything to one dataset and could not separate development from production logs. It is tempting because one sink is the smallest possible number, but it cannot satisfy the split.

**Option B is _Violates Requirement_.** A sink in each project multiplies the number of sinks and requires someone to create a new sink every time a project is added, which fails both “minimize” and “future projects.”

**Option C is _Technically Possible but Not Best_.** Two organization-level sinks match the minimum count, but filtering by project ID only matches the projects named in the filter. Each new project would require editing a filter, and filters are limited to 20,000 characters, so the design neither applies to future projects automatically nor scales cleanly. It is tempting because the sink count is the same as in D.

**Exam Trap**

The trap is the pair of answers that both look like they use the “minimum” number of sinks: A with one and C with two. A fails because one sink cannot feed two datasets, and C fails because project-ID filtering is a list of names rather than a rule that follows folder membership. The answer would change to A if all logs, development and production alike, were to go to a single dataset. It would change toward B only if the requirement were per-project isolation of log routing.

**Foundation Concept**

Log routing has two independent decisions: scope (which resources’ logs a sink sees) and destination (where matching logs go). Scope is set by where the sink is attached in the resource hierarchy, and aggregated sinks extend a sink’s reach to the resources below that node, including ones created later. Each sink has one destination, so the number of distinct destinations sets the minimum number of sinks. Filters refine what a sink matches but are a poor tool for expressing hierarchy membership.

**Real-World Connection**

A platform team attaches one sink to the Dev folder and one to the Prod folder, each writing to its own BigQuery dataset with partitioned tables. When a team spins up a new project in Prod, its logs appear in prod_dataset immediately, and analysts keep the two environments separate in permissions and cost. The trade-off is that sinks at a folder are broad, so noisy logs from every project in the folder flow to BigQuery unless exclusion filters are added to control volume and storage cost.

**Memory Hook**

One destination per sink, so two datasets mean two sinks, and attach each to the folder that holds the projects.

**30-Second Exam Takeaway**

When logs must be split across destinations and cover future projects, attach one aggregated sink per destination at the folder that contains the right projects. Avoid per-project sinks and project-ID filters, which do not follow the hierarchy.

**Official References**

[Google Cloud — Collate and route organization- and folder-level logs to supported destinations (aggregated sinks): ](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks)Supports: aggregated sinks route logs from the resources in a folder or organization to a destination, can be created with a folder as parent with children included, support BigQuery datasets, and filter by project only by naming it (Options D, A, and C)

[**Google Cloud — Route logs to supported destinations:**](https://cloud.google.com/logging/docs/export/configure_export) Supports: a log entry that matches a sink is routed to that sink’s destination, and the BigQuery destination dataset must be write-enabled, which explains why one sink cannot feed two datasets

[Professional Cloud DevOps Engineer Exam Guide — Section 4.2, Managing and analyzing logs: ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment via “Exporting and retaining logs (e.g., routing to BigQuery, Pub/Sub, Cloud Storage)”

---

## Question 17

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

Your organization uses Terraform to provision and manage infrastructure as code through a CI/CD pipeline. You observe that each time a configuration change is applied, an entirely new copy of the infrastructure stack is provisioned in your Google Cloud project rather than the existing stack being updated, resulting in duplicate resources and unnecessary spend. You need to ensure that the pipeline maintains exactly one instance of the infrastructure stack at all times, in line with Google-recommended practices. What should you do?

- [ ] A. Build an additional pipeline whose sole purpose is to identify and delete infrastructure stacks that are no longer required.
- [x] B. Verify that the pipeline reads and writes the terraform.tfstate file to and from Cloud Storage using Terraform’s gcs backend.
- [ ] C. Verify that the pipeline reads and writes the terraform.tfstate file to and from a source control repository.
- [ ] D. Modify the pipeline so that it tears down all existing infrastructure prior to applying the newest configuration.

### Explanation

**Correct Answer**

**B. Verify that the pipeline reads and writes the terraform.tfstate file to and from Cloud Storage using Terraform’s gcs backend.**

**Exam Reasoning Explanation**

Separate the hard constraint from the symptom first: the requirement is “exactly one stack at all times, Google-recommended practice” — not “clean up extra stacks” and not “guarantee freshness at any cost.” Work backward from the symptom: a brand-new stack appearing on every apply means Terraform has no memory of what it already created, which only happens when it can’t read a consistent, shared state file. That isolates the fix to state storage and rules out anything that reacts to duplicates after the fact (A), stores state somewhere unsafe for concurrent pipeline use (C), or avoids the problem by destroying everything every run (D). The decision converges on configuring a locked, remote backend — the `gcs` backend — so every pipeline execution sees the same state.

**Key Exam Clues**

  * “a new copy... is created each time a change... is made” — technical signal that Terraform is not recognizing prior resources, pointing at state visibility rather than a cleanup gap.

  * “ensure that only a single instance... exists at a time” — hard constraint that rules out reactive or destructive workarounds in favor of a practice that prevents duplication from happening at all.

  * “You want to follow Google-recommended practices” — exclusion signal: the answer must be the documented best practice, not merely a workaround that happens to achieve the stated goal.

  * “within a CI/CD pipeline” — preference/context clue: pipeline runs are typically ephemeral, which is exactly the condition under which unshared local state gets lost between runs.

**Why This Is Correct**

Terraform decides what to create, update, or leave alone by diffing your configuration against its state file, which maps configuration to real-world resource IDs. If that state lives only on the ephemeral pipeline runner’s local disk (or isn’t being reliably written back), each run starts from a blank slate and `terraform apply` concludes nothing exists yet — so it creates a full new stack. Configuring the `gcs` backend directs Terraform to read and write `terraform.tfstate` from a persistent Cloud Storage bucket on every run, and the backend also provides state locking, so concurrent or repeated pipeline executions converge on updating the one real stack instead of spawning another.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** A cleanup pipeline can reduce the cost impact of stacks that already exist, but it does nothing to stop the root cause, so new duplicates will keep appearing between cleanup runs. It’s an operational patch layered on top of a broken workflow, not the Google-recommended fix.

  * **Option C — Violates Requirement:** Source control is not a valid remote state backend. It offers no state locking, so overlapping pipeline runs can corrupt or desynchronize state, and committed state files commonly expose sensitive resource attributes in plaintext. This is a documented anti-pattern, and critically, state drifting between source control and reality is a plausible cause of the very symptom described — not a solution to it.

  * **Option D — Violates Requirement:** Destroying and recreating the entire stack on every deployment technically prevents duplicates, but at the cost of full service downtime and unnecessary resource churn on every change — the opposite of balancing delivery speed with reliability, and not how Google recommends operating persistent infrastructure with Terraform.

**Exam Trap**

The visible symptom — “multiple stacks exist” — pulls you toward a deletion/cleanup answer (A) because that directly addresses what you can see. The trap is treating the symptom as the problem instead of asking why Terraform keeps failing to recognize the stack it already built. If the scenario were changed so that state was already correctly centralized in a GCS backend but the team intentionally spins up ephemeral per-branch environments that pile up by design, a cleanup pipeline (A) would become the right answer instead.

**Foundation Concept**

Terraform’s state file is the single source of truth linking your `.tf` configuration to actual deployed resources. Whether separate executions of a pipeline “remember” prior infrastructure depends entirely on whether they share that same state consistently. A remote backend with locking (such as `gcs`) is what turns Terraform from a per-run, stateless tool into a safe, idempotent automation component for CI/CD.

**Real-World Connection**

A platform team wires `terraform apply` into Cloud Build on every merge to main but never adds a `backend` block. Every merge spins up a parallel, fully duplicated environment, multiplying compute and storage spend and leaving no clear “real” environment. Adding a `backend "gcs" {}` block pointing at a versioned, access-controlled bucket fixes the duplication immediately and, as a side benefit, protects against race conditions from two pipeline runs applying at once.

**Memory Hook**

No shared remote state means Terraform forgets what it already built, so every apply looks like day one.

**30-Second Exam Takeaway**

When a Terraform-driven pipeline keeps creating duplicate infrastructure instead of updating it, suspect the state backend first. Google’s recommended practice is a locked, remote GCS backend — not source control, and not a destroy-and-rebuild or after-the-fact cleanup workaround.

**Official References**

[**Google Cloud — Store Terraform state in a Cloud Storage bucket:**](https://docs.cloud.google.com/docs/terraform/resource-management/store-state) Supports: the correct-answer mechanism (why local/unshared state causes duplicate stacks, and how the gcs backend fixes it) and the elimination of Option C (source control is not the documented remote-state solution)

[Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide: ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment to Section 1.2, “Managing infrastructure,” which explicitly lists infrastructure-as-code tooling including Terraform

---

## Question 18

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

Your team runs workloads on three Google Kubernetes Engine (GKE) environments: development, staging, and production. Your GitHub repositories serve as the single source of truth for cluster configuration. You must keep all three environments consistent and, following Google-recommended practices, enforce and install a set of network policies and a logging DaemonSet across every cluster in these environments. What should you do?

- [ ] A. Use Cloud Deploy to roll out the network policies and the DaemonSet, and configure Cloud Monitoring to raise an alert whenever either one diverges from the configuration stored in the repository.
- [ ] B. Use Cloud Deploy to roll out the DaemonSet and Policy Controller to define the network policies, then rely on Cloud Monitoring to detect divergence from the repository and Cloud Run functions to remediate it.
- [x] C. Use Cloud Build to render and deploy the network policies and the DaemonSet, and configure Config Sync to keep the configurations of all three environments synchronized.
- [ ] D. Use Cloud Build to render and deploy the network policies and the DaemonSet, and configure Policy Controller to enforce the configurations across all three environments.

### Explanation

**Correct Answer**

**C. Use Cloud Build to render and deploy the network policies and the DaemonSet, and configure Config Sync to keep the configurations of all three environments synchronized.**

**Exam Reasoning Explanation**

Start by separating the hard constraints from the noise. The hard constraints are: Git is the source of truth, all three clusters must stay consistent, and the same resources (network policies and a DaemonSet) must be both installed and kept enforced. “Install and keep consistent from Git” is the GitOps pattern, so the decision reduces to asking which option contains a component that continuously reconciles cluster state to the repository. Option C does through Config Sync; A only notifies, B builds a bespoke remediation chain, and D uses a component built for admission control, not for installing resources. Requirement → capability → elimination → decision: Git-driven consistency → continuous reconciliation → Config Sync.

**Key Exam Clues**

  * “GitHub repositories as your source of truth” — technical signal for GitOps; the answer must pull configuration from Git and reconcile clusters to it.

  * “ensure that the three environments are consistent” — hard constraint requiring continuous convergence, not one-time deployment.

  * “enforce and install” — sequence/capability signal: the solution must both create the resources and keep them in place, which requires a reconciler.

  * “Google-recommended practices” — exclusion signal that disfavors custom drift-detection plumbing assembled from alerts and functions.

**Why This Is Correct**

Config Sync is the GitOps service included with GKE. It continuously monitors a central source of truth, such as a Git repository, and automatically reconciles each cluster’s state to match it. Pointing the dev, staging, and production clusters at the repository means the network policies and the logging DaemonSet are installed everywhere and any manual change or deletion is automatically reverted, which is exactly the consistency requirement. Cloud Build’s role in this option is the CI side: rendering the manifests (for example with Kustomize or Helm) so they can be committed or deployed as rendered output, while Config Sync handles the continuous delivery and drift correction.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** Cloud Deploy can deliver the manifests, and Cloud Monitoring can alert on divergence. It is tempting because it looks like a complete deploy-plus-observe loop. It loses because an alert only tells a human about drift after it happens; nothing enforces or restores the desired state, so consistency depends on manual intervention.

  * **Option B — Technically Possible but Not Best:** This adds automated remediation, which makes it look more complete than A. It loses on two counts: Policy Controller is an admission-control and audit engine built on Gatekeeper that validates or rejects requests against constraints, and is not the tool for installing network policy resources. The Monitoring-plus-Cloud Run functions drift-correction chain is also custom plumbing that duplicates what Config Sync does natively, so it is not the Google-recommended approach.

  * **Option D — Different Use Case:** Policy Controller is valuable for enforcing guardrails, such as rejecting noncompliant objects at admission time and auditing existing ones, so it is tempting for the word “enforce”. But it does not synchronize resources from Git or deliver a DaemonSet, so it cannot, on its own, guarantee that the required network policies and DaemonSet exist and match the repository across clusters.

**Exam Trap**

The strongest trap is Option D, because “enforce” maps naturally onto “Policy Controller”. The subtle distinction is that Policy Controller enforces what is allowed (admission and audit of constraints), while Config Sync enforces what exists and matches Git (reconciliation). If the question instead asked to prevent teams from creating Pods that violate a security standard, Policy Controller would become the right answer.

**Foundation Concept**

GitOps means the desired state lives in version control and an in-cluster agent continuously pulls and reconciles actual state to it, which makes drift self-healing rather than something to be detected and fixed by people. Policy engines and reconcilers solve different problems: a reconciler makes the cluster match a declared state, while a policy engine accepts or rejects changes against rules. Mature setups often combine them, with Config Sync delivering both workloads and the policy constraints themselves.

**Real-World Connection**

A platform team registers its dev, staging, and production clusters in a fleet and configures Config Sync to read a single repository with per-environment overlays. When an engineer manually deletes a NetworkPolicy in production during an incident, Config Sync restores it from Git automatically, and the change history for every policy lives in pull requests. The result is auditable, consistent security posture with far less operational toil than alert-and-fix workflows.

**Memory Hook**

Git as the source of truth plus “keep clusters matching it” means Config Sync; Policy Controller decides what is allowed, not what gets installed.

**30-Second Exam Takeaway**

When a question pairs a Git source of truth with consistency across multiple GKE clusters, look for Config Sync as the continuous reconciler. Treat Policy Controller as the admission and audit guardrail, and be wary of answers that rely on alerts or custom functions to handle drift.

**Official References**

[**Google Cloud — Config Sync overview:**](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview) Supports: the correct-answer mechanism (continuous reconciliation of clusters to a Git source of truth, drift prevention, and fleet-wide consistency) and the elimination of Options A and B

[**Google Cloud — Policy Controller overview:**](https://docs.cloud.google.com/kubernetes-engine/enterprise/policy-controller/docs/overview) Supports: the distinction that Policy Controller enforces constraints through admission control and auditing, which eliminates Option D as the mechanism for installing resources from Git

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment to Section 1.4, “Managing multiple environments,” which covers managing configuration and policy and managing GKE clusters across an enterprise

---

## Question 19

*Domain 2: Building and Implementing CI/CD Pipelines*

The latest version of your containerized application has passed testing and is ready for production on Google Kubernetes Engine (GKE). You were unable to fully load-test the new version in pre-production, so you need to make sure it does not introduce performance problems once it is deployed. The deployment must also be automated. What should you do?

- [x] A. Deploy through a continuous delivery pipeline that uses a canary deployment, watch for performance issues in Cloud Monitoring, and increase traffic to the new version as the metrics support it.
- [ ] B. Deploy through a continuous delivery pipeline that uses a blue/green deployment, move traffic to the new version, and watch for performance issues in Cloud Monitoring.
- [ ] C. Deploy with kubectl, use Config Connector to gradually shift traffic between the versions, and watch for performance issues in Cloud Monitoring.
- [ ] D. Deploy with kubectl with the spec.updateStrategy.type field set to RollingUpdate, watch for performance issues in Cloud Monitoring, and run the kubectl rollback command if any issues appear.

### Explanation

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

---

## Question 20

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

Your organization is building a CI/CD pipeline that deploys Google Cloud resources with Terraform. The CI/CD tooling runs on Google Kubernetes Engine (GKE), and each pipeline run executes in its own ephemeral Pod. You need to make sure that the pipelines running in these Pods hold the right Identity and Access Management (IAM) permissions to carry out the Terraform deployments, and you want to follow Google-recommended practices for identity management. Which two actions should you take? (Choose two.)

- [x] A. Create a Kubernetes service account, associate it with the Pods, and use Workload Identity Federation for GKE to authenticate as the Google service account.
- [ ] B. Generate a JSON key for the Google service account, save it as a Kubernetes secret, mount it into the Pods, and set the GOOGLE_APPLICATION_CREDENTIALS environment variable.
- [x] C. Create a Google service account and grant it the IAM permissions that the deployments require.
- [ ] D. Generate a JSON key for the Google service account, keep it in the CI/CD tool’s secret management store, and configure Terraform to authenticate with that key.
- [ ] E. Grant the required IAM permissions to the Google service account used by the Compute Engine VM instances that host the Pods.

### Explanation

**Correct Answer**

**A. Create a Kubernetes service account, associate it with the Pods, and use Workload Identity Federation for GKE to authenticate as the Google service account.**

**C. Create a Google service account and grant it the IAM permissions that the deployments require.**

**Exam Reasoning Explanation**

Identify the hard constraints: the workload is on GKE, Pods are ephemeral, and the identity approach must follow Google-recommended practice, which means no long-lived credentials. That eliminates anything built around exported service account keys (B, D). The remaining requirement is a least-privilege identity for the pipeline rather than a shared node identity, which eliminates E. For a multi-select item, check that the two answers are complementary rather than redundant: one creates and permissions the identity (C), and the other connects the Pods to it keylessly (A). Together they form the complete chain from Pod to Google Cloud IAM.

**Key Exam Clues**

  * “ephemeral Pod for each pipeline run” — technical signal: credentials must be obtained automatically at runtime, and nothing long-lived should be distributed to short-lived Pods.

  * “appropriate Identity and Access Management (IAM) permissions” — hard constraint: the identity must carry only the roles Terraform needs, which points to a dedicated, purpose-built service account.

  * “Google-recommended practices for identity management” — exclusion signal: service account keys and node-level identities are the documented anti-patterns on GKE.

  * “(Choose two.)” — cardinality instruction: the answer is a pair of steps that work together, not two alternatives.

**Why This Is Correct**

Option C establishes the identity: a dedicated Google service account, with just the IAM roles required for the Terraform deployments, is what the pipeline will act as, and it keeps those permissions separate from every other workload. Option A connects the Pods to that identity without any exported secret. With Workload Identity Federation for GKE enabled, a Kubernetes ServiceAccount assigned to the Pods is granted the ability to act as the Google service account (by impersonating it), and GKE exchanges the Pod’s identity for short-lived credentials automatically. The two options are interdependent: A has nothing to authenticate as without C, and C’s permissions are unreachable from the Pods without A. The set is complete because it covers identity creation, permission assignment, and keyless Pod authentication.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Violates Requirement:** It works technically and is tempting because it is a familiar pattern, but it relies on a long-lived exported JSON key. Keys are static credentials that can be leaked, copied, or left unrotated, and they are exactly what keyless mechanisms replace. Kubernetes secrets are only base64-encoded by default, which does not change that.

  * **Option D — Violates Requirement:** Moving the key into the CI/CD tool’s secret store improves storage slightly, but it is still a long-lived exported key requiring rotation and carrying leak risk. It also bypasses the native identity that GKE provides to Pods, so it is not the recommended practice.

  * **Option E — Technically Possible but Not Best:** Granting permissions to the node VMs’ service account does let the Pods obtain credentials via the metadata server, which is why it is tempting as the “no keys” choice. However, every Pod on those nodes would inherit the same broad permissions, which violates least privilege and blurs workload isolation. Workload Identity Federation for GKE exists specifically to give each workload its own identity.

**Exam Trap**

The most dangerous distractor is E, because it is keyless and therefore looks like it satisfies the “no keys” instinct. The distinction is scope: node-level identity is shared by all Pods on the node, while Workload Identity Federation for GKE scopes identity per Kubernetes ServiceAccount. If the scenario stated that the cluster was dedicated entirely to this one pipeline and per-workload isolation was not required, E would become a defensible choice.

**Foundation Concept**

Prefer short-lived, automatically issued credentials bound to a workload’s own identity over static secrets. On GKE, that means mapping a Kubernetes ServiceAccount to a Google Cloud identity so that the platform vouches for the Pod. Least privilege then comes from granting that dedicated identity only the roles its task requires. Note that Google’s current guidance also allows granting IAM roles directly to the Kubernetes ServiceAccount principal without impersonation, but the exam item asks for a Google service account, so the impersonation pattern in A and C is the matching approach here.

**Real-World Connection**

A platform team runs Terraform jobs as ephemeral Pods in a CI namespace. They create a dedicated Google service account with only the roles needed for the target projects, bind the job’s Kubernetes ServiceAccount to it, and deploy. There are no keys to rotate, no secrets to leak from the cluster, and audit logs attribute each Terraform change to a single, purpose-built identity, which simplifies incident review and permission tightening.

**Memory Hook**

On GKE, give each workload its own identity and let the platform issue short-lived credentials; never ship keys to Pods.

**30-Second Exam Takeaway**

For workloads on GKE that need Google Cloud access, choose Workload Identity Federation for GKE with a dedicated, least-privilege service account. Reject exported JSON keys, wherever they are stored, and reject node-level service accounts shared by every Pod.

**Official References**

[**Google Cloud — Authenticate to Google Cloud APIs from GKE workloads:**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) Supports: the correct-answer mechanism (A and C), covering how Workload Identity Federation for GKE lets Kubernetes ServiceAccounts access Google Cloud with granted IAM permissions and without keys, and why this is preferred over keys (B, D) and node-level identity (E)

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment to Section 1.1, “Designing the overall resource hierarchy for an organization,” which includes Identity and Access Management (IAM) roles and creating and managing service accounts

---

## Question 21

*Domain 2: Building and Implementing CI/CD Pipelines*

You need to build a CI/CD pipeline in Google Cloud for a containerized application. Your development team practices trunk-based development with a central Git repository. You want every new version of the application to pass through all of your tests in the pipeline so that quality improves. What should you do?

- [ ] A. First, install a Git hook that requires developers to run unit tests before pushing code to the central repository. Second, trigger Cloud Build to build the application container, deploy it to a testing environment, and run integration tests. Third, if the integration tests pass, deploy the container to production and run acceptance tests.
- [ ] B. First, install a Git hook that requires developers to run unit tests before pushing code to the central repository, and build a container if all tests pass. Second, trigger Cloud Build to deploy the container to a testing environment and run integration tests and acceptance tests. Third, if all tests pass, tag the code as production ready, then trigger Cloud Build to build and deploy the application container to production.
- [ ] C. First, trigger Cloud Build to build the application container and run unit tests using that container. Second, if the unit tests pass, deploy the container to a testing environment and run integration tests. Third, if the integration tests pass, have the pipeline deploy the container to production, then run acceptance tests.
- [x] D. First, trigger Cloud Build to run unit tests whenever code is pushed, and if all unit tests pass, build the application container and push it to a central registry. Second, trigger Cloud Build to deploy the container to a testing environment and run integration tests and acceptance tests. Third, if all tests pass, have the pipeline deploy the application to production and run smoke tests.

### Explanation

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

---

## Question 22

*Domain 2: Building and Implementing CI/CD Pipelines*

You are defining the deployment and testing approach for a CI/CD pipeline on Google Cloud. The approach you choose must satisfy two requirements:

  * It must simplify release deployments and keep the time needed to roll back a release as short as possible.

  * It must let you validate changes against real production traffic while progressively widening the share of users exposed to the change.

Which deployment strategy and testing strategy should you select?

- [ ] A. Recreate deployment combined with canary testing
- [x] B. Blue/green deployment combined with canary testing
- [ ] C. Rolling update deployment combined with A/B testing
- [ ] D. Rolling update deployment combined with shadow testing

### Explanation

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

---

## Question 23

*Domain 3: Applying Site Reliability Engineering Practices*

You operate a globally used service that has a 99% availability target, and your team has limited engineering capacity. For the current calendar month, measured availability is 99.5%. You need to keep the service within its defined availability goals while staying able to respond to business changes, including an upcoming launch of new features. You must also reduce technical debt and keep operational costs low, and you want to follow Google-recommended practices. What should you do?

- [ ] A. Provide N+1 redundancy for the service by provisioning additional compute capacity.
- [x] B. Identify, quantify, and eliminate toil by automating repetitive operational tasks.
- [ ] C. Establish an error budget for the service’s availability target and work to minimize the remaining error budget.
- [ ] D. Assign the available engineers to the feature backlog while making sure the service stays within its availability target.

### Explanation

**Correct Answer**

**B. Identify, quantify, and eliminate toil by automating repetitive operational tasks.**

**Exam Reasoning Explanation**

Separate the must-haves from the context. The context is that the service already beats its target, so reliability is not the problem. The must-haves are three simultaneous goals: keep meeting the target and absorb upcoming change, reduce technical debt, and minimize operational cost, all with few engineers. Test each option against all three, not just the first. An option that adds cost, or that uses the spare reliability headroom for something other than debt and cost reduction, fails a requirement. Only the option that converts engineering time into lasting automation satisfies all of them together.

**Key Exam Clues**

  * “99% target” versus “99.5% availability” — technical signal: the service is over-delivering, so the problem is not reliability and no new reliability spend is justified.

  * “limited engineering resources” — hard constraint: the chosen work must free capacity, not consume more of it ongoing.

  * “reduce technical debt while minimizing operational costs” — hard constraint: the answer must lower recurring effort and cost, which feature work or added infrastructure does not.

  * “react to business changes, including the upcoming launch” — preference: the team needs spare capacity and headroom for change, which comes from removing manual work.

**Why This Is Correct**

Toil is manual, repetitive, automatable operational work that scales with the service and brings no lasting value. Google SRE practice is to identify it, measure it, and eliminate it with engineering, keeping operational work below about half of each engineer’s time so the rest goes to projects that reduce future toil or add features. Automating toil directly reduces technical debt, lowers operating cost, and frees scarce engineers to support the launch, while the existing availability surplus gives the team room to invest in that automation safely. It satisfies every requirement at once, which none of the other options do.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** It is tempting because redundancy sounds like reliability protection ahead of a launch. But the service already exceeds its target, so extra capacity buys reliability nobody asked for while directly increasing operating cost, the opposite of what the question requires. It also does nothing about technical debt.

  * **Option C — Technically Possible but Not Best:** Error budgets are a core SRE tool, and the 99% target already implies a 1% budget, of which only half a point has been used this month. But the item asks for action on debt and cost, and “minimizing the remaining budget” would mean deliberately burning reliability headroom as an end in itself. Budgets govern how fast you may change things, not how you reduce toil or debt, so this does not solve the stated problem.

  * **Option D — Technically Possible but Not Best:** The surplus budget does permit feature velocity, which is why this is the most tempting distractor. However, it directs scarce engineers to new features and leaves technical debt and operational cost unaddressed, so it meets only the first goal and ignores the other two.

**Exam Trap**

The trap is reading “99.5% against a 99% target” as a signal to spend the error budget on feature work, which leads to Option D. The surplus budget describes what is safe to do, but the question’s explicit requirements are debt reduction and low operational cost, so the best use of limited engineers is toil elimination. If the question dropped those two requirements and asked only how to take advantage of the surplus, Option D would be the right answer.

**Foundation Concept**

An SLO defines acceptable reliability, and the gap between it and 100% is the error budget that can be spent on change and risk. Toil work is a separate lever: automation turns recurring human effort into a one-time engineering investment, which compounds by freeing capacity. Reliability work, feature work, and toil reduction compete for the same limited engineering time, so the right choice depends on which constraint the scenario emphasizes.

**Real-World Connection**

A small team notices it spends hours each week on manual certificate renewals, ad hoc capacity changes, and ticket-driven access grants. By measuring that time and automating those tasks, they cut recurring on-call and ticket load and shrink the manual surface that creates inconsistencies. When the feature launch arrives, they have engineers available and a simpler system to change, without having paid for extra infrastructure.

**Memory Hook**

When reliability already exceeds the target and the goals are less debt and lower cost, spend engineering time on removing toil, not on more capacity or more features.

**30-Second Exam Takeaway**

Read every stated goal in an SRE scenario, since the surplus-error-budget detail is a distraction when the question asks for debt and cost reduction. Choose toil elimination through automation when engineering capacity is limited and recurring manual work is the cost driver.

**Official References**

[**Google SRE Book — Eliminating Toil:**](https://sre.google/sre-book/eliminating-toil/) Supports: the correct-answer mechanism (defining toil, capping operational work at about 50 percent, and using engineering project time to reduce future toil), and the elimination of Options A and D as responses to debt and cost goals

[**Google Cloud Blog — Identifying and tracking toil using SRE principles:**](https://cloud.google.com/blog/products/management-tools/identifying-and-tracking-toil-using-sre-principles) Supports: the link between identifying, measuring, and reducing toil and lower operating costs, and the role of an SLO and error budget in deciding when to invest in automation (distinguishing Option C)

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment to Section 3, “Applying site reliability engineering practices,” covering balancing change, velocity, and reliability and managing the service lifecycle

---

## Question 24

*Domain 5: Optimizing Performance and Cost*

You are setting up the frontend tier of an application on Google Cloud. The frontend runs nginx on a managed instance group and sits behind an Envoy-based external Application Load Balancer. The entire application is deployed in the europe-west2 region and serves only users located in the United Kingdom. You need to pick the network tier and load balancing scope that minimize cost. Which combination should you choose?

- [ ] A. Premium Tier with a global load balancer
- [ ] B. Premium Tier with a regional load balancer
- [ ] C. Standard Tier with a global load balancer
- [x] D. Standard Tier with a regional load balancer

### Explanation

**Correct Answer**

**D. Standard Tier with a regional load balancer**

**Exam Reasoning Explanation**

Start with the requirement that drives cost: users and backends are all in one region, so nothing in the scenario needs global reach or Google’s global backbone. Then work through the two decisions in order. First, decide which tier is cheapest while still workable: Standard. Second, check which load balancer scope is actually available in that tier. Because the question specifies an Envoy-based load balancer, the global option is eliminated by tier compatibility, which leaves the regional option as the only valid cheapest combination.

**Key Exam Clues**

  * “most cost-effective” — hard constraint: the answer must optimize cost, which favors Standard Tier over Premium Tier.

  * “deployed entirely within the europe-west2 region” — technical signal: all backends are in a single region, so a global load balancer adds no value.

  * “only serves users based in the United Kingdom” — technical signal: there is no need for global anycast IPs or worldwide backbone ingress, and users are close to the region.

  * “Envoy-based external ... load balancer” — technical signal: the Envoy-based global external Application Load Balancer runs only in Premium Tier, which constrains valid pairings.

**Why This Is Correct**

Standard Tier is the cost-optimized tier: traffic enters and leaves Google’s network at a peering point near the region where the load balancer is configured, instead of riding Google’s global backbone. The regional external Application Load Balancer, which is Envoy-based, can be configured in either Premium or Standard Tier, and it serves backends from a single region, which matches this deployment exactly. Pairing it with Standard Tier gives the lowest-cost valid design for UK-only users in one region. One prerequisite to remember is that the regional external Application Load Balancer needs a proxy-only subnet in the region.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** A global external Application Load Balancer in Premium Tier works and would serve these users, which makes it tempting as the “default” choice. It loses because you would pay for global capabilities, such as anycast IPs and worldwide backbone ingress, that a single-region, UK-only application never uses.

  * **Option B — Technically Possible but Not Best:** A regional load balancer is the right scope, and it does run in Premium Tier, so it is a close second. It loses on the cost requirement because Standard Tier is available for the same load balancer and is the lower-cost tier, and nothing in the scenario requires Premium Tier’s performance.

  * **Option C — Incorrect:** This combination is not available for an Envoy-based global load balancer. Global external Application Load Balancers use global external IP addresses and global forwarding rules, which require Premium Tier, so it cannot be built even though it sounds cheapest. The classic Application Load Balancer can operate regionally in Standard Tier, but then it is not functioning as a global load balancer and is not the Envoy-based type the question describes.

**Exam Trap**

The trap is Option C, because “Standard Tier” pairs with the cost requirement and “global” pairs with the load balancer type, so the combination looks like the best of both. The distinction is that Standard Tier is regional only, so a global Envoy-based load balancer cannot use it. If the users were spread worldwide, had backends in multiple regions, or needed Cloud CDN, Premium Tier with a global load balancer would become the correct choice.

**Foundation Concept**

Network Service Tiers decide how traffic travels between the internet and your resources: Premium Tier uses Google’s global backbone for performance, while Standard Tier uses regular ISP networks to reduce cost. The tier also constrains which resources you can use, since global IP addresses and global load balancing require Premium Tier, whereas regional resources can use either. The general design rule is to buy global capability only when users or backends are actually global. Standard Tier trades some routing performance and feature breadth for lower cost, which is an acceptable trade when users sit near a single region.

**Real-World Connection**

A UK-focused retail site runs its nginx frontend in europe-west2 and creates a regional external Application Load Balancer using a Standard Tier regional IP address, plus the required proxy-only subnet. Because traffic enters near the London region and no global features are needed, networking costs stay low without changing the application. The team accepts that it has no global anycast address and cannot attach Cloud CDN, and it would move to Premium Tier only if the audience expanded internationally.

**Memory Hook**

One region and local users mean Standard Tier with a regional load balancer, because global load balancers require Premium Tier.

**30-Second Exam Takeaway**

When a question asks for the cheapest network tier and the workload and users are in a single region, choose Standard Tier with a regional load balancer. Check pairing validity first: any global load balancer or global IP in the Envoy-based family forces Premium Tier.

**Official References**

[**Google Cloud — Network Service Tiers overview:**](https://docs.cloud.google.com/network-tiers/docs/overview) Supports: the cost-versus-performance distinction between tiers and the fact that global external IP addresses and the global external Application Load Balancer require Premium Tier while regional resources can use Standard Tier (eliminating Option C and justifying D over B)

[**Google Cloud — External Application Load Balancer overview:**](https://docs.cloud.google.com/load-balancing/docs/https) Supports: the regional external Application Load Balancer being configurable in Premium or Standard Tier and serving a single region, and the global mode being Premium only (supporting D and eliminating A)

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment to Section 5.2, “Implementing FinOps practices for optimizing resource utilization and costs,” which lists infrastructure cost planning including network tiers

---

## Question 25

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your company’s Google Cloud resource hierarchy has separate folders for production, test, and development. The cyber security team is reviewing the organization’s Google Cloud security posture and wants to find and resolve security issues faster. You need to consolidate the logs generated by Google Cloud services across all projects that sit only within the production folder, so the team can configure alerting and perform near-real-time analysis. What should you do?

- [ ] A. Enable the Workflows API and direct all logs into Cloud Logging.
- [ ] B. Set up a central Cloud Monitoring metrics scope and add all relevant projects to it.
- [ ] C. Create an aggregated log sink on the production folder that routes to a Pub/Sub topic.
- [x] D. Create an aggregated log sink on the production folder that routes to a Cloud Logging bucket.

### Explanation

**Correct Answer**

**D. Create an aggregated log sink on the production folder that routes to a Cloud Logging bucket.**

**Exam Reasoning Explanation**

Split the requirement into three tests: scope (only production projects), content (logs, not metrics), and outcome (alerting and near-real-time analysis available without extra build-out). Apply scope first, since only a folder-level construct can bound the result to production. Then apply the content test, which removes anything that deals with metrics or unrelated services. Finally apply the outcome test to the remaining routing options: the destination that natively supports querying and alerting wins over a destination that merely transports data elsewhere.

**Key Exam Clues**

  * “only inside your production folder” — hard constraint: the collection point must be attached at the production folder so test and development projects are excluded.

  * “centralize the logs ... from all projects” — technical signal: points to an aggregated sink, which gathers logs from every child project in one routing rule.

  * “alerting and near-real time analysis” — hard constraint: the destination must support alerting and analysis on its own, without additional consumer infrastructure.

  * “logs generated by Google Cloud services” — exclusion signal: this is about log entries, which rules out metrics-focused or unrelated service options.

**Why This Is Correct**

An aggregated sink created on the production folder with child inclusion enabled routes matching log entries from every project in that folder to a single destination, and it does not touch the test and development folders. Choosing a Cloud Logging bucket as the destination keeps the logs inside Cloud Logging, where the security team can query them in Logs Explorer and configure log-based alerting policies, which meets the near-real-time analysis and alerting need with no additional pipeline. One prerequisite is that the sink’s writer identity must be granted permission to write to the destination bucket, and an inclusion filter can keep the bucket focused on security-relevant logs.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Incorrect:** Workflows is a service for orchestrating steps across services and has no role in collecting or aggregating logs. It is tempting because “route all the logs to Cloud Logging” sounds like centralization, but each project already writes to its own Cloud Logging, so nothing is consolidated and nothing limits the scope to the production folder.

  * **Option B — Different Use Case:** A metrics scope lets one scoping project view metrics from multiple monitored projects, which is valuable for cross-project dashboards. It is tempting because it uses a Cloud Monitoring construct that spans projects, but it consolidates metrics rather than log entries, so it does not meet the log-centralization requirement.

  * **Option C — Technically Possible but Not Best:** A Pub/Sub topic does receive the routed logs in a streaming fashion, which makes it tempting for “near-real-time.” However, it is only a transport layer: you would still need a subscriber, storage, and an analysis and alerting layer to make the logs useful, whereas a Cloud Logging bucket provides querying and alerting natively.

**Exam Trap**

The trap is Option C, because streaming through Pub/Sub sounds like the natural fit for near-real-time. The distinction is that Pub/Sub moves logs somewhere else, while a Cloud Logging bucket keeps them where alerting and analysis already work. If the security team’s analysis happened in an external SIEM that needed a streaming feed, a Pub/Sub destination would become the correct choice.

**Foundation Concept**

The Log Router evaluates sinks to send log entries to supported destinations such as log buckets, BigQuery datasets, Cloud Storage buckets, Pub/Sub topics, and other projects. A sink created at a folder or organization becomes an aggregated sink when it includes child resources, letting one rule collect from many projects. Destination choice decides what you can do next: buckets favor in-place analysis and alerting, BigQuery favors SQL analytics, Cloud Storage favors cheap archival, and Pub/Sub favors streaming to external systems.

**Real-World Connection**

A security team creates a dedicated logging project with a log bucket, then adds a folder-level aggregated sink on the production folder with child inclusion and a filter for audit and security logs. They grant the sink’s writer identity permission on the bucket and create log-based alerting policies for risky events such as IAM policy changes. New production projects are covered automatically, while test and development logs never enter the central bucket.

**Memory Hook**

Scope the sink to the folder, then pick the destination that matches what you need to do with the logs.

**30-Second Exam Takeaway**

For centralizing logs across many projects under one folder, use an aggregated sink on that folder with child inclusion. Choose a Cloud Logging bucket when the goal is in-place alerting and analysis, and choose Pub/Sub only when the logs must be streamed to an external consumer.

**Official References**

  * [Google Cloud — Collate and route organization- and folder-level logs to supported destinations (aggregated sinks): ](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks)Supports: the correct-answer mechanism (folder-level aggregated sinks with child inclusion, and the supported destinations including Cloud Logging buckets and Pub/Sub topics), and the elimination of Option A

  * [**Google Cloud — Metrics scopes overview:**](https://docs.cloud.google.com/monitoring/workspaces) Supports: the distinction that a metrics scope lets a scoping project view metrics from multiple monitored projects, which eliminates Option B for a log-centralization requirement

  * [**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment to Section 4.2, “Managing and analyzing logs,” which covers exporting and retaining logs by routing to destinations such as BigQuery, Pub/Sub, and Cloud Storage

---

## Question 26

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your organization needs to collect system logs from its Google Cloud project to power dashboards in Google Cloud Observability. You must configure every current and future Compute Engine instance to collect these system logs, and you must make sure the Ops Agent stays up to date. What should you do?

- [ ] A. Use the Google Cloud CLI to install the Ops Agent on each VM listed in Cloud Asset Inventory.
- [ ] B. On the Cloud Monitoring VM Instances dashboard, select every VM whose agent status is Not detected, then choose the option to install agents.
- [x] C. Use the Google Cloud CLI to create an agent policy.
- [ ] D. Use a startup script to install the Ops Agent on the Compute Engine image.

### Explanation

**Correct Answer**

**C. Use the Google Cloud CLI to create an agent policy.**

**Exam Reasoning Explanation**

Pull out the two lifecycle requirements: coverage must include VMs that do not exist yet, and the agent must be kept current over time. Both describe a continuously enforced desired state, not a one-time installation. Test each option by asking what happens to a VM created next month and to a VM running an outdated agent. Any option that acts only on the VMs present today, or only on a fixed image, fails one of the tests. Only the option that declares a project-level policy for current and future VMs passes both.

**Key Exam Clues**

  * “all current and future Compute Engine instances” — hard constraint: the mechanism must apply automatically to VMs created after setup, which excludes one-time actions against an existing list.

  * “ensure that the Ops Agent remains up to date” — hard constraint: requires ongoing lifecycle management of the agent, not just initial installation.

  * “system logs ... dashboards” — technical signal: the Ops Agent is the agent that collects logs and metrics from Compute Engine VMs for use in Google Cloud Observability.

  * “Use the Google Cloud CLI” — technical signal: agent policies are created through the `gcloud compute instances ops-agents policies` command group.

**Why This Is Correct**

An agent policy is a project-level definition that governs both existing and new VMs matching the criteria you specify, such as operating system, labels, or specific instances, and it automates installing and maintaining the Ops Agent. It builds on VM Manager’s OS Config capabilities, which keep applying the declared state, so a newly created VM that matches the policy receives the agent without anyone logging in. That satisfies the “current and future” requirement directly, and it is the mechanism Google provides for keeping the agent managed across a fleet. One prerequisite is that the OS Config agent must be present on the VMs, and it may need to be installed manually on older VMs.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** Looping over the VMs listed in Cloud Asset Inventory does install the agent, which is tempting because it is scriptable and covers the existing fleet. It loses because the inventory is a snapshot, so VMs created later are not covered, and the script installs at one point in time with no ongoing upgrade management.

  * **Option B — Technically Possible but Not Best:** The dashboard offers a convenient install action for VMs shown as Not detected. It loses on both lifecycle requirements: it is a manual, point-in-time action that does not reach future VMs, and VMs already running an older agent are not part of the Not detected set, so nothing keeps them current.

  * **Option D — Violates Requirement:** Baking the agent into the image covers only VMs created from that image, so VMs already running are untouched. It also freezes the agent version at the time the image was built, so the agent drifts out of date unless you keep rebuilding images and recreating VMs.

**Exam Trap**

The most tempting distractor is Option B, because it is the quickest visible fix and the dashboard states the problem directly. The distinction is that it remediates today’s gap, whereas the question demands a standing guarantee for future VMs and for currency. If the scenario asked only to fix a handful of existing VMs once, the dashboard install would become a reasonable answer.

**Foundation Concept**

Fleet management works best as declarative desired state: you state what every matching VM should have, and a control plane continuously reconciles reality to that state, rather than running imperative per-VM steps that go stale. Agent policies apply this idea to monitoring agents. For exam purposes, “current and future” plus “stay up to date” points to policy-based management. In production, check how upgrades are handled: Google’s documentation describes beta agent policies as able to upgrade the agent automatically, and for GA policies it points to OS Patch jobs for keeping the agent at the latest version.

**Real-World Connection**

A platform team creates an agent policy that selects VMs by label, so new application VMs inherit the Ops Agent automatically at creation. Because agent policies apply only to the zone they are created in, the team defines one per zone that hosts VMs. System logs then appear in Cloud Logging and feed dashboards without per-VM toil, and compliance can be reviewed from the OS policies page.

**Memory Hook**

“Current and future” plus “stays up to date” means a policy, not a per-VM action or an image.

**30-Second Exam Takeaway**

When a question requires agents on both existing and newly created VMs and asks that they be kept current, choose a policy-based, centrally managed approach such as an agent policy. Reject manual installs, inventory-driven scripts, and image baking, since each covers only a moment in time or only part of the fleet.

**Official References**

[**Google Cloud — Agent policies overview (Ops Agent):**](https://cloud.google.com/monitoring/agent/ops-agent/agent-policies-overview) Supports: the correct-answer mechanism (a policy governing existing and new VMs, built on VM Manager OS Config, created with the gcloud ops-agents policies commands) and the upgrade-handling nuance for beta versus GA policies

[Google Cloud — Installing the agent on individual VMs (VM Instances dashboard and agent status): ](https://docs.cloud.google.com/monitoring/agent/installation)Supports: the elimination of Option B, showing that the dashboard install acts on selected VMs and that Not detected status means an agent is missing or not running

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment to Section 4.1, “Instrumenting and collecting telemetry,” which includes collecting and importing logs using the Ops Agent

---

## Question 27

*Domain 3: Applying Site Reliability Engineering Practices*

Your team runs microservices on Google Kubernetes Engine (GKE). You want to detect when your error budget is being consumed so that you can protect customers and establish release policies. What should you do?

- [ ] A. Derive SLIs from metrics, and enable alerting policies to fire when the services fail to pass.
- [ ] B. Use the metrics from Cloud Service Mesh to gauge the health of the microservices.
- [x] C. Define an SLO, and create an alerting policy on select_slo_burn_rate.
- [ ] D. Define an SLO and set up uptime checks for your services, and enable alerting policies to fire when the services fail to pass.

### Explanation

**Correct Answer**

**C. Define an SLO, and create an alerting policy on select_slo_burn_rate.**

**Exam Reasoning Explanation**

Work through the dependency chain the question implies. An error budget exists only when an SLO sets a target, so the answer must include defining an SLO. Next, “detect consumption” is about how quickly the budget is being used, not whether a single check passed or failed, so the alerting signal must be a rate of consumption. Finally, “protect customers” favors an early warning before the SLO is breached. Apply those three tests in order, and only one option carries an SLO and an alert on the burn rate.

**Key Exam Clues**

  * “error budget” — technical signal: an error budget is derived from an SLO target, so an SLO must be defined and an SLI alone is not enough.

  * “detect consumption” — hard constraint: the alert must measure how fast the budget is being spent, which is the burn rate.

  * “protect customers” — preference: alerting on the rate of consumption warns before the SLO is violated, instead of after.

  * “define release policies” — technical signal: budget status gives an objective basis for deciding when to slow or pause releases.

**Why This Is Correct**

An SLO combines an SLI, a target, and a compliance period, and the error budget is the amount of failure the target permits. The burn rate describes how quickly that budget is being used, and Cloud Monitoring exposes it through the time-series selector `select_slo_burn_rate`, which takes the SLO and a lookback period. A sustained burn rate above one means the service will miss its SLO for that period. An alerting policy on this selector therefore notifies the team while there is still budget left, which protects customers, and the same signal gives an objective basis for release policies, such as slowing rollouts while the budget is burning fast. Google’s guidance recommends pairing a fast-burn alert with a slow-burn alert to cover both sudden and gradual consumption.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** SLIs are measurements, and alerting when services fail to pass reacts to threshold crossings on those measurements. It is tempting because SLIs are the foundation of reliability monitoring. But without an SLO target there is no error budget, so nothing can be detected as being consumed.

  * **Option B — Different Use Case:** Cloud Service Mesh telemetry gives visibility into service health, such as latency, traffic, and error rates, and it can be the data source for an SLI. It is tempting because it is native to GKE microservices. But raw health metrics have no objective or budget attached, so they do not detect consumption or inform release policy.

  * **Option D — Technically Possible but Not Best:** Defining an SLO is correct, but alerting when an uptime check fails is binary failure alerting on probe results. It is the closest distractor because it names both an SLO and alerting. It loses because the alert is not tied to the rate at which the error budget is being spent, so it does not give the early, proportional warning the question asks for.

**Exam Trap**

The trap is Option D, since “SLO plus alerting” looks like a complete answer. The subtle distinction is what the alert evaluates: a failed check says something is down now, while a burn-rate alert says the budget is being used up faster than the SLO can tolerate. If the question had asked to be notified as soon as an endpoint becomes unreachable, uptime-check alerting would be the better fit.

**Foundation Concept**

The reliability chain runs from SLI (what you measure) to SLO (the target for it) to error budget (the permitted failure) to burn rate (how fast that allowance is being used). Alerting on burn rate ties monitoring directly to the objective, rather than to arbitrary thresholds on symptoms, and it lets teams trade release velocity against reliability using a shared measure. This is why error budget status is used to decide when to ship and when to focus on stability.

**Real-World Connection**

A team defines an availability SLO for a checkout microservice over a rolling window, then creates a fast-burn alerting policy that pages on-call and a slow-burn policy that opens a ticket. Their release policy states that non-urgent rollouts pause while the fast-burn alert is active. Customers are protected because the team reacts to rapid budget loss early, and release decisions rest on an agreed measure instead of opinion. The cost is tuning thresholds and lookback windows so alerts stay actionable.

**Memory Hook**

The SLO sets the budget, and the burn rate shows how fast you are spending it, so alert on the rate.

**30-Second Exam Takeaway**

When a question asks how to detect error budget consumption, look for an SLO plus an alerting policy based on burn rate. SLIs alone, raw mesh metrics, and uptime-check failures do not tell you how fast the budget is being used.

**Official References**

[**Google Cloud — Alerting on your burn rate (Cloud Monitoring SLO monitoring):**](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/alerting-on-budget-burn-rate) Supports: the correct-answer mechanism (burn rate of the error budget, the select_slo_burn_rate time-series selector, and fast-burn and slow-burn alert types) and the elimination of Options A and D

[**Google Cloud — Design service level objectives (Cloud Service Mesh):**](https://docs.cloud.google.com/service-mesh/docs/observability/design-slo) Supports: how SLIs, SLO targets, compliance periods, and error budgets fit together for services running on GKE with Cloud Service Mesh, which distinguishes Option B

[Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide: ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment to Section 3.1, “Balancing change, velocity, and reliability of the service,” which covers defining SLIs, SLOs, and SLAs and managing error budgets

---

## Question 28

*Domain 2: Building and Implementing CI/CD Pipelines*

Your organization requires a change advisory board (CAB) to approve every change made to an existing service. You want to redesign this process so that it no longer has a negative effect on software delivery performance. Which two actions should you take? (Choose two.)

- [ ] A. Replace the CAB with a senior manager who provides continuous oversight from development through deployment.
- [ ] B. Allow developers to merge their own changes, provided the team’s deployment platform can roll back changes if problems are found.
- [x] C. Adopt a peer-review-based process for individual changes that is enforced at code check-in and backed by automated tests.
- [ ] D. Group changes into larger, less frequent software releases.
- [x] E. Make sure the team’s development platform gives developers fast feedback on the impact of their changes.

### Explanation

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

---

## Question 29

*Domain 2: Building and Implementing CI/CD Pipelines*

Your organization is developing and releasing a microservice on Cloud Run that many internal applications depend on. You are shipping a new release and must test it thoroughly in both the staging and production environments, while keeping the impact on service consumers and on developers as low as possible. What should you do?

- [ ] A. Deploy the new release to the staging environment and split traffic so that 1% reaches the latest version. Run your tests against it. If they succeed, progressively roll the latest version out to both the staging and production environments.
- [ ] B. Deploy the new release to the staging environment and split traffic so that 50% reaches the latest version. Run your tests against it. If they succeed, route all traffic to the latest version, then repeat the process in the production environment.
- [x] C. Deploy the new release to the staging environment with a new-release tag and no traffic assigned. Run your tests against the tagged version. If they succeed, progressively roll out the tagged version, then repeat the process in the production environment.
- [ ] D. Create a new environment tagged green to serve as the staging environment and deploy the new release there for testing. If the tests succeed, route all traffic to the green environment and delete the existing staging environment, then repeat the process in the production environment.

### Explanation

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

---

## Question 30

*Domain 2: Building and Implementing CI/CD Pipelines*

Your team recently moved an application onto Google Kubernetes Engine (GKE) and is now preparing to ship an updated version. The release approach must let you revert to the earlier version immediately if the update proves faulty. Which deployment model fits best?

- [ ] A. Roll out the update with a rolling deployment, then run tests on the new application after the rollout completes.
- [ ] B. Use A/B testing, and run tests on the application at regular intervals after the rollout completes.
- [ ] C. Use a canary deployment, and test the new application at regular intervals after the new version is live.
- [x] D. Use a blue/green deployment, and test the new application after the rollout completes.

### Explanation

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

---

## Question 31

*Domain 3: Applying Site Reliability Engineering Practices*

You support a service that has a well-defined Service Level Objective (SLO). Over the past six months, the service has consistently met its SLO and customer satisfaction has remained high. Most of its operational tasks are automated, so few repetitive tasks occur often. You want to optimize the balance between reliability and deployment velocity while following site reliability engineering (SRE) best practices. Which two actions should you take? (Choose two.)

- [ ] A. Tighten the service’s SLO.
- [x] B. Raise the service’s deployment velocity and/or accepted risk.
- [x] C. Reassign engineering time to other services that need greater reliability.
- [ ] D. Persuade the product team to put reliability work ahead of new features.
- [ ] E. Revise how the service’s Service Level Indicators (SLIs) are implemented so they cover more of the service.

### Explanation

**Correct Answer**

**B. Raise the service’s deployment velocity and/or accepted risk.**

**C. Reassign engineering time to other services that need greater reliability.**

**Exam Reasoning Explanation**

Read the scenario as a set of diagnostic signals, and ask what each says about where effort is needed. The SLO is consistently met, so reliability is sufficient. Customers are consistently happy, so the SLO matches what users need. Toil is low, so operations are not consuming engineering time. None of the signals show a shortfall, which means the service is spending less of its error budget than it is allowed to. The sensible decisions are therefore to spend that surplus on speed and to move scarce engineering capacity to where reliability is lacking. Options that add reliability investment to an already healthy service, or that adjust measurement without a trigger, do not follow from the signals.

**Key Exam Clues**

  * “consistently met its SLO” over six months — technical signal: reliability exceeds what is required, so error budget is going unused.

  * “customer satisfaction has been consistently high” — hard constraint on the answer: the current SLO is adequate for users, so there is no basis for raising the target.

  * “Most of the service’s operational tasks are automated” — technical signal: toil is low, so there is no toil-reduction work to prioritize.

  * “optimize the balance between reliability and deployment velocity” — hard constraint: with reliability in surplus, the balance should move toward velocity.

  * “(Choose two.)” — cardinality instruction: select two complementary actions that together redeploy the surplus.

**Why This Is Correct**

Option B uses the surplus reliability directly. An SLO defines the reliability users need, and the error budget exists so it can be spent on change and risk; consistently leaving it unspent means releases are slower or more cautious than necessary. Releasing faster or accepting more risk converts that headroom into delivery speed while the SLO still defines the safe boundary. Option C addresses the other surplus, people. Engineers are scarce, and their time should go to the most important characteristics of the most important services, so with this service stable and toil low, capacity is better used on services that fall short of their reliability needs. The two actions are complementary and cover both resources the scenario leaves unspent, error budget and engineering time.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** A stricter SLO shrinks the error budget and increases the cost of reliability, yet customers are already happy at the current target. It is tempting because the team is beating the target easily, but it moves the balance toward reliability when the signals call for velocity, and it sets a bar users did not ask for.

  * **Option D — Violates Requirement:** Prioritizing reliability over new features is the right response to a missed SLO or exhausted error budget. Here the SLO is met and customers are satisfied, so this reverses the intended use of the budget and slows delivery with no benefit.

  * **Option E — Different Use Case:** Increasing SLI coverage is valuable when indicators miss important user journeys, for example when customers are unhappy even though the SLO is met. The scenario shows the opposite, so there is no evidence the SLIs are inadequate, and the change does not address the reliability-versus-velocity balance.

**Exam Trap**

The most tempting distractor is Option A, because “we are easily exceeding the target, so raise the bar” feels like continuous improvement. The distinction is that SLOs reflect user needs and cost, not engineering pride, and happy customers indicate the target is already right. If customers had been unhappy while the SLO was being met, tightening the SLO or improving SLI coverage (Option E) would become the correct direction.

**Foundation Concept**

An SLO sets the reliability level at which user happiness and cost are balanced, and the error budget is the tolerated unreliability that can be traded for velocity. Reliability beyond the target has diminishing value and real costs, such as slower releases and engineering time that could go elsewhere. SRE decision making combines three signals: whether the SLO is met, whether customers are happy, and how much toil exists. Different combinations point to different actions, and this combination points toward spending surplus rather than adding investment.

**Real-World Connection**

A team whose service has comfortably exceeded its SLO for two quarters shortens release cycles, reduces canary soak times, and takes on a long-delayed migration while watching error budget burn-rate alerts. They also lend an engineer to a neighboring service that keeps missing its SLO. Feature delivery speeds up and reliability effort is focused where it is needed, with the SLO and burn-rate alerting acting as the guardrail if the added risk causes problems.

**Memory Hook**

Surplus reliability is unspent budget, so spend it on velocity and send spare engineers where reliability is short.

**30-Second Exam Takeaway**

When a service consistently beats its SLO, users are happy, and toil is low, shift the balance toward velocity and move engineering capacity to services that need reliability. Tighten the SLO or prioritize reliability work only when the signals show unhappy users or a missed SLO.

**Official References**

[**Google SRE Workbook — Implementing SLOs:**](https://sre.google/workbook/implementing-slos/) Supports: the correct-answer mechanism for options B and C (SLOs reflect user happiness, engineering time should go to the most important services, and decisions about reliability versus functionality follow from SLO and error budget status), and the elimination of options A, D, and E

[Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide: ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment to Section 3.1, “Balancing change, velocity, and reliability of the service,” which covers SLOs, error budgets, and the opportunity cost of risk and reliability

---

## Question 32

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You run an application on Google Kubernetes Engine (GKE). For each request, the application calls several other services, and its responses are too slow. You need to determine which downstream service or services are responsible for the delay. What should you do?

- [ ] A. Analyze VPC Flow Logs along the path that the request takes.
- [ ] B. Examine the liveness and readiness probes of each service.
- [ ] C. Build a Dataflow pipeline that analyzes service metrics in real time.
- [x] D. Use a distributed tracing framework, such as OpenTelemetry or Cloud Trace.

### Explanation

**Correct Answer**

**D. Use a distributed tracing framework, such as OpenTelemetry or Cloud Trace.**

**Exam Reasoning Explanation**

The decisive requirement is attribution: you must split one slow request into the time spent in each downstream service. That calls for data recorded per request, with each hop timed and linked to its caller. Check each option for whether it measures per-request, per-service duration or something else, such as network connections, container health, or fleet-wide aggregates. Only one option produces a per-request breakdown across services without extra construction.

**Key Exam Clues**

  * “invokes multiple services per request” — technical signal: a single request’s latency is the sum of several service calls, so the answer must expose each call’s timing within that request.

  * “identify which downstream service or services” — hard constraint: the evidence must attribute delay to specific services, not just show that the application is slow overall.

  * “responds too slowly” — technical signal: this is a latency problem, not an availability or health problem.

  * “Google Kubernetes Engine” — context clue: the runtime is supported by Cloud Trace, and instrumentation with OpenTelemetry works there.

**Why This Is Correct**

Distributed tracing follows a request as it crosses services. Each operation is recorded as a span with a start, a duration, and a parent-child link to the span that triggered it, and the spans for a request form a trace. Viewing a trace shows exactly which downstream call consumed most of the time. Cloud Trace is Google Cloud’s distributed tracing system for this purpose, it runs with applications on GKE, and its Trace Explorer lets you examine aggregate latency and individual traces. Google recommends instrumenting applications with OpenTelemetry. One prerequisite is that the services must be instrumented and must propagate trace context, so that spans from different services join into the same trace.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Different Use Case:** VPC Flow Logs record network-level information about connections, which helps with traffic patterns and connectivity questions. It is tempting because the services communicate over the network, but flow records do not show application-level request latency or which spans belong to the same request.

  * **Option B — Different Use Case:** Liveness and readiness probes tell Kubernetes whether a container should be restarted or receive traffic. They are tempting because they relate to service health, but a service can pass its probes and still be slow, and probes do not measure how long individual requests take.

  * **Option C — Technically Possible but Not Best:** A streaming pipeline could process service metrics and might show which service is slow in aggregate, which is why it is tempting. It would require building and maintaining custom infrastructure, and aggregated metrics do not tie time to specific requests or show where inside a request the delay occurred, which tracing provides natively.

**Exam Trap**

The strongest distractor is Option C, because “real-time analysis of metrics” sounds sophisticated and metrics do reveal that something is slow. The distinction is that metrics aggregate across requests, while the question needs a per-request view of where time is spent. If the goal were to detect anomalies continuously across a large fleet’s aggregated metrics, a streaming analytics pipeline could be justified.

**Foundation Concept**

Observability signals have complementary roles: metrics show that a problem exists and how large it is, logs explain discrete events, and traces show where time is spent along a request path. A trace is made of spans, and trace-context propagation between services is what stitches those spans together. Tracing has limits, since services must be instrumented and sampling can hide rare slow requests, but it is the standard tool for latency attribution in microservice architectures.

**Real-World Connection**

A team instruments its GKE services with OpenTelemetry and exports spans to Cloud Trace. In Trace Explorer, the latency heatmap shows the slow requests, and a trace waterfall reveals that one inventory-lookup span takes most of the request time. The team fixes that service and uses the trace ID to jump to the related logs. The costs are instrumentation effort and a sampling choice that balances detail against volume.

**Memory Hook**

Metrics tell you that it is slow, and traces tell you where.

**30-Second Exam Takeaway**

When a request fans out to several services and you must find which one adds latency, choose distributed tracing. Network flow logs, health probes, and custom metric pipelines do not give a per-request breakdown across services.

**Official References**

[**Google Cloud — Cloud Trace overview:**](https://docs.cloud.google.com/trace/docs/overview) Supports: the correct-answer mechanism (Cloud Trace as a distributed tracing system for finding where request latency arises, support for GKE, the recommendation to instrument with OpenTelemetry, and Trace Explorer for analysis)

[**Kubernetes — Configure liveness, readiness and startup probes:**](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) Supports: the elimination of Option B, since probes determine container restart and traffic-readiness decisions and not request latency

[**Google Cloud — VPC Flow Logs overview:**](https://docs.cloud.google.com/vpc/docs/flow-logs) Supports: the elimination of Option A, since flow logs describe network-level connections and not application request latency

---

## Question 33

*Domain 3: Applying Site Reliability Engineering Practices*

You support a user-facing web application. When you analyze its error budget for the past six months, you find that it has never used more than 5% of its error budget in any given time window. You hold a Service Level Objective (SLO) review with business stakeholders and confirm that the SLO is set appropriately. You want the application’s SLO to reflect its observed reliability more closely. Which two steps can you take to further that goal while balancing velocity, reliability, and business needs? (Choose two.)

- [ ] A. Add more serving capacity to every zone the application runs in.
- [x] B. Make application releases more frequent or potentially riskier.
- [ ] C. Tighten the SLO to match the application’s observed reliability.
- [ ] D. Implement and measure additional Service Level Indicators (SLIs) for the application.
- [x] E. Announce planned downtime to use up more of the error budget, and make sure users are not depending on a tighter SLO.

### Explanation

**Correct Answer**

**B. Make application releases more frequent or potentially riskier.**

**E. Announce planned downtime to use up more of the error budget, and make sure users are not depending on a tighter SLO.**

**Exam Reasoning Explanation**

Identify what is fixed and what can move. The SLO is fixed, because stakeholders just confirmed it matches business needs. What can move is the observed reliability, which is far higher than the SLO requires. The goal of aligning the two therefore has to be met from the observed side, by deliberately using some of the unspent error budget, and not by changing the target. Evaluate each option by asking whether it spends surplus budget safely or whether it adds reliability, changes the agreed target, or only changes measurement. Only two options spend the surplus in ways the business can accept.

**Key Exam Clues**

  * “never consumed more than 5% of its error budget” — technical signal: reliability substantially exceeds the SLO, so most of the budget goes unused.

  * “confirm that the SLO is set appropriately” — hard constraint: the SLO target should stay as it is, so the gap must be closed by moving observed reliability.

  * “SLO to more closely reflect its observed reliability” — goal statement: reduce the over-delivery rather than reinforce it.

  * “balancing velocity, reliability, and business needs” — preference: favor actions that convert surplus reliability into delivery speed without breaking business commitments.

  * “(Choose two.)” — cardinality instruction: pick two complementary ways to spend the budget.

**Why This Is Correct**

Option B spends the unused budget on change. Releases are a major source of outages, so more frequent or somewhat riskier releases use budget in exchange for velocity, and the SLO remains the boundary that limits how far to go. Option E addresses a less obvious risk of over-delivering: users come to depend on the reliability they actually observe, not the reliability promised, so an SLO that is greatly exceeded effectively becomes a tighter implicit SLO. Google describes this with its Chubby lock service, where SRE makes a service meet, but not significantly exceed, its SLO, and introduces planned outages so dependents do not assume it never fails. The two work together: B uses the surplus to speed delivery, and E uses part of it to reset user expectations and expose hidden dependencies. Both lower observed reliability toward the SLO while staying within the agreed budget, which makes the pair complete for the stated goal.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Extra capacity in every zone raises reliability and cost further, which widens the gap between the SLO and observed reliability, the opposite of the goal.

  * **Option C — Violates Requirement:** Matching the SLO to observed performance is tempting because it makes the two numbers agree immediately. But the SLO has just been validated against business needs, and SLOs should reflect what users and the business require, not what the system happens to deliver. Tightening shrinks the error budget, leaving less room for change and slowing velocity, and it commits the team to a level nobody asked for.

  * **Option D — Different Use Case:** More SLIs improve measurement coverage, which is valuable if existing indicators miss important user journeys. Nothing in the scenario suggests the SLIs are inadequate, and extra measurement does not close the gap between a validated SLO and the unused budget.

**Exam Trap**

The most tempting distractor is Option C, because “make the SLO match observed reliability” reads like the literal request. The distinction is that the SLO review confirmed the target, so the question is asking how to bring behavior toward the target. If stakeholders had instead determined that users really needed higher reliability, tightening the SLO would become appropriate, and if the SLIs were found to miss key user journeys, Option D would become relevant.

**Foundation Concept**

An SLO sets the reliability users and the business actually need, and the error budget is the amount of unreliability that can be traded for other benefits. Persistently exceeding the SLO is not free: it slows delivery, raises cost, and teaches users to rely on performance that was never promised, which creates a de facto tighter SLO. SRE therefore treats unused budget as something to spend deliberately. In production, any planned downtime must stay within the budget, be announced in advance, and be coordinated with dependent teams.

**Real-World Connection**

A team that has never used more than a small share of its error budget increases release frequency and shortens canary soak times. It also schedules announced, time-boxed maintenance events sized to use part of the budget, and tells dependent teams so they add retries and fallbacks. Delivery speeds up and downstream services become more resilient, with burn-rate alerting watching that the budget is not overspent.

**Memory Hook**

Meet the SLO without greatly exceeding it, because unspent budget is wasted velocity and a hidden promise.

**30-Second Exam Takeaway**

When a service far outperforms an SLO that stakeholders have confirmed, close the gap by spending budget safely, through faster or riskier releases and announced planned downtime. Do not tighten the SLO, add capacity, or simply measure more.

**Official References**

[**Google SRE Book — Service Level Objectives:**](https://sre.google/sre-book/service-level-objectives/) Supports: the correct-answer mechanism for options B and E (users rely on actual performance, and the Chubby example of meeting but not significantly exceeding an SLO with planned outages), and the elimination of Option C

[Google SRE Workbook — Implementing SLOs: ](https://sre.google/workbook/implementing-slos/)Supports: the use of error budgets to balance reliability against change and velocity, which eliminates Option A and distinguishes Option D

---

## Question 34

*Domain 3: Applying Site Reliability Engineering Practices*

Your development team has built a new version of its service’s API. You need to roll out the new version with the least possible disruption to third-party developers and to the end users of third-party installed applications. What should you do?

- [x] A. Introduce the new API version. Announce the deprecation of the old version. Deprecate the old version. Contact the remaining users of the old version. Provide best-effort support to users of the old version. Turn down the old version.
- [ ] B. Announce the deprecation of the old version. Introduce the new API version. Contact the remaining users of the old version. Deprecate the old version. Turn down the old version. Provide best-effort support to users of the old version.
- [ ] C. Announce the deprecation of the old version. Contact the remaining users of the old version. Introduce the new API version. Deprecate the old version. Provide best-effort support to users of the old version. Turn down the old version.
- [ ] D. Introduce the new API version. Contact the remaining users of the old version. Announce the deprecation of the old version. Deprecate the old version. Turn down the old version. Provide best-effort support to users of the old version.

### Explanation

**Correct Answer**

**A. Introduce the new API version. Announce the deprecation of the old version. Deprecate the old version. Contact the remaining users of the old version. Provide best-effort support to users of the old version. Turn down the old version.**

**Exam Reasoning Explanation**

Because every option contains the same six steps, the question is purely about ordering, so derive the ordering rules from the constraint. Third-party developers and their installed applications cannot be upgraded on your schedule, so every step that pressures users must come after something that makes the pressure reasonable, and the only step that breaks clients must come last. That yields four dependencies: the replacement exists before anyone is asked to migrate, notice comes before the deprecation takes effect, outreach to remaining users follows the migration period, and support for stragglers is offered while the old version still runs, before it is turned down. Check each option for violations, and only one has none.

**Key Exam Clues**

  * “least disruption to third-party developers and end users” — hard constraint: clients you do not control must keep working throughout, so the breaking step, turn down, must come last.

  * “third-party installed applications” — technical signal: installed apps update slowly and unpredictably, so a long overlap and direct outreach are needed.

  * “deploy the new versions of the API” — sequence instruction: the new version must be available first so there is something to migrate to.

  * “remaining users” and “best-effort support” — sequence signals: these steps address stragglers after migration has begun and before the old version is removed.

**Why This Is Correct**

Option A follows the dependency order. Introducing the new version first gives users a destination. Announcing the deprecation then gives them notice and a timeline, and deprecating the old version formally marks it as superseded. Contacting the remaining users comes next, because only after the migration period can you identify who has not moved. Providing best-effort support to those users helps them finish migrating while the old version still works, and turning it down last removes the old version only after migration has been supported, which keeps disruption to a minimum. This matches Google’s published API guidance that an older version must go through a reasonable, well-communicated deprecation period before it is shut down.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Violates Requirement:** It announces deprecation before the new version exists, so users are told to leave with nowhere to go. It also provides support after turning the old version down, when the users who needed help have already lost service.

  * **Option C — Violates Requirement:** It announces deprecation and contacts users before introducing the replacement, so the outreach has nothing to offer them. Starting the process this way creates exactly the disruption the question is trying to avoid.

  * **Option D — Violates Requirement:** It starts correctly by introducing the new version, which makes it the most tempting distractor. It then contacts the remaining users before any deprecation announcement, so there is no migration period from which anyone could be “remaining,” and it offers support only after the old version has been turned down.

**Exam Trap**

The trap is Option D, because it shares the correct first step and looks nearly identical to A. The errors are in the middle and end: outreach before announcement, and support after shutdown. Support after turn-down is illogical under any reading, so no single changed requirement would make D correct. As a rule of thumb, scan each sequence for the turn-down step, which must be last.

**Foundation Concept**

When you run an API consumed by clients you do not control, the producer owns the migration timeline but not the clients’ release schedules. Safe lifecycle management therefore follows a pattern: ship the replacement, give notice, keep the old version working during an overlap, identify and help stragglers, and remove the old version last because removal is the only step that breaks clients. The exam’s six-step labels are framing for this pattern; Google’s API guidance (AIP-185) states the general requirement as a reasonable, well-communicated deprecation period before shutdown.

**Real-World Connection**

A team publishes v2 beside v1 behind the same API gateway and announces a deprecation timeline with dates. It marks v1 as deprecated in documentation and responses, then uses request logs and API keys to find the callers who are still on v1 and contacts them directly. After helping those callers migrate, it turns v1 down once traffic is negligible. Partner applications keep working throughout, and the cost is running two versions in parallel during the overlap.

**Memory Hook**

Replacement first and shutdown last, with notice before deprecation and outreach before turn-down.

**30-Second Exam Takeaway**

For API version retirement questions, order the steps by dependency: new version, announcement, deprecation, outreach to remaining users, support, then turn-down. Reject any sequence that asks users to migrate before the replacement exists or that supports users after the old version is gone.

**Official References**

[**Google API Improvement Proposals — AIP-185: API Versioning:**](https://google.aip.dev/185) Supports: Google’s guidance that an older API version must go through a reasonable, well-communicated deprecation period before being shut down, which underpins the ordering in option A

[Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide: ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment to Section 3.2, “Managing service lifecycle,” which covers service management from planning and deployment through maintenance and retirement

---

## Question 35

*Domain 3: Applying Site Reliability Engineering Practices*

You are drafting the action items in a postmortem for an outage and assigning people to them. The outage has ended, but its root causes still need to be fixed, and you want the team to complete the action items promptly and efficiently. What is the best way to assign owners and collaborators to the action items?

- [x] A. Name one owner for each action item, and add collaborators where needed.
- [ ] B. Name several owners for each item so the team is guaranteed to complete items quickly.
- [ ] C. Name collaborators only, with no individual owner, so the postmortem stays blameless.
- [ ] D. Name the team lead as the owner of every action item, because they lead the SRE team.

### Explanation

**Correct Answer**

**A. Name one owner for each action item, and add collaborators where needed.**

**Exam Reasoning Explanation**

Begin with the one hard requirement, which is that corrective work gets finished quickly and efficiently. Then picture each assignment model once the incident pressure has faded and the item competes with feature work. Speed depends on whether someone clearly knows the item is theirs to push, and on whether helpers know whom they are supporting. So separate the two roles in the question: an accountable owner and supporting collaborators. Screen each option for whether it keeps accountability single, present, and close to the work. Only one option meets all three conditions.

**Key Exam Clues**

  * “address the root causes” — technical signal: the action items are corrective work that must be completed, and recording them alone does not reduce risk.

  * “quickly and efficiently” — hard constraint: the assignment model must remove ambiguity about who drives the item and avoid handoff delays.

  * “owners and collaborators” — technical signal: these are separate roles, so the answer must define both and keep them distinct.

  * “The outage is over” — context clue: with no incident urgency, follow-through depends on clear ownership while other priorities compete.

**Why This Is Correct**

One named owner is accountable for moving the item from idea to completion, which means a single person tracks status, chases dependencies, and escalates blockers. Collaborators contribute expertise or access, such as another team’s system, without sharing the accountability. This keeps decisions fast, because one person can proceed without waiting for agreement among several people. It also matches how SRE guidance treats postmortem action items: as prioritized, tracked work that needs a clear accountable person to reach closure. The pair of roles is complete for the question, since it covers who drives the work and who supports it.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Violates Requirement:** Several owners sounds like extra assurance, which is why it is tempting. But shared ownership spreads responsibility, so each person can reasonably assume another is handling the item, and coordination overhead rises. Nothing about it guarantees speed.

  * **Option C — Violates Requirement:** Blameless postmortems avoid assigning fault for what happened. They do not remove accountability for completing the fix. With no individual owner, nobody is answerable for progress, so items tend to stall, which defeats the goal of addressing root causes.

  * **Option D — Technically Possible but Not Best:** The team lead is a single accountable person, so this option does not fail on ambiguity. It loses because routing every item through one person creates a bottleneck, and ownership follows seniority instead of who is best placed to do the work, which slows items that need hands-on expertise.

**Exam Trap**

The strongest distractor is Option C, because it applies the blameless principle to the wrong thing. Blamelessness concerns how the incident’s causes are analyzed and described, whereas ownership of a corrective action is forward-looking accountability. If the question had asked how to write the incident narrative without attributing fault to individuals, then not naming people would be the right approach.

**Foundation Concept**

Accountability and blame are different ideas: blame looks backward at fault, while ownership looks forward at who will deliver the change. Tasks shared among many people are prone to diffusion of responsibility, and the usual remedy is one accountable person supported by contributors, a pattern similar to the accountable and consulted roles in responsibility-assignment models. Good action items are also prioritized, tracked in the team’s normal work system, and reviewed on a regular cadence so they do not fade after the postmortem is published.

**Real-World Connection**

After a memory-exhaustion outage, an action item to add a saturation alert is assigned to one engineer on the owning service team, with the observability team listed as a collaborator. The item has a priority and due date in the issue tracker and is checked in the weekly reliability review. The owner reports status and raises any blocker with the collaborating team, so the fix competes fairly with feature work and gets closed.

**Memory Hook**

One owner drives each item, and collaborators help without sharing the accountability.

**30-Second Exam Takeaway**

For postmortem action items, choose a single accountable owner with collaborators as needed. Eliminate multiple owners, ownerless items justified by blamelessness, and blanket assignment to the team lead.

**Official References**

[**Google SRE Workbook — Postmortem Culture: Learning from Failure:**](https://sre.google/workbook/postmortem-culture/) Supports: the correct-answer mechanism, since it explains what makes postmortem action items actionable for preventing recurrence, including clear priorities, and why options that blur accountability fall short

[**USENIX ;login: — Postmortem Action Items: Plan the Work and Work the Plan (Google SRE):**](https://www.usenix.org/publications/login/spring2017/lunney) Supports: Google’s approach to categorizing, prioritizing, and tracking action items so that they are actually executed

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment to Section 3, “Applying site reliability engineering practices,” whose incident-related objectives (3.3) cover post-incident follow-through

---

## Question 36

*Domain 2: Building and Implementing CI/CD Pipelines*

Your organization runs a containerized web application on-premises. As part of its migration to Google Cloud, you must choose a deployment strategy and a platform that satisfy all of the following acceptance criteria:

  1. The platform can route traffic from Android devices to an Android-specific microservice.

  2. The platform supports arbitrary percentage-based traffic splitting.

  3. The deployment strategy supports continuous testing of multiple versions of any microservice.

What should you do?

- [ ] A. Release a canary of the application on Cloud Run, and use traffic splitting to send 10% of user traffic to the canary according to the revision tag.
- [ ] B. Release a canary of the application on App Engine, and use traffic splitting to send a subset of user traffic to the new version according to the IP address.
- [ ] C. Release a canary of the application on Compute Engine, and use Cloud Service Mesh with Compute Engine to send 10% of user traffic to the canary by configuring the virtual service.
- [x] D. Release a canary on Google Kubernetes Engine (GKE) with Cloud Service Mesh, and use traffic splitting to send 10% of user traffic to the new version according to the user-agent header configured in the virtual service.

### Explanation

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

---

## Question 37

*Domain 3: Applying Site Reliability Engineering Practices*

Your company applies Site Reliability Engineering (SRE) principles. You are writing the postmortem for an incident that was triggered by a software change and severely affected users. You want to prevent a severe incident like this from happening again. What should you do?

- [ ] A. Identify the engineers responsible for the incident and escalate the matter to senior management.
- [x] B. Make sure that test cases capable of catching errors of this kind pass before new software releases.
- [ ] C. Follow up with the employees who reviewed the changes and prescribe the practices they should follow going forward.
- [ ] D. Design a policy requiring on-call teams to immediately call engineers and management to agree on a plan of action whenever an incident occurs.

### Explanation

**Correct Answer**

**B. Make sure that test cases capable of catching errors of this kind pass before new software releases.**

**Exam Reasoning Explanation**

Start from the SRE principle that postmortems look for systemic causes, not culprits, and that their action items should reduce the chance of recurrence. Then ask where the failure entered: a software change reached users, so a control was missing between code and release. Test each option on two questions: does it target the system or specific people, and does it prevent the failure or only react to it? Options that point at individuals fail the first test, an option about response coordination fails the second, and only one option adds a systemic preventive control.

**Key Exam Clues**

  * “follows Site Reliability Engineering principles” — technical signal: postmortems are blameless and focus on contributing causes in the system, not on individuals.

  * “triggered by a software change” — technical signal: the defect passed through the release process, so the fix belongs before release.

  * “prevent severe incident from happening in the future” — hard constraint: the action must lower the likelihood of recurrence, not just improve how the next incident is handled.

  * “writing a postmortem” — context clue: the deliverable is concrete action items that address root causes.

**Why This Is Correct**

The incident shows a gap: a class of error was able to reach users because no release-time check caught it. Adding test cases that detect this kind of error, and requiring them to pass before new releases, converts the lesson into an automated, repeatable control. It works no matter who writes or reviews a change, which is what a systemic fix should do. In Google’s classification of postmortem action items, it is a prevention-type item, the type that aims to stop recurrence or reduce its impact, whereas items that only mitigate or improve response leave the underlying defect path open.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Naming responsible engineers and escalating them is the opposite of blameless practice. It is tempting because it appears to create accountability, but it discourages honest reporting and changes nothing in the system, so the same class of error can recur with a different author.

  * **Option C — Violates Requirement:** Following up with reviewers and prescribing practices sounds like process improvement, which makes it tempting. It still singles out individuals, and it relies on people remembering to apply guidance each time, which is a weaker and less reliable control than an automated test gate.

  * **Option D — Different Use Case:** A call-out policy improves coordination during an incident, which is valid incident management practice. It does not stop a faulty change from reaching users, and it would apply to every incident regardless of severity, so it fails the prevention requirement.

**Exam Trap**

The strongest distractor is Option C, because improving the review process feels like a systemic fix. The distinction is that it targets the people who reviewed the change and depends on their future diligence, while the SRE approach is to fix the system with controls that do not depend on any one person. If the question had asked how to shorten response time to future incidents, Option D would move up, since it addresses coordination rather than prevention.

**Foundation Concept**

A blameless postmortem identifies contributing causes without indicting individuals or teams, because people who fear punishment hide problems and the organization stops learning. The output is a set of concrete, owned, tracked action items, which Google categorizes as investigate, mitigate, repair, detect, and prevent. Prefer automated prevention, such as tests and pipeline gates, over reminders, training, or additional approvals. Google’s SRE Workbook also warns against postmortems whose action items are mostly mitigative and fail to address recurrence.

**Real-World Connection**

After an outage caused by an unvalidated configuration change, a team writes a regression test that reproduces the failure pattern and makes it a required check in its release pipeline. The postmortem records the action item with an owner and a due date and tracks it to closure. Releases that would trigger the same class of failure are now blocked automatically, at the cost of maintaining the test and a slightly longer pipeline.

**Memory Hook**

Fix the system, not the person, by turning the lesson into an automated release gate.

**30-Second Exam Takeaway**

In an SRE postmortem question about preventing recurrence, pick the systemic, automated control that closes the gap the change slipped through. Reject answers that blame or retrain individuals, and answers that only improve incident response.

**Official References**

[**Google SRE Book — Postmortem Culture: Learning from Failure:**](https://sre.google/sre-book/postmortem-culture/) Supports: the blameless-postmortem principle and the focus on contributing causes over individuals, which eliminates Options A and C

[**Google SRE Workbook — Postmortem Culture: Learning from Failure:**](https://sre.google/workbook/postmortem-culture/) Supports: the need for action items that prevent recurrence and not merely mitigate, which supports option B over option D

---

## Question 38

*Domain 3: Applying Site Reliability Engineering Practices*

You are responsible for the reliability of a high-volume enterprise application. Many users report that an important part of its functionality, a data-intensive reporting feature, consistently fails with an HTTP 500 error. When you review the application’s dashboards, you see a strong correlation between the failures and a metric that tracks the size of an internal queue used to generate reports. You trace the failures to a reporting backend with high I/O wait times, and you resolve the problem quickly by resizing the backend’s persistent disk (PD). Now you need to create an availability Service Level Indicator (SLI) for the report generation feature. How should you define it?

- [ ] A. As the I/O wait times aggregated across all report generation backends.
- [x] B. As the proportion of report generation requests that result in a successful response.
- [ ] C. As the application’s report generation queue size compared with a known-good threshold.
- [ ] D. As the reporting backend’s PD throughput capacity compared with a known-good threshold.

### Explanation

**Correct Answer**

**B. As the proportion of report generation requests that result in a successful response.**

**Exam Reasoning Explanation**

Separate the diagnostic story from the actual ask. The troubleshooting details, queue size, I/O wait, and disk capacity, describe what caused one incident, whereas the requirement is an availability indicator for the feature. An availability SLI should answer one question: did users get a successful result when they asked for a report? Test each option on whether it counts successful outcomes against all valid attempts, or whether it measures an internal condition that merely correlated with failure. Only one option is a direct measure of the user-visible outcome, and the rest are cause-side signals.

**Key Exam Clues**

  * “availability Service Level Indicator” — hard constraint: the indicator must express whether requests to the feature succeed, not how a component is behaving.

  * “report generation feature” — scope clue: the SLI should be limited to requests for this feature, not the whole application.

  * “consistently failing with an HTTP 500 error” — technical signal: the user-visible failure is a failed response, so success versus failure of responses is the natural basis for good and bad events.

  * “queue size,” “I/O wait times,” and “persistent disk” — exclusion signals: these are causes found during troubleshooting, and an SLI built on them would track one failure mode instead of availability.

**Why This Is Correct**

An SLI is most useful as a ratio of good events to valid events, and for availability the natural form is the proportion of requests that were served successfully. Defining it as the share of report generation requests that return a successful response measures exactly what users experience, and it moves down whatever the cause of failure is, whether disk I/O, a full queue, a software defect, or something not yet seen. That makes it a stable basis for an SLO and an error budget. One boundary is to define “valid” and “good” explicitly, for example by excluding health checks and by treating 5xx responses as bad events.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Different Use Case:** I/O wait time is a resource saturation signal that is valuable for diagnosing backend performance, and it is tempting because it was the cause here. But it does not say whether requests succeeded: high I/O wait may not break requests, and requests can fail with low I/O wait.

  * **Option C — Technically Possible but Not Best:** Queue size correlated strongly with failures, which makes it attractive as a signal and potentially useful as a leading indicator for alerting. It is still an internal proxy, and a threshold on it describes system state instead of user-visible success, so it can miss failures that have other causes and can fire when users are unaffected.

  * **Option D — Different Use Case:** Disk throughput capacity compared with a threshold is a capacity-planning and configuration measure, and resizing the disk was the fix for this incident. It says nothing directly about whether report requests succeed, and the “known-good” threshold is subjective.

**Exam Trap**

The strongest distractor is Option C, because the dashboard correlation makes the queue metric feel authoritative. The distinction is that SLIs measure the outcome users experience, while queue size is one of several possible causes of a bad outcome. If the question had asked for an early-warning alert that fires before users are affected, a queue-size threshold would be a reasonable leading indicator for that purpose.

**Foundation Concept**

An SLI is a carefully defined measure of an aspect of the service level that users receive, and the preferred form is good events divided by valid events. SLIs and SLOs should reflect user experience, so they track symptoms, while cause-based metrics such as saturation, queue depth, and I/O wait belong on diagnostic dashboards and in supporting alerts. Common SLI types for request-driven features are availability, latency, and quality, and each requires a precise definition of which events count as valid and which count as good.

**Real-World Connection**

A team defines the report feature’s availability SLI as the number of report requests answered with a non-5xx status divided by all report requests, measured at the load balancer or in application metrics. It sets an SLO over a rolling window and alerts on error budget burn rate. I/O wait and queue depth stay on a diagnostic dashboard with warning alerts. The SLI drops no matter what breaks the feature, though it does not explain why, so the diagnostic signals remain necessary for troubleshooting.

**Memory Hook**

An SLI measures what users get, as good over valid events, not what a backend is doing.

**30-Second Exam Takeaway**

When asked to define an availability SLI, choose the ratio of successful requests to valid requests for the feature in question. Do not pick resource, queue, or capacity metrics, which are causes that help diagnose problems but do not measure availability.

**Official References**

[**Google SRE Book — Service Level Objectives:**](https://sre.google/sre-book/service-level-objectives/) Supports: the correct-answer mechanism, including the definition of an SLI as a carefully defined measure of the service level provided and the guidance to build indicators around what users care about, which eliminates options A, C, and D

[**Google SRE Workbook — Implementing SLOs:**](https://sre.google/workbook/implementing-slos/) Supports: the request-based SLI form, the proportion of good requests among all valid requests, and how SLIs feed SLOs and error budgets

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment to Section 3.1, “Balancing change, velocity, and reliability of the service,” which covers defining SLIs such as availability and latency, SLOs, and SLAs

---

## Question 39

*Domain 2: Building and Implementing CI/CD Pipelines*

You are ready to release a new feature of a web-based application to production. You want to use Google Kubernetes Engine (GKE) to perform a phased rollout that first reaches half of the web server pods. What should you do?

- [x] A. Use a partitioned rolling update.
- [ ] B. Use node taints with the NoExecute effect.
- [ ] C. Use a ReplicaSet in the Deployment specification.
- [ ] D. Use a StatefulSet with the Parallel pod management policy.

### Explanation

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

---

## Question 40

*Domain 3: Applying Site Reliability Engineering Practices*

You are writing the postmortem for an incident that had a severe impact on users, and you want to prevent similar incidents in the future. Which two of the following sections should you include in the postmortem? (Choose two.)

- [x] A. An explanation of the incident’s root cause.
- [ ] B. A list of the employees responsible for causing the incident.
- [x] C. A list of action items to prevent the incident from recurring.
- [ ] D. Your personal assessment of how the incident’s severity compares with past incidents.
- [ ] E. Copies of the design documents for every service the incident affected.

### Explanation

**Correct Answer**

**A. An explanation of the incident’s root cause.**

**C. A list of action items to prevent the incident from recurring.**

**Exam Reasoning Explanation**

The stated purpose is prevention of similar incidents, so the test for each section is whether it helps the organization understand why the failure happened or change something so it does not happen again. Sections that identify people, offer subjective rankings, or bulk up the document with reference material do not serve that purpose. Because the question asks for two answers, look for a complementary pair: one section that diagnoses and one that prescribes. That pair covers the learning loop, from understanding the cause to acting on it.

**Key Exam Clues**

  * “prevent similar incidents in the future” — hard constraint: every included section must contribute to understanding causes or driving corrective change.

  * “postmortem” — technical signal: SRE postmortems are blameless learning documents, so sections that single out individuals are excluded.

  * “severely affected users” — context clue: a serious incident warrants a thorough causal analysis and concrete follow-up work.

  * “(Choose two.)” — cardinality instruction: pick two sections that together form a diagnosis-and-remediation pair.

**Why This Is Correct**

An explanation of the root cause, or more precisely the contributing causes, records why the incident happened and gives readers the understanding needed to find similar weaknesses elsewhere. A list of action items turns that understanding into work: concrete, prioritized changes with owners that reduce the chance or impact of recurrence. The two sections work together and neither is sufficient alone, since cause analysis without actions leaves the gap open, and actions without a causal explanation risk fixing the wrong thing. Together they are the minimum that delivers the question’s goal.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Violates Requirement:** A list of people responsible turns the postmortem into a blame exercise. It is tempting because accountability sounds useful, but SRE postmortems are blameless, since blaming individuals discourages honest reporting and leaves the underlying system gaps unaddressed.

  * **Option D — Technically Possible but Not Best:** A severity comparison can add context, and teams often record impact and severity in a postmortem. A personal opinion on how it ranks against past incidents is subjective, so it does not explain the cause or lead to a fix, and it is not among the sections that serve the stated prevention goal.

  * **Option E — Different Use Case:** Design documents are reference material for understanding a system, and a postmortem may link to specific relevant ones. Attaching copies for every impacted service adds bulk without analysis, and it does not explain this incident or prescribe changes.

**Exam Trap**

The strongest distractor is Option B, because naming those involved feels like part of an honest account. The distinction is that postmortems analyze the system conditions that allowed the failure, and people appear in the timeline only as actors whose decisions the system made possible. If the question asked for the incident timeline, referring to roles or decisions made at each step would be appropriate, but a list of culprits would still not be.

**Foundation Concept**

A postmortem is a written record of an incident: its impact, the actions taken to resolve it, the contributing causes, and the follow-up actions to prevent recurrence. Blameless practice focuses on those causes without indicting individuals or teams, because people who fear punishment hide problems and organizations stop learning. Good action items are concrete, prioritized, owned, and tracked to completion, and they cover prevention as well as detection and mitigation.

**Real-World Connection**

After an outage caused by a configuration change that overloaded a backend, the team writes a postmortem with a causal analysis that explains why the change passed review and why alerts fired late. The action items add a pre-release load check and a saturation alert, each with an owner and due date. Other teams read it and apply the same checks to their services, so the incident produces systemic improvement instead of a list of names.

**Memory Hook**

A postmortem explains why it happened and what will change, never who to blame.

**30-Second Exam Takeaway**

For postmortem content questions, include the root-cause analysis and the action items that prevent recurrence. Exclude lists of people, subjective opinions, and bulk attachments that do not drive learning or change.

**Official References**

[**Google SRE Book — Postmortem Culture: Learning from Failure:**](https://sre.google/sre-book/postmortem-culture/) Supports: the correct-answer mechanism, since it describes postmortems as documentation of the incident, its root causes, and the follow-up actions to prevent recurrence, and it establishes the blameless principle that eliminates option B

[**Google SRE Workbook — Postmortem Culture: Learning from Failure:**](https://sre.google/workbook/postmortem-culture/) Supports: the need for actionable items that prevent recurrence, which supports option C and distinguishes the other options

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment to Section 3, “Applying site reliability engineering practices,” whose incident-related objectives (3.3) cover post-incident learning

---

## Question 41

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You are running an application on Compute Engine and collecting its logs through Cloud Logging. You discover that some personally identifiable information (PII) is leaking into certain log entry fields. You want to stop these fields from being written to new log entries as quickly as possible. What should you do?

- [x] A. Use the filter-record-transformer Fluentd filter plugin to strip the fields from log entries in flight.
- [ ] B. Use the fluent-plugin-record-reformer Fluentd output plugin to strip the fields from log entries in flight.
- [ ] C. Wait for the application developers to patch the application, then confirm that new log entries no longer expose PII.
- [ ] D. Stage log entries in Cloud Storage, then trigger a Cloud Run function that removes the fields and writes the entries to Cloud Logging through the Cloud Logging API.

### Explanation

**Correct Answer**

**A. Use the filter-record-transformer Fluentd filter plugin to strip the fields from log entries in flight.**

**Exam Reasoning Explanation**

Two hard constraints decide this: the fields must never reach Cloud Logging in new entries, and the fix must take effect as fast as possible. The first constraint locates the control point. It has to sit in the path between the application’s log file and the write to Cloud Logging, which on Compute Engine is the logging agent running on the VM. The second constraint favors a configuration change on that agent over anything that needs code changes or a new pipeline. Check each option against both constraints, and only the one that edits records inside the agent’s pipeline satisfies both.

**Key Exam Clues**

  * “PII is leaking into certain log entry fields” — technical signal: specific fields must be removed from records, which calls for record-level transformation and not dropping entire logs.

  * “prevent these fields from being written in new log entries” — hard constraint: removal has to happen before the entry is written to Cloud Logging, so it must occur at the agent.

  * “as quickly as possible” — hard constraint: a configuration change on the existing agent beats waiting for a code release or building new infrastructure.

  * “running an application on Compute Engine” — context clue: the Fluentd-based logging agent on the VM is the available interception point.

**Why This Is Correct**

The Cloud Logging agent, google-fluentd, is a modified version of the Fluentd log collector, so Fluentd plugins and configuration apply to it. Fluentd’s `filter_record_transformer` is built into Fluentd core and needs no installation, and its `remove_keys` parameter deletes the listed keys from each record as it passes through the pipeline. Adding a filter stanza that matches the affected log’s tag and restarting the agent stops the PII fields from being included in new entries immediately, without touching the application. Entries already written to Cloud Logging are not changed by this, so the application fix and any cleanup of existing data are separate follow-ups.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Technically Possible but Not Best:** The plugin name is almost identical to the correct one, which is why it is tempting. However, `fluent-plugin-record-reformer` is a separate gem that must be installed, and the option frames it as an output-stage plugin, while Fluentd already provides a built-in filter for deleting record keys in flight. It adds avoidable setup and is not the standard mechanism for this task.

  * **Option C — Violates Requirement:** Patching the application is the proper root-cause fix and should happen eventually, which makes it tempting. But waiting leaves PII flowing into new log entries until the release ships, which fails “as quickly as possible.”

  * **Option D — Violates Requirement:** Staging entries in Cloud Storage and rewriting them with a function would eventually remove the fields before they reach Cloud Logging, but it places the raw PII in a storage bucket, adds latency and moving parts, and takes far longer to build than an agent configuration change.

**Exam Trap**

The trap is the pair of nearly identical plugin names in Options A and B. The distinguishing facts are that A names a built-in Fluentd filter whose `remove_keys` parameter exists for exactly this purpose, while B names an add-on plugin framed at the output stage. The other temptation is Option C, which is right for permanent remediation. If the question had asked for the long-term root-cause fix, patching the application would become the answer, and in practice you would do both.

**Foundation Concept**

Sensitive data is best controlled as early as possible, at the point where records are produced or collected, because anything written to a central log store is harder to remove and may be widely readable. Agent-side processing lets you filter or transform records before ingestion. The exam item is framed around the legacy Logging agent, which is Fluentd-based. Google recommends the Ops Agent as the current agent for Compute Engine, and it is configured through YAML receivers, processors, and pipelines. Google has also announced that standard maintenance for the legacy agents ended on September 28, 2026, with a 12-month migration grace period, so a real-world fix should plan for that move.

**Real-World Connection**

An operator adds a `record_transformer` filter with `remove_keys` for the fields that carry email addresses and account numbers, rolls it out to the affected VMs through configuration management, and restarts the agent. New entries stop containing the fields within minutes while developers prepare the application fix. A configuration typo could interrupt log ingestion, so the change is tested on one VM first, and the team must separately decide what to do about the PII already stored.

**Memory Hook**

Scrub at the source: remove the fields in the agent before the log entry is written.

**30-Second Exam Takeaway**

When PII must stop appearing in new log entries immediately, change the agent’s configuration to drop the fields in flight, using the Fluentd record_transformer filter’s remove_keys on the legacy agent. Waiting for a code patch or building a separate cleanup pipeline is slower and leaves exposure in the meantime.

**Official References**

[Fluentd — record_transformer filter plugin: ](https://docs.fluentd.org/filter/record_transformer)Supports: the correct-answer mechanism (filter_record_transformer is included in Fluentd core, and its remove_keys parameter deletes listed keys from records in flight) and the contrast with Option B’s separately installed plugin

[Google Cloud — Logging agent configuration: ](https://docs.cloud.google.com/logging/docs/agent/configuration)Supports: that the Logging agent google-fluentd is a modified Fluentd collector configured through Fluentd plugins and configuration files, which makes the Fluentd filter the applicable control point

[**Google Cloud — Cloud Monitoring agent overview (legacy agent phase-out):**](https://docs.cloud.google.com/monitoring/agent) Supports: the lifecycle note that the legacy Monitoring and Logging agents are being phased out in favor of the Ops Agent, with standard maintenance ending September 28, 2026

---

## Question 42

*Domain 3: Applying Site Reliability Engineering Practices*

You support a popular mobile game application deployed on Google Kubernetes Engine (GKE) across several Google Cloud regions, and each region has multiple Kubernetes clusters. You receive a report that none of the users in one specific region can connect to the application. You want to resolve the incident in line with Site Reliability Engineering (SRE) practices. What should you do first?

- [x] A. Redirect user traffic from the affected region to the other regions that report no issues.
- [ ] B. Use Cloud Monitoring to look for a spike in CPU or memory usage in the affected region.
- [ ] C. Add a node pool of high-memory, high-CPU machine type instances to the cluster.
- [ ] D. Use Cloud Logging to filter on the affected region’s clusters and inspect the error messages in the logs.

### Explanation

**Correct Answer**

**A. Redirect user traffic from the affected region to the other regions that report no issues.**

**Exam Reasoning Explanation**

The word “first” makes this a sequencing question, and the SRE rule for incidents is to limit user impact before investigating the cause. Sort the options into two groups: those that restore service for users now, and those that gather information or attempt a fix. Then ask whether a restoring option is available. Multiple healthy regions exist, so redirecting users is possible and fast. Every investigative or speculative action therefore comes later, because users remain unable to connect while you perform it.

**Key Exam Clues**

  * “none of the users in a specific region can connect” — technical signal: total impact confined to one region, which makes the region a clear unit to isolate or drain.

  * “across several Google Cloud regions” with multiple clusters each — technical signal: redundancy exists, so healthy regions can serve the affected users.

  * “following Site Reliability Engineering practices” — hard constraint: mitigation takes priority over root-cause analysis during an incident.

  * “What should you do first?” — sequence instruction: the first action must reduce user impact, and diagnosis belongs after it.

**Why This Is Correct**

Redirecting traffic away from the failing region restores service to users within the time it takes to change routing, without needing to know why the region failed. This follows Google’s SRE guidance that the first response in a major outage should be to make the system work as well as it can under the circumstances, for example by diverting traffic from a broken cluster to others, and not to chase the root cause immediately. It also preserves the failing region intact for investigation afterward. One prerequisite is that the remaining regions must have enough capacity headroom to absorb the redirected load, since overloading them would spread the outage.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Technically Possible but Not Best:** Checking CPU and memory in the affected region is a sound diagnostic step, which is why it is tempting. But it only examines one hypothesis, and users remain unable to connect for as long as the investigation takes, so it belongs after mitigation.

  * **Option C — Violates Requirement:** Adding larger instances assumes the problem is a capacity shortage, which has no supporting evidence. It takes time, adds cost, and may not address a connectivity failure at all, so it is a guess that leaves users down.

  * **Option D — Technically Possible but Not Best:** Inspecting logs is the reflexive first move in troubleshooting, and it will eventually be needed to find the cause. As a first action it delays relief for users, and it can be done more calmly once traffic is flowing to healthy regions.

**Exam Trap**

The strongest distractor is Option D, because looking at logs feels like the natural start of any investigation. The distinction is that SRE separates mitigation from diagnosis, and Google’s guidance explicitly tells responders to resist the instinct to start with root-cause hunting. If the question had asked what to do next, after traffic was moved, then inspecting logs and metrics in the affected region would be the right answer.

**Foundation Concept**

An incident has distinct phases: detect, mitigate, diagnose, fix, and learn. Mitigation reduces user impact using fast, reversible actions such as draining or redirecting traffic, rolling back a change, or adding capacity, and it does not require understanding the cause. Diagnosis and the permanent fix follow once users are protected. Multi-region redundancy exists so that one region’s failure can be absorbed by others, but that only works if capacity and routing controls were prepared in advance.

**Real-World Connection**

An on-call engineer sets the affected region’s weight to zero in the global load balancer or traffic management layer and watches saturation in the healthy regions. Players reconnect within minutes through other regions, at somewhat higher latency. The team then examines logs and metrics in the isolated region, fixes the fault, and shifts traffic back gradually. The main risk is overloading the receiving regions, so their headroom is checked before and during the shift.

**Memory Hook**

Stop the bleeding first, then find the cause.

**30-Second Exam Takeaway**

In “what should you do first” incident questions, choose the fast mitigation that restores user service, such as redirecting traffic or rolling back. Diagnostic steps like checking logs and metrics, and speculative fixes like adding capacity, come after impact is reduced.

**Official References**

[**Google SRE Book — Effective Troubleshooting:**](https://sre.google/sre-book/effective-troubleshooting/) Supports: the correct-answer mechanism, since it advises that the first response to a major outage is to make the system work as well as possible, for example by diverting traffic from a broken cluster, instead of immediately seeking the root cause, which eliminates options B, C, and D as first steps

[Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide: ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment to Section 3.3, “Mitigating incident impact on users,” which lists draining or redirecting traffic, adding capacity, and rollback strategies

---

## Question 43

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

A government agency requires application logs to be archived for seven years. Cloud Logging needs to be configured so that the logs are exported and stored while keeping storage costs as low as possible. What should be done?

- [ ] A. Create a Cloud Storage bucket, and build the application so it sends its logs directly to that bucket.
- [ ] B. Build an App Engine application that pulls the logs out of Cloud Logging and writes them into BigQuery.
- [ ] C. Create an export in Cloud Logging, and configure Pub/Sub to retain the logs in permanent storage for seven years.
- [x] D. Create a named sink in Cloud Logging, create a Cloud Storage bucket to hold the archived logs, and set that bucket as the sink’s export destination.

### Explanation

**Correct Answer**

**D. Create a named sink in Cloud Logging, create a Cloud Storage bucket to hold the archived logs, and set that bucket as the sink’s export destination.**

**Exam Reasoning Explanation**

Two constraints matter here: a seven-year retention requirement, and minimizing storage cost. Those two together point squarely at long-term, infrequently accessed “cold” storage rather than an analytics-ready store or a messaging layer. Cloud Logging already has a native, built-in mechanism for this exact job — a sink that routes matching log entries to an external destination — so any option that bypasses that mechanism in favor of custom application code is adding unnecessary engineering effort without buying anything. Among the destinations a sink can target, Cloud Storage is the one purpose-built and priced for durable long-term archival; BigQuery is priced and optimized for querying, and Pub/Sub isn’t storage at all. The decision resolves to: use the native sink mechanism, and point it at the one destination actually designed for cheap, durable, multi-year retention.

**Key Exam Clues**

  * “archive application logs for seven years” — a long-duration, infrequent-access retention requirement, which favors cold/archival storage over an analytics store.

  * “minimizing costs of storage” — a hard constraint that rules out any option carrying unnecessary compute, query, or engineering overhead on top of the raw storage cost.

  * “configure Stackdriver [Cloud Logging] to export and store the logs” — signals the intended mechanism is the native log export (sink) feature, not custom application-level logging code.

**Why This Is Correct**

A Cloud Logging sink is the documented, built-in way to continuously route a filtered stream of log entries to an external destination without writing or maintaining any extra application code. Of the destination types a sink supports, Cloud Storage is explicitly the one intended for long-term log storage, and a Cloud Storage bucket can be set to a low-cost storage class suited to data that is rarely accessed but must be retained for years — directly satisfying both the seven-year retention requirement and the cost-minimization requirement in a single, fully managed configuration.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** writing logs directly from the application to a Cloud Storage bucket bypasses Cloud Logging’s native export mechanism entirely. It requires custom application code to implement and maintain, forfeits the filtering, reliability, and centralized routing Cloud Logging sinks already provide, and doesn’t actually “configure” Cloud Logging to export anything — it reinvents a feature that already exists.

  * **Option B — Technically Possible but Not Best:** this also discards the native sink mechanism in favor of a custom App Engine application that has to be built and operated just to pull logs out. On top of that engineering overhead, BigQuery is priced and designed for analysis and querying, not for minimizing the cost of seven years of rarely-touched archival data — it is a more expensive and more complex choice than necessary for this requirement.

  * **Option C — Incorrect:** Pub/Sub is a messaging and streaming service, not a durable storage service, and its message retention tops out at a matter of weeks, nowhere near the seven years the agency requires. An export can legitimately target Pub/Sub, but Pub/Sub cannot hold onto those messages for anywhere close to the required duration, making this option technically infeasible as written.

**Exam Trap**

The trap is treating “a valid sink destination” as interchangeable with “a place to store data long-term.” Pub/Sub is a perfectly legitimate export destination for streaming logs to other applications in near real time, which can make it look plausible here — but it was never built to retain data, only to deliver it, and its retention limits make it unusable for a multi-year archival mandate. The decisive move is checking whether the destination is actually a storage service at all, not just whether it can receive exported logs.

**Foundation Concept**

Cloud Logging’s export (sink) mechanism can route a filtered set of log entries to a Cloud Logging bucket, a Cloud Storage bucket, a BigQuery dataset, or a Pub/Sub topic. Each destination is optimized for a different purpose: Cloud Storage for durable, low-cost long-term retention; BigQuery for analysis and querying; Pub/Sub for streaming logs onward to other systems or applications. Matching the destination type to the actual need — in this case, cheap, durable, multi-year storage — is the core design decision behind configuring log exports well.

**Real-World Connection**

Routing a Cloud Logging sink to a Cloud Storage bucket, and configuring that bucket with a lower-cost storage class suited to infrequently accessed archival data, lets an organization meet a multi-year compliance retention mandate at a fraction of what the same volume of logs would cost sitting in an actively queried BigQuery table — while avoiding the ongoing operational burden of running and maintaining a custom log-export application.

**Memory Hook**

For “store it cheaply for years,” use a Cloud Logging sink into a Cloud Storage bucket — Pub/Sub moves logs, it doesn’t keep them, and BigQuery is priced for querying, not cold archival.

**30-Second Exam Takeaway**

When a Cloud Logging question asks for low-cost, long-term log retention, favor the native sink-to-Cloud-Storage pattern over custom application code, BigQuery, or Pub/Sub; remember that Pub/Sub specifically cannot provide durable, multi-year storage at all.

**Official References**

[**Google Cloud — Configure and manage log exports (sinks):**](https://cloud.google.com/logging/docs/export/configure_export_v2) Supports: the correct-answer mechanism (a sink routing logs to a Cloud Storage bucket) and the elimination of Options A and B

[**Google Cloud — Configure message retention for a Pub/Sub subscription:**](https://cloud.google.com/pubsub/docs/subscription-message-retention) Supports: the maximum retention limit that eliminates Option C as technically infeasible for seven-year storage

---

## Question 44

*Domain 3: Applying Site Reliability Engineering Practices*

You support a service that recently suffered an outage. A new release that exhausted the service’s memory resources caused it, and you successfully rolled the release back to limit the impact on users. You are now responsible for the post-mortem and want to follow Site Reliability Engineering (SRE) practices while developing it. What should you do?

- [ ] A. Concentrate on building new features instead of preventing the outage from recurring.
- [x] B. Concentrate on identifying the contributing causes of the incident instead of the individual responsible for it.
- [ ] C. Schedule one-on-one meetings with every engineer involved, and establish who approved and pushed the new release to production.
- [ ] D. Use the Git history to locate the related code commit, and bar the engineer who made it from working on production services.

### Explanation

**Correct Answer**

**B. Concentrate on identifying the contributing causes of the incident instead of the individual responsible for it.**

**Exam Reasoning Explanation**

The impact has already been mitigated by the rollback, so the remaining question is what the post-mortem is for: learning and preventing recurrence. Apply the SRE test to each option by asking what it directs attention toward, systems and processes or individuals. The memory exhaustion reached production because some control failed to catch it, so the useful question is which controls were missing, not which person was involved. Only one option aims the investigation at causes in the system, and the others either drop the prevention goal or hunt for a person.

**Key Exam Clues**

  * “follow Site Reliability Engineering practices when developing the post-mortem” — technical signal: SRE post-mortems are blameless and focus on learning from failure.

  * “new release that exhausted the service memory resources” — technical signal: the defect passed through the release process, so the analysis should examine why existing controls did not catch it.

  * “rolled back the release successfully to mitigate” — context clue: the incident is over, and the remaining work is understanding and preventing recurrence.

**Why This Is Correct**

A blameless post-mortem identifies the contributing causes of an incident without indicting any individual or team for bad or inappropriate behavior. In this case that means asking questions such as why a memory-exhausting change passed testing, why the rollout did not surface the problem before full exposure, and why monitoring did not flag memory pressure sooner. The answers produce systemic action items, such as memory regression tests, resource-limit checks, or longer canary phases, that prevent a similar release from reaching users regardless of who wrote or approved it. Google’s experience is that a truly blameless post-mortem culture produces more reliable systems, partly because people who are not afraid of punishment report problems honestly.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** A post-mortem exists to document what happened and drive actions that reduce the chance or impact of recurrence. Prioritizing new features over that work leaves the underlying gap open, so the same class of outage can return.

  * **Option C — Violates Requirement:** Talking with the engineers involved is a normal way to gather facts, which makes this tempting. But the stated purpose is to establish who approved and pushed the release, which turns the exercise into a search for responsibility and discourages candid accounts.

  * **Option D — Violates Requirement:** Barring the engineer who made the commit is punitive and treats one person as the cause. It teaches others to hide mistakes, and it fixes nothing in the system, so the same change could be made by someone else.

**Exam Trap**

The strongest distractor is Option C, because collecting information from the people involved looks like diligence. The distinction is the objective: reconstructing what happened and why is blameless, while determining who approved and pushed the release is attribution of fault. If the same meetings aimed to rebuild the timeline and the decision context without assigning fault, they would be consistent with SRE practice.

**Foundation Concept**

People respond to incentives, so if reporting a mistake leads to punishment, problems are hidden and the organization stops learning. Blameless post-mortems separate accountability for improving the system from blame for individuals, and they treat human error as a symptom of gaps in tooling, testing, review, or monitoring. A good post-mortem records impact, timeline, contributing causes, and concrete action items that have owners and are tracked to completion.

**Real-World Connection**

After a release exhausts memory and is rolled back, the team writes a post-mortem that lists contributing causes: a leak in a new code path, no soak test, a canary period too short to show growth, and no alert on memory trend. Action items add a memory regression test and a resource-saturation alert and lengthen the canary stage, each with an owner and a due date. The document is shared widely so other teams can learn from it, and engineers continue to report issues honestly.

**Memory Hook**

Ask what failed in the system, not who failed.

**30-Second Exam Takeaway**

For SRE post-mortem questions, pick the blameless answer that analyzes contributing causes and drives systemic fixes. Reject answers that single out, question, or sideline individuals, and answers that skip prevention work.

**Official References**

[Google SRE Book — Postmortem Culture: Learning from Failure: ](https://sre.google/sre-book/postmortem-culture/)Supports: the correct-answer mechanism (blameless post-mortems that focus on contributing causes without indicting individuals or teams) and the elimination of Options C and D

[**Google SRE Workbook — Postmortem Culture: Learning from Failure:**](https://sre.google/workbook/postmortem-culture/) Supports: the link between a blameless post-mortem culture and more reliable systems, and the need for action items that prevent recurrence, which eliminates Option A

---

## Question 45

*Domain 2: Building and Implementing CI/CD Pipelines*

You use Cloud Build to build and deploy your application. You want to incorporate database credentials and other application secrets into the build pipeline securely, while keeping development effort to a minimum. What should you do?

- [ ] A. Create a Cloud Storage bucket that relies on built-in encryption at rest, store the secrets in it, and grant Cloud Build access to the bucket.
- [ ] B. Encrypt the secrets and keep them in the application repository, keep the decryption key in a separate repository, and grant Cloud Build access to that repository.
- [ ] C. Encrypt the secrets on the client side and store them in a Cloud Storage bucket, keep the decryption key in the same bucket, and grant Cloud Build access to the bucket.
- [x] D. Use Cloud Key Management Service (Cloud KMS) to encrypt the secrets and reference them in your Cloud Build deployment configuration, and grant Cloud Build access to the key ring.

### Explanation

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

---

## Question 46

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

A trading application is written in Python and runs on App Engine flexible environment. The team wants to customize the error details that are sent to Error Reporting. What should be done?

- [ ] A. Install the Error Reporting library for Python, and run the application on a Compute Engine VM instead.
- [ ] B. Install the Error Reporting library for Python, and run the application on Google Kubernetes Engine instead.
- [ ] C. Install the Error Reporting library for Python, and continue running the application on App Engine flexible environment.
- [x] D. Use the Error Reporting API to write application errors as ReportedErrorEvent objects, generating properly formatted log entries in Cloud Logging.

### Explanation

**Correct Answer**

**D. Use the Error Reporting API to write application errors as ReportedErrorEvent objects, generating properly formatted log entries in Cloud Logging.**

**Exam Reasoning Explanation**

The hard constraint here is the word “customize.” Nothing in the scenario asks for a platform change, so any option that relocates the application off App Engine flexible is solving a problem that was never posed — that eliminates A and B immediately. Between the two remaining options, the question becomes: does installing the client library and letting it run give you control over _what_ gets reported, or does it just give you default, automatic capture? Error Reporting’s default integrations (including the one built into App Engine flexible) and the client library’s convenience methods populate a fixed, standard set of fields. Full control over the content of an error event — the actual “customization” the scenario asks for — comes from constructing the ReportedErrorEvent payload yourself and submitting it, either directly through the Error Reporting API or as a correspondingly formatted Cloud Logging entry.

**Key Exam Clues**

  * “hosted on App Engine flexible environment” — establishes the current platform; no requirement in the stem calls for changing it, so platform-migration options are suspect by default.

  * “customize the error information being sent” — the decisive phrase; it specifically asks for control over the content/shape of the error data, not just enabling error capture.

  * Single-select “What should you do?” — only one action is expected, so the correct option must fully satisfy the customization requirement on its own.

**Why This Is Correct**

Reporting errors as ReportedErrorEvent objects — either by calling the Error Reporting API’s `report` method directly, or by writing a Cloud Logging entry whose payload is formatted to match the ReportedErrorEvent schema — gives the application full control over every field Error Reporting receives: the error message, service name and version, HTTP request context, affected user, and report location. This is the documented extensibility point for anything beyond default exception capture, and the API automatically turns these calls into properly structured log entries that Error Reporting parses and groups. That combination — direct construction of the event plus automatic, correctly formatted logging — is what “customizing the error information being sent” actually means in Error Reporting.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Different Use Case:** migrating the application to a Compute Engine VM is an unnecessary and disruptive platform change that the scenario never asked for, and it still doesn’t address customization — it only relocates where the same default library behavior would run.

  * **Option B — Different Use Case:** migrating to Google Kubernetes Engine has the identical problem as A — an unrequested platform migration that leaves the actual “customize the error data” requirement unresolved.

  * **Option C — Technically Possible but Not Best:** installing the library and running on App Engine flexible is largely redundant, since Error Reporting is already automatically enabled there with no additional setup required. More importantly, the library’s convenience calls (such as reporting an exception or a simple message) populate only the standard default fields; they don’t give the application the fine-grained control over the event’s content that “customize” calls for.

**Exam Trap**

The trap is equating “install the client library” with “customize the error data.” The library is the easy path to default, automatic error capture — it is not, by itself, a customization mechanism. The moment a scenario asks specifically for custom error content, the correct move shifts from the convenience wrapper to directly building the underlying ReportedErrorEvent object, whether through the API or a matching Cloud Logging entry.

**Foundation Concept**

Error Reporting is built on top of Cloud Logging: it continuously analyzes log entries for a recognizable error structure (a stack trace, or a payload shaped like a ReportedErrorEvent) and groups matching entries into error events. There are two ways to produce that structure — let a platform integration or client library populate it automatically with standard fields, or construct it yourself for full control. The second path is the one the platform explicitly documents for custom error events.

**Real-World Connection**

A trading application might need each error enriched with operational context a default exception capture won’t include — which trading desk or order ID was affected, which upstream dependency call failed, or a custom severity classification tied to trade risk. Building the ReportedErrorEvent directly lets the team attach exactly that context to every error, which materially speeds up triage during a live incident on a time-sensitive system.

**Memory Hook**

Installing the library gives you default error capture; constructing the ReportedErrorEvent yourself gives you customized error capture — when the ask is “customize,” go to the object, not just the install.

**30-Second Exam Takeaway**

When an Error Reporting (or similar observability) question’s decisive word is “customize,” look past the “install the client library and run it somewhere” options and favor the one that directly constructs the underlying event or log payload — that’s where control over content actually lives.

**Official References**

[**Google Cloud — Format a log entry to report error events:**](https://cloud.google.com/error-reporting/docs/formatting-error-messages) Supports: the correct-answer mechanism (ReportedErrorEvent via the Error Reporting API or a formatted Cloud Logging entry)

[**Google Cloud — Setting up Error Reporting on App Engine flexible environment:**](https://cloud.google.com/error-reporting/docs/setup/app-engine-flexible-environment) Supports: elimination of Options A, B, and C by confirming Error Reporting is automatically enabled on App Engine flexible with no additional setup

---

## Question 47

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

A company builds several applications that run on Google Kubernetes Engine (GKE), with each application owned by a separate team. The organization needs development and production environments for every team while keeping overall spend as low as possible, and no team should be able to reach another team’s environment. Which approach should be taken?

- [ ] A. Provision a separate Google Cloud project for each team, and within every project create one GKE cluster for Development and a second for Production; grant each team IAM permissions scoped to its own clusters.
- [ ] B. Provision a separate Google Cloud project for each team, and within every project create a single GKE cluster containing one Kubernetes namespace for Development and another for Production; grant each team IAM permissions scoped to its own cluster.
- [ ] C. Provision one shared Development GKE cluster and one shared Production GKE cluster, each in its own project, and create a Kubernetes namespace per team inside every cluster; restrict each team to its own namespace by configuring Identity-Aware Proxy.
- [x] D. Provision one shared Development GKE cluster and one shared Production GKE cluster, each in its own project, and create a Kubernetes namespace per team inside every cluster; restrict each team to its own namespace by configuring Kubernetes role-based access control (RBAC).

### Explanation

**Correct Answer**

**D. Provision one shared Development GKE cluster and one shared Production GKE cluster, each in its own project, and create a Kubernetes namespace per team inside every cluster; restrict each team to its own namespace by configuring Kubernetes role-based access control (RBAC).**

**Exam Reasoning Explanation**

Two hard constraints govern this scenario: minimize cost, and enforce hard isolation between teams. Everything else (how many clusters, which access-control tool) is a means to those ends, not a requirement in itself. Start from cost: GKE bills a per-cluster management fee regardless of cluster size, so the number of clusters — not the number of projects — drives the cluster portion of the bill. Any design that creates a cluster (or cluster pair) per team scales cost linearly with team count; a design that shares two clusters (one Development, one Production) across all teams does not. That eliminates A and B as cost-optimal. From there, the remaining decision is which mechanism correctly restricts a team to only its own namespace inside a shared cluster — and only Kubernetes RBAC operates at that object level; IAP does not.

**Key Exam Clues**

  * “while minimizing costs” — a hard constraint that rules out any option whose cluster count scales with the number of teams.

  * “Different teams should not be able to access other teams’ environments” — a hard constraint requiring a mechanism that actually enforces namespace-level boundaries, not just convenience.

  * “configure Identity-Aware Proxy” vs. “configure Kubernetes Role-based access control (RBAC)” — the single technical-signal phrase that separates the two lowest-cost options (C and D) from each other.

**Why This Is Correct**

Sharing one Development cluster and one Production cluster across every team caps the cluster-management-fee exposure at two clusters total, independent of how many teams exist. Namespaces then give each team its own logical partition for objects (Pods, Services, ConfigMaps, and so on) inside those shared clusters, at no additional infrastructure cost. Kubernetes RBAC is the mechanism built to authorize actions against those in-cluster objects: a Role scoped to a namespace, bound to a team’s users or group via a RoleBinding, lets GKE grant or deny access to exactly that namespace and nothing else. That combination — shared clusters, namespace partitioning, RBAC enforcement — satisfies both constraints simultaneously.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** a dedicated cluster pair per team does achieve isolation through project and IAM boundaries, but it multiplies the per-cluster management fee by the number of teams, directly violating the cost-minimization requirement.

  * **Option B — Technically Possible but Not Best:** collapsing each team down to one cluster (instead of two) is an improvement over A, but it still creates one cluster per team rather than two shared clusters total, so cluster costs still scale with team count. It also relies on project-level IAM to gate the whole cluster rather than using RBAC to gate the namespace, which is coarser than necessary now that namespaces are already in play.

  * **Option C — Incorrect:** this option gets the cost structure right (two shared clusters, namespace per team) but names the wrong enforcement tool. Identity-Aware Proxy authorizes HTTPS requests to applications sitting behind Cloud Run, App Engine, or Cloud Load Balancing — it has no concept of a Kubernetes namespace and cannot authorize `kubectl` or Kubernetes API Server requests. It cannot deliver the stated isolation requirement at all.

**Exam Trap**

The trap is conflating two Google Cloud access-control tools that sound similar but operate at different layers: IAP governs identity-based access to HTTP(S) applications and infrastructure endpoints (VMs, load-balanced web apps), while Kubernetes RBAC governs authorization for objects inside the Kubernetes API itself. A scenario that explicitly says “namespace” is signaling the Kubernetes API layer — that should immediately point toward RBAC (or cluster-level IAM) and away from IAP. The distractor would only become defensible if the requirement shifted from “restrict access to a namespace” to “restrict access to a web application exposed from the cluster,” which is a materially different ask.

**Foundation Concept**

GKE access control operates on two cooperating layers. Google Cloud IAM governs access at the Google Cloud resource level — primarily the project containing the cluster — and is what determines whether a principal can reach the cluster at all. Kubernetes RBAC governs access to objects inside the cluster’s API, scoped either to a single namespace (via a Role/RoleBinding) or cluster-wide (via a ClusterRole/ClusterRoleBinding). GKE checks RBAC policy first and falls back to IAM permissions, and in nearly all multi-tenant designs, RBAC is the right tool once you’ve decided to share a cluster across tenants. IAP sits in an entirely separate control plane for securing HTTP(S)-reachable applications, not the Kubernetes control plane.

**Real-World Connection**

Choosing shared clusters with namespace-scoped RBAC lowers the cluster-management bill and centralizes platform operations (upgrades, node pool management, security patching) into two cluster lifecycles instead of dozens — a real operational win for a platform team. The trade-off is that RBAC alone does not stop a noisy or misconfigured team from consuming a disproportionate share of shared node capacity; production designs typically pair namespace RBAC with ResourceQuotas and NetworkPolicies to keep teams from affecting each other’s reliability, not just their authorization boundary.

**Memory Hook**

IAP guards the front door to web applications; Kubernetes RBAC guards the namespace door inside the cluster — when the ask is “restrict access to a namespace,” reach for RBAC.

**30-Second Exam Takeaway**

When a GKE scenario asks for low-cost multi-team isolation, favor the design with the fewest clusters (shared Dev/Prod clusters, namespace per team) over one cluster or cluster pair per team, and verify the proposed access-control tool actually operates at the Kubernetes API/namespace level rather than at the HTTP application layer.

**Official References**

[**Google Cloud — Control access to GKE clusters using Kubernetes RBAC:**](https://cloud.google.com/kubernetes-engine/docs/role-based-access-control) Supports: the correct-answer mechanism (namespace-scoped Role/RoleBinding authorization) and the elimination of Option C

[**Google Cloud — Identity-Aware Proxy overview:**](https://cloud.google.com/iap/docs/concepts-overview) Supports: why IAP cannot enforce namespace-level access, eliminating Option C

[**Google Cloud — Google Kubernetes Engine pricing:**](https://cloud.google.com/kubernetes-engine/pricing) Supports: the per-cluster management fee basis for the cost-minimization requirement, eliminating Options A and B

---

## Question 48

*Domain 5: Optimizing Performance and Cost*

You manage several production systems that run on Compute Engine in the same Google Cloud project. Each system uses its own dedicated set of Compute Engine instances. You want to know how much it costs to run each system. What should you do?

- [ ] A. In the Google Cloud console, use the cost breakdown report to visualize costs for each system.
- [x] B. Apply a label specific to its system to every instance, enable Cloud Billing export to BigQuery, and query costs by label.
- [ ] C. Add metadata specific to its system to every instance, export Cloud Logging to BigQuery, and query costs based on the metadata.
- [ ] D. Name each virtual machine (VM) after its system, export usage reports to a Cloud Storage bucket, and configure the bucket as a BigQuery source to query costs by VM name.

### Explanation

**Correct Answer**

**B. Apply a label specific to its system to every instance, enable Cloud Billing export to BigQuery, and query costs by label.**

**Exam Reasoning Explanation**

Cost reporting needs two things: billing data that contains the costs, and an attribute on each cost line that identifies the system. Work from that. First ask where cost data lives, which rules out options that rely on logs or other non-billing data. Then ask whether the billing data can distinguish the systems, given that all of them share one project and so project-level grouping cannot separate them. The answer must therefore add a per-system attribute that Cloud Billing carries through to its cost records, and then provide a way to aggregate by it.

**Key Exam Clues**

  * “in the same Google Cloud project” — technical signal: project is not a usable grouping dimension, so a resource-level attribute is required.

  * “its own set of dedicated Compute Engine instances” — technical signal: each system maps cleanly onto a set of resources that can carry a system-specific label.

  * “how much it costs to run each of the systems” — hard constraint: the data source must be actual billed cost data, not usage or operational telemetry.

**Why This Is Correct**

A label is a key-value pair that you attach to a resource, and Google Cloud forwards label information to the billing system so charges can be broken down by label. Labeling every instance with a value that identifies its system, such as `system=<name>`, adds the missing dimension. Enabling Cloud Billing export to BigQuery then writes billing line items, including their labels, into a dataset, and a query that sums cost grouped by the label gives the cost of each system. Google’s labels documentation describes this exact use, finding the cost of a particular service by exporting usage and labels to BigQuery. One boundary is that only consistently labeled resources can be attributed, so unlabeled spend will appear separately and should be monitored.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** The built-in billing reports are valuable, which makes this tempting. As stated, though, there is nothing in the data that identifies a system, because everything shares a project and no label has been applied, so the report cannot split costs per system.

  * **Option C — Incorrect:** Instance metadata describes configuration and is not part of billing data, and Cloud Logging exports contain log entries, not charges. Querying that data cannot produce costs.

  * **Option D — Technically Possible but Not Best:** Naming VMs after systems and exporting usage reports builds an unusual pipeline around a naming convention. VM names are not how Cloud Billing attributes cost, and this path would require you to derive costs yourself, when Cloud Billing already exports cost data with labels to BigQuery.

**Exam Trap**

The strongest distractor is Option A, because the console’s billing reports are the quickest place to look at costs. The distinction is that a report can only group by dimensions present in the data, so the systems must be labeled first. If the instances were already labeled by system, the built-in billing reports, which can filter and group costs by resource label, would be a fast alternative to a BigQuery query.

**Foundation Concept**

Cost attribution works by attaching a dimension to each cost line item. Project, service, and SKU come with the billing data, while labels add custom dimensions such as system, team, or environment. Billing export to BigQuery makes those line items queryable at full detail, which supports custom grouping, dashboards, and chargeback or showback. Good practice is to define a consistent labeling scheme, apply it at provisioning time, and track unlabeled spend.

**Real-World Connection**

A team sets a `system` label on every instance through its infrastructure-as-code templates and enables Cloud Billing export to BigQuery. A scheduled query sums monthly cost by label and feeds a dashboard, so each system’s owner can see their spend. Shared costs, such as networking, need a separate allocation rule, and a periodic check for unlabeled resources keeps the data trustworthy.

**Memory Hook**

Label the resource, export the bill, and group the cost by label.

**30-Second Exam Takeaway**

To find costs per system within one project, apply system-specific labels to the resources, export Cloud Billing data to BigQuery, and query by label. Logs, metadata, and VM names are not billing dimensions, and built-in reports can only group by attributes that already exist.

**Official References**

[Google Cloud — Labels overview (Resource Manager): ](https://docs.cloud.google.com/resource-manager/docs/labels-overview)Supports: the correct-answer mechanism (labels are forwarded to billing, can be exported to BigQuery with usage, and are used to find the cost of a particular service), and the note that built-in billing reports can group by labels

[**Google Cloud — Export Cloud Billing data to BigQuery:**](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) Supports: how billing export writes cost data, including labels, to BigQuery so costs can be queried by label, which distinguishes options C and D

---

## Question 49

*Domain 3: Applying Site Reliability Engineering Practices*

A team is defining Service Level Objectives (SLOs) for a high-traffic, multi-region web application whose customers expect the service to be consistently available and fast. Customers are currently satisfied with both availability and performance. Over the trailing 28-day window, measurements show a 90th-percentile latency of 120 ms and a 95th-percentile latency of 275 ms. Which latency SLO should the team publish?

- [ ] A. Publish a 90th-percentile latency target of 100 ms and a 95th-percentile latency target of 250 ms.
- [ ] B. Publish a 90th-percentile latency target of 120 ms and a 95th-percentile latency target of 275 ms.
- [x] C. Publish a 90th-percentile latency target of 150 ms and a 95th-percentile latency target of 300 ms.
- [ ] D. Publish a 90th-percentile latency target of 250 ms and a 95th-percentile latency target of 400 ms.

### Explanation

**Correct Answer**

**C. Publish a 90th-percentile latency target of 150 ms and a 95th-percentile latency target of 300 ms.**

**Exam Reasoning Explanation**

The must-have constraint is that the published target has to leave room for normal variance — a service that is already running at 120 ms/275 ms cannot publish those exact numbers as its SLO without being perpetually one bad minute away from violating it. The second constraint, equally important, is that “customers are currently happy,” which anchors how much slack is appropriate: the target should stay close enough to today’s real performance that it still reflects what users actually experience, rather than drifting into territory where a real regression could hide behind a technically-met SLO. Evaluate each option against both constraints together, and only the option with a modest, proportionate buffer survives.

**Key Exam Clues**

  * “Customers are currently happy with the application performance and availability” — a signal that the published target should stay close to current measured values, ruling out an excessively loose target.

  * “90th percentile of latency is 120ms and the 95th percentile of latency is 275ms” — the baseline the recommended SLO must be benchmarked against, not copied.

  * “What latency SLO would you recommend to the team to publish” — asks for a target the team will defend going forward, which implies the target needs headroom (an error budget) rather than being a snapshot of current measurement.

**Why This Is Correct**

A target of 150 ms (p90) and 300 ms (p95) sits modestly above the measured 120 ms and 275 ms. That gap is the SLO’s error budget: it absorbs ordinary, expected variance in a high-traffic, multi-region system — traffic spikes, routine releases, minor infrastructure hiccups — without the service falling out of SLO on a routine basis. At the same time, the buffer is small enough that the target still tracks what satisfied customers are actually experiencing today, so a genuine regression (say, p90 latency drifting to 200 ms) would still trip the SLO well before users started noticing a meaningfully worse experience.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** a 100 ms / 250 ms target is tighter than the service’s own currently measured performance (120 ms / 275 ms). The service would already be out of SLO under normal, currently-satisfactory conditions, which makes the target unworkable from day one.

  * **Option B — Incorrect:** this sets the SLO to exactly the currently measured values, leaving zero buffer between achieved performance and the target. Any ordinary fluctuation in a high-traffic system would push the SLI past the SLO, triggering false alarms and unnecessary feature freezes despite customers being happy — this is the specific mistake SRE guidance warns against when it comes to choosing SLO targets.

  * **Option D — Technically Possible but Not Best:** 250 ms / 400 ms is more than double the current p90 and nearly 1.5x the current p95. That much slack would let the service’s real performance degrade substantially — well past the point where “currently happy” customers would stay happy — while still reporting as fully within SLO, defeating the purpose of the SLO as an early-warning signal tied to actual user experience.

**Exam Trap**

The trap in Option B is mistaking precision for rigor: measuring carefully and then publishing exactly what you measured feels disciplined, but it’s the canonical error SRE guidance calls out directly — a target with no buffer isn’t a target, it’s a tripwire. The trap in Option D is overcorrecting in the other direction, assuming “more margin is always safer,” when the stem’s “customers are currently happy” detail is precisely what tells you the margin shouldn’t be that large. The decisive test is always: does this target leave a believable, proportionate buffer over what’s actually being achieved?

**Foundation Concept**

A latency SLO should be set with intentional headroom above currently observed performance — enough to function as a real error budget, but not so much that the target stops reflecting genuine user experience. That buffer is what makes the SLO useful as a decision-making tool: small, expected fluctuations stay within budget, while real regressions still get caught early, and it also gives engineering room to make trade-offs elsewhere (cost, maintainability) that might cost a little latency without breaching the SLO.

**Real-World Connection**

With a 150 ms / 300 ms SLO in place, the team can ship a normal release that nudges p90 latency up a few milliseconds without burning through its error budget or triggering a reliability-first response — but a release or incident that pushes p90 toward 200 ms would still clearly violate the SLO, prompting investigation well before the degradation became severe enough for customers to complain.

**Memory Hook**

A latency SLO should sit a reasonable step above what’s currently measured — never exactly at it, and never so far above it that it stops meaning anything.

**30-Second Exam Takeaway**

When a question gives you current measured percentiles and asks what SLO to publish, eliminate the option that matches those numbers exactly (no error budget) and the option far looser than them (no longer reflects real user experience); the modest-headroom option is almost always correct.

**Official References**

[**Google SRE Book — Service Level Objectives (Choosing Targets):**](https://sre.google/sre-book/service-level-objectives/) Supports: the correct-answer reasoning and the elimination of Option B’s “set the target to current performance” anti-pattern

[**Google SRE Workbook — Implementing SLOs:**](https://sre.google/workbook/implementing-slos/) Supports: practical guidance on setting initial reliability targets and buffers for an error budget

---

## Question 50

*Domain 2: Building and Implementing CI/CD Pipelines*

An organization has recently moved to a container-based application development workflow, and the team builds many applications that are deployed continuously through an automated pipeline into production. A recent security audit found that code reaching production could contain vulnerabilities, and that the team’s existing virtual machine (VM) vulnerability tooling no longer applies now that workloads run in containers. The security and patch level of every piece of code moving through the pipeline needs to be assured. What should be done?

- [x] A. Set up Artifact Analysis to scan container images and report Common Vulnerabilities and Exposures (CVEs).
- [ ] B. Configure the containers in the build pipeline to automatically update themselves just before release.
- [ ] C. Reconfigure the existing operating-system vulnerability scanning software to run inside the containers themselves.
- [ ] D. Implement static code analysis tooling that scans the Dockerfiles used to build the containers.

### Explanation

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

---

## Question 51

*Domain 3: Applying Site Reliability Engineering Practices*

A web application hosted on Compute Engine provides a booking service to thousands of users. Shortly after a new feature is released, the monitoring dashboard shows every user experiencing elevated latency at login. The goal is to limit the impact of this incident on the service’s users. What should be done first?

- [x] A. Roll back the release that was just deployed.
- [ ] B. Review the Cloud Monitoring data in more depth.
- [ ] C. Increase the size of the virtual machines that run the login service.
- [ ] D. Deploy another new release to see whether it resolves the problem.

### Explanation

**Correct Answer**

**A. Roll back the release that was just deployed.**

**Exam Reasoning Explanation**

Two things anchor this question: the symptom began shortly after a new release, and the stated goal is to mitigate user impact, not to understand root cause. A tight timing correlation between a deploy and a new, universal symptom is strong evidence the release caused it, and when the likely cause of an incident is a recent change, SRE practice is to restore the last known-good state immediately rather than spend time investigating or risk introducing further change. Rolling back does exactly that: it’s the fastest, lowest-risk way to stop user impact given the evidence already in hand, which is what “what should you do first” is asking for.

**Key Exam Clues**

  * “Shortly after the release of a new feature... all users are experiencing latency” — a strong timing correlation between the deploy and the symptom, pointing to the release as the likely cause.

  * “mitigate the impact of the incident on the users” — the explicit goal is impact reduction, not root-cause diagnosis.

  * “What should you do first?” — a sequencing constraint favoring the fastest, safest corrective action over further investigation or additional risky changes.

**Why This Is Correct**

Rolling back the release immediately restores the application to the state it was in before the latency began, directly addressing the most probable cause without requiring any further diagnosis first. This mitigates the impact on the thousands of affected users as quickly as possible, which is the explicit goal stated in the question — consistent with SRE incident-response priority of restoring service first and investigating root cause afterward, once the system is stable again.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Technically Possible but Not Best:** reviewing monitoring data is a reasonable diagnostic activity, but it doesn’t itself reduce user impact, and the evidence already available — the tight timing correlation with the release — is already strong enough to justify acting. Spending time investigating further before taking the indicated corrective action delays mitigation without a clear need.

  * **Option C — Technically Possible but Not Best:** resizing the VMs assumes the problem is a capacity or resource constraint, but nothing in the scenario points to a load increase — the correlation is specifically with a code release, not traffic growth. Acting on that unverified assumption risks spending time and money without addressing the more probable actual cause.

  * **Option D — Violates Requirement:** deploying another release introduces more unverified change into a system that’s already experiencing an incident, rather than first stabilizing it. This runs directly counter to standard incident practice, which calls for restoring a known-good state before introducing any further changes.

**Exam Trap**

The trap in Option B is that “investigate before acting” sounds like the careful, responsible choice, but the question isn’t asking what’s generally prudent — it’s asking what mitigates user impact first, and the evidence already on hand (the tight timing correlation with a release) is sufficient to justify an immediate rollback. Waiting to confirm what’s already strongly indicated only prolongs the impact the question is asking you to minimize.

**Foundation Concept**

A central tenet of SRE incident management is limiting the disruption of an incident and restoring normal operation as quickly as possible — which is exactly why every rollout is expected to have a well-understood, well-tested rollback mechanism. When a recent change is strongly implicated, rolling it back is the standard fastest path to restoring service; a full root-cause investigation follows afterward, typically through a postmortem, once the immediate user impact has been addressed.

**Real-World Connection**

Rolling back the suspect release the moment users begin experiencing latency right after a deploy stops the impact on thousands of active logins immediately. The team can then investigate what specifically in the new feature caused the regression in a calmer, lower-pressure setting, rather than leaving users degraded while that investigation happens live in production.

**Memory Hook**

When a problem starts right after a release, mitigate first by rolling it back — don’t investigate further or ship more changes before restoring the known-good state.

**30-Second Exam Takeaway**

A strong timing correlation between a deploy and a new symptom, combined with a question asking what to do “first” to mitigate user impact, points to rolling back the suspect change rather than further diagnosis or an additional deployment.

**Official References**

[**Google SRE Book — Chapter 14, Managing Incidents:**](https://sre.google/sre-book/incident-response/) Supports: the core principle that effective incident management limits disruption and restores service as quickly as possible

[**Google Cloud Blog — Adventures in SRE-land: Incident management at Google:**](https://cloud.google.com/blog/products/gcp/incident-management-at-google-adventures-in-sre-land) Supports: rollback as the standard, well-tested mechanism for restoring service once a recent change is implicated in an incident

---

## Question 52

*Domain 2: Building and Implementing CI/CD Pipelines*

An application runs entirely on Google Cloud, and the team needs to stand up Jenkins to deploy application releases into that environment. The goals are to streamline the release process, reduce operational toil, and keep user data secure. What should be done?

- [ ] A. Run Jenkins on individual local workstations.
- [ ] B. Run Jenkins on a Kubernetes cluster hosted on-premises.
- [ ] C. Run Jenkins on Cloud Run functions.
- [x] D. Run Jenkins on Compute Engine virtual machines.

### Explanation

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

---

## Question 53

*Domain 3: Applying Site Reliability Engineering Practices*

A team operates a large service governed by a clearly defined Service Level Objective (SLO), and engineers ship new releases of that service several times each week. In the event that a significant incident pushes the service outside its SLO, the goal is for engineering effort to pivot away from feature work and toward restoring reliability. Which action should be taken in advance of any such incident?

- [x] A. Work with every service stakeholder to establish a suitable error budget policy ahead of time.
- [ ] B. Negotiate an agreement with the product team that service reliability will always take priority over shipping new features.
- [ ] C. Negotiate with the development team to cut the release cadence down to once a week at most.
- [ ] D. Introduce a plugin into the Jenkins pipeline that blocks new releases any time the service is outside its SLO.

### Explanation

**Correct Answer**

**A. Work with every service stakeholder to establish a suitable error budget policy ahead of time.**

**Exam Reasoning Explanation**

The hard constraint is timing: whatever mechanism makes the reliability-versus-features decision has to be agreed and in place _before_ the incident, so that nobody is negotiating priorities while the service is already broken. The soft constraint is sustainability: the organization still releases multiple times a week under normal conditions, so the mechanism can’t be a permanent brake on velocity — it has to be conditional on an objective trigger. An error budget policy satisfies both: it is written and agreed in advance, and it only forces a reliability-first posture once the budget is actually spent, leaving normal release cadence untouched the rest of the time. Options that either impose a permanent constraint (B, C) or implement only a narrow technical fragment of the policy (D) fail one of these two requirements.

**Key Exam Clues**

  * “deploys new releases of the service multiple times a week” — establishes that high release velocity is the normal, desired state, which rules out any option that permanently throttles releases as the default.

  * “If a major incident causes the service to miss its SLO” — defines an objective, data-driven trigger condition, which is exactly what an error budget policy is built to key off of.

  * “before a major incident occurs” — a hard constraint requiring the mechanism to be pre-agreed rather than negotiated reactively.

**Why This Is Correct**

An error budget policy is a document, agreed in advance by both the team building features and the team(s) accountable for reliability, that spells out exactly what happens as the error budget is consumed — up to and including redirecting engineering effort away from features and onto reliability work once the budget is exhausted. Because it is negotiated and signed off before any incident, it converts what would otherwise be an ad hoc, politically charged argument during a crisis into a pre-agreed, objective consequence that triggers automatically. That directly produces the outcome the scenario asks for: a clean shift in focus from features to reliability precisely when the SLO is missed, and normal behavior the rest of the time.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Violates Requirement:** committing to “always” prioritize reliability over features removes the balancing mechanism SRE is built around. Error budgets exist precisely so that reliability work is prioritized only when the data (budget burn) says it should be, not unconditionally — an absolute rule like this is neither what the scenario needs nor realistic for a product organization to accept.

  * **Option C — Technically Possible but Not Best:** capping release frequency addresses the symptom the question never raised. The stated problem is what happens _after_ a major incident causes an SLO miss, not that releases are currently too frequent; arbitrarily slowing down a healthy, well-functioning release cadence doesn’t target the actual trigger condition and sacrifices velocity even when the service is well within budget.

  * **Option D — Technically Possible but Not Best:** an automated release gate tied to SLO status is a reasonable _implementation detail_ that an error budget policy might eventually include, but introduced on its own it is a unilateral technical control rather than an agreement reached with stakeholders, and it only blocks releases — it does nothing to actually redirect engineering focus onto reliability work, run postmortems, or reallocate sprint capacity, which is the broader shift the scenario is asking for.

**Exam Trap**

The trap options sound protective of reliability but each oversimplifies the SRE balancing act: B swings too far by making reliability win unconditionally, and D swings too narrow by automating only the release-blocking piece without the surrounding stakeholder agreement. The decisive test is whether the option is both collaboratively agreed upon _and_ conditional on an objective trigger — only the error budget policy is both.

**Foundation Concept**

An error budget is the inverse of the SLO (roughly, 1 − SLO) — the quantified amount of unreliability a service is allowed to accumulate over a measurement window. On its own, that number is just a metric; the error budget policy is what gives it consequences, defining in advance what the team does as the budget is spent, including the point at which feature work pauses in favor of reliability work. This is the core SRE mechanism for resolving the structural tension between product development’s incentive to ship and reliability’s incentive to stay within SLO.

**Real-World Connection**

A team that has a signed-off error budget policy going into a major incident can redirect the next sprint’s capacity to reliability fixes immediately and without internal conflict, because the response was already agreed before anyone had a deadline or a launch on the line. Teams that skip this step typically end up re-litigating the reliability-versus-features trade-off incident by incident, which slows the response, breeds inconsistency, and makes recurring SLO misses more likely.

**Memory Hook**

When a question asks what to put in place _before_ an incident to make the reliability-versus-features call automatic, the answer is an error budget policy agreed with stakeholders — not a blanket rule, a fixed release cadence, or a single pipeline gate.

**30-Second Exam Takeaway**

SRE questions about balancing velocity and reliability almost always resolve to establishing an error budget (and its policy) with stakeholders in advance; treat “always prioritize X” absolutes and single-tool technical fixes as the standard distractor pattern.

**Official References**

[**Google SRE Book — Embracing Risk (Motivation for Error Budgets):**](https://sre.google/sre-book/embracing-risk/) Supports: the correct-answer mechanism and the rationale for why reliability work is prioritized conditionally rather than always

[**Google SRE Workbook — Example Error Budget Policy:**](https://sre.google/workbook/error-budget-policy/) Supports: what an error budget policy contains and how it operationalizes the shift from features to reliability work

---

## Question 54

*Domain 2: Building and Implementing CI/CD Pipelines*

Cloud Build is used to build an application, and the goal is to shorten the build time while keeping both cost and development effort as low as possible. What should be done?

- [x] A. Cache intermediate build artifacts in Cloud Storage between builds.
- [ ] B. Stand up multiple Jenkins agents to run the build in parallel.
- [ ] C. Break the build into multiple smaller steps to cut down execution time.
- [ ] D. Switch to a larger Cloud Build virtual machine (VM) using the machine-type option.

### Explanation

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

---

## Question 55

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

A team uses Cloud Logging to monitor applications running on Google Cloud. A newly deployed application’s logs are not showing up in Cloud Logging, and the issue needs to be troubleshot. What should be done?

- [x] A. Confirm that the Ops Agent has been installed on the virtual machine hosting the application.
- [ ] B. Confirm that the account being used has the permissions needed to view Cloud Logging.
- [ ] C. Confirm that port 25 has been opened in the firewall to allow traffic through to Cloud Logging.
- [ ] D. Confirm that the application is using the required client library and that its service account key has the proper permissions.

### Explanation

**Correct Answer**

**A. Confirm that the Ops Agent has been installed on the virtual machine hosting the application.**

**Exam Reasoning Explanation**

The symptom is specific: logs for one newly deployed application are entirely missing, not that the console or dashboard is inaccessible. That points toward a data-collection problem rather than a viewing-permission problem. Compute Engine VMs do not have the agent responsible for collecting and forwarding logs installed by default — it has to be explicitly installed on each VM. Since this is a newly deployed application, quite possibly on a newly created VM, the single most common and most fundamental explanation for a total absence of logs is that this agent was simply never installed, which is exactly why it’s the first thing official Google diagnostic tooling checks when a VM’s logs or metrics go missing.

**Key Exam Clues**

  * “recently deployed a new application” — a new or newly configured VM is a strong candidate for never having had the logging agent explicitly installed on it.

  * “its logs are not appearing” — specifically a data problem for one application’s logs, not a description of being locked out of the console entirely.

  * Single-select “What should you do?” — asking for the first, most fundamental thing to check.

**Why This Is Correct**

Compute Engine VM instances don’t ship with monitoring or logging agents pre-installed; the Ops Agent must be explicitly installed on a VM for its logs to be collected and sent to Cloud Logging. Because installing the agent is a separate, easy-to-forget step when standing up a new VM or application, it’s the standard, most common root cause whenever a VM’s logs are completely absent — and it’s precisely the first condition official Google troubleshooting tooling verifies when logs or metrics aren’t showing up for a Compute Engine instance.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Different Use Case:** a permissions problem on the viewing account typically prevents access to the Cloud Logging console itself, producing an access-denied experience rather than selectively missing data for one new application while the dashboard is otherwise usable. The described symptom doesn’t match what an account-permission issue would look like.

  * **Option C — Incorrect:** port 25 is the standard SMTP mail-relay port and has no role in how a logging agent communicates with Cloud Logging. This option names the wrong protocol entirely and doesn’t correspond to any real mechanism involved here.

  * **Option D — Technically Possible but Not Best:** checking the client library and service account permissions is a legitimate step for an application that writes logs directly through an API rather than relying on a VM-level agent, but given the scenario’s framing around “the hosting virtual machine,” the far more common and better-documented first failure mode for a VM-hosted application is simply that the collection agent itself was never installed.

**Exam Trap**

Option C sounds like a reasonable “check the firewall” instinct, but the specific port it names is simply wrong for the service involved — a classic plausible-sounding-but-factually-incorrect distractor. Option B generalizes “logs not appearing” into “an access problem,” when the described symptom — one new application’s data missing, not a broad inability to use the dashboard — points somewhere more specific.

**Foundation Concept**

Compute Engine VMs are not monitored or logged automatically. The Ops Agent — the unified successor to the earlier, separate Stackdriver Logging and Monitoring agents — must be explicitly installed on a VM in order for its logs and metrics to be collected and sent to Cloud Logging and Cloud Monitoring. Because this installation step can easily be skipped when a new VM or deployment is created, it’s the standard first thing to verify whenever a VM’s data is unexpectedly absent.

**Real-World Connection**

If a newly deployed application’s VM never had the Ops Agent installed, the application itself may be running fine and writing its own logs locally or to stdout, but nothing reaches Cloud Logging at all — from the console, it looks exactly like the application produces no logs, which is the symptom described. Installing and starting the agent on that VM typically resolves the issue immediately.

**Memory Hook**

No agent, no data — before chasing permissions or firewall ports, confirm the Ops Agent is actually installed and running on the VM.

**30-Second Exam Takeaway**

When a specific, newly deployed VM-hosted application’s logs are entirely missing from Cloud Logging, check first whether the Ops Agent is installed and running on that VM — it’s the most common root cause and the first condition official Google diagnostics verify.

**Official References**

[**Google Cloud — Ops Agent overview:**](https://cloud.google.com/logging/docs/agent/ops-agent) Supports: the correct-answer mechanism that the Ops Agent is what collects and sends a VM’s logs to Cloud Logging

[**Google Cloud — Find troubleshooting information for the Ops Agent:**](https://cloud.google.com/monitoring/agent/ops-agent/troubleshoot-find-info) Supports: confirming that checking whether the Ops Agent is installed and sending data is the standard first diagnostic step for missing VM logs

---

## Question 56

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

A company is standing up a new, cloud-native Google Cloud organization. It will initially be used by a small number of departments, then expand to support a large number of departments, each of which runs a large number of applications of varying sizes. The VPC network architecture needs to be designed so that it minimizes the amount of ongoing management required, while staying flexible enough for development teams to adapt quickly as their needs evolve. What should be done?

- [x] A. Give each department its own VPC, and connect those VPCs using VPC Network Peering.
- [ ] B. Give each department its own VPC, and use Private Service Connect to connect those VPCs.
- [ ] C. Give each application its own VPC, and use Private Service Connect to connect those VPCs.
- [ ] D. Give each department its own VPC, and connect those VPCs using Cloud VPN.

### Explanation

**Correct Answer**

**A. Give each department its own VPC, and connect those VPCs using VPC Network Peering.**

**Exam Reasoning Explanation**

Two constraints have to be satisfied together: minimal ongoing management, and enough flexibility for teams to adapt quickly without waiting on networking work. That combination favors a connectivity mechanism that operates at the whole-network level — connect two VPCs once, and every application in either one can reach the other without any further configuration — over a mechanism that has to be set up per application or per service. It also rules out any VPC-per-application structure outright, since the stated scale (“a large number of applications” per department, scaling to “a large number of departments”) would make that approach unmanageable regardless of which connectivity tool sits on top of it. Among the remaining whole-network options, the one actually built and documented for connecting Google Cloud VPCs to each other, running over Google’s own internal network, is VPC Network Peering.

**Key Exam Clues**

  * “minimize the amount of management required” — disfavors anything that has to be configured per application or per service, and disfavors a per-application VPC structure outright.

  * “flexible enough for development teams to quickly adapt” — favors a connectivity layer that grants broad reachability once established, so new applications don’t require new networking configuration.

  * “expand... to a large number of departments” and “a large number of applications” — a scale signal that should be weighed against each option’s native fit for intra-Google-Cloud connectivity, not just whether it technically works.

**Why This Is Correct**

VPC Network Peering is Google Cloud’s native mechanism specifically for connecting two VPC networks so that resources in each can communicate with each other, using internal IP addresses over Google’s own network rather than the public internet. Once two departmental VPCs are peered, every application already running in either VPC — and every application added to either VPC afterward — can reach the other side without any additional per-application setup. That satisfies both requirements at once: one peering relationship per pair of departments covers all current and future applications (minimizing management), and development teams can add new applications freely without touching the network layer (supporting fast adaptation).

**Why the Other Options Are Not the Best Fit**

  * **Option B — Incorrect:** Private Service Connect is documented as a way for consumers to privately access specific managed or published services, not as a mechanism for general inter-VPC network communication between customer-owned VPCs. Using it as the department-to-department connectivity layer would mean individually publishing and connecting each application or service as it’s created — more ongoing management as the application count grows, not less, directly working against the stated goal.

  * **Option C — Violates Requirement:** giving every application its own VPC multiplies the number of VPCs (and the connections needed between them) far beyond what’s manageable, given each department already runs a large number of applications. This fails the “minimize management” requirement on its own, independent of which connectivity mechanism is layered on top of it.

  * **Option D — Technically Possible but Not Best:** Cloud VPN is documented as encrypting traffic over the public internet and as being suited to low-volume data connections — a profile built for hybrid connectivity to an external network, not for linking VPCs that live entirely within Google Cloud. It adds tunnel and gateway configuration and encryption overhead without providing any connectivity advantage over native Peering for this all-cloud scenario.

**Exam Trap**

The trap is assuming the newer-sounding “Private Service Connect” must be the more modern, correct choice over “plain” VPC Peering — but PSC solves a different problem (narrowly exposing one service to specific consumers), and official guidance is explicit that it does not provide general inter-VPC communication between customer networks. A second trap is treating a VPC per application as inherently more secure or well-isolated without weighing it against the explicit “minimize management” requirement at the stated scale.

**Foundation Concept**

VPC Network Peering connects two entire VPC networks at the network level over Google’s internal backbone, giving every resource in each network reachability to every resource in the other — well suited to linking a department-scale set of VPCs with minimal per-workload configuration. Private Service Connect operates one layer down: it privately exposes and consumes individual services, which is the right tool for sharing one specific service narrowly, not for establishing broad reachability between two whole networks.

**Real-World Connection**

With departmental VPCs peered, a development team can deploy a brand-new internal application in their department’s VPC and have it immediately reachable from another department’s VPC with zero additional networking work, instead of waiting on a networking team to publish a new Private Service Connect endpoint for every new service — which is exactly the kind of fast, low-friction adaptation the scenario is asking for.

**Memory Hook**

Peering connects whole networks; Private Service Connect connects one published service at a time — for broad, low-maintenance department-to-department reachability, reach for Peering.

**30-Second Exam Takeaway**

When a VPC design question asks for minimal-management, broadly flexible connectivity between a moderate number of VPCs that live entirely within Google Cloud, favor native VPC Network Peering; rule out Private Service Connect for general inter-VPC connectivity (it’s for specific published services) and Cloud VPN for pure intra-Google-Cloud links (it’s built for internet-traversing, low-volume, hybrid connectivity).

**Official References**

[**Google Cloud — VPC Network Peering:**](https://cloud.google.com/vpc/docs/vpc-peering) Supports: the correct-answer mechanism for connecting whole VPC networks over Google’s internal network

[**Google Cloud — Private Service Connect overview:**](https://cloud.google.com/vpc/docs/private-service-connect) Supports: the elimination of Options B and C by confirming PSC’s purpose is private access to specific published/managed services, not general inter-VPC connectivity

[**Google Cloud — Cloud VPN documentation:**](https://cloud.google.com/network-connectivity/docs/vpn) Supports: the elimination of Option D by confirming Cloud VPN traverses the public internet via IPsec and is intended for low-volume data connections

---

## Question 57

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

A web application runs on App Engine and relies on Cloud SQL and Cloud Storage for data storage. After a brief spike in site traffic, request latency rises sharply for every user, along with higher CPU usage and a larger number of application processes. Investigation turns up the following:

  * Traffic levels return to normal after the spike, but elevated latency persists.

  * Requests that read from the Cloud SQL database and requests that fetch images from Cloud Storage show the same degree of added latency.

  * Nothing about the website’s code or configuration changed around the time latency began rising.

  * The error rate seen by users has not increased.

Another traffic spike is expected in the next few days, and the goal is to prevent users from experiencing that latency again. What should be done?

- [ ] A. Convert the Cloud Storage buckets to multi-regional storage.
- [ ] B. Turn on high availability for the Cloud SQL instances.
- [ ] C. Migrate the application off App Engine and onto Compute Engine.
- [x] D. Adjust the App Engine configuration to keep a larger pool of idle instances available.

### Explanation

**Correct Answer**

**D. Adjust the App Engine configuration to keep a larger pool of idle instances available.**

**Exam Reasoning Explanation**

The single most important piece of evidence is that Cloud SQL requests and Cloud Storage requests show the _same_ elevated latency. If either backend were the bottleneck, only requests touching that specific backend would slow down — the fact that two unrelated services are equally affected means the shared layer every request passes through, the App Engine instances themselves, is the actual bottleneck. Combine that with latency persisting after load already returned to normal, and the picture is an App Engine deployment that scaled instances down after the spike and is now paying a provisioning/startup cost whenever it has to scale back up to meet ordinary traffic — a cost every request incurs regardless of which backend it ultimately calls. The fix has to act on that shared layer, proactively, before the next anticipated spike.

**Key Exam Clues**

  * “Requests... from the Cloud SQL database and images from Cloud Storage show the same high latency” — the decisive clue: identical latency across two unrelated backends points to a shared upstream cause, not a backend-specific one.

  * “load levels returned to normal but users still experience high latency” — latency outlives the triggering spike, pointing to a lingering instance-capacity mismatch rather than an active load problem.

  * “No changes were made to the website” and “no increase in the number of errors” — rules out a code regression or an outage/overload condition; this is a pure latency issue tied to capacity, not correctness or availability.

**Why This Is Correct**

App Engine’s automatic scaler can reduce the number of running instances once traffic subsides, and bringing a new instance online to absorb renewed load takes measurable time to initialize. Configuring a minimum number of idle instances keeps a buffer of already-initialized, “warm” instances on standby at all times, so the next traffic spike is absorbed immediately instead of triggering a wave of cold instance starts. Because that initialization delay sits in front of every request — whichever backend it eventually calls — pre-warming capacity this way reduces latency uniformly for both Cloud SQL-backed and Cloud Storage-backed requests, exactly matching what was observed.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Different Use Case:** multi-regional Cloud Storage is about data durability and serving reads with low latency to users spread across multiple geographic regions, not about recovering from an App Engine instance-capacity shortfall. It also does nothing to explain or fix the matching latency seen on Cloud SQL requests, which share no infrastructure with a Cloud Storage bucket’s regional configuration.

  * **Option B — Different Use Case:** Cloud SQL high availability exists specifically to reduce downtime during a zonal or instance failure by failing over to a standby instance — it is not a performance or latency feature, and there’s no sign of a Cloud SQL outage here (no increase in errors). It also can’t account for the identical latency on Cloud Storage requests, which an HA setting on Cloud SQL has no influence over at all.

  * **Option C — Technically Possible but Not Best:** moving the application to Compute Engine would work eventually, but it means giving up App Engine’s managed autoscaling and deployment automation and rebuilding that capacity-management logic manually — a disproportionate, disruptive response when the same platform already exposes the exact configuration knob (idle instances) needed to solve this.

**Exam Trap**

The trap is reaching for a backend-specific fix because the stem names Cloud SQL and Cloud Storage explicitly — it’s tempting to “fix the database” or “fix the storage.” The clue that both backends show the identical latency increase is what rules that out: a real backend-specific issue would show up on only one of them. That detail should redirect attention to the one layer common to every request, the App Engine instances serving them.

**Foundation Concept**

App Engine’s automatic scaling adjusts the number of running instances to match demand, scaling down aggressively once load drops to control cost. Provisioning a new instance when demand rises again isn’t instantaneous — it carries startup/initialization latency. Keeping a configured minimum of idle instances trades a predictable amount of extra instance-hours for the elimination of that startup latency on the next burst of traffic, a benefit that applies to every request regardless of destination, since it happens before the request ever reaches Cloud SQL or Cloud Storage.

**Real-World Connection**

Knowing a traffic spike is coming in the next few days, raising the minimum idle instance count ahead of time converts an unpredictable, user-facing latency spike into a small, known, budgeted increase in App Engine instance costs — a standard capacity-planning trade-off whenever the timing of increased demand can be anticipated, rather than leaving the autoscaler to react after the fact and re-incur the same cold-start penalty.

**Memory Hook**

When latency rises equally across unrelated backend services after a traffic spike and doesn’t recover once load normalizes, suspect the shared serving layer’s instance capacity, not either backend individually.

**30-Second Exam Takeaway**

Identical latency across different backend services is the signal to look at the layer common to every request — here, App Engine’s instance count — rather than tuning either backend in isolation; use idle-instance configuration to pre-warm capacity ahead of an expected spike.

**Official References**

[**Google Cloud — How Instances Are Managed (App Engine):**](https://cloud.google.com/appengine/docs/standard/python/how-instances-are-managed) Supports: the correct-answer mechanism of keeping idle instances available to avoid provisioning latency on renewed traffic

[**Google Cloud — About high availability (Cloud SQL):**](https://cloud.google.com/sql/docs/high-availability) Supports: the elimination of Option B by confirming HA addresses zonal/instance failover, not request latency

---

## Question 58

*Domain 2: Building and Implementing CI/CD Pipelines*

Some of your production services run on Google Kubernetes Engine (GKE) in a Europe region, while your build system runs in a US region. You want to push the container images from the build system to a scalable registry so that the bandwidth available for transferring the images to the cluster is as high as possible. What should you do?

- [ ] A. Push the images to Artifact Registry by using the gcr.io hostname.
- [ ] B. Push the images to Artifact Registry by using the us.gcr.io hostname.
- [x] C. Push the images to Artifact Registry by using the eu.gcr.io hostname.
- [ ] D. Push the images to a private image registry running on a Compute Engine instance in the same Europe region as the cluster.

### Explanation

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

---

## Question 59

*Domain 5: Optimizing Performance and Cost*

An e-commerce application has recently been migrated to Google Cloud, and the team wants to get it ready for the upcoming busy season. What is the first thing that should be done to prepare?

- [x] A. Run load tests against the application to profile how its performance behaves under scaling.
- [ ] B. Turn on autoscaling for the production clusters in anticipation of traffic growth.
- [ ] C. Pre-provision twice the compute capacity that was used during last season, anticipating growth.
- [ ] D. Write a runbook describing how to scale up the disaster recovery (DR) environment if growth occurs.

### Explanation

**Correct Answer**

**A. Run load tests against the application to profile how its performance behaves under scaling.**

**Exam Reasoning Explanation**

The decisive word in the question is “first.” Every one of the four options is a plausible activity somewhere in a busy-season readiness plan, so the question isn’t testing whether each is a good idea in isolation — it’s testing sequencing. Autoscaling thresholds, how much capacity to pre-provision, and how far a DR environment needs to scale are all decisions that should be derived from data about how the application actually behaves under load: where it bottlenecks, at what traffic level, and in which component. Until that data exists, any of those decisions is a guess. Load testing is the step that produces the data, so it has to come before the others, not alongside or after them.

**Key Exam Clues**

  * “What is the first thing that should be done to prepare?” — a sequencing constraint; the correct option must be the foundational step everything else depends on, not merely a reasonable preparation activity.

  * “recently been migrated to Google Cloud” — the application’s scaling behavior in this environment hasn’t necessarily been characterized yet, reinforcing the need to establish a performance baseline before making capacity commitments.

  * Options B, C, and D are each specific infrastructure or process decisions, none of which states that performance data already exists to base that decision on.

**Why This Is Correct**

Load testing reveals the application’s actual scaling characteristics and bottlenecks under simulated peak conditions — whether the constraint is compute, a database connection pool, a downstream API quota, or something else entirely. That information is a precondition for making every other preparation decision well: it tells you what signal and thresholds to configure for autoscaling, how much capacity actually needs to be reserved or pre-provisioned, and whether DR capacity needs to scale differently than production. Running it first means every subsequent decision is grounded in evidence rather than assumption.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Technically Possible but Not Best:** enabling autoscaling is a sound long-term practice, but configuring it effectively requires knowing which metric to scale on and what thresholds and instance limits actually match the application’s real behavior under load — exactly what a load test reveals. Turning it on without that information risks thresholds that are poorly matched to the application’s actual bottlenecks.

  * **Option C — Technically Possible but Not Best:** doubling last season’s compute is an arbitrary multiplier with no basis in measured need. It assumes growth will be linear and that compute is the binding constraint, when the real bottleneck could just as easily be a database, a third-party integration, or application code — something more compute alone wouldn’t fix, and something a load test would surface.

  * **Option D — Different Use Case:** a runbook for scaling the DR environment addresses disaster recovery — restoring service after a catastrophic failure — which is a related but separate concern from preparing production capacity for an expected, non-catastrophic increase in ordinary traffic. It doesn’t speak to the busy-season capacity question the scenario is actually asking about.

**Exam Trap**

The trap is evaluating each option only on “is this a sensible thing to do,” which makes B, C, and D all look reasonable. The question isn’t asking which options are valid preparation activities — it’s asking which one has to happen first so the others can be done well. Skipping past the diagnostic step straight to a specific infrastructure decision is the exact ordering mistake the question is testing for.

**Foundation Concept**

Capacity planning for an anticipated demand increase starts with establishing, through load testing under realistic simulated peak conditions, how the system actually scales and where its real limits are. Every subsequent decision — autoscaling configuration, capacity reservations, redundancy planning, DR sizing — should be derived from that evidence rather than assumed ahead of time.

**Real-World Connection**

Running load tests well ahead of a peak event — Google Cloud’s own peak-event guidance recommends starting three to five months out — surfaces bottlenecks like a saturated connection pool or an undersized API quota while there’s still time to fix them, and gives the team the concrete numbers needed to correctly size autoscaling policies and capacity reservations, instead of discovering those limits for the first time during the actual busy season.

**Memory Hook**

Before tuning autoscaling, pre-provisioning compute, or updating a DR runbook — measure first. Load test to find out how the system actually scales.

**30-Second Exam Takeaway**

When a question asks what to do “first” to prepare for anticipated higher demand, favor the step that produces the data every other decision should be based on — load testing — over any specific capacity or configuration action taken without it.

**Official References**

[**Google Cloud — Conduct load testing (peak capacity event preparation):**](https://cloud.google.com/support/docs/peak-events/conduct-load-testing) Supports: the correct-answer reasoning that load testing is a foundational, early preparation step that surfaces scaling bottlenecks before an event

[**Google Cloud — Manage traffic and load for your workloads in Google Cloud:**](https://cloud.google.com/architecture/infra-reliability-guide/traffic-load) Supports: why capacity decisions such as autoscaling configuration and provisioning should be derived from load-test results rather than assumed in advance

---

## Question 60

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

An application being deployed needs access to sensitive information, and that information must stay encrypted with the exposure kept to a minimum if a breach were to occur. What should be done?

- [x] A. Store the encryption keys in Cloud Key Management Service (KMS), and rotate those keys on a frequent schedule.
- [ ] B. Inject the secret into the instance at creation time through an encrypted configuration management system.
- [ ] C. Integrate the application with a single sign-on (SSO) system, keeping secrets from ever being exposed to the application.
- [ ] D. Use a continuous build pipeline that generates a different version of the secret for every instance of the application.

### Explanation

**Correct Answer**

**A. Store the encryption keys in Cloud Key Management Service (KMS), and rotate those keys on a frequent schedule.**

**Exam Reasoning Explanation**

The scenario sets two requirements that have to be satisfied together: the information must actually be encrypted, and exposure must be minimized specifically “if a breach occurs” — meaning the design has to assume a breach is possible and bound how much damage it can do, not just prevent it. That second requirement is the decisive one: it’s asking for a defense-in-depth property, not just an encryption mechanism. A centrally managed key service that encrypts the data satisfies the first requirement, and regularly rotating those keys is what satisfies the second, because rotation limits how much data any single compromised key version could ever expose. Options that only address how a secret is delivered or generated, rather than how the underlying encryption keys are managed over time, don’t provide that bounding property.

**Key Exam Clues**

  * “ensure that this information is encrypted” — the chosen approach must directly protect the sensitive data through encryption, not merely restrict who can see it.

  * “the risk of exposure is minimal if a breach occurs” — a hard requirement for limiting the blast radius of a compromise, not just preventing one.

  * Single-select “What should you do?” — only one mechanism needs to satisfy both requirements at once.

**Why This Is Correct**

Cloud KMS centrally creates and manages the cryptographic keys used to encrypt the sensitive information. Rotating those keys on a frequent schedule limits the cryptoperiod — the span of time a given key version is used to encrypt new data — so that if a key version is ever compromised, only the data encrypted during that version’s active window is at risk, not the full accumulated history of sensitive data the application has ever handled. That combination — managed encryption plus a bounded exposure window through rotation — directly satisfies both halves of the requirement at once.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Technically Possible but Not Best:** delivering a secret to an instance through an encrypted channel protects it in transit at creation time, but says nothing about how the underlying sensitive information is encrypted or how long that secret remains valid afterward. A secret injected once and never rotated stays exploitable for the entire lifetime of the instance, which does not minimize exposure if it’s later compromised.

  * **Option C — Different Use Case:** single sign-on governs how human users authenticate to a system. It has no bearing on how an application’s sensitive data is encrypted or how machine-level secrets are protected, so it doesn’t address either requirement the scenario actually states.

  * **Option D — Violates Requirement:** generating a distinct secret version for every instance through a build pipeline means secrets get baked into build artifacts and spread across many build outputs and logs — more places a secret could leak, and more difficulty tracking which version is active where. That works against minimizing exposure rather than for it.

**Exam Trap**

Options B and D both sound protective — an encrypted delivery channel, a fresh secret per instance — but neither one manages the lifecycle of the cryptographic material actually protecting the sensitive data over time; they’re adjacent practices to secret handling, not key management. The scenario specifically asks for bounded exposure in the event of a breach, which is exactly what a centrally managed, rotated key lifecycle is designed to deliver, not what secret delivery or build-time secret generation provides.

**Foundation Concept**

Cloud KMS is Google Cloud’s centralized service for creating, managing, and using cryptographic keys to protect data, both in compatible Google Cloud services and in custom applications. A core discipline of key management is limiting a key’s cryptoperiod through regular rotation — the standard recommended practice precisely because it bounds how much data any single compromised key version could expose, rather than leaving one key protecting an ever-growing body of sensitive data indefinitely.

**Real-World Connection**

Rotating an application’s Cloud KMS keys on a regular schedule means that if an attacker ever obtains one key version, they can only read the data encrypted during that key’s active period — not months or years of accumulated sensitive data sitting behind a single, never-changed key — turning what could be a catastrophic breach into a bounded, time-limited incident.

**Memory Hook**

Encrypting data protects it; rotating the keys protecting it is what actually limits how much a breach can expose — manage the keys, don’t just manage how the secret moves around.

**30-Second Exam Takeaway**

When a question asks for both encrypting sensitive information and limiting exposure if a breach happens, look for the option that manages the cryptographic key lifecycle — a centralized key service plus regular rotation — rather than one that only addresses how a secret is delivered or generated.

**Official References**

[**Google Cloud — Rotate a key (Cloud KMS):**](https://cloud.google.com/kms/docs/key-rotation) Supports: the correct-answer mechanism of key rotation limiting the exposure window if a key is compromised

[**Google Cloud — Cloud Key Management Service overview:**](https://cloud.google.com/kms/docs/key-management-service) Supports: Cloud KMS’s role as the centralized service for creating and managing the encryption keys used to protect application data

---
