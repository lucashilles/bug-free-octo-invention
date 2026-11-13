# Professional Cloud DevOps Engineer — Practice Exam 3

60 questions.

## Question 1

*Domain 2: Building and Implementing CI/CD Pipelines*

You have configured a Cloud Build pipeline to deploy Terraform configurations maintained in a GitHub repository. Developers work in short-lived branches and occasionally create tags during development. When a release is ready for deployment, you assign it a semantic version tag. You need the pipeline to apply the Terraform configuration whenever a new release becomes available, while minimizing operational overhead. What should you do?

- [x] A. Configure a Cloud Build trigger for tag pushes matching `\d+\.\d+\.\d+`.
- [ ] B. Configure a Cloud Build trigger for branch pushes matching `\d+\.\d+\.\d+`.
- [ ] C. Configure a Cloud Build trigger for tag pushes matching `.*`.
- [ ] D. Configure a Cloud Build trigger for branch pushes matching `.*`.

### Explanation

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

---

## Question 2

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your team is deploying an application on Google Kubernetes Engine (GKE) that handles personally identifiable information (PII). You must collect the application’s logs in Cloud Logging while preventing sensitive user data from being exposed in those logs. What should you do?

- [ ] A. Apply log sampling to reduce the number of application log entries collected.
- [x] B. Use Sensitive Data Protection to inspect log entries in real time and redact PII before storing them in Cloud Logging.
- [ ] C. Turn off Cloud Logging for the application to prevent sensitive information from being collected.
- [ ] D. Retain all application logs in an encrypted Cloud Storage bucket with restricted access.

### Explanation

**Correct Answer**

**B. Use Sensitive Data Protection to inspect log entries in real time and redact PII before storing them in Cloud Logging.**

**Exam Reasoning Explanation**

Two requirements must be satisfied together: retain application logging and protect sensitive content. Redaction addresses the content while preserving useful diagnostic information. Sampling reduces volume, disabling logging removes observability, and encrypted storage does not remove sensitive values.

**Key Exam Clues**

  * **“Collect the application’s logs in Cloud Logging” — Hard constraint:** Logging must remain enabled, with Cloud Logging as the destination.

  * **“Preventing sensitive user data from being exposed” — Hard constraint:** Protection must address the information contained in log entries.

  * **“Personally identifiable information” — Technical signal:** Sensitive-data detection and de-identification are relevant capabilities.

**Why This Is Correct**

Sensitive Data Protection supports synchronous content de-identification through the DLP API. Configure the relevant information types and redaction transformations, then send the sanitized content to Cloud Logging. Its text-redaction functionality can replace detected sensitive values with placeholders. 

**Implementation boundary:** This requires integration into the application’s logging path or a preprocessing component. Enabling Sensitive Data Protection alone does not sanitize GKE logs. GKE’s default logging agent collects application output, so redaction must occur before unsanitized content reaches that collection path. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Different Use Case:** Sampling selects a subset of log entries to control volume. Retained entries can still contain PII because sampling does not redact their contents.

  * **Option C — Violates Requirement:** Disabling application log collection conflicts with the requirement to collect those logs in Cloud Logging. It also removes diagnostic evidence without changing what the application writes locally.

  * **Option D — Violates Requirement:** This substitutes Cloud Storage for the required logging destination and retains the sensitive content. Encryption and restricted access protect stored data, but authorized readers still receive decrypted content. 

**Exam Trap**

Do not confuse encryption with redaction. Encryption protects stored information from unauthorized access; redaction removes sensitive values from the content that log readers receive.

Also, interpret B as a preprocessing integration—not an automatic Cloud Logging redaction setting.

**Foundation Concept**

Privacy-preserving logging combines data minimization, sanitization, and access control. Avoid recording unnecessary personal information, redact sensitive content that must pass through the logging path, and restrict access to the resulting logs. Detection rules must cover the application’s actual sensitive-data types.

**Real-World Connection**

An application logger can sanitize a message containing a customer’s email address before writing it to standard output. GKE then forwards the sanitized entry to Cloud Logging, preserving request status and diagnostic context while keeping the original address out of the stored message.

**Memory Hook**

To retain useful logs without exposing PII, sanitize sensitive content before ingestion.

**30-Second Exam Takeaway**

When a question requires both logging and PII protection, select content redaction before storage. Sampling, disabling collection, and encryption each address a different concern.

**Official References**

  * [**Google Cloud — Redacting sensitive data from text**](https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data)

Supports: Sensitive Data Protection redaction, information-type configuration, and replacement of detected values.

  * [**Google Cloud — About GKE logs**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs)

