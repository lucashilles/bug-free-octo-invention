# Professional Cloud DevOps Engineer — Practice Exam 5

65 questions.

## Question 1

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You created a **Cloud Monitoring chart for CPU utilization** in a **dashboard** within your **workspace project**. You want to **share the chart with your Site Reliability Engineering (SRE) team only**. You want to ensure that you **follow the principle of least privilege**. What should you do?

- [ ] **I.** Share the **workspace Project ID** with the **SRE team**. Assign the **SRE team** the **Monitoring Viewer IAM role** in the workspace project.
- [ ] **II.** Share the **workspace Project ID** with the **SRE team**. Assign the **SRE team** the **Dashboard Viewer IAM role** in the workspace project.
- [x] **III.** Click **“Share chart by URL”** and provide the **URL** to the **SRE team**. Assign the **SRE team** the **Monitoring Viewer IAM role** in the workspace project.
- [ ] **IV.** Click **“Share chart by URL”** and provide the **URL** to the **SRE team**. Assign the **SRE team** the **Dashboard Viewer IAM role** in the workspace project.

### Explanation

**Correct Option:**

**C (III. Click “Share chart by URL” and provide the URL to the SRE team. Assign the SRE team the Monitoring Viewer IAM role in the workspace project.)**

Justification:

Cloud Monitoring supports sharing **individual charts from Metrics Explorer** using the _Share chart by URL_ feature

