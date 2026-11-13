# Professional Cloud Developer — Practice Exam 2

60 questions.

## Question 1

*Domain 3: Configuring and Deploying Applications*

**You're strategizing the deployment of your application on Google Kubernetes Engine (GKE). Your application demands horizontal scalability, with each instance necessitating both a stable network identity and its persistent disk. Which GKE component aligns best with this requirement?**

- [ ] I. Deployment
- [ ] III. ReplicaSet
- [ ] IV. ReplicaController
- [x] II. StatefulSet

### Explanation

**II. StatefulSet**

Explanation:

  * **Stable Network Identities:** Each pod in a StatefulSet is assigned a unique and persistent hostname/DNS entry, allowing reliable communication within and outside the cluster.

  * **Persistent Disks:** StatefulSets are designed to work with persistent storage. Pods can be associated with individual PersistentVolumeClaims, ensuring data persists even if pods are rescheduled.

  * **Ordered Scaling:** StatefulSets scale pods in a sequential order (0, 1, 2...), which can be important for certain applications that rely on pod identity during initialization or coordination.

Why Other Options Are Less Ideal:

  * **I. Deployment:** Deployments manage stateless pods designed for horizontal scaling. They don't guarantee stable network identities or have built-in mechanisms for persistent storage association.

  * **III. ReplicaSet:** Similar to Deployments, ReplicaSets primarily manage stateless replicas and don't directly handle persistent storage or stable identifiers.

  * **IV. ReplicaController:** ReplicaControllers are an older version of ReplicaSets with less functionality and shouldn't be used in new deployments.

Ref:

<https://cloud.google.com/kubernetes-engine/docs/concepts/statefulset>

---

## Question 2

*Domain 2: Building and Testing Applications*

**How should you configure the load testing for a set of REST API endpoints deployed to Cloud Run, meeting Google-recommended best practices?**

- [ ] II. Employ an unmanaged instance group to deploy an image with cURL installed. Configure cURL within the image to execute a test plan, running one instance per VM to initiate load from multiple parallel threads and source IP addresses.
- [ ] IV. Download a container image of a distributed load testing framework on Cloud Shell. Sequentially launch multiple instances of the container on Cloud Shell to augment the load on the API.
- [ ] I. Utilize a managed instance group to deploy an image with cURL installed. Configure cURL within the image to execute a test plan, running one instance per VM to initiate load from multiple parallel threads and source IP addresses.
- [x] III. Implement a distributed load testing framework on a private Google Kubernetes Engine (GKE) cluster. Scale by deploying additional Pods as necessary to generate more traffic and support concurrent users.

### Explanation

Here's a breakdown of the options and why the best choice aligns with Google's recommended practices:

**Correct Option:**

  * **III. Implement a distributed load testing framework on a private Google Kubernetes Engine (GKE) cluster. Scale by deploying additional Pods as necessary to generate more traffic and support concurrent users.**

**Justification:**

  * **Scalability:** GKE is inherently designed for scalability, especially for load testing purposes. Adding pods dynamically allows you to simulate realistic user loads, including spikes.

  * **Distributed Testing:** Load testing frameworks are best leveraged in a distributed manner, ensuring that the load generated mimics real-world scenarios with traffic originating from diverse sources. GKE's flexibility facilitates this.

  * **Manageability:** GKE provides managed infrastructure, simplifying cluster configuration and maintenance, allowing you to focus on your test plans.

  * **Google Best Practices:** Aligns with Google's advice to use tools like JMeter in a distributed setup for thorough Cloud Run load testing.

**Why Other Options Are Not Ideal:**

  * **I. Utilizing a managed instance group to deploy an image with cURL installed...**

    * **Inefficient Scaling:** Managed instance groups are not as easily scalable as GKE for quick load ramp-up and ramp-down.

    * **Limited Distribution:** Load generated will originate from similar IP addresses, unlike real user scenarios.

  * **II. Employ an unmanaged instance group to deploy an image with cURL installed...**

    * **Even less scalable than option I** and has the same distribution issue.

    * **Management Overhead:** Unmanaged instance groups require more effort for configuration and maintenance.

  * **IV. Download a container image of a distributed load testing framework on Cloud Shell...**

    * **Resource Constraints:** Cloud Shell instances have limited resources for extensive load testing.

    * **Sequential Launch:** Launching containers sequentially doesn't reflect realistic traffic patterns.

**References:**

