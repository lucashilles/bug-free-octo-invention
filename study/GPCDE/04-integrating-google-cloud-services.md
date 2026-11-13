# Domain 4 — Integrating Applications with Google Cloud Services

63 questions. Answers are collapsed — try each question before expanding it.

## Questions

### Exam 1 · Q13

**Your code, operating on Cloud Functions within project A, aims to write an object to a Cloud Storage bucket owned by project B. Unfortunately, the write operation fails with a "403 Forbidden" error. How can you address this issue effectively?**

- III. Allocate the roles/storage.objectCreator role to the service-PROJECTA@gcf-admin-robot.iam.gserviceaccount.com service account for the Cloud Storage bucket.
- IV. Ensure the Cloud Storage API is enabled within project B.
- II. Provide your user account with the roles/iam.serviceAccountUser role for the service-PROJECTA@gcf-admin-robot.iam.gserviceaccount.com service account.
- I. Grant your user account the roles/storage.objectCreator role for the Cloud Storage bucket.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Allocate the roles/storage.objectCreator role to the service-PROJECTA@gcf-admin-robot.iam.gserviceaccount.com service account for the Cloud Storage bucket.

**III. Allocate the roles/storage.objectCreator role to the service-PROJECTA@gcf-admin-robot.iam.gserviceaccount.com service account for the Cloud Storage bucket.**

Here's why this is the correct approach:

  * **Service Account Permissions:** Cloud Functions execute using a service account. It is this service account that needs the necessary permissions to write to the Cloud Storage bucket in project B.

  * **Principle of Least Privilege:** Granting the specific role `roles/storage.objectCreator` provides the minimal permission required, limiting the potential security impact.

  * **Cross-Project Access:** This approach addresses the issue of cross-project communication, the core reason why the write operation fails.

**Why Other Options are Not Ideal:**

  * **I. Grant your user account the roles/storage.objectCreator role ...** While this might work, it's overly broad and ties permissions to your personal user account rather than the function's identity.

  * **II. Provide your user account with the roles/iam.serviceAccountUser ...** This role grants you the ability to impersonate service accounts, but doesn't directly give the function's service account the needed bucket permissions.

  * **IV. Ensure the Cloud Storage API is enabled for project B** This is a prerequisite for any interaction with Cloud Storage, but does not address the specific permissions issue.

Ref:

<https://cloud.google.com/functions/docs/concepts/iam#troubleshooting_permission_errors>

</details>

---

### Exam 1 · Q15

**To enable clients to download a file from your website for a limited period while adhering to Google's recommended best practices, how should you architect the application?**

- II. Generate and allocate a Cloud Storage-signed URL for the file, then provide the URL to the client for downloading.
- III. Create a temporary Cloud Storage bucket with a specified time expiration, granting download permissions to the bucket, copying the file, and providing it to the client.
- IV. Generate HTTP cookies with a specified time expiration. If the time is valid, retrieve the file from the Cloud Storage bucket and make it accessible for the client to download.
- I. Configure the application to deliver the file to the client as an email attachment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Generate and allocate a Cloud Storage-signed URL for the file, then provide the URL to the client for downloading.

**II. Generate and allocate a Cloud Storage signed URL for the file, then provide the URL to the client for downloading.**

Here's why this is the ideal choice:

  * **Secure and Scalable:** Signed URLs leverage Cloud Storage's security mechanisms and scale well without impacting your application's workload.

  * **Time-limited Access:** You can set an expiration time directly on the signed URL, controlling the download window.

  * **Simplicity:** Generating signed URLs is relatively straightforward, reducing implementation complexity.

  * **Google Best Practice:** Google recommends signed URLs for this use case.

**Let's analyze the other options:**

  * **I. Email Attachment:** This approach is less scalable and secure, especially for larger files compared to a direct download link.

  * **III. Temporary Bucket:** Creating and managing temporary buckets adds unnecessary overhead and complexity.

  * **IV. HTTP Cookies:** Cookies are designed to store client-side data and aren't ideal for managing file access and security.

Ref:

<https://cloud.google.com/storage/docs/access-control/signed-urls>

</details>

---

### Exam 1 · Q18

**You recently migrated a monolithic application to Google Cloud, breaking it down into microservices. One of these microservices is deployed using Cloud Functions. As you modernize the application, you introduce a backward-incompatible change to the service's API. You now need to support both existing callers using the original API and new callers utilizing the updated API. What's the best approach?**

- II. Keep the original Cloud Function unchanged and deploy a second Cloud Function containing only the modified API. Calls are automatically routed to the appropriate function.
- IV. Update the Cloud Function's code to support the new API and redeploy it. Requests for both API versions are handled based on a version identifier included in the call.
- III. Retain the original Cloud Function unchanged and deploy a second Cloud Function with the new API. Utilize Cloud Endpoints to provide an API gateway exposing a versioned API.
- I. Maintain the original Cloud Function unchanged and deploy a second Cloud Function with the new API. Employ a load balancer to distribute calls between the versions.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Retain the original Cloud Function unchanged and deploy a second Cloud Function with the new API. Utilize Cloud Endpoints to provide an API gateway exposing a versioned API.

**III. Retain the original Cloud Function unchanged and deploy a second Cloud Function with the new API. Utilize Cloud Endpoints to provide an API gateway exposing a versioned API.**

Here's why this approach is superior:

  * **Clear Versioning:** Cloud Endpoints allows you to explicitly define different API versions, providing clarity to developers and avoiding confusion over ambiguous routing.

  * **API Management:** Cloud Endpoints offers additional features like authentication, rate limiting, and API analytics, which can be beneficial as your API evolves.

  * **Flexibility:** You can control how traffic is routed between versions for gradual rollout, testing, and eventual deprecation of the old version.

  * **Maintainability:** Keeping the original function untouched simplifies rollback if necessary and allows you to isolate changes within the new version.

**Why Other Options Are Less Ideal:**

  * **I. Load Balancer:** While possible, manually configuring a load balancer for API versioning is less streamlined and lacks the features of a dedicated API management tool like Cloud Endpoints.

  * **II. Automatic Routing:** Cloud Functions don't natively support automatic routing based on API versioning.

  * **IV. Single Function Update:** This approach risks downtime for consumers of the old API, making the migration disruptive. It also adds complexity to the codebase.

