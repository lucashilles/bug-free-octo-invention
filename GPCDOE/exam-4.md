# Professional Cloud DevOps Engineer — Practice Exam 4

60 questions.

## Question 1

*Domain 3: Applying Site Reliability Engineering Practices*

Cloud Monitoring alerts you to potentially malicious activity on a node in your Google Kubernetes Engine (GKE) cluster. A container running on that node might be compromised.

You need to isolate the affected node while investigating the incident and minimize disruption to applications running in the cluster. What should you do?

- [ ] A. Taint the suspicious node to prevent Pods that previously interacted with it from being scheduled on other cluster nodes.
- [ ] B. Scale the Deployment associated with the suspected container to zero replicas.
- [ ] C. Restart the node to interrupt the malicious activity and force its Pods to be recreated on other nodes.
- [x] D. Cordon the node to prevent new Pod scheduling, then drain it gracefully so controller-managed workloads can be recreated on other nodes.

### Explanation

**Correct Answer**

**D. Cordon the node to prevent new Pod scheduling, then drain it gracefully so controller-managed workloads can be recreated on other nodes.**

**Exam Reasoning Explanation**

D provides controlled evacuation of the affected node while preventing normal scheduling onto it. It is the best available option, although complete incident containment also requires network restrictions. 

**Key Exam Clues**

  * **Security signal:** A container might be compromised.

  * **Containment requirement:** Isolate the affected node during investigation.

  * **Availability preference:** Minimize disruption to other workloads.

**Why This Is Correct**

Cordoning marks the node as unschedulable. Draining gracefully evicts eligible Pods, allowing their controllers to create replacements elsewhere. Normal eviction respects PodDisruptionBudgets, helping limit simultaneous application disruption. 

Successful evacuation depends on suitable workload controllers, healthy replicas, and sufficient capacity on other nodes. It does not guarantee zero downtime.

**Why the Other Options Are Not the Best Fit**

  * **A — Incorrect:** Taints affect scheduling or eviction on the tainted node. They do not track which Pods interacted with it or automatically prevent those Pods from running elsewhere. 

  * **B — Violates Requirement:** Scaling to zero removes every replica of that Deployment, potentially taking the application offline. It also leaves the suspicious node available to other workloads.

  * **C — Incorrect:** Restarting does not establish scheduling or network quarantine. It also does not guarantee that replacement Pods run on different nodes or that the underlying compromise is resolved. 

**Exam Trap**

**Cordon and drain are not complete security isolation.** Google’s incident-response guidance recommends retaining the suspected Pod for investigation, draining the other workloads, and restricting network access to the node’s VM. Do not blindly redeploy the suspected workload elsewhere. 

**Foundation Concept**

These controls serve different purposes:

  * **Cordon:** Prevent normal scheduling onto the node.

  * **Drain:** Gracefully evacuate eligible workloads.

  * **Network quarantine:** Restrict communication involving the suspected node.

**Real-World Connection**

Google documents this selective evacuation pattern:
    
          1. kubectl cordon NODE_NAME
      2. kubectl label pod SUSPECT_POD -n APP_NAMESPACE quarantine=true
      3. kubectl drain NODE_NAME --pod-selector='!quarantine' --ignore-daemonsets

This excludes the quarantined Pod from evacuation. DaemonSet Pods remain, and node-level network restrictions must be configured separately. 

**Memory Hook**

Cordon stops arrivals, drain evacuates workloads, and network controls restrict communication.

**30-Second Exam Takeaway**

Choose **D** for controlled node evacuation with minimal disruption. During an actual compromise investigation, add network quarantine and preserve the suspected workload appropriately.

**Official References**

  * [**Mitigate security incidents — GKE**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/security-mitigations)  
Supports: Selective draining, suspected-Pod quarantine, network restrictions, and incident-response tradeoffs.

  * [**kubectl drain**](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_drain/)  
Supports: Unschedulable nodes, graceful eviction, workload-controller requirements, and DaemonSet exclusions.

  * [**Taints and Tolerations**](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)  
Supports: What node taints control and why option A misrepresents their behavior.

  * [**Disruptions**](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)  
Supports: PodDisruptionBudgets and maintaining availability during voluntary disruptions.

---

## Question 2

*Domain 2: Building and Implementing CI/CD Pipelines*

You are configuring a continuous integration (CI) pipeline in Cloud Build with the following `cloudbuild.yaml` configuration:
    
          1. steps:
      2. - name: foo
      3.   id: foo
      4. - name: bar
      5.   id: bar
      6. - name: baz
      7.   id: baz

The `foo` and `bar` steps each take five minutes and can run independently. The `baz` step must wait until both have completed successfully. You need to reduce build time by running the independent steps concurrently. What should you do?

- [ ] A. Add the following machine configuration:
      
            1. options:
        2.   machineType: 'E2_HIGHCPU_8'
- [ ] B. Add the following machine configuration:
      
            1. options:
        2.   machineType: 'E2_HIGHCPU_32'
- [ ] C. Configure `foo` to start immediately and make `baz` wait for both preceding steps:
      
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
- [x] D. Configure both independent steps to start immediately and make `baz` wait for their completion.
      
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

### Explanation

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

---

## Question 3

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

You are designing a multi-tenant Google Kubernetes Engine (GKE) cluster. Your customer wants to avoid the risks of long-lived credentials and ensure that each workload receives only the IAM permissions it requires.

You need to implement IAM service account impersonation following Google-recommended practices. What should you do?

- [ ] A. Create an IAM service account and configure it as the node identity of a dedicated node pool. Restrict the workload to that pool using node selectors, taints, and tolerations. Repeat this configuration for each workload.
- [ ] B. Create an IAM service account and configure it as the node identity of a node pool without taints. Grant the required IAM permissions to that service account.
- [x] C. Create an IAM service account and a Kubernetes ServiceAccount in a cluster with Workload Identity Federation for GKE enabled. Grant the Kubernetes ServiceAccount `roles/iam.workloadIdentityUser` on the IAM service account, and link them using the `iam.gke.io/gcp-service-account` annotation. Configure the workload to use the Kubernetes ServiceAccount. Repeat for each workload.
- [ ] D. Create an IAM service account and generate a service account key. Store the key in a Kubernetes Secret, mount it into the workload, and set `GOOGLE_APPLICATION_CREDENTIALS` to the mounted key file’s path. Repeat for each workload.

### Explanation

**Correct Answer**

**C. Create an IAM service account and a Kubernetes ServiceAccount in a cluster with Workload Identity Federation for GKE enabled. Grant the Kubernetes ServiceAccount**`**roles/iam.workloadIdentityUser**`**on the IAM service account, and link them using the**`**iam.gke.io/gcp-service-account**`**annotation. Configure the workload to use the Kubernetes ServiceAccount. Repeat for each workload.**

**Exam Reasoning Explanation**

Workload Identity Federation for GKE provides workload-specific access to Google Cloud APIs without distributing service account key files. Its impersonation configuration matches the role binding and annotation described in C. 

**Key Exam Clues**

  * **Credential requirement:** Avoid long-lived credentials.

  * **Authorization requirement:** Apply least privilege separately to each workload.

  * **Architecture:** Multiple tenants share the cluster.

  * **Explicit mechanism:** IAM service account impersonation.

**Why This Is Correct**

The implementation requires:

  * A dedicated workload identity with narrowly scoped resource permissions.

  * An impersonation binding restricted to the intended Kubernetes namespace and ServiceAccount.

  * The annotation linking that Kubernetes ServiceAccount to its IAM service account.

  * Assignment of the Kubernetes ServiceAccount through the Pod’s `serviceAccountName`.

Both the impersonation binding and annotation are required. Workload Identity Federation uses short-lived tokens rather than downloaded service account keys. 

**Why the Other Options Are Not the Best Fit**

  * **A — Technically Possible but Not Best:** Dedicated pools can separate workload placement, but this ties identity to nodes and requires a pool per workload. Google recommends workload-level identities rather than relying on node service accounts for application access. 

  * **B — Violates Requirement:** Workloads sharing the node identity can inherit the same permissions. This does not establish separate least-privilege identities for each tenant workload. 

  * **D — Violates Requirement:** Mounting a service account key in a Kubernetes Secret still distributes a persistent credential. Google recommends avoiding user-managed service account keys when a more secure authentication method is available.

**Exam Trap**

Current guidance generally prefers direct IAM grants to federated workload principals where supported. However, this question explicitly requires **IAM service account impersonation** , making C the appropriate configuration. 

**Foundation Concept**

The `roles/iam.workloadIdentityUser` binding authorizes **impersonation**. Separate roles granted to the IAM service account determine **which Google Cloud resources the workload can access**.

**Real-World Connection**

Two applications can share a GKE node while using different identities: one reads objects from a specific Cloud Storage bucket, while another accesses a particular Secret Manager secret. Their permissions remain independently configurable.

**Memory Hook**

Give each workload a scoped identity that uses short-lived credentials.

**30-Second Exam Takeaway**

Choose **C**. Use Workload Identity Federation for GKE, the impersonation binding, the linking annotation, and a dedicated Kubernetes ServiceAccount assigned to each workload.

**Official References**

  * [**Authenticate to Google Cloud APIs from GKE workloads**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)  
Supports: IAM impersonation bindings, required annotations, workload assignment, and direct federation alternatives.

  * [**About Workload Identity Federation for GKE**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity?)  
Supports: Short-lived credentials and the risks of shared node identities.

  * [**About service accounts in GKE**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts)  
Supports: Dedicated, minimally privileged ServiceAccounts for individual workloads.

  * [**Best practices for managing service account keys**](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys)  
Supports: Avoiding user-managed keys and reducing credential leakage risks.

---

## Question 4

*Domain 2: Building and Implementing CI/CD Pipelines*

Your application is running in production on Cloud Run. Your team has completed a new version, revision B, and wants to test it with 10% of your clients.

You need to implement this test with the **least operational effort**. What should you do?

- [ ] A. Deploy revision B to the existing service without allocating production traffic. Assign it a revision tag and share its tagged URL with 10% of your clients.
- [ ] B. Deploy revision B to a separate Cloud Run service. Update the existing application to forward a percentage of incoming requests to the new service.
- [ ] C. Deploy revision B to a separate Cloud Run service. Configure a load balancer to distribute traffic between the existing and new services.
- [x] D. Deploy revision B to the existing service without initially allocating traffic. Configure Cloud Run traffic splitting to send 10% of traffic to revision B and 90% to the existing revision.

### Explanation

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

---

## Question 5

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

Your organization keeps a large amount of rarely accessed data in Cloud Storage. Separately, the projects under your CustomerService folder make frequent Cloud Storage calls but hold very little data of their own. You want to turn on Data Access audit logging company-wide so you can analyze data usage patterns, but the CustomerService folder’s projects need to be left out of that logging. What should you do?

- [x] A. Enable Data Access audit logging for Cloud Storage at the organization level, and add the principals used by the CustomerService folder’s projects to the exempted principals list.
- [ ] B. Enable Data Access audit logging for Cloud Storage at the organization level, and leave the configuration as is with no further changes.
- [ ] C. Enable Data Access audit logging for Cloud Storage individually on every project and folder except the CustomerService folder.
- [ ] D. Enable Data Access audit logging for Cloud Storage individually on every project and folder, and add the principals used by the CustomerService folder’s projects to the exempted principals list.

### Explanation

**Correct Answer**

**A. Enable Data Access audit logging for Cloud Storage at the organization level, and add the principals used by the CustomerService folder’s projects to the exempted principals list.**

**Exam Reasoning Explanation**

Must-have constraints: Data Access logging has to reach every current and future project “across the company,” and the CustomerService folder’s projects specifically must not end up logged. Not a requirement: excluding any particular human reviewer or adding logging service by service — the scope is Cloud Storage, company-wide. Capability: enabling at the organization level cascades the configuration to every folder and project beneath it automatically, including ones created later, with no per-project setup. Elimination: Cloud Audit Logs’ hierarchy rules explicitly block a child resource from disabling a Data Access log type its parent already enabled, which rules out any plan built around “enable everywhere except this folder” (C) as a way to selectively disable logging downstream. Manually enabling resource by resource (C, D) also doesn’t extend to future projects the way an org-level setting does. Decision: only an org-level enablement paired with the exempted principals list — Google’s documented mechanism for excluding specific identities from an already-enabled configuration — satisfies both the company-wide requirement and the CustomerService exclusion at once.

**Key Exam Clues**

  * “across the company” — a hard constraint pointing toward an organization-level configuration rather than a project-by-project one.

  * “exclude the CustomerService folder projects from Data Access audit logging” — a hard constraint requiring a reliable, complete exclusion for that folder specifically.

  * CustomerService “accesses Cloud Storage frequently, but store[s] very little data” — background explaining why their activity would otherwise flood the audit logs with high-volume, low-value entries, motivating the exclusion rather than changing the mechanism used.

  * No mention of excluding particular people, only the folder’s projects — a technical signal that the folder-level exclusion has to be translated into identity terms, since that’s the lever Cloud Audit Logs actually exposes.

**Why This Is Correct**

Enabling the Data Access audit log for Cloud Storage at the organization level applies it immediately to every existing folder and project and automatically extends to any project created later, which is exactly what “across the company” calls for with the least ongoing maintenance. Google Cloud’s documented mechanism for narrowing who gets logged under an already-enabled configuration is the exempted principals list: adding the identities the CustomerService folder’s projects actually use (their service accounts, and any human users) means Cloud Storage activity from those projects stops producing Data Access log entries, while every other project in the organization keeps being logged normally.

**Why the Other Options Are Not the Best Fit**

**Option B — Violates Requirement:** This enables logging everywhere, including the CustomerService folder, with no exclusion at all. It satisfies the “across the company” half of the requirement but directly ignores the explicit instruction to leave CustomerService out.

**Option C — Violates Requirement:** This assumes you can scope initial enablement around a folder as a substitute for exclusion, but Cloud Audit Logs doesn’t work that way — there’s no single org-level action that says “enable for everyone except X”; you would have to configure each non-CustomerService project and folder individually, and a project created later anywhere else in the company wouldn’t be covered until someone remembers to configure it. It also doesn’t actually use the one supported exclusion mechanism (exempted principals) at all.

**Option D — Technically Possible but Not Best:** Manually enabling Data Access logging on every project and folder individually, then adding CustomerService’s principals to the exemption list, can produce the same end state as Option A for the resources configured today, but it carries all of Option C’s scaling problem — any new project outside CustomerService needs its own manual enablement rather than inheriting it from one org-level setting — making it considerably more administrative effort for no functional benefit over Option A.

**Exam Trap**

The trap is reading “exclude the CustomerService folder” and reaching for the option that scopes enablement away from that folder, since that looks like the most literal translation of the requirement (Option C). But Data Access log inheritance only allows a lower-level resource to add to what a parent enabled, never to disable or narrow it, and per-resource enablement doesn’t automatically cover future projects. The only way Google actually lets you narrow an enabled configuration is by principal, not by resource branch — so “exclude a folder” has to become “exempt that folder’s principals.”

**Foundation Concept**

Data Access log configuration lives inside the IAM policy of organization, folder, and project resources and follows IAM’s inheritance model: the effective configuration across the hierarchy is a union, a descendant can add more logging or more exemptions, but it can never disable a log type or remove an exemption a parent already set. Because inheritance only ever adds, scoped exclusions have to be expressed as exempted principals rather than as selective non-enablement at certain branches of the resource hierarchy.

**Real-World Connection**

Centralizing an org-wide audit logging policy at the top of the resource hierarchy, then layering in narrow, documented exemptions for known high-volume, low-risk workloads, is the standard pattern for keeping Data Access log volume — and the Cloud Logging storage costs that come with it — manageable without creating silent blind spots elsewhere; it also means a security or compliance reviewer can audit the entire exception list in one place instead of discovering gaps caused by a project nobody remembered to configure.

**Memory Hook**

Enable Data Access logging high, in the organization; exempt low, by principal — you can never disable what a parent resource already turned on.

**30-Second Exam Takeaway**

When a scenario wants Data Access audit logging turned on broadly but one part of the org left out, look for the option that enables at the top of the hierarchy and uses exempted principals for the exclusion — any option that tries to withhold enablement from one branch of the hierarchy, or re-enables resource by resource, is fighting how Cloud Audit Logs inheritance actually works.

**Official References**