[https://cloud.google.com/architecture/distributed-load-testing-using-gke#build_the_](https://cloud.google.com/architecture/distributed-load-testing-using-gke#build_the_c)[container_image](https://cloud.google.com/architecture/distributed-load-testing-using-gke#build_the_ccontainer_image)

---

## Question 3

*Domain 2: Building and Testing Applications*

**In the process of parsing a log file containing timestamp, account number (string), and transaction amount (number) columns, you aim to efficiently compute the sum of transaction amounts for each unique account number. Which data structure is best suited for this task?**

- [ ] IV. A comma-delimited string
- [ ] III. A two-dimensional array
- [ ] I. A linked list
- [x] II. A hash table

### Explanation

**II. A hash table**

  * **Efficient Lookups:** Hash tables offer near-constant time lookups based on keys (in this case, the account number). This is critical for quickly finding existing entries or adding new ones as you parse the log file.

  * **Natural Key-Value Fit:** The 'account number' (key) and its corresponding 'total transaction amount' (value) map perfectly to the key-value structure of a hash table.

**Why Other Options Are Less Ideal:**

  * **I. A linked list** Searching for the right account number in a linked list would be linear (O(n)), meaning it gets slower as the number of accounts grows.

  * **III. A two-dimensional array** While an array could work, it's less efficient than a hash table for lookups if the account numbers are not known beforehand or aren't sequential.

  * **IV. A comma-delimited string** Storing data this way would make calculations and lookups extremely inefficient. Strings are not ideal for structured data.

Reference:  
<https://open4tech.com/array-vs-linked-list-vs-hash-table/>

---

## Question 4

*Domain 3: Configuring and Deploying Applications*

**You've containerized a legacy application that relies on configuration stored on an NFS share. How can you ensure the application doesn't serve traffic until its configuration is retrieved when deploying it to Google Kubernetes Engine (GKE)?**

- [ ] IV. Introduce a startup script to the GKE instance group to mount the NFS share during node startup, transferring the configuration files into the container, and activate the service via an ENTRYPOINT script.
- [x] II. Establish a PersistentVolumeClaim (PVC) on the GKE cluster, accessing configuration files from the volume, and commence the service via an ENTRYPOINT script.
- [ ] I. Utilize the gsutil utility within the Docker container at startup, copying files, and initiate the service via an ENTRYPOINT script.
- [ ] III. Incorporate the COPY statement in the Dockerfile to inject the configuration into the container image, validating its availability, and launch the service using an ENTRYPOINT script.

### Explanation

**II. Establish a PersistentVolumeClaim (PVC) on the GKE cluster, accessing configuration files from the volume, and commence the service via an ENTRYPOINT script.**

Here's why this stands out as the ideal choice:

  * **Kubernetes Native:** Using PersistentVolumeClaims (PVCs) integrates seamlessly with Kubernetes, providing a standard way to manage persistent storage for Pods.

  * **Configuration Decoupling:** Separating the configuration from the container image enhances flexibility and maintainability, avoiding re-building images for configuration changes.

  * **Availability Check:** Your ENTRYPOINT script can include logic to verify the configuration is accessible from the mounted volume before starting the application, ensuring it doesn't serve traffic prematurely.

**Why Other Options Are Less Ideal:**

  * **I. gsutil within the container:** While possible, it adds complexity and potential security risks due to embedding credentials within the container.

  * **III. Embedding config in the image:** This makes image management less flexible, requiring rebuilds for configuration changes.

  * **IV. Instance Group Startup Script:** This approach tightly couples configuration management to the underlying infrastructure, making it less portable and harder to manage within Kubernetes.

**References** :

[https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes  https://cloud.google.com/filestore/docs/accessing-fileshares  https://cloud.google.com/storage/docs/gcs-fuse)

[https://cloud.google.com/filestore/docs/accessing-fileshares](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes  https://cloud.google.com/filestore/docs/accessing-fileshares  https://cloud.google.com/storage/docs/gcs-fuse)

[https://cloud.google.com/storage/docs/gcs-fuse](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes  https://cloud.google.com/filestore/docs/accessing-fileshares  https://cloud.google.com/storage/docs/gcs-fuse)

---

## Question 5

*Domain 3: Configuring and Deploying Applications*

**Upon installing the Stackdriver Logging Agent to transmit an application's log file to Stackdriver from a Compute Engine virtual machine instance, what is the initial step you should take?**

- [ ] IV. Establish a Stackdriver Logs Export Sink with a filter aligning with the application's log entries.
- [x] III. Define the application log file as a custom source.
- [ ] II. Provide the instance with complete access to all Cloud APIs.
- [ ] I. Activate the Error Reporting API for the project.

### Explanation

**The initial step you should take upon installing the Stackdriver Logging Agent to transmit an application's log file to Stackdriver from a Compute Engine virtual machine instance is:**

**III. Define the application log file as a custom source.**

**Explanation:**

I. Activating the Error Reporting API for the project:

  * While activating the Error Reporting API may be necessary for capturing and reporting errors, it is not the initial step for configuring log forwarding with the Stackdriver Logging Agent.

II. Providing the instance with complete access to all Cloud APIs:

  * Providing the instance with complete access to all Cloud APIs is not necessary for configuring log forwarding with the Stackdriver Logging Agent. It is a security best practice to provide only the necessary permissions to instances.

**III. Defining the application log file as a custom source:**

  * **This is the initial step in configuring log forwarding with the Stackdriver Logging Agent. By defining the application log file as a custom source, you specify which log files should be collected and forwarded to Stackdriver Logging.**

IV. Establishing a Stackdriver Logs Export Sink with a filter aligning with the application's log entries:

  * Establishing a Stackdriver Logs Export Sink with a filter aligning with the application's log entries is a subsequent step after defining the custom log source. It involves configuring the destination for the logs and specifying any filters to ensure only relevant log entries are exported.

**Therefore, the initial step you should take is to define the application log file as a custom source (Option III).**

Ref:  
<https://cloud.google.com/logging/docs/agent/configuration>

---

## Question 6

*Domain 2: Building and Testing Applications*

**Your company's development teams wish to incorporate various open-source operating systems into their Docker builds. As images are generated and published in containers within your company's environment, you need to conduct scans for Common Vulnerabilities and Exposures (CVEs) without hindering software development agility. Additionally, you prefer employing managed services whenever possible. What's the best course of action?**

- [ ] II. Develop a Cloud Function triggered by code check-ins to perform CVE scans on the code.
- [ ] III. Restrict the usage of non-commercially supported base images within your development environment.
- [x] I. Activate the Vulnerability scanning feature within the Container Registry.
- [ ] IV. Utilize Cloud Monitoring to scrutinize Cloud Build's output and detect if a vulnerable version has been utilized.

### Explanation

**I. Activate the Vulnerability scanning feature within the Container Registry.**

Here's why this stands out as the most suitable option:

  * **Purpose-Built:** Container Registry's vulnerability scanning feature is specifically designed to scan container images for known CVEs. It aligns directly with your core requirement.

  * **Seamless Integration:** It works seamlessly with container images stored in the Container Registry, fitting naturally into your existing workflow.

  * **Minimal Disruption:** Activating this scanning feature does not require significant changes to the development process, maintaining agility.

  * **Managed Service:** Utilizing this feature within the Container Registry aligns with your stated preference for managed services.

**Why Other Options are Less Ideal:**

  * **II. Develop a Cloud Function triggered by code check-ins to perform CVE scans on the code.** Code-level CVE scans are important, but they won't identify vulnerabilities introduced by dependencies in the container image.

  * **III. Restrict the usage of non-commercially supported base images within your development environment.** This improves security posture but might be overly restrictive and could hinder development flexibility. Not all vulnerabilities stem from lack of commercial support.

  * **IV. Utilize Cloud Monitoring to scrutinize Cloud Build's output and detect if a vulnerable version has been utilized.** Cloud Monitoring is useful for general logging and alerting but lacks the specialized CVE scanning capabilities.

**References:**  
[https://docs.docker.com/engine/scan/](https://docs.docker.com/engine/scan/  https://cloud.google.com/container-analysis/docs/os-overview)

[https://cloud.google.com/container-analysis/docs/os-overview](https://docs.docker.com/engine/scan/  https://cloud.google.com/container-analysis/docs/os-overview)

---

## Question 7

*Domain 3: Configuring and Deploying Applications*

**Your application comprises a series of loosely interconnected services managed by code executed on Compute Engine. To facilitate the seamless deployment of new Compute Engine instances accessing a specific service version, how should you configure the setup?**

- [ ] IV. Configure your service to utilize a fixed hostname and port for connecting to the desired service, and update the service at the endpoint with the new version.
- [x] I. Specify your service endpoint details as metadata fetched at runtime, enabling connection to the desired service.
- [ ] II. Specify your service endpoint details as label data fetched at runtime, facilitating connection to the desired service.
- [ ] III. Define your service endpoint details to be fetched from an environment variable at runtime, facilitating connection to the desired service.

### Explanation

**I. Specify your service endpoint details as metadata fetched at runtime, enabling connection to the desired service.**

**Explanation:**

  * **Dynamic Configuration:** Metadata is a key strength in Compute Engine. It allows you to provide instance-specific information that code running on the instance can access. This is ideal for discovering the correct endpoint to connect to.

  * **Deployment Flexibility:** With metadata, you don't need to modify code or environment variables with each service version change. Updating the metadata is enough for your new instances to point to the correct location.

**Why Other Options Aren't as Suitable**

  * **II. Labels:** Labels are primarily for organizing resources, not dynamically providing runtime configuration details.

  * **III. Environment Variables:** Environment variables can work but they introduce another element to manage during your deployment process. Metadata is more streamlined in this case.

  * **IV. Fixed Hostname/Port:** This approach is inflexible, especially if you use load balancing or service discovery, where endpoints may change dynamically.

**References:**  
[https://cloud.google.com/apis/design/glossary#api_service_endpoint https://cloud.google.com/compute/docs/metadata/overview](https://cloud.google.com/apis/design/glossary#api_service_endpoint   https://cloud.google.com/compute/docs/metadata/overview  https://cloud.google.com/service-infrastructure/docs/service-metadata/reference/rest#service-endpoint)

[https://cloud.google.com/service-infrastructure/docs/service-metadata/reference/rest#service-endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint   https://cloud.google.com/compute/docs/metadata/overview  https://cloud.google.com/service-infrastructure/docs/service-metadata/reference/rest#service-endpoint)

---

## Question 8

*Domain 3: Configuring and Deploying Applications*

**You're utilizing Cloud Build to create a new Docker image for each source code commit to a Cloud Source Repositories repository. Commits to the master branch trigger builds for your application. How can you automate the release process for specific commits to the master branch?**

- [ ] III. Configure a build trigger based on a Git branch name pattern, adhering to a Git branch naming convention for releases.
- [ ] I. Trigger the build manually for new releases.
- [x] II. Set up a build trigger based on a Git tag pattern, following a Git tag convention for releases.
- [ ] IV. Store your source code in a secondary Cloud Source Repositories repository with a distinct Cloud Build trigger solely for new releases.

### Explanation

**II. Set up a build trigger based on a Git tag pattern, following a Git tag convention for releases.**

Explanation:

  * **Versioning:** Git tags provide a clear and structured way to mark specific commits as releasable versions (e.g., v1.0.0, v1.1.2).

  * **Automation:** A Cloud Build trigger tied to your tag pattern (e.g., `v*.**`) automatically initiates builds when you create a release tag.

  * **Consistency:** A well-defined tagging convention streamlines the release process and maintains historical tracking of releases.

Why Other Options Are Less Ideal:

  * **I. Trigger the build manually...** This lacks automation and introduces potential for errors due to manual intervention.

  * **III. Configure a build trigger based on a Git branch name pattern ...** Branch naming conventions might change or be less reliable than an explicit tagging strategy.

  * **IV. Store your source code in a secondary Cloud Source Repositories repository ...** This adds unnecessary complexity, fragmenting your codebase and its history.

**Reference:**

<https://cloud.google.com/source-repositories/docs/integrating-with-cloud-build#create_a_build_trigger>

---

## Question 9

*Domain 4: Integrating Applications with Google Cloud Services*

**As you develop an event-driven application, you've set up a Pub/Sub topic to receive messages. Your objective is to process these messages in real-time while ensuring the application operates independently, incurring costs only upon message arrival. How should you architect this setup?**

- [ ] III. Deploy the application on Google Kubernetes Engine, utilizing the Pub/Sub API to establish a pull subscription for reading messages from the Pub/Sub topic.
- [ ] I. Deploy the application on Compute Engine, leveraging a Pub/Sub push subscription for processing incoming messages from the topic.
- [x] IV. Deploy your code on Cloud Functions, employing a Pub/Sub trigger to manage incoming messages from the topic.
- [ ] II. Deploy your code on Cloud Functions, utilizing a Pub/Sub trigger to invoke the function. Use the Pub/Sub API to establish a pull subscription for message retrieval from the topic.

### Explanation

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

---

## Question 10

*Domain 3: Configuring and Deploying Applications*

**Which approach should you take to install a third-party logging solution on each node in your Google Kubernetes Engine (GKE) cluster to troubleshoot intermittent performance issues?**

- [ ] IV. Utilize Terraform to deploy the third-party solution and deploy the logging Pod as a Kubernetes Deployment
- [ ] III. Manually install the software on GKE nodes via SSH
- [x] I. Implement the third-party solution as a DaemonSet
- [ ] II. Embed the monitoring software into your container image

### Explanation

**Correct option- I. Implement the third-party solution as a DaemonSet**

**I. Implement the third-party solution as a DaemonSet**

  * **Correct Option:** DaemonSets offer the most suitable approach for this scenario.

  * **Justification:** DaemonSets ensure that a pod (in this case, the logging agent) runs on each node within the Kubernetes cluster. This guarantees consistent logging across all nodes, crucial for investigating intermittent performance problems that could occur anywhere within the cluster.

**II. Embed the monitoring software into your container image**

  * **Incorrect Option:** While possible, it's not ideal for this use case.

  * **Justification:**

    * **Tight Coupling:** Embedding the logging agent directly in your application containers creates unnecessary dependencies and complicates future updates to either the application or the logging solution.

    * **Node-Level Issues:** This method only logs issues within your application container, missing potential problems at the node or infrastructure level that might be causing the performance problems.

**III. Manually install the software on GKE nodes via SSH**

  * **Incorrect Option:** This approach should be avoided.

  * **Justification:**

    * **Scalability:** Manual installation is time-consuming and prone to human error, especially in large clusters.

    * **Maintenance:** Updating the logging agent across nodes becomes tedious and harder to track.

    * **Kubernetes Philosophy:** It goes against the declarative nature of Kubernetes, where infrastructure state should be managed through configuration, not manual intervention.

**IV. Utilize Terraform to deploy the third-party solution and deploy the logging Pod as a Kubernetes Deployment**

  * **Potentially Correct, but less ideal than DaemonSets:** Terraform can automate the deployment, but...

  * **Justification:**

    * **Node-Level Granularity:** Regular Deployments don't guarantee a pod on each node. You might get multiple logging pods on the same node or miss some nodes entirely, leading to inconsistent logging coverage.

---

## Question 11

*Domain 2: Building and Testing Applications*

**As part of updating Cloud Build steps to align with best practices, you're tasked with integrating a vulnerability scan for the built container image. The scan results should seamlessly integrate into your Google Cloud deployment pipeline without causing disruptions to other teams' processes. What's the recommended approach?**

- [x] III. Enable the Container Scanning API in Artifact Registry to scan the built container images for vulnerabilities.
- [ ] IV. Integrate Artifact Registry with your Aqua Security instance to perform vulnerability scans on the built container images.
- [ ] II. Upload the built container images to your Docker Hub instance and conduct vulnerability scans.
- [ ] I. Enable Binary Authorization and configure it to attest that no vulnerabilities exist in the container image.

### Explanation

**Correct Option:**

**III. Enable the Container Scanning API in Artifact Registry to scan the built container images for vulnerabilities.**

**Explanation:**

  * **Native Integration:** The Container Scanning API is a built-in feature of Artifact Registry, providing a seamless and integrated vulnerability scanning experience within Google Cloud.

  * **Minimal Disruption:** Adding a vulnerability scan in Artifact Registry is unlikely to disrupt other teams' workflows, as it's a natural extension of storing images.

  * **Actionable Results:** Container Scanning can be configured to generate findings viewable in Security Command Center, providing insights and the ability to potentially block deployments based on vulnerability severity.

**Why other options are less ideal:**

  * **I. Binary Authorization:** While critical, Binary Authorization relies on attestations. Vulnerability scanning would be the mechanism to generate such attestations but isn't a vulnerability scanner itself.

  * **II. Docker Hub Scanning:** This involves pushing images to an external repository and adds another dependency outside of GCP.

  * **IV. Aqua Security Integration:** While Aqua Security is a robust tool, it introduces another external system to manage and adds complexity to your pipeline.

**References:**  
<https://cloud.google.com/container-analysis/docs/automated-scanning-howto#view_the_image_vulnerabilities>

---

## Question 12

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You're tasked with constructing an API for Android and iOS apps, with the following prerequisites:**

**HTTPS support is essential**

**Bandwidth usage should be minimized**

**Seamless integration with mobile apps is a priority**

**Which API architecture is the most appropriate choice for meeting these criteria?**

- [x] III. gRPC-based APIs
- [ ] I. RESTful APIs
- [ ] IV. SOAP-based APIs
- [ ] II. MQTT for APIs

### Explanation

The most appropriate choice for meeting the given criteria is 

**III. gRPC-based APIs**. Here's why:

gRPC-based APIs:

  * **HTTPS support** : gRPC natively supports HTTPS via HTTP/2, ensuring secure data transmission.

  * **Bandwidth usage** : gRPC is optimized for performance by using **HTTP/2** , which allows multiplexing and reduces latency. It also uses **Protobuf** (Protocol Buffers) for data serialization, which is more compact than JSON (used by REST) or XML (used by SOAP), leading to reduced bandwidth consumption.

  * **Seamless integration** : gRPC offers excellent cross-platform compatibility and comes with **code generation tools** for multiple languages (including Android and iOS), simplifying the integration process with mobile apps.

Other options and why they are less suitable:

  * **I. RESTful APIs** : While REST is widely used and supports HTTPS, it relies on **JSON** for data exchange, which is bulkier than Protobuf. REST also uses HTTP/1.1, which is not as efficient as HTTP/2 in terms of bandwidth usage and performance, particularly in mobile environments.

  * **II. MQTT for APIs** : MQTT is a lightweight protocol primarily designed for messaging in IoT systems. It is not ideal for APIs intended for mobile applications as it focuses more on **publish/subscribe messaging** rather than standard request/response patterns that are common in APIs. While it minimizes bandwidth, it's not designed to integrate seamlessly with mobile app APIs.

  * **IV. SOAP-based APIs** : SOAP uses **XML** for message formats, which is much larger and more verbose compared to gRPC’s Protobuf or even REST’s JSON. SOAP APIs are also less flexible and have more overhead in terms of both bandwidth usage and development complexity, especially for mobile platforms.

Ref:

[https://www.imaginarycloud.com/blog/grpc-vs-rest/](https://www.imaginarycloud.com/blog/grpc-vs-rest/  https://cloud.google.com/blog/products/api-management/understanding-grpc-openapi-and-rest-and-when-to-use-them)

[https://cloud.google.com/blog/products/api-management/understanding-grpc-openapi-and-rest-and-when-to-use-them](https://www.imaginarycloud.com/blog/grpc-vs-rest/  https://cloud.google.com/blog/products/api-management/understanding-grpc-openapi-and-rest-and-when-to-use-them)

---

## Question 13

*Domain 3: Configuring and Deploying Applications*

**Your data resides in Cloud Storage buckets. Colleagues have reported that retrieving data from Cloud Storage is causing sluggish performance in API responses. To investigate the issue thoroughly and provide pertinent details to the GCP support team, which command should you execute?**

- [ ] III. `**gcloud compute scp example-instance:~/test-data -o output.json gs://my-bucket**`
- [ ] IV. `**gcloud services test -o output.json gs://my-bucket**`
- [ ] I. `**gsutil test -o output.json gs://my-bucket**`
- [x] II. `**gsutil perfdiag -o output.json gs://my-bucket**`

### Explanation

**II. gsutil perfdiag -o output.json gs://my-bucket**

Explanation:

  * **gsutil perfdiag:** This command specifically diagnoses Cloud Storage performance issues, capturing detailed metrics and trace information.

  * **output.json:** The output is stored in a structured JSON file for easy analysis and inclusion in your communication with GCP support.

  * **Targeted Diagnostics:** `perfdiag` measures factors like network latency, object sizes, throughput, and error rates – all directly influencing data retrieval speed.

Why Other Options Are Less Ideal:

  * **I. gsutil test ...** This performs basic connectivity tests but doesn't provide the in-depth performance profiling relevant to your scenario.

  * **III. gcloud compute scp ...** This command is for copying files between a Compute Engine instance and Cloud Storage. It might be useful in some performance investigations, but not for the initial diagnosis.

  * **IV. gcloud services test ...** This tests the health status of Google Cloud services in general, not the granular performance of Cloud Storage.

**Reference:**  
<https://cloud.google.com/storage/docs/gsutil/commands/perfdiag#providing-diagnostic-output-to-cloud-storage-team>

---

## Question 14

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**In your Google Cloud-hosted application, you're utilizing a MySQL relational database schema with substantial read and write activity. This necessitates backups and ongoing capacity planning. While your team can handle minor administrative tasks, full database management is challenging. How should you deploy the database?**

- [ ] III. Configure Bigtable to host the database and import the data.
- [x] I. Implement Cloud SQL for hosting the database, importing the schema accordingly.
- [ ] IV. Set up Cloud Spanner to host the database, importing the schema.
- [ ] V. Utilize Firestore for hosting the database, importing the data.
- [ ] II. Deploy MySQL from the Google Cloud Marketplace using a client and import the schema.

### Explanation

**Correct Answer:**

  * **I. Implement Cloud SQL for hosting the database, importing the schema accordingly.**

**Justification:**

  * **Managed MySQL:** Cloud SQL provides a fully managed MySQL service, specifically aligned with the scenario's requirements.

  * **Reduced Operational Burden:** Cloud SQL handles backups, replication, scaling, and updates, significantly decreasing your team's administrative overhead.

  * **Relational Workload Alignment:** Cloud SQL is inherently designed for relational database workloads with high read/write activity.

  * **Capacity Planning:** Cloud SQL offers tools and insights for managing and projecting database capacity needs.

**Why Other Options Are Less Suitable:**

  * **II. Deploy MySQL from the Google Cloud Marketplace using a client and import the schema.**

    * **Administrative Overhead:** This approach leaves you responsible for managing the entire database lifecycle, including backups, patches, scaling, etc., which your team wants to avoid.

  * **III. Configure Bigtable to host the database and import the data.**

    * **Schema Mismatch:** Bigtable is a NoSQL wide-column database. Its structure and query model are vastly different from a relational MySQL schema.

  * **IV. Set up Cloud Spanner to host the database, importing the schema.**

    * **Potential Overkill:** Cloud Spanner is a globally distributed, strongly consistent relational database. While powerful, it might be more than you need for a standard MySQL use-case and could increase costs.

  * **V. Utilize Firestore for hosting the database, importing the data.**

    * **NoSQL Model:** Firestore is a document-oriented NoSQL database, not a suitable replacement for a relational schema.

**Reference:**  
<https://cloud.google.com/sql/docs/mysql>

---

## Question 15

*Domain 3: Configuring and Deploying Applications*

**In setting up a build pipeline for an application intended to operate in Google Kubernetes Engine (GKE), your team prioritizes security to permit only images generated by the pipeline to be deployed to the GKE cluster. Which combination of Google Cloud services should be employed?**

- [ ] I. Cloud Build, Cloud Storage, and Binary Authorization
- [ ] III. Google Cloud Deploy, Artifact Registry, and Google Cloud Armor
- [ ] II. Google Cloud Deploy, Cloud Storage, and Google Cloud Armor
- [x] IV. Cloud Build, Artifact Registry, and Binary Authorization

### Explanation

**Correct Answer:**

  * **IV. Cloud Build, Artifact Registry, and Binary Authorization**

**Justification:**

  * **Image Pipeline:** Cloud Build is ideal for creating the container images in a secure and controlled build process.

  * **Trusted Repository:** Artifact Registry serves as a secure, managed image repository, providing fine-grained access controls.

  * **Deployment Authorization:** Binary Authorization acts as a gatekeeper, ensuring that only images that have passed specific checks (build provenance, vulnerability scans, etc.) are allowed for deployment to GKE.

**Why Other Options Are Less Ideal:**

  * **I. Cloud Build, Cloud Storage, and Binary Authorization**

    * **Artifact Registry Advantage:** While Cloud Storage can store images, Artifact Registry offers features tailored for container management, such as versioning and vulnerability scanning integration.

  * **II. Google Cloud Deploy, Cloud Storage, and Google Cloud Armor**

    * **Focus Mismatch:** Google Cloud Deploy is for managing application deployments, not enforcing image security policy. Google Cloud Armor is a web application firewall (WAF), not directly related to secure build pipelines.

  * **III. Google Cloud Deploy, Artifact Registry, and Google Cloud Armor**

    * **Missing Authorization:** While Artifact Registry provides a secure repository, it needs Binary Authorization to enforce the "only approved images" policy.

**References:**

[https://cloud.google.com/binary-authorization/docs/cloud-build](https://cloud.google.com/binary-authorization/docs/cloud-build  https://cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke#objectives)

[https://cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke#objectives](https://cloud.google.com/binary-authorization/docs/cloud-build  https://cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke#objectives)

---

## Question 16

*Domain 4: Integrating Applications with Google Cloud Services*

**To enhance the performance of your Go application when interacting with a Cloud Spanner database, which approach should you adopt based on Google's recommended best practices?**

- [x] I. Utilize Cloud Client Libraries to interface with Cloud Spanner.
- [ ] II. Utilize Google API Client Libraries to interact with Cloud Spanner.
- [ ] III. Employ a custom gRPC client library for writing to Cloud Spanner.
- [ ] IV. Implement a third-party HTTP client library for writing to Cloud Spanner.

### Explanation

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

---

## Question 17

*Domain 2: Building and Testing Applications*

**You are monitoring a web application deployed on Google Kubernetes Engine, developed in Go. An increase in CPU and memory usage has been observed. How can you determine which sections of the source code are consuming the most CPU and memory resources?**

- [ ] III. Integrate OpenTelemetry and Trace export packages into your application to create the trace provider. Examine the latency data for your application on the Trace overview page to identify bottleneck areas.
- [ ] IV. Develop a Cloud Logging query to collect the web application's logs. Create a Python script to compute the difference between the timestamps from the beginning and end of the application's longest functions to identify time-intensive functions.
- [ ] I. Install the Snapshot Debugger agent in your VM. Capture debug snapshots of the functions with the longest execution time. Analyze the call stack frame to identify the local variables at that level in the stack.
- [x] II. Incorporate the Cloud Profiler package into your application and initialize the Profiler agent. Review the generated flame graph in the Google Cloud console to pinpoint time-intensive functions.

### Explanation

**Correct Answer:**

  * **II. Incorporate the Cloud Profiler package into your application and initialize the Profiler agent. Review the generated flame graph in the Google Cloud console to pinpoint time-intensive functions.**

**Justification:**

  * **Specific to Application Profiling:** Cloud Profiler is a continuous profiling tool designed explicitly to identify performance bottlenecks in applications running on production environments like Google Kubernetes Engine.

  * **Optimized for GKE:** It has seamless integration with GKE, minimizing setup complexity.

  * **Flame Graphs:** Flame graphs are an effective visual representation for pinpointing resource-heavy code sections, making analysis efficient.

**Why Other Options Are Less Suitable:**

  * **I. Install the Snapshot Debugger agent in your VM...**

    * **Debugging vs. Profiling:** Snapshot Debugger is primarily a debugging tool. While it can provide insights into code execution, it's less tailored for continuous resource usage monitoring.

    * **Overhead:** Introducing a debugger can add overhead to a production environment.

  * **III. Integrate OpenTelemetry and Trace export packages...**

    * **Focus on Tracing:** OpenTelemetry is excellent for distributed tracing, which primarily tracks request flows across systems. It's less direct for pinpointing CPU or memory-heavy code sections within the application itself.

  * **IV. Develop a Cloud Logging query to collect the web application's logs...**

    * **Manual and Time-Consuming:** Analyzing logs manually can be effective but is often tedious for pinpointing performance issues. Profilers are more efficient for this specific task.

**References:**

[https://cloud.google.com/profiler/docs](https://cloud.google.com/profiler/docs  https://cloud.google.com/profiler/docs/about-profiler#profiling_agent  https://cloud.google.com/profiler/docs/about-profiler#environment_and_languages)

[https://cloud.google.com/profiler/docs/about-profiler#profiling_agent](https://cloud.google.com/profiler/docs  https://cloud.google.com/profiler/docs/about-profiler#profiling_agent  https://cloud.google.com/profiler/docs/about-profiler#environment_and_languages)

[https://cloud.google.com/profiler/docs/about-profiler#environment_and_languages](https://cloud.google.com/profiler/docs  https://cloud.google.com/profiler/docs/about-profiler#profiling_agent  https://cloud.google.com/profiler/docs/about-profiler#environment_and_languages)

---

## Question 18

*Domain 3: Configuring and Deploying Applications*

**To deploy a new European version of a website on Google Kubernetes Engine, ensuring both the current and new websites can be accessed via the same HTTP(S) load balancer's external IP address but with different domain names, what action should you take?**

- [ ] I. Define a new Ingress resource with a host rule matching the new domain.
- [ ] III. Create a new Service of type LoadBalancer specifying the existing IP address as the loadBalancerIP.
- [ ] IV. Generate a new Ingress resource and specify the existing IP address as the kubernetes.io/ingress.global-static-ip-name annotation value.c
- [x] II. Modify the existing Ingress resource with a host rule matching the new domain.

### Explanation

**II. Modify the existing Ingress resource with a host rule matching the new domain.**

Here's why:

  * **Ingress for Routing:** Ingress is the preferred way to expose Kubernetes services outside the cluster, and it's designed for routing traffic based on domain names.

  * **Shared Load Balancer:** Since you want to reuse the existing HTTP(S) load balancer, modifying the existing Ingress is the most straightforward approach.

  * **Host-based Routing:** Ingress resources use host rules to determine which backend service to route traffic to based on the incoming domain name. By adding a new host rule for the European domain, you can direct traffic to the appropriate service within your GKE cluster.

**Why other options are not as suitable:**

  * **I. New Ingress Resource:** While technically possible, creating a separate Ingress would likely result in the provisioning of a new external IP address, which isn't the goal.

  * **III. New LoadBalancer Service:** Creating a new LoadBalancer service would also provision a new IP address. Moreover, using raw Kubernetes services for this type of routing is less manageable than using an Ingress.

  * **IV. Static IP Annotation:** This annotation is used to associate a specific static IP address with an Ingress resource. While relevant for preserving an IP, it's not the primary mechanism for adding a new domain route.

**References:**

[https://kubernetes.io/docs/concepts/services-networking/ingress/#name-based-virtual-hosting https://cloud.google.com/kubernetes-engine/docs/tutorials/configuring-domain-name-static-ip](https://kubernetes.io/docs/concepts/services-networking/ingress/#name-based-virtual-hosting   https://cloud.google.com/kubernetes-engine/docs/tutorials/configuring-domain-name-static-ip)

---

## Question 19

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Your company operates a data warehouse in BigQuery, storing 2 PBs of user data. With the expansion of your user base to include EU users, compliance requirements mandate:**

  * **User account information must be deletable upon user request.**

  * **EU user data must reside within a designated EU region.**

**Which two actions should you take to meet these requirements? (Choose two.)**

- [ ] IV. Utilize a Cloud Dataflow pipeline to re-upload data, filtering out user records based on region.
- [ ] I. Implement BigQuery federated queries to access data stored in Cloud Storage.
- [ ] III. Create a Cloud Storage bucket in the EU region to exclusively store data for EU users.
- [x] V. Execute Data Manipulation Language (DML) statements within BigQuery to update or delete user records as per their requests.
- [x] II. Establish a dataset in the EU region dedicated to storing information for EU users exclusively.

### Explanation

* **II. Establish a dataset in the EU region dedicated to storing information for EU users exclusively.** This allows you to comply with data residency requirements by storing EU user data within the specified region.

  * **V. Execute Data Manipulation Language (DML) statements within BigQuery to update or delete user records as per their requests.** DML statements are necessary to fulfill user requests for data modification or deletion, ensuring compliance with privacy regulations.

**Why Other Options Are Not Ideal**

  * **I. Implement BigQuery federated queries to access data stored in Cloud Storage.** While federated queries can be useful, they don't directly address user deletion or data residency requirements.

  * **III. Create a Cloud Storage bucket in the EU region to exclusively store data for EU users.** Using a regional Cloud Storage bucket helps with data residency, but it doesn't intrinsically offer mechanisms for user data deletion. You would still need additional processes in place.

  * **IV. Utilize a Cloud Dataflow pipeline to re-upload data, filtering out user records based on region.** This could achieve compliance, but is likely more complex than necessary. Modifying or deleting data in BigQuery directly is likely to be more efficient.

---

## Question 20

*Domain 2: Building and Testing Applications*

**While employing Cloud Build to build and test application source code stored in Cloud Source Repositories, you encounter a requirement for a build tool that isn't available in the Cloud Build environment. What's the recommended course of action?**

- [ ] III. Embed the binary in your Cloud Source Repositories repository and reference it in your build scripts.
- [ ] IV. Request the addition of the binary to the Cloud Build environment by submitting a feature request via the Cloud Build public Issue Tracker.
- [x] II. Develop a custom cloud builder image and specify it in your build steps.
- [ ] I. Fetch the binary from the internet during the build process.

### Explanation

**II. Develop a custom cloud builder image and specify it in your build steps.**

**Explanation:**

  * **Customization:** Creating a custom cloud builder image gives you complete control over the tools and libraries available in the build environment.

  * **Reproducibility:** The image ensures that builds are consistent and independent of changes in default Cloud Build environments.

  * **Maintainability:** You manage the build tool's installation and version within the image.

**Why Other Options Are Less Ideal:**

  * **I. Fetch the binary from the internet during the build process.** This introduces potential security risks, network dependency, and could make builds less reproducible if the external source changes.

  * **III. Embed the binary in your Cloud Source Repositories repository and reference it in your build scripts.** Bundling a large binary with your source code can increase repository size and potentially complicate build scripts.

  * **IV. Request the addition of the binary...** This is a viable long-term option, but it doesn't give you immediate control and might not be possible if the tool isn't widely used.

**Reference:**

<https://cloud.google.com/cloud-build/docs/configuring-builds/use-community-and-custom-builders#creating_a_custom_builder>

---

## Question 21

*Domain 3: Configuring and Deploying Applications*

**You're preparing to deploy a new Go application to Cloud Run, with its source code stored in Cloud Source Repositories. You aim to establish a fully managed, automated, continuous deployment pipeline triggered by each source code commit. Seeking the simplest deployment solution,**

**what should you do?**

- [ ] II. Configure a Jenkins trigger to initiate the container build and deployment process for each source code commit made to Cloud Source Repositories.
- [ ] III. Enable continuous deployment of new revisions from the source repository to Cloud Run using buildpacks.
- [ ] I. Set up a cron job on your workstations to periodically execute 'gcloud run deploy --source' within the working directory.
- [x] IV. Utilize Cloud Build with a trigger configured to execute the container build and deploy process for each source code commit to Cloud Source Repositories.

### Explanation

**Correct Option:**

**IV. Utilize Cloud Build with a trigger configured to execute the container build and deploy process for each source code commit to Cloud Source Repositories.**

**Explanation:**

  * **Fully Managed:** Cloud Build is a serverless CI/CD platform within Google Cloud, eliminating the need to manage your own build infrastructure.

  * **Easy Integration:** Cloud Build integrates seamlessly with Cloud Source Repositories, allowing you to set up triggers that automatically initiate builds on commits.

  * **Cloud Run Deployment:** Cloud Build can directly build and deploy container images to Cloud Run, simplifying the entire pipeline.

  * **Simplicity:** This approach offers a streamlined workflow with minimal setup on your side.

**Why other options are less ideal:**

  * **I. Cron Job:** This solution is manual, not automated, and requires you to manage the cron schedule and deployment script.

  * **II. Jenkins:** While powerful, Jenkins introduces the overhead of maintaining your own Jenkins server and its configuration.

  * **III. Buildpacks:** Buildpacks can be a great option, but they might require additional configuration if you have specific build requirements beyond what buildpacks provide.

**Reference:**  
<https://cloud.google.com/run/docs/continuous-deployment-with-cloud-build>

---

## Question 22

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**As your development team refactors an existing monolithic application into a set of composable microservices, which design aspects should you prioritize for the new application? (Select two.)**

- [x] V. Introduce a versioning scheme to accommodate future changes that might be incompatible with the current interface.
- [x] II. Establish an API contract agreement between the microservice implementation and microservice caller.
- [ ] I. Craft the microservice code in the same programming language utilized by the microservice caller.
- [ ] IV. Ensure adequate instances of the microservice are running to meet performance requirements.
- [ ] III. Implement asynchronous communications between all microservice implementations and microservice callers.

### Explanation

**II. Establish an API contract agreement between the microservice implementation and microservice caller.**

**V. Introduce a versioning scheme to accommodate future changes that might be incompatible with the current interface.**

Here's why these choices are critical:

  * **API Contracts:** Decoupling is a core principle of microservices. Well-defined API contracts ensure that microservices can change internally without impacting their consumers as long as they honor the agreed-upon contract.

  * **Versioning:** In a distributed system, it's inevitable that you'll need to introduce changes. A robust versioning scheme allows you to evolve microservices while maintaining compatibility or enabling graceful transitions for consumers.

**Let's analyze the other options:**

  * **I. Same Programming Language:** While using the same language can sometimes be convenient, microservice architectures should prioritize language-agnostic communication protocols (like REST or gRPC) to enable flexibility and choice of technology.

  * **III. Asynchronous Communication (Always):** While asynchronous communication is often beneficial in microservices, it's not always strictly necessary. Some interactions might be better suited for synchronous communication patterns.

  * **IV. Adequate Instances for Performance:** While scaling is important, it's more of an operational concern rather than a fundamental microservice design aspect.

**References:**  
[https://cloud.google.com/architecture/migrating-a-monolithic-app-to-microservices-gke#api_contracts](https://cloud.google.com/architecture/migrating-a-monolithic-app-to-microservices-gke#api_contracts  https://cloud.google.com/architecture/migrating-a-monolithic-app-to-microservices-gke#versioning  https://cloud.google.com/architecture/microservices-architecture-refactoring-monoliths)

[https://cloud.google.com/architecture/migrating-a-monolithic-app-to-microservices-gke#versioning](https://cloud.google.com/architecture/migrating-a-monolithic-app-to-microservices-gke#api_contracts  https://cloud.google.com/architecture/migrating-a-monolithic-app-to-microservices-gke#versioning  https://cloud.google.com/architecture/microservices-architecture-refactoring-monoliths)

[https://cloud.google.com/architecture/microservices-architecture-refactoring-monoliths](https://cloud.google.com/architecture/migrating-a-monolithic-app-to-microservices-gke#api_contracts  https://cloud.google.com/architecture/migrating-a-monolithic-app-to-microservices-gke#versioning  https://cloud.google.com/architecture/microservices-architecture-refactoring-monoliths)

---

## Question 23

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**For deploying a new API with three distinct URL paths - /students, /teachers, and /classes - each invoking a different function in your code, what action should you take?**

- [x] IV. Deploy three distinct Cloud Functions, each as a separate backend service, exposed via an HTTPS load balancer, and configure them to handle requests for /students, /teachers, and /classes, respectively.
- [ ] II. Establish three separate Cloud Functions, each directly exposed, to handle requests for /students, /teachers, and /classes.
- [ ] I. Deploy a single Cloud Function serving as a backend service, exposed via an HTTPS load balancer, and configure it to handle requests for all three URL paths.
- [ ] III. Create a single Cloud Function directly exposed to handle all incoming requests regardless of the URL path.

### Explanation

**IV. Deploy three distinct Cloud Functions, each as a separate backend service, exposed via an HTTPS load balancer, and configure them to handle requests for /students, /teachers, and /classes, respectively.**

Explanation:

Option IV is the most suitable approach for deploying a new API with three distinct URL paths (/students, /teachers, and /classes), each invoking a different function in your code. Here's why:

  * **Three distinct Cloud Functions** : Since each URL path (/students, /teachers, and /classes) invokes a different function in your code, deploying three separate Cloud Functions allows you to encapsulate the logic for each endpoint separately. This ensures better maintainability and scalability.

  * **Separate backend services** : By configuring each Cloud Function as a separate backend service, you can route requests to the appropriate function based on the URL path. This allows for clear separation of concerns and efficient handling of incoming requests.

  * **Exposed via an HTTPS load balancer** : Exposing the Cloud Functions via an HTTPS load balancer ensures that incoming requests are distributed evenly and efficiently across the backend services. It also provides HTTPS encryption and scalability features.

Options I, II, and III suggest deploying a single Cloud Function or fewer Cloud Functions to handle all incoming requests, which would not align with the requirement of having distinct functions for each URL path.

Therefore, option IV is the recommended action for deploying a new API with three distinct URL paths on Google Cloud Platform.

---

## Question 24

*Domain 4: Integrating Applications with Google Cloud Services*

**You are developing a social media application and planning to implement an image upload feature. The images can range from 2 MB to 1 GB in size. You aim to minimize infrastructure operations for this feature. What approach should you take?**

- [ ] III. Configure a web server on GCP to handle user image uploads. Establish a file store to store uploaded files, and modify the application to fetch images from this file store.
- [ ] I. Modify the application to directly accept images and store them in the database along with other user information.
- [x] II. Implement signed URLs for Cloud Storage in the application. Provide these signed URLs to clients for uploading images to Cloud Storage.
- [ ] IV. Create individual buckets for each user in Cloud Storage. Assign separate service accounts to each bucket for write access. Provide client applications with the necessary service account credentials based on user information to upload images to Cloud Storage.

### Explanation

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

---

## Question 25

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You manage an application hosted on a Compute Engine instance and multiple backend services deployed in standalone Docker containers across Compute Engine instances managed by instance groups in different regions. To achieve loose coupling, you aim to call different service implementations based on the value of an HTTP header in the request. Which Google Cloud feature should you utilize to invoke the backend services?**

- [ ] II. Service Directory
- [ ] IV. Internal HTTP(S) Load Balancing
- [x] I. Traffic Director
- [ ] III. Anthos Service Mesh

### Explanation

**I. Traffic Director**

Here's why Traffic Director is the best fit:

  * **Content-based Routing:** Traffic Director allows you to define routing rules based on various attributes of the request, including HTTP headers. This enables you to route requests to different backend services depending on the value of a specific header.

  * **Global Service Management:** Traffic Director is a global service, allowing you to manage traffic across multiple regions and seamlessly steer requests to distributed backend instances.

  * **Integration with Load Balancing:** Traffic Director can integrate with Internal HTTP(S) Load Balancing to distribute traffic among backend instances within each region.

**Why Other Options Are Less Ideal**

  * **II. Service Directory:** While Service Directory aids in service discovery, it doesn't directly provide the content-based routing capabilities necessary for your scenario.

  * **III. Anthos Service Mesh:** Anthos Service Mesh offers advanced traffic management but introduces complexity in this case. Traffic Director is a more streamlined solution for your specific requirement.

  * **IV. Internal HTTP(S) Load Balancing:** Internal HTTP(S) Load Balancing lacks the ability to make routing decisions based on HTTP headers.

**References:**

[https://cloud.google.com/traffic-director/docs/set-up-gce-vms](https://cloud.google.com/traffic-director/docs/set-up-gce-vms  https://cloud.google.com/traffic-director/docs/overview#traffic_management)

[https://cloud.google.com/traffic-director/docs/overview#traffic_management](https://cloud.google.com/traffic-director/docs/set-up-gce-vms  https://cloud.google.com/traffic-director/docs/overview#traffic_management)

---

## Question 26

*Domain 2: Building and Testing Applications*

**In response to a surge in errors within an application operating on Cloud Run within your production environment, configured to handle messages from Pub/Sub topic A, process them, and then forward them to topic B, what steps should you take to identify the error's cause, utilizing mock messages for testing?**

- [ ] IV. Utilize the Google Cloud console to generate mock messages for topic A. Adjust the application's logging level to DEBUG or INFO, then analyze the logs for diagnostic information.
- [ ] III. Set up the Pub/Sub emulator locally. Redirect the production application to interact with local Pub/Sub topics. Generate mock messages for topic A and analyze the resulting logs.
- [ ] II. Utilize the gcloud CLI to generate mock messages for topic A. Adjust the application's logging level to DEBUG or INFO, then analyze the logs for insights.
- [x] I. Install the Pub/Sub and Cloud Run emulators on your local system. Deploy the application locally, adjusting the logging level to DEBUG or INFO. Generate mock messages for topic A and analyze the application logs.

### Explanation

The most effective approach to identify the error's cause in your Cloud Run application using mock messages is:

**I. Install the Pub/Sub and Cloud Run emulators on your local system. Deploy the application locally, adjusting the logging level to DEBUG or INFO. Generate mock messages for topic A and analyze the application logs.**

Here's why this approach is the best:

  * **Isolated testing environment:** The emulators allow you to replicate the production environment locally, isolating the issue and eliminating potential interference from other production components.

  * **Controlled testing:** You have complete control over the mock messages generated, enabling you to reproduce specific scenarios that trigger the errors.

  * **Detailed logging:** Adjusting the logging level provides granular insights into the application's behavior during message processing, helping pinpoint the root cause of the errors.

  * **Efficient debugging:** Debugging locally is generally faster and more convenient than troubleshooting in a production environment.

Let's analyze why the other options aren't as suitable:

  * **II. Utilize the gcloud CLI to generate mock messages for topic A.** While this allows you to generate mock messages, it doesn't provide an isolated testing environment, potentially making it difficult to isolate the issue.

  * **III. Set up the Pub/Sub emulator locally. Redirect the production application to interact with local Pub/Sub topics.** This approach involves modifying the production application's configuration, which could introduce risks and disruptions to the live environment.

  * **IV. Utilize the Google Cloud console to generate mock messages for topic A.** Similar to option II, this lacks an isolated testing environment and might not be the most efficient way to reproduce and diagnose the errors.

**By installing the emulators and testing locally, you create a safe and controlled environment to thoroughly investigate the errors and identify their root cause without impacting the production system.**

---

## Question 27

*Domain 3: Configuring and Deploying Applications*

**You are designing a deployment strategy for your new applications on Google Cloud. As part of your deployment planning, you aim to leverage live traffic to collect performance metrics for both new and existing applications. You need to test against the full production load before launch. What should you do?**

- [ ] II. Implement blue/green deployment.
- [x] IV. Employ A/B testing with traffic mirroring during deployment.
- [ ] I. Opt for canary deployment.
- [ ] III. Choose rolling updates deployment.

### Explanation

**IV. Employ A/B testing with traffic mirroring during deployment.**

Let's break down why this is the most effective choice:

  * **Live Production Traffic:** Traffic mirroring allows you to test new code with real production traffic without impacting user experience. This gives you the most realistic performance assessment.

  * **Full Load Testing:** Mirroring the entire production load ensures you're testing against the true scale of your traffic.

  * **A/B Comparison:** Comparing the performance of your new application code against the existing version under identical load provides valuable insights for optimization.

  * **Controlled Rollout:** Based on the results of your A/B tests, you can gradually and safely increase traffic to the new version.

**Why Other Options are Less Ideal:**

  * **I. Canary Deployment:** While it offers gradual rollout and risk mitigation, its focus is not on pre-launch load testing. You'd get only partial traffic exposure.

  * **II. Blue/Green Deployment:** This is for rapid cutovers, not gradual testing with full production load. You'd also need to maintain duplicate production environments.

  * **III. Rolling Updates:** This focuses on gradual rollout, but doesn't inherently provide side-by-side comparisons or full production load testing.

**Reference:**

<https://cloud.google.com/architecture/application-deployment-and-testing-strategies#shadow_test_pattern>

---

## Question 28

*Domain 2: Building and Testing Applications*

**After integrating a new application with OpenTelemetry, you aim to monitor the latency of your application requests within Trace. Your goal is to guarantee that a particular request is consistently traced. What is the recommended course of action?**

- [ ] III. Employ the Trace API to assign custom attributes to the trace.
- [ ] II. Develop a custom script to continuously send requests of this type from your development project.
- [ ] I. Allow a 10-minute interval to confirm that Trace automatically captures these specific requests.
- [x] IV. Append the X-Cloud-Trace-Context header to the request with the correct parameters.

### Explanation

**IV. Append the X-Cloud-Trace-Context header to the request with the correct parameters.**

Here's why:

  * **Forced Tracing:** The `X-Cloud-Trace-Context` header directly instructs Cloud Trace to include the specific request in its traces. This ensures the desired request is traced regardless of other factors or sampling configurations.

Here's why the other options are less ideal:

  * **I. Waiting:** Traces might not automatically capture the request, especially if sampling is in place or the request volume is low.

  * **II. Scripting:** While a script could help, it's not the most efficient way to force tracing for a specific request type.

  * **III. Custom Attributes:** Adding attributes helps provide context but doesn't guarantee the request is traced.

References:

<https://cloud.google.com/trace/docs/setup#force-trace>

---

## Question 29

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**As part of your role in an ecommerce company planning global expansion, you are tasked with selecting a SQL database and designing a schema capable of scaling with organizational growth. To store all customer transactions, you need to create a table ensuring uniqueness for both CustomerId and TransactionId. Which approach should you take?**

- [ ] II. Establish a Cloud SQL table with TransactionId and CustomerId set as primary keys, utilizing random strings (UUID) for TransactionId.
- [x] III. Implement a Cloud Spanner table with TransactionId and CustomerId configured as primary keys, employing random strings (UUID) for TransactionId.
- [ ] I. Establish a Cloud SQL table with TransactionId and CustomerId set as primary keys, employing incremental numbers for TransactionId.
- [ ] IV. Implement a Cloud Spanner table with TransactionId and CustomerId configured as primary keys, utilizing incremental numbers for TransactionId.

### Explanation

**The best option is**

**III: Implement a Cloud Spanner table with TransactionId and CustomerId configured as primary keys, employing random strings (UUID) for TransactionId.**

**Here's why:**

  * **Scalability:** Cloud Spanner is Google Cloud's globally distributed, strongly consistent database designed for massive scale. It's ideal for handling the high volume and geographic spread expected with global expansion.

  * **Uniqueness:** Using UUIDs (Universally Unique Identifiers) for TransactionIds guarantees uniqueness across distributed systems. This is crucial in a global context where transactions might originate from different regions simultaneously.

  * **Strong Consistency:** Cloud Spanner ensures that data is always consistent, even across globally distributed nodes. This is important for financial transactions in e-commerce, where data integrity is paramount.

**Why other options are less suitable:**

  * **I. Cloud SQL with incremental TransactionIds:** Cloud SQL is a regional database and might struggle to scale as your business expands globally. Additionally, sequential transaction IDs can become a bottleneck and increase the risk of collisions in a high-volume, distributed environment.

  * **II. Cloud SQL with UUID TransactionIds:** While UUIDs would address the uniqueness issue, Cloud SQL's regional nature still poses a challenge for a globally distributed application.

  * **IV. Cloud Spanner with incremental TransactionIds:** This option combines the scalability of Cloud Spanner with the potential collision risks of sequential transaction IDs.

**Reference:**

<https://cloud.google.com/spanner/docs/schema-design#uuid_primary_key>

---

## Question 30

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You're structuring a schema for a Cloud Spanner customer database, aiming to incorporate a phone number array field in the customer table for efficient customer search by phone number. How should you design this schema?**

- [ ] I. Design a "Customers" table featuring an Array field to accommodate multiple phone numbers per customer.
- [ ] II. Create a "Customers" table along with a separate "Phones" table. Include a "CustomerId" field in the "Phones" table to associate phone numbers with customers.
- [ ] III. Set up a "Customers" table with an Array field to store phone numbers for each customer. Implement a secondary index on the Array field for efficient querying.
- [x] IV. Establish a "Customers" parent table and a nested "Phones" child table. Interleave the "Phones" table into the "Customers" table and create an index on the phone number field in the "Phones" table for optimized search operations.

### Explanation

**Given the requirement to efficiently search customers by phone number in a Cloud Spanner customer database, the most suitable schema design would be:**

**IV. Establish a "Customers" parent table and a nested "Phones" child table. Interleave the "Phones" table into the "Customers" table and create an index on the phone number field in the "Phones" table for optimized search operations.**

**Explanation:**

I. Design a "Customers" table featuring an Array field to accommodate multiple phone numbers per customer:

  * While using an Array field might allow storage of multiple phone numbers per customer, it may not be efficient for searching and querying based on phone numbers, especially in large datasets.

II. Create a "Customers" table along with a separate "Phones" table. Include a "CustomerId" field in the "Phones" table to associate phone numbers with customers:

  * This approach introduces additional complexity with a separate table and a foreign key relationship. While it allows for better organization, it may not be the most efficient for querying customers by phone number.

III. Set up a "Customers" table with an Array field to store phone numbers for each customer. Implement a secondary index on the Array field for efficient querying:

  * While using an Array field with a secondary index may improve query performance compared to option I, it may still not provide optimal performance for searching by phone number, especially in large datasets.

**IV. Establish a "Customers" parent table and a nested "Phones" child table. Interleave the "Phones" table into the "Customers" table and create an index on the phone number field in the "Phones" table for optimized search operations:**

  * **Interleaving the "Phones" table into the "Customers" table allows for co-location of related data, improving query performance. Creating an index on the phone number field in the "Phones" table further enhances search efficiency, making it the most suitable option for efficient customer search by phone number.**

**Therefore, option IV is the most appropriate schema design for efficient customer search by phone number in a Cloud Spanner database.**

**Reference:**

<https://cloud.google.com/spanner/docs/schema-design#creating-indexes:>

---

## Question 31

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You've recently developed a web application to daily transfer log data to a Cloud Storage bucket. Authenticated users will regularly review logs from the prior two weeks for critical events, while logs will be annually reviewed by an external auditor thereafter. Data retention is required for a minimum of 7 years. To propose a cost-effective storage solution meeting these needs,**

**what should you do? (Choose two.)**

- [ ] III. Generate a JSON Web Token (JWT) for users requiring access to the Coldline storage buckets.
- [ ] I. Apply the Bucket Lock feature to enforce a retention policy on the data.
- [ ] V. Configure a lifecycle management policy to transition objects older than 14 days to the Nearline storage class.
- [x] IV. Establish a lifecycle management policy to transition objects older than 14 days to the Coldline storage class.
- [x] II. Schedule a job to transition objects older than 14 days to the Coldline storage class.

### Explanation

**Correct Answers:**

  * **II. Schedule a job to transition objects older than 14 days to the Coldline storage class.**

  * **IV. Establish a lifecycle management policy to transition objects older than 14 days to the Coldline storage class.**

**Justification:**

  * **Tiered Storage:** Both approaches leverage Cloud Storage's different storage classes. Since recent logs (<= 14 days) are accessed frequently, keeping them on Standard storage makes sense. Older logs can safely transition to the less expensive Coldline storage class.

  * **Automation:** While scheduling a job is possible, lifecycle management policies provide a more declarative and automated way to enforce the storage tiering.

  * **Data Retention:** Neither of these solutions directly address the 7-year retention requirement. That could be handled with Object Lifecycle Management (e.g., deleting after 7 years) or Bucket Lock.

**Why Other Options Are Less Ideal:**

  * **I. Apply the Bucket Lock feature to enforce a retention policy on the data.**

    * **Cost:** Bucket Lock is designed for legal holds and compliance, not primarily for cost optimization. It can become expensive for large datasets with long retention periods.

  * **III. Generate a JSON Web Token (JWT) for users requiring access to the Coldline storage buckets.**

    * **Relevance:** JWTs are for authentication, not directly related to cost optimization of storage.

  * **V. Configure a lifecycle management policy to transition objects older than 14 days to the Nearline storage class.**

    * **Cost:** Nearline, while less expensive than Standard, is still more costly than Coldline for infrequently accessed data.

**References** :  
[https://cloud.google.com/storage/docs/bucket-lock ](https://cloud.google.com/storage/docs/bucket-lock   https://cloud.google.com/storage/docs/lifecycle)

[https://cloud.google.com/storage/docs/lifecycle](https://cloud.google.com/storage/docs/bucket-lock   https://cloud.google.com/storage/docs/lifecycle)

---

## Question 32

*Domain 3: Configuring and Deploying Applications*

**How should you design a study to determine whether a new color scheme for a global ecommerce web application hosted on Cloud Run will increase sales, utilizing live production traffic?**

- [ ] III. Utilize an external HTTP(S) load balancer to mirror traffic to the new version of the application with the updated color scheme. Analyze the results to determine whether there is a statistically significant difference in sales.
- [ ] II. Utilize an external HTTP(S) load balancer to direct traffic to the original color scheme while creating and testing the new deployment. Upon completion of testing, switch all traffic to the new color scheme. Analyze the results to evaluate any statistically significant difference in sales.
- [x] I. Utilize an external HTTP(S) load balancer to split a predetermined percentage of traffic between two different color schemes of the application. Analyze the results to assess any statistically significant difference in sales.
- [ ] IV. Implement a feature flag to display the new color scheme to half of all users. Monitor sales for this group to assess whether there is an increase.

### Explanation

**I. Option I: Utilize an external HTTP(S) load balancer to split a predetermined percentage of traffic between two different color schemes of the application. Analyze the results to assess any statistically significant difference in sales.**

  * **Feedback: This option effectively implements A/B testing, allowing for a controlled comparison between the original and new color schemes. By splitting traffic, it enables the assessment of any impact on sales without disrupting the user experience for all users.**

  * **Justification for selection: A/B testing is a widely used method for evaluating changes in web applications, as it provides clear insights into the effectiveness of variations. By directing a portion of the traffic to the new color scheme, it allows for a direct comparison with the original scheme, facilitating analysis of any differences in sales.**

II. Utilize an external HTTP(S) load balancer to direct traffic to the original color scheme while creating and testing the new deployment. Upon completion of testing, switch all traffic to the new color scheme. Analyze the results to evaluate any statistically significant difference in sales.

  * Feedback: This option involves a phased rollout approach, which may not provide immediate insights into the impact on sales. While it minimizes risk by initially testing the new color scheme on a subset of traffic, it delays the assessment of its effectiveness until after full deployment.

  * Justification for not selecting: This approach might not be suitable for immediate evaluation of the new color scheme's impact on sales, as it delays the comparison between the original and new schemes until after full deployment. It's generally preferable to conduct A/B testing to directly compare performance variations.

III. Utilize an external HTTP(S) load balancer to mirror traffic to the new version of the application with the updated color scheme. Analyze the results to determine whether there is a statistically significant difference in sales.

  * Feedback: While mirroring traffic allows for observation of user behavior without affecting their experience, it doesn't directly compare the performance of the two versions. This approach might not provide clear insights into the impact of the new color scheme on sales.

  * Justification for not selecting: Without a direct comparison between the original and new color schemes, it may be challenging to determine whether any observed differences in sales are attributable to the color scheme change or other factors.

IV. Implement a feature flag to display the new color scheme to half of all users. Monitor sales for this group to assess whether there is an increase.

  * Feedback: Implementing a feature flag allows for random assignment of users to different groups, enabling evaluation of the new color scheme's impact on sales. However, this approach doesn't split traffic evenly and may not provide a clear comparison between the two versions.

  * Justification for not selecting: While feature flags can be useful for experimentation, they may not provide as controlled an environment for comparison as A/B testing. Randomly assigning users to different groups might not result in an even distribution of traffic between the original and new color schemes, potentially biasing the results.

**In summary, while all options present different approaches for evaluating the impact of the new color scheme on sales, Option I (utilizing A/B testing with an external HTTP(S) load balancer) provides the most direct and controlled comparison between the original and new schemes, making it the preferred choice for determining the effectiveness of the color scheme change.**

**References:**

[https://cloud.google.com/load-balancing/docs/l7-internal/traffic-management#traffic_actions_weight-based_traffic_splitting](https://cloud.google.com/load-balancing/docs/l7-internal/traffic-management#traffic_actions_weight-based_traffic_splitting  https://cloud.google.com/load-balancing/docs/https/setting-up-https-serverless)

[https://cloud.google.com/load-balancing/docs/https/setting-up-https-serverless](https://cloud.google.com/load-balancing/docs/l7-internal/traffic-management#traffic_actions_weight-based_traffic_splitting  https://cloud.google.com/load-balancing/docs/https/setting-up-https-serverless)

---

## Question 33

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**In your application, users can read and post comments on news articles, and you're configuring Firestore to manage this. How should you structure the schema to handle an unspecified number of comments and articles?**

- [ ] III. Store each comment as a document and include its key in an array property associated with the article.
- [ ] IV. Store each comment as a document and include its key in an array property within the user profile.
- [ ] II. Place each comment within an array property linked to the article.
- [x] I. Save each comment under a subcollection related to the article.

### Explanation

**I. Save each comment under a subcollection related to the article.**

This is the most efficient and scalable approach for these reasons:

  * **Unlimited Comments:** Subcollections provide a way to store an unbounded number of comments associated with each article while maintaining a clear relationship.

  * **Efficient Retrieval:** Firestore is optimized for retrieving subcollections, allowing you to easily fetch all comments for a specific article.

  * **Scalability:** This design distributes the load across multiple documents, avoiding potential bottlenecks as the number of comments grows.

**Why Other Options Are Less Ideal:**

  * **II. Array Property on Article:** Arrays in Firestore have limitations on size and write operations. This could become a scaling issue as the number of comments increases, and could lead to hot-spotting where one document is frequently updated.

  * **III. Array on Article with Comment IDs** Storing just the comment IDs on the article introduces additional fetch operations and potential consistency concerns if comments are modified or deleted.

  * **IV. Array on User Profile:** This design makes it difficult to efficiently retrieve comments related to a specific article.

**References:**  
[https://firebase.google.com/docs/firestore/data-model#subcollections](https://firebase.google.com/docs/firestore/data-model#subcollections  https://firebase.google.com/docs/firestore/best-practices#high_read_write_and_delete_rates_to_a_narrow_document_range)

[https://firebase.google.com/docs/firestore/best-practices#high_read_write_and_delete_rates_to_a_narrow_document_range](https://firebase.google.com/docs/firestore/data-model#subcollections  https://firebase.google.com/docs/firestore/best-practices#high_read_write_and_delete_rates_to_a_narrow_document_range)

---

## Question 34

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You're tasked with constructing an API for Android and iOS apps, with the following prerequisites:**

**HTTPS support is essential**

**Bandwidth usage should be minimized**

**Seamless integration with mobile apps is a priority**

**Which API architecture is the most appropriate choice for meeting these criteria?**

- [ ] II. MQTT for APIs
- [ ] IV. SOAP-based APIs
- [ ] I. RESTful APIs
- [x] III. gRPC-based APIs

### Explanation

**Given the prerequisites of HTTPS support, minimized bandwidth usage, and seamless integration with mobile apps, the most appropriate choice for API architecture would be:**

**III. gRPC-based APIs**

**Explanation:**

I. RESTful APIs:

  * While RESTful APIs are widely used and support HTTPS, they typically use JSON or XML for data serialization, which may not be as efficient in terms of bandwidth usage compared to other options like gRPC.

II. MQTT for APIs:

  * MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol designed for IoT devices with low bandwidth and high latency. While it's efficient in terms of bandwidth usage, it may not be the best choice for general-purpose APIs used in mobile apps, especially when seamless integration and support for HTTPS are essential.

**III. gRPC-based APIs:**

  * **gRPC is a modern, high-performance RPC (Remote Procedure Call) framework developed by Google. It uses HTTP/2 for transport, which supports HTTPS by default. gRPC offers efficient binary serialization using Protocol Buffers, resulting in minimized bandwidth usage compared to textual formats like JSON or XML. Additionally, gRPC provides seamless integration with mobile platforms through generated client libraries, making it a suitable choice for Android and iOS apps.**

IV. SOAP-based APIs:

  * SOAP (Simple Object Access Protocol) is an older, XML-based protocol for exchanging structured information in the implementation of web services. While SOAP can support HTTPS, it's generally considered more heavyweight and complex compared to other options like RESTful or gRPC-based APIs. SOAP may not be the best fit for mobile app development due to its complexity and overhead.

**Therefore, option III, gRPC-based APIs, aligns well with the given prerequisites, providing HTTPS support, minimizing bandwidth usage with efficient binary serialization, and offering seamless integration with mobile apps.**

Ref:

[https://www.imaginarycloud.com/blog/grpc-vs-rest/](https://www.imaginarycloud.com/blog/grpc-vs-rest/  https://cloud.google.com/blog/products/api-management/understanding-grpc-openapi-and-rest-and-when-to-use-them)

[https://cloud.google.com/blog/products/api-management/understanding-grpc-openapi-and-rest-and-when-to-use-them](https://www.imaginarycloud.com/blog/grpc-vs-rest/  https://cloud.google.com/blog/products/api-management/understanding-grpc-openapi-and-rest-and-when-to-use-them)

---

## Question 35

*Domain 3: Configuring and Deploying Applications*

**You need to transfer the directory "local-scripts" and all its contents from your local workstation to a Compute Engine virtual machine instance. Which command should you use?**

- [ ] IV. `**gcloud compute mv --project my-gcp-project --recurse ~/local-scripts/ gcp-instance-name:~/server-scripts/ --zone us-east1-b**`
- [x] III. `**gcloud compute scp --project my-gcp-project --recurse ~/local-scripts/ gcp-instance-name:~/server-scripts/ --zone us-east1-b**`
- [ ] II. `**gsutil cp --project my-gcp-project -R ~/local-scripts/ gcp-instance-name:~/server-scripts/ --zone us-east1-b**`
- [ ] I. `**gsutil cp --project my-gcp-project -r ~/local-scripts/ gcp-instance-name:~/server-scripts/ --zone us-east1-b**`

### Explanation

**III. gcloud compute scp --project my-gcp-project --recurse ~/local-scripts/ gcp-instance-name:~/server-scripts/ --zone us-east1-b**

**Explanation:**

  * **gcloud compute scp:** This is the appropriate tool for secure file transfers between local machines and Compute Engine instances.

  * **\--project my-gcp-project:** Specifies your Google Cloud Project for authentication.

  * **\--recurse:** This flag is essential since you want to copy the entire directory, including its contents.

  * **~/local-scripts/** : The source path on your local machine.

  * **gcp-instance-name:~/server-scripts/** : The destination path on the Compute Engine instance (make sure to replace 'gcp-instance-name' with your actual instance's name).

  * **\--zone us-east1-b:** Specifies the zone of your Compute Engine instance.

**Why Other Options Are Incorrect:**

  * **I & II. gsutil cp...** The `gsutil` command is primarily for interacting with Google Cloud Storage buckets, not direct file transfers to Compute Engine instances. While there are ways to make it work, it's less straightforward than using `gcloud compute scp`.

  * **IV. gcloud compute mv ...** The `mv` command is for moving or renaming files, not copying them across machines.

---

## Question 36

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**To expand its user base globally for a popular application, your company seeks to ensure 99.999% availability of the database while minimizing read latency for users worldwide. Which two actions should the company prioritize? (Select two.)**

- [ ] V. Create at least two Cloud Spanner instances in separate regions, each with a minimum of one node.
- [x] III. Establish a cluster comprising a minimum of 3 Spanner nodes.
- [ ] VI. Develop a Cloud Dataflow pipeline for data replication across diverse databases.
- [x] I. Deploy a multi-regional Cloud Spanner instance configured with "nam-asia-eur1".
- [ ] IV. Set up a cluster with at least 1 Spanner node.
- [ ] II. Implement a multi-regional Cloud Spanner instance with the "nam3" configuration.

### Explanation

**To achieve 99.999% availability of the database while minimizing read latency for users worldwide, the company should prioritize options that enhance both availability and latency. The most suitable actions would be:**

**I. Deploy a multi-regional Cloud Spanner instance configured with "nam-asia-eur1."**

  * **This option involves deploying Cloud Spanner in a multi-regional configuration spanning across regions in North America, Asia, and Europe. Multi-regional setups enhance availability by distributing data across multiple geographic regions, reducing the risk of downtime due to regional failures. Additionally, by choosing a configuration that includes regions from multiple continents, the company can minimize read latency for users worldwide by locating data closer to users, thereby improving overall performance.**

**III. Establish a cluster comprising a minimum of 3 Spanner nodes.**

  * **Having a cluster with multiple nodes improves database availability and fault tolerance. With a minimum of 3 Spanner nodes, the system can maintain availability even if one node fails. This redundancy ensures that the database remains accessible and operational, contributing to the goal of achieving 99.999% availability.**

Options II, IV, V, and VI are not the optimal choices for achieving the stated objectives:

II. Implement a multi-regional Cloud Spanner instance with the "nam3" configuration.

  * "nam3" configuration refers to a regional instance in North America, which may not provide the desired global availability and latency improvements compared to a multi-regional configuration.

IV. Set up a cluster with at least 1 Spanner node.

  * While having at least one node is necessary, it doesn't address the need for redundancy and fault tolerance provided by a cluster with multiple nodes.

V. Create at least two Cloud Spanner instances in separate regions, each with a minimum of one node.

  * While this option provides some redundancy by having multiple instances in separate regions, it doesn't offer the same level of fault tolerance and global availability as a multi-regional instance.

VI. Develop a Cloud Dataflow pipeline for data replication across diverse databases.

  * While data replication is essential for disaster recovery and ensuring data availability, it doesn't directly address the goal of minimizing read latency for users worldwide or achieving 99.999% availability of the database.

**Therefore, options I and III should be prioritized to achieve the company's objectives.**

**Reference:**

<https://cloud.google.com/spanner/docs/instances#configs-multi-region#>

---

## Question 37

*Domain 4: Integrating Applications with Google Cloud Services*

**As a developer within a large organization, you manage an application written in Go deployed on a production Google Kubernetes Engine (GKE) cluster. You're tasked with implementing a new feature that requires access to BigQuery. Your objective is to grant BigQuery access to your GKE cluster, adhering to Google's recommended best practices. How should you proceed?**

- [ ] III. Generate a Google service account with BigQuery access, store the Google service account JSON key in Secret Manager, and implement an init container to retrieve the secret for the application's usage.
- [x] IV. Establish both a Google service account and a Kubernetes service account, enable Workload Identity on the GKE cluster, and specify the Kubernetes service account within the application Deployment configuration.
- [ ] I. Generate a Google service account with BigQuery access, store the associated JSON key securely in Secret Manager, and utilize the Go client library to access the JSON key.
- [ ] II. Generate a Google service account with BigQuery access, incorporate the Google service account JSON key into a Kubernetes secret, and configure the application to utilize this secret.

### Explanation

The best answer is

**IV: Establish both a Google service account and a Kubernetes service account, enable Workload Identity on the GKE cluster, and specify the Kubernetes service account within the application Deployment configuration.**

Here's why this approach aligns with Google's best practices:

  * **Workload Identity:** This is the most secure and recommended way to manage service account credentials within GKE. It eliminates the need to handle service account keys directly within your pods, reducing the risk of exposing them.

  * **Principle of Least Privilege:** Assign the necessary BigQuery permissions only to the Google service account, ensuring that it can't access resources other than those required for the application.

**Why other options are less ideal:**

  * **I, II, and III:** All involve direct handling and storage of service account keys either in secrets or an init container. While functional, this increases the potential attack surface if those keys are compromised.

**References:**

<https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#what_is>

---

## Question 38

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You are deploying your application on a Compute Engine instance, which needs to communicate with Cloud SQL. To ensure minimal access for the role assigned to the service account associated with the instance, following Google's best practices, what action should you take?**

- [x] III. Assign the Cloud SQL Client role.
- [ ] II. Designate the Project Owner role.
- [ ] IV. Grant the Cloud SQL Editor role.
- [ ] I. Allocate the Project Editor role.

### Explanation

**III. Assign the Cloud SQL Client role.**

Here's why:

  * **Least Privilege:** The Cloud SQL Client role is specifically designed to provide the necessary permissions for connecting to a Cloud SQL database and performing basic operations like reading and writing data. It avoids granting excessive permissions that could be misused.

  * **Security Best Practice:** Google explicitly recommends using the Cloud SQL Client role for this use case to minimize risks.

**Why other options are not suitable:**

  * **I. Project Editor ** and **II. Project Owner:** These roles grant broad permissions across the entire project, significantly violating the principle of least privilege and creating unnecessary security risks.

  * **IV. Cloud SQL Editor:** This role includes the ability to create, modify, and delete databases, which is far more powerful than what your application likely needs.

**References:**

[https://cloud.google.com/sql/docs/mysql/roles-and-permissions](https://cloud.google.com/sql/docs/mysql/roles-and-permissions  https://cloud.google.com/sql/docs/mysql/roles-and-permissions#proxy-roles-permissions)

[https://cloud.google.com/sql/docs/mysql/roles-and-permissions#proxy-roles-permissions](https://cloud.google.com/sql/docs/mysql/roles-and-permissions  https://cloud.google.com/sql/docs/mysql/roles-and-permissions#proxy-roles-permissions)

---

## Question 39

*Domain 3: Configuring and Deploying Applications*

**You've transitioned an on-premises monolithic application to a microservices setup on Google Kubernetes Engine (GKE), with backend dependencies such as a CRM system and a MySQL database containing PII residing on-premises for regulatory compliance. Despite establishing a Cloud VPN connection between your on-premises data center and Google Cloud, you're encountering latency-related crashes due to fluctuating bandwidth. How should you tackle these latency issues?**

- [ ] I. Implement Memorystore to cache frequently accessed PII data from the on-premises MySQL database
- [x] III. Scale up the number of Cloud VPN tunnels for the connection between Google Cloud and the on-premises services
- [ ] IV. Reduce network layer packet size by adjusting the Maximum Transmission Unit (MTU) value from its default setting on Cloud VPN
- [ ] II. Utilize Istio to establish a service mesh encompassing the microservices on GKE and the on-premises services

### Explanation

**III. Scale up the number of Cloud VPN tunnels for the connection between Google Cloud and the on-premises services.**

**Explanation:**

  1. **Scaling Cloud VPN Tunnels: Increasing the number of Cloud VPN tunnels can help distribute the network traffic between your on-premises data center and Google Cloud, thus potentially mitigating the impact of fluctuating bandwidth and reducing latency-related crashes. This approach can provide additional bandwidth and redundancy, improving the stability and reliability of the connection.**

Options I, II, and IV are less likely to directly address the latency issues caused by fluctuating bandwidth:

I. Implementing Memorystore to cache frequently accessed PII data from the on-premises MySQL database might improve performance by reducing the need to access the database frequently, but it may not directly address the latency issues caused by fluctuating bandwidth between the on-premises data center and Google Cloud.

II. Utilizing Istio to establish a service mesh can help manage and secure communication between microservices, but it may not directly alleviate the latency issues arising from the fluctuating bandwidth between on-premises services and microservices on GKE.

IV. Adjusting the Maximum Transmission Unit (MTU) value on Cloud VPN could potentially optimize network performance, but it may not be as effective in addressing latency issues caused by fluctuating bandwidth compared to scaling up the number of VPN tunnels. Additionally, adjusting MTU values requires careful consideration and testing to avoid introducing compatibility or performance issues.

**Hint:**

[https://cloud.google.com/network-connectivity/docs/vpn/concepts/topologies#more-bandwidth](https://cloud.google.com/network-connectivity/docs/vpn/concepts/topologies#more-bandwidth  https://cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#route-alignment)

[https://cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#route-alignment](https://cloud.google.com/network-connectivity/docs/vpn/concepts/topologies#more-bandwidth  https://cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#route-alignment)

---

## Question 40

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Your existing application manages user state data in a single MySQL database. This data is intensely user-specific and intricately tied to user activity duration. However, maintaining and evolving the schema for diverse user requirements in the MySQL database is proving challenging. Which storage option is the optimal choice in this situation?**

- [ ] I. Cloud SQL
- [x] IV. Cloud Datastore/Firestore
- [ ] III. Cloud Spanner
- [ ] II. Cloud Storage

### Explanation

**IV. Cloud Datastore/Firestore (Firestore in document mode)**

Here's why it's particularly well-suited to this situation:

  * **Schema Flexibility:** Firestore's document model allows for flexibility and variation in your data structures. Each user's document can have its own fields and nested data, accommodating changing requirements without strict schema constraints.

  * **Focus on User Data:** Firestore is designed for storing and retrieving data quickly on a per-user basis, making it a good fit for your intensely user-specific data.

  * **Scalability:** Firestore scales automatically to handle large numbers of users and data without complex management on your part.

  * **Evolving Requirements:** Firestore's flexibility allows you to add or modify fields for individual users as needed, making it easier to adapt to changing needs.

**Why Other Options Might Be Less Ideal:**

  * **Cloud SQL:** While SQL offers robust relational modeling, its schema-on-write approach might hinder your ability to rapidly adapt to evolving user-specific data structures.

  * **Cloud Storage:** Cloud Storage is great for storing objects or files, but it's not designed for structured, queryable user data with complex relationships.

  * **Cloud Spanner:** Spanner is a powerful distributed database, but its strength lies in its scalability and consistency across large, structured datasets. It might be overkill if the primary challenge is schema flexibility for individual user data.

**Reference:**

<https://cloud.google.com/datastore/docs/concepts/overview#what_its_good_for>

---

## Question 41

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**In the process of auditing all deployed applications in Google Kubernetes Engine, your security team found that some applications transmit data within the cluster in plain text. How can you swiftly encrypt all application traffic, minimizing alterations to applications and ensuring Google support?**

- [ ] III. Establish Trusted Network ranges within the application, allowing traffic exclusively from these networks.
- [ ] IV. Employ an automated procedure to procure SSL Certificates for applications from Let's Encrypt and integrate them into the applications.
- [x] II. Deploy Istio, activate proxy injection in the application namespace, and then implement mutual TLS (mTLS).
- [ ] I. Implement Network Policies to restrict traffic between applications.

### Explanation

**Correct Option:**

**II. Deploy Istio, activate proxy injection in the application namespace, and then implement mutual TLS (mTLS).**

**Justification:**

  * **Istio is a service mesh explicitly engineered for managing, securing, and observing microservices-based applications.** It accomplishes this by adding sidecar proxies next to each application instance (injected automatically). These sidecars regulate the flow of traffic within the cluster.

  * **Mutual TLS offers robust encryption and identity verification for service-to-service communication.** This guarantees the confidentiality and integrity of data exchanged between applications.

  * **The use of Istio and mTLS satisfies the requirement for minimal modifications to the applications themselves.** The proxies manage encryption transparently.

  * **Istio is widely used with Kubernetes and offers robust Google support.**

**Why Other Options are Less Ideal:**

  * **I. Implement Network Policies to restrict traffic between applications.** Network policies offer traffic control mechanisms. But they neither encrypt data nor address the clear mandate of encrypting application traffic.

  * **III. Establish Trusted Network ranges within the application, allowing traffic exclusively from these networks.** This strategy concentrates on access control and relies on the initial trustworthiness of those "trusted" networks. It doesn't inherent encrypt traffic in transit.

  * **IV. Employ an automated procedure to procure SSL Certificates for applications from Let's Encrypt and integrate them into the applications.** While this improves web traffic security, it presents several challenges:

    * It requires significant modifications to applications to incorporate those certificates.

    * It doesn't address other communication protocols within the cluster beyond standard web traffic.

**References:**

[https://cloud.google.com/istio/docs/istio-on-gke/installing](https://cloud.google.com/istio/docs/istio-on-gke/installing  https://cloud.google.com/istio/docs/istio-on-gke/overview Istio gives you the following benefits)

[https://cloud.google.com/istio/docs/istio-on-gke/overview Istio gives you the following benefits](https://cloud.google.com/istio/docs/istio-on-gke/installing  https://cloud.google.com/istio/docs/istio-on-gke/overview Istio gives you the following benefits)

---

## Question 42

*Domain 4: Integrating Applications with Google Cloud Services*

**As a developer working on an internal payroll processing application, you're tasked with implementing a component for timesheet submission, triggering various independent steps. Which approach should you take to ensure effective communication with downstream systems and accommodate future step additions?**

- [ ] IV. Develop a timesheet microservice deployed on Google Kubernetes Engine, orchestrating calls to each downstream step and awaiting successful responses before proceeding.
- [x] III. Set up a Pub/Sub topic dedicated to timesheet submissions, with subscriptions created for each downstream team to receive notifications.
- [ ] II. Establish separate Pub/Sub topics for each step, with subscriptions tailored for downstream development teams to subscribe to their specific step.
- [ ] I. Implement individual Cloud Functions for each step, enabling direct calls to respective downstream systems.

### Explanation

**III. Set up a Pub/Sub topic dedicated to timesheet submissions, with subscriptions created for each downstream team to receive notifications.**

Here's why this approach excels:

  * **Loose Coupling:** Pub/Sub promotes a decoupled architecture. The timesheet submission component simply publishes an event; downstream systems subscribe without tight dependencies.

  * **Scalability:** New steps can be easily added by creating additional subscriptions, without needing to modify the core timesheet submission logic.

  * **Reliability:** Pub/Sub provides durable messaging, helping handle temporary issues with downstream systems.

  * **Future-Proof:** This architecture aligns with event-driven patterns, accommodating changing requirements gracefully.

---

## Question 43

*Domain 3: Configuring and Deploying Applications*

**As you deploy your applications on Compute Engine, you face a failure to launch one of your Compute Engine instances. What steps should you take? (Select two.)**

- [ ] III. Investigate firewall rules or routes on the instance.
- [ ] V. Review whether network traffic to or from your instance is being dropped.
- [x] IV. Check if your instance's boot disk is completely full.
- [ ] II. Try accessing Compute Engine using an alternative SSH user.
- [x] I. Evaluate whether your file system is corrupted.

### Explanation

* **IV. Check if your instance's boot disk is completely full.** A full boot disk can prevent the operating system from loading, hindering the startup process.

  * **I. Evaluate whether your file system is corrupted.** File system corruption on the boot disk can also cause startup issues.

Here's why the other options are less important initially:

  * **II. Try accessing Compute Engine using an alternative SSH user.** This assumes the instance has at least booted, allowing for SSH access. It's helpful for later-stage troubleshooting, not when the instance won't launch at all.

  * **III. Investigate firewall rules or routes on the instance.** Similar to the previous point, this assumes the instance has some level of functionality, whereas firewall issues are unlikely to prevent initial startup entirely.

  * **V. Review whether network traffic to or from your instance is being dropped.** Network connectivity issues, while possible, are less likely to be the sole cause of a complete launch failure.

**References:**

<https://cloud.google.com/compute/docs/troubleshooting/vm-startup#identify_the_reason_why_the_boot_disk_isnt_booting>

---

## Question 44

*Domain 3: Configuring and Deploying Applications*

**As a developer at a large organization deploying a web application to Google Kubernetes Engine (GKE), you're tasked with configuring a CI/CD pipeline using Cloud Deploy. The pipeline should deploy the application to Dev, Test, and Prod clusters in GKE. Following Google-recommended best practices, how should you configure the process to automatically promote the application from the Dev to the Test cluster after a successful deployment?**

- [ ] IV. Establish a Cloud Build pipeline utilizing the gke-deploy builder. Create a Cloud Build trigger to monitor SUCCEEDED Pub/Sub messages from the cloud-builds topic. Configure this pipeline to execute a deployment step to the Test cluster.
- [ ] II. Develop a Cloud Function to call the Google Cloud Deploy API for promoting the application to the Test cluster. Configure this function to be triggered by SUCCEEDED Pub/Sub messages from the cloud-builds topic.
- [x] III. Create a Cloud Function to invoke the Google Cloud Deploy API for promoting the application to the Test cluster. Configure this function to be triggered by SUCCEEDED Pub/Sub messages from the clouddeploy-operations topic.
- [ ] I. Set up a Cloud Build trigger to monitor SUCCEEDED Pub/Sub messages from the clouddeploy-operations topic. Configure Cloud Build to include a step for promoting the application to the Test cluster.

### Explanation

**Correct Answer:**

  * **III. Create a Cloud Function to invoke the Google Cloud Deploy API for promoting the application to the Test cluster. Configure this function to be triggered by SUCCEEDED Pub/Sub messages from the clouddeploy-operations topic.**

**Justification:**

  * **Automation & Integration:** Cloud Deploy emits events to a Pub/Sub topic (`clouddeploy-operations`) when deployment operations succeed or fail. A Cloud Function directly subscribing to this topic provides a clean, event-driven promotion mechanism.

  * **API Directness:** Utilizing the Google Cloud Deploy API within the Cloud Function ensures you're directly controlling the promotion step and adhering to Google's prescribed practices.

  * **Flexibility:** Cloud Functions provide flexibility if you need additional logic or customization around the promotion process.

**Why Other Options Are Less Ideal:**

  * **I. Set up a Cloud Build trigger to monitor SUCCEEDED Pub/Sub messages...**

    * **Scope:** While Cloud Build is excellent for CI/CD pipelines, it's not the primary tool for managing promotions within Cloud Deploy. Using a Cloud Function aligns better with Cloud Deploy's native mechanisms.

  * **II. ... Configure this function to be triggered by SUCCEEDED Pub/Sub messages from the cloud-builds topic.**

    * **Topic Mismatch:** The `cloud-builds` topic is related to build events, not Cloud Deploy's deployment lifecycle events.

  * **IV. Establish a Cloud Build pipeline utilizing the gke-deploy builder ...**

    * **Separation of Concerns:** While Cloud Build is suitable for the initial deployment steps, it's cleaner to use Cloud Deploy's native eventing and API for managing promotions between environments.

**References:**  
[https://cloud.google.com/functions/docs/calling/pubsub https://cloud.google.com/deploy/docs/integrating#integrating_with_automated_testing](https://cloud.google.com/functions/docs/calling/pubsub   https://cloud.google.com/deploy/docs/integrating#integrating_with_automated_testing  https://cloud.google.com/build/docs/automate-builds-pubsub-events#console_2  https://cloud.google.com/deploy/docs/integrating#before_you_begin)

[https://cloud.google.com/build/docs/automate-builds-pubsub-events#console_2](https://cloud.google.com/functions/docs/calling/pubsub   https://cloud.google.com/deploy/docs/integrating#integrating_with_automated_testing  https://cloud.google.com/build/docs/automate-builds-pubsub-events#console_2  https://cloud.google.com/deploy/docs/integrating#before_you_begin)

[https://cloud.google.com/deploy/docs/integrating#before_you_begin](https://cloud.google.com/functions/docs/calling/pubsub   https://cloud.google.com/deploy/docs/integrating#integrating_with_automated_testing  https://cloud.google.com/build/docs/automate-builds-pubsub-events#console_2  https://cloud.google.com/deploy/docs/integrating#before_you_begin)

---

## Question 45

*Domain 3: Configuring and Deploying Applications*

**As the manager responsible for your company's ecommerce platform payment system on Google Cloud, you're mandated to retain user logs for specific durations. Logs must be kept for 1 year for internal audits and for 3 years to meet compliance standards. To reduce on-premises storage usage and ensure efficient searchability, what's the optimal method for storing new user logs on Google Cloud with minimal effort while ensuring correct storage?**

- [ ] I. Store logs in a Cloud Storage bucket with bucket locking enabled.
- [ ] II. Store logs in a Cloud Storage bucket with a 3-year retention period.
- [x] III. Employ Cloud Logging to store logs as customized logs with a tailored retention duration.
- [ ] IV. Initially store logs in a Cloud Storage bucket with a 1-year retention period. After 1 year, transfer logs to another bucket with a 2-year retention period.

### Explanation

**The optimal method for storing new user logs on Google Cloud with minimal effort while ensuring correct storage is option III:**

**III. Employ Cloud Logging to store logs as customized logs with a tailored retention duration.**

**Explanation:**

  1. **Cloud Logging (formerly Stackdriver Logging)** : Cloud Logging is a fully managed service by Google Cloud Platform for collecting, viewing, and analyzing logs from applications and services. It offers customizable retention periods, making it an ideal solution for meeting specific compliance requirements.

  2. **Customized retention duration** : With Cloud Logging, you can set retention periods tailored to your specific needs. In this scenario, you can set a retention period of 1 year for internal audits and 3 years to meet compliance standards.

Options I, II, and IV do not fully address the requirements and may introduce unnecessary complexity:

I. Storing logs in a Cloud Storage bucket with bucket locking enabled can prevent deletion of objects but doesn't address the need for different retention periods for internal audits and compliance standards.

II. Storing logs in a Cloud Storage bucket with a fixed 3-year retention period doesn't meet the requirement of retaining logs for 1 year for internal audits.

IV. Initially storing logs in a Cloud Storage bucket with a 1-year retention period and then transferring logs to another bucket with a 2-year retention period after 1 year adds unnecessary complexity and management overhead. Using Cloud Logging with customized retention durations is a more straightforward solution.

**References:**  
[https://cloud.google.com/logging/docs/buckets#custom-retention](https://cloud.google.com/logging/docs/buckets#custom-retention  https://cloud.google.com/logging/docs/central-log-storage)

[https://cloud.google.com/logging/docs/central-log-storage](https://cloud.google.com/logging/docs/buckets#custom-retention  https://cloud.google.com/logging/docs/central-log-storage)

---

## Question 46

*Domain 4: Integrating Applications with Google Cloud Services*

**You are utilizing Cloud Run to host a web application and require a secure method to retrieve and display the application's project ID and region to users. Your goal is to implement the most performant approach. What action should you take?**

- [ ] II. Access the Google Cloud console, navigate to the Project Dashboard to collect configuration details, and then proceed to the Cloud Run "Variables & Secrets" tab to add the desired environment variables in Key:Value format.
- [x] I. Utilize HTTP requests to query the metadata server available at the `**http://metadata.google.internal/**` endpoint with the `**Metadata-Flavor: Google**` header.
- [ ] IV. Make an API call to the Cloud Asset Inventory API from the application, formatting the request to include instance metadata.
- [ ] III. Access the Google Cloud console, navigate to the Project Dashboard to collect configuration details, and write the application configuration information to Cloud Run's in-memory container filesystem.

### Explanation

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

---

## Question 47

*Domain 3: Configuring and Deploying Applications*

**In developing an application comprising various internal microservices on Google Kubernetes Engine (GKE), you seek the ability to configure each microservice with a distinct number of replicas. Additionally, you aim for a uniform approach to address any microservice from another, irrespective of the microservice's scaling. How should you implement this solution?**

- [ ] III. Deploy each microservice as a Pod, exposing it within the cluster via a Service. Employ the Service DNS name for microservice-to-microservice interaction.
- [x] I. Deploy each microservice as a Deployment, exposing it within the cluster via a Service. Utilize the Service DNS name for inter-microservice communication.
- [ ] IV. Deploy each microservice as a Pod, exposing it within the cluster via an Ingress. Utilize the Ingress IP address for communication between microservices.
- [ ] II. Deploy each microservice as a Deployment, exposing it within the cluster via an Ingress. Utilize the Ingress IP address for communication between microservices.

### Explanation

**I. Deploy each microservice as a Deployment, exposing it within the cluster via a Service. Utilize the Service DNS name for inter-microservice communication.**

Here's why this approach excels:

  * **Scaling Flexibility:** Deployments allow you to easily control the number of replicas for each microservice, providing granular scaling to match workload demands.

  * **Reliability:** Services provide stable, internal DNS names that remain consistent even if the underlying Pods are rescheduled or replaced.

  * **Abstraction:** Using Service DNS names abstracts away the details of individual Pods, making it simpler to reason about inter-microservice communication within the cluster.

  * **Kubernetes-Native:** This approach aligns with standard Kubernetes practices for deploying and exposing microservices.

**Why Other Options Are Less Ideal:**

  * **II. Deploy each microservice as a Deployment, exposing it within the cluster via an Ingress. Utilize the Ingress IP address for communication between microservices.**

    * Ingresses are primarily designed for external traffic entering the cluster. While technically possible, it's less efficient for internal service-to-service communication.

  * **III. Deploy each microservice as a Pod, exposing it within the cluster via a Service. Employ the Service DNS name for microservice-to-microservice interaction.**

    * Pods are ephemeral; they can be created and destroyed frequently. Deployments provide a higher-level abstraction and management capabilities that are better suited for microservices.

  * **IV. Deploy each microservice as a Pod, exposing it within the cluster via an Ingress. Utilize the Ingress IP address for communication between microservices.**

    * This combines the drawbacks of both Pods and using Ingress for internal communication, making it the least desirable option.

---

## Question 48

*Domain 2: Building and Testing Applications*

**Your API backend operates across multiple cloud providers, and you need to analyze the network latency of your API. Which two actions should you take? (Select two.)**

- [x] I. Utilize Zipkin collector to gather data efficiently.
- [ ] V. Employ Stackdriver Profiler to identify performance bottlenecks and generate reports.
- [ ] IV. Leverage Stackdriver Debugger to analyze network latency issues.
- [ ] II. Implement Fluentd agent to collect data seamlessly.
- [x] III. Use Stackdriver Trace for generating comprehensive latency reports.

### Explanation

* **I. Utilize Zipkin collector to gather data efficiently.**

    * **Distributed Tracing:** Zipkin is designed explicitly for tracing requests across distributed systems, including those spanning multiple cloud providers. It's compatible with various frameworks and protocols.

    * **Latency Analysis:** Zipkin captures detailed timing data about each "span" within a request, crucial for network latency analysis.

  * **III. Use Stackdriver Trace for generating comprehensive latency reports.**

    * **Trace Analysis:** Stackdriver Trace ingests trace data (including from Zipkin) and provides powerful visualization and analysis tools specifically tailored to investigating latency issues.

    * **Cross-Cloud Visibility:** If parts of your backend are on GCP, Stackdriver Trace will integrate with them natively.

**Why Other Options Are Less Ideal**

  * **II. Implement Fluentd agent ...** While Fluentd is a versatile log aggregator, it's not focused on distributed tracing. It would require custom processing to extract the latency data you need.

  * **IV. Leverage Stackdriver Debugger ...** Debugger is primarily for debugging running code, not for tracing distributed request paths and measuring network time specifically.

  * **V. Employ Stackdriver Profiler ...** Profiler focuses on code-level performance issues, not end-to-end network latency.

**Reference:**

[https://cloud.google.com/trace/docs/zipkin](https://cloud.google.com/trace/docs/zipkin  https://cloud.google.com/trace/docs/zipkin#frequently_asked_questions)

[https://cloud.google.com/trace/docs/zipkin#frequently_asked_questions](https://cloud.google.com/trace/docs/zipkin  https://cloud.google.com/trace/docs/zipkin#frequently_asked_questions)

---

## Question 49

*Domain 4: Integrating Applications with Google Cloud Services*

**Your application relies on service accounts for authentication to GCP services, utilizing credentials stored on its Compute Engine virtual machine instances. You aim to securely distribute these credentials to the host instances. What's the recommended approach?**

- [ ] III. Generate a P12 file from the GCP Console post-deployment, transferring the credentials to the host instance prior to application launch.
- [x] II. Utilize the instance's service account Application Default Credentials for authentication to the necessary resources.
- [ ] IV. Embed the credential JSON file within your application's source repository, integrating it into the deployment process via CI/CD for package delivery to the instance.
- [ ] I. Implement HTTP signed URLs for secure access to the required resources.

### Explanation

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

---

## Question 50

*Domain 3: Configuring and Deploying Applications*

**After mistakenly typing a configuration error in a low-level Linux file, preventing your Compute Engine instance from booting normally, what corrective action should you take?**

- [ ] IV. Rectify the mistake by configuring and logging into the Compute Engine instance using a remote desktop client.
- [ ] I. Download the file via scp, modify it locally, and then upload the corrected version to the Compute Engine instance.
- [x] III. Correct the error by configuring and accessing the Compute Engine instance through the serial port connection.
- [ ] II. Access and modify the file directly by configuring and logging into the Compute Engine instance via SSH.

### Explanation

Here's the most effective way to resolve this issue:

**III. Correct the error by configuring and accessing the Compute Engine instance through the serial port connection.**

Here's why this is the best approach:

  * **System Can't Fully Boot:** The configuration error prevents your instance from booting normally, making traditional remote access options like SSH unavailable.

  * **Serial Port Access:** The serial port provides access even when regular boot processes fail. This lets you directly interact with the early boot stages and file system.

  * **Corrects the Root Cause:** You can diagnose and fix the configuration error in the file, addressing the issue preventing a successful boot.

**Why other options are less ideal:**

  * **I. Downloading and Uploading:** This assumes that you can still access the file system somehow, which might not be the case if the system can't boot completely.

  * **II. SSH Access:** SSH requires that the instance is booted with a functional network stack – a scenario the configuration error likely prevents.

  * **IV. Remote Desktop:** Remote desktop relies on the instance being fully booted and running a graphical interface, which is unlikely with this error.

**References:**

<https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console>

---

## Question 51

*Domain 2: Building and Testing Applications*

**Your team is responsible for crafting services operating on Google Kubernetes Engine. Storing your team's code in Cloud Source Repositories, you're aiming to swiftly pinpoint bugs in the code prior to deployment to production. Your objective is to streamline developer feedback and optimize the process through automation. What's the recommended course of action?**

- [ ] III. Leverage Spinnaker to automate the deployment of container images to the production environment.
- [ ] IV. Employ Cloud Build to automate the creation of container images from code, initiated by forked versions.
- [ ] I. Employ Spinnaker to automate the creation of container images from code, triggered by Git tags.
- [x] II. Utilize Cloud Build to automate the creation of container images from code, activated by Git tags.

### Explanation

**II. Utilize Cloud Build to automate the creation of container images from code, activated by Git tags.**

Here's why:

  * **Focus on Pre-Deployment Testing:** The goal here is to catch bugs **before** code reaches production. Cloud Build excels at automating image creation, a key part of a pre-deployment testing and validation pipeline.

  * **Git Tag Integration:** Tagging in source control often signifies a release candidate. Using Git tags to trigger Cloud Build ensures the image built reflects a potentially releasable state of your code, ideal for testing.

  * **Streamlined Workflow:** Cloud Build offers a well-integrated workflow for building container images directly from Cloud Source Repositories, promoting efficiency for developers.

Let's analyze why other options are less optimal:

  * **I. Employ Spinnaker...** Spinnaker is primarily a continuous delivery (CD) platform focused on deployment automation. While it can integrate image building tasks, its strength lies in managing deployments, not pre-deployment testing feedback.

  * **III. Leverage Spinnaker...** Again, Spinnaker's core competency is deployment, making it less ideal for the bug-identification stage that happens earlier in the pipeline.

  * **IV. Employ Cloud Build...forked versions.** Building images from forked versions could introduce inconsistencies and make it harder to track the connection between code and image for testing purposes. Using Git tags provides a more controlled and predictable workflow.

---

## Question 52

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Your application is managed by a managed instance group. You aim to distribute a large read-only dataset among all instances in the group. Your goal is to ensure swift instance startup and access to the dataset via the filesystem with minimal latency. Additionally, you seek to minimize the overall solution cost. What's the optimal approach?**

- [ ] II. Transfer the data to a Cloud Storage bucket and copy it to the boot disk of each instance using a startup script.
- [ ] I. Move the data to a Cloud Storage bucket and mount the bucket on the filesystem using Cloud Storage FUSE.
- [x] III. Migrate the data to a Compute Engine persistent disk and attach the disk in read-only mode to multiple Compute Engine virtual machine instances.
- [ ] IV. Shift the data to a Compute Engine persistent disk, create a snapshot, produce multiple disks from the snapshot, and attach each disk to its respective instance.

### Explanation

**Given the requirements of ensuring swift instance startup, minimal latency for dataset access, and minimizing overall solution cost, the optimal approach would be:**

**III. Migrate the data to a Compute Engine persistent disk and attach the disk in read-only mode to multiple Compute Engine virtual machine instances.**

**Explanation:**

I. Move the data to a Cloud Storage bucket and mount the bucket on the filesystem using Cloud Storage FUSE:

  * While Cloud Storage FUSE allows you to mount a Cloud Storage bucket as a filesystem, it may introduce latency, especially for large read-only datasets, as data needs to be fetched over the network. Additionally, there might be cost implications depending on the volume of data accessed and the number of requests made to Cloud Storage.

II. Transfer the data to a Cloud Storage bucket and copy it to the boot disk of each instance using a startup script:

  * This approach would copy the data to each instance's boot disk, potentially increasing instance startup time and leading to duplication of data across instances. Additionally, it might not be scalable or cost-effective, especially for large datasets.

**III. Migrate the data to a Compute Engine persistent disk and attach the disk in read-only mode to multiple Compute Engine virtual machine instances:**

  * **This approach allows you to store the dataset on a persistent disk, ensuring swift instance startup as the data is readily available on the disk. Attaching the disk in read-only mode ensures that multiple instances can access the dataset without risk of modification. This approach minimizes latency for dataset access and can be cost-effective, especially if the dataset is large and accessed frequently.**

IV. Shift the data to a Compute Engine persistent disk, create a snapshot, produce multiple disks from the snapshot, and attach each disk to its respective instance:

  * While this approach allows you to create multiple disks from a snapshot, it might introduce complexity and management overhead. Additionally, attaching multiple disks to instances might not be as efficient as attaching a single read-only disk to multiple instances, especially if the dataset is static and read-only.

**Therefore, option III, migrating the data to a Compute Engine persistent disk and attaching the disk in read-only mode to multiple Compute Engine virtual machine instances, is the optimal approach for meeting the requirements outlined.**

**References:**

[https://cloud.google.com/compute/docs/disks/sharing-disks-between-vms#use-multi-instances](https://cloud.google.com/compute/docs/disks/sharing-disks-between-vms#use-multi-instances  https://cloud.google.com/compute/docs/disks/gcs-buckets#mount_bucket  https://github.com/GoogleCloudPlatform/gcsfuse/)

[https://cloud.google.com/compute/docs/disks/gcs-buckets#mount_bucket](https://cloud.google.com/compute/docs/disks/sharing-disks-between-vms#use-multi-instances  https://cloud.google.com/compute/docs/disks/gcs-buckets#mount_bucket  https://github.com/GoogleCloudPlatform/gcsfuse/)

[https://github.com/GoogleCloudPlatform/gcsfuse/](https://cloud.google.com/compute/docs/disks/sharing-disks-between-vms#use-multi-instances  https://cloud.google.com/compute/docs/disks/gcs-buckets#mount_bucket  https://github.com/GoogleCloudPlatform/gcsfuse/)

---

## Question 53

*Domain 3: Configuring and Deploying Applications*

**You have a variety of packaged and internally developed applications hosted on a Linux Compute Engine instance. These applications log data as text in local files. You want these logs to be stored in Cloud Logging. What's the recommended approach?**

- [ ] III. Implement a Google-provided version of collectd on the Compute Engine instance.
- [ ] IV. Set up a cron job to transfer the log files to Cloud Storage once a day.
- [x] II. Deploy a Google-provided version of fluentd on the Compute Engine instance.
- [ ] I. Configure the files' content to be directed to the Linux Syslog daemon.

### Explanation

**II. Deploy a Google-provided version of Fluentd on the Compute Engine instance.**

Here's why this is the best option:

  * **Log Collection & Parsing:** Fluentd is a powerful open-source log collector designed specifically for this purpose. It can parse various log formats, structure data, and send it to Cloud Logging efficiently.

  * **Google Integration:** Google provides a pre-configured Fluentd agent tailored for integration with Cloud Logging. This simplifies setup and ensures compatibility.

  * **Flexibility:** Fluentd can handle not only standard text log files but also diverse log sources, providing you with room for expansion.

**Why Other Options Are Less Ideal:**

  * **I. Linux Syslog:** While Syslog could be a step, it doesn't directly forward logs to Cloud Logging. You'd need an additional tool to bridge this gap.

  * **III. Collectd:** Collectd is primarily focused on system and performance metrics, not general-purpose log collection.

  * **IV. Cron job to Cloud Storage:** This approach lacks real-time insights, adds complexity by requiring further processing for Cloud Logging, and isn't ideal for large volumes of logs.

Ref:

<https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent>

---

## Question 54

*Domain 2: Building and Testing Applications*

**In the process of adding unit tests to your application, you aim to assert that published Pub/Sub messages are processed by your subscriber in the correct order. Your priority is to ensure the unit tests are cost-effective and reliable. What approach should you take?**

- [x] IV. Utilize the Pub/Sub emulator for testing purposes.
- [ ] II. Establish a topic and subscription for each tester.
- [ ] I. Implement a mocking framework for testing.
- [ ] III. Introduce a filter by tester to the subscription.

### Explanation

Here's the breakdown of why the best option is:

**IV. Utilize the Pub/Sub emulator for testing purposes.**

Here's why this approach is the most suitable:

  * **Cost-Effectiveness:** The Pub/Sub emulator runs locally, eliminating costs associated with using the actual Google Cloud Pub/Sub service during testing.

  * **Isolation:** The emulator provides a controlled testing environment, allowing you to focus on message order verification without external interference.

  * **Control:** You can easily manipulate message order and timing in the emulator, enabling thorough testing of your subscriber's logic.

  * **Reliability:** The emulator offers a consistent and predictable environment for unit testing, enhancing test reliability.

**Why Other Options Are Less Ideal:**

  * **I. Implement a mocking framework for testing.**

    * Mocking can be useful for certain aspects of subscriber testing but may struggle to fully replicate Pub/Sub behavior and message ordering in a complex system.

  * **II. Establish a topic and subscription for each tester.**

    * This approach introduces provisioning and management overhead within the production Pub/Sub service and can become costly with a large number of testers.

  * **III. Introduce a filter by tester to the subscription.**

    * Filtering adds complexity and may not be a sca

---

## Question 55

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You are developing an internal application to facilitate organizing community events within your company. The application is deployed on a single Compute Engine instance. Your company utilizes Google Workspace (formerly G Suite), and you need to ensure that company employees can authenticate to the application from anywhere. What should you do?**

- [ ] IV. Assign a public IP address to your instance and enable internet traffic. Generate a random hash and create a subdomain containing this hash, pointing it to your instance. Share this DNS address with your company's employees.
- [x] II. Set up an HTTP(S) load balancer in front of the instance and configure Identity-Aware Proxy (IAP). Customize the IAP settings to grant access to the website from your company's domain.
- [ ] III. Establish a VPN tunnel between your company network and your instance's VPC location on Google Cloud. Configure necessary firewall rules and routing information for both on-premises and Google Cloud networks.
- [ ] I. Provide a public IP address to your instance and restrict access using firewall rules, allowing only your company's proxy as the source IP address.

### Explanation

**II. Set up an HTTP(S) load balancer in front of the instance and configure Identity-Aware Proxy (IAP). Customize the IAP settings to grant access to the website from your company's domain.**

Here's why this is the ideal choice:

  * **Secure and Integrated:** IAP leverages Google Workspace for authentication, ensuring only authorized company employees can access the application. No need to manage separate credentials.

  * **Ease of Access:** Users don't need a VPN to access the application from anywhere as long as they can sign in with their Google Workspace account.

  * **Scalability:** The load balancer can help manage traffic growth if the application becomes more popular.

  * **Google Best Practice:** IAP is Google's recommended solution for this scenario.

**Why Other Options Are Less Ideal**

  * **I. Firewall Restrictions:** While possible, managing firewall rules for individual company proxies can be cumbersome and prone to configuration errors.

  * **III. VPN Tunnel:** A VPN adds overhead and complexity, especially for a single application with potentially many remote users.

  * **IV. Obscure URL:** Relying on an obscure URL is not a true security mechanism and offers a poor user experience. It's also not integrated with your company's identity system.

**References:**

[https://cloud.google.com/iap/docs/concepts-overview#how_iap_works](https://cloud.google.com/iap/docs/concepts-overview#how_iap_works  https://cloud.google.com/blog/topics/developers-practitioners/control-access-your-web-sites-identity-aware-proxy)

[https://cloud.google.com/blog/topics/developers-practitioners/control-access-your-web-sites-identity-aware-proxy](https://cloud.google.com/iap/docs/concepts-overview#how_iap_works  https://cloud.google.com/blog/topics/developers-practitioners/control-access-your-web-sites-identity-aware-proxy)

---

## Question 56

*Domain 4: Integrating Applications with Google Cloud Services*

**You've created a JavaScript web application requiring access to Google Drive's API to store files in users' Google Drives. What's the recommended authorization approach for your application?**

- [ ] II. Generate a SAML token.
- [x] IV. Generate an OAuth Client ID.
- [ ] I. Generate an API key.
- [ ] III. Generate a service account.

### Explanation

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

---

## Question 57

*Domain 3: Configuring and Deploying Applications*

**You are tasked with deploying an internet-facing microservices application to Google Kubernetes Engine (GKE) and implementing A/B testing for new features. Your deployment must adhere to the following requirements:**

  * **Zero downtime during the deployment of new container images.**

  * **Testing and verification of new production releases using a subset of production users.**

**Which approach should you take?**

- [x] III. Install Anthos Service Mesh on the GKE cluster. Create two Deployments labeled with different version names. Implement an Istio routing rule to direct a small percentage of traffic to the Deployment with the new application version.
- [ ] IV. Implement a rolling update pattern by gradually replacing Pods with the new release version. Validate application performance for the subset of users during the rollout and rollback if necessary.
- [ ] II. Create a second namespace on GKE for the new release version. Set up a Deployment configuration in the new namespace with the required number of Pods. Deploy new container versions in this namespace and update the Ingress configuration to direct traffic to it.
- [ ] I. Configure your CI/CD pipeline to update the Deployment manifest file with the latest container version. Recreate Pods in the cluster by applying the updated Deployment manifest file. Validate application performance by comparing functionality with the previous release and rollback if necessary.

### Explanation

**Correct Option:**

**III. Install Anthos Service Mesh on the GKE cluster. Create two Deployments labeled with different version names. Implement an Istio routing rule to direct a small percentage of traffic to the Deployment with the new application version.**

**Explanation:**

  * **Zero downtime:** Service meshes like Istio facilitate traffic management without disrupting running Pods. This ensures no downtime during deployments.

  * **A/B Testing:** Istio's routing capabilities allow fine-grained control over traffic splitting, ideal for directing a small percentage of users to the new version for testing.

  * **Canary Releases:** This approach aligns with the concept of canary releases where you gradually expose new versions to increasing subsets of users.

**Why other options are less ideal:**

  * **I. Replacing Pods:** This will incur downtime as existing pods are terminated before new ones are launched. Not suitable for zero downtime requirements.

  * **II. Separate Namespaces:** While possible, managing traffic redirection through namespaces is less sophisticated than using a service mesh. It can add operational complexity.

  * **IV. Rolling Update:** Standard rolling updates achieve zero downtime, but lack the granular traffic control needed for true A/B testing on a subset of production users.

**References:**  
<https://cloud.google.com/architecture/implementing-deployment-and-testing-strategies-on-gke#perform_an_ab_test>

---

## Question 58

*Domain 2: Building and Testing Applications*

**You are preparing to test the Pub/Sub integration of your application, which reads credit card data from a Pub/Sub subscription. After completing code and unit testing, what is the recommended approach for testing the Pub/Sub integration before deploying to Google Cloud?**

- [x] IV. Establish a service for message publication and deploy the Pub/Sub emulator. Publish a predefined set of testing messages from the publishing service to the emulator for testing
- [ ] III. Implement a service for message publication and deploy the Pub/Sub emulator. Capture the messages from Pub/Sub in the production environment and publish them to the emulator for testing.
- [ ] II. Set up a service to publish messages to your application. Capture the messages from Pub/Sub in the production environment and replay them through the publishing service for testing.
- [ ] I. Develop a service for message publication and deploy the Pub/Sub emulator. Generate random content in the publishing service and publish it to the emulator for testing.

### Explanation

**IV. Establish a service for message publication and deploy the Pub/Sub emulator. Publish a predefined set of testing messages from the publishing service to the emulator for testing**

Here's the reasoning:

  * **Isolation:** Using the Pub/Sub emulator within a local or isolated testing environment protects your production environment from unintended consequences and experimental data.

  * **Control:** Predefined test messages allow you to test specific scenarios, edge cases, and potential error conditions relevant to your credit card processing logic.

  * **Reproducibility:** Having a controlled set of test messages makes the testing process more reproducible, aiding in debugging and ensuring consistent results.

**Why other options are less ideal:**

  * **I. Random Content:** While testing with random data can be useful, it might not cover all the important scenarios for your credit card data processing.

  * **II & III. Using Production Messages:** Relying on messages from production introduces these risks:

    * **Data Exposure:** Sensitive credit card data may be exposed in test environments.

    * **Inconsistency:** Production message patterns might not be suitable for your test cases.

    * **Potential Impact:** Replaying messages could interfere with real production operations.

**Reference:**

<https://cloud.google.com/pubsub/docs/emulator>

---

## Question 59

*Domain 3: Configuring and Deploying Applications*

**You encountered a situation where your application abruptly terminated during a Deployment update in Google Kubernetes Engine due to not closing the database connection properly. Now, you aim to enhance your application to ensure it undergoes a graceful shutdown. What is the recommended action to take?**

- [x] I. Revise your code to handle a received SIGTERM signal appropriately to gracefully disconnect from the database.
- [ ] III. Extend the terminationGracePeriodSeconds for your application.
- [ ] II. Implement a PodDisruptionBudget to safeguard the Pod from being forcibly terminated.
- [ ] IV. Set up a PreStop hook to manage the shutdown process of your application.

### Explanation

**Correct Option:**

**I. Update your code to process a received SIGTERM signal to gracefully disconnect from the database.**

**Explanation:**

  * This directly targets the root cause of the forceful shutdown. Kubernetes sends a SIGTERM signal before terminating a Pod. Your code needs to intercept this signal and initiate a graceful shutdown, including closing database connections.

**Why other options are less suitable:**

  * **II. Configure a PodDisruptionBudget:** While helpful for minimizing disruptions, this won't prevent shutdowns during node failures or manual deletions. It doesn't address the lack of graceful database connection handling.

  * **III. Increase the terminationGracePeriodSeconds:** This gives your application more time to shut down but doesn't ensure it will actually use that time to properly close connections if the SIGTERM signal isn't handled.

  * **IV. Configure a PreStop hook:** This can be useful for additional shutdown logic but is ineffective if your code still doesn't handle SIGTERM and close the database connection within the hook.

**References:**

[https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks  https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-a-graceful-shutdown-for-your-application)

[https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-a-graceful-shutdown-for-your-application](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks  https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-a-graceful-shutdown-for-your-application)

---

## Question 60

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Following a recent Google Kubernetes Engine (GKE) API outage caused by a zone failure, you aim to implement a highly available GKE architecture to reduce service interruptions for users during future zone failures. What action should you take?**

- [ ] III. Implement Multi-Zone clusters
- [ ] I. Implement Zonal clusters
- [x] II. Implement Regional clusters
- [ ] IV. Implement GKE on-premises clusters

### Explanation

The most appropriate action to take is 

**II. Implement Regional clusters**. Here's why:

**Regional clusters** :

  * **High Availability** : Regional clusters in GKE are designed for **high availability** as they automatically distribute nodes across multiple zones within a region. In the event of a zone failure, workloads are still available in other zones, minimizing service interruptions.

  * **Automatic replication** : The GKE control plane and worker nodes are replicated across multiple zones within a region, providing redundancy and failover capabilities.

  * **Managed failover** : Regional clusters automatically handle failover between zones, reducing the risk of service disruption during zone-level outages.

Other options and why they are less suitable:

  * **I. Implement Zonal clusters** : Zonal clusters are confined to a **single zone**. While they are easier to set up and may have lower costs, they are vulnerable to zone failures. If the zone goes down, all resources in that zone are affected, leading to outages.

  * **III. Implement Multi-Zone clusters** : Multi-Zone clusters distribute worker nodes across multiple zones but keep the **control plane in a single zone**. While this provides some level of redundancy for the nodes, the **control plane is still a single point of failure** , meaning if the control plane’s zone experiences issues, the entire cluster can be affected.

  * **IV. Implement GKE on-premises clusters** : GKE on-prem is primarily designed for hybrid cloud setups, where Kubernetes clusters are managed both on Google Cloud and in on-premises data centers. While it provides control and flexibility, it is not directly related to improving availability in the event of **zone failures** within Google Cloud.

**Reference:**

<https://cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#regional_clusters>

---