[Share charts in Metrics Explorer](https://cloud.google.com/monitoring/charts/metrics-explorer#share-charts)

For the SRE team to view the chart and underlying metric data, they need the **Monitoring Viewer role (**`**roles/monitoring.viewer**`**)** , which grants **read-only access to monitoring data and configurations**

[Monitoring IAM roles](https://cloud.google.com/monitoring/access-control#predefined_roles)

More restrictive roles like **Dashboard Viewer/Configuration Viewer** only allow viewing dashboard _configurations_ and don’t allow access to metric data. That’s why they cannot be used for chart sharing.

Since the requirement is to **share the chart** , not the entire dashboard, option C best matches both the technical capability and the principle of least privilege achievable in this scenario.

**Why other options are not a perfect fit**

**A (Project ID + Monitoring Viewer)** :  
Technically valid (they can see dashboards and charts), but it shares **all monitoring dashboards and metrics in the project** , not just the specific chart. This goes beyond the requirement and does not strictly follow “share the chart only.”

**B (Project ID + Dashboard Viewer)** :  
This role (actually “Dashboard Configuration Viewer” in practice) only provides access to dashboard definitions. It does not allow viewing chart **data**. Users will see errors like _“Invalid resource type/metric type”_. Not valid.

**D (Share URL + Dashboard Viewer)** :  
Same problem as B — Dashboard Viewer/Config Viewer cannot access metric data, so the shared chart URL fails with errors. Not valid.

**Final Answer: C is correct.**

Because:

It leverages the official **“share chart by URL”** feature in Metrics Explorer.

It grants the **Monitoring Viewer role** , the minimum role that allows access to metric data needed for charts.

Other options either over-share (A) or don’t work at all (B, D).

---

## Question 2

*Domain 2: Building and Implementing CI/CD Pipelines*

You use a **multi-step Cloud Build pipeline** to build and deploy your application to **Google Kubernetes Engine (GKE)**. You want to **integrate with a third-party monitoring platform** by performing an **HTTP POST of the build information to a webhook**. You want to **minimize development effort**.

What should you do?

- [ ] **A.** Add logic to **each Cloud Build step** to **HTTP POST the build information** to a webhook.
- [ ] **B.** Add a **new step at the end of the pipeline** in **Cloud Build** to **HTTP POST the build information** to a webhook.
- [ ] **C.** Use **Cloud Logging** to create a **logs-based metric** from the **Cloud Build logs**. Create an **alert** with a **Webhook notification type**.
- [x] **D.** Create a **Cloud Pub/Sub push subscription** to the **Cloud Build**`**cloud-builds**`**Pub/Sub topic** to **HTTP POST the build information** to a webhook.

### Explanation

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

---

## Question 3

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

**You have a pool of application servers running on Compute Engine. You need to provide a secure solution that requires the least amount of configuration and allows developers to easily access application logs for troubleshooting.**

**How would you implement the solution on Google Cloud?**

- [x] **A.Deploy the Cloud Logging agent** to the application servers.
    **Give the developers the IAM Logs Viewer role** to access **Cloud Logging** and view logs.
- [ ] **B.Deploy the Cloud Logging agent** to the application servers.
    **Give the developers the IAM Logs Private Logs Viewer role** to access **Cloud Logging** and view logs.
- [ ] **C.Deploy the Cloud Monitoring agent** to the application servers.
    **Give the developers the IAM Monitoring Viewer role** to access **Cloud Monitoring** and view metrics.
- [ ] **D.Install the**`**gsutil**`**command-line tool** on your application servers.
    **Write a script using**`**gsutil**` to upload application logs to a **Cloud Storage bucket** , and then schedule it to run via `cron` every 5 minutes.
    **Give the developers IAM Object Viewer access** to view the logs in the specified bucket.

### Explanation

**Correct Answer:**

**A.**

  * **Deploy the Cloud Logging agent** to the application servers.

  * **Give the developers the IAM Logs Viewer role** to access **Cloud Logging** and view logs.

**Explanation:**

The **best and easiest** approach to allow developers to access logs is to:

  1. **Deploy the Cloud Logging agent** – This automatically **collects logs from Compute Engine VMs** and **sends them to Cloud Logging**.

  2. **Grant the IAM Logs Viewer role** – This allows developers to **view logs in the Cloud Logging UI** without needing full admin access.

  3. **Least configuration effort** – The Cloud Logging agent **integrates natively with Compute Engine** and **requires minimal setup**.

**Why Other Options Are Incorrect:**

**B. Logs Private Logs Viewer Role** – This role **is used for viewing private logs** , which include **admin activity and system logs**. It **is not required for regular application logs**.

**C. Cloud Monitoring Agent + Monitoring Viewer Role** – The **Cloud Monitoring agent** is for **metrics (CPU, memory, network, etc.)** , **not logs**. Developers need access to **Cloud Logging, not Cloud Monitoring**.

**D. Using**`**gsutil**`**to upload logs manually** – This is **overly complex and inefficient** :

  * Requires **writing and maintaining a log upload script**.

  * Logs will only be available in **Cloud Storage** , making **real-time log analysis difficult**.

  * **Cloud Logging already provides native log storage and filtering** , eliminating the need for manual uploads.

**Reference Documentation:**

[Installing the Cloud Logging Agent](https://cloud.google.com/logging/docs/agent/logging/install-index)  
[ IAM Roles for Cloud Logging](https://cloud.google.com/logging/docs/access-control)

---

## Question 4

*Domain 5: Optimizing Performance and Cost*

**You manage the backend infrastructure of a mobile game running on a Google Kubernetes Engine (GKE) cluster, serving HTTP requests from users. To optimize network expenses, what step should you take?**

- [ ] I. Establish the VPC as a Shared VPC Host project.
- [x] II. Set up your network services on the Standard Tier.
- [ ] III. Configure your Kubernetes cluster as a Private Cluster.
- [ ] IV. Implement a Google Cloud HTTP Load Balancer as Ingress.

### Explanation

**Correct option: II**

**Why option II is correct**

**II. Set up your network services on the Standard Tier.**

When the explicit goal is to **optimize network expenses** , the most direct and impactful lever in Google Cloud is the **Network Service Tier** selection.

  * **Standard Tier** is priced lower than Premium Tier because traffic is routed over the public internet instead of Google’s global private backbone.

  * For a **mobile game backend** where traffic is typically **regional** and ultra-low global latency is not the primary requirement, Standard Tier provides **significant cost savings** on:

    * Network egress

    * Load-balancing data processing

  * This choice requires **no changes to application code or cluster design** , making it the cleanest cost-optimization step.

This is a classic **exam signal** : when cost optimization is the focus (not latency, availability, or security), **Standard Tier** is the expected answer.

Authoritative documentation:  
<https://cloud.google.com/network-tiers/docs/overview>

**Why the other options are not correct**

**I. Establish the VPC as a Shared VPC Host project.**  
Shared VPC improves **network governance and IAM separation** , not runtime network costs. It does not reduce egress or traffic processing charges.

**III. Configure your Kubernetes cluster as a Private Cluster.**  
Private clusters improve **security** by removing public node IPs. They do not reduce inbound HTTP traffic costs and may even introduce additional NAT costs.

**IV. Implement a Google Cloud HTTP Load Balancer as Ingress.**  
While this is architecturally recommended for HTTP workloads, **external HTTP(S) Load Balancing runs on Premium Tier by default** , which is **more expensive** , not cheaper. It optimizes performance, not cost.

**Final answer:** **II**

---

## Question 5

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

**Your company encounters frequent bugs, outages, and performance issues in its production systems. Developers often utilize the production environment for new feature development and bug fixes, alongside conducting configurations and experiments, causing disruptions for users. Moreover, testers conduct load testing in the production environment, impacting system performance. How should you redesign the environment to mitigate bugs and outages in production while enabling effective load testing of new features?**

- [ ] I. Deploy an automated testing script within the production environment to promptly identify failures as they occur.
- [ ] II. Establish a dedicated development environment with scaled-down server capacity, granting access solely to developers and testers.
- [ ] III. Strengthen security measures within the production environment to prevent unauthorized alterations by developers, and implement a regulated update schedule, permitting only one update annually.
- [x] IV. Create separate environments: one for development purposes focused on code creation, and another for testing configurations, experiments, and load testing.

### Explanation

**Correct option: IV**

**Why option IV is correct**

**IV. Create separate environments: one for development purposes focused on code creation, and another for testing configurations, experiments, and load testing.**

This option directly addresses the **root causes** of the production instability while aligning with **SRE and DevOps best practices**.

Core reliability principles at play:

  * **Production must be protected** : SRE strongly discourages using production for development, experimentation, or load testing because it introduces uncontrolled risk and user-facing impact.

  * **Environment isolation** : Separating **development** , **testing (including load testing and experiments)** , and **production** environments ensures that failures, misconfigurations, and performance tests do not affect real users.

  * **Realistic testing without user impact** : A dedicated testing environment allows load tests, chaos experiments, and configuration validation under controlled conditions that resemble production, without risking outages.

  * **Reduced blast radius** : Bugs and performance regressions are caught before deployment to production, significantly reducing incidents.

This redesign improves:

  * System reliability

  * User experience

  * Developer velocity

  * Confidence in releases

Google SRE explicitly promotes isolating environments to reduce risk and prevent accidental production impact.

**Authoritative documentation:**  
<https://sre.google/sre-book/release-engineering/>

**Why the other options are not suitable**

**I. Deploy automated testing scripts in production.**  
Automated testing is valuable, but running tests _in production_ does not prevent outages caused by experiments, load testing, or unsafe changes. It detects failures after they impact users rather than preventing them.

**II. Establish a single scaled-down development environment for both developers and testers.**  
This partially helps but is insufficient. Load testing and configuration experiments require an environment closer to production scale and behavior. Mixing development and testing still increases risk and reduces test accuracy.

**III. Restrict production changes and allow only one update per year.**  
This is an extreme and impractical approach that harms agility and does not solve the underlying problem of improper environment usage. SRE encourages _frequent, safe releases_ , not infrequent ones.

**Final answer:** **IV**

---

## Question 6

*Domain 3: Applying Site Reliability Engineering Practices*

**You're on-call for an infrastructure service with numerous dependent systems. An alert notifies you of widespread failure in serving requests, impacting all dependent systems with hundreds of thousands of users. Following Site Reliability Engineering (SRE) incident management protocols, you designate yourself as Incident Commander (IC) and assign two experienced team members as Operations Lead (OL) and Communications Lead (CL). What's your immediate next step?**

- [ ] I. Initiate actions to mitigate user impact and implement the mitigations in production.
- [ ] II. Contact the owners of the affected services and keep them informed about the incident status.
- [x] III. Establish a dedicated communication channel for incident responders and leads to ensure seamless coordination.
- [ ] IV. Begin a postmortem process, incorporating incident details, share the draft internally, and solicit input from internal stakeholders.#

### Explanation

**Correct option: III**

**Why option III is correct**

**III. Establish a dedicated communication channel for incident responders and leads to ensure seamless coordination.**

Under **Google SRE incident management** , once an incident is declared and roles are assigned (IC, Operations Lead, Communications Lead), the **very next step** is to **create a single, dedicated communication channel** (for example, a Slack channel or conference bridge).

Core SRE fundamentals behind this step:

  * **Single source of truth:** All responders coordinate in one place, avoiding fragmented updates across emails, chats, or calls.

  * **Clear command structure:** The IC can direct actions efficiently, the OL can report mitigation progress, and the CL can prepare consistent external/internal updates.

  * **Reduced cognitive load:** Responders focus on fixing the issue rather than tracking scattered communications.

  * **Scalability:** As more responders join, they can quickly get context without interrupting mitigation work.

Google SRE explicitly defines this as an _early, mandatory step_ before mitigation actions begin.

**Authoritative documentation:**  
<https://sre.google/sre-book/managing-incidents/>

**Why the other options are not correct**

**I. Initiate actions to mitigate user impact immediately.**  
Mitigation is critical, but acting _before_ establishing a coordination channel leads to duplicated effort, missed context, and confusion—especially in large, multi-team incidents.

**II. Contact owners of affected services right away.**  
Stakeholder communication is important, but it is the responsibility of the **Communications Lead** _after_ coordination mechanisms are in place.

**IV. Begin a postmortem process.**  
Postmortems occur **after incident resolution** , not during active response.

**Final answer:** **III**

---

## Question 7

*Domain 5: Optimizing Performance and Cost*

**To diminish costs for a stable, business-critical workload running on a fixed set of Compute Engine instances over several months, without compromising performance, what's the recommended approach?**

- [x] I. Opt for Committed Use Discounts to avail discounted pricing.
- [ ] II. Transition the instances to a Managed Instance Group for enhanced management and potential cost efficiencies.
- [ ] III. Convert the instances to preemptible virtual machines to benefit from lower pricing for non-essential workloads.
- [ ] IV. Set up an Unmanaged Instance Group dedicated to running the workload on instances.

### Explanation

**Correct option: I**

**Why option I is correct**

**I. Opt for Committed Use Discounts to avail discounted pricing.**

For a **stable, business-critical workload** running on a **fixed set of Compute Engine instances over several months** , **Committed Use Discounts (CUDs)** are the **recommended and exam-correct approach**.

Core cost-optimization principles:

  * **Designed for predictable workloads:** CUDs provide significant discounts (up to ~55–70%) in exchange for a **1-year or 3-year commitment** on vCPU, memory, or specific machine types.

  * **No performance impact:** Unlike preemptible/Spot VMs, committed instances **retain full availability and performance guarantees**.

  * **No architectural changes required:** You continue running the same instance types; the discount is applied automatically to matching usage.

  * **SRE-aligned:** Reduces cost while maintaining reliability for business-critical services.

This exactly matches the scenario: _long-running, stable, fixed capacity, performance-sensitive workload_.

Authoritative documentation:  
<https://cloud.google.com/compute/docs/instances/committed-use-discounts-overview>

**Why the other options are not suitable**

**II. Transition the instances to a Managed Instance Group (MIG).**  
MIGs improve **availability, scaling, and lifecycle management** , but they **do not reduce compute pricing** by themselves. Cost savings come from discounts, not grouping.

**III. Convert the instances to preemptible virtual machines.**  
Preemptible (Spot) VMs are **not suitable for business-critical workloads** because they can be terminated at any time. This violates the “without compromising performance” requirement.

**IV. Set up an Unmanaged Instance Group.**  
Unmanaged instance groups offer **no cost benefits** and add operational complexity. They are not a pricing optimization mechanism.

**Final answer:** **I**

---

## Question 8

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

**In managing Terraform templates for your infrastructure, you're joined by two new engineers. How can you establish a process and adopt a tool to prevent code conflicts while ensuring all updates are incorporated into the latest version?**

- [ ] I. Store the code in a Git-based version control system. Implement a process for developers to merge changes daily. Upload code to a versioned Cloud Storage bucket, marking it as the latest master version.
- [x] II. Utilize a Git-based version control system for code storage. Introduce a process involving peer code reviews and unit testing to validate integrity and functionality before code integration. Designate the fully integrated code in the repository as the latest master version.
- [ ] III. Organize code as text files in Google Drive within a defined folder structure. Ensure daily changes are captured in the files and rename the folder structure using a predefined version naming convention.
- [ ] IV. Structure code as text files in Google Drive within a defined folder hierarchy. Confirm daily changes are captured, creating a new .zip archive with a predefined naming convention. Upload the .zip archive to a versioned Cloud Storage bucket, declaring it as the latest version.

### Explanation

**Correct option: II**

**Why option II is correct**

**II. Utilize a Git-based version control system for code storage. Introduce a process involving peer code reviews and unit testing to validate integrity and functionality before code integration. Designate the fully integrated code in the repository as the latest master version.**

This option reflects **industry-standard Terraform and SRE practices** for collaborative Infrastructure as Code (IaC) development.

Core fundamentals behind this choice:

  * **Git as the source of truth:** Git is explicitly recommended for Terraform to manage concurrent changes, maintain history, and resolve conflicts through merges.

  * **Conflict prevention through workflow, not timing:** Peer reviews and pull requests prevent conflicting or unsafe changes from being merged, instead of relying on manual coordination (such as “daily merges”).

  * **Quality gates before merge:** Code reviews and automated tests (e.g., `terraform validate`, `terraform plan`) ensure correctness and prevent broken infrastructure changes from reaching main/master.

  * **Clear latest state:** The main/master branch represents the **current desired state of infrastructure** , aligning perfectly with declarative IaC principles.

This approach scales cleanly as more engineers join and is the **exam-expected, production-grade solution**.

**Authoritative documentation:**  
<https://developer.hashicorp.com/terraform/tutorials/teamwork/teamwork-remote>

**Why the other options are not suitable**

**I. Daily merges + Cloud Storage as master copy**  
Daily merging does not prevent conflicts and Cloud Storage is not a version control system. This introduces race conditions and lacks review, rollback, and auditability.

**III. Google Drive with renamed folders**  
Google Drive offers no native merge conflict resolution, code review, or change history suitable for IaC. This is unsafe for infrastructure management.

**IV. Zipped versions uploaded to Cloud Storage**  
Archiving code removes real-time collaboration, prevents incremental review, and makes conflict resolution nearly impossible.

**Final answer:** **II**

---

## Question 9

*Domain 2: Building and Implementing CI/CD Pipelines*

**In managing your CI/CD pipeline for building and deploying application artifacts, ensuring secure access to secrets and simplifying their rotation in the event of a security breach is paramount. What action should you take to address this concern?**

- [ ] I. Require developers to input secrets during the build process and emphasize avoiding storage of secrets at rest.
- [ ] II. Store secrets in a distinct configuration file within Git, granting specific developers access to this file.
- [x] III. Securely store secrets in Cloud Storage encrypted with a key from Cloud KMS, providing the CI/CD pipeline access via IAM.
- [ ] IV. Encrypt the secrets and store them within the source code repository, while safeguarding the decryption key in a separate repository accessible to the pipeline.

### Explanation

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

---

## Question 10

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

**You support an application that stores product information in cached memory. For every cache miss, an entry is logged in Cloud Logging.**

**You want to visualize how often a cache miss happens over time.**

**What should you do?**

- [ ] **A.** **Link Cloud Logging** as a source in **Looker Studio (formerly Data Studio)**. **Filter the logs on cache misses**.
- [ ] **B.** **Configure Cloud Profiler** to identify and visualize when the **cache misses occur** based on the logs.
- [x] **C.** **Create a logs-based metric in Cloud Logging** and a **dashboard for that metric in Cloud Monitoring**.
- [ ] **D.** **Configure BigQuery as a sink** for **Cloud Logging**. **Create a scheduled query** to filter the **cache miss logs** and write them to a **separate table**.

### Explanation

**Correct Answer:**

**C.** **Create a logs-based metric in Cloud Logging** and a **dashboard for that metric in Cloud Monitoring**.

**Explanation:**

  * **Cloud Logging allows you to create logs-based metrics** , which can track specific log patterns such as **cache misses**.

  * **Cloud Monitoring can visualize these metrics in real-time** via a **custom dashboard** , providing insights into **cache performance over time**.

  * This approach **requires minimal configuration** and is the **most efficient solution** for tracking cache misses.

**Steps to Implement:**

  1. **Create a logs-based metric** in **Cloud Logging** that **counts occurrences of cache miss logs**.

  2. **View the logs-based metric in Cloud Monitoring**.

  3. **Create a dashboard** in Cloud Monitoring to **visualize cache misses over time**.

**Why Other Options Are Incorrect:**

**A. Linking Cloud Logging to Looker Studio and filtering logs** – **Looker Studio is not optimized for real-time log-based monitoring**. **Logs-based metrics in Cloud Monitoring are more efficient** for tracking cache misses.

**B. Using Cloud Profiler** – **Cloud Profiler is for analyzing CPU and memory performance** , **not tracking log-based events like cache misses**.

**D. Exporting logs to BigQuery and creating scheduled queries** – While **BigQuery is useful for deeper historical analysis** , it **introduces unnecessary complexity** for simple **real-time monitoring**.

**Reference Documentation:**

[ Using Logs-Based Metrics in Cloud Monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/logs-based-metrics)

---

## Question 11

*Domain 3: Applying Site Reliability Engineering Practices*

**In line with Site Reliability Engineering principles, you're drafting a postmortem for an incident triggered by a software change that significantly impacted users. How can you prevent similar severe incidents in the future?**

- [ ] I. Hold the engineers involved accountable and escalate the issue to their senior management.
- [x] II. Ensure that test cases detecting errors of this nature are successfully executed before every new software release.
- [ ] III. Conduct follow-up discussions with personnel responsible for reviewing the changes, prescribing best practices for future implementations.
- [ ] IV. Implement a policy mandating immediate engagement of on-call teams to convene engineers and management for prompt incident resolution planning.

### Explanation

**Best Option:**

**II. Ensure that test cases detecting errors of this nature are successfully executed before every new software release.** This approach directly targets the root cause and promotes proactive issue prevention.

**Reasoning:**

**Preventing Recurrence:** By focusing on testing, you establish a robust barrier to prevent similar errors from reaching production and impacting users.

**SRE Alignment:** Thorough testing is a core element of SRE, emphasizing a proactive approach to reliability.

**Tangible Improvement:** This action item leads to concrete changes in your development and release processes.

**Why Others Are Less Optimal:**

**I. Hold the engineers involved accountable ...** While understanding the causes is important, focusing solely on accountability fosters a blame culture, which is counterproductive for long-term improvement and contradicts SRE principles.

**III. Conduct follow-up discussions ...** Postmortem discussions are vital for learning from the incident, but they are not a direct preventive measure against future similar failures.

**IV. Implement a policy mandating immediate engagement ...** While incident response speed is crucial, the policy doesn't address the root cause of the issue, making it less effective in preventing similar incidents.

**Important Considerations**

While improving test coverage is a top priority, consider these additional SRE-aligned actions:

**Blameless Culture:** Promote a culture where errors are seen as opportunities for learning and improvement. This encourages open communication and problem-solving rather than fear.

**Code Review:** Strengthen code review processes to enhance the identification of potential issues before deployment.

**Chaos Engineering:** Experiment with deliberate disruptions in testing or staging environments to uncover hidden vulnerabilities and build resilience.

---

## Question 12

*Domain 3: Applying Site Reliability Engineering Practices*

**Your team has recently deployed an NGINX-based application into Google Kubernetes Engine (GKE) and has exposed it to the public via an HTTP Google Cloud Load Balancer (GCLB) ingress.**

**You want to scale the deployment of the application's frontend using an appropriate Service Level Indicator (SLI).**

**What should you do?**

- [ ] **A.** Configure the **horizontal pod autoscaler** to use the **average response time** from the **Liveness and Readiness probes**.
- [ ] **B.** Configure the **vertical pod autoscaler in GKE** and enable the **cluster autoscaler** to scale the cluster as pods expand.
- [x] **C.** **Install the Cloud Monitoring (formerly Stackdriver) custom metrics adapter** and configure a **horizontal pod autoscaler (HPA) to use the number of requests** provided by the **Google Cloud Load Balancer (GCLB)**.
- [ ] **D.** Expose the **NGINX stats endpoint** and configure the **horizontal pod autoscaler** to use the **request metrics** exposed by the **NGINX deployment**.

### Explanation

**Correct Answer:**

**C.** **Install the Cloud Monitoring (formerly Stackdriver) custom metrics adapter** and configure a **horizontal pod autoscaler (HPA) to use the number of requests** provided by the **Google Cloud Load Balancer (GCLB)**.

**Explanation:**

  * **Horizontal Pod Autoscaler (HPA) is the best approach for scaling stateless applications** like **NGINX-based frontends** based on real traffic metrics.

  * **Google Cloud Load Balancer (GCLB) provides HTTP request count metrics** , which are **more relevant SLIs** for scaling than CPU/memory alone.

  * The **Cloud Monitoring custom metrics adapter** enables **HPA to use external HTTP request rate metrics** from GCLB, ensuring **demand-based autoscaling**.

**Why Other Options Are Incorrect:**

**A. Using Liveness and Readiness probe response times for HPA** –

  * Liveness and readiness probes are **used for health checks** , not for **measuring real traffic load**.

  * Response time **does not accurately represent the need for scaling**.

**B. Using Vertical Pod Autoscaler (VPA) and Cluster Autoscaler** –

  * **VPA optimizes individual pod resource allocation** , **not the number of replicas**.

  * **Cluster Autoscaler only adjusts node counts** , which is **not sufficient** for handling increasing request loads dynamically.

**D. Using the NGINX stats endpoint for autoscaling** –

  * While **NGINX exposes request metrics** , these **are not natively integrated with Cloud Monitoring or HPA**.

  * **GCLB already provides request count metrics** in **Cloud Monitoring** , making it **a better choice**.

**Recommended Approach:**

  1. **Install the Cloud Monitoring custom metrics adapter for Kubernetes**  
[ Cloud Monitoring Custom Metrics Adapter](https://cloud.google.com/monitoring/custom-metrics/creating-metrics)

  2. **Use GCLB's HTTP request metrics for autoscaling**  
[ Autoscaling with External HTTP Request Metrics](https://cloud.google.com/kubernetes-engine/docs/concepts/custom-and-external-metrics)

  3. **Configure the HPA to use request count per second from GCLB**  
[ Scaling Workloads with HPA](https://cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling)

---

## Question 13

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

**You are managing an application that exposes an HTTP endpoint without using a load balancer. The latency of HTTP responses is important for the user experience.**

**You want to understand what HTTP latencies all of your users are experiencing. You use Cloud Monitoring.**

**What should you do?**

- [ ] **A. In your application, create a custom metric with metricKind set to DELTA and valueType set to DOUBLE.**
    **In Cloud Monitoring's Metrics Explorer, use a Stacked Bar graph to visualize the metric.**
- [ ] **B. In your application, create a custom metric with metricKind set to CUMULATIVE and valueType set to DOUBLE.**
    **In Cloud Monitoring's Metrics Explorer, use a Line graph to visualize the metric.**
- [x] **C. In your application, create a custom metric with metricKind set to GAUGE and valueType set to DISTRIBUTION.**
    **In Cloud Monitoring's Metrics Explorer, use a Heatmap graph to visualize the metric.**
- [ ] **D. In your application, create a custom metric with metricKind set to METRIC_KIND_UNSPECIFIED and valueType set to INT64.**
    **In Cloud Monitoring's Metrics Explorer, use a Stacked Area graph to visualize the metric.**

### Explanation

**Correct Answer:**

**C.**

  * In your application, create a **custom metric** with `metricKind` set to `GAUGE` and `valueType` set to `DISTRIBUTION`.

  * In **Cloud Monitoring's Metrics Explorer** , use a **Heatmap graph** to visualize the metric.

**Explanation:**

  * **HTTP response latency varies over time** and across requests.

  * The **best way to track user latency experience** is to **capture individual latency values** and store them in a **custom distribution metric**.

  * The `**GAUGE**`**metricKind** is appropriate because **latency represents a real-time value** at a given point in time.

  * The `**DISTRIBUTION**`**valueType** allows **storing multiple latency measurements** , making it easier to analyze **percentiles and trends**.

  * A **Heatmap graph** helps **visualize latency patterns over time** and **identify spikes or trends** in user experience.

**Why Other Options Are Incorrect:**

**A. Using a**`**DELTA**`**metricKind and**`**DOUBLE**`**valueType with a Stacked Bar Graph** –

  * `DELTA` is used for **rate-based metrics over time** , but **latency should be measured as a point-in-time value (GAUGE)**.

  * **Stacked Bar graphs are not ideal for latency distributions**.

**B. Using a**`**CUMULATIVE**`**metricKind and**`**DOUBLE**`**valueType with a Line Graph** –

  * `CUMULATIVE` metrics track values **increasing over time** (e.g., total number of requests).

  * **Latency is not cumulative** , so this **does not provide accurate insights**.

**D. Using**`**METRIC_KIND_UNSPECIFIED**`**and**`**INT64**`**with a Stacked Area Graph** –

  * `METRIC_KIND_UNSPECIFIED` is **not a valid selection** for Cloud Monitoring.

  * `INT64` is **not appropriate for capturing floating-point latency values**.

**Reference Documentation:**

[ Creating Custom Metrics in Cloud Monitoring](https://cloud.google.com/monitoring/custom-metrics/creating-metrics)  
[ Using Heatmaps for Distribution Metrics](https://cloud.google.com/monitoring/charts/charting-distribution-metrics#:~:text=Heatmap%20charts%20are%20designed%20to,color%20indicates%20a%20higher%20value.)

---

## Question 14

*Domain 2: Building and Implementing CI/CD Pipelines*

**Your organization recently shifted to a container-based workflow for application development. Within this setup, your team continuously deploys multiple applications via an automated build pipeline to the production environment. However, a recent security audit flagged concerns about potential vulnerabilities in the code deployed to production. The conventional tooling for virtual machine (VM) vulnerabilities is inadequate for the containerized environment. How can you ensure the security and patch level of all code processed through the pipeline?**

- [x] I. Implement Container Analysis to scan and report Common Vulnerabilities and Exposures (CVEs).
- [ ] II. Configure the containers within the build pipeline to autonomously update themselves before release.
- [ ] III. Adapt existing operating system vulnerability software to function within the containerized environment.
- [ ] IV. Integrate static code analysis tooling to scrutinize the Docker files utilized in creating the containers.

### Explanation

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

---

## Question 15

*Domain 3: Applying Site Reliability Engineering Practices*

**You support a web application hosted on Compute Engine that provides a booking service for thousands of users.**

**Shortly after the release of a new feature, your monitoring dashboard shows that all users are experiencing latency at login.**

**You want to mitigate the impact of the incident on the users of your service.**

**What should you do first?**

- [x] **A. Roll back the recent release.**
- [ ] **B. Review Cloud Monitoring.**
- [ ] **C. Upsize the virtual machines running the login services.**
- [ ] **D. Deploy a new release to see whether it fixes the problem.**

### Explanation

**Correct Answer:**

**A. Roll back the recent release.**

**Explanation:**

  * The **latency issue started immediately after the new release** , indicating that the **new deployment is likely the root cause**.

  * The **fastest and safest way to mitigate impact** is to **roll back to the previous stable version** while investigating the issue.

  * This follows **Site Reliability Engineering (SRE) best practices** , where a rollback is the **primary mitigation strategy** for post-release incidents.

**Why Other Options Are Incorrect:**

**B. Reviewing Cloud Monitoring logs before rolling back** –

  * While **Cloud Monitoring helps diagnose the issue** , **it does not mitigate user impact immediately**.

  * **Rollback first** to reduce user disruption, then analyze the cause.

**C. Upsizing VMs running the login service** –

  * **Scaling resources does not fix application-level issues**.

  * If the new release introduced **inefficient code or database locks** , **increasing VM size won't resolve the root cause**.

**D. Deploying another release without investigation** –

  * **This is risky** because it might **worsen the issue** or introduce new bugs.

  * **Rollback first** , verify the issue is resolved, then debug and prepare a **proper fix** for a future deployment.

**Recommended Approach:**

  1. **Rollback to the last stable release immediately** to restore service availability.

  2. **Investigate logs in Cloud Logging & Monitoring** to find the root cause.

  3. **Run a post-mortem** to ensure the issue is resolved before the next deployment.

  4. **Test the fix in a staging environment** before rolling out again.

**Reference Documentation:**

[ Google SRE Handbook: Managing Incidents](https://sre.google/resources/practices-and-processes/anatomy-of-an-incident/)  
[ Rolling Back Deployments on Compute Engine](https://cloud.google.com/deploy/docs/roll-back)

---

## Question 16

*Domain 2: Building and Implementing CI/CD Pipelines*

**You're responsible for deploying application releases to Google Cloud Platform (GCP) using Jenkins to streamline processes, reduce overhead, and ensure data security. What's the best course of action?**

- [ ] I. Deploy Jenkins on local workstations.
- [ ] II. Implement Jenkins on an on-premises Kubernetes cluster.
- [ ] III. Utilize Jenkins within Google Cloud Functions.
- [x] IV. Set up Jenkins on Compute Engine virtual machines.

### Explanation

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

---

## Question 17

*Domain 3: Applying Site Reliability Engineering Practices*

**You provide support for a large service with a clearly defined Service Level Objective (SLO). The development team frequently deploys new releases of the service each week. In the event of a significant incident causing the service to miss its SLO, you aim for the development team to pivot their focus from feature development to enhancing service reliability. What action should you take proactively before a major incident arises?**

- [x] I. Collaborate with all service stakeholders to formulate an appropriate error budget policy.
- [ ] II. Advocate for prioritizing service reliability over introducing new features in discussions with the product team.
- [ ] III. Discuss with the development team to potentially reduce the frequency of releases to once a week or less.
- [ ] IV. Implement a plugin within your Jenkins pipeline to halt new releases when the service is out of compliance with its SLO.

### Explanation

**I. Collaborate with all service stakeholders to formulate an appropriate error budget policy.**

Let's break down why this is the most effective starting point:

  * **Shared Responsibility:** An error budget policy creates a framework for making decisions around reliability vs. feature development. It aligns stakeholders (development, product, operations) on priorities.

  * **Proactive:** Establishes a clear mechanism for when to shift focus _before_ a major incident disrupts the service.

  * **Data-Driven:** Error budgets are based on your SLO. They translate a reliability goal into tangible terms that everyone can understand.

**Why Other Options Are Less Ideal (Initially):**

  * **II. Advocate for prioritizing service reliability ...** While important, a general prioritization doesn't provide the same specific guidance or shared understanding as an error budget policy.

  * **III. Discuss with the development team ...** Slowing down releases might be a consequence of an error budget policy, but it's a blunt instrument and could hinder necessary fixes or improvements.

  * **IV. Implement a plugin within your Jenkins pipeline ...** Halting releases automatically can be a tool to enforce an error budget policy, but the policy itself needs to be defined first.

**Important Considerations**

  * **Communication:** An error budget policy is only effective if well-communicated and agreed upon across the organization.

  * **Review and Adjust:** The error budget should be reviewed periodically and adjusted based on changing business needs and service performance.

**Reference:**

<https://sre.google/workbook/error-budget-policy/>

---

## Question 18

*Domain 5: Optimizing Performance and Cost*

You manage **several production systems** that run on **Compute Engine** in the same **Google Cloud Platform (GCP) project**.

Each system has its **own set of dedicated Compute Engine instances**.

You want to know **how much it costs to run each system**.

What should you do?

- [ ] **A.** In the **Google Cloud Console** , use the **Cost Breakdown section** to visualize the **costs per system**.
- [x] **B.** **Assign all instances a label specific to the system they run**. Configure **BigQuery billing export** and query **costs per label**.
- [ ] **C.** **Enrich all instances with metadata** specific to the system they run. Configure **Cloud Logging (formerly Stackdriver Logging) to export to BigQuery** , and query **costs based on the metadata**.
- [ ] **D.** **Name each virtual machine (VM) after the system it runs**. Set up a **usage report export** to a **Cloud Storage bucket**. Configure the bucket as a source in **BigQuery** to **query costs based on VM name**.

### Explanation

**Correct Answer:**

**B.** **Assign all instances a label specific to the system they run**. Configure **BigQuery billing export** and **query costs per label**.

**Explanation:**

  * **Google Cloud billing supports resource labels** that allow you to **track costs based on specific attributes** like **which system a VM belongs to**.

  * **BigQuery billing export** provides **detailed billing data** , which can be queried **by labels to determine per-system costs**.

  * This approach **follows Google Cloud best practices for cost allocation** and allows for **granular cost analysis**.

**Steps to Implement:**

  1. **Assign labels to Compute Engine instances** for each system:
        
                    1. bash
            2. CopyEditgcloud compute instances add-labels instance-name --labels=system=my-system

  2. **Enable BigQuery billing export** to **store billing data**.

  3. **Query costs per system using BigQuery** :
        
                    1. sql
            2. CopyEditSELECT service.description, labels.system, SUM(cost) AS total_cost
            3. FROM `billing_dataset.gcp_billing_export`
            4. WHERE usage_start_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
            5. GROUP BY service.description, labels.system
            6. ORDER BY total_cost DESC;

**Why Other Options Are Incorrect:**

**A. Using the Cost Breakdown section in Google Cloud Console** –

  * **The Cost Breakdown section does not provide detailed per-system costs**.

  * **It is not as granular as querying BigQuery exports with labels**.

**C. Exporting logs to BigQuery and querying based on metadata** –

  * **Cloud Logging does not track cost-related data**.

  * **Billing data is stored in Cloud Billing, not Cloud Logging** , so this approach **won't provide accurate cost breakdowns**.

**D. Naming VMs after the system and using usage report exports** –

  * **VM names are not included in detailed billing exports**.

  * **Labels are the recommended approach for cost allocation**.

**Reference Documentation:**

[ Using Labels for Cost Allocation](https://cloud.google.com/blog/topics/cost-management/use-labels-to-gain-visibility-into-gcp-resource-usage-and-spending)  
[ Exporting Cloud Billing Data to BigQuery](https://cloud.google.com/billing/docs/how-to/export-data-bigquery)

---

## Question 19

*Domain 2: Building and Implementing CI/CD Pipelines*

**You're set to deploy a new feature of a web-based application to production and wish to utilize Google Kubernetes Engine (GKE) for a phased rollout to half of the web server pods. What is the optimal course of action?**

- [x] I. Employ a partitioned rolling update method.
- [ ] II. Implement Node taints with NoExecute.
- [ ] III. Utilize a replica set within the deployment specification.
- [ ] IV. Opt for a stateful set with parallel pod management policy.

### Explanation

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

---

## Question 20

*Domain 3: Applying Site Reliability Engineering Practices*

**As you craft and allocate action items in a postmortem following an outage, your goal is to efficiently address the root causes. Although the outage has concluded, it's vital to swiftly tackle the action items. How should you designate owners and collaborators for these action items?**

- [x] I. Assign a single owner for each action item, along with any necessary collaborators.
- [ ] II. Allocate multiple owners for each item to expedite the team's response.
- [ ] III. Assign collaborators to the items without designating individual owners to maintain a blameless postmortem approach.
- [ ] IV. Designate the team lead as the owner for all action items, given their oversight of the SRE team.

### Explanation

**I. Assign a single owner for each action item, along with any necessary collaborators.**

**Justification:**

  * **Clarity & Accountability:** A single owner ensures there's no confusion about who is ultimately responsible for driving the action item to completion.

  * **Collaboration:** Collaborators provide support, expertise, and diverse perspectives while maintaining accountability with the designated owner.

  * **Urgency:** Given the need for swift action, having clear ownership fosters a sense of responsibility and helps prioritize tasks.

**Why Other Options Are Less Suitable:**

  * **II. Allocate multiple owners for each item...** While well-intentioned, multiple owners can lead to diffusion of responsibility and potential delays if it's unclear who's driving the resolution.

  * **III. Assign collaborators to the items without designating individual owners...** Collaboration is vital, but without clear ownership, tasks risk falling through the cracks or lacking the necessary drive for quick resolution.

  * **IV. Designate the team lead as the owner for all action items...** This places too much burden on the team lead and may not leverage the specific expertise of other team members who are better suited to own individual action items.

**References:**  
<https://sre.google/sre-book/example-postmortem/>

<https://devops.com/when-it-disaster-strikes-part-3-conducting-a-blameless-post-mortem/>

---

## Question 21

*Domain 2: Building and Implementing CI/CD Pipelines*

**During the migration of an on-premises containerized web application to Google Cloud, considering specific traffic direction and testing needs, which deployment strategy and platform should you opt for?**

- [ ] I. Implement the canary release on Cloud Run, employing traffic splitting to route 10% of user traffic to the canary release based on the revision tag.
- [ ] II. Choose App Engine for deploying the canary release, utilizing traffic splitting to direct a subset of user traffic to the new version based on IP address.
- [ ] III. Deploy the canary release on Compute Engine, utilizing Anthos Service Mesh with Compute Engine to direct 10% of user traffic to the canary release via virtual service configuration.
- [x] IV. Opt for Google Kubernetes Engine with Anthos Service Mesh for deploying the canary release, employing traffic splitting to direct 10% of user traffic to the new version based on the user-agent header configured in the virtual service.

### Explanation

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

---

## Question 22

*Domain 5: Optimizing Performance and Cost*

**When configuring the frontend tier of an application deployed in Google Cloud, which serves only users from the United Kingdom within the europe-west2 region, utilizing nginx and a managed instance group with an Envoy-based external HTTP(S) load balancer, what network tier and load balancing setup offer the most cost-effective solution?**

- [ ] I. Premium Tier with a global load balancer
- [ ] II. Premium Tier with a regional load balancer
- [ ] III. Standard Tier with a global load balancer
- [x] IV. Standard Tier with a regional load balancer

### Explanation

**Correct option: IV**

**Why option IV is correct**

**IV. Standard Tier with a regional load balancer**

Your users are **only in the UK** and the application is served from **a single region (europe-west2)**. In this case, the most cost-effective design is to use a **regional external Application Load Balancer** (Envoy-based external HTTP(S) load balancer) with the **Standard Network Service Tier** :

  * In **Standard Tier** , the external Application Load Balancer is intended for **single-region** delivery (it distributes traffic to backends in a single region).

  * Google’s pricing guidance explicitly calls out the **regional external Application Load Balancer** as a cost-effective option for single-region workloads because it uses **Standard Tier** , which has lower outbound data transfer charges.

  * Since you are not serving global users, paying for global premium backbone/edge features is unnecessary for the requirement.

**Documentation:** <https://cloud.google.com/network-tiers/docs/overview>

**Why the other options are not suitable**

**I. Premium Tier with a global load balancer**  
Premium Tier is optimized for global users and multi-region/backbone performance. For a UK-only, single-region serving model, it is typically **more expensive than needed**.

**II. Premium Tier with a regional load balancer**  
Even though regional is correct for the geography constraint, choosing **Premium** defeats the cost goal when **Standard Tier regional** is available and intended for single-region delivery.

**III. Standard Tier with a global load balancer**  
For Envoy-based external HTTP(S) / external Application Load Balancing, **Standard Tier effectively operates in a single region** (not true global multi-region Anycast behavior). If you want global external Application Load Balancing behavior, it requires Premium Tier.

**Final answer: IV**

---

## Question 23

*Domain 3: Applying Site Reliability Engineering Practices*

**As a member of a global organization managing a service with a 99% availability target and limited engineering resources, you've noted a 99.5% availability for the current month. To meet the set availability objectives, adapt to business changes, including forthcoming feature launches, and diminish technical debt while minimizing operational expenses, which Google-endorsed approach should take precedence?**

- [ ] I. Bolster service resilience by implementing N+1 redundancy through the incorporation of extra computing resources.
- [x] II. Streamline operations by identifying, quantifying, and automating repetitive tasks to eradicate unnecessary manual effort.
- [ ] III. Establish an error budget for service-level availability and actively work to reduce any remaining errors.
- [ ] IV. Assign available engineers to feature backlog development, ensuring adherence to the availability target.

### Explanation

**The Priority:**

**II. Streamline operations by identifying, quantifying, and automating repetitive tasks to eradicate unnecessary manual effort.**

**Why this takes precedence:**

  * **Efficiency Optimization:** Google's Site Reliability Engineering (SRE) philosophy prioritizes efficient use of available resources. Automating manual processes reduces the potential for human error and frees up engineers for higher-value tasks.

  * **Addressing Root Issues:** Manual operations are a common source of delays and errors. Automation tackles these problems at their core, leading to inherent reliability improvements.

  * **Resource Maximization:** Reducing manual work allows your limited engineers to focus on proactive improvements, new features, and reducing technical debt, all leading to a better service.

  * **Cost-effectiveness:** Operational streamlining through automation often leads to significant cost savings.

**Why Others are Less Ideal:**

  * **I. Bolster service resilience by implementing N+1 redundancy...** Redundancy is valuable but can be expensive. It doesn't address existing operational inefficiencies, which could still lead to outages.

  * **III. Establish an error budget...** Error budgets are an important SRE tool, but a sole focus on reduction might discourage necessary development work and innovation.

  * **IV. Assign available engineers to feature backlog development...** Features are important, but a service that fails to meet its availability targets due to operational problems won't be useful, regardless of feature additions.

---

## Question 24

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

**To ensure consistency across your Google Kubernetes Engine (GKE) environments - development, staging, and production - while following Google-recommended practices for enforcing network policies and deploying a logging DaemonSet, what steps should you take?**

- [ ] I. Employ Google Cloud Deploy to enforce network policies and deploy the DaemonSet. Utilize Cloud Monitoring to trigger alerts for any deviations from the repository source.
- [ ] II. Use Google Cloud Deploy for the DaemonSet deployment and Policy Controller to configure network policies. Leverage Cloud Monitoring to identify drifts and Cloud Functions to rectify them.
- [x] III. Utilize Cloud Build to generate and deploy network policies and the DaemonSet. Implement Config Sync to synchronize configurations across all three environments.
- [ ] IV. Utilize Cloud Build to generate and deploy network policies and the DaemonSet. Set up a Policy Controller to enforce configurations across the three environments.

### Explanation

**Correct option: III**

**Why option III is correct**

**III. Utilize Cloud Build to generate and deploy network policies and the DaemonSet. Implement Config Sync to synchronize configurations across all three environments.**

This option most closely follows **Google-recommended GitOps practices for GKE** when the goal is **consistency across dev, staging, and prod**.

Key fundamentals behind this choice:

  * **Config Sync (Anthos Config Management)** is Google’s **authoritative solution** for enforcing configuration consistency across multiple GKE clusters and environments. It continuously reconciles the desired state stored in Git with the actual cluster state.

  * **Network policies and DaemonSets** are classic cluster-level configurations that should be enforced declaratively and continuously, not deployed ad hoc.

  * **Cloud Build** integrates naturally with Git-based workflows to validate and promote configuration changes before they reach the repository that Config Sync watches.

  * This approach **prevents configuration drift automatically** , rather than merely detecting it after the fact.

This is the canonical pattern Google documents for:

  * GitOps-driven configuration management

  * Multi-environment consistency

  * Policy and system workload enforcement in GKE

**Authoritative documentation:**  
<https://cloud.google.com/anthos-config-management/docs/concepts/config-sync-overview>

**Why the other options are not suitable**

**I. Google Cloud Deploy + Cloud Monitoring alerts**  
Cloud Deploy is for **application delivery** , not enforcing cluster-level configurations like network policies or DaemonSets. Monitoring detects drift but does **not prevent or correct it**.

**II. Cloud Deploy + Policy Controller + Cloud Functions**  
This combines tools with overlapping responsibilities and introduces unnecessary operational complexity. Drift remediation via Cloud Functions is not Google’s recommended approach.

**IV. Cloud Build + Policy Controller only**  
Policy Controller enforces **policy constraints** , not the **deployment and synchronization** of resources like DaemonSets. It cannot replace Config Sync for full configuration consistency.

**Final answer:** **III**

---

## Question 25

*Domain 2: Building and Implementing CI/CD Pipelines*

**To facilitate trunk-based development in a central Git repository, how can you establish a robust CI/CD pipeline for a containerized application in Google Cloud, ensuring thorough testing for new versions to enhance its quality**

- [ ] I. Enforce a Git hook to mandate developers execute unit tests before pushing code to the central repository. Subsequently, initiate Cloud Build to construct the application container. Upon completion, deploy the container to a testing environment and execute integration tests. If successful, proceed to deploy the application container to the production environment, followed by the execution of acceptance tests.
- [ ] II. Implement a Git hook to enforce developers execute unit tests before pushing code to the central repository. Upon successful unit tests, trigger Cloud Build to build a container. Subsequently, deploy the application container to a testing environment, execute integration tests, and acceptance tests. If all tests pass, designate the code as production-ready and deploy the application container to the production environment.
- [ ] III. Initiate Cloud Build to build the application container and conduct unit tests within the container. Upon successful completion, deploy the application container to a testing environment and execute integration tests. Following successful integration tests, deploy the application container to the production environment, and execute acceptance tests.
- [x] IV. Trigger Cloud Build to execute unit tests upon code push. If all unit tests pass, proceed to build and push the application container to a central registry. Subsequently, deploy the container to a testing environment, execute integration tests, and acceptance tests. Upon passing all tests, deploy the application to the production environment, and conduct smoke tests.

### Explanation

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

---

## Question 26

*Domain 2: Building and Implementing CI/CD Pipelines*

**In your organization's multi-cloud setup, you're tasked with setting up a CI/CD pipeline for an application deployed using custom Compute Engine images across various cloud platforms. The solution should enable seamless building and deployment of images in the current environment while remaining adaptable to future changes. Which solution stack should you choose?**

- [x] I. Opt for Cloud Build integrated with Packer.
- [ ] II. Choose Cloud Build combined with Google Cloud Deploy.
- [ ] III. Implement Google Kubernetes Engine alongside Google Cloud Deploy.
- [ ] IV. Utilize Cloud Build integrated with kpt (Kubernetes Package Manager).

### Explanation

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

---

## Question 27

*Domain 5: Optimizing Performance and Cost*

**To optimize costs, you've deployed a serverless application on Cloud Run in your production environment. How can you effectively identify the application's resource utilization?**

- [ ] I. Utilize Cloud Trace with distributed tracing to monitor the application's resource utilization.
- [ ] II. Use Cloud Profiler with Ops Agent to track the CPU and memory utilization of the application.
- [x] III. Monitor the container CPU and memory utilization of the application using Cloud Monitoring.
- [ ] IV. Employ Cloud Ops to establish logs-based metrics for monitoring the resource utilization of the application.

### Explanation

**III. Monitor the container CPU and memory utilization of the application using Cloud Monitoring.**

Here's why this is the most direct and effective approach:

  * **Container-Level Metrics:** Cloud Run resources are allocated at the container level, making container-specific metrics essential for understanding utilization.

  * **Cloud Monitoring Integration:** Cloud Monitoring provides built-in metrics for tracking CPU, memory, and other resources for Cloud Run instances.

  * **Optimization Focus:** Monitoring container resource usage directly helps you make informed decisions about right-sizing your Cloud Run instances to reduce costs.

**Why Others Are Less Ideal:**

  * **I. Utilize Cloud Trace with distributed tracing...** Cloud Trace is primarily for investigating latency and performance issues in distributed systems, less so for granular resource monitoring.

  * **II. Use Cloud Profiler with Ops Agent...** Cloud Profiler is designed for code-level profiling, which might be less relevant than container-level resource tracking in a pure serverless context.

  * **IV. Employ Cloud Ops to establish logs-based metrics...** While logs hold valuable information, extracting detailed resource metrics from them can be complex compared to using Cloud Monitoring's pre-built metrics.

**Reference:**

<https://cloud.google.com/run/docs/monitoring?hl=ja>

---

## Question 28

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

**Your web application, deployed on a Compute Engine managed instance group with Ops Agent installed on all instances, has detected suspicious activity from a specific IP address. To monitor the number of requests from that IP address with minimal operational complexity, what's the most effective approach?**

- [x] I. Set up the Ops Agent with a logging receiver and establish a logs-based metric.
- [ ] II. Develop a script to extract IP address request metrics from the web server log and transmit them to the Cloud Monitoring API.
- [ ] III. Enhance the application to directly transmit IP address request metrics to the Cloud Monitoring API.
- [ ] IV. Configure the Ops Agent with a metrics receiver.

### Explanation

**The Best Approach:**

**I. Set up the Ops Agent with a logging receiver and establish a logs-based metric.**

**Reasons:**

  * **Low Operational Overhead:** The Ops Agent you already have installed can easily collect web server logs.

  * **Logs-Based Metrics:** Creating a logs-based metric in Cloud Monitoring allows you to track requests from the suspicious IP without modifying your application.

  * **Flexibility:** You can filter, aggregate, and analyze this metric alongside other Ops Agent data.

**Why Other Options Are Less Ideal:**

  * **II. Develop a script to extract IP address request metrics...** This adds development & maintenance overhead, especially if your web server log format is complex.

  * **III. Enhance the application to directly transmit IP address request metrics...** Modifying production code for monitoring purposes introduces risks and complexity.

  * **IV. Configure the Ops Agent with a metrics receiver.** While the Ops Agent can collect custom metrics, this likely requires more configuration and potentially custom code than a logs-based solution.

**Reference:**

<https://cloud.google.com/monitoring/agent/ops-agent/configuration>

---

## Question 29

*Domain 2: Building and Implementing CI/CD Pipelines*

**While setting up the CI/CD pipeline for an application deployed on Google Kubernetes Engine (GKE) utilizing Kubernetes Deployment, Service, and Ingress, the application team desires deployment using the blue/green methodology. What are the appropriate rollback actions to implement?**

- [ ] I. Perform a rollback using the kubectl rollout undo command.
- [ ] II. Delete the new container image and subsequently terminate the running Pods.
- [x] III. Update the Kubernetes Service to revert to the previous Kubernetes Deployment.
- [ ] IV. Scale down the new Kubernetes Deployment to zero.

### Explanation

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

---

## Question 30

*Domain 2: Building and Implementing CI/CD Pipelines*

**In developing an application on Cloud Run requiring access to a third-party API via an API key, adherence to Google-recommended practices for secure storage and usage of the key is paramount. What's the recommended approach?**

- [x] I. Store the API key securely in Secret Manager as a secret, then reference it as an environment variable within the Cloud Run application.
- [ ] II. Save the API key in Secret Manager as a secret key, then mount it under the /sys/api_key directory and decrypt it within the Cloud Run application.
- [ ] III. Secure the API key in Cloud Key Management Service (Cloud KMS) as a key, then reference it as an environment variable within the Cloud Run application.
- [ ] IV. Encrypt the API key using Cloud Key Management Service (Cloud KMS), pass it as an environment variable to Cloud Run, and decrypt it for usage within the applicationX

### Explanation

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

---

## Question 31

*Domain 2: Building and Implementing CI/CD Pipelines*

**In optimizing your deployment pipeline with Google Cloud Deploy to minimize toil and reduce deployment time, what steps should you take? (Choose two.)**

- [x] I. Implement a trigger system to alert the relevant team for manual intervention when necessary during the deployment process.
- [ ] II. Break down automation tasks into smaller, more manageable components to streamline deployment.
- [ ] III. Develop a script to automate the setup of the deployment pipeline within Google Cloud Deploy, reducing manual configuration efforts.
- [ ] IV. Increase the number of engineers to expedite completion of manual steps in the deployment process.
- [x] V. Automate approval procedures for promoting deployments from the development environment to the testing environment.

### Explanation

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

---

## Question 32

*Domain 3: Applying Site Reliability Engineering Practices*

**In preparation for deploying a new service to production, you aim to achieve automatic scalability across multiple regions using a managed instance group. This service requires significant resources per instance, necessitating meticulous capacity planning. What actions should you take?**

- [ ] I. Evaluate Cloud Trace insights to determine the most effective resource sizing strategy for the service.
- [ ] II. Specify the n2-highcpu-96 machine type within the managed instance group configuration to accommodate the service's resource requirements adequately.
- [ ] III. Implement deployment across multiple regions and utilize an internal load balancer to efficiently manage traffic distribution.
- [x] IV. Validate that the resource demands align with the available project quota limits in each region before initiating deployment.

### Explanation

**Correct option: IV**

**Why option IV is correct**

**IV. Validate that the resource demands align with the available project quota limits in each region before initiating deployment.**

When deploying a **multi-region managed instance group (MIG)** for a **resource-intensive service** , the most critical prerequisite is **quota validation**.

Core infrastructure fundamentals behind this choice:

  * **Managed instance groups scale automatically** , but **scaling is hard-blocked by quotas** (vCPU, CPU families, memory, IP addresses, regional limits).

  * For **large machine types** and **multi-region deployments** , quota exhaustion is one of the **most common production blockers** , even when configuration is correct.

  * **Capacity planning in Google Cloud is quota-driven**. If quotas are insufficient in _any_ target region, autoscaling will fail silently or partially, breaking availability guarantees.

  * Google explicitly recommends **verifying and increasing quotas before production rollout** , especially for high-resource workloads.

This step ensures:

  * Predictable autoscaling behavior

  * No partial regional failures

  * No last-minute deployment blockers

**Why the other options are not suitable**

**I. Evaluate Cloud Trace insights for resource sizing.**  
Cloud Trace is for **latency analysis and request tracing** , not for determining instance sizing or capacity planning.

**II. Specify a large machine type (n2-highcpu-96).**  
Selecting a machine type alone does not ensure availability. Without confirming **regional quota capacity** , instances may fail to launch entirely.

**III. Deploy across multiple regions using an internal load balancer.**  
Internal load balancers are **regional** , not global. They cannot distribute traffic across regions and are inappropriate for multi-region production access.

**Final answer:** **IV**

---

## Question 33

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

**Your organization employs Jenkins hosted on Google Cloud VM instances for CI/CD processes. To expand functionality, you want to integrate infrastructure as code automation using Terraform. Ensuring the Terraform module within Jenkins can create Google Cloud resources with proper authorization is essential. How should you proceed to align with Google-recommended practices?**

- [x] I. Ensure the Jenkins VM instance is associated with a service account holding appropriate Identity and Access Management (IAM) permissions.
- [ ] II. Implement the Terraform module to enable Secret Manager for secure credential retrieval.
- [ ] III. Establish a dedicated service account for the Terraform instance. Then, configure the GOOGLE_CREDENTIALS environment variable on the Jenkins server, injecting the secret key value.
- [ ] IV. Integrate the gcloud auth application-default login command into Jenkins as a preliminary step before executing Terraform commands.

### Explanation

**I. Ensure the Jenkins VM instance is associated with a service account holding appropriate Identity and Access Management (IAM) permissions.**

Here's why this is the most secure and easily managed method:

  * **Principle of Least Privilege:** Grant the service account only the specific IAM permissions needed for Terraform to manage resources, minimizing potential security risks.

  * **Workload Identity:** Workload Identity is specifically designed for VM-to-Google Cloud service communication. It doesn't involve long-lived credentials or manual key management.

  * **Operational Ease:** You manage permissions centrally through IAM instead of handling credentials directly within Jenkins jobs.

**Why Other Options Are Less Ideal:**

  * **II. Implement the Terraform module to enable Secret Manager...** Managing secrets with Secret Manager is recommended, but it doesn't directly address how Jenkins obtains authorization to perform actions on GCP.

  * **III. Establish a dedicated service account ...** Creating a service account is necessary, but storing the key as an environment variable introduces risks if the Jenkins server is compromised.

  * **IV. Integrate the gcloud auth application-default login ...** This necessitates manual key rotation and places sensitive credentials on your Jenkins server

---

## Question 34

*Domain 2: Building and Implementing CI/CD Pipelines*

**In alignment with your company's security strategy to shift left on security, the InfoSec team requires all teams to enforce guardrails on Google Kubernetes Engine (GKE) clusters, allowing only the deployment of trusted and approved images. How can you fulfill this requirement effectively?**

- [ ] I. Implement Container Analysis in Artifact Registry to scan container images for common vulnerabilities and exposures (CVEs) during your CI/CD pipeline.
- [x] II. Utilize Binary Authorization to verify and attest images during the CI/CD pipeline, ensuring only approved images are deployed to GKE clusters.
- [ ] III. Establish Identity and Access Management (IAM) policies to establish a least privilege model on GKE clusters, restricting image deployments based on predefined permissions.
- [ ] IV. Deploy Falco or Twistlock on GKE to actively monitor running Pods for vulnerabilities and security issues.

### Explanation

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

---

## Question 35

*Domain 5: Optimizing Performance and Cost*

**In your company's Google Kubernetes Engine (GKE) setup, the development environment's clusters are logging applications with verbosity, accessed by developers via kubectl logs without utilizing Cloud Logging. Additionally, there's no standardized logging structure across applications. To minimize logging-related costs while retaining GKE operational logs, what's the optimal approach?**

- [ ] I. Update the development cluster using the command: gcloud container clusters update --logging=SYSTEM.
- [ ] II. Modify the logging configuration for the development cluster with: gcloud container clusters update --logging=WORKLOAD.
- [ ] III. Disable the default logging sink within the project associated with the development environment using: gcloud logging sinks update _Default --disabled.
- [x] IV. Implement an exclusion filter on the default logging sink within the project tied to the development environment with: severity >= DEBUG resource.type = "k8s_container".

### Explanation

**Correct Option:**

**IV. Implement an exclusion filter on the default logging sink within the project tied to the development environment with: severity >= DEBUG resource.type = "k8s_container".**

**Justification:**

  * **Targeted Filtering:** Directly addresses the verbose application logs by filtering out DEBUG and lower severity log entries from Kubernetes containers, significantly reducing log volume.

  * **Retains Operational Logs:** Keeps essential GKE system logs flowing to Cloud Logging for operational visibility.

  * **Minimal Change:** Minimizes disruption, requiring just a filter update on the existing logging sink.

  * **Cost-Effective:** Reduces the volume of ingested logs, directly impacting logging costs.

**Why Other Options Are Less Suitable:**

  * **I. Update the development cluster using the command: gcloud container clusters update --logging=SYSTEM.**

    * **Too Broad:** Disables application logging entirely, potentially hindering necessary debugging for developers.

    * **Loses Valuable Developer Insights:** May eliminate useful troubleshooting logs generated by developer-side applications.

  * **II. Modify the logging configuration for the development cluster with: gcloud container clusters update --logging=WORKLOAD.**

    * **No Filtering:** Doesn't address the verbosity issue. Logs would still be sent to Cloud Logging, incurring costs.

  * **III. Disable the default logging sink within the project associated with the development environment using: gcloud logging sinks update _Default --disabled.**

    * **Extreme Measure:** Completely disables all logging, including crucial GKE operational logs, hindering monitoring and troubleshooting.

---

## Question 36

*Domain 3: Applying Site Reliability Engineering Practices*

**You're tasked with establishing a Cloud Monitoring SLO for an upcoming service launch, aiming to ensure that requests are handled within 300 ms for at least 90% of the time per calendar month. How should you select the metric and evaluation method to meet this objective?**

- [x] I. Opt for a latency metric using a request-based evaluation approach.
- [ ] II. Opt for a latency metric using a window-based evaluation approach.
- [ ] III. Opt for an availability metric using a request-based evaluation approach.
- [ ] IV. Opt for an availability metric using a window-based evaluation approach.

### Explanation

**Correct Option:**

  * **I. Opt for a latency metric using a request-based evaluation approach.**

**Justification:**

  * **Matches the SLO Requirement:** Directly aligns with the performance goal of requests being handled within 300 ms.

  * **Focus on User Experience:** Request-based evaluation emphasizes the individual user experience with each request, ensuring a majority of users see acceptable performance.

  * **Typical for Latency SLOs:** This combination is commonly used for latency-based SLOs.

**Why Other Options Are Less Suitable:**

  * **II. Opt for a latency metric using a window-based evaluation approach.**

    * **Less User-Centric:** While relevant, window-based SLOs can mask significant latency issues within short time periods, potentially not reflecting the actual user experience.

  * **III. Opt for an availability metric using a request-based evaluation approach.**

    * **Measures a Different Aspect:** Availability deals with whether a service can respond at all, not how fast it responds. It wouldn't accurately measure the desired 300ms performance.

  * **IV. Opt for an availability metric using a window-based evaluation approach.**

    * **Even Less Granular:** This combines the wrong metric type (availability) with the less user-centric evaluation (window-based).

**References:**

<https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring#slo-type-request>

<https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring#slo-types>

---

## Question 37

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

**To enforce multiple constraint templates, including policies such as restricting the Kubernetes API, across your Google Kubernetes Engine (GKE) clusters, while ensuring these parameters are stored in a GitHub repository and automatically applied upon changes, what approach should you take?**

- [ ] I. Implement a GitHub action to trigger Cloud Build upon parameter changes, then use Cloud Build to execute a gcloud CLI command for applying the modifications.
- [ ] II. Utilize a webhook to notify Anthos Service Mesh of changes in GitHub, triggering the application of modifications.
- [x] III. Configure Anthos Config Management with the GitHub repository to automatically apply changes from the repository.
- [ ] IV. Configure Config Connector with the GitHub repository to automatically apply changes from the repository.

### Explanation

**Correct Option:**

**III. Configure Anthos Config Management with the GitHub repository to automatically apply changes from the repository.**

**Justification:**

  * **Purpose-Built Tool:** Anthos Config Management (ACM) is designed specifically for managing configurations across multiple Kubernetes clusters, including policies like constraint templates.

  * **GitOps Workflow:** ACM integrates seamlessly with Git, enabling a GitOps workflow where configuration changes in the repository trigger automatic updates to clusters.

  * **Centralized Management:** Provides a centralized way to enforce multiple constraint templates consistently across GKE clusters.

**Why Other Options Are Less Suitable:**

  * **I. Implement a GitHub action to trigger Cloud Build upon parameter changes, then use Cloud Build to execute a gcloud CLI command for applying the modifications.**

    * **More Complexity:** This approach requires building custom automation with GitHub Actions and Cloud Build. It's less streamlined than a dedicated config management tool like ACM.

  * **II. Utilize a webhook to notify Anthos Service Mesh of changes in GitHub, triggering the application of modifications.**

    * **Mismatched Focus:** Anthos Service Mesh is primarily focused on service networking and traffic management, not enforcing cluster policies across multiple clusters.

  * **IV. Configure Config Connector with the GitHub repository to automatically apply changes from the repository.**

    * **Specific Use Case:** Config Connector is suitable for managing external GCP resources via Kubernetes style definitions, but not the primary choice for enforcing intra-cluster Kubernetes policies.

**References:**

<https://medium.com/@kasiarun/introduction-to-anthos-config-management-1a43917c26ae>

<https://cloud.google.com/anthos-config-management/docs/concepts/policy-controller>

---

## Question 38

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

**Your company manages applications in Google Kubernetes Engine (GKE) using a GitOps approach. Developers frequently create cloud resources for their applications. To enable developers to handle infrastructure as code while adhering to Google-recommended practices and preventing configuration drift, what should you do?**

- [x] I. Implement and configure Config Connector in Google Kubernetes Engine (GKE).
- [ ] II. Set up Cloud Build with a Terraform builder to execute `**terraform plan**` and `**terraform apply**` commands.
- [ ] III. Deploy a Pod resource with a Terraform Docker image to execute `**terraform plan**` and `**terraform apply**` commands.
- [ ] IV. Configure a Job resource with a Terraform Docker image to execute `**terraform plan**` and `**terraform apply**` commands.

### Explanation

**Correct Option:**

**I. Implement and configure Config Connector in Google Kubernetes Engine (GKE).**

**Justification:**

  * **GitOps Alignment:** Config Connector is explicitly designed to manage GCP resources using Kubernetes-style declarative configurations, fitting seamlessly into a GitOps workflow.

  * **Google-Recommended:** Config Connector is Google's recommended tool for enabling Infrastructure as Code practices on GKE, ensuring compatibility and support.

  * **Prevents Configuration Drift:** By defining cloud resources as Kubernetes manifests, tracked in Git, Config Connector enforces consistency and detects/corrects drift.

**Why Other Options Are Less Ideal:**

  * **II. Set up Cloud Build with a Terraform builder to execute terraform plan and terraform apply commands.**

    * **Less Integrated:** While workable, it introduces an additional layer (Cloud Build) for managing cloud resources, increasing complexity compared to Config Connector's native Kubernetes integration.

  * **III. Deploy a Pod resource with a Terraform Docker image to execute terraform plan and terraform apply commands.**

    * **Manual Management:** Running Terraform in a Pod requires managing the Pod's lifecycle, state persistence, and ensuring it can run to completion, adding operational overhead.

  * **IV. Configure a Job resource with a Terraform Docker image to execute terraform plan and terraform apply commands.**

    * **Temporary Solution:** Jobs in Kubernetes are suitable for one-time tasks, not continuous management of cloud resources like Config Connector provides.

**References:**

<https://cloud.google.com/config-connector/docs/overview>

<https://cloud.google.com/blog/products/containers-kubernetes/anthos-config-management-config-controller-available-on-gke>

---

## Question 39

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

**Your company operates applications in Google Kubernetes Engine (GKE), with several relying on ephemeral volumes. Recently, you've observed instability in some applications due to the DiskPressure node condition on the worker nodes. However, you lack execute access to workloads and nodes. What should you do to identify which Pods are causing the issue?**

- [ ] I. Use Metrics Explorer to examine the node/ephemeral_storage/used_bytes metric.
- [x] II. Use Metrics Explorer to examine the container/ephemeral_storage/used_bytes metric.
- [ ] III. Identify all Pods with emptyDir volumes and employ the df -h command to measure volume disk usage.
- [ ] IV. Identify all Pods with emptyDir volumes and use the df -sh * command to measure volume disk usage.

### Explanation

**Correct option: II**

**Why option II is correct**

**II. Use Metrics Explorer to examine the**`**container/ephemeral_storage/used_bytes**`**metric.**

You explicitly **do not have execute access** to workloads or nodes, so the solution must rely on **observability data** , not shell commands.  
To identify **which Pods (containers)** are contributing to **DiskPressure** , you need **container-level visibility** into ephemeral storage usage.

Key fundamentals:

  * **DiskPressure** on a node is often caused by **excessive ephemeral storage consumption by one or more Pods** (for example, large `emptyDir` usage, logs, or temporary files).

  * The metric `**container/ephemeral_storage/used_bytes**` provides **per-container (and therefore per-Pod)** ephemeral storage usage.

  * Using **Metrics Explorer** , you can:

    * Group by `pod_name` / `container_name`

    * Identify the top consumers

    * Correlate spikes with DiskPressure events

  * This works **without any exec access** , fully satisfying the constraint.

This is the **Google-recommended, SRE-aligned approach** for diagnosing resource pressure issues when direct access is unavailable.

**Documentation:**  
<https://cloud.google.com/monitoring/api/metrics_gcp#gcp-kubernetes>

**Why the other options are not suitable**

**I.**`**node/ephemeral_storage/used_bytes**`  
This metric shows **node-level usage only**. It tells you _that_ a node is under pressure, but not **which Pods** are responsible.

**III. Use**`**df -h**`**on Pods with emptyDir volumes**  
This requires **exec access to workloads or nodes** , which you explicitly do not have.

**IV. Use**`**df -sh ***` **on Pods with emptyDir volumes**  
Same issue as III—this is a command-line, in-Pod approach and is not possible without execute access.

**Final answer:** **II**

---

## Question 40

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

**Your company has recently migrated to Google Cloud. To efficiently provision new projects and essential resources in Google Cloud, you aim to design a solution that is both swift and dependable. What should be your approach?**

- [ ] I. Opt for manual creation of projects using the Google Cloud console.
- [ ] II. Develop a script utilizing the gcloud CLI, capable of accepting relevant parameters from the request, and store it in a Git repository.
- [ ] III. Create a Terraform module and store it in your version control repository. Execute the terraform apply command to instantiate the new project.
- [x] IV. Utilize the Terraform repositories provided by the Cloud Foundation Toolkit, applying the code with appropriate parameters to create the Google Cloud project and related resources.

### Explanation

**Correct option: IV**

**Why option IV is correct**

**IV. Utilize the Terraform repositories provided by the Cloud Foundation Toolkit, applying the code with appropriate parameters to create the Google Cloud project and related resources.**

This is the **most Google-recommended, scalable, and reliable approach** for rapidly provisioning Google Cloud projects and foundational resources after a migration.

Core fundamentals behind this choice:

  * **Cloud Foundation Toolkit (CFT)** provides **production-ready, opinionated Terraform modules** designed by Google specifically for:

    * Project creation

    * IAM setup

    * Networking

    * Logging, billing, and org-level governance

  * The modules follow **Google Cloud best practices** and are continuously maintained to stay aligned with platform changes.

  * Using CFT significantly **reduces risk, time, and design errors** compared to building everything from scratch.

  * Terraform ensures:

    * Idempotent and repeatable provisioning

    * Version control and auditability

    * Fast, parameter-driven project creation

This approach is ideal when the goal is **speed + reliability + standardization** at scale.

**Why the other options are not suitable**

**I. Manual project creation via the console**  
Manual workflows are slow, error-prone, non-repeatable, and unsuitable for enterprise-scale provisioning.

**II. Custom gcloud CLI script stored in Git**  
While better than manual steps, scripts lack:

  * Strong state management

  * Dependency tracking

  * Built-in drift detection  
Terraform is explicitly recommended over imperative scripting for infrastructure provisioning.

**III. Create a custom Terraform module from scratch**  
This is viable, but unnecessary. Google already provides **battle-tested modules** via CFT, making this option slower and riskier than IV.

**Final answer:** **IV**

---

## Question 41

*Domain 5: Optimizing Performance and Cost*

**As you monitor a service employing n2-standard-2 Compute Engine instances for delivering large files, users complain of slow download speeds. Cloud Monitoring indicates that VMs are operating at maximum network throughput. How can you improve network throughput performance?**

- [ ] I. Enhance the VMs by adding more network interface controllers (NICs).
- [ ] II. Implement a Cloud NAT gateway and link it to the VMs' subnet.
- [x] III. Upgrade the VMs' machine type to n2-standard-8.
- [ ] IV. Deploy the Ops Agent to access supplementary monitoring metrics.

### Explanation

**Correct option: III**

**Why option III is correct**

**III. Upgrade the VMs' machine type to n2-standard-8.**

In Google Compute Engine, **network throughput scales with machine type size**. When Cloud Monitoring shows that VMs are already operating at **maximum network throughput** , it means the instances have hit their **per-VM network bandwidth ceiling** , not a software or configuration issue.

Key fundamental concepts:

  * **Network performance is tied to vCPU count** : Larger machine types provide higher **egress and ingress bandwidth caps**.

  * **n2-standard-2** instances have relatively low maximum network throughput, which is insufficient for serving **large file downloads** at high speed.

  * By upgrading to **n2-standard-8** , you significantly increase:

    * Available network bandwidth

    * Packet processing capacity

    * Sustained throughput per VM

  * This improves download speeds **without changing application logic or architecture** , making it the most direct and effective fix.

This is a classic **capacity scaling** scenario where vertical scaling is the correct response.

**Relevant documentation:**  
<https://cloud.google.com/compute/docs/network-bandwidth>

**Why the other options are not suitable**

**I. Add more network interface controllers (NICs).**  
Multiple NICs are used for **network isolation or multi-network connectivity** , not for increasing outbound throughput of a single workload. They do not aggregate bandwidth for standard traffic flows.

**II. Implement a Cloud NAT gateway.**  
Cloud NAT provides **outbound internet access** for private VMs. It does not increase VM network throughput and can actually introduce additional limits.

**IV. Deploy the Ops Agent.**  
The Ops Agent improves observability only. It does not affect performance and does not remove network bandwidth limits.

**Final answer:** **III**

---

## Question 42

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

You support an **e-commerce application** that runs on a **large Google Kubernetes Engine (GKE) cluster** deployed **both on-premises and on Google Cloud**. The application consists of **microservices running in containers**.

You want to **identify containers that are using the most CPU and memory**.

What should you do?

- [x] **A.** Use **Cloud Operations for GKE (Cloud Monitoring and Cloud Logging)**.
- [ ] **B.** Use **Prometheus** to collect and aggregate logs per container, and then analyze the results in **Grafana**.
- [ ] **C.** Use the **Cloud Monitoring API** to create **custom metrics** , and then organize your containers using **groups**.
- [ ] **D.** Use **Cloud Logging** to export application logs to **BigQuery** , aggregate logs per container, and then analyze **CPU and memory consumption**.

### Explanation

**Correct Answer: A. Use Cloud Operations for GKE (Cloud Monitoring and Cloud Logging).**

**Explanation**

To identify which containers are consuming the most **CPU** and **memory** across a hybrid GKE deployment (on-prem + Google Cloud), the most efficient and fully integrated solution is **Cloud Operations for GKE**.

Cloud Operations for GKE provides:

  * **Per-container CPU usage metrics**

  * **Per-container memory usage metrics**

  * **Node and pod-level resource dashboards**

  * Built-in **workload monitoring**

  * Automatic telemetry collection with minimal setup

You can directly view the highest resource-consuming containers using built-in charts and dashboards—no need for custom metrics, log exports, or additional tooling.

**Why the Other Options Are Incorrect**

**B. Prometheus + Grafana**

Although technically possible and common in Kubernetes environments, it introduces:

  * More infrastructure to manage

  * Higher operational overhead

  * No need for Grafana when Cloud Operations already provides dashboards  
Not the simplest or most integrated solution.

**C. Create custom metrics with Cloud Monitoring API**

Not required—CPU and memory metrics for containers are **already provided automatically** by GKE + Cloud Monitoring.  
Custom metrics add unnecessary work.

**D. Export logs to BigQuery**

Application logs do **not** include CPU/memory usage.  
You can't infer resource consumption from logs, so this approach will not work.

**Authoritative Google Documentation**

Cloud Operations for GKE – Observability and Container Metrics  
<https://cloud.google.com/stackdriver/docs/solutions/gke>

**Final Answer: A. Use Cloud Operations for GKE**

---

## Question 43

*Domain 2: Building and Implementing CI/CD Pipelines*

**Following your organization's recent adoption of a container-based workflow for application development, your team consistently deploys numerous applications to a Kubernetes cluster in the production environment through an automated build pipeline. However, the security auditor has expressed concerns regarding the potential for developers or operators to bypass automated testing and push unauthorized code changes to production. How can you enforce approvals in this scenario?**

- [ ] I. Implement protected branches in the build system, mandating approval of pull requests.
- [ ] II. Deploy an Admission Controller to validate that incoming requests originate from approved sources.
- [ ] III. Utilize Kubernetes Role-Based Access Control (RBAC) to restrict access exclusively to approved users.
- [x] IV. Enable binary authorization within the Kubernetes cluster and configure the build pipeline as an attestor.

### Explanation

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

---

## Question 44

*Domain 3: Applying Site Reliability Engineering Practices*

**You manage a service with a well-defined Service Level Objective (SLO) that has consistently been achieved for the past 6 months, resulting in high customer satisfaction. With most operational tasks automated and only a few repetitive tasks occurring frequently, you aim to optimize the balance between reliability and deployment velocity while adhering to site reliability engineering best practices. What steps should you take? (Select two.)**

- [ ] I. Consider tightening the service's SLO criteria.
- [x] II. Potentially accelerate the service's deployment velocity and/or risk profile.
- [x] III. Allocate engineering resources to other services requiring greater reliability.
- [ ] IV. Collaborate with the product team to prioritize reliability improvements over new features.
- [ ] V. Adjust the implementation of your Service Level Indicators (SLIs) to broaden coverage.

### Explanation

**The two best steps for this scenario are:**

  * **II. Potentially accelerate the service's deployment velocity and/or risk profile.** Your service's track record demonstrates the ability to maintain a reliable SLO. This allows for experimentation with quicker iterations and potentially more complex changes to boost innovation.

  * **III. Allocate engineering resources to other services requiring greater reliability.** Capitalize on your current service's success by shifting resources to areas that need attention. This promotes a balanced and efficient approach across your systems.

**Why these options are the most suitable:**

  * **Utilizing Success:** Your service's reliability creates space for focusing efforts on other areas or pushing for greater feature development velocity.

  * **SRE Alignment:** This approach aligns with SRE principles by allocating resources strategically across systems to maximize overall user experience.

**Why other options are less ideal:**

  * **I. Consider tightening the service's SLO criteria.** While a possibility, it might be unnecessary given the consistent success and could even introduce undue pressure.

  * **IV. Collaborate with the product team to prioritize reliability improvements over new features.** With the current service already performing well, this might unnecessarily stifle product development.

  * **V. Adjust the implementation of your Service Level Indicators (SLIs) to broaden coverage.** While always beneficial to improve monitoring, it doesn't directly address the opportunity to balance reliability and velocity.

**Reference:**

<https://sre.google/workbook/implementing-slos/#slo-decision-matrix>

---

## Question 45

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

**You're utilizing Terraform to manage infrastructure as code within a CI/CD pipeline. However, you notice that multiple copies of the entire infrastructure stack persist in your Google Cloud project, with a new copy created each time a change is made to the existing infrastructure. To optimize your cloud spend following Google-recommended practices, what steps should you take?**

- [ ] I. Implement a new pipeline to automatically delete outdated infrastructure stacks when they're no longer required.
- [x] II. Ensure that the pipeline stores and retrieves the terraform.tfstate file from Cloud Storage using the Terraform gcs backend.
- [ ] III. Verify that the pipeline stores and retrieves the terraform.tfstate file from a source control repository.
- [ ] IV. Update the pipeline to remove any existing infrastructure before applying the latest configuration.

### Explanation

**II. Ensure that the pipeline stores and retrieves the terraform.tfstate file from Cloud Storage using the Terraform gcs backend.**

**Reasoning:**

  * **State Management:** The `terraform.tfstate` file is vital as it tracks the mapping between your Terraform configuration and the actual deployed infrastructure. Storing it remotely in Cloud Storage allows Terraform to correctly identify changes needed, instead of always creating an entirely new stack.

  * **Cloud Integration:** The GCS backend integrates seamlessly with Google Cloud, ensuring secure and reliable state storage.

  * **Cost Optimization:** This approach directly addresses the issue of redundant stacks proliferating, reducing the need for unnecessary resources and associated costs.

**Why Other Options Are Less Ideal:**

  * **I. Implement a new pipeline...** While deleting old infrastructure could help, it doesn't address the root cause of the issue – incorrect state management.

  * **III. Verify that the pipeline stores...** Source control systems are excellent for code versioning, but less ideal for handling the dynamic `terraform.tfstate`.

  * **IV. Update the pipeline to remove...** Destructive actions can lead to accidental data loss if applied without careful state tracking.

**Reference:**

<https://cloud.google.com/docs/terraform/resource-management/managing-infrastructure-as-code#configuring_terraform_to_store_state_in_a_cloud_storage_bucket>

---

## Question 46

*Domain 3: Applying Site Reliability Engineering Practices*

**Your organization aims to elevate the availability target of an application from 99.9% to 99.99% with a $2,000 investment. The current revenue generated by the application is $1,000,000. You need to assess whether the increased availability justifies the investment for a single year of usage. What should you do?**

- [x] I. Evaluate the value of enhanced availability at $900 and conclude that the investment is not justified.
- [ ] II. Assess the value of enhanced availability at $1,000 and conclude that the investment is not justified.
- [ ] III. Determine the value of enhanced availability at $1,000 and conclude that the investment is justified.
- [ ] IV. Calculate the value of enhanced availability at $9,000 and conclude that the investment is justified.

### Explanation

**Correct choice — I. “Evaluate the value of enhanced availability at $900 and conclude that the investment is not justified.”**

**Why option I is correct**

  1. **How many outage hours are removed?**

     * 99.9 % (“three-nines”) permits ≈ 8 h 45 m 57 s of downtime per year. [uptime.is](https://uptime.is/)

     * 99.99 % (“four-nines”) permits ≈ 52 m 36 s of downtime per year. [uptime.is](https://uptime.is/99.99)

     * Δ downtime = 8.76 h − 0.876 h ≈ 7.884 h saved.

  2. **How much money does that save?**

     * Annual revenue = $1 000 000.

     * Revenue/hour = $1 000 000 ÷ 8 760 h ≈ $114.16 per hour.

     * Value of avoided downtime = 7.884 h × $114.16 ≈ **$900**.

  3. **Compare benefit to cost.**

     * Benefit ≈ $900 / year < Cost = $2 000 / year → financially **unfavorable**.

Therefore option I, which identifies the benefit as $900 and rejects the $2 000 spend, matches the calculation.

**Why the other options are wrong**

  * **II. “Assess the value at $1 000 and conclude the investment is not justified.”**

    * The conclusion (not justified) is fine, but the _benefit figure_ is wrong. Correct math gives ≈ $900, not $1 000; an extra $100 appears from rounding far beyond two significant digits.

  * **III. “Determine the value at $1 000 and conclude the investment is justified.”**

    * Two errors: the benefit is overstated (should be ≈ $900) **and** even at $1 000 the cost still exceeds the benefit, so calling it “justified” is logically inconsistent.

  * **IV. “Calculate the value at $9 000 and conclude the investment is justified.”**

    * The $9 000 figure is off by an order of magnitude (likely mis-placing a decimal). Because the correct benefit is only about $900, this option both mis-states the savings and reaches an incorrect conclusion.

**Bottom line:** Elevating availability from 99.9 % to 99.99 % yields ~7.9 hours of extra uptime worth roughly **$900** in annual revenue protection—far short of the proposed **$2 000** outlay. Only option I reflects that reality.

---

## Question 47

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

**You encounter an error "The organization policy constraint iam.disableServiceAccounKeyCreation is enforced" when attempting to export a service account key for a third-party application. How can you resolve this while adhering to Google's security recommendations?**

- [ ] A. Activate the default service account key and obtain it.
- [ ] B. Eliminate the iam.disableServiceAccountKeyCreation policy at the organization level, then generate the key.
- [ ] C. Deactivate the service account key creation policy within the project's folder and obtain the default key.
- [x] D. Include a directive to disable the iam.disableServiceAccountKeyCreation policy in your project, then proceed to create a key.

### Explanation

**Correct answer: D — Add a project-level exception to the**`**iam.disableServiceAccountKeyCreation**`**constraint, create the one key you need, then keep the exception as narrow and short-lived as possible.**

  * Google recommends enforcing **Disable service account key creation** at the **organization** root to block long-lived user-managed keys everywhere by default. [cloud.google.com](https://cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts?utm_source=chatgpt.com)

  * When a workload truly cannot use a stronger alternative (for example, Workload Identity Federation), you should **override the constraint only on the affected project or even a single service account**. In the policy editor you choose _Override parent’s policy_ and switch **Enforcement** off just for that scope. [cloud.google.com](https://cloud.google.com/iam/docs/troubleshoot-org-policies?utm_source=chatgpt.com)

This keeps the global protection intact while letting you create exactly one key for the third-party integration—and nothing else.

**Why the other options fall short**

  * **Option A – “Activate the default service-account key and obtain it.”**  
Google-managed keys are rotated automatically and are **not downloadable** ; only newly created **user-managed** keys can ever be exported. [googlecloudcommunity.com](https://www.googlecloudcommunity.com/gc/Developer-Tools/Issue-with-user-managed-GCP-public-key-for-Service-Account/td-p/780657?utm_source=chatgpt.com)

  * **Option B – “Remove the constraint at the organization level.”**  
Disabling the policy for the whole organization re-opens key creation for every project, defeating the very control Google recommends you keep enabled. [cloud.google.com](https://cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts?utm_source=chatgpt.com)

  * **Option C – “Turn the policy off on the folder.”**  
A folder-wide exemption is narrower than option B but still broader than necessary. Best practice is the smallest possible scope—usually a single project or service account. [cloud.google.com](https://cloud.google.com/iam/docs/troubleshoot-org-policies?utm_source=chatgpt.com)

**Extra security tip**

Before creating any key, verify whether the third-party product can authenticate with **Workload Identity Federation** , which “eliminates the maintenance and security burden associated with service-account keys.” [cloud.google.com](https://cloud.google.com/iam/docs/workload-identity-federation?utm_source=chatgpt.com)

---

## Question 48

*Domain 3: Applying Site Reliability Engineering Practices*

**Your company adheres to Site Reliability Engineering principles. Following a severe incident triggered by a software change, you're drafting a postmortem to prevent similar incidents in the future. What steps should you take?**

- [ ] A. Identify the engineers accountable for the incident and escalate the matter to senior management.
- [x] B. Ensure that test cases capable of catching errors like this are successfully executed before every new software release.
- [ ] C. Conduct follow-ups with the staff who reviewed the changes and establish best practices for future adherence.
- [ ] D. Develop a policy mandating that on-call teams promptly engage engineers and management in discussions to devise an action plan upon incident occurrence.

### Explanation

**The best answer here is**

**B. Ensure that test cases capable of catching errors like this are successfully executed before every new software release.**

Here's why and a breakdown of the other options:

**Why Option B is the Best Approach:**

  * **Focus on Prevention:** SRE is about building resilient systems and preventing failures. While other options have value, this option directly addresses the root cause by creating a safety net to catch similar errors before they impact production.

  * **Systems-Based Approach:** It emphasizes improving processes rather than focusing on individuals, aligning with SRE and fostering a blameless culture.

**Why Other Options are Less Ideal:**

  * **A. Identify the engineers accountable for the incident and escalate the matter to senior management.**

    * **Blame Culture:** This promotes a culture of fear and discourages open communication, undermining SRE principles and making it harder to uncover the true systemic causes of failure.

  * **C. Conduct follow-ups with the staff who reviewed the changes and establish best practices for future adherence.**

    * **While valuable, it's reactive:** This option is important for learning from the incident, but it doesn't directly prevent a similar error from happening again.

  * **D. Develop a policy mandating that on-call teams promptly engage engineers and management in discussions to devise an action plan upon incident occurrence.**

    * **Focus on Response, Not Prevention:** This optimizes incident response, which is vital, but the main goal of the postmortem is to proactively avoid repeating the incident.

---

## Question 49

*Domain 3: Applying Site Reliability Engineering Practices*

**You're maintaining a user-facing web application and analyzing its error budget over the past six months. Despite occasional fluctuations, the application has consistently stayed below 5% of its error budget. After a Service Level Objective (SLO) review with stakeholders, you confirm that the current SLO is appropriate. How can you better align the application's SLO with its actual reliability, considering velocity, reliability, and business needs? (Select two.)**

- [ ] A. Increase serving capacity across all application zones.
- [x] B. Opt for more frequent or potentially risky application releases.
- [ ] C. Adjust the SLO to better match the observed reliability of the application.
- [x] D. Introduce and assess additional Service Level Indicators (SLIs) for the application.
- [ ] E. Schedule planned downtime to utilize more of the error budget, ensuring users aren't reliant on a stricter SLO.

### Explanation

**Correct Answers: B and D**

**Reasoning**

Your application has consistently consumed **less than 5%** of its error budget over six months.  
This means:

  * The service is **more reliable than required** by the current SLO.

  * You are **under-utilizing your error budget**.

  * You can afford to **move faster** without hurting users or violating SLOs.

Google SRE guidance states:

  * **If your error budget is consistently under-consumed** , you should **increase the release velocity**.

  * **If your SLO is appropriate and not too strict** , you should **NOT tighten it** , but instead improve value delivery or observability by adding meaningful SLIs.

This leads to the two correct choices.

**Correct Answer 1: B. Opt for more frequent or potentially risky application releases.**

Why this is correct

Underused error budget means:

  * You can ship faster

  * You can take more risk

  * You can accelerate innovation

This is exactly what Google’s **Error Budget Policy** recommends.

**Reference:**  
**Google SRE Book - Error Budget Policy**  
<https://sre.google/sre-book/availability-table/>

**Correct Answer 2: D. Introduce and assess additional Service Level Indicators (SLIs) for the application.**

**Why this is correct**

If your system appears _too reliable_ , you might not be measuring **all** important aspects of user experience.

Adding or refining SLIs can:

  * Improve understanding of real reliability

  * Ensure all critical user interactions are measured

  * Align reliability signals with business needs

This is a standard SRE practice when reliability seems artificially high.

**Reference:**  
**Google SRE Workbook – Implementing SLIs**  
<https://sre.google/workbook/implementing-slos/>

**Why the Other Options Are Incorrect**

**A. Increase serving capacity**

This increases cost and does not improve alignment with SLOs.  
Your system is already exceeding expectations.

**C. Adjust the SLO**

You **already confirmed** the SLO is appropriate.  
Tightening it would reduce error budget artificially and may slow velocity without business need.

**E. Schedule planned downtime**

This is anti-SRE and harmful.  
Never reduce reliability intentionally just to “use up” error budget.

**Final Answer: B and D**

---

## Question 50

*Domain 2: Building and Implementing CI/CD Pipelines*

**What steps should you take to deploy the new versions of your service's API with minimal disruption to third-party developers and end users of third-party installed applications?**

- [x] A. Implement the new API version, announce deprecation of the old version, contact remaining users of the old API, provide best effort support to users, and finally, deactivate the old version.
- [ ] B. Announce the old API version deprecation, introduce the new version, contact users still on the old version, deactivate the old version, and offer best effort support to old API users.
- [ ] C. Notify the deprecation of the old API version, contact remaining users of the old version, introduce the new version, deactivate the old version, provide best effort support, and finally, turn down the old version.
- [ ] D. Introduce the new API version, contact users still on the old API version, announce the deprecation of the old version, deactivate the old version, and provide best effort support to old API users.

### Explanation

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

---

## Question 51

*Domain 3: Applying Site Reliability Engineering Practices*

**As the SRE engineer for a microservice deployed to a Google Kubernetes Engine (GKE) Autopilot cluster, you oversee an online store's functionality. The system publishes order messages to Pub/Sub, and a microservice processes these messages to update stock information in the warehousing system. Due to a surge in orders during a sales event, stock updates are lagging, leading to orders being accepted for out-of-stock products. Reviewing the microservice metrics against typical levels reveals:**

**Current Microservice Metrics:**

**A. Average CPU usage across all Pods: 30% of Pod limit (typical state: 20% of Pod limit)**

**B. Average memory usage across all Pods: 10% of Pod limit (typical state: 10% of Pod limit)**

**C. Pub/Sub subscription:A. Average oldest unacknowledged message age: 8074 milliseconds (typical state: 347 milliseconds)**

**D. Average undelivered messages: 14705 messages (typical state: 5 messages)**

**E. Average acknowledgment latency: 354 milliseconds (typical state: 312 milliseconds)**

**Your objective is to ensure accurate inventory representation in the warehouse system during order placement while minimizing customer impact. What course of action should you take to resolve the current situation?**

- [ ] I. Decrease the acknowledgment deadline on the subscription.
- [ ] II. Introduce a virtual queue to manage typical traffic levels on the online store.
- [x] III. Scale up the number of Pod replicas.
- [ ] IV. Increase the Pod CPU and memory limits.

### Explanation

**Correct Answer: III. Increase the number of Pod replicas.**

Reasoning

The metrics clearly indicate a **processing throughput bottleneck** , not a resource constraint on individual Pods.

Key observations from the metrics:

  * **CPU usage:** 30% of Pod limit (only slightly higher than normal 20%)

  * **Memory usage:** 10% of Pod limit (same as normal)

This shows that **individual Pods are not resource-constrained**.

However, Pub/Sub metrics show a **large backlog** :

  * **Oldest unacknowledged message age:** 8074 ms (vs 347 ms normally)

  * **Undelivered messages:** 14,705 (vs 5 normally)

  * **Acknowledgment latency:** slightly increased

These metrics indicate that **messages are accumulating faster than the microservice can process them** , meaning the system **needs more parallel consumers**.

In a Pub/Sub-driven architecture, the standard scaling strategy is:

  * Increase the number of **consumer instances** (Pods)

  * Each Pod pulls messages independently

  * Pub/Sub distributes messages across consumers automatically

In **GKE Autopilot** , scaling Pods increases message processing concurrency without managing nodes manually.

Increasing replicas will:

  * Increase message processing throughput

  * Reduce backlog

  * Ensure inventory updates keep pace with order intake

  * Prevent overselling inventory

This aligns with Google Cloud’s guidance for Pub/Sub consumer scaling.

Reference:  
<https://cloud.google.com/pubsub/docs/pull#scaling_subscribers>

**Why the other options are not the best choice**

**I. Decrease the acknowledgment deadline on the subscription**

The acknowledgment deadline determines **how long the subscriber has to acknowledge a message** before Pub/Sub redelivers it.  
Reducing it would **increase duplicate deliveries** and worsen load rather than increasing processing throughput.

Reference:  
<https://cloud.google.com/pubsub/docs/subscriber#ack_deadline>

**II. Add a virtual queue to the online store that allows typical traffic levels**

Introducing a queue or throttling layer at the store would **delay or reject orders** , negatively impacting customers during a sales event.  
It does not solve the underlying issue of **insufficient consumer throughput**.

**IV. Increase the Pod CPU and memory limits**

Current usage shows:

  * CPU ~30%

  * Memory ~10%

This indicates Pods **are not CPU or memory bound**. Increasing limits would not increase message processing throughput.

Reference:  
<https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview>

**Key Concept to Remember**

When **Pub/Sub backlog increases while CPU/memory usage remains low** , the issue is typically **insufficient consumer parallelism** , not resource exhaustion.

The recommended solution is to **scale horizontally (more subscriber Pods)** rather than vertically scaling Pod resources.

---

## Question 52

*Domain 2: Building and Implementing CI/CD Pipelines*

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

- [ ] A. Update the Deployment blue-app to revert to the previous version of the application.
- [ ] B. Roll back the Deployment green-app to use the prior version of the application.
- [ ] C. Modify the selector on the Service appservice to app: my-app.
- [x] D. Adjust the selector on the Service appservice to app: my-app, version: blue.

### Explanation

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

---

## Question 53

*Domain 2: Building and Implementing CI/CD Pipelines*

**You're managing an application on Google Cloud Platform (GCP) using Terraform. The application leverages a managed instance group for deployment on instances defined by an instance template. Your CI/CD pipeline deploys the Terraform code. When you attempt to update the machine type within the instance template via Terraform, the pipeline fails during the terraform apply stage, encountering the following error message:**

**Error waiting for deleting instance template: The instance_template resource 'project/demo-project/global/instanceTemplates/demo-instance-2024010000010001' is already being used by 'projects/demo-project/regions/us-central1/instanceGroupManagers/demo-mig'**

**Your objective is to update the instance template while minimizing disruptions to both the application and the CI/CD pipeline execution frequency.**

**What's the most appropriate course of action?**

- [ ] A. Delete the managed instance group entirely, then recreate it after updating the instance template.
- [ ] B. Introduce a new instance template, update the managed instance group to use this new template, and subsequently delete the old instance template.
- [ ] C. Eliminate the managed instance group from your Terraform state file, update the instance template, and then re-import the managed instance group.
- [x] D. Employ the create_before_destroy meta-argument within the instance template's lifecycle block, setting it to `true`.

### Explanation

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

---

## Question 54

*Domain 4: Implementing Observability Practices and Troubleshooting Issues*

**You are devising a plan to present Cloud Monitoring metrics for your organization's Google Cloud projects. The organizational structure includes three folders (Development, Staging, and Production), each containing two projects (app-1-dev, app-1-staging, app-1-prod, app-2-dev, app-2-staging, and app-2-prod).**

**Folders:**

  * Development: app-1-dev, app-2-dev

  * Staging: app-1-staging, app-2-staging

  * Production: app-1-prod, app-2-prod

**Your objective is to configure Cloud Monitoring dashboards to exhibit metrics solely from the projects within a designated folder (e.g., the Development folder). It's crucial to adhere to Google's recommended practices for this setup.**

**What course of action should you pursue?**

- [ ] A. Establish a single new scoping project.
- [x] B. Establish new scoping projects for each folder (Development, Staging, and Production).
- [ ] C. Utilize the current app-1-prod project as the scoping project.
- [ ] D. Employ the current projects (app-1-dev, app-1-staging, and app-1-prod) as the scoping project for the Development folder.

### Explanation

The most appropriate course of action for configuring Cloud Monitoring dashboards to exhibit metrics solely from the projects within a designated folder is:

**B. Establish new scoping projects for each folder (Development, Staging, and Production).**

**Explanation:**

Establishing new scoping projects for each folder aligns with Google's recommended practices for organizing resources and managing access control within Google Cloud Platform. By creating separate scoping projects for each folder, you can effectively segregate the monitoring metrics based on the environment (Development, Staging, and Production). This approach provides better isolation, scalability, and control over the monitoring setup for each environment.

**Justification for why other options are not suitable:**

**A. Establishing a single new scoping project:**

  * This option would result in a lack of segregation between the different environments (Development, Staging, and Production), making it challenging to manage access control and monitor metrics specific to each environment effectively.

**C. Utilizing the current app-1-prod project as the scoping project:**

  * Using an existing production project as the scoping project could lead to issues with access control and resource isolation. Mixing production monitoring with development or staging environments may not adhere to best practices and could potentially expose sensitive production metrics to inappropriate access.

**D. Employing the current projects (app-1-dev, app-1-staging, and app-1-prod) as the scoping project for the Development folder:**

  * This option suggests using individual projects within a folder as the scoping project, which may not provide the desired level of organization and segregation. It's more practical to have separate scoping projects for each folder to ensure better management and control over the monitoring setup.

---

## Question 55

*Domain 3: Applying Site Reliability Engineering Practices*

**Your organization is leading a DevOps project. The current responsibilities are as follows:**

  * **The DevOps team manages the service infrastructure and is on-call for incidents.**

  * **The Software Development team writes, submits, and reviews code.**

**Currently, neither team has published Service Level Objectives (SLOs) for the service. You are tasked with designing a new joint-ownership model where both teams share responsibility for the service.**

**How should you allocate the responsibilities between the DevOps team and the Software Development team in this new model?**

- [ ] A: Limited Collaboration
    DevOps: Management of service infrastructure and response to incidents.
    Software Development: Code development, submission of code for review, and conducting reviews of code.
    Shared: No shared responsibilities.
- [ ] B: Complete Role Reversal
    DevOps: Code development, submission of code for review, and conducting reviews of code.
    Software Development: Management of service infrastructure and response to incidents.
    Shared: No shared responsibilities.
- [x] C: SLO-Focused Collaboration
    DevOps: Management of service infrastructure and response to incidents.
    Software Development: Code development, submission of code for review, and conducting reviews of code.
    Shared: Defining and making public Service Level Objectives (SLOs) for the service.
- [ ] D: Expanded Joint Ownership
    DevOps: Management of service infrastructure, response to incidents, definition and publication of SLOs.
    Software Development: Code development, submission of code for review, conducting reviews of code, monitoring of application performance metrics.
    Shared: No explicit shared responsibilities (though collaboration on SLOs is likely).

### Explanation

Out of the provided options, the best approach for the new joint-ownership model is

**C: SLO-Focused Collaboration**. Here's why:

**Why SLOs Matter**

  * **Shared Understanding:** SLOs create a common language around service health and reliability, providing clear targets for both teams to work towards.

  * **Customer Focus:** SLOs directly tie service performance to user experience, ensuring the focus remains on delivering a reliable product.

  * **Proactive Approach:** Monitoring performance against SLOs allows teams to identify and address potential issues before they escalate into major incidents.

**Breakdown of Responsibilities**

  * **DevOps:**

    * **Manage Infrastructure:** DevOps remains responsible for maintaining the underlying infrastructure supporting the service.

    * **Incident Response:** As the specialists in infrastructure and operations, DevOps continues to handle incident resolution.

  * **Software Development:**

    * **Code Ownership:** Software devs focus on writing, submitting, and reviewing code to ensure quality and maintainability.

  * **Shared:**

    * **Defining SLOs:** Both teams collaborate to determine appropriate SLOs based on user expectations, business needs, and the capabilities of the system.

    * **Publishing SLOs:** Making SLOs visible to stakeholders improves transparency and builds trust.

**Advantages of SLO-Focused Collaboration**

  * **Balance:** Maintains core strengths of each team while creating a clear overlap in responsibility around service reliability.

  * **Mutual Accountability:** Both teams are incentivized to work together to meet the agreed-upon SLOs.

  * **Data-Driven Improvement:** SLO monitoring leads to insights that drive improvements across development and operational practices.

**Why Other Options Are Less Ideal**

  * **A: Limited Collaboration:** No shared goals or responsibilities make it hard to drive holistic service improvements.

  * **B: Complete Role Reversal:** Forcing teams into unfamiliar domains is disruptive and inefficient. It's better to leverage existing expertise.

  * **D: Expanded Joint Ownership:** While good in theory, it risks overextending team responsibilities. SLOs provide a more manageable starting point for shared ownership.

---

## Question 56

*Domain 2: Building and Implementing CI/CD Pipelines*

**In the context of managing a high-priority workload on an autoscaled managed instance group within a single zone, with the need to validate alterations before finalizing changes and ensuring uninterrupted capacity for handling requests during testing, what is the recommended action to achieve this?**

- [x] I. Modify autoscaling settings to "Only scale out" during the modification process.
- [ ] II. Transform the managed instance group to function across multiple zones.
- [ ] III. Temporarily disable autoscaling while implementing changes.
- [ ] IV. Enable predictive autoscaling to anticipate resource requirements.

### Explanation

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

---

## Question 57

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

**Your company mandates adherence to a standardized development environment template, including popular integrated development environments (IDEs), with a focus on maintaining security patches and updates. Additionally, you aim to implement a reliable method, recommended by Google, to ensure consistent development environments across all team members. Which approach should you choose?**

- [ ] I. Implement daily Compute Engine snapshots of a 'golden' machine with all security patches, allowing developers to update their own machines from these snapshots.
- [ ] II. Create a comprehensive checklist of software updates along with update scripts for developers to apply updates on their own machines.
- [ ] III. Develop an image containing all current dependencies and deploy this image on developers' laptops for their use.
- [x] IV. Establish Cloud Workstations configurations customized to each team's needs.

### Explanation

**Out of the options provided, the best approach to achieve your goals is**

**IV. Establish Cloud Workstations configurations customized to each team's needs.** Here's why:

**Advantages of Cloud Workstations:**

  * **Standardized Environments:** Cloud Workstations provide centrally managed development environments, ensuring consistency across your team and easier adherence to your company's template.

  * **Easy Updates and Security:** You can maintain and update a base configuration with all the required tools, dependencies, and security patches, which developers then access through Cloud Workstations.

  * **Scalability and Portability:** Cloud Workstations eliminates setup issues on individual machines and offers flexibility for developers to work from different locations or devices.

  * **Google Recommended:** Cloud Workstations is a solution natively integrated with Google Cloud Platform, making it a recommended and well-supported choice for GCP users.

**Why Other Options are Less Ideal:**

  * **I. Compute Engine Snapshots:** While snapshots can be useful for backups, they are not efficient for frequently updated development environments. Developers would need to manually restore snapshots regularly, which is time-consuming.

  * **II. Checklists and Scripts:** Relies heavily on individual developers to consistently apply updates and configurations. This is error-prone and can lead to inconsistencies across environments.

  * **III. Deploying images on laptops:** This can work for smaller teams with homogeneous hardware. However, it introduces management overhead for different hardware types and doesn't scale easily.

**References:**

<https://cloud.google.com/workstations/docs/overview>

<https://cloud.google.com/workstations/docs/create-configuration>

<https://cloud.google.com/workstations/docs/create-workstation>

<https://www.youtube.com/watch?v=C6Dpmujxp9Q>

---

## Question 58

*Domain 2: Building and Implementing CI/CD Pipelines*

**Your team has been alerted to a critical security vulnerability requiring a patch on Compute Engine instances serving millions of global customers. The goal is to swiftly deploy the security patch while minimizing costs and impact on end customers. What is the recommended course of action?**

- [x] I. Perform a canary rollout of the security patch with a brief duration for testing.
- [ ] II. Simultaneously update all Compute Engine instances worldwide.
- [ ] III. Conduct a 24-hour rolling update during each region's overnight hours.
- [ ] IV. Implement an A/B rollout by duplicating all Compute Engine instances, applying the security patch to one set, and then transitioning users.

### Explanation

**Choose I — start with a short-lived canary rollout of the patched instance template, verify that the first few VMs stay healthy, and then let the Managed Instance Group (MIG) updater finish rolling the patch out everywhere.**

  * Google Cloud’s MIG updater is designed for exactly this scenario: it lets you **canary a new template on a small slice of instances** (for example, 1-5 %) and, if health checks stay green, automatically continue to a full rollout. This gets the security fix into production much faster than a region-by-region schedule, yet still limits blast radius if something goes wrong. [cloud.google.com](https://cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups?utm_source=chatgpt.com) | [cloud.google.com](https://cloud.google.com/compute/docs/instance-groups?utm_source=chatgpt.com)

  * A canary update is markedly cheaper than running an entire duplicate fleet (the A/B pattern) and avoids the customer-visible risk of a simultaneous global restart. Google’s documentation calls canary deployment a **“progressive rollout that splits traffic between the existing and new versions before ramping up to 100 %.”** [cloud.google.com](https://cloud.google.com/deploy/docs/deployment-strategies/canary?utm_source=chatgpt.com)

  * Because this is a _critical_ vulnerability, waiting until each region’s overnight window (24 h) leaves too large an exposure window; a tight canary followed immediately by an automated rollout closes the gap quickly while still providing a safety valve.

**Why the other options are not ideal**

  * **II — update all instances at once:** fastest, but any unforeseen issue would take the whole service down simultaneously, violating high-availability principles. Google recommends staged rollouts (canary or rolling) rather than “all-at-once” for production MIGs. [cloud.google.com](https://cloud.google.com/compute/docs/release-notes?utm_source=chatgpt.com)

  * **III — 24-hour regional rolling update:** safer than II but too slow for an urgent fix; attackers could exploit the vulnerability in regions that have not yet been patched.

  * **IV — duplicate the fleet and do an A/B cut-over:** provides safety but **doubles VM cost** during the patch window and still requires a traffic switch. Google highlights canary updates as a lighter-weight alternative that meets the same safety goals without the extra spend. [cloud.google.com](https://cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups?utm_source=chatgpt.com)

In short, a brief canary rollout (option I) best balances **speed, safety, and cost** in line with Google’s recommended practices for managed instance groups.

---

## Question 59

*Domain 5: Optimizing Performance and Cost*

**Your Cloud Run-deployed application caters to users worldwide, and the goal is to configure Cloud Run to direct users to their nearest region for optimal response times. What is the recommended approach?**

- [ ] I. Deploy the application to a single region and serve it from a global anycast IP address routed behind a global external HTTP(S) load balancer.
- [x] II. Deploy the application to each region and serve it from a global anycast IP address routed behind a global external HTTP(S) load balancer.
- [ ] III. Deploy the application to one region per continent, utilizing a regional external HTTP(S) load balancer in each region, and assign the same global IP address to all regional load balancers.
- [ ] IV. Deploy the application to a single region and configure Google Cloud Armor in the frontend to permit traffic from all IP addresses.

### Explanation

**The recommended approach to configure Cloud Run to direct users to their nearest region for optimal response times is:**

**II. Deploy the application to each region and serve it from a global anycast IP address routed behind a global external HTTP(S) load balancer.**

**Explanation:**

Deploying the application to each region and serving it from a global anycast IP address routed behind a global external HTTP(S) load balancer allows users to be directed to their nearest region based on latency, ensuring optimal response times. This approach leverages Google's global network infrastructure to route traffic efficiently to the closest region, minimizing latency and improving user experience.

**Justification for why other options are not suitable:**

**I. Deploy the application to a single region and serve it from a global anycast IP address routed behind a global external HTTP(S) load balancer.**

  * This approach does not utilize the benefits of deploying the application to multiple regions to minimize latency and improve response times for users worldwide.

**III. Deploy the application to one region per continent, utilizing a regional external HTTP(S) load balancer in each region, and assign the same global IP address to all regional load balancers.**

  * While deploying the application to one region per continent can improve latency compared to a single region deployment, it may not provide the most optimal response times as users within continents may still experience latency due to regional distances.

**IV. Deploy the application to a single region and configure Google Cloud Armor in the frontend to permit traffic from all IP addresses.**

  * This approach does not optimize response times by directing users to their nearest region. Instead, it allows traffic from all IP addresses, which may not necessarily result in the best user experience in terms of latency.

**References:**

<https://cloud.google.com/run/docs/multiple-regions>

<https://cloud.google.com/run/docs/container-contract>

---

## Question 60

*Domain 3: Applying Site Reliability Engineering Practices*

**Your company relies on a legacy database hosted on Google Kubernetes Engine (GKE), which experiences significant delays in responding to Pod evictions and rescheduling. Any interruptions to the database's operation are deemed unacceptable. To ensure continuous operation, you need to select an appropriate GKE maintenance strategy. What should you do?**

- [ ] I. Set the GKE maintenance channel to "Stable".
- [ ] II. Define a node pool upgrade strategy with the max-surge-upgrade parameter set to 0.
- [ ] III. Establish a "PodDisruptionBudget" object with maxUnavailable specified as 100%.
- [x] IV. Configure a maintenance exclusion window with a scope of "No minor or node upgrades".

### Explanation

The most appropriate GKE maintenance strategy to ensure continuous operation of the legacy database hosted on Google Kubernetes Engine is:

**IV. Configure a maintenance exclusion window with a scope of "No minor or node upgrades".**

**Explanation:**

Configuring a maintenance exclusion window with a scope of "No minor or node upgrades" allows you to prevent GKE from performing any minor or node upgrades during the specified window. This ensures that no interruptions occur due to upgrades that may lead to Pod evictions and rescheduling, which could impact the database's operation. By defining this exclusion window, you can maintain continuous operation of the legacy database without the risk of disruptions caused by GKE maintenance activities.

**Justification for why other options are not suitable:**

**I. Setting the GKE maintenance channel to "Stable":**

  * Setting the maintenance channel to "Stable" provides predictability in terms of when upgrades occur, but it doesn't prevent upgrades from happening altogether. It may still lead to interruptions if upgrades occur during critical times.

**II. Defining a node pool upgrade strategy with the max-surge-upgrade parameter set to 0:**

  * While setting max-surge-upgrade to 0 ensures that no additional nodes are added during node pool upgrades, it doesn't prevent the upgrades themselves. Node pool upgrades could still result in Pod evictions and rescheduling, potentially impacting the database's operation.

**III. Establishing a "PodDisruptionBudget" object with maxUnavailable specified as 100%:**

  * Specifying maxUnavailable as 100% in a PodDisruptionBudget would effectively prevent any Pod disruptions during maintenance activities. However, it wouldn't prevent node upgrades or other maintenance tasks that could still impact the database's operation. Additionally, this approach may not align with best practices for managing Pod disruptions.

**References:**

<https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions>

<https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#scope_of_maintenance_to_exclude>

<https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels>

<https://cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters>

<https://www.youtube.com/watch?v=eqJQTANI_RI>

---

## Question 61

*Domain 2: Building and Implementing CI/CD Pipelines*

**Your organization conducts numerous builds on Google Cloud daily. To protect against data exfiltration and ensure VMs lack public IP addresses, you aim to implement Google-recommended practices to create a customizable, easily-managed solution for your builds capable of scaling to your organization's needs. What action should you take?**

- [x] A. Deploy private pools in Cloud Build with VPC service control.
- [ ] B. Configure and execute the builds in Cloud Build within a default pool to enforce necessary privacy measures.
- [ ] C. Create a build environment using Compute Engine VMs within a custom VPC, utilizing Jenkins to execute the builds.
- [ ] D. Establish a build environment using Compute Engine Spot VM instances within a custom VPC, employing Jenkins to execute the builds.

### Explanation

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

---

## Question 62

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

**Your company is gearing up for a significant sales event scheduled for September, during which a designated group of employees will support operations. To comply with Google-recommended practices, how can you provide these employees with access to Google Cloud resources for the duration of September only?**

- [ ] A. Set up a firewall rule allowing traffic from the identified employees' machines to the resources, then adjust the firewall rule to block traffic at the end of September.
- [x] B. Create a group containing the identified employees, grant the group permissions to access the resources, and configure an Identity and Access Management (IAM) condition with a date/time expression for September.
- [ ] C. Establish a group comprising the identified employees, assign the group a custom Identity and Access Management (IAM) role granting permissions to access the resources, and remove the custom role at the end of September.
- [ ] D. Allocate a custom Identity and Access Management (IAM) role, granting permissions to access the resources, to each of the identified employees. Set up a Cloud Scheduler task to revoke the custom role at the end of September.

### Explanation

The action that aligns with Google-recommended practices to provide employees with access to Google Cloud resources for the duration of September only is:

**B. Create a group containing the identified employees, grant the group permissions to access the resources, and configure an Identity and Access Management (IAM) condition with a date/time expression for September.**

**Explanation:**

Option B involves creating a group containing the identified employees and granting the group permissions to access the resources. By configuring an IAM condition with a date/time expression for September, you can ensure that the group's access is limited to the specified timeframe. This approach follows Google-recommended practices for access management by leveraging IAM conditions to enforce time-based access controls. At the end of September, access will automatically be revoked based on the IAM condition, ensuring security and compliance.

**Justification for why other options are not suitable:**

**A. Setting up a firewall rule allowing traffic from the identified employees' machines to the resources, then adjusting the firewall rule to block traffic at the end of September.**

  * Firewall rules control network traffic and are not suitable for managing access to Google Cloud resources at the IAM level. Additionally, manually adjusting firewall rules introduces complexity and potential for human error.

**C. Establishing a group comprising the identified employees, assigning the group a custom Identity and Access Management (IAM) role granting permissions to access the resources, and removing the custom role at the end of September.**

  * While this option grants access to the identified employees, it requires manual intervention to remove the custom role at the end of September. It is preferable to leverage IAM conditions for automated and more granular access control.

**D. Allocating a custom Identity and Access Management (IAM) role, granting permissions to access the resources, to each of the identified employees, and setting up a Cloud Scheduler task to revoke the custom role at the end of September.**

  * While this option automates the revocation of access at the end of September, it involves assigning custom roles to individual employees, which can be more complex to manage compared to using groups. Additionally, managing access at the individual level may not scale well for larger organizations. Using groups and IAM conditions provides a more scalable and manageable solution.

**Reference:**

<https://cloud.google.com/iam/docs/conditions-overview>

---

## Question 63

*Domain 1: Bootstrapping and Maintaining a Google Cloud Organization*

**Your company operates applications serving users located in Europe. Regulatory requirements mandate that resources be instantiated exclusively in specific regions. To ensure compliance across all projects within your Google Cloud organization, what action should you take?**

- [ ] A. Set up a log-based alert to identify resources created outside the permitted list of regions, subsequently deleting any non-compliant resources.
- [ ] B. Perform an Asset Inventory scan hourly to catalog all resources, removing any instances outside of the permitted list of regions.
- [ ] C. Designate a restricted group of users with authorization to create new instances, implementing processes to verify compliance.
- [x] D. Configure an organizational policy specifying the allowed regions within an "in: allowed_values" list.

### Explanation

The action that aligns with Google-recommended practices to ensure compliance across all projects within your Google Cloud organization regarding the instantiation of resources exclusively in specific regions is:

**D. Configure an organizational policy specifying the allowed regions within an "in: allowed_values" list.**

**Explanation:**

**Option D involves configuring an organizational policy that specifies the allowed regions within an "in: allowed_values" list. This approach allows you to define and enforce regional restrictions across all projects within your Google Cloud organization. By implementing this organizational policy, you can ensure that resources are instantiated only in the permitted regions, thus ensuring compliance with regulatory requirements. This method provides a centralized and standardized approach to enforce regional compliance across all projects.**

**Justification for why other options are not suitable:**

**A. Setting up a log-based alert to identify resources created outside the permitted list of regions, subsequently deleting any non-compliant resources**.

  * While log-based alerts can help identify non-compliant resources, relying solely on alerts for enforcement may not be sufficient. Manually deleting non-compliant resources based on alerts can also be time-consuming and error-prone.

**B. Performing an Asset Inventory scan hourly to catalog all resources, removing any instances outside of the permitted list of regions.**

  * Performing Asset Inventory scans hourly and manually removing non-compliant instances is not an efficient or scalable approach to enforce regional compliance. It may also lead to delays and inconsistencies in compliance enforcement.

**C. Designating a restricted group of users with authorization to create new instances, implementing processes to verify compliance.**

  * While restricting user access and implementing verification processes can help enforce compliance, it relies heavily on manual intervention and oversight. It may not provide a scalable or automated solution for enforcing regional compliance across all projects within the organization. Configuring organizational policies is a more robust and centralized approach to ensure compliance.

**References:**

<https://cloud.google.com/resource-manager/docs/organization-policy/defining-locations#gcloud>

<https://cloud.google.com/resource-manager/docs/organization-policy/overview>

---

## Question 64

*Domain 5: Optimizing Performance and Cost*

**Your application contains a module responsible for executing a computationally intensive task. The development team aims to optimize this module by experimenting with different algorithms. To facilitate testing, the team wants to evaluate the performance of each algorithm in both staging and production environments, gathering detailed performance data. What action should you take?**

- [x] A. Integrate the code with profiling libraries to collect detailed performance data. Visualize the data using Cloud Profiler, presenting it as flame graphs for analysis.
- [ ] B. Implement code instrumentation to track the flow of requests and responses. Analyze request latencies using Cloud Trace to assess algorithm performance.
- [ ] C. Integrate the code with log statements at various algorithmic stages. Utilize log-based notifications to capture data on algorithm execution.
- [ ] D. Embed log statements within the code at various algorithmic stages. Use log-metric-based notifications to capture data when specific control structures are invoked multiple times.

### Explanation

**The best course of action to achieve this goal is**

**A. Integrate the code with profiling libraries to collect detailed performance data. Visualize the data using Cloud Profiler, presenting it as flame graphs for analysis.**

Here's why this approach is ideal:

  * **Focused on performance:** Profiling libraries are specifically designed to gather in-depth performance metrics about code execution, such as function call times, memory usage, and CPU consumption.

  * **Cloud Profiler Integration:** Cloud Profiler seamlessly integrates with GCP, collecting profiling data from your running application in both staging and production.

  * **Visual Analysis with Flame Graphs:** Flame graphs provide an intuitive, hierarchical visualization of where the code spends the most time, making bottlenecks easily identifiable.

  * **Algorithm-Specific Insights:** Profiling allows fine-grained analysis within your algorithms, helping compare their performance characteristics.

**Why Other Options are Less Suitable:**

  * **B. Cloud Trace:** Cloud Trace is primarily for tracing distributed requests and identifying latency issues across services, less focused on algorithmic performance within a module.

  * **C & D. Log statements & notifications:** While logging can provide some information, it's less efficient and accurate than profiling for detailed performance analysis. This approach can also become overly verbose.

**References:**

<https://cloud.google.com/profiler/docs/concepts-profiling>

<https://cloud.google.com/profiler/docs/measure-app-performance>

<https://cloud.google.com/profiler/docs/concepts-flame>

<https://codelabs.developers.google.com/codelabs/otel-cloudtrace-go#0>

---

## Question 65

*Domain 2: Building and Implementing CI/CD Pipelines*

**Your code is hosted on GitHub and built using Cloud Build, both manually and via webhooks. Building the code requires accessing confidential information. To adhere to Google-recommended practices and protect the confidentiality of this information, what action should you take?**

- [ ] A. Initiate the builds from the command line each time, providing the necessary confidential information as parameters during the build process.
- [ ] B. Create an encrypted file within your GitHub repository containing only the confidential information, and reference this encrypted file within your Cloud Build configuration file.
- [x] C. Store the confidential secrets in Secret Manager, specify the URI for the secrets within the Cloud Build configuration file, and reference the secret as parameters in the build steps.
- [ ] D. Maintain the code in GitHub and establish a separate repository within Cloud Source Repositories solely for storing confidential information. Reference this new repository within your Cloud Build configuration file.

### Explanation

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

---
