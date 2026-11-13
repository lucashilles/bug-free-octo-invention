# Professional Cloud Developer — Practice Exam 6

16 questions.

## Question 1

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Your ecommerce application is rapidly gaining new users, resulting in performance issues caused by a high volume of requests to your backend API. This API, which your team maintains, connects to a Cloud SQL database that is currently overwhelmed, leading to high latency and frequent timeouts. You need to find a solution to optimize API performance and enhance the user experience.**

**What approach should you take?**

- [x] A. Use Apigee to expose your API, integrate Memorystore for Redis to cache frequently requested data, and implement exponential backoff in the application to retry failed requests.
- [ ] B. Use Apigee to manage your API, apply rate limiting and access control policies in Apigee to regulate API traffic, and utilize Pub/Sub to queue requests and reduce database load.
- [ ] C. Expose your API through Cloud Load Balancing, place Cloud CDN in front of the load balancer to cache responses, and incorporate exponential backoff for retrying failed requests.
- [ ] D. Use Cloud Load Balancing to expose your API, increase the database instance memory to support more concurrent requests, and build a custom rate-limiting mechanism within your application code to control API traffic.

### Explanation

**The correct answer is**

**A. Use Apigee to expose your API, integrate Memorystore for Redis to cache frequently requested data, and implement exponential backoff in the application to retry failed requests.**

Explanation:

This approach combines multiple techniques to optimize API performance and reduce load on your backend **Cloud SQL database** :

  1. **Use Apigee to expose your API** : Apigee provides API management capabilities such as traffic control, monitoring, and analytics, which can help manage high traffic more effectively. It also offers caching and rate limiting features, which can further protect your backend from being overwhelmed.

  2. **Integrate Memorystore for Redis to cache frequently requested data** : Adding Redis caching for commonly requested data offloads traffic from Cloud SQL by returning cached data for repeat requests, reducing latency and decreasing the number of direct calls to the database.

  3. **Implement exponential backoff for retrying failed requests** : Exponential backoff allows the application to retry failed requests more gradually, helping to reduce repeated bursts of traffic to Cloud SQL and improving resiliency during peak loads.

**Justifications for Incorrect Options:**

  * **Option B: Apigee with rate limiting and Pub/Sub for request queuing**  
Although rate limiting helps control traffic, Pub/Sub is more suited for asynchronous message processing rather than synchronous API request handling. This setup would not solve the immediate need to reduce latency and improve response times for synchronous API calls.

  * **Option C: Cloud Load Balancing with Cloud CDN and exponential backoff**  
Cloud CDN is suitable for caching static content but not ideal for caching dynamic API responses connected to a database. Additionally, without an in-memory cache like Redis, this setup lacks efficient backend caching for frequently accessed data.

  * **Option D: Cloud Load Balancing, increasing database memory, and custom rate limiting**  
Simply increasing database memory may provide temporary relief but does not address the core issue of high database load. A custom rate-limiting mechanism would also add development overhead, whereas Apigee offers built-in rate-limiting capabilities.

---

## Question 2

*Domain 3: Configuring and Deploying Applications*

**You are tasked with deploying a new feature to production on Cloud Run. Your company’s SRE team requires that all deployments be gradual to minimize the risk of downtime due to potential code issues. You want to set up this deployment with minimal configuration effort.**

**What should you do?**

- [ ] A. Set up the application’s frontend load balancer to alternate traffic between the new and previous revisions.
- [ ] B. Modify the application code to route a small portion of users to the new revision.
- [x] C. Deploy the feature with the “Serve this revision immediately” option turned off, configure the new revision to handle a small percentage of traffic, monitor for issues, and gradually increase traffic if no errors are found.
- [ ] D. Deploy the feature with “Serve this revision immediately” enabled. Check for any issues, roll back to the prior revision if errors occur, and repeat until the deployment is confirmed to be error-free.

### Explanation

The correct answer is 

**C. Deploy the feature with the “Serve this revision immediately” option turned off, configure the new revision to handle a small percentage of traffic, monitor for issues, and gradually increase traffic if no errors are found.**

Explanation:

Cloud Run supports **traffic splitting** between revisions, allowing you to roll out a new version gradually. By deploying the new feature with the **“Serve this revision immediately”** option turned off, you can initially direct a small percentage of traffic to the new revision. This strategy minimizes the risk of downtime because you can monitor for issues with a limited user base. If no issues are detected, you can gradually increase the traffic until 100% is routed to the new revision. This approach aligns with the SRE team’s requirement for a gradual rollout and minimizes configuration effort.

Justifications for Incorrect Options:

  * **Option A: Set up the load balancer to alternate traffic between revisions**  
Configuring a load balancer to alternate traffic is complex and unnecessary. Cloud Run’s built-in traffic splitting feature provides a simpler, more effective solution for gradual rollouts.

  * **Option B: Modify application code to route users to the new revision**  