Supports: Application log collection, the default logging agent, and the need to sanitize content before collection.

  * [**Google Cloud — Logging query language**](https://docs.cloud.google.com/logging/docs/view/logging-query-language)

Supports: Sampling selects a fraction of log entries rather than redacting sensitive fields.

  * [**Google Cloud — Standard Cloud Storage encryption**](https://docs.cloud.google.com/storage/docs/encryption/default-keys)

Supports: Encryption at rest and automatic decryption for authorized readers.

---

## Question 3

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your team is preparing to release a new API on Cloud Run. The application uses an OpenTelemetry agent to export distributed traces to Cloud Trace for analyzing request latency. However, trace collection has been inconsistent. Which configuration change should you make to address this issue?

- [ ] A. Configure an HTTP health check for the Cloud Run service.
- [x] B. Enable instance-based billing to allocate CPU throughout each instance’s lifetime.
- [ ] C. Increase the Cloud Run service’s CPU limit from 2 vCPUs to 4 vCPUs.
- [ ] D. Enable request-based billing to allocate CPU only during request processing.

### Explanation

**Correct Answer**

**B. Enable instance-based billing to allocate CPU throughout each instance’s lifetime.**

**Exam Reasoning Explanation**

The relevant distinction is when the tracing agent can execute. OpenTelemetry can perform background work after an HTTP response has been returned. Request-based CPU allocation can interrupt that work, making instance-based billing the best configuration among the options. Google explicitly identifies OpenTelemetry agents as a background-processing use case.

**Key Exam Clues**

  * **“Cloud Run” — Technical signal:** CPU availability depends on the service’s billing configuration.

  * **“OpenTelemetry agent” — Technical signal:** Telemetry processing can require background execution.

  * **“Trace collection has been inconsistent” — Problem signal:** Investigate the agent’s execution conditions before increasing processing capacity.

**Why This Is Correct**

Instance-based billing keeps CPU allocated throughout the container instance’s lifecycle, including periods without active requests. This allows the agent’s background processing and trace exports to continue after responses finish.

This setting was previously called **CPU always allocated** ; instance-based billing is the current terminology. It does not prevent autoscaling or instance termination, so normal shutdown handling remains necessary. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Different Use Case:** HTTP health checks assess whether an instance can start, serve traffic, or needs restarting. They do not directly resolve background trace-export execution. They would fit a container-health problem.

  * **Option C — Technically Possible but Not Best:** Additional vCPUs can help CPU-bound workloads, but increasing capacity does not change when CPU is available. The scenario provides no evidence of CPU saturation. 

  * **Option D — Different Use Case:** Request-based billing suits work completed within request handling. After a response, CPU access can be disabled or severely limited, which can suspend the agent’s background activity. 

**Exam Trap**

Do not confuse **CPU capacity** with **CPU availability**. Increasing the CPU limit cannot compensate for CPU being unavailable between requests. If the diagnosed problem were sustained CPU saturation, increasing vCPUs could be appropriate.

**Foundation Concept**

A serverless execution environment can keep a container in memory while restricting its ability to execute background code. Any asynchronous work that continues after the response must be compatible with that execution model. Cloud Run recommends instance-based billing for background activity. 

**Real-World Connection**

After an API response completes, the tracing agent might still need to export telemetry. Keeping CPU available lets that work proceed between requests. Evaluate the billing impact because instances are charged throughout their lifetimes, including idle periods. 

**Memory Hook**

For Cloud Run agents that work after responses, keep CPU available between requests.

**30-Second Exam Takeaway**

Cloud Run plus background OpenTelemetry processing points to instance-based billing, formerly CPU always allocated. Choose more vCPUs when evidence identifies a capacity bottleneck.

**Official References**

  * [**Google Cloud — Billing settings for services**](https://docs.cloud.google.com/run/docs/configuring/billing-settings)

Supports: Current terminology, CPU allocation behavior, billing implications, and OpenTelemetry background execution.

  * [**Google Cloud — General development tips**](https://docs.cloud.google.com/run/docs/tips/general)

Supports: Background activity restrictions under request-based billing and the recommended configuration.

  * [**Google Cloud — Container runtime contract**](https://docs.cloud.google.com/run/docs/container-contract)

Supports: The distinction between configured CPU capacity and CPU allocation timing.

  * [**Google Cloud — Configure container health checks for services**](https://docs.cloud.google.com/run/docs/configuring/healthchecks)

Supports: Health-check purposes and why option A addresses a different concern.

---

## Question 4

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

Your company handles highly sensitive user information. You are designing Google Kubernetes Engine (GKE) infrastructure to host several applications in development and production environments. The architecture must prevent unauthorized access to data between applications while keeping administrative overhead low. Which design should you choose?

- [ ] A. Deploy a single organization-wide cluster, with a separate namespace for each application and environment combination.
- [ ] B. Deploy a dedicated cluster for each application, with separate namespaces for its development and production workloads.
- [x] C. Deploy a separate cluster for each environment, with each application assigned its own namespace within that cluster.
- [ ] D. Deploy a single organization-wide cluster, with a separate namespace for each application.

### Explanation

**Correct Answer**

**C. Deploy a separate cluster for each environment, with each application assigned its own namespace within that cluster.**

**Exam Reasoning Explanation**

Balance environment separation with manageable application isolation. Separate clusters keep development and production apart, while application namespaces avoid the administrative burden of maintaining a cluster for every application. This combines Google’s recommendation to separate environment clusters with its namespace-based enterprise multi-tenancy model.

**Key Exam Clues**

  * **“Highly sensitive user information” — Hard constraint:** The design must support enforced access boundaries.

  * **“Development and production environments” — Technical signal:** These environments warrant separate operational and security controls.

  * **“Between applications” — Hard constraint:** Applications need individually scoped access policies.

  * **“Administrative overhead low” — Preference:** Avoid unnecessary proliferation of clusters.

**Why This Is Correct**

Separate development and production clusters allow independent cluster configuration and administration. Within each cluster, namespaces provide scopes for application-specific permissions and policies, reducing the number of clusters to manage. 

**Namespaces alone do not prevent unauthorized access.** Enforce least-privilege Kubernetes RBAC and network policies, and restrict application permissions to underlying data. By default, Pods can communicate across namespaces; network policies must explicitly restrict unwanted traffic. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** Separate namespaces can support application and environment policies, but development and production still share a control plane and cluster-wide components. This provides less environment separation than the recommended layout. 

  * **Option B — Technically Possible but Not Best:** Dedicated application clusters provide stronger separation between applications, but increase cluster-management overhead. Development and production also remain together within each application’s cluster. This model is more appropriate when applications require dedicated cluster boundaries. 

  * **Option D — Technically Possible but Not Best:** This separates applications logically but provides no explicit separation between their development and production deployments. It offers the least suitable environment structure for this sensitive-data scenario. 

**Exam Trap**

Do not equate creating namespaces with enforcing security. Namespaces organize resources and scope policies; RBAC and network policies enforce the relevant access restrictions. Also, choosing the fewest clusters does not automatically provide the best balance of security and management effort.

**Foundation Concept**

Choose isolation boundaries according to trust and operational requirements. Clusters separate control planes and cluster-wide administration; namespaces support policy-controlled sharing within a cluster. Workloads requiring stronger isolation than shared-cluster policies provide may need dedicated clusters. 

**Real-World Connection**

Create development and production clusters containing separate namespaces for billing and customer-profile applications. Apply namespace-scoped permissions and allow only required service communication. This preserves shared cluster administration while reducing opportunities for unintended cross-application access.

**Memory Hook**

For shared enterprise GKE, separate environments by cluster and enforce application boundaries with namespace policies.

**30-Second Exam Takeaway**

When the question combines development/production separation, application isolation, and low management overhead, choose one cluster per environment with application namespaces. Security still depends on correctly enforced policies.

**Official References**

  * [**Google Cloud — Best practices for continuous integration and delivery to Google Kubernetes Engine**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/best-practices-continuous-integration-delivery-kubernetes)

Supports: Separate clusters for development and production; distinctions affecting options A, B, and D.

  * [**Google Cloud — Cluster multi-tenancy**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multitenancy-overview)

Supports: Namespace-based enterprise sharing, reduced management overhead, policy enforcement, and isolation limitations.

  * [**Google Cloud — Control communication between Pods and Services using network policies**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy)

Supports: Default Pod connectivity and enforcing communication restrictions between namespaces.

---

## Question 5

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Following several production incidents, your company is building a Cloud Monitoring dashboard to investigate service failures. You need the dashboard to help distinguish problems originating in your service from disruptions affecting the Google Cloud services it depends on. What should you do?

- [ ] A. Define a log-based metric for Google Cloud service errors and display it on the dashboard.
- [ ] B. Add a logs widget that displays system-error entries from Cloud Logging.
- [ ] C. Configure an alerting policy based on system-error metrics.
- [x] D. Turn on Personalized Service Health event annotations for the dashboard.

### Explanation

**Correct Answer**

**D. Turn on Personalized Service Health event annotations for the dashboard.**

**Exam Reasoning Explanation**

The dashboard needs Google Cloud incident context alongside your service’s telemetry. Personalized Service Health annotations provide that context, allowing you to compare application failures with provider-reported disruptions. Generic error metrics, logs, and alerts describe symptoms without automatically establishing their origin. 

**Key Exam Clues**

  * **“Cloud Monitoring dashboard” — Technical signal:** The solution should integrate incident information into the dashboard.

  * **“Distinguish problems originating in your service” — Hard constraint:** Observing errors alone is insufficient; dependency-health context is needed.

  * **“Google Cloud services it depends on” — Technical signal:** Personalized Service Health supplies relevant Google Cloud disruption information.

**Why This Is Correct**

Cloud Monitoring queries the Service Health API and displays relevant Google Cloud incidents as annotations on metric charts. These annotations show incident timing and duration, with details about affected services and locations. This lets you correlate service degradation with dependency disruptions. 

Enable the Service Health API and ensure viewers have permission to read its events, such as through `roles/servicehealth.viewer`. Select the events through the dashboard’s **Annotations** menu and pin the selection to persist it.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** An error metric helps quantify failures recorded in logs. However, a generic count does not automatically provide the provider-reported incident context needed to distinguish application problems from Google Cloud disruptions.

  * **Option B — Technically Possible but Not Best:** System-error logs support detailed investigation, but a generic logs widget does not directly overlay relevant Google Cloud incident timelines. It complements Service Health annotations. 

  * **Option C — Different Use Case:** An alerting policy detects configured conditions and can notify responders. It does not, by itself, add the required dependency-health context to the dashboard. Personalized Service Health supports separate alerting workflows when notifications are also needed. 

**Exam Trap**

An error involving a Google Cloud dependency is not automatically evidence of a provider incident. Use Service Health annotations for incident correlation. Option A would fit a requirement to count particular logged errors.

**Foundation Concept**

Effective troubleshooting combines application symptoms with dependency-health events. Matching timestamps, affected services, and locations helps narrow the investigation. Correlation does not prove causation, and the absence of an annotation does not independently prove that your application caused the failure.

**Real-World Connection**

When request errors increase, compare the spike with the Service Health annotations. If a relevant incident affects the same dependency and location, inspect its details alongside your application telemetry. This can focus the investigation and reduce unnecessary application changes.

**Memory Hook**

Use Service Health annotations to compare application symptoms with Google Cloud incident timelines.

**30-Second Exam Takeaway**

When a dashboard must distinguish application failures from Google Cloud dependency disruptions, enable Personalized Service Health annotations. Use logs and metrics to investigate the resulting correlation.

**Official References**

  * [**Google Cloud — Event types**](https://docs.cloud.google.com/monitoring/dashboards/event-types)

Supports: Google Cloud incident annotations, relevance filtering, affected services, and incident duration.

  * [**Google Cloud — Show events on a dashboard**](https://docs.cloud.google.com/monitoring/dashboards/show-events)

Supports: Annotation configuration, persistence, API prerequisites, permissions, and distinctions between event sources.

  * [**Google Cloud — Personalized Service Health overview**](https://docs.cloud.google.com/service-health/docs/overview)

Supports: Project-relevant provider incidents and complementary logging and alerting integrations.

---

## Question 6

*Domain 2: Building and Implementing CI/CD Pipelines*

Your company uses several Cloud Deploy delivery pipelines to release applications across different environments. The development team currently has no access to these pipelines. You must grant the team access exclusively to the development delivery pipeline while following Google-recommended access-control practices. What should you do?

- [ ] A. Grant the team `roles/clouddeploy.operator` through the Google Cloud console, and configure deny conditions for every pipeline except the development delivery pipeline.
- [ ] B. Create a custom IAM role containing all `clouddeploy.automations.*` permissions through the Google Cloud console, and grant it through an allow policy scoped to the development delivery pipeline.
- [ ] C. Define a policy file granting the team `roles/clouddeploy.operator`, and apply it to the development target.
- [x] D. Define a policy file granting the team `roles/clouddeploy.developer`, and apply it to the development delivery pipeline.

### Explanation

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

---

## Question 7

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

You are provisioning development environments for your company’s developers. Every developer must receive the same IDE setup, and the environments must not be exposed to public networks. You need the **MOST** cost-effective approach that preserves developer productivity. What should you do?

- [ ] A. Provision Compute Engine VMs with public IP addresses, configure Public NAT, and schedule the VMs to shut down.
- [ ] B. Provision Compute Engine VMs without public IP addresses and schedule the VMs to shut down.
- [x] C. Create a private Cloud Workstations cluster and configure `idleTimeout` in the workstation configuration.
- [ ] D. Create a private Cloud Workstations cluster and configure `runningTimeout` in the workstation configuration.

### Explanation

**Correct Answer**

**C. Create a private Cloud Workstations cluster and configure**`**idleTimeout**`**in the workstation configuration.**

**Exam Reasoning Explanation**

The solution must combine consistent developer tooling, private access, and efficient resource use. Cloud Workstations configurations standardize the environment, while a private cluster restricts access. An inactivity timeout reduces unused compute time without imposing a shutdown solely because a fixed runtime or scheduled hour has been reached.

**Key Exam Clues**

  * **“Same IDE setup” — Hard constraint:** Use a reusable configuration that standardizes developer environments.

  * **“Not … exposed to public networks” — Hard constraint:** Provide private workstation access.

  * **“MOST cost-effective” — Optimization requirement:** Reduce unnecessary resource consumption.

  * **“Preserves developer productivity” — Hard constraint:** Prefer activity-aware shutdown over stopping an actively used environment.

**Why This Is Correct**

A workstation configuration defines the IDE, container image, machine settings, and other shared environment properties. The `idleTimeout` field determines how long a workstation can remain without user traffic before the configured idle action occurs; stopping is the default action. 

Private clusters prevent clients from connecting through the public internet. Complete the private design by disabling public IP addresses on workstation VMs and providing the required Private Service Connect endpoint and private connectivity for developers. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Assigning public IP addresses conflicts with the required private environment design. Adding Public NAT does not remove those addresses or make this equivalent to private workstation access. 

  * **Option B — Technically Possible but Not Best:** Private VMs can host standardized IDEs, but require additional environment management. Scheduled shutdowns follow configured times rather than developer activity, so they can interrupt work or leave unused VMs running until the next shutdown. 

  * **Option D — Technically Possible but Not Best:** `runningTimeout` stops a workstation after a specified runtime, even if the developer remains active. It is useful for bounding session duration and facilitating updates, but is less suited to the inactivity-based cost control required here. 

**Exam Trap**

The documented inactivity parameter is `**idleTimeout**`; its spelling has been corrected in option C. Do not confuse it with `runningTimeout`, which applies regardless of activity.

**Foundation Concept**

An idle timeout responds to inactivity; a runtime limit responds to elapsed time; a schedule responds to the clock. Choose the mechanism that matches the operational goal. Set an appropriate inactivity threshold because background tasks without user interaction can still be considered idle.

**Real-World Connection**

Give developers workstations created from one configuration and automatically stop abandoned sessions. Developers retain consistent tooling while the organization reduces idle compute usage and repetitive setup work.

**Memory Hook**

Use an idle timeout to reclaim unused development compute while preserving active sessions.

**30-Second Exam Takeaway**

Consistent IDEs, private access, and activity-aware cost control point to a private Cloud Workstations cluster with `idleTimeout`. Fixed schedules and runtime limits can stop developers during active work.

**Official References**

[**Google Cloud — WorkstationConfig REST resource**](https://docs.cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters.workstationConfigs)

Supports: Configuration templates, IDE standardization, `idleTimeout`, idle actions, and `runningTimeout`.

[**Google Cloud — Configure VPC Service Controls and private clusters**](https://docs.cloud.google.com/workstations/docs/configure-vpc-service-controls-private-clusters)

Supports: Private cluster access, disabling workstation public IP addresses, and private connectivity requirements.

[**Google Cloud — Scheduling a VM instance to start and stop**](https://docs.cloud.google.com/compute/docs/instances/schedule-instance-start-stop)

Supports: Time-based VM shutdown behavior and its distinction from inactivity-based shutdown.

---

## Question 8

*Domain 2: Building and Implementing CI/CD Pipelines*

You operate Service A, a public-facing API with a response-time SLO of 500 ms. Service A synchronously calls Service B, an internal API that collects request information for transactions handled by Service A.

Under heavy load, Service B becomes unreliable, returning HTTP 500 errors or causing connection timeouts. You need to protect Service A’s users from these failures. What should you do?

- [ ] A. Increase the capacity of the request queue preceding Service A’s worker thread pool.
- [ ] B. Retry failed calls to Service B using exponential backoff.
- [x] C. Implement a circuit breaker with a fallback that stores the request data in a database.
- [ ] D. Apply rate limiting in Service A to restrict outbound requests to Service B.

### Explanation

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

---

## Question 9

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

You administer Google Cloud resources for a healthcare company whose regulatory requirements mandate creating all resources in United States regions. When you attempt to create a Secret Manager secret, the operation returns this error:
    
          1. Constraint constraints/gcp.resourceLocations violated for [orgpolicy:projects/000000] attempting to create a secret in [global]

How should you resolve the failure while preserving the required location restrictions?

- [ ] A. Delete the organization policy identified in the error message.
- [ ] B. Configure automatic replication when creating the secret.
- [x] C. Configure user-managed replication when creating the secret.
- [ ] D. Update the organization policy to permit the `global` location.

### Explanation

**Correct Answer**

**C. Configure user-managed replication when creating the secret.**

**Exam Reasoning Explanation**

Preserve the location restriction and change the secret’s replication configuration. Automatic replication requires `global` to be permitted. User-managed replication lets you explicitly select US locations, provided every selected location is allowed by the organization policy. 

**Key Exam Clues**

  * **“United States regions” — Hard constraint:** Every selected replica location must satisfy the geographic requirement.

  * `**constraints/gcp.resourceLocations**`**— Technical signal:** The failure concerns resource placement, not IAM authorization.

  * `**[global]**`**— Technical signal:** The attempted configuration conflicts with the permitted locations.

**Why This Is Correct**

User-managed replication stores the secret payload in locations you specify. Create the secret with replicas only in approved US regions.

Secret Manager evaluates all selected replica locations against the resource-location policy. Creation succeeds only when every location is permitted. This resolves the placement conflict without weakening the policy. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Removing the policy does not configure compliant secret placement. It attempts to bypass the control enforcing the company’s location restrictions.

  * **Option B — Incorrect:** Automatic replication requires the organization policy to allow `global`, so it does not resolve the reported failure. Its unrestricted replication also does not guarantee US-only payload storage. 

  * **Option D — Violates Requirement:** Allowing `global` would permit automatic replication, but would not restrict replicas to US regions. Making secret creation succeed is insufficient unless the resulting placement remains compliant. 

**Exam Trap**

Do not relax an organization policy simply because it blocks resource creation. First select a resource configuration that satisfies it. Also, choosing user-managed replication is insufficient unless **every configured replica location** is approved.

**Foundation Concept**

Organization policies establish deployment guardrails; service-specific settings determine how a resource satisfies them. For Secret Manager, replication policies control secret-payload storage locations.

Storage placement is distinct from broader processing and access requirements. Secret Manager’s regional service provides additional regional controls when requirements extend to data at rest, in use, and in transit. 

**Real-World Connection**

Create an application credential with replicas confined to approved US regions. The existing policy continues rejecting disallowed placements, reducing the risk of accidental storage outside the permitted geography.

**Memory Hook**

When a location policy rejects `global`, explicitly place every secret replica in an approved region.

**30-Second Exam Takeaway**

For this Secret Manager error, choose user-managed replication with permitted US locations. Keep the organization policy intact; enabling `global` would not enforce US-only replication.

**Official References**

[**Google Cloud — Choose a secret replication policy**](https://docs.cloud.google.com/secret-manager/docs/choosing-replication)

Supports: Automatic replication’s `global` requirement, user-managed replica placement, and validation of every selected location.

[**Google Cloud — Services that support restricting resource locations**](https://docs.cloud.google.com/organization-policy/reference/restrict-locations-supported-services)

Supports: Secret Manager’s enforcement of the resource-location organization policy.

[**Google Cloud — Compare global and regional service**](https://docs.cloud.google.com/secret-manager/docs/secret-manager-secrets-comparison)

Supports: The distinction between replica placement and stricter regional data-residency controls.

---

## Question 10

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

You are using Code OSS in Cloud Workstations to develop a Node.js utility that serves a simple web page. The application is running on port 3000, and you have verified that the required firewall rules are configured. You now need to view the page from your local computer while following Google-recommended security practices. What should you do?

- [ ] A. Open the page using a browser hosted on a bastion VM.
- [ ] B. Run `gcloud compute start-iap-tunnel` against the VM underlying the workstation.
- [ ] C. Enable public IP addresses in the workstation configuration.
- [x] D. Open the application’s preview link in the Code OSS panel.

### Explanation

**Correct Answer**

**D. Open the application’s preview link in the Code OSS panel.**

**Exam Reasoning Explanation**

The application is already running, and the firewall configuration has been verified. The remaining requirement is secure browser access from your computer. Cloud Workstations provides built-in web access, making the editor’s preview the appropriate choice without introducing another VM or direct access path. 

**Key Exam Clues**

  * **“Code OSS in Cloud Workstations” — Technical signal:** The development environment supports application previews.

  * **“Required firewall rules are configured” — Exclusion:** Additional firewall configuration is not the requested solution.

  * **“Following Google-recommended security practices” — Hard constraint:** Prefer the managed, authenticated workstation access path.

**Why This Is Correct**

Cloud Workstations lets your local browser access HTTP applications running on workstation ports. The base editor redirects application links to the appropriate workstation URL. Access requires authentication and the `workstations.workstations.use` permission, included in the Cloud Workstations User role.

Port 3000 is supported by default. If administrators restrict access through `allowedPorts`, that configuration must permit the application’s port. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** A suitably connected bastion could host a browser, but it introduces another machine and access workflow. The existing workstation preview already provides the required browser access.

  * **Option B — Technically Possible but Not Best:** IAP TCP forwarding supports connections to Compute Engine instances when appropriately configured. However, targeting the underlying VM introduces a separate access mechanism. Google recommends restricting access to underlying workstation resources and using the workstation gateway. 

  * **Option C — Technically Possible but Not Best:** Public IP addresses are unnecessary for the managed preview and do not themselves provide authenticated application access. Google’s security guidance supports restricting public connectivity when appropriate. 

**Exam Trap**

Do not assume that viewing a remotely hosted development page requires a public IP address. The workstation’s authenticated web endpoint provides browser access without requiring direct public access to its VM.

**Foundation Concept**

Network reachability and user authorization are separate controls. A managed development gateway can route requests to an application while enforcing identity-based access. Opening additional network paths does not automatically improve that security model.

**Real-World Connection**

Keep the Node.js server running on port 3000 and open its preview from Code OSS. You can test the page in your local browser while retaining the workstation’s access controls and avoiding another VM to administer.

**Memory Hook**

For a web application running in Cloud Workstations, use its authenticated preview before adding network access paths.

**30-Second Exam Takeaway**

When a Cloud Workstations application already runs successfully, use the editor’s preview for local browser testing. Bastions, VM-level tunnels, and public IP changes add unnecessary configuration for this scenario.

**Official References**

  * [**Google Cloud — Connect to HTTP servers running on a workstation**](https://docs.cloud.google.com/workstations/docs/access-http-servers-running-on-workstations)

Supports: Browser access, editor link forwarding, authentication, IAM permissions, and allowed ports.

  * [**Google Cloud — Set up security best practices**](https://docs.cloud.google.com/workstations/docs/set-up-security-best-practices)

Supports: Restricting direct VM access, limiting underlying-resource permissions, and controlling public connectivity.

  * [**Google Cloud CLI — gcloud compute start-iap-tunnel**](https://docs.cloud.google.com/sdk/gcloud/reference/compute/start-iap-tunnel)

Supports: The purpose of IAP TCP forwarding and its distinction from workstation web preview.

---

## Question 11

*Domain 3: Applying Site Reliability Engineering Practices*

You are responsible for your company’s main revenue-generating application. Its error budget policy suspends production deployments when the service approaches a breach of its service level objective (SLO). Recent service problems have exhausted the available error budget. A pending release includes a feature urgently needed by your largest customer, and you have been informed that all unit tests have passed. How should you proceed?

- [x] A. Wait for the error budget to be replenished before deploying the feature.
- [ ] B. Repeat the unit tests and deploy the feature if they succeed.
- [ ] C. Proceed with the feature deployment immediately.
- [ ] D. Introduce the feature to a subset of users, then expand the rollout if no errors are reported.

### Explanation

**Correct Answer**

**A. Wait for the error budget to be replenished before deploying the feature.**

**Exam Reasoning Explanation**

The deployment freeze is the decisive constraint. The service has exhausted its error budget, so the established policy takes precedence over customer urgency and successful testing. Neither repeating tests nor reducing rollout size changes whether this feature release is permitted.

**Key Exam Clues**

  * **“Suspends production deployments” — Hard constraint:** The organization has already defined its response to reliability risk.

  * **“Exhausted the available error budget” — Technical signal:** The service has reached the condition requiring the freeze.

  * **“Feature urgently needed” — Business pressure:** Urgency does not establish an exception to the policy.

  * **“All unit tests have passed” — Supporting evidence:** Testing increases confidence but does not replenish the budget.

**Why This Is Correct**

An error budget policy translates measured reliability into release decisions. When the budget is depleted, postponing feature releases limits additional change risk and creates room for reliability improvements. Google’s guidance freezes changes until sufficient budget becomes available again. 

Google’s example policy permits exceptions for P0 issues and security fixes. The scenario describes a customer feature, with no qualifying exception identified.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Violates Requirement:** Passing the tests again does not lift the deployment freeze. Unit tests also cannot establish that every production interaction will behave correctly; some defects emerge only under real traffic. 

  * **Option C — Violates Requirement:** Immediate deployment disregards the explicit error budget policy. The customer’s importance does not independently authorize bypassing that policy. 

  * **Option D — Violates Requirement:** A canary limits the number of users initially exposed to a change, but it remains a production deployment. It is useful when releases are permitted; it does not override an active freeze. 

**Exam Trap**

A gradual rollout is normally a sound reliability practice, making D tempting. However, rollout safety and release permission are separate decisions. If the error budget had recovered and the freeze were lifted, a monitored canary would be an appropriate deployment strategy.

**Foundation Concept**

An error budget represents the failures permitted by an SLO over its measurement period. Its policy determines how remaining budget affects engineering priorities. Recovery depends on the defined measurement window and release criteria; successful tests do not erase previously observed failures. 

**Real-World Connection**

Keep the tested feature ready while the team addresses the recent reliability problems. Once the policy permits feature releases again, deploy progressively and monitor the result. This protects the application’s existing revenue while preserving the work needed for the customer’s feature.

**Memory Hook**

A safer rollout reduces deployment risk, but it does not lift an error-budget freeze.

**30-Second Exam Takeaway**

An exhausted error budget plus an explicit deployment freeze means postponing feature releases. Customer urgency, passing tests, and canaries do not replace the policy’s release criteria.

**Official References**

  * [**Google SRE Workbook — Example Error Budget Policy**](https://sre.google/workbook/error-budget-policy/)

Supports: Deployment freezes, reliability prioritization, and exceptions for P0 issues or security fixes.

  * [**Google SRE Book — A Collection of Best Practices for Production Services**](https://sre.google/sre-book/service-best-practices/)

Supports: Freezing feature changes when the budget is spent and resuming after budget recovery.

  * [**Google SRE Workbook — Canarying Releases**](https://sre.google/workbook/canarying-releases/)

Supports: Canary risk reduction, production exposure, and limitations of pre-production testing.

---

## Question 12

*Domain 2: Building and Implementing CI/CD Pipelines*

Your company is adopting Cloud Deploy to deliver a web service running on Google Kubernetes Engine (GKE). The application currently has no automated tests. The Quality Assurance (QA) team must manually validate each new release before that version handles any production traffic. Which delivery pipeline design should you implement?

- [ ] A. Configure a delivery pipeline with one stage and a standard deployment strategy.
- [ ] B. Configure a delivery pipeline with one stage and a canary deployment strategy.
- [ ] C. Configure a delivery pipeline with two stages and a canary deployment strategy.
- [x] D. Configure a delivery pipeline with two stages and a standard deployment strategy.

### Explanation

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

---

## Question 13

*Domain 3: Applying Site Reliability Engineering Practices*

You are rolling out a new application version to a Google Kubernetes Engine (GKE) cluster spanning multiple zones. Most of the rollout appears healthy, but some Pods in one zone are showing increased error rates. You need to revert the update only for the affected Pods while minimizing disruption to users. What should you do?

- [ ] A. Reduce the number of Pods in the affected zone, then deploy the new application version again.
- [ ] B. Drain the affected nodes, then deploy the new application version on the remaining nodes.
- [x] C. Restore the Deployment’s previous Pod template and use a rolling update to replace the Pods in the affected zone.
- [ ] D. Run `kubectl rollout undo` for the entire Deployment, then redeploy the new version while excluding the affected zone.

### Explanation

**Correct Answer**

**C. Restore the Deployment’s previous Pod template and use a rolling update to replace the Pods in the affected zone.**

However, C requires an unstated prerequisite: **the affected Pods must belong to an independently managed Deployment scoped to that zone**. Changing a Deployment’s template applies to its managed replicas across all zones—not just the zone experiencing errors. 

**Exam Reasoning Explanation**

The decisive requirement is rollback scope. A rolling update controls how Pods are replaced; it does not automatically restrict replacement to a geographic zone. First establish whether the affected zone has a separate Deployment. Without that boundary, C cannot provide the requested selective rollback.

**Key Exam Clues**

  * **“Only for the affected Pods” — Hard constraint:** Healthy portions must remain outside the rollback scope.

  * **“One zone” — Technical signal:** Placement and Deployment ownership must be distinguished.

  * **“Minimizing disruption” — Preference:** Replace affected workloads gradually while preserving sufficient serving capacity.

**Why This Is Correct**

C describes an appropriate rollback mechanism **when the Deployment already manages only the affected zone’s workload**. Restore its previous template and use controlled rolling replacement.

An architecture supporting this can combine separate Deployments with zone-specific node selectors or required node affinity. The conclusion follows from combining independent Deployment management with explicit Pod-placement constraints. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Incorrect:** Scaling down and redeploying the new version does not restore the previous application version. It can reduce capacity without performing the required rollback.

  * **Option B — Different Use Case:** Draining evicts workloads and makes nodes unavailable for new scheduling. It supports node maintenance or evacuation, but does not revert the application version and can affect additional workloads on those nodes. 

  * **Option D — Violates Requirement:** It explicitly rolls back the entire Deployment, including healthy replicas, before introducing another deployment. That exceeds the requested selective scope. Deployment rollback restores the selected Deployment’s previous template. 

**Exam Trap**

**Rolling** describes replacement behavior; it does not mean **zone-selective**. C becomes valid if the question specifies that each zone has its own independently managed Deployment.

**Foundation Concept**

Availability zones determine workload placement. Deployments determine the desired application version for their managed replicas. Selective recovery requires those management boundaries to match the desired recovery scope.

**Real-World Connection**

With separate Deployments for zones A, B, and C, you can restore the previous version only in zone B while preserving the other Deployments. If one Deployment spans all three zones, reverting its template eventually affects its replicas throughout that Deployment.

**Memory Hook**

For native Kubernetes Deployments, rollback scope follows the Deployment boundary.

**30-Second Exam Takeaway**

C is the intended answer only with an independently managed Deployment for the affected zone. A shared Deployment does not gain zone-specific rollback merely by restoring its previous Pod template.

**Official References**

[**Kubernetes — Deployments**](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

Supports: Template-driven rollouts, Deployment-wide reconciliation, rollback behavior, and rolling-update controls.

[**Kubernetes — Assigning Pods to Nodes**](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)

Supports: Node selectors, required node affinity, and zone-based placement constraints.

[**Kubernetes — kubectl drain**](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_drain/)

Supports: Node evacuation, Pod eviction, and why draining is distinct from application rollback.

---

## Question 14

*Domain 2: Building and Implementing CI/CD Pipelines*

You are configuring a continuous integration (CI) pipeline whose integration tests require access to APIs hosted in a private Virtual Private Cloud (VPC) network. Your security team requires that API traffic remain private. You need a solution that minimizes operational overhead. What should you do?

- [x] A. Use Cloud Build private pools configured to connect to your private VPC network.
- [ ] B. Use Cloud Build to create a Compute Engine VM in your private VPC network, and execute the integration tests through a startup script.
- [ ] C. Use Cloud Build to run the pipeline, and configure a cross-region internal Application Load Balancer to provide access to the APIs.
- [ ] D. Use Cloud Build to run the pipeline, and configure a global external Application Load Balancer with a Google Cloud Armor security policy to provide access to the APIs.

### Explanation

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

---

## Question 15

*Domain 2: Building and Implementing CI/CD Pipelines*

You store container images built by Cloud Build in Artifact Registry. You need to maintain vulnerability scanning coverage for both existing and newly uploaded images. You also need to identify the principal responsible for pushing each image. What should you do?

- [x] A. Enable automatic vulnerability scanning for newly uploaded images and arrange periodic rescanning of all stored images. Use Cloud Audit Logs to track image uploads and identify the uploading principal.
- [ ] B. Export vulnerability scan results to a Cloud Storage bucket, and use a custom script to analyze the results and notify the security team.
- [ ] C. Configure automatic daily rescanning of images. Enable Cloud Audit Logs for scan operations, and use Logs Explorer to identify vulnerabilities.
- [ ] D. Trigger automatic vulnerability scans when new image tags are created, and review the results. Use Cloud Audit Logs to track tag creation events.

### Explanation

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

---

## Question 16

*Domain 2: Building and Implementing CI/CD Pipelines*

Your web application connects to an AlloyDB for PostgreSQL cluster through a private IP address accessible from your default VPC network. Before deploying a new application version, your Cloud Build CI/CD pipeline must execute a database schema migration.

You need to implement this process following Google-recommended security practices. What should you do?

- [ ] A. Configure a Cloud Build private pool with a static external IP address. Restrict database connections to that address, and execute the migration script in the private pool.
- [x] B. Create a service account with the required database access permissions. Configure Cloud Build to use this service account, and execute the migration script in a private pool.
- [ ] C. Store the database username and password in Secret Manager, and retrieve them when executing the migration script.
- [ ] D. Store the database username and encrypted password in the application configuration file, and use these credentials to execute the migration through Cloud Build.

### Explanation

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

---

## Question 17

*Domain 3: Applying Site Reliability Engineering Practices*

You manage a critical API deployed on Cloud Run that handles an average of 10,000 requests per minute. Users expect **99.9% availability** and response times of **200 milliseconds or less for at least 95% of requests**.

You need to define service level objectives (SLOs) that reflect these expectations and implement ongoing measurement and monitoring. What should you do?

- [ ] A. Configure Cloud Monitoring alerts to trigger when average API latency exceeds 150 milliseconds or the error rate exceeds 0.1%.
- [ ] B. Define latency as the only SLO, requiring 99% of requests to complete within 100 milliseconds.
- [ ] C. Define an availability SLO of 99% and a latency SLO requiring 90% of requests to complete within 500 milliseconds. Use Cloud Monitoring to measure compliance and alert on violations.
- [x] D. Define availability and latency SLOs using the corresponding service level indicators (SLIs). Use Cloud Monitoring to measure compliance and alert on violations.

### Explanation

**Correct Answer**

**D. Define availability and latency SLOs using the corresponding service level indicators (SLIs). Use Cloud Monitoring to measure compliance and alert on violations.**

**Exam Reasoning Explanation**

D connects the user expectations to measurable indicators, explicit objectives, and operational monitoring. An SLO requires an SLI, a target, and a defined compliance period.

**Key Exam Clues**

  * **Availability requirement:** At least 99.9% availability.

  * **Latency requirement:** At least 95% of requests complete within 200 milliseconds.

  * **Operational requirement:** Continuously measure performance and notify the team about problems.

**Why This Is Correct**

Define two request-based SLOs over an agreed compliance period:

  * **Availability:** Successful eligible requests divided by total eligible requests, with a target of **at least 99.9%**.

  * **Latency:** Eligible requests completing within 200 milliseconds divided by total eligible requests, with a target of **at least 95%**. 

Cloud Run automatically supplies request-count and request-latency metrics to Cloud Monitoring. Use suitable metrics to measure the SLIs, track compliance, and configure notification channels with SLO alerting. Burn-rate alerts can warn when the error budget is being consumed too quickly. 

**Why the Other Options Are Not the Best Fit**

  * **A — Technically Possible but Not Best:** These alerts can supplement monitoring, but average latency does not establish whether 95% of requests meet the 200-millisecond threshold. The option also does not explicitly define and measure the requested SLOs. Google’s SRE guidance explains that averages can conceal slow requests. 

  * **B — Violates Requirement:** It omits availability entirely. A stricter latency target does not replace the missing availability objective.

  * **C — Violates Requirement:** Both targets are weaker than required: 99% availability instead of 99.9%, and 90% within 500 milliseconds instead of 95% within 200 milliseconds.

**Exam Trap**

**Average latency and a percentile-based latency requirement are different measurements.** A lower average does not guarantee that the required fraction of requests is fast enough. 

**Foundation Concept**

An **SLI** measures service behavior. An **SLO** sets the acceptable target for that measurement over a specified period. An **alerting policy** determines when the team should respond. 

**Real-World Connection**

Suppose 90% of requests take 50 milliseconds and 10% take 500 milliseconds. Average latency is only **95 milliseconds** , yet just **90%** meet the 200-millisecond threshold—the required latency SLO fails.

**Memory Hook**

Measure successful requests and sufficiently fast requests, then set targets and alerts for both.

**30-Second Exam Takeaway**

Choose **D**. Define separate availability and latency SLIs, apply the required targets over a compliance period, and monitor them with SLO-based alerts.

**Official References**

  * [**Concepts in service monitoring**](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring)  
Supports: Availability and latency SLIs, request-based SLOs, targets, and compliance periods.

  * [**Service Level Objectives — Google SRE**](https://sre.google/sre-book/service-level-objectives/)  
Supports: User-focused objectives and why average latency can conceal poor tail performance.

  * [**Monitor Health and Performance — Cloud Run**](https://docs.cloud.google.com/run/docs/monitoring)  
Supports: Automatic collection of request-count and request-latency metrics.

  * [**Alerting on your burn rate**](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/alerting-on-budget-burn-rate)  
Supports: SLO-based alerting, notification channels, and error-budget burn monitoring.

---

## Question 18

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your organization’s main ecommerce platform runs on Google Kubernetes Engine (GKE) and has started showing intermittent spikes in response latency. Customers have reported that the checkout flow sometimes takes noticeably longer to complete. You need to determine what is actually causing this performance degradation. What should you do?

- [ ] A. Increase the replica count for the application’s GKE deployment and turn on Horizontal Pod Autoscaling.
- [ ] B. In Cloud Logging, create a logs-based metric that counts slow requests, then configure a Cloud Monitoring alerting policy to notify you when the count crosses a defined threshold.
- [ ] C. Review the rollout history in Cloud Deploy and roll back to an earlier application version to check whether the problem goes away.
- [x] D. Use Cloud Trace to examine distributed traces for the checkout flow, and inspect the trace waterfalls to pinpoint which service or operation is contributing the most latency.

### Explanation

**Correct Answer**

**D. Use Cloud Trace to examine distributed traces for the checkout flow, and inspect the trace waterfalls to pinpoint which service or operation is contributing the most latency.**

**Exam Reasoning Explanation**

The hard requirement in the stem is “identify the root cause” — not “reduce latency” and not “confirm a hunch.” That rules out anything that only reacts to symptoms or guesses at a cause without evidence. Cloud Trace is purpose-built to answer “where in a multi-service request is the time actually going?” by breaking a single checkout request down into spans per service/operation and rendering them as a waterfall, so you can see directly which hop is slow. Every other option either treats a symptom (A), detects that a problem exists without localizing it (B), or tests an unproven assumption by making a disruptive production change (C). Only D gives you evidence pointing at a specific component.

**Key Exam Clues**

  * **“intermittent periods of high ... latency”** — points toward a tool that captures per-request timing data over time, not a static config check.

  * **“sometimes very slow”** — rules out a uniform, always-on problem; favors a tool that can show you the slow instances specifically, not just an aggregate count.

  * **“identify the root cause”** — a decisive requirement/exclusion signal: it eliminates any option that only mitigates symptoms or only detects that an issue occurred.

  * **“checkout process”** — implies a multi-step, likely multi-service flow, which is exactly what distributed tracing is designed to decompose.

**Why This Is Correct**

Cloud Trace collects per-request latency data across the services involved in a transaction and displays it as a waterfall of spans, with each span showing how much time was spent in that specific service or operation. For an intermittent, checkout-specific slowdown, this lets you compare a slow trace against a fast one and see exactly which downstream call (a database query, a payment service, an external API) is adding the delay — which is precisely “identifying the root cause” rather than inferring it indirectly.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Different Use Case:** Horizontal Pod Autoscaling solves a capacity problem (not enough replicas for the load), which is a different failure mode than “one particular downstream call is slow.” Adding replicas might mask an overload-related symptom but tells you nothing about which service or operation is responsible, and if the real cause isn’t capacity, it won’t help at all.

  * **Option B — Technically Possible but Not Best:** A logs-based metric and alert is good for knowing _that_ slow requests are occurring and getting notified when they cross a threshold, but a count of slow requests doesn’t tell you _where_ in the request path the time is being lost — it’s a detection mechanism, not a localization mechanism.

  * **Option C — Violates Requirement:** Rolling back assumes, without evidence from the scenario, that a recent deployment introduced the regression. It’s a disruptive, all-or-nothing experiment: if the rollback doesn’t help, you’ve learned little and still have to diagnose the issue, and if it does help, you still don’t know which part of the previous change was the actual cause.

**Exam Trap**

The trap is picking an option that sounds like reasonable incident-response practice (scale up, roll back, alert) instead of one that specifically answers “where is the time going.” Google Cloud DevOps-track exams frequently pair a correct observability-analysis answer against plausible-sounding operational actions that would only be the right move after root cause is already known.

**Foundation Concept**

In a distributed system, overall request latency is the sum of time spent across every service and network hop a request touches. Metrics and logs can tell you that latency increased in aggregate; only a distributed trace reconstructs the full path of an individual request and attributes latency to specific spans, which is why it’s the standard tool for localizing latency root causes in microservices-style architectures.

**Real-World Connection**

A team that jumps straight to autoscaling for an intermittent latency complaint often burns on-call time and cloud spend without fixing anything, because the real cause (for example, a slow downstream payment-processor call or an unindexed database query) keeps happening regardless of replica count. Tracing the checkout flow first turns a vague “it’s sometimes slow” ticket into a specific, actionable fix targeted at the one slow hop.

**Memory Hook**

Need to know _that_ it’s slow → logs/metrics and alerts. Need to know _where_ it’s slow → Cloud Trace and trace waterfalls.

**30-Second Exam Takeaway**

When a question explicitly asks you to “identify the root cause” of latency in a multi-service or multi-step flow, look for the distributed-tracing answer (Cloud Trace, trace waterfalls, spans) over any option that only mitigates, detects, or guesses at the cause.

**Official References**

[**Google Cloud — Cloud Trace overview:**](https://cloud.google.com/trace/docs/overview) Supports: the correct-answer mechanism (distributed tracing, spans, and trace waterfalls used to localize latency)

[**Google Cloud — Log-based metrics overview:**](https://cloud.google.com/logging/docs/logs-based-metrics) Supports: the option B distinction (logs-based metrics and alerting are for detection/counting, not per-request root-cause localization)

---

## Question 19

*Domain 3: Applying Site Reliability Engineering Practices*

Your organization is actively developing a new web service and preparing it for production. As the SRE team lead, you **MUST** apply Google-recommended practices throughout productionalization. Which two activities should you prioritize next? **(Choose two.)**

- [x] A. Establish monitoring and alerting for the service.
- [ ] B. Begin preparing guidelines for using infrastructure systems.
- [ ] C. Collaborate with the product team on the service’s design.
- [ ] D. Implement redundant resources within the service environment.
- [x] E. Provide early SRE consultation to review architecture and design decisions in detail.

### Explanation

**Correct Answer**

The supplied answer key selects:

**A. Establish monitoring and alerting for the service.**

**E. Provide early SRE consultation to review architecture and design decisions in detail.**

However, **this pair is not uniquely supported by the wording**. Google’s guidance also directly supports D during active-development productionalization. 

**Exam Reasoning Explanation**

A and E address operational visibility and early identification of architectural risks. Both are recommended practices. However, the scenario specifically identifies active development and productionalization, for which Google also explicitly recommends redundancy. Therefore, the supplied key is plausible, but eliminating D requires additional context. 

**Key Exam Clues**

  * **“Actively developing” — Technical signal:** Identifies the service’s lifecycle stage.

  * **“Preparing it for production” — Required outcome:** Calls for operational readiness work.

  * **“Google-recommended practices” — Hard constraint:** Requires authoritative support for the selected activities.

  * **“Choose two” — Cardinality instruction:** Requires a defensible distinction between the selected pair and the remaining options.

**Why This Is Correct**

  * **A:** Monitoring and alerting provide visibility into service behavior and enable detection of operational problems.

  * **E:** Early consultation identifies architectural risks while design changes are comparatively easier to make. Google’s early-engagement model extends through design and implementation, so this activity remains relevant during development.

These activities complement each other, but their validity does not establish that they are the only appropriate pair. 

**Why the Other Options Are Not the Best Fit**

  * **Option B — Technically Possible but Not Best:** Infrastructure guidelines support consistent engineering decisions. Google associates this activity primarily with architecture and design, making it less directly aligned with the stated productionalization work. 

  * **Option C — Technically Possible but Not Best:** Collaborative design is legitimate SRE work. The stem provides no specific design problem that makes codesign the immediate priority, although it should not be described as an incorrect practice. 

  * **Option D — Best Fit under a phase-specific interpretation:** Google explicitly includes additional resources for redundancy in active-development productionalization. Consequently, D cannot be reliably eliminated, and A/D is another defensible selection. 

**Exam Trap**

Distinguish an intended answer key from a uniquely validated answer. Treating redundancy as unnecessary would introduce an assumption absent from the scenario.

**Foundation Concept**

SRE combines early design influence with operational readiness. Lifecycle phases guide priorities, while consultation, documentation, monitoring, and resilience work can overlap.

**Real-World Connection**

An SRE team could review architectural failure modes, establish actionable alerts, and validate redundant capacity before launch. Actual priorities depend on existing controls, reliability objectives, and identified risks.

**Memory Hook**

Production readiness combines operational visibility, resilience, and early reliability review.

**30-Second Exam Takeaway**

**A/E is the supplied key, while A/D has direct lifecycle-specific support.** This item needs clarification before it can be published as a uniquely graded two-answer question.

**Official References**

  * [**Google SRE Workbook — SRE Engagement Model:**](https://sre.google/workbook/engagement-model/)

Supports: Monitoring, alerting, and redundancy during active development; infrastructure guidance during architecture and design.

  * [**Google SRE Book — The Evolving SRE Engagement Model:**](https://sre.google/sre-book/evolving-sre-engagement-model/)

Supports: Early consultation, collaborative design, and SRE participation during implementation.

  * [**Google Cloud — Professional Cloud DevOps Engineer Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)

Supports: Objective 3.2, managing the service lifecycle.

---

## Question 20

*Domain 2: Building and Implementing CI/CD Pipelines*

Your company uses Cloud Build and Artifact Registry in a CI/CD pipeline that deploys container images to Google Kubernetes Engine (GKE). Images are tagged with their corresponding commit hashes and promoted to production after passing tests in development and pre-production. A recent production release failed because an integration scenario had not been tested, leading to a disruptive manual rollback. During recovery, you also discovered numerous outdated, unused images in Artifact Registry. You need to improve deployment and rollback management and remove unnecessary images. What should you do?

- [ ] A. Create a dedicated rollback pipeline in Cloud Build, and configure an Artifact Registry cleanup policy.
- [x] B. Manage application deployments with Cloud Deploy, and configure an Artifact Registry cleanup policy.
- [ ] C. Deploy Cloud Service Mesh across the GKE clusters, and manually delete obsolete images from Artifact Registry.
- [ ] D. Manage application deployments with Cloud Deploy, and schedule a Cloud Build job to delete obsolete container images.

### Explanation

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

---

## Question 21

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your service runs on Google Kubernetes Engine (GKE), and you collect its metrics through Google Cloud Managed Service for Prometheus with managed collection. Following deployment, no metrics appear in Cloud Monitoring, although no errors have been reported. Which troubleshooting action should you take?

- [ ] A. Check whether metric ingestion has exceeded the Cloud Monitoring API write quota.
- [x] B. Validate the application metrics port specified in the `PodMonitoring` resource.
- [ ] C. Check whether a Grafana service is installed in the GKE cluster.
- [ ] D. Verify that the service has been granted the `monitoring.servicesViewer` IAM role.

### Explanation

**Correct Answer**

**B. Validate the application metrics port specified in the**`**PodMonitoring**`**resource.**

**Exam Reasoning Explanation**

The combination of missing metrics and no reported errors points toward exporter or scrape configuration problems. Among the choices, validating the configured port directly tests whether managed collection can discover and scrape the application’s metrics endpoint. Google explicitly recommends this check for these symptoms. 

**Key Exam Clues**

  * **“Managed collection” — Technical signal:** Application scraping is configured through resources such as `PodMonitoring`.

  * **“No metrics appear in Cloud Monitoring” — Diagnostic signal:** Investigate the collection and ingestion path.

  * **“No errors have been reported” — Diagnostic signal:** A scrape configuration problem is a stronger match than an explicitly rejected API request.

**Why This Is Correct**

A `PodMonitoring` resource identifies the application pods and endpoints to scrape. Its port must resolve to the intended metrics endpoint; when using a named port, the name must match the application’s declared container port. A mismatched reference can prevent collection even when the application itself runs normally. 

This is the best diagnostic check among the options, rather than proof that the port is necessarily the root cause.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** Exhausted ingestion quota can prevent metrics from arriving. However, Google documents this condition with HTTP `429` quota-exceeded errors. Without that evidence, scrape configuration is the stronger starting hypothesis. 

  * **Option C — Different Use Case:** Grafana is an optional query and visualization interface. Installing it does not configure application scraping or resolve metrics missing from Cloud Monitoring. Google’s troubleshooting process can use Metrics Explorer directly. 

  * **Option D — Incorrect:** `roles/monitoring.servicesViewer` grants read-only access to service-monitoring resources and SLOs. It does not authorize metric ingestion. The relevant writing role is Monitoring Metric Writer, applied to the identity performing ingestion when required. 

**Exam Trap**

An absence of errors does not establish that scraping is configured correctly. Conversely, if the scenario reported ingestion-related `429` errors, checking the write quota in A would become appropriate.

**Foundation Concept**

Metrics must be exposed, discovered, scraped, ingested, and queried. Troubleshooting should isolate the failing stage. A working application and a running collector do not establish that the collector has a valid target.

**Real-World Connection**

For example, a pod might declare its metrics port as `metrics`, while `PodMonitoring` references `http-metrics`. Align the names, then inspect target status and verify that samples appear. This addresses collection configuration without unnecessary dashboard installation or IAM changes. 

**Memory Hook**

Silent missing metrics in managed collection call for checking the exporter and scrape configuration.

**30-Second Exam Takeaway**

For managed Prometheus collection with no metrics and no errors, validate the `PodMonitoring` port, selectors, namespace, and exposed endpoint before pursuing unsupported quota or permission hypotheses.

**Official References**

  * [**Google Cloud — Troubleshooting Managed Service for Prometheus:**](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting)Supports: The missing-metrics symptom, valid-port checks, quota-error distinction, and troubleshooting independently of Grafana.

  * [**Google Cloud — Get started with managed collection:**](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed)

Supports: `PodMonitoring` target selection, endpoint ports, and target-status verification.

  * [**Google Cloud Monitoring — Control access with IAM:**](https://docs.cloud.google.com/monitoring/access-control)

Supports: Monitoring Services Viewer versus Monitoring Metric Writer permissions.

---

## Question 22

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You operate applications on Google Kubernetes Engine (GKE) clusters distributed across several Google Cloud projects. You need a centralized, scalable approach to collect their Prometheus metrics and analyze them using a flexible query language. Which solution follows Google-recommended practices?

- [ ] A. Deploy a Prometheus server on an administration cluster with cluster autoscaling enabled, and expose its endpoint for queries.
- [ ] B. Use the Ops Agent to collect metrics, and query the collected data through Metrics Explorer.
- [x] C. Configure Google Cloud Managed Service for Prometheus with managed collection, and query the collected metrics through Metrics Explorer.
- [ ] D. Deploy a Prometheus server as an application sidecar in each cluster, and query the metrics through Cloud Monitoring.

### Explanation

**Correct Answer**

**C. Configure Google Cloud Managed Service for Prometheus with managed collection, and query the collected metrics through Metrics Explorer.**

**Exam Reasoning Explanation**

The solution must provide scalable collection, visibility across projects, and expressive querying. Managed Service for Prometheus supplies the managed backend and recommended Kubernetes collection approach, while Metrics Explorer supports PromQL. Configure cross-project visibility through a metrics scope rather than operating a central Prometheus server yourself.

This aligns with objective 4.1, which explicitly includes collecting metrics through Google Cloud Managed Service for Prometheus. 

**Key Exam Clues**

  * **“GKE clusters” — Technical signal:** Favors managed collection designed for Kubernetes.

  * **“Several Google Cloud projects” — Hard constraint:** Requires cross-project query visibility.

  * **“Centralized, scalable” — Hard constraint:** Requires a shared monitoring backend that scales beyond individual servers.

  * **“Flexible query language” — Technical signal:** PromQL provides expressive querying of Prometheus metrics.

**Why This Is Correct**

Google recommends managed collection for Kubernetes environments. It handles collector configuration and ingestion scaling, avoiding the operational burden of maintaining Prometheus servers. 

Metrics Explorer supports PromQL queries against the managed metrics. To query across projects, add the relevant projects to the metrics scope of a designated scoping project and provide appropriate access. Enabling collection alone does not automatically establish cross-project visibility. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** A central Prometheus server can collect and expose metrics, but you remain responsible for its configuration, storage, availability, and scaling. Cluster autoscaling does not remove those responsibilities. Managed collection directly addresses this operational burden. 

  * **Option B — Different Use Case:** The Ops Agent can scrape Prometheus metrics from Compute Engine VMs. For Kubernetes workloads, Google recommends managed collection instead. Metrics Explorer is an appropriate query interface, but the proposed collector does not match the recommended GKE approach. 

  * **Option D — Different Use Case:** Application-side Prometheus servers create separate collection and storage instances. As written, this does not establish ingestion into Cloud Monitoring’s shared backend; an explicit export integration would still be required. It also introduces per-application server management. 

**Exam Trap**

The Ops Agent supports Prometheus collection, so its name alone does not make B incorrect. The deployment environment resolves the choice: if these workloads ran on Compute Engine VMs, an Ops Agent configured with its Prometheus receiver could be appropriate. 

**Foundation Concept**

Collection determines which metrics reach the backend; query scope determines which projects’ metrics a user can analyze. A centralized view does not require physically relocating every project’s metrics into one project—the metrics scope combines visibility at query time. 

**Real-World Connection**

Enable managed collection on each cluster and define `PodMonitoring` resources for application metrics endpoints. Then query from a scoping project containing the participating projects. This provides consistent collection and shared analysis without maintaining a Prometheus server for every application. 

**Memory Hook**

For standard GKE Prometheus monitoring, use managed collection, PromQL, and a metrics scope for cross-project visibility.

**30-Second Exam Takeaway**

Choose managed collection for Prometheus metrics on GKE. Use Metrics Explorer’s PromQL support and configure a multi-project metrics scope when the applications span projects.

**Official References**

  * [**Google Cloud — Managed Service for Prometheus:**](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus)

Supports: Recommended Kubernetes collection, managed scaling, self-deployed collection trade-offs, and the Ops Agent’s VM use case.

  * [**Google Cloud — Query using Cloud Monitoring:**](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-cm)

Supports: Metrics Explorer, PromQL, shared backend access, and cross-project metrics scopes.

  * [**Google Cloud — Get started with managed collection:**](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed)

Supports: Application endpoint scraping through `PodMonitoring` resources.

---

## Question 23

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You manage a retail website composed of several microservices running in a Google Kubernetes Engine (GKE) Standard node pool with cluster autoscaling enabled. Each microservice has resource limits and a Horizontal Pod Autoscaler (HPA) configured.

During peak traffic, you receive alerts for one microservice. You discover that half of its Pods report `OOMKilled` container terminations, while its replica count remains at the HPA’s configured minimum. You need to resolve the issue. What should you do?

- [ ] A. Change the node pool’s machine type to one with more memory.
- [ ] B. Increase the maximum number of nodes allowed in the node pool.
- [ ] C. Increase the maximum replica count configured for the Horizontal Pod Autoscaler.
- [x] D. Increase the memory resource limit configured for the affected microservice.

### Explanation

**Correct Answer**

**D. Increase the memory resource limit configured for the affected microservice.**

**Exam Reasoning Explanation**

The strongest indication is insufficient memory available to the affected containers. Increasing their memory limit directly addresses container-level OOM terminations. The replica count being at its minimum also indicates that raising the HPA’s maximum is unlikely to help. 

**Key Exam Clues**

  * **Technical signal:** `OOMKilled` indicates an out-of-memory termination.

  * **Configuration clue:** Each microservice has resource limits.

  * **Scaling clue:** The workload remains at its minimum replica count, rather than reaching its maximum.

**Why This Is Correct**

Kubernetes enforces each container’s configured memory limit. When a container exceeds that boundary, it can be terminated even when its node has free memory. Increase `resources.limits.memory` to accommodate the application’s peak requirements. 

**Why the Other Options Are Not the Best Fit**

  * **A — Technically Possible but Not Best:** Larger nodes can address node-level memory exhaustion. However, additional node memory does not change an existing container memory limit. 

  * **B — Different Use Case:** Increasing the node pool maximum helps when unschedulable Pods require additional nodes and the existing maximum prevents expansion. It does not increase memory limits for running containers. 

  * **C — Incorrect for the stated symptoms:** Increasing `maxReplicas` raises the scaling ceiling; it does not itself trigger additional replicas. HPA scales according to configured metrics and does not adjust container memory limits. 

**Exam Trap**

`OOMKilled` can also result from node-level memory exhaustion. In production, confirm which boundary was exceeded. For this question, **D is the best fit** given the configured limits and absence of evidence of node pressure. 

**Foundation Concept**

These settings control different resources:

  * **Memory limit:** Memory a container may consume.

  * **HPA:** Number of workload replicas.

  * **Cluster autoscaler:** Number of nodes available to schedule Pods. 

**Real-World Connection**

Inspect the affected container’s termination details and memory consumption. After adjusting its limit, review memory requests for appropriate scheduling and investigate whether a memory leak contributed to the failures. 

**Memory Hook**

Match the corrective action to the resource boundary that is failing.

**30-Second Exam Takeaway**

Choose **D**. Container memory exhaustion calls for an appropriate memory limit; increasing a scaling maximum does not automatically provide that memory.

**Official References**

  * [**Troubleshoot OOM events**](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/oom-events)  
Supports: Container-level versus node-level OOM events, memory limits, and remediation.

  * [**Horizontal Pod autoscaling**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler)  
Supports: Metric-driven replica scaling and its distinction from node scaling.

  * [**About GKE cluster autoscaling**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler)  
Supports: Node expansion for unschedulable Pods based on resource requests.

---

## Question 24

*Domain 2: Building and Implementing CI/CD Pipelines*

You are designing a CI/CD pipeline that packages an application into container images. Images must reach Artifact Registry only after a vulnerability scan confirms there are no critical findings. You also want to minimize ongoing pipeline maintenance. Which approach best satisfies both requirements?

- [ ] A. Build and publish the image using a custom script on a VM. Use Artifact Analysis automatic scanning after publication and delete the image if critical vulnerabilities are found.
- [x] B. Build the image with Cloud Build. Run Artifact Analysis On-Demand Scanning before publication and push the image to Artifact Registry only if no critical vulnerabilities are found.
- [ ] C. Build the image using Jenkins installed on a VM. Run Artifact Analysis On-Demand Scanning before publication and push the image to Artifact Registry only if no critical vulnerabilities are found.
- [ ] D. Build and publish the image using Cloud Build. Use Artifact Analysis automatic scanning after publication and delete the image if critical vulnerabilities are found.

### Explanation

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

---

## Question 25

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your company operates several applications on Google Kubernetes Engine (GKE) and Cloud Run. You intend to use BigQuery as the central repository for application logs. You need to consolidate log collection and analysis to understand system health and performance while keeping configuration complexity and costs low. What should you do?

- [ ] A. Modify each application to send its logs directly to BigQuery through the BigQuery API.
- [ ] B. Collect the GKE and Cloud Run logs through Datadog, and forward them from Datadog to BigQuery.
- [x] C. Use Cloud Logging to collect logs from GKE and Cloud Run, and configure a log sink that routes them to BigQuery.
- [ ] D. Download the application logs from GKE and Cloud Run, and manually upload them to BigQuery through the Google Cloud console.

### Explanation

**Correct Answer**

**C. Use Cloud Logging to collect logs from GKE and Cloud Run, and configure a log sink that routes them to BigQuery.**

**Exam Reasoning Explanation**

BigQuery is the required destination; simplicity and cost efficiency guide the collection method. Use the platforms’ existing logging integrations and configure routing centrally. This avoids adding delivery logic to every application, an intermediary platform, or recurring manual transfers.

Exam objective 4.2 explicitly covers exporting and retaining logs through destinations such as BigQuery. 

**Key Exam Clues**

  * **“GKE and Cloud Run” — Technical signal:** Both platforms integrate with Cloud Logging.

  * **“BigQuery as the central repository” — Hard constraint:** Logs must reach BigQuery for centralized analysis.

  * **“Configuration complexity and costs low” — Preference:** Favors native collection and managed routing over additional integrations.

**Why This Is Correct**

GKE’s managed logging integration collects system and application logs when the relevant collection settings are enabled. Cloud Run automatically collects supported application output, including `stdout` and `stderr`, along with platform-generated logs. 

A Cloud Logging sink filters incoming entries and routes matching logs to a BigQuery dataset. Authorize the sink’s writer identity to write to the destination, including the appropriate BigQuery permissions. This provides centralized routing without requiring each application to implement BigQuery ingestion. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** Direct API writes can populate BigQuery, but each application must maintain its own delivery integration. Native collection and a sink avoid that repeated implementation work. 

  * **Option B — Different Use Case:** Datadog provides an additional observability platform, but this proposal inserts another collection and forwarding layer. The scenario does not require its capabilities, and Cloud Logging already supports the required BigQuery destination. 

  * **Option D — Technically Possible but Not Best:** Manual uploads can transfer selected historical files, but repeated downloading and uploading creates operational work and delays analysis. A sink provides managed routing as new logs arrive. 

**Exam Trap**

A central repository does not require every application to write directly to it. Separate log production from delivery. Also, native routing does not make storage free: Log Router has no additional charge, but destination storage charges still apply. 

**Foundation Concept**

A logging architecture separates four responsibilities: producing events, collecting them, routing selected records, and analyzing stored data. Centralizing routing lets administrators change destinations and filters without updating every application.

**Real-World Connection**

Standardize structured application logs, verify collection from both platforms, and configure a sink filter that retains the records needed for troubleshooting and performance analysis. Filtering unnecessary entries reduces the data sent to BigQuery while keeping routing rules centrally maintained. 

**Memory Hook**

For GKE and Cloud Run logs destined for BigQuery, use native collection plus a Cloud Logging sink.

**30-Second Exam Takeaway**

When supported Google Cloud services need centralized log analysis in BigQuery, prefer Cloud Logging and a sink. Direct application writes, extra platforms, and manual transfers add work unless another requirement specifically justifies them.

**Official References**

  * [**Google Kubernetes Engine — About GKE logs:**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs)

Supports: Managed log collection, workload logging settings, structured logging, and BigQuery export.

  * [**Google Cloud Run — Logging and viewing logs:**](https://docs.cloud.google.com/run/docs/logging)

Supports: Automatic collection from supported application outputs and platform-generated logs.

  * [**Google Cloud Logging — Route logs to supported destinations:**](https://docs.cloud.google.com/logging/docs/export/configure_export_v2)

Supports: BigQuery sinks, inclusion filters, destination permissions, and managed routing instead of application-specific or manual delivery.

  * [**Google Cloud Observability — Pricing:**](https://cloud.google.com/products/observability/pricing)

Supports: No additional Log Router charge and applicable destination storage charges.

---

## Question 26

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your company is developing an ecommerce application for deployment on Google Cloud. You need to periodically exercise the production checkout process, verify that it works correctly, and confirm that failures generate automated notifications. You want to minimize ongoing administration while following Google-recommended practices. What should you do?

- [ ] A. Create a Workflows workflow that validates checkout functionality, and use Cloud Tasks to invoke it periodically.
- [x] B. Implement a Cloud Run function for synthetic monitoring, and configure an alerting policy for test failures.
- [ ] C. Create a log-based alerting policy in Cloud Logging that detects failure messages generated during checkout.
- [ ] D. Configure an uptime check for the application, and create an alerting policy for check failures.

### Explanation

**Correct Answer**

**B. Implement a Cloud Run function for synthetic monitoring, and configure an alerting policy for test failures.**

**Exam Reasoning Explanation**

The mandatory requirements are active checkout testing and failure notifications. Minimizing administration favors managed test execution and alerting over custom orchestration. Select synthetic monitoring because the target is a business workflow, rather than endpoint availability alone.

Exam objective 4.1 explicitly covers synthetic monitors that proactively probe application endpoints and workflows. 

**Key Exam Clues**

  * **“Periodically exercise the production checkout process” — Hard constraint:** Requires scheduled execution of application functionality.

  * **“Verify that it works correctly” — Technical signal:** Requires assertions about checkout behavior.

  * **“Failures generate automated notifications” — Hard constraint:** Requires an alerting policy and notification channels.

  * **“Minimize ongoing administration” — Preference:** Favors integrated scheduling, execution, and monitoring.

**Why This Is Correct**

Cloud Monitoring synthetic monitors execute test scripts deployed as second-generation Cloud Run functions. The scripts can interact with web pages or APIs, perform checkout steps, and assert expected results. Cloud Monitoring manages recurring execution and records outcomes; an associated alerting policy sends failure notifications through configured channels. Google specifically identifies ecommerce checkout testing as a synthetic monitoring use case. 

Configure the function through a synthetic monitor so that scheduling and result collection are included.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** Workflows can orchestrate validation, but Cloud Tasks dispatches individually configured tasks. It does not provide Cloud Scheduler’s recurring cron-job behavior. Building recurrence and monitoring around this approach adds administration. 

  * **Option C — Different Use Case:** Log-based alerts notify you when incoming logs match specified criteria. They can detect recorded checkout errors, but they do not independently execute checkout transactions. This option therefore misses the active-testing requirement. 

  * **Option D — Different Use Case:** Uptime checks validate endpoint responses and can generate alerts. However, their requests are independent and stateless; they do not directly reproduce a checkout journey involving a sequence of interactions. 

**Exam Trap**

An application can return a successful HTTP response while checkout is broken. Uptime checks can validate response content, but that capability does not make them a scripted transaction test. If the requirement were only endpoint availability, D would be appropriate.

**Foundation Concept**

Match monitoring depth to the behavior being verified: endpoint checks assess individual responses, synthetic transactions exercise workflows, and log-based alerts detect recorded events. Each provides useful evidence, but they answer different operational questions.

**Real-World Connection**

Create a checkout test using controlled test data and meaningful success assertions. Connect its alerting policy to the operational notification channel, then perform a controlled failing test to verify delivery. This validates both the transaction checks and the notification path.

**Memory Hook**

For a recurring user journey with failure alerts, choose a synthetic monitor.

**30-Second Exam Takeaway**

Look for active testing of checkout, login, or another application workflow. Synthetic monitoring provides scripted validation with managed execution and integrated alerting; uptime checks and log alerts cover narrower needs.

**Official References**

  * [**Google Cloud Monitoring — Synthetic monitoring overview:**](https://docs.cloud.google.com/monitoring/uptime-checks/introduction)

Supports: Checkout testing, managed execution, and the distinction between synthetic monitors and uptime checks.

  * [**Google Cloud Monitoring — Create a synthetic monitor:**](https://docs.cloud.google.com/monitoring/synthetic-monitors/create)

Supports: Cloud Run function execution, test frameworks, scheduling, alerting policies, and notification channels.

  * [**Google Cloud — Compare Cloud Tasks to Cloud Scheduler:**](https://docs.cloud.google.com/tasks/docs/comp-tasks-sched)

Supports: Individual task scheduling versus recurring execution; option A’s additional orchestration requirements.

  * [**Google Cloud Logging — Configure log-based alerting policies:**](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts)

Supports: Notifications based on matching log entries; option C’s passive detection behavior.

---

## Question 27

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

Your company is developing a Java web application with AI capabilities. You must provide developers with a secure, managed, cloud-based Java integrated development environment (IDE). Each developer’s instance must have the GPUs required for development attached. Which approach follows Google-recommended practices?

- [ ] A. Create a dedicated development project with adequate GPU quota, and give developers access to Cloud Shell Editor for that project.
- [x] B. Provision a dedicated GPU-equipped workstation for each developer using Cloud Workstations, and grant developers the Cloud Workstations User role.
- [ ] C. Create an individual Google Cloud project for each developer, provision a GPU-equipped Compute Engine VM in each project, and grant the developer the Editor role.
- [ ] D. Provision a GKE cluster with GPU-equipped nodes, create a dedicated namespace for each developer, and grant each developer access to their namespace.

### Explanation

**Correct Answer**

**B. Provision a dedicated GPU-equipped workstation for each developer using Cloud Workstations, and grant developers the Cloud Workstations User role.**

**Exam Reasoning Explanation**

The mandatory requirements are a managed development environment, Java tooling, attached GPUs, and secure developer access. Select the service designed to provide developer workstations with configurable hardware and scoped permissions. Cloud Shell does not meet the hardware requirement, while individual VMs and Kubernetes workspaces require additional environment management.

**Key Exam Clues**

  * **“Managed, cloud-based Java … IDE” — Hard constraint:** Requires a development environment, beyond compute infrastructure alone.

  * **“GPUs … attached” — Hard constraint:** The workstation must support configurable accelerator hardware.

  * **“Secure” — Hard constraint:** Developer access should use permissions appropriate to workstation usage.

  * **“Google-recommended practices” — Preference:** Favors the purpose-built managed service and appropriately scoped IAM roles.

**Why This Is Correct**

Cloud Workstations configurations define the development tools, IDE image, machine settings, and GPU-compatible placement. Administrators can use a common configuration to provision consistent workstations for developers. GPU selection must match supported machine types and available zones. 

The Cloud Workstations User role, `roles/workstations.user`, provides workstation access. For a complete implementation, Google’s current access guide also lists Cloud Workstations Operation Viewer, `roles/workstations.operationViewer`, on the project. This additional setup detail does not change B as the best option. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Cloud Shell offers convenient browser-based development, making it tempting. However, its temporary backing VM is owned by Google and resides outside the developer’s projects. Allocating GPU quota to a development project does not attach GPUs to that Cloud Shell environment. 

  * **Option C — Technically Possible but Not Best:** GPU-equipped VMs can support Java development, but the company must configure and maintain the IDE environments. Project-level Editor access also grants broader permissions than workstation usage requires. Google permits basic roles in some development scenarios, so Editor is not universally prohibited; it is an inferior fit here. 

  * **Option D — Different Use Case:** GPU-backed Kubernetes infrastructure can run development workloads, but the proposed cluster and namespaces do not themselves supply the requested Java IDE. A workspace platform would still need to be configured and maintained. Cloud Workstations directly provides reproducible development environments through workstation configurations.

**Exam Trap**

Do not equate a managed browser editor with configurable development hardware. Cloud Shell’s project selection does not determine its backing VM’s GPU configuration. Without the GPU requirement, Cloud Shell could be suitable for some browser-based development tasks.

**Foundation Concept**

A managed development service combines configurable compute, development tooling, and access controls. Providing a GPU VM or container cluster supplies infrastructure; providing a developer workstation also requires configuring and maintaining the development environment.

**Real-World Connection**

Create a shared workstation configuration containing the approved Java tools and GPU settings, then provision individual workstations from it. Central configuration changes apply when workstations next start, reducing configuration drift and repeated setup work. An inactivity shutdown policy can also reduce idle compute spending.

**Memory Hook**

For managed developer IDEs that need attached GPUs, consider Cloud Workstations with workstation-scoped access.

**30-Second Exam Takeaway**

When a question combines managed cloud development, configurable GPUs, and controlled developer access, choose Cloud Workstations. The most specific blueprint objective is enabling secure cloud development environments. 

**Official References**

  * [**Google Cloud Workstations — Create a workstation configuration:**](https://docs.cloud.google.com/workstations/docs/create-configuration)

Supports: IDE configuration, GPU-compatible placement, reusable environments, inactivity shutdown, and the distinction from assembling VM or Kubernetes workspaces.

  * [**Google Cloud Workstations — Access control with IAM:**](https://docs.cloud.google.com/workstations/docs/access-control)

Supports: Cloud Workstations User and Operation Viewer roles.

  * [**Google Cloud — How Cloud Shell works:**](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works)

Supports: Google-owned backing VMs and why development-project GPU quota does not configure Cloud Shell hardware.

  * [**Google Cloud IAM — Use IAM securely:**](https://docs.cloud.google.com/iam/docs/using-iam-securely)

Supports: Least privilege, narrow permission scope, and the qualified use of basic roles in development environments.

---

## Question 28

*Domain 2: Building and Implementing CI/CD Pipelines*

You are deploying a containerized application to Cloud Run. The application requires a password to connect to a database and retrieve data. Your company’s security policy requires the password to be rotated weekly. You need a solution that minimizes the ongoing effort required to manage password rotation. What should you do?

- [ ] **A.** Deploy the application to Cloud Run. Each week, build a new container image with the updated database password configured as an environment variable in the Dockerfile. Deploy the image and migrate traffic to the new revision.
- [ ] **B.** Store the database password in Secret Manager. Deploy the application to Cloud Run and expose the secret’s `latest` version as an environment variable. Add a new secret version containing the updated password each week.
- [ ] **C.** Deploy the application to Cloud Run. Each week, build a new container image and supply the updated database password as a build-time secret. Deploy the image and migrate traffic to the new revision.
- [x] **D.** Store the database password in Secret Manager. Deploy the application to Cloud Run and mount the secret’s `latest` version as a volume. Add a new secret version containing the updated password each week.

### Explanation

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

---

## Question 29

*Domain 3: Applying Site Reliability Engineering Practices*

You manage the reliability of an internally developed, distributed file-storage service that processes thousands of uploads and downloads each day. You need to select a service level indicator (SLI) and use it to support alerts for potential service problems. Which metric best represents the reliability experienced when using the service?

- [ ] A. Mean response time of API operations such as `get`, `put`, and `list`.
- [ ] B. Count of successfully completed file uploads and downloads per minute.
- [ ] C. Mean size of the objects stored by the service.
- [x] D. Number of successful API calls divided by the total number of attempted API calls.

### Explanation

**Correct Answer**

**D. Number of successful API calls divided by the total number of attempted API calls.**

**Exam Reasoning Explanation**

The indicator should show whether users can successfully perform operations. A success ratio directly measures that outcome while accounting for changing request volume. Latency measures responsiveness, successful-operation counts measure throughput, and object size describes the workload. D therefore provides the strongest measure of operational availability.

**Key Exam Clues**

  * **“Uploads and downloads” — Technical signal:** Reliability should reflect whether requested operations succeed.

  * **“Thousands … each day” — Technical signal:** Request outcomes provide a useful population of measurable events.

  * **“Reliability experienced when using the service” — Hard constraint:** Prefer a user-outcome measure over workload characteristics.

  * **“Support alerts” — Technical signal:** The indicator should support comparison against a defined reliability objective.

**Why This Is Correct**

Google’s SRE guidance recommends expressing SLIs as good events divided by total events. For request-driven availability:

\\[ \text{Availability SLI} = \frac{\text{Successful API calls}}{\text{Total attempted API calls}} \\]

Both counts must cover the same measurement period and request population. The result is dimensionless and can be expressed as a percentage. For example, \\(9{,}990/10{,}000 \times 100 = 99.9\%\\). 

For implementation, explicitly define eligible requests and successful completion so that the measurement reflects the service contract. Google commonly defines request-based availability using well-formed requests that succeed. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** Latency is a valid SLI for responsiveness, but it does not directly measure successful completion. Requests can fail quickly while average latency remains low. Averages can also conceal slow requests in the distribution’s tail.

  * **Option B — Different Use Case:** Successful operations per minute measures throughput. Without total attempts, it cannot distinguish reduced demand from increased failures or reveal the fraction of users whose operations fail.

  * **Option C — Different Use Case:** Average object size helps characterize storage workloads and capacity needs. It does not indicate whether uploads or downloads complete successfully.

**Exam Trap**

A large number of successful operations can coexist with many failures. The denominator reveals the fraction of attempted work that succeeds. If the requirement instead asked for successful processing volume per minute, B would be appropriate.

**Foundation Concept**

An SLI measures observed service behavior; an SLO sets the target for that behavior. Success ratio measures availability, while latency and durability capture additional aspects of storage reliability. One indicator does not fully describe every user expectation.

**Real-World Connection**

Instrument attempted and successful operations, then define an availability SLO using their ratio. Configure error-budget burn-rate alerts to notify the team when failures threaten that objective. This ties alerts to reliability impact rather than ordinary changes in traffic volume. 

**Memory Hook**

To measure whether operations work, divide successful attempts by total attempts.

**30-Second Exam Takeaway**

For request-based availability, look for a success ratio with a meaningful denominator. Counts describe volume, latency describes speed, and neither alone establishes the proportion of successful operations.

**Official References**

  * [**Google SRE Workbook — Implementing SLOs:**](https://sre.google/workbook/implementing-slos/)

Supports: Good-event ratios, request-based availability, and the relationship between SLIs and SLOs.

  * [**Google SRE Book — Service Level Objectives:**](https://sre.google/sre-book/service-level-objectives/)

Supports: Availability, latency, throughput, durability, and the limitations of averages.

  * [**Google Cloud Observability — Alerting on your burn rate:**](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/alerting-on-budget-burn-rate)

Supports: Using SLO-based error-budget alerts to detect reliability risks.

  * [**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)

Supports: Objective 3.1, covering the definition of SLIs, SLOs, and error budgets.

---

## Question 30

*Domain 2: Building and Implementing CI/CD Pipelines*

Your team needs to debug a live issue affecting a workload running in a Google Kubernetes Engine (GKE) cluster that has Binary Authorization enabled. To investigate, you want to launch a short-lived diagnostic Pod using an unsigned utility image pulled from Artifact Registry. When you apply the Pod manifest, the Binary Authorization policy blocks the deployment. You need the approach that lets the Pod run while keeping the deployment as secure and auditable as possible. What should you do?

- [ ] A. Change the enforcementMode setting in the Binary Authorization policy to ALWAYS_ALLOW.
- [x] B. Add the image-policy.k8s.io/break-glass label to the Pod specification.
- [ ] C. Temporarily turn off Binary Authorization on the GKE cluster.
- [ ] D. Add the diagnostic image to the admissionWhitelistPatterns entry of the Binary Authorization policy.

### Explanation

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

---

## Question 31

*Domain 2: Building and Implementing CI/CD Pipelines*

Your company is rolling out supply chain security controls for its containerized applications running on Google Kubernetes Engine (GKE). You need the ability to trace a container image running in production back to the exact source and build process that produced it, and your solution needs to follow Google-recommended practice for software supply chain security. What should you do?

- [ ] A. Store every build artifact in Artifact Registry, and turn on automatic vulnerability scanning.
- [ ] B. Enable the Container Analysis API, configure Cloud Build to use only official base images, and turn on automatic vulnerability scanning.
- [ ] C. Run every GKE node pool on Container-Optimized OS, enable Binary Authorization on the cluster, and turn on automatic security updates.
- [x] D. Enable the Container Analysis API, configure Cloud Build to generate and sign build provenance attestations for every build, and configure Binary Authorization to verify those attestations before deployment.

### Explanation

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

---

## Question 32

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You are designing the hosting architecture on Google Kubernetes Engine (GKE) for a set of business-critical applications. These applications already expose custom metrics in Prometheus format for monitoring. You need to collect these application metrics so they can be used for alerting and troubleshooting. You want to minimize ongoing manual effort and maintenance while following Google-recommended practices. What should you do?

- [ ] A. Deploy your own Prometheus servers inside the GKE clusters, and configure them to scrape the custom metrics and forward the data to the Cloud Monitoring API.
- [ ] B. Deploy the OpenTelemetry Collector inside the GKE clusters, and configure it to collect and export the custom metrics to Cloud Monitoring.
- [ ] C. Change each application so it pushes its custom metrics directly to Cloud Monitoring through the Cloud Monitoring API.
- [x] D. Enable Google Cloud Managed Service for Prometheus collection on the GKE clusters to collect the custom metrics.

### Explanation

**Correct Answer**

**D. Enable Google Cloud Managed Service for Prometheus collection on the GKE clusters to collect the custom metrics.**

**Exam Reasoning Explanation**

Separate the hard requirement from the preferences. The hard requirement is: collect Prometheus-format custom metrics from GKE workloads for alerting and troubleshooting. The preferences are: minimize manual effort/maintenance, and follow Google’s recommended practice. All four options can technically get the metrics into Cloud Monitoring, so the preferences decide the answer. Managed Service for Prometheus is Google’s purpose-built, fully managed Prometheus-compatible service for exactly this scenario: it ingests standard Prometheus-exposed metrics from GKE workloads without you operating the Prometheus server stack yourself, and Google explicitly documents it as the solution that avoids manually managing and operating Prometheus at scale. That satisfies both preferences at once, which is why it beats the other three, each of which trades away one of them.

**Key Exam Clues**

  * **“provide custom metrics for monitoring with Prometheus”** — a technical-signal clue: the applications already speak the Prometheus exposition format, so the answer should consume that format natively rather than requiring re-instrumentation.

  * **“for alerting and troubleshooting purposes”** — tells you the destination needs to be Cloud Monitoring (where alerting policies and dashboards live), ruling out any option that stops short of getting data there.

  * **“minimize the amount of manual effort and maintenance required”** — a decisive preference/exclusion clue: it eliminates any option that makes you operate infrastructure (a self-run Prometheus server) or rewrite application code.

  * **“following Google-recommended practices”** — points directly at the option Google documents as its recommended, fully managed path for this exact use case.

**Why This Is Correct**

Google Cloud Managed Service for Prometheus is Google’s fully managed Prometheus-compatible collection and storage backend. On GKE it can scrape Prometheus-format metrics, including your applications’ custom metrics, and send them into Cloud Monitoring, where they become available for alerting policies, dashboards, and PromQL-based troubleshooting. Because collection is managed by Google and is enabled by default on GKE clusters (with configuration needed only to pick up additional, non-system metrics like your custom ones), you avoid standing up, scaling, and operating a Prometheus server yourself.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** Running your own Prometheus servers in-cluster absolutely works and is the traditional way to scrape Prometheus metrics, but you take on everything Managed Service for Prometheus exists to remove: sizing, scaling, storage, and high availability for the Prometheus server itself. That directly conflicts with “minimize manual effort and maintenance.”

  * **Option B — Technically Possible but Not Best:** The OpenTelemetry Collector can scrape Prometheus-format metrics and export them (including to Managed Service for Prometheus as a backend), so it’s a legitimate pattern in some architectures. But deploying and configuring your own collector is additional infrastructure you have to manage, and it isn’t Google’s primary recommended, lowest-effort path when your workloads already emit standard Prometheus metrics on GKE — enabling the managed collection directly is simpler and requires no collector of your own.

  * **Option C — Violates Requirement:** Rewriting every application to push metrics via the Cloud Monitoring API means touching application code for every service, discarding the Prometheus instrumentation you already have. This is the most manual-effort-intensive option of the four, the opposite of what the scenario asks for.

**Exam Trap**

The trap is treating A, B, and D as interchangeable because they all “get Prometheus metrics into Cloud Monitoring.” The question is decided by the maintenance-burden qualifier, not by capability — once you notice “minimize manual effort and maintenance” plus “Google-recommended,” the fully managed service is the only option that doesn’t require you to run or configure a collection component yourself.

**Foundation Concept**

When a workload already speaks a standard metrics protocol (here, Prometheus exposition format), the lowest-maintenance integration path is almost always a managed, protocol-compatible collector service rather than (a) a self-hosted version of the same open-source tool, (b) a general-purpose collector you must configure yourself, or (c) changing the application to speak a different, proprietary API.

**Real-World Connection**

A platform team that self-hosts Prometheus for dozens of GKE clusters typically ends up owning its own on-call rotation just for Prometheus storage and scaling issues. Switching the same workloads to Managed Service for Prometheus collection removes that operational surface entirely while keeping the same PromQL queries, dashboards, and alerting workflows the team already built.

**Memory Hook**

Already emitting Prometheus metrics on GKE and want the lowest-maintenance path into Cloud Monitoring → Google Cloud Managed Service for Prometheus.

**30-Second Exam Takeaway**

Whenever a GKE question stresses “custom/application Prometheus metrics,” “minimize manual effort,” and “Google-recommended,” the answer is almost always Google Cloud Managed Service for Prometheus rather than a self-run Prometheus server, a generic collector, or application code changes.

**Official References**

[Google Cloud — Managed Service for Prometheus overview (metrics collection on GKE): ](https://cloud.google.com/monitoring/integrate/gke)Supports: the correct-answer mechanism (fully managed, Google-recommended Prometheus-compatible collection on GKE)

[Google Cloud — Collect specific Prometheus metrics on GKE: ](https://cloud.google.com/kubernetes-engine/docs/how-to/collect-specific-prometheus-metrics)Supports: how custom/user-defined Prometheus metrics (beyond built-in system metrics) are configured for collection, distinguishing D from a default/no-config scenario

---

## Question 33

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your team operates a high-traffic application that produces several terabytes of log data every day. You need to lower your Cloud Logging costs without losing critical operational and security information. What should you do?

- [ ] A. Configure an exclusion filter that drops DEBUG-level logs, and set up an export of ERROR-level logs to BigQuery.
- [ ] B. Reduce the retention period for the _Default logging bucket from its current setting down to 15 days.
- [ ] C. Turn on sampling across every log severity level in the _Default logging bucket.
- [x] D. Build log-based metrics for the key indicators you care about, and configure an exclusion filter that drops all non-ERROR logs.

### Explanation

**Correct Answer**

**D. Build log-based metrics for the key indicators you care about, and configure an exclusion filter that drops all non-ERROR logs.**

**Exam Reasoning Explanation**

Separate the hard requirement from the preference: the hard requirement is “retain critical operational and security information” (so nothing can silently drop ERROR-level or security-relevant entries), and the preference is “lower Cloud Logging costs” for a workload whose dominant cost driver is ingestion volume, not retention length. An exclusion filter on everything except ERROR logs attacks the actual volume driver directly — the non-error traffic/debug noise that makes up the bulk of “several terabytes daily” — while leaving ERROR logs flowing into Cloud Logging untouched. Log-based metrics then recover the operational visibility you’d otherwise lose from the excluded logs, because metric evaluation happens independently of exclusion filtering, so a metric can still count and track key indicators even from logs that are never stored or billed as ingested volume. That combination is the only option that meaningfully cuts the real cost driver while provably keeping both the critical logs and ongoing visibility intact.

**Key Exam Clues**

  * **“several terabytes of logs daily”** — a technical signal that the cost problem is ingestion volume, which points toward exclusion/filtering rather than a retention-period tweak.

  * **“retaining critical operational and security information”** — a hard constraint/exclusion signal: any option that could drop ERROR-level or security-relevant entries, even partially, fails this requirement outright.

  * **“reduce Cloud Logging costs”** — favors the option that removes the largest share of billed log volume, not the option with the smallest or most indirect cost effect.

  * **“non-ERROR logs”** in option D vs **“DEBUG logs”** in option A — a scope clue: excluding only DEBUG leaves other high-volume levels (such as INFO-level request logs typical of a high-traffic app) fully billed, while excluding everything except ERROR removes far more of the volume.

**Why This Is Correct**

Cloud Logging’s exclusion filters prevent matching log entries from being ingested into a bucket (and billed), so excluding all non-ERROR logs removes the great majority of a high-traffic application’s log volume at the source. Because ERROR logs are explicitly left out of the exclusion, they keep flowing into Cloud Logging exactly as before, satisfying the “critical operational and security information” requirement. Layering log-based metrics on top closes the remaining gap: a log-based metric’s filter is evaluated against the log stream independently of exclusion filters, so you can still track counts or trends for key indicators (for example, warning rates or specific event types) drawn from logs that are no longer stored, at a fraction of the cost of retaining the full log volume.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** Excluding only DEBUG-level logs leaves every other non-error level (most notably INFO, which is typically where high-volume per-request logging lives) fully ingested and billed, so it addresses only a slice of the actual volume problem. Exporting ERROR logs to BigQuery is also reasonable for durable analysis, but on its own it adds a second storage destination rather than removing cost, and nothing in this option stops ERROR logs from also continuing to be stored (and billed) in the _Default bucket.

  * **Option B — Violates Requirement:** Cloud Logging’s cost driver for a high-volume workload is ingestion, not how long data sits in the bucket afterward, so shortening retention from 30 to 15 days does little to address “several terabytes daily.” Worse, it shortens how long operational and security logs remain available for investigation, directly working against “retaining critical operational and security information.”

  * **Option C — Violates Requirement:** Applying sampling indiscriminately across every severity level means a fraction of ERROR and security-relevant log entries gets dropped right along with the low-value noise. That’s the one outcome the scenario explicitly rules out — losing some of the critical information you were told to keep.

**Exam Trap**

The trap is assuming “any filtering or sampling mechanism that cuts volume” is equally valid. The scenario’s real constraint is which logs you’re allowed to touch: DEBUG-only filtering (A) is too narrow, retention shortening (B) doesn’t touch volume at all, and blanket sampling (C) touches the one category you must not touch (ERROR/security). Only D’s “exclude everything except ERROR” scope satisfies both the cost goal and the retention constraint simultaneously.

**Foundation Concept**

In Cloud Logging, cost control and information retention are solved by two different mechanisms that can be combined: exclusion filters decide what gets stored (and billed) at all, while log-based metrics let you keep lightweight, aggregated visibility into logs you’ve chosen not to store in full. Treating “what do I keep in full,” “what do I just count,” and “what do I drop entirely” as three separate decisions — rather than one blanket setting — is what lets you cut cost without losing the signal you actually need.

**Real-World Connection**

A team that applies a single blunt setting, like reducing retention or sampling everything uniformly, often discovers the gap only during an incident or security review, when the exact log entries needed are missing. A team that excludes low-value logs by category while routing key indicators through log-based metrics keeps both a low Cloud Logging bill and a reliable audit trail for the entries that actually matter operationally and for security.

**Memory Hook**

Cut cost by excluding everything except what must be kept (ERROR), and recover visibility into the rest with metrics, not by shortening retention or sampling indiscriminately.

**30-Second Exam Takeaway**

When a Cloud Logging cost question also demands you keep critical/security information intact, look for the option that scopes exclusion precisely to the non-critical log levels and recovers lost visibility through log-based metrics — a retention-period change or blanket sampling will almost always risk the exact data you were told to protect.

**Official References**

[**Google Cloud — Exclusion filters in Cloud Logging**](https://cloud.google.com/logging/docs/exclusions)**:** Supports: the correct-answer mechanism (excluding non-ERROR logs from ingestion to cut cost) and the option C distinction (sampling via exclusion filters is meant to be scoped away from critical severities, not applied to all of them)

[Google Cloud — Control Dataflow log ingestion (exclusion filters and logs-based metrics): ](https://cloud.google.com/dataflow/docs/guides/filter-logs)Supports: the key technical fact that exclusion filters do not apply to user-defined logs-based metrics, which is why option D still provides visibility into excluded logs

---

## Question 34

*Domain 2: Building and Implementing CI/CD Pipelines*

You’re designing a containerized CI pipeline and want to reduce how much the pipeline depends on public upstream container registries, while improving build reproducibility and security. You need a design that caches every containerized dependency the pipeline uses, while keeping ongoing manual effort and maintenance to a minimum. What should you do?

- [ ] A.
    Create a remote Docker repository in Artifact Registry for each upstream registry you depend on.
    Have the CI pipeline pull container images directly through these remote repositories.
- [ ] B.
    Create a standard Docker repository in Artifact Registry for each upstream registry you depend on.
    Upload the container images used by the build pipelines into the appropriate repositories yourself.
- [ ] C.
    Create a standard Docker repository in Artifact Registry for each upstream registry you depend on.
    Create a single, central virtual Docker repository that fronts these standard repositories.
    Have the CI pipeline pull container images through the central virtual repository.
- [x] D.
    Create a remote Docker repository in Artifact Registry for each upstream registry you depend on.
    Create a single, central virtual Docker repository that fronts these remote repositories.
    Have the CI pipeline pull container images through the central virtual repository.

### Explanation

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

---

## Question 35

*Domain 2: Building and Implementing CI/CD Pipelines*

You manage a critical, high-traffic application running on Google Kubernetes Engine (GKE). You are about to release a new version that makes significant changes to the payment processing workflow. You need a deployment approach that minimizes risk and automatically rolls back the release if it turns out to be unstable. What should you do?

- [x] A. Use Cloud Deploy to run a canary deployment. Configure the delivery pipeline with a multi-phase canary sequence that starts at a 5% traffic split, define success criteria from application telemetry in Cloud Monitoring, and configure Cloud Deploy to automatically roll back the release if the new version fails verification.
- [ ] B. Configure your GKE deployment manifest to follow a blue-green pattern: deploy the new version as a “green” deployment next to the existing “blue” one, then, once “green” is live, update the Service selector to gradually move user traffic over to the new version.
- [ ] C. Edit the GKE Service manifest to add a selector for the v2 Pods, then create a second GKE Deployment for the new version, and gradually shift traffic by scaling the new Deployment’s replica count up while scaling the old Deployment’s replica count down.
- [ ] D. Use the GKE Deployment’s default rolling update strategy, monitor logs and metrics in Cloud Monitoring while it rolls out, and if a problem appears, run kubectl rollout undo to revert the application to the previous stable version.

### Explanation

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

---

## Question 36

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You manage a complex microservices application running on Google Kubernetes Engine (GKE), and you recently instrumented your services with OpenTelemetry to produce traces. While investigating performance in Cloud Trace, you spot a transaction with unusually high latency. The trace waterfall doesn’t give you enough detail to pin down the root cause, and you suspect the delay originates in the service’s business logic. This service already sends structured logs to Cloud Logging. You need to quickly analyze the logs that correspond to this specific high-latency request. What should you do?

- [ ] A. In the Cloud Trace waterfall view, note the trace ID of the slow request, then go to Logs Explorer and write a query filtering for log entries that contain that specific trace ID.
- [ ] B. Configure a log-based metric in Cloud Logging to count error-message occurrences, create an alerting policy on that metric so you’re notified of future issues, and analyze the logs tied to those alerts.
- [ ] C. Export all logs from Cloud Logging to BigQuery, then write a SQL query that joins the trace data with the log data on the trace ID field and filters for this specific transaction to find the related log entries.
- [x] D. Make sure your application’s logging configuration includes the trace ID from the OpenTelemetry context in every structured log entry, then, from the Cloud Trace details view for the slow request, click “Show logs” to see the correlated logs directly alongside the trace’s span waterfall.

### Explanation

**Correct Answer**

**D. Make sure your application’s logging configuration includes the trace ID from the OpenTelemetry context in every structured log entry, then, from the Cloud Trace details view for the slow request, click “Show logs” to see the correlated logs directly alongside the trace’s span waterfall.**

**Exam Reasoning Explanation**

The hard requirement is “quickly analyze the logs that correspond to the high-latency request,” which means both correctness (you need the logs for that exact request, not a broader set) and speed (minimal manual steps). The scenario tells you logs are already structured and sent to Cloud Logging, but it never confirms those log entries actually carry the trace context — and that’s the real gap keeping you from correlating them with the slow trace. D is the only option that names this missing piece explicitly (include the trace ID from the OpenTelemetry context in each log entry) and then uses the single built-in, one-click mechanism Cloud Trace provides for viewing exactly those correlated logs next to the waterfall. Every other option either assumes the correlation already works, solves a different problem, or reaches for a slower, heavier mechanism than the one Google Cloud already provides for this.

**Key Exam Clues**

  * **“trace waterfall lacks the detail needed”** — tells you the trace data alone is insufficient; the fix must bring in a second data source (logs), not more trace configuration.

  * **“sends structured logs to Cloud Logging”** — a technical signal that logs exist, but doesn’t confirm they carry trace context, which is the actual precondition for correlation.

  * **“you need to quickly analyze the logs”** — a decisive preference clue: it favors the fastest, most integrated path over one requiring exports, joins, or separately built queries.

  * **“corresponds to the high-latency request”** — a scope clue: the goal is the logs for one specific request, which rules out any option built around aggregate counts or alerts.

**Why This Is Correct**

Cloud Logging and Cloud Trace correlate log entries to traces through a reserved trace field on the log entry; this only works if your logging configuration populates that field (here, from the OpenTelemetry trace context) on each structured log entry. Once that’s in place, the Cloud Trace details view for any request exposes a “Show logs” control on the waterfall graph that displays exactly the log entries associated with that trace, right alongside the spans — letting you go from “this request was slow” to “here’s what the business logic logged during this request” in essentially one click, with no separate query, export, or join required.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** Manually copying the trace ID and writing a Logs Explorer query is a legitimate way to view correlated logs, but it silently assumes the log entries already contain the trace field — if they don’t, the query returns nothing. It also requires an extra manual step (building and running a query) in a situation that calls for speed, when the trace details view already offers the same correlated logs directly.

  * **Option B — Different Use Case:** Counting error messages and alerting on them is a detection/monitoring pattern for catching future problems in aggregate. It does nothing to surface the logs for the one specific slow request you’ve already identified, and it doesn’t address the business-logic root cause you’re investigating right now.

  * **Option C — Technically Possible but Not Best:** Exporting the entire log volume to BigQuery and writing a SQL join can eventually get you the same correlated log entries, but it’s a heavyweight, batch-oriented path (export latency, storage/query cost, manual SQL) for a task the scenario explicitly asks you to do quickly, when the correlated view is already built into Cloud Trace.

**Exam Trap**

The trap is treating “the logs mention the trace ID” as a given rather than a configuration step. A learner who jumps straight to “query Logs Explorer by trace ID” (A) or “join on trace ID in BigQuery” (C) is assuming correlation already works, when the scenario’s real obstacle is that the trace waterfall alone isn’t enough — which is a strong hint that the missing piece is getting trace context into the logs in the first place, not just querying for it.

**Foundation Concept**

Distributed tracing and structured logging are complementary signals: traces show you timing and call structure across services, while logs show you what the code actually did. They become powerful together only when log entries carry the same trace (and span) identifiers as the trace itself, which lets tooling like Cloud Trace present both side by side instead of leaving you to manually stitch them together.

**Real-World Connection**

A team that instruments traces but never threads the trace ID into its structured logs ends up doing exactly the slow, manual correlation work options A and C describe every time they investigate a slow request. Teams that bake trace-ID propagation into their logging setup from the start get single-click, per-request log correlation for every future investigation, which is a large recurring time savings during incidents.

**Memory Hook**

No trace ID in the log entry, no correlation — fix the logging configuration first, then use Cloud Trace’s “Show logs,” not a manual query or export.

**30-Second Exam Takeaway**

When a question pairs “trace waterfall isn’t detailed enough” with “structured logs already exist,” check whether the logs actually carry the trace context before assuming you can just query for it — the Google-recommended, fastest path is ensuring trace-ID propagation into logs and then using Cloud Trace’s built-in correlated log view.

**Official References**

[Google Cloud — Link log entries with traces: ](https://cloud.google.com/trace/docs/trace-log-integration)Supports: the correct-answer mechanism (including the trace field in structured log entries and using “Show logs” in the Trace details pane) and the precondition that eliminates option A when correlation isn’t yet configured

---

## Question 37

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

You manage a Google Cloud environment that serves 20 different business units, with 50 production projects and 50 development projects all sitting directly under the organization node. This flat layout makes it hard to apply security policies consistently across every production project, and it’s difficult to track the aggregated costs of the production and development environments separately. You need to restructure the resource hierarchy to fix both problems. What should you do?

- [x] A. Create a folder for the production environment and a folder for the development environment, then move the corresponding projects into each folder.
- [ ] B. Create a separate folder for each business unit, then move that business unit’s projects into its folder.
- [ ] C. Apply a label identifying the environment to every project.
- [ ] D. Create a common services project for each business unit.

### Explanation

**Correct Answer**

**A. Create a folder for the production environment and a folder for the development environment, then move the corresponding projects into each folder.**

**Exam Reasoning Explanation**

There are two hard requirements here: security policies need to apply consistently across all production projects, and costs need to be tracked in aggregate separately for production versus development. In Google Cloud’s resource hierarchy, folders are the attachment point for IAM and Organization Policy inheritance, and they’re also a natural grouping boundary for billing and cost reports. Grouping all 50 production projects under one “Production” folder means one policy set at that folder cascades to every production project automatically, and grouping development projects under a separate folder gives you a clean boundary for aggregating development costs apart from production costs. Every other option either organizes along the wrong axis (business unit) or uses a mechanism (a label, a shared-services project) that isn’t actually a policy-inheritance or billing-aggregation boundary in Google Cloud.

**Key Exam Clues**

  * **“difficult to apply security policies consistently across all production projects”** — a technical signal pointing at IAM/Organization Policy inheritance, which in Google Cloud flows down from folders, not from labels or project-level settings.

  * **“track the aggregated costs of the production and development environments separately”** — a scope clue: the grouping needed is by environment specifically, not by business unit or by individual project.

  * **“this flat structure makes it difficult”** — tells you the fix is structural (resource hierarchy), ruling out an option (labels) that leaves the hierarchy flat and only adds metadata.

  * **“restructure the resource hierarchy”** — explicitly points you at folders/projects as the mechanism, not at billing labels or a services-centralization pattern.

**Why This Is Correct**

Folders in the Google Cloud resource hierarchy are both an IAM/Organization Policy inheritance point and a natural unit for grouping cost data. Moving all production projects into a single “Production” folder lets you set IAM bindings and organization policies once, at the folder, and have them apply to every current and future project placed in that folder — directly solving the “consistent security policy across production” problem. The same folder boundary lets you view and aggregate billing data at the folder level, so production and development costs can be tracked and reported separately without relying on per-project tagging discipline.

**Why the Other Options Are Not the Best Fit**

  * **Option B — Different Use Case:** Business-unit folders solve a different problem — delegating ownership or administrative autonomy to each business unit — not the one described here. Google’s own landing zone guidance specifically cautions against mapping your corporate org chart onto the resource hierarchy as the primary structure, and with business-unit folders, production and development projects for the same unit would sit in the same folder, making it harder, not easier, to apply one consistent policy to “all production projects” or to cleanly separate production and development costs.

  * **Option C — Violates Requirement:** A label can help you filter or break down a billing export by environment, so it partially helps with cost visibility, but labels are not an IAM or Organization Policy attachment point in Google Cloud — you cannot apply a security policy to “every project labeled production” the way you can to a folder. This option fails the “apply security policies consistently” requirement outright.

  * **Option D — Different Use Case:** A common services project per business unit is a pattern for centralizing shared infrastructure (such as a Shared VPC host project, logging, or security tooling) for that business unit. It doesn’t create any environment-wide policy inheritance boundary and doesn’t help separate production and development costs in aggregate.

**Exam Trap**

The trap is assuming that because the scenario mentions “20 business units,” the fix must be organized around business units. The scenario’s actual pain points — policy consistency across production, and separate environment-level cost tracking — are both environment problems, not business-unit problems, and Google Cloud’s own guidance explicitly favors environment-based (or sensitivity-based) folders over org-chart-based folders for exactly this kind of requirement.

**Foundation Concept**

In the Google Cloud resource hierarchy, IAM policies and Organization Policies flow downward from organization to folder to project, and folders are the recommended place to attach controls that should apply to a whole class of projects at once. Choosing the right folder axis — environment, sensitivity, business unit, or some combination — should be driven by which axis your policies and reporting actually need to group by, not by mirroring your company’s org chart by default.

**Real-World Connection**

An organization that structures folders by business unit alone often finds itself reapplying the same “production-grade” IAM bindings and Organization Policy constraints separately inside each business unit’s folder, with a high risk of drift as units update independently. Structuring folders by environment first lets a central platform or security team maintain one authoritative production policy set and one aggregated production cost view, regardless of how many business units contribute projects to it.

**Memory Hook**

Need one policy and one cost view across all production projects → a production folder (and a development folder), not a folder per business unit.

**30-Second Exam Takeaway**

When a resource-hierarchy question asks for consistent policy enforcement and separate cost tracking “across environments,” the answer is almost always environment-based folders — reach for business-unit folders only when the stated need is ownership, delegation, or billing isolation per business unit specifically.

**Official References**

[**Google Cloud — Decide your resource hierarchy (landing zone design)**](https://cloud.google.com/architecture/landing-zones/decide-resource-hierarchy)**:** Supports: the correct-answer mechanism (folders as the recommended grouping and policy-inheritance boundary) and the explicit caution against mapping business-unit/org-chart structure as the primary hierarchy axis, used to eliminate option B

[**Google Cloud — Security foundations blueprint: organization structure:**](https://cloud.google.com/architecture/security-foundations/organization-structure) Supports: Google’s own reference architecture, which groups projects into folders by environment specifically for consistent policy application

---

## Question 38

*Domain 2: Building and Implementing CI/CD Pipelines*

You need a pipeline that builds a containerized application from GitHub and publishes its image to Artifact Registry. Each new Git tag must automatically submit a build, but execution must wait for approval from a member of the `gcp-developers-admins@mountkirk.com` Google group.

Security policy prohibits static credentials and federation between Google Cloud IAM and external identity providers. Which configuration satisfies these requirements?

- [x] A. Create a GitHub-connected Cloud Build trigger for new tag pushes and enable required approval. Grant `roles/cloudbuild.builds.approver` to `gcp-developers-admins@mountkirk.com` and `roles/artifactregistry.writer` to the service account used to execute the builds.
- [ ] B. Create a GitHub Actions workflow that builds and publishes images on new tag pushes. Mirror the Google group’s membership into a GitHub team and require that team’s approval. Create a Google Cloud service account, download its key, and use the key to authenticate the workflow. Grant the service account `roles/artifactregistry.writer`.
- [ ] C. Generate an SSH key pair and register its public key as a GitHub repository deploy key. Configure an approval-required Cloud Build trigger that retrieves the repository using this key. Grant `roles/cloudbuild.builds.editor` to `gcp-developers-admins@mountkirk.com` and `roles/artifactregistry.writer` to the build service account.
- [ ] D. Create a GitHub Actions workflow that builds and publishes images on new tag pushes. Mirror the Google group’s membership into a GitHub team and require that team’s approval. Configure a Google Cloud workload identity pool that trusts the GitHub workflow identity, and grant the authorized federated principal `roles/artifactregistry.writer`.

### Explanation

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

---

## Question 39

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You’re responsible for a critical, user-facing application and have an SLO configured in Cloud Monitoring that targets 99% availability over a rolling 30-day window. A string of minor issues has recently driven up latency, and as a result the error budget is being consumed faster than expected. You want to be notified proactively if the service is at risk of breaching its SLO, ideally before the error budget runs out completely. What should you do?

- [ ] A. Configure a log-based metric in Cloud Monitoring that tracks the rate of application error log entries, then create an alerting policy on that metric that fires when the error rate shows a significant anomalous deviation from its historical baseline.
- [ ] B. Build a custom dashboard in Cloud Monitoring that visualizes SLO compliance percentage and remaining error budget, and configure the dashboard to email a scheduled daily report.
- [x] C. In Cloud Monitoring, create an alerting policy based on the SLO’s error budget burn rate, and configure it to fire when the current consumption rate is projected to exhaust the budget before the end of the 30-day compliance period.
- [ ] D. In Metrics Explorer, create an alerting policy based on the application load balancer’s average request latency, and configure it to fire when latency exceeds a predefined threshold.

### Explanation

**Correct Answer**

**C. In Cloud Monitoring, create an alerting policy based on the SLO’s error budget burn rate, and configure it to fire when the current consumption rate is projected to exhaust the budget before the end of the 30-day compliance period.**

**Exam Reasoning Explanation**

The hard requirement is being warned before the SLO is actually violated, based on the trajectory of error-budget consumption, not just on a raw symptom crossing a fixed line. That rules out anything that measures a side signal (error-log anomalies, latency thresholds) instead of the budget itself, and anything that isn’t forward-looking (a periodic report instead of a real-time, projection-based alert). Cloud Monitoring’s SLO burn-rate alerting is purpose-built for exactly this: it continuously evaluates how fast the error budget is being spent and can warn you specifically when, at the current rate, the budget would run out before the compliance window ends — which is precisely “at risk of violating the SLO before the budget is depleted,” stated almost word for word.

**Key Exam Clues**

  * **“99% availability over a 30-day rolling window”** — establishes the SLO and its compliance period, which is the denominator any proactive alert needs to reason about.

  * **“error budget to be consumed at an accelerated rate”** — a technical signal that the right alert should track the rate of consumption (burn rate), not a static error count or a fixed latency number.

  * **“proactively notified when the service is at risk of violating its SLO before the error budget is fully depleted”** — a decisive requirement clue: it specifically wants a forward-looking, budget-exhaustion-projecting alert, not a lagging report or a generic symptom alert.

  * **“minor issues have increased latency”** — tells you the root cause is latency-driven, but the thing you need to monitor and alert on is the SLO’s error budget, which already reflects the downstream effect of that latency on availability.

**Why This Is Correct**

Cloud Monitoring’s SLO-based alerting computes a burn-rate metric: a normalized value where a rate greater than one means that, if sustained, the service will be out of SLO for the compliance period. Configuring an alerting policy with a burn-rate threshold — a “slow-burn” style alert — warns you specifically when the current rate of consumption, if it continues, will exhaust the error budget before the 30-day window ends. That is a direct, purpose-built answer to “notify me before the budget runs out,” independent of which underlying symptom (latency, errors, or anything else) is driving the consumption.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Different Use Case:** A log-based metric with anomaly detection flags statistical deviations in the error-log rate from a historical baseline, which is a general error-detection pattern, not a measure of how much of the SLO’s error budget remains or how fast it’s being spent. It also may not even fire here, since the scenario’s root cause is latency, which might not show up as application error log entries at all.

  * **Option B — Technically Possible but Not Best:** A dashboard with a scheduled daily email gives visibility into compliance and remaining budget, but it’s a periodic report, not a real-time, threshold-triggered alert. With the budget already burning faster than normal, a day’s delay between reports could mean the budget is exhausted before anyone sees the next email.

  * **Option D — Different Use Case:** Alerting on raw average load-balancer latency crossing a fixed threshold monitors the symptom causing the problem, not the SLO’s actual compliance measure. A latency threshold alert can’t tell you whether the service is on track to violate its 99% availability target over the 30-day window — it only tells you latency is currently high, with no connection to remaining error budget or time-to-exhaustion.

**Exam Trap**

The trap is picking an option that reacts to the symptom mentioned in the stem (latency, in option D) instead of the SLO itself. The scenario describes latency as the cause, but the thing you’re actually responsible for protecting is the SLO’s error budget, and Cloud Monitoring’s SLO alerting is designed to track that budget directly regardless of which symptom is driving its consumption.

**Foundation Concept**

An SLO’s error budget is the single number that already integrates every source of unreliability (latency, errors, availability) relative to your compliance target. Alerting directly on the budget’s burn rate — rather than on any one symptom that might be contributing to it — gives you a true, root-cause-agnostic early warning, and lets you set a consistent policy (“alert me if we’re on pace to blow the budget”) regardless of what breaks next.

**Real-World Connection**

A team that only alerts on fixed latency thresholds has to separately guess at a different threshold for every new kind of incident; a team that alerts on burn rate gets one unified signal that fires whenever anything — latency, a bad deploy, a dependency outage — threatens the SLO, letting on-call engineers prioritize based on actual business risk (are we going to breach our commitment?) rather than chasing every individual metric spike.

**Memory Hook**

To know if you’ll run out of error budget before the window closes, alert on the burn rate — not on a symptom metric and not on a scheduled report.

**30-Second Exam Takeaway**

When a question asks for a proactive warning tied to an SLO’s error budget and a compliance window, look for the option that explicitly configures a burn-rate alert projecting budget exhaustion — alerts on raw symptom metrics (latency, error counts) or passive reporting (dashboards, scheduled emails) are almost always the weaker distractors.

**Official References**

[**Google Cloud — Alerting on burn rate (SLO monitoring)**](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/alerting-on-budget-burn-rate)**:** Supports: the correct-answer mechanism (burn-rate alerting and the “slow-burn” alert that warns of budget exhaustion before the compliance period ends)

[Google Cloud — Creating an alerting policy for an SLO: ](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-alert)Supports: how the burn-rate threshold is configured in an SLO-based alerting policy

---

## Question 40

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your company runs applications in a private VPC that has no internet access, and it has internal APIs reachable only from within that VPC network. You need to monitor these internal APIs’ availability using a solution that follows Google-recommended practice and keeps manual effort and ongoing maintenance to a minimum. What should you do?

- [ ] A. Deploy the application on a Google Kubernetes Engine (GKE) instance with a liveness and a readiness probe configured.
- [x] B. Set up private uptime checks.
- [ ] C. Build a Cloud Run function with a VPC connector that pings the internal endpoints, then configure public uptime checks against that Cloud Run function.
- [ ] D. Set up a synthetic monitor, and use Cloud VPN to reach the private endpoints.

### Explanation

**Correct Answer**

**B. Set up private uptime checks.**

**Exam Reasoning Explanation**

The hard requirement is monitoring availability of endpoints that are reachable only inside the VPC, with the preference of minimal custom engineering and upkeep. Every other option either solves the wrong problem (A) or solves this one by building extra infrastructure to bridge into the private network (C’s relay function and VPC connector, D’s VPN tunnel). Cloud Monitoring’s private uptime checks exist specifically to send HTTP or TCP requests directly into a customer VPC network over the private network, using Service Directory to resolve the internal target — no relay function, no VPN tunnel, and no custom code required. That makes it the only option that directly satisfies both the “internal-only reachability” requirement and the “minimize manual effort and maintenance” preference at the same time.

**Key Exam Clues**

  * **“private VPC without internet access”** and **“only accessible within your VPC network”** — a technical signal that rules out any monitoring approach assuming public reachability, and points toward a mechanism built for private-network targets specifically.

  * **“monitor the availability”** — a scope clue favoring a dedicated availability-monitoring feature (uptime checks) over a Kubernetes self-healing mechanism (liveness/readiness probes), which serves a different purpose.

  * **“Google-recommended practices”** — points at Cloud Monitoring’s native, documented private uptime checks feature rather than a hand-built workaround.

  * **“minimize the amount of manual effort and maintenance required”** — a decisive preference clue: it eliminates any option requiring you to build and operate custom relay infrastructure (a Cloud Run function, a VPN connection) just to make the target reachable.

**Why This Is Correct**

Private uptime checks let Cloud Monitoring send HTTP or TCP requests over the private network to resources like a VM or an internal load balancer, while enforcing IAM restrictions and VPC Service Controls perimeters, with the internal target registered through Service Directory. Because this capability is built directly into Cloud Monitoring, configuring a private uptime check against the internal API is a matter of registering the service and creating the check — no custom proxy application, no VPN tunnel, and no separate compute resource to build, deploy, or maintain, which is exactly the low-overhead, Google-native path to monitoring an internal-only endpoint’s availability.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Different Use Case:** Liveness and readiness probes are a Kubernetes mechanism the kubelet uses to decide whether to restart a container or route traffic to it; they don’t give you an external, alertable availability signal in Cloud Monitoring, and they’d require redeploying the application onto GKE specifically rather than monitoring the APIs where they already run. This solves pod health management, not availability monitoring.

  * **Option C — Technically Possible but Not Best:** Building a Cloud Run function with a VPC connector to relay requests, then pointing a public uptime check at that function, can work, but it requires you to write, deploy, and maintain a custom piece of software purely to bridge network reachability — exactly the ongoing maintenance burden the requirement asks you to avoid, when private uptime checks already provide that bridge natively.

  * **Option D — Technically Possible but Not Best:** Standing up a Cloud VPN connection specifically to let a synthetic monitor reach private endpoints is significant additional networking infrastructure to build and operate, when private uptime checks already reach into the VPC over the private network without requiring a VPN tunnel at all.

**Exam Trap**

The trap is assuming that because the endpoints are private, you must build a bridge yourself (a relay function, a VPN) to make a monitoring tool reach them. Google Cloud Monitoring already has a purpose-built feature for exactly this case, and recognizing “private uptime checks” as that native capability is what separates the correct answer from the plausible-sounding, more labor-intensive workarounds.

**Foundation Concept**

When a monitoring need involves a resource that standard, internet-facing tooling can’t reach, the lowest-maintenance solution is usually a provider-native feature designed for that specific reachability gap, rather than custom infrastructure built to bridge the gap yourself. Recognizing when such a native feature already exists — versus when it genuinely doesn’t and a workaround is necessary — is the core judgment this kind of question is testing.

**Real-World Connection**

A team that builds a Cloud Run relay function or a dedicated VPN tunnel just to monitor an internal API takes on ownership of that bridge indefinitely: patching it, monitoring the monitor, and handling its own failure modes. A team that uses private uptime checks offloads all of that to Cloud Monitoring itself, leaving only the uptime check configuration to maintain.

**Memory Hook**

Need to monitor an endpoint that’s reachable only inside your VPC → private uptime checks, not a custom relay function and not a VPN tunnel.

**30-Second Exam Takeaway**

When a question asks how to monitor the availability of an internal-only endpoint with minimal custom effort, check whether Cloud Monitoring already has a native feature for that reachability gap — private uptime checks — before reaching for a hand-built bridge like a relay function or a VPN connection.

**Official References**

[**Google Cloud — Create private uptime checks:**](https://cloud.google.com/monitoring/uptime-checks/private-checks) Supports: the correct-answer mechanism (sending HTTP/TCP requests into a customer VPC over the private network via Service Directory, without a relay function or VPN)

[**Google Cloud — Professional Cloud DevOps Engineer exam guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)Supports: domain alignment (Section 4.1, Instrumenting and collecting telemetry, explicitly names creating synthetic monitors/checks to proactively probe application endpoints)

---

## Question 41

*Domain 2: Building and Implementing CI/CD Pipelines*

You have a CI/CD pipeline in Cloud Build that builds container images, which are stored in Artifact Registry. You need to guarantee that only images built by this Cloud Build pipeline in your production project can be deployed to your Google Kubernetes Engine (GKE) cluster, while keeping the implementation and ongoing maintenance effort as low as possible. What should you do?

- [ ] A. Turn on Binary Authorization for the GKE cluster, and build a Cloud Run function that’s triggered by Artifact Registry INSERT events to check that pushed containers carry the projects/PROJECT_ID/attestors/built-by-cloud-build attestor.
- [ ] B. Restrict Artifact Registry so that only the Cloud Build service account is permitted to push container images.
- [ ] C. Turn on Binary Authorization for the GKE cluster. Create a Cloud Key Management Service (Cloud KMS) keyring and the built-by-cloud-build attestor yourself. After each Cloud Build push, use the key to generate an attestation, and update the Binary Authorization policy to require the projects/PROJECT_ID/attestors/built-by-cloud-build attestor.
- [x] D. Turn on Binary Authorization for the GKE cluster, and set the Binary Authorization policy to require the projects/PROJECT_ID/attestors/built-by-cloud-build attestor.

### Explanation

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

---

## Question 42

*Domain 3: Applying Site Reliability Engineering Practices*

Your team manages a critical service with a 99.9% availability SLO. The quarterly error budget has nearly run out because of several recent incidents. Your team has a new set of features planned for release next week. You need to avoid exceeding the error budget while following Google-recommended practice. What should you do?

- [ ] A. Go ahead with the release, but put an automatic rollback in place in case new errors show up.
- [ ] B. Release the features in stages, rolling out to one subset of users at a time to limit the potential impact on the SLO.
- [x] C. Postpone the release and have the team focus on reliability improvements until the error budget replenishes.
- [ ] D. Postpone the release and have the team spend the time building up a backlog of features to deploy once the error budget replenishes.

### Explanation

**Correct Answer**

**C. Postpone the release and have the team focus on reliability improvements until the error budget replenishes.**

**Exam Reasoning Explanation**

The error budget exists specifically to govern this trade-off: it’s the amount of unreliability the service can absorb while still meeting its SLO, and it’s meant to be spent deliberately on things like feature launches when it’s healthy. With the budget nearly exhausted, any further risk-bearing change — even a carefully staged one — threatens to push the service out of SLO. Google’s own SRE guidance treats this situation as a trigger for a feature freeze specifically so that engineering effort shifts to reliability work, which is the only one of the four options that both avoids further budget risk and redirects effort toward actually fixing the underlying problem rather than just sitting on hands or stockpiling unrelated work.

**Key Exam Clues**

  * **“error budget for the quarter has been nearly depleted”** — a decisive constraint clue: there is very little room left to absorb any additional errors, which argues against any option that still introduces new risk.

  * **“due to several incidents”** — signals that the service has an active reliability problem, which is the condition Google’s error budget policy explicitly treats as a reason to pause feature work and fix the underlying issues.

  * **“planning on releasing new features next week”** — frames the choice as whether to proceed, in some form, with new risk-bearing change right now.

  * **“following Google-recommended practices”** — points directly at the documented SRE error-budget policy response (a feature freeze focused on reliability), rather than at ad hoc risk-mitigation tactics.

**Why This Is Correct**

Google’s SRE practice treats an exhausted or near-exhausted error budget as the signal to impose a freeze on new feature releases, specifically so that the team can redirect its attention to reliability improvements until the budget is replenished. Postponing the release removes the immediate source of additional risk, and spending that time on reliability work (fixing root causes, improving testing, hardening the release process) is what actually restores headroom in the budget and reduces the odds of repeating the recent incidents, rather than just waiting out the clock or doing unrelated work.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** An automatic rollback limits how long a bad release stays live, but it doesn’t prevent the release from consuming more of an already nearly-exhausted budget before the rollback triggers. Proceeding with a risk-bearing release at all runs directly counter to the recommended response to a strained budget.

  * **Option B — Technically Possible but Not Best:** Staged, subset-based rollout is a reasonable general technique for limiting blast radius, and it reduces risk relative to a full release. But it still introduces new change and new risk onto a service whose budget is nearly gone; Google’s documented guidance for this situation is a full pause on feature releases, not merely a more cautious version of the same release.

  * **Option D — Different Use Case:** This option correctly postpones the risky release, but it spends the freed time on building a feature backlog rather than on reliability work. That addresses a different goal (being ready to ship more features later) and does nothing to reduce the chance of repeating the incidents that burned the budget in the first place — which is the specific purpose Google’s guidance assigns to this kind of pause.

**Exam Trap**

The trap is treating “postpone the release” as the whole answer and picking whichever postponement option is listed, without checking what the team is supposed to do with the freed time. Google’s guidance is explicit that a freeze is meant to create space for reliability work specifically, not simply to delay the release or redirect effort toward unrelated feature planning.

**Foundation Concept**

An error budget converts “how reliable should this service be” into a concrete, spendable quantity, which lets a team make principled trade-offs between shipping new risk-bearing changes and investing in stability. When the budget is nearly spent, the policy response isn’t just “be more careful” — it’s a deliberate, temporary rebalancing of where engineering effort goes, specifically toward the reliability work that restores the budget.

**Real-World Connection**

A team that keeps shipping features, even cautiously, while its error budget is nearly gone tends to keep having the same category of incident recur, because nothing is actually being invested in root-cause fixes or hardening. A team that treats budget depletion as an explicit freeze trigger and spends that time on reliability work typically breaks the cycle and arrives at the next compliance period with both a healthier budget and a more resilient service.

**Memory Hook**

Budget nearly gone → freeze features, spend the time on reliability — not on a safer release and not on a bigger feature backlog.

**30-Second Exam Takeaway**

When an error-budget question asks what to do about an upcoming release while the budget is nearly or fully depleted, the Google-recommended answer is almost always to pause the release and redirect the team to reliability work until the budget refreshes — any option that still ships something, however carefully, or that spends the pause on non-reliability work, is the weaker distractor.

**Official References**

[**Google SRE Workbook — Example Error Budget Policy (Appendix B):**](https://sre.google/workbook/error-budget-policy/) Supports: the correct-answer mechanism (freezing feature releases and dedicating the team to reliability work when the error budget is overspent)

[**Google Cloud Blog — Good housekeeping for error budgets (CRE life lessons)**](https://cloud.google.com/blog/products/devops-sre/good-housekeeping-error-budgetscre-life-lessons)**:** Supports: the canonical response to overspending an error budget being a feature freeze aimed specifically at reliability work, used to eliminate option D’s “build a feature backlog” framing

---

## Question 43

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

Your organization is bringing the marketing department onto Google Cloud. The marketing team will independently manage its own development work, but you need visibility into total departmental spending and want to receive an alert if spending exceeds the marketing budget as a whole. What should you do?

- [ ] A. Create all of the marketing department’s projects independently, and configure a separate budget alert for each project using the full marketing budget divided by the number of projects as that project’s limit.
- [ ] B. Create all of the marketing department’s projects under a dedicated marketing folder, and configure a separate budget alert for each project using the full marketing budget as that project’s limit.
- [x] C. Create all of the marketing department’s projects under a dedicated marketing folder, and configure a single budget alert scoped to the folder using the full marketing budget as its limit.
- [ ] D. Create all of the marketing department’s projects independently, and configure a separate budget alert for each project using the full marketing budget as that project’s limit.

### Explanation

**Correct Answer**

**C. Create all of the marketing department’s projects under a dedicated marketing folder, and configure a single budget alert scoped to the folder using the full marketing budget as its limit.**

**Exam Reasoning Explanation**

Must-have constraints: a resource structure that groups every current and future marketing project together, and one alert tied to the department’s real total budget. Not a requirement: granularity down to the individual project — the question never asks which project overspent, only whether the department as a whole did. Capability: folders in the resource hierarchy exist to group projects for IAM, policy, and billing purposes, and a Cloud Billing budget can be scoped to a folder, which sums spend from every project nested under it. Elimination: any option without a folder (A, D) has no structural anchor for department-wide scoping, and any option that assigns the full budget to each individual project (B, D) lets combined spend across several projects run well past the real budget while every individual alert still reads “under threshold.” Only the folder-plus-single-folder-alert combination satisfies both constraints at once.

**Key Exam Clues**

  * “visibility into total departmental spending” — a hard constraint requiring aggregate monitoring, not per-project monitoring.

  * “alert if spending exceeds the marketing budget as a whole” — a cardinality signal: one ceiling, evaluated once, not a ceiling duplicated per project.

  * “will independently manage its own development work” — implies multiple, possibly growing, projects, which is why a grouping mechanism matters.

  * No stated project count — a technical signal that the correct approach must keep working as projects are added, ruling out any option whose math depends on a fixed project count.

**Why This Is Correct**

Grouping every marketing project inside one folder turns that folder into a single accounting unit in the resource hierarchy. A budget’s scope can be filtered to that folder, and Cloud Billing then totals the cost of every project beneath it before comparing the total to the configured amount. Setting that single budget’s amount to the full marketing allocation means the alert fires exactly when true cumulative departmental spend crosses the line — and because the scope is the folder, not a fixed list of projects, a new marketing project dropped into that folder later is automatically covered with no reconfiguration.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** Dividing the total budget by project count creates an artificial per-project ceiling disconnected from how spend actually distributes. One project can blow past its slice while the department overall is still under budget (a false alarm), or every project can stay under its slice while combined spend exceeds the real budget (a missed alarm) — and the slice size breaks the moment a project is added or removed.

**Option B — Violates Requirement:** The folder grouping is correct, but assigning the FULL marketing budget as each individual project’s limit means no alert fires until one project alone has consumed the entire department’s budget. Combined spend across several projects can be multiples of the real budget before anything triggers, which directly fails the “total spending” requirement.

**Option D — Violates Requirement:** This combines both weaknesses above — no folder to anchor department-wide visibility, and a full-budget threshold applied per project rather than in aggregate — so it neither organizes the projects nor catches cumulative overspend.

**Exam Trap**

The trap is assuming more alerts means tighter cost control. What determines correctness here isn’t the number of alerts, it’s the scope each alert sums against. Options that create more alerts (A, B, D) can still fail to answer what the question actually asks — whether the department’s combined spend stayed within budget. A per-project alerting approach would only become correct if the question instead asked you to identify which individual project overspent.

**Foundation Concept**

The organization → folder → project hierarchy exists so policies, IAM, and billing can be applied once at a grouping level instead of repeated per resource. Cloud Billing budgets extend that pattern to cost control: a budget’s scope can be the billing account, one or more folders, or one or more projects, and that scope choice determines what gets summed before comparison to the configured amount. Matching the scope to the actual question being asked — “how is this one project doing” versus “how is this whole department doing” — is the underlying skill, independent of console click-paths.

**Real-World Connection**

Organizations commonly mirror their org chart with one folder per department or cost center specifically so FinOps and engineering leads can watch a single dashboard and a single alert per department instead of reconciling numbers from dozens of per-project alerts. It also means a project spun up mid-quarter is automatically captured by the existing folder-level budget, keeping cost governance consistent as the environment grows without anyone having to remember to wire up a new per-project alert each time.

**Memory Hook**

One department, one folder, one budget — group first, then alert once at the level you actually need to monitor.

**30-Second Exam Takeaway**

When a scenario asks you to monitor combined spend across several projects and alert on one overall ceiling, pick the option that both groups those projects under a folder and scopes the budget alert to that folder — any option alerting per project, however the per-project amount is calculated, is solving a different problem.

**Official References**

[**Google Cloud — Create, edit, or delete budgets and budget alerts:**](https://cloud.google.com/billing/docs/how-to/budgets) Supports: folder-level budget scoping and the budget creation/scope-setting workflow

[**Google Cloud — Budget resource (REST reference), billingAccounts.budgets:**](https://cloud.google.com/billing/docs/reference/budget/rest/v1/billingAccounts.budgets) Supports: confirms a budget’s filter can include a set of folder names, so usage from every project under that folder is aggregated into the budget

---

## Question 44

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

You’re working on a Google Cloud project that’s been running in production for several months, and you need to update an IAM policy to grant a team member additional permissions. Before applying the change to the production environment, you need to proactively surface any potential risks tied to this IAM policy change. What should you do?

- [ ] A. Apply the IAM policy change, then use the recent change recommendations to watch for any unintended consequences.
- [x] B. Use the change risk recommendations to evaluate the potential impact of the IAM policy change and surface any associated risks before applying it.
- [ ] C. Grant the new team member the Project Owner role, and reassess their permissions once their task is finished.
- [ ] D. Use the Cloud deprecation and breaking changes general recommender to evaluate how the IAM policy change might affect any services that are deprecated or due to change soon.

### Explanation

**Correct Answer**

**B. Use the change risk recommendations to evaluate the potential impact of the IAM policy change and surface any associated risks before applying it.**

**Exam Reasoning Explanation**

The hard requirement is timing and scope: you need risk visibility for this specific IAM policy change, before it’s applied, not after. That rules out A outright, since it applies the change first and only observes afterward — the opposite of proactive. It also rules out D, which targets a completely different risk category (deprecated or soon-to-change services) rather than the risk of an IAM permission grant itself. C doesn’t attempt any risk assessment at all; it just grants broad access and defers the real work. Change risk recommendations is the Recommender/Active Assist feature purpose-built for exactly this scenario — it’s explicitly scoped to include IAM policy changes and is designed to warn you about the risk of a change before you make it, based on recent usage activity tied to that policy.

**Key Exam Clues**

  * **“been in production for several months”** — a technical signal that the policy likely has real, active dependents whose access could be affected, which is exactly the kind of usage-based risk change risk recommendations is designed to surface.

  * **“proactively identify any potential risks”** — a decisive requirement/exclusion clue: it rules out any option where the change is made first and checked afterward (A).

  * **“before applying them to the production environment”** — reinforces the same timing requirement and rules out C’s “grant broad access now, fix it later” approach.

  * **“associated risks associated with these IAM policy changes”** — a scope clue naming IAM policy changes specifically, distinguishing the needed tool from one aimed at service deprecations (D).

**Why This Is Correct**

Change risk recommendations is a family of Active Assist recommendations within the Recommender service, specifically built to warn you about the risk of making a change — including an IAM policy change — based on that resource’s recent usage activity, before you actually apply it. Running this check against the proposed IAM policy update lets you see, ahead of time, whether the change could break an essential dependency or have other unintended consequences, which is precisely the proactive, pre-application risk assessment the scenario asks for.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** This applies the IAM policy change before assessing anything, then relies on a different, retrospective signal (recent change recommendations) to catch problems after the fact. That inverts the stated requirement to identify risks before applying the change, and by the time an unintended consequence is observed, the risky change is already live in production.

  * **Option C — Violates Requirement:** Granting Project Owner sidesteps the actual question entirely — it doesn’t assess risk at all, it just grants far more access than requested and pushes the real evaluation to some later point. This also conflicts with least-privilege practice, since Project Owner is a broad, high-privilege role for what was described as an incremental permission addition.

  * **Option D — Different Use Case:** The deprecation and breaking-changes recommender addresses a different risk category — whether a service or API your project depends on is being deprecated or changed — not the risk introduced by modifying an IAM policy. It wouldn’t surface anything about who currently depends on the policy being changed or what could break as a result of the permission grant itself.

**Exam Trap**

The trap is picking an option that includes the word “recommendations” or sounds proactive without checking whether its scope actually matches “risk of an IAM policy change.” Recent change recommendations and the deprecation/breaking-changes recommender are both real Google Cloud tools, but neither is scoped to pre-application IAM risk assessment the way change risk recommendations specifically is.

**Foundation Concept**

Google Cloud’s Active Assist recommenders are organized by what they help you decide, not just by when they run: some (like change risk recommendations) are designed to be consulted before you make a change, using recent usage data to warn you of likely impact, while others are designed to surface issues after a change or event has already occurred, or to track an entirely different category of risk such as service lifecycle changes. Picking the right recommender means matching both its timing (before vs. after) and its subject (IAM policy vs. service deprecation) to what you actually need to evaluate.

**Real-World Connection**

A platform team that applies IAM changes first and only reviews recent-change recommendations afterward tends to discover broken dependencies only once something has already failed in production. A team that runs change risk recommendations against a proposed IAM policy update before applying it can catch that, for example, a service account’s access is a load-bearing dependency for another team’s pipeline, and adjust the change before it ever goes live.

**Memory Hook**

Need to know the risk of a change before you make it → change risk recommendations, not a broader role grant, not a post-hoc monitoring recommender, and not a deprecation recommender.

**30-Second Exam Takeaway**

When a question asks for a proactive, pre-application risk assessment of an IAM policy change, look specifically for “change risk recommendations” — any option that applies the change first, grants broader access as a workaround, or points to a recommender scoped to a different kind of risk (like service deprecation) is the weaker distractor.

**Official References**

[**Google Cloud — Change risk recommendations (Recommender):**](https://cloud.google.com/recommender/docs/change-risk-recommendations) Supports: the correct-answer mechanism (proactive, usage-based risk warnings for IAM policy changes before they’re applied)

[Google Cloud — Recommender reference (recommender and insight types): ](https://cloud.google.com/recommender/docs/reference/rest/v1beta1/recommenders)Supports: the distinction between change risk recommendations and the separate recent change recommendations and deprecation-related recommenders, used to eliminate options A and D

---

## Question 45

*Domain 5: Optimizing Performance and Cost*

A newly created Google Cloud project will host several applications on Compute Engine VM instances distributed across multiple regions. You expect the total instance count to remain steady or increase, although you might redistribute instances among regions over time. Which approach best minimizes compute costs for this multi-year project?

- [ ] A. Purchase a three-year resource-based commitment.
- [ ] B. Purchase a three-year compute flexible commitment and create capacity reservations.
- [x] C. Purchase a three-year compute flexible commitment.
- [ ] D. Purchase a one-year resource-based commitment.

### Explanation

**Correct Answer**

**C. Purchase a three-year compute flexible commitment.**

**Exam Reasoning Explanation**

The solution must accommodate changes in regional allocation. The stable overall demand supports committing to ongoing usage, while the multi-year horizon favors the longer term. Resource-based commitments introduce regional restrictions. Between the flexible options, reservations add capacity assurance that the scenario does not request, making C the best fit.

**Key Exam Clues**

  * **“Distributed across multiple regions” — Technical signal:** Evaluate the geographical scope of each commitment.

  * **“Total instance count to remain steady or increase” — Technical signal:** Indicates an ongoing consumption baseline.

  * **“Redistribute instances among regions” — Hard constraint:** Savings must remain applicable as regional placement changes.

  * **“Minimizes compute costs” — Optimization objective:** Avoid adding capacity arrangements without a corresponding requirement.

  * **“Multi-year project” — Technical signal:** Supports considering a three-year commitment.

**Why This Is Correct**

Compute flexible commitments apply to eligible spending across regions and projects within the same Cloud Billing account. Their coverage can therefore follow eligible workloads as the regional distribution changes. A three-year term provides greater discounts than a one-year term for eligible Compute Engine resources.

The commitment covers a minimum **hourly spend** , rather than a fixed number of instances. Actual savings depend on maintaining sufficient eligible consumption.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** A three-year resource-based commitment can provide substantial savings for predictable regional usage. However, its coverage remains tied to the specified region. Moving workloads elsewhere can leave paid commitments underutilized.

  * **Option B — Technically Possible but Not Best:** Flexible commitments can cover eligible usage that consumes separately created reservations. Reservations hold capacity in specified zones; they do not independently increase the commitment discount. Unused reserved resources can incur charges, so this option introduces unnecessary cost exposure for the stated objective. Consuming a reservation does **not** create duplicate resource charges for the same VM usage. 

  * **Option D — Technically Possible but Not Best:** A one-year resource-based commitment reduces the commitment duration but retains the regional restriction. It also provides a smaller discount than the corresponding three-year resource-based plan. It would be more appropriate for predictable regional demand with only a one-year commitment horizon. 

**Exam Trap**

Do not confuse a **pricing commitment** with a **capacity reservation**. Option B becomes appropriate if the requirements additionally include assured capacity for particular VM configurations in specified zones. Compute flexible commitments do not support attached reservations; any required reservations are created separately. 

**Foundation Concept**

Evaluate commitment scope, duration, and capacity assurance separately. A favorable discount rate only produces useful savings when actual consumption continues to match the commitment’s eligibility and scope.

**Real-World Connection**

An application team could redistribute eligible VMs between two regions while continuing to consume the same billing account’s flexible commitment. Before purchasing, it should forecast minimum hourly eligible spending: unchanged instance counts alone do not guarantee unchanged spending when VM sizes or regional prices differ.

**Memory Hook**

Stable demand with changing regions favors flexible commitments; add reservations when capacity assurance is required.

**30-Second Exam Takeaway**

Identify what remains predictable: total consumption or consumption within a particular region. For ongoing eligible compute usage whose regional distribution may change, prefer a compute flexible commitment and select the term supported by the workload horizon.

**Official References**

  * [**Google Cloud — Committed use discounts for Compute Engine:**](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)

Supports: Cross-region flexible coverage, regional resource-based restrictions, commitment duration, and hourly spending obligations.

  * [**Google Cloud — Combine reservations with committed use discounts:**](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments)

Supports: The distinction between discounts and capacity assurance, including separate reservations with compute flexible commitments.

[**Google Cloud — About reservations:**](https://docs.cloud.google.com/compute/docs/instances/reservations-overview)

Supports: Zonal capacity assurance, charges for unused reserved resources, and the absence of duplicate resource charges when reservations are consumed.

[**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)

Supports: Alignment with “Optimizing performance and cost,” objective 5.2, which includes infrastructure cost planning and committed-use discounts. [English](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf?utm_source=chatgpt.com)

---

## Question 46

*Domain 2: Building and Implementing CI/CD Pipelines*

You’re designing a secure Cloud Build pipeline for a web application that needs access to a package manager. The package manager credentials are highly sensitive and must be protected from unauthorized access. You need a way to retrieve these credentials securely at build time, following Google-recommended practice, while keeping ongoing maintenance to a minimum. What should you do?

- [ ] A. Grant roles/cloudkms.cryptoKeyDecrypter to the Cloud Build service account. Store Cloud KMS-encrypted data in the build config file, specifying the secret under the secrets field.
- [ ] B. Grant roles/cloudkms.cryptoKeyDecrypter to the Cloud Build service account. Store Cloud KMS-encrypted data in the build config file, specifying the secret under the availableSecrets.inline field.
- [x] C. Grant roles/secretmanager.secretAccessor to the service account used for the build, and specify the secret under the availableSecrets.secretManager field.
- [ ] D. Store base64-encoded data in the web application’s source control repository, and decrypt and use the secret during the build.

### Explanation

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

---

## Question 47

*Domain 2: Building and Implementing CI/CD Pipelines*

You’re setting up a Cloud Deploy pipeline to deploy an application to Google Kubernetes Engine (GKE) as a Deployment. You need the Deployment to run two replicas in the development environment and five replicas in production, while keeping every other configuration parameter identical across both environments. You also want to minimize the ongoing effort of updating the manifests going forward. How should you configure the skaffold.yaml file?

- [x] A. Define multiple profiles, and configure the manifests.kustomize section.
- [ ] B. Define a single profile, and configure the manifests.kustomize section.
- [ ] C. Define multiple profiles, and configure the manifests.rawYaml section.
- [ ] D. Define a single profile, and configure the manifests.rawYaml section.

### Explanation

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

---

## Question 48

*Domain 2: Building and Implementing CI/CD Pipelines*

A third-party application continuously uploads encrypted files to a Cloud Storage bucket. Each file is protected with an HMAC-SHA256 key and contains sensitive data that must be loaded into BigQuery for analysis every day shortly after midnight. You need to design a secure, fully automated pipeline that decrypts these files and loads them into BigQuery, following Google-recommended practices while keeping custom development effort to a minimum. What should you do?

- [ ] A. 1. Upload the decryption key into the same Cloud Storage bucket that stores the encrypted files. 2. Build a Cloud Build pipeline that decrypts each file and then loads it into BigQuery. 3. Set up a Cloud Scheduler job that triggers the pipeline daily at the required time.
- [x] B. 1. Create a Cloud Key Management Service (Cloud KMS) key ring and import the decryption key into it. 2. Containerize the decrypt-and-load script, then push the resulting image to an Artifact Registry repository. 3. Create a Cloud Run job that runs the image on a recurring schedule. 4. Grant the Cloud Run service agent the Cloud KMS CryptoKey Encrypter/Decrypter role.
- [ ] C. 1. Create a Cloud Key Management Service (Cloud KMS) key ring and import the decryption key into it. 2. Configure a Cloud Build trigger that calls Cloud KMS to decrypt each file before loading it into BigQuery. 3. Set up a Cloud Scheduler job that fires the trigger daily at the required time.
- [ ] D. 1. Upload the decryption key into the same Cloud Storage bucket that stores the encrypted files. 2. Write a script that retrieves the key from Cloud Storage and uses it to decrypt each file. 3. Containerize the script and push the resulting image to an Artifact Registry repository. 4. Create a Cloud Run job that runs the image on a recurring schedule.

### Explanation

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

---

## Question 49

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You’re investigating slow Apigee responses for calls made to the orders proxy in the Production environment. This proxy relies on several services running in Google Kubernetes Engine (GKE) behind Cloud Service Mesh. You need to find the root cause of the latency without affecting the performance of the other proxies exposed in that environment. What should you do?

- [ ] A. Turn on distributed tracing for the whole Production environment. Use Cloud Trace to inspect each span and pinpoint the service adding the most latency.
- [ ] B. Use Cloud Monitoring and the Apigee target latencies metric to pinpoint the service adding the most latency.
- [ ] C. Use Cloud Logging to review logs from the different backend services to pinpoint the service adding the most latency.
- [x] D. Turn on distributed tracing on Apigee, configured so that only the orders proxy is traced. Use Cloud Trace to inspect each span and pinpoint the service adding the most latency.

### Explanation

**Correct Answer**

**D. Turn on distributed tracing on Apigee, configured so that only the orders proxy is traced. Use Cloud Trace to inspect each span and pinpoint the service adding the most latency.**

**Exam Reasoning Explanation**

There are two requirements stacked here: pinpoint exactly which service in a multi-hop chain is adding latency, and do it without adding overhead to every other proxy running in the same environment. Apigee’s distributed trace configuration applies by default to every API proxy in an environment, but it also supports a trace configuration override scoped to one specific API proxy. Scoping the trace to just the orders proxy satisfies the “don’t impact other services” constraint directly, while Cloud Trace’s span-level breakdown is what lets you see exactly which downstream service in the Cloud Service Mesh chain is responsible for the added latency. Options that use coarser signals (an aggregate latency metric, raw logs) can’t localize the problem as precisely, and enabling tracing environment-wide ignores the explicit “without impacting the other exposed services” constraint.

**Key Exam Clues**

  * **“multiple services running in GKE with Cloud Service Mesh”** — a technical signal that the latency could originate at any of several hops, which calls for span-level breakdown rather than a single aggregate metric.

  * **“determine the root cause”** — a scope clue favoring a diagnostic tool that attributes latency to a specific service, not just confirms that latency exists.

  * **“without impacting the performance of the other exposed services”** — a decisive constraint clue: it rules out any approach that applies tracing (or its overhead) broadly across every proxy in the environment.

  * **“orders proxy”** named specifically — points toward a mechanism that can be scoped to just that one proxy, which Apigee’s trace configuration override supports directly.

**Why This Is Correct**

Apigee’s environment-level distributed trace configuration defines a default sampling behavior applied to every API proxy in that environment, but Apigee also supports a trace configuration override that targets one specific API proxy by ID, letting you enable (and sample) tracing for just that proxy while leaving every other proxy’s tracing configuration untouched. Scoping the configuration to the orders proxy means only calls through that proxy incur any tracing overhead, directly satisfying “without impacting the other exposed services.” Once that scoped trace data flows into Cloud Trace, you get a span per hop (through Apigee and through the chain of GKE/mesh services), letting you see exactly which span accounts for the bulk of the latency.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Enabling distributed tracing “in the Production environment” without scoping it to a specific proxy applies the sampling configuration to every API proxy in that environment by default. That adds tracing overhead across all exposed services, directly conflicting with the requirement to avoid impacting the other proxies.

  * **Option B — Technically Possible but Not Best:** The Apigee target latencies metric can confirm that the backend target for the orders proxy is responding slowly in aggregate, but it doesn’t decompose that latency across the individual downstream services sitting behind Cloud Service Mesh. It tells you something is slow, not specifically which of the “multiple services” is the cause.

  * **Option C — Technically Possible but Not Best:** Manually reviewing logs from each backend separately, with no shared trace context tying them together, is a slower and less precise way to reconstruct a multi-hop request’s timing than a tool built specifically to show per-span duration across that same chain.

**Exam Trap**

The trap is picking the option that correctly identifies “distributed tracing + Cloud Trace” as the right tool category (A) but misses the scoping detail that the scenario explicitly calls for. Without noticing “without impacting the performance of the other exposed services,” enabling tracing environment-wide looks like the obvious, complete answer — the constraint is what separates it from the proxy-scoped version.

**Foundation Concept**

Observability tooling often supports both a broad, default configuration and a narrower, resource-specific override; choosing the broad default when only one resource is under investigation is a common way to introduce unintended overhead elsewhere. Scoping diagnostic instrumentation (tracing, enhanced logging, sampling) to the specific resource under investigation is the general pattern for getting the detail you need without disturbing unrelated, healthy traffic.

**Real-World Connection**

A platform team that enables distributed tracing environment-wide to chase down one slow proxy risks adding latency and cost to every other API exposed from that environment, potentially masking the very problem they’re chasing with new noise elsewhere. A team that scopes the trace configuration override to just the proxy under investigation gets the detailed span data it needs while leaving the rest of production traffic completely unaffected.

**Memory Hook**

One proxy is slow → trace just that proxy, not the whole environment.

**30-Second Exam Takeaway**

When an Apigee/GKE latency question asks you to find the root cause “without impacting other services,” look for the option that scopes distributed tracing to the specific proxy under investigation — environment-wide tracing, aggregate latency metrics, and raw log review are all weaker distractors by comparison.

**Official References**

[**Google Cloud — Enabling distributed tracing (Apigee):**](https://cloud.google.com/apigee/docs/api-platform/develop/enabling-distributed-trace)Supports: the correct-answer mechanism (Apigee’s Cloud Trace integration and span-level request breakdown)

[**Google Cloud — TraceConfig and trace configuration overrides (Apigee API reference):**](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.traceConfig.overrides) Supports: the environment-wide default sampling configuration versus a per-API-proxy trace configuration override, which distinguishes option D from option A

---

## Question 50

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You’re building a centralized platform to monitor applications that run on Kubernetes clusters both on-premises and across several Google Cloud projects. You want developers to be able to monitor both infrastructure and application metrics using OpenTelemetry across these on-premises and Google Cloud environments, while keeping day-to-day operation simple and bringing all the metrics together in one place. What should you do?

- [ ] A. Run a sidecar OpenTelemetry Collector alongside every Pod across all the Kubernetes clusters (on-premises and GKE), configured to export Prometheus-formatted metrics. Run a dedicated Prometheus instance in each cluster, federate them with Thanos in a central GKE cluster, install Grafana on a GKE cluster, and use Grafana to monitor the applications.
- [x] B. Create a scoping project and add all the Google Cloud projects to it. Use Bindplane to streamline OpenTelemetry metric collection from the on-premises Kubernetes clusters into Cloud Monitoring.
- [ ] C. Create a new Google Cloud project to act as a scoping project, and add the other Google Cloud projects to it. Instrument the applications running on-premises so they export metrics to Cloud Monitoring as user-defined metrics, and use Cloud Monitoring to monitor the applications.
- [ ] D. Enable Google Cloud Managed Service for Prometheus collection using the OpenTelemetry Collector on the GKE clusters, and run unmanaged Prometheus on the on-premises Kubernetes clusters. Install Grafana on a GKE cluster, and use Grafana to monitor the applications.

### Explanation

**Correct Answer**

**B. Create a scoping project and add all the Google Cloud projects to it. Use Bindplane to streamline OpenTelemetry metric collection from the on-premises Kubernetes clusters into Cloud Monitoring.**

**Exam Reasoning Explanation**

There are three things to solve at once: aggregate metrics across several Google Cloud projects, bring in OpenTelemetry-based infrastructure and application metrics from on-premises, and do both with minimal self-managed infrastructure. Cloud Monitoring’s metrics scope, hosted by a scoping project, is the native, built-in mechanism for the first part — no extra software to run. Bindplane is Google’s own documented, OpenTelemetry-native pipeline specifically built to pull metrics, logs, and traces from hybrid and on-premises environments straight into Cloud Monitoring, and it’s offered at no additional cost to Cloud Observability customers, which covers the second and third parts simultaneously: real OpenTelemetry collection from on-prem infrastructure and applications, landing directly in the same single pane of glass as the Google Cloud projects, with no Prometheus servers, Thanos federation, or Grafana deployment for you to operate.

**Key Exam Clues**

  * **“multiple Google Cloud projects”** — a technical signal pointing directly at Cloud Monitoring’s scoping project/metrics scope feature, which exists specifically to unify metrics across several projects.

  * **“monitor both infrastructure and application metrics using OpenTelemetry across on-premises and Google Cloud environments”** — a scope clue requiring a genuine OpenTelemetry collection path from on-premises infrastructure, not just hand-instrumented application code.

  * **“keep the operation easy to support”** — a decisive preference clue: it eliminates any option built around self-hosted Prometheus, Thanos, or Grafana stacks that the team would have to operate.

  * **“integrate all metrics into a single place”** — reinforces that the destination should be one existing, managed service (Cloud Monitoring) rather than a separately maintained visualization layer like a self-hosted Grafana instance.

**Why This Is Correct**

A scoping project with a multi-project metrics scope lets every Google Cloud project’s metrics appear in one Cloud Monitoring view with no additional infrastructure — it’s a configuration setting, not a service you run. Bindplane complements this by deploying and managing OpenTelemetry collectors across on-premises and hybrid cloud sources, sending that telemetry directly to Cloud Monitoring’s APIs, so on-premises Kubernetes infrastructure and application metrics land in exactly the same place as the Google Cloud project metrics. Together, this gives developers a single, OpenTelemetry-based view across every environment, with Google managing both the central monitoring platform and the hybrid collection pipeline’s fleet management.

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** Running a sidecar collector per Pod, a dedicated Prometheus server per cluster, Thanos for federation, and a self-hosted Grafana instance is the heaviest possible stack to build and operate yourself. This is the opposite of “easy to support” — every one of those components needs its own scaling, patching, and high-availability story.

  * **Option C — Technically Possible but Not Best:** Using a scoping project correctly solves the multi-Google-Cloud-project aggregation, but instrumenting on-premises applications individually to push user-defined metrics only covers application-level data — it misses infrastructure metrics from the on-premises clusters entirely, and it means every application needs its own custom instrumentation work rather than a single, uniform OpenTelemetry collection layer.

  * **Option D — Technically Possible but Not Best:** Managed Service for Prometheus handles the GKE side with little operational burden, but falling back to unmanaged (self-hosted) Prometheus on-premises reintroduces the exact maintenance burden the requirement asks to avoid, and adding a self-hosted Grafana instance as the unifying view means operating yet another component instead of using the already-centralized, managed Cloud Monitoring.

**Exam Trap**

The trap is assuming that because Prometheus and Grafana are familiar, industry-standard observability tools, building a stack around them is automatically the right answer. The scenario’s explicit “easy to support” and “single place” requirements are specifically testing whether you’ll recognize Google’s managed, purpose-built hybrid path (Bindplane into Cloud Monitoring, with a scoping project for multi-project aggregation) over a more familiar but self-operated alternative.

**Foundation Concept**

When a monitoring architecture needs to span cloud-native and on-premises environments, the lowest-maintenance design usually pairs the cloud provider’s own managed collection pipeline for hybrid sources with the provider’s native multi-project aggregation feature, rather than building a parallel open-source observability stack (Prometheus, Thanos, Grafana) that duplicates capabilities the managed platform already provides.

**Real-World Connection**

A platform team that stands up per-cluster Prometheus instances, Thanos federation, and a self-hosted Grafana deployment takes on the full operational lifecycle of all three — upgrades, storage scaling, and failure recovery — on top of the monitoring work itself. A team that configures a Cloud Monitoring scoping project and deploys Bindplane’s managed collector fleet gets the same cross-environment visibility while Google operates the aggregation and collection-management layers.

**Memory Hook**

Multiple Google Cloud projects in one view → scoping project; on-premises OpenTelemetry metrics into that same view with the least effort → Bindplane into Cloud Monitoring, not a self-hosted Prometheus/Thanos/Grafana stack.

**30-Second Exam Takeaway**

When a question asks for low-maintenance, unified monitoring across multiple Google Cloud projects and on-premises environments using OpenTelemetry, look for a Cloud Monitoring scoping project paired with Bindplane — options that build a self-hosted Prometheus/Thanos/Grafana stack, or that only manually instrument individual on-premises applications, are the weaker distractors.

**Official References**

[**Google Cloud — About Bindplane:**](https://cloud.google.com/stackdriver/bindplane) Supports: the correct-answer mechanism (an OpenTelemetry-native pipeline that collects metrics, logs, and traces from hybrid/on-premises environments into Cloud Monitoring, free for Cloud Observability customers)

[**Google Cloud — Metrics scopes overview:**](https://cloud.google.com/monitoring/settings) Supports: the scoping project / multi-project metrics scope mechanism used to unify metrics across multiple Google Cloud projects

[**Google Cloud — Professional Cloud DevOps Engineer exam guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf) Supports: domain alignment (Section 4.1, Instrumenting and collecting telemetry, explicitly names hybrid/multi-cloud environments and Google Cloud Managed Service for Prometheus)

---

## Question 51

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

While investigating a sustained spike in request volume, you build a custom dashboard in Cloud Monitoring and trace the unusual traffic to a single type of client. You now want your company’s development team to continue the investigation using that same custom dashboard. Following Google-recommended practices, what should you do?

- [ ] A. Export the custom dashboard as a JSON file and send the file to the development team.
- [ ] B. Export the dashboard’s time series data in CSV format, and have the development team analyze it in BigQuery.
- [x] C. Grant the development team the Monitoring Viewer (roles/monitoring.viewer) IAM role at the project level, and share the custom dashboard’s URL with them.
- [ ] D. Grant the development team the Viewer (roles/viewer) IAM role at the project level, and share the custom dashboard’s URL with them.

### Explanation

**Correct Answer**

**C. Grant the development team the Monitoring Viewer (roles/monitoring.viewer) IAM role at the project level, and share the custom dashboard’s URL with them.**

**Exam Reasoning Explanation**

Must-have constraints: the development team needs to go on using the _same live dashboard_ you already built, and the chosen method has to match Google’s own documented recommendation. Not a requirement: the team editing the dashboard, managing alerts, or touching anything outside Monitoring. Capability: Cloud Monitoring dashboards are sharable in place — anyone with sufficient IAM permission on the project can open the dashboard’s URL directly and see live, filterable data, no export step needed. Elimination: options that export the dashboard or its data (A, B) hand the team a disconnected, static artifact instead of the live investigative tool you built, and require extra engineering (a JSON re-import flow, or a whole BigQuery analysis pipeline) that the scenario doesn’t call for. Option D grants access, but through `roles/viewer`, a broad basic role that reaches far beyond Monitoring into most of the project’s resources — more access than the task needs. Decision: Option C is the only one that preserves the live dashboard experience and grants exactly the scope required, nothing more.

**Key Exam Clues**

  * “continue the investigation using that same custom dashboard” — a hard constraint that the team needs the live, interactive dashboard, not a copy or a derived dataset.

  * “following Google-recommended practices” — a technical signal pointing straight at Google’s own documented least-privilege sharing pattern for Monitoring dashboards.

  * No mention of editing, alerting, or configuration needs — an exclusion signal ruling out any role broader than a viewer-level grant.

  * “development team” (a whole team, ongoing investigation) — favors a durable IAM grant over a one-time file export, since the team will likely need to keep coming back to the dashboard.

**Why This Is Correct**

`roles/monitoring.viewer` is the predefined Cloud Monitoring role scoped specifically to viewing Monitoring data and configuration — dashboards, metrics, alerting policies — without reaching into unrelated Google Cloud resources. Granting it at the project level, then sharing the dashboard’s URL, is exactly the workflow Google documents: the people who need to view a dashboard get the Monitoring Viewer role on the project that stores it, and from there they can open the URL and interact with the same live dashboard, including its filters and time ranges, with no rebuilding or re-importing involved.

**Why the Other Options Are Not the Best Fit**

**Option A — Technically Possible but Not Best:** A JSON export captures the dashboard’s _definition_ (its widgets and layout), which is useful for recreating the dashboard in another project or checking it into version control, but it is not live data. The development team would need to import it somewhere they already have permissions, and even then they’d be looking at a copy, not the dashboard you’re actively using to investigate.

**Option B — Different Use Case:** Exporting time series data to CSV and routing it through BigQuery is a legitimate pattern for long-term analysis or custom querying, but it’s a heavier, custom-built workflow for a task that Cloud Monitoring already solves natively. It also strips away the dashboard’s visual context (the charts and layout that already isolated the anomalous client), forcing the team to reconstruct that view themselves.

**Option D — Technically Possible but Not Best:**`roles/viewer` does grant enough access to see the dashboard, so it isn’t outright broken — but it’s a basic/primitive role that provides view access across nearly all resource types in the project, far beyond what’s needed to look at one Monitoring dashboard. That’s more standing access than the task requires, which runs against the least-privilege principle Google’s own guidance calls out for this exact scenario.

**Exam Trap**

The trap is assuming “a role that works” is the same as “the Google-recommended role.” `roles/viewer` would technically let the team see the dashboard, so it’s tempting to treat it as equivalent to the Monitoring-specific option. The exam is testing whether you reach for the narrowest predefined role that satisfies the need — here, Monitoring Viewer — rather than a broader basic role that happens to also cover it.

**Foundation Concept**

The transferable principle is least privilege applied to sharing, not just to initial provisioning: when someone needs to view a specific Cloud Monitoring artifact, grant the Monitoring-scoped viewer role rather than a project-wide basic role, and let them reach the artifact through its own URL rather than exporting it into a different format. One precision note for real-world use: the correct role identifier is `roles/monitoring.viewer` (with a dot, under the `monitoring.*` permission namespace) — a role string like `roles/monitoringViewer` isn’t a real IAM role, so if you’re ever typing this into `gcloud` or Terraform, use the dotted form.

**Real-World Connection**

Teams running incident response commonly standardize on this exact pattern: grant a Monitoring-scoped viewer role to whoever needs visibility into an ongoing investigation, and share dashboard links directly, rather than emailing exports around. That keeps everyone looking at the same live, current data during the incident, and it means revoking access afterward is a single IAM change instead of tracking down every exported file that was sent out.

**Memory Hook**

Sharing a live Monitoring dashboard = grant `roles/monitoring.viewer` \+ send the URL, not an export.

**30-Second Exam Takeaway**

When a Google Cloud scenario asks how to let another team view a Cloud Monitoring dashboard you built, look for the option that grants the narrow `monitoring.viewer` role and shares the dashboard’s URL — exporting the dashboard or its data, and granting a broad basic role like `viewer`, are both signs of the wrong answer.

**Official References**

[**Google Cloud — Share a custom dashboard:**](https://cloud.google.com/monitoring/charts/share-dashboards) Supports: documents the exact recommended pattern of granting Monitoring Viewer and sharing the dashboard URL

[**Google Cloud — Cloud Monitoring roles and permissions:**](https://cloud.google.com/iam/docs/roles-permissions/monitoring) Supports: confirms the correct `roles/monitoring.viewer` identifier and its scope relative to other Monitoring roles

[**Google Cloud — Control access with IAM (Monitoring):**](https://cloud.google.com/monitoring/access-control) Supports: confirms `roles/viewer` is a broad, project-wide basic role, the basis for eliminating Option D on least-privilege grounds

---

## Question 52

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

Your organization maintains separate Google Kubernetes Engine (GKE) clusters for staging and production. You must select release channels according to Google-recommended practices, prioritizing cluster stability over early access to new features. Which configuration should you choose?

- [ ] A. Enroll production in the Stable channel and staging in the Regular channel.
- [ ] B. Enroll production in the Extended channel and staging in the Rapid channel.
- [x] C. Enroll both production and staging in the Stable channel.
- [ ] D. Enroll both production and staging in the Regular channel.

### Explanation

**Correct Answer**

**C. Enroll both production and staging in the Stable channel.**

**Exam Reasoning Explanation**

Apply two decisions: choose the channel that prioritizes release maturity, then keep staging representative of production. Stable satisfies the stability preference. Using it in both environments supports consistent validation before production deployment. Selecting different channels introduces version differences without serving the stated priority.

**Key Exam Clues**

  * **“Separate … clusters for staging and production” — Technical signal:** Staging should provide meaningful validation of the production environment.

  * **“Google-recommended practices” — Technical signal:** Consider coordinated upgrades across environments alongside channel selection.

  * **“Prioritizing cluster stability over early access” — Preference:** Favors Stable over the more feature-oriented channels.

**Why This Is Correct**

Stable receives releases after they have accumulated validation in Rapid and Regular, making it the channel intended for prioritizing maturity over new features. 

Using the same channel in staging and production supports testing the versions intended for production. Google’s upgrade guidance recommends progressively validating upgrades across environments using a common release channel. **Channel alignment alone does not guarantee identical versions or staging-first upgrades** ; upgrade timing and sequencing must also be managed. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Technically Possible but Not Best:** Stable suits production, and Regular staging can help evaluate upcoming changes. However, staging can move ahead of production, reducing its fidelity as the final validation environment. This arrangement is less aligned with the stated emphasis on stability and representative testing.

  * **Option B — Different Use Case:** Extended supports retaining a Kubernetes minor version longer, while Rapid provides earlier access to releases. Extended is useful when prolonged minor-version support is required; it is not simply a more thoroughly validated Stable channel. Rapid staging also emphasizes release freshness rather than the requested stability preference. 

  * **Option D — Technically Possible but Not Best:** Matching channels supports consistency, and Regular is Google’s default recommendation for balancing feature availability with stability. However, the question explicitly favors stability over feature freshness, making Stable the stronger choice. 

**Exam Trap**

Do not assume staging must always use a faster channel than production. Early feature exploration and final production validation serve different purposes. If the priority changed to **balancing feature freshness with stability** , Regular for both environments—option D—would become the better fit.

**Foundation Concept**

Release maturity, support duration, and upgrade order are separate decisions. Select a channel for the desired maturity level, keep validation environments representative, and control when upgrades progress between environments.

**Real-World Connection**

A team can place both clusters on Stable, validate an available upgrade in staging, observe workload health, and then advance production to the validated version. A controlled rollout reduces the risk that production encounters compatibility problems that staging never exercised. 

**Memory Hook**

For stability-focused production validation, align both environments on Stable and test upgrades in staging first.

**30-Second Exam Takeaway**

Choose the channel from the stated maturity-versus-freshness preference, then evaluate staging alignment. Maximum release maturity favors Stable; representative validation favors matching staging and production channels.

**Official References**

  * [**Google Cloud — About release channels:**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels)

Supports: Stable, Regular, Rapid, and Extended channel purposes and their distinctions.

[**Google Cloud — Best practices for GKE cluster upgrades:**](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters)

Supports: Representative testing environments, release-channel selection, maintenance controls, and progressive upgrades.

  * [**Google Cloud — About rollout sequencing with custom stages:**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing)

Supports: Same-channel recommendations and qualifying upgrades before advancing to subsequent environments.

  * [**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)

Supports: Objective 1.4, covering staging and production environments, GKE cluster management, and safe upgrading practices.

---

## Question 53

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Your organization is consolidating its monitoring and alerting systems. The centralized alerting platform exposes a webhook that is accessible only from within your VPC network. You need to deliver Google Cloud alert notifications to this endpoint while minimizing costs and following Google-recommended practices. Which approach should you choose?

- [x] A. Create a Pub/Sub topic and a notification channel that publishes to it, then configure a pull subscription to consume the notifications.
- [ ] B. Create a Pub/Sub topic and a notification channel that publishes to it, then configure a push subscription targeting the internal webhook.
- [ ] C. Create a webhook notification channel targeting the internal endpoint, then associate that channel with your alerting policies.
- [ ] D. Create a Pub/Sub topic and notification channel, deploy a Cloud Run function that forwards notifications to the internal endpoint using Direct VPC egress, and configure a push subscription targeting the function.

### Explanation

**Correct Answer**

**A. Create a Pub/Sub topic and a notification channel that publishes to it, then configure a pull subscription to consume the notifications.**

**Exam Reasoning Explanation**

Private endpoint reachability is the decisive constraint. Eliminate direct delivery mechanisms that cannot reach the internal webhook. Google explicitly recommends Pub/Sub notifications with a pull subscription for private Monitoring destinations. This approach also avoids mandating the additional function introduced by option D. 

**Key Exam Clues**

  * **“Accessible only from within your VPC network” — Hard constraint:** The destination cannot receive ordinary public webhook delivery.

  * **“Following Google-recommended practices” — Technical signal:** Select the documented private-endpoint notification pattern.

  * **“Minimizing costs” — Optimization objective:** Avoid unnecessary components, while accounting for the resources needed to consume messages.

**Why This Is Correct**

Cloud Monitoring publishes notifications to the configured Pub/Sub topic. A consumer with access to Pub/Sub and network reachability to the webhook retrieves those notifications through the pull subscription and invokes the internal endpoint.

The consumer initiates the Pub/Sub connection, so notification delivery does not require opening an inbound endpoint in the VPC. **The consuming application must perform the webhook call; creating a pull subscription alone does not invoke it.**

**Why the Other Options Are Not the Best Fit**

  * **Option B — Violates Requirement:** Push delivery sends HTTPS requests to a reachable subscriber endpoint. An arbitrary webhook accessible only through private VPC addressing cannot serve directly as that endpoint. Pub/Sub does not acquire private network connectivity merely because the topic belongs to the same project. 

  * **Option C — Violates Requirement:** A webhook notification channel is attractive because it directly matches the destination’s interface. However, Cloud Monitoring webhook channels require public endpoints and cannot directly deliver to this private webhook. It would fit if the destination were appropriately reachable through a public endpoint. 

  * **Option D — Technically Possible but Not Best:** A Cloud Run function can bridge Pub/Sub push delivery to the private webhook through Direct VPC egress. This is a valid architecture with appropriate invocation permissions and networking, but Google’s specific private-endpoint guidance recommends pull delivery. D becomes attractive when an event-driven serverless relay is an explicit architectural requirement. 

**Exam Trap**

Do not reject D as technically unsupported: Direct VPC egress supports second-generation Cloud Run functions. Conversely, do not assume A is automatically cheaper in every deployment. Its cost advantage is clearest when an existing integration service can consume the subscription; actual costs depend on subscriber hosting and notification volume.

**Foundation Concept**

Separate message delivery from private network access. A messaging subscription transports notifications, while an application with the necessary connectivity performs the internal action. Google’s documented integration recommendation does not establish a universal cost ranking for every possible implementation.

**Real-World Connection**

If the centralized alerting service supports a Pub/Sub consumer, integrate consumption into that service and have it invoke the webhook locally. Reusing that runtime can avoid deploying and maintaining a separate forwarding function.

**Memory Hook**

For private Monitoring destinations, use Pub/Sub pull and a consumer that can reach the internal endpoint.

**30-Second Exam Takeaway**

Check destination reachability before choosing a notification channel. For a private webhook, Google recommends Pub/Sub with pull consumption; a serverless forwarding function remains a feasible alternative when its operational benefits justify it.

**Official References**

  * [**Google Cloud Monitoring — Troubleshoot missing notifications:**](https://docs.cloud.google.com/monitoring/alerts/troubleshoot-missing-notifications)

Supports: The explicit private-endpoint recommendation, webhook restrictions, and pull-consumer connectivity.

  * [**Google Cloud Pub/Sub — Push subscriptions:**](https://docs.cloud.google.com/pubsub/docs/push)

Supports: Push delivery behavior and subscriber endpoint reachability requirements.

  * [**Google Cloud — Configure Direct VPC egress for 2nd gen functions:**](https://docs.cloud.google.com/functions/docs/running/direct-vpc)

Supports: The technical feasibility of option D and its generation-specific prerequisite.

  * [**Google Cloud — Professional Cloud DevOps Engineer Certification Exam Guide:**](https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf)

Supports: Objective 4.3, covering alerting policies and integration with third-party alerting tools, including webhooks.

---

## Question 54

*Domain 5: Optimizing Performance and Cost*

Your company offers a free photo-processing application. You are selecting compute infrastructure for its backend processing service, which:

  * Stores original and processed photos in Cloud Storage.

  * Can resume processing after a failure.

  * Is unsuitable for containerization.

There is no service level objective (SLO) for photo-processing completion time. You need to minimize compute costs. What should you do?

- [ ] A. Deploy the service on Cloud Run.
- [ ] B. Deploy the service on standard Compute Engine VMs covered by a three-year committed use discount.
- [ ] C. Deploy the service on Google Kubernetes Engine (GKE).
- [x] D. Deploy the service on Compute Engine Spot VMs.

### Explanation

**Correct Answer**

**D. Deploy the service on Compute Engine Spot VMs.**

**Exam Reasoning Explanation**

The workload tolerates interruptions, has flexible completion times, and requires a VM-based execution environment. These characteristics make Spot VMs the best fit among the available options. 

**Key Exam Clues**

  * **Recovery capability:** Processing can resume after a failure.

  * **Scheduling flexibility:** There is no processing-time SLO.

  * **Hard constraint:** The service is unsuitable for containerization.

  * **Primary objective:** Minimize costs.

**Why This Is Correct**

Google recommends Spot VMs for fault-tolerant workloads such as batch processing. They offer substantially discounted compute capacity in exchange for accepting possible interruption when Google reclaims resources. 

The service can run directly on the VM without containerization. Its recovery capability and flexible completion time accommodate the interruptions and capacity delays associated with Spot VMs.

**Why the Other Options Are Not the Best Fit**

  * **A — Violates Requirement:** Cloud Run executes workloads in containers. The service’s containerization constraint makes it unsuitable, even though Cloud Run supports batch jobs. 

  * **B — Technically Possible but Not Best:** Standard VMs can run the service, and committed use discounts benefit predictable usage. However, this option requires a three-year commitment and does not exploit the workload’s suitability for discounted interruptible capacity. 

  * **C — Violates Requirement:** GKE is a container orchestration platform designed to deploy and operate containerized applications. It does not match the stated execution constraint. 

**Exam Trap**

Spot VMs can be interrupted and might not be immediately available again. The processing system must implement recovery and retry behavior; selecting Spot VMs does not provide application recovery automatically. 

**Foundation Concept**

Spot pricing exchanges interruption tolerance for lower compute costs. Committed use discounts exchange a minimum usage or spending commitment for discounted prices. 

**Real-World Connection**

Keep processing progress in durable storage and make retries safe. A replacement worker can then resume unfinished work without corrupting or unnecessarily duplicating completed outputs.

**Memory Hook**

Resumable processing with flexible deadlines is a strong candidate for Spot VMs.

**30-Second Exam Takeaway**

Choose **D**. The service can tolerate interruptions and delays, making Spot VMs the appropriate cost-saving option.

**Official References**

  * [**Spot VMs**](https://docs.cloud.google.com/compute/docs/instances/spot)  
Supports: Discounted capacity, preemption, availability limitations, and suitability for fault-tolerant batch workloads.

  * [**Committed use discounts for Compute Engine**](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)  
Supports: Commitment requirements and suitability for predictable usage.

  * [**Cloud Run container runtime contract**](https://docs.cloud.google.com/run/docs/container-contract)  
Supports: Cloud Run’s container execution requirements.

  * [**GKE overview**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)  
Supports: GKE’s role as a platform for containerized applications.

---

## Question 55

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

Your organization is moving its production workloads to Google Cloud. During the migration, you need to establish site reliability engineering (SRE) practices that reduce customer disruption when future incidents occur.

Which two practices should you implement? **Choose two.**

- [x] A. Maintain current playbooks that explain how to troubleshoot problems and mitigate their impact.
- [ ] B. Allow every team to modify the production environment when resolving issues.
- [ ] C. Configure alerts for the SRE team based on the system’s internal behavior.
- [x] D. Automate recurring tasks to analyze key impact information and recommend mitigation actions to on-call engineers.
- [ ] E. Grant full operational autonomy and permissions exclusively to the on-call team.

### Explanation

**Correct Answer**

**A. Maintain current playbooks that explain how to troubleshoot problems and mitigate their impact.**

**D. Automate recurring tasks to analyze key impact information and recommend mitigation actions to on-call engineers.**

**Exam Reasoning Explanation**

The objective is to reduce customer disruption during incidents. Select practices that help responders assess problems and restore service quickly. A provides prepared response procedures; D reduces repetitive analysis and supports faster decisions. Each is useful independently, and together they improve incident response readiness.

**Key Exam Clues**

  * **“Production workloads” — Operational signal:** Response procedures must support real service failures.

  * **“During the migration” — Timing requirement:** Establish readiness before incidents occur.

  * **“Reduce customer disruption” — Decisive objective:** Prioritize effective mitigation and shorter recovery times.

  * **“Choose two” — Selection requirement:** Select both documented procedures and operational automation.

**Why This Is Correct**

**A — Maintained playbooks:** Playbooks capture incident impact, debugging guidance, and possible mitigation steps. Keeping them aligned with production changes helps responders act consistently. Google’s SRE Workbook explicitly connects playbooks with reduced repair time, stress, and human error.

**D — Diagnostic and response automation:** Automating repeatable information gathering and analysis reduces manual effort and gives responders useful context sooner. Recommendations can support human decisions for unfamiliar situations. Google’s SRE guidance identifies consistency, faster action, and faster repairs as benefits of appropriately designed automation. 

**Why the Other Options Are Not the Best Fit**

**Option B — Technically Possible but Not Best:** Giving every team production modification capability does not establish a coordinated response process. Google recommends defined incident roles and an operations team responsible for system changes during an incident. Uncoordinated interventions can worsen an outage. 

**Option C — Technically Possible but Not Best:** Internal monitoring is valuable and can support valid alerts. However, internal behavior alone does not establish that an alert is urgent, actionable, or associated with actual or imminent customer impact. Google recommends emphasizing symptoms and actionable problems when paging responders. A and D more directly describe effective mitigation practices. 

**Option E — Technically Possible but Not Best:** On-call engineers need sufficient authority to respond, but exclusive, unrestricted permissions are not a general SRE requirement. Use scoped permissions and coordinated escalation to additional specialists when necessary. Google recommends least privilege, including temporary elevated access where appropriate. 

**Exam Trap**

Do not interpret C as proof that internal metrics are unsuitable for alerting. An internally measured request-error rate can reveal customer impact. The weakness is that the option specifies internal behavior without establishing alert actionability or impact.

**Foundation Concept**

Effective incident response combines prepared knowledge, timely evidence, clear responsibilities, and safe mitigation. Automation handles repeatable work; responders apply judgment when circumstances require it. Mitigation can restore service before the complete root cause is understood.

**Real-World Connection**

Before migration cutover, rehearse a failed deployment. An automated diagnostic tool can gather recent changes and error trends, while a maintained playbook guides rollback and recovery checks. This tests both the documentation and tooling before customers depend on them.

**Memory Hook**

Prepare the response in playbooks; accelerate it with tested automation.

**30-Second Exam Takeaway**

For reducing incident impact, choose maintained troubleshooting and mitigation playbooks plus automation that supports responders. Evaluate alerting by actionability and customer impact, and grant production access according to defined responsibilities.

**Official References**

  * [**Google SRE Workbook — On-Call**](https://sre.google/workbook/on-call/)  
Supports: Playbook contents, maintenance, and operational automation.

  * [**Google SRE — The Evolution of Automation at Google**](https://sre.google/sre-book/automation-at-google/)  
Supports: Consistency and faster incident recovery through automation.

  * [**Google SRE — Monitoring Distributed Systems**](https://sre.google/sre-book/monitoring-distributed-systems/)  
Supports: Symptom-oriented, actionable alerting and valid internal monitoring.

  * [**Google SRE — Managing Incidents**](https://sre.google/sre-book/managing-incidents/)  
Supports: Coordinated production changes, incident roles, and delegation.

  * [**Google Cloud — Use IAM securely**](https://docs.cloud.google.com/iam/docs/using-iam-securely)  
Supports: Least privilege and appropriately scoped production permissions.

---

## Question 56

*Domain 3: Applying Site Reliability Engineering Practices*

A new version of your Cloud Run application is being introduced through a canary rollout. An SRE colleague reports that the application is now breaching a service level objective (SLO). Your immediate priority is to restore healthy service as quickly as possible. Which action should you take **FIRST**?

- [ ] A. Update the traffic allocation so that the latest revision receives 100% of requests.
- [x] B. Update the traffic allocation so that the previous revision receives 100% of requests.
- [ ] C. Deploy a new revision from the application’s last known good version.
- [ ] D. Investigate the source of the latency using Cloud Trace.

### Explanation

**Correct Answer**

**B. Update the traffic allocation so that the previous revision receives 100% of requests.**

**Exam Reasoning Explanation**

The immediate requirement is service recovery. The recent rollout provides a plausible mitigation target, and traffic reassignment offers a direct way to reverse exposure to that change. Prioritize restoring the previous serving revision over deploying another revision or completing a root-cause investigation. Google’s SRE guidance prioritizes mitigating user impact before investigating the underlying cause. 

**Key Exam Clues**

  * **“Canary rollout” — Technical signal:** Traffic is being introduced to a candidate revision while an earlier revision remains available.

  * **“Breaching a service level objective” — Technical signal:** Reliability has degraded sufficiently to require intervention.

  * **“Restore healthy service as quickly as possible” — Hard constraint:** Favor the shortest available recovery path.

  * **“FIRST” — Sequence instruction:** Choose immediate mitigation before subsequent diagnosis and remediation.

**Why This Is Correct**

Cloud Run supports rolling back by assigning 100% of service traffic to an existing previous revision. Changing traffic allocation does not require deploying the application again.

This answer assumes the previous revision remains a healthy, compatible rollback target. Traffic changes are not instantaneous, and in-flight requests can continue during the transition, so confirm recovery after changing the allocation. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** This completes the rollout to the revision associated with the emerging reliability problem, potentially increasing user impact. It would suit promoting a successfully validated canary rather than responding to the reported degradation.

  * **Option C — Technically Possible but Not Best:** Redeploying a known good application version can restore service, but it introduces another deployment when the existing previous revision can receive traffic directly. The additional deployment work delays the available mitigation. 

  * **Option D — Technically Possible but Not Best:** Cloud Trace helps investigate request latency and performance bottlenecks. However, investigation alone does not redirect traffic or restore service. It is appropriate for diagnosing the problem after mitigation, or in parallel without delaying recovery.

**Exam Trap**

Identifying the exact defect can feel like the necessary first step, but a safe rollback can reduce impact before that investigation finishes. If no usable previous revision remained available, deploying a new revision from the known good application version—option C—could become necessary.

**Foundation Concept**

Canary deployment limits exposure while evaluating a candidate release. Retaining the established baseline makes reversal practical; determining why the candidate failed is a separate task from restoring acceptable service.

**Real-World Connection**

After redirecting traffic, monitor current error rates and latency to confirm that user experience improves. Preserve the unsuccessful revision’s logs and traces for investigation. This approach reduces recovery time while retaining evidence needed to prevent recurrence.

**Memory Hook**

When a canary degrades service, restore traffic to the healthy baseline before pursuing detailed diagnosis.

**30-Second Exam Takeaway**

For **FIRST** -action questions during a rollout incident, look for an available mitigation that reduces user impact with minimal additional change. Prefer traffic rollback to an existing healthy revision over redeployment or extended troubleshooting.

**Official References**

  * [**Google Cloud Run — Rollbacks, gradual rollouts, and traffic migration:**](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration)

Supports: Routing all traffic to a previous revision, changing allocation without redeployment, and transition behavior.

  * [**Google SRE Workbook — Incident Response:**](https://sre.google/workbook/incident-response/)

Supports: Prioritizing mitigation before root-cause analysis and using rollback to reduce incident impact.

  * [**Google Cloud — Cloud Trace overview:**](https://docs.cloud.google.com/trace/docs/overview)

Supports: Cloud Trace’s role in latency analysis and performance troubleshooting.

---

## Question 57

*Domain 2: Building and Implementing CI/CD Pipelines*

Jenkins orchestrates application deployments to Google Kubernetes Engine (GKE) and on-premises VMs. Following an expansion of the on-premises infrastructure, deployments to those VMs take longer to start, although resource utilization remains within normal levels. You need to reduce the delay before on-premises deployments begin. Which change should you make?

- [ ] A. Increase the CPU performance and memory capacity of the on-premises VMs.
- [ ] B. Adopt blue-green deployments for applications running on the on-premises VMs.
- [x] C. Increase the configured number of Jenkins executors.
- [ ] D. Configure Jenkins to retrieve deployment artifacts from an on-premises artifact repository.

### Explanation

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

---

## Question 58

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

You are deploying a web application to Cloud Run. Expected traffic varies from 10 requests per second during quiet periods to 1,000 requests per second during peak periods. You need automatic scaling that responds efficiently to demand while staying within the project’s resource quotas.

What should you do?

- [ ] A. Manually change the instance count throughout the day according to observed traffic.
- [x] B. Set appropriate resource limits for the Cloud Run service and verify that project quotas support the intended scaling range.
- [ ] C. Configure CPU-based autoscaling with a target utilization of 80%.
- [ ] D. Configure request-count-based autoscaling with a target of 500 requests per instance.

### Explanation

**Correct Answer**

**B. Set appropriate resource limits for the Cloud Run service and verify that project quotas support the intended scaling range.**

**Exam Reasoning Explanation**

The requirements combine automatic capacity adjustment with resource control. A scaling metric determines when more instances are needed; it does not establish how much capacity the service may consume. B addresses the service’s resource configuration and the quota needed to support its scaling range.

**Key Exam Clues**

  * **“10 … to 1,000 requests per second” — Workload signal:** Capacity must adapt to substantial demand changes.

  * **“Automatic scaling” — Hard requirement:** Repeated manual instance adjustments are unsuitable.

  * **“Within the project’s resource quotas” — Decisive constraint:** Resource sizing and scaling limits must align with available quota.

**Why This Is Correct**

In practice, choose suitable CPU and memory allocations per instance, configure a maximum instance count, and check the relevant regional project quotas. Cloud Run recommends service-level maximum instances unless revision-level limits are specifically needed. 

Review quota availability before peak demand and request increases where necessary. Available quota does not guarantee that regional capacity will always be available. 

Per-instance CPU and memory limits alone are insufficient: the instance-count limit also matters. Leave capacity headroom because Cloud Run can briefly exceed its configured maximum instance count in certain circumstances.

**Why the Other Options Are Not the Best Fit**

**Option A — Violates Requirement:** Manual adjustments do not meet the requirement to use autoscaling. Cloud Run already supports automatically adjusting instance counts as workload demand changes. 

**Option C — Technically Possible but Not Best:** Current Cloud Run supports custom CPU utilization targets, including 80%. However, selecting that target does not establish resource ceilings or ensure sufficient quota. The appropriate utilization target also depends on the workload’s performance requirements. 

**Option D — Incorrect as Stated:** Cloud Run’s request-based scaling considers **concurrent requests** , rather than an arbitrary cumulative request count. If “500 requests per instance” means concurrency, it could describe a configuration choice, but it still does not address the quota requirement. 

**Exam Trap**

Do not reject C by assuming Cloud Run’s CPU target cannot be customized; current documentation permits it. The distinction is between a **scaling target** and a **resource boundary**. CPU-target tuning becomes relevant after resource sizing, instance limits, and quotas have been established.

**Foundation Concept**

Autoscaling has three separate concerns: signals that indicate demand, limits that constrain scaling, and quotas that govern available resources. Requests per second alone cannot determine the required instance count; request duration and each instance’s processing capacity also matter.

**Real-World Connection**

Load-test the application at 1,000 requests per second, measure latency and resource usage, and select an appropriate instance configuration and scaling range. Check regional quotas and leave headroom for other workloads and deployment activity. This provides evidence that the planned configuration can support peak traffic.

**Memory Hook**

Scaling targets guide growth; instance limits and quotas define its boundaries.

**30-Second Exam Takeaway**

When a question emphasizes quota-aware autoscaling, choose resource sizing, maximum instances, and quota validation. A CPU or concurrency target alone does not satisfy that requirement.

**Official References**

  * [**Cloud Run instance autoscaling**](https://docs.cloud.google.com/run/docs/about-instance-autoscaling)  
Supports: Automatic scaling and CPU/concurrency scaling signals.

  * [**Set maximum instances for services**](https://docs.cloud.google.com/run/docs/configuring/max-instances)  
Supports: Scaling limits, service-level configuration, and temporary overshoot.

  * [**Cloud Run quotas and limits**](https://docs.cloud.google.com/run/quotas)  
Supports: Regional resource quotas and quota adjustments.

  * [**Configure custom scaling controls**](https://docs.cloud.google.com/run/docs/configuring/scaling-controls)  
Supports: Configurable CPU targets and why option C is feasible but incomplete.

---

## Question 59

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

Several applications share a load balancer protected by Google Cloud Armor. You need a dashboard that shows blocked requests specifically for the HTTPS API URL prefix `mountkirk.com/api` and identifies the request parameter names associated with the blocking matches. Which approach should you use?

- [ ] A. Create a log-based counter metric filtered by `configuredAction="ALLOW"` and the API `requestUrl` prefix. Extract `matchedFieldName` as a label and chart the counts in Cloud Monitoring grouped by that label.
- [ ] B. Create a Boolean log-based metric filtered by `configuredAction="DENY"`. Extract `matchedFieldName` as a label and chart the results in Cloud Monitoring grouped by that label.
- [x] C. Create a log-based counter metric filtered by `configuredAction="DENY"` and the API `requestUrl` prefix. Extract `matchedFieldName` as a label and chart the counts in Cloud Monitoring grouped by that label.
- [ ] D. Chart the built-in `networksecurity.googleapis.com/https/request_count` metric in Cloud Monitoring and filter its `blocked` label to `true`.

### Explanation

**Correct Answer**

**C. Create a log-based counter metric filtered by**`**configuredAction="DENY"**`**and the API**`**requestUrl**`**prefix. Extract**`**matchedFieldName**`**as a label and chart the counts in Cloud Monitoring grouped by that label.**

**Exam Reasoning Explanation**

The solution must provide three things: blocked-request counts, isolation of the API’s traffic, and a breakdown by matched parameter name. A filtered counter supplies the counts and URL scope; an extracted label supplies the breakdown. A total blocked-request metric lacks the required detail.

**Key Exam Clues**

  * **“Several applications share a load balancer” — Technical signal:** Load-balancer-wide totals can include unrelated application traffic.

  * **“Specifically for …**`**mountkirk.com/api**`**” — Hard constraint:** Filter the request URL before counting.

  * **“Blocked requests” — Hard constraint:** Select denied traffic rather than allowed traffic.

  * **“Request parameter names” — Hard constraint:** Preserve the matched field name as a metric label.

**Why This Is Correct**

A counter metric counts matching log entries. For enforced deny rules, the filter uses the documented action value and complete field paths:
    
          1. jsonPayload.enforcedSecurityPolicy.configuredAction="DENY"
      2. httpRequest.requestUrl=~"^https://mountkirk[.]com/api"

Extract a string label named `matchedFieldName` using:
    
          1. EXTRACT(jsonPayload.enforcedSecurityPolicy.matchedFieldName)

Group the dashboard’s series by this label and sum the counts within each group. Log fields become usable grouping dimensions only after extraction into metric labels. 

**Prerequisite:** Relevant request logs must contain the matched-field details. Cloud Armor verbose logging supplies these details for applicable WAF matches. The field can be empty when the match does not identify a key-value parameter. 

**Why the Other Options Are Not the Best Fit**

  * **Option A — Violates Requirement:** The URL filter and grouping approach are useful, but `ALLOW` selects permitted requests. It cannot provide the required denied-request breakdown.

  * **Option B — Incorrect:** User-defined log-based metrics support counter and distribution types; Boolean is not a supported user-defined log-based metric type. This option also omits the API URL filter. A Boolean-valued _label_ is supported, but that is different from creating a Boolean log-based metric. 

  * **Option D — Different Use Case:** The built-in metric can show blocked-request totals through its `blocked` label. However, it does not expose `requestUrl` or `matchedFieldName` dimensions, so it cannot provide the requested URL-specific parameter breakdown. 

**Exam Trap**

The built-in metric’s `blocked` Boolean is tempting, but it identifies enforcement results without supplying parameter-level detail. D would fit a requirement for aggregate blocked-request totals. In request-log filters, use the documented `DENY` action value rather than treating the metric label as an action string.

**Foundation Concept**

A metric filter decides **which events count** ; extracted labels decide **how those events can be categorized**. Cloud Armor denies requests—the matched parameter identifies information that triggered a rule, rather than a parameter being independently blocked.

**Real-World Connection**

A dashboard showing increased matches for a parameter such as `search` can guide investigation of a possible WAF false positive. Keep label values controlled: highly variable values create additional time series and can increase monitoring costs. 

**Memory Hook**

Filter the denied requests, count the matching logs, and extract the field needed for grouping.

**30-Second Exam Takeaway**

Choose built-in metrics when their existing dimensions satisfy the requirement. When the dashboard needs URL filtering and request-field detail available in logs, use a log-based counter with an extracted label.

**Official References**

  * [**Google Cloud Armor — Verbose logging:**](https://docs.cloud.google.com/armor/docs/verbose-logging)

Supports: The `DENY` action example, matched-field details, verbose logging prerequisites, and empty-field limitations.

  * [**Cloud Logging — Log-based metrics overview:**](https://docs.cloud.google.com/logging/docs/logs-based-metrics)

Supports: Counter behavior, supported user-defined metric types, and charting log-based metrics.

  * [**Cloud Logging — Configure labels on log-based metrics:**](https://docs.cloud.google.com/logging/docs/logs-based-metrics/labels)

Supports: Label extraction, `EXTRACT` syntax, grouping dimensions, and cardinality considerations.

  * [**Cloud Monitoring — Google Cloud metrics: networksecurity:**](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#networksecurity)

Supports: The built-in request-count metric and its available labels.

---

## Question 60

*Domain 2: Building and Implementing CI/CD Pipelines*

Your team builds an application from a Dockerfile using Cloud Build and stores the resulting container images in Artifact Registry. Developers report that builds take too long. You need to reduce build times using Google-recommended practices. What should you do?

- [x] A. Use `--cache-from` to reference a previously built image in Artifact Registry, and copy frequently modified files in later Dockerfile instructions.
- [ ] B. Use `--cache-from` to reference a previously built image in Artifact Registry, and copy frequently modified files in earlier Dockerfile instructions.
- [ ] C. Store the container-layer cache in Cloud Storage, and copy frequently modified files in earlier Dockerfile instructions.
- [ ] D. Store the container-layer cache in Cloud Storage, and copy frequently modified files in later Dockerfile instructions.

### Explanation

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

---