**Refrences:**  
[https://cloud.google.com/endpoints/docs/openapi/versioning-an-api#backwards-incompatible](https://cloud.google.com/endpoints/docs/openapi/versioning-an-api#backwards-incompatible  https://cloud.google.com/architecture/migrating-a-monolithic-app-to-microservices-gke#versioning  https://cloud.google.com/endpoints/docs/openapi/versioning-an-api#backwards-incompatible)

[https://cloud.google.com/architecture/migrating-a-monolithic-app-to-microservices-gke#versioning](https://cloud.google.com/endpoints/docs/openapi/versioning-an-api#backwards-incompatible  https://cloud.google.com/architecture/migrating-a-monolithic-app-to-microservices-gke#versioning  https://cloud.google.com/endpoints/docs/openapi/versioning-an-api#backwards-incompatible)

[https://cloud.google.com/endpoints/docs/openapi/versioning-an-api#backwards-incompatible](https://cloud.google.com/endpoints/docs/openapi/versioning-an-api#backwards-incompatible  https://cloud.google.com/architecture/migrating-a-monolithic-app-to-microservices-gke#versioning  https://cloud.google.com/endpoints/docs/openapi/versioning-an-api#backwards-incompatible)

</details>

---

### Exam 1 · Q22

**While conducting load testing on your server application, you observe that an inactive Cloud Storage bucket is now handling 2000 write requests per second and 7500 read requests per second within the initial 30 seconds. Consequently, your application begins experiencing intermittent 5xx and 429 HTTP responses from the Cloud Storage JSON API due to increased demand. To mitigate the occurrence of failed responses from the Cloud Storage API, what action should you take?**

- II. Opt for the XML API instead of the JSON API for interacting with Cloud Storage.
- III. Transmit the HTTP response codes back to clients initiating uploads from your application.
- I. Distribute the uploads across multiple individual storage buckets.
- IV. Restrict the upload rate from your application clients to ensure a gradual increase in the dormant bucket's peak request rate.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Restrict the upload rate from your application clients to ensure a gradual increase in the dormant bucket's peak request rate.

**IV. Restrict the upload rate from your application clients to ensure a gradual increase in the dormant bucket's peak request rate.**

Let's break down why it's the best choice:

  * **Addresses the Root Cause:** The sudden surge in requests is overwhelming Cloud Storage's capacity to handle them, leading to 5xx errors (server-side issues) and 429 errors (rate limiting). Slowing down uploads directly tackles the cause of the problem.

  * **Rate Limiting/Throttling** : Implementing rate limiting in your application logic allows you to control the flow of requests, preventing the Cloud Storage bucket from being flooded.

  * **Prevents Recurrence:** A gradual increase allows Cloud Storage to scale its request handling capabilities, reducing the risk of further outages in your application.

**Why Other Options Are Less Ideal:**

  * **I. Distribute the uploads across multiple individual storage buckets.** While this could help long-term with scalability, it doesn't immediately address the issue at hand with the current bucket.

  * **II. Opt for the XML API ...** Changing the API won't solve the fundamental problem of overwhelming the bucket with requests.

  * **III. Transmit the HTTP response codes ...** While passing these responses to clients is informative, it doesn't fix the core issue of too many requests hitting Cloud Storage.

**References:**

<https://cloud.google.com/storage/docs/request-rate#ramp-up>

</details>

---

### Exam 1 · Q24

**Your service annotates images fetched from Cloud Storage. During peak periods, requests to Cloud Storage result in HTTP 429 "Too Many Requests" errors. How should you address this issue?**

- IV. Switch the storage class of the Cloud Storage bucket to Multi-regional.
- II. Request a quota increase through the GCP Console.
- III. Retry the request employing a truncated exponential backoff strategy.
- I. Apply a cache-control header to the objects.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Retry the request employing a truncated exponential backoff strategy.

**III. Retry the request employing a truncated exponential backoff strategy.**

Here's why this is the most effective immediate solution and why the others have limitations:

  * **Addresses the Root Issue:** HTTP 429 errors signal that you're exceeding your Cloud Storage request rate. Retrying with exponential backoff allows your service to gracefully handle temporary throttling, giving the quota time to reset.

  * **Quick Implementation:** Implementing this retry mechanism likely involves minor code changes in the component making requests to Cloud Storage.

  * **Scalability:** Exponential backoff helps your service automatically adjust its behavior to handle temporary load spikes.

**Why Other Options Might Help, But Have Limitations:**

  * **I. Apply a cache-control header...** Caching can reduce future requests for the same images, but it doesn't directly address the 429 errors when the cache is empty.

  * **II. Request a quota increase...** This can be a valid solution, but it might take time for approval and involves additional costs.

  * **IV. Switch ... to Multi-regional.** Multi-regional storage can improve availability and redundancy but might not directly alleviate the current quota limitations.

</details>

---

### Exam 1 · Q30

**Your team is responsible for developing services on Google Cloud. You're tasked with constructing a data processing service using Cloud Functions. However, the data being processed is sensitive, necessitating robust security measures. You must ensure that invocations originate only from authorized services, adhering to Google's recommended security practices for functions. What's the optimal approach to achieve this?**

- III. Create a service account with the Cloud Functions Invoker role, and utilize that service account for invoking the function.
- II. Create a service account with the Cloud Functions Viewer role, and utilize that service account for invoking the function.
- I. Enable Identity-Aware Proxy in your project and secure function access using its permissions.
- IV. Generate an OAuth 2.0 client ID for your calling service within the same project as the function you intend to secure, and utilize those credentials for invoking the function.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Create a service account with the Cloud Functions Invoker role, and utilize that service account for invoking the function.

**III. Create a service account with the Cloud Functions Invoker role, and utilize that service account for invoking the function.**

Here's the breakdown:

  * **Principle of Least Privilege:** The Cloud Functions Invoker role grants the service account the specific permission needed to invoke the function, nothing more. This minimizes the risk should the service account credentials be compromised.

  * **Identity and Access Management (IAM):** Google Cloud's IAM system provides granular control over permissions assigned to service accounts, allowing you to precisely manage which services can invoke the function.

Let's analyze the other options:

  * **I. Enable Identity-Aware Proxy...** IAP is excellent for protecting web applications accessed by users, but it's less suitable for direct service-to-service authorization within Google Cloud.

  * **II. Create a service account with the Cloud Functions Viewer role...** The Cloud Functions Viewer role only grants read-only access to functions and their configurations, not the ability to invoke them.

  * **IV. Generate an OAuth 2.0 client ID...** While OAuth 2.0 is a valid authorization mechanism, it adds a layer of complexity that might be unnecessary for simple service-to-service calls within the same project.

**References:**

[https://cloud.google.com/functions/docs/reference/iam/roles#cloud-functions-roles](https://cloud.google.com/functions/docs/reference/iam/roles#cloud-functions-roles  https://cloud.google.com/functions/docs/securing/authenticating)

[https://cloud.google.com/functions/docs/securing/authenticating](https://cloud.google.com/functions/docs/reference/iam/roles#cloud-functions-roles  https://cloud.google.com/functions/docs/securing/authenticating)

</details>

---

### Exam 1 · Q31

**Your operations team requires a script for listing Cloud Bigtable, Memorystore, and Cloud SQL databases within a project. The script should accommodate user-defined filter expressions to narrow down the presented results. How should you retrieve the data?**

- II. Employ the HBase API, Redis API, and MySQL connection to fetch database lists. Independently filter the results, then merge them for display.
- IV. Execute `**gcloud bigtable instances list**`, `**gcloud redis instances list**`, and `**gcloud sql databases list**` commands. Apply the `**--filter**` flag with each command, then showcase the results.
- I. Utilize the HBase API, Redis API, and MySQL connection to fetch database lists. Merge the results and apply the filter for displaying.
- III. Execute `**gcloud bigtable instances list**`, `**gcloud redis instances list**`, and `**gcloud sql databases list**` commands. Implement a filter within the application, then showcase the results.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Execute `**gcloud bigtable instances list**`, `**gcloud redis instances list**`, and `**gcloud sql databases list**` commands. Apply the `**--filter**` flag with each command, then showcase the results.

**IV. Execute gcloud bigtable instances list, gcloud redis instances list, and gcloud sql databases list commands. Apply the --filter flag with each command, then showcase the results.**

**Reasoning:**

  * **Efficiency and Simplicity:** The `gcloud` CLI is the most efficient way to interact with Google Cloud services. These commands directly provide the desired information without complex API interactions.

  * **Filtering at the Source:** The `--filter` flag for each command allows filtering during data retrieval. This is the most efficient approach, reducing processing required within your script.

  * **Consistency:** `gcloud` offers a consistent interface for these tasks, minimizing script complexity.

**Disadvantages of other options:**

  * **I & II. Unnecessary Complexity:** Using HBase, Redis, and MySQL APIs introduces unnecessary complexity. These APIs are designed for data interaction, not listing databases. Moreover, merging and filtering would add overhead to your script.

  * **III. Filtering Overhead:** Retrieving all data then filtering within the application is less efficient. It increases data transfer and puts more processing burden on your script.

Ref:

<https://cloud.google.com/sdk/gcloud/reference/topic/filter>s

</details>

---

### Exam 1 · Q38

**You have an HTTP Cloud Function that's triggered by POST requests. Each request contains a flat, unnested JSON structure with both numerical and textual data. Post-execution, the aggregated data must be promptly accessible for comprehensive analytics by multiple users concurrently. How should you store the submitted data persistently?**

- IV. Save each POST request's JSON data as an individual file within Cloud Storage, with the file name containing the request identifier.
- III. Process the JSON data from the POST request and store it in a regional Cloud SQL cluster.
- II. Process the JSON data from the POST request and stream it into BigQuery.
- I. Directly persist each POST request's JSON data into Datastore.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Process the JSON data from the POST request and stream it into BigQuery.

**II. Process the JSON data from the POST request and stream it into BigQuery.** Here's why:

  * **Analytics Focus:** BigQuery is explicitly designed for large-scale data analysis and querying. It excels at handling structured data (even from flat JSON) and enables complex analysis with SQL-like queries.

  * **Real-Time Streaming:** BigQuery's streaming ingestion allows data to be made available for analytics almost immediately after it's received by your Cloud Function, minimizing latency.

  * **Scalability & Concurrent Access:** BigQuery handles massive datasets, and its serverless nature means it scales seamlessly to support many concurrent analysis requests.

Let's analyze the other options:

  * **I. Directly persist each POST request's JSON data into Datastore:** Datastore is a NoSQL database better suited for storing and retrieving individual data entities with relationships. While it can store JSON, it's less optimal for large-scale, ad-hoc analytics involving complex aggregations.

  * **III. Process the JSON data ... store it in a regional Cloud SQL cluster:** Cloud SQL (MySQL, PostgreSQL) are relational databases. While they can handle JSON, their strength lies in storing highly structured data with well-defined relationships, not in the type of flexible analytics needed here.

  * **IV. Save each POST request's JSON data as an individual file...** Cloud Storage is object storage. This approach creates overhead with individual files and makes analysis complex, requiring you to merge data across files before querying.

</details>

---

### Exam 1 · Q44

**You're developing a microservice-based application intended for deployment on a Google Kubernetes Engine cluster. This application requires both reading from and writing to a Spanner database. Your objective is to ensure adherence to security best practices while minimizing code adjustments. How should you configure the application to access Spanner credentials?**

- IV. Safeguard the application credentials using Cloud Key Management Service and retrieve them as needed when establishing a database connection.
- III. Configure suitable routing rules and utilize a VPC-native cluster to establish a direct connection to the database.
- II. Protect the application credentials as Kubernetes Secrets and expose them as environment variables.
- I. Establish the required service accounts and employ Workload Identity to execute the pods.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Establish the required service accounts and employ Workload Identity to execute the pods.

**I. Establish the required service accounts and employ Workload Identity to execute the pods.**

Here's why this is the most secure and streamlined approach:

  * **Security:** Workload Identity eliminates the need to directly manage Spanner credentials within your pods or Kubernetes Secrets. Google handles the secure binding of service accounts and provides temporary tokens.

  * **Least Privilege:** You can associate each microservice with a specific service account that has only the necessary permissions on the Spanner database, adhering to the principle of least privilege.

  * **Minimal Code Changes:** Workload Identity integration often requires minimal adjustments to your application code, as the authentication flow is handled by the underlying Kubernetes environment.

  * **Google Best Practice:** This is the recommended approach by Google for secure access to GCP services from GKE.

**Why Other Options Are Less Ideal:**

  * **II. Kubernetes Secrets:** While Secrets help improve over storing credentials directly in code, they still introduce a layer of management and potential exposure within the cluster.

  * **III. VPC-native Cluster:** Network configuration impacts connectivity but doesn't directly address how your application handles credentials.

  * **IV. Cloud KMS:** Cloud KMS is great for encryption but adds complexity compared to Workload Identity for this scenario. Your application would still need a mechanism to retrieve and manage the decrypted credentials.

**References:**

[https://cloud.google.com/blog/products/containers-kubernetes/introducing-workload-identity-better-authentication-for-your-gke-applications](https://cloud.google.com/blog/products/containers-kubernetes/introducing-workload-identity-better-authentication-for-your-gke-applications  https://cloud.google.com/sql/docs/mysql/connect-kubernetes-engine#secrets   https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity)

[https://cloud.google.com/sql/docs/mysql/connect-kubernetes-engine#secrets ](https://cloud.google.com/blog/products/containers-kubernetes/introducing-workload-identity-better-authentication-for-your-gke-applications  https://cloud.google.com/sql/docs/mysql/connect-kubernetes-engine#secrets   https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity)

[https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity](https://cloud.google.com/blog/products/containers-kubernetes/introducing-workload-identity-better-authentication-for-your-gke-applications  https://cloud.google.com/sql/docs/mysql/connect-kubernetes-engine#secrets   https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity)

</details>

---

### Exam 1 · Q47

**As you develop a Compute Engine-hosted application in project A, you need to establish secure authentication to a Cloud Pub/Sub topic in project B. What should be your approach?**

- II. Equip the instances with a service account from project A, and authorize this service account as a publisher directly on the Cloud Pub/Sub topic.
- IV. Utilize Application Default Credentials with the private key of a service account from project A, and designate this service account as a publisher directly on the Cloud Pub/Sub topic in project B.
- I. Set up the instances with a service account from project B, then grant this service account publisher permissions on the Cloud Pub/Sub topic in project A.
- III. Configure Application Default Credentials to utilize the private key of a service account from project B, and assign this service account publisher rights in project A's Cloud Pub/Sub.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Equip the instances with a service account from project A, and authorize this service account as a publisher directly on the Cloud Pub/Sub topic.

**II. Equip the instances with a service account from project A, and authorize this service account as a publisher directly on the Cloud Pub/Sub topic.**

Let's break down why this approach excels:

  * **Principle of Least Privilege:** Granting the service account in project A (where your application runs), the `roles/pubsub.publisher` role on the topic in project B aligns with the principle of least privilege.

  * **Identity Ownership:** Project A, being the resource owner, naturally controls the identities used within its environment.

  * **Application Default Credentials (ADC):** ADCs simplify authentication management within your application code. They leverage the service account attached to the Compute Engine instance.

**Drawbacks of Other Options:**

  * **I. Set up the instances with a service account from project B ...**  
This creates a reverse dependency, where project B would manage credentials used by resources in project A, complicating management.

  * **III & IV. ... Utilize Application Default Credentials with the private key of a service account ...** Manually managing private keys introduces security risks and operational complexity compared to relying on ADCs.

**Reference:**  
<https://cloud.google.com/pubsub/docs/access-control>

</details>

---

### Exam 1 · Q48

**You aim to move files from an on-premises virtual machine to Google Cloud Storage for utilization within a Cloud DataProc Hadoop cluster in a GCP environment. Which command is the appropriate choice for this task?**

- I. `**gsutil cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/**`
- IV. `**gcloud dataproc cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/**`
- II. `**gcloud cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/**`
- III. `**hadoop fs cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/**`

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. `**gsutil cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/**`

**I. gsutil cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/**

**Explanation:**

  * `gsutil` is the command-line tool specifically designed to interact with Google Cloud Storage. It's the most efficient and reliable way to transfer files between your local machine and Google Cloud Storage buckets.

**Why Other Options Are Not Suitable:**

  * **II. gcloud cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/** While the `gcloud` tool has a `cp` command, it's intended for more general-purpose copying operations within the Google Cloud environment. For interacting specifically with Cloud Storage, `gsutil` is the preferred tool.

  * **III. hadoop fs cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/** The `hadoop fs` command with a `gs://` destination can work, but it requires the Google Cloud Storage connector for Hadoop. This adds a layer of setup and might be less efficient than using `gsutil` directly.

  * **IV. gcloud dataproc cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/** The `gcloud dataproc` tool doesn't have a `cp` command. It's designed for managing Cloud Dataproc clusters, not general data transfer tasks.

Ref:

<https://cloud.google.com/storage/docs/uploading-objects>

</details>

---

### Exam 1 · Q50

**Your application collects user input and publishes it to the user's contacts. This input is stored in a Cloud Spanner table. Given that your application prioritizes latency over consistency, how should you handle reads from Cloud Spanner?**

- II. Conduct stale reads using single-read methods.
- IV. Carry out stale reads using read-write transactions.
- III. Execute strong reads using single-read methods.
- I. Perform Read-Only transactions.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Conduct stale reads using single-read methods.

**II. Conduct stale reads using single-read methods.**

**Explanation:**

Since your application prioritizes fast reads and can tolerate slightly outdated data, stale reads offer the best balance:

  * **Low Latency:** Stale reads can often be served directly from a replica without the coordination required for strong reads, reducing overall latency.

  * **Read Scalability:** Stale reads help scale under high read loads by reducing contention on the Spanner leader.

  * **Single-Read Methods:** These methods are the most efficient way to perform reads, adding minimal overhead.

**Why Other Options Are Less Ideal:**

  * **I. Perform Read-Only transactions.** Read-only transactions still offer consistency guarantees that might involve contacting the Spanner leader, adding potential overhead.

  * **III. Execute strong reads using single-read methods.** These ensure the latest data but introduce the potential for increased latency due to leader communication.

  * **IV. Carry out stale reads using read-write transactions.** Read-write transactions are intended for scenarios where you need both reads and writes within the same transaction.

**References:**

[https://cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions](https://cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions  https://cloud.google.com/spanner/docs/reads)

[https://cloud.google.com/spanner/docs/reads](https://cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions  https://cloud.google.com/spanner/docs/reads)

</details>

---

### Exam 1 · Q51

**How can you enable your application, developed within Google Kubernetes Engine (GKE), to access Google Cloud services across various projects?**

- IV. Utilize GKE role-based access control (RBAC) with a designated Google service account.
- I. Configure a Google service account for the GKE nodes.
- III. Securely store the Google service account credentials within a Kubernetes Secret.
- II. Implement Workload Identity with a designated Google service account for running the Pod.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Implement Workload Identity with a designated Google service account for running the Pod.

**II. Implement Workload Identity with a designated Google service account for running the Pod.**

Here's why this is the most secure and streamlined approach:

  * **Identity-based Access:** Workload Identity eliminates the need to manage long-lived credentials within your Kubernetes cluster. It binds Kubernetes Service Accounts (KSAs) to Google Service Accounts (GSAs), granting fine-grained IAM permissions.

  * **Least Privilege:** You can associate each Pod with a specific GSA, adhering to the principle of least privilege within GCP.

  * **Google Best Practice:** Google explicitly recommends Workload Identity for secure access to Google Cloud services from GKE.

**Why Other Options Are Less Ideal:**

  * **I. GKE Node Service Account:** This grants access to the _entire node,_ not just individual applications, violating the least privilege principle.

  * **III. Kubernetes Secrets:** While secrets are helpful, they still introduce the risk of credentials being exposed within the cluster.

  * **IV. GKE RBAC:** GKE RBAC controls permissions _within_ the Kubernetes cluster, not access to external Google Cloud services.

References:

[https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity](https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity  https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#what_is)

[https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#what_is](https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity  https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#what_is)

</details>

---

### Exam 1 · Q55

**Which tool should you employ to construct an architecture that authenticates, enforces quotas, and tracks metrics for API callers?**

**

**

**Diagram showing a Google Cloud architecture. An arrow from a “computer” to “Cloud Load Balancing”. An arrow from “Cloud Load Balancing” to an empty box. An arrow from the empty box to “PHP application”.**

- C. Consider Identity-Aware Proxy (IAP) for securing your APIs by verifying user identities and controlling access based on their permissions, while also offering features for monitoring and reporting API usage metrics.
- D. Leverage GKE Ingress for HTTP(S) Load Balancing to configure routing rules and manage traffic efficiently to your PHP application, while incorporating additional layers of security and metrics reporting as per your requirements.
- B. Choose Cloud Endpoints to streamline the process of building, deploying, and managing APIs with robust security features, including authentication mechanisms, quota enforcement capabilities, and comprehensive metric tracking for API usage.
- A. Opt for Cloud Run to establish a scalable and fully managed environment for deploying containerized applications, ensuring efficient execution and seamless integration with authentication, quota enforcement, and metric reporting functionalities.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Choose Cloud Endpoints to streamline the process of building, deploying, and managing APIs with robust security features, including authentication mechanisms, quota enforcement capabilities, and comprehensive metric tracking for API usage.

**B. Choose Cloud Endpoints to streamline the process of building, deploying, and managing APIs with robust security features, including authentication mechanisms, quota enforcement capabilities, and comprehensive metric tracking for API usage.**

Here's why Cloud Endpoints is the optimal choice:

  * **Authentication:** Cloud Endpoints offers built-in authentication mechanisms like OAuth 2.0, API keys, and IAM roles, allowing you to control access to your API.

  * **Quota Enforcement:** Cloud Endpoints enables you to define quotas and rate limits for API calls, preventing misuse and ensuring resource optimization.

  * **Metric Tracking:** Cloud Endpoints provides comprehensive metrics and logging capabilities that give you insights into API usage patterns and performance.

  * **Integration with Cloud Load Balancing:** Cloud Endpoints seamlessly integrates with Cloud Load Balancing, which is already present in your architecture, for efficient traffic management.

**Why Other Options Are Less Ideal:**

  * **A. Cloud Run:** While Cloud Run is a great platform for deploying containerized applications, it lacks the built-in security features like authentication and quota enforcement that Cloud Endpoints offers. You'd need additional tools to achieve these functionalities.

  * **C. Identity-Aware Proxy (IAP):** IAP primarily focuses on user identity verification and access control at the perimeter level. While it can provide some usage metrics, it's not as comprehensive as Cloud Endpoints for API-specific metrics and quota enforcement.

  * **D. GKE Ingress:** GKE Ingress is a load balancing solution for containerized applications deployed on Google Kubernetes Engine (GKE). It doesn't have built-in functionalities for authentication, quota enforcement, or detailed API metrics tracking.

**References:**

[https://cloud.google.com/endpoints/docs/openapi/quotas-configure](https://cloud.google.com/endpoints/docs/openapi/quotas-configure  https://cloud.google.com/endpoints/docs/openapi/monitoring-your-api)

[https://cloud.google.com/endpoints/docs/openapi/monitoring-your-api](https://cloud.google.com/endpoints/docs/openapi/quotas-configure  https://cloud.google.com/endpoints/docs/openapi/monitoring-your-api)

</details>

---

### Exam 1 · Q57

**To ensure proper authentication of services accessing various Google Cloud APIs within a Google Kubernetes Engine (GKE) cluster, adhering to Google's recommended best practices, which approaches should you implement? (Choose two)**

- V. Utilize gcloud to bind Google service accounts and Kubernetes service accounts using roles/iam.workloadIdentityUser, which is a feasible approach but not as endorsed as enabling Workload Identity directly on the cluster.
- IV. Storing Google service account keys in Secret Manager (as mentioned) could be a method, but it's not a recommended best practice by Google for authenticating services within a GKE cluster.
- I. Employ the service account linked to the GKE node, enabling services to authenticate with Google Cloud APIs using the node's identity.
- III. Accessing Google service account keys from Secret Manager (as mentioned) could be a method, but it's not a recommended best practice by Google for authenticating services within a GKE cluster.
- II. Enable Workload Identity on the cluster through the gcloud command-line tool, establishing a secure mechanism for workloads operating in the cluster to access Google Cloud services with fine-grained IAM permissions.

<details><summary>Answer &amp; explanation</summary>

**Correct:** V. Utilize gcloud to bind Google service accounts and Kubernetes service accounts using roles/iam.workloadIdentityUser, which is a feasible approach but not as endorsed as enabling Workload Identity directly on the cluster. **|** II. Enable Workload Identity on the cluster through the gcloud command-line tool, establishing a secure mechanism for workloads operating in the cluster to access Google Cloud services with fine-grained IAM permissions.

The recommended approaches for ensuring proper authentication of services accessing various Google Cloud APIs within a Google Kubernetes Engine (GKE) cluster are:

**II. Enable Workload Identity on the cluster through the gcloud command-line tool, establishing a secure mechanism for workloads operating in the cluster to access Google Cloud services with fine-grained IAM permissions.**

**V. Utilize gcloud to bind Google service accounts and Kubernetes service accounts using roles/iam.workloadIdentityUser, which is a feasible approach but not as endorsed as enabling Workload Identity directly on the cluster.**

Explanation:

  * Option II suggests enabling Workload Identity on the GKE cluster, which is a recommended best practice by Google. Workload Identity allows GKE workloads to securely access Google Cloud services with fine-grained IAM permissions, without the need to manage service account keys directly.

  * Option V proposes binding Google service accounts and Kubernetes service accounts using roles/iam.workloadIdentityUser. While it's a feasible approach, it's not as endorsed as enabling Workload Identity directly on the cluster, but it still provides a secure mechanism for service authentication.

Options I, III, and IV are not recommended best practices:

  * Option I suggests employing the service account linked to the GKE node for authentication. While this might work, it's not the recommended approach because it lacks granularity and control over IAM permissions.

  * Option III mentions accessing Google service account keys from Secret Manager, which is not a recommended best practice by Google for authenticating services within a GKE cluster. It introduces unnecessary complexity and potential security risks.

  * Option IV suggests storing Google service account keys in Secret Manager, which again is not a recommended best practice. Managing service account keys manually introduces security risks and operational overhead.

**References:**

[https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity  https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable_on_existing_cluster)

[https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable_on_existing_cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity  https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable_on_existing_cluster)

</details>

---

### Exam 2 · Q9

**As you develop an event-driven application, you've set up a Pub/Sub topic to receive messages. Your objective is to process these messages in real-time while ensuring the application operates independently, incurring costs only upon message arrival. How should you architect this setup?**

- III. Deploy the application on Google Kubernetes Engine, utilizing the Pub/Sub API to establish a pull subscription for reading messages from the Pub/Sub topic.
- I. Deploy the application on Compute Engine, leveraging a Pub/Sub push subscription for processing incoming messages from the topic.
- IV. Deploy your code on Cloud Functions, employing a Pub/Sub trigger to manage incoming messages from the topic.
- II. Deploy your code on Cloud Functions, utilizing a Pub/Sub trigger to invoke the function. Use the Pub/Sub API to establish a pull subscription for message retrieval from the topic.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Deploy your code on Cloud Functions, employing a Pub/Sub trigger to manage incoming messages from the topic.

The most suitable architecture for your event-driven application that processes messages in real-time, operates independently, and incurs costs only upon message arrival is:

**IV. Deploy your code on Cloud Functions, employing a Pub/Sub trigger to manage incoming messages from the topic.**

Here's why:

  * **Real-time processing:** Cloud Functions are triggered instantly upon message arrival in the Pub/Sub topic, ensuring real-time message handling.

  * **Independent operation:** Cloud Functions are serverless, meaning you don't need to manage any infrastructure. They scale automatically based on the incoming message volume.

  * **Cost efficiency:** Cloud Functions are billed based on execution time and the number of invocations. You only pay when messages are processed, making it a cost-effective solution for event-driven applications.

  * **Simplified development:** Cloud Functions allow you to focus on your application logic without worrying about infrastructure setup or scaling.

Let's look at why the other options aren't as ideal:

  * **I. Compute Engine:** This requires you to manage a virtual machine instance, which incurs costs even when no messages are being processed.

  * **II. Cloud Functions with pull subscription:** While this uses Cloud Functions, pulling messages manually adds complexity and might introduce delays in message processing compared to a Pub/Sub trigger.

  * **III. Google Kubernetes Engine:** GKE provides more control but also requires infrastructure management and might not be as cost-efficient as Cloud Functions for this use case.

**Therefore, deploying your code on Cloud Functions with a Pub/Sub trigger is the most effective way to meet your requirements for real-time processing, independent operation, and cost efficiency in your event-driven application.**

</details>

---

### Exam 2 · Q16

**To enhance the performance of your Go application when interacting with a Cloud Spanner database, which approach should you adopt based on Google's recommended best practices?**

- I. Utilize Cloud Client Libraries to interface with Cloud Spanner.
- II. Utilize Google API Client Libraries to interact with Cloud Spanner.
- III. Employ a custom gRPC client library for writing to Cloud Spanner.
- IV. Implement a third-party HTTP client library for writing to Cloud Spanner.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Utilize Cloud Client Libraries to interface with Cloud Spanner.

To enhance the performance of your Go application when interacting with a Cloud Spanner database, the best approach based on Google's recommended practices is:

**I. Utilize Cloud Client Libraries to interface with Cloud Spanner.**

Here's why:

  * **Optimized for performance:** Cloud Client Libraries are specifically designed and optimized for interacting with Google Cloud services, including Cloud Spanner. They handle low-level details like connection management, retries, and error handling, allowing you to focus on your application logic.

  * **Idiomatic Go code:** Cloud Client Libraries provide a natural and intuitive way to interact with Cloud Spanner using Go idioms and conventions, making your code easier to read and maintain.

  * **Built-in best practices:** Cloud Client Libraries incorporate Google's recommended best practices for interacting with Cloud Spanner, ensuring optimal performance and reliability out of the box.

Let's look at why the other options aren't as suitable:

  * **Google API Client Libraries:** While these libraries can be used to interact with various Google APIs, they are not as specialized as Cloud Client Libraries for Cloud Spanner and might not offer the same level of performance optimization.

  * **Custom gRPC client library:** Building a custom gRPC client library requires significant development effort and might not be as efficient or well-maintained as the official Cloud Client Library.

  * **Third-party HTTP client library:** Using a third-party HTTP client library adds another layer of complexity and potential performance overhead compared to the dedicated Cloud Client Library.

**Therefore, utilizing Cloud Client Libraries is the recommended approach for maximizing the performance of your Go application when working with Cloud Spanner, aligning with Google's best practices.**

**Reference:**

<https://cloud.google.com/apis/docs/cloud-client-libraries>

</details>

---

### Exam 2 · Q24

**You are developing a social media application and planning to implement an image upload feature. The images can range from 2 MB to 1 GB in size. You aim to minimize infrastructure operations for this feature. What approach should you take?**

- III. Configure a web server on GCP to handle user image uploads. Establish a file store to store uploaded files, and modify the application to fetch images from this file store.
- I. Modify the application to directly accept images and store them in the database along with other user information.
- II. Implement signed URLs for Cloud Storage in the application. Provide these signed URLs to clients for uploading images to Cloud Storage.
- IV. Create individual buckets for each user in Cloud Storage. Assign separate service accounts to each bucket for write access. Provide client applications with the necessary service account credentials based on user information to upload images to Cloud Storage.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Implement signed URLs for Cloud Storage in the application. Provide these signed URLs to clients for uploading images to Cloud Storage.

**II. Implement signed URLs for Cloud Storage in the application. Provide these signed URLs to clients for uploading images to Cloud Storage.**

Explanation:

  * **Scalability and Offloading:** Using Cloud Storage and signed URLs lets you leverage Google's highly scalable object storage. It removes the burden of managing image storage and handling potentially large uploads from your application infrastructure.

  * **Security:** Signed URLs can be generated with expiration dates and access restrictions, adding a layer of control.

  * **Operational Simplicity:** This approach avoids the operational overhead of setting up and maintaining web servers and file stores.

  * **Direct Uploads:** Clients upload images directly to Cloud Storage, improving performance and user experience.

**Why Other Options Are Less Ideal:**

  * **I. Modify the application ... store them in the database ...** Storing large images in a database introduces scalability issues and can lead to database performance bottlenecks.

  * **III. Configure a web server ...** This approach adds complexity by requiring you to manage additional infrastructure (web servers, file storage) compared to using Cloud Storage directly.

  * **IV. Create individual buckets ...** Managing numerous buckets and service accounts per user significantly increases complexity and might have cost implications.

</details>

---

### Exam 2 · Q37

**As a developer within a large organization, you manage an application written in Go deployed on a production Google Kubernetes Engine (GKE) cluster. You're tasked with implementing a new feature that requires access to BigQuery. Your objective is to grant BigQuery access to your GKE cluster, adhering to Google's recommended best practices. How should you proceed?**

- III. Generate a Google service account with BigQuery access, store the Google service account JSON key in Secret Manager, and implement an init container to retrieve the secret for the application's usage.
- IV. Establish both a Google service account and a Kubernetes service account, enable Workload Identity on the GKE cluster, and specify the Kubernetes service account within the application Deployment configuration.
- I. Generate a Google service account with BigQuery access, store the associated JSON key securely in Secret Manager, and utilize the Go client library to access the JSON key.
- II. Generate a Google service account with BigQuery access, incorporate the Google service account JSON key into a Kubernetes secret, and configure the application to utilize this secret.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Establish both a Google service account and a Kubernetes service account, enable Workload Identity on the GKE cluster, and specify the Kubernetes service account within the application Deployment configuration.

The best answer is

**IV: Establish both a Google service account and a Kubernetes service account, enable Workload Identity on the GKE cluster, and specify the Kubernetes service account within the application Deployment configuration.**

Here's why this approach aligns with Google's best practices:

  * **Workload Identity:** This is the most secure and recommended way to manage service account credentials within GKE. It eliminates the need to handle service account keys directly within your pods, reducing the risk of exposing them.

  * **Principle of Least Privilege:** Assign the necessary BigQuery permissions only to the Google service account, ensuring that it can't access resources other than those required for the application.

**Why other options are less ideal:**

  * **I, II, and III:** All involve direct handling and storage of service account keys either in secrets or an init container. While functional, this increases the potential attack surface if those keys are compromised.

**References:**

<https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#what_is>

</details>

---

### Exam 2 · Q42

**As a developer working on an internal payroll processing application, you're tasked with implementing a component for timesheet submission, triggering various independent steps. Which approach should you take to ensure effective communication with downstream systems and accommodate future step additions?**

- IV. Develop a timesheet microservice deployed on Google Kubernetes Engine, orchestrating calls to each downstream step and awaiting successful responses before proceeding.
- III. Set up a Pub/Sub topic dedicated to timesheet submissions, with subscriptions created for each downstream team to receive notifications.
- II. Establish separate Pub/Sub topics for each step, with subscriptions tailored for downstream development teams to subscribe to their specific step.
- I. Implement individual Cloud Functions for each step, enabling direct calls to respective downstream systems.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Set up a Pub/Sub topic dedicated to timesheet submissions, with subscriptions created for each downstream team to receive notifications.

**III. Set up a Pub/Sub topic dedicated to timesheet submissions, with subscriptions created for each downstream team to receive notifications.**

Here's why this approach excels:

  * **Loose Coupling:** Pub/Sub promotes a decoupled architecture. The timesheet submission component simply publishes an event; downstream systems subscribe without tight dependencies.

  * **Scalability:** New steps can be easily added by creating additional subscriptions, without needing to modify the core timesheet submission logic.

  * **Reliability:** Pub/Sub provides durable messaging, helping handle temporary issues with downstream systems.

  * **Future-Proof:** This architecture aligns with event-driven patterns, accommodating changing requirements gracefully.

</details>

---

### Exam 2 · Q46

**You are utilizing Cloud Run to host a web application and require a secure method to retrieve and display the application's project ID and region to users. Your goal is to implement the most performant approach. What action should you take?**

- II. Access the Google Cloud console, navigate to the Project Dashboard to collect configuration details, and then proceed to the Cloud Run "Variables & Secrets" tab to add the desired environment variables in Key:Value format.
- I. Utilize HTTP requests to query the metadata server available at the `**http://metadata.google.internal/**` endpoint with the `**Metadata-Flavor: Google**` header.
- IV. Make an API call to the Cloud Asset Inventory API from the application, formatting the request to include instance metadata.
- III. Access the Google Cloud console, navigate to the Project Dashboard to collect configuration details, and write the application configuration information to Cloud Run's in-memory container filesystem.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Utilize HTTP requests to query the metadata server available at the `**http://metadata.google.internal/**` endpoint with the `**Metadata-Flavor: Google**` header.

**I. Utilize HTTP requests to query the metadata server available at the**[**http://metadata.google**](http://metadata.google/)**.internal/ endpoint with the Metadata-Flavor: Google header.**

Explanation:

  * **Efficiency:** Accessing this built-in metadata server is the most direct and performant way to retrieve information about the Cloud Run environment.

  * **Specificity:** You can query specific values like `computeMetadata/v1/project/project-id` and `computeMetadata/v1/instance/zone` for the project ID and region respectively.

  * **Security:** The metadata server is only accessible from within the service instance itself, enhancing security.

  * **Dynamic:** The metadata server provides up-to-date information.

Why Other Options Are Less Ideal:

  * **II. Access the Google Cloud console, navigate to the Project Dashboard to collect configuration details, and then proceed to the Cloud Run "Variables & Secrets" tab to add the desired environment variables in Key:Value format.**

    * **Manual Intervention:** This requires manual updates every time your deployment changes which is inefficient and prone to errors.

  * **III. Access the Google Cloud console, navigate to the Project Dashboard to collect configuration details, and write the application configuration information to Cloud Run's in-memory container filesystem.**

    * **Static:** This method doesn't provide the dynamic aspect of retrieving real-time project and region information. It also creates potential inconsistency if the information changes.

  * **IV. Make an API call to the Cloud Asset Inventory API from the application, formatting the request to include instance metadata.**

    * **Overhead:** Calling an external API introduces additional latency and complexity compared to the metadata server.

**Here's a simple example (Python) of how to query the metadata server:**

**Python**
    
          1.  import requests
      2.  
      3. def get_project_id():
      4.     metadata_url = 'http://metadata.google.internal/computeMetadata/v1/project/project-id'
      5.     headers = {'Metadata-Flavor': 'Google'}
      6.     response = requests.get(metadata_url, headers=headers)
      7.     return response.text
      8.  
      9. print(get_project_id())

**Reference:**

<https://cloud.google.com/run/docs/container-contract#metadata-server>

</details>

---

### Exam 2 · Q49

**Your application relies on service accounts for authentication to GCP services, utilizing credentials stored on its Compute Engine virtual machine instances. You aim to securely distribute these credentials to the host instances. What's the recommended approach?**

- III. Generate a P12 file from the GCP Console post-deployment, transferring the credentials to the host instance prior to application launch.
- II. Utilize the instance's service account Application Default Credentials for authentication to the necessary resources.
- IV. Embed the credential JSON file within your application's source repository, integrating it into the deployment process via CI/CD for package delivery to the instance.
- I. Implement HTTP signed URLs for secure access to the required resources.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Utilize the instance's service account Application Default Credentials for authentication to the necessary resources.

**II. Utilize the instance's service account Application Default Credentials for authentication to the necessary resources.**

Here's why this is the most secure and streamlined approach:

  * **Automatically Managed by Google:** Compute Engine VMs have metadata servers providing access to the associated service account's credentials. Google handles rotation and management of these credentials.

  * **No Manual Distribution** : You avoid the risks of storing and transferring sensitive credential files.

  * **Least Privilege:** Libraries that support Application Default Credentials (ADCs) make it easy to grant the instance only the permissions it needs by assigning appropriate IAM roles to the service account.

**Why Other Options are Less Ideal:**

  * **I. Implement HTTP signed URLs ...** Signed URLs are primarily for granting time-limited access to objects, not for general application authentication to most GCP services.

  * **III. Generate a P12 file ...** Manually transferring credentials creates security risks (potential leaks) and management overhead.

  * **IV. Embed the credential JSON file ...** Embedding credentials in your source code is extremely insecure, risking exposure if the repository is compromised.

**Reference:**

[https://cloud.google.com/docs/authentication/production#automatically](https://cloud.google.com/docs/authentication/production#automatically  https://cloud.google.com/compute/docs/api/how-tos/authorization:)

[https://cloud.google.com/compute/docs/api/how-tos/authorization:](https://cloud.google.com/docs/authentication/production#automatically  https://cloud.google.com/compute/docs/api/how-tos/authorization:)

</details>

---

### Exam 2 · Q56

**You've created a JavaScript web application requiring access to Google Drive's API to store files in users' Google Drives. What's the recommended authorization approach for your application?**

- II. Generate a SAML token.
- IV. Generate an OAuth Client ID.
- I. Generate an API key.
- III. Generate a service account.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Generate an OAuth Client ID.

**IV. Generate an OAuth Client ID.**

**Justification:**

  * **User-Centric Authorization:** OAuth 2.0 is designed for applications to access user data on behalf of the user, which is exactly what your application needs to do (store files in a user's Drive).

  * **Fine-grained Scopes:** OAuth allows you to request specific access scopes like "[invalid URL removed]" to limit your app's access to only the Drive functionality it needs.

  * **Security and User Control:** OAuth provides a secure authorization flow where users explicitly grant your application permission. They can revoke this access if needed.

**Why Other Options are Less Ideal:**

  * **I. Generate an API key.** API keys primarily identify your project to Google but don't associate the request with a specific user. They lack the fine-grained control needed for user-specific data access.

  * **II. Generate a SAML token.** SAML (Security Assertion Markup Language) is used for Single Sign-On (SSO) with identity providers and not directly related to authorizing data access for web apps.

  * **III. Generate a service account.** Service accounts are designed for server-to-server communication where there's no direct user interaction involved.

**References:**

<https://developers.google.com/drive/api/guides/api-specific-auth>

</details>

---

### Exam 3 · Q7

**In developing a Java Web Server, requiring interaction with Google Cloud services through the Google Cloud API on behalf of users, what workflow should be implemented for user authentication to the Google Cloud API?**

- II. Upon user arrival, request Google username and password. Forward these credentials in an HTTPS request to the Google Cloud authorization server to obtain an access token. Validate user credentials at the Google server, which returns an access token to the application for subsequent Google Cloud API calls.
- III. Redirect users to a Google Cloud consent screen on arrival, presenting requested permissions. Prompt users to sign in via SSO to their Google Account. After sign-in and consent, the application receives an authorization code from a Google server, stored in the browser's cookies. Authenticate to the Google Cloud API using this authorization code.
- IV. Upon user arrival, redirect to a Google Cloud consent screen displaying requested permissions. Prompt users to sign in via SSO to their Google Account. Following sign-in and consent, the application receives an authorization code from a Google server. The application exchanges this code for an access token with another request to the Google server, subsequently used for Google Cloud API calls.
- I. Prompt users for their Google username and password upon arrival at the application. Store an SHA password hash in the application's database along with the username. Authenticate to the Google Cloud API using HTTPS requests, including the username and password hash in the Authorization request header.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Upon user arrival, redirect to a Google Cloud consent screen displaying requested permissions. Prompt users to sign in via SSO to their Google Account. Following sign-in and consent, the application receives an authorization code from a Google server. The application exchanges this code for an access token with another request to the Google server, subsequently used for Google Cloud API calls.

The correct answer is 

**IV: Upon user arrival, redirect to a Google Cloud consent screen displaying requested permissions. Prompt users to sign in via SSO to their Google Account. Following sign-in and consent, the application receives an authorization code from a Google server. The application exchanges this code for an access token with another request to the Google server, subsequently used for Google Cloud API calls.**

**Here's why this is the best approach:**

  * **Security:** It follows the OAuth 2.0 standard, a secure and widely used framework for delegated authorization. Your application never handles the user's Google credentials directly, reducing security risks.

  * **User Experience:** Leverages Google's Single Sign-On (SSO), providing a seamless login experience for users as they likely already have active Google account sessions.

  * **Control:** The consent screen allows users to understand and explicitly grant the specific permissions your application needs to interact with Google Cloud API on their behalf.

  * **Standard Compliance:** Adheres to industry-standard best practices for handling user authentication and authorization.

**Why other options are not ideal:**

  * **I. Prompt users for their Google username and password...** This is a major security risk. You should never directly ask for or store user passwords. It undermines trust and exposes your application to credential theft.

  * **II. Upon user arrival, request Google username and password...** While slightly better than option I, it still involves your application handling user credentials and carries the risk of those being compromised.

  * **III. Redirect users to a Google Cloud consent screen...** This option is partially correct but doesn't go far enough. While it utilizes the consent screen, it doesn't describe the crucial step of exchanging the authorization code for an access token, which is what ultimately allows your application to make API calls.

**Reference:**

<https://developers.google.com/identity/protocols/oauth2>

</details>

---

### Exam 3 · Q9

**You've recently developed an application and now need to access the Cloud Storage API from a Compute Engine instance without a public IP address. What's the best approach?**

- IV. Enable Private Google Access
- III. Implement Shared VPC networks
- II. Utilize VPC Network Peering
- I. Opt for Carrier Peering

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Enable Private Google Access

**IV. Enable Private Google Access**

Here's why this is the most suitable option:

  * **Internal Networking:** Private Google Access allows instances with private IPs to reach Google APIs and services using internal IP addresses within Google's network.

  * **Security:** This approach eliminates the need to expose your Compute Engine instance to the public internet, improving security posture.

  * **Simplicity:** Private Google Access is often a simple configuration setting on the subnet level, making it easy to implement.

**Why Other Options Are Less Ideal:**

  * **I. Carrier Peering:** Carrier peering is primarily used for connecting your on-premises network to Google's network and is unrelated to accessing internal Google Cloud services without public IPs.

  * **II. VPC Network Peering:** While network peering allows communication between different VPC networks, it mainly targets resource sharing and doesn't directly impact access to Google APIs..

  * **III. Shared VPC Networks:** Shared VPC enables resource sharing across projects but doesn't inherently grant access to Google APIs from private instances.

**Reference:**

<https://cloud.google.com/vpc/docs/private-google-access>

</details>

---

### Exam 3 · Q13

**In an ANSI-SQL compliant database, you have two tables with matching columns that require swift combination into a single table, eliminating duplicate rows from the result. What's the optimal approach?**

- III. Leverage the UNION operator in SQL for table merging.
- I. Utilize the JOIN operator in SQL for table merging.
- II. Employ nested WITH statements for table combination.
- IV. Deploy the UNION ALL operator in SQL for table merging.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Leverage the UNION operator in SQL for table merging.

**III. Leverage the UNION operator in SQL for table merging.**

**Explanation:**

The `UNION` operator in SQL specifically addresses the goal of combining data from multiple tables while removing duplicates:

  * **Combination:** The `UNION` operator appends the results of one query below the results of another.

  * **Duplicate Removal:** `UNION` automatically eliminates any duplicate rows from the combined result set.

**Why Other Options Are Less Ideal:**

  * **I. Utilize the JOIN operator in SQL for table merging.** While `JOIN` is excellent for combining tables based on related columns, it doesn't inherently remove duplicates. You'd need additional clauses (`DISTINCT`) to achieve the same behavior as `UNION`.

  * **II. Employ nested WITH statements for table combination.** `WITH` statements (Common Table Expressions) are useful for simplifying complex queries but don't directly offer the functionality of `UNION` in this case.

  * **IV. Deploy the UNION ALL operator in SQL for table merging.** `UNION ALL` appends results like `UNION` but _retains_ duplicate rows. This does not satisfy the requirement of duplicate elimination.

</details>

---

### Exam 3 · Q21

**In developing a new public-facing application, you're tasked with retrieving specific properties in the metadata of users' objects within their Cloud Storage buckets while adhering to privacy and data residency regulations, ensuring only metadata is retrieved, not object data. The goal is to optimize retrieval performance. How should you approach metadata retrieval?**

- I. Employ the patch method for metadata retrieval.
- IV. Use the fields request parameter to retrieve only the desired metadata properties, enhancing retrieval performance.
- II. Utilize the compose method for efficient metadata extraction.
- III. Employ the copy method to retrieve metadata while preserving privacy and data residency requirements.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Use the fields request parameter to retrieve only the desired metadata properties, enhancing retrieval performance.

**Best Option:**

  * **IV. Use the fields request parameter to retrieve only the desired metadata properties, enhancing retrieval performance.**

**Reasons for its superiority:**

  * **Targeted Retrieval:** The `fields` parameter provides the most direct way to extract specific metadata elements without retrieving unnecessary data. This translates to optimized network traffic and reduced processing time.

  * **Efficiency:** Minimizing data transfer significantly enhances the performance of metadata retrieval operations.

  * **Compliance:** This approach adheres to privacy and data residency regulations by ensuring that you only access the necessary metadata and avoid retrieving any sensitive object data.

**Why other options are less ideal:**

  * **I. Employ the patch method for metadata retrieval.** The `patch` method is primarily designed to update metadata rather than simply retrieve it. It would often involve fetching the entire metadata object, making it less efficient.

  * **II. Utilize the compose method for efficient metadata extraction.** The `compose` method is used for combining multiple objects in Cloud Storage. It's not relevant to the task of retrieving metadata from a single object.

  * **III. Employ the copy method to retrieve metadata while preserving privacy and data residency requirements.** While copying an object preserves its metadata, this method is primarily focused on creating duplicates. It is less efficient for pure metadata retrieval compared to the `fields` parameter.

**Reference:**  
[https://cloud.google.com/storage/docs/json_api/v1/objects/get https://firebase.google.com/docs/storage/web/file-metadata#get_file_metadata](https://cloud.google.com/storage/docs/json_api/v1/objects/get   https://firebase.google.com/docs/storage/web/file-metadata#get_file_metadata)

</details>

---

### Exam 3 · Q27

**In Google Kubernetes Engine (GKE), you aim to update your application for authorized requests to Google Cloud managed services, ensuring a one-time setup while adhering to security best practices for auto-rotating security keys stored in an encrypted manner. Given that you've already configured a service account with the necessary access to Google Cloud services, what should be your next step?**

- III. Embed the exported Google Cloud service account directly into the application's source code.
- IV. Upload the exported Google Cloud service account to HashiCorp Vault to generate a dynamic service account for your application.
- I. Implement Workload Identity to associate the Google Cloud service account with your GKE Pod.
- II. Export the Google Cloud service account and provide it to the Pod as a Kubernetes Secret.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Implement Workload Identity to associate the Google Cloud service account with your GKE Pod.

**I. Implement Workload Identity to associate the Google Cloud service account with your GKE Pod.**

Here's why this choice stands out:

  * **Security:** Workload Identity eliminates the need to manage long-lived service account keys directly within your application or cluster. This substantially reduces the risk of keys being leaked or compromised.

  * **Best Practice Alignment:** Google recommends Workload Identity as the preferred method for securely authenticating GKE workloads to Google Cloud services.

  * **Key Rotation:** Workload Identity handles automatic key rotation for you, improving security posture without manual intervention.

  * **Simplicity:** Once configured, Workload Identity provides a seamless and secure way for your GKE pods to obtain the permissions they need.

**Why Other Options Are Not Ideal**

  * **II. Export the Google Cloud service account and provide it to the Pod as a Kubernetes Secret.**

    * **Security Risk:** Secrets, even when encrypted, are more vulnerable to leakage than Workload Identity's dynamic authorization mechanism.

    * **Management Overhead:** You would be responsible for secure key storage and rotation.

  * **III. Embed the exported Google Cloud service account directly into the application's source code.**

    * **Major Security Flaw:** This is extremely insecure! Hardcoding credentials make them highly susceptible to exposure in a source code leak.

  * **IV. Upload the exported Google Cloud service account to HashiCorp Vault to generate a dynamic service account for your application.**

    * **Unnecessary Complexity:** While HashiCorp Vault offers strong security features, it introduces additional infrastructure to manage and maintain, when Workload Identity provides a simpler, more integrated solution within GKE.

**Reference:**

<https://cloud.google.com/iam/docs/best-practices-service-accounts#use-workload-identity>

</details>

---

### Exam 3 · Q28

**While developing a new application deployed on Cloud Run and leveraging Cloud Functions, managing ENV variables for interservice communication has become challenging with each feature deployment. Seeking a scalable solution, how should you implement dynamic discovery?**

- III. Adopt a well-documented naming convention to rename Cloud Functions and Cloud Run services endpoints.
- II. Establish a Service Directory namespace, utilizing API calls to register services during deployment and query them at runtime.
- I. Configure your microservices to utilize the Cloud Run Admin and Cloud Functions APIs for querying deployed services within the Google Cloud project.
- IV. Deploy HashiCorp Consul on a single Compute Engine instance, registering services with Consul during deployment and querying them at runtime.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Establish a Service Directory namespace, utilizing API calls to register services during deployment and query them at runtime.

**Correct Option:** **II. Establish a Service Directory namespace, utilizing API calls to register services during deployment and query them at runtime.**

**Explanation:**

  * **Designed for Dynamic Discovery:** Service Directory is Google Cloud's native solution specifically designed for service registration and discovery. It handles dynamic changes as your application evolves.

  * **Scalability:** Service Directory is a managed service, providing scalability and reliability without needing to manage your own infrastructure.

  * **Ease of Integration:** It integrates well with other GCP services (Cloud Run, Cloud Functions), offering APIs for seamless registration and discovery.

**Why other options are less ideal:**

  * **I. Cloud Run/Functions APIs:** While these APIs provide some service information, they are not primarily designed for service discovery and might become complex to manage at scale.

  * **III. Naming Conventions:** Relying solely on naming conventions is not robust, prone to errors, and hard to maintain as the application grows.

  * **IV. Consul on Compute Engine:** Consul is a powerful service discovery tool, but deploying and managing it on a Compute Engine instance introduces overhead and potential scaling limitations.

**Reference:**

[https://medium.com/google-cloud/fine-grained-cloud-dns-iam-via-service-directory-446058b4362e https://cloud.google.com/service-directory/docs/overview](https://medium.com/google-cloud/fine-grained-cloud-dns-iam-via-service-directory-446058b4362e   https://cloud.google.com/service-directory/docs/overview)

</details>

---

### Exam 3 · Q29

**You're managing an application employing an HTTP Cloud Function to process user activity from both desktop browser and mobile application clients. This function serves as the endpoint for all metric submissions using HTTP POST. However, due to legacy constraints, the function must be linked to a domain separate from the one requested by users on web or mobile sessions. The Cloud Function's domain is https://fn.example.com, while desktop and mobile clients use https://www.example.com. To restrict metric submissions solely to browser and mobile sessions, which response header should you include?**

- I. Add Access-Control-Allow-Origin: *
- IV. Add Access-Control-Allow-Origin: https://www.example.com
- II. Add Access-Control-Allow-Origin: https://*.example.com
- III. Add Access-Control-Allow-Origin: https://fn.example.com

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Add Access-Control-Allow-Origin: https://www.example.com

**IV. Add Access-Control-Allow-Origin:**[**https://www.example.com**](https://www.example.com/).

Here's the reasoning:

  * **CORS (Cross-Origin Resource Sharing):** CORS is a browser mechanism that controls whether JavaScript code running on one domain can send requests and receive responses from another domain.

  * **The 'Access-Control-Allow-Origin' header:** This header, sent by your Cloud Function, tells the browser which domains are explicitly allowed to make requests.

  * **Why**[**https://www.example.com**](https://www.example.com/)**:** Setting this header allows requests only from the 'www' subdomain of your main website, not arbitrary domains or the Cloud Function domain.

Why the other options are less suitable:

  * **I. Access-Control-Allow-Origin: *** :** This is too permissive, allowing any website to send requests to your Cloud Function, defeating the purpose of the restriction.

  * **II. Access-Control-Allow-Origin: https://*.example.com** :** This allows requests from any subdomain of 'example.com', which might be broader than you desire.

  * **III. Access-Control-Allow-Origin:**[**https://fn.example.com**](https://fn.example.com/):** This allows only requests from the function domain itself, preventing the intended user activity.

**Reference:**

[https://www.example.com and back-end service domain where cloud function runs is https://fn.example.comhttps://cloud.google.com/functions/docs/samples/functions-http-cors](https://www.example.com and back-end service domain where cloud function runs is https://fn.example.com  https://cloud.google.com/functions/docs/samples/functions-http-cors)

</details>

---

### Exam 3 · Q31

**As you develop a microservice-based application to operate on Google Kubernetes Engine (GKE), certain services require access to various Google Cloud APIs. How should you configure authentication for these services within the cluster, adhering to Google's recommended best practices? (Select two.)**

- II. Activate Workload Identity within the cluster via the gcloud command-line tool.
- V. Bind the Kubernetes service account and the Google service account using roles/iam.workloadIdentity with gcloud.
- I. Utilize the service account associated with the GKE node.
- IV. Centralize the storage of Google service account keys within a secret management service.
- III. Retrieve the Google service account keys from a secret management service.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Activate Workload Identity within the cluster via the gcloud command-line tool. **|** V. Bind the Kubernetes service account and the Google service account using roles/iam.workloadIdentity with gcloud.

**The two most suitable approaches are:**

  * **II. Activate Workload Identity within the cluster via the gcloud command-line tool.**

  * **V. Bind the Kubernetes service account and the Google service account using roles/iam.workloadIdentity with gcloud.**

**Explanation:**

  * **Workload Identity:** This is the preferred method for authentication in GKE. It eliminates the need to manage service account keys directly within your pods. Instead, Kubernetes service accounts are securely mapped to Google service accounts, simplifying permissions management.

  * **IAM Binding:** The `roles/iam.workloadIdentity` binding is the mechanism that associates the Kubernetes and Google service accounts, enabling your pods to use the correct Google Cloud permissions.

**Why Other Options Aren't as Suitable**

  * **I. GKE Node Service Account:** While technically possible, this is strongly discouraged. It grants broad permissions to all pods on a node, violating the principle of least privilege.

  * **III & IV. Service Account Key Management:** Managing keys directly creates overhead. Keys can be revoked, rotated, and potentially leaked. Workload Identity eliminates these concerns.

**References:**

[https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity  https://cloud.google.com/kubernetes-engine/docs/tutorials/authenticating-to-cloud-platform#use_workload_identity  https://cloud.google.com/kubernetes-engine/docs/how-to/kubernetes-service-accounts)

[https://cloud.google.com/kubernetes-engine/docs/tutorials/authenticating-to-cloud-platform#use_workload_identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity  https://cloud.google.com/kubernetes-engine/docs/tutorials/authenticating-to-cloud-platform#use_workload_identity  https://cloud.google.com/kubernetes-engine/docs/how-to/kubernetes-service-accounts)

[https://cloud.google.com/kubernetes-engine/docs/how-to/kubernetes-service-accounts](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity  https://cloud.google.com/kubernetes-engine/docs/tutorials/authenticating-to-cloud-platform#use_workload_identity  https://cloud.google.com/kubernetes-engine/docs/how-to/kubernetes-service-accounts)

</details>

---

### Exam 3 · Q32

**You manage an application utilizing the Cloud Storage API. Upon reviewing the logs, you notice several HTTP 503 Service Unavailable errors from the API. Your application logs these errors but does not take any immediate action. To enhance success rates, you want to implement Google-recommended retry logic. Which approach should you take?**

- III. Retry each failed operation at increasing time intervals, up to a maximum number of tries.
- II. Retry each failed operation at consistent time intervals, up to a maximum number of attempts.
- I. Retry failed operations in batches after a defined number of failures have been logged.
- IV. Retry each failed operation at decreasing time intervals, up to a maximum number of tries.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Retry each failed operation at increasing time intervals, up to a maximum number of tries.

**III. Retry each failed operation at increasing time intervals, up to a maximum number of attempts.**

This is generally known as exponential backoff. Here's why it's the recommended approach:

  * **Resolve Transient Errors:** HTTP 503 errors often signal temporary issues like resource contention or throttling. Exponential backoff gives the system time to recover, increasing the likelihood of success on subsequent retries.

  * **Avoid Overloading:** Increasing intervals between retries prevent your application from hammering the service further when it's already experiencing issues.

  * **Google Best Practices:** Exponential backoff is a standard retry mechanism recommended by Google, particularly for transient errors like 503.

**Why other options are less ideal**

  * **I. Retrying in Batches:** While batching retries could be useful in certain scenarios, it doesn't guarantee immediate retries for individual failures and might delay error resolution.

  * **II. Consistent Intervals:** This could still overload the system if it's under strain. Increasing intervals are generally more considerate.

  * **IV. Decreasing Intervals:** This goes against the principle of backing off and risks worsening the situation for the overwhelmed service.

**Reference:**  
[https://cloud.google.com/storage/docs/retry-strategy#exponential-backoff](https://cloud.google.com/storage/docs/retry-strategy#exponential-backoff  https://cloud.google.com/storage/docs/retry-strategy)

[https://cloud.google.com/storage/docs/retry-strategy](https://cloud.google.com/storage/docs/retry-strategy#exponential-backoff  https://cloud.google.com/storage/docs/retry-strategy)

</details>

---

### Exam 3 · Q41

**Your analytics system executes queries against a BigQuery dataset. The SQL query is run in batch mode, where the contents of a SQL file are passed to the BigQuery CLI. Subsequently, the output of the BigQuery CLI is redirected to another process. However, a permission error occurs when executing the queries.**

**You aim to resolve this issue. What action should you take?**

- IV. Create a new dataset in BigQuery, copy the source table to the new dataset, and then query the new dataset and table from the CLI.
- I. Grant the service account the BigQuery Data Viewer and BigQuery Job User roles.
- II. Grant the service account the BigQuery Data Editor and BigQuery Data Viewer roles.
- III. Create a view in BigQuery based on the SQL query, then query the view using the CLI.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Grant the service account the BigQuery Data Viewer and BigQuery Job User roles.

**To resolve the permission error when executing queries using the BigQuery CLI, the most appropriate action would be:**

**I. Grant the service account the BigQuery Data Viewer and BigQuery Job User roles.**

**Explanation:**

**I. Grant the service account the BigQuery Data Viewer and BigQuery Job User roles:**

  * **The BigQuery Data Viewer role grants read access to datasets and tables within BigQuery, allowing the service account to view the data needed for the queries.**

  * **The BigQuery Job User role allows the service account to create and manage jobs (such as query jobs) within BigQuery. This role is necessary for executing queries using the BigQuery CLI.**

II. Grant the service account the BigQuery Data Editor and BigQuery Data Viewer roles:

  * The BigQuery Data Editor role grants read and write access to datasets and tables within BigQuery, which might be more permissions than necessary and could potentially lead to unintended modifications to the data.

  * While the BigQuery Data Viewer role is appropriate for granting read access to datasets and tables, the Data Editor role is not necessary and could introduce unnecessary risks.

III. Create a view in BigQuery based on the SQL query, then query the view using the CLI:

  * While creating a view could be a workaround, it might not address the underlying permission issue. Additionally, it adds complexity to the solution without directly addressing the problem.

IV. Create a new dataset in BigQuery, copy the source table to the new dataset, and then query the new dataset and table from the CLI:

  * This approach involves unnecessary duplication of data and resources, which is not optimal for resolving a permission error.

**Therefore, option I, granting the service account the BigQuery Data Viewer and BigQuery Job User roles, is the most appropriate action to resolve the permission error when executing queries using the BigQuery CLI.**

**Reference:**

<https://cloud.google.com/bigquery/docs/access-control#bigquery>

</details>

---

### Exam 3 · Q43

**You're tasked with transferring an internal file upload API, which enforces a 500-MB file size limit, to App Engine. What's the optimal approach?**

- III. Implement signed URLs for file uploads.
- II. Use CPanel for file uploads.
- I. Utilize FTP for uploading files.
- IV. Modify the API to function as a multipart file upload API.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Modify the API to function as a multipart file upload API.

**The optimal approach for transferring an internal file upload API to App Engine with a 500-MB file size limit would be:**

**IV. Modify the API to function as a multipart file upload API.**

Explanation:

I. Utilize FTP for uploading files.

  * Using FTP (File Transfer Protocol) for uploading files might not be the best option for App Engine as it is a platform-as-a-service (PaaS) offering by Google Cloud Platform, and direct FTP access is not typically supported. Additionally, managing file uploads through FTP might introduce complexities in terms of security, scalability, and integration with the App Engine environment.

II. Use CPanel for file uploads.

  * CPanel is a web hosting control panel that allows users to manage their website and server settings. While it provides file management capabilities, it's not directly applicable to App Engine, which is a managed platform for building and deploying applications. CPanel is more suitable for traditional web hosting environments rather than cloud platforms like App Engine.

III. Implement signed URLs for file uploads.

  * Signed URLs can be useful for providing temporary, secure access to resources stored in cloud storage services like Google Cloud Storage. However, App Engine itself is capable of handling file uploads, and implementing signed URLs might add unnecessary complexity to the solution. Additionally, signed URLs don't inherently address the multipart file upload requirement.

**IV. Modify the API to function as a multipart file upload API.**

  * **This option is the most appropriate as it involves adapting the existing API to support multipart file uploads, which is a common approach for handling large file uploads in web applications. By modifying the API to support multipart file uploads, you can ensure compatibility with the App Engine environment and adhere to the specified file size limit. This approach allows you to leverage the capabilities of App Engine for handling file uploads while ensuring efficient and scalable processing of large files.**

**Therefore, option IV is the optimal approach for transferring the internal file upload API to App Engine with a 500-MB file size limit.**

</details>

---

### Exam 3 · Q45

**In the development of your web application, which access configuration should you implement for controlling access to private images and videos stored in a Cloud Storage bucket, considering that your users are anonymous and don't have Google Accounts?**

- III. Set up Identity-Aware Proxy (IAP) for user authentication within the web application. Grant users access to the bucket post-authentication via IAP.
- IV. Generate a signed URL providing read access to the bucket. Users can access the URL following authentication through your web application.
- I. Cache each web application user's IP address and establish a named IP table using Google Cloud Armor. Then, create a Google Cloud Armor security policy permitting user access to the backend bucket.
- II. Assign the Storage Object Viewer IAM role to allUsers. Users can access the bucket upon authentication through your web application.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Generate a signed URL providing read access to the bucket. Users can access the URL following authentication through your web application.

Here's why the best option is still 

**IV. Generate a signed URL providing read access to the bucket. Users can access the URL following authentication through your web application.**

Let's reiterate the reasoning and address some potential concerns :

**Why Signed URLs are Ideal:**

  * **Granular Control:** You maintain complete control over access duration and expiration of the signed URLs, ensuring a short-lived authorization mechanism.

  * **Authentication Tie-in** You integrate the signed URL generation with your application's authentication logic, ensuring that only authenticated users receive access.

  * **Anonymity Compliant:** Signed URLs don't require Google Accounts, making them perfect for anonymous users.

**Limitations and Mitigations:**

  * **Overly Broad Permissions:** If your bucket contains other sensitive objects, you'll need additional logic to prevent signed URLs from granting access to them. Carefully structure your bucket and possibly use separate buckets to isolate private resources.

  * **URL Exposure Risk:** If a signed URL leaks, temporary unauthorized access is possible. Minimize this risk by using short expiration periods for the signed URLs.

**Why Others are Less Suitable (Recap):**

  * **I. (IP-Based Access):** IP addresses are unreliable for individual user authorization as they are often shared or dynamic.

  * **II. (allUsers Permission):** Exposes your bucket to the entire internet, a serious security vulnerability.

  * **III. (IAP):** IAP primarily handles authentication, not fine-grained authorization for specific objects in a bucket.

**Reference** :

<https://cloud.google.com/storage/docs/access-control/signed-urls#should-you-use>

</details>

---

### Exam 3 · Q47

**Your company is developing an application that uploads reports to a Cloud Storage bucket. Upon uploading a report, you aim to trigger the publication of a message to a Cloud Pub/Sub topic. You want a solution that requires minimal implementation effort. What should you do?**

- IV. Deploy an application on a Google Kubernetes Engine cluster to handle the uploaded files and publish messages to the Cloud Pub/Sub topic upon receipt.
- I. Configure the Cloud Storage bucket to activate Cloud Pub/Sub notifications when objects are modified.
- II. Develop an App Engine application to receive the uploaded files and then publish messages to the Cloud Pub/Sub topic.
- III. Create a Cloud Function triggered by changes in the Cloud Storage bucket, responsible for publishing messages to the Cloud Pub/Sub topic.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Configure the Cloud Storage bucket to activate Cloud Pub/Sub notifications when objects are modified.

**I. Configure the Cloud Storage bucket to activate Cloud Pub/Sub notifications when objects are modified.**

Here's why this stands out:

  * **Built-in Integration:** Cloud Storage has native integration with Cloud Pub/Sub. You can configure notifications directly, without writing custom code.

  * **Serverless and Scalable:** The notification mechanism is managed by Google, handling scaling and reliability concerns for you.

  * **Focus on Core Logic:** This approach eliminates the need to develop and deploy code solely for reacting to Cloud Storage events.

**Why Other Options Require More Effort:**

  * **II. Develop an App Engine application ...** This involves developing application code, handling deployments, and potentially scaling logic for the App Engine app.

  * **III. Create a Cloud Function ...** While less overhead than a full App Engine app, you still need to write the Cloud Function and manage its deployment.

  * **IV. Deploy an application on a Google Kubernetes Engine cluster ...** Kubernetes offers flexibility, but introduces the highest complexity for this simple use case

**References:**

[https://cloud.google.com/storage/docs/pubsub-notifications#overview](https://cloud.google.com/storage/docs/pubsub-notifications#overview  https://cloud.google.com/storage/docs/pubsub-notifications#other_notification_options  https://cloud.google.com/storage/docs/pubsub-notifications)

[https://cloud.google.com/storage/docs/pubsub-notifications#other_notification_options](https://cloud.google.com/storage/docs/pubsub-notifications#overview  https://cloud.google.com/storage/docs/pubsub-notifications#other_notification_options  https://cloud.google.com/storage/docs/pubsub-notifications)

[https://cloud.google.com/storage/docs/pubsub-notifications](https://cloud.google.com/storage/docs/pubsub-notifications#overview  https://cloud.google.com/storage/docs/pubsub-notifications#other_notification_options  https://cloud.google.com/storage/docs/pubsub-notifications)

</details>

---

### Exam 3 · Q56

**While developing an application requiring user-specific subdirectories in Cloud Storage to store files, what action should be taken to ensure the creation of an empty subdirectory when a new user is added?**

- II. Establish an object with the subdirectory name and promptly delete it to create an empty subdirectory structure.
- IV. Produce an object with the subdirectory name, ensuring it has a zero-byte size, and set the Content-Type metadata to CLOUDSTORAGE_FOLDER.
- I. Generate an object with the subdirectory name, appending a trailing slash ('/') to denote an empty directory.
- III. Create an object with the subdirectory name, ensuring it has a zero-byte size and WRITER access control list permission.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Generate an object with the subdirectory name, appending a trailing slash ('/') to denote an empty directory.

**I. Generate an object with the subdirectory name, appending a trailing slash ('/') to denote an empty directory.**

Here's why this approach excels:

  * **Cloud Storage Conventions:** Cloud Storage recognizes objects ending in a trailing slash as representing folders (subdirectories). This behavior is widely understood and aligns with common file system concepts.

  * **Simplicity and Efficiency:** Creating a zero-byte object with a trailing slash is straightforward and efficient. There's no need for additional metadata management.

  * **Tool Compatibility:** Most tools and libraries that work with Cloud Storage will recognize and handle these objects as folders, ensuring seamless integration.

**Why other options are less suitable:**

  * **II. Create and Delete:** This method is unnecessarily convoluted; it introduces an additional step (deletion) without any benefits.

  * **III. WRITER ACL:** While setting WRITER permission is important for security, it doesn't directly address folder creation.

  * **IV. Content-Type Metadata:** Cloud Storage infers folders from the trailing slash, so setting specific Content-Type metadata is redundant.

**Reference:**

<https://cloud.google.com/storage/docs/folders>

</details>

---

### Exam 3 · Q57

**As the lead developer overseeing a new retail system operating on Cloud Run and Firestore in Datastore mode, you've successfully implemented the functionality to display a list of available products on the web UI. However, you've encountered HTTP 500 errors during peak usage times, indicating Cloud Run instances exceeding memory limits, coinciding with spikes in Datastore entity reads. To optimize system performance and prevent crashes, what action should you take?**

- II. Refine the query retrieving the product list by applying limits.
- I. Adjust the query retrieving the product list by employing integer offsets.
- IV. Refine the query retrieving the product list by implementing cursors.
- III. Adjust the Cloud Run configuration to raise memory limits.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Refine the query retrieving the product list by implementing cursors.

**Correct Option:** **IV. Refine the query retrieving the product list by implementing cursors.**

**Explanation:**

  * **Cursors for Pagination:** Cursors are essential for efficiently managing large result sets in Firestore. They allow you to break down the retrieval of the product list into smaller, more manageable chunks, preventing memory overload in Cloud Run instances.

**Why other options are less ideal:**

  * **I. Integer Offsets:** While offsets can be used for pagination, they become less efficient as the dataset grows. Firestore needs to skip over the specified number of results each time, leading to increased latency and read costs.

  * **II. Limits:** Simply limiting the results per query helps, but if you have many products, users may need multiple requests to see everything. This leads to a less seamless user experience.

  * **III. Increasing Memory Limits:** This is a temporary fix that masks the underlying problem. It doesn't address inefficient data retrieval and will likely lead to higher costs.

**Reference:**

<https://cloud.google.com/datastore/docs/concepts/queries#cursors_limits_and_offsets>

</details>

---

### Exam 4 · Q1

**You’re developing an integration for an ecommerce website to manage all steps in order fulfillment. You’ve created several Cloud Functions for each step in the order process and need to orchestrate their execution so that each function’s output guides the workflow. To minimize latency, what should you do?**

- C. Use Cloud Composer to call the functions and apply an Apache Airflow HTTP operator to manage execution logic.
- B. Use Workflows to call the functions and apply conditional jumps to manage execution logic.
- A. Use Workflows to call the functions and implement callbacks to manage execution logic.
- D. Use Cloud Composer to call the functions and apply an Apache Airflow operator to manage execution logic.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use Workflows to call the functions and apply conditional jumps to manage execution logic.

**The correct answer is**

**B. Use Workflows to call the functions and apply conditional jumps to manage execution logic.**

Explanation:

**Google Cloud Workflows** is designed to orchestrate the execution of Cloud Functions and other Google Cloud services in a **low-latency, serverless environment**. Workflows allows you to create sequences and apply **conditional jumps** to control the logic based on the output of each Cloud Function. This minimizes latency, as Workflows is optimized for coordinating serverless functions with minimal overhead and is more lightweight than Cloud Composer for simple, step-by-step orchestration needs.

Key advantages of using Workflows:

  * **Conditional jumps** allow dynamic control of execution flow based on the response of each function, ensuring that the next function is only called if certain conditions are met.

  * **Low latency** orchestration designed for serverless applications makes it ideal for real-time order processing and fulfillment tasks.

Justifications for Incorrect Options:

  * **Option A: Use Workflows with callbacks**  
While Workflows can use callbacks, **conditional jumps** are more straightforward and directly suited for decision-based execution flows, avoiding the complexity of managing callbacks in a sequential workflow.

  * **Option C: Use Cloud Composer with an Apache Airflow HTTP operator**  
Cloud Composer (Apache Airflow) is a powerful tool for complex, long-running ETL workflows, but it introduces more latency and complexity than Workflows. It’s not as suitable for low-latency orchestration in a real-time serverless environment like order fulfillment.

  * **Option D: Use Cloud Composer with an Apache Airflow operator**  
Similar to Option C, using Cloud Composer adds unnecessary latency for a serverless, low-latency workflow. Workflows is a better choice for orchestrating serverless functions efficiently.

**Relevant Documentation:**

For more on Google Cloud Workflows, refer to:

  * [Google Cloud Workflows Documentation](https://cloud.google.com/workflows/docs)

  * [Workflows Conditional Jumps](https://cloud.google.com/workflows/docs/samples/workflows-step-conditional-jump)

</details>

---

### Exam 4 · Q2

**You manage a popular mobile game deployed on Google Cloud using Firebase, Firestore, and Cloud Functions. Recently, the game experienced a spike in usage, resulting in HTTP 429 RESOURCE_EXHAUSTED errors when accessing the Firestore API. With an upcoming marketing campaign, another usage surge is expected. To prevent this issue from recurring, what should you do?**

- D. Optimize database queries to reduce read/write operations and update the code to retry Firestore API calls using exponential backoff.
- A. Request a quota increase and update the code to retry Firestore API calls using fixed backoff.
- B. Request a quota increase and update the code to retry Firestore API calls using exponential backoff.
- C. Optimize database queries to reduce read/write operations and update the code to retry Firestore API calls using fixed backoff.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Optimize database queries to reduce read/write operations and update the code to retry Firestore API calls using exponential backoff.

The correct answer is 

**D. Optimize database queries to reduce read/write operations and update the code to retry Firestore API calls using exponential backoff.**

Explanation:

The **RESOURCE_EXHAUSTED (HTTP 429)** error indicates that Firestore's quota or rate limits have been exceeded. To prevent this from happening again, it's essential to both **optimize database queries** and implement a **robust retry strategy** with **exponential backoff** :

  1. **Optimize Database Queries** : Reducing unnecessary read/write operations will help keep usage within limits, making the application more efficient and reducing the chance of hitting Firestore's quota limits.

  2. **Retry with Exponential Backoff** : Exponential backoff is the recommended retry strategy for handling temporary quota limits, as it prevents overwhelming the system by gradually increasing the delay between retries. This approach improves resilience by reducing the chances of immediate repeated requests that could exacerbate quota issues.

Justifications for Incorrect Options:

  * **Option A: Request a quota increase and use fixed backoff**  
While a quota increase may help, fixed backoff is not an optimal retry strategy for handling quota limits, as it can lead to repeated requests without adjusting to the system's capacity, increasing the likelihood of continued 429 errors.

  * **Option B: Request a quota increase and use exponential backoff**  
While exponential backoff is beneficial, simply increasing the quota without optimizing queries may not be enough to avoid quota issues during future spikes. Optimization is essential to efficiently manage resource use and reduce load on Firestore.

  * **Option C: Optimize database queries and use fixed backoff**  
Although optimizing queries is important, fixed backoff is not ideal for managing high-load scenarios, as it does not adapt as well as exponential backoff to fluctuating system loads.

**Relevant Documentation:**

For more on Firestore rate limits and best practices for managing resource usage, refer to:

  * [Firestore Quotas and Limits](https://cloud.google.com/firestore/quotas)

</details>

---

### Exam 4 · Q7

**As the overseer of a microservice-driven ecommerce platform on Google Cloud encountering HTTP 500 errors when triggering a Cloud Function responsible for sending confirmation emails, what adjustment should be made to minimize email loss?**

- I. Extend the Cloud Function's timeout to nine minutes.
- III. Modify the sender application to store emails in Memorystore and trigger the Cloud Function. Upon invocation, the function retrieves email details from Memorystore and dispatches them to the email service.
- II. Revise the sender application to dispatch outgoing emails as messages to a Pub/Sub topic. Update the Cloud Function configuration to consume the Pub/Sub queue.
- IV. Configure the sender application to implement Cloud Function execution retries every one second in case of request failures.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Revise the sender application to dispatch outgoing emails as messages to a Pub/Sub topic. Update the Cloud Function configuration to consume the Pub/Sub queue.

**The most suitable solution:**

**II. Revise the sender application to dispatch outgoing emails as messages to a Pub/Sub topic. Update the Cloud Function configuration to consume the Pub/Sub queue.**

**Explanation:**

  * **Reliability:** Pub/Sub introduces a durable message queue, ensuring emails aren't lost even if the Cloud Function temporarily fails.

  * **Decoupling:** Separates email generation from email sending, making the components more resilient to individual failures.

  * **Scalability:** Pub/Sub can handle bursts of emails without overwhelming the Cloud Function.

**Why Other Options Are Less Ideal:**

  * **I. Extend the Cloud Function's timeout to nine minutes.** While increasing the timeout might help in some cases, it doesn't fundamentally address potential issues with the email sending process itself. Long timeouts can also lead to higher costs.

  * **III. Modify the sender application to store emails in Memorystore and trigger the Cloud Function. Upon invocation, the function retrieves email details from Memorystore and dispatches them to the email service.** Memorystore is primarily for transient caching. It introduces an additional dependency and potential point of failure.

  * **IV. Configure the sender application to implement Cloud Function execution retries every one second in case of request failures.** Aggressive retries might overwhelm the system. They don't solve the root cause of the errors and don't provide the durability of Pub/Sub.

</details>

---

### Exam 4 · Q11

**You are building an application component to capture and stream user behavior data into BigQuery using the BigQuery Storage Write API. To prevent duplicate data in BigQuery, you need a straightforward solution. What should you do?**

- A. Use the default type to create a write stream.
- B. Use the committed type to create a write stream.
- D. Set up a Pub/Sub topic and use Cloud Functions to subscribe and remove duplicates.
- C. Set up a Kafka cluster and use a unique identifier (UUID) to filter out duplicate messages.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use the committed type to create a write stream.

The correct answer is **B. Use the committed type to create a write stream**.

Explanation:

Using the **committed** type to create a write stream with the **BigQuery Storage Write API** is the recommended approach to prevent duplicate data. The committed stream type ensures that data written to BigQuery is immediately visible to queries and that each write operation is atomic. The BigQuery Storage Write API handles duplicate checks internally, making it a straightforward solution to avoid duplicate entries without additional infrastructure or deduplication logic.

Justifications for Incorrect Options:

  * **Option A: Use the default type to create a write stream**  
The default stream type is **buffered** , which means data is not immediately visible and requires a flush operation to make it available in BigQuery. Buffered streams are more prone to duplicates because they don’t enforce atomic writes as the committed type does.

  * **Option C: Set up a Kafka cluster and use a unique identifier (UUID) to filter out duplicate messages**  
This would require additional infrastructure (Kafka) and a more complex deduplication setup, which is unnecessary given BigQuery’s built-in capabilities with the committed stream type.

  * **Option D: Set up a Pub/Sub topic and use Cloud Functions to subscribe and remove duplicates**  
Although this approach could manage deduplication, it would introduce additional latency and complexity. Using the committed type write stream is a simpler and more efficient solution for directly streaming data into BigQuery without duplicates.

**Relevant Documentation:**

For more details on the **BigQuery Storage Write API** and stream types, refer to:

  * [BigQuery Storage Write API Documentation](https://cloud.google.com/bigquery/docs/write-api-streaming)

  * [BigQuery Streaming Best Practices](https://cloud.google.com/bigquery/docs/write-api-best-practices)

</details>

---

### Exam 4 · Q13

**To facilitate updating the current stock price in an in-memory database for an application monitoring stock prices, how should you configure the Pub/Sub subscription, given each message includes the stock symbol, price, and timestamp?**

- IV. Establish a push subscription with both ordering and exactly-once delivery disabled.
- III. Configure a pull subscription with ordering enabled, utilizing the stock symbol as the ordering key.
- I. Set up a push subscription with exactly-once delivery enabled.
- II. Create a pull subscription with both ordering and exactly-once delivery disabled.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Configure a pull subscription with ordering enabled, utilizing the stock symbol as the ordering key.

**III. Configure a pull subscription with ordering enabled, utilizing the stock symbol as the ordering key.**

**Explanation:**

  * **Pull Subscriptions:** Provide better control over message consumption, beneficial when updating an in-memory database.

  * **Ordering:** Ensures stock price updates for the same symbol are processed sequentially, maintaining accuracy in your in-memory database.

  * **Stock Symbol as Ordering Key:** Guarantees that updates for a specific stock are applied in the correct order, preventing outdated values from overwriting newer ones.

**Why Other Options Are Less Suitable:**

  * **I. Set up a push subscription with exactly-once delivery enabled.** While push subscriptions can be useful, they relinquish control over message processing order, which might lead to inconsistencies in your in-memory database.

  * **II. Create a pull subscription with both ordering and exactly-once delivery disabled.** No ordering means you could update your in-memory database with older stock prices over newer ones.

  * **IV. Establish a push subscription with both ordering and exactly-once delivery disabled.** Combines the drawbacks of push subscriptions (lack of ordering control) with the potential for duplicate messages.

</details>

---

### Exam 4 · Q14

**As a manager of a system utilizing stateless Compute Engine VMs and Cloud Run instances connected to a VPC with internal ingress settings, you encounter a 403 Permission Denied error when attempting to schedule tasks on Cloud Run. How should you resolve this issue?**

- II. Set up a cron job on the Compute Engine VMs to trigger Cloud Run based on the schedule.
- I. Assign the roles/run.developer IAM role to the service account.
- IV. Utilize Cloud Scheduler in conjunction with Pub/Sub to invoke Cloud Run.
- III. Modify the Cloud Run ingress setting to 'Internal and Cloud Load Balancing.'

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Utilize Cloud Scheduler in conjunction with Pub/Sub to invoke Cloud Run.

**The most likely solution is:**

**IV. Utilize Cloud Scheduler in conjunction with Pub/Sub to invoke Cloud Run.**

**Explanation:**

  * **Cloud Scheduler:** Designed specifically for scheduling tasks on Google Cloud. It has the necessary permissions to work with Cloud Run.

  * **Pub/Sub:** A decoupling mechanism between Cloud Scheduler and Cloud Run, ensuring the security of your internal ingress settings. Cloud Scheduler can publish a message to a Pub/Sub topic, which your Cloud Run service can subscribe to.

**Why Other Options Might Not Be the Best Fit:**

  * **I. Assign the roles/run.developer IAM role to the service account.** Giving the `roles/run.developer` role to an external service account might loosen security too much for an internally facing Cloud Run instance.

  * **II. Set up a cron job on the Compute Engine VMs to trigger Cloud Run based on the schedule.** While possible, it introduces more management overhead and potential points of failure compared to dedicated services like Cloud Scheduler.

  * **III. Modify the Cloud Run ingress setting to 'Internal and Cloud Load Balancing.'** This would expose your Cloud Run instance, breaking your internal ingress requirement.

</details>

---

### Exam 4 · Q16

**You're developing a new application and require it to trigger only upon updates to a specific file in your Cloud Storage bucket. Your trigger specifications may vary, necessitating a process that accommodates different trigger types. Additionally, you aim for a straightforward configuration to enable multiple team members to update triggers in the future. What is the recommended approach?**

- II. Establish an Eventarc trigger to monitor your Cloud Storage bucket for a designated filename, with the target set as Cloud Run.
- III. Configure a Cloud Function designed to execute your application, triggered by object updates in Cloud Storage.
- IV. Configure a Firebase function to execute your application, triggered by object updates in Cloud Storage.
- I. Configure Cloud Storage events to dispatch to Pub/Sub, leveraging Pub/Sub events to initiate a Cloud Build job executing your application.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Establish an Eventarc trigger to monitor your Cloud Storage bucket for a designated filename, with the target set as Cloud Run.

The **recommended approach is:**

✅ **II. Establish an Eventarc trigger to monitor your Cloud Storage bucket for a designated filename, with the target set as Cloud Run.**

✅ **Explanation for Correct Option:**

**II. Eventarc + Cloud Run (✅ Recommended)**

  * **Eventarc** allows you to configure triggers for **specific Cloud Storage events** , such as `google.cloud.storage.object.v1.finalized` or `metadataUpdated`, and you can **filter by object name** (i.e., specific file).

  * Eventarc supports **advanced filtering** , **multiple trigger types** , and **targeting services like Cloud Run** , which is suitable for modern, scalable apps.

  * It enables **simple YAML-based configuration** , so multiple team members can manage/update triggers easily.

  * This is the **most flexible** , **scalable** , and **modern** approach recommended by Google Cloud.

**Official Documentation:**

  * <https://cloud.google.com/eventarc/docs>

  * <https://cloud.google.com/run/docs/tutorials/eventarc>

❌ **Explanation for Incorrect Options:**

**I. Cloud Storage → Pub/Sub → Cloud Build**

  * **Pub/Sub only supports event types like**`**OBJECT_FINALIZE**`**, not specific filename filtering**.

  * Involving **Cloud Build** to execute your app is **not ideal** , as Cloud Build is primarily for **CI/CD** , not app runtime execution.

  * **More complex** , and managing filters in Pub/Sub is harder and less maintainable.

**Docs:**  
<https://cloud.google.com/storage/docs/pubsub-notifications>  
<https://cloud.google.com/build/docs/automating-builds/create-pubsub-triggers>

**III. Cloud Function triggered by Cloud Storage**

  * Cloud Functions can be triggered by Cloud Storage events, but they **don’t support advanced filtering** , such as matching **specific filenames** directly.

  * Also, if your app grows in complexity, Cloud Run offers better scalability and control compared to Cloud Functions.

  * Not as configurable or scalable as Eventarc + Cloud Run.

**Docs:**  
<https://cloud.google.com/functions/docs/calling/storage>

**IV. Firebase Functions with Cloud Storage**

  * **Firebase Functions** are typically used in conjunction with **Firebase Storage** , not general-purpose **Cloud Storage** buckets.

  * This option is **not recommended** for enterprise or team workflows unless the application is Firebase-based.

**Docs:**  
<https://firebase.google.com/docs/functions/gcp-storage-events>

</details>

---

### Exam 4 · Q17

**What approach should your company adopt to enable data analysts to analyze events using SQL on a near real-time basis, while also accommodating rapid growth and leveraging managed services?**

- I. Create a Pub/Sub topic and a subscription. Stream events from the source into the Pub/Sub topic. Utilize Dataflow to ingest these events into BigQuery.
- IV. Deploy a Kafka instance on a large Compute Engine instance. Stream events from the source into a Kafka pipeline. Leverage Dataflow to ingest these events into Cloud Storage.
- III. Create a Pub/Sub topic and a subscription. Stream events from the source into the Pub/Sub topic. Utilize Dataflow to ingest these events into Firestore in Datastore mode.
- II. Create a Pub/Sub topic and a subscription. Stream events from the source into the Pub/Sub topic. Utilize Dataflow to ingest these events into Cloud Storage.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Create a Pub/Sub topic and a subscription. Stream events from the source into the Pub/Sub topic. Utilize Dataflow to ingest these events into BigQuery.

The best approach here is 

**I. Create a Pub/Sub topic and a subscription. Stream events from the source into the Pub/Sub topic. Utilize Dataflow to ingest these events into BigQuery.**

Here's why this combination is optimal for your requirements:

  * **Near Real-Time Processing:** Pub/Sub's asynchronous messaging enables low-latency event streaming, ensuring near-real-time data availability for analysis.

  * **Scalability with Managed Services:** Pub/Sub and Dataflow are fully managed services on GCP, meaning they automatically handle the scaling and infrastructure needs to accommodate rapid growth.

  * **SQL Analysis and Big Data:** BigQuery excels at managing vast datasets and provides a familiar SQL interface for analysts to work with.

  * **Dataflow's Power:** Dataflow handles complex data transformations and the reliable streaming of data into BigQuery.

**Why other options are less ideal:**

  * **II. Create a Pub/Sub topic and a subscription. Stream events from the source into the Pub/Sub topic. Utilize Dataflow to ingest these events into Cloud Storage.** Cloud Storage is for object storage, not structured analysis. Additional processing would be required to query data from Cloud Storage effectively.

  * **III. Create a Pub/Sub topic and a subscription. Stream events from the source into the Pub/Sub topic. Utilize Dataflow to ingest these events into Firestore in Datastore mode.** Firestore in Datastore mode is optimized for real-time applications, not large-scale analytics suitable for SQL querying.

  * **IV. Deploy a Kafka instance on a large Compute Engine instance. Stream events from the source into a Kafka pipeline. Leverage Dataflow to ingest these events into Cloud Storage.** This introduces overhead and complexity of manually managing a Kafka instance compared to the fully managed Pub/Sub.

**Relevant Documentation**

  * **Pub/Sub:** <https://cloud.google.com/pubsub>

  * **Dataflow:** <https://cloud.google.com/dataflow>

  * **BigQuery:** <https://cloud.google.com/bigquery>

</details>

---

### Exam 4 · Q20

**As you're developing a web application to function on a Google Cloud runtime, with the aim of allowing users to save files to their Drive without domain restrictions, how should you configure authentication for the Google Drive API?**

- I. Employ an OAuth Client ID along with delegated domain-wide authority.
- II. Utilize a service account empowered with delegated domain-wide authority.
- IV. Leverage a service account and request the https://www.googleapis.com/auth/drive.file scope to generate a signed JSON Web Token (JWT).
- III. Opt for an OAuth Client ID and request the https://www.googleapis.com/auth/drive.file scope to acquire an access token for each user.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Opt for an OAuth Client ID and request the https://www.googleapis.com/auth/drive.file scope to acquire an access token for each user.

Here's why **III is the most suitable approach with explanations on why the others fall short:**

**III. Opt for an OAuth Client ID and request the**[**https://www.googleapis.com/auth/drive.file**](https://www.googleapis.com/auth/drive.file)**scope to acquire an access token for each user.**

  * **User-Centric Access:** OAuth 2.0 is designed for granting applications access to a user's data on their behalf.

  * **Fine-Grained Permissions:** The `https://www.googleapis.com/auth/drive.file` scope allows you to control permissions to the level of individual files, which seems appropriate for your web application.

  * **Security:** Access tokens enable user-specific access and can be revoked as needed, enhancing security.

**Why other options aren't as ideal:**

  * **I. Employ an OAuth Client ID along with delegated domain-wide authority.**

    * **Excessive Permissions:** Domain-wide authority gives the app access to _all_ user data within the Google Workspace domain. This is rarely needed and poses a significant security risk if the application is compromised.

  * **II. Utilize a service account empowered with delegated domain-wide authority.**

    * **Identity Mismatch:** Service accounts are best for server-to-server interactions. With user-driven file uploads to Drive, OAuth 2.0 is more aligned.

  * **IV. Leverage a service account and request the**[**https://www.googleapis.com/auth/drive.file**](https://www.googleapis.com/auth/drive.file)**scope to generate a signed JSON Web Token (JWT).**

    * **Complexity:** JWTs with service accounts are generally used for when a separate application needs to act on a user's behalf, adding complexity without offering clear advantage in this scenario.

**Documentation:**

  * **OAuth 2.0 for Web Applications:** <https://developers.google.com/identity/protocols/oauth2/web-server>

  * **Google Drive API Scopes:** <https://developers.google.com/drive/api/v3/about-auth>

</details>

---

### Exam 4 · Q24

**In order to conduct near real-time analysis of audit activity logs captured in Cloud Logging, with multiple processes performing different types of analysis on the logging data, what approach should you adopt?**

- A. Develop an application to directly read the logs from the Cloud Logging API.
- B. Configure a Cloud Logging sink to Pub/Sub, and retrieve the logs from a Pub/Sub topic.
- C. Implement a Cloud Function endpoint to directly read from the Cloud Logging API and transfer the logs to Dataproc.
- D. Establish a Cloud Logging sink to Cloud Storage and retrieve the logs from a Cloud Storage bucket.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Configure a Cloud Logging sink to Pub/Sub, and retrieve the logs from a Pub/Sub topic.

The most appropriate approach to conduct near real-time analysis of audit activity logs captured in Cloud Logging, with multiple processes performing different types of analysis on the logging data, is:

**B. Configure a Cloud Logging sink to Pub/Sub, and retrieve the logs from a Pub/Sub topic.**

Explanation:

Option B involves configuring a Cloud Logging sink to export the logs to a Pub/Sub topic. This approach decouples the processing of logs from the logging infrastructure and allows multiple processes to subscribe to the Pub/Sub topic and perform different types of analysis on the logs in near real-time. Pub/Sub provides reliable message delivery and scales automatically to accommodate varying message throughput, making it suitable for handling large volumes of logs.

Option A suggests developing an application to directly read the logs from the Cloud Logging API. While this approach is feasible, it requires managing the infrastructure for log retrieval and may not be as scalable or fault-tolerant as using Pub/Sub.

Option C proposes implementing a Cloud Function endpoint to directly read from the Cloud Logging API and transfer the logs to Dataproc. While Cloud Functions can be used for log processing, transferring logs directly to Dataproc may introduce additional complexity and may not be the most efficient approach for real-time analysis.

Option D suggests establishing a Cloud Logging sink to Cloud Storage and retrieving the logs from a Cloud Storage bucket. While Cloud Storage can be used to store logs for archival purposes, retrieving logs from Cloud Storage may not provide the near real-time processing capabilities required for real-time analysis.

Therefore, option B is the most suitable approach for conducting near real-time analysis of audit activity logs captured in Cloud Logging with multiple processes performing different types of analysis.

**Documentation:**

  * Exporting Logs with Sinks: <https://cloud.google.com/logging/docs/export/configure_export#configuring-log-sinks>

</details>

---

### Exam 4 · Q26

**In the context of an application monitoring numerous stock prices, how should the Pub/Sub subscription be configured to manage a high volume of messages and update the current stock price in a single large in-memory database, considering each message includes the stock symbol, price, and timestamp?**

- IV. Establish a pull subscription with both ordering and exactly-once delivery disabled.
- II. Create a push subscription with both ordering and exactly-once delivery disabled.
- I. Set up a pull subscription with exactly-once delivery enabled.
- III. Configure a push subscription with exactly-once delivery enabled.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Configure a push subscription with exactly-once delivery enabled.

**Given the context of an application monitoring numerous stock prices and updating the current stock price in a single large in-memory database, considering each message includes the stock symbol, price, and timestamp, the most suitable configuration for the Pub/Sub subscription would be:**

**III. Configure a push subscription with exactly-once delivery enabled.**

Here's why:

  1. **Push Subscription** : Push subscriptions are generally preferred for high-volume message processing because they can handle a large number of incoming messages more efficiently than pull subscriptions. Push subscriptions allow Google Cloud Pub/Sub to push messages to the subscriber, reducing the need for the subscriber to continuously poll the Pub/Sub topic.

  2. **Exactly-once Delivery Enabled** : Ensuring exactly-once delivery helps prevent duplicate processing of messages, which is crucial for maintaining data consistency, especially in scenarios where updates to the stock prices need to be accurate and not duplicated. This ensures that each message is processed exactly once, avoiding potential issues with data integrity.

Option I is less suitable because pull subscriptions might not be as efficient for managing a high volume of messages, as they require the subscriber to actively pull messages from the Pub/Sub topic.

Option II is not ideal because push subscriptions are generally preferred for high-volume message processing, and disabling exactly-once delivery could lead to potential issues with data consistency.

Option IV might not be the most efficient choice for managing a high volume of messages, and disabling exactly-once delivery could lead to potential issues with data consistency.

**Therefore, option III, configuring a push subscription with exactly-once delivery enabled, is the most appropriate choice for efficiently managing a high volume of messages and ensuring data consistency in updating the current stock prices.**

</details>

---

### Exam 4 · Q27

**As part of an e-commerce company, you are designing a new Orders API to be hosted via Apigee. You created two environments in Apigee, orders-test and orders-prod, and plan to use unique URLs, test.lnk-42.com/api/v1/orders and lnk-42.com/api/v1/orders, for each environment. How can you ensure that each environment is only accessible via its designated URL?**

- D. 1. Attach orders-test to the test environment group and orders-prod to the production environment group.  
  2\. Add each hostname to the relevant environment group.
- A. 1. Attach orders-test and orders-prod to the orders environment group.  
  2\. Add each hostname to the respective environment.
- C. 1. Attach orders-test to the test environment group and orders-prod to the production environment group.  
  2\. Add each hostname to the appropriate environment.
- B. 1. Attach orders-test and orders-prod to the orders environment group.  
  2\. Add each hostname to the orders environment group.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. 1. Attach orders-test to the test environment group and orders-prod to the production environment group.  

The correct answer is **D.**

  1. **Attach**`**orders-test**`**to the test environment group and**`**orders-prod**`**to the production environment group.**

  2. **Add each hostname to the relevant environment group.**

Explanation:

In **Apigee** , environment groups allow you to manage hostnames and route traffic based on environments. To ensure that each environment (`orders-test` and `orders-prod`) is only accessible via its designated URL, you need to:

  1. **Attach**`**orders-test**`**to the test environment group** and `orders-prod` to the production environment group.** This setup isolates the environments by their groups, so test environments and production environments don’t overlap in URL accessibility.

  2. **Add each hostname to the relevant environment group** (e.g., `test.lnk-42.com` to the test environment group and `lnk-42.com` to the production environment group). By adding each hostname to its specific environment group, you ensure that each URL points only to the corresponding environment.

Justifications for Incorrect Options:

  * **Option A: Attach both**`**orders-test**`**and**`**orders-prod**`**to the orders environment group**  
Attaching both environments to a single environment group would make both URLs accessible within the same group, which would not isolate them as intended.

  * **Option B: Add each hostname to the**`**orders**`**environment group**  
Like Option A, using a single environment group does not separate access to test and production URLs, allowing possible cross-access between environments.

  * **Option C: Attach**`**orders-test**`**to the test environment group and**`**orders-prod**`**to the production environment group, then add each hostname to the appropriate environment**  
Adding hostnames directly to environments, instead of environment groups, will not configure host-based access control correctly, as hostname bindings must be set at the environment group level.

**Relevant Documentation:**

For more on Apigee environment groups and hostnames, refer to:

  * [Apigee Environment Groups](https://cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with)

</details>

---

### Exam 4 · Q32

**In the process of developing an application on Cloud Run that relies on REST API calls to interact with Google Cloud services, and considering the absence of support for Cloud Client Libraries in the selected programming language, the goal is to configure the associated service account to serve as the authorization identity for these calls. What is the recommended approach to achieve this?**

- I. Embed an API key within the application and transmit its value through the Authorization header.
- III. Utilize an API key associated with the service account by setting its value as the GOOGLE_APPLICATION_CREDENTIALS environment variable.
- II. Obtain the access token from the metadata server and transmit its value through the Authorization header.
- IV. During startup, fetch and store the access token using gcloud auth application-default print-access-token, saving it in a file whose path is specified in the GOOGLE_APPLICATION_CREDENTIALS environment variable.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Obtain the access token from the metadata server and transmit its value through the Authorization header.

A breakdown of why 

**II (obtain the access token from the metadata server) is the best approach** and why the others aren't as suitable:

**II. Obtain the access token from the metadata server and transmit its value through the Authorization header.**

  * **Security:** The metadata server provides a secure way to get short-lived access tokens, minimizing the risk of exposing long-term credentials.

  * **Cloud Run Integration:** Cloud Run automatically injects a service account into your container. Using the metadata server leverages this seamlessly.

  * **Ease of Use:** This method is the standard way to authorize Google Cloud API calls from within Cloud Run.

**Why other options aren't as ideal:**

  * **I. Embed an API key within the application and transmit its value through the Authorization header.**

    * **Security Risk:** Embedding keys directly in code is strongly discouraged. If code is compromised, the key is exposed.

    * **Management:** API keys typically have more limited scope compared to service accounts.

  * **III. Utilize an API key associated with the service account by setting its value as the GOOGLE_APPLICATION_CREDENTIALS environment variable.**

    * **Same Risks as I:** Embedding a key, even if it's an API Key associated with a service account, poses similar security risks.

  * **IV. During startup, fetch and store the access token using gcloud auth application-default print-access-token...**

    * **Unnecessary Complexity:** Requires external scripts running at startup and file management for storing the token.

    * **Token Expiration:** Access tokens expire; your application would need a mechanism to refresh the token. The metadata server handles all of this automatically.

**Documentation:**

  * **Cloud Run service account and the Metadata Server:** <https://cloud.google.com/compute/docs/metadata/overview>

  * **Obtaining Access Tokens on Cloud Run:** <https://cloud.google.com/run/docs/authenticating/service-to-service>

</details>

---

### Exam 4 · Q33

**To allow a Compute Engine instance without a public IP address to access the Cloud Storage API, what should you implement?**

- II. Implement VPC Network Peering.
- I. Utilize Carrier Peering.
- III. Deploy Shared VPC networks.
- IV. Enable Private Google Access.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Enable Private Google Access.

Here's the breakdown of why the correct answer is 

**IV – Enable Private Google Access** and why the other options aren't the best fit.

**IV. Enable Private Google Access**

  * **Purpose:** Private Google Access allows VMs in a subnet to access Google APIs and services using internal IP addresses, even if they don't have external IPs. This is the exact functionality needed in this scenario.

  * **How it Works:** It extends the internal IP address space of your VPC network to include Google's network. (<https://cloud.google.com/vpc/docs/configure-private-google-access>)

**Why other options aren't suitable:**

  * **I. Utilize Carrier Peering**

    * Carrier Peering facilitates direct network connections between your on-premises infrastructure and Google Cloud. It's unrelated to internal traffic within a VPC. (<https://cloud.google.com/network-connectivity/docs/carrier-peering>)

  * **II. Implement VPC Network Peering**

    * VPC Network Peering connects two VPC networks privately for resource sharing. It doesn't directly solve the issue of a VM without an external IP accessing Google APIs. (<https://cloud.google.com/vpc/docs/vpc-peering>)

  * **III. Deploy Shared VPC Networks**

    * Shared VPC enables centralized management of network resources across multiple projects. It doesn't inherently solve the issue of internal VMs reaching Google APIs without external IPs. (<https://cloud.google.com/vpc/docs/shared-vpc>)

</details>

---

### Exam 4 · Q35

**In deploying an application on a Google Kubernetes Engine (GKE) cluster, it needs to connect to a legacy REST service spread across two GKE clusters in different regions. The objective is to establish a resilient connection with minimal steps and enable probe-based health checks on the legacy service via a separate port. How should the connection be configured? (Select two options.)**

- V. Configure the legacy service's firewall to allow health checks initiated from the Traffic Director control plane.
- III. Configure the legacy service's firewall to allow health checks initiated from the sidecar proxy.
- II. Implement a proxyless Traffic Director configuration for the application.
- I. Utilize Traffic Director alongside a sidecar proxy to link the application to the service.
- IV. Configure the legacy service's firewall to allow health checks initiated from the application.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Configure the legacy service's firewall to allow health checks initiated from the sidecar proxy. **|** I. Utilize Traffic Director alongside a sidecar proxy to link the application to the service.

**To configure the connection between the application deployed on a Google Kubernetes Engine (GKE) cluster and the legacy REST service spread across two GKE clusters in different regions, while enabling probe-based health checks on the legacy service via a separate port, the following options would be suitable:**

**I. Utilize Traffic Director alongside a sidecar proxy to link the application to the service.**

  * **Traffic Director can help manage traffic between different services and clusters. Using a sidecar proxy alongside Traffic Director can facilitate connectivity and resilience between the application and the legacy service.**

**III. Configure the legacy service's firewall to allow health checks initiated from the sidecar proxy.**

  * **Since the health checks are initiated from the sidecar proxy, the firewall rules of the legacy service should allow these health checks to pass through.**

Explanation for excluding other options:

II. Implement a proxyless Traffic Director configuration for the application.

  * Proxyless Traffic Director configuration might not provide the necessary flexibility and control required for connecting to the legacy service, especially when dealing with health checks on a separate port.

IV. Configure the legacy service's firewall to allow health checks initiated from the application.

  * It's not typically recommended to directly initiate health checks from the application, as it may introduce complexities and potential issues with managing health checks separately from the networking infrastructure.

V. Configure the legacy service's firewall to allow health checks initiated from the Traffic Director control plane.

  * Health checks initiated from the Traffic Director control plane might not directly interact with the legacy service's firewall. The health checks are typically initiated from proxies or other agents deployed alongside the application, which then communicate with the legacy service. Therefore, configuring the firewall to allow health checks from the sidecar proxy (option III) is more appropriate.

</details>

---

### Exam 4 · Q39

**In your mobile web application where global users vote on popular topics, with a very high volume of votes expected during each 30-minute voting window for each topic, you need to capture and count votes within these intervals while also storing them for future analysis and reporting. How should you approach this?**

- I. Save the votes to Memorystore, then utilize Cloud Functions to insert the counts into BigQuery, and visualize the results in Google Data Studio.
- III. Publish the votes to Pub/Sub and use Cloud Functions to insert both the counts and votes into Cloud Storage, thereafter displaying the results in Google Data Studio.
- IV. Implement Firebase for user authentication, enabling the direct publication of votes to Firestore. Export the votes to a CSV file and import them into Sheets for reporting purposes.
- II. Publish the votes to Pub/Sub, and employ a Dataflow pipeline to insert both the counts and votes into BigQuery, subsequently visualizing the results in Google Data Studio.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Publish the votes to Pub/Sub, and employ a Dataflow pipeline to insert both the counts and votes into BigQuery, subsequently visualizing the results in Google Data Studio.

Given the high volume of votes expected during each voting window for each topic in your mobile web application, along with the need to capture, count, and store votes for future analysis and reporting, the most suitable approach would be:

**II. Publish the votes to Pub/Sub, and employ a Dataflow pipeline to insert both the counts and votes into BigQuery, subsequently visualizing the results in Google Data Studio.**

Explanation:

Option I suggests saving the votes to Memorystore and using Cloud Functions to insert counts into BigQuery. While this approach can work, using Memorystore might not be the most efficient solution for capturing and storing high volumes of votes, especially if real-time processing and analysis are required. Dataflow is better suited for processing large streams of data, making it a more appropriate choice.

Option III proposes publishing votes to Pub/Sub and using Cloud Functions to insert both counts and votes into Cloud Storage. While this approach could work, Cloud Storage is primarily used for object storage rather than structured data storage like BigQuery. Additionally, Cloud Functions might not be the best choice for handling high-volume data processing and insertion.

Option IV suggests using Firebase for user authentication and Firestore for storing votes. While Firebase and Firestore are suitable for real-time data synchronization and user authentication, exporting votes to a CSV file and importing them into Sheets for reporting purposes might not be the most efficient or scalable solution for large volumes of data.

Option II is the recommended approach because it leverages Pub/Sub for handling high-volume data streams, Dataflow for processing and transforming data in real-time, and BigQuery for storing and analyzing structured data. Visualizing the results in Google Data Studio allows for easy and customizable reporting and visualization.

Therefore, option II is the most appropriate approach for capturing, counting, and storing votes in your mobile web application while also facilitating future analysis and reporting.

**Documentation:**

  * Pub/Sub: <https://cloud.google.com/pubsub/docs/overview>

  * Dataflow: <https://cloud.google.com/dataflow/docs>

  * BigQuery: <https://cloud.google.com/bigquery/docs>

  * Google Data Studio: <https://datastudio.google.com/>

</details>

---

### Exam 4 · Q41

**What action should you take to ensure that consumers of your API endpoint are notified when a write request to Firestore in Datastore mode fails due to encountering an HTTP 5xx server error?**

- B. Return an HTTP 406 Not Acceptable response.
- A. Return an HTTP 204 No Content response.
- C. Return an HTTP 500 Internal Server Error response.
- D. Retry the Datastore API with exponential backoff until Firestore returns an HTTP 2xx response.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Return an HTTP 500 Internal Server Error response.

Here's why the best approach is a combination of 

**C. Return an HTTP 500 Internal Server Error response** and **D. Retry the Datastore API with exponential backoff until Firestore returns an HTTP 2xx response.**

**Explanation:**

  * **C. Return an HTTP 500 Internal Server Error response.** This clearly signals to API consumers that a server-side error has occurred, indicating the client request was likely valid, but the server failed to process it correctly.

  * **D. Retry the Datastore API with exponential backoff until Firestore returns an HTTP 2xx response.** Retries with exponential backoff (increasing wait times between attempts) help handle potential transient errors and improve the likelihood of successful writes. However, make sure to limit retries to prevent infinite loops.

**Why Other Options are Less Ideal:**

  * **A. Return an HTTP 204 No Content response.** A 204 response implies success, which would be misleading in this case, preventing API consumers from taking corrective actions.

  * **B. Return an HTTP 406 Not Acceptable response.** A 406 response typically indicates issues with content negotiation. It's not the most accurate representation of a server-side failure during a write request.

**Important Considerations:**

  * **Logging and Monitoring:** Implement robust logging and monitoring to help pinpoint the root cause of the 5xx errors, allowing you to address them proactively.

  * **Idempotency:** If possible, design API operations to be idempotent (producing the same result with multiple executions) to make retries safer.

  * **User Feedback:** If retry strategies fail after a reasonable number of attempts, provide informative error messages to the API user.

**Documentation:**

  * **HTTP Status Codes:** <https://developer.mozilla.org/en-US/docs/Web/HTTP/Status>

  * **Exponential Backoff:** <https://en.wikipedia.org/wiki/Exponential_backoff>

</details>

---

### Exam 4 · Q43

**Your company relies on a BigQuery data mart to furnish analytics insights to numerous employees. One user requires the ability to run jobs without impeding important workloads, showing no concern for job duration. Your goal is to fulfill this request while minimizing both company expenses and your own effort. What action should you take?**

- IV. Permit the user to execute jobs during periods when critical workloads are not active, ensuring minimal disruption while utilizing existing resources efficiently.
- II. Establish a separate project dedicated to the user, providing autonomy for job execution without impacting existing workloads.
- III. Grant the user the job.user role within the current project, enabling them to submit jobs without unnecessary administrative overhead.
- I. Instruct the user to execute the jobs as batch jobs, allowing for flexible scheduling and resource allocation.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Instruct the user to execute the jobs as batch jobs, allowing for flexible scheduling and resource allocation.

**Correct Option:**

  * **I. Instruct the user to execute the jobs as batch jobs, allowing for flexible scheduling and resource allocation.**

**Reasoning:**

  * **Cost-effective and Efficient:** Batch jobs in BigQuery are the ideal solution for this scenario. They are executed when resources are available, ensuring other workloads are not impacted. Batch jobs are also generally less expensive than on-demand queries.

  * **Minimal Overhead:** This option minimizes administrative effort, as batch jobs require no extra project setup or advanced permissions. It's a straightforward way to accommodate the user's needs.

**Incorrect Options and Why:**

  * **II. Establish a separate project dedicated to the user, providing autonomy for job execution without impacting existing workloads.**

    * While isolating the user's jobs would work, creating and managing a separate project introduces unnecessary complexity and overhead.

  * **III. Grant the user the job.user role within the current project, enabling them to submit jobs without unnecessary administrative overhead.**

    * The `job.user` role doesn't address the core problem of prioritizing workloads. Providing it won't guarantee that the user's jobs won't interfere with important tasks.

  * **IV. Permit the user to execute jobs during periods when critical workloads are not active, ensuring minimal disruption while utilizing existing resources efficiently.**

    * This requires continuous monitoring and manual timing, making it inconvenient and prone to error. It doesn't leverage BigQuery's built-in resource management capabilities.

**Supporting Documentation:**

  * **BigQuery Batch Queries:** <https://cloud.google.com/batch/docs/get-started>

  * **BigQuery Pricing** <https://cloud.google.com/bigquery/pricing>

</details>

---

### Exam 4 · Q44

**In order to minimize operational overhead while using Cloud Run to write every Pub/Sub message to both a Cloud Storage object and a BigQuery table, which architecture should you implement?**

- D. Two topics, 2 subscriptions, 2 Cloud Run services: Two independent Pub/Sub topics are used. Each topic has its own subscription, and a Cloud Run service listens to each subscription. This configuration allows for handling completely separate message streams with independent processing.
- A. One topic, 1 subscription, 2 Cloud Run services: A single Pub/Sub topic publishes messages to one subscription. Two separate Cloud Run services can be configured to listen on that subscription and process the messages.
- C. One topic, 1 Cloud Run service, 1 push subscription: One Pub/Sub topic with a single subscription. A Cloud Run service receives messages via a push subscription, meaning Pub/Sub actively delivers messages to the service. Data can be written to BigQuery and then Cloud Storage.
- B. One topic, 2 subscriptions, 2 Cloud Run services: Similar to A, but with two subscriptions. Each Cloud Run service listens to a different subscription, allowing for further message filtering or processing specialization.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. One topic, 2 subscriptions, 2 Cloud Run services: Similar to A, but with two subscriptions. Each Cloud Run service listens to a different subscription, allowing for further message filtering or processing specialization.

To minimize operational overhead while using Cloud Run to write every Pub/Sub message to both a Cloud Storage object and a BigQuery table, the most suitable architecture to implement is:

**B. One topic, 2 subscriptions, 2 Cloud Run services: Similar to A, but with two subscriptions. Each Cloud Run service listens to a different subscription, allowing for further message filtering or processing specialization.**

Explanation:

Option B involves setting up one Pub/Sub topic with two subscriptions. Each subscription can be configured to deliver messages to a separate Cloud Run service. This architecture allows for decoupling of message processing logic, enabling each Cloud Run service to handle a specific aspect of message processing (e.g., writing to Cloud Storage or BigQuery). It also provides flexibility for future enhancements or modifications to each processing pipeline independently.

Option A, while simpler, may result in a single Cloud Run service handling all message processing tasks, leading to potential scalability and maintenance challenges as the system grows.

Option C suggests using a single Cloud Run service with a push subscription, which may limit scalability and introduce complexity if the processing logic for writing to Cloud Storage and BigQuery needs to be separated or modified independently in the future.

Option D involves using two independent Pub/Sub topics, each with its own subscription and Cloud Run service. This option may introduce unnecessary complexity unless there are distinct message streams that require separate processing pipelines.

Therefore, option B is the most suitable architecture to minimize operational overhead while using Cloud Run to write every Pub/Sub message to both a Cloud Storage object and a BigQuery table.

**Documentation:**

  * Cloud Run: <https://cloud.google.com/run>

  * Pub/Sub: <https://cloud.google.com/pubsub>

</details>

---

### Exam 4 · Q50

**To effectively manage a significant surge in traffic and ensure efficient scalability during the redesign of the audit event ingestion from the authentication service, currently sharing a Compute Engine virtual machine with the audit service, you plan to separate them into their own pools of Compute Engine VM instances and utilize Pub/Sub for event transmission. How should you configure the Pub/Sub topics and subscriptions?**

- C. Implement a single Pub/Sub topic and create a push subscription.
- A. Establish a single Pub/Sub topic and set up a single pull subscription.
- B. Set up a single Pub/Sub topic and create a pull subscription for each instance of the audit service.
- E. Set up a Pub/Sub topic for each instance of the authentication service and create a push subscription for each topic.
- D. Create a Pub/Sub topic for each instance of the authentication service and set up a pull subscription for each topic.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Establish a single Pub/Sub topic and set up a single pull subscription.

**_A_ is correct. This is the most flexible way to scale, allowing the authentication and audit services to be sized independently according to load.**

B is incorrect. This will cause messages to be duplicated, one copy per subscription.  
C is incorrect. This will allow the system to scale, but push subscriptions are less suited to handle large volumes of messages.  
D is incorrect. This will allow the system to scale, however each audit service will listen to all subscriptions.  
E. is incorrect. This will allow the system to scale, however it will require each audit service to listen to all subscriptions. Also push subscriptions are less suited to handle large volumes of messages.

**Reference:**

[https://cloud.google.com/pubsub/docs/subscriber#push-subscription](%0d https:/cloud.google.com/pubsub/docs/subscriber#push-subscription)

</details>

---

### Exam 4 · Q56

**You're developing a web application on a Compute Engine instance that writes files to users' Google Drive accounts. To enable authentication with the Google Drive API, what should you do?**

- I. Implement an OAuth Client ID with the https://www.googleapis.com/auth/drive.file scope to acquire an access token for each user.
- II. Configure an OAuth Client ID with delegated domain-wide authority.
- IV. Employ the App Engine service account with delegated domain-wide authority.
- III. Utilize the App Engine service account along with the https://www.googleapis.com/auth/drive.file scope to generate a signed JSON Web Token (JWT).

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Implement an OAuth Client ID with the https://www.googleapis.com/auth/drive.file scope to acquire an access token for each user.

**Correct Option:**

  * **I. Implement an OAuth Client ID with the**[**https://www.googleapis.com/auth/drive.file**](https://www.googleapis.com/auth/drive.file)**scope to acquire an access token for each user.**

**Reasoning:**

  * **User-Centric Authorization:** OAuth 2.0 is the standard for allowing users to grant applications access to their data on other services. In this case, you need users to directly authorize your web application to access their Google Drive.

  * **Appropriate Scope:** The `https://www.googleapis.com/auth/drive.file` scope grants the necessary permission to write files to the user's Drive while limiting access to only the required actions.

**Incorrect Options and Why:**

  * **II. Configure an OAuth Client ID with delegated domain-wide authority.**

    * Domain-wide delegation is powerful and usually reserved for admin-like actions across an entire Google Workspace domain. It's not necessary for typical user-driven file writing.

  * **III. Utilize the App Engine service account along with the**[**https://www.googleapis.com/auth/drive.file**](https://www.googleapis.com/auth/drive.file)**scope to generate a signed JSON Web Token (JWT).**

    * While service accounts are useful for server-to-server communication, they don't offer the user-level authorization needed in this scenario.

  * **IV. Employ the App Engine service account with delegated domain-wide authority.**

    * Like option II, this grants excessive administrative-level access, which is unnecessary and poses security risks.

**Supporting Documentation:**

  * **OAuth 2.0 for Web Server Applications:** <https://developers.google.com/identity/protocols/oauth2/web-server>

  * **Google Drive API - Scopes:** <https://developers.google.com/drive/api/v3/about-auth>

</details>

---

### Exam 6 · Q3

**You are developing an external-facing application on GKE that provides a streaming API with two subscription tiers, “basic” and “premium.” Each tier limits the number of API requests allowed per client application per day. You want to design the application architecture to support these subscription tiers following Google-recommended practices. What approach should you take?**

- **A.**
    Set up the service on **GKE** as a backend to an **Apigee proxy**.
    Provide **API keys** to users to identify client applications.
    Configure a **Quota policy** in **Apigee** based on the subscription tier for each API key.
- **B.**
    Set up the service on **GKE** as a backend to an **Apigee proxy**.
    Provide **API keys** to users to identify client applications.
    Configure a **SpikeArrest policy** in **Apigee** for API keys based on the subscription tier.
- **C.**
    Configure the service on **GKE** as a backend to two separate projects, each with its own **Application Load Balancer**.
    Set up quotas for **“Queries per second (QPS) per region per network”** for each project individually.
    Assign users API endpoints based on their subscription tier.
- **D.**
    Deploy the application to two **GKE clusters** , one for each subscription tier, with separate **Ingress** configurations.
    Set up each cluster as a backend to an **Apigee proxy**.
    Provide **API keys** to users to identify client applications.
    Configure different rate limits based on the subscription tier.

<details><summary>Answer &amp; explanation</summary>

**Correct:** **A.**

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

</details>

---

### Exam 6 · Q7

**You are building a secure platform for sharing documents, where users can share files with others, including individuals outside their organization. To maintain security, access to shared documents must expire after a customizable period. These documents are stored in Cloud Storage.**

**How should you set up Cloud Storage to support this access expiration?**

- A. Use signed policy documents on the Cloud Storage bucket to control access.
- B. Configure access control lists (ACLs) on the Cloud Storage bucket to manage permissions.
- C. Generate a signed URL for each document that users want to share temporarily.
- D. Assign the Storage Object Viewer IAM role to all authenticated users to allow document access.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Generate a signed URL for each document that users want to share temporarily.

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

</details>

---

### Exam 6 · Q9

**Your infrastructure team manages Compute Engine VMs and uses the Google Cloud console and gcloud CLI to provision resources for the development environment. To meet compliance requirements, all Compute Engine VMs must have the correct labels. You need a solution that automatically corrects any missing labels without altering the current provisioning process. You want this solution to be highly scalable.**

**What should you do?**

- A. Set up a trigger in Cloud Audit Logs to activate a Cloud Function whenever a Compute Engine VM is created. The function should check for missing labels and add them if needed.
- B. Use Terraform to deploy resources and run the gcloud terraform vet command with a policy that ensures each Compute Engine VM provisioned by Terraform has the required labels.
- C. Create a script that periodically checks all Compute Engine VMs for missing labels using Cloud Scheduler. Have the script apply labels where they are missing.
- D. Manually review all Compute Engine VMs for missing labels on a regular basis and use the console to assign any necessary lab

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Set up a trigger in Cloud Audit Logs to activate a Cloud Function whenever a Compute Engine VM is created. The function should check for missing labels and add them if needed.

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

</details>

---

### Exam 6 · Q13

**You’re a developer for a local concert venue, and customers use your company’s website to purchase event tickets. You need to ensure customers receive immediate confirmation when they reserve a specific seat.**

**How should you structure the ticket reservation process?**

- A. Place the seat reservation request in a Cloud Tasks queue, which initiates a Workflow to handle the reservation processing.
- B. Publish the seat reservation to a Pub/Sub topic and configure the backend service to use Eventarc for processing the reservation on GKE.
- C. Store the seat reservation in a Cloud Storage bucket, triggering an event to a Cloud Run service that processes the order.
- D. Send the seat reservation as an HTTP POST request to an Application Load Balancer, which distributes it to a Compute Engine managed instance group that processes the reservation.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Publish the seat reservation to a Pub/Sub topic and configure the backend service to use Eventarc for processing the reservation on GKE.

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

</details>

---
