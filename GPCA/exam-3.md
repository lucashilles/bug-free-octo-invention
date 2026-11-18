# Professional Cloud Architect — Practice Exam 3

65 questions.

## Question 1

*Domain 6: Ensuring Solution and Operations Excellence*

**The operations team at CloudNova Inc. has asked for your assistance in investigating a performance issue affecting a production application hosted on Google Compute Engine. Under heavy traffic, the application begins to drop incoming requests. System diagnostics reveal that one application process on each impacted instance is consuming 100% of CPU resources. The autoscaler has already reached its configured maximum instance count, and no anomalies are detected in connected systems like the database. You need to recommend a solution that will restore production traffic as quickly as possible.**

**What should you suggest?**

- [ ] A. Update the autoscaling policy to use the metric `agent.googleapis.com/memory/percent_used`.
- [ ] B. Initiate a phased restart of the impacted instances.
- [ ] C. Connect to each instance via SSH and manually restart the application process.
- [x] D. Increase the autoscaling group's maximum instance limit.

### Explanation

**Correct Answer: D. Increase the autoscaling group's maximum instance limit**

**Explanation:**

**Scenario Summary:**

- Production application is hosted on **Google Compute Engine (GCE)**.
- **Under heavy traffic**, application is **dropping requests**.
- Diagnostics show **100% CPU usage** by the application process on each instance.
- **Autoscaler has already reached its configured max instance count**.
- No anomalies in connected systems (like the database).
- Goal: **Restore traffic quickly**.

✅ **Why Option D is Correct:**

**Increasing the autoscaling group’s maximum instance limit** is the most effective way to:

- **Allow the managed instance group to scale out** further in response to CPU saturation.
- **Immediately reduce load per instance** by adding new VM instances.
- **Preserve system stability** without downtime or manual intervention.

**Google Cloud documentation states:**

“If an autoscaler reaches its maximum number of instances and your application still experiences high load, increasing the maximum limit allows autoscaler to continue scaling out.”
— Source: Compute Engine Autoscaler – Maximum number of instances

This is the **fastest and most scalable way** to handle high CPU usage caused by traffic spikes.

❌ **Why Other Options Are Incorrect:**

**A. Update the autoscaling policy to use the metric** `agent.googleapis.com/memory/percent_used`

- The bottleneck is **CPU**, not memory.
- Changing the metric to memory usage **would delay or mislead autoscaler behavior**.
- Google recommends selecting a metric that **matches the application’s resource constraint**.

**Documentation reference:**

“Choose a metric that best reflects your application's bottleneck resource.”
— Using Cloud Monitoring Metrics with Autoscaler

So, using a memory-based metric won’t address the **CPU-bound nature** of the issue.

**B. Initiate a phased restart of the impacted instances**

- Restarting instances doesn't **add more capacity**.
- It may temporarily reduce CPU usage but **disrupts traffic and service availability**.
- The issue will **likely return** when the instance restarts and receives the same load.

**Docs for VM Troubleshooting:**

“Restart instances only when they are stuck or unresponsive.”
— Troubleshooting VM Instances

Here, the instances are responsive—they’re just **overloaded**.

**C. Connect to each instance via SSH and manually restart the application process**

- This is **manual, time-consuming, and not scalable** for production systems.
- Restarting the app doesn’t resolve **excessive load** or increase capacity.
- May offer temporary relief but doesn't solve the underlying CPU saturation.

**Docs on SSH into VM instances:**

SSH is a helpful diagnostic tool, but manual restarts are not suitable for automated, scalable solutions.
— Connecting to Instances

✅ Final Recommendation:

**Increase the autoscaler’s maximum instance count** so it can continue scaling out to meet traffic demands and reduce CPU pressure.

**Documentation:**