Code-based traffic routing adds unnecessary complexity and maintenance overhead. Cloud Run’s traffic splitting can handle this without code changes, providing a more efficient deployment strategy.

  * **Option D: Enable “Serve this revision immediately” and roll back if issues arise**  
Serving the revision immediately directs 100% of traffic to the new version, which doesn’t allow for a gradual rollout. This approach increases the risk of downtime if issues are detected only after deployment.

**Relevant Documentation:**

For more information, refer to:

  * [Traffic Splitting in Cloud Run](https://cloud.google.com/functions/docs/configuring/traffic-splitting)

---

## Question 3

*Domain 4: Integrating Applications with Google Cloud Services*

**You are developing an external-facing application on GKE that provides a streaming API with two subscription tiers, “basic” and “premium.” Each tier limits the number of API requests allowed per client application per day. You want to design the application architecture to support these subscription tiers following Google-recommended practices. What approach should you take?**

- [x] **A.**
    Set up the service on **GKE** as a backend to an **Apigee proxy**.
    Provide **API keys** to users to identify client applications.
    Configure a **Quota policy** in **Apigee** based on the subscription tier for each API key.
- [ ] **B.**
    Set up the service on **GKE** as a backend to an **Apigee proxy**.
    Provide **API keys** to users to identify client applications.
    Configure a **SpikeArrest policy** in **Apigee** for API keys based on the subscription tier.
- [ ] **C.**
    Configure the service on **GKE** as a backend to two separate projects, each with its own **Application Load Balancer**.
    Set up quotas for **“Queries per second (QPS) per region per network”** for each project individually.
    Assign users API endpoints based on their subscription tier.
- [ ] **D.**
    Deploy the application to two **GKE clusters** , one for each subscription tier, with separate **Ingress** configurations.
    Set up each cluster as a backend to an **Apigee proxy**.
    Provide **API keys** to users to identify client applications.
    Configure different rate limits based on the subscription tier.

### Explanation

**The correct answer is A.**

**Explanation:**

Using **Apigee** as a proxy for your GKE backend service provides a robust API management layer that can handle **subscription-based quota policies** effectively. The steps outlined in Option A align with best practices by allowing:

  1. **API Keys for Client Identification** : Apigee can issue and manage API keys to identify different client applications, making it easy to enforce access control based on user subscription tiers.

  2. **Quota Policy** : Apigee's **Quota policy** allows you to enforce daily limits on API requests based on subscription tier (e.g., “basic” and “premium”). This policy is ideal for managing the number of API requests per day, aligning with the requirement to limit daily requests based on subscription levels.

This approach is scalable, follows Google-recommended practices, and does not require duplicating infrastructure, which minimizes operational overhead.

Justifications for Incorrect Options:

  * **Option B: SpikeArrest policy**  
While **SpikeArrest** controls the rate of requests to prevent traffic spikes, it is not intended for managing daily quotas. SpikeArrest limits burst requests but does not provide daily quota enforcement, which is necessary for subscription tiers.

  * **Option C: Separate projects and Application Load Balancers**  
Configuring separate projects and load balancers adds unnecessary complexity. Using Apigee with a Quota policy is a more efficient way to manage subscription-based quotas without duplicating infrastructure.

  * **Option D: Separate GKE clusters for each subscription tier**  
Deploying separate GKE clusters for each subscription tier is costly and complex. Apigee's Quota policy allows quota management per subscription tier without needing multiple clusters, making it a more scalable solution.

Relevant Documentation:

For more information, refer to:

  * [Apigee Quota Policy](https://cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy)

---

## Question 4

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Your organization has users and groups set up in an external identity provider (IdP). You want to allow all employees to access the Google Cloud console through this IdP and personalize the sign-in experience by showing each user’s name and photo. What should you do?**

- [x] A. Set up workforce identity federation with the external IdP, and configure attribute mapping to display user information.
- [ ] B. Create a service account for each employee using their name and photo, and grant each user permissions to impersonate their respective service accounts.
- [ ] C. Set up workload identity federation to obtain tokens from the external IdP, then use these tokens to enable access to the Google Cloud console.
- [ ] D. Create a Google group that includes all employees’ organization email addresses. Instruct users to use the same name, email, and password when registering and signing in.

### Explanation

The correct answer is

**A. Set up workforce identity federation with the external IdP, and configure attribute mapping to display user information.**

Explanation:

**Workforce identity federation** allows you to integrate an external identity provider (IdP) with Google Cloud, enabling users to authenticate through the external IdP to access the Google Cloud console. Workforce identity federation supports **attribute mapping** , which can be used to personalize the sign-in experience by displaying user details such as name and photo. This approach ensures secure, centralized identity management while providing a customized experience.

Justifications for Incorrect Options:

  * **Option B: Create a service account for each employee**  
Service accounts are intended for applications and workloads, not individual user access. Granting impersonation permissions for individual access is not secure and does not support user personalization.

  * **Option C: Set up workload identity federation**  
**Workload identity federation** is designed for applications and services running on external platforms to access Google Cloud resources, not for users accessing the Google Cloud console.

  * **Option D: Create a Google group and instruct users to register with specific details**  
Creating a Google group without proper identity federation does not integrate with the external IdP. This approach lacks centralized identity management and does not allow for attribute mapping or secure authentication through the IdP.

**Relevant Documentation:**

For more information, refer to:

  * [Workforce Identity Federation Overview](https://cloud.google.com/iam/docs/workforce-identity-federation)

---

## Question 5

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You are developing a new API to create requests on an asynchronous message service, which will be consumed by different services. You want to use a gRPC interface to expose the API and minimize infrastructure management overhead. How should you deploy the API?**

- [ ] A. Deploy the API to App Engine, create a Pub/Sub topic, and configure the API to publish messages to this topic.
- [x] B. Deploy the API as a Cloud Run service, create a Pub/Sub topic, and configure the API to publish messages to this topic.
- [ ] C. Deploy the API to a GKE cluster, set up a Kafka cluster, and configure the API to send messages to this Kafka cluster.
- [ ] D. Deploy the API on a Compute Engine instance, set up a Kafka cluster, and configure the API to send messages to this Kafka cluster.

### Explanation

The correct answer is

**B. Deploy the API as a Cloud Run service, create a Pub/Sub topic, and configure the API to publish messages to this topic.**

Explanation:

**Cloud Run** is a fully managed, serverless platform that supports **gRPC** and minimizes infrastructure management overhead, making it an ideal choice for deploying the API. By using **Cloud Pub/Sub** as the asynchronous message service, you can publish messages that will be consumed by different services, allowing for scalable, decoupled communication between the producer and consumer services.

Key benefits:

  * **Serverless** : Cloud Run handles scaling, load balancing, and infrastructure management automatically.

  * **gRPC Support** : Cloud Run natively supports gRPC, enabling efficient API communication.

  * **Pub/Sub Integration** : Using Pub/Sub for message distribution provides high scalability, reliability, and minimal configuration.

Justifications for Incorrect Options:

  * **Option A: App Engine with Pub/Sub**  
While App Engine is managed and supports Pub/Sub integration, it does not support gRPC natively. Cloud Run is a better choice for gRPC-based APIs.

  * **Option C: GKE with Kafka**  
GKE requires managing Kubernetes clusters, which increases infrastructure management overhead. Additionally, Kafka requires additional setup and maintenance compared to the serverless and fully managed Pub/Sub service.

  * **Option D: Compute Engine with Kafka**  
Compute Engine requires managing virtual machines, which adds infrastructure management overhead. Kafka also involves additional configuration and maintenance, making this option more complex than using Cloud Run with Pub/Sub.

**Relevant Documentation:**

For more details, refer to:

  * [Cloud Run and gRPC](https://cloud.google.com/run/docs/triggering/grpc)

---

## Question 6

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You are preparing to deploy an application running on a Windows-based Compute Engine instance that connects to a Cloud SQL database. To establish this connection, you plan to use the Cloud SQL Auth Proxy while adhering to Google’s best practices and the principle of least privilege. You have already set up a custom service account.**

**What is your next step?**

- [x] A. Create a custom role for the service account, granting only the cloudsql.instances.connect permission. Then, update the Cloud SQL Auth Proxy startup command with your instance connection name.
- [ ] B. Assign the roles/cloudsql.client role to the custom service account. Modify the Cloud SQL Auth Proxy startup command to include the --unix-socket option.
- [ ] C. Grant the custom service account the roles/cloudsql.editor role for broad permissions.
- [ ] D. Assign the roles/cloudsql.viewer role to the custom service account and adjust the Cloud SQL Auth Proxy command to specify your instance connection name.

### Explanation

The correct answer is 

**A. Create a custom role for the service account, granting only the cloudsql.instances.connect permission. Then, update the Cloud SQL Auth Proxy startup command with your instance connection name.**

Explanation:

According to Google’s best practices and the **principle of least privilege** , it is recommended to create a custom role that grants only the permissions necessary for the task. For connecting to Cloud SQL using the **Cloud SQL Auth Proxy** , the `**cloudsql.instances.connect**` permission is sufficient to establish a secure connection to the Cloud SQL instance. By limiting the permissions to only what’s necessary, you enhance security by reducing the potential for unintended access.

Additionally, updating the **Cloud SQL Auth Proxy startup command** with the instance connection name is essential to correctly establish the connection to your Cloud SQL instance.

Justifications for Incorrect Options:

  * **Option B: Assign the roles/cloudsql.client role with the --unix-socket option**  
While the `roles/cloudsql.client` role includes the `cloudsql.instances.connect` permission, it also includes other permissions that may not be necessary, which doesn’t align with the principle of least privilege. The `--unix-socket` option is specific to UNIX-based systems and is not applicable to Windows.

  * **Option C: Grant the roles/cloudsql.editor role**  
The `roles/cloudsql.editor` role provides broad permissions, including modifying database instances, which violates the principle of least privilege and poses a security risk.

  * **Option D: Assign the roles/cloudsql.viewer role**  
The `roles/cloudsql.viewer` role allows read-only access to Cloud SQL resources but does not grant the `cloudsql.instances.connect` permission needed for the Cloud SQL Auth Proxy to establish a connection.

**Relevant Documentation:**

For more information, refer to:

  * [Using the Cloud SQL Auth Proxy](https://cloud.google.com/sql/docs/mysql/sql-proxy)

---

## Question 7

*Domain 4: Integrating Applications with Google Cloud Services*

**You are building a secure platform for sharing documents, where users can share files with others, including individuals outside their organization. To maintain security, access to shared documents must expire after a customizable period. These documents are stored in Cloud Storage.**

**How should you set up Cloud Storage to support this access expiration?**

- [ ] A. Use signed policy documents on the Cloud Storage bucket to control access.
- [ ] B. Configure access control lists (ACLs) on the Cloud Storage bucket to manage permissions.
- [x] C. Generate a signed URL for each document that users want to share temporarily.
- [ ] D. Assign the Storage Object Viewer IAM role to all authenticated users to allow document access.

### Explanation

The correct answer is 

**C. Generate a signed URL for each document that users want to share temporarily.**

Explanation:

**Signed URLs** are the recommended method for providing **temporary access** to files in Cloud Storage. They allow you to generate a URL that grants time-limited access to a specific object, and the expiration time can be customized as needed. This approach provides a secure and controlled way to share documents with external users without altering bucket-level permissions.

Key benefits:

  * **Customizable expiration** : Signed URLs allow you to set an expiration period, ensuring access automatically expires after the specified time.

  * **Granular access** : Each signed URL is unique to a specific document, and access is limited to the document associated with the URL, maintaining security for other stored objects.

Justifications for Incorrect Options:

  * **Option A: Use signed policy documents**  
Signed policy documents provide temporary access but are primarily intended for uploading objects to Cloud Storage, not for controlling access to already stored objects.

  * **Option B: Configure access control lists (ACLs)**  
ACLs allow fine-grained access control but do not provide time-bound access. Managing expiration through ACLs is complex and requires manual updates to remove permissions after the expiration period.

  * **Option D: Assign the Storage Object Viewer IAM role to all authenticated users**  
This option would grant broad access to all authenticated users, which does not meet the security requirement of time-limited, controlled access. IAM roles are not suitable for temporary, user-specific access control.

**Relevant Documentation:**

For more information, refer to:

  * [Signed URLs for Cloud Storage](https://cloud.google.com/storage/docs/access-control/signed-urls)

---

## Question 8

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You work for an environmental agency in a large metropolitan area, developing a new platform to monitor air quality. Thousands of sensors will capture air quality data across the city, and you want each device to send and receive data payloads to a RESTful backend every minute using a curl command. The backend is hosted in a single cloud region with Premium Tier networking. Your goal is to connect the devices to the backend in a way that minimizes the average daily latency, specifically focusing on reducing Time to First Byte (TTFB).**

**What setup should you use?**

- [ ] A. 1. Host the air quality backend on Compute Engine VMs.  
  2\. Set up a weighted round-robin routing policy on Cloud DNS.  
  3\. Configure the devices to connect using this DNS setup.
- [ ] B. 1. Host the air quality backend on Compute Engine VMs.  
  2\. Create a round-robin routing policy on Cloud DNS for these VMs.  
  3\. Configure the devices to connect using this DNS configuration.
- [ ] C. 1. Run the air quality backend in a managed instance group.  
  2\. Set up an external passthrough Network Load Balancer linked to the managed instance group.  
  3\. Configure the devices to connect through the Network Load Balancer.
- [x] D. 1. Run the air quality backend in a managed instance group.  
  2\. Set up an external Application Load Balancer and connect it to the managed instance group.  
  3\. Configure the devices to connect through the Application Load Balancer.

### Explanation

The correct answer is **D.**

Explanation:

To achieve minimal latency and optimize **Time to First Byte (TTFB)** for a RESTful backend with thousands of devices, the best approach is to:

  1. **Use an external Application Load Balancer** : Google Cloud's external **Application Load Balancer** is built on the **Premium Tier network** , offering global load balancing with proximity-based routing. This setup reduces latency by routing each request to the backend instance closest to the device, minimizing TTFB.

  2. **Managed Instance Group** : Using a managed instance group for the backend ensures scalability and resilience, as it can automatically scale based on demand and distribute traffic efficiently.

The Application Load Balancer also supports caching, SSL termination, and session affinity, which can improve performance and security for high-frequency, low-latency data exchanges.

Justifications for Incorrect Options:

  * **Option A: Compute Engine VMs with weighted round-robin routing in Cloud DNS**  
Cloud DNS round-robin routing lacks proximity-based routing and does not optimize for the closest regional endpoint, which is essential for reducing TTFB. This setup would likely result in higher latency.

  * **Option B: Compute Engine VMs with round-robin Cloud DNS routing**  
Basic round-robin DNS routing does not provide latency optimization or failover, and Cloud DNS does not route based on geographic proximity, making it unsuitable for minimizing TTFB across a large number of devices.

  * **Option C: Network Load Balancer with a managed instance group**  
The Network Load Balancer operates at Layer 4 (TCP/UDP) and does not support HTTP(S) protocols natively. It also lacks advanced features like proximity-based routing, which is crucial for reducing TTFB for a geographically dispersed user base.

**Relevant Documentation:**

For more information, refer to:

  * [Google Cloud External Application Load Balancer](https://cloud.google.com/load-balancing/docs/https)

---

## Question 9

*Domain 4: Integrating Applications with Google Cloud Services*

**Your infrastructure team manages Compute Engine VMs and uses the Google Cloud console and gcloud CLI to provision resources for the development environment. To meet compliance requirements, all Compute Engine VMs must have the correct labels. You need a solution that automatically corrects any missing labels without altering the current provisioning process. You want this solution to be highly scalable.**

**What should you do?**

- [x] A. Set up a trigger in Cloud Audit Logs to activate a Cloud Function whenever a Compute Engine VM is created. The function should check for missing labels and add them if needed.
- [ ] B. Use Terraform to deploy resources and run the gcloud terraform vet command with a policy that ensures each Compute Engine VM provisioned by Terraform has the required labels.
- [ ] C. Create a script that periodically checks all Compute Engine VMs for missing labels using Cloud Scheduler. Have the script apply labels where they are missing.
- [ ] D. Manually review all Compute Engine VMs for missing labels on a regular basis and use the console to assign any necessary lab

### Explanation

**The correct answer is**

**A. Set up a trigger in Cloud Audit Logs to activate a Cloud Function whenever a Compute Engine VM is created. The function should check for missing labels and add them if needed.**

Explanation:

This solution uses **Cloud Audit Logs** to trigger a **Cloud Function** automatically whenever a new Compute Engine VM is created. The function can be programmed to check for the required labels and add any that are missing, ensuring compliance without manual intervention. This approach is scalable and does not alter the current provisioning process, as it operates independently and responds in real-time to new VM creations.

Justifications for Incorrect Options:

  * **Option B: Use Terraform with**`**gcloud terraform vet**`  
While Terraform can manage resources with labels, this solution would require a complete shift to Terraform for provisioning. The `gcloud terraform vet` command is used to validate Terraform configurations but does not directly apply to existing resources provisioned via the Google Cloud Console or gcloud CLI. This approach would not work well with the existing provisioning process.

  * **Option C: Use Cloud Scheduler to run a script periodically**  
Although a scheduled script could check and apply labels, this solution is less efficient and scalable than a trigger-based approach. Periodic checks would introduce latency in correcting missing labels and increase resource usage.

  * **Option D: Manually review and assign labels**  
Manual reviews are inefficient, prone to human error, and do not scale effectively with large environments. Automated enforcement is preferred for compliance.

---

## Question 10

*Domain 2: Building and Testing Applications*

**You are developing a discussion portal hosted on Cloud Run, where incoming requests pass through multiple microservices before a response is returned. Some of these microservices connect to databases. To optimize performance, you want to conduct a load test to identify any potential bottlenecks when the application is under heavy traffic. You plan to follow Google’s recommended practices.**

**What should you do?**

- [ ] A. Modify responses to include a time series showing the elapsed time for each service. Then, use Log Analytics in Cloud Logging to create a heatmap highlighting any bottleneck services.
- [x] B**.** Enable Cloud Trace to track requests from load testing clients and review request timings in Cloud Trace.
- [ ] C. Expose latency metrics for each service with every request. Set up Google Cloud Managed Service for Prometheus to collect and analyze these metrics.
- [ ] D. Add log statements that capture elapsed time for each service. Use BigQuery to analyze the logs and metrics.

### Explanation

**The correct answer is**

**B. Enable Cloud Trace to track requests from load testing clients and review request timings in Cloud Trace.**

Explanation:

**Cloud Trace** is a distributed tracing service designed for tracking request latencies across microservices, which is ideal for identifying bottlenecks in a complex application architecture like the discussion portal. By enabling Cloud Trace, you can capture latency data for each service in the request path, allowing you to pinpoint performance issues and evaluate how each microservice impacts overall response times. Cloud Trace is part of Google’s recommended practices for identifying latency bottlenecks in distributed systems.

Justifications for Incorrect Options:

  * **Option A: Modify responses to include a time series**  
Adding time series data to responses would require substantial changes to response formatting and is not a scalable or efficient way to monitor service latency. Log Analytics is useful but would not offer as comprehensive a view as Cloud Trace for end-to-end request tracking.

  * **Option C: Use Google Cloud Managed Service for Prometheus with latency metrics**  
Exposing latency metrics for each request can be helpful for ongoing monitoring, but Prometheus is less suited for detailed, end-to-end request tracing compared to Cloud Trace, especially in scenarios involving multiple microservices.

  * **Option D: Capture elapsed time with log statements and analyze in BigQuery**  
Logging elapsed times for each service can provide useful data, but it’s less efficient for real-time performance analysis across multiple services. Cloud Trace is specifically optimized for distributed tracing and offers more granular insights into request latency.

**Relevant Documentation:**

For more information, refer to:

  * [Google Cloud Trace Overview](https://cloud.google.com/trace/docs/overview)

---

## Question 11

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Your team uses Bigtable as the backend database for your application. In the app profile, you observe that the Bigtable connection is set to single-cluster routing, with manual failover configured if the cluster becomes unavailable. You want to improve the application’s Bigtable connectivity to be more efficient and highly available.**

**What should you do?**

- [ ] A. Implement a Memcached layer so that queries are directed to the cache first, retrieving data from Bigtable only on a cache miss.
- [ ] B. Increase the connection pool size in the Bigtable client to allow more simultaneous connections.
- [ ] C. Set up a Dataflow template and use a Beam connector to stream data changes.
- [x] D. Change the app profile to use multi-cluster routing for improved availability.

### Explanation

**The correct answer is**

**D. Change the app profile to use multi-cluster routing for improved availability.**

**Explanation:**

By changing the **Bigtable app profile to use multi-cluster routing** , you enable **automatic failover** and **load balancing** across multiple clusters, which enhances both the **availability** and **resilience** of the application. With multi-cluster routing, Bigtable can direct requests to any available cluster in the instance, automatically managing failover if a cluster becomes unavailable. This setup ensures seamless, highly available connections without requiring manual intervention.

**Justifications for Incorrect Options:**

  * **Option A: Implement a Memcached layer**  
While caching with Memcached can improve read latency, it does not address high availability or failover needs for Bigtable connectivity. A cache does not eliminate the need for a more resilient connection strategy in the event of a cluster failure.

  * **Option B: Increase the connection pool size in the Bigtable client**  
Increasing the connection pool size may help with throughput but does not impact availability or failover capability. It also does not improve resilience if a cluster becomes unavailable.

  * **Option C: Set up a Dataflow template with a Beam connector**  
Using Dataflow with a Beam connector is suited for data processing and transformation but does not impact the availability or connectivity resilience of the Bigtable app profile. It is unrelated to Bigtable client connectivity and failover.

---

## Question 12

*Domain 3: Configuring and Deploying Applications*

**You work for an ecommerce company migrating several applications to Google Cloud, and you're involved in migrating one of these applications. The application currently runs on a VM without specific OS dependencies. You’ve created a Dockerfile and uploaded the resulting image to Artifact Registry. To reduce infrastructure management and operational complexity, you need an appropriate deployment option.**

**What should you do?**

- [x] A. Deploy the image to Cloud Run.
- [ ] B. Deploy the image to a GKE Autopilot cluster.
- [ ] C. Deploy the image to a GKE Standard cluster.
- [ ] D. Deploy the image on a Compute Engine instance.

### Explanation

The correct answer is

**A. Deploy the image to Cloud Run**.

Explanation:

**Cloud Run** is a fully managed, serverless platform designed for deploying containerized applications. It automatically scales based on traffic, significantly reduces infrastructure management, and requires minimal operational overhead. Since your application has no specific OS dependencies and you’re aiming to reduce infrastructure management and complexity, Cloud Run is the best choice.

Key benefits of Cloud Run:

  * **Serverless** : Cloud Run handles all infrastructure management, including scaling, load balancing, and updates.

  * **Cost-effective** : You only pay when the application is serving requests, making it ideal for unpredictable or bursty traffic.

  * **Low complexity** : Cloud Run requires minimal configuration compared to setting up and maintaining a Kubernetes cluster or virtual machine.

Justifications for Incorrect Options:

  * **Option B: Deploy the image to a GKE Autopilot cluster**  
Although GKE Autopilot reduces some Kubernetes management overhead, it still requires more configuration and ongoing Kubernetes management than Cloud Run. Cloud Run is a simpler and more cost-effective choice for an application without OS dependencies.

  * **Option C: Deploy the image to a GKE Standard cluster**  
A GKE Standard cluster provides more control over configuration but requires significant Kubernetes management, which increases complexity and operational overhead.

  * **Option D: Deploy the image on a Compute Engine instance**  
Using Compute Engine would involve managing VM instances, including scaling, health checks, and OS updates, adding unnecessary complexity compared to a serverless option like Cloud Run.

**Relevant Documentation:**

For more information on Cloud Run, refer to:

  * [Getting started with Cloud Run](https://cloud.google.com/run/docs/quickstarts)

---

## Question 13

*Domain 4: Integrating Applications with Google Cloud Services*

**You’re a developer for a local concert venue, and customers use your company’s website to purchase event tickets. You need to ensure customers receive immediate confirmation when they reserve a specific seat.**

**How should you structure the ticket reservation process?**

- [ ] A. Place the seat reservation request in a Cloud Tasks queue, which initiates a Workflow to handle the reservation processing.
- [x] B. Publish the seat reservation to a Pub/Sub topic and configure the backend service to use Eventarc for processing the reservation on GKE.
- [ ] C. Store the seat reservation in a Cloud Storage bucket, triggering an event to a Cloud Run service that processes the order.
- [ ] D. Send the seat reservation as an HTTP POST request to an Application Load Balancer, which distributes it to a Compute Engine managed instance group that processes the reservation.

### Explanation

The most suitable approach to ensure immediate confirmation and efficient processing of seat reservations is:

**B. Publish the seat reservation to a Pub/Sub topic and configure the backend service to use Eventarc for processing the reservation on GKE.**

**Explanation:**

  * **Immediate confirmation:** Pub/Sub ensures a reliable and scalable messaging system. The reservation request is immediately published to the topic, allowing the client to receive confirmation as soon as the request is acknowledged.

  * **Efficient processing:** Eventarc triggers the backend service on GKE automatically when a new message arrives on the Pub/Sub topic. This eliminates the need for polling or constant monitoring of the queue, leading to efficient processing.

  * **Scalability:** Pub/Sub and Eventarc are highly scalable, allowing the system to handle increased load during peak booking times.

  * **Reliability:** Pub/Sub ensures reliable message delivery, reducing the risk of lost reservations.

**Why other options are not suitable:**

  * **A. Cloud Tasks and Workflow:** While this approach can be used, it might introduce latency as the reservation request is first queued and then processed by Workflow. This could delay the confirmation process.

  * **C. Cloud Storage:** Storing the reservation in Cloud Storage and triggering a Cloud Run service is not the most efficient way to handle real-time processing. It might introduce unnecessary delays.

  * **D. HTTP POST and Load Balancer:** While this approach can work, it relies on polling the load balancer for new requests, which can be less efficient than event-driven architectures. Additionally, it might introduce complexities in scaling the backend service.

By using Pub/Sub and Eventarc, you can achieve a reliable, scalable, and efficient seat reservation process, ensuring immediate confirmation for your customers.

---

## Question 14

*Domain 3: Configuring and Deploying Applications*

**You work at a financial services company that prioritizes containerized applications, and your team develops microservices. A Cloud Build pipeline is set up to create container images, run regression tests, and publish the images to Artifact Registry. To ensure only containers that pass regression tests are deployed to GKE clusters, you have already enabled Binary Authorization on the clusters.**

**What should you do next?**

- [ ] A. Deploy both Voucher Server and Voucher Client components. After a container image passes the regression tests, run Voucher Client as a step in the Cloud Build pipeline.
- [ ] B. Set up an attestor and a policy, then perform a vulnerability scan and create an attestation for the container image as part of the Cloud Build pipeline.
- [x] C. Set up an attestor and a policy. Create an attestation for container images that pass regression tests as a step in the Cloud Build pipeline.
- [ ] D. Apply the Restricted level of Pod Security Standard to the relevant namespaces. Digitally sign the container images that pass regression tests as a step in the Cloud Build pipeline.

### Explanation

The correct answer is 

**C. Set up an attestor and a policy. Create an attestation for container images that pass regression tests as a step in the Cloud Build pipeline.**

Explanation:

With **Binary Authorization** enabled, deploying only trusted container images requires creating **attestations** that certify an image has met specific criteria. By setting up an **attestor** and defining a **policy** in Binary Authorization, you can restrict deployments to images that have a valid attestation. Adding an attestation step in the **Cloud Build pipeline** ensures that only images passing regression tests are signed, thus allowing only those images to be deployed to the GKE clusters.

This approach leverages Binary Authorization to enforce security policies, ensuring that only verified and tested images are deployed to production environments.

Justifications for Incorrect Options:

  * **Option A: Deploy Voucher Server and Client**  
Voucher is a third-party tool for creating attestations, but Google Cloud provides native support for attestations with Binary Authorization. Using Voucher introduces additional complexity and is unnecessary if Binary Authorization and Cloud Build are already integrated.

  * **Option B: Perform a vulnerability scan and create an attestation**  
A vulnerability scan is useful, but the question specifies ensuring that images passing regression tests are deployed. While scanning for vulnerabilities is beneficial, the attestation step should focus on confirming that regression tests have passed.

  * **Option D: Apply the Restricted Pod Security Standard and sign images**  
The Restricted Pod Security Standard governs security settings for pod configurations but does not verify or enforce container image provenance. Binary Authorization attestations are necessary to enforce that only approved images (those that passed tests) are deployed.

**Relevant Documentation:**

For more information, refer to:

  * [Binary Authorization Overview](https://cloud.google.com/binary-authorization/docs/overview)

  * [Creating Attestations in Binary Authorization](https://cloud.google.com/binary-authorization/docs/making-attestations)

---

## Question 15

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Your team is preparing to use AlloyDB as the database backend for a new application release. The application is hosted in a separate project and network from the AlloyDB instances. You need a secure way to connect the application to the AlloyDB instance while keeping both projects isolated. You also want to minimize additional setup steps and follow Google’s best practices.**

**How should you set up network connectivity for the database?**

- [x] A. Create a Shared VPC and add both the application and AlloyDB projects as service projects to enable connectivity.
- [ ] B. Use the AlloyDB Auth Proxy and configure the application project’s firewall to allow traffic on port 5433.
- [ ] C. Generate a service account from the AlloyDB project, then use the JSON key file of this service account as the --credentials-file for connecting to AlloyDB.
- [ ] D. Request that the database team deploy AlloyDB databases within the same project and network as the application.

### Explanation

The correct answer is 

**A. Create a Shared VPC and add both the application and AlloyDB projects as service projects to enable connectivity.**

Explanation:

Using a **Shared VPC** allows secure and efficient communication between resources in separate projects by enabling them to share the same VPC network while maintaining isolation at the project level. By adding both the application and AlloyDB projects as **service projects** to the Shared VPC, the application can securely connect to AlloyDB without requiring additional complex networking setups or firewall adjustments. This approach follows Google’s best practices for inter-project connectivity and ensures a secure, centralized network management setup.

Justifications for Incorrect Options:

  * **Option B: Use the AlloyDB Auth Proxy and adjust firewall settings**  
The AlloyDB Auth Proxy helps secure database connections but does not address the need for inter-project network connectivity directly. Additionally, manually adjusting firewall rules in the application project could introduce security risks and increase operational complexity.

  * **Option C: Use a service account key file for connecting to AlloyDB**  
While service accounts can authenticate access, this option does not address network connectivity between separate projects. It also involves managing and distributing sensitive credentials, which can introduce security risks.

  * **Option D: Deploy AlloyDB within the same project and network as the application**  
Consolidating resources in a single project reduces isolation, making it harder to manage project-specific permissions and security policies independently. It’s also not a scalable or flexible setup for larger organizations with separate ownership of resources.

**Relevant Documentation:**

For more information, refer to:

  * [Shared VPC Overview](https://cloud.google.com/vpc/docs/shared-vpc)

---

## Question 16

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You have a containerized service running on-premises, written in the current stable version of Python 3, and accessible only to users in the United States. This service experiences high traffic during the day and no traffic at night. You want to migrate this application to Google Cloud, track error logs using Error Reporting after migration, and keep costs and setup effort low.**

**What should you do?**

- [x] A. Deploy the service on Cloud Run, and configure it to log errors to standard error.
- [ ] B. Deploy the service on Cloud Run, and set it up to stream errors to a Cloud Storage bucket.
- [ ] C. Deploy the service on a GKE Autopilot cluster, and configure it to log errors to standard error.
- [ ] D. Deploy the service on a GKE Autopilot cluster, and set it up to log errors to a Cloud Storage bucket.

### Explanation

**The correct answer is**

**A. Deploy the service on Cloud Run, and configure it to log errors to standard error.**

**Explanation:**

**Cloud Run** is a fully managed, serverless platform that automatically scales up and down based on traffic, which is ideal for an application with high traffic during the day and no traffic at night. Cloud Run charges only for active usage, keeping costs low during off-peak hours.

Configuring the service to log errors to **standard error** enables **Google Cloud Error Reporting** to automatically capture and track errors, providing insights without additional configuration or infrastructure setup. This setup is both cost-effective and requires minimal setup effort.

Justifications for Incorrect Options:

  * **Option B: Cloud Run with errors logged to Cloud Storage**  
Logging to Cloud Storage does not provide direct integration with Error Reporting, so additional setup would be required to track errors. Logging to standard error is simpler and allows direct integration with Google Cloud’s monitoring tools.

  * **Option C: GKE Autopilot with errors logged to standard error**  
GKE Autopilot is managed but still requires more setup and operational management than Cloud Run. For a stateless, containerized service with intermittent traffic, Cloud Run is more cost-effective.

  * **Option D: GKE Autopilot with errors logged to Cloud Storage**  
Using GKE Autopilot and Cloud Storage for logging increases both costs and setup complexity, as it doesn’t integrate directly with Error Reporting.

---