[**Google Cloud — Enable Data Access audit logs:**](https://cloud.google.com/logging/docs/audit/configure-data-access) Supports: confirms a descendant resource can’t disable a Data Access log type enabled by a parent organization, that hierarchy configurations merge as a union, and that exempted principals is the supported mechanism for excluding specific identities from logging

[**Google Cloud — Cloud Audit Logs overview:**](https://cloud.google.com/logging/docs/audit) Supports: general context on Data Access audit logs versus Admin Activity logs and how audit logging is scoped across organizations, folders, and projects

---

## Question 6

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your company operates an ecommerce business. The service that handles payment processing emits structured JSON log entries using this schema:
    
          1. {
      2.   "logName": ...,
      3.   "resource": ...,
      4.   "httpRequest": ...,
      5.   "jsonPayload": {
      6.     "user_email" : ...,
      7.     "method" : ...,
      8.     "code" : ...,
      9.   },
      10.   ...
      11. }

Capturing these payment-processing logs and making them available for operations is required, but the `jsonPayload.user_email` field holds personally identifiable information (PII). Your security team does not want the broader engineering team to be able to see that PII, and wants access to it limited to security team members. What should you do?

- [ ] A. Apply a conditional IAM role binding using the expression `resource.name.extract("locations/global/buckets/{bucket}/") == "_Default"` against the `_Default` bucket.
- [x] B. Mark `jsonPayload.user_email` as a restricted field on the `_Default` bucket, and grant the Log Field Accessor role to the security team members.
- [ ] C. Apply an exclusion filter on `jsonPayload.user_email` to the `_Default` bucket.
- [ ] D. Change the application so that it only includes `user_email` in its logs when the `LOG_USER_EMAIL` environment variable is set to true, and restrict which engineering team members can modify that production environment variable by using a CODEOWNERS file.

### Explanation

**Correct Answer**

**B. Mark**`**jsonPayload.user_email**`**as a restricted field on the**`**_Default**`**bucket, and grant the Log Field Accessor role to the security team members.**

**Exam Reasoning Explanation**

Must-have constraints: log capture and general operational access to the payment-processing logs must keep working, the `user_email` field specifically must stop being visible to engineering at large, and visibility into that field must be limited to the security team. Not a requirement: changing whether the data is logged at all, or building a custom access gate outside Google Cloud’s own controls. Capability: Cloud Logging’s field-level access control lets you name a specific field path, such as `jsonPayload.user_email`, as restricted on a log bucket; once restricted, that field is hidden from anyone who doesn’t also hold the Log Field Accessor role (`roles/logging.fieldAccessor`) for that path, while the rest of the log entry, and log access generally, is unaffected. Elimination: any option that drops or withholds the underlying log data (C) breaks mandatory capture; any option that controls whether data is written rather than who can view it (D) can’t distinguish between engineering and security once the field is logged; an option that only gestures at a conditional binding without actually marking the field restricted or granting the field-accessor role to security (A) does nothing to hide the field at all. Decision: Option B is the only one that uses the purpose-built mechanism end to end — restrict the field, then grant the matching viewer role to exactly the group that should see it.

**Key Exam Clues**

  * “Capture and access of logs... is mandatory for operations” — a hard constraint ruling out anything that prevents the data from being ingested or generally accessible.

  * “`jsonPayload.user_email` field contains personally identifiable information” — a technical anchor naming the exact field path, pointing directly at a field-level (not entry-level) control.

  * “does not want the entire engineering team to have access to PII... restrict access to security team members only” — a precise least-privilege, per-group constraint that calls for an IAM role grant scoped to specific principals, not a blanket on/off switch.

  * “stop exposing PII to the engineering team” — confirms the fix has to act on who can _see_ the field, not on whether the field gets stored, which is what rules out dropping the data entirely.

**Why This Is Correct**

Restricting `jsonPayload.user_email` on the `_Default` bucket tells Cloud Logging to hide that specific field’s value from anyone querying the bucket’s logs, independent of everything else in the log entry. Granting the Log Field Accessor role to the security team’s principals then gives exactly that group permission to see the real value, provided they also have ordinary log-viewing access to the bucket (which, as the team responsible for investigating this data, they would). Engineering continues to see and query every other field — satisfying “mandatory for operations” — while `user_email` itself comes back redacted or denied for them, satisfying the PII restriction, all without touching what gets captured or stored.

**Why the Other Options Are Not the Best Fit**

**Option A — Incorrect:** The CEL expression shown is a real piece of Cloud Logging’s own IAM Condition syntax — it’s the documented way to scope a role grant to a specific bucket like `_Default`. But on its own, with no field marked as restricted and no mention of granting the Log Field Accessor role to the security team, applying this condition accomplishes nothing: there is nothing yet for the condition to scope. Without first restricting `jsonPayload.user_email`, the field remains fully visible to anyone with ordinary log access, engineering included.

**Option C — Violates Requirement:** An exclusion filter prevents matching log data from being ingested and stored in the first place, rather than hiding it from unauthorized viewers. Applying one here would mean the payment-processing logs are no longer fully captured, which directly contradicts the requirement that capture remain mandatory for operations — and it would also deny the security team any access to the PII they’re supposed to retain access to.

**Option D — Violates Requirement:** Gating whether `user_email` gets logged behind an application environment variable, and gating who can change that variable through a CODEOWNERS file, controls whether the data exists in logs at all, not who can view it once it’s there. Anyone with ordinary log access — engineering included — would see `user_email` whenever the flag happened to be on, so this never actually limits viewing to the security team, and it relies on a source-control review convention rather than any Google Cloud access control.

**Exam Trap**

The trap in Option A is that the CEL expression is genuinely pulled from Google’s own documented workflow for field-level access control — it’s real syntax used when scoping a Log Field Accessor grant to a particular bucket. Seeing accurate, official-looking syntax can read as “this must be the right answer,” but a condition on a role binding is only half a mechanism: without the field actually being marked restricted and without that role being granted to the right group, the condition has nothing to act on.

**Foundation Concept**

Field-level access control is a narrower tool than bucket- or log-view-level access control: it hides individual named fields within a `LogEntry` from principals who lack the matching `logging.fieldAccessor` grant, while leaving the rest of the entry, and the entry’s existence, untouched. The transferable principle is matching the access-control mechanism to the actual shape of the requirement — when the ask is “keep the data, hide one field, let one group see it,” reach for field-level restriction plus a scoped viewer role, not an ingestion-time filter or an application-level toggle.

**Real-World Connection**

Teams handling regulated or sensitive fields — SSNs, emails, health identifiers — inside otherwise-operational logs commonly use exactly this pattern: keep full logs flowing for incident response and debugging, restrict the one or two sensitive fields, and grant the field-accessor role only to the security or compliance group that has a legitimate need to see the raw value, with everyone else’s dashboards and queries working exactly as before, just with that one field redacted.

**Memory Hook**

To hide one PII field without losing the log: restrict the field, then grant Log Field Accessor to the one group that should still see it.

**30-Second Exam Takeaway**

When a scenario needs a specific named log field hidden from most viewers while logs stay fully captured and a smaller group retains access, look for the option that configures a restricted field on the bucket and grants the Log Field Accessor role to that group — options that drop the data, toggle it at the application level, or apply an access condition with no restricted field behind it are all solving a different problem.

**Official References**

[**Google Cloud — Configure field-level access:**](https://cloud.google.com/logging/docs/field-level-acl) Supports: confirms how to mark a field such as `jsonPayload.user_email` as restricted on a bucket, and that only principals with the Log Field Accessor role (plus ordinary log-view access) can see the unredacted value

[**Google Cloud — Access control with IAM (Logging)**](https://cloud.google.com/logging/docs/access-control)**:** Supports: confirms the Log Field Accessor (`roles/logging.fieldAccessor`) role definition and how it differs from general log-viewing role

---

## Question 7

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

Your organization gives engineering teams autonomy to self-manage their own Google Cloud projects, including project-level Identity and Access Management (IAM) assignments. You are worried that the team that owns the Shared VPC host project could accidentally delete the project, so you have already attached a deletion lien to it. You now need a design that limits who can remove that lien on the Shared VPC project to only principals holding the resourcemanager.projects.updateLiens permission at the organization level. What should you do?

- [ ] A. Require every team to manage their IAM permission assignments exclusively through Terraform-based infrastructure as code.
- [ ] B. Create a VPC Service Controls perimeter that covers the container.googleapis.com API service.
- [ ] C. Strip the resourcemanager.projects.updateLiens permission from every user who is associated with the project.
- [x] D. Turn on the compute.restrictXpnProjectLienRemoval organization policy constraint.

### Explanation

**Correct Answer**

**D. Turn on the compute.restrictXpnProjectLienRemoval organization policy constraint.**

**Exam Reasoning Explanation**

The hard constraint is that project-level IAM self-management already exists, so a project-level permission grant can never be trusted as the enforcement boundary — teams can simply grant themselves whatever project-level permission the control relies on. The preference is to raise the required permission scope specifically for lien removal on a Shared VPC host project, without disrupting normal self-service IAM elsewhere. Google Cloud exposes exactly one capability built for this: an organization policy constraint that re-scopes the permission check for lien removal from project level to organization level. Process controls (A), unrelated security perimeters (B), and blanket permission revocation (C) are eliminated because none of them changes which scope Google Cloud actually checks when a lien-removal request is evaluated, leaving D as the only option that implements the stated requirement.

**Key Exam Clues**

  * “self-manage Google Cloud projects, including project-level IAM” — hard constraint signaling that project-level permission grants cannot be relied on as a security boundary

  * “a lien has been placed on the project” — confirms the lien already exists; the question is strictly about who can remove it, not whether to create one

  * “restrict ... to those with ... permission at the organization level” — technical signal pointing directly to a mechanism that elevates a permission’s required scope from project to organization

  * “Shared VPC project” — narrows the answer to the XPN-specific lien-removal constraint rather than any generic project-lien behavior

**Why This Is Correct**

compute.restrictXpnProjectLienRemoval is a boolean organization policy constraint purpose-built for Shared VPC host projects. By default, any principal holding resourcemanager.projects.updateLiens at any scope — including project level — can remove a lien. Enforcing this constraint changes that default: lien removal on a Shared VPC host project then requires the permission to be held at the organization level specifically. Because the scenario’s teams can self-manage project-level IAM, a project-level grant of updateLiens would otherwise let them clear the lien and delete the host project; this constraint closes exactly that gap without requiring any change to how teams normally operate.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** Managing IAM as code improves auditability and review discipline, but it is a process convention, not an access-control mechanism. Nothing prevents a team from authoring Terraform that grants itself project-level updateLiens, so it does not change which scope Google Cloud checks.

**Option B — Different Use Case:** VPC Service Controls perimeters govern data exfiltration and API access boundaries for services like Cloud Storage or BigQuery; container.googleapis.com governs GKE API access. Neither the service named nor the VPC Service Controls mechanism has any bearing on project liens or project deletion.

**Option C — Violates Requirement:** Revoking the permission from everyone associated with the project removes the ability to manage the lien entirely rather than restricting it to organization-level holders as required, and it would also block legitimate org-level administrators. It establishes no organization-level control, and project self-management could simply re-grant the permission at any time.

**Exam Trap**

The trap is reaching for a direct IAM action — revoking or granting resourcemanager.projects.updateLiens (Option C) —**** because the question names that exact permission. But the scenario’s real obstacle is that project-level IAM is self-managed and therefore untrustworthy as an enforcement boundary; the decisive phrase is “at the organization level,” which only an organization policy constraint can enforce. If the scenario instead said project-level removal was acceptable, blanket revocation could become defensible — but as written, it is not.

**Foundation Concept**

Organization policies form a hierarchy-wide control plane that can tighten or override default IAM-permission checks for specific, high-impact operations, independent of how IAM roles are assigned on any individual resource. A project lien is a metadata marker blocking deletion until explicitly removed, and removal normally follows wherever resourcemanager.projects.updateLiens is granted. The Shared VPC-specific constraint is a targeted exception: it raises the required scope of that one permission just for Shared VPC host projects, because deleting a host project disrupts every service project attached to it.

**Real-World Connection**

A platform team centralizes network administration in a Shared VPC host project while application teams keep project-level autonomy for their own service projects. Enforcing compute.restrictXpnProjectLienRemoval preserves that autonomy for day-to-day IAM work while guaranteeing that no application team — however broad its project-level grants become — can single-handedly trigger an organization-wide network outage by deleting the host project, reducing operational risk without adding review friction elsewhere.

**Memory Hook**

Shared VPC host project + lien removal → compute.restrictXpnProjectLienRemoval forces the updateLiens check up to the organization level.

**30-Second Exam Takeaway**

When a question asks you to raise an IAM permission’s required scope from project to organization for one specific, high-impact action, look for a purpose-built organization policy constraint before reaching for generic IAM grants/revocations or unrelated controls like VPC Service Controls.

**Official References**

  * [Google Cloud — Provision Shared VPC (Prevent accidental deletion of host projects): ](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc)Supports: the compute.restrictXpnProjectLienRemoval mechanism, its enforcement command, and why it eliminates Option C’s blanket-revocation approach

  * [**Google Cloud — Organization policy constraints reference:**](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints) Supports: confirming compute.restrictXpnProjectLienRemoval as a current, valid Google-managed constraint and its classification as an organization-level control

---

## Question 8

*Domain 2: Building and Implementing CI/CD Pipelines*

Your company runs a GKE application composed of 12 microservices across development (Dev), staging (Staging), and production (Prod) environments. Multiple teams develop features concurrently. Deployments from different feature branches into the shared Dev cluster cause dependency test failures and delay releases.

You need a cost-effective approach that gives developers stable environments for testing their microservice changes independently of other development work. What should you do?

- [ ] A. Use Cloud Build to build container images and update Kubernetes manifests from main-branch merge requests. Use Config Sync to deploy the images for testing in dynamically created namespaces within the autoscaling Dev cluster. Delete the namespaces after testing.
- [ ] B. Use Cloud Build to build container images and update Kubernetes manifests for each commit. Use Cloud Deploy to progressively deliver changes to the Dev, Staging, and Prod clusters. Use Config Sync to maintain consistent Kubernetes configurations across environments.
- [x] C. Use Cloud Build to build container images and update Kubernetes manifests from feature-branch commits. Use Config Sync to deploy the images for testing in dynamically created namespaces within the autoscaling Dev cluster. Delete the namespaces after testing.
- [ ] D. Use Cloud Build to build container images and update Kubernetes manifests from feature-branch commits. Use Config Sync to deploy the images into a separate, dynamically provisioned Dev cluster for each feature branch. Delete the clusters during the merge-request workflow.

### Explanation

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

---

## Question 9

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your organization runs its workloads on Google Cloud, with each team operating its applications inside its own dedicated project. New teams and new projects are provisioned on an ongoing basis. Your security team mandates that every log entry be forwarded to a security information and event management (SIEM) platform, which ingests data exclusively through Pub/Sub. You need an approach that guarantees logs from both current projects and any projects created later are automatically captured and sent to the SIEM. What should you do?

- [ ] A. Configure an aggregated sink at the organization level that routes to a Cloud Logging bucket named siem, and set its inclusion filter to match every log entry.
- [ ] B. Configure an aggregated sink at the folder level that routes to a Pub/Sub topic named siem, set its inclusion filter to match every log entry, and repeat this configuration for each folder.
- [x] C. Configure an aggregated sink at the organization level that routes to a Pub/Sub topic named siem, and set its inclusion filter to match every log entry.
- [ ] D. Configure a logging sink at the project level that routes to a Pub/Sub topic named siem, set its inclusion filter to match every log entry, and repeat this configuration for each project.

### Explanation

**Correct Answer**

**C. Configure an aggregated sink at the organization level that routes to a Pub/Sub topic named siem, and set its inclusion filter to match every log entry.**

**Exam Reasoning Explanation**

Two hard constraints must both be satisfied: the destination has to be something the SIEM can actually ingest (Pub/Sub, not a bucket or dataset), and coverage has to extend to projects that don’t exist yet without ongoing manual work. Cloud Logging’s aggregated sink, scoped to the organization and set to include child resources, satisfies the coverage constraint because the organization is the ancestor of every project the company will ever create; pairing it with a Pub/Sub topic destination and an all-logs inclusion filter satisfies the ingestion constraint. Each distractor fails exactly one of the two constraints: A gets the scope right but the destination wrong, while B and D get the destination right but scope too low, forcing repeated manual setup as the org grows.

**Key Exam Clues**

  * “New teams and projects are created regularly” — a hard constraint that eliminates any solution requiring per-resource repetition for resources that don’t exist yet

  * “The SIEM ingests logs by using Pub/Sub” — a hard constraint on destination type, ruling out log buckets, BigQuery datasets, or Cloud Storage buckets

  * “all existing and future logs” — the decisive phrase pointing to organization-level scope, since only the organization is guaranteed to be an ancestor of every future project

  * “Repeat for each folder” / “Repeat for each project” (in the distractors) — an explicit tell that those options require ongoing manual maintenance, directly conflicting with the “future” requirement

**Why This Is Correct**

An aggregated sink defined at the organization level, with child resources included, evaluates its filter against log entries generated anywhere inside the organization’s resource hierarchy — including projects and folders created after the sink was configured. An inclusion filter that matches every log entry means nothing is dropped, and a Pub/Sub topic destination gives the SIEM the exact mechanism it needs to ingest the data. Because the sink lives at the top of the hierarchy, no further action is required as the company provisions new teams and projects.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement:** The scope is correct — an organization-level aggregated sink does cover current and future projects — but the destination is a log bucket. A SIEM that ingests exclusively through Pub/Sub has no way to consume a log bucket directly, so the integration requirement fails despite the coverage being right.

**Option B — Technically Possible but Not Best:** The Pub/Sub destination is correct, and a folder-level aggregated sink does automatically cover every present and future project nested under that folder. But “repeat for each folder” means any folder created after this configuration is not covered until someone manually adds a sink for it, so future coverage is incomplete without ongoing maintenance that an organization-level sink avoids entirely.

**Option D — Violates Requirement:** A project-level sink has no concept of child resources — it covers only the single project it’s created in. Repeating it for every existing project still leaves every future project unmonitored until a new sink is manually created for it, which directly contradicts the requirement to capture future logs automatically.

**Exam Trap**

The trap is validating only one of the two independent requirements — scope or destination — and assuming the option is correct. Option A passes the scope check but fails the destination check; Options B and D pass the destination check but fail the scope check. Only the organization-level-plus-Pub/Sub combination passes both. If the SIEM instead ingested from Cloud Storage or BigQuery, Option A’s destination would become the right choice, and the correct answer would change accordingly.

**Foundation Concept**

An aggregated sink is a Cloud Logging resource created at the folder or organization level that, when configured to include child resources, automatically evaluates its filter against log entries from every project nested anywhere beneath it, present and future, with no per-project configuration required — unlike a standard sink, which only ever processes logs generated inside the single resource it belongs to. A sink’s destination type (log bucket, BigQuery dataset, Cloud Storage bucket, or Pub/Sub topic) is a separate, independent choice from its scope, and both have to be correct for a given downstream consumer.

**Real-World Connection**

A platform team centralizes security log collection with a single organization-level aggregated sink feeding a Pub/Sub topic that their SIEM consumes, instead of asking every application team to build and maintain its own export pipeline. As new initiatives spin up new projects, the security team never has to chase down and onboard each one individually — the aggregated sink already has it covered — which keeps audit and compliance coverage complete and removes a recurring operational burden from both security and application teams.

**Memory Hook**

“Existing and future, everywhere in the org” → organization-level aggregated sink; “ingests via Pub/Sub” → destination must be a Pub/Sub topic, not a bucket or dataset.

**30-Second Exam Takeaway**

When a scenario stresses that new projects or folders appear regularly and all of them must be covered without extra setup, that’s a signal for an organization-level aggregated sink rather than a per-project or per-folder sink — then separately verify the destination type actually matches what the downstream consumer requires.

**Official References**

[**Google Cloud — Aggregated sinks (Cloud Logging):**](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks) Supports: the aggregated-sink mechanism, include-children behavior that automatically captures future child projects/folders, and why organization scope beats folder or project scope for this requirement

[**Google Cloud — Route logs to supported destinations:**](https://docs.cloud.google.com/logging/docs/install/logs_export) Supports: the list of supported sink destination types (log bucket, Cloud Storage bucket, BigQuery dataset, Pub/Sub topic), underpinning why Option A’s log-bucket destination cannot serve a Pub/Sub-only SIEM

---

## Question 10

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

Your organization hosts its applications on Google Kubernetes Engine (GKE). Application developers routinely provision cloud resources to support those applications. You want to give developers a way to manage infrastructure as code that follows Google-recommended practices. The approach must let developers define infrastructure through Kubernetes Custom Resource Definitions (CRDs), and it must be a configuration that Google Cloud Support can officially assist with. What should you do?

- [ ] A. Set up Cloud Build with a Terraform builder step that runs terraform plan and terraform apply.
- [ ] B. Deploy and configure Crossplane inside the GKE cluster.
- [ ] C. Set up a GitHub Action that runs a Terraform builder step invoking terraform plan and terraform apply during the pull request workflow.
- [x] D. Deploy and configure Config Connector inside the GKE cluster.

### Explanation

**Correct Answer**

**D. Deploy and configure Config Connector inside the GKE cluster.**

**Exam Reasoning Explanation**

Two independent constraints must both be satisfied: infrastructure has to be expressed through Kubernetes CRDs specifically, and the resulting setup has to be something Google Cloud Support can officially assist with. Both Terraform-based options define infrastructure in Terraform configuration executed by the Terraform CLI — not as Kubernetes CRDs — so they fail the first constraint regardless of which CI/CD system runs them. That leaves two CRD-based Kubernetes operators, Config Connector and Crossplane, which both satisfy the first constraint equally well. The second constraint breaks the tie: Config Connector is a Google-built product with official, documented Google support channels, while Crossplane is an independent, community-governed open-source project with no relationship to Google Cloud Support at all. Only Config Connector satisfies both constraints at once.

**Key Exam Clues**

  * “manage infrastructure as code through Kubernetes Custom Resource Definitions (CRDs)” — hard constraint eliminating both Terraform-based options, since Terraform’s HCL configuration is not a Kubernetes CRD

  * “ensure that your chosen setup can be supported by the Google Cloud Support Portal” — hard constraint that separates the two remaining CRD-based tools from each other

  * “adhering to Google-recommended practices” — reinforces favoring the Google-built tool once two options are otherwise functionally equivalent

  * “Application developers frequently create cloud resources” — points toward a Kubernetes-native, GitOps-friendly workflow developers can use with the same tooling they already use for applications

**Why This Is Correct**

Config Connector is a Kubernetes add-on built and published by Google that provides CRDs and controllers mapping directly onto Google Cloud resources — for example, creating a StorageBucket or SQLInstance custom resource causes Config Connector to provision the corresponding Google Cloud resource. Running it inside GKE lets developers manage infrastructure with the same kubectl-based, declarative workflow they already use for application manifests. Because it is a Google-authored product with officially documented support and issue-tracking channels, it is the configuration that satisfies both the CRD requirement and the Google Cloud Support requirement together.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement:** Running Terraform through Cloud Build is a legitimate, well-supported way to manage infrastructure as code, but it defines infrastructure in Terraform configuration files applied via the Terraform CLI, not Kubernetes CRDs. It fails the scenario’s explicit CRD requirement regardless of how well Cloud Build itself is supported.

**Option B — Violates Requirement:** Crossplane extends Kubernetes with CRDs for managing cloud resources, so it satisfies the CRD requirement on its own merits. However, it is an independent, community-governed open-source project with no official relationship to Google Cloud, so a Crossplane deployment has no path into Google’s official support channels — failing the support requirement.

**Option C — Violates Requirement:** Running Terraform through a GitHub Action during the pull request process has the same core problem as Option A — infrastructure is defined in Terraform, not CRDs — and additionally depends on tooling (GitHub Actions) entirely outside Google Cloud, moving further from a Google-supported configuration rather than closer to one.

**Exam Trap**

The trap is stopping as soon as an option satisfies the CRD requirement, which makes Crossplane look attractive since it is a legitimate, widely used CRD-based infrastructure tool. The scenario layers a second, independent constraint — an official Google support path — that only a Google-built product can satisfy, and the two Terraform options test the opposite failure mode of recognizing “infrastructure as code” without checking that the mechanism is CRD-based at all. Each option has to be checked against both constraints independently. If the support requirement were dropped, Crossplane would become an equally defensible answer.

**Foundation Concept**

Kubernetes Custom Resource Definitions let non-native objects behave like first-class Kubernetes resources, with a controller reconciling them the same way the control plane reconciles built-in objects like Deployments. Several tools apply this pattern to cloud infrastructure so developers can provision cloud resources declaratively with the same kubectl and GitOps tooling used for applications — but exposing resources as CRDs is a technical mechanism, not a support relationship. Whether a given CRD-based tool has an official vendor support path is a separate question that depends entirely on who builds and maintains it.

**Real-World Connection**

A platform team standardizes on Config Connector so developers can request a Cloud SQL instance or a storage bucket using the same YAML manifests and GitOps pipeline they already use to deploy their services, rather than maintaining a separate Terraform workflow and state backend. Because Config Connector is a Google-authored product with documented support and issue-tracking channels, the platform team has a defined, Google-sanctioned path to escalate reconciliation failures or unexpected behavior — something they would not have with a third-party controller like Crossplane that Google has no official relationship with.

**Memory Hook**

CRDs plus an official Google support path together → Config Connector; either Terraform option fails on “CRDs,” Crossplane fails on “Google Cloud Support.”

**30-Second Exam Takeaway**

When a scenario stacks a specific technical mechanism (like CRDs) with a support-channel requirement, check each option against both independently — a technically capable tool can still be wrong if it isn’t a Google-supported product.

**Official References**

[**Google Cloud — Config Connector overview:**](https://cloud.google.com/config-connector/docs/overview) Supports: the CRD-based mechanism Config Connector uses to map Kubernetes objects to Google Cloud resources, and its status as a Google-built product

[**Google Cloud — Get support (Config Controller / Config Connector):**](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/get-support) Supports: the documented, official Google support and issue-tracking channels for Config Connector, contrasted with Crossplane having no such relationship with Google Cloud

---

## Question 11

*Domain 3: Applying Site Reliability Engineering Practices*

You are defining service level objectives for a high-traffic web application whose customers are currently satisfied with its performance and availability. Over a trailing 28-day measurement window, the application’s 90th-percentile latency is 160 ms and its 95th-percentile latency is 300 ms. Which latency SLO should you publish?

- [ ] A. A 90th-percentile latency SLO of 150 ms, paired with a 95th-percentile latency SLO of 290 ms.
- [ ] B. A 90th-percentile latency SLO of 160 ms, paired with a 95th-percentile latency SLO of 300 ms.
- [x] C. A 90th-percentile latency SLO of 190 ms, paired with a 95th-percentile latency SLO of 330 ms.
- [ ] D. A 90th-percentile latency SLO of 300 ms, paired with a 95th-percentile latency SLO of 450 ms.

### Explanation

**Correct Answer**

**C. A 90th-percentile latency SLO of 190 ms, paired with a 95th-percentile latency SLO of 330 ms.**

**Exam Reasoning Explanation**

The SLO must be achievable — not tighter than what the service already delivers — so the team isn’t immediately out of compliance. It should also stay close enough to what users already experience happily that it remains a meaningful signal rather than a number so loose it lets real degradation go unnoticed. Option A sets targets below current measured performance, which the service hasn’t demonstrated it can meet. Option B matches current performance exactly, leaving zero error budget — any ordinary variance breaches it immediately. Option D loosens the targets so far that the published 90th-percentile figure nearly matches today’s 95th-percentile figure, no longer reflecting real user experience. Option C loosens both figures by a modest, deliberate margin, preserving a workable error budget while staying anchored to today’s actual performance.

**Key Exam Clues**

  * “Customers are currently happy with the application performance” — signals current measured performance is the right anchor point; the published SLO shouldn’t diverge sharply from it in either direction

  * “90th percentile of latency is 160 ms and the 95th percentile of latency is 300 ms” — the baseline both figures in a correct option must sit at or modestly above, eliminating anything below these values

  * “over a 28-day window” — a sustained measurement, not a single data point, making it a credible basis for the target rather than something needing heavy discounting

  * Two coupled thresholds — a correct answer must get both the 90th- and 95th-percentile figures right simultaneously, not just one

**Why This Is Correct**

Publishing an SLO at or below current measured performance leaves no room for ordinary variance in traffic, infrastructure, or dependencies — any normal fluctuation would immediately put the service out of SLO and exhaust the error budget before a genuine problem even occurs. Setting the target a modest amount looser than current performance, as this option does, creates a workable error budget while staying close enough to today’s experience that a real regression will still breach the SLO and trigger a response. This balances defensibility with meaningfulness in a way none of the other options do.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement:** Both figures (150 ms and 290 ms) are tighter than what the service currently delivers (160 ms and 300 ms). Publishing an SLO the service doesn’t already meet puts it out of compliance immediately, with no realistic path to meeting it without first improving the system — contradicting the premise that customers are already happy with current performance.

**Option B — Technically Possible but Not Best:** Matching the SLO exactly to current measured performance looks appealing because the service meets it by construction, but it leaves zero error budget. Any small fluctuation in traffic or dependency behavior pushes the service out of SLO, making the target brittle and difficult to defend operationally.

**Option D — Violates Requirement:** Loosening the targets this far (300 ms and 450 ms) means the published SLO no longer reflects the experience customers are actually happy with — the 90th-percentile target alone is nearly double today’s measured value. A target this loose would let a genuine, user-impacting regression occur without ever breaching the SLO, defeating its purpose as an early warning signal.

**Exam Trap**

The trap is reading “base the SLO on current measurement” as “set the SLO equal to current measurement” (Option B), rather than using the measurement as a starting anchor with deliberate headroom built in. The opposite trap is assuming more headroom is always safer, which makes Option D look reasonable — but excessive headroom turns the SLO into a number that no longer represents genuine user happiness, since real degradations could occur well within the published target. The correct answer sits between these two failure modes; further tightening or loosening comes later, from comparing the SLO against actual user-satisfaction signals, not from guessing a wide margin upfront.

**Foundation Concept**

A sound starting SLO is typically derived from a recent, sustained measurement window and then loosened by a modest, deliberate margin rather than published as an exact match to that measurement. This creates an error budget — the gap between “always meets target” and the published objective — that absorbs ordinary variance and gives engineering teams room to make changes without immediately breaching the SLO, while staying close enough to actual performance to remain a meaningful signal of user happiness. The target is refined further over time by comparing it against real indicators of user satisfaction, such as support tickets or sentiment data.

**Real-World Connection**

A team publishing its first formal SLO for a service users already like takes the current 28-day latency percentiles as a baseline, adds a modest buffer, and publishes that as the objective rather than the raw measured numbers. This gives the on-call team a genuine error budget to absorb routine fluctuations from deploys, traffic spikes, or dependency hiccups without constant SLO-violation alerts, while keeping the target tight enough that a real regression — say, a bad release pushing 90th-percentile latency to 250 ms — still breaches the SLO and triggers the team’s error budget policy.

**Memory Hook**

Anchor the SLO to current measured performance, then loosen it by a modest margin — never match it exactly (zero error budget) and never loosen it so far that it stops reflecting real user experience.

**30-Second Exam Takeaway**

When a question gives current measured performance and asks what SLO to publish, rule out anything tighter than the measurement, rule out an exact match (zero error budget), and rule out an excessively loose target that would stop representing real user experience — the right answer sits a modest, deliberate margin above what’s already being delivered.

**Official References**

[**Google SRE Workbook — Chapter 2: Implementing SLOs:**](https://sre.google/workbook/implementing-slos/) Supports: the methodology of deriving a starting SLO from a recent measurement window and loosening it by a modest margin rather than publishing the exact measured value, illustrated by the book’s own worked example (90th-percentile latency measured at 432 ms, published SLO of 450 ms)

---

## Question 12

*Domain 2: Building and Implementing CI/CD Pipelines*

Your organization is beginning to containerize its workloads on Google Cloud. You need a fully managed storage solution capable of holding both container images and Helm charts, and it must integrate natively with the Google Cloud services you already rely on — Google Kubernetes Engine (GKE), Cloud Run, VPC Service Controls, and Identity and Access Management (IAM). What should you do?

- [ ] A. Configure Docker’s registry storage driver to use a Cloud Storage bucket owned by your organization as the backing store.
- [ ] B. Deploy an open source container registry server inside GKE, locked down with a restrictive role-based access control (RBAC) configuration.
- [x] C. Configure Artifact Registry as an OCI-based registry that stores both container images and Helm charts.
- [ ] D. Configure Container Registry as an OCI-based registry for container images.

### Explanation

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

---

## Question 13

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your organization runs several Google Kubernetes Engine (GKE) clusters within a single project. You need a highly available way to collect and query both your own domain-specific workload metrics and GKE’s default metrics across every cluster, while keeping operational overhead to a minimum. What should you do?

- [ ] A. Install Prometheus in every cluster using the Prometheus Operator, scrape the metrics there, configure remote-write to a single central Prometheus instance, and query that central instance.
- [ ] B. Enable managed collection on every GKE cluster, and query the resulting metrics in BigQuery.
- [ ] C. Install Prometheus in every cluster using the Prometheus Operator, scrape the metrics there, enable a Thanos sidecar on each Prometheus instance, deploy Thanos in a central cluster, and query that central Thanos instance.
- [x] D. Enable managed collection on every GKE cluster, and query the resulting metrics in Cloud Monitoring.

### Explanation

**D. Enable managed collection on every GKE cluster, and query the resulting metrics in Cloud Monitoring.**

**Correct Answer**

**D. Enable managed collection on every GKE cluster, and query the resulting metrics in Cloud Monitoring.**

**Exam Reasoning Explanation**

Must-have constraints: native high availability with no DIY engineering, low ongoing operational burden, ingestion of two distinct metric sources — custom Prometheus-format workload metrics and GKE’s built-in default metrics — and one query surface spanning every cluster. Not a requirement: a particular query language or tool, only that both metric types are queryable together. Capability: Google Cloud Managed Service for Prometheus’s managed collection mode runs the scraping and collection machinery for you in each cluster, with nothing to deploy, scale, or shard yourself, and ships everything into the same backend Cloud Monitoring uses — a globally distributed, highly available time-series store. Cloud Monitoring then exposes GKE’s default metrics and any custom workload metrics side by side via PromQL, across every cluster, from one place. Elimination: Options A and C both require you to deploy and operate Prometheus (and, for C, Thanos) in every cluster plus a central aggregation layer you must keep highly available yourself — the opposite of minimizing operational overhead. Option B gets the collection step right but sends the query step to BigQuery, which isn’t where these metrics natively live or get queried. Decision: only D pairs zero-maintenance collection with the metrics’ already-highly-available, native query surface.

**Key Exam Clues**

  * “highly available” — a hard constraint that must be satisfied by the platform itself, not something you engineer on top of it.

  * “minimizing operational overhead” — a hard constraint eliminating any option where you deploy, scale, or federate Prometheus or Thanos yourself.

  * “both domain-specific workload metrics and GKE default metrics” — a technical signal requiring one solution that natively ingests both custom application metrics and GKE’s built-in system metrics.

  * “across all clusters” — requires a single, unified, multi-cluster query surface rather than per-cluster silos or manual federation.

  * “query” — the solution needs a convenient native query path, not just storage, which is what eliminates routing to BigQuery.

**Why This Is Correct**

Managed collection is Google’s own recommended approach for Kubernetes environments precisely because it removes the work of deploying, scaling, sharding, configuring, and maintaining Prometheus servers — you enable it per cluster and the collection runs itself. Because Managed Service for Prometheus shares its backend and APIs with Cloud Monitoring, both GKE’s default metrics and any custom, domain-specific workload metrics scraped under managed collection land in the same store and become queryable together with PromQL inside Cloud Monitoring, across every cluster in the project, with no central query tier for you to assemble. The backing store is Google’s own highly available, globally distributed time-series database, so the “highly available” requirement is met by the platform rather than by anything you design or operate.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** Self-deployed Prometheus via the Prometheus Operator is a supported collection mode, but it puts you back in charge of deploying, scaling, and maintaining a Prometheus server in every cluster. Remote-writing everything into one central Prometheus instance also adds a component you must separately make highly available — a single Prometheus instance isn’t inherently HA — working against both “highly available” and “minimizing operational overhead.”

**Option C — Technically Possible but Not Best:** Pairing self-deployed Prometheus with a Thanos sidecar and a central Thanos deployment is a well-known way to get multi-cluster federation and HA, but it means deploying, configuring, and operating an entire additional system — Thanos components, object storage, compaction — on top of Prometheus itself, which is substantially more operational overhead than enabling a managed feature.

**Option B — Different Use Case:** Managed collection is the right ingestion choice, but Managed Service for Prometheus data isn’t natively stored in or queried from BigQuery — it’s queried through Cloud Monitoring (or any PromQL-compatible tool pointed at that backend). Routing to BigQuery would mean building and maintaining an export pipeline just to answer a question the native query surface already handles, adding overhead rather than minimizing it.

**Exam Trap**

The trap is treating the word “Prometheus” as a cue to reach for a traditional self-hosted architecture, especially when an option describes a legitimate, well-known HA pattern like Thanos federation. The decisive phrase is “minimizing operational overhead”: any option where you are the one deploying, scaling, or federating Prometheus or Thanos servers fails that constraint no matter how sound the architecture is otherwise.

**Foundation Concept**

Google Cloud Managed Service for Prometheus stays Prometheus-compatible at the collection and query layer — PromQL, scrape configs, standard exporters — while swapping the operational burden of running Prometheus servers for a managed collector and Google’s own highly available metrics backend. The transferable skill is recognizing “collect once, query everywhere, someone else runs the infrastructure” as the signature of a managed service, versus “I deploy and federate the infrastructure myself” as the signature of a self-hosted one — a distinction that applies to observability tooling generally, not just Prometheus.

**Real-World Connection**

Organizations running many GKE clusters commonly standardize on managed collection specifically to avoid the recurring work of patching, resizing, and troubleshooting their own Prometheus/Thanos stack, freeing engineering time for the metrics and alerts that actually matter, while keeping full PromQL compatibility so existing dashboards, alerting rules, and Grafana integrations continue to work unchanged.

**Memory Hook**

“Managed collection in, Cloud Monitoring out” — if you’re the one running or federating Prometheus or Thanos yourself, you’ve already added the overhead the question asked you to minimize.

**30-Second Exam Takeaway**

When a multi-cluster GKE scenario asks for highly available metrics collection with minimal operational overhead, favor the option that enables Managed Service for Prometheus’s managed collection and queries through Cloud Monitoring — any option where you personally deploy, scale, or federate Prometheus or Thanos is solving the HA problem the hard way.

**Official References**

[**Google Cloud — Google Cloud Managed Service for Prometheus:**](https://cloud.google.com/managed-prometheus) Supports: confirms managed collection eliminates the operational burden of deploying, scaling, and maintaining Prometheus, and that the backend is a highly available, globally distributed time-series database

[Google Cloud — Google Cloud Managed Service for Prometheus overview (data collection methods): ](https://cloud.google.com/stackdriver/docs/managed-prometheus)Supports: confirms managed collection is Google’s recommended approach for Kubernetes environments and that metrics are queried via PromQL in Cloud Monitoring, not BigQuery

---

## Question 14

*Domain 5: Optimizing Performance and Cost*

You monitor a service built on n2-standard-2 Compute Engine instances that serve large files to end users, and customers have been reporting slow downloads. Your Cloud Monitoring dashboard confirms the VMs are consistently hitting their maximum network throughput. You need to raise the network throughput ceiling for these instances. What should you do?

- [ ] A. Attach additional virtual network interface controllers (vNICs) to each VM.
- [ ] B. Deploy a Cloud NAT gateway and attach it to the VMs’ subnet.
- [x] C. Resize the VMs to the n2-standard-8 machine type.
- [ ] D. Install the Ops Agent on the VMs to export additional monitoring metrics.

### Explanation

**Correct Answer**

**C. Resize the VMs to the n2-standard-8 machine type.**

**Exam Reasoning Explanation**

The fix has to raise the actual network throughput ceiling, since the dashboard confirms the VMs are already saturating their current cap. Google Cloud enforces network bandwidth limits per compute instance based on machine type and vCPU count, not per network interface, so adding vNICs (A) does nothing to raise the cap. Cloud NAT (B) solves an unrelated problem — outbound internet access for instances without external IPs — and has no effect on bandwidth ceilings. The Ops Agent (D) only adds observability, not capacity. Increasing the vCPU count by moving to a larger machine type (C) directly raises the per-instance maximum egress bandwidth, since that limit scales with vCPU count up to the machine series’ cap, making it the only option that actually increases available throughput.

**Key Exam Clues**

  * “running at peak network throughput” — the decisive signal that the bottleneck is the instance’s bandwidth cap, not an unrelated connectivity or configuration issue

  * “n2-standard-2” — a small vCPU count, implying real headroom to grow within the N2 series before hitting its bandwidth ceiling

  * “serve large files” / “downloads are slow” — frames this as a sustained egress-bandwidth problem rather than a one-off latency or routing issue

  * “improve the network throughput performance” — specifically asks for a capacity fix, ruling out anything that only adds visibility (Ops Agent) or addresses outbound internet access for private instances (Cloud NAT)

**Why This Is Correct**

Google Cloud’s per-instance maximum egress bandwidth is generally around 2 Gbps per vCPU, up to a cap defined by the machine series. Moving from n2-standard-2 (2 vCPUs) to n2-standard-8 (8 vCPUs) quadruples the vCPU count, directly raising the per-instance bandwidth ceiling within the N2 family’s limits. Since the VMs are already measured at their current peak, this change actually gives them room to serve files faster rather than leaving them capped where they already sit.

**Why the Other Options Are Not the Best Fit**

**Option A — Incorrect:** Google Cloud accounts for network bandwidth per compute instance, not per virtual network interface. Adding more vNICs does not raise a VM’s aggregate egress or ingress bandwidth limit — the instance remains capped at the same total throughput regardless of how many interfaces that traffic is split across.

**Option B — Different Use Case:** Cloud NAT provides outbound internet connectivity for instances without external IP addresses; it has no effect on an instance’s network bandwidth ceiling. Since the VMs here are already serving traffic — just slowly — the problem isn’t connectivity, it’s throughput capacity, which Cloud NAT doesn’t address.

**Option D — Violates Requirement:** The Ops Agent exports additional monitoring and logging metrics; it’s an observability tool, not a performance capability. Deploying it would give more visibility into the problem but do nothing to raise the network throughput ceiling the scenario asks you to improve.

**Exam Trap**

The trap is assuming that because traffic flows through NICs, adding more NICs must increase available bandwidth — but Google Cloud explicitly caps bandwidth at the instance level based on machine type, not per interface, so Option A looks intuitively correct while being technically wrong. A secondary trap is reaching for Cloud NAT whenever “network” and “VM” appear together, without noticing that NAT addresses outbound connectivity for private instances, not throughput capacity for instances that are already reachable and transferring data.

**Foundation Concept**

Compute Engine enforces a maximum egress (and roughly similar ingress) bandwidth per instance, derived primarily from vCPU count and machine series — generally around 2 Gbps per vCPU up to a series-specific ceiling. This limit applies to the instance as a whole regardless of how many network interfaces or IP addresses it has, which is why scaling vCPUs — by resizing to a larger machine type, or enabling a high-bandwidth Tier_1 networking configuration on qualifying machine types — are the mechanisms that actually raise available throughput.

**Real-World Connection**

A team serving large media or software downloads from Compute Engine VMs notices download speeds plateauing as demand grows, and monitoring confirms the VMs are pinned at their network bandwidth cap. Rather than adding more interfaces or spinning up unrelated networking components, they resize the instances to a larger machine type (or enable Tier_1 networking on a qualifying series) to raise the per-instance throughput ceiling, directly improving the download experience without re-architecting the service.

**Memory Hook**

Bandwidth caps are per-instance (vCPU-based), not per-NIC — to raise the ceiling, scale the machine type, not the interface count.

**30-Second Exam Takeaway**

When a VM is confirmed to be at its network throughput ceiling, look for a fix that raises the per-instance bandwidth cap — typically a larger machine type or Tier_1 networking — and rule out adding NICs, which Google Cloud explicitly does not credit toward instance bandwidth, along with unrelated tools like Cloud NAT or monitoring agents.

**Official References**

[**Google Cloud — Network bandwidth:**](https://docs.cloud.google.com/compute/docs/network-bandwidth) Supports: bandwidth being accounted per compute instance rather than per vNIC, vCPU-based scaling of the per-instance egress cap, and the N2 machine series bandwidth limits

---

## Question 15

*Domain 3: Applying Site Reliability Engineering Practices*

You recently migrated an ecommerce application onto Google Cloud, and you now need to get it ready for the approaching peak shopping season. You want to follow Google-recommended practices for this preparation. What is the first thing you should do to get ready for the high-traffic period?

- [ ] A. Re-platform the application onto Cloud Run and rely on its built-in autoscaling.
- [ ] B. Write a Terraform configuration for the application’s infrastructure so you can quickly stand it up in additional regions.
- [x] C. Run load tests against the application to profile how it performs and scales.
- [ ] D. Pre-provision the same amount of additional compute capacity used during last year’s peak season, on the assumption that this year’s growth will be similar.

### Explanation

**Correct Answer**

**C. Run load tests against the application to profile how it performs and scales.**

**Exam Reasoning Explanation**

The “first” step must be the one that generates the data every other decision depends on. Options A, B, and D each commit to a specific architectural or capacity decision — re-platforming to Cloud Run, building multi-region deployment automation, or copying last season’s provisioning numbers — without first knowing how the newly migrated application actually performs or where it breaks under load. Google’s own peak-event preparation guidance places load testing early in the preparation phase, months ahead of the event, precisely because it reveals the bottlenecks and scaling behavior that then inform every subsequent architecture and capacity decision. Only load testing produces that foundational data, making it the correct first action; the other three are plausible later steps that are premature without it.

**Key Exam Clues**

  * “recently migrated” — the application’s behavior on Google Cloud is unproven, so prior performance data (and, by extension, last season’s provisioning figures) can’t be trusted to transfer directly

  * “what should you do first” — signals a sequencing question where several options could eventually be reasonable, but only one belongs at the very start

  * “follow Google-recommended practices” — points to Google’s own documented peak-event methodology, which places load testing in the preparation phase ahead of architecture changes

  * “prepare for the upcoming peak traffic season” — a known, anticipated event, which Google’s guidance treats as something to test for well in advance rather than react to

**Why This Is Correct**

Load testing reveals how the newly migrated application actually behaves under increasing demand — where it bottlenecks, how its components scale, and what capacity it genuinely needs — using real data from the current Google Cloud deployment rather than assumptions carried over from before the migration. That data is the necessary input for every subsequent decision: whether to re-platform a component, how many regions to deploy to, or how much capacity to provision. Doing it first, well ahead of the peak season, is also explicitly how Google’s own peak-event preparation guidance sequences this work.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** Moving to Cloud Run and relying on autoscaling can be a reasonable architectural choice, but committing to it before understanding the application’s current bottlenecks and scaling behavior is premature — you don’t yet know whether the application’s architecture even suits Cloud Run’s execution model, or where its real constraints lie.

**Option B — Technically Possible but Not Best:** Automating infrastructure deployment to additional regions is valuable, but it assumes multi-region expansion is the right response to peak load without first confirming that regional capacity, rather than some other bottleneck entirely, is actually what limits the application under load.

**Option D — Violates Requirement:** Pre-provisioning based on last season’s compute usage assumes the application’s resource needs on its new Google Cloud infrastructure mirror its needs on whatever platform it ran on before migration, and assumes a growth figure without any current data to support it. This is guesswork rather than the data-driven approach Google recommends, and it skips the step that would reveal whether last season’s numbers are even relevant anymore.

**Exam Trap**

The trap is picking an option that sounds like solid peak-season preparation — more autoscaling, more automation, more pre-provisioned capacity — without noticing that each one presupposes knowledge the team doesn’t have yet, since the application was only just migrated. The “first” in the question is the tell: it’s asking which action produces the information the other actions would need to be well-informed, not which action sounds the most proactive in isolation.

**Foundation Concept**

Capacity planning and architectural decisions for a known, high-stakes event should be grounded in current, measured performance data rather than assumptions carried over from a previous environment or a previous season. Load testing supplies that data by simulating expected (and above-expected) traffic against the actual production environment, surfacing bottlenecks and scaling limits before they become customer-facing incidents, and giving every later decision — scaling strategy, regional footprint, provisioned capacity — a factual basis instead of a guess.

**Real-World Connection**

A retailer that just migrated its storefront to Google Cloud runs load tests simulating its expected Black Friday traffic months in advance, discovering that a particular database connection pool, not raw compute capacity, is the actual bottleneck at scale. That finding changes their entire preparation plan — instead of blindly provisioning more VMs or committing to a platform migration, they fix the specific constraint the test revealed, then validate the fix with another round of testing before the season arrives.

**Memory Hook**

Just migrated, peak season coming → load test first; everything else (autoscaling platform, multi-region automation, pre-provisioning) is a decision that load-test data should inform, not precede.

**30-Second Exam Takeaway**

When a scenario asks what to do “first” to prepare a recently migrated or newly deployed application for a known high-traffic event, look for the option that generates performance data — load testing — rather than one that commits to a specific architecture or capacity decision before that data exists.

**Official References**

[**Google Cloud — Prepare for a peak capacity event:**](https://docs.cloud.google.com/support/docs/checklists/plan-peak-capacity-event) Supports: load testing and capacity planning as part of the documented preparation phase for a known high-traffic event, ahead of architecture or capacity commitments

[**Google Cloud — Conduct load testing:**](https://docs.cloud.google.com/support/docs/peak-events/conduct-load-testing) Supports: load testing as an early step (recommended three to five months before the event) that determines whether the system will scale successfully and surfaces bottlenecks before other preparation decisions are made

---

## Question 16

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

You are setting up a continuous integration pipeline whose integration-testing build step needs to reach APIs that live inside your private VPC network. Your security team has mandated that API traffic must never be exposed publicly. You also need a solution that keeps management overhead to a minimum. What should you do?

- [x] A. Run the build on Cloud Build private pools, peered into the private VPC.
- [ ] B. Deploy Spinnaker for Google Cloud and connect it to the private VPC.
- [ ] C. Run the build on Cloud Build’s default pool, and front the APIs with an Internal HTTP(S) Load Balancer.
- [ ] D. Run the build on Cloud Build’s default pool, and front the APIs with an External HTTP(S) Load Balancer protected by a Google Cloud Armor policy.

### Explanation

**Correct Answer**

**A. Run the build on Cloud Build private pools, peered into the private VPC.**

**Exam Reasoning Explanation**

Two constraints must both be satisfied: API traffic must never be exposed publicly, and the solution should minimize management overhead. Cloud Build’s default worker pool runs outside the customer’s VPC with no inherent path into private resources, so “default pool plus a load balancer” doesn’t actually solve connectivity on its own — an external load balancer (D) directly violates the no-public-exposure requirement regardless of Cloud Armor, and an internal load balancer (C) doesn’t give default-pool workers, which sit outside the VPC, any way to reach it without extra networking work. Spinnaker (B) is a deployment-orchestration tool, not a mechanism for private build-time network access, and self-hosting it adds overhead rather than removing it. Cloud Build private pools (A) are purpose-built for exactly this problem: fully managed, scaling to zero with no infrastructure to maintain, and connected to the customer’s VPC via private peering so builds reach internal resources without any traffic touching the public internet — satisfying both constraints at once.

**Key Exam Clues**

  * “requires access to APIs inside your private VPC network” — hard constraint that the build execution environment itself needs network reachability into the VPC, not just that the API exists somewhere

  * “do not expose API traffic publicly” — hard constraint eliminating any option that fronts the API with a public-facing component, however well protected

  * “minimizes management overhead” — hard constraint favoring a fully managed, Google-operated solution over anything self-deployed or requiring extra infrastructure

  * “CI pipeline” / “build step” — frames this as a Cloud Build execution-environment problem specifically, not a general application traffic-routing problem

**Why This Is Correct**

Cloud Build private pools are a fully managed, dedicated worker pool hosted and automatically scaled by Google — including to zero — with no infrastructure for the customer to set up, patch, or scale. Because the private pool’s network is peered directly with the customer’s VPC, builds running in the pool can reach private resources, including internal APIs, using only internal IP addressing, with no traffic ever crossing the public internet. This satisfies both the no-public-exposure requirement and the low-overhead requirement in a single, purpose-built configuration.

**Why the Other Options Are Not the Best Fit**

**Option B — Different Use Case:** Spinnaker is a continuous delivery and deployment-orchestration tool, not a mechanism for giving a CI build step private network access. Standing it up to solve this specific connectivity problem means deploying and operating an additional system, increasing management overhead rather than minimizing it, and it still wouldn’t natively solve how build steps reach private VPC resources.

**Option C — Technically Possible but Not Best:** An internal load balancer keeps the API off the public internet, which is a step in the right direction, but Cloud Build’s default worker pool runs outside the customer’s VPC and has no inherent path to an internal, VPC-only IP address. Making this work requires additional networking configuration layered on top of the default pool — complexity that private pools avoid entirely by being peered into the VPC from the start.

**Option D — Violates Requirement:** An external HTTP(S) load balancer is, by definition, internet-facing. A Cloud Armor policy improves the security posture of that public endpoint, but doesn’t change the fact that the API becomes reachable over the public internet, directly contradicting the security team’s explicit requirement.

**Exam Trap**

The trap is assuming that any load balancer paired with a security control — an internal LB, or an external LB with Cloud Armor — is an equally valid way to expose an API to a CI pipeline, without checking where the pipeline’s build workers actually run. Cloud Build’s default pool executes outside the customer’s VPC, so neither load-balancer option solves the fundamental reachability problem on its own, and the external option additionally breaks the explicit “no public exposure” requirement regardless of how well it’s protected.

**Foundation Concept**

By default, Cloud Build executes builds in a Google-managed environment with public internet access but no connectivity into a customer’s private VPC. Private pools solve this by running builds in a dedicated, customer-specific pool hosted in a Google-owned service producer network that is peered directly with the customer’s VPC, giving builds internal-IP-only access to private resources without any additional load balancing, VPN, or custom networking layer — all while remaining fully managed by Cloud Build itself.

**Real-World Connection**

A platform team running integration tests that call internal microservices during every CI build switches their build step from Cloud Build’s default pool to a private pool peered with their VPC. Their build steps can now reach internal APIs directly over private IPs, satisfying the security team’s no-public-exposure policy, while the platform team avoids having to design, secure, or operate any additional networking infrastructure — Cloud Build handles the pool’s scaling and lifecycle automatically.

**Memory Hook**

CI build needs private VPC access, no public exposure, low overhead → Cloud Build private pools (peered into the VPC); an external load balancer is public by definition, and an internal one alone doesn’t get a default-pool build worker into the VPC in the first place.

**30-Second Exam Takeaway**

When a CI/CD build step needs to reach resources inside a private VPC without public exposure and with minimal operational overhead, look for a fully managed, VPC-peered execution environment — like Cloud Build private pools — rather than adding load balancers or standing up additional orchestration tools around a build runner that was never on the VPC to begin with.

**Official References**

[**Google Cloud — Private pools overview:**](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview) Supports: private pools being fully managed with no infrastructure to maintain, and their VPC-peering mechanism that gives builds private-only access to internal resources

---

## Question 17

*Domain 2: Building and Implementing CI/CD Pipelines*

You are investigating a failed deployment in your CI/CD pipeline. Deployment logs show that the application container could not start because a required environment variable was missing.

You need to identify the configuration error and add a safeguard to the CI/CD workflow to prevent similar failures. What should you do?

- [ ] A. Adopt a canary deployment strategy.
- [ ] B. Add static code analysis to the CI pipeline.
- [x] C. Add integration tests to the CI pipeline.
- [ ] D. Enable Cloud Audit Logs for deployment operations.

### Explanation

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

---

## Question 18

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

Your company recently completed a migration to Google Cloud. You now need to design a fast, reliable, and repeatable way for the organization to provision new projects and their foundational resources in Google Cloud. What should you do?

- [ ] A. Create each new project manually through the Google Cloud console.
- [ ] B. Write a gcloud CLI script that accepts the request’s parameters and provisions the project, and store that script in a Git repository.
- [ ] C. Author your own Terraform module from scratch, store it in your source control repository, and run terraform apply against a copy of it for each new project.
- [x] D. Adopt the Terraform modules provided by the Cloud Foundation Toolkit, and apply them with the appropriate parameters to create each Google Cloud project and its related resources.

### Explanation

**Correct Answer**

**D. Adopt the Terraform modules provided by the Cloud Foundation Toolkit, and apply them with the appropriate parameters to create each Google Cloud project and its related resources.**

**Exam Reasoning Explanation**

The solution has to be fast, reliable, and repeatable for provisioning projects and their basic resources. Manual console creation (A) is inherently non-repeatable and slow at scale, dependent on a person correctly redoing every step each time. A custom gcloud CLI script (B) codifies the steps but is imperative — the team must build and maintain their own idempotency, error handling, and drift detection. Writing a custom Terraform module from scratch (C) gets declarative, state-managed infrastructure as code, but the team still has to design and validate their own best-practice provisioning logic before it’s trustworthy. The Cloud Foundation Toolkit (D) already provides that logic as Google-maintained, best-practice Terraform modules purpose-built for exactly this task, so applying it with the team’s own parameters delivers speed (no module to design), reliability (maintained, widely used code), and repeatability (a standard Terraform workflow) in one step.

**Key Exam Clues**

  * “fast, reliable, and repeatable” — the three criteria every option must be checked against; manual work fails “fast” and “repeatable” immediately

  * “recently migrated to Google Cloud” — implies the team doesn’t yet have mature internal tooling, favoring a solution that supplies that maturity rather than requiring them to build it

  * “provision new projects and basic resources” — a standard, well-understood task, exactly what a pre-built, parameterized toolkit is designed to handle

  * “new projects” implying an ongoing need — signals this must scale as a repeatable process, not a one-off action

**Why This Is Correct**

The Cloud Foundation Toolkit provides Google-maintained Terraform modules — such as a project-factory-style module — that already encode best practices for provisioning a new Google Cloud project and its foundational resources: IAM bindings, API enablement, networking attachment, and similar basics, as parameterized, reusable code. Applying this existing code with the appropriate parameters is faster than designing equivalent logic from scratch, more reliable because the modules are actively maintained, and fully repeatable because each new project is just another parameterized apply of the same proven module — satisfying all three stated criteria at once.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement:** Manually creating projects through the console depends entirely on someone correctly repeating every configuration step each time. It doesn’t scale, isn’t fast beyond a handful of projects, and offers no built-in guarantee of consistency between projects — failing “reliable” and “repeatable” outright.

**Option B — Technically Possible but Not Best:** A gcloud CLI script is more repeatable than manual console work, but it’s an imperative script the team must design, test, and maintain themselves, including retries, partial failures, and drift — concerns a declarative, state-tracked tool like Terraform manages natively. It also means building provisioning best practices from scratch instead of reusing Google’s.

**Option C — Technically Possible but Not Best:** A custom Terraform module is a real improvement — declarative and state-managed — but it still requires the team to design and validate their own best-practice provisioning logic before it can be trusted at scale, which is slower to get right and more prone to missing edge cases than adopting the Cloud Foundation Toolkit’s existing, maintained modules for the same purpose.

**Exam Trap**

The trap is treating any Terraform-based option as equally good once it’s declarative and version-controlled, without noticing that one option (C) still requires building the provisioning logic yourself while the other (D) lets you reuse logic Google already built and maintains. The fastest, most reliable path to a repeatable process is rarely to author it from scratch when a purpose-built, well-tested toolkit already exists for exactly this task.

**Foundation Concept**

Infrastructure as code becomes genuinely fast, reliable, and repeatable not merely by being declarative and version-controlled, but by being built on modules that are already tested, maintained, and aligned with best practices — so provisioning a new instance of a standard resource, like a project, is a matter of supplying parameters to proven code rather than designing that code anew each time it’s needed.

**Real-World Connection**

A platform team standardizes new-project requests by wiring an intake process to a Cloud Foundation Toolkit project module: a requester supplies a project name, owning team, and a few other parameters, and the team applies the module to produce a correctly configured project — with the right IAM bindings, enabled APIs, and network attachments — in minutes, consistently, without hand-crafting provisioning logic for every request or risking configuration drift between projects created months apart.

**Memory Hook**

Fast, reliable, repeatable project provisioning → reuse the Cloud Foundation Toolkit’s existing Terraform modules, don’t build equivalent logic yourself from a script or a module you author from scratch.

**30-Second Exam Takeaway**

When a scenario asks for a fast, reliable, repeatable way to provision standard Google Cloud resources like new projects, favor an existing, Google-maintained toolkit of modules over writing custom scripts or custom Terraform from scratch — reusing proven, parameterized code beats building equivalent logic yourself.

**Official References**

[Google Cloud — Terraform blueprints and modules for Google Cloud (Cloud Foundation Toolkit): ](https://cloud.google.com/docs/terraform/blueprints/terraform-blueprints)Supports: the Cloud Foundation Toolkit’s production-ready, best-practice Terraform modules for automating the provisioning of Google Cloud projects and related resources

---

## Question 19

*Domain 3: Applying Site Reliability Engineering Practices*

Your company is planning a major marketing event for an online retail site during the holiday shopping season, and you expect the web application to receive a large volume of traffic in a short window. You need to prepare the application for potential failures during the event. What should you do? (Choose two.)

- [ ] A. Set up Anthos Service Mesh on the application so you can spot issues on its topology map.
- [x] B. Confirm that the relevant system metrics are being collected in Cloud Monitoring, and configure alerts at thresholds that matter to you.
- [x] C. Review your expected increase in capacity requirements and plan out the quota management you’ll need to support it.
- [ ] D. Track your services’ latency using an average percentile latency measurement.
- [ ] E. Configure Cloud Monitoring alerts for every common failure your application experiences.

### Explanation

**Correct Answer**

**B. Confirm that the relevant system metrics are being collected in Cloud Monitoring, and configure alerts at thresholds that matter to you.**

**C. Review your expected increase in capacity requirements and plan out the quota management you’ll need to support it.**

**Exam Reasoning Explanation**

Preparing for a known, high-stakes traffic event has two independent needs: having enough capacity to absorb the expected load, and having the visibility to detect and respond when something does go wrong. C directly addresses capacity — without reviewing increased needs and planning quota management in advance, the application can be throttled or fail outright no matter how well it’s monitored. B directly addresses observability — meaningful, well-tuned alerts on relevant metrics let the team detect and react to real problems during the event. Option A proposes deploying new infrastructure tooling shortly before a high-stakes event, adding risk rather than readiness. Options D and E each sound like reasonable monitoring practices but describe flawed implementations: averaged latency hides the tail-latency problems that actually hurt users, and alerting on every common failure produces noise rather than actionable signal. B and C work independently — one is a capacity action, the other an observability action — and together they form a complete readiness picture: enough capacity, plus the ability to detect trouble if capacity or anything else still goes wrong.

**Key Exam Clues**

  * “prepare your application for potential failures during the event” — frames this as readiness with two distinct angles: having enough capacity, and being able to detect problems

  * “large volume of traffic in a short period” — signals a capacity/quota concern specifically, since everyday quotas may not cover a sudden spike

  * “alerts at levels of interest” (B) versus “all common failures” (E) — a deliberate contrast between targeted, meaningful alerting and indiscriminate alerting

  * “average percentile latency” (D) — an internally inconsistent phrase signaling a flawed metric choice, since averages and percentiles summarize a distribution in different, non-interchangeable ways

**Why This Is Correct**

Reviewing increased capacity requirements and planning quota management (C) ensures the application has enough underlying resource headroom to actually handle the expected spike — without it, the event could fail regardless of monitoring quality, since requests could be throttled or rejected at the infrastructure or API level. Ensuring relevant metrics are captured with alerts set at meaningful thresholds (B) ensures that if something does go wrong, the team finds out quickly enough to respond rather than discovering it through customer complaints. Together these cover both halves of event readiness — sufficient capacity, and the ability to detect trouble when it happens — and neither one substitutes for the other, which is why both are needed and the set is complete at two.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** Service mesh topology visibility can eventually be useful, but introducing new infrastructure tooling into the application shortly before a known high-stakes event adds operational risk and complexity precisely when stability matters most, rather than directly strengthening readiness for the event itself.

**Option D — Violates Requirement:** Monitoring latency as an “average” obscures the tail latency that actually affects user experience — a service with a low average but a long tail of slow requests can still be delivering a poor experience to a meaningful share of users. SRE practice favors percentile-based latency metrics specifically because they surface this tail behavior that averages hide.

**Option E — Violates Requirement:** Alerting on every common failure generates a high volume of low-value notifications, many of which may be routine or self-correcting. This creates alert fatigue, making it harder, not easier, for the on-call team to notice and act on the alerts that actually matter during a high-traffic event.

**Exam Trap**

The trap is picking any option containing “monitor” or “alert” without checking whether it describes monitoring and alerting done well. D sounds like good observability practice but names an inferior metric; E sounds like proactive readiness but describes a noisy, unfocused alerting strategy. The correct pair requires recognizing that readiness for a known traffic spike needs both adequate capacity and well-targeted detection — not just “more monitoring” or “more infrastructure” in any form.

**Foundation Concept**

Preparing a service for a known period of elevated demand has two largely independent prerequisites: confirming the underlying infrastructure and quotas can absorb the expected load, and ensuring the team has the observability to detect and respond to problems that do occur. Within observability itself, implementation quality matters — percentile-based metrics over averages, and targeted alerts over blanket ones, are what make monitoring actually useful during an incident rather than just noisy or misleading.

**Real-World Connection**

An online retailer preparing for a major holiday sale reviews its expected traffic increase, requests the necessary quota increases for compute, networking, and API calls well ahead of the event, and separately tunes its Cloud Monitoring dashboards to alert on signals like p99 latency and error rate crossing meaningful thresholds — rather than paging engineers for every minor, self-resolving blip. When a backend dependency does slow down during the sale, the team is alerted promptly on a signal that actually reflects degraded user experience, and they already have the quota headroom to scale additional capacity in response.

**Memory Hook**

Preparing for a traffic spike needs two things: enough capacity (review and raise quotas) and good visibility (meaningful metrics and targeted alerts) — not new infrastructure tooling, not averaged latency, and not alerts on every failure.

**30-Second Exam Takeaway**

When a scenario asks how to prepare a service for a known high-traffic event, look for one action that secures adequate capacity/quota headroom and one that ensures well-targeted observability — and be suspicious of any monitoring-sounding option that uses averages instead of percentiles, or alerts on everything instead of what matters.

**Official References**

[**Google Cloud — Prepare for a peak capacity event:**](https://docs.cloud.google.com/support/docs/checklists/plan-peak-capacity-event) Supports: capacity planning and quota review as a core part of preparing for a known high-traffic event

[**Google SRE Book — Chapter 6: Monitoring Distributed Systems:**](https://sre.google/sre-book/monitoring-distributed-systems/) Supports: the four golden signals framework, and latency being tracked as a percentile-based distribution rather than an average, underpinning why targeted, meaningful alerting beats averaged metrics and blanket alerting

---

## Question 20

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your Cloud Run application currently writes its logs as plain unstructured text strings, which land in Cloud Logging. You want those logs to become JSON-based structured logs instead. What should you do?

- [x] A. Update the application code to use the Cloud Logging client library and emit log entries whose payload is structured JSON.
- [ ] B. Add a Fluent Bit sidecar container to the service and configure it with a JSON parser.
- [ ] C. Bundle a logging agent into the Cloud Run container image and have the agent forward logs to Cloud Logging.
- [ ] D. Configure the logging agent to convert the existing text payload of each log entry into a JSON payload.

### Explanation

**Correct Answer**

**A. Update the application code to use the Cloud Logging client library and emit log entries whose payload is structured JSON.**

**Exam Reasoning Explanation**

Cloud Run already automatically captures anything written to stdout/stderr and forwards it to Cloud Logging, with no agent to install or configure by the customer. Whether a line lands in textPayload or jsonPayload is determined entirely by whether that line is a single, valid, serialized JSON object at the moment it’s written — Cloud Logging doesn’t retroactively convert plain text into JSON. That means the only way to get structured logs is to change what the application itself emits, which is exactly what using the Cloud Logging client library to construct and write JSON-formatted entries accomplishes. Options B, C, and D each propose some kind of agent transforming the logs after the fact, which doesn’t match how Cloud Run’s logging pipeline works and doesn’t solve the stated problem.

**Key Exam Clues**

  * “writes unstructured logs as text strings” — identifies the root cause as the application’s own output format, not a transport or forwarding problem

  * “convert the unstructured logs to JSON-based structured logs” — the desired end state is specifically the jsonPayload field, which Cloud Logging only populates from a genuinely JSON-formatted log line

  * “Cloud Run application” — a serverless, fully managed environment where the customer doesn’t install or manage logging agents the way they might on a VM or in a self-managed Kubernetes cluster

  * Three of the four options revolve around an “agent,” which should prompt checking whether Cloud Run’s logging architecture even has a customer-configurable agent step to intervene in

**Why This Is Correct**

Cloud Logging treats a log line as structured only when that line is a single, valid serialized JSON object, placing it in jsonPayload instead of textPayload. The Cloud Logging client library gives the application a direct way to construct such JSON-formatted entries — including fields like severity and message — and write them to stdout, stderr, or directly via the API, which Cloud Run automatically picks up. Because the transformation has to happen at the point the log is produced, modifying the application to emit structured entries through the client library is the only option that changes the log format at its source.

**Why the Other Options Are Not the Best Fit**

**Option B — Technically Possible but Not Best:** A Fluent Bit sidecar with a JSON parser could theoretically reformat log output, but it adds an extra container, configuration surface, and point of failure to parse and restructure text that the application could simply emit as JSON in the first place — solving the same problem with substantially more complexity than using the Cloud Logging client library directly.

**Option C — Incorrect:** Cloud Run is fully managed and serverless; log capture from stdout, stderr, and the Cloud Logging client libraries is already built in and automatic. There is no customer-installable logging agent in the Cloud Run execution environment, and even if there were, forwarding unstructured text unchanged would not make it structured.

**Option D — Incorrect:** There is no agent-level feature in Cloud Logging that retroactively rewrites an existing text payload into a JSON payload. Whether a log entry is structured is determined at write time by whether the line was valid JSON, not by any downstream agent configuration applied after ingestion.

**Exam Trap**

The trap is assuming that because “agents” commonly appear in other Google Cloud logging contexts — such as the Ops Agent on Compute Engine or Fluent Bit in GKE — a similar agent-based approach must apply to Cloud Run too. Cloud Run’s fully managed nature means there’s no agent for the customer to install or configure in the execution environment; stdout/stderr capture is automatic, and the only lever available is what the application itself writes, which is exactly what the client-library option controls.

**Foundation Concept**

In Cloud Logging, a log entry is structured specifically when its payload is a JSON object stored in the jsonPayload field, as opposed to a plain string stored in textPayload. This distinction is determined when the log line is written, not through any later transformation step, which is why structured logging guidance centers on writing a single line of serialized JSON to stdout/stderr or using a Cloud Logging client library, rather than on any agent-based post-processing.

**Real-World Connection**

A team running a Cloud Run service switches from ad hoc print statements to the Cloud Logging client library, emitting each log entry as a JSON object with fields like severity, message, and a request trace identifier. Doing so lets them filter and query logs in the Logs Explorer by those structured fields — for example, isolating all ERROR-severity entries for a specific request — something that was impossible when every log entry was just an opaque block of text.

**Memory Hook**

Structured logs come from what the app writes, not from an agent — use the Cloud Logging client library to emit JSON, since Cloud Run has no customer-installable agent to convert text after the fact.

**30-Second Exam Takeaway**

When a Cloud Run (or other serverless) application needs structured JSON logs instead of plain text, look for the option that changes what the application itself writes — typically via the Cloud Logging client library — and be skeptical of any answer that proposes installing or configuring an agent, since Cloud Run’s managed logging pipeline doesn’t work that way.

**Official References**

[**Google Cloud — Cloud Run logging:**](https://cloud.google.com/run/docs/logging) Supports: automatic stdout/stderr log capture, the textPayload-versus-jsonPayload distinction, and writing structured logs via the Cloud Logging client library

[**Google Cloud — Structured logging:**](https://docs.cloud.google.com/logging/docs/structured-logging) Supports: the jsonPayload mechanism and the client-library/API approach as the documented way to write structured logs, as opposed to any agent-based conversion

---

## Question 21

*Domain 2: Building and Implementing CI/CD Pipelines*

You are choosing a deployment approach for your applications on Google Cloud, and as part of that planning you want to gather performance metrics for new application versions using live traffic. The new versions need to be tested against the full production load before they are actually launched. What should you do?

- [ ] A. Combine A/B testing with a blue/green deployment.
- [ ] B. Combine canary testing with continuous deployment.
- [ ] C. Combine canary testing with a rolling updates deployment.
- [x] D. Combine shadow testing with continuous deployment.

### Explanation

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

---

## Question 22

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

You are designing a new Google Cloud organization on behalf of a client who is concerned about the risks posed by long-lived credentials in Google Cloud. You need a solution that completely removes the risk associated with JSON service account keys while keeping ongoing operational overhead to a minimum. What should you do?

- [x] A. Enforce the constraints/iam.disableServiceAccountKeyCreation organization policy constraint at the organization level.
- [ ] B. Build custom versions of the relevant predefined roles that strip out every iam.serviceAccountKeys.* permission.
- [ ] C. Enforce the constraints/iam.disableServiceAccountKeyUpload organization policy constraint at the organization level.
- [ ] D. Grant the roles/iam.serviceAccountKeyAdmin role solely to organization administrators.

### Explanation

**Correct Answer**

**A. Enforce the constraints/iam.disableServiceAccountKeyCreation organization policy constraint at the organization level.**

**Exam Reasoning Explanation**

The solution must completely eliminate the risk of JSON service account key creation — not merely reduce exposure or restrict who can do it — while adding minimal ongoing operational burden. Option B requires building and maintaining custom IAM roles org-wide, which is high-overhead and incomplete, since any principal retaining a broader role could still create keys. Option D restricts who can create keys to administrators, but those administrators can still create JSON keys — the risk is concentrated, not eliminated, and gatekeeping adds process overhead. Option C enforces a constraint that blocks a different, narrower action — uploading an externally generated public key — which does nothing to stop the standard JSON key creation flow the client is worried about. Option A enforces the constraint purpose-built to block creation of new user-managed service account keys org-wide, in a single, centrally enforced setting with no per-role or per-principal maintenance, fully satisfying both requirements.

**Key Exam Clues**

  * “completely eliminate the risks” — a hard constraint ruling out anything that merely restricts or reduces who can create keys (D) or requires comprehensive, error-prone permission auditing to guarantee coverage (B)

  * “JSON service account keys” specifically — points to the standard key-creation flow, as opposed to uploading externally generated key material, which is the distinction between the two similarly named constraints

  * “minimizing operational overhead” — a hard constraint favoring a single, centrally enforced organization policy over custom IAM roles or administrative gatekeeping that require ongoing maintenance

  * “designing a new Google Cloud organization” — frames this as foundational setup, where an org-wide policy constraint is naturally applied once at the top of the hierarchy

**Why This Is Correct**

The constraints/iam.disableServiceAccountKeyCreation organization policy constraint, enforced at the organization level, prevents any principal anywhere in the organization from creating new user-managed (including JSON) service account keys, regardless of what IAM roles they otherwise hold. Because this is a single policy enforced centrally by the Organization Policy Service, it requires no per-role redesign, no list of approved administrators to manage, and no ongoing auditing to confirm coverage — it applies uniformly and automatically, satisfying “completely eliminate” and “minimizing operational overhead” together.

**Why the Other Options Are Not the Best Fit**

**Option B — Technically Possible but Not Best:** Custom roles excluding iam.serviceAccountKeys.* permissions could reduce key creation if applied everywhere correctly, but require identifying and modifying every predefined role in use, maintaining those custom roles going forward, and ensuring no principal is ever granted a broader role that reintroduces the permission — a much higher, more error-prone burden than a single org policy, with no guarantee of complete coverage.

**Option C — Violates Requirement:** constraints/iam.disableServiceAccountKeyUpload blocks uploading an externally generated public key to a service account, not the creation of new JSON keys through Google’s standard key-creation flow. Enforcing it alone leaves the primary risk the client is worried about completely unaddressed.

**Option D — Violates Requirement:** Restricting roles/iam.serviceAccountKeyAdmin to organization administrators narrows who can create keys but doesn’t eliminate the ability to create them — those administrators can still generate JSON keys. It also adds overhead, since anyone else who legitimately needs a key must now go through the restricted admin group.

**Exam Trap**

The trap is confusing constraints/iam.disableServiceAccountKeyUpload with constraints/iam.disableServiceAccountKeyCreation, since their names are nearly identical and both relate to service account keys. Upload blocks associating an externally generated key with a service account; creation blocks generating a new key through Google’s own key-creation process — the action this scenario actually describes. A second trap is assuming that restricting a role (D) or redesigning permissions (B) is equivalent to eliminating a capability outright, when only an enforced organization policy constraint guarantees that outcome regardless of what roles anyone holds.

**Foundation Concept**

Organization policy constraints operate above and independently of IAM role grants: even a principal with a broad IAM role like Owner cannot perform an action that an enforced organization policy constraint blocks. This makes constraints the appropriate tool whenever a requirement is to eliminate a capability organization-wide with certainty, as opposed to IAM role design, which only shapes what a specific principal can do and depends on every relevant role being correctly and consistently configured to achieve the same guarantee.

**Real-World Connection**

A platform team migrating their organization toward keyless authentication, such as Workload Identity Federation, enforces constraints/iam.disableServiceAccountKeyCreation at the organization level as a first step, immediately and permanently closing off new JSON key creation across every current and future project without redesigning a single IAM role or manually policing who holds which permissions — freeing the team to focus on migrating existing workloads off any keys created before the policy was enforced.

**Memory Hook**

JSON key creation risk, zero overhead, complete elimination → constraints/iam.disableServiceAccountKeyCreation at the org level; “Upload” blocks a different action, and custom roles or admin-only grants don’t eliminate the capability outright.

**30-Second Exam Takeaway**

When a scenario wants service account key creation eliminated organization-wide with minimal ongoing effort, reach for the organization policy constraint built for exactly that (disableServiceAccountKeyCreation) rather than IAM role redesign or role-grant restrictions, and don’t confuse it with the similarly named upload-blocking constraint, which addresses a different action entirely.

**Official References**

[**Google Cloud — Service account credentials:**](https://cloud.google.com/iam/docs/service-account-creds) Supports: the distinction between disableServiceAccountKeyCreation (blocks creating user-managed keys) and disableServiceAccountKeyUpload (blocks uploading external public keys)

[**Google Cloud — Restrict IAM service account usage:**](https://docs.cloud.google.com/organization-policy/restrict-service-accounts) Supports: the constraint’s function of disabling creation of new external service account keys at the organization level

---

## Question 23

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your company runs its applications on Google Kubernetes Engine (GKE), and several of them rely on ephemeral volumes. You’ve noticed that some applications have become unstable because worker nodes are reporting a DiskPressure condition. You need to identify which Pods are responsible, but you don’t have execute access into either the workloads or the nodes. What should you do?

- [ ] A. Inspect the node/ephemeral_storage/used_bytes metric in Metrics Explorer.
- [x] B. Inspect the container/ephemeral_storage/used_bytes metric in Metrics Explorer.
- [ ] C. Find every Pod that uses an emptyDir volume, and run the df -h command to measure that volume’s disk usage.
- [ ] D. Find every Pod that uses an emptyDir volume, and run the df -sh * command to measure that volume’s disk usage.

### Explanation

**Correct Answer**

**B. Inspect the container/ephemeral_storage/used_bytes metric in Metrics Explorer.**

**Exam Reasoning Explanation**

Two constraints must both be satisfied: identifying specifically which Pods are responsible for the DiskPressure condition, and doing so without execute access to workloads or nodes. Options C and D both require running a shell command inside or against a Pod or node, which needs exec or SSH access — directly violating the stated constraint regardless of the exact df syntax used. That leaves the two Metrics Explorer options, which differ only in which metric they check. The node-level metric (A) reports aggregate ephemeral storage usage for an entire node, confirming a node is under pressure but not attributing that usage to any particular Pod. The container-level metric (B) reports ephemeral storage usage per container, which can be filtered and grouped by Pod and namespace in Metrics Explorer, directly revealing which specific Pods are the likely cause.

**Key Exam Clues**

  * “identify which Pods are causing the issue” — the central requirement, which only a per-container/per-Pod metric can satisfy; a node-level metric cannot attribute usage to an individual workload

  * “you do not have execute access to workloads and nodes” — a hard constraint eliminating any option that requires running a command inside a Pod or on a node

  * “ephemeral volumes” / “DiskPressure” — identifies ephemeral storage specifically as the resource under pressure, pointing to the ephemeral_storage metric family rather than memory or CPU metrics

  * “using Metrics Explorer” appears in two of the four options — signals that the real decision point is which metric to select, not which tool to use

**Why This Is Correct**

The container/ephemeral_storage/used_bytes metric reports local ephemeral storage usage at the individual container level, and because GKE’s Cloud Monitoring metrics carry labels such as pod_name and namespace_name, this metric can be filtered or grouped in Metrics Explorer to show exactly which Pods are consuming the most ephemeral storage. This gives a direct, per-Pod view of resource consumption entirely through the monitoring console, with no need to exec into a container or SSH into a node — satisfying both the identification requirement and the access constraint.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** The node/ephemeral_storage/used_bytes metric confirms that a given node’s overall ephemeral storage usage is high, which is useful for seeing that a node is under pressure, but it’s an aggregate across every container on the node and cannot attribute that usage to any specific Pod — it answers “which nodes,” not “which Pods.”

**Option C — Violates Requirement:** Running df -h against a Pod’s emptyDir volume requires exec access into the Pod, or SSH access to the node hosting it, which the scenario explicitly states is unavailable. This approach is also far more labor-intensive, requiring each Pod to be checked individually rather than viewing consumption across the fleet at once.

**Option D — Violates Requirement:** This has the same fundamental problem as Option C — df -sh * still requires executing a command inside a Pod or on a node. Changing the specific df flags doesn’t change the fact that this approach is blocked by the stated access constraint.

**Exam Trap**

The trap is reflexively reaching for a hands-on shell command (df) to check disk usage, since that’s the natural instinct for a storage question, without registering that the scenario explicitly removes execute access as an option. A second, more subtle trap is picking the node-level metric (A) because it’s the one most directly tied to the DiskPressure condition’s name, without noticing the question asks specifically which Pods are responsible — something only a container-level metric can answer.

**Foundation Concept**

GKE automatically exports both node-level and container-level resource metrics to Cloud Monitoring, and the two serve different diagnostic purposes: node-level metrics tell you that a resource constraint exists on a given node, while container-level metrics carry Pod and namespace labels that let you attribute that constraint to specific workloads. When the question is “which workload is responsible,” the container-level metric is the one that can actually answer it — all without needing shell access to anything.

**Real-World Connection**

A platform team notices DiskPressure alerts firing on several GKE nodes and, without needing to exec into any Pod, opens Metrics Explorer, selects the container/ephemeral_storage/used_bytes metric, and groups the results by pod_name to immediately see a handful of Pods consuming far more ephemeral storage than the rest — typically ones writing large temporary files to an emptyDir volume without limits. They can then set ephemeral storage requests and limits on those specific workloads to prevent them from starving other Pods on the same node.

**Memory Hook**

“Which Pods?” needs a container-level metric, not a node-level one — and “no exec access” rules out any df command; container/ephemeral_storage/used_bytes in Metrics Explorer answers both.

**30-Second Exam Takeaway**

When a GKE troubleshooting question asks which specific Pods are responsible for a resource-pressure condition and rules out shell/exec access, look for the container-level Cloud Monitoring metric (filterable by Pod) rather than the node-level aggregate or any command that requires running something inside a Pod or node.

**Official References**

[**Google Cloud — Introduction to monitoring your GKE environment**](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-monitoring)**:** Supports: the definitions and troubleshooting significance of container/ephemeral_storage/used_bytes (per-container, Pod-attributable) versus node/ephemeral_storage/used_bytes (node-level aggregate), and the DiskPressure node condition

---

## Question 24

*Domain 2: Building and Implementing CI/CD Pipelines*

You have a Cloud Build job configured to deploy Terraform code whenever a Git branch is updated. During testing, the job fails, and the build logs show the following error:

Initializing the backend...

Error: Failed to get existing workspaces: querying Cloud Storage failed: googleapi: Error 403

You need to resolve this by following Google-recommended practices. What should you do?

- [ ] A. Update the Terraform configuration to use local state instead of a remote backend.
- [ ] B. Create a Cloud Storage bucket matching the name referenced in the Terraform configuration.
- [ ] C. Grant the Cloud Build service account the roles/owner Identity and Access Management (IAM) role on the project.
- [x] D. Grant the Cloud Build service account the roles/storage.objectAdmin Identity and Access Management (IAM) role, scoped to just the state file’s storage bucket.

### Explanation

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

---

## Question 25

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You are setting up Cloud Logging for a new application running on a Compute Engine instance that has a public IP address and a user-managed service account attached. You’ve confirmed the required logging agents are running on the instance, but no log entries from it are showing up in Cloud Logging. You want to fix this following Google-recommended practices. What should you do?

- [ ] A. Export a key for the service account, and configure the agents to authenticate using that key.
- [ ] B. Switch the instance to use the default Compute Engine service account instead.
- [x] C. Grant the service account the Logs Writer IAM role.
- [ ] D. Turn on Private Google Access for the subnet the instance resides in.

### Explanation

**Correct Answer**

**C. Grant the service account the Logs Writer IAM role.**

**Exam Reasoning Explanation**

The fix must restore the already-running agent’s ability to write log entries to Cloud Logging, and it must align with Google-recommended practice, which rules out anything introducing long-lived credentials or weakening the security posture. Option D addresses a networking path relevant only to instances without a public IP that need internal routing to reach Google APIs; this instance already has a public IP and a route to those APIs, so it isn’t the blocker. Option A would technically let the agent authenticate, but exporting and distributing a key is explicitly a secondary, less-recommended method compared to using the attached service account’s identity directly. Option B might fix the symptom if the default service account happens to carry broader permissions, but replacing a purpose-built custom service account with the default one is a step backward from least privilege and doesn’t target what’s actually missing. Option C grants exactly the permission the agent needs — the Logs Writer role — resolving the issue at its root.

**Key Exam Clues**

  * “you confirmed that the necessary agents are running” — rules out an agent installation or configuration problem, narrowing the cause to authorization

  * “user-managed service account” — a custom service account doesn’t automatically carry the Logs Writer role the way some default-account scenarios do, making IAM the first thing to check

  * “public IP address” — rules out Private Google Access as relevant, since the instance already has a direct path to Google APIs

  * “following Google-recommended practices” — a hard constraint eliminating the service-account-key option, which Google positions as a fallback rather than the preferred approach when an attached service account is available

**Why This Is Correct**

Both the Ops Agent and the legacy Logging agent authenticate using application default credentials tied to the VM’s attached service account, and that service account needs the Logs Writer (roles/logging.logWriter) IAM role to actually write entries to Cloud Logging. Newly created Compute Engine VMs often have sufficient access scopes and a service account already holding this role, but a user-managed service account isn’t guaranteed to have it granted automatically. Since the agent is confirmed running and simply failing to deliver log entries, granting this specific role to the attached service account directly closes the authorization gap, which is the documented, Google-recommended way to authorize the agent via an attached service account.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** Service account keys are a supported authentication method for the agent, but Google documents attaching a service account directly as the preferred path and keys as the fallback for cases where an attached service account isn’t an option — introducing a key here adds credential-management overhead the scenario’s existing setup doesn’t require.

**Option B — Technically Possible but Not Best:** Switching to the default Compute Engine service account could resolve the symptom if that account carries the necessary role, but it abandons a purpose-built custom service account for a broader, less-scoped identity, running counter to least-privilege practice and sidestepping the actual gap — a missing role grant on the account already in use.

**Option D — Different Use Case:** Private Google Access provides a path to Google APIs for instances without a public IP by routing traffic internally. This instance already has a public IP and can already reach Google’s APIs, so enabling it addresses nothing relevant to a failure that’s about authorization, not connectivity.

**Exam Trap**

The trap is reaching for a networking fix (Private Google Access) simply because the instance has a public IP and logging can feel like a connectivity concern, without checking whether connectivity was ever actually the problem. A second trap is treating a key-based or default-service-account fix as equally valid because it would also make the symptom disappear, without weighing it against the explicit “Google-recommended practices” requirement, which favors a scoped IAM role grant on the existing attached service account over credential export or a broader, less-scoped identity.

**Foundation Concept**

Any identity writing log entries to Cloud Logging — a default service account, a custom service account, or an application client library — needs the Logs Writer IAM role on the relevant resource. This requirement is independent of network reachability or whether agents are installed and running: an agent that can reach the Cloud Logging API endpoint will still fail to write entries if the identity it authenticates as lacks this specific role, which is why confirming the agent is running doesn’t rule out an authorization problem.

**Real-World Connection**

A platform team provisions Compute Engine instances with purpose-built, minimally scoped service accounts rather than the broad default service account, and as part of their standard instance template explicitly grants each custom service account the Logs Writer role so every instance’s logs reliably reach Cloud Logging. When a new application’s logs don’t show up despite the agent running correctly, checking IAM role assignments on the attached service account is the first and most direct place to look, rather than suspecting agent configuration or network routing.

**Memory Hook**

Agent running, public IP present, no logs appearing → check the service account’s IAM roles first; grant Logs Writer rather than exporting keys, switching to the default service account, or touching network access.

**30-Second Exam Takeaway**

When a Compute Engine instance’s logging agent is confirmed running but logs never reach Cloud Logging, suspect a missing Logs Writer IAM role on the attached service account before looking at network configuration or reaching for a service account key — especially when the service account is user-managed, since it won’t carry that role automatically.

**Official References**

[Google Cloud — Authorize the Ops Agent: ](https://docs.cloud.google.com/logging/docs/agent/ops-agent/authorization)Supports: authorizing the agent via an attached service account granted the Logs Writer role as the primary method, with service account keys documented as a secondary alternative

---

## Question 26

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

You are designing a platform with three environments — development, quality assurance (QA), and production. Each environment is provisioned with Terraform and includes its own Google Kubernetes Engine (GKE) cluster where application teams deploy their workloads. Anthos Config Management, using templated Kustomize manifests, deploys infrastructure-level resources into each GKE cluster. Every user — infrastructure operators and application owners alike — works through GitOps. How should you structure your source control repositories for both infrastructure as code (IaC) and application source code?

- [x] A. Cloud infrastructure (Terraform) repository is shared, with different directories representing different environments. GKE infrastructure (Anthos Config Management Kustomize manifests) repository is shared, with different overlay directories representing different environments. Application (app source code) repositories are separate per application, with different branches representing different features.
- [ ] B. Cloud infrastructure (Terraform) repository is shared, with different directories representing different environments. GKE infrastructure (Anthos Config Management Kustomize manifests) repositories are separate, with different branches representing different environments. Application (app source code) repositories are separate per application, with different branches representing different features.
- [ ] C. Cloud infrastructure (Terraform) repository is shared, with different branches representing different environments. GKE infrastructure (Anthos Config Management Kustomize manifests) repository is shared, with different overlay directories representing different environments. Application (app source code) repository is shared, with different directories representing different features.
- [ ] D. Cloud infrastructure (Terraform) repositories are separate per environment, with different branches also representing different environments within each. GKE infrastructure (Anthos Config Management Kustomize manifests) repositories are separate, with different overlay directories representing different environments. Application (app source code) repositories are separate per application, with different branches representing different features.

### Explanation

**Correct Answer**

**A. Cloud infrastructure (Terraform) repository is shared, with different directories representing different environments. GKE infrastructure (Anthos Config Management Kustomize manifests) repository is shared, with different overlay directories representing different environments. Application (app source code) repositories are separate per application, with different branches representing different features.**

**Exam Reasoning Explanation**

The structure must support GitOps for every user, keep each tooling layer consistent with how that tool is actually designed to be used, and avoid double-encoding the same dimension in two places. Option D fragments both Terraform and ACM/Kustomize into separate repositories per environment while also layering branches or overlay directories for environment inside each already-environment-specific repository — a redundant, internally inconsistent double-encoding that undermines a single source of truth. Option C combines a legitimate branch-per-environment Terraform pattern with a single shared application-source repository using directories for features, which collapses every application team’s code into one repository and treats “feature” as a static folder. Option B structures ACM/Kustomize with separate repositories and branches per environment, fighting against Kustomize’s own base-and-overlay design, which already expresses environment differences through overlay directories in one repository. Option A keeps each infrastructure layer in a single shared repository with environments as directories/overlays — matching how Kustomize is built and a well-documented Terraform pattern — while giving each application team its own repository with standard feature branches.

**Key Exam Clues**

  * “Anthos Config Management... templated to deploy infrastructure level resources” — points directly at Kustomize’s base-and-overlay design, where overlay directories, not branches or separate repos, are the standard way to express environment differences

  * “application teams can deploy their applications” (plural teams) — signals application source code belongs to distinct teams, favoring separate per-team repositories over one shared application repository

  * “All users... will use GitOps” — reinforces that each layer needs a single source of truth that changes promote through, which overlay directories and environment branches both support, but double-fragmenting a layer does not

  * Three named environments (dev, QA, production) — frames “environment” as the dimension each infrastructure layer’s structure needs to cleanly represent

**Why This Is Correct**

Terraform and Anthos Config Management/Kustomize are both infrastructure layers best kept in shared repositories with environments expressed as directories (Terraform’s root configurations) or overlays (Kustomize’s purpose-built base-plus-overlay pattern), keeping one source of truth per layer and making promotion between environments a simple, reviewable diff between directories rather than a cross-repository or cross-branch operation. Application source code belongs to individual teams and follows ordinary software development practice, where features are developed on branches and merged back into a main line — not expressed as folders, and not mixed with other teams’ unrelated code in one repository. This combination matches both infrastructure-as-code structuring guidance and standard application development workflow at once.

**Why the Other Options Are Not the Best Fit**

**Option B — Technically Possible but Not Best:** Separate repositories with environment branches for ACM/Kustomize works against Kustomize’s own design, which already differentiates environments through overlay directories on a shared base within one repository; splitting both repository and branch by environment adds fragmentation with no corresponding benefit.

**Option C — Technically Possible but Not Best:** Branch-per-environment for the Terraform root configuration is a legitimate, documented pattern, but pairing it with a single shared application source repository where directories represent features breaks down once there are multiple distinct application teams — their codebases, release cadences, and ownership boundaries don’t fit naturally into folders of one shared repository.

**Option D — Violates Requirement:** Separating both Terraform and ACM/Kustomize repositories by environment and then also using branches or overlay directories for environment within each already-environment-specific repository encodes the same distinction twice, which is redundant and undermines the single-source-of-truth structure GitOps depends on.

**Exam Trap**

The trap is assuming “more separation” is always safer or more organized — splitting repositories by environment feels thorough, but when a tool like Kustomize is explicitly designed around one shared base with environment-specific overlays in a single repository, adding repository- or branch-level environment separation on top just duplicates what overlays already do. A second trap is treating “shared repository” as always correct without checking ownership — infrastructure benefits from a shared repository with directory-based environment separation, but application source code belongs to individual teams and shouldn’t be collapsed into one shared repository just because the infrastructure layers are.

**Foundation Concept**

GitOps repository structure should match the actual design and ownership model of what’s being managed: Kustomize’s base-and-overlay pattern is built for a single repository with per-environment overlay directories, Terraform root configurations are commonly structured with environment-specific directories within a shared repository (environment branches are a documented alternative for directly-deployed root configs), and application source code should follow standard team-based ownership with feature branches rather than being folded into shared infrastructure repositories.

**Real-World Connection**

A platform team sets up one Terraform repository with dev, qa, and prod directories for foundational cloud infrastructure, and one Anthos Config Management repository with a base configuration and dev/qa/prod overlay directories for cluster-level resources, so promoting a change to production is a reviewable pull request that carries a directory’s state forward. Each application team keeps its own source repository and follows an ordinary feature-branch workflow, merging into main and letting the CI/CD pipeline — not a repository or branch per environment — handle deploying the resulting build to each environment’s GKE cluster.

**Memory Hook**

Infrastructure layers (Terraform, Kustomize/ACM): one shared repo, directories/overlays for environments. Application code: one repo per app, branches for features — not the reverse.

**30-Second Exam Takeaway**

When a GitOps repository-structure question involves both infrastructure (Terraform, Kustomize) and application code, expect infrastructure to live in shared repositories with directory- or overlay-based environment separation, and application code to live in per-team repositories using ordinary feature branches — watch for options that double-encode environment separation or collapse multiple application teams into one shared repository.

**Official References**

[Google Cloud — Best practices for version control (Terraform): ](https://docs.cloud.google.com/docs/terraform/best-practices/version-control)Supports: directory-based component and environment organization, the default feature-branch workflow for application-style repositories, and environment branches as a documented alternative pattern for directly-deployed root configurations

[**Google Cloud — Manage infrastructure as code with Terraform, Cloud Build, and GitOps:**](https://docs.cloud.google.com/docs/terraform/resource-management/managing-infrastructure-as-code) Supports: the environments/ directory pattern (dev, prod subfolders) for expressing environment separation within a single shared Terraform repository

---

## Question 27

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

Your company runs applications on Google Kubernetes Engine (GKE), deployed using a GitOps methodology. Application developers frequently need to create cloud resources to support their applications, and you want to give them a way to manage infrastructure as code that follows Google-recommended practices. The solution also needs to reconcile the infrastructure periodically so configuration drift doesn’t go uncorrected. What should you do?

- [x] A. Deploy and configure Config Connector inside the GKE cluster.
- [ ] B. Set up Cloud Build with a Terraform builder step that runs terraform plan and terraform apply.
- [ ] C. Create a standalone Pod running a Terraform container image that executes terraform plan and terraform apply.
- [ ] D. Create a Kubernetes Job running a Terraform container image that executes terraform plan and terraform apply.

### Explanation

**Correct Answer**

**A. Deploy and configure Config Connector inside the GKE cluster.**

**Exam Reasoning Explanation**

Two constraints must both be satisfied: developers manage infrastructure as code following Google-recommended practices, and the infrastructure continuously reconciles on its own to correct drift, not just on a one-time or triggered basis. A Pod (C) runs its process once, with no built-in mechanism to re-run itself or detect drift afterward. A Job (D) is Kubernetes’ primitive for a single run-to-completion task and doesn’t repeat by design. Cloud Build with Terraform (B) runs on triggers, typically a Git push, producing a single apply per trigger rather than an ongoing reconciliation process; achieving periodicity would require additional scheduling the option doesn’t describe. Config Connector (A) is architected as a Kubernetes controller, and controllers are fundamentally built around a continuous reconciliation loop — Config Connector re-evaluates each managed resource’s actual state against its desired state on every update and on a recurring interval, automatically correcting drift as a built-in property of the tool itself.

**Key Exam Clues**

  * “reconciles periodically to avoid configuration drift” — the decisive requirement, ruling out anything that only runs once or only runs in response to a Git push

  * “Create a Pod resource” / “Create a Job resource” — both name Kubernetes primitives that run to completion rather than continuously operate, signaling they lack built-in repetition

  * “Application developers frequently create cloud resources” — points toward a Kubernetes-native, CRD-based tool fitting naturally into a GitOps workflow developers already use

  * “following a GitOps methodology” already in place — favors a tool whose resources are ordinary Kubernetes manifests that slot into the existing pipeline, rather than a separate build-triggered or batch mechanism

**Why This Is Correct**

Config Connector is a Kubernetes controller, built around a reconciliation loop by design: it continuously compares each managed resource’s declared state against the actual Google Cloud resource state, re-checking on every update and again on a recurring interval, and automatically correcting any detected drift. Because Config Connector resources are ordinary Kubernetes YAML, they fit directly into the GitOps pipeline already used for applications, letting developers manage infrastructure the same way they manage workloads, while the controller itself — not a scheduled job or pipeline trigger — guarantees the periodic reconciliation the scenario requires.

**Why the Other Options Are Not the Best Fit**

**Option B — Technically Possible but Not Best:** A Cloud Build Terraform pipeline is legitimate for managing infrastructure as code, but it executes on triggers, most commonly a Git push, producing a single terraform apply per trigger rather than an ongoing reconciliation process. Periodic execution would require separate scheduling, and even then each run is a discrete apply, not a continuously operating controller.

**Option C — Violates Requirement:** A standalone Pod runs its container’s process once, or keeps a single process running without re-executing it; it has no native mechanism to periodically re-run terraform plan and apply or detect drift afterward, so it fails “reconciles periodically” entirely.

**Option D — Violates Requirement:** A Kubernetes Job is specifically designed to run to completion exactly once and doesn’t repeat on a schedule by itself. At best it produces a single apply, with no periodic reconciliation unless a different resource type (a CronJob) were used — and even that wouldn’t provide the continuous drift detection a controller offers natively.

**Exam Trap**

The trap is treating “run Terraform somewhere in Kubernetes” (Pod or Job) as equivalent to a reconciling controller, when neither primitive is designed to repeat or recheck state on its own — a Job in particular sounds like it might be scheduled or recurring, but Kubernetes Jobs are explicitly single-run resources. A second trap is assuming a CI/CD pipeline inherently provides ongoing reconciliation because it’s automated, when its automation is trigger-based rather than a continuously running state-comparison loop.

**Foundation Concept**

A reconciliation loop — continuously comparing a system’s actual state to its declared desired state and correcting differences — is the foundational pattern behind every Kubernetes controller, and it’s what distinguishes an operator like Config Connector from a one-shot execution mechanism like a Pod, a Job, or a triggered CI/CD pipeline step. Tools built on this pattern provide drift correction as an inherent property of simply running, rather than something separately scheduled or re-triggered.

**Real-World Connection**

A platform team lets application developers request Cloud SQL instances, Pub/Sub topics, and storage buckets by committing Config Connector YAML manifests through the same GitOps pipeline and pull-request review process they already use for application deployments. If someone later changes a resource’s configuration directly in the Google Cloud console, Config Connector’s next reconciliation pass detects the mismatch against the manifest in Git and reverts it automatically, keeping Git as the enforced source of truth without the platform team building or maintaining any separate drift-detection mechanism.

**Memory Hook**

“Reconciles periodically” is a controller behavior, not a Pod/Job/pipeline behavior — Config Connector’s built-in reconciliation loop continuously corrects drift; Pods and Jobs run once, and Cloud Build runs on triggers.

**30-Second Exam Takeaway**

When a requirement specifically calls for infrastructure as code to reconcile periodically and self-correct drift, look for a Kubernetes-native controller like Config Connector rather than a one-time execution resource (Pod, Job) or a trigger-based CI/CD pipeline step, since only a controller’s reconciliation loop provides that ongoing behavior natively.

**Official References**

[**Google Cloud — Config Connector reconciliation:**](https://cloud.google.com/config-connector/docs/concepts/reconciliation) Supports: the controller’s reconciliation-loop behavior, re-checking resource state on every update and on a recurring interval to automatically correct drift

---

## Question 28

*Domain 2: Building and Implementing CI/CD Pipelines*

You are deploying an application to Cloud Run that needs a password to start up. Your organization mandates that every password be rotated every 24 hours, and the application must always be working with the current password. You need to achieve this without any downtime. What should you do?

- [ ] A. Store the password in Secret Manager and expose it to the application as an environment variable.
- [x] B. Store the password in Secret Manager and mount it as a volume inside the application’s container.
- [ ] C. Have Cloud Build bake the password into the application container image at build time, and make sure Artifact Registry is locked down from public access.
- [ ] D. Hard-code the password directly in the application’s source code, and use Cloud Build to rebuild and redeploy the application whenever the password changes.

### Explanation

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

---

## Question 29

*Domain 5: Optimizing Performance and Cost*

As a Site Reliability Engineer, you support a Go application running in production on Google Kubernetes Engine (GKE). After a new release, you notice the application runs for roughly 15 minutes before restarting. You add Cloud Profiler to the application and observe that heap usage climbs steadily until each restart. What should you do?

- [ ] A. Raise the CPU limit configured on the application’s deployment.
- [ ] B. Add nodes with more memory to the cluster’s node pool.
- [x] C. Raise the memory limit configured on the application’s deployment.
- [ ] D. Instrument the application with Cloud Trace, and redeploy it.

### Explanation

**Correct Answer**

**C. Raise the memory limit configured on the application’s deployment.**

**Exam Reasoning Explanation**

The fix must address the memory-growth-then-restart pattern Cloud Profiler has already confirmed, and it must actually change what determines whether the container gets OOMKilled. Option A targets CPU, a different resource than the one Profiler identified as the problem, so it can’t affect a memory-driven restart. Option D adds Cloud Trace, a distributed-tracing tool for request latency and call paths, not a memory-diagnostic tool — Profiler has already supplied the relevant heap data, and Trace adds nothing toward solving a memory problem. Option B adds nodes with more physical memory, but a container’s OOMKill is governed by its own configured memory limit, not by how much memory is available on the node it runs on — more node capacity doesn’t change when that specific container gets killed. Option C directly raises the limit the container is actually measured against, giving the application room to run without hitting that ceiling — the mechanism that determines restart behavior.

**Key Exam Clues**

  * “heap usage grows constantly until the application restarts” — identifies this specifically as a memory-consumption problem, ruling out any fix targeting a different resource (CPU)

  * “runs for about 15 minutes and then restarts” — a classic OOMKill/crash-loop pattern, pointing toward resource limits as the mechanism to examine

  * “add Cloud Profiler... and now notice” — establishes profiling has already successfully diagnosed the issue, so the next step should act on that finding rather than add a different, unrelated diagnostic tool

  * “application deployment” appears in two of the four options — signals the decision is about which deployment-level resource setting to change, not whether to change one at all

**Why This Is Correct**

Cloud Profiler’s heap data has already identified memory, not CPU, as the resource driving the restarts, and in Kubernetes a container is terminated with an out-of-memory kill specifically when it exceeds the memory limit configured for that container in its deployment spec — regardless of how much memory the underlying node has available. Raising the memory limit directly changes that ceiling, giving the application room to operate without triggering a restart, targeting the exact mechanism responsible for the crash-loop behavior Profiler has already diagnosed.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement:** Profiler specifically showed heap (memory) usage climbing, not CPU usage. Raising the CPU limit changes a resource unrelated to the diagnosed problem and would have no effect on when the container gets OOMKilled.

**Option B — Technically Possible but Not Best:** A container’s OOM kill is triggered by its own configured memory limit, not the physical memory available on its node. Adding higher-memory nodes increases cluster capacity in general, but without also raising the container’s own memory limit, that same container is still killed at the same threshold regardless of how much memory the surrounding node has.

**Option D — Violates Requirement:** Cloud Trace captures distributed request latency and call-path data, not memory allocation information, so it contributes nothing new toward diagnosing or resolving a heap-growth problem Cloud Profiler has already clearly identified. Redeploying with an unrelated diagnostic tool also doesn’t address the restarts themselves.

**Exam Trap**

The trap is treating “add more resources somewhere in the cluster” (B) as equivalent to “fix the container’s resource limit” (C) — they sound similar but operate at different layers: node capacity versus the cgroup-enforced limit on the individual container, and only the latter determines whether that specific container gets OOMKilled. A second trap is reaching for a familiar observability tool (Cloud Trace) just because the scenario already involves observability, without checking whether that specific tool measures the resource in question; Trace addresses latency and request flow, not memory.

**Foundation Concept**

In Kubernetes, a container’s memory limit is enforced independently of the node’s total memory capacity: the container is killed once its own usage crosses its configured limit, even if the node still has free memory elsewhere, and adding memory to the node doesn’t raise that container-specific ceiling. This is why diagnosing a memory-related restart requires checking not just whether there’s “enough memory in the cluster,” but specifically whether the container’s own configured limit is appropriate for how much memory the application actually needs.

**Real-World Connection**

An SRE investigating a Go service that restarts every 15 minutes adds Cloud Profiler, confirms the heap grows continuously rather than plateauing, and raises the container’s memory limit in the deployment manifest so it has enough headroom to run without hitting its ceiling — buying stability immediately while a parallel workstream uses the same profiler data to track down and fix whatever code change in the new release caused the excess allocation in the first place.

**Memory Hook**

Profiler shows memory, not CPU, climbing until restart → raise the container’s own memory limit; more node memory or a tracing tool doesn’t touch the limit that’s actually triggering the kill.

**30-Second Exam Takeaway**

When profiling data shows a container’s heap climbing until an OOM-style restart, fix the resource limit Kubernetes actually enforces against that container — its configured memory limit — rather than adding node-level capacity (which doesn’t change the container’s own ceiling) or reaching for a tool, like Cloud Trace, that measures a different kind of problem entirely.

**Official References**

[Google Cloud — Put it all together: Example GKE troubleshooting scenario: ](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-example)Supports: the exact diagnostic pattern of climbing container memory usage leading to an OOMKilled restart, and raising the container’s configured memory limit as a documented response

---

## Question 30

*Domain 2: Building and Implementing CI/CD Pipelines*

You are building a CI/CD pipeline natively on Google Cloud, and you want every build deployed to a pre-production Google Kubernetes Engine (GKE) environment to be automatically load-tested before it can be promoted to production. Only builds that pass this test should ever reach production, and you want to follow Google-recommended practices for doing this with Binary Authorization. How should you configure the pipeline?

- [ ] A. Have the lead quality assurance engineer manually sign the attestation for each passing build, using their own personal private key.
- [ ] B. Have the pipeline sign the attestation for each passing build with a private key stored in Cloud Key Management Service (Cloud KMS), authenticating with a service account JSON key stored as a Kubernetes Secret.
- [x] C. Have the pipeline sign the attestation for each passing build with a private key stored in Cloud Key Management Service (Cloud KMS), authenticating through Workload Identity.
- [ ] D. Have the lead quality assurance engineer manually sign the attestation for each passing build, using a key stored in Cloud Key Management Service (Cloud KMS).

### Explanation

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

---

## Question 31

*Domain 3: Applying Site Reliability Engineering Practices*

You are the Operations Lead handling an ongoing incident on one of your services. The service typically operates at around 70% capacity, and you’ve noticed that one node is returning 5xx errors on every request it receives, along with a noticeable rise in customer support cases. You need to pull the offending node out of the load balancer pool so you can isolate and investigate it, while following Google-recommended practices to manage the incident and limit the impact on users. What should you do?

- [x] A.
    Communicate your intent to the incident team.
    Perform a load analysis to determine whether the remaining nodes can absorb the traffic that would be offloaded from the removed node, and scale the pool if the analysis shows it’s needed.
    Once any new nodes report healthy, drain traffic from the unhealthy node and remove it from service.
- [ ] B.
    Communicate your intent to the incident team.
    Add a new node to the pool, and wait for it to report as healthy.
    Once traffic is being served from the new node, drain traffic from the unhealthy node and remove the old node from service.
- [ ] C.
    Drain traffic from the unhealthy node and remove it from service.
    Monitor traffic to confirm the error is resolved and that the remaining nodes in the pool are handling the load appropriately.
    Scale the pool as necessary to handle the new load.
    Communicate your actions to the incident team.
- [ ] D.
    Drain traffic from the unhealthy node and remove the old node from service.
    Add a new node to the pool, wait for it to report as healthy, and begin serving traffic from it.
    Monitor traffic to confirm the pool is healthy and handling traffic appropriately.
    Communicate your actions to the incident team.

### Explanation

**Correct Answer**

**A.**

  1. Communicate your intent to the incident team.

  2. Perform a load analysis to determine whether the remaining nodes can absorb the traffic that would be offloaded from the removed node, and scale the pool if the analysis shows it’s needed.

  3. Once any new nodes report healthy, drain traffic from the unhealthy node and remove it from service.

**Exam Reasoning Explanation**

Three things must hold: the incident team stays informed as part of coordinated response rather than finding out after the fact; removing the unhealthy node must not leave the remaining pool unable to absorb its traffic, since the service already runs at a substantial 70% baseline; and the node should be removed gracefully, by draining it, rather than abruptly. Options C and D both act first and communicate last, running against coordinated incident response, and both remove the unhealthy node before confirming sufficient remaining capacity, risking a cascading overload in the window before new capacity is added. Option B communicates first and ensures a new node is healthy before removing the bad one, protecting capacity, but it unconditionally adds a new node without first checking whether the existing 30% of spare capacity is actually enough — less analysis-driven than evaluating first. Option A communicates first, performs a load analysis to determine whether scaling is actually needed given the service’s normal 70% utilization, scales only if that analysis shows a genuine gap, and only then drains and removes the unhealthy node — satisfying all three requirements with the most measured, analysis-driven approach.

**Key Exam Clues**

  * “The service usually runs at around 70% capacity” — a deliberately given detail establishing headroom in the system, prompting an analysis of whether that headroom is sufficient rather than an automatic decision to add capacity

  * “follow Google-recommended practices to manage the incident” — points toward structured incident response, including communication to the incident team as coordination happens, not as a final report

  * “remove the offending node... so that you can isolate and investigate” — frames node removal as the goal, but one that still needs to happen safely, which is why the order of operations matters

  * Communication appearing as either the first or last step across the four options — a clear signal that when communication happens is one of the things being tested

**Why This Is Correct**

Communicating intent to the incident team first keeps everyone coordinated before a production-affecting action is taken, core to structured incident response. Performing a load analysis before deciding whether to scale directly uses the fact that the service normally runs at 70% capacity — rather than assuming new capacity is automatically required, the analysis determines whether existing headroom is enough to absorb the unhealthy node’s traffic, scaling only if it isn’t. Waiting until any new nodes report healthy before draining and removing the unhealthy node ensures the pool never dips below the capacity needed to serve current demand, and draining lets in-flight requests complete safely rather than being abruptly cut off.

**Why the Other Options Are Not the Best Fit**

**Option B — Technically Possible but Not Best:** Communicating first and ensuring a new node is healthy before removing the bad one protects capacity, but it skips the load analysis step and always adds a new node regardless of whether the service’s existing spare capacity would have been sufficient on its own — a less deliberate response than evaluating first.

**Option C — Violates Requirement:** Removing the unhealthy node before confirming the remaining nodes can handle the offloaded traffic risks overloading the pool during the gap before scaling happens reactively in step 3, and communicating to the incident team only as the final step means coordination happens after the mitigating action has already been taken.

**Option D — Violates Requirement:** This shares Option C’s core problems — the unhealthy node is removed before any replacement capacity exists, creating a window where the pool may be under-provisioned, and communication again comes last, after the node has already been pulled and a new one added.

**Exam Trap**

The trap is treating “remove the bad node quickly” as the priority, when the real priority is removing it _safely_ , without creating a second, broader problem by overloading the remaining capacity — Options C and D both act first and reason about capacity afterward, reversing the safer order. A second trap is assuming any option that adds a new node before removing the old one is equally good; Option B does this unconditionally, while the specifically called-out 70% baseline capacity detail rewards recognizing that a load analysis might show scaling isn’t even necessary, which only Option A captures.

**Foundation Concept**

Mitigating an incident that involves removing a capacity-serving component from production should follow a sequence that protects users throughout: communicate with the incident team as actions are planned and taken, assess whether remaining capacity is sufficient using the real utilization data already known about the system, scale only if that assessment shows a genuine gap, and perform the actual removal gracefully only once any necessary additional capacity is confirmed healthy. This ordering keeps both the team and the user-facing system in a known-good state at every step.

**Real-World Connection**

An on-call engineer managing a node reporting 5xx errors on all requests tells the incident channel what they’re about to do, checks current utilization against the service’s normal 70% baseline, confirms the remaining nodes have enough headroom to absorb the bad node’s share of traffic without needing to scale, and then drains and removes the unhealthy node — all while the incident team has visibility into each step as it happens, and users experience a smooth transition rather than a second wave of errors from an overloaded remaining pool.

**Memory Hook**

Communicate first, analyze capacity before acting, scale only if the analysis shows it’s needed, then drain and remove — never remove the bad node before confirming the rest of the pool can handle the load, and never save communication for last.

**30-Second Exam Takeaway**

When a question sequences incident mitigation steps around removing a capacity-serving node, look for the option that communicates to the incident team first, performs a capacity/load analysis before deciding whether to scale, and only drains and removes the unhealthy node once sufficient capacity is confirmed — options that act before analyzing or communicate only after acting are the wrong order.

**Official References**

[**Google SRE Workbook — Chapter 9: Incident Response:**](https://sre.google/workbook/incident-response/) Supports: the “3Cs” of incident management (coordinate, communicate, control) that make early communication with the incident team a core part of a well-run mitigation, rather than a final report after action has already been taken

---

## Question 32

*Domain 2: Building and Implementing CI/CD Pipelines*

You are developing reusable infrastructure as code modules. Each module includes integration tests that launch the module in a test project, and your source control is GitHub. You need to test your feature branches continuously and make sure all code is tested before any change is accepted. You need to automate the integration tests. What should you do?

- [ ] A. Use a Jenkins server for your CI/CD pipelines, and run all of the tests on the feature branch on a periodic schedule.
- [ ] B. Have the pull request reviewers run the integration tests before they approve the code.
- [ ] C. Use Cloud Build to run the tests, and trigger the full set of tests after a pull request has been merged.
- [x] D. Use Cloud Build to run the tests in a specific folder, and trigger a Cloud Build run for every GitHub pull request.

### Explanation

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

---

## Question 33

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

You need to enforce several constraint templates across your Google Kubernetes Engine (GKE) clusters, with policy parameters that include restrictions on the Kubernetes API. The policy parameters must live in a GitHub repository and be applied automatically whenever that repository changes. What should you do?

- [ ] A. Configure a GitHub Action that triggers Cloud Build whenever a parameter changes, and have Cloud Build run a gcloud CLI command to apply the change.
- [ ] B. Configure a webhook that fires on GitHub changes and sends a request to Anthos Service Mesh to apply the change.
- [x] C. Configure Anthos Config Management to sync with the GitHub repository, so it automatically applies the change whenever the repository is updated.
- [ ] D. Configure Config Connector to sync with the GitHub repository, so it automatically applies the change whenever the repository is updated.

### Explanation

**Correct Answer**

**C. Configure Anthos Config Management to sync with the GitHub repository, so it automatically applies the change whenever the repository is updated.**

**Exam Reasoning Explanation**

The solution must enforce Kubernetes-level policy constraint templates, keep parameters in a Git repository, and apply changes automatically with no manual steps. Policy Controller, the Anthos Config Management component built for exactly this, lets you define and parameterize constraint templates — such as ones restricting Kubernetes API usage — as Kubernetes custom resources, while Config Sync continuously syncs those resources from a Git repository to registered clusters, applying changes automatically as the repository updates. Config Connector (D) is architecturally built to manage Google Cloud resources, not Kubernetes-level policy constraints, so it’s the wrong tool for this object type regardless of being wired to a repository. Anthos Service Mesh (B) is a traffic-management product with no role in applying Kubernetes policy objects. A custom Cloud Build pipeline (A) could technically apply changes via gcloud/kubectl, but means building and maintaining a bespoke sync mechanism rather than using the Google-managed tool designed for this. Anthos Config Management (C) satisfies every part of the requirement as a single, purpose-built solution.

**Key Exam Clues**

  * “enforce several constraint templates... policy parameters, such as restricting the Kubernetes API” — specifically names the Policy Controller/Gatekeeper constraint-template pattern, pointing directly at ACM’s policy-enforcement component

  * “stored in a GitHub repository and automatically applied when changes occur” — describes a continuous GitOps sync pattern, Config Sync’s defining function

  * “across your... GKE clusters” (plural) — reinforces a tool built for consistently applying the same policy set across a fleet from one source of truth, not a one-off scripted pipeline

  * Four very different tool categories across the options (CI/CD pipeline, service mesh, config/policy management, cloud-resource management) — signals this is a “match the capability to the tool” question

**Why This Is Correct**

Anthos Config Management combines Policy Controller, which lets you define parameterized constraint templates — including ones restricting Kubernetes API usage — as Kubernetes custom resources, with Config Sync, which continuously reads configuration from a connected Git repository and applies it across registered clusters as a single source of truth. Pointing Config Sync at the GitHub repository means any committed change to the constraint parameters is automatically detected and applied to every configured cluster, with no custom pipeline logic and no manual steps.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** A GitHub Action triggering Cloud Build to run a gcloud command could eventually apply the same changes, but requires designing, securing, and maintaining a custom sync pipeline, duplicating functionality Anthos Config Management already provides as a managed, purpose-built capability.

**Option B — Different Use Case:** Anthos Service Mesh manages traffic routing, mutual TLS, and observability between services; it has no mechanism for applying Kubernetes constraint templates or policy objects, so routing a webhook to it accomplishes nothing related to the described policies.

**Option D — Different Use Case:** Config Connector’s custom resources map to Google Cloud resources like databases and storage buckets, not Kubernetes policy constraint templates. It isn’t built to enforce API restrictions or other cluster-level policy constraints, and syncing it to a Git repository doesn’t change what kind of objects it manages.

**Exam Trap**

The trap is seeing “Kubernetes CRDs synced from a Git repo” and reaching for Config Connector, since it sounds structurally similar, without checking that Config Connector’s CRDs represent Google Cloud infrastructure resources, not Kubernetes policy constraints. The actual tool for constraint templates and policy parameters is Policy Controller, bundled with Config Sync inside Anthos Config Management — a distinction the question tests by pairing two superficially similar “GitHub repo plus GKE-adjacent tool” options that solve different problems.

**Foundation Concept**

Anthos Config Management is Google’s combined configuration-and-policy management service for Kubernetes: Config Sync continuously applies configuration from a Git repository as a single source of truth across one or many clusters, while Policy Controller defines and enforces constraint templates and their parameters, built on the open source Gatekeeper project. Together they implement a GitOps workflow specifically for Kubernetes configuration and policy, distinct from Config Connector’s separate role of managing Google Cloud resources through Kubernetes custom resources.

**Real-World Connection**

A platform team maintains a Git repository containing Policy Controller constraint templates that restrict which Kubernetes API groups and verbs are allowed across the fleet, and configures Config Sync on every GKE cluster to pull from that repository. When a security engineer tightens a policy parameter and merges the change, every connected cluster picks up and enforces the new restriction automatically, with no per-cluster manual application and a clear, auditable Git history of every policy change over time.

**Memory Hook**

Constraint templates and policy parameters, synced automatically from Git, across many GKE clusters → Anthos Config Management (Policy Controller + Config Sync); Config Connector manages Google Cloud resources, not Kubernetes policy constraints.

**30-Second Exam Takeaway**

When a question describes enforcing Kubernetes constraint templates or policy parameters from a Git repository across GKE clusters, that’s Anthos Config Management’s Policy Controller and Config Sync — don’t confuse it with Config Connector (Google Cloud resource management), Anthos Service Mesh (traffic management), or a custom CI/CD pipeline built to replicate functionality Google already provides natively.

**Official References**

[Google Cloud — Config Sync overview: ](https://cloud.google.com/anthos-config-management/docs/config-sync-overview)Supports: Config Sync applying Policy Controller constraints from a Git repository consistently across registered clusters

[**Google Cloud — gcloud apply fields reference (Anthos Config Management):**](https://cloud.google.com/anthos-config-management/docs/reference/gcloud-apply-fields) Supports: the configSync.syncRepo and policyController configuration fields used to wire a Git repository to automatic constraint-template enforcement

---

## Question 34

*Domain 3: Applying Site Reliability Engineering Practices*

You have just noticed that one of your services has used up its error budget for the current rolling window. Meanwhile, your company’s product team is about to launch a new feature. You want to follow Site Reliability Engineering (SRE) practices. What should you do?

- [ ] A. Tell the team there is no error budget left, and make sure all of their tests pass so the launch doesn’t put any further strain on the budget.
- [x] B. Tell the team their error budget is used up. Negotiate with them between a launch freeze and accepting a somewhat worse user experience.
- [ ] C. Escalate the situation and ask for additional error budget.
- [ ] D. Search the product’s other metrics for SLOs that still have error budget left, reallocate that budget, and let the feature launch proceed.

### Explanation

**Correct Answer**

**B. Tell the team their error budget is used up. Negotiate with them between a launch freeze and accepting a somewhat worse user experience.**

**Exam Reasoning Explanation**

The error budget exists to give product and SRE teams a shared, data-driven way to trade reliability against feature velocity. Once the budget is spent, the data says reliability should take priority, and the decision about releases is made transparently with the team that wants to launch. Option B does this. It surfaces the fact that the budget is exhausted and puts the actual trade-off on the table: freeze the launch, or knowingly accept a degraded user experience. Options A, C, and D each try to get around the signal instead of acting on it. A assumes passing tests protect the budget, but tests do not stop production errors. C treats the budget as something to request more of, which defeats its purpose. D moves budget between unrelated SLOs, which does not reflect the reliability of the service that has actually exceeded its budget.

**Key Exam Clues**

  * “exceeded the error budget for the current rolling window” is the trigger condition that the SRE error budget policy exists to handle

  * “You want to follow Site Reliability Engineering (SRE) practices” points to the error budget policy and its release-versus-reliability trade-off, not to workarounds

  * “about to launch a new feature” sets up the tension between velocity and reliability that error budgets are designed to arbitrate

  * The options that reallocate or request more budget (C, D) treat the budget as negotiable arithmetic, which should stand out as incompatible with how SLOs work

**Why This Is Correct**

Google’s example error budget policy states that when a service has exceeded its error budget for the preceding four-week window, all changes and releases other than P0 issues or security fixes are halted until the service is back within its SLO. The same policy says it is not meant as a punishment, and that it gives teams permission to focus on reliability when the data indicates it matters more than new features. Notifying the product team and negotiating between a launch freeze and tolerating a slightly worse user experience follows this approach. It treats the exhausted budget as a decision point for the whole organization, to be resolved openly with the team that owns the launch, rather than as something to hide, bypass, or inflate.

**Why the Other Options Are Not the Best Fit**

**Option A: Technically Possible but Not Best.** Passing tests is good practice, but it does not address the situation. The service has already overspent its budget, and tests cannot guarantee that a launch won’t add production errors. It also leaves the trade-off implicit and doesn’t give the product team the information needed to decide about the launch.

**Option C: Violates Requirement.** An error budget is derived directly from the SLO, which is 1 minus the target, so it is not something that can be granted on request. Asking for more budget turns the budget from a decision-making tool into a negotiable allowance and removes the signal that reliability needs attention.

**Option D: Violates Requirement.** Each SLO measures a different aspect of user experience, so spare budget on one SLO does not offset overspending on another. Reallocating budget hides the fact that the affected service is unreliable and lets the launch go ahead while users are already seeing degraded reliability on that dimension.

**Exam Trap**

The trap is choosing an option that sounds cooperative, such as being helpful by ensuring the launch is safe (A), finding more budget (C), or reallocating it (D). All three let the launch proceed without confronting the exhausted budget. The correct answer is the one that surfaces the exhausted budget to the product team and has them decide between a freeze and a worse user experience, because the error budget is meant to inform that decision, not be engineered around. The option wording is also a trap: “tolerate a slightly worse user experience” can look like a poor choice, but it is the honest alternative to a freeze that the policy expects teams to weigh.

**Foundation Concept**

An error budget is the allowed amount of unreliability implied by an SLO, calculated as 100% minus the SLO target. Error budgets give product and SRE teams a shared way to balance reliability against feature velocity. While budget remains, teams can take risks and release features. When it is exhausted, an error budget policy agreed in advance by the stakeholders governs what happens next, typically halting non-critical releases until the service is back within its SLO. Disputes about how the policy applies are escalated to a defined decision maker rather than resolved by changing the budget.

**Real-World Connection**

A team’s checkout service has used all of its four-week error budget after a series of incidents, and the product team plans to ship a promotion feature next week. The SRE lead meets with the product manager, shows that the budget is exhausted and which incidents consumed it, and lays out two options: delay the launch while engineering fixes the causes, or launch on schedule and accept that checkout reliability may stay below target for a while. The product manager decides to slip the launch by two weeks. The decision is made with the data in front of everyone, and nobody has altered the SLO or moved budget around to make the numbers look acceptable.

**Memory Hook**

Budget spent means the launch decision goes back to the team: freeze it or knowingly accept worse reliability. Don’t ask for more budget, don’t move budget between SLOs, and don’t treat passing tests as a substitute.

**30-Second Exam Takeaway**

When a scenario says a service has exhausted its error budget and a launch is coming, choose the answer that communicates the exhausted budget and has the team decide between halting the launch and accepting reduced reliability. Reject any option that creates, requests, or reallocates budget to make the launch possible.

**Official References**

[**Google SRE Workbook, Appendix B: Example Error Budget Policy:**](https://sre.google/workbook/error-budget-policy/) Supports: halting changes and releases other than P0 issues or security fixes once the four-week error budget is exceeded, the policy’s non-goal of punishing teams for missing SLOs, and escalation to a named decision maker when parties disagree

[**Google SRE Workbook, Chapter 2: Implementing SLOs:**](https://sre.google/workbook/implementing-slos/) Supports: the definition of an error budget as 100% minus the SLO, and the use of an error budget policy to decide what to do once the budget is exhausted

---

## Question 35

*Domain 3: Applying Site Reliability Engineering Practices*

You are creating a Cloud Monitoring SLO for a service that will be published soon. You want to verify that requests to the service are handled in under 300 ms at least 90% of the time over each calendar month. You need to choose the metric and the evaluation method. What should you do?

- [x] A. Select a latency metric and use the request-based evaluation method.
- [ ] B. Select a latency metric and use the windows-based evaluation method.
- [ ] C. Select an availability metric and use the request-based evaluation method.
- [ ] D. Select an availability metric and use the windows-based evaluation method.

### Explanation

**Correct Answer**

**A. Select a latency metric and use the request-based evaluation method.**

**Exam Reasoning Explanation**

Two independent choices have to be right: which metric measures the thing the SLO is about, and which evaluation method counts the right kind of event. The goal is about how fast requests are served, so the metric must be latency, which removes both availability options. The goal is also stated as a share of requests that meet a threshold (“fewer than 300 ms at least 90% of the time”), so each request is the unit being counted, and that is the request-based method. “Per calendar month” is a separate SLO setting, the compliance period, and does not influence either choice. Only A is correct on both.

**Key Exam Clues**

  * “requests... addressed in fewer than 300 ms” is a technical signal that the SLI is latency, with a 300 ms threshold deciding which requests count as good

  * “at least 90%” is the performance goal, expressed as a proportion of requests that meet the threshold, which is how a request-based SLI is defined

  * “per calendar month” is a compliance-period setting, not a clue about the metric or evaluation method

  * “identify the metric and evaluation method” tells you the answer needs one choice for each, so both must be checked

**Why This Is Correct**

A latency SLI in Cloud Monitoring is the ratio of calls under a latency threshold to all calls. With request-based evaluation, the SLO is met when the fraction of good requests, here those faster than 300 ms, is at or above the goal over the compliance period. Cloud Monitoring’s own example is “Latency is below 100 ms for at least 95% of requests”, which has the same structure as this requirement. You set the 300 ms threshold in the SLI details, the 90% goal as the performance goal, and a calendar month as the compliance period.

**Why the Other Options Are Not the Best Fit**

**Option B, Violates Requirement.** Windows-based evaluation counts time intervals that meet a goodness criterion, for example 10-minute windows in which the 95th-percentile latency is under a threshold. That measures the share of time a service performed well, which is not the share of requests under 300 ms. It also gives a quiet interval the same weight as a busy one, which changes what is being measured.

**Option C, Different Use Case.** Request-based evaluation is the right method, but an availability metric measures the ratio of successful responses to all responses, not how fast they were. A fast failure or a slow success would both be misjudged, so this option cannot verify a latency target.

**Option D, Violates Requirement.** It is wrong on both counts: availability does not measure speed, and windows-based evaluation does not count requests.

**Exam Trap**

The phrase “90% of the time” tempts people toward windows-based evaluation, since “of the time” sounds like time intervals. In this scenario, though, “of the time” is shorthand for “of the requests”, because the subject of the sentence is requests and the threshold applies to each of them. A second trap is treating “per calendar month” as a hint about the evaluation method, when it is only the compliance period. The answer would change to windows-based if the goal were stated per interval, for example “95th-percentile latency under 300 ms in at least 90% of 10-minute windows”, or if the only raw metric available were a latency percentile, since Google’s documentation says a percentile metric requires a windows-based SLO.

**Foundation Concept**

A Cloud Monitoring SLO is built from three parts: an SLI that measures performance, a performance goal, and a compliance period, either calendar-based or rolling. The SLI is chosen in two steps, the metric (such as availability or latency) and the evaluation method. Request-based evaluation treats each request as the event and reports the fraction of good requests. Windows-based evaluation treats each time interval as the event and reports the fraction of good intervals.

**Real-World Connection**

A team preparing to launch an API defines its latency SLO in the Cloud Monitoring console by choosing the latency metric, selecting request-based evaluation, setting the threshold to 300 ms, setting the goal to 90%, and using a calendar month as the compliance period. Once the service is live, the console shows what share of requests came in under 300 ms. The team can also use the remaining error budget to decide whether a risky release is acceptable.

**Memory Hook**

Choose the metric for what you measure (speed means latency), choose the evaluation method for what you count (requests means request-based), and treat the calendar month as the compliance period.

**30-Second Exam Takeaway**

When a Cloud Monitoring SLO is worded as “X% of requests faster than N ms”, use a latency metric with request-based evaluation. Pick windows-based only when the goal is about the share of time intervals that meet a criterion, or when the raw metric is a percentile.

**Official References**

[**Google Cloud Observability: Concepts in service monitoring:**](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring) Supports: the definition of a latency SLI as the ratio of calls below a threshold to all calls, request-based versus windows-based SLO compliance, the example “Latency is below 100 ms for at least 95% of requests”, and calendar-based compliance periods

[**Google Cloud Observability: Creating an SLO:**](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-slo) Supports: the console workflow of choosing a metric, then a request-based or windows-based evaluation method, setting the latency threshold, and choosing a calendar or rolling compliance period

---

## Question 36

*Domain 2: Building and Implementing CI/CD Pipelines*

Your application runs on Cloud Run. You want to test a new version using live production traffic, and at the same time let the quality assurance (QA) team test it manually. You need to limit the potential impact of any problems found during testing, and you must be able to roll back to a previous version of the application if necessary. How should you deploy the new version? (Choose two.)

- [ ] A. Deploy the application as a new, separate Cloud Run service.
- [x] B. Deploy a new Cloud Run revision that has a tag, using the --no-traffic option.
- [ ] C. Deploy a new Cloud Run revision that has no tag, using the --no-traffic option.
- [ ] D. Deploy the new application version using the --no-traffic option, and route production traffic to the revision’s URL.
- [x] E. Deploy the new application version, and split traffic to the new version.

### Explanation

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

---

## Question 37

*Domain 2: Building and Implementing CI/CD Pipelines*

You are investigating problems in a production application that runs on Google Kubernetes Engine (GKE). You’ve traced the problem to a recently updated container image, but you haven’t been able to identify which code change caused it. The deployment currently references the image by its latest tag. You need to get the cluster running a version of the container that works as intended. What should you do?

- [ ] A. Create a new tag named stable that points to the previously working container image, and change the deployment to reference that new tag.
- [x] B. Change the deployment to reference the sha256 digest of the previously working container image.
- [ ] C. Build a new container image from an earlier Git tag, and perform a rolling update of the deployment to that new image.
- [ ] D. Reapply the latest tag to the previous container image, and perform a rolling update of the deployment.

### Explanation

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

---

## Question 38

*Domain 3: Applying Site Reliability Engineering Practices*

You are the Site Reliability Engineer responsible for your company’s data services and products. You regularly deal with operational challenges, such as unpredictable data volume and high cost, in your company’s data ingestion processes. You have just learned that a new data ingestion product will be developed in Google Cloud. You need to work with the product development team to give them operational input on the new product. What should you do?

- [ ] A. Deploy the prototype product to a test environment, run a load test, and share the results with the product development team.
- [ ] B. After the initial version passes the quality assurance phase and compliance assessments, deploy the product to a staging environment, and share error logs and performance metrics with the product development team.
- [ ] C. Once at least one internal customer is using the new product in production, share error logs and monitoring metrics with the product development team.
- [x] D. Review the product’s design with the product development team, and give feedback early in the design phase.

### Explanation

**Correct Answer**

**D. Review the product’s design with the product development team, and give feedback early in the design phase.**

**Exam Reasoning Explanation**

The operational problems named in the scenario, unpredictable data volume and high cost, are largely determined by architecture and design choices. The input you provide is therefore worth the most when it arrives while those choices are still being made. Options A, B, and C each offer evidence and feedback at a later stage of the lifecycle, after the design has been built and more commitments exist. Only D puts operational experience into the design itself, where changes are cheapest. The later options also use test, staging, or production data to describe problems that earlier input could have prevented.

**Key Exam Clues**

  * “unpredictable data volume and high cost” are design-level concerns, such as how the system absorbs bursts and how it uses resources, which are hard to fix after the architecture is set

  * “a new data ingestion product will be developed” means the product is at the start of its lifecycle, so there is still a design phase to influence

  * “collaborate with the product development team to provide operational input” points to working together on the product’s design, not delivering test or monitoring reports

  * Options A, B, and C describe progressively later lifecycle stages (prototype test, staging, production), while D is the only one at the design stage

**Why This Is Correct**

Google’s SRE engagement model describes the architecture and design phase as the first place SRE can contribute, for example by sharing best practices, giving early engagement consulting on architectures and design choices, and helping validate assumptions with targeted prototypes. The SRE Workbook notes that early SRE engagement can help avoid costly redesigns that become necessary once a system meets real-world users and has to scale as the service grows. That is the same set of problems you face with unpredictable volume and cost. Reviewing the design with the development team lets you bring the lessons from your existing ingestion processes into the new product before they are expensive to apply.

**Why the Other Options Are Not the Best Fit**

**Option A, Technically Possible but Not Best.** A prototype load test gives useful evidence, but it comes after a prototype exists, so major design decisions have already been made. Results that show a scaling or cost problem may then force rework that earlier design input could have avoided.

**Option B, Technically Possible but Not Best.** Waiting until the product has passed quality assurance and compliance assessments means the design is largely fixed and changes are expensive. Error logs and performance metrics from staging describe what was built, not what should be built.

**Option C, Technically Possible but Not Best.** Sharing logs and metrics only after an internal customer uses the product in production is the most reactive choice. It treats SRE as a recipient of problems instead of a contributor to the product, and real users are already exposed to any issue before the first piece of input is given.

**Exam Trap**

The trap is picking a hands-on validation step, especially the load test in A, because it sounds concrete and data-driven. A load test is valuable, but it answers whether a design copes after the design exists. The scenario’s cues, unpredictable volume and high cost, are design problems that are best handled before building. The answer would change to A if the product were already built and the question asked how to verify capacity before launch.

**Foundation Concept**

The cost of changing a decision rises as a service moves through its lifecycle. Characteristics such as how a system handles variable load and how efficiently it uses resources are set during architecture and design. Engaging early, sometimes called shifting left, lets operational experience shape those decisions instead of being applied as fixes later. SRE can take part through design reviews, best practices, and consulting, and still engage at later stages when a team arrives late.

**Real-World Connection**

An SRE with experience of bursty ingestion volumes is invited to the new product’s design review. They raise questions about what happens when input spikes, how cost grows with volume, and how operators will see and control both. The development team revises the design before any code is written, and the team avoids discovering the problem later through a failed load test or a production incident.

**Memory Hook**

Operational problems that come from design are best fixed in the design phase, so review the design early.

**30-Second Exam Takeaway**

When a new product is just starting development and SRE wants to contribute operational input, choose early engagement in the design phase over any option that waits for a prototype, staging, or production. Later steps validate or react to design choices, but only early input can change them cheaply.

**Official References**

[**Google SRE Workbook, Chapter 18: SRE Engagement Model:**](https://sre.google/workbook/engagement-model/) Supports: Phase 1 (Architecture and Design) engagement activities, such as early engagement consulting and best practices, and the point that early SRE engagement can help avoid costly redesigns when systems meet real users and need to scale

[**Google SRE Book, Chapter 32: The Evolving SRE Engagement Model:**](https://sre.google/sre-book/evolving-sre-engagement-model/) Supports: the Early Engagement Model and the Production Readiness Review process as ways for SRE to partner with development teams across a service’s lifecycle

---

## Question 39

*Domain 3: Applying Site Reliability Engineering Practices*

You need to introduce postmortems into your organization, and you want the postmortem process to be well received. What should you do? (Choose two.)

- [ ] A. Encourage new employees to learn the practice by conducting postmortems for the team.
- [ ] B. Set up a dedicated team that is responsible for conducting every postmortem.
- [x] C. Encourage senior leadership to acknowledge and take part in postmortems.
- [x] D. Make sure that writing effective postmortems is a practice that is both rewarded and celebrated.
- [ ] E. Give the organization a forum in which to critique earlier postmortems.

### Explanation

**Correct Answer**

**C. Encourage senior leadership to acknowledge and take part in postmortems.**

**D. Make sure that writing effective postmortems is a practice that is both rewarded and celebrated.**

**Exam Reasoning Explanation**

The goal is cultural adoption: people must see the postmortem process as valuable and safe rather than as a burden or a punishment. Two options describe the reinforcement mechanisms that build that perception. Visible senior-leadership participation signals that the practice is important and that the whole organization, including those at the top, takes part in learning from failure (C). Rewarding and celebrating effective postmortem writing gives the people who do the work a positive reason to do it well and to keep doing it (D). The remaining options each undermine the goal. Handing every postmortem to a designated team (B) takes ownership away from the engineers who understand the incident. Assigning new employees to conduct postmortems (A) puts the least-equipped people in charge of the process. Opening earlier postmortems to critique (E) risks making authors feel judged. C and D act independently, one through top-down modeling and the other through bottom-up recognition, and together they cover the two main levers of cultural change.

**Key Exam Clues**

  * “introduce postmortems into your organization” frames this as a culture-change question, not a process-design or staffing question

  * “well received” is the success criterion: the right answers are the ones that build acceptance, not the ones that merely get postmortems written

  * “(Choose two.)” signals two complementary actions, here one leadership-driven and one recognition-driven

  * “designated team that is responsible for conducting all postmortems” is a centralization pattern that conflicts with ownership by the engineers involved

**Why This Is Correct**

Google’s SRE guidance says that introducing a postmortem culture takes continuous cultivation and reinforcement, and it lists specific strategies for winning people over. Two of them are to encourage senior leadership’s acknowledgment and participation in postmortems, and to make sure that writing effective postmortems is a rewarded and celebrated practice, both publicly and through individual and team performance management. Leadership participation shows that postmortems matter. Visible rewards show that the effort is valued, which counters the common objection that postmortems cost too much time for too little benefit.

**Why the Other Options Are Not the Best Fit**

**Option A: Technically Possible but Not Best.** Practice has value for newcomers, but having new employees conduct the team’s postmortems puts the least experienced people in charge of a sensitive process whose goal is to build trust. Google’s guidance instead has new SREs learn through exercises that reenact past postmortems, such as the Wheel of Misfortune, which is practice without ownership of real incidents.

**Option B: Violates Requirement.** A dedicated team that conducts every postmortem separates the analysis from the engineers closest to the incident. It makes the process feel imposed from outside and cuts against the collaborative, engineer-owned approach that Google describes, in which blameless postmortems are ideally the product of engineer self-motivation.

**Option E: Technically Possible but Not Best.** Feedback on the postmortem process is valuable, and Google surveys teams about its effectiveness. A forum to critique previous postmortems, though, invites judgment of individual authors’ work, which can make people reluctant to write them. It is not one of the recommended strategies for building acceptance.

**Exam Trap**

The trap is picking options that sound rigorous or process-oriented, such as a dedicated postmortem team (B) or a critique forum (E), when the question asks what makes the process well received. Acceptance comes from signals of safety and value, namely leadership participation and visible recognition, not from adding oversight or centralizing ownership. Option A is a subtler trap, because training newcomers sounds constructive but gives them a sensitive responsibility they are not yet equipped to carry.

**Foundation Concept**

Introducing postmortems is a cultural change as much as a technical one. Cultures shift through what leaders visibly do and what the organization visibly rewards. If senior people participate and good postmortem work is celebrated, others conclude that the practice is safe, valued, and expected. Mandates, centralized ownership, or critique mechanisms can produce documents without producing the openness that makes postmortems useful.

**Real-World Connection**

A new engineering director starts joining postmortem review sessions and says openly what they learned from each one. The team also starts a monthly newsletter that highlights a well-written postmortem and its author, and managers cite strong postmortem work in performance reviews. Engineers who initially saw postmortems as paperwork begin to see them as a way to gain recognition, and they start volunteering to write them.

**Memory Hook**

To make postmortems well received: leaders take part, and good postmortem work gets visibly rewarded. Do not centralize them, hand them to newcomers, or open them to critique.

**30-Second Exam Takeaway**

When a question asks how to get a postmortem culture accepted, choose the options that build safety and perceived value: visible senior-leadership participation and public and performance-based recognition for writing good postmortems. Avoid options that centralize ownership, assign the process to inexperienced staff, or expose authors to critique.

**Official References**

[**Google SRE Book, Chapter 15: Postmortem Culture: Learning from Failure:**](https://sre.google/sre-book/postmortem-culture/) Supports: the “Introducing a Postmortem Culture” strategies of rewarding and celebrating effective postmortem writing and encouraging senior leadership’s acknowledgment and participation, plus the collaborative, engineer-owned approach that rules out a dedicated postmortem team

[**Google SRE Workbook, Chapter 10: Postmortem Culture: Learning from Failure:**](https://sre.google/workbook/postmortem-culture/) Supports: the framing of introducing postmortems as a cultural change that can start small and be tuned to the organization

---

## Question 40

*Domain 3: Applying Site Reliability Engineering Practices*

You have deployed a fleet of Compute Engine instances in Google Cloud. You need to make sure the instances’ monitoring metrics and logs appear in Cloud Logging and Cloud Monitoring, where your company’s operations and cybersecurity teams can see them. You must grant the required roles to the Compute Engine service account through Identity and Access Management (IAM), following the principle of least privilege. What should you do?

- [x] A. Grant the logging.logWriter and monitoring.metricWriter roles to the Compute Engine service accounts.
- [ ] B. Grant the logging.admin and monitoring.editor roles to the Compute Engine service accounts.
- [ ] C. Grant the logging.editor and monitoring.metricWriter roles to the Compute Engine service accounts.
- [ ] D. Grant the logging.logWriter and monitoring.editor roles to the Compute Engine service accounts.

### Explanation

**Correct Answer**

**A. Grant the logging.logWriter and monitoring.metricWriter roles to the Compute Engine service accounts.**

**Exam Reasoning Explanation**

The roles in question go to the service account that the instances run as. That identity only needs to send telemetry, meaning log entries to Cloud Logging and metrics to Cloud Monitoring. The operations and security teams’ ability to view the data depends on their own identities’ access, which this question does not ask you to configure. Because the stated requirement is least privilege, the right choice is the narrowest write-only role for each service. Any role that adds read, edit, or administrative abilities to the service account is wrong. A is the only option made up of two write-only roles.

**Key Exam Clues**

  * “grant the required roles for the Compute Engine service account” is a hard constraint: the identity being configured is the one that sends telemetry, not the people who read it

  * “following the principle of least privilege” is a hard constraint that rules out admin and editor roles when a write-only role exists

  * “monitoring metrics and logs” is a technical signal that two separate write permissions are needed, one for each service

  * Every option pairs one logging role with one monitoring role, so both halves must be checked for excess privilege

**Why This Is Correct**

Google’s Ops Agent authorization guidance names Logs Writer and Monitoring Metric Writer as the roles for the service account the agent uses. The Logs Writer role (logging.logWriter) provides the permissions to write log entries. The Monitoring Metric Writer role (monitoring.metricWriter) is write-only and is intended for service accounts and agents. Together they let the instances send logs and metrics and do nothing beyond that. The same guidance says to grant the service account the least privileged IAM roles possible.

**Why the Other Options Are Not the Best Fit**

**Option B — Violates Requirement:** Logging Admin gives full access to all features of Cloud Logging, and Monitoring Editor gives read-write access to Monitoring, including creating and editing configurations such as dashboards and alerting policies. A service account that only sends telemetry needs neither, so this pair breaks least privilege on both sides.

**Option C — Violates Requirement:** Monitoring Metric Writer is correct, but it is paired with an editor-style logging role, which implies broader access than writing log entries. Google documents Logs Writer as the role that provides the permission to write log entries, so the editor-style role adds privilege without adding capability the agent needs.

**Option D — Violates Requirement:** Logs Writer is correct, but Monitoring Editor grants read-write access to Monitoring and the ability to create and edit configurations. The service account only has to write metrics, which Monitoring Metric Writer already covers.

**Exam Trap**

The trap is choosing a role pair that would certainly make everything work, such as editor or admin roles, instead of the narrowest pair that does the job. Options B, C, and D each contain one plausible role, which makes them look reasonable. Both halves have to be write-only. A second trap is reading “visible by the operations and security teams” as a reason to give the service account viewing roles, when visibility is a matter of the teams’ own access. The answer would change only if the question asked what the teams themselves need to read the data, in which case viewer roles would apply to them and not to the service account.

**Foundation Concept**

A telemetry agent on a VM authenticates as the VM’s attached service account and needs permission only to write data. Cloud Logging and Cloud Monitoring each have a purpose-built write-only role for this, Logs Writer and Monitoring Metric Writer, which are separate from the viewer, editor, and admin roles meant for people. IAM roles are one part of authorization. For VMs that use the default Compute Engine service account, the instance’s access scopes must also permit writing, and Google notes that new VMs usually have adequate scopes but older VMs or VMs with modified scopes might not.

**Real-World Connection**

A platform team builds an instance template for a fleet and attaches a service account that holds only Logs Writer and Monitoring Metric Writer. The Ops Agent on each VM sends logs and metrics, and the operations and security teams read them using their own viewer roles. If an instance were compromised, the service account could do little beyond writing telemetry, so the potential damage is limited.

**Memory Hook**

An instance’s service account only writes telemetry, so give it Logs Writer and Monitoring Metric Writer.

**30-Second Exam Takeaway**

When a question asks which roles an instance’s service account needs for logs and metrics under least privilege, choose the two write-only roles, Logs Writer and Monitoring Metric Writer. Reject admin and editor roles, which add abilities the service account never uses.

**Official References**

[**Google Cloud Observability — Authorize the Ops Agent:**](https://docs.cloud.google.com/logging/docs/agent/ops-agent/authorization) Supports: the Logs Writer and Monitoring Metric Writer roles for the service account the agent uses, the guidance to grant the least privileged roles possible, and the access-scope caveat for older VMs

[**Google Cloud Monitoring — Control access with IAM:**](https://docs.cloud.google.com/monitoring/access-control) Supports: Monitoring Metric Writer as the write-only role for service accounts and agents, Monitoring Editor’s read-write access to configurations, and Logging Admin’s full access to Cloud Logging

[**Google Cloud IAM — Cloud Logging roles and permissions:**](https://docs.cloud.google.com/iam/docs/roles-permissions/logging) Supports: Logs Writer (roles/logging.logWriter) providing the permissions to write log entries

---

## Question 41

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your company runs its services on Google Kubernetes Engine (GKE). The GKE clusters in the development environment run applications with verbose logging turned on. Developers read logs with the `kubectl logs` command and do not use Cloud Logging. The applications do not follow a uniform logging structure. You need to minimize the cost of application logging while still collecting GKE operational logs. What should you do?

- [x] A. Run the `gcloud container clusters update` command with `--logging=SYSTEM` on the development cluster.
- [ ] B. Run the `gcloud container clusters update` command with `--logging=WORKLOAD` on the development cluster.
- [ ] C. Run the `gcloud logging sinks update _Default --disabled` command in the project that hosts the development environment.
- [ ] D. Add an exclusion filter of `severity >= DEBUG resource.type = "k8s_container"` to the `_Default` log sink in the project that hosts the development environment.

### Explanation

**Correct Answer**

**A. Run the**`**gcloud container clusters update**`**command with**`**--logging=SYSTEM**`**on the development cluster.**

**Exam Reasoning Explanation**

Two requirements must both hold: the cost of application logs in Cloud Logging has to drop, and GKE operational logs must keep being collected. Developers already read logs with `kubectl logs`, and the applications have no uniform log structure, so the verbose application logs have little value in Cloud Logging. GKE lets you choose which log sources a cluster sends, and the `--logging` flag separates operational (system) logs from application (workload) logs. Setting the cluster to system-only collection removes the application logs at the source and keeps the operational logs. The other options either collect the wrong source or cut logs after collection with a wide net that can also drop operational logs.

**Key Exam Clues**

  * “minimize the costs associated with application logging” is a hard constraint, and application logs are the specific thing to cut

  * “while still collecting GKE operational logs” is a hard constraint that rules out any option that stops or filters system logs

  * “Developers view logs by using the `kubectl logs` command and do not use Cloud Logging” is context showing that nobody consumes the application logs in Cloud Logging

  * “Applications do not have a uniform logging structure” is context showing the application logs have limited value for querying and that field-based filtering is not reliable

  * `--logging=SYSTEM` versus `--logging=WORKLOAD` is a technical signal that the decision is about which log source the cluster collects

**Why This Is Correct**

The `--logging` flag controls which logs a GKE cluster sends to Cloud Logging. The `SYSTEM` value collects logs from Pods in system namespaces such as kube-system, from non-containerized services such as containerd and kubelet, and Kubernetes events. Google documents it as required for all cluster types. The `WORKLOAD` value collects all logs from non-system containers on user nodes and is on by default. Google’s documentation states that a Standard cluster can be configured to capture only system logs and not collect application logs. Setting `--logging=SYSTEM` therefore stops the verbose application logs from being collected at all, so they are not ingested or billed, and the operational logs continue to flow.

**Why the Other Options Are Not the Best Fit**

**Option B — Violates Requirement:** `WORKLOAD` is the log source that collects application logs, which is the opposite of what is needed, and it is already on by default. Google also documents `SYSTEM` as required for all cluster types, so selecting only `WORKLOAD` does not express the intended configuration.

**Option C — Violates Requirement:** Disabling the `_Default` sink stops it from routing log entries into the `_Default` bucket for the whole project, not only the application logs of the development cluster. That includes the GKE system logs the scenario says must still be collected.

**Option D — Technically Possible but Not Best:** Exclusion filters are a legitimate way to reduce log volume, but this filter selects by resource type and severity, not by whether a container is an application or a system Pod. `k8s_container` also covers system Pods, so it can drop operational logs, and it filters after collection instead of avoiding collection. Google also cautions that exclusion filters which keep GKE logs from being ingested can leave you without logs to share with Google Cloud support.

**Exam Trap**

The trap is reaching for an exclusion filter (D) because it is the most familiar log-cost tool. When a whole category of logs has no consumer, turning off its collection is cleaner than ingesting and then filtering. The answer would change to an exclusion filter if you needed to keep part of the application logs in Cloud Logging, such as only higher-severity entries or specific namespaces. It would also change if the clusters were Autopilot, because Google’s documentation describes system-only collection for Standard clusters and exclusion filters for reducing volume on both modes.

**Foundation Concept**

You can control logging cost at two layers. At the source, you configure what the cluster’s logging agent collects. At the routing layer, the Log Router applies sinks and exclusion filters to logs that were already collected. Source-level control suits cases where an entire category of logs is not needed, and routing-level control suits partial reductions. In GKE, system logs are the operational baseline and cannot be turned off while Cloud Logging is on, while workload logs are optional.

**Real-World Connection**

A platform team sets `--logging=SYSTEM` on its development clusters. Developers keep reading application output with `kubectl logs`, node and system-component logs stay in Cloud Logging for troubleshooting and for Google Cloud support, and the logging bill falls because the verbose application logs are no longer ingested. If a team later needs application logs in Cloud Logging for a specific test, the team can re-enable `WORKLOAD` for that cluster.

**Memory Hook**

To drop application logs but keep operational ones, set the cluster’s `--logging` to SYSTEM instead of filtering or disabling at the Log Router.

**30-Second Exam Takeaway**

When a GKE logging-cost question asks to cut application logs while keeping operational logs, choose the cluster-level `--logging=SYSTEM` setting. Avoid disabling the `_Default` sink or using broad exclusion filters, which can also remove system logs.

**Official References**

[**Google Cloud — About GKE logs:**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs) Supports: the `--logging` values `SYSTEM` and `WORKLOAD`, what each collects, that `SYSTEM` is required for all cluster types, that a Standard cluster can capture only system logs, and the caution about exclusion filters affecting GKE logs

[**Google Cloud — Route logs to supported destinations:**](https://docs.cloud.google.com/logging/docs/install/logs_export) Supports: sinks belonging to a project, and the `_Default` sink routing matching log entries into the `_Default` bucket, which shows why disabling it affects every log the project routes there

[**Google Cloud — Professional Cloud DevOps Engineer Certification exam guide (Section 4.1, optimizing logs: filtering, exclusions, cost management, source considerations):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain and objective alignment

---

## Question 42

*Domain 5: Optimizing Performance and Cost*

Your company processes IoT data at scale using Pub/Sub, the App Engine standard environment, and an application written in Go. You have noticed that performance degrades intermittently at peak load, and you could not reproduce the problem on your workstation. You need to monitor the application continuously in production to find the slow paths in the code, while keeping both performance impact and management overhead to a minimum. What should you do?

- [ ] A. Use Cloud Monitoring to review the App Engine CPU utilization metric.
- [ ] B. Install a continuous profiling tool on Compute Engine, and configure the application to send its profiling data to that tool.
- [ ] C. Periodically run the go tool pprof command against the application instance, and analyze the output by using flame graphs.
- [x] D. Set up Cloud Profiler, and initialize the cloud.google.com/go/profiler library in the application.

### Explanation

**Correct Answer**

**D. Set up Cloud Profiler, and initialize the cloud.google.com/go/profiler library in the application.**

**Exam Reasoning Explanation**

Three requirements must hold together. The problem can’t be reproduced locally and appears only intermittently under peak load, so the monitoring has to run continuously in production. You need to find slow paths in the code, so the data must be attributed to functions in the source, not just to resource totals. Finally, both performance impact and management overhead must be minimal, which favors a managed, low-overhead tool over anything you operate yourself. A metric only shows that a resource is busy, and the self-managed and manual profiling options fail the overhead or continuity requirement. Cloud Profiler is the only option that meets all three.

**Key Exam Clues**

  * “could not reproduce this issue on your workstation” is a technical signal that profiling has to happen in production

  * “continuously monitor the application in production” is a hard constraint that rules out occasional manual captures

  * “identify slow paths in the code” is a technical signal that code-level attribution is needed, not infrastructure metrics

  * “minimize performance impact and management overhead” is a hard constraint that favors a managed, low-overhead service

  * “App Engine standard environment” and “written in Go” together point to a supported Cloud Profiler configuration

**Why This Is Correct**

Cloud Profiler is a statistical, low-overhead profiler that continuously gathers CPU usage and memory-allocation information from production applications and attributes it to the source code that generated it. Google states that the overhead of CPU and heap profiling at collection time is under 5 percent, and amortized across the execution time and replicas of a service it is commonly under 0.5 percent, which makes it suitable for always-on use in production. Go on the App Engine standard environment is a supported configuration. You enable it by calling profiler.Start from the cloud.google.com/go/profiler package early in main, and on App Engine the service name and version are inferred from the environment. Google manages the backend and the interface, so you don’t run profiling infrastructure.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** CPU utilization shows how busy the instances are at peak load, which fits the symptom, but it does not show which functions or code paths consume the CPU. It tells you that something is slow, not where in the code.

**Option B — Technically Possible but Not Best:** A continuous profiling tool does fit the continuity requirement, but installing and running it on Compute Engine means provisioning, operating, and securing your own profiling infrastructure and wiring the application to it. That is the management overhead the scenario asks you to avoid, when a managed service already supports this environment.

**Option C — Violates Requirement:** Running go tool pprof periodically is manual and point-in-time, so it can miss an intermittent problem that appears only at peak load, and it is not continuous monitoring. Collecting and analyzing samples by hand is also ongoing operational work.

**Exam Trap**

The trap is picking option A because the symptom appears at peak load and CPU is the obvious resource to check. A resource metric can confirm saturation, but it can’t tell you which code is responsible, which is the actual goal. Option C is a second trap, since pprof is a real Go profiling tool, but it is manual and not continuous. The answer would change to option A only if the goal were to confirm resource saturation or alert on it, and different tooling again (distributed tracing) if the goal were to find which downstream call in a request is slow.

**Foundation Concept**

Metrics and profiles answer different questions. Metrics such as CPU utilization show that a service is slow or saturated, while profiles show where in the code the CPU time or memory goes. Statistical (sampling) profiling takes brief samples at intervals instead of tracing every operation, which keeps overhead low enough to leave on permanently in production. That is what makes it suitable for problems that are intermittent, load-dependent, and impossible to reproduce on a workstation.

**Real-World Connection**

A team adds a single profiler.Start call to its Go service’s main function and deploys to App Engine. After the next peak-load slowdown, they open Profiler, look at the profile data for the period when the degradation occurred, and find that one message-handling function dominates CPU time. They fix that function and redeploy. They never provisioned profiling servers, and the overhead stayed small enough to leave profiling on for good.

**Memory Hook**

For slow code paths in production with minimal overhead, use Cloud Profiler, because metrics show that a resource is busy and profiles show which code is using it.

**30-Second Exam Takeaway**

When a question needs continuous, low-overhead, code-level performance analysis of a production application, choose Cloud Profiler. Reject resource metrics, which don’t point to code, and reject self-hosted or manual profiling, which adds management effort or misses intermittent problems.

**Official References**

[**Google Cloud Profiler — Cloud Profiler overview:**](https://docs.cloud.google.com/profiler/docs/about-profiler) Supports: Cloud Profiler as a statistical, low-overhead continuous profiler for production applications, the overhead figures (under 5 percent at collection, commonly under 0.5 percent amortized), and Go on the App Engine standard environment as a supported configuration

[**Google Cloud Profiler — Profiling Go applications:**](https://docs.cloud.google.com/profiler/docs/profiling-go) Supports: initializing the cloud.google.com/go/profiler library with profiler.Start and App Engine inferring the service name and version

[**Google Cloud — Professional Cloud DevOps Engineer Certification exam guide (Section 5.1, collecting performance information: application performance monitoring):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain and objective alignment

---

## Question 43

*Domain 3: Applying Site Reliability Engineering Practices*

Your CTO has asked you to put a postmortem policy in place for every incident, for internal use. You want to define what a good postmortem looks like so that the policy succeeds at your company. What should you do? (Choose two.)

- [ ] A. Require every postmortem to state what caused the incident, name the person or team responsible for causing it, and describe how to prevent it from recurring.
- [x] B. Require every postmortem to state what caused the incident, describe how the incident could have been worse, and describe how to prevent it from recurring.
- [ ] C. Require every postmortem to state the severity of the incident, describe how to prevent it from recurring, and describe what caused it without naming internal system components.
- [ ] D. Require every postmortem to state how the incident was resolved and what caused it, without naming customer information.
- [x] E. Require every postmortem to involve all incident participants in authoring it, and share postmortems as widely as possible.

### Explanation

**Correct Answer**

**B. Require every postmortem to state what caused the incident, describe how the incident could have been worse, and describe how to prevent it from recurring.**

**E. Require every postmortem to involve all incident participants in authoring it, and share postmortems as widely as possible.**

**Exam Reasoning Explanation**

A successful postmortem policy needs two things: a clear standard for what a postmortem contains, and a process that keeps postmortems honest and useful. The content standard must produce learning and prevention, which means a real root cause, the near-misses that show hidden risk, and actions that prevent recurrence, without blaming anyone. The process standard must bring in everyone who saw the incident and make the result visible to the people who can learn from it. B supplies the content, and E supplies the process. A, C, and D each contain a flaw that would weaken the policy: blame, withheld technical detail, or missing preventive action. B and E work independently of each other, and together they cover both halves of what the CTO asked for.

**Key Exam Clues**

  * “define what a good postmortem is” is a hard constraint that points to both the content and the practices of a quality postmortem

  * “to ensure that the policy is successful” is a hard constraint favoring practices that build trust and adoption, such as blamelessness and open sharing

  * “for internal use” is a technical signal that postmortems can name specific systems and include specific data, which weighs against options that remove technical detail

  * “(Choose two.)” is a cardinality instruction, so one selected option should cover content and the other process

  * “identify the person or team responsible” is an exclusion, since it describes the blame-oriented pattern the policy needs to avoid

**Why This Is Correct**

Option B matches how Google describes a good postmortem. It identifies the root cause and trigger, it includes a “Where we got lucky” lesson, which records the factors that kept the incident from being worse and exposes latent risk, and it ends in preventive action items. The Workbook states that a postmortem with no action items is ineffective, and it describes root-cause sections that focus on what went wrong, not who caused it. Option E matches the Workbook’s recommendations to include all incident participants in postmortem authoring, because a postmortem written in isolation or by one team can overlook contributing factors, and to share postmortems as widely as possible, because the value of a postmortem is proportional to the learning it creates. The two work independently, since one governs what is written and the other governs how it is written and shared, and together they form a complete definition of a good postmortem.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement:** Naming the person or team responsible is the blame-oriented pattern the Workbook lists as a failure mode. It makes people risk-averse and tempts them to hide facts that are critical to preventing recurrence. It is tempting because it names a cause and a prevention step, but the policy’s success depends on blamelessness.

**Option C — Violates Requirement:** Severity and prevention are useful, but banning internal system component names removes the technical specifics needed to explain the root cause and write measurable action items. Google’s good example names the systems involved and explains unfamiliar terms in a glossary, and a policy for internal use should allow that detail.

**Option D — Technically Possible but Not Best:** Describing resolution and cause is useful, and keeping end-user information out of postmortems matches Google’s practice. The option omits follow-up and preventive actions, though, which Google treats as essential, and it says nothing about collaboration or sharing, so it leaves the policy’s success to chance.

**Exam Trap**

The trap is option A, because identifying who caused an incident feels like accountability. A blameless postmortem pursues accountability through owned, tracked action items and through fixing system gaps, not through naming individuals. Option D is a quieter trap, since protecting customer information is a real concern and the option sounds responsible, but it is incomplete without preventive actions. D would come closer to correct if it added action items, and C would be acceptable if it withheld only end-user details instead of internal components.

**Foundation Concept**

A blameless postmortem is a learning tool that focuses on contributing causes and gaps in systems and processes, assuming people acted with good intentions on the information they had. Its quality has two parts. The content part covers impact, root cause and trigger, resolution, lessons including what went well, what went poorly, and where the team got lucky, and action items that have an owner, a priority, and a measurable end state. The process part covers collaborative authoring, timely publication, and wide sharing. A policy that sets standards for both is more likely to produce postmortems that people trust and learn from.

**Real-World Connection**

A company adopts a postmortem template that requires a root cause, a “where we got lucky” section, and prioritized, owned action items filed as tracked bugs. Each postmortem has one owner and collaborators from every team involved in the incident, and the result is published to all engineering employees within about a week. Engineers outside the incident read the postmortems and fix similar weaknesses in their own systems, so repeat incidents decline and people are willing to share information because nobody is blamed.

**Memory Hook**

A good postmortem is blameless in content (cause, how it could have been worse, prevention) and open in process (everyone involved writes it and everyone can read it).

**30-Second Exam Takeaway**

When a question asks how to define a good postmortem, choose the options that keep the content blameless and focused on cause, near-misses, and prevention, and keep the process collaborative and widely shared. Eliminate options that name individuals, remove technical specifics, or leave out preventive actions.

**Official References**

[**Google SRE Workbook, Chapter 10: Postmortem Culture: Learning from Failure:**](https://sre.google/workbook/postmortem-culture/) Supports: the good-postmortem example with root cause, “Where we got lucky”, and prioritized owned action items, blamelessness, including all incident participants in authoring, and sharing postmortems as widely as possible

[**Google SRE Book, Chapter 15: Postmortem Culture: Learning from Failure:**](https://sre.google/sre-book/postmortem-culture/) Supports: the definition of a postmortem as a record of impact, mitigation, root causes, and follow-up actions, blameless postmortems, sharing to the widest useful audience, and keeping end-user-identifying information out of postmortems

[**Google Cloud — Professional Cloud DevOps Engineer Certification exam guide (Section 3, applying site reliability engineering practices):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment

---

## Question 44

*Domain 2: Building and Implementing CI/CD Pipelines*

Your company operates in a highly regulated industry, and its security team requires that only trusted container images can be deployed to Google Kubernetes Engine (GKE). You need a solution that meets this requirement while keeping management overhead to a minimum. What should you do?

- [x] A. Configure Binary Authorization on your GKE clusters to enforce deploy-time security policies.
- [ ] B. Grant the roles/artifactregistry.writer role to the Cloud Build service account, and verify that no employee has write permission on Artifact Registry.
- [ ] C. Use Cloud Run to build and deploy a custom validator, and enable an Eventarc trigger so that validation runs whenever a new image is uploaded.
- [ ] D. Configure Kritis in your GKE clusters to enforce deploy-time security policies.

### Explanation

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

---

## Question 45

*Domain 5: Optimizing Performance and Cost*

You support a set of Java applications running in production, and every application already has Cloud Profiler and Cloud Trace enabled by default. You need a way to identify which of these applications actually require performance tuning. What should you do? (Choose two.)

- [x] A. Compare the application’s wall-clock time with its CPU time; if the gap between them is large, increase its CPU resource allocation
- [ ] B. Compare the application’s wall-clock time with its CPU time; if the gap between them is large, increase its memory resource allocation
- [ ] C. Compare the application’s wall-clock time with its CPU time; if the gap between them is large, increase its local disk storage allocation
- [x] D. Compare the application’s latency, wall-clock time, and CPU time together; if latency is steadily consuming the error budget while the gap between wall-clock time and CPU time is small, mark the application for optimization
- [ ] E. Check the application’s heap usage; if usage is low, mark the application for optimization

### Explanation

**Correct Answer**

**A. Compare the application’s wall-clock time with its CPU time; if the gap between them is large, increase its CPU resource allocation**

**D. Compare the application’s latency, wall-clock time, and CPU time together; if latency is steadily consuming the error budget while the gap between wall-clock time and CPU time is small, mark the application for optimization**

**Exam Reasoning Explanation**

Cloud Profiler reports CPU time (time actually executing on a CPU) and wall-clock time (total elapsed time, including everything the thread wasn’t executing) separately, so comparing the two tells you something different depending on which way the gap points. A must-have constraint is that the chosen signals have to actually distinguish “needs tuning” from “doesn’t,” rather than pointing to an unrelated resource. Working the chain: requirement (use Profiler/Trace data to flag applications that genuinely need tuning) → capability (the wall-clock/CPU gap reveals two distinct conditions depending on its size, and Trace’s latency/error-budget data adds the user-impact dimension) → elimination (B and C swap in resources that have no causal link to CPU/wall-time accounting, and E’s “low heap usage” has no established link to a performance problem) → decision (A and D are the two conditions where the Profiler/Trace signals actually justify action, each addressing a different root cause).

**Key Exam Clues**

  * “the gap between them is large” (A) is a technical signal that a large share of elapsed time was not spent executing on CPU, which is consistent with the application not getting enough CPU time to run when it has work ready to do.

  * “latency... steadily consuming the error budget” combined with “the gap... is small” (D) is a compound hard constraint: the small wall-clock/CPU gap shows the thread is genuinely CPU-bound (actively computing nearly the whole time), and the error-budget erosion confirms that this CPU-bound behavior is measurably hurting users — together these justify flagging the app.

  * “(Choose two.)” signals the answer set should cover two distinct, non-overlapping diagnostic conditions rather than two phrasings of the same one.

**Why This Is Correct**

For A: when wall-clock time is much larger than CPU time, the thread spent most of its elapsed duration not actively running on a CPU core. One concrete cause of this pattern is that the application isn’t being allocated enough CPU capacity to run as often as it’s ready to — it’s sitting ready but not scheduled. In that situation, giving the application more CPU resource allocation directly closes the gap, because the limiting factor is CPU availability, not the code itself.

For D: when wall-clock time and CPU time are close together, the thread is spending nearly all of its elapsed time actively executing — it is genuinely CPU-bound, not waiting on anything. Pairing that with Cloud Trace data showing latency is steadily burning the error budget confirms this CPU-bound behavior is a real, user-facing reliability problem rather than a harmless inefficiency. That combination is exactly the signal that should mark an application for optimization work (such as algorithmic or code-level tuning), since simply adding more of the same resource won’t change code that’s already fully using what it has.

**Why the Other Options Are Not the Best Fit**

**Option B — Incorrect:** a wall-clock/CPU time gap reflects how much of an application’s elapsed time was spent executing versus not, which has no causal connection to how much memory it has. Increasing memory allocation changes how much data the application can hold, not how promptly its threads get CPU time, so it doesn’t address what the gap is actually showing.

**Option C — Incorrect:** the same reasoning applies to local disk storage. Disk capacity governs how much data can be stored and accessed on disk, not whether a thread is executing or waiting, so it has no logical relationship to a wall-clock/CPU time comparison.

**Option E — Incorrect:** heap usage reflects how much memory is currently allocated to live objects, not how efficiently or how slowly the application is running. Low heap usage simply means the application isn’t using much memory — on its own that says nothing about latency, throughput, or CPU behavior, so it isn’t a reliable signal that an application needs performance tuning.

**Exam Trap**

The trap is assuming that any “substantial difference” between wall-clock and CPU time always means the same thing, or that it can be fixed the same way regardless of direction. A large gap and a small gap point to opposite conditions — one suggests the application isn’t getting enough CPU, the other confirms it’s already fully using the CPU it has — so the correct response depends entirely on which direction the comparison points, and in the small-gap case, the fix is code-level optimization rather than scaling a resource at all.

**Foundation Concept**

Application performance monitoring works by correlating multiple signals rather than reading any single metric in isolation. CPU time versus wall-clock time tells you how much of an operation’s duration was spent actively computing, which separates “waiting for a resource” problems from “genuinely compute-intensive” ones; latency and error-budget trends from distributed tracing tell you whether that behavior is actually affecting users enough to matter. Combining both is what turns raw profiling data into an actionable judgment about which applications deserve tuning effort.

**Real-World Connection**

A team notices one service’s wall-clock time is consistently far above its CPU time and finds the service is capped at a low CPU limit even though demand has grown; raising that limit lets the service actually use the CPU time it needs, and the gap closes. A different service shows wall-clock and CPU time nearly identical, and its latency has been quietly eating into its SLO’s error budget for weeks; because the code is already fully CPU-bound, the team profiles the hot path and optimizes an inefficient algorithm rather than scaling resources, which is what actually reduces latency and stops the budget burn.

**Memory Hook**

“Big gap, give it CPU. Small gap plus a shrinking budget, fix the code.”

**30-Second Exam Takeaway**

When a question pairs Cloud Profiler’s CPU-time-versus-wall-time comparison with Cloud Trace’s latency/error-budget data, read the size and direction of the gap as the diagnosis: a large gap points toward insufficient CPU allocation, while a small gap combined with budget-burning latency points toward genuinely CPU-bound code that needs optimization rather than more resources.

**Official References**

[**Google Cloud — Cloud Profiler concepts (CPU time and wall time definitions):**](https://cloud.google.com/profiler/docs/concept) Supports: correct-answer mechanism — what CPU time versus wall time measure and why their gap is diagnostic

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 5.1, Collecting performance information in Google Cloud):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment — application performance monitoring as the basis for identifying optimization candidates

---

## Question 46

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

Your organization routes application logs from several Google Cloud projects into a single central Cloud Logging project. The security team requires that each project team be able to see only their own project’s logs, while the operations team is the only group that can see every project’s logs, and the solution needs to keep costs as low as possible. What should you do?

- [ ] A. Grant each project team access to the central logging project’s _Default view, and grant the operations team Logging Viewer access on the central logging project
- [ ] B. Define a custom IAM role for each project team scoped to the _Default log view in their own individual Google Cloud project, and grant the operations team viewer access on the central logging project
- [x] C. Create a separate log view for each project team that exposes only that team’s application logs, and grant the operations team access to the central logging project’s built-in _AllLogs view
- [ ] D. Export each project team’s logs to its own BigQuery dataset and grant that team access to it, then grant the operations team Logs Writer access on the central logging project

### Explanation

**Correct Answer**

**C. Create a separate log view for each project team that exposes only that team’s application logs, and grant the operations team access to the central logging project’s built-in _AllLogs view**

**Exam Reasoning Explanation**

The must-have constraints are per-team visibility scoped to each project’s own logs, full visibility for operations, and no added storage cost. Preferences like administrative simplicity matter less than meeting those three hard constraints together. Walking the chain: requirement (segment one shared log store by team without duplicating data) → capability (log views filter a subset of a single log bucket and are individually IAM-grantable, with an automatic _AllLogs view for full visibility) → elimination (A relies on a view that doesn’t scope by project, B abandons the central project and adds unnecessary custom roles, D duplicates storage and grants the wrong access direction) → decision (C uses the one mechanism purpose-built for this exact scenario at no extra storage cost).

**Key Exam Clues**

  * “central Cloud Logging project” collecting logs from multiple source projects is a technical signal pointing to a single shared log bucket, which is exactly where log views apply.

  * “each project team can only view their respective logs” and “only the operations team can view all the logs” are hard constraints requiring both narrow, per-project read access and one group with full access from the same store.

  * “minimizing costs” is a hard constraint that eliminates any option that copies or duplicates log data into a separate storage destination.

**Why This Is Correct**

Log views are a Cloud Logging resource that filter a subset of entries within a single log bucket and can be granted individually through IAM, letting a team see only the log entries matching a filter — such as those originating from their own project — without copying or moving any underlying data. Every log bucket also automatically includes a built-in _AllLogs view exposing every entry in that bucket, which is the natural, no-setup grant for the operations team that needs complete visibility. Because both the per-team views and the _AllLogs view operate on the same underlying bucket, there is no additional storage, export, or duplication cost, which satisfies the cost-minimization requirement as well as the access-segregation requirement.

**Why the Other Options Are Not the Best Fit**

**Option A — Incorrect:** a “_Default” view is not a generic view available on any bucket; Cloud Logging automatically creates a _Default view only for the _Default log bucket specifically, and that view shows all non-Data-Access audit logs in that bucket to anyone granted it. It has no built-in mechanism to scope visibility down to a single project’s logs within a shared central bucket, so it cannot deliver “only view their respective logs.”

**Option B — Different Use Case:** pointing each project team back to the _Default view in their own individual project sidesteps the central logging project entirely, undermining the point of centralizing logs for controlled access in the first place. It also requires creating and maintaining a custom IAM role per team, adding management overhead that the purpose-built log views feature is designed to avoid.

**Option D — Violates Requirement:** exporting logs into a separate BigQuery dataset per team duplicates every log entry’s storage, directly conflicting with “minimizing costs.” It compounds the problem by granting the operations team Logs Writer access, which is the wrong direction of permission for a team that needs to view logs, not create them.

**Exam Trap**

The trap is treating “_Default” as a flexible, filterable view that can be scoped per project the way a custom log view can — in reality it is a single, automatically created view tied specifically to the _Default bucket, and it surfaces everything in that bucket rather than a filtered subset. If the requirement instead were about independent retention or export policies per team rather than simply viewing logs, per-team exports (closer to option D) could become more relevant, though the cost trade-off would still need to be weighed.

**Foundation Concept**

Cloud Logging separates storage (log buckets) from access control (log views). A single bucket can hold logs from many sources, and log views let you carve that bucket into filtered, independently access-controlled slices without moving or copying the underlying data. This lets an organization centralize storage for operational simplicity while still enforcing least-privilege, per-team visibility — the same general pattern of separating “where data lives” from “who can see what part of it” that recurs across Google Cloud’s access-control design.

**Real-World Connection**

A platform team aggregates application logs from dozens of projects into one central bucket using an aggregated log sink, then creates one log view per application team filtered to that team’s source project, and grants the operations team the bucket’s _AllLogs view. The result is that each application team gets a focused, noise-free view limited to its own logs, reducing accidental exposure of other teams’ data, while operations retains the full cross-project picture needed for incident response — all without any additional storage spend beyond the single central bucket.

**Memory Hook**

“One bucket, many windows” — log views slice a single bucket into per-team visibility without copying any data.

**30-Second Exam Takeaway**

When a question asks how to let different teams see only their own slice of logs stored in one shared bucket without added cost, think log views paired with the automatic _AllLogs view for full visibility, rather than exporting to a separate store or relying on a bucket’s fixed default view.

**Official References**

[**Google Cloud — About log views (Cloud Logging):**](https://cloud.google.com/logging/docs/logs-views) Supports: correct-answer mechanism, including the documented example of centralizing multi-project logs with one log view per project, and the automatically created _AllLogs and _Default views

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 1.1, Designing the overall resource hierarchy for an organization):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment — multi-project monitoring and logging, and IAM roles and organization-level policies

---

## Question 47

*Domain 2: Building and Implementing CI/CD Pipelines*

Your organization’s shift-left security initiative requires every team to add guardrails to their Google Kubernetes Engine (GKE) clusters so that only trusted, approved container images can be deployed. Which approach best satisfies this requirement?

- [ ] A. Turn on Artifact Analysis for your Artifact Registry repositories to scan container images for known common vulnerabilities and exposures (CVEs)
- [x] B. Require Binary Authorization to attest container images as part of your CI/CD pipeline before they can be deployed
- [ ] C. Set up Identity and Access Management (IAM) policies that enforce a least-privilege model across your GKE clusters
- [ ] D. Run Falco or Prisma Cloud on your GKE clusters to monitor running Pods for vulnerabilities

### Explanation

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

---

## Question 48

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your team supports production systems that frequently become unhealthy and are automatically restarted within a minute, yet you still receive an alert every time this happens. You want to reduce the risk of staff burnout while staying consistent with Site Reliability Engineering (SRE) practices. What should you do?

- [x] A. Stop sending alerts for conditions that don’t require a human to take action
- [ ] B. Adjust the service’s SLO so the error budget isn’t consumed by these events
- [ ] C. Route the alerts to on-call engineers across different time zones
- [ ] D. File an incident report every time one of these alerts fires

### Explanation

**Correct Answer**

**A. Stop sending alerts for conditions that don’t require a human to take action**

**Exam Reasoning Explanation**

The hard constraint is that the system already resolves the problem on its own within a minute, so there is nothing a human can actually do when the alert fires — it can only be acknowledged and dismissed. The preference is to protect genuine incident-response capacity rather than erode it further. Walking the chain: requirement (cut unnecessary interruptions while staying within real SRE discipline) → capability (SRE alerting philosophy pages humans only for conditions requiring action) → elimination (B changes the reliability target instead of the alert, C spreads the same non-actionable load across more people, D adds more non-actionable work) → decision (A removes the root cause: paging humans for something they neither need nor are able to fix).

**Key Exam Clues**

  * “automatically restarted within a minute” is a hard constraint showing the condition already self-remediates, so a human alert adds nothing actionable.

  * “alerts... every time this happens” paired with “reduce the risk of staff burnout” signals the core problem is alert volume/noise, not reliability or staffing capacity.

  * “staying consistent with Site Reliability Engineering (SRE) practices” is an exclusion cue: the answer must align with the SRE principle that paging is reserved for conditions needing human judgment or action.

**Why This Is Correct**

Core SRE monitoring philosophy holds that a page should interrupt a human only when the situation requires timely judgment or action; everything else belongs in logs, dashboards, or tickets rather than the paging path. Because these systems self-heal automatically in under a minute, there is nothing for an engineer to do when the alert fires — it is pure noise. Stopping (or down-routing) alerts for self-healing, non-actionable conditions directly reduces the interruption load on staff, which is the mechanism that prevents burnout while remaining aligned with SRE practice.

**Why the Other Options Are Not the Best Fit**

**Option B — Violates Requirement:** adjusting the SLO so the error budget isn’t consumed by these events changes how reliability is measured, not how often a human is paged. The alerts keep firing and staff keep being interrupted; loosening an SLO purely to protect the error budget also undermines the SLO’s purpose as an honest reliability signal rather than something tuned to avoid discomfort.

**Option C — Different Use Case:** distributing alerts to engineers in other time zones is a follow-the-sun staffing pattern that can help on-call coverage generally, but it does nothing to reduce the total number of non-actionable alerts — it just spreads the same noise across more people, redistributing burnout risk instead of reducing it.

**Option D — Violates Requirement:** filing an incident report for every alert adds manual work on top of an already non-actionable event, increasing toil instead of reducing it — moving further from the stated goal rather than toward it.

**Exam Trap**

The trap is mistaking “document every occurrence” (Option D) or “share the load” (Option C) for sound operational hygiene, when the real SRE lever is reducing alert volume at the source by reserving paging for actionable conditions. If the scenario instead described a self-healing mechanism that was unreliable or masking a worsening trend, suppressing the alert outright would be the wrong move, and tracking occurrences as a metric (distinct from an incident report per event) would matter more.

**Foundation Concept**

In SRE monitoring philosophy, every page should be actionable, every page response should require intelligence, and pages should be reserved for problems that are either happening now or clearly about to happen — not routine, self-resolving events. Conditions a system already auto-remediates are, by definition, not actionable for a human on receipt, so they belong in logs, dashboards, or aggregated metrics rather than the paging pipeline. Keeping the signal-to-noise ratio of pages high is itself a toil-reduction and burnout-prevention practice.

**Real-World Connection**

A team notices their on-call rotation is paged dozens of times a night for Pods that crash and automatically restart within seconds. By reclassifying those events as non-paging log entries — while still tracking their frequency as a metric that can trigger a real investigation if the rate spikes — the team cuts nighttime pages dramatically. The operational result is fewer interrupted nights for on-call engineers, lower attrition risk, and a cleaner signal so that when a page does fire, it’s trusted and acted on quickly rather than reflexively dismissed.

**Memory Hook**

“If a human can’t do anything about it, it shouldn’t page a human.”

**30-Second Exam Takeaway**

When a question describes alerts firing for conditions a system already resolves on its own, look for the option that stops paging on non-actionable conditions rather than one that changes reliability targets, redistributes the same noise, or adds more manual work — SRE treats a high signal-to-noise alerting pipeline as a core defense against toil and burnout.

**Official References**

[**Google SRE Book — Monitoring Distributed Systems:**](https://sre.google/sre-book/monitoring-distributed-systems/) Supports: correct-answer mechanism — the “every page should be actionable” alerting philosophy

[**Google SRE Book — Practical Alerting:**](https://sre.google/sre-book/practical-alerting/) Supports: why non-actionable, self-healing conditions belong outside the paging path (logs/tickets vs. pages)

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 4.3, Managing metrics, dashboards, and alerts):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment — configuring alerting and alerting policies

---

## Question 49

*Domain 2: Building and Implementing CI/CD Pipelines*

Your organization runs Jenkins on a Google Cloud Compute Engine VM for CI/CD and wants to extend its pipelines to manage infrastructure as code with Terraform. The Terraform runs that execute on this Jenkins instance need to be authorized to create Google Cloud resources, and you want to follow Google-recommended practices for granting that authorization. What should you do?

- [x] A. Verify that the Jenkins VM has an attached service account granted the appropriate Identity and Access Management (IAM) permissions
- [ ] B. Configure a Terraform module that has Secret Manager supply the authentication credentials at runtime
- [ ] C. Create a separate service account, download its key file, and set its value in the GOOGLE_CREDENTIALS environment variable on the Jenkins server
- [ ] D. Add a gcloud auth application-default login step to the Jenkins job before the Terraform commands run

### Explanation

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

---

## Question 50

*Domain 3: Applying Site Reliability Engineering Practices*

You’re preparing to launch a new production service that will autoscale through a managed instance group and run across several regions. Each instance will require a substantial amount of resources, and you need to plan for that capacity before launch. What should you do?

- [ ] A. Monitor Cloud Trace output over time to determine the right instance sizing
- [ ] B. Configure the managed instance group to use the n2-highcpu-96 machine type
- [ ] C. Deploy the service across multiple regions behind an internal load balancer that routes traffic between them
- [x] D. Confirm that the instance group’s resource requirements fit within the project’s available quota in each target region

### Explanation

**Correct Answer**

**D. Confirm that the instance group’s resource requirements fit within the project’s available quota in each target region**

**Exam Reasoning Explanation**

The hard constraint is that this question is specifically about capacity planning, not architecture choice or sizing methodology. Walking the chain: requirement (plan for capacity for a resource-heavy, autoscaling, multi-region deployment) → capability (Google Cloud enforces allocation quotas — CPU, instances, IP addresses, and the instance-group resources themselves — at the regional level, and scaling cannot exceed what a region’s quota allows) → elimination (A addresses latency monitoring rather than capacity, B picks an implementation detail that was never justified by the scenario and still doesn’t confirm availability, C restates an already-given requirement and adds an unaddressed routing decision) → decision (D is the step that directly verifies the deployment can actually obtain the resources it needs in every target region).

**Key Exam Clues**

  * “need to plan for capacity” is the hard constraint that points directly at capacity-planning practice, not at sizing, routing, or monitoring tooling.

  * “a large number of resources for each instance” combined with “multiple regions” signals that per-region resource consumption could be substantial, making quota exhaustion a realistic risk.

  * “should be deployed across multiple regions” and “automatically scale using a managed instance group” are design decisions the scenario has already made, so any option that simply restates them isn’t answering what’s being asked.

**Why This Is Correct**

Google Cloud enforces allocation quotas at the regional level — CPU quota, instance-group resource quota, IP addresses, and disk are all capped per region, and using an instance group requires having enough available quota for every resource it consumes. Because this service needs a large amount of resources per instance and will autoscale across several regions, the amount of quota consumed in each region could be significant, and an autoscaler that hits a quota ceiling simply stops growing rather than failing loudly. Confirming that each target region’s available quota can support the planned resource requirements before launch is what capacity planning concretely means here, and it’s the one option that directly prevents a silent scaling ceiling in production.

**Why the Other Options Are Not the Best Fit**

**Option A — Different Use Case:** Cloud Trace reports on request latency and the behavior of distributed calls; it has no role in determining machine sizing or confirming quota availability, so monitoring it doesn’t address planning for capacity.

**Option B — Technically Possible but Not Best:** choosing a specific machine type is a real configuration step that has to happen at some point, but nothing in the scenario establishes this workload is specifically CPU-optimized, and selecting a machine type says nothing about whether that scale of resource is actually obtainable in each region — it isn’t capacity planning on its own.

**Option C — Different Use Case:** the scenario already states the service will run across multiple regions, so repeating that isn’t new guidance, and adding an internal load balancer introduces a traffic-routing decision intended for private, internal-only traffic that isn’t established as appropriate here; neither part addresses resource or capacity planning.

**Exam Trap**

The trap is reaching for an architecture or tooling decision — a machine type, a load balancer, a tracing tool — when the question explicitly asks about capacity planning, which in Google Cloud’s documented sense centers on quotas, limits, and reservations. If the scenario instead asked how to pick the right machine shape for a known workload profile, option B’s reasoning would become the relevant one; here, the stated task is specifically to plan for capacity.

**Foundation Concept**

Capacity planning on Google Cloud means confirming, ahead of scaling, that the quotas and limits governing a project in each target region can actually support the resource consumption you expect. Because quotas for things like CPUs, IP addresses, and instance-group resources are enforced per region, a workload that scales smoothly in one region can still stall in another if that region’s quota was never checked or raised in advance.

**Real-World Connection**

A team launches an autoscaling, resource-heavy service into a new region and finds the managed instance group stalls well below its target size during a traffic spike — not because of an application bug, but because the project’s CPU quota in that region was never raised to match the expected scale. After requesting a quota increase ahead of the next regional launch, the same spike is absorbed without incident, which is why checking quota is treated as a pre-launch capacity-planning step rather than something discovered during an outage.

**Memory Hook**

“Before you scale wide, check what each region will actually let you have.”

**30-Second Exam Takeaway**

When a question explicitly asks about planning for capacity for an autoscaling workload spread across multiple regions, look for the option addressing project quotas and limits — that’s Google Cloud’s documented meaning of capacity planning, distinct from sizing, routing, or monitoring decisions.

**Official References**

[**Google Cloud — Resource quotas for Compute Engine:**](https://cloud.google.com/compute/quotas) Supports: correct-answer mechanism — instance groups require available quota for every resource they consume, and quotas are enforced regionally

[Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 3.2, Managing service lifecycle): ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment — capacity planning (quotas, limits, reservations) and autoscaling with managed instance groups

---

## Question 51

*Domain 2: Building and Implementing CI/CD Pipelines*

While reviewing your delivery pipeline in Google Cloud Deploy, you determine that you need to cut down the toil built into the pipeline and shorten how long an end-to-end deployment takes to complete. What should you do? (Choose two.)

- [x] A. Set up a trigger that notifies the responsible team as soon as a manual intervention step is reached
- [ ] B. Break the pipeline’s automation steps down into a larger number of smaller tasks
- [ ] C. Write a script that automates how the delivery pipeline itself is created in Google Cloud Deploy
- [ ] D. Bring in additional engineers to work through the manual steps
- [x] E. Automate the promotion approval that moves a release from the development environment to the test environment

### Explanation

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

---

## Question 52

*Domain 3: Applying Site Reliability Engineering Practices*

An application running on Google Kubernetes Engine (GKE), made up of several microservices deployed with Deployments and Services, has one microservice whose Pods start returning 403 errors once they’ve been running for more than five hours. Your development team expects it will take about a month to fix the underlying cause, and in the meantime you need to keep the service operating normally, using the fewest steps and following Google-recommended practice. What should you do?

- [ ] A. Create a scheduled job that terminates any Pod that has been running for more than five hours
- [x] B. Add an HTTP liveness probe to the microservice’s Deployment
- [ ] C. Have someone watch the Pods and manually terminate any that have been running for more than five hours
- [ ] D. Set up an alert that notifies you whenever a Pod starts returning 403 errors

### Explanation

**Correct Answer**

**B. Add an HTTP liveness probe to the microservice’s Deployment**

**Exam Reasoning Explanation**

The hard constraint is that whatever solution is chosen has to keep working automatically, unattended, for about a month, using as little new infrastructure as possible. Walking the chain: requirement (keep a known, time-based failure from affecting operations, with the fewest steps) → capability (Kubernetes’ liveness probe is a built-in mechanism precisely for containers that degrade after running for a while, triggering an automatic restart) → elimination (A duplicates that built-in capability with a separate custom resource, C is unscalable manual toil, D only reports the problem without fixing it) → decision (B is the single, declarative addition that uses Kubernetes’ own self-healing feature exactly as designed).

**Key Exam Clues**

  * “Pod returns 403 errors after... running for more than five hours” is a technical signal describing a container that degrades over time and needs a restart to recover — the exact condition liveness probes exist to detect and fix.

  * “will not be resolved for a month” paired with “ensure continued operations” is a hard constraint requiring the solution to keep working automatically and unattended for weeks, ruling out anything that needs a person to keep intervening.

  * “fewest number of steps” and “Google-recommended practices” together form an exclusion cue favoring Kubernetes’ built-in, declarative self-healing feature over custom external automation.

**Why This Is Correct**

An HTTP liveness probe lets the kubelet periodically check whether a container is still healthy; once the probe starts failing, Kubernetes automatically restarts that container. This matches the documented pattern for long-running processes that work correctly at first but degrade after running for a while and need a periodic restart to keep functioning. Configuring the probe is a single, declarative addition to the existing Deployment’s Pod spec, requiring no new resources, no custom scripts, and no ongoing human attention — giving the service a self-healing cycle that can run unattended for the month it takes the development team to ship the real fix.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** a scheduled job that finds and deletes Pods older than five hours can produce a similar outcome, but it duplicates functionality Kubernetes already provides natively through liveness probes, and it means building and maintaining a separate resource with its own logic and permissions — more steps than the built-in mechanism requires.

**Option C — Incorrect:** manually watching Pods and terminating them is pure human toil that doesn’t scale, and it directly conflicts with both “fewest number of steps” and the month-long duration this workaround would need to survive unattended.

**Option D — Incorrect:** an alert only notifies that the problem occurred; it doesn’t restart anything or restore the Pod to a healthy state, so on its own it doesn’t “ensure continued operations” — someone would still have to manually act on every alert for a month.

**Exam Trap**

The trap is reaching for custom automation, like a scheduled job, or for observability, like an alert, as if either were a complete fix, when Kubernetes already has a built-in, declarative mechanism purpose-built for “a container that degrades after running for a while and needs a restart.” Any option that adds infrastructure Kubernetes doesn’t require, or that only reports on the problem instead of fixing it, misses what “fewest steps” and “Google-recommended practice” are pointing at here.

**Foundation Concept**

Kubernetes’ self-healing model relies on probes to decide when a container needs to be restarted, rather than requiring external tooling to watch and intervene. A liveness probe is specifically designed for processes that run fine initially but can enter a broken state over time, since it keeps checking the container’s health on an ongoing basis and lets the kubelet act the moment the probe starts failing, with no outside system required.

**Real-World Connection**

A team discovers that one of their services develops a slow memory leak and starts returning errors after running for several hours, with a proper fix still weeks away. Adding a liveness probe against a simple health endpoint lets Kubernetes automatically cycle affected Pods before users are impacted, buying the team time to ship the real fix without anyone having to babysit the cluster or build throwaway automation in the meantime.

**Memory Hook**

“A container that breaks after a while needs a liveness probe, not a babysitter or a timer job.”

**30-Second Exam Takeaway**

When a GKE Pod reliably becomes unhealthy after running for a while and a permanent fix is still some time away, the Google-recommended, fewest-steps answer is almost always an HTTP liveness probe — it lets Kubernetes restart the Pod automatically rather than relying on custom jobs, manual monitoring, or alerts that only report the problem.

**Official References**

[**Kubernetes documentation — Configure Liveness, Readiness and Startup Probes:**](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) Supports: correct-answer mechanism — liveness probes automatically restarting containers that become unhealthy after running for a while

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 3.3, Mitigating incident impact on users):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment — keeping a service operating while a known issue’s root cause is still being resolved

---

## Question 53

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You build and operate client-facing applications on Cloud Run and Cloud Run functions. Your client needs every log to remain available for a full year so they can later import it into their own logging platform, and you must keep required code changes to a minimum. What should you do?

- [ ] A. Modify every Cloud Run image and every Cloud Run function so that it writes logs to both Cloud Logging and the client’s logging service, and open the VPC firewall ports needed to send that traffic
- [ ] B. Create a Pub/Sub topic and subscription along with a logging sink that routes all logs into the topic, then give the client access to the topic so they can pull the logs
- [ ] C. Create a Cloud Storage bucket with the necessary VPC firewall rules, and modify every Cloud Run image and every Cloud Run function so that it writes its logs to a file in that bucket
- [x] D. Create a custom log bucket with its retention set to 365 days, configure a logging sink that routes logs into that bucket, and give the client access to the bucket so they can retrieve the logs

### Explanation

**Correct Answer**

**D. Create a custom log bucket with its retention set to 365 days, configure a logging sink that routes logs into that bucket, and give the client access to the bucket so they can retrieve the logs**

**Exam Reasoning Explanation**

Two hard constraints must be satisfied together: the logs need to stay available for a full year, and the solution can’t require rewriting application code. Walking the chain: requirement (one year of log availability, minimal code changes) → capability (Cloud Run and Cloud Run functions already send stdout/stderr output to Cloud Logging automatically, and a custom log bucket can be set to retain data for exactly 365 days, with a logging sink routing logs into it entirely at the platform level) → elimination (A and C both require touching every service’s code to add new logging destinations, B requires no code changes but can’t retain messages anywhere near a year) → decision (D is the only option where both constraints are met by configuration alone).

**Key Exam Clues**

  * “available for one year” is a hard, specific duration constraint that the chosen storage mechanism must actually be capable of supporting.

  * “MUST minimize required code changes” is a hard constraint that eliminates any option requiring every Cloud Run image and Cloud Run function to be modified.

  * “import the logs into their logging service” signals the client needs read access to a durable store of the log data on their own schedule, not a live push integration into their specific external system.

**Why This Is Correct**

Cloud Run and Cloud Run functions already write anything sent to stdout or stderr into Cloud Logging automatically, with no application code changes required. Creating a custom log bucket, setting its retention to 365 days, and configuring a logging sink to route logs into that bucket all happen at the platform and infrastructure layer, completely outside the application code, so required code changes stay at zero. Granting the client access to the bucket lets them retrieve and import a full year of logs whenever suits their own process, satisfying every stated requirement at once.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement:** modifying every Cloud Run image and every Cloud Run function to add a second logging destination, plus managing the networking that destination needs, requires touching every service’s code and configuration — directly conflicting with the instruction to minimize required code changes.

**Option B — Violates Requirement:** a logging sink into Pub/Sub requires no code changes, but Pub/Sub message retention tops out at 31 days even at its maximum configurable duration, far short of the one year the client needs — logs would be purged from the topic or subscription long before a year’s worth could be imported.

**Option C — Violates Requirement:** having every Cloud Run image and Cloud Run function write its own log file into a storage bucket means rewriting each service’s logging logic from scratch, which is exactly the kind of code change the requirement is trying to avoid, and it ignores that Cloud Logging already captures this output for free.

**Exam Trap**

The trap is treating “minimize code changes” and “available for one year” as separate problems that can be solved independently, when the correct answer has to satisfy both together with a single, code-free configuration. An option that solves one constraint well — no code changes, as with Pub/Sub — but silently fails the other, with retention far short of a year, is just as wrong as an option that nails the retention duration but requires rewriting every service.

**Foundation Concept**

Cloud Logging already captures stdout and stderr output from Cloud Run and Cloud Run functions without any application involvement, and routing and retaining that data is handled entirely through platform configuration — log buckets for storage and retention, and logging sinks for routing logs into a bucket, a Pub/Sub topic, or another destination. Recognizing that the logs already exist in Cloud Logging by default, and that retention and routing are infrastructure concerns rather than application concerns, points directly at a sink-and-bucket solution instead of any approach that touches application code.

**Real-World Connection**

A platform team supporting dozens of Cloud Run services for a client needs to guarantee a year of log history without asking every service owner to change their code. By standing up one custom log bucket with 365-day retention and a single sink that captures logs from all the services, the team meets the requirement with one piece of infrastructure to maintain, and the client simply pulls from that bucket on whatever schedule suits their own import process.

**Memory Hook**

“Logs already flow into Cloud Logging for free — retention and sharing are a bucket-and-sink problem, not a code problem.”

**30-Second Exam Takeaway**

When a question asks for long-term log retention from Cloud Run or Cloud Run functions with minimal code changes, look for a custom log bucket with the needed retention period paired with a logging sink — Cloud Logging already captures the logs automatically, so the work belongs entirely on the infrastructure side.

**Official References**

[**Google Cloud — Configure log buckets:**](https://cloud.google.com/logging/docs/buckets) Supports: correct-answer mechanism — custom log buckets with retention configurable from 1 to 3650 days, routed to by a logging sink

[**Google Cloud — Configure message retention for a Pub/Sub subscription:**](https://cloud.google.com/pubsub/docs/subscription-message-retention) Supports: why Option B fails — Pub/Sub message retention maxes out at 31 days, far short of one year

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 4.2, Managing and analyzing logs):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment — exporting and retaining logs

---

## Question 54

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You want to share a custom Cloud Monitoring dashboard with a partner team. What should you do?

- [ ] A. Send the partner team the dashboard’s URL so they can use it to create their own copy
- [ ] B. Export the underlying metrics to BigQuery, build an equivalent dashboard in Data Studio, and share that new dashboard with the partner team
- [ ] C. Copy the Monitoring Query Language (MQL) query used in the dashboard and send that query to the partner team
- [x] D. Export the dashboard’s JSON definition and send that JSON file to the partner team

### Explanation

**Correct Answer**

**D. Export the dashboard’s JSON definition and send that JSON file to the partner team**

**Exam Reasoning Explanation**

The hard constraint is handing over the complete dashboard — its widgets, queries, and layout — to a team that doesn’t already have standing access to the project that owns it. Walking the chain: requirement (transfer a full, working dashboard to an outside team) → capability (Cloud Monitoring lets you export a dashboard’s entire configuration as JSON, which can be pasted or imported into a new dashboard in another project) → elimination (A assumes access the partner team likely doesn’t have, B rebuilds something different in another tool, C captures only a fragment of the dashboard’s configuration) → decision (D is the one option that transfers the actual, complete dashboard definition).

**Key Exam Clues**

  * “partner team” is a contextual signal suggesting a team outside your project’s existing IAM boundary, which rules out any approach that silently assumes they already have, or should be given, direct access to your project.

  * “share a Cloud Monitoring custom dashboard” — not “share the underlying metrics” or “build a new reporting view” — is a hard constraint: the goal is to hand over the dashboard itself, not a subset of it or a reimplementation elsewhere.

  * The option describing a “JSON definition” lines up directly with Cloud Monitoring’s own documented export/import mechanism for moving a dashboard between projects.

**Why This Is Correct**

Cloud Monitoring custom dashboards can be exported as a complete JSON definition that captures every widget, query, and layout choice in the dashboard. Sending that JSON file to the partner team lets them paste or import it into a new dashboard in their own project, recreating the exact same dashboard without requiring you to grant them IAM access to your project or rebuild anything by hand. This matches Google’s documented path for moving a dashboard from one project to another.

**Why the Other Options Are Not the Best Fit**

**Option A — Incorrect:** a raw dashboard URL only works for someone who already has viewing permissions on the project that owns the dashboard. A partner team on a different project typically doesn’t have that access, and simply sending a link neither grants it nor otherwise lets them create their own copy.

**Option B — Technically Possible but Not Best:** exporting metrics to BigQuery and rebuilding the visualization in Data Studio produces a different artifact, not the original dashboard, and introduces considerably more setup — a metrics export pipeline plus a report built from scratch — than the task of sharing an existing dashboard calls for.

**Option C — Incorrect:** a custom dashboard is typically made up of multiple widgets, each with its own query, layout, and formatting. Copying a single MQL query only captures a fragment of that configuration and loses everything else that makes up the dashboard.

**Exam Trap**

The trap is treating “sharing a dashboard” as equivalent to “sharing a link,” the way you might with a typical collaborative document, when Cloud Monitoring dashboards are scoped to a project and governed by that project’s IAM. The documented way to hand a dashboard’s actual configuration to someone outside that boundary is to export its definition, not merely point them at its URL.

**Foundation Concept**

A Cloud Monitoring custom dashboard is a saved configuration — widgets, queries, layout — rather than a dataset. Moving that configuration to a different project is a configuration-transfer problem, which Cloud Monitoring solves by letting you export and import the dashboard’s JSON definition, rather than an access-control or data-export problem, which is what granting a URL or standing up a parallel reporting pipeline would actually solve.

**Real-World Connection**

A platform team wants a partner team in a separate Google Cloud project to use the same on-call dashboard they rely on. Rather than granting the partner team IAM access into their project, they export the dashboard’s JSON and send the file over; the partner team pastes it into a new dashboard in their own project, and from then on each team can independently customize, filter, or extend its own copy using data scoped to its own project.

**Memory Hook**

“A dashboard is configuration, not a link — export the JSON to hand someone their own copy.”

**30-Second Exam Takeaway**

When a question asks how to share a Cloud Monitoring custom dashboard with a team outside your project, think export/import of the dashboard’s JSON definition — that’s the one option that transfers the complete, original configuration without requiring cross-project IAM access or rebuilding it elsewhere.

**Official References**

[**Google Cloud — Create and manage custom dashboards:**](https://cloud.google.com/monitoring/charts/dashboards) Supports: correct-answer mechanism — exporting a dashboard’s JSON and pasting/importing it into a new dashboard in another project

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 4.3, Managing metrics, dashboards, and alerts):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment — managing dashboards, including sharing

---

## Question 55

*Domain 3: Applying Site Reliability Engineering Practices*

Your team is building a service that runs compute-intensive processing on batches of data, where processing speed depends directly on the number and speed of CPUs available. These batches vary in size and can arrive at any time from several third-party sources, which need a secure way to upload their data. You want to keep costs as low as possible while still processing each batch as quickly as possible. What should you do?

- [ ] A. Stand up a secure file transfer protocol (SFTP) server on a Compute Engine instance for third parties to upload their batches to, and issue them the appropriate credentials. Create a Cloud Run function with a Cloud Storage trigger on the object-finalized event, and have that function scale up a Compute Engine autoscaling managed instance group. Use an instance image pre-loaded with the processing software that terminates its instances once processing finishes.
- [ ] B. Provide a Cloud Storage bucket for third parties to upload their batches to, with Identity and Access Management (IAM) access granted appropriately. Run a Standard Google Kubernetes Engine (GKE) cluster with two services: one that processes the batches and another that watches Cloud Storage for new batches. Stop the processing service whenever there are no batches left to process.
- [x] C. Provide a Cloud Storage bucket for third parties to upload their batches to, with Identity and Access Management (IAM) access granted appropriately. Create a Cloud Run function with a Cloud Storage trigger on the object-finalized event, and have that function scale up a Compute Engine autoscaling managed instance group. Use an instance image pre-loaded with the processing software that terminates its instances once processing finishes.
- [ ] D. Provide a Cloud Storage bucket for third parties to upload their batches to, with Identity and Access Management (IAM) access granted appropriately. Use Cloud Monitoring to detect new batches landing in the bucket and have it trigger a Cloud Run function that processes the data directly. Configure that Cloud Run function to use the largest available CPU allocation to minimize its runtime.

### Explanation

**Correct Answer**

**C. Provide a Cloud Storage bucket for third parties to upload their batches to, with Identity and Access Management (IAM) access granted appropriately. Create a Cloud Run function with a Cloud Storage trigger on the object-finalized event, and have that function scale up a Compute Engine autoscaling managed instance group. Use an instance image pre-loaded with the processing software that terminates its instances once processing finishes.**

**Exam Reasoning Explanation**

The must-have constraints are a secure, low-overhead upload path for outside parties, processing that scales with CPU count and speed, triggering that reacts instantly to unpredictable arrivals, and compute that doesn’t cost anything once the work is done. Walking the chain: requirement (secure upload + CPU-scalable processing + fast reaction + minimal cost) → capability (Cloud Storage with IAM gives secure, serverless uploads; an object-finalized trigger reacts the instant a batch lands; a Compute Engine autoscaling group lets the heavy lifting run on machines sized for real CPU needs; a self-terminating image stops billing once processing ends) → elimination (A adds an unnecessary self-managed SFTP server, B keeps a cluster and a polling service running even when idle, D does the heavy compute inside a resource-capped function and detects uploads indirectly through Monitoring) → decision (C is the only path where every piece matches a stated requirement without adding overhead the scenario didn’t ask for).

**Key Exam Clues**

  * “processed faster based on the speed and number of CPUs” is a technical signal that the heavy computation needs to run on infrastructure you can size with CPUs, not inside a resource-capped serverless function.

  * “vary in size and may arrive at any time” favors an event-driven trigger that reacts the instant a batch appears, over a scheduled or polling-based detection mechanism.

  * “upload their data securely” points toward a native, access-controlled Google Cloud storage destination rather than a self-managed server that has to be secured and maintained.

  * “minimize costs, while... processed as quickly as possible” is a dual constraint requiring both an instant trigger and compute that doesn’t sit running, or idle, once the work is finished.

**Why This Is Correct**

A Cloud Storage bucket with IAM gives third parties a secure, access-controlled upload destination with nothing to patch or operate. The object-finalized Cloud Storage trigger fires a lightweight Cloud Run function the instant an upload completes, with no polling delay, and that function’s only job is to scale up a Compute Engine autoscaling managed instance group — handing the actual compute-heavy work to machines that can be sized with as many, or as fast, CPUs as the workload needs. Because the instance image is pre-loaded with the processing software and configured to terminate once processing completes, the project pays for compute only while a batch is actively being processed, which minimizes cost while keeping the time from “upload finishes” to “processing starts” as short as possible.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** standing up a self-managed SFTP server on a Compute Engine instance means an always-running machine that has to be secured, patched, and paid for continuously, when Cloud Storage with IAM already provides a secure, serverless upload path at lower operational cost and overhead — the rest of the path is identical to the correct answer, so this is purely a worse choice for the upload step.

**Option B — Technically Possible but Not Best:** a Standard GKE cluster running two always-on services — one processing, one watching Cloud Storage — keeps compute (and a polling loop) running even when there’s nothing to process. Stopping the processing service when idle still requires something to be continuously watching and deciding that, which is less efficient and less immediate than a native, push-based event trigger, and it doesn’t scale compute to match genuinely CPU-heavy, variable-sized batches the way a right-sized Compute Engine group can.

**Option D — Violates Requirement:** performing the compute-heavy processing inside the Cloud Run function itself, even with its largest CPU setting, ignores the stated requirement that speed depends on “the number and speed of CPUs on the machine” — serverless functions have bounded CPU and memory ceilings well below what a purpose-sized Compute Engine machine can offer. Using Cloud Monitoring to detect new uploads is also an indirect, less immediate substitute for the native Cloud Storage event trigger used in the correct path.

**Exam Trap**

The trap is assuming any combination of a Cloud Storage bucket with a Cloud Run function is equally good, without checking where the actual heavy computation happens. A function that does the processing itself — even dialed up to its largest CPU allocation — is still bounded by serverless compute ceilings, so it fails a requirement explicitly tied to CPU count and speed. The correct pattern uses the function only as a lightweight trigger that hands off to appropriately sized Compute Engine capacity, never as the processor itself.

**Foundation Concept**

Event-driven architectures separate “detecting that work has arrived” from “doing the work.” A lightweight, serverless function is well suited to the first job — reacting instantly to a storage event — but a compute-heavy workload belongs on infrastructure that can be sized to the job and that scales down to zero cost once the job is done, which is exactly what an autoscaling managed instance group paired with a self-terminating image provides.

**Real-World Connection**

A media-processing service lets outside partners drop large video files into a Cloud Storage bucket; the moment an upload finishes, a lightweight Cloud Run function fires and resizes a Compute Engine instance group to match the batch, with each VM pre-loaded to start transcoding immediately and shut itself down once its job is done. Partners get a simple, secure upload target, transcoding starts within seconds of the upload completing rather than on the next polling cycle, and the team’s bill reflects only the minutes of actual transcoding rather than a cluster or server running around the clock.

**Memory Hook**

“Let the trigger be tiny; let the compute be big — and let the big compute turn itself off.”

**30-Second Exam Takeaway**

For compute-heavy, event-driven batch work with unpredictable arrival, look for the pattern of a lightweight serverless trigger (never doing the heavy lifting itself) handing off to right-sized, autoscaling Compute Engine capacity that terminates when finished — that combination is what actually minimizes processing latency and cost together.

**Official References**

[**Google Cloud — Cloud Storage triggers for Cloud Run functions:**](https://cloud.google.com/functions/docs/calling/storage)Supports: correct-answer mechanism — reacting to the object-finalized event the instant an upload completes

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 3.2, Managing service lifecycle):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment — autoscaling with managed instance groups as part of service lifecycle management

---

## Question 56

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

Your company’s security team needs read-only access to your Google Cloud project’s Data Access audit logs. You want to grant that access following the principle of least privilege and Google-recommended practices. What should you do?

- [ ] A. Grant the roles/logging.viewer role to each individual member of the security team
- [ ] B. Grant the roles/logging.viewer role to a group that contains the security team’s members
- [ ] C. Grant the roles/logging.privateLogViewer role to each individual member of the security team
- [x] D. Grant the roles/logging.privateLogViewer role to a group that contains the security team’s members

### Explanation

**Correct Answer**

**D. Grant the roles/logging.privateLogViewer role to a group that contains the security team’s members**

**Exam Reasoning Explanation**

Two hard constraints have to be satisfied together: the role itself must actually include permission to view Data Access audit logs, and the assignment method must follow Google’s documented IAM guidance. Walking the chain: requirement (read-only access to Data Access audit logs, granted the recommended way) → capability (Private Logs Viewer specifically includes Data Access audit log read permission, and Google explicitly recommends binding roles to groups rather than individuals) → elimination (A and B both use a role that can’t see Data Access audit logs regardless of assignment method, C uses the right role but the wrong assignment method) → decision (D is the only option where both the role and the assignment method match what’s required).

**Key Exam Clues**

  * “read-only access to... Data Access audit logs” is a hard, specific technical signal: the standard Logs Viewer role does not include Data Access audit log visibility, so the role choice itself is what’s being tested.

  * “principle of least privilege” favors the role that grants exactly the read access needed for the required log categories, no more and no less.

  * “Google-recommended practices” is an exclusion cue pointing toward granting the role to a group rather than to individual accounts, which is Google’s documented IAM guidance for managing access at scale.

**Why This Is Correct**

The Logs Viewer role doesn’t include permission to view Data Access audit logs; only the Private Logs Viewer role includes that permission, in addition to everything Logs Viewer already grants, so it’s the only role of the two that actually satisfies “read-only access to Data Access audit logs.” Google’s own IAM security guidance separately recommends granting roles to groups rather than to individual users, because updating a group’s membership is simpler and less error-prone than updating many individual policy bindings. Granting Private Logs Viewer to a group containing the security team satisfies both the specific permission requirement and the recommended management practice at the same time.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement:** Logs Viewer doesn’t grant visibility into Data Access audit logs regardless of who it’s assigned to, so this fails the core access requirement outright, independent of the assignment method.

**Option B — Violates Requirement:** using a group is the right practice, but Logs Viewer still can’t surface Data Access audit logs, so the fundamental permission gap remains even with the correct assignment approach.

**Option C — Technically Possible but Not Best:** Private Logs Viewer is the correct role and does grant the needed access, but assigning it to each team member individually works against Google’s own guidance to manage access through groups, making it harder to onboard, offboard, or audit the team’s access over time.

**Exam Trap**

The trap is assuming Logs Viewer is “enough” because it’s the more commonly used, general-purpose log-access role — Data Access audit logs are deliberately walled off behind the more privileged Private Logs Viewer role because they can reveal sensitive details about who accessed what data, so a plain Viewer role is insufficient no matter how it’s assigned.

**Foundation Concept**

Cloud Logging separates general log visibility from visibility into more sensitive audit log categories. Private Logs Viewer is effectively a superset of Logs Viewer that adds the ability to see Data Access and other sensitive audit log entries, reflecting the principle that broader visibility into who accessed what data should require a deliberately broader grant. Separately, in IAM generally, roles are meant to be bound to groups rather than individuals so that access reviews, onboarding, and offboarding happen by managing group membership rather than editing a resource’s IAM policy every time someone joins or leaves a team.

**Real-World Connection**

A security team needs to review who accessed sensitive customer records, which only appears in Data Access audit logs. Granting Private Logs Viewer to a dedicated security-team Google group lets every analyst query those logs immediately, and when someone joins or leaves the team, an administrator only has to update the group’s membership rather than hunting down and editing IAM bindings tied to that person across every project.

**Memory Hook**

“Data Access logs need the ‘Private’ role; access for a team needs a group, not a list of names.”

**30-Second Exam Takeaway**

When a question asks for read-only access to Data Access audit logs, reach for Private Logs Viewer rather than Logs Viewer, and when it’s for a team, grant that role to a group rather than to each person individually — both are explicit, documented Google-recommended practices.

**Official References**

[**Google Cloud — Cloud Audit Logs overview:**](https://cloud.google.com/logging/docs/audit) Supports: correct-answer mechanism — Private Logs Viewer versus Logs Viewer and which role is required to read Data Access audit logs

[**Google Cloud — Use IAM securely:**](https://cloud.google.com/iam/docs/using-iam-securely) Supports: Google-recommended practice of granting roles to groups rather than individual users

[Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 1.1, Designing the overall resource hierarchy for an organization): ](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment — IAM roles and organization-level policies

---

## Question 57

*Domain 3: Applying Site Reliability Engineering Practices*

You’ve deployed a stateless application, running as multiple pods at once, on a large Standard Google Kubernetes Engine (GKE) cluster. Traffic to the application is unpredictable, and you need the user experience to stay consistent through those traffic swings while also keeping the cluster’s resource usage efficient. What should you do?

- [ ] A. Set up a cron job that scales the deployment on a fixed schedule
- [x] B. Set up a Horizontal Pod Autoscaler for the deployment
- [ ] C. Set up a Vertical Pod Autoscaler for the deployment
- [ ] D. Enable cluster autoscaling on the node pool

### Explanation

**Correct Answer**

**B. Set up a Horizontal Pod Autoscaler for the deployment**

**Exam Reasoning Explanation**

The must-have constraint is that the mechanism has to react to actual, unpredictable traffic in real time, while also avoiding wasted capacity — a schedule-based or slow-to-react approach fails the first half, and anything that doesn’t change how much capacity is actually running fails the second. Walking the chain: requirement (keep performance steady under unpredictable load while staying resource-efficient) → capability (the Horizontal Pod Autoscaler continuously tracks live demand signals and adjusts replica count to match) → elimination (A follows a fixed schedule unrelated to real traffic, C reacts too slowly and disruptively for inconsistent load, D only reacts to pod-scheduling pressure that something else has to create first) → decision (B is the single mechanism that directly and continuously ties pod capacity to actual demand).

**Key Exam Clues**

  * “inconsistent traffic” is a hard constraint that rules out any schedule-based approach, since a fixed timetable can’t track unpredictable demand.

  * “stateless... multiple pods run at the same time” is a technical signal that the workload is naturally suited to horizontal (replica-count) scaling rather than resizing individual pods.

  * “user experience... stay consistent” paired with “resource usage... efficient” is a dual requirement: the right mechanism must add capacity under load and shed it when load drops, in the same motion.

**Why This Is Correct**

The Horizontal Pod Autoscaler watches real-time signals such as CPU or memory utilization, or custom and external metrics tied to actual demand like request rate, and adjusts the deployment’s pod replica count accordingly. Adding pods as traffic rises keeps response times and throughput steady for users, while removing pods as traffic falls stops the deployment from holding capacity it no longer needs. Because this responds continuously to the live traffic pattern rather than a predetermined timetable, and operates at exactly the layer that fits a stateless, horizontally scalable application, it’s the mechanism built for this combination of unpredictable load and resource efficiency.

**Why the Other Options Are Not the Best Fit**

**Option A — Incorrect:** a cron job scales on a fixed schedule, which has no way to track traffic that is genuinely inconsistent; the deployment could easily be over-provisioned during a scheduled-up window with little actual demand, or under-provisioned during a scheduled-down window that happens to see a spike, directly undermining a consistent user experience.

**Option C — Different Use Case:** the Vertical Pod Autoscaler adjusts a pod’s own CPU and memory requests and limits based on observed usage over time, which suits workloads with predictable, steadily trending resource needs rather than fast, unpredictable swings. Applying a new recommendation typically requires evicting and recreating the pod, so it reacts too slowly and disruptively for inconsistent traffic, and Google’s own guidance cautions against running it together with the Horizontal Pod Autoscaler on the same resource dimension.

**Option D — Technically Possible but Not Best:** cluster autoscaling adds or removes nodes in response to pods that can’t be scheduled due to insufficient node capacity, which is a valuable complement once something else is changing how many pods need to run. On its own, with a fixed pod count, it has nothing to react to as traffic changes, so by itself it cannot keep the user experience consistent as load fluctuates.

**Exam Trap**

The trap is reading “optimize cluster resource usage” as a cue to reach for cluster-level autoscaling (option D) rather than recognizing that right-sizing the pod replica count is itself what prevents wasted resources at this layer — cluster autoscaling only has something to act on once pod-level scaling, like the Horizontal Pod Autoscaler, changes the demand for nodes. If the scenario instead described pods failing to schedule because a fixed replica count occasionally can’t fit on the available nodes, cluster autoscaling would become directly relevant in its own right.

**Foundation Concept**

Kubernetes offers scaling at different layers for different needs: horizontal scaling changes how many replicas of a stateless workload are running to track changing demand, vertical scaling changes how much CPU and memory a single pod is allocated to match its own resource profile, and cluster-level scaling changes how many nodes exist to host whatever pods are currently scheduled. A stateless application facing unpredictable traffic is the textbook case for horizontal scaling, because adding and removing identical replicas is faster and safer than resizing or rescheduling individual pods.

**Real-World Connection**

A retail team’s stateless checkout service sees large, unpredictable traffic swings around promotions and social-media mentions. Configuring a Horizontal Pod Autoscaler against request-based metrics lets the deployment automatically grow from a handful of replicas to dozens during a surge and shrink back afterward, keeping checkout latency steady for shoppers during the spike while freeing up capacity, and the cost that comes with it, once traffic subsides — without anyone having to predict the next surge in advance.

**Memory Hook**

“Unpredictable traffic, stateless pods: scale the replica count, not the schedule or the pod’s own size.”

**30-Second Exam Takeaway**

When a stateless, horizontally scalable GKE workload faces unpredictable traffic and the goal is both consistent performance and efficient resource use, reach for the Horizontal Pod Autoscaler first — it’s the mechanism built to react to live demand at the replica-count layer, with the Vertical Pod Autoscaler and cluster autoscaling serving more specialized or complementary roles.

**Official References**

[**Google Cloud — Horizontal Pod autoscaling in GKE:**](https://cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) Supports: correct-answer mechanism — reacting to real-time resource/demand signals by adjusting replica count, and why it isn’t combined with VPA on the same resource dimension

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 3.2, Managing service lifecycle):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment — autoscaling (including GKE) as part of service lifecycle management

---

## Question 58

*Domain 5: Optimizing Performance and Cost*

Your organization runs a monolithic application on Compute Engine, and you need to choose a machine type that optimizes CPU utilization, basing that choice on historical system metrics and reaching it in as few steps as possible. You want to follow Google-recommended practices. What should you do?

- [x] A. Query the Recommender API for the VM’s machine type recommendation and apply what it suggests
- [ ] B. Set up an Agent Policy that automatically installs the Ops Agent on every VM
- [ ] C. Manually install the Ops Agent across the fleet of VMs using the gcloud CLI
- [ ] D. Inspect the VM’s Cloud Monitoring dashboard yourself and pick a machine type based on its lowest observed CPU utilization

### Explanation

**Correct Answer**

**A. Query the Recommender API for the VM’s machine type recommendation and apply what it suggests**

**Exam Reasoning Explanation**

The must-have constraints are using historical metrics, reaching a decision in the fewest steps, and following Google-recommended practice — all three have to be satisfied together, not traded off against each other. Walking the chain: requirement (pick an optimal machine type from historical CPU data with minimal effort) → capability (the VM instance rightsizing recommender already monitors CPU and memory utilization automatically and surfaces a ready-to-apply suggestion through the Recommender API) → elimination (B and C both add agent-installation steps that aren’t required for a base CPU recommendation, D substitutes manual review and judgment for an automated calculation) → decision (A is the single call that goes directly from existing historical data to an actionable recommendation).

**Key Exam Clues**

  * “fewest number of steps” is a hard constraint that rules out any option requiring setup or configuration work before a recommendation exists.

  * “historical system metrics” is a technical signal pointing to a feature that already analyzes a window of past utilization automatically, rather than one requiring manual interpretation.

  * “follow Google-recommended practices” is an exclusion cue favoring the documented, purpose-built mechanism over an ad hoc or tangential configuration task.

**Why This Is Correct**

The VM instance rightsizing recommender, accessed through the Recommender API, automatically monitors a Compute Engine instance’s CPU and memory utilization over the trailing eight days and produces a specific, ready-to-apply recommendation for a better-fitting machine type — no manual configuration or agent installation is required to get this CPU-based recommendation, since Compute Engine already collects the underlying utilization data by default. Querying the Recommender API and applying its suggestion is the single, documented, lowest-step path from historical metrics to a chosen machine type, satisfying every constraint in the scenario at once.

**Why the Other Options Are Not the Best Fit**

**Option B — Technically Possible but Not Best:** an Agent Policy that installs the Ops Agent fleet-wide can improve recommendation accuracy or provide richer guest-level telemetry, but it’s an optional enhancement rather than a prerequisite for a base CPU-utilization recommendation, and it adds setup steps the scenario explicitly asks to avoid.

**Option C — Technically Possible but Not Best:** manually installing the Ops Agent through the gcloud CLI has the same issue as B — it’s an extra configuration step that doesn’t by itself identify a machine type, and it isn’t necessary for CPU-based rightsizing, which Compute Engine already monitors without it.

**Option D — Violates Requirement:** manually reviewing a dashboard and selecting a machine type by eye is a multi-step, subjective process rather than Google’s documented, repeatable mechanism, and it substitutes a vague heuristic (“lowest observed CPU utilization”) for the recommender’s actual sizing calculation — which can lead to choosing a machine type that doesn’t actually fit the workload.

**Exam Trap**

The trap is assuming that better recommendations must start with manually installing an agent, since Compute Engine already collects the CPU (and memory) utilization used for rightsizing by default — the Ops Agent steps look relevant but are an unnecessary detour for this specific, already-available CPU-based recommendation. If the scenario instead needed more granular guest-OS or application-level metrics to sharpen a memory-based recommendation, installing the Ops Agent would become a genuinely necessary step.

**Foundation Concept**

Google Cloud’s Active Assist recommenders continuously analyze operational telemetry Google already collects and turn it into specific, actionable suggestions exposed through the Recommender API, console, or gcloud CLI, removing the need for an operator to manually collect, graph, and interpret metrics before making an infrastructure decision. Recognizing that a recommender already exists for a given optimization goal is usually the fastest, most Google-aligned path, compared to building the same analysis by hand.

**Real-World Connection**

A platform team managing hundreds of Compute Engine VMs across a global organization uses the VM instance rightsizing recommender to surface overprovisioned and underprovisioned machines automatically, instead of having an engineer manually chart CPU usage for each VM. Applying the suggested machine type changes directly from the recommendation reduces wasted spend on oversized VMs and protects performance on undersized ones, without a separate metrics-collection effort to design and maintain.

**Memory Hook**

“Before you build your own dashboard-and-judgment process, check whether a recommender already does the sizing for you.”

**30-Second Exam Takeaway**

When a question asks for the fastest, Google-recommended way to pick a resource size or configuration based on data Google already collects, look first for the matching Active Assist recommender exposed through the Recommender API, rather than agent installation or manual dashboard analysis.

**Official References**

[**Google Cloud — Apply machine type recommendations to VM instances (VM instance rightsizing recommender):**](https://cloud.google.com/recommender/docs/vm-instance-rightsizing-recommender) Supports: correct-answer mechanism — automatic CPU/memory utilization analysis over the trailing 8 days and ready-to-apply recommendations via the Recommender API

[**Google Cloud — Professional Cloud DevOps Engineer exam guide (Section 5.1, Collecting performance information in Google Cloud):**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment — Active Assist insights and recommendations

---

## Question 59

*Domain 2: Building and Implementing CI/CD Pipelines*

You’re building the CI/CD pipeline for an application on Google Kubernetes Engine (GKE), deployed with a Kubernetes Deployment, Service, and Ingress. The application team has asked for blue/green deployments, and you now need to implement the rollback step. What should you do?

- [ ] A. Run kubectl rollout undo
- [ ] B. Delete the new container image and delete its running Pods
- [x] C. Update the Kubernetes Service’s selector to point back at the previous Deployment
- [ ] D. Scale the new Kubernetes Deployment down to zero replicas

### Explanation

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

---

## Question 60

*Domain 2: Building and Implementing CI/CD Pipelines*

You’re building a Cloud Run application that needs an API key to call a third-party API, and you want to store and use that key securely, following Google-recommended practices. What should you do?

- [x] A. Store the API key as a secret in Secret Manager, and expose that secret to the Cloud Run service as an environment variable
- [ ] B. Store the API key as a secret in Secret Manager, mount it as a file under a custom directory, and have the application decrypt it before use
- [ ] C. Store the API key as a key in Cloud Key Management Service (Cloud KMS), and expose it to the Cloud Run service as an environment variable
- [ ] D. Encrypt the API key with Cloud Key Management Service (Cloud KMS), pass the resulting ciphertext to Cloud Run as an environment variable, and have the application decrypt it before use

### Explanation

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

---