- [Autoscaler Overview – Compute Engine](https://cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions)
- [Scaling based on load](https://cloud.google.com/compute/docs/autoscaler/scaling-load-balancing)

---

## Question 2

*Domain 1: Designing and Planning a Cloud Solution Architecture*

You are designing the infrastructure for a high-throughput web application on Google Cloud. The application must handle up to **500,000 incoming requests per second**, storing data from each request. Later, this data will be queried in **real time** using **exact-match lookups on a known set of attributes**. The application may experience **periods of inactivity**, and the business has emphasized **cost efficiency** as a priority.

Which combination of web service platform and database would best meet these requirements?

- [ ] A. Deploy the service on **Cloud Run** and store the data in **BigQuery**
- [x] B. Deploy the service on **Cloud Run** and store the data in **Cloud Bigtable**
- [ ] C. Use a **Compute Engine autoscaling managed instance group** with **BigQuery** for storage
- [ ] D. Use a **Compute Engine autoscaling managed instance group** with **Cloud Bigtable** for storage

### Explanation

✅ **Correct Answer: B. Deploy the service on Cloud Run and store the data in Cloud Bigtable**

**Detailed Analysis:**

**Requirements Summary:**

- **Very high throughput**: 500,000 requests per second
- **Each request stores data**
- **Later queried via real-time, exact-match lookups**
- **May have periods of inactivity**
- **Cost efficiency is important**

✅ **Why Option B is Correct:**

**Platform: Cloud Run**

- **Fully managed, serverless**: scales to **zero** when idle, saving costs.
- Scales **automatically and quickly** to handle very high throughput (hundreds of thousands of requests per second, per region).
- Ideal for bursty traffic patterns and cost efficiency.

**Documentation:**

- Cloud Run Scalability
  Cloud Run automatically scales out to handle high request volumes and scales to zero when not in use.

**Database: Cloud Bigtable**

- **High-performance NoSQL database**, ideal for large-scale, **low-latency workloads**.
- Supports **millions of operations per second**.
- Optimized for **real-time lookups** and **time-series data**.
- **Cost-effective** for high-throughput applications with predictable access patterns.

**Documentation:**

- Cloud Bigtable Overview
  Cloud Bigtable is ideal for applications that need very high throughput and scalability with low latency.

❌ **Why Other Options Are Incorrect:**

**A. Deploy the service on Cloud Run and store the data in BigQuery**

- **BigQuery is an analytics data warehouse**, not designed for **real-time** exact-match queries.
- Query latency is **too high** for real-time request/response use cases.
- It is **cost-optimized for analytical queries**, not operational/transactional queries.

**Docs:**

- BigQuery Use Cases
  Best for OLAP, not OLTP or real-time lookups.

**C. Use a Compute Engine autoscaling managed instance group with BigQuery for storage**

- Same issue with **BigQuery** not being suitable for **real-time lookups**.
- **Compute Engine MIGs** are less cost-efficient for bursty workloads; they **don’t scale to zero**.
- You pay for VMs even during periods of inactivity.

**Docs:**

- Compute Engine autoscaling
- BigQuery is not suitable for low-latency or transactional queries

**D. Use a Compute Engine autoscaling managed instance group with Cloud Bigtable for storage**

- **Cloud Bigtable is appropriate**, but **Compute Engine MIGs are less cost-efficient** than Cloud Run.
- They incur **overhead** in terms of management, longer scaling time, and **costs during idle periods**.
- Doesn’t take advantage of **serverless scaling and scale-to-zero** capabilities of Cloud Run.

**Docs:**

- Cloud Run vs Compute Engine Comparison

✅ Final Recommendation:

**B. Deploy the service on Cloud Run and store the data in Cloud Bigtable**

This combo provides:

- **High scalability** for request handling
- **Low latency, real-time, exact-match querying**
- **Cost efficiency** via serverless compute (scale to zero) and suitable storage backend

---

## Question 3

*Domain 2: Managing and Provisioning a Solution Infrastructure*

You are building an application composed of multiple **microservices**, which should remain **internal to the Kubernetes cluster**. Each microservice must be **independently scalable**, allowing you to configure a **specific number of replicas** per service. Additionally, other microservices should be able to **communicate with any microservice** using a **consistent address**, regardless of how many replicas it has.

You are deploying this on **Google Kubernetes Engine (GKE)**.

What is the most appropriate way to implement this?

- [x] A. Deploy each microservice as a **Deployment**, expose it using a **ClusterIP Service**, and reference it via the **Service DNS name** from other microservices.
- [ ] B. Deploy each microservice as a **Deployment**, expose it using an **Ingress**, and reference it via the **Ingress IP address** from other microservices.
- [ ] C. Deploy each microservice as a **Pod**, expose it using a **Service**, and reference it via the **Service DNS name** from other microservices.
- [ ] D. Deploy each microservice as a **Pod**, expose it using an **Ingress**, and reference it via the **Ingress IP address** from other microservices.

### Explanation

✅ **Correct Answer: A. Deploy each microservice as a Deployment, expose it using a ClusterIP Service, and reference it via the Service DNS name from other microservices.**

**Detailed Analysis**

**Given Requirements:**

- Application has **multiple microservices**.
- Microservices should be **internal to the GKE cluster** (not public-facing).
- Each microservice must be **independently scalable**.
- Other microservices should be able to communicate with any microservice via a **consistent address**, regardless of the number of replicas.

✅ **Why Option A is Correct:**

- **Deployment**: Manages replica sets, provides self-healing, and allows you to scale the number of replicas independently for each microservice.
- **ClusterIP Service**: Default type of Kubernetes service; exposes the service **internally within the cluster** only (no external IP). Perfect for internal microservice communication.
- **Service DNS name**: Kubernetes provides a **built-in DNS service** that maps a service name to its virtual IP. Microservices can reach others via `<service-name>.<namespace>.svc.cluster.local`.

This approach ensures:

- Internal-only access (**ClusterIP**).
- Scalable and self-healing microservices (**Deployment**).
- Stable communication endpoint regardless of pod replica count (**Service DNS**).

**Documentation Reference:**

- Kubernetes Services - ClusterIP
- Kubernetes DNS for Service Discovery
- Deployments in Kubernetes

❌ **Why Other Options Are Incorrect:**

**B. Deploy each microservice as a Deployment, expose it using an Ingress, and reference it via the Ingress IP address from other microservices**

- **Ingress** is intended for **external HTTP/S traffic**, not for internal microservice-to-microservice communication.
- Using Ingress for internal communication is unnecessary overhead and **against best practices**.
- Ingress requires **Layer 7 (HTTP) routing configuration**, and it’s more complex and less efficient for internal use cases.

**Docs:**

- Ingress overview

**C. Deploy each microservice as a Pod, expose it using a Service, and reference it via the Service DNS name from other microservices**

- Using **Pods directly** is incorrect because Pods are **ephemeral** (subject to restarts and rescheduling), and **do not scale or self-heal**.
- You should use **Deployments** (not standalone Pods) to manage scaling, availability, and replication.

**Docs:**

- Pods are not meant for direct deployment in production

**D. Deploy each microservice as a Pod, expose it using an Ingress, and reference it via the Ingress IP address from other microservices**

- Combines the two incorrect practices:
  - Exposing standalone **Pods** (no scalability or resilience)
  - Using **Ingress** for internal communication (adds complexity and is not appropriate)
- This would be inefficient and fragile in a microservice architecture.

✅ Final Recommendation:

**Option A** is the most appropriate design:

- Scalable microservices using **Deployments**
- Internal exposure using **ClusterIP Services**
- Stable, internal communication via **Kubernetes DNS**

---

## Question 4

*Domain 3: Designing for Security and Compliance*

Your organization has **two separate teams**: a **networking team** and an **application development team**. The development team deploys applications on **Compute Engine instances** that contain **confidential data**. They require **admin-level access** to manage Compute Engine resources.

Meanwhile, the company enforces a policy where **all networking components** must be controlled by the **networking team**. The development team wants to **ensure that the networking team cannot access sensitive instance data**.

How should you design the Google Cloud environment to meet these requirements?

- [ ] A. Create a project with its own **standalone VPC** and grant the **Network Admin** role to the networking team. Create a second project with another **standalone VPC** and grant the **Compute Admin** role to the development team. Connect both VPCs using **Cloud VPN**.
- [ ] B. Create a single project with a **standalone VPC**, and assign the **Network Admin** role to the networking team. In the same project, assign the **Compute Admin** role to the development team.
- [x] C. Create a host project with a **Shared VPC** and grant the **Network Admin** role to the networking team. Create a separate **service project** without its own VPC, attach it to the Shared VPC, and grant the **Compute Admin** role to the development team.
- [ ] D. Create a project with a **standalone VPC** and assign the **Network Admin** role to the networking team. Create another project with a separate **standalone VPC** and assign the **Compute Admin** role to the development team. Connect the two VPCs using **VPC Peering**.

### Explanation

✅ **Correct Answer: C. Create a host project with a Shared VPC and grant the Network Admin role to the networking team. Create a separate service project without its own VPC, attach it to the Shared VPC, and grant the Compute Admin role to the development team.**

**Scenario Summary:**

- Two teams:
  - **Networking Team**: manages networking resources only.
  - **Application Development Team**: manages **Compute Engine instances** that handle **confidential data**.
- **Development team needs admin access** to Compute Engine but **must not** have control over or visibility into networking configuration.
- **Networking team should not have access to instance data.**

✅ **Why Option C is Correct:**

Key Design Features:

1. **Shared VPC Architecture**:
  - **Host Project**: Owned/managed by the **networking team**, which **creates and controls** the VPC, subnets, firewall rules, etc.
  - **Service Project**: Owned/managed by the **development team**. It contains the **Compute Engine resources (VMs)** that **use the networking resources** from the host project.
2. **IAM Role Separation**:
  - **Networking Team**:
    - Granted **Network Admin** role on the **host project**.
    - Cannot access the VMs or their data in the service project.
  - **Development Team**:
    - Granted **Compute Admin** role on the **service project**.
    - Can manage VMs but **cannot modify network configuration**, which is owned by the host project.
3. **Security Boundary**:
  - This setup enforces **least privilege access** and **clear boundaries** between network and compute responsibilities.
  - Ensures that **networking team has no access** to confidential data stored on instances.

Supporting Documentation:

- Shared VPC Overview
  Shared VPC allows organization administrators to configure and centrally manage VPCs while allowing other projects to provision resources in shared networks.
- IAM Roles and Permissions for Shared VPC
  Projects attached to a Shared VPC host retain administrative independence and resource isolation.

❌ **Why Other Options Are Incorrect:**

**A. Two standalone VPCs with Cloud VPN**

- **Not efficient or secure for internal teams** within the same organization.
- **Cloud VPN** adds **unnecessary cost and complexity** for intra-org connectivity.
- Does not provide **centralized network control**, and VPCs are not centrally managed.
- Lacks **fine-grained IAM controls** across project boundaries like Shared VPC.

**B. Single project with shared roles**

- **Both teams operate in the same project** – no strong boundary between **networking and compute**.
- Even with IAM separation, the development team could potentially access networking components, **violating organizational policy**.

**D. VPC Peering between projects**

- Similar issue as A: introduces **unnecessary peering complexity**.
- VPC peering **does not support transitive routing** and doesn’t centralize control.
- **Network Admin** in one project has **no visibility or control** over another project's VPC.
- Lacks the **centralized governance** offered by Shared VPC.

✅ **Final Recommendation:**

**Use Shared VPC** with:

- **Host project**: managed by the **networking team**.
- **Service project**: used by the **development team**, isolated in terms of data.
- Role-based access ensures **security, scalability, and operational efficiency**.

Hint - [https://cloud.google.com/vpc/docs/shared-vpc](https://cloud.google.com/vpc/docs/shared-vpc)

---

## Question 5

*Domain 1: Designing and Planning a Cloud Solution Architecture*

Your company has asked you to design a **highly reliable web application** that includes a **few public APIs** as the backend. While **regular traffic is expected to be low**, there may be **occasional spikes**. You are required to use **Cloud Load Balancing**, and the solution should remain **cost-efficient for end users**.

What is the most appropriate solution?

- [ ] A. Store static content (HTML, images) in **Cloud CDN**, host the APIs on **App Engine**, and save user data in **Cloud SQL**.
- [ ] B. Store static content (HTML, images) in a **Cloud Storage bucket**, deploy the APIs to a **zonal Google Kubernetes Engine cluster** with nodes spread across multiple zones, and use **Cloud Spanner** for storing user data.
- [ ] C. Store static content (HTML, images) in **Cloud CDN**, host the APIs using **Cloud Run**, and store user data in **Cloud SQL**.
- [x] D. Store static content (HTML, images) in a **Cloud Storage bucket**, use **Cloud Functions** for hosting the APIs, and store user data in **Firestore**.

### Explanation

Correct Answer: **D**

**Store static content (HTML, images) in a Cloud Storage bucket, use Cloud Functions for hosting the APIs, and store user data in Firestore.**

Why **D** is the best solution

The question emphasizes **four key requirements**:

1. **Highly reliable**
2. **Occasional traffic spikes**
3. **Must use Cloud Load Balancing**
4. **Cost-efficient for low baseline traffic**

Option **D** aligns best with *all* of them.

1. Cost efficiency with low traffic + spikes

- **Cloud Functions** scale automatically to zero and only charge per invocation.
- No idle cost, no baseline compute.
- Ideal for *sporadic or bursty API workloads*.

Google explicitly positions Cloud Functions for this use case.
Documentation:
[https://cloud.google.com/functions/docs/concepts/overview](https://cloud.google.com/functions/docs/concepts/overview)

2. Cloud Load Balancing requirement is still met

- **External HTTP(S) Load Balancer** can front:
  - Cloud Functions
  - Cloud Run
  - Cloud Storage static content
- Static assets in **Cloud Storage** can be served directly behind the global load balancer (optionally with Cloud CDN, but not mandatory).

Documentation:
[https://cloud.google.com/load-balancing/docs/https](https://cloud.google.com/load-balancing/docs/https)

3. Firestore is the correct datastore choice

- **Firestore** is:
  - Serverless
  - Automatically replicated
  - Highly available
  - Scales transparently
- No connection pooling, no instance sizing, no regional failover management.

Using **Cloud Spanner** or even **Cloud SQL** for “user data” is unnecessary unless:

- Global strong consistency is required (Spanner)
- Complex relational joins are required (Cloud SQL)

Neither is stated in the question.

Firestore documentation:
[https://cloud.google.com/firestore/docs/overview](https://cloud.google.com/firestore/docs/overview)

4. No requirement for GKE or container orchestration

- The question **never** mentions:
  - Kubernetes
  - Container control
  - Custom networking
- Introducing **GKE** adds:
  - Cluster management overhead
  - Node costs even when idle
  - Operational complexity

This directly violates the *cost-efficient* requirement.

**Why the other options are weaker**

Option A (App Engine)

- Reliable, but **not the most cost-efficient**
- App Engine still maintains warm instances
- Inferior to Cloud Functions for low baseline traffic

App Engine scaling behavior:
[https://cloud.google.com/appengine/docs/standard/python3/how-instances-are-managed](https://cloud.google.com/appengine/docs/standard/python3/how-instances-are-managed)

Option B (GKE + Cloud Spanner)

Your criticism is 100% valid.

- **Cloud Spanner** is expensive and overkill for simple user data
- **GKE** is unnecessary without container-level requirements
- Highest operational and financial cost of all options

Cloud Spanner use cases:
https://cloud.google.com/spanner/docs/overview

Option C (Cloud Run + Cloud SQL)

- Technically valid, but **not optimal**
- Cloud SQL introduces:
  - Connection limits
  - Scaling concerns during spikes
  - Regional availability constraints
- Firestore is a better fit for serverless APIs unless relational modeling is explicitly required

Cloud SQL scaling considerations:
[https://cloud.google.com/sql/docs/mysql/instance-settings](https://cloud.google.com/sql/docs/mysql/instance-settings)

Final conclusion:

- **Firestore** is more appropriate than Cloud Spanner or Cloud SQL for generic user data.
- **Cloud Functions** meet scalability and cost goals better than App Engine or GKE.
- There is **no justification** for GKE in the problem statement.

**Correct answer: D**
Your reasoning aligns fully with Google Cloud architectural best practices.

###### Explanation

Why **D** is the best solution

The question emphasizes **four key requirements**:

1. **Highly reliable**
2. **Occasional traffic spikes**
3. **Must use Cloud Load Balancing**
4. **Cost-efficient for low baseline traffic**

Option **D** aligns best with *all* of them.

1. Cost efficiency with low traffic + spikes

- **Cloud Functions** scale automatically to zero and only charge per invocation.
- No idle cost, no baseline compute.
- Ideal for *sporadic or bursty API workloads*.

Google explicitly positions Cloud Functions for this use case.
Documentation:
[https://cloud.google.com/functions/docs/concepts/overview](https://cloud.google.com/functions/docs/concepts/overview)

2. Cloud Load Balancing requirement is still met

- **External HTTP(S) Load Balancer** can front:
  - Cloud Functions
  - Cloud Run
  - Cloud Storage static content
- Static assets in **Cloud Storage** can be served directly behind the global load balancer (optionally with Cloud CDN, but not mandatory).

Documentation:
[https://cloud.google.com/load-balancing/docs/https](https://cloud.google.com/load-balancing/docs/https)

3. Firestore is the correct datastore choice

- **Firestore** is:
  - Serverless
  - Automatically replicated
  - Highly available
  - Scales transparently
- No connection pooling, no instance sizing, no regional failover management.

Using **Cloud Spanner** or even **Cloud SQL** for “user data” is unnecessary unless:

- Global strong consistency is required (Spanner)
- Complex relational joins are required (Cloud SQL)

Neither is stated in the question.

Firestore documentation:
[https://cloud.google.com/firestore/docs/overview](https://cloud.google.com/firestore/docs/overview)

4. No requirement for GKE or container orchestration

- The question **never** mentions:
  - Kubernetes
  - Container control
  - Custom networking
- Introducing **GKE** adds:
  - Cluster management overhead
  - Node costs even when idle
  - Operational complexity

This directly violates the *cost-efficient* requirement.

> [!note]- Why the other options are wrong
> Option A (App Engine)
>
> - Reliable, but **not the most cost-efficient**
> - App Engine still maintains warm instances
> - Inferior to Cloud Functions for low baseline traffic
>
> App Engine scaling behavior:
> [https://cloud.google.com/appengine/docs/standard/python3/how-instances-are-managed](https://cloud.google.com/appengine/docs/standard/python3/how-instances-are-managed)
>
> Option B (GKE + Cloud Spanner)
>
> Your criticism is 100% valid.
>
> - **Cloud Spanner** is expensive and overkill for simple user data
> - **GKE** is unnecessary without container-level requirements
> - Highest operational and financial cost of all options
>
> Cloud Spanner use cases:
> [https://cloud.google.com/spanner/docs/overview](https://cloud.google.com/spanner/docs/overview)
>
> Option C (Cloud Run + Cloud SQL)
>
> - Technically valid, but **not optimal**
> - Cloud SQL introduces:
>   - Connection limits
>   - Scaling concerns during spikes
>   - Regional availability constraints
> - Firestore is a better fit for serverless APIs unless relational modeling is explicitly required
>
> Cloud SQL scaling considerations:
> [https://cloud.google.com/sql/docs/mysql/instance-settings](https://cloud.google.com/sql/docs/mysql/instance-settings)

---

## Question 6

*Domain 3: Designing for Security and Compliance*

Your organization routes all Google Cloud logs to **Cloud Logging**. The **security team** needs to **actively monitor these logs** and must be able to **respond quickly to anomalies**, such as **unauthorized firewall modifications** or a **potential server compromise**. You want to implement a solution that aligns with **Google-recommended best practices**.

What should you do?

- [ ] A. Use **Cloud Scheduler** to run a **cron job** every minute that queries the logs for specific security-related events.
- [ ] B. **Export logs to BigQuery** and run scheduled **queries** to analyze them for anomalies.
- [x] C. **Export logs to a Pub/Sub topic** and trigger a **Cloud Function** to process and respond to relevant log entries.
- [ ] D. **Export logs to a Cloud Storage bucket** and trigger a **Cloud Run** service when specific log events occur.

### Explanation

✅ **Correct Answer: C. Export logs to a Pub/Sub topic and trigger a Cloud Function to process and respond to relevant log entries.**

**Scenario Summary:**

- All logs are routed to **Cloud Logging**.
- The **Security team needs to actively monitor logs** for real-time security anomalies (e.g., firewall rule changes, server compromise).
- They must be able to **respond quickly**.
- Solution must follow **Google Cloud recommended best practices**.

✅ **Why Option C is Correct:**

**Real-time Monitoring via Cloud Logging + Pub/Sub + Cloud Functions:**

- **Cloud Logging** can **stream log entries to a Pub/Sub topic** using **log sinks**.
- **Pub/Sub** acts as a real-time delivery channel.
- **Cloud Functions** can be triggered on each relevant log message to:
  - Parse the entry,
  - Detect anomalies (e.g., firewall change event),
  - Take action (e.g., alert security team, revoke access, etc.).

This is a **real-time, serverless, event-driven architecture**, aligned with Google Cloud’s **Security Command Center and logging best practices**.

**Official Documentation:**

- Routing Logs with Sinks
- Real-time log monitoring with Pub/Sub
- Trigger Cloud Functions from Pub/Sub

*"To receive notifications about changes or anomalies in your logs in real time, configure a sink to route logs to Pub/Sub, and set up a Cloud Function that processes and responds to those events."*
— *Google Cloud Logging Best Practices*

❌ **Why Other Options Are Incorrect:**

**A. Use Cloud Scheduler to run a cron job every minute that queries the logs for specific security-related events**

- **Polling-based**, not **event-driven** → introduces latency.
- Doesn’t scale well or respond **immediately** to critical events.
- Not aligned with **real-time monitoring** best practices.

**Docs:** Cloud Scheduler

Not intended for real-time log processing.

**B. Export logs to BigQuery and run scheduled queries to analyze them for anomalies**

- Useful for **historical analysis and dashboards**, but **not real-time detection**.
- Scheduled queries often run **every few hours or once a day**.
- **Too slow** for high-priority alerts (like firewall rule modifications).

**Docs:** Log Export to BigQuery

For analysis, not live incident detection.

**D. Export logs to a Cloud Storage bucket and trigger a Cloud Run service when specific log events occur**

- **Cloud Storage log exports** are batch-based and intended for **archival** or **batch analysis**.
- Cannot **trigger real-time actions** like Cloud Pub/Sub.
- Cloud Run doesn’t have native support for Cloud Storage triggers (would require additional setup via Eventarc).

**Docs:** Log Export to Cloud Storage

✅ **Final Recommendation:**

**Use Pub/Sub log sinks and trigger Cloud Functions** to process and respond to security anomalies in real time.

This approach offers:

- **Real-time detection**
- **Serverless and scalable architecture**
- **Fast response to security events**
- **Google-recommended design**

Hint - [https://cloud.google.com/blog/products/management-tools/automate-your-response-to-a-cloud-logging-event](https://cloud.google.com/blog/products/management-tools/automate-your-response-to-a-cloud-logging-event)

---

## Question 7

*Domain 3: Designing for Security and Compliance*

You have launched several **Compute Engine instances** within your Google Cloud environment. Due to **security policies**, these instances **must not have public IP addresses**. There is **no existing VPN connection** between your corporate office and Google Cloud. However, you need to **SSH into one specific instance** without breaching the defined security constraints.

What is the most appropriate approach?

- [ ] A. Set up **Cloud NAT** for the subnet containing the instance, and initiate an **SSH connection to the Cloud NAT IP address** to access the instance.
- [ ] B. Add all instances to an **unmanaged instance group**, configure **TCP Proxy Load Balancing** with the group as the backend, and connect to the instance using the **TCP proxy IP address**.
- [x] C. Enable **Identity-Aware Proxy (IAP)** for the instance, ensure you have the **IAP-secured Tunnel User** role, and use the **gcloud CLI** to SSH into the instance.
- [ ] D. Deploy a **bastion host** in the same VPC network, connect to it via SSH from your office, and then use it to access the **target instance via internal SSH**.

### Explanation

✅ **Correct Answer: C. Enable Identity-Aware Proxy (IAP) for the instance, ensure you have the IAP-secured Tunnel User role, and use the gcloud CLI to SSH into the instance.**

**Scenario Summary:**

- Compute Engine instances **must not have public IP addresses** (security policy).
- **No VPN** or interconnect with on-prem network.
- You need to SSH into one instance **without violating security constraints**.

✅ **Why Option C is Correct:**

**Identity-Aware Proxy (IAP) for TCP forwarding**:

- **IAP** allows SSH access to internal (no public IP) instances **without exposing them to the internet**.
- SSH tunnels are initiated through a **Google-managed proxy**, allowing you to connect to the VM **via the gcloud CLI** using **IAP TCP forwarding**.
- Requires assigning the `roles/iap.tunnelResourceAccessor` (**IAP-secured Tunnel User**) role and setting up proper **OS Login or SSH key access**.

**Advantages:**

- **No public IP** is needed.
- No need for VPN or bastion host.
- Fully compliant with **zero-trust and security-first architectures**.

**Official Documentation:**

- IAP for TCP forwarding (SSH/RDP)
- Connect to VMs that do not have external IP addresses

*"If a VM instance does not have a public IP address, you can still connect to it by using Identity-Aware Proxy (IAP) TCP forwarding."*

❌ **Why Other Options Are Incorrect:**

**A. Set up Cloud NAT and SSH to the Cloud NAT IP**

- **Cloud NAT** is **only for egress** — it allows **VMs without public IPs** to initiate outbound internet traffic.
- It **does not support inbound connections**, including SSH.

**Docs:**

- Cloud NAT overview

*"Cloud NAT does not support incoming connections initiated from outside of your VPC network."*

**B. Configure TCP Proxy Load Balancer with an unmanaged instance group**

- **TCP Proxy Load Balancer** is meant for **TCP-based applications**, not SSH.
- Requires a **backend service** and health checks — not intended for one-off admin access like SSH.
- **Security risks**: exposes a public IP to a group of instances.

**Docs:**

- TCP Proxy Load Balancing

**D. Deploy a bastion host in the same VPC**

- Technically **valid**, but not the most **appropriate** solution here:
  - Requires provisioning a **new public-facing VM**, increasing **attack surface**.
  - Adds **operational overhead** (patching, monitoring the bastion).
  - Violates the policy of **no public IPs**, unless the bastion is specially exempted.

**Docs:**

- Best practices for bastion hosts

✅ **Final Recommendation:**

**Use Identity-Aware Proxy (IAP)** for secure, **zero-public-IP SSH access** to internal VM instances — without a VPN or bastion host.

---

## Question 8

*Domain 3: Designing for Security and Compliance*

Your organization uses **Google Cloud** and has set up two folders under its **Organization node**: one for the **Finance** department and another for the **Retail** team. The **development team members** are part of a **Google Group**, and this group has been granted the **Project Owner role at the Organization level**.

You want to ensure that **developers are restricted from creating resources** in any project located under the **Finance folder**.

What is the best way to enforce this restriction?

- [ ] A. Grant the development team group the **Project Viewer** role on the Finance folder and the **Project Owner** role on the Retail folder.
- [ ] B. Grant the development team group **only the Project Viewer** role on the Finance folder.
- [x] C. Remove the Project Owner role for the development team group from the Organization level, and assign them the **Project Owner** role only on the Retail folder.
- [ ] D. Assign the development team group the **Project Owner** role only on the Retail folder.

### Explanation

✅ **Correct Answer: C. Remove the Project Owner role for the development team group from the Organization level, and assign them the Project Owner role only on the Retail folder.**

**Scenario Summary:**

- Organization structure has **two folders** under the Organization node:
  - **Finance folder**
  - **Retail folder**
- A **Google Group (Dev Team)** has the **Project Owner** role **at the Organization level**.
- You need to **restrict developers from creating resources** in any project under the **Finance folder**.

✅ **Why Option C is Correct:**

- **Roles assigned at the Organization level** are inherited by all resources under the org, including **folders and projects**.
- So, if the **Project Owner role is granted at the Organization level**, the development group has **full control** over **all folders/projects**, including **Finance**, which violates the requirement.
- The correct action is to **remove that Organization-level role**, and instead **grant more restrictive access**:
  - Only assign **Project Owner** on the **Retail folder**.
  - No permissions assigned on the **Finance folder**, so developers **cannot create or manage resources** there.

**Google Documentation:**

- Understanding IAM hierarchy and inheritance
  "Permissions granted at higher levels of the resource hierarchy (like the organization) are inherited by lower levels (like folders and projects)."
- Best practices for using folders and resource hierarchies
  "Use folders to group resources that share the same access control policies."

❌ **Why Other Options Are Incorrect:**

**A. Grant the development team group the Project Viewer role on the Finance folder and the Project Owner role on the Retail folder**

- Assigning **Project Viewer** on the Finance folder **does not override** the **Project Owner** permission they already have from the **Organization level**.
- Because of IAM **inheritance**, they would still retain **full access** to the Finance folder unless the higher-level permission is removed.

**B. Grant the development team group only the Project Viewer role on the Finance folder**

- Similar issue as A.
- The group **already has Project Owner at the Organization level**, which **supersedes** the Viewer role.
- They’ll still have **full control** over Finance folder resources unless the higher-level role is revoked.

**D. Assign the development team group the Project Owner role only on the Retail folder**

- This **does not fix the issue** unless the existing **Organization-level Project Owner role is explicitly removed**.
- The key problem is the **broad Organization-level role**, which must be removed to limit access.

✅ **Final Recommendation:**

To ensure developers **cannot manage or create resources** under the **Finance folder**, you must:

- **Remove the Project Owner role from the Organization level**, and
- **Assign the role only at the Retail folder level**.

---

## Question 9

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

You are developing a **microservices-based application** running on **Google Kubernetes Engine (GKE)**. As part of testing, you want to **simulate a sudden failure of a specific microservice** to observe how your application responds under failure conditions.

What is the most appropriate way to simulate this scenario?

- [ ] A. Apply a **taint** to one of the Kubernetes nodes, and set a **pod anti-affinity rule** for the specific microservice, using the tainted node’s name as the label value.
- [x] B. Use **Istio’s fault injection** capability to simulate failure behavior in the target microservice.
- [ ] C. **Manually delete a node** from the Kubernetes cluster to observe how the system reacts.
- [ ] D. Use **Istio's traffic management** features to redirect traffic away from the microservice that is expected to crash.

### Explanation

✅ **Correct Answer: B. Use Istio’s fault injection capability to simulate failure behavior in the target microservice.**

**Scenario Summary:**

- You're running a **microservices-based application on GKE**.
- You want to **simulate a sudden failure** of a **specific microservice** to test the resilience of your app.
- This is part of a **controlled testing environment**, not a real outage.
- You’re aiming to **observe system behavior** (e.g., retries, fallbacks, alerting).

✅ **Why Option B is Correct:**

**Istio's Fault Injection Features:**

- Istio provides a **powerful traffic management API**, including **fault injection** capabilities.
- You can simulate:
  - **Delays** (to test timeouts)
  - **HTTP errors** (e.g., 500, 404)
  - **Abort scenarios** (to simulate microservice failure)

With Istio, you can **precisely target a microservice** and control:

- The percentage of requests affected
- The type and timing of the faults
- Specific routing conditions

This makes it the most appropriate tool for **controlled and repeatable failure injection**.

**Documentation:**

- Istio: Fault Injection

"Istio’s fault injection can be used to test the robustness of your microservices by simulating failures like HTTP errors and latency."

❌ **Why Other Options Are Incorrect:**

**A. Apply a taint and set anti-affinity rule**

- Taints and anti-affinity rules are **node scheduling mechanisms**, not failure simulation tools.
- They control **where pods run**, but **do not simulate microservice failure** or unavailability at runtime.

**Docs:**

- Taints and Tolerations
- Affinity and Anti-Affinity

**C. Manually delete a node from the Kubernetes cluster**

- Deleting a node is **disruptive and not precise**.
- It can affect **multiple workloads**, not just the target microservice.
- Not recommended for simulating a failure of a **specific service** in a controlled test.

**Docs:**

- Node lifecycle management

**D. Use Istio's traffic management to redirect traffic away**

- Redirecting traffic **avoids the microservice**, rather than simulating its **failure**.
- This tests **traffic shifting**, not **failure response**.
- Doesn’t help validate how your system handles **unexpected microservice unavailability**.

**Docs:**

- Istio Traffic Routing

✅ **Final Recommendation:**

Use **Istio's fault injection** to simulate microservice failure in a **targeted, repeatable, and safe** manner.

**⚠️ Note:** Google's managed Istio offering is now Cloud Service Mesh, which supports the same fault injection.

---

## Question 10

*Domain 1: Designing and Planning a Cloud Solution Architecture*

Your organization is building a new application that will enable **users around the world** to **upload and share photos** with selected individuals. The application must be able to **handle millions of concurrent users**. The development team wants to **focus solely on writing application code** without being responsible for provisioning or managing the underlying infrastructure.

Which Google Cloud service should you choose to **deploy the application**?

- [x] A. App Engine
- [ ] B. Cloud Endpoints
- [ ] C. Compute Engine
- [ ] D. Google Kubernetes Engine

### Explanation

✅ **Correct Answer: A. App Engine**

**Scenario Summary:**

- A **global-scale photo sharing application** with **millions of concurrent users**.
- Users can **upload and share photos**.
- Development team wants to **focus only on code**, **not infrastructure**.
- Needs **automatic scaling**, **high availability**, and **minimal operational overhead**.

✅ **Why Option A is Correct:**

**App Engine: Fully Managed Platform-as-a-Service (PaaS)**

- Allows developers to **deploy code without managing infrastructure**.
- Supports **automatic scaling** from **zero to millions** of users based on incoming traffic.
- Built-in **load balancing**, **traffic splitting**, **zero-downtime deployments**.
- Supports popular languages and frameworks (Java, Python, Go, Node.js, etc.).
- Ideal for **web applications** with variable or high traffic.

**App Engine Standard or Flexible environment**:

- Choose **Standard** for fast scale-out and cost-efficiency (especially with idle periods).
- Choose **Flexible** for custom runtime or longer request handling.

**Documentation Reference:**

- App Engine Overview

*"App Engine lets you build and host applications in the cloud, and scale automatically as your traffic grows."*

❌ **Why Other Options Are Incorrect:**

**B. Cloud Endpoints**

- Not a deployment platform.
- It's a **fully managed API gateway** to **secure and monitor APIs**.
- Used **in conjunction with backend services** like App Engine, GKE, or Cloud Run.
- Does **not support application hosting** by itself.

**Docs:** Cloud Endpoints Overview

**C. Compute Engine**

- Infrastructure-as-a-Service (IaaS) — gives full control of VM instances.
- Requires **managing provisioning, scaling, patching, monitoring**, etc.
- Not aligned with the requirement to **avoid infrastructure management**.

**Docs:** Compute Engine Overview

**D. Google Kubernetes Engine (GKE)**

- While GKE provides **powerful container orchestration**, it still requires managing **clusters**, **node pools**, and **upgrades** (even with Autopilot).
- More operational complexity compared to App Engine.
- Better suited for **complex microservices architectures** when **container-level control** is required.

**Docs:** GKE Overview

✅ **Final Recommendation:**

**App Engine** is the best choice for:

- **Massively scalable**, user-facing applications.
- **Zero infrastructure management**.
- **Developer agility** and fast time-to-market.

---

## Question 11

*Domain 5: Managing Implementation*

Your company offers a **recommendation engine** to retail clients via an **API**. Retail clients submit a **user ID** to the API and receive **personalized recommendations** in return. You are responsible for managing the **API lifecycle**, and you want to ensure that customers are not impacted by **backward-incompatible changes**. You aim to follow **Google-recommended best practices** for API stability and evolution.

What should you do?

- [ ] A. Maintain a **mailing list of all clients** and notify them at least **one month in advance** before replacing the old API with a new version that includes breaking changes.
- [ ] B. Implement an **automated CI/CD pipeline** that regenerates and publishes **API documentation** each time an update is deployed.
- [x] C. Apply an **API versioning strategy** that **increments the version number** with every **backward-incompatible change**.
- [ ] D. Use an API versioning approach where you **append “DEPRECATED”** to the current version number when introducing a breaking change, while keeping the **same version number** for the new API.

### Explanation

✅ **Correct Answer: C. Apply an API versioning strategy that increments the version number with every backward-incompatible change.**

**Scenario Summary:**

- You offer a **recommendation API** used by retail clients.
- Clients send a user ID and receive recommendations.
- You are responsible for **API lifecycle management**.
- You must **avoid breaking existing client integrations** during API updates.
- You aim to follow **Google Cloud–recommended API best practices** for **stability and evolution**.

✅ **Why Option C is Correct:**

**Use Explicit API Versioning for Breaking Changes**

- **Backward-incompatible changes** (such as removing fields, changing request/response structure, etc.) **must not impact current consumers**.
- The best practice is to:
  - **Increment the version number** (e.g., `/v1/`, `/v2/`) when introducing **breaking changes**.
  - **Keep the old version available** so existing clients are not disrupted.
  - Give clients time to **migrate** at their own pace.

**Google Recommendation:**

“Use versioning to help manage changes in your API, and **increment the version number** in the URI path or header for **breaking changes**.”
— Source: Google Cloud API Design Guide – Versioning

❌ **Why Other Options Are Incorrect:**

**A. Maintain a mailing list and notify clients about breaking changes in advance**

- **Communication is important**, but **not sufficient**.
- Clients should **not be forced to upgrade immediately** just because of an announcement.
- Breaks the principle of **API stability** if existing clients are impacted.

**B. Implement automated CI/CD to regenerate and publish API documentation**

- **Useful practice**, but this only improves **documentation quality**, not **API stability**.
- Does not prevent breaking changes from affecting clients.

**D. Append “DEPRECATED” to the version number while keeping the same version for the new API**

- This is **confusing** and **violates semantic versioning best practices**.
- You should not **reuse version identifiers** for updated/breaking versions.
- Proper versioning requires each major breaking change to have a **distinct version identifier**.

✅ **Final Recommendation:**

Use **explicit versioning** (e.g., `/v1/`, `/v2/`) to **safely evolve APIs** and **avoid disruptions** to existing clients.

This is the **standard best practice** followed by Google and other cloud providers.

---

## Question 12

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

Your organization has built a **monolithic, 3-tier application** that enables **external users to upload and share files**. The current system is **difficult to enhance** and suffers from **reliability issues**. The development team wants to **re-architect the application** using a **microservices model** and **fully managed cloud services**, but they need to **justify the value** of this shift to leadership.

Which key benefit(s) should the team emphasize to help gain leadership support?

- [ ] A. The new architecture will be **more cost-effective**, simplify **infrastructure management**, and provide **automated CI/CD pipeline management**.
- [ ] B. The current monolith can be **containerized using Docker**, and the resulting container can be deployed to a **Kubernetes cluster**.
- [x] C. The new approach will allow for **decoupling infrastructure from the application**, **faster feature development and release**, easier **CI/CD and infrastructure management**, support for **A/B testing**, and **scalability on demand**.
- [ ] D. The migration process can be **automated using Migrate for Compute Engine**.

### Explanation

✅ **Correct Answer: C. The new approach will allow for decoupling infrastructure from the application, faster feature development and release, easier CI/CD and infrastructure management, support for A/B testing, and scalability on demand.**

**Scenario Summary:**

- Organization currently runs a **monolithic 3-tier app**.
- App supports **external file uploads/sharing** but has **reliability issues** and is **hard to enhance**.
- Team proposes a **microservices-based rearchitecture** using **fully managed cloud services**.
- Leadership needs to understand the **value proposition** of this architectural shift.

✅ **Why Option C is Correct:**

**Key Benefits of Microservices and Fully Managed Services:**

1. **Decoupling of Infrastructure and Application Logic**:
  - Services can be developed and deployed independently.
  - No tight coupling to specific machines or monolithic constraints.
2. **Faster Feature Development & Release**:
  - Teams can iterate independently on different components.
  - Enables **agile development practices** and **smaller, focused deployments**.
3. **Easier CI/CD and Infrastructure Management**:
  - Fully managed services (like Cloud Run, Cloud Functions, Cloud Pub/Sub, Cloud SQL, etc.) eliminate operational overhead.
  - Better support for **automation and deployment pipelines**.
4. **Support for A/B Testing**:
  - Microservices and cloud load balancing allow **traffic splitting** for testing and gradual rollouts.
5. **Scalability on Demand**:
  - Serverless and container-based platforms scale automatically based on traffic.
  - You pay only for what you use, improving cost-efficiency.

**Official Documentation Reference:**

- Google Cloud Architecture Framework – App Modernization
- Why Microservices? – Google Cloud Architecture Center

“Microservices architectures improve agility, scalability, and reliability. They allow independent scaling and deployment of components and are well-suited to CI/CD and DevOps practices.”

❌ **Why Other Options Are Incorrect:**

**A. More cost-effective, simplify infrastructure, provide CI/CD**

- While **partially correct**, it:
  - **Overemphasizes cost** (microservices may initially **increase complexity** and cost before optimization).
  - Does not mention **key architectural benefits** like **decoupling**, **scalability**, or **faster innovation**.
  - CI/CD automation is a benefit, but **not unique** to microservices.

**B. Containerize monolith and deploy to Kubernetes**

- This is **not microservices** — it’s **“lift-and-shift”**.
- You’re still running a **monolith**, just in a container.
- It **doesn’t address** the core problems: poor reliability, slow development cycles, lack of modularity.

**D. Migrate using Migrate for Compute Engine**

- This is a **migration tool** for VMs, not a solution for **application modernization**.
- Does not help with **rearchitecting** or achieving the benefits of a **microservices-based approach**.
- Relevant only for VM-based “as-is” migrations.

✅ **Final Recommendation:**

Emphasize the **strategic technical benefits** of re-architecting to microservices using managed services:

- **Decoupling**, **agility**, **scalability**, **resilience**, **faster innovation**, and **better operational efficiency**.

---

## Question 13

*Domain 6: Ensuring Solution and Operations Excellence*

Your team is building a **web application** that will be deployed on **Google Kubernetes Engine (GKE)**. The **CTO anticipates high user traffic** at launch, potentially **tens of thousands of users**. You need to ensure that the application can **maintain acceptable latency** under this expected load.

How should you test your current deployment to validate that latency stays within an acceptable threshold?

- [x] A. Use a **load testing tool** to simulate the anticipated number of **concurrent users and requests**, then analyze the performance results.
- [ ] B. Enable **GKE cluster autoscaling** and **horizontal pod autoscaling** for your application. Use `curl` commands to send requests and verify if autoscaling responds correctly.
- [ ] C. Deploy your application across **multiple GKE clusters in all Google Cloud regions** and configure a **global HTTP(S) load balancer** with a single global IP to route traffic.
- [ ] D. Use **Cloud Debugger** in your development environment to observe **latency between microservices**.

### Explanation

✅ **Correct Answer: A. Use a load testing tool to simulate the anticipated number of concurrent users and requests, then analyze the performance results.**

**Scenario Summary:**

- You are deploying a **web application on GKE**.
- Expecting **high traffic at launch** (tens of thousands of users).
- Goal: **Ensure acceptable latency** under anticipated load.
- Need to **validate current deployment** before going live.

✅ **Why Option A is Correct:**

**Load Testing is the Industry Best Practice**

- You need to **simulate real-world traffic patterns** with the expected number of users and requests.
- Load testing tools such as **Locust**, **k6**, **Apache JMeter**, or **Gatling** allow:
  - Simulation of **concurrent users**
  - Control over **request rate**
  - Measurement of **latency**, **error rate**, **throughput**, etc.
  - Generation of **performance reports**

This helps validate:

- Whether the app can **scale under load**
- If the system **meets latency thresholds**
- How **pods, services, and GKE autoscaling** respond under pressure

**Google Recommendation:**

"Before launching your application, use load testing tools to simulate expected workloads and verify that the application performs correctly under that load."
— Google Cloud: Testing application scalability

❌ **Why Other Options Are Incorrect:**

**B. Enable autoscaling and use `curl` to send requests**

- `curl` is **not a suitable load testing tool**.
- It simulates a **very small number of requests** and cannot replicate **tens of thousands of concurrent users**.
- Autoscaling should be part of the testing strategy, but you need a **proper load generator** to validate latency under real traffic.

**C. Deploy across multiple GKE clusters globally**

- This is a **scalability and availability strategy**, not a **testing method**.
- Global deployment helps with **geo-latency reduction**, but it does **not test or validate** latency under load.
- You must validate latency **before** global rollout using **controlled load testing**.

**D. Use Cloud Debugger to observe latency**

- Cloud Debugger is used to **inspect application state without stopping it**, typically for **debugging during development**.
- It does **not simulate traffic** or measure **request latency under load**.
- Not suitable for **performance testing**.

**Docs:** Cloud Debugger

✅ **Final Recommendation:**

Use a **load testing tool** to simulate anticipated traffic levels and measure latency. This is the most accurate and scalable way to validate system behavior before launch.

**⚠️ Note:** Cloud Debugger was shut down in 2023.

---

## Question 14

*Domain 2: Managing and Provisioning a Solution Infrastructure*

Your organization has deployed a **Kubernetes application** that **pulls messages from Pub/Sub** and stores them in **Filestore**. Since the application is relatively simple, it was originally deployed as a **single pod**. However, the infrastructure team has reviewed **Pub/Sub metrics** and found that the application is **not keeping up with real-time message processing**—many messages are delayed by several minutes before being handled. The application’s workload is **I/O-intensive**, and you need to **scale the processing layer** to address the performance issue.

What should you do?

- [ ] A. Run the command: `kubectl autoscale deployment APP_NAME --max 6 --min 2 --cpu-percent 50` to configure **horizontal pod autoscaling based on CPU usage**.
- [ ] B. Set up **Kubernetes autoscaling** using the `subscription/push_request_latencies` metric from Pub/Sub.
- [ ] C. Use the `--enable-autoscaling` flag when creating the **GKE cluster** to automatically enable cluster-level autoscaling.
- [x] D. Configure **Kubernetes autoscaling** based on the `subscription/num_undelivered_messages` metric from Pub/Sub

### Explanation

✅ **Correct Answer: D. Configure Kubernetes autoscaling based on the `subscription/num_undelivered_messages` metric from Pub/Sub.**

**Scenario Summary:**

- Application running on **Kubernetes** pulls messages from **Pub/Sub** and writes to **Filestore**.
- It's **I/O-intensive**, and **currently underperforms** — Pub/Sub shows **message processing delays**.
- The goal is to **scale the processing layer effectively** based on actual workload (Pub/Sub backlog).
- CPU is **not the bottleneck** — **Pub/Sub backlog is**.

✅ **Why Option D is Correct:**

**Custom Metric-Based Autoscaling with Pub/Sub Backlog:**

- Kubernetes **Horizontal Pod Autoscaler (HPA)** can use **custom metrics** via the **Custom Metrics API**.
- You can configure HPA to **scale pods** based on **Pub/Sub backlog size** (`subscription/num_undelivered_messages`), which is a direct indicator of processing demand.
- This ensures scaling is aligned with **actual message load**, not CPU usage (which might not correlate well with I/O workloads).

**Metric Explanation:**

- `subscription/num_undelivered_messages`:
  *The number of unprocessed messages in the Pub/Sub subscription backlog.*
- When this value increases, it indicates **your app isn’t keeping up**, and **more pods should be added**.

**Official Documentation:**

- Google Cloud – Custom metrics for autoscaling
- GKE – Autoscale based on custom metrics

❌ **Why Other Options Are Incorrect:**

**A. Use `kubectl autoscale` based on CPU usage**

- CPU-based autoscaling is **not appropriate for I/O-bound workloads**.
- Pub/Sub backlog growth is **not necessarily tied to CPU usage**, especially if processing is **disk or network-bound**.

**B. Use autoscaling based on** `subscription/push_request_latencies`

- This metric reflects **Pub/Sub push latency**, not pull subscriber backlog.
- Your app uses **pull**, and the relevant metric is **backlog size**, not delivery latency.
- Also, this metric doesn't directly map to **how many pods you need** to process the load.

**C. Enable cluster-level autoscaling with** `--enable-autoscaling`

- Cluster autoscaler scales **node count**, not **pod count**.
- You still need a correctly configured **HPA** that uses **the right metric**.
- Cluster autoscaler works **with** HPA but does not replace the need for **proper scaling logic** based on message backlog.

✅ **Final Recommendation:**

Configure **HPA to scale your Kubernetes deployment** based on **Pub/Sub** `subscription/num_undelivered_messages` — this gives the **most accurate and workload-specific autoscaling behavior**.

---

## Question 15

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

Your organization is building a **web-based application**, and you need to ensure that **production deployments can be traced back to specific source code commits**. This traceability should support **full auditability** of what code was deployed and when.

What is the most effective approach to achieve this?

- [ ] A. Require developers to **tag each commit** with the **date and time** of the commit.
- [ ] B. Instruct developers to **include a comment in each commit** that references the corresponding **deployment**.
- [x] C. Ensure the **container image tag** matches the **source code commit hash**.
- [ ] D. Have developers **tag all commits** with the **label “latest”**.

### Explanation

✅ **Correct Answer: C. Ensure the container image tag matches the source code commit hash.**

**Scenario Summary:**

- You are building a **web-based application**.
- You must ensure **production deployments can be traced** to the **exact source code commit**.
- This is required to support **full auditability** of what code was deployed and **when**.

✅ **Why Option C is Correct:**

**Tagging container images with Git commit hashes is an industry best practice**:

- When you **build and deploy a container image**, tag it with the **corresponding Git commit hash** (e.g., `gcr.io/my-project/my-app:abc1234`).
- This approach provides:
  - **Immutable traceability** between deployed artifact and source code.
  - **Auditability** — you can inspect production containers and immediately know **which version of the code** is running.
  - Supports **repeatable deployments**, rollbacks, and debugging.

**Google Cloud Best Practices:**

"Tagging container images with the commit SHA (e.g. git commit hash) ensures that every deployment is traceable to the exact source code version used."
— Google Cloud: Deploying containers – best practices

**Also supported by tools like:**

- **Cloud Build**, **Cloud Deploy**, **Cloud Run**, **GKE**
- CI/CD pipelines often inject the commit SHA and use it as an image tag automatically.

❌ **Why Other Options Are Incorrect:**

**A. Require developers to tag each commit with the date and time of the commit**

- Git already records **timestamped metadata** for every commit.
- Manual tagging introduces **human error**, inconsistency, and **is not reliable for deployments**.

**B. Instruct developers to include a comment in each commit that references the corresponding deployment**

- Comments are **non-enforceable and non-unique**.
- You cannot reliably associate deployments with code.
- It’s backwards — you want the deployment to **reference the commit**, not the other way around.

**D. Have developers tag all commits with the label “latest”**

- The tag `"latest"` is **ambiguous** and **mutable**.
- It **overwrites previous versions**, which makes it **impossible to audit** what version of code was deployed.
- Using `"latest"` in production is a **well-known anti-pattern**.

✅ **Final Recommendation:**

**Tag container images with the Git commit hash** to ensure **strong traceability**, **auditability**, and **clarity** in your production deployment process.

---

## Question 16

*Domain 1: Designing and Planning a Cloud Solution Architecture*

A **development team** is seeking your guidance. They plan to build and deploy an **HTTP(S) API** using **Go 1.12**. The workload for this API is expected to be **highly unpredictable**, and the system must maintain **reliability during traffic spikes**. They also want to **minimize operational overhead** and infrastructure management.

Which solution should you recommend?

- [ ] A. Containerize the application and deploy it on **Google Kubernetes Engine (GKE)**.
- [x] B. Build the application for the **App Engine standard environment**.
- [ ] C. Deploy the application to **Compute Engine** using a **Managed Instance Group (MIG)**.
- [ ] D. Build the application for the **App Engine flexible environment** using a **custom runtime**.

### Explanation

✅ **Correct Answer: B. Build the application for the App Engine standard environment.**

**Scenario Summary:**

- Building an **HTTP(S) API using Go 1.12**
- **Workload is highly unpredictable**, with potential **traffic spikes**
- Requires **reliability under varying load**
- Team wants to **minimize operational overhead** and **infrastructure management**

✅ **Why Option B is Correct:**

**App Engine Standard Environment**

- **Fully managed serverless platform**: no need to manage infrastructure, VMs, or scaling.
- **Supports Go 1.12 natively** in the **standard environment**, which is optimized for fast startup and scale-to-zero.
- Automatically **scales out during traffic spikes** and **scales in to zero** during idle times, reducing cost.
- Offers **reliability and autoscaling** out-of-the-box without manual tuning or cluster management.

**Google Documentation Reference:**

- App Engine Standard Environment for Go

"App Engine automatically scales your application in response to the amount of traffic it receives. It also handles load balancing and microservices architecture by default."

- App Engine Scalability

"The standard environment is designed to scale up quickly and down to zero when not in use."

❌ **Why Other Options Are Incorrect:**

**A. Containerize the application and deploy it on GKE**

- GKE offers flexibility and control but **requires managing clusters, node pools, and upgrades**.
- Not optimal for teams aiming to **minimize operational overhead**.
- GKE is **more complex and costlier** to maintain for unpredictable, bursty workloads compared to App Engine standard.

**C. Deploy to Compute Engine using a Managed Instance Group (MIG)**

- MIGs offer autoscaling, but require **infrastructure management**, instance template creation, and **manual handling of VM images**.
- **Slower scaling** compared to serverless platforms.
- Higher **ops overhead**, not aligned with the goal of **minimizing infrastructure management**.

**D. App Engine Flexible Environment with custom runtime**

- App Engine Flexible provides more flexibility (e.g., custom runtimes), but:
  - Comes with **more operational overhead**.
  - **Does not scale to zero** (minimum one instance always running).
  - **Slower to scale up/down** than standard environment.
- Overkill for a Go 1.12 app, since **Go is natively supported in App Engine Standard**.

✅ **Final Recommendation:**

**App Engine Standard Environment** is the **best fit** for:

- Natively supported Go 1.12 apps
- **Bursty and unpredictable traffic**
- Teams seeking **low operational overhead**
- **Serverless auto-scaling** with fast startup and **cost efficiency**

---

## Question 17

*Domain 1: Designing and Planning a Cloud Solution Architecture*

Your organization is designing a **data lake architecture on Google Cloud** to support various **data ingestion pipelines** that collect **unstructured data** from multiple sources. After the data is ingested, it will be used in **several processing pipelines** to build a **recommendation engine** for website users.

The **structure of the incoming data may change at any time**, and it is crucial to **store the data exactly as received** so it can be **reprocessed later** if the current pipelines fail to handle the structural changes.

What is the best architectural approach for storing the ingested data to meet this requirement?

- [ ] A. Process the data first through the pipeline, then store the **processed data** in **BigQuery** for future reprocessing.
- [ ] B. Store the **raw data directly in BigQuery**, and have the processing pipelines read from the BigQuery table.
- [ ] C. Process the data through the pipeline first, then store the **processed output** in a **Cloud Storage bucket** for reprocessing.
- [x] D. Store the **raw unprocessed data** in a **Cloud Storage bucket**, and design the processing pipelines to read from that bucket.

### Explanation

✅ **Correct Answer: D. Store the raw unprocessed data in a Cloud Storage bucket, and design the processing pipelines to read from that bucket.**

**Scenario Summary:**

- Designing a **data lake architecture** on **Google Cloud**.
- Multiple ingestion pipelines collect **unstructured data** from various sources.
- Incoming data structures **may change at any time**.
- It's **crucial to store data exactly as received** to allow **reprocessing later**, especially if the pipelines fail due to schema changes.
- Data will feed into **processing pipelines** to build a **recommendation engine**.

✅ **Why Option D is Correct:**

**Cloud Storage as Raw Data Landing Zone (Data Lake Ingestion Layer):**

- **Cloud Storage** is the recommended solution for storing **raw, unstructured, and semi-structured data** in data lakes.
- It allows you to:
  - **Store data in its original form** (without enforcing schema).
  - Enable **schema-on-read** — meaning pipelines can interpret data format **at processing time**, not ingestion.
  - **Reprocess data** anytime from the raw source if the structure changes or new processing logic is needed.
- Highly durable, scalable, and cost-effective for storing large volumes of data.

**Google Cloud Best Practice:**

“Cloud Storage is a good choice for storing raw data because it preserves the original structure, supports schema evolution, and enables batch or streaming processing with services like Dataflow or Dataproc.”
— Google Cloud: Building a data lake on GCP

❌ **Why Other Options Are Incorrect:**

**A. Process the data first through the pipeline, then store the processed data in BigQuery**

- Violates the requirement to **store the data exactly as received**.
- You lose **raw source fidelity** after processing.
- If pipeline fails due to structural change, **original data is lost** or **hard to reprocess**.

**B. Store the raw data directly in BigQuery**

- BigQuery enforces **schemas**, which are difficult to manage with **frequently changing or unstructured data**.
- Not suitable for direct storage of **unstructured or semi-structured raw data**.
- Best used for **processed and queryable data**, not raw ingestion.

**Docs:** When to use Cloud Storage vs BigQuery

**C. Process the data through the pipeline first, then store the processed output in Cloud Storage**

- Similar to option A — if you process data first, you may lose **original format**.
- Defeats the requirement of storing the **raw, unaltered** data for future reprocessing.

✅ **Final Recommendation:**

Use **Cloud Storage to store raw unprocessed data** immediately after ingestion.
Then let downstream processing pipelines (e.g., using **Dataflow**, **Dataproc**, **Cloud Functions**, etc.) **read from that bucket**, ensuring **reliability, flexibility**, and **reprocessability**.

---

## Question 18

*Domain 3: Designing for Security and Compliance*

You are managing your organization's **Google Cloud environment**, where **multiple departments** require access to their own set of projects. Within each department, **team members will share the same responsibilities** across their projects. You want to **minimize administrative overhead** while maintaining a **clear view of IAM permissions**, especially as projects are created and decommissioned over time. You aim to follow **Google-recommended best practices**.

What should you do?

- [ ] A. **Individually assign IAM permissions** to all department members for each of their respective projects.
- [x] B. **Create a Google Group** for each department and add relevant members to their group. Then, create a **folder per department**, assign the required IAM roles to the group **at the folder level**, and place department projects under the appropriate folder.
- [ ] C. Create a **folder per department** and assign the required IAM permissions **directly to the individual department members** at the folder level. Add each department's projects under its folder.
- [ ] D. Create a **Google Group** for each department and add department members. Then, assign IAM permissions **to the group on a per-project basis** for each of their respective projects.

### Explanation

✅ **Correct Answer: B. Create a Google Group for each department and add relevant members to their group. Then, create a folder per department, assign the required IAM roles to the group at the folder level, and place department projects under the appropriate folder.**

**Scenario Overview:**

- Multiple departments, each managing their own projects in **Google Cloud**.
- **Department members share common roles** across their projects.
- Projects are **created and decommissioned regularly**.
- Goal:
  - **Minimize administrative overhead**
  - **Maintain clear IAM visibility**
  - **Align with Google Cloud best practices**

✅ **Why Option B is Correct:**

**Google Cloud Best Practices Alignment:**

1. **Use Google Groups for IAM:**
  - Groups allow centralized management of access.
  - Adding/removing members doesn’t require changes to IAM policies.
  - Supports **auditability** and **access consistency**.
2. **Use Folders to Structure Resources:**
  - Organize resources by **department, team, or business unit**.
  - **IAM roles inherited** from the folder to all projects under it.
  - When a **new project is created under a folder**, **IAM roles are automatically applied**, minimizing manual IAM configuration.
3. **Assign IAM at the Folder Level:**
  - Reduces redundancy (you avoid repetitive per-project permissions).
  - Easier to **audit and manage** access as a single policy controls multiple projects.

**Documentation Reference:**

- Google Cloud Resource Hierarchy
- Best practices for using folders

"You can assign IAM roles at the folder level to apply to all projects within the folder, simplifying permission management."

- Best Practices for IAM

"Use Google Groups to manage access instead of adding users individually."

❌ **Why Other Options Are Incorrect:**

**A. Individually assign IAM permissions per project**

- **High maintenance** and error-prone.
- Difficult to manage as the number of projects and users grows.
- **Not scalable** and hard to audit.

**C. Assign IAM directly to individuals at folder level**

- Better than project-level roles but still **not scalable**.
- You’d need to **update IAM policies** every time a team member joins or leaves.
- Violates best practice of using **Google Groups** for access management.

**D. Use groups but assign IAM per project**

- Using groups is good, but assigning IAM **per project** increases operational overhead.
- Every new project needs a **manual IAM configuration**, which defeats the goal of **minimal administration**.

✅ **Final Recommendation:**

- Create a **Google Group per department**
- Create a **folder per department**
- Assign IAM roles **at the folder level to the group**
- Add all related projects **under the folder**

This provides a **scalable**, **auditable**, and **low-maintenance** IAM strategy aligned with **Google Cloud best practices**.

---

## Question 19

*Domain 3: Designing for Security and Compliance*

Your company has an application deployed as a **Kubernetes Deployment** running in **Google Kubernetes Engine (GKE)**. You maintain **separate clusters for development, staging, and production** environments.

Recently, you discovered that the team is able to **deploy Docker images directly to the production cluster** without first deploying and testing them in the **development** and **staging** environments.

While you want to maintain the team’s **deployment autonomy**, you also want to **enforce proper promotion flow** to prevent this issue from recurring. You are looking for a **Google Cloud-native solution** that can be implemented **quickly with minimal operational overhead**.

What should you do?

- [ ] A. Set up a **Kubernetes lifecycle hook** to block the container from starting unless it is approved for use in the specific environment.
- [ ] B. Enforce a **company policy** requiring that images must be tested in lower environments before deployment to production.
- [x] C. Use **Binary Authorization policies** for the development, staging, and production clusters, and configure **attestations** in the CI pipeline.
- [ ] D. Develop a **Kubernetes admission controller** that blocks containers from starting unless they have been approved for the respective environment.

### Explanation

✅ **Correct Answer: C. Use Binary Authorization policies for the development, staging, and production clusters, and configure attestations in the CI pipeline.**

**Scenario Summary:**

- Application runs on **GKE** using **Kubernetes Deployments**.
- You have **separate clusters** for **dev**, **staging**, and **prod**.
- Issue: teams can **bypass dev/staging** and **deploy directly to production**.
- Goal: enforce a **promotion flow** (dev → staging → prod).
- You want a **Google Cloud-native solution** with **minimal operational overhead** and **retained deployment autonomy**.

✅ **Why Option C is Correct:**

**Binary Authorization:**

- **Binary Authorization** is a **Google Cloud-native** security feature that:
  - **Prevents unauthorized container images** from being deployed to GKE.
  - Enforces **deploy-time policies** using **attestations** and **signers**.
- You can define **different policies per environment** (e.g., dev, staging, prod).
- **Attestations** can be generated automatically in the **CI/CD pipeline**, confirming that:
  - The image passed required tests,
  - It was promoted through dev and staging before reaching production.

**How it Works:**

1. CI builds image and runs tests.
2. If tests pass in **dev**, the CI system generates an **attestation** (a cryptographically signed statement).
3. Staging CI pipeline does the same.
4. Production Binary Authorization policy is configured to **require attestations** from both dev and staging environments before allowing deployment.

**Benefits:**

- Enforces **promotion flow** without manual intervention.
- **Prevents unauthorized deployments** to production.
- Fully **integrated with GKE and Cloud Build**.
- Minimal operational overhead once configured.

**Documentation References:**

- Binary Authorization Overview
- Set up Binary Authorization with GKE

❌ **Why Other Options Are Incorrect:**

**A. Kubernetes lifecycle hook to block container start**

- Lifecycle hooks (**e.g., preStart**) are meant for **application-level initialization**, not for **enforcing deployment policies**.
- They **run inside the pod**, which is **too late** — the image is already deployed and running.
- Not intended for security enforcement or environment validation.

**B. Company policy requiring testing in lower environments**

- While governance policies are important, this is a **manual, unenforceable measure**.
- **No technical control** — still allows bypassing the process.
- Not a reliable solution to prevent production misuse.

**D. Custom Kubernetes admission controller**

- Admission controllers can enforce policies, but writing and maintaining a **custom controller** is **complex and high overhead**.
- You'd have to **build, deploy, and manage** the controller yourself.
- Not a **quick or Google Cloud-native** solution.

✅ **Final Recommendation:**

**Use Binary Authorization** to enforce image promotion flow across **dev → staging → prod** by requiring **attestations** before allowing deployments.

This is the **most secure**, **scalable**, and **Google Cloud-aligned** solution with **minimal operational burden.**

Ref - [https://cloud.google.com/binary-authorization/docs/overview#policy_model](https://cloud.google.com/binary-authorization/docs/overview#policy_model)

---

## Question 20

*Domain 5: Managing Implementation*

Your organization is planning to **migrate a 10 TB database export** from its **on-premises environment to Cloud Storage**. You need to **minimize transfer time**, **reduce overall cost**, and **limit the load on the source database** during the migration. The available **bandwidth between the on-prem environment and Google Cloud is 1 Gbps**. You aim to follow **Google-recommended best practices** for this type of data transfer.

What is the most appropriate solution?

- [ ] A. Build a **Dataflow pipeline** that reads data directly from the source database and writes it to **Cloud Storage**.
- [ ] B. Use the **Transfer Appliance** to perform an **offline migration** of the data to Cloud Storage.
- [ ] C. Use a **third-party ETL tool** to extract data from the on-prem database and upload it to Cloud Storage.
- [x] D. **Compress the export files** and use `gsutil -m` to upload the data to Cloud Storage using **multi-threaded transfers**.

### Explanation

**Correct answer: D. Compress the export files and use `gsutil -m` to upload the data to Cloud Storage using multi-threaded transfers.**

For a **10 TB database export** with **1 Gbps bandwidth**, Google-recommended practice is to use an **online transfer** when the available bandwidth is sufficient to meet the migration timeline. At 1 Gbps, 10 TB is large but still practical to transfer online. Google’s migration guidance says that with reasonable network connectivity, even **100 TB at 1 Gbps** can be transferred online in a little over 10 days, and Transfer Appliance is mainly recommended when bandwidth is not enough or cannot be acquired in time.

Option D is best because:

- The data is already a **database export**, so the source database does not need to be continuously queried during transfer.
- Compression reduces the amount of data sent over the network.
- `gsutil -m` enables parallel/multi-threaded transfer behavior, reducing overall upload time.
- It avoids the cost and logistics of ordering, receiving, loading, shipping, and ingesting a Transfer Appliance.

Google’s current documentation mentions `gcloud storage` as the preferred command-line tool for small-to-medium on-premises transfers, but older PCA-style questions often use `gsutil -m` for the same concept: parallelized command-line upload to Cloud Storage. Google Cloud documentation also states that command-line Cloud Storage copy operations can perform parallel multi-threaded/multi-processing copies where appropriate.

**Why the other options are not the best choice**

A. **Incorrect.** Dataflow is not appropriate here because the data is already exported. Reading directly from the source database would increase database load, which violates the requirement to limit source database impact.

B. **Incorrect.** Transfer Appliance is useful for very large offline transfers or when network bandwidth is insufficient. Here, 10 TB over 1 Gbps is feasible online, and Transfer Appliance adds hardware, shipping, and operational overhead. Google’s guidance positions Transfer Appliance for cases where bandwidth is limited or not enough to meet the deadline.

C. **Incorrect.** A third-party ETL tool would add cost and complexity. It may also read directly from the database, increasing database load. There is no transformation requirement here, only movement of an existing export.

**Need-to-know foundational concept**

For PCA exam scenarios, choose **Transfer Appliance** when the data volume is very large and network transfer is impractical. For a manageable export such as **10 TB with 1 Gbps bandwidth**, use compressed files and a parallel command-line transfer to Cloud Storage.

###### Explanation

**Correct answer: D. Compress the export files and use `gsutil -m` to upload the data to Cloud Storage using multi-threaded transfers.**

For a **10 TB database export** with **1 Gbps bandwidth**, Google-recommended practice is to use an **online transfer** when the available bandwidth is sufficient to meet the migration timeline. At 1 Gbps, 10 TB is large but still practical to transfer online. Google’s migration guidance says that with reasonable network connectivity, even **100 TB at 1 Gbps** can be transferred online in a little over 10 days, and Transfer Appliance is mainly recommended when bandwidth is not enough or cannot be acquired in time.

Option D is best because:

- The data is already a **database export**, so the source database does not need to be continuously queried during transfer.
- Compression reduces the amount of data sent over the network.
- `gsutil -m` enables parallel/multi-threaded transfer behavior, reducing overall upload time.
- It avoids the cost and logistics of ordering, receiving, loading, shipping, and ingesting a Transfer Appliance.

Google’s current documentation mentions `gcloud storage` as the preferred command-line tool for small-to-medium on-premises transfers, but older PCA-style questions often use `gsutil -m` for the same concept: parallelized command-line upload to Cloud Storage. Google Cloud documentation also states that command-line Cloud Storage copy operations can perform parallel multi-threaded/multi-processing copies where appropriate.

> [!note]- Why the other options are wrong
> A. **Incorrect.** Dataflow is not appropriate here because the data is already exported. Reading directly from the source database would increase database load, which violates the requirement to limit source database impact.
>
> B. **Incorrect.** Transfer Appliance is useful for very large offline transfers or when network bandwidth is insufficient. Here, 10 TB over 1 Gbps is feasible online, and Transfer Appliance adds hardware, shipping, and operational overhead. Google’s guidance positions Transfer Appliance for cases where bandwidth is limited or not enough to meet the deadline.
>
> C. **Incorrect.** A third-party ETL tool would add cost and complexity. It may also read directly from the database, increasing database load. There is no transformation requirement here, only movement of an existing export.

---

## Question 21

*Domain 1: Designing and Planning a Cloud Solution Architecture*

TechNova Inc. has an enterprise-grade application deployed on Google Compute Engine that demands both high availability and high performance. The application is set up in an active-passive configuration across two virtual machine instances located in separate zones within the same region. It stores data on a persistent disk. In the event of a zone failure, the data must be instantly accessible by the instance in the other zone. You are tasked with optimizing performance while minimizing both downtime and potential data loss.

**What should you do to meet these requirements?**

- [ ] A. Attach a persistent SSD disk to the active instance. Schedule hourly snapshots of the disk. If a zone becomes unavailable, recreate the persistent SSD disk from the latest snapshot and attach it to the standby instance.
- [ ] B. Create a Cloud Storage bucket. Mount it on the active instance using gcsfuse. If a zone outage occurs, mount the same Cloud Storage bucket on the passive instance using gcsfuse.
- [x] C. Attach a **regional SSD persistent disk** to the active instance. In case of a zone failure, **force-attach** the regional disk to the passive instance in the other zone.
- [ ] D. Attach a **local SSD** to the active instance. Use rsync every hour to copy data to a persistent SSD disk attached to the passive instance. If a zone outage occurs, switch operations to the passive instance.

### Explanation

The **correct option is: C**

**1. Attach a regional SSD persistent disk to the active instance.**
**2. In case of a zone failure, force-attach the regional disk to the passive instance in the other zone.**

Justification for Correct Option (C):

- A **regional persistent disk** is designed for **high availability** and **zonal redundancy**. It replicates data **synchronously** between two zones in the same region.
- This ensures that if one zone goes down, **data is immediately available** in the other zone without needing to restore from a snapshot or sync manually.
- The **SSD variant** provides **high performance**, fulfilling the performance requirement.
- You can **force-attach** a regional disk to the standby instance during a failure scenario, allowing the passive instance to take over quickly with minimal downtime or data loss.

**Reference:**
**Google Cloud documentation on regional persistent disks:**
[https://cloud.google.com/compute/docs/disks#regionalpersistentdisk](https://cloud.google.com/compute/docs/disks#regionalpersistentdisk)

**Why the other options are not suitable:**

A.

1. Attach a persistent SSD disk to the active instance.
2. Schedule hourly snapshots of the disk.
3. If a zone becomes unavailable, recreate the persistent SSD disk from the latest snapshot and attach it to the standby instance.

- **Issue**: Standard persistent disks are **zonal** and do not offer cross-zone availability.
- **Snapshots** are **asynchronous** and taken **periodically**, so data can be **lost** between snapshot intervals (e.g., up to an hour of data).
- Recreating a disk from a snapshot introduces **downtime** and is **not instantaneous**.

**Reference:**
[https://cloud.google.com/compute/docs/disks/snapshots#how_snapshots_work](https://cloud.google.com/compute/docs/disks/snapshots#how_snapshots_work)

B.

1. Create a Cloud Storage bucket.
2. Mount it using `gcsfuse`.
3. Mount the same bucket on the passive instance during failover.

- **Issue**: Cloud Storage is **object storage**, not block storage. It's **not suitable** for applications requiring high IOPS or low-latency disk access.
- `gcsfuse` is **not recommended** for production workloads requiring high performance and low latency.
- This approach **violates performance requirements** and may have consistency issues.

**Reference:**
[https://cloud.google.com/storage/docs/gcs-fuse](https://cloud.google.com/storage/docs/gcs-fuse)

*"gcsfuse is not recommended for latency-sensitive or high-throughput applications."*

D.

1. Attach a local SSD to the active instance.
2. Use `rsync` every hour to copy to a persistent disk on passive instance.
3. Switch over on failure.

- **Issue**: **Local SSDs are ephemeral** – their data is lost when the VM is stopped or crashes.
- **rsync** is manual and interval-based, leading to **potential data loss** and **delayed failover**.
- Also, this setup increases operational complexity and does **not guarantee high availability**.

**Reference:**
[https://cloud.google.com/compute/docs/disks/local-ssd](https://cloud.google.com/compute/docs/disks/local-ssd)

*"Local SSDs are ephemeral and data does not persist when the instance is stopped or deleted."*

Final Answer: **C**

Because it ensures **high availability**, **zonal redundancy**, and **low-latency performance**, all with **minimal operational overhead** and **instant failover capability**.

---

## Question 22

*Domain 3: Designing for Security and Compliance*

At CloudLogic Solutions, you're designing a data warehouse solution on Google Cloud. The plan involves storing sensitive information in BigQuery. Your organization enforces a policy requiring that encryption keys must be generated externally and not within Google Cloud.

**Which solution should you implement to meet this requirement?**

- [ ] A. Generate a new key in Cloud Key Management Service (Cloud KMS). Store all data in Cloud Storage using the **customer-managed key** option, selecting the newly created key. Then, use a Dataflow pipeline to decrypt the data and load it into a new BigQuery dataset.
- [ ] B. Generate a new key in Cloud KMS. Create a new dataset in BigQuery using the **customer-managed key** option and select the generated key.
- [x] C. Import an externally generated key into Cloud KMS. Store all data in Cloud Storage using the **customer-managed key** option and select the imported key. Then, use a Dataflow pipeline to decrypt the data and load it into BigQuery.
- [ ] D. Import an externally generated key into Cloud KMS. Create a BigQuery dataset using the **customer-supplied key** option and choose the imported key.

### Explanation

**The correct option is:**
**C. Import an externally generated key into Cloud KMS. Store all data in Cloud Storage using the customer-managed key option and select the imported key. Then, use a Dataflow pipeline to decrypt the data and load it into BigQuery.**

Justification for Correct Option (C):

- The key requirement is that **encryption keys must be generated externally** — outside of Google Cloud.
- Google Cloud allows importing externally generated keys into **Cloud KMS**, using a process called **External Key Management (EKM)** or **imported keys** for **Cloud KMS**.
- Once the key is imported into **Cloud KMS**, it becomes a **customer-managed key (CMEK)**, which can be used for services like Cloud Storage.
- BigQuery does **not** support customer-supplied keys (CSEK), so option D is impossible. Among the options given, C is the only one that uses an externally generated key:
  - You **store encrypted data in Cloud Storage** using the externally imported key.
  - Then, use **Dataflow to decrypt** the data with the imported key and load it into BigQuery.
  - BigQuery will then use its own encryption (default or CMEK if acceptable), but you’ve ensured the sensitive data **was encrypted with an externally generated key before entering BigQuery**.

**Reference:**

- Importing external keys into Cloud KMS
- BigQuery CMEK limitations
- Dataflow and CMEK

**Why Other Options Are Incorrect:**

A.

Generate a new key in Cloud KMS...

- **Incorrect** because it states the key is **generated in Cloud KMS**, violating the requirement that keys must be **generated externally**.

B.

Generate a new key in Cloud KMS and use it as a CMEK for BigQuery...

- **Incorrect** for the same reason as above — the key is **generated within Google Cloud**, not externally.
- BigQuery has no CSEK option at all.

D.

Import an externally generated key and use it as a customer-supplied key in BigQuery...

- **Incorrect** because **BigQuery does not support Customer-Supplied Encryption Keys (CSEK)**.
- BigQuery only supports Google-managed keys or CMEK.

**Reference:**

- BigQuery does **not support CSEK**: [https://cloud.google.com/bigquery/docs/customer-managed-encryption#limitations](https://cloud.google.com/bigquery/docs/customer-managed-encryption#limitations)

**Final Answer: C**

This is the only solution that:

- Uses **externally generated keys**.
- **Encrypts sensitive data before it enters BigQuery**.
- Leverages **Cloud Storage + Dataflow** to enforce encryption control.

**⚠️ Note:** An imported key is an ordinary Cloud KMS key, and BigQuery CMEK accepts any Cloud KMS key, so in practice you would import the key and set it as the dataset's CMEK directly. That option isn't offered here, so C remains the best of the four.

---

## Question 23

*Domain 3: Designing for Security and Compliance*

At DataSecure Corp., sensitive information is stored in a Google Cloud Storage bucket. Due to regulatory compliance requirements, the organization must be able to **rotate the encryption key** used to protect the data stored in that bucket. The data will later be processed using Google Cloud Dataproc. You aim to follow **Google-recommended best practices for security**.

**What should you do to meet these requirements?**

- [ ] A. Create a key using **Cloud Key Management Service (Cloud KMS)**. Use the `encrypt` method of Cloud KMS to manually encrypt the data before uploading it.
- [x] B. Create a key using **Cloud Key Management Service (Cloud KMS)**. Assign this key as the **default encryption key** for the Cloud Storage bucket.
- [ ] C. Generate a **GPG key pair**. Encrypt the data using this GPG key, then upload the encrypted data to the Cloud Storage bucket.
- [ ] D. Generate a **custom AES-256 encryption key**. Encrypt the data in the Cloud Storage bucket using the **customer-supplied encryption key (CSEK)** feature.

### Explanation

The correct answer is:
**B. Create a key using Cloud Key Management Service (Cloud KMS). Assign this key as the default encryption key for the Cloud Storage bucket.**

Justification for Correct Option (B):

- **Cloud KMS** allows you to create **Customer-Managed Encryption Keys (CMEK)** that can be used with Google Cloud Storage.
- Assigning a **CMEK as the default encryption key** for a bucket ensures that all newly uploaded objects are automatically encrypted using this key.
- **Key rotation** is supported and **managed via Cloud KMS**, making it easier to meet **regulatory compliance** and **security best practices**.
- This approach is **fully integrated with Google Cloud services like Dataproc**, so when data is accessed or processed, the CMEK-protected data can be decrypted securely.

**Google-recommended best practices** include using **CMEK** over CSEK or manual encryption for production workloads requiring compliance and auditability.

**Official Documentation:**

- Using customer-managed encryption keys (CMEK) with Cloud Storage
- Key rotation with Cloud KMS

**Why Other Options Are Incorrect:**

A.

Create a key using Cloud KMS. Use the encrypt method of Cloud KMS to manually encrypt the data before uploading it.

- This involves **manual encryption**, which is **not scalable** and **not recommended** for production or compliance-heavy environments.
- It complicates integration with other GCP services like Dataproc.
- Also lacks native support for **automatic key rotation and access management**.

**Reference:**

- Manual encryption is possible but not recommended for managing encrypted data at scale:
  [https://cloud.google.com/kms/docs/encrypt-decrypt](https://cloud.google.com/kms/docs/encrypt-decrypt)

C.

Generate a GPG key pair. Encrypt the data using this GPG key, then upload the encrypted data to the Cloud Storage bucket.

- GPG keys are **not natively integrated** with Google Cloud services.
- **Manual encryption** with GPG makes **key rotation, auditability, and access control** more complex and error-prone.
- This approach **doesn’t meet Google’s best practices** for cloud-native data protection.

D.

Generate a custom AES-256 encryption key. Encrypt the data using the CSEK feature.

- **Customer-Supplied Encryption Keys (CSEK)** are supported but **not recommended** for most use cases.
- CSEK does **not support automatic key rotation**, and you are fully responsible for key lifecycle and availability.
- **Google does not retain** a copy of CSEKs, which means that data can be **permanently lost** if the key is lost.

**Reference:**

- [https://cloud.google.com/storage/docs/encryption/customer-supplied-keys](https://cloud.google.com/storage/docs/encryption/customer-supplied-keys)
- [https://cloud.google.com/security/encryption/default-encryption#choose_encryption](https://cloud.google.com/security/encryption/default-encryption#choose_encryption)

Final Answer: **B**

It enables secure, compliant encryption with **key rotation**, **audit logging**, and **tight IAM control**, following **Google Cloud's recommended best practices** for managing sensitive data at scale.

---

## Question 24

*Domain 2: Managing and Provisioning a Solution Infrastructure*

At NetCore Labs, your team is preparing to deploy a newly developed application on **Google Kubernetes Engine (GKE)**. This application needs to interact with external third-party services over the internet. However, your organization's security policy **prohibits assigning public IP addresses** to any **Compute Engine** instances in your environment.

**What deployment strategy should you use to meet these requirements while aligning with best practices?**

- [x] A. Set up a **private GKE cluster**, and configure a **Cloud NAT Gateway** for the subnet used by the cluster.
- [ ] B. Set up a **private GKE cluster**, and enable **Private Google Access** on the associated **Virtual Private Cloud (VPC)** network.
- [ ] C. Deploy a **route-based GKE cluster**, and enable **Private Google Access** on the associated VPC.
- [ ] D. Provision a **Compute Engine instance** to run a custom **NAT proxy**, and configure all GKE workloads to route traffic through this instance to access third-party services.

### Explanation

The correct answer is:
**A. Set up a private GKE cluster, and configure a Cloud NAT Gateway for the subnet used by the cluster.**

✅ Justification for Correct Option (A):

- **Private GKE clusters** do not assign public IP addresses to nodes, aligning perfectly with the security policy that **prohibits public IPs**.
- However, for workloads in the cluster to **access the internet** (e.g., third-party APIs), they need **egress access**.
- The recommended and **secure** approach for enabling internet access **without assigning public IPs** is to use **Cloud NAT**.
- **Cloud NAT (Network Address Translation)** allows resources in a **private subnet** (like GKE nodes) to initiate **outbound connections** to the internet **without needing external IPs**.

**Official Documentation:**

- Using Cloud NAT with GKE
- Cloud NAT overview

❌ Why Other Options Are Incorrect:

B.

Set up a private GKE cluster, and enable Private Google Access on the associated VPC.

- **Private Google Access** allows access to **Google APIs and services**, **not** arbitrary **third-party internet services**.
- Since the requirement involves connecting to **external third-party services**, Private Google Access alone **does not meet the need**.

**Reference:**

- Private Google Access

C.

Deploy a route-based GKE cluster, and enable Private Google Access on the associated VPC.

- This option is also **incorrect** because:
  - **Private Google Access only allows access to Google APIs**.
  - **Route-based GKE** isn’t relevant here and does not solve the egress internet connectivity issue without public IPs.

D.

Provision a Compute Engine instance to run a custom NAT proxy...

- While **technically feasible**, running a **custom NAT proxy** introduces **management complexity**, **scalability challenges**, and **availability risks**.
- **Google Cloud recommends using Cloud NAT** instead of custom-built solutions for **managed, secure, and highly available** NAT functionality.

**Reference:**

- Cloud NAT best practices

✅ Final Answer: **A**

Use a **private GKE cluster with Cloud NAT**, which is a **Google-recommended solution** for enabling **secure outbound internet access** from **private nodes**, ensuring **compliance with the organization's policy**.

Link - [https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#private-nodes-outbound](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#private-nodes-outbound)

---

## Question 25

*Domain 2: Managing and Provisioning a Solution Infrastructure*

TechAxis Inc. runs a support ticketing system hosted on **App Engine Standard Environment**. The Google Cloud project hosting the App Engine app is already connected to the company's **on-premises network** via a **Cloud VPN tunnel**, and a **Virtual Private Cloud (VPC)** is fully set up.

The App Engine application must now be able to **connect to a database hosted in the on-premises environment**.

**What should you do to enable this connectivity?**

- [ ] A. Enable **Private Google Access for on-premises hosts only**.
- [ ] B. Enable **Private Google Access**.
- [ ] C. Configure **Private Services Access**.
- [x] D. Configure **Serverless VPC Access**.

### Explanation

The correct answer is:
**D. Configure Serverless VPC Access.**

✅ Justification for Correct Option (D):

- The application is running on **App Engine Standard Environment**, which is a **serverless** platform.
- To allow **serverless apps** (such as App Engine Standard, Cloud Functions, or Cloud Run) to connect to resources in a **VPC network**, including **on-premises resources connected via Cloud VPN**, you must configure **Serverless VPC Access**.
- **Serverless VPC Access connectors** allow serverless environments to **communicate with internal IPs** in the VPC, which includes the **Cloud VPN tunnel** and **on-premises systems**.

**Official Documentation:**

- App Engine Standard → Serverless VPC Access
- Serverless VPC Access Overview

❌ Why the Other Options Are Incorrect:

A.

Enable Private Google Access for on-premises hosts only.

- This setting allows **on-premises systems** to access **Google APIs** using **Private Google Access**, but it **does not allow App Engine** to access on-prem systems.
- This is **not related** to App Engine accessing the on-prem database.

**Reference:**

- Private Google Access for on-premises hosts

B.

Enable Private Google Access.

- This enables **VMs without external IPs** in the VPC to access **Google APIs**, but it **does not allow outbound access** from **App Engine Standard** to **on-prem resources**.
- Again, **not applicable** for serverless-to-on-prem connectivity.

C.

Configure Private Services Access.

- Private Services Access is used to **connect to managed services**, like **Cloud SQL or Filestore**, over internal IP.
- It is **not used** for accessing **on-premises databases** or **establishing serverless access** to VPC networks.

**Reference:**

- Private Services Access overview

✅ Final Answer: **D. Configure Serverless VPC Access.**

It is the **only correct and supported method** for enabling **App Engine Standard Environment** to communicate with **on-premises systems** via **Cloud VPN and VPC**.

---

## Question 26

*Domain 5: Managing Implementation*

At CloudOps Solutions, your team is preparing to upload a collection of critical files to **Google Cloud Storage**. After the upload completes, they want to ensure that the data in the cloud is **exactly the same** as the original files stored **on-premises**. The solution should **minimize both cost and effort** during the validation process.

**What should you do to achieve this?**

- [ ] A. Use the shasum command on Linux to generate checksums for the local files. Upload the files to Cloud Storage using gsutil -m. Download the uploaded files using gsutil cp. Run shasum again on the downloaded files. Compare the two sets of hashes.
- [ ] B. Upload the files to Cloud Storage using gsutil -m. Write a custom Java program to generate **CRC32C** hashes for the local files. Use gsutil ls -L gs://[YOUR_BUCKET_NAME] to retrieve the CRC32C hashes of the uploaded files. Compare the hashes.
- [ ] C. Upload all files using gsutil -m. Download the uploaded files using gsutil cp. Use the diff command on Linux to compare the content of the downloaded files with the originals.
- [x] D. Upload the files using gsutil -m. Use gsutil hash -c FILE_NAME to generate **CRC32C** hashes for the local files. Use gsutil ls -L gs://[YOUR_BUCKET_NAME] to retrieve the **CRC32C** hashes of the uploaded files. Compare the hashes.

### Explanation

The correct answer is:
**D.**

1. Upload the files using `gsutil -m`.
2. Use `gsutil hash -c FILE_NAME` to generate **CRC32C hashes** for the local files.
3. Use `gsutil ls -L gs://[YOUR_BUCKET_NAME]` to retrieve the **CRC32C hashes** of the uploaded files.
4. Compare the hashes.

**Justification for Correct Option (D):**

- **Google Cloud Storage** automatically calculates a **CRC32C checksum** for every uploaded object.
- You can use `gsutil hash -c` on your **original local files** to generate CRC32C hashes in the same format used by GCS.
- Use `gsutil ls -L` to fetch metadata of the uploaded objects, which includes the **CRC32C value**.
- By comparing both CRC32C values, you can **verify data integrity** efficiently **without re-downloading the files**, which is both **cost-effective and fast**.

This is a **Google-recommended method** for validating uploaded files.

**Official Documentation:**

- gsutil hash command
- gsutil ls -L for metadata including CRC32C
- Using CRC32C for integrity checking

**Why the Other Options Are Incorrect:**

**A.**

Uses `shasum` to generate hashes before and after upload.

- While SHA-1 provides a way to verify integrity, **Google Cloud Storage does not store SHA-1 hashes**.
- So, to verify integrity, this option **requires downloading the files again**, which **adds cost and effort** — violating the requirement to **minimize cost and effort**.

B.

Use a custom Java program to generate CRC32C, and compare with GCS.

- While CRC32C is the correct hash, writing a **custom Java program** adds **unnecessary complexity and effort**.
- This approach is **less efficient** than using the built-in `gsutil hash -c`.

C.

Upload, then re-download the files and use `diff`.

- This involves **downloading all files again**, which increases **network and egress costs**, especially for large datasets.
- It also adds significant **manual effort** and **processing time**.

Final Answer: **D**

Because it uses **built-in GCS tools**, leverages **matching checksum algorithms (CRC32C)**, and avoids **extra data transfers**, aligning with the goals of **minimal cost and effort** while ensuring **high confidence in data integrity**.

**Ref** - [https://cloud.google.com/storage/docs/gsutil/commands/hash](https://cloud.google.com/storage/docs/gsutil/commands/hash)

---

## Question 27

*Domain 6: Ensuring Solution and Operations Excellence*

At DevSphere Inc., you’ve deployed a new application using **Anthos clusters (formerly Anthos GKE)**. As per your organization’s **Site Reliability Engineering (SRE)** practices, you are required to receive alerts if the **request latency** exceeds a defined threshold for a specific duration.

**What should you do to implement this requirement?**

- [x] A. Install **Anthos Service Mesh** on your cluster. Use the **Google Cloud Console** to define a **Service Level Objective (SLO)**, and create an alerting policy based on the SLO.
- [ ] B. Enable the **Cloud Trace API** in your project, and configure **Cloud Monitoring Alerts** to trigger based on latency metrics from Cloud Trace.
- [ ] C. Use **Cloud Profiler** to monitor request latency. Define a custom metric in **Cloud Monitoring** using Profiler data, and set up an alerting policy that triggers if the threshold is exceeded.
- [ ] D. Set up **Anthos Config Management** on your cluster, and define an SLO and alerting policy using a YAML file that gets deployed to the cluster.

### Explanation

The correct answer is:
**A. Install Anthos Service Mesh on your cluster. Use the Google Cloud Console to define a Service Level Objective (SLO), and create an alerting policy based on the SLO.**

Justification for Correct Option (A):

- **Anthos Service Mesh (ASM)**, based on **Istio**, provides **observability features** including request latency, error rates, and availability metrics.
- ASM integrates with **Cloud Monitoring** and **Cloud Logging**, enabling you to define **Service Level Objectives (SLOs)** directly via the **Google Cloud Console**.
- You can then create **alerting policies** based on these SLOs to notify the team when **latency exceeds a predefined threshold** over a defined time window.
- This approach directly aligns with **SRE practices** for **proactive monitoring** and **reliability engineering**.

**Official Documentation:**

- Anthos Service Mesh Observability
- Create SLOs and alerting policies
- Create SLOs in Cloud Console

**Why Other Options Are Incorrect:**

B.

Enable the Cloud Trace API and configure Cloud Monitoring Alerts on latency metrics.

- While **Cloud Trace** provides **latency details**, it is not designed for **alerting** based on latency thresholds over time.
- Trace is **sampling-based**, so it **may not catch all high-latency requests**, making it unsuitable for **reliable SLO-based alerting**.

**Reference:**

- Cloud Trace Overview

C.

Use Cloud Profiler to monitor latency and define custom metrics.

- **Cloud Profiler** is used for **analyzing application performance at the code level** (CPU, heap usage) — **not request latency** or request-level observability.
- It does not emit latency metrics for creating **request-based alerting policies**.

**Reference:**

- Cloud Profiler Overview

D.

Use Anthos Config Management and define an SLO via YAML.

- **Anthos Config Management (ACM)** is used to enforce **policy-as-code**, config sync, and **RBAC controls**, not for defining SLOs or alerts.
- SLOs and alerts are configured via **Cloud Monitoring or the Cloud Console**, not ACM YAML manifests.

**Reference:**

- Anthos Config Management Overview

Final Answer: **A**

Because it uses **Anthos Service Mesh**, which provides **native observability**, **SLO definitions**, and **alerting integration** aligned with SRE best practices.

Link - [https://cloud.google.com/service-mesh/docs/observability/slo-overview](https://cloud.google.com/service-mesh/docs/observability/slo-overview)

**⚠️ Note:** Anthos clusters are now GKE Enterprise, Anthos Service Mesh is now Cloud Service Mesh, and Anthos Config Management is now Config Sync + Policy Controller.

---

## Question 28

*Domain 1: Designing and Planning a Cloud Solution Architecture*

At **CalcNet Solutions**, your team manages a **stateless web API** that performs scientific computations. This API is currently hosted on a **Google Kubernetes Engine (GKE)** cluster located in the `us-central1` region. The company now wants to **expand access to customers in Asia**, with a key objective of **reducing latency** for users in that region.

**Which action should you take to best meet this requirement?**

- [ ] A. Provision a second GKE cluster in `asia-southeast1`, expose both clusters using **Service of type LoadBalancer**, and add the **public IPs** to the **Cloud DNS** zone.
- [ ] B. Use a **global HTTP(S) load balancer** with **Cloud CDN** enabled.
- [x] C. Deploy a second GKE cluster in `asia-southeast1`, and use **kubemci** to configure a **global HTTP(S) load balancer**.
- [ ] D. Increase the **CPU and memory resources** allocated to the application running in the existing cluster.

### Explanation

The correct answer is:
**C. Deploy a second GKE cluster in asia-southeast1, and use kubemci to configure a global HTTP(S) load balancer.**

✅ Justification for Correct Option (C):

- **Latency reduction** for users in **Asia** requires hosting the application **closer to those users**, which means provisioning infrastructure in an **Asia-based region** like `asia-southeast1`.
- Deploying a **second GKE cluster** in `asia-southeast1` ensures users are served from the **nearest location**, improving response times.
- **kubemci** (Kubernetes Multi-Cluster Ingress) allows you to set up a **single global HTTP(S) load balancer** that can distribute traffic **based on proximity and availability** to **multiple GKE clusters** across regions.
- This setup provides **low-latency**, **high availability**, and **global routing**, aligning with Google Cloud’s **multi-cluster best practices**.

**Official Documentation:**

- Setting up multi-cluster Ingress with kubemci
- Global Load Balancing with GKE
- Best practices for serving global traffic

❌ Why Other Options Are Incorrect:

A.

Provision a second GKE cluster and expose both with type LoadBalancer, adding IPs to Cloud DNS.

- This results in **static IP-based routing**, which doesn’t support **automatic proximity-based traffic routing**.
- DNS-based load balancing is **less effective**, especially with **global user distribution**, and may not always serve the closest endpoint.

B.

Use a global HTTP(S) load balancer with Cloud CDN enabled.

- While Cloud CDN helps **cache static content**, it does **not help for dynamic content** (like scientific computations).
- Also, if only one backend (the us-central1 cluster) is deployed, the latency for Asian users would still be high.
- You need **regional presence** for latency reduction, which this option lacks.

D.

Increase CPU/memory in the current cluster.

- This may improve **performance under load**, but it does **not reduce geographic latency** for Asia-based users.
- The physical distance still creates unavoidable round-trip latency.

✅ Final Answer: **C**

Because it ensures **low-latency**, **geo-aware routing**, and **multi-region high availability** using **global load balancing** with **multi-cluster GKE deployments**, which is **best practice** for global applications.

Link - [https://cloud.google.com/blog/products/gcp/how-to-deploy-geographically-distributed-services-on-kubernetes-engine-with-kubemci](https://cloud.google.com/blog/products/gcp/how-to-deploy-geographically-distributed-services-on-kubernetes-engine-with-kubemci)

**⚠️ Note:** kubemci is deprecated. The current way to put one global load balancer in front of clusters in several regions is **Multi Cluster Ingress** or the multi-cluster **Gateway** API.

---

## Question 29

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

At **VirtuScale Technologies**, you're migrating several **third-party applications** from **performance-optimized on-premises virtual machines** to **Google Cloud**. These applications show **consistent usage patterns** over multiple weeks, but you're uncertain about the ideal **CPU and memory configurations** in the cloud. Your goal is to **optimize resource usage** while **minimizing costs**.

**What should you do to achieve this?**

- [ ] A. Create an **instance template** with the smallest available machine type, using an image of the application from your on-premises VM. Then, set up a **managed instance group** that autoscales based on **average CPU utilization**, and adjust the utilization threshold to optimize the instance count.
- [ ] B. Deploy the application in an **App Engine flexible environment** using a **Dockerfile** and custom runtime. Define **CPU and memory settings** similar to the on-prem VM in the `app.yaml` file.
- [ ] C. Provision **multiple Compute Engine instances** with various CPU and memory settings. Install the **Cloud Monitoring agent**, deploy the application on each, run **high-traffic load tests**, and use the results to determine the most suitable configuration.
- [x] D. Launch a **Compute Engine instance** with CPU and memory settings similar to your on-prem setup. Install the **Cloud Monitoring agent**, deploy the application, perform **normal-traffic load testing**, and follow **Rightsizing Recommendations** in the **Cloud Console**.

### Explanation

The correct answer is:
**D. Launch a Compute Engine instance with CPU and memory settings similar to your on-prem setup. Install the Cloud Monitoring agent, deploy the application, perform normal-traffic load testing, and follow Rightsizing Recommendations in the Cloud Console.**

✅ Justification for Correct Option (D):

- **Rightsizing Recommendations** in Google Cloud help optimize your VM usage based on **actual performance metrics** collected over time.
- By deploying your application with **initially estimated resources** (e.g., from your on-prem setup) and monitoring it under **real-world traffic**, you can collect **accurate usage data** using the **Cloud Monitoring agent**.
- Google Cloud then analyzes CPU and memory utilization and provides **customized recommendations** for scaling up or down to **reduce costs without impacting performance**.

This approach is **cost-effective**, **accurate**, and aligned with **Google Cloud best practices** for optimizing resource utilization.

**Official Documentation:**

- Compute Engine Rightsizing Recommendations
- Installing the Monitoring Agent

❌ Why Other Options Are Incorrect:

A.

Use the smallest machine type in an instance group with autoscaling based on CPU.

- **Incorrect** because:
  - Autoscaling is suitable for **horizontal scaling** and stateless applications, not for right-sizing individual VM **vertical resource allocation**.
  - Starting with the **smallest machine type** may lead to **performance bottlenecks** and **false autoscaling triggers**.
  - This approach does not help determine **ideal per-VM CPU/memory configuration**.

B.

Deploy to App Engine flexible environment with Dockerfile and on-prem settings.

- **App Engine flexible environment** is good for certain web apps, but not always suitable for **third-party VM-based applications**, especially those with complex dependencies.
- This method **does not help optimize** CPU/memory utilization — it just **replicates on-prem settings** without performance insight.

C.

Provision multiple instance types and run high-traffic load tests to choose the best.

- This is **labor-intensive, costly, and inefficient**.
- Running full-scale **load tests on multiple instance types** manually does not scale and wastes time/resources.
- Google Cloud’s **built-in rightsizing tools** already automate and optimize this process using actual workload patterns.

✅ Final Answer: **D**

It provides an **efficient, data-driven approach** to identifying the **most cost-effective and performance-optimized configuration** using **built-in Google Cloud tooling and monitoring**.

- Link -[https://cloud.google.com/migrate/compute-engine/docs/4.9/concepts/planning-a-migration/cloud-instance-rightsizing?hl=en](https://cloud.google.com/migrate/compute-engine/docs/4.9/concepts/planning-a-migration/cloud-instance-rightsizing?hl=en)

---

## Question 30

*Domain 3: Designing for Security and Compliance*

At **DataShield Analytics**, your team manages a **Google Cloud project** that utilizes **BigQuery** as the central data warehouse. A **Cloud VPN tunnel** connects your on-premises infrastructure with Google Cloud. To enhance data security, the **security team** wants to **prevent data exfiltration** caused by **malicious insiders**, **compromised code**, or **accidental oversharing**.

**What should you do to best meet these security requirements?**

- [ ] A. Enable **Private Google Access** for on-premises traffic only.
- [ ] B. Take the following actions: Create a **service account**. Assign the **BigQuery JobUser** and **Storage Object Viewer** roles to that service account. **Revoke all other IAM access** to the project.
- [x] C. Implement **VPC Service Controls** and enable **Private Google Access**.
- [ ] D. Enable **Private Google Access**.

### Explanation

The correct answer is:
**C. Implement VPC Service Controls and enable Private Google Access.**

✅ Justification for Correct Option (C):

To **prevent data exfiltration** from BigQuery and other Google-managed services, the best and **Google-recommended solution** is to implement:

- **VPC Service Controls**, which create a **security perimeter** around sensitive services like **BigQuery**, **Cloud Storage**, etc., and
- **Private Google Access**, which allows access to Google APIs **without traversing the public internet**, ensuring internal-only traffic routing.

Together, these two controls:

- Restrict **unauthorized or untrusted networks or code** from accessing or leaking data.
- Prevent access to BigQuery from outside the defined **perimeter (such as external networks, compromised VMs, or cloud functions)**.
- Enforce **context-aware access** and restrict services by **source network**, **user identity**, and **device attributes**.

**Official Documentation:**

- VPC Service Controls Overview
- Best practices for securing BigQuery
- Private Google Access

❌ Why Other Options Are Incorrect:

A.

Enable Private Google Access for on-premises traffic only.

- This only allows **on-prem systems to reach Google APIs** using internal IPs but does **not restrict access from other locations** or prevent **exfiltration**.
- It does **not create a security perimeter**, so **malicious insiders or compromised cloud services** can still access/export data.

B.

Create a service account with limited roles and revoke other IAM access.

- Limiting IAM permissions is **necessary** but **not sufficient**.
- IAM alone cannot **prevent data exfiltration** if the authorized identity is **compromised**.
- It lacks **network-level protection**, which is why **VPC Service Controls** are required.

D.

Enable Private Google Access.

- While this ensures Google APIs can be accessed from VMs **without public IPs**, it does **not provide any data exfiltration protection** or security perimeter by itself.

✅ Final Answer: **C**

Because it provides **defense-in-depth** against **data exfiltration**, combining **network-level restrictions (VPC Service Controls)** and **secure access paths (Private Google Access)** — which is aligned with **Google Cloud security best practices**.

**Link-** [https://cloud.google.com/vpc-service-controls/docs/overview#benefits](https://cloud.google.com/vpc-service-controls/docs/overview#benefits)

---

## Question 31

*Domain 2: Managing and Provisioning a Solution Infrastructure*

You are working at **MediCore Institute**, an organization that processes **sensitive medical data**. As part of your cloud migration strategy, you are moving multiple workloads to **Google Cloud**. Due to strict **compliance requirements**, all workloads must run on **physically isolated hardware**, and **workloads from different clients must be completely separated**.

You have created a **sole-tenant node group** and assigned a **dedicated node for each client**. Now, you need to ensure that each workload is deployed to the appropriate dedicated host.

**What should you do to meet these requirements?**

- [ ] A.Attach the **node group name** as a **network tag** when creating **Compute Engine instances** so that each workload is hosted on the correct node group.
- [ ] B.Attach the **node name** as a **network tag** when creating Compute Engine instances to ensure each workload is deployed to the correct node.
- [ ] C. Use **node affinity labels** referencing the **node group name** when creating Compute Engine instances to schedule workloads on the appropriate node group.
- [x] D. Use **node affinity labels** referencing the **node name** when creating Compute Engine instances to schedule each workload on its designated node.

### Explanation

The correct answer is:
**D. Use node affinity labels referencing the node name when creating Compute Engine instances to schedule each workload on its designated node.**

✅ Justification for Correct Option (D):

- **Sole-tenant nodes** provide **physically isolated hardware** for running sensitive workloads, which is essential for **compliance** in industries like healthcare.
- To schedule workloads on a **specific sole-tenant node**, you must use **node affinity labels**, referencing the **exact node name**.
- This ensures that a specific workload is placed on its **designated, physically isolated node**, guaranteeing **strict client separation**.

**Node affinity** is the mechanism used by Google Cloud to control **VM placement** on sole-tenant nodes.

**Official Documentation:**

- Placing VMs on sole-tenant nodes using node affinity
- Node affinity reference

❌ Why Other Options Are Incorrect:

A.

Attach the node group name as a network tag when creating Compute Engine instances.

- **Network tags** are used for **firewall rules and network configurations**, not for **VM placement on nodes**.
- They **do not influence** how Compute Engine schedules VMs on sole-tenant nodes.

B.

Attach the node name as a network tag when creating Compute Engine instances.

- Again, **network tags do not control VM placement** on nodes.
- They are unrelated to **sole-tenant node scheduling**.

C.

Use node affinity labels referencing the node group name.

- This references a **group of nodes**, not a specific one.
- Since the requirement is **strict client isolation**, placing a workload on **any node in a group** would **not ensure that isolation**.
- Only referencing the **specific node name** ensures a workload is tied to a particular dedicated host.

✅ Final Answer: **D**

Because it uses **node affinity with specific node names**, ensuring **compliance with physical isolation requirements** and **strict workload separation** per client, which is essential in handling **sensitive medical data**.

Ref- [https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes#default_affinity_labels](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes#default_affinity_labels)

---

## Question 32

*Domain 1: Designing and Planning a Cloud Solution Architecture*

At **TechVeritas Inc.**, the testing framework is a **custom C++ application** that executes a full suite of tests throughout the day on **Linux virtual machines**. Running the complete test suite takes several hours and currently relies on a small pool of **on-premises servers dedicated to testing**.

The company now wants to **move the testing infrastructure to Google Cloud** in order to **significantly reduce the total test execution time**, while making **minimal changes** to the existing tests.

**Which cloud infrastructure should you recommend?**

- [ ] A.Use **Google Compute Engine unmanaged instance groups** with a **Network Load Balancer**.
- [x] B.Use **Google Compute Engine managed instance groups** with **auto-scaling** to dynamically provision test VMs.
- [ ] C.Use **Google Cloud Dataproc** to run the tests as **Apache Hadoop** jobs for distributed processing.
- [ ] D.Use **Google App Engine** and configure **Cloud Logging (formerly Stackdriver)** for test monitoring.

### Explanation

The correct answer is:
**B. Use Google Compute Engine managed instance groups with auto-scaling to dynamically provision test VMs.**

- ✅ Justification for Correct Option (B):
  - **Google Compute Engine (GCE)** supports **Linux virtual machines**, making it compatible with the existing **C++ test framework** with **minimal changes**.
  - **Managed Instance Groups (MIGs)** allow you to **dynamically scale** the number of VMs up or down based on demand (e.g., time of day, job queue size, or custom metrics).
  - This approach enables you to **parallelize test execution** across multiple instances, significantly **reducing total test time**.
  - MIGs offer **automation**, **reliability**, and **load balancing (if needed)**, but load balancing is not essential in this test workload scenario.
  **Official Documentation:**
  - Managed instance groups overview
  - Autoscaling instance groups
  ❌ Why Other Options Are Incorrect:
  A.
  Use Compute Engine **unmanaged** instance groups with a Network Load Balancer.
  - **Unmanaged instance groups** lack automation for scaling and health checks.
  - **Network Load Balancer** is unnecessary for this scenario, as it's used for traffic distribution across front-end applications, not internal batch processing.
  C.
  Use Cloud Dataproc to run tests as Apache Hadoop jobs.
  - **Dataproc** is a managed service for running **Apache Spark/Hadoop** jobs — it's suitable for **big data workloads**, not for running a **custom C++ test framework**.
  - This would require a **major rewrite** or wrapper, which violates the **"minimal changes"** requirement.
  D.
  Use App Engine with Cloud Logging for monitoring.
  - **App Engine** is designed for **stateless web applications**, not for executing long-running **C++ binaries** or **custom Linux-based test suites**.
  - Also, you can use **Cloud Logging** with **GCE instances** too, so using App Engine offers no added benefit here and imposes strict runtime limitations.
  ✅ Final Answer: **B**
  Because it offers **dynamic scalability**, **parallel execution**, and **compatibility with Linux and C++**, fulfilling both performance and minimal-change requirements for migrating the test infrastructure to Google Cloud.

Link - [https://cloud.google.com/compute/docs/autoscaler/](https://cloud.google.com/compute/docs/autoscaler/)

---

## Question 33

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

A **lead developer at CloudInnovate Systems** informs you that their new application architecture utilizes **WebSockets** and **non-distributed HTTP sessions**, meaning session state is maintained on individual web servers. You want to ensure the application will function properly when deployed to **Google Cloud Platform (GCP)**.

**What should you do to support this deployment?**

- [ ] A.Assist the developer in **modifying the WebSocket implementation** to use **HTTP streaming** instead.
- [ ] B.Coordinate with the **security team** to review **encryption requirements** for WebSocket traffic.
- [x] C.Organize a discussion between the **cloud operations team** and the developer to explore **Google Cloud load balancing** options.
- [ ] D.Help the developer **redesign the application** to use **distributed session management** and eliminate dependencies on WebSockets and local HTTP sessions.

### Explanation

The correct answer is:
**C. Organize a discussion between the cloud operations team and the developer to explore Google Cloud load balancing options.**

✅ Justification for Correct Option (C):

- The application uses **WebSockets** and **non-distributed HTTP sessions** (i.e., session state is tied to individual web servers).
- In this architecture, it is **critical that clients consistently connect to the same backend server** (also known as **session affinity** or **sticky sessions**).
- **Google Cloud HTTP(S) Load Balancer** supports **WebSockets** and also provides **session affinity options** using client IP, cookies, or headers.

Thus, organizing a discussion with the cloud operations team ensures:

- The right **load balancer configuration** (such as enabling **session affinity**) is chosen.
- The team is aware of the **requirements for maintaining WebSocket connections and local session state**.
- There is **alignment between infrastructure capabilities and application architecture**.

**Official Documentation:**

- HTTP(S) Load Balancing and WebSockets
- Session Affinity with Load Balancers

❌ Why Other Options Are Incorrect:

A.

Modify WebSocket implementation to use HTTP streaming.

- **WebSockets and HTTP streaming** are **different technologies** with different use cases and capabilities.
- Replacing WebSockets with HTTP streaming could **break core application functionality**, and contradicts the application's architectural design.

B.

Review encryption requirements for WebSocket traffic.

- While security is always important, the core issue here is **application functionality**, not **data protection**.
- GCP’s HTTP(S) Load Balancer already supports **TLS termination** for secure WebSocket traffic.
- This doesn’t address the **load balancing and session affinity** needs.

D.

Redesign the app to use distributed session management and eliminate WebSockets.

- While using distributed session storage (e.g., Redis) is a good practice, this option involves **significant redesign**.
- The goal is to **support the current architecture**, not **replace** it entirely.

✅ Final Answer: **C**

It focuses on configuring Google Cloud’s infrastructure (load balancing and session affinity) to **support the existing WebSocket-based, non-distributed session architecture** with **minimal changes**, aligning with the practical deployment needs.

Ref - [https://cloud.google.com/load-balancing/docs/https#websocket_support](https://cloud.google.com/load-balancing/docs/https#websocket_support)

---

## Question 34

*Domain 1: Designing and Planning a Cloud Solution Architecture*

The **application reliability team at Innovare Tech** has recently introduced a debug feature in their backend service that streams **all server event records** to **Google Cloud Storage** for later analysis. Each event record ranges from **50 KB to 15 MB** in size, and the system may produce up to **3,000 events per second** during peak load.

As the cloud architect, you're tasked with designing a process that **minimizes data loss** while handling this volume and variety of data.

**Which process should you implement?**

- [ ] A.Append metadata directly to the file body Compress each event file individually Name each file using the format: `serverName-Timestamp` If the current bucket is older than 1 hour, create a new bucket and save files to it; otherwise, continue using the existing bucket
- [ ] B.Batch every 10,000 events along with a **manifest file** containing metadata Compress the batch and manifest into a single archive file Name files using the format: `serverName-EventSequence` If the current bucket is older than 1 day, create a new bucket and upload the archive there; otherwise, use the current bucket
- [ ] C.Compress each file individually Name each file as `serverName-EventSequence` Save all files into a single bucket After upload, set custom metadata headers for each object
- [x] D.Append metadata to the body of each file Compress files individually Name each file using a **random prefix pattern** Save all files into a single Cloud Storage bucket

### Explanation

The correct answer is:
**D. Append metadata to the body of each file, compress files individually, name each file using a random prefix pattern, save all files into a single Cloud Storage bucket.**

✅ Justification for Correct Option (D):

This option best addresses the **high-throughput**, **large-volume**, and **performance-oriented** nature of the event streaming use case with the following benefits:

1. **Appending metadata to the body of each file**:

- Embedding metadata within the event file ensures **data integrity and portability**, especially during debugging or offline analysis.
- Prevents reliance on potentially inconsistent or delayed metadata synchronization using object metadata headers.

2. **Compressing files individually**:

- Reduces **storage costs** and **network transfer times**, especially important for high-ingestion scenarios like **3,000 events/second**.
- Per-object compression is preferable here due to variable event sizes (50 KB – 15 MB).

3. **Random prefix pattern for file names**:

- This is **crucial for optimizing write throughput in Cloud Storage**.
- GCS stores data in a **distributed, sharded backend**, and using random prefixes ensures **parallelization** and prevents **hotspotting** (where too many writes hit the same storage shard).

**Reference**:
Google Cloud Storage naming best practices:
https://cloud.google.com/storage/docs/naming-objects#best-practices

"Avoid sequential naming patterns (e.g., timestamp-based) to prevent performance issues. Prefer a hash or random prefix."

4. **Single Cloud Storage bucket**:

- Easier to manage, monitor, and secure compared to dynamically creating buckets.
- Buckets are **scalable** and support extremely high throughput, so there's **no need to rotate buckets based on time**.

❌ Why Other Options Are Incorrect:

A.

Sequential timestamp-based file names and rotating buckets hourly.

- **Timestamp-based names** lead to **hotspotting** in Cloud Storage and can degrade performance.
- Rotating buckets **adds unnecessary complexity** and is not required — GCS is highly scalable with **a single bucket**.

B.

Batch every 10,000 events and compress into a single archive.

- Large batched files increase the risk of **data loss** if the archive fails before upload.
- Adding batching logic increases **latency** and **complexity**, violating the need to **minimize data loss**.
- Also uses sequential naming, which is **not ideal** for high-performance ingestion.

C.

Set custom metadata headers after upload.

- Relying on metadata headers adds **extra API calls** and potential for **consistency issues** or partial metadata application.
- Also uses **sequential naming**, leading to **hotspotting**.

✅ Final Answer: **D**

It ensures **optimal Cloud Storage write performance**, **low latency**, and **high reliability** for streaming high-volume events, following **Google Cloud best practices** for **object naming, compression, and scalability**.

Ref - [https://cloud.google.com/storage/docs/request-rate#naming-convention](https://cloud.google.com/storage/docs/request-rate#naming-convention)

---

## Question 35

*Domain 6: Ensuring Solution and Operations Excellence*

Your company, **AppSphere Solutions**, runs a production application as a **Deployment in a Google Kubernetes Engine (GKE) cluster**. During **rolling deployments** of new versions, the team has been unintentionally causing **service outages**. The issue has been traced back to **misconfigured parameters** that are only present in the **production environment**.

You want to implement **preventive measures** within the platform to reduce the risk of such outages in the future.

**What should you do?**

- [x] A.Set up **liveness and readiness probes** in the pod specifications to ensure Kubernetes routes traffic only to healthy pods.
- [ ] B.Configure **health checks** on the underlying **managed instance group**.
- [ ] C.Create a **Scheduled Task** to verify the application’s availability at regular intervals.
- [ ] D.Set up an **uptime check alert** in **Cloud Monitoring** to notify when the service becomes unavailable.

### Explanation

The correct answer is:
**A. Set up liveness and readiness probes in the pod specifications to ensure Kubernetes routes traffic only to healthy pods.**

✅ Justification for Correct Option (A):

- **Liveness and readiness probes** are essential features in Kubernetes that allow the platform to:
  - **Detect unresponsive or misconfigured containers** (`livenessProbe`) and restart them automatically.
  - **Prevent routing traffic to containers that are not ready** to serve requests (`readinessProbe`), which is crucial during rolling updates.
- When rolling out a new version in GKE, Kubernetes replaces old pods with new ones. If the new pods are **misconfigured**, but no readiness probe is defined, traffic might be routed to these **unready** pods, causing **service outages**.
- Properly configured **readiness probes** prevent new, misconfigured pods from being added to the load balancer before they are fully ready.

This is the **Kubernetes-native and platform-recommended approach** to managing availability during rolling deployments.

**Official Documentation:**

- Kubernetes Probes: Liveness and Readiness
- Rolling Updates with Readiness Probes

❌ Why Other Options Are Incorrect:

B.

Configure health checks on the underlying managed instance group.

- GKE nodes run inside a **managed instance group (MIG)**, but configuring health checks at the MIG level **does not control Kubernetes pod traffic routing**.
- Kubernetes does not use MIG health checks for determining pod availability.

C.

Create a Scheduled Task to verify the application’s availability at regular intervals.

- A scheduled task (e.g., a cron job) could detect issues, but it is **reactive**, not **proactive**.
- It does not integrate with the rolling update mechanism and cannot prevent outages during deployment.

D.

Set up an uptime check alert in Cloud Monitoring.

- This provides **external alerting**, which is useful for monitoring, but **does not prevent traffic from being routed to failing pods**.
- It helps with **detection**, not **prevention**.

✅ Final Answer: **A**

Because **liveness and readiness probes** allow **Kubernetes to manage pod health intelligently**, ensuring that **only healthy pods receive traffic**, especially during **rolling updates**, thereby minimizing the risk of service disruption due to misconfiguration.

Hint:

[https://cloud.google.com/blog/products/containers-kubernetes/best-practices-for-creating-a-highly-available-gke-cluster](https://cloud.google.com/blog/products/containers-kubernetes/best-practices-for-creating-a-highly-available-gke-cluster)

---

## Question 36

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

Your company, **CloudNova Technologies**, uses **Google Kubernetes Engine (GKE)** as the primary platform for running all workloads. Currently, there's a **single large GKE cluster** with a **node pool of 200 nodes** hosting a mix of **batch, stateful, and stateless workloads**.

To optimize operations, the organization wants to **reduce infrastructure costs** while ensuring **no loss of availability**.

**What should you do to meet these goals?**

- [ ] A.Create a second GKE cluster dedicated to **batch workloads**, and **split the original 200 nodes** between the two clusters.
- [ ] B.Define **CPU and memory limits** at the **namespace level**, and require that all Pods specify **CPU and memory limits** in their configurations.
- [x] C.Configure a **HorizontalPodAutoscaler** for all **stateless** and **autoscaling-compatible stateful workloads**, and enable **cluster autoscaling** on the GKE cluster.
- [ ] D.Reconfigure the current **node pool** to use **preemptible VMs** to reduce compute costs.

### Explanation

The correct answer is:
**C. Configure a HorizontalPodAutoscaler for all stateless and autoscaling-compatible stateful workloads, and enable cluster autoscaling on the GKE cluster.**

✅ Justification for Correct Option (C):

This option aligns perfectly with both goals: **reducing infrastructure costs** and **ensuring availability**.

Here's why:

- **HorizontalPodAutoscaler (HPA)** automatically adjusts the number of pod replicas based on resource utilization (like CPU, memory, or custom metrics). This ensures workloads scale **up when needed** and **down when idle**, optimizing resource usage.
- **Cluster Autoscaler** works in tandem with HPA by automatically **adding or removing nodes** based on the cluster's workload demands. It removes underutilized nodes when pods no longer need them and adds nodes when there's insufficient capacity.
- When configured correctly, this combination results in:
  - **Cost savings** during low usage periods
  - **Automatic scaling** to maintain availability during demand spikes
  - **Optimized resource usage** across the cluster

**Official Documentation:**

- Horizontal Pod Autoscaler
- Cluster Autoscaler on GKE

❌ Why Other Options Are Incorrect:

A.

Create a second GKE cluster and split the nodes.

- **Incorrect** because:
  - Maintaining multiple clusters increases **operational complexity and costs** (e.g., logging, monitoring, network overhead).
  - Splitting existing resources might **degrade performance or availability** without delivering proportional cost benefits.

B.

Define CPU and memory limits at the namespace level and require limits in pod specs.

- While this is a **good practice for resource management and quota enforcement**, it doesn’t **automatically optimize utilization or reduce costs**.
- It lacks **dynamic scaling**, so it alone won’t meet the cost-saving and availability goals.

D.

Use preemptible VMs in the node pool.

- **Preemptible VMs** (now called **Spot VMs**) can reduce costs significantly, but:
  - They are **ephemeral** and can be **terminated at any time**, making them **unsuitable for critical or stateful workloads** unless carefully isolated.
  - Using only preemptible VMs in a mixed-workload cluster can compromise **availability and stability**.

✅ Final Answer: **C**

Because it enables **dynamic workload and infrastructure scaling**, delivering both **cost efficiency** and **high availability** — a **Google Cloud best practice** for production-grade GKE environments.

---

## Question 37

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**Your company aims to explore cloud services with minimal risk. They intend to archive around 100 TB of their log data to the cloud and experiment with serverless analytics features while maintaining the data for long-term disaster recovery backup. What two steps should they undertake? (Choose two)**

- [x] A. Load logs into BigQuery.
- [ ] B. Load logs into Cloud SQL.
- [ ] C. Import logs into Cloud Logging.
- [ ] D. Insert logs into Cloud Bigtable.
- [x] E. Upload log files into Cloud Storage.

### Explanation

The correct answers are:
**A. Load logs into BigQuery**
**E. Upload log files into Cloud Storage**

✅ Justification:

**E. Upload log files into Cloud Storage**

- **Cloud Storage** is the **ideal service for archiving large volumes of log data (like 100 TB)** at a low cost.
- It is highly durable and suitable for **long-term disaster recovery**, especially when using **Coldline or Archive storage classes**.
- Cloud Storage supports **easy ingestion**, **lifecycle management**, and is the **recommended entry point** for large data archiving.

**Reference:**
Cloud Storage storage classes for archival

**A. Load logs into BigQuery**

- **BigQuery** is a **serverless analytics data warehouse**, perfect for **experimenting with analytics features** without managing infrastructure.
- You can either:
  - Load logs **directly** into BigQuery from Cloud Storage.
  - Use federated queries or **Cloud Logging export sinks** to push logs into BigQuery.
- It allows **powerful SQL-based queries** over massive datasets, which is ideal for exploring analytics features.

**Reference:**
Exporting logs to BigQuery

❌ Why the Other Options Are Incorrect:

**B. Load logs into Cloud SQL**

- Cloud SQL is designed for **relational transactional workloads**, not large-scale analytics or storage.
- Loading 100 TB of log data would be **costly, inefficient, and possibly exceed storage limits**.

**Reference:**
Cloud SQL storage limits

**C. Import logs into Cloud Logging**

- Cloud Logging is for collecting and **monitoring real-time logs**, not for **archiving** or **large-scale historical log storage**.
- It has **retention and cost limits** that make it unsuitable for storing 100 TB of historical data.

**Reference:**
Cloud Logging retention limits

**D. Insert logs into Cloud Bigtable**

- Cloud Bigtable is suited for **low-latency NoSQL workloads** and time-series data at massive scale.
- However, it's **complex to manage**, **not serverless**, and **not ideal for ad-hoc analytics** or archival.

**Reference:**
Bigtable use cases

✅ Final Answer:

**A. Load logs into BigQuery**
**E. Upload log files into Cloud Storage**
These steps meet the needs for **low-risk cloud exploration**, **long-term archival**, and **serverless analytics experimentation**.

References:

[https://cloud.google.com/storage/docs/storage-classes](https://cloud.google.com/storage/docs/storage-classes)

[https://cloud.google.com/bigtable/](https://cloud.google.com/bigtable/)

[https://cloud.google.com/products/operations](https://cloud.google.com/products/operations)

[https://cloud.google.com/sql/](https://cloud.google.com/sql/)

[https://cloud.google.com/bigquery/](https://cloud.google.com/bigquery/)

---

## Question 38

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**You've set up an autoscaling managed instance group to handle web traffic for an imminent launch. Upon configuring the instance group as a backend service to an HTTP(S) load balancer, you observe that virtual machine (VM) instances are being terminated and restarted every minute. These instances lack public IP addresses, yet you've confirmed that each instance is properly responding to web requests using the curl command. How should you ensure that the backend is configured correctly?**

- [ ] A. Verify the presence of a firewall rule permitting source traffic on HTTP/HTTPS to reach the load balancer.
- [ ] B. Allocate a public IP to each instance and configure a firewall rule to enable the load balancer to access the instance public IP.
- [x] C. Confirm the existence of a firewall rule enabling load balancer health checks to reach the instances within the instance group.
- [ ] D. Attach a tag to each instance matching the load balancer's name. Establish a firewall rule with the load balancer's name as the source and the instance tag as the destination.

### Explanation

The correct answer is:
**C. Confirm the existence of a firewall rule enabling load balancer health checks to reach the instances within the instance group.**

✅ **Justification for Correct Option (C):**

In Google Cloud, when you configure an **HTTP(S) load balancer** with a **backend service** (such as a **Managed Instance Group**), the load balancer uses **Google Front Ends (GFEs)** to perform **health checks** on the backend instances.

If:

- The health checks **fail** due to blocked traffic,
- Or the instances **don't respond to health check probes** properly,

Then the instances are considered **unhealthy** and are subject to **termination and recreation** by the autoscaler (as part of instance group health management).

Since the instances **do not have public IPs**, the health checks must come from **Google’s health check IP ranges**, and for those to succeed, you must allow them using an **ingress firewall rule**.

**Required Action:**

- Create a **firewall rule** allowing traffic from the health check IP ranges (source IPs) to reach the **health check ports** (e.g., TCP:80 for HTTP, TCP:443 for HTTPS).

**Official Documentation:**

- Health check firewall requirements
- Allowing health check probes

❌ **Why Other Options Are Incorrect:**

**A. Verify the presence of a firewall rule permitting source traffic on HTTP/HTTPS to reach the load balancer.**

- **Incorrect** because traffic from **users to the load balancer** is handled over the public internet via **Google Front Ends** — your backend VMs **do not need to receive traffic directly from clients**, and this firewall rule doesn't affect **health checks**.

**B. Allocate a public IP to each instance and configure a firewall rule...**

- **Not required**. Google Cloud **HTTP(S) Load Balancers use internal IPs** to connect to the backends — you do **not need public IPs** on VM instances for the load balancer to work.
- Adding public IPs introduces unnecessary **security risks and costs**.

**D. Attach a tag to each instance matching the load balancer's name...**

- GCP **does not use instance tags to match load balancers**.
- Also, the **source IP for health checks is not the load balancer name**, but specific **IP address ranges**, which must be allowed via **source IP ranges**, not tags.

✅ **Final Answer: C**

Ensure the backend instance group has a **firewall rule** that explicitly allows **health check probes** from **Google Cloud's health check IP ranges**, so the load balancer can correctly determine backend health.

References:[https://cloud.google.com/load-balancing/docs/https/](https://cloud.google.com/load-balancing/docs/https/)

[https://cloud.google.com/load-balancing/docs/health-check-concepts](https://cloud.google.com/load-balancing/docs/health-check-concepts)

---

## Question 39

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**Your organization hosts a 3-tier web application within the same Google Cloud Virtual Private Cloud (VPC). Each tier (web, API, and database) scales independently. Network traffic is intended to flow from the web tier to the API tier and then to the database tier. However, traffic should not traverse directly between the web and database tiers. How should you configure the network with minimal steps?**

- [ ] A. Assign each tier to a distinct subnetwork.
- [ ] B. Implement software-based firewalls on individual VMs.
- [ ] C. Apply tags to each tier and establish routes to enable the desired traffic flow.
- [x] D. Apply tags to each tier and create firewall rules to permit the intended traffic flow.

### Explanation

The correct answer is:
**D. Apply tags to each tier and create firewall rules to permit the intended traffic flow.**

✅ Justification for Correct Option (D):

In Google Cloud's Virtual Private Cloud (VPC), **firewall rules** are essential for controlling traffic flow between Virtual Machine (VM) instances. By default, all incoming traffic is **denied**, and all outgoing traffic is **allowed**. To enforce the desired communication patterns among your web, API, and database tiers, you can:

1. **Assign Network Tags to Each Tier:**
  - **Network tags** are labels that you can attach to VM instances, allowing you to **group instances** and apply firewall rules selectively.
  - For example:
    - Assign the tag `web-tier` to all web server instances.
    - Assign the tag `api-tier` to all API server instances.
    - Assign the tag `db-tier` to all database server instances.
2. **Create Firewall Rules Using These Tags:**
  - **Allow traffic** from the web tier to the API tier:
    - **Source filter:** `web-tier`
    - **Target filter:** `api-tier`
    - **Allowed protocols/ports:** Specify the necessary protocols and ports (e.g., TCP:80, TCP:443).
  - **Allow traffic** from the API tier to the database tier:
    - **Source filter:** `api-tier`
    - **Target filter:** `db-tier`
    - **Allowed protocols/ports:** Specify the necessary protocols and ports (e.g., TCP:3306 for MySQL).
  - **Deny direct traffic** from the web tier to the database tier:
    - **Source filter:** `web-tier`
    - **Target filter:** `db-tier`
    - **Denied protocols/ports:** All or specify as needed.

By implementing these steps, you ensure that:

- **Only authorized communication** occurs between the tiers.
- **Direct access** from the web tier to the database tier is **prevented**, adhering to the principle of least privilege.

**Official Documentation:**

- VPC firewall rules
- Using firewall rules with network tags

❌ Why Other Options Are Incorrect:

A. Assign each tier to a distinct subnetwork.

- **Subnetworks** primarily define **IP address ranges** and **routing domains**. While segmenting tiers into different subnetworks can provide **some level of isolation**, it does **not inherently control traffic flow** between them. You would still need to implement **firewall rules** to enforce the desired communication patterns.

B. Implement software-based firewalls on individual VMs.

- Managing **software-based firewalls** (e.g., `iptables` on Linux) on each VM introduces **operational complexity** and **inconsistencies**. Centralized management through **VPC firewall rules** is more **efficient**, **scalable**, and **aligned with Google Cloud best practices**.

C. Apply tags to each tier and establish routes to enable the desired traffic flow.

- **Routes** in Google Cloud determine how packets are **directed** within the network but do not **filter or control** traffic. To enforce **which traffic is allowed or denied**, you need to use **firewall rules**, not routes.

✅ Final Answer: **D**

Applying network tags to each tier and creating corresponding firewall rules allows you to **precisely control inter-tier communication**, ensuring that traffic flows only as intended while maintaining **security** and **compliance** with best practices.

References:

[https://cloud.google.com/vpc/docs/using-vpc](https://cloud.google.com/vpc/docs/using-vpc)

[https://cloud.google.com/vpc/docs/routes](https://cloud.google.com/vpc/docs/routes)

[https://cloud.google.com/vpc/docs/add-remove-network-tags](https://cloud.google.com/vpc/docs/add-remove-network-tags)

---

## Question 40

*Domain 3: Designing for Security and Compliance*

**You're architecting a sizable distributed application comprising 30 microservices, each requiring connection to a database backend. Your priority is to securely store the credentials. Where should you store these credentials?**

- [ ] A. In the source code
- [ ] B. Within an environment variable
- [x] C. Within a secret management system
- [ ] D. In a configuration file with restricted access via ACLs

### Explanation

The correct answer is:
**C. Within a secret management system**

✅ **Correct Option: C. Within a secret management system**

**Explanation:**
When designing a large-scale distributed application (e.g., with 30 microservices), **secure storage of sensitive information like database credentials** is critical. The **Google-recommended** and **industry-standard** approach is to use a **secret management system** such as:

- **Google Secret Manager**: Enables you to store, manage, and access secrets like API keys, passwords, and certificates with IAM-controlled access and audit logging.

**Benefits:**

- Centralized management of secrets
- Fine-grained IAM permissions
- Integration with GKE, Cloud Functions, Cloud Run, etc.
- Secret versioning and automatic rotation
- Audit logging for access tracking

❌ Incorrect Options:

**A. In the source code**

- **Risky and insecure**: Hardcoding credentials in source code can lead to accidental exposure via version control (e.g., GitHub).
- Violates best practices and fails compliance audits.

**B. Within an environment variable**

- Better than hardcoding, but still **less secure and harder to manage at scale**.
- Environment variables can be exposed through debugging or process dumps.
- Lacks centralized control and rotation features.

**D. In a configuration file with restricted access via ACLs**

- While better than source code, this still **lacks centralized control**, auditing, and built-in rotation.
- ACLs can be difficult to manage at scale and might still be misconfigured.

📚 Google Cloud Documentation:

- Secret Manager Overview – Google Cloud
- Best practices for secrets management

References:

[https://cloud.google.com/kubernetes-engine/docs/concepts/secret](https://cloud.google.com/kubernetes-engine/docs/concepts/secret)

[https://cloud.google.com/secret-manager](https://cloud.google.com/secret-manager)

---

## Question 41

*Domain 3: Designing for Security and Compliance*

**Your customer is migrating their corporate applications to Google Cloud. The security team seeks comprehensive visibility of all organization resources. You have established yourself as the Organization Administrator using Resource Manager. Which Identity and Access Management (IAM) roles should you assign to the security team, in accordance with Google's recommended practices?**

- [ ] A. Organization viewer, Project owner
- [x] B. Organization viewer, Project viewer
- [ ] C. Organization administrator, Project browser
- [ ] D. Project owner, Network administrator

### Explanation

✅ **Correct Option: B. Organization viewer, Project viewer**

**Explanation:**
To give the **security team visibility across all Google Cloud resources** (without giving them unnecessary permissions to modify resources), you should follow the principle of **least privilege**.

Assigning the following roles ensures **read-only access** at both the organization and project levels:

- `roles/resourcemanager.organizationViewer` **(Organization Viewer)**:
  - Provides **read-only** access to view the organization’s structure, policies, and resources.
  - Allows visibility into folders, projects, and IAM policies.
- `roles/viewer` **(Project Viewer)** or `roles/browser` (for navigating resources):
  - Provides **read-only access** to project-level resources, including Compute Engine, GKE, Cloud Storage, etc.

🔐 These roles are **recommended by Google** to give security teams visibility without write access.

❌ Incorrect Options:

**A. Organization viewer, Project owner**

- **Too much privilege**: The `Project Owner` role (`roles/owner`) includes full administrative rights, which exceeds the visibility requirement and violates least privilege.

**C. Organization administrator, Project browser**

- **Overprivileged**: The `Organization Administrator` (`roles/resourcemanager.organizationAdmin`) role grants broad administrative control over all resources in the organization. This role should be tightly controlled and not assigned for simple visibility needs.

**D. Project owner, Network administrator**

- **Wrong scope & permissions**: These roles grant **administrative access**, not just visibility. Also, they’re limited to specific scopes (project/network), not the entire organization.

📚 Google Cloud Documentation:

- Understanding IAM Roles
- Predefined IAM Roles
- Best practices for enterprise organizations

[https://cloud.google.com/resource-manager/docs/access-control-org#using_predefined_roles](https://cloud.google.com/resource-manager/docs/access-control-org#using_predefined_roles)

---

## Question 42

*Domain 3: Designing for Security and Compliance*

A security review at **CloudNova Corp** uncovered that a new VPC network was recently created in your Google Cloud project. Within this network, a Compute Engine instance has its SSH port exposed to the public internet. You need to determine who created this network and when.

What is the best course of action?

- [ ] A. Use the Stackdriver alerting console to look for a "Create VM" entry
- [ ] B. Go to the **Activity** section under the **Home** tab, filter by **Data Access**, and search for a "Create VM" entry
- [x] C. Open the **Logs Explorer**, filter by **GCE Network** resource type, and search for a "compute.instances.insert" log entry
- [ ] D. Connect to the VM using project-level SSH keys, review system login logs, and compare user activity with the list of project owners

### Explanation

The correct answer is:
**C. Open the Logs Explorer, filter by GCE Network resource type, and search for a `compute.instances.insert` log entry**

✅ **Justification for Correct Option (C):**

To determine **who created a VPC network or a Compute Engine instance** (such as one exposing SSH to the public), the most reliable and audit-friendly method is to:

1. **Open the Cloud Logging > Logs Explorer**
2. Filter by **resource type**: `gce_network` (or use `gce_instance` for VM creation)
3. Search for the **Admin Activity log** entry for:
  - `compute.networks.insert` → for VPC creation
  - `compute.instances.insert` → for VM creation

These entries include:

- **Actor identity** (email or service account)
- **Timestamp** of the action
- **Resource details** (network name, instance name, etc.)

These logs are **automatically recorded** under **Admin Activity** logs, even if you haven’t enabled Data Access logging.

**Official Documentation:**

- Audit logs for Compute Engine
- Viewing audit logs in Logs Explorer

❌ **Why Other Options Are Incorrect:**

**A. Use the Stackdriver alerting console to look for a "Create VM" entry**

- **Incorrect** because Stackdriver alerts (now Cloud Monitoring) are for **monitoring metrics**, not auditing.
- It **doesn't log admin activity** like resource creation unless custom alerts were set up in advance.

**B. Go to the Activity section under the Home tab, filter by Data Access**

- **Incorrect** because:
  - The **Activity page** only shows **high-level summaries**, not detailed event logs.
  - **Data Access logs** are **not enabled by default**, and this action (VM/VPC creation) would fall under **Admin Activity**, not Data Access.

**D. Connect to the VM using project-level SSH keys and review login logs**

- **Not reliable** or recommended.
- May show **system logins**, but won't show **who created the VM** or the VPC.
- Requires access to the VM, and system logs may be rotated or limited.

✅ **Final Answer: C**

Use **Logs Explorer** with the appropriate **resource type** and **log filter** (e.g., `compute.instances.insert`) to accurately identify **who created the VM/network** and **when** — as per **Google Cloud’s recommended auditing practices**.

**⚠️ Note:** The audit-log method for creating a network is `compute.networks.insert` (resource type `gce_network`); `compute.instances.insert` is VM creation. The approach in C (Admin Activity audit logs in Logs Explorer) is still the right one.

---

## Question 43

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**You need to create a duplicate of a production Linux VM currently running in the us-central1 region. The goal is to easily manage and update this copy when changes are made to the original VM. You plan to deploy this duplicate VM in a different Google Cloud project located in the us-east1 region. What steps should you take to achieve this?**

- [ ] A. Use Linux dd and netcat commands to stream the contents of the root disk directly to a new VM in the us-east1 region
- [ ] B. Take a snapshot of the root disk and use it as the boot disk when launching a new VM in the us-east1 region
- [ ] C. Use the dd command to create an image file of the root disk, then use this image to create a new VM in the us-east1 region
- [x] D. Take a snapshot of the root disk, export it to a Cloud Storage bucket as an image file, and create a new VM in the us-east1 region using that image as the boot disk

### Explanation

The correct answer is:
**D. Take a snapshot of the root disk, export it to a Cloud Storage bucket as an image file, and create a new VM in the us-east1 region using that image as the boot disk.**

✅ **Justification for Correct Option (D):**

To duplicate a production **Linux VM** from one **region and project** (e.g., `us-central1`) to another **region and project** (`us-east1`), the most reliable and scalable approach is:

1. **Take a snapshot** of the source VM's root disk.
2. **Create a custom image** from the snapshot.
3. **Export** the custom image to a **Cloud Storage bucket** (if transferring to another **project or region**).
4. **Import the image** into the destination project.
5. Use the image to **create a new VM** in `us-east1`.

This method:

- Ensures **cross-region and cross-project portability**
- Provides a **manageable image** that can be reused or updated
- Is **Google Cloud–supported and documented**

**Official Documentation:**

- Exporting a custom image to Cloud Storage
- Importing a custom image from Cloud Storage
- Creating VM from custom image

❌ **Why Other Options Are Incorrect:**

**A. Use Linux `dd` and `netcat` to stream disk content**

- This is a **manual and error-prone** method.
- It is **not scalable or secure** for cloud VM duplication.
- Doesn’t integrate well with Google Cloud’s **managed services** for VM creation or backup.

**B. Take a snapshot of the root disk and use it as the boot disk in** `us-east1`

- Snapshots are global resources and can, with the right IAM permission, boot a disk in another region or project, so B is workable. But a snapshot is a backup of one disk, not a reusable boot artifact. An **image** is the artifact meant for creating and refreshing VM copies.
- You must **export/import** the image for cross-region or cross-project usage.

**Reference:**
Snapshot storage location considerations

**C. Use `dd` to create a disk image and use it to create a new VM**

- Like A, this involves **manual disk imaging** and doesn’t use **GCP-native tools**.
- Using `dd` and image files requires additional conversion steps and doesn’t provide **managed lifecycle capabilities** like custom images do.

✅ **Final Answer: D**

This approach follows **Google Cloud best practices** for **duplicating VMs across regions and projects** using snapshots, images, and Cloud Storage for secure and manageable transfer.

Link - [https://cloud.google.com/compute/docs/instances/copy-vm-between-projects](https://cloud.google.com/compute/docs/instances/copy-vm-between-projects)

**⚠️ Note:** Exporting to a Cloud Storage file isn't strictly required: a custom image is global and can be shared with another project through IAM (`roles/compute.imageUser`), and image families make it easy to roll out a refreshed copy. Keep the key (image-based copy), but know that the export step is optional.

---

## Question 44

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**SkyData Solutions** operates multiple databases on a single MySQL instance hosted on Google Cloud. The team needs to regularly back up one specific database. The backup process must be fast and should not cause any noticeable impact on disk performance.

How should the storage be set up to meet these requirements?

- [ ] A. Set up a cron job that uses the `gcloud` CLI to create periodic backups using persistent disk snapshots
- [ ] B. Attach a Local SSD volume to the instance for temporary backup storage, then transfer the backup to Cloud Storage using `gsutil`
- [ ] C. Mount a Cloud Storage bucket directly on the instance using `gcsfuse`, and use `mysqldump` to write backups to the mounted location
- [x] D. Attach multiple persistent disks to the VM, configure them in a RAID10 array, and use LVM snapshots for backups, which are then uploaded to Cloud Storage

### Explanation

**Correct answer: D. Attach multiple persistent disks to the VM, configure them in a RAID10 array, and use LVM snapshots for backups, which are then uploaded to Cloud Storage.**

For this scenario, the key requirement is to back up **one specific MySQL database** from a MySQL instance that hosts **multiple databases**, while keeping the backup fast and avoiding noticeable disk-performance impact. Using separate storage volumes managed with LVM allows the database data to be isolated logically, and an LVM snapshot can capture the relevant volume quickly. RAID10 across persistent disks can also improve disk throughput and reduce the performance impact during backup operations.

Google Cloud documentation supports using multiple persistent disks with software RAID to improve throughput and IOPS, and Persistent Disk performance scales based on disk type, size, and configuration. Google also documents disk snapshots as a backup mechanism, but disk snapshots operate at the disk level rather than at the individual MySQL database level.
Reference: [Optimize Persistent Disk performance](https://cloud.google.com/compute/docs/disks/optimizing-pd-performance) and [Persistent Disk snapshots](https://cloud.google.com/compute/docs/disks/snapshots)

**Why the other options are not the best choice**

A. **Incorrect.** Persistent Disk snapshots are fast and useful for backups, but they capture an entire disk, not one specific MySQL database. If multiple databases share the same disk, this does not meet the requirement to back up only one database.

B. **Incorrect.** Local SSD is high-performance temporary storage, but it is ephemeral and not suitable as a reliable backup target. Google Cloud states that Local SSD data is not durable and should be copied to durable storage if it must be preserved.
Reference: [About Local SSD disks](https://cloud.google.com/compute/docs/disks/local-ssd)

C. **Incorrect.** Mounting Cloud Storage with Cloud Storage FUSE and writing `mysqldump` output directly to it can introduce higher latency than a local file system. It also performs a logical dump, which can significantly affect MySQL read I/O and database performance. Google Cloud notes that Cloud Storage FUSE has higher latency than local file systems and should not be used as a database backend.
Reference: [Cloud Storage FUSE overview](https://cloud.google.com/storage/docs/cloud-storage-fuse/overview)

**Need-to-know foundational concept**

Persistent Disk snapshots are excellent when you need disk-level backups. However, when the requirement is to back up **one specific database** from a MySQL instance hosting multiple databases, the storage layout must isolate that database at the volume level. That is why an LVM-based setup with performance-optimized persistent disks is the best fit among the given options.

###### Explanation

**Correct answer: D. Attach multiple persistent disks to the VM, configure them in a RAID10 array, and use LVM snapshots for backups, which are then uploaded to Cloud Storage.**

For this scenario, the key requirement is to back up **one specific MySQL database** from a MySQL instance that hosts **multiple databases**, while keeping the backup fast and avoiding noticeable disk-performance impact. Using separate storage volumes managed with LVM allows the database data to be isolated logically, and an LVM snapshot can capture the relevant volume quickly. RAID10 across persistent disks can also improve disk throughput and reduce the performance impact during backup operations.

Google Cloud documentation supports using multiple persistent disks with software RAID to improve throughput and IOPS, and Persistent Disk performance scales based on disk type, size, and configuration. Google also documents disk snapshots as a backup mechanism, but disk snapshots operate at the disk level rather than at the individual MySQL database level.
Reference: [Optimize Persistent Disk performance](https://cloud.google.com/compute/docs/disks/optimizing-pd-performance) and [Persistent Disk snapshots](https://cloud.google.com/compute/docs/disks/snapshots)

> [!note]- Why the other options are wrong
> A. **Incorrect.** Persistent Disk snapshots are fast and useful for backups, but they capture an entire disk, not one specific MySQL database. If multiple databases share the same disk, this does not meet the requirement to back up only one database.
>
> B. **Incorrect.** Local SSD is high-performance temporary storage, but it is ephemeral and not suitable as a reliable backup target. Google Cloud states that Local SSD data is not durable and should be copied to durable storage if it must be preserved.
> Reference: [About Local SSD disks](https://cloud.google.com/compute/docs/disks/local-ssd)
>
> C. **Incorrect.** Mounting Cloud Storage with Cloud Storage FUSE and writing `mysqldump` output directly to it can introduce higher latency than a local file system. It also performs a logical dump, which can significantly affect MySQL read I/O and database performance. Google Cloud notes that Cloud Storage FUSE has higher latency than local file systems and should not be used as a database backend.
> Reference: [Cloud Storage FUSE overview](https://cloud.google.com/storage/docs/cloud-storage-fuse/overview)

**⚠️ Note:** This key is debated. LVM snapshots are copy-on-write, so they add write overhead while they exist, and they capture a whole volume, not one database. Many candidates prefer B (dump the one database to Local SSD, which doesn't share Persistent Disk performance, then copy it to Cloud Storage). Answer D if you see this exact wording.

---

## Question 45

*Domain 6: Ensuring Solution and Operations Excellence*

You are assisting the QA team at **NextGen Systems** in deploying a new load-testing tool to evaluate the scalability of key cloud services that run on **Google Compute Engine** and **Cloud Bigtable**.

Which **three** requirements should be included in the rollout plan? *(Choose three.)*

- [x] A. Verify that the load tests measure and validate Cloud Bigtable’s performance
- [x] B. Set up a separate Google Cloud project specifically for the load-testing environment
- [ ] C. Configure the load-testing tool to run periodically against the production environment
- [ ] D. Make sure all third-party services integrated with your application can handle increased traffic during load testing
- [ ] E. Update the production environment to log all transactions for replay during testing
- [x] F. Add detailed logging and metrics to both the load-testing tool and the services being tested

### Explanation

The correct answers are:
**A. Verify that the load tests measure and validate Cloud Bigtable’s performance**
**B. Set up a separate Google Cloud project specifically for the load-testing environment**
**F. Add detailed logging and metrics to both the load-testing tool and the services being tested**

✅ Justification for Correct Answers:

**A. Verify that the load tests measure and validate Cloud Bigtable’s performance**

- The **main goal of load testing** is to understand how well services like **Cloud Bigtable** scale under pressure.
- You must design your test scenarios to **generate realistic workloads** that exercise **reads, writes, and schema usage**, and **validate throughput, latency, and CPU usage**.

**Reference:**
Cloud Bigtable performance tuning

**B. Set up a separate Google Cloud project specifically for the load-testing environment**

- Creating a **separate project** offers **resource isolation**, **billing segregation**, and **permissions control**.
- It ensures that load testing does **not affect production** or violate quota limits unexpectedly.

**Reference:**
Best practices for enterprise organizations

**F. Add detailed logging and metrics to both the load-testing tool and the services being tested**

- **Observability is essential**: you need metrics (CPU, latency, throughput) and logs to **identify bottlenecks** and verify expected behavior.
- Tools like **Cloud Monitoring**, **Cloud Logging**, and **Cloud Trace** help you **correlate test load with backend behavior**.

**Reference:**
Operations Suite overview

❌ Why the Other Options Are Incorrect:

**C. Configure the load-testing tool to run periodically against the production environment**

- This is risky. Running periodic load tests on **production** can cause **latency spikes, service degradation**, or **downtime**.
- Load tests should be conducted on **staging or mirrored environments**, unless the production environment is explicitly built to tolerate it.

**D. Make sure all third-party services integrated with your application can handle increased traffic during load testing**

- While important in **end-to-end system validation**, this is often **outside the scope** of internal service load testing.
- Many third-party services have **rate limits** and **cost implications**, and it's best to **mock or isolate** them during load tests.

**E. Update the production environment to log all transactions for replay during testing**

- Logging **all** transactions can lead to **performance degradation** and **high costs**.
- It’s better to use **representative synthetic data** or **sampled logs** for test replay scenarios.

✅ Final Answer:

**A.**, **B.**, and **F.**
These steps align with **Google Cloud best practices** for performance testing and help ensure **safe, effective, and observable load testing** of services like **Compute Engine and Cloud Bigtable**.

---

## Question 46

*Domain 3: Designing for Security and Compliance*

TechNova Inc. is migrating its internal applications to Google Cloud. The cybersecurity team at TechNova requires comprehensive visibility into all projects across the organization. You have already enabled Google Cloud Resource Manager and assigned yourself the Organization Administrator role.

Which **Cloud Identity and Access Management (IAM)** roles should be granted to the cybersecurity team to meet their visibility needs?

- [ ] A. Organization Viewer and Project Owner
- [x] B. Organization Viewer and Project Viewer
- [ ] C. Organization Administrator and Project Browser
- [ ] D. Project Owner and Network Administrator

### Explanation

✅ Correct Answer:

**B. Organization Viewer and Project Viewer**

✅ Justification for Correct Answer:

To **gain visibility into all projects and their configurations** across the organization, the cybersecurity team needs:

1. **Organization-level visibility**:
  This is provided by the `roles/resourcemanager.organizationViewer` (Organization Viewer).
  - This role allows read-only access to organization-level resources and policies such as:
    - Organization policies
    - Folders
    - Projects
    - IAM policies
  **Official Reference**:
  https://cloud.google.com/iam/docs/understanding-roles#resourcemanager-organizationViewer
2. **Project-level visibility**:
  The `roles/viewer` (Project Viewer) role gives read-only access to all project resources:
  - Compute Engine
  - IAM policies
  - Networking components
  - Logs and monitoring
  **Official Reference**:
  https://cloud.google.com/iam/docs/understanding-roles#viewer

Together, these two roles **satisfy the visibility requirement** without granting excessive permissions.

❌ Justifications for Incorrect Options:

**A. Organization Viewer and Project Owner**

- **Organization Viewer** is good (read-only visibility at org level).
- But **Project Owner** (`roles/owner`) gives **full control**, including the ability to:
  - Modify configurations
  - Delete resources
  - Manage IAM policies

This **violates the principle of least privilege** and is **not suitable for a cybersecurity team** that only needs **visibility**, not modification rights.

**Reference**:
https://cloud.google.com/iam/docs/understanding-roles#owner

**C. Organization Administrator and Project Browser**

- **Organization Administrator** (`roles/resourcemanager.organizationAdmin`) allows **modification and management of the entire organization**, including:
  - Managing IAM roles and policies
  - Creating/deleting folders and projects
    This is **too powerful for visibility needs**.
- **Project Browser** (`roles/browser`) only allows listing of resources, not detailed inspection or viewing configurations, logs, etc.

**References**:

- Organization Admin: https://cloud.google.com/iam/docs/understanding-roles#resourcemanager-organizationAdmin
- Project Browser: https://cloud.google.com/iam/docs/understanding-roles#browser

This combination fails to provide **deep visibility** and **over-privileges** the org level.

**D. Project Owner and Network Administrator**

- **Project Owner** gives full permissions (create, delete, modify) within the project.
- **Network Administrator** (`roles/compute.networkAdmin`) allows managing networking resources (e.g., VPC, firewall rules), but **doesn't provide broad visibility into all project configurations** or security auditability.

This combo is inappropriate:

- **Over-privileges control**
- **Under-delivers visibility across the organization**

**Reference**:
[https://cloud.google.com/iam/docs/understanding-roles#compute-networkAdmin](https://cloud.google.com/iam/docs/understanding-roles#compute-networkAdmin)

✅ Final Answer:

**B. Organization Viewer and Project Viewer**

This is the **least-privilege, visibility-only** approach that gives the **cybersecurity team** full insight without administrative access.

---

## Question 47

*Domain 3: Designing for Security and Compliance*

CloudWorks Ltd. emphasizes rapid responsiveness and prioritizes meeting customer demands quickly. Their main business goals are **accelerated release cycles and increased agility**. As part of your DevSecOps initiative, you aim to minimize the risk of unintentionally introducing security issues during development.

Which **two measures** should you implement to achieve this? *(Choose two.)*

- [ ] A. Require that every code commit is peer-reviewed by a security subject matter expert (SME)
- [x] B. Integrate static source code security analysis tools into the CI/CD pipeline
- [ ] C. Ensure all component interfaces have stubs for unit testing
- [ ] D. Enable code signing and use a trusted binary repository integrated with your CI/CD workflow
- [x] E. Include a vulnerability scanning tool as part of your continuous integration and delivery process

### Explanation

✅ Correct Answers:

**B. Integrate static source code security analysis tools into the CI/CD pipeline**
**E. Include a vulnerability scanning tool as part of your continuous integration and delivery process**

✅ Explanation of Correct Options:

**B. Integrate static source code security analysis tools into the CI/CD pipeline**

**Why it’s correct:**

- Static Application Security Testing (**SAST**) tools analyze source code for vulnerabilities **before the code is compiled**.
- When integrated into the **CI/CD pipeline**, they provide **automated, early detection** of security flaws without manual effort or delay.
- It allows **security to shift left**, aligning perfectly with DevSecOps.

**Official Reference:**
Google Cloud DevSecOps Guide – Security in CI/CD:
https://cloud.google.com/architecture/devsecops-overview#secure-your-code-in-ci/cd-pipelines

**E. Include a vulnerability scanning tool as part of your continuous integration and delivery process**

**Why it’s correct:**

- Integrates tools like **Container Analysis** or **third-party vulnerability scanners** into the build and deployment process.
- Helps identify known vulnerabilities in **libraries, images, or dependencies** before code reaches production.
- Works seamlessly with rapid CI/CD cycles.

**Official Reference:**
Google Cloud DevSecOps – Secure your software supply chain:
https://cloud.google.com/architecture/devsecops-overview#detect-vulnerabilities-in-software-components

❌ Explanation of Incorrect Options:

**A. Require that every code commit is peer-reviewed by a security subject matter expert (SME)**

**Why it’s incorrect:**

- While **peer reviews are important**, requiring a **security SME for every commit** is **not scalable** and will **slow down release cycles**.
- This approach conflicts with the company’s goal of **agility and rapid releases**.

**C. Ensure all component interfaces have stubs for unit testing**

**Why it’s incorrect:**

- Stubbed interfaces are useful for **functional testing**, but they don’t help detect **security vulnerabilities**.
- This measure supports **testability**, not **security validation**.

**D. Enable code signing and use a trusted binary repository integrated with your CI/CD workflow**

**Why it’s not ideal in this context:**

- Code signing and secure artifact storage are important for **software supply chain integrity**, but:
  - They are more about **ensuring authenticity of builds and preventing tampering** post-build.
  - They don’t **actively detect or prevent** vulnerabilities during development.
- Helpful later in the chain, not for minimizing **introduction** of vulnerabilities during early dev.

✅ Final Answers:

**B. Integrate static source code security analysis tools into the CI/CD pipeline**
**E. Include a vulnerability scanning tool as part of your continuous integration and delivery process**

---

## Question 48

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**You are managing a running Google Kubernetes Engine (GKE) cluster for AppVantage Corp. and want to ensure it automatically scales as application demand fluctuates.**

**What action should you take?**

- [ ] A. Manually scale the cluster by running: `gcloud container clusters resize CLUSTER_NAME --size 10`
- [ ] B. Add a tag to the cluster instances to enable autoscaling using: `gcloud compute instances add-tags INSTANCE_NAME --tags enable-autoscaling,max-nodes-10`
- [x] C. Enable autoscaling on the existing cluster by executing: `gcloud alpha container clusters update mycluster --enable-autoscaling --min-nodes=1 --max-nodes=10`
- [ ] D. Create a new cluster with autoscaling enabled and redeploy your app using: `gcloud alpha container clusters create mycluster --enable-autoscaling --min-nodes=1 --max-nodes=10`

### Explanation

✅ **Correct Answer:**

**C. Enable autoscaling on the existing cluster by executing:**
`gcloud alpha container clusters update mycluster --enable-autoscaling --min-nodes=1 --max-nodes=10`

✅ **Justification for Option C:**

- This command uses the `gcloud` CLI to **update an existing cluster** and **enable autoscaling**.
- You can configure **minimum and maximum node counts**, which allow GKE’s **Cluster Autoscaler** to automatically add/remove nodes based on pod resource requests and current usage.

**Note:** Although this command uses `gcloud alpha`, it might also be supported under `gcloud container clusters update` in **GA or beta** depending on your SDK version. Always verify based on the active gcloud release.

**Official GCP Documentation:**

- Cluster autoscaler:
  [https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler)
- Enabling autoscaling:
  [https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler#enabling_autoscaling](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler#enabling_autoscaling)

❌ **Why the Other Options Are Incorrect:**

**A. Manually scale the cluster by running:

`gcloud container clusters resize CLUSTER_NAME --size 10`**

- This **resizes the cluster manually**, setting a fixed node count.
- It does **not provide automatic scaling** based on demand.
- Does not meet the requirement of **automatic scaling**.

**Reference:**
[https://cloud.google.com/sdk/gcloud/reference/container/clusters/resize](https://cloud.google.com/sdk/gcloud/reference/container/clusters/resize)

**B. Add a tag to the cluster instances to enable autoscaling using:

`gcloud compute instances add-tags INSTANCE_NAME --tags enable-autoscaling,max-nodes-10`**

- GKE **autoscaling is not enabled by setting instance tags**.
- Tags are used for **network/firewall rules**, not for controlling autoscaler behavior.
- GKE autoscaler is configured via the `gcloud container clusters` or UI/API, **not via instance tags**.

**Reference:**
[https://cloud.google.com/sdk/gcloud/reference/compute/instances/add-tags](https://cloud.google.com/sdk/gcloud/reference/compute/instances/add-tags)
(No link between tags and autoscaling behavior.)

**D. Create a new cluster with autoscaling enabled and redeploy your app using:

`gcloud alpha container clusters create mycluster --enable-autoscaling --min-nodes=1 --max-nodes=10`**

- While this command **does enable autoscaling**, it **creates a new cluster**, which:
  - **Is not required** since the question says you’re managing a **running cluster**
  - Requires **redeployment of applications**, which is unnecessary and disruptive.

This is a **more destructive approach** than needed.

✅ Final Answer:

**C. Enable autoscaling on the existing cluster by executing:**
`gcloud alpha container clusters update mycluster --enable-autoscaling --min-nodes=1 --max-nodes=10`

**⚠️ Note:** Cluster autoscaling is GA; you no longer need the `alpha` track. Today's form is `gcloud container clusters update CLUSTER --enable-autoscaling --node-pool=POOL --min-nodes=1 --max-nodes=10`. The point still holds: update the existing cluster instead of recreating it.

---

## Question 49

*Domain 1: Designing and Planning a Cloud Solution Architecture*

The **marketing team at NexaDigital** plans to launch a promotional email campaign. The **development team** wants to minimize operational overhead while preparing for a potentially high volume of customer interactions—ranging from **100 to 500,000 click-throughs per day**. The campaign will direct users to a lightweight promotional website that collects basic user details and preferences.

Which **two infrastructure solutions** should you recommend to meet their scalability and management goals? *(Choose two.)*

- [x] A. Deploy the website on **Google App Engine**, and use **Cloud Datastore** to store user information.
- [ ] B. Use **Google Kubernetes Engine (GKE)** to host the website and store user data on **persistent disks**.
- [x] C. Serve the website with a **Managed Instance Group (MIG)** and use **Cloud Bigtable** for storing user data.
- [ ] D. Run the website on a **single Compute Engine VM** backed by **Cloud SQL** for data storage.

### Explanation

✅ Correct Answers:

**A. Deploy the website on Google App Engine, and use Cloud Datastore to store user information**
**C. Serve the website with a Managed Instance Group (MIG) and use Cloud Bigtable for storing user data**

✅ **Option A: App Engine + Cloud Datastore**

**Why it’s correct:**

- **App Engine** is a fully managed serverless platform that **automatically scales** based on traffic.
- Requires **minimal operational management**, perfect for short-term high-traffic campaigns.
- **Cloud Datastore** (now **Firestore in Datastore mode**) is a highly scalable NoSQL database designed for **user-centric, web/mobile apps**.

**Relevant Docs:**

- App Engine Overview: [https://cloud.google.com/appengine/docs](https://cloud.google.com/appengine/docs)
- Firestore in Datastore mode: [https://cloud.google.com/datastore/docs](https://cloud.google.com/datastore/docs)

✅ **Option C: Managed Instance Group (MIG) + Cloud Bigtable**

**Why it’s correct:**

- **Managed Instance Groups** auto-scale instances based on load, providing **flexible scalability**.
- **Cloud Bigtable** is ideal for **high-throughput, large-scale writes and reads**, suitable for large-scale campaigns with clickstream-like data.
- Offers more **fine-grained control** than App Engine if needed, while still allowing scaling.

**Relevant Docs:**

- MIGs: [https://cloud.google.com/compute/docs/instance-groups](https://cloud.google.com/compute/docs/instance-groups)
- Cloud Bigtable: [https://cloud.google.com/bigtable/docs/overview](https://cloud.google.com/bigtable/docs/overview)

❌ Why the Other Options Are Incorrect:

**B. GKE with Persistent Disks**

- GKE provides flexibility and scalability but **requires significant operational overhead**:
  - Managing clusters, nodes, deployments
  - Configuring persistent volumes
- Not ideal when **minimizing operations is a goal**.

**Docs:** [https://cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview](https://cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)

**D. Single Compute Engine VM + Cloud SQL**

- A **single VM** creates a **scalability bottleneck** — unsuitable for **500K daily interactions**.
- Although Cloud SQL is scalable, this architecture lacks **redundancy and elasticity**.
- Also **high operational overhead** (patching, scaling, uptime management).

**Docs:** [https://cloud.google.com/sql/docs/introduction](https://cloud.google.com/sql/docs/introduction)
[https://cloud.google.com/compute/docs/instances](https://cloud.google.com/compute/docs/instances)

✅ Final Answer:

**A. Deploy the website on Google App Engine, and use Cloud Datastore to store user information**
**C. Serve the website with a Managed Instance Group (MIG) and use Cloud Bigtable for storing user data**

**⚠️ Note:** Bigtable is oversized and has a fixed node cost for 'basic user details'. Option C is keyed because GKE with persistent disks and a single VM are worse, not because Bigtable is a natural fit.

---

## Question 50

*Domain 1: Designing and Planning a Cloud Solution Architecture*

TechNova Solutions recently completed a rapid **lift-and-shift migration** to **Google Compute Engine** to meet immediate compute requirements. You now have **nine months** to plan and implement a more **cloud-native architecture** that emphasizes **auto-scaling** and requires **minimal operational overhead (no-ops)**.

Which **two Google Cloud compute services** would best support this transformation? *(Choose two.)*

- [ ] A. Compute Engine running containerized workloads
- [x] B. Google Kubernetes Engine (GKE) using containers
- [x] C. Google App Engine Standard Environment
- [ ] D. Compute Engine with custom machine types
- [ ] E. Compute Engine with managed instance groups (MIGs)

### Explanation

✅ Correct Answers:

**B. Google Kubernetes Engine (GKE) using containers**
**C. Google App Engine Standard Environment**

✅ Justification for Correct Answers:

**B. Google Kubernetes Engine (GKE) using containers**

- GKE is a **managed Kubernetes service**, ideal for **cloud-native containerized workloads**.
- Supports **auto-scaling** at both the **pod** and **cluster** levels.
- Minimizes overhead by providing:
  - **Managed control plane**
  - Integration with **Cloud Monitoring, Logging**
- Enables modernization from VM-based apps to **microservices and container orchestration**.

**Relevant Docs:**

- Autopilot mode (for minimal ops): [https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview](https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

**C. Google App Engine Standard Environment**

- App Engine is a **fully managed serverless platform**, perfect for **no-ops** use cases.
- Automatically handles:
  - **Scaling**
  - **Instance provisioning**
  - **Load balancing**
- Excellent for running **web applications or APIs** with minimal infrastructure management.

**Relevant Docs:**

- App Engine Standard: [https://cloud.google.com/appengine/docs/the-appengine-environments](https://cloud.google.com/appengine/docs/the-appengine-environments)
- Auto-scaling in App Engine: [https://cloud.google.com/appengine/docs/standard#automatic_scaling](https://cloud.google.com/appengine/docs/standard#automatic_scaling)

❌ Why the Other Options Are Incorrect:

**A. Compute Engine running containerized workloads**

- Although you can run containers on VMs, this is **not cloud-native** compared to GKE or App Engine.
- Still requires **VM management**, patching, and monitoring.
- **Does not meet “minimal operational overhead”** requirement.

**D. Compute Engine with custom machine types**

- Custom machine types are useful for **cost optimization**, not for enabling **auto-scaling** or **no-ops**.
- Still tied to **VM management**, so not ideal for cloud-native transformation.

**E. Compute Engine with Managed Instance Groups (MIGs)**

- MIGs offer **auto-scaling**, but still operate at the **VM level**.
- Requires:
  - **Instance templates**
  - **OS patching**
  - **Application deployment logic**
- More operational overhead than **App Engine** or **GKE Autopilot**.

✅ Final Answer:

**B. Google Kubernetes Engine (GKE) using containers**
**C. Google App Engine Standard Environment**

---

## Question 51

*Domain 3: Designing for Security and Compliance*

A key objective for **DataSure Systems** is ensuring the **integrity and trustworthiness** of data stored in its application. To support this goal, the team wants to **log every change** made to application data and be able to **verify the authenticity** of those logs.

How should you design the logging system to ensure log authenticity?

- [ ] A. Simultaneously write each log entry to both a cloud-based system and an on-premises server
- [ ] B. Store the logs in a SQL database with strict access controls on who can modify the log table
- [x] C. Digitally sign each log entry along with its timestamp, and store the signature securely
- [ ] D. Export each log entry as a JSON file and save it to **Google Cloud Storage**

### Explanation

✅ Correct Answer:

**C. Digitally sign each log entry along with its timestamp, and store the signature securely**

✅ Justification for Option C:

- **Digital signatures** provide cryptographic assurance that:
  - The log entry hasn’t been tampered with.
  - The source is authentic.
- Signing each log entry ensures **non-repudiation** and **tamper detection**.
- When combined with **timestamps**, it also enables **chronological integrity**.
- This approach is consistent with **best practices in trusted logging systems**, particularly in security-sensitive or regulated environments.

**Google Reference** (while not specific to this use case, the general cryptographic best practice is emphasized):

- Google Cloud Key Management Service documentation – Sign Data
- Cloud Audit Logs Overview — for logging best practices including integrity considerations

❌ Justifications for Incorrect Options:

**A. Simultaneously write each log entry to both a cloud-based system and an on-premises server**

- While this may add redundancy, it does **not ensure authenticity** or tamper detection.
- Logs can still be altered at either location unless cryptographically protected.
- Adds complexity but **no guarantee of integrity**.

**B. Store the logs in a SQL database with strict access controls on who can modify the log table**

- Access control helps **prevent unauthorized modifications**, but:
  - It does **not prove log authenticity**.
  - A rogue administrator or compromised account could still modify logs.
- This lacks cryptographic protection and **cannot verify integrity retrospectively**.

**D. Export each log entry as a JSON file and save it to Google Cloud Storage**

- Storing logs in **Cloud Storage** can provide **immutability** if combined with Object Versioning and IAM.
- However, **JSON files alone are not authenticated** unless you also use **signatures or hashing**.
- Without digital signatures, this approach **fails to meet the authenticity requirement**.

✅ Final Answer:

**C. Digitally sign each log entry along with its timestamp, and store the signature securely**

This is the most robust and **cryptographically verifiable method** to ensure **log integrity and authenticity**.

---

## Question 52

*Domain 3: Designing for Security and Compliance*

**CloudOps Inc.** uses both a **Google Workspace account** and a **Google Cloud Organization**. However, some developers have been creating Google Cloud projects **outside the organization structure**.

You want to redesign the **Organization resource hierarchy** to:

- Allow developers to create their own projects
- Prevent them from modifying production projects
- Centralize policy management for all projects
- Apply **stricter policies** to production environments
- Minimize disruptions when business requirements evolve
- Follow **Google-recommended best practices**

How should you structure the organization?

- [ ] A.Create a second Google Workspace account and a new Cloud Organization Grant developers the **Project Creator** IAM role on the new Organization Move developer-owned projects into the new Organization Set organization-wide policies for both Organizations Apply production-specific policies on the original Organization
- [ ] B.Create a folder named **"Production"** under the Organization resource Grant developers the **Project Creator** role on the Organization Move developer projects into the Organization Set default policies at the Organization level Apply stricter policies at the **"Production"** folder level
- [x] C.Create two folders under the Organization: **"Development"** and **"Production"** Grant developers the **Project Creator** IAM role on the **"Development"** folder only Move developer projects into the **"Development"** folder Set baseline policies at the Organization level Apply more restrictive policies to the **"Production"** folder
- [ ] D.Reserve the Organization exclusively for production projects Ensure developers do **not** have the **Project Creator** role at the Organization level Allow developers to create development projects **outside** the Organization using their Workspace accounts Set policies at the Organization level for all production projects Apply specific production policies at the individual project level

### Explanation

✅ Correct Answer:

**C.**

Create two folders under the Organization: "Development" and "Production"
Grant developers the Project Creator IAM role on the "Development" folder only
Move developer projects into the "Development" folder
Set baseline policies at the Organization level
Apply more restrictive policies to the "Production" folder

✅ **Justification for Option C:**

This solution follows **Google Cloud’s best practices for resource hierarchy design**:

- **Use folders** to separate **environments** such as **Development** and **Production**.
- Grant **Project Creator** IAM role **only on the “Development” folder**, not the whole org — giving developers autonomy **without compromising production**.
- Apply **organization-wide baseline policies** (e.g., domain restriction, logging).
- Apply **stricter policies (e.g., deny roles, stricter access controls)** to the **Production folder**.
- This design is **centralized**, **scalable**, and **flexible** for future changes.

**Official Documentation References:**

- Google Cloud Resource Hierarchy Best Practices:
  https://cloud.google.com/resource-manager/docs/creating-managing-folders
  https://cloud.google.com/resource-manager/docs/creating-managing-organization
- Designing resource hierarchy for access control and policy management:
  https://cloud.google.com/docs/enterprise/best-practices-for-enterprise-org-structure

❌ Why the Other Options Are Incorrect:

**A. Create a second Google Workspace account and new Cloud Organization**

- **Not recommended** to use **multiple Organizations** to separate dev/prod.
- Splitting Orgs **fragments policy control** and **increases management complexity**.
- **Cross-organization management is not supported** for IAM/policies.

**B. Grant Project Creator at the Organization level**

- This gives **developers access to create projects anywhere**, including in Production, which **violates the goal of isolating prod**.
- While using a “Production” folder is correct, this **exposes prod risk**.

**D. Allow developers to create projects outside the Organization**

- **Defeats the goal of centralized policy management**.
- Projects outside the Organization:
  - **Cannot be governed** by Org policies
  - Are **invisible to Org Admins**
- Google **strongly recommends bringing all projects under a single Organization**.

✅ Final Answer:

**C. Create two folders under the Organization: "Development" and "Production"**
**Grant developers the Project Creator IAM role on the "Development" folder only**
**Move developer projects into the "Development" folder**
**Set baseline policies at the Organization level**
**Apply more restrictive policies to the "Production" folder**

---

## Question 53

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**SoundStream Inc.** runs a music streaming application on **Google Compute Engine**. The application lets users play their favorite songs, which are stored in **Cloud Storage** and streamed directly to users. The backend operates with a **fixed number of Compute Engine instances**.

Recently, users have reported intermittent failures when trying to play **popular songs**, often requiring multiple attempts before playback is successful. You need to **enhance the application’s performance and reliability**.

What should you do?

- [ ] A.Mount the Cloud Storage bucket using **gcsfuse** on each backend Compute Engine instance Serve music files directly from the backend instance
- [ ] B.Set up a **Cloud Filestore NFS volume** and attach it to the backend Compute Engine instances Download frequently played songs to the Filestore volume Serve music files directly from the backend instances
- [ ] C.Copy frequently accessed songs into **Cloud SQL** as BLOB data Modify the application to query **Cloud SQL** if Cloud Storage performance degrades
- [x] D.Create a **Managed Instance Group (MIG)** of Compute Engine instances Set up a **global external HTTP(S) load balancer** with two backends: The Managed Instance Group The Cloud Storage bucket **Enable Cloud CDN** on the Cloud Storage backend to cache popular content closer to users

### Explanation

✅ **Correct Answer:**

**D.**

Create a Managed Instance Group (MIG) of Compute Engine instances
Set up a global external HTTP(S) load balancer with two backends:

- The Managed Instance Group
- The Cloud Storage bucket

Enable Cloud CDN on the Cloud Storage backend to cache popular content closer to users

✅ **Why Option D is Correct:**

- This approach **offloads traffic** from your backend instances by allowing **popular content to be cached and served by Cloud CDN**.
- **Cloud CDN** integrates natively with **Cloud Storage-backed HTTP(S) load balancers**, allowing **edge caching** of frequently accessed music files.
- A **global HTTP(S) load balancer** ensures **resilience, routing optimization, and failover**, improving **availability and latency**.
- The **MIG** ensures your backend can auto-heal and scale in response to usage if needed.
- This approach combines **scalability**, **caching**, and **reliability** in a production-ready solution.

**Official Docs:**

- Cloud CDN with Cloud Storage: https://cloud.google.com/cdn/docs/setting-up-cdn-with-buckets
- Load balancing backend buckets: https://cloud.google.com/load-balancing/docs/backend-buckets
- Cloud CDN overview: https://cloud.google.com/cdn/docs/overview

❌ Justifications for Incorrect Options:

**A. Mount the Cloud Storage bucket using gcsfuse on each backend Compute Engine instance**

- `gcsfuse` **is not suitable for high-throughput, production-grade streaming**.
- It's best for **batch workloads or development**, and has **known performance limitations and consistency caveats**.
- You’d also be **reintroducing latency** and dependency on backend compute instances.

**Reference:**
https://cloud.google.com/storage/docs/gcs-fuse

**B. Use Cloud Filestore and download frequently played songs**

- **Cloud Filestore** is an NFS solution intended for low-latency, POSIX-compatible access—not for **serving content to end-users over the internet**.
- Downloading songs manually increases **operational overhead**.
- Doesn’t scale well or leverage **caching at the edge**, unlike Cloud CDN.

**Reference:**
https://cloud.google.com/filestore/docs/overview

**C. Store frequently accessed songs in Cloud SQL as BLOBs**

- **Cloud SQL is not designed for storing and streaming media files**.
- Large BLOBs in SQL databases **impact performance, storage cost, and query efficiency**.
- Adds complexity without solving the core issue.

**Reference:**
https://cloud.google.com/sql/docs/introduction (BLOBs discouraged for media content)

✅ Final Answer:

**D. Create a Managed Instance Group (MIG) and set up a global external HTTP(S) load balancer with Cloud CDN enabled on the Cloud Storage backend**

This provides the best combination of **performance, scalability, and operational simplicity**.

---

## Question 54

*Domain 3: Designing for Security and Compliance*

The **IT operations team at NetSecure Corp.** wants to **retain Cloud VPN log events for one year** to support compliance and auditing needs. You need to configure Google Cloud to store these logs appropriately.

What should you do?

- [x] A. Create a **log sink** in Cloud Logging with a filter for Cloud VPN logs, and set a **Cloud Storage bucket** as the destination to store logs long term.
- [ ] B. Enable the **Compute Engine API**, and configure logging on firewall rules that match VPN traffic.
- [ ] C. Create a **Cloud Logging Dashboard** named “Cloud VPN Logs,” and add a chart that visualizes VPN metrics for the past year.
- [ ] D. Set up a **Cloud Logging filter** and create a **Pub/Sub topic** to publish selected log entries.

### Explanation

✅ Correct Answer:

**A. Create a log sink in Cloud Logging with a filter for Cloud VPN logs, and set a Cloud Storage bucket as the destination to store logs long term.**

✅ Justification:

- **Cloud Logging** by default retains logs for **30 days (for user logs)** unless you export them.
- To **retain logs for 1 year**, you must **export** them using a **log sink**.
- The most cost-effective and compliance-friendly destination for long-term storage is a **Cloud Storage bucket**, which supports **custom retention policies** (e.g., 1 year).
- You can filter for **Cloud VPN logs** using a **log sink filter** like:
  ```
  resource.type="gce_vpn_gateway"
  ```

**Official Documentation:**

- Log Retention and Export: [https://cloud.google.com/logging/docs/export](https://cloud.google.com/logging/docs/export)
- VPN Logging: [https://cloud.google.com/network-connectivity/docs/vpn/how-to/logging](https://cloud.google.com/network-connectivity/docs/vpn/how-to/logging)
- Exporting logs to Cloud Storage: [https://cloud.google.com/logging/docs/export/storage](https://cloud.google.com/logging/docs/export/storage)

❌ Why Other Options Are Incorrect:

**B. Enable the Compute Engine API and configure logging on firewall rules that match VPN traffic**

- Firewall logging only captures **traffic metadata for firewall rule matches**, not **Cloud VPN tunnel state or events**.
- VPN logs come from **VPN Gateway resources**, not firewall rules.
- This does **not guarantee VPN-specific logs** or long-term storage.

**Reference:**
[https://cloud.google.com/vpc/docs/firewall-rules-logging](https://cloud.google.com/vpc/docs/firewall-rules-logging)
[https://cloud.google.com/network-connectivity/docs/vpn/how-to/logging](https://cloud.google.com/network-connectivity/docs/vpn/how-to/logging)

**C. Create a Cloud Logging Dashboard named “Cloud VPN Logs,” and add a chart that visualizes VPN metrics for the past year**

- Dashboards are for **visualization**, not **log storage**.
- Logging dashboards display up to **30 days** of log-based metrics by default.
- Does **not meet the retention requirement** of **1 year**.

**D. Set up a Cloud Logging filter and create a Pub/Sub topic to publish selected log entries**

- Exporting to **Pub/Sub** is typically used for **real-time streaming or processing** (e.g., with Dataflow), not long-term archival.
- Pub/Sub **does not store messages indefinitely**—it only retains them for up to **7 days**.

**Reference:**
[https://cloud.google.com/logging/docs/export/pubsub](https://cloud.google.com/logging/docs/export/pubsub)
[https://cloud.google.com/pubsub/docs/overview#features](https://cloud.google.com/pubsub/docs/overview#features)

✅ Final Answer:

**A. Create a log sink in Cloud Logging with a filter for Cloud VPN logs, and set a Cloud Storage bucket as the destination to store logs long term.**

---

## Question 55

*Domain 3: Designing for Security and Compliance*

You are collaborating with the **data warehousing team at DataWise Analytics**, which conducts analytical processing on incoming data. The team needs to handle data received from **external partners**, but this data includes **personally identifiable information (PII)**. The goal is to **process and store the data without retaining any PII**.

What should you do?

- [x] A. Build a **Dataflow pipeline** to ingest data from external sources. Within the pipeline, use the **Cloud Data Loss Prevention (Cloud DLP) API** to detect and remove PII. Store the cleansed data in **BigQuery**.
- [ ] B. Design a **Dataflow pipeline** that stores non-PII data in **BigQuery**, and stores PII data in a **Cloud Storage bucket** with a **retention policy** configured.
- [ ] C. Request external partners to upload data to **Cloud Storage**, and apply **Bucket Lock** on the bucket. Use a **Dataflow pipeline** to read from the bucket, apply **Cloud DLP** to strip PII, and then store the results in **BigQuery**.
- [ ] D. Ask partners to import their data directly into your **BigQuery dataset**. Then, use a **Dataflow pipeline** to copy the data into a new table, skipping all columns that may contain PII.

### Explanation

✅ Correct Answer:

**A. Build a Dataflow pipeline to ingest data from external sources. Within the pipeline, use the Cloud Data Loss Prevention (Cloud DLP) API to detect and remove PII. Store the cleansed data in BigQuery.**

✅ Justification for Option A:

- **Cloud DLP** is specifically designed to:
  - **Inspect**, **de-identify**, **mask**, or **redact** PII (like names, SSNs, emails).
- Integrating **Cloud DLP** within a **Dataflow pipeline** allows you to **automatically detect and remove PII during ingestion**.
- Once the data is cleaned, you can **safely store it in BigQuery** for analytics.
- This ensures full compliance with **privacy** and **data minimization** principles.

**Official Docs:**

- Cloud DLP Overview: [https://cloud.google.com/dlp/docs](https://cloud.google.com/dlp/docs)

❌ Justifications for Incorrect Options:

**B. Dataflow pipeline stores non-PII in BigQuery and PII in Cloud Storage with retention**

- This still involves **storing PII**, even if temporarily.
- The requirement clearly states: **“without retaining any PII”**
- Violates the directive of **not keeping PII at all**

**C. Use Bucket Lock + Cloud DLP after storage**

- Uploading data **with PII directly into Cloud Storage** (even with Bucket Lock) **means PII is retained** during that period.
- **DLP is applied *after* storage**, which conflicts with the goal to **never retain PII**.
- **Bucket Lock** is for **immutability**, not for PII protection.

**D. Partners import into BigQuery, then copy excluding PII columns**

- **Risky and non-compliant approach**: PII is **already in BigQuery**, even temporarily.
- **Violates the "no retention" requirement**
- Also depends on partners to comply with schema expectations—less reliable

✅ Final Answer:

**A. Build a Dataflow pipeline to ingest data from external sources. Within the pipeline, use the Cloud DLP API to detect and remove PII. Store the cleansed data in BigQuery.**

---

## Question 56

*Domain 6: Ensuring Solution and Operations Excellence*

At **OpsBridge Corp.**, the operations team needs access to **logs from all production projects** within the Google Cloud Organization. These production projects are grouped under a specific **folder** in the organization structure. The goal is to **automatically collect logs from all current and future production projects**, without including logs from non-production projects.

What should you do to meet these requirements?

- [x] A. Create an **aggregated log export** at the **Production folder** level. Set the **log sink** destination to a **Cloud Storage bucket** in a centralized operations project.
- [ ] B. Create an **aggregated log export** at the **Organization** level. Set the **log sink** destination to a **Cloud Storage bucket** in an operations project.
- [ ] C. Create **individual log exports** in each production project. Set the **log sinks** to write logs to a **Cloud Storage bucket** in the operations project.
- [ ] D. Create **log exports** in each production project that write to **BigQuery datasets** in the same projects. Grant the **operations team IAM access** to query these datasets.

### Explanation

✅ Correct Answer:

**A. Create an aggregated log export at the Production folder level. Set the log sink destination to a Cloud Storage bucket in a centralized operations project.**

✅ **Why Option A is Correct:**

- **Folder-level aggregated log sinks** automatically apply to **all projects within that folder**, including **future projects**.
- Since all **production projects** are grouped under one folder, exporting logs at the **folder level** precisely targets the required scope.
- **Aggregated log exports** can include logs from **child resources** (projects) within the folder.
- Exporting to a **centralized Cloud Storage bucket** in an operations project allows central visibility and management.

**Official Documentation:**

- Aggregated exports: Export logs for an entire folder
- Create and manage log sinks

❌ Why Other Options Are Incorrect:

**B. Organization-level log export**

- This exports **logs from all projects in the entire organization**, including **non-production** ones.
- Fails to meet the requirement to **exclude non-production logs**.
- Over-collects and can introduce **noise and compliance concerns**.

**C. Individual log exports in each production project**

- Requires **manual setup per project** and **manual updates** as new projects are added.
- **Does not scale** and **fails automation** requirement.
- Higher chance of **inconsistency or misconfiguration**.

**D. Export to BigQuery datasets in each project + IAM access**

- Again, requires **manual configuration per project**.
- Adds complexity with **IAM configuration on multiple datasets**.
- Harder to **centralize** visibility and maintain **long-term governance**.

✅ Final Answer:

**A. Create an aggregated log export at the Production folder level. Set the log sink destination to a Cloud Storage bucket in a centralized operations project.**

This satisfies all requirements: targeted, automated, scalable, and aligned with Google Cloud best practices.

---

## Question 57

*Domain 3: Designing for Security and Compliance*

**LogiTrack Inc.** runs an application on multiple **Compute Engine instances**, generating approximately **1 TB of log data per day**. For **compliance**, the logs must be retained for **at least two years**. However, logs only need to be **actively queryable for the first 30 days**—after that, they should simply be **retained for audit purposes**.

You need to implement a **cost-efficient and compliant** logging solution that aligns with **Google Cloud's best practices**.

What should you do?

- [x] A.Install the **Cloud Logging agent** on all Compute Engine instances Create a **log sink** that exports logs to a **regional Cloud Storage bucket** Set an **Object Lifecycle rule** to move logs to **Coldline Storage** after 30 days Apply a **bucket retention policy** using **Bucket Lock** to enforce two-year retention
- [ ] B.Write a **cron job** on each instance to upload daily logs to a Cloud Storage bucket Create a **log sink** to export logs to a **regional Cloud Storage bucket** Set an **Object Lifecycle rule** to move logs to **Coldline Storage** after one month
- [ ] C.Install the **Cloud Logging agent** on all instances Export logs to a **partitioned BigQuery table** using a log sink Set **time_partitioning_expiration** to **30 days** for automatic pruning
- [ ] D.Create a **daily cron job** on each instance to upload logs into a **partitioned BigQuery table** Set **time_partitioning_expiration** to 30 days to delete old partitions

### Explanation

✅ Correct Answer:

**A.**

Install the Cloud Logging agent on all Compute Engine instances
Create a log sink that exports logs to a regional Cloud Storage bucket
Set an Object Lifecycle rule to move logs to Coldline Storage after 30 days
Apply a bucket retention policy using Bucket Lock to enforce two-year retention

✅ Why Option A is Correct:

This solution meets all objectives:

1. **High Volume Logging (~1 TB/day)**

- Google Cloud Logging agent collects logs efficiently.
- Exporting to **Cloud Storage** handles large volume logs at **low cost**.

2. **30-Day Queryability**

- You can access logs in **Cloud Logging** for 30 days (default retention).
- After that, logs are **available in Cloud Storage** for compliance—but not actively queried.

3. **Cost-Efficiency**

- Moving logs to **Coldline Storage** (via Lifecycle Rules) reduces long-term storage costs.
- Cloud Storage is **cheaper than BigQuery** for storing logs not being queried.

4. **2-Year Retention (Compliance)**

- Apply a **retention policy using Bucket Lock**, which:
  - Prevents deletion or modification
  - Is **compliant with regulatory requirements** such as audit and legal holds

**Official Documentation:**

- Exporting logs to Cloud Storage
- Bucket Lock & Retention Policies
- Cloud Storage Lifecycle Rules
- Cloud Logging Agent

❌ Why Other Options Are Incorrect:

**B. Cron job to upload logs + export to Storage + lifecycle rules**

- Unnecessarily **duplicates log upload** effort—both **manual upload** and **log sink export**.
- Increases **operational overhead** and **risk of inconsistency**.
- Not scalable for 1 TB/day.

**C. Export logs to BigQuery with 30-day expiration**

- **BigQuery** is powerful for analytics, but:
  - **Expensive** for long-term storage of large log volumes
  - After 30 days, logs are **deleted**, which **violates the 2-year retention requirement**
- **No long-term archival** after logs expire

**D. Cron job to upload logs into BigQuery with 30-day expiration**

- Similar to Option C, but also uses **manual upload**, which is **inefficient** at 1 TB/day.
- Again, logs **expire after 30 days**, violating **compliance** needs.

✅ Final Answer:

**A. Install the Cloud Logging agent on all Compute Engine instances**
**Create a log sink that exports logs to a regional Cloud Storage bucket**
**Set an Object Lifecycle rule to move logs to Coldline Storage after 30 days**
**Apply a bucket retention policy using Bucket Lock to enforce two-year retention**

This is **cost-efficient, compliant, and aligned with Google Cloud’s recommended practices**.

**⚠️ Note:** The legacy Cloud Logging agent is replaced by the Ops Agent; the design (sink to Cloud Storage, lifecycle to Coldline, locked retention) is unchanged.

---

## Question 58

*Domain 3: Designing for Security and Compliance*

**SecuGuard Ltd.** has recently enabled **Cloud Identity** to manage its user accounts and has also configured its **Google Cloud Organization**. The **security team** now wants to **secure all projects** within the Organization by **preventing IAM users outside the company’s Cloud Identity domain from being granted permissions** moving forward.

What is the most appropriate action to take?

- [x] A. Configure an **Organization Policy** to **restrict identities by domain** to ensure only users from the company's Cloud Identity domain can be granted IAM roles.
- [ ] B. Set an **Organization Policy** to **block the creation of service accounts** across all projects.
- [ ] C. Use **Cloud Scheduler** to trigger a **Cloud Function** every hour that scans IAM policies and removes users who are not part of the company domain.
- [ ] D. Create a technical service account (e.g., `crawler@yourdomain.com`) and assign it the **Project Owner** role at the Organization level. Then, write a **bash script** that: Lists IAM policies of all projects Deletes users not in the company domain Deploy this script on a **Compute Engine VM** and run it using a **cron job every hour**.

### Explanation

✅ **Correct Answer:**

**A. Configure an Organization Policy to restrict identities by domain to ensure only users from the company's Cloud Identity domain can be granted IAM roles.**

✅ **Why Option A is Correct:**

Google Cloud provides an **Organization Policy constraint** named:

```
constraints/iam.allowedPolicyMemberDomains
```

This constraint allows an **Organization Administrator** to **restrict IAM principals** to specific identity domains—e.g., only `@secuguard.com` users.

When enforced:

- IAM policies **cannot be updated** to include **external identities**.
- It **prevents violations proactively**, rather than relying on reactive cleanups.
- Applies at the **Organization level** and can inherit to **all folders/projects**.

This satisfies SecuGuard's goal of **ensuring only internal users** (from their Cloud Identity domain) can be granted IAM roles.

**Official Documentation:**

- Restricting IAM policies by domain
- constraints/iam.allowedPolicyMemberDomains

❌ Why Other Options Are Incorrect:

**B. Set an Organization Policy to block the creation of service accounts**

- This **does not prevent external users from being granted IAM roles**.
- **Service accounts** are internal identities and may still be needed for automation.
- Not aligned with the core requirement (controlling **user** identities by **domain**).

**C. Use Cloud Scheduler + Cloud Function to remove external users**

- This is a **reactive workaround**, not a preventive control.
- May lead to **security gaps** (e.g., external users having temporary access between scans).
- **Complex**, **hard to maintain**, and not Google-recommended.

**D. Use a bash script on a Compute Engine VM to remove external users via cron**

- Similar to option C, but even worse:
  - Requires full **Project Owner** privileges
  - Introduces **operational risk and complexity**
  - Lacks **granular auditing**, and prone to **errors**
- Not a scalable or **policy-driven solution**

✅ Final Answer:

**A. Configure an Organization Policy to restrict identities by domain to ensure only users from the company's Cloud Identity domain can be granted IAM roles.**

---

## Question 59

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**EdgeSense Corp.** runs an application on **Google Cloud** that collects data from **thousands of globally distributed IoT devices**. The incoming data is published to **Pub/Sub** and streamed in real time into a **Cloud Bigtable SSD cluster** via a **Dataflow pipeline**.

Recently, the operations team reported that the **Cloud Bigtable cluster is experiencing a hotspot**, causing query performance to degrade.

You need to resolve the issue and ensure it doesn’t recur in the future.

What should you do?

- [ ] A. Instruct clients to switch from using **Node.js APIs** to **HBase APIs** for data interaction.
- [ ] B. Implement logic to **delete records older than 30 days** from the Bigtable cluster.
- [x] C. **Revisit your RowKey design** and ensure the keys are **evenly distributed** across the alphabet to avoid hotspots.
- [ ] D. **Double the number of nodes** in the Cloud Bigtable cluster to distribute the load more evenly.

### Explanation

✅ Correct Answer:

**C. Revisit your RowKey design and ensure the keys are evenly distributed across the alphabet to avoid hotspots.**

✅ Why Option C is Correct:

- **RowKey design** is the **most critical factor** in avoiding hotspots in Cloud Bigtable.
- Bigtable stores rows **lexicographically**, so sequential or predictable keys (e.g., timestamps, device IDs) will cause **hotspots** by directing too many writes to the same tablet/server.
- To fix this, you should:
  - **Randomize prefixes**
  - Use **salting** or **hash-based prefixes**
  - Avoid monotonically increasing keys (e.g., raw timestamps)

**Official Documentation:**

- Cloud Bigtable Schema Design Best Practices
- Avoiding Hotspots

❌ Why Other Options Are Incorrect:

**A. Instruct clients to switch from using Node.js APIs to HBase APIs for data interaction**

- The **API used has no impact on hotspotting**.
- This would introduce **development effort** without solving the underlying issue.

**B. Implement logic to delete records older than 30 days**

- Data retention is important, but **hotspotting is caused by how data is written**, not how old it is.
- Deletion of old data does **not improve key distribution** or prevent hotspots.

**D. Double the number of nodes in the Cloud Bigtable cluster**

- Adding nodes **increases capacity**, but:
  - If RowKey design is poor, **data will still funnel into a small number of nodes**, and hotspots will remain.
  - This is a **costly and temporary workaround**, not a fix.

✅ Final Answer:

**C. Revisit your RowKey design and ensure the keys are evenly distributed across the alphabet to avoid hotspots.**

This is the **best practice recommended by Google** to resolve and prevent **Cloud Bigtable performance issues due to hotspotting**.

---

## Question 60

*Domain 3: Designing for Security and Compliance*

**DataSecure Inc.** uses **BigQuery** for its data warehousing needs. Some of the datasets contain **personally identifiable information (PII)** that should be **accessible only to the compliance team**. However, the **data science team** needs access to the **non-PII data** in the same tables.

You want to **minimize both cost and administrative overhead** when granting the appropriate access to each team.

What should you do?

- [ ] A.In the source dataset, create **views** of the tables that **exclude PII fields** Grant the data science team an appropriate **project-level IAM role** Set **access controls** on the dataset containing the views
- [ ] B.In the source dataset, create **materialized views** of the tables that **exclude PII fields** Grant the data science team an appropriate **project-level IAM role** Set **access controls** on the dataset containing the views
- [x] C.Create a **separate dataset** for the data science team In that dataset, create **views** of the tables that **exclude PII** Assign a **project-level IAM role** to the data science team Set **access controls** on the new dataset **Authorize the view** to access the original dataset
- [ ] D.Create a **separate dataset** for the data science team In that dataset, create **materialized views** of the tables that **exclude PII** Assign a **project-level IAM role** to the data science team Set **access controls** on the new dataset **Authorize the view** to access the original dataset

### Explanation

✅ Correct Answer:

**C.**

Create a separate dataset for the data science team
In that dataset, create **views** of the tables that exclude PII
Assign a **project-level IAM role** to the data science team
Set access controls on the **new dataset**
Authorize the view to access the original dataset

✅ Why Option C is Correct:

- **Views** in BigQuery are **logical representations** of data and do **not incur additional storage or compute costs** until queried.
- By creating views that **exclude PII columns**, you **safely isolate sensitive data**.
- Placing these views in a **separate dataset** allows you to apply **fine-grained IAM controls** specifically for the data science team.
- The **authorized views mechanism** lets views in one dataset access data in another while enforcing column-level security.

This method:

- **Meets privacy requirements**
- **Minimizes cost** (compared to materialized views)
- **Keeps admin overhead low** (IAM at dataset/view level is simple and scalable)

**Key Google Docs:**

- Authorized views in BigQuery
- Controlling access to datasets
- Views vs. materialized views

❌ Why Other Options Are Incorrect:

**A. Views in the source dataset + project-level IAM role**

- Creating views in the **same source dataset** does **not provide strong separation** of access control.
- IAM permissions at the dataset level can inadvertently expose underlying PII data.
- **Best practice is to put views in a separate dataset** to fully leverage authorized views.

**B. Materialized views in the source dataset**

- **Materialized views incur storage and compute costs** as they precompute and store results.
- Also shares the **same problem as A**: being in the **same dataset** as the source, which complicates access control.

**D. Materialized views in a separate dataset**

- While access control is better than B, **materialized views are unnecessary and more expensive** for the requirement.
- Views suffice when you just need to **hide PII columns** without performance optimization.

✅ Final Answer:

**C. Create a separate dataset for the data science team. In that dataset, create views of the tables that exclude PII. Assign a project-level IAM role to the data science team. Set access controls on the new dataset. Authorize the view to access the original dataset.**

---

## Question 61

*Domain 5: Managing Implementation*

The **CloudOps team at SkyNet Solutions** currently stores **10 TB of data** in an **object storage service provided by a third party**. They want to **migrate this data to a Google Cloud Storage bucket** as quickly and **cost-effectively** as possible, while adhering to **Google-recommended best practices**.

What is the best approach to meet these requirements?

- [ ] A. Use the `gsutil mv` command to transfer the data to Cloud Storage.
- [x] B. Use **Storage Transfer Service** to migrate the data directly to a Cloud Storage bucket.
- [ ] C. Transfer the data to a **Transfer Appliance**, then ship it to Google for ingestion.
- [ ] D. **Download the data** to an **on-premises data center**, then upload it to Cloud Storage manually.

### Explanation

✅ Correct Answer:

**B. Use Storage Transfer Service to migrate the data directly to a Cloud Storage bucket.**

✅ Why Option B is Correct:

- **Storage Transfer Service (STS)** is **Google Cloud’s fully managed service** for transferring data from:
  - **AWS S3**
  - **Azure Blob Storage**
  - **Other HTTP/HTTPS-based storage services**
- Ideal for **large-scale transfers** (10 TB+) and designed to be:
  - **Fast** with parallelism
  - **Reliable** with retry mechanisms
  - **Cost-effective** since no intermediate storage or manual downloads are needed
- Supports **scheduling**, **filters**, and **data synchronization**, and follows **Google Cloud best practices**.

**Official Documentation:**

- Storage Transfer Service Overview
- Supported sources for Storage Transfer Service

❌ Why Other Options Are Incorrect:

**A. Use the `gsutil mv` command**

- `gsutil mv` is intended for **moving** files **between buckets** or **from local storage** to GCS.
- It **does not support third-party cloud object storage** directly.
- It requires **data to be local first**, which adds **latency and bandwidth cost**.
- Not scalable for **10 TB**, and not Google-recommended for third-party transfers.

**Reference:**
[https://cloud.google.com/storage/docs/gsutil/commands/mv](https://cloud.google.com/storage/docs/gsutil/commands/mv)

**C. Use Transfer Appliance**

- **Transfer Appliance** is designed for **extremely large datasets (100+ TB)** that cannot be moved over the network efficiently.
- For 10 TB, **network-based migration (STS)** is faster and more cost-effective.
- Using the appliance adds unnecessary **logistics, shipping time, and complexity**.

**D. Download to on-prem and upload manually**

- Highly **inefficient** and **time-consuming** for 10 TB of data.
- Introduces unnecessary **network egress costs** and **administrative overhead**.
- Not scalable or aligned with **cloud-native migration best practices**.

✅ Final Answer:

**B. Use Storage Transfer Service to migrate the data directly to a Cloud Storage bucket.**

---

## Question 62

*Domain 6: Ensuring Solution and Operations Excellence*

You manage a **Compute Engine managed instance group** at **AppScale Corp.**, which automatically **scales instances up and down** based on application load. Each instance runs a **shutdown script** that is supposed to **clean up REDIS database entries** associated with that instance.

However, you've noticed that many REDIS entries remain after instance shutdowns, and you suspect the **shutdown script is not executing reliably**. To fix this, you've created a **Cloud Function** that can remove the REDIS entries.

What should you do next to **ensure reliable cleanup every time an instance is shut down**?

- [ ] A. Update the shutdown script to wait for 30 seconds before calling the Cloud Function.
- [ ] B. Discard the Cloud Function approach and instead modify the shutdown script to automatically retry if it doesn't complete within 30 seconds.
- [x] C. Configure a **Cloud Monitoring log-based alert or sink** to **trigger the Cloud Function** whenever an **instance removal log entry** is detected in **Cloud Logging**.
- [ ] D. Change the shutdown script to **wait 30 seconds**, then **publish a message to a Pub/Sub topic**, triggering downstream cleanup.

### Explanation

✅ **Correct Answer:**

**C. Configure a Cloud Monitoring log-based alert or sink to trigger the Cloud Function whenever an instance removal log entry is detected in Cloud Logging.**

✅ **Why Option C is Correct:**

- When a Compute Engine VM in a MIG is deleted or terminated, a log entry is written to **Cloud Logging** (e.g., `"compute.instances.delete"` or `"compute.instances.shutdown"`).
- You can create a **log-based sink** or **alerting policy** that triggers a **Cloud Function** whenever such an event is logged.
- This approach is:
  - **Reliable** – works even if the shutdown script fails or times out
  - **Decoupled** – cleanup does not rely on the instance being healthy or responsive during shutdown
  - **Cloud-native** – aligns with **event-driven architecture** using **Cloud Logging + Cloud Functions**

**Official Docs:**

- Log-based alerts
- Triggering Cloud Functions from Cloud Logging

❌ **Why the Other Options Are Incorrect:**

**A. Update the shutdown script to wait for 30 seconds before calling the Cloud Function**

- Adding a delay **does not guarantee execution** of the shutdown script.
- If the instance is terminated abruptly or the script fails, the **Cloud Function won't be called**.
- **Still unreliable** for critical cleanup.

**B. Discard the Cloud Function and retry the shutdown script logic**

- Doubling down on the shutdown script **misses the root issue**: it's inherently unreliable in forceful shutdowns.
- Retry logic **within the instance** doesn’t help if the instance is gone before the script finishes.

**D. Change the shutdown script to wait 30 seconds, then publish a message to a Pub/Sub topic**

- Again, **relies on the shutdown script running correctly** and the instance surviving long enough.
- If shutdown is forceful, Pub/Sub message may **never be published**.

✅ **Final Answer:**

**C. Configure a Cloud Monitoring log-based alert or sink to trigger the Cloud Function whenever an instance removal log entry is detected in Cloud Logging.**

This solution ensures **reliable, event-driven cleanup** of REDIS entries, regardless of how or when the instance shuts down.

**⚠️ Note:** Strictly, the trigger is a Cloud Logging sink that routes the instance-removal audit log entry to Pub/Sub (or an Eventarc trigger on that audit log), which invokes the function. Cloud Functions is now Cloud Run functions.

---

## Question 63

*Domain 5: Managing Implementation*

You are managing **multiple Google Cloud projects** at **CloudFleet Corp.** and need to work regularly with **BigQuery**, **Cloud Bigtable**, and **Google Kubernetes Engine (GKE)** using the **gcloud CLI**. Since you frequently **travel and switch between different workstations**, you want to avoid the overhead of manually managing the gcloud installation on each machine.

What is the **best way** to interact with Google Cloud services without managing gcloud manually on every device?

- [x] A. Use **Google Cloud Shell** from the Google Cloud Console to access gcloud from any browser, without installing anything locally.
- [ ] B. Set up a **Compute Engine VM**, install gcloud there, and SSH into the instance from any device to run gcloud commands.
- [ ] C. Install gcloud on all workstations and run `gcloud components auto-update` on each machine to keep it up to date.
- [ ] D. Use a **package manager** (like apt, yum, or brew) to install gcloud on each workstation instead of installing it manually.

### Explanation

✅ **Correct Answer:**

**A. Use Google Cloud Shell from the Google Cloud Console to access gcloud from any browser, without installing anything locally.**

✅ **Why Option A is Correct:**

- **Google Cloud Shell** is a **browser-based shell environment** with the `gcloud` CLI and other tools (e.g., `kubectl`, `bq`, `git`) **pre-installed and always up-to-date**.
- You can access it **from any device with a browser**, which is ideal for a **mobile/remote work setup**.
- It **requires no local setup or maintenance**, removing overhead entirely.
- It offers:
  - **5 GB persistent disk**
  - Integrated editor
  - Secure access to Google Cloud resources

**Official Documentation:**

- Google Cloud Shell Overview

❌ Why Other Options Are Incorrect:

**B. Set up a Compute Engine VM with gcloud installed**

- Adds **unnecessary cost and complexity**:
  - VM charges (compute, network, storage)
  - Requires secure access setup and maintenance
- Still requires **manual gcloud installation and updates** on the VM

**C. Install gcloud and use auto-update on each machine**

- Defeats the purpose of the question (avoiding manual management).
- Requires **installing and updating** `gcloud` across **all workstations**, which is **tedious and error-prone**.

**D. Use package managers (apt, yum, brew) to install gcloud**

- While easier than manual installation, it still requires:
  - **Installation on every device**
  - Periodic updates to keep versions consistent
- **Does not eliminate setup and maintenance overhead**

✅ **Final Answer:**

**A. Use Google Cloud Shell from the Google Cloud Console to access gcloud from any browser, without installing anything locally.**

---

## Question 64

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**CloudLink Inc.** has recently acquired **NetFusion Ltd.**, and both companies operate their infrastructure on **Google Cloud**, each within its **own Google Cloud Organization**. Both organizations use **Shared VPCs** to manage network connectivity for their applications.

Some of the **subnets in both environments overlap**, but the applications that need to communicate **do not reside in the overlapping subnets**. You are tasked with enabling **private network connectivity** between these applications with **minimal re-engineering**.

What should you do?

- [ ] A. Set up **VPC Network Peering** between the two Shared VPCs.
- [ ] B. **Migrate the acquired company's projects** into your organization's Cloud Organization, and **relaunch the instances** into your Shared VPC.
- [x] C. Set up a **Cloud VPN gateway** in each Shared VPC and **establish a VPN connection** between them.
- [ ] D. Use **SSH port forwarding** to connect applications between the two Shared VPCs.

### Explanation

✅ Correct Answer:

**C. Set up a Cloud VPN gateway in each Shared VPC and establish a VPN connection between them.**

✅ Why Option C is Correct:

- **Cloud VPN** is supported for **cross-organization connectivity** and **works between Shared VPC networks**.
- It **allows private, secure communication** over the public internet, or via **Cloud Interconnect** if needed.
- **Subnets can overlap** as long as the communicating instances are in **non-overlapping IP ranges**.
- **Minimal re-engineering** is needed:
  - No need to migrate projects
  - No need to redesign or merge networks
- It's a **Google-recommended approach** for inter-org connectivity when peering is not viable due to constraints like overlapping IP ranges.

**Official Documentation:**

- VPN Overview
- Connecting VPC networks across organizations

❌ Why Other Options Are Incorrect:

**A. Set up VPC Network Peering between the two Shared VPCs**

- **Not supported** across different organizations when **IP address ranges overlap**, even partially.
- VPC Peering does **not support transitive routing**, and **Shared VPCs themselves cannot be directly peered across orgs** in overlapping IP scenarios.

**Reference:**
[https://cloud.google.com/vpc/docs/vpc-peering#restrictions](https://cloud.google.com/vpc/docs/vpc-peering#restrictions)

**B. Migrate the acquired company's projects into your organization's Cloud Organization and relaunch the instances**

- This involves **significant re-engineering**:
  - Project migration
  - Instance re-creation
  - Network and IAM reconfiguration
- **High risk**, **time-consuming**, and unnecessary for simple private connectivity.

**D. Use SSH port forwarding to connect applications between the two Shared VPCs**

- **Not a scalable or secure solution**
- Requires:
  - Manual port forwarding setups
  - SSH access and credentials
  - Custom scripts and maintenance
- **Not enterprise-grade** or compliant for production workloads

✅ Final Answer:

**C. Set up a Cloud VPN gateway in each Shared VPC and establish a VPN connection between them.**

---

## Question 65

*Domain 6: Ensuring Solution and Operations Excellence*

You are responsible for managing several **internal applications running on Google Compute Engine** at **IntraTech Solutions**. Recently, some **business users** reported that one of the applications has become **significantly slower** over the last few days.

To troubleshoot and address the issue, what is the **first step** you should take?

- [x] A. Check **Cloud Logging** and **Cloud Monitoring** to inspect logs and performance metrics from the Compute Engine instances.
- [ ] B. Upgrade the machine type for the Compute Engine instances to provide **more CPU and memory**.
- [ ] C. **Restore a backup** of the application’s database from a time when performance was not an issue.
- [ ] D. Redeploy the application using a **Managed Instance Group with autoscaling**, and place a **load balancer** in front of the group. Have users access the application through the load balancer's IP address.

### Explanation

✅ Correct Answer:

**A. Check Cloud Logging and Cloud Monitoring to inspect logs and performance metrics from the Compute Engine instances.**

✅ **Why Option A is Correct:**

- **Cloud Monitoring** provides **metrics** like:
  - CPU utilization
  - Memory usage
  - Disk I/O
  - Network traffic
- **Cloud Logging** shows application logs and system logs, which may reveal:
  - Errors
  - Latency spikes
  - Unusual behavior

Using these tools allows you to:

- **Identify the root cause** before taking further action
- Make **data-driven decisions** on whether to scale, fix bugs, or reconfigure

This is the **recommended first step in the Google Cloud troubleshooting process**.

**Official Docs:**

- Cloud Monitoring Overview
- Cloud Logging Overview

❌ Why Other Options Are Incorrect:

**B. Upgrade the machine type for the Compute Engine instances**

- Premature optimization without knowing the root cause.
- Could increase cost without resolving the issue if it's not resource-related.

**C. Restore a backup of the application’s database**

- This action assumes a database corruption or data issue without confirmation.
- May result in **data loss** and **service disruption**.
- Not appropriate until you've **confirmed it's a DB issue**.

**D. Redeploy with Managed Instance Group and Load Balancer**

- This is a **scaling and high availability solution**, not a first troubleshooting step.
- Adds complexity and cost without confirming the cause of the slowdown.

✅ Final Answer:

**A. Check Cloud Logging and Cloud Monitoring to inspect logs and performance metrics from the Compute Engine instances.**

---
