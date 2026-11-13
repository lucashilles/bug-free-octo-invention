# Professional Cloud Developer — Practice Exam 1

60 questions.

## Question 1

*Domain 2: Building and Testing Applications*

**What approach should you take to implement a custom step in Cloud Build that ensures a copyright comment is present at the beginning of all source files, triggered by each source commit, and adds one if it's missing?**

- [ ] II. Develop a new Docker container to inspect files in /workspace, validating and appending a copyright comment to each source file. There's no requirement to commit the modified files back to the source repository.
- [ ] IV. Develop a new Docker container to inspect files in a Cloud Storage bucket, validating and appending a copyright comment to each source file. Modified files are explicitly committed back to the source repository.
- [x] I. Develop a new Docker container to analyze files in /workspace, verifying and adding a copyright comment to each source file. Any modified files are directly committed back to the source repository.
- [ ] III. Develop a new Docker container to inspect files in a Cloud Storage bucket, verifying and appending a copyright comment to each source file. Any changed files are written back to the Cloud Storage bucket.

### Explanation

**I. Develop a new Docker container to analyze files in /workspace, verifying and adding a copyright comment to each source file. Any modified files are directly committed back to the source repository.**

Here's why this stands out:

  * **Integration with Source Control:** Directly committing changes back to the repository ensures the copyright comment exists in the canonical source code, simplifying collaboration and preventing future inconsistencies.

  * **/workspace Context:** Cloud Build provides the `/workspace` directory, which contains the current state of your source repository. This aligns seamlessly with your Docker container's file analysis.

  * **Trigger Efficiency:** Triggering the build step on each source commit guarantees that the copyright comment is always present.

**Why other options are less ideal:**

  * **II. No Commit:** Without committing changes, your source code wouldn't reflect the updated copyright comments, leading to potential inaccuracies.

  * **III & IV. Cloud Storage Bucket:** While you could temporarily use a Cloud Storage bucket, it introduces unnecessary overhead compared to the direct `/workspace` approach and potential syncing complications if multiple builds run concurrently.

References:

<https://cloud.google.com/build/docs/configuring-builds/pass-data-between-steps#passing_data_using_workspaces>

---

## Question 2

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Which storage solution would best fulfill the requirements of transferring log data to a Cloud Storage bucket daily, allowing authenticated users to review logs from the prior two weeks for critical events and enabling annual reviews by an external auditor while minimizing costs? Choose two options from the following:**

- [x] IV. Establish a lifecycle management policy to transition the storage class to Coldline for objects older than 14 days.
- [ ] III. Generate a JSON Web Token (JWT) for users necessitating access to the Coldline storage buckets.
- [ ] V. Implement a lifecycle management policy to transition the storage class to Nearline for objects older than 14 days.
- [x] I. Implement the Bucket Lock feature to enforce a retention policy on the data.
- [ ] II. Utilize a scheduled job to transition the storage class to Coldline for objects older than 14 days.

### Explanation

The two storage solutions that would best fulfill the requirements of transferring log data to a Cloud Storage bucket daily, allowing authenticated users to review logs from the prior two weeks for critical events and enabling annual reviews by an external auditor while minimizing costs are:

**I. Implement the Bucket Lock feature to enforce a retention policy on the data.**

**IV. Establish a lifecycle management policy to transition the storage class to Coldline for objects older than 14 days.**

Explanation:

  * Option I suggests implementing the Bucket Lock feature to enforce a retention policy on the data. This ensures that the log data cannot be modified or deleted for a specified period, which aligns with the requirement for allowing authenticated users to review logs from the prior two weeks and enabling annual reviews by an external auditor.

  * Option IV proposes establishing a lifecycle management policy to transition the storage class to Coldline for objects older than 14 days. This allows for cost-effective storage of older log data while ensuring accessibility for the required duration and minimizing costs by moving data to a lower-cost storage class after the two-week review period.

Option II suggests transitioning the storage class to Coldline for objects older than 14 days, which aligns with the requirement for minimizing costs but does not address the requirement for authenticated users to review logs or enable annual reviews by an external auditor.

Option III mentions generating a JSON Web Token (JWT) for users necessitating access to the Coldline storage buckets, which addresses access control but does not directly fulfill the requirements related to data storage and management.

Option V proposes transitioning the storage class to Nearline for objects older than 14 days, which might reduce costs but does not ensure that the data remains accessible for the required duration or address the need for annual reviews by an external auditor.

Therefore, Options I and IV are the most suitable choices for fulfilling the specified requirements.

**References:**

[https://cloud.google.com/storage/docs/bucket-lock](https://cloud.google.com/storage/docs/bucket-lock  https://cloud.google.com/storage/docs/lifecycle)

[https://cloud.google.com/storage/docs/lifecycle](https://cloud.google.com/storage/docs/bucket-lock  https://cloud.google.com/storage/docs/lifecycle)

---

## Question 3

*Domain 2: Building and Testing Applications*

**How should you set up the unit testing process for Cloud Function code stored in a Cloud Source Repositories repository, ensuring deployment only occurs after passing the tests?**

- [x] IV. Utilize Cloud Build to perform unit tests, employing the specific service account for building; upon test success, Cloud Build automatically deploys the Cloud Function.
- [ ] I. Set up Cloud Build to handle Cloud Function deployment, with deployment approval triggered after passing tests.
- [ ] III. Implement Cloud Build to execute unit tests; upon successful testing, developers can proceed with Cloud Function deployment.
- [ ] II. Employ Cloud Build for deploying the Cloud Function, utilizing the specific service account for the build process, and executing unit tests post-deployment.

### Explanation

**The correct option is**

**IV: Utilize Cloud Build to perform unit tests, employing the specific service account for building; upon test success, Cloud Build automatically deploys the Cloud Function.**

**Here's why:**

  * **Automation & Efficiency:** This option streamlines testing and deployment into a single integrated process, saving time and effort.

  * **Enforced Testing:** Guarantees code quality because deployment happens _only_ after tests pass. This is critical for preventing broken code from reaching production.

  * **Cloud Build:** This Google Cloud service is ideal for building, testing, and deploying cloud-native applications, including Cloud Functions.

  * **Service Account:** Using a specific service account with deployment permissions ensures controlled access and security.

**Here's why the other options aren't as suitable:**

  * **I. Set up Cloud Build to handle Cloud Function deployment, with deployment approval triggered after passing tests.** While correct in ensuring that tests run, this option introduces a manual approval step. This can slow down deployment and might be unnecessary in many scenarios.

  * **II. Employ Cloud Build for deploying the Cloud Function, utilizing the specific service account for the build process, and executing unit tests post-deployment.** This approach is problematic because it deploys potentially untested code. Executing tests after deployment could reveal issues, necessitating rollbacks and adding complexity.

  * **III. Implement Cloud Build to execute unit tests; upon successful testing, developers can proceed with Cloud Function deployment.** This option places the deployment burden on developers and is less efficient than automated deployment through Cloud Build. It risks inconsistent deployment procedures as different developers handle this step.

---

## Question 4

*Domain 3: Configuring and Deploying Applications*

**Upon encountering HTTP request failures between two Pods directed at specific URLs, while other requests between the pods to different URLs are successful in your microservices application on Google Kubernetes Engine (GKE) utilizing Istio, what is the probable cause of the connection issue?**

- [ ] IV. If the cluster is configured with mTLS in permissive mode but the Pod's sidecar proxy is transmitting unencrypted traffic in plain text, it could lead to connection failures for specific URLs, particularly if mTLS enforcement is mandated for those URLs.
- [ ] II. It's plausible that the Pod initiating the HTTP requests is trying to connect to the target Pod via an incorrect TCP port, resulting in failed communication for specific URLs.
- [ ] I. The connection issue might stem from a Kubernetes NetworkPolicy resource, which could be limiting HTTP traffic between the Pods, potentially obstructing communication to specific URLs.
- [x] III. The observed connection failures for certain URLs could be attributable to the AuthorizationPolicy of your cluster being configured to block HTTP requests for specific paths within your application.

### Explanation

The probable cause of the connection issue between two Pods directed at specific URLs in your microservices application on Google Kubernetes Engine (GKE) utilizing Istio is:

**III. The observed connection failures for certain URLs could be attributable to the AuthorizationPolicy of your cluster being configured to block HTTP requests for specific paths within your application.**

Explanation:

  * Option I suggests that the connection issue might be caused by a Kubernetes NetworkPolicy resource limiting HTTP traffic between the Pods. While NetworkPolicy could potentially cause connectivity problems, it typically applies to all traffic, not specific URLs, making it less likely to be the cause of failures for certain URLs.

  * Option II implies that the failure might be due to incorrect TCP port configuration. However, if other requests between the pods to different URLs are successful, this is less likely to be the cause, as it would likely affect all requests.

  * Option III points to the AuthorizationPolicy of the cluster being configured to block HTTP requests for specific paths within the application. This is a plausible cause, as an AuthorizationPolicy can indeed restrict access to certain URLs based on specific criteria.

  * Option IV mentions the potential mismatch between mTLS configuration and the Pod's sidecar proxy transmitting unencrypted traffic. While this could lead to connection failures, it's less likely if other requests between the pods are successful, as mTLS enforcement would generally apply to all traffic equally.

Therefore, Option III is the most probable cause of the observed connection failures for specific URLs in this scenario.

**References:**

[https://istio.io/latest/docs/tasks/security/authorization/authz-http/](https://istio.io/latest/docs/tasks/security/authorization/authz-http/  https://kubernetes.io/docs/concepts/services-networking/network-policies/  https://istio.io/latest/docs/tasks/security/authentication/mtls-migration/)

[https://kubernetes.io/docs/concepts/services-networking/network-policies0](https://istio.io/latest/docs/tasks/security/authorization/authz-http/  https://kubernetes.io/docs/concepts/services-networking/network-policies/  https://istio.io/latest/docs/tasks/security/authentication/mtls-migration/)

[https://istio.io/latest/docs/tasks/security/authentication/mtls-migration/](https://istio.io/latest/docs/tasks/security/authorization/authz-http/  https://kubernetes.io/docs/concepts/services-networking/network-policies/  https://istio.io/latest/docs/tasks/security/authentication/mtls-migration/)

---

## Question 5

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**How should you securely manage session and shopping cart data for your ecommerce platform while adhering to Google's recommended standards?**

- [ ] I. Utilize advanced techniques such as storing session and cart data in local memory and enabling cookie-based session affinity within a global external HTTP(S) load balancer, ensuring optimal performance and security.
- [x] IV. Implement a comprehensive approach by utilizing Memorystore for Redis to securely store session data and Firestore for the shopping cart information, ensuring data integrity and scalability for your ecommerce platform.
- [ ] III. Opt for BigQuery as the storage solution for both session and shopping cart information, leveraging its scalability and analytical capabilities for robust data management.
- [ ] II. Employ Cloud Storage to store the shopping cart details, associating each cart with a unique session identifier, thus facilitating efficient retrieval and management of user data.

### Explanation

The most suitable approach for securely managing session and shopping cart data for your ecommerce platform while adhering to Google's recommended standards is:

**IV. Implement a comprehensive approach by utilizing Memorystore for Redis to securely store session data and Firestore for the shopping cart information, ensuring data integrity and scalability for your ecommerce platform.**

Explanation:

  * Option IV suggests a comprehensive approach by leveraging Memorystore for Redis to securely store session data and Firestore for shopping cart information. This approach aligns with Google's recommended standards as it provides a secure, scalable, and managed solution for both session and shopping cart data.

  * Option I mentions storing session and cart data in local memory and enabling cookie-based session affinity within a global external HTTP(S) load balancer. While this might offer performance benefits, it may not provide the same level of security and scalability as managed services like Memorystore for Redis and Firestore.

  * Option II proposes using Cloud Storage to store shopping cart details, which may not be the most suitable solution for managing session data due to its eventual consistency and lack of real-time querying capabilities.

  * Option III suggests using BigQuery for both session and shopping cart information. While BigQuery is powerful for analytical purposes, it may not be the most optimal solution for real-time data retrieval and management of session and shopping cart data.

Therefore, Option IV provides a balanced and recommended approach for securely managing session and shopping cart data while ensuring scalability and data integrity for your ecommerce platform.

**References:**

<https://cloud.google.com/memorystore>

<https://cloud.google.com/datastore/docs>

---

## Question 6

*Domain 2: Building and Testing Applications*

**You are preparing to deploy a microservices application on Google Kubernetes Engine (GKE) that will undergo daily updates. With a large number of distinct containers running on the Linux operating system (OS), you aim to stay informed about any known OS vulnerabilities in the new containers. Prioritizing Google's recommended best practices, what is the most suitable approach for achieving this?**

- [ ] III. Enable Container Analysis, store new container images in Artifact Registry, and specifically review critical vulnerability results before each deployment.
- [ ] IV. Utilize the Container Analysis REST API to invoke Container Analysis for scanning new container images, then review the vulnerability results before each deployment.
- [x] II. Enable Container Analysis and store new container images in Artifact Registry, subsequently reviewing the vulnerability results before each deployment.
- [ ] I. Utilize the gcloud CLI to invoke Container Analysis for scanning new container images and review the vulnerability results before each deployment.

### Explanation

**II. Enable Container Analysis and store new container images in Artifact Registry, subsequently reviewing the vulnerability results before each deployment.**

Explanation:

Option II is the most suitable approach for achieving the goal of staying informed about any known OS vulnerabilities in the new containers while prioritizing Google's recommended best practices. Here's why:

  * **Enable Container Analysis** : By enabling Container Analysis, you ensure that each container image pushed to Artifact Registry is automatically scanned for vulnerabilities. This allows you to proactively identify any potential security issues.

  * **Store new container images in Artifact Registry** : Storing container images in Artifact Registry provides a centralized location for managing and storing your images securely. It integrates seamlessly with Container Analysis, allowing vulnerability scanning to be performed automatically on each image upload.

  * **Review the vulnerability results before each deployment** : Before deploying a new container image, it's crucial to review the vulnerability results generated by Container Analysis. This ensures that you are aware of any known vulnerabilities present in the image and can take appropriate actions, such as patching or updating dependencies, before deployment.

**Options I, III, and IV also involve utilizing Container Analysis for scanning container images, but they either lack the integration with Artifact Registry (option I) or do not emphasize the importance of reviewing vulnerability results before each deployment (options III and IV).**

**Therefore, option II aligns with Google's recommended best practices and provides a comprehensive approach to staying informed about OS vulnerabilities in container images before deployment on Google Kubernetes Engine (GKE).**

**Reference:**

[https://cloud.google.com/artifact-registry/docs/analysis ](https://cloud.google.com/artifact-registry/docs/analysis)

---

## Question 7

*Domain 2: Building and Testing Applications*

**Considering the scenario of configuring a continuous integration pipeline using Cloud Build to automate container image builds, which optimization can be implemented based on the provided code segment? Choose two options.**

FROM python:3.7-alpine 

COPY . /app WORKDIR /app 

RUN pip install -r requirements.txt 

CMD ["gunicorn", "-w 4", "main:app"]

- [ ] E. Store the application's source code on Cloud Storage and configure the pipeline to download it using gsutil.
- [x] A. Opt for a larger virtual machine (VM) size with increased CPU capacity for Cloud Build operations.
- [ ] B. Establish a Container Registry on a Compute Engine VM within a Virtual Private Cloud (VPC) to store final images.
- [x] C. Employ caching for container images in subsequent builds using the --cache-from argument in the build configuration file.
- [ ] D. Adjust the base image in the build file to ubuntu:latest and install Python 3.7 using a package manager.

### Explanation

Correct answer

**A. Opt for a larger virtual machine (VM) size with increased CPU capacity for Cloud Build operations.**

**C. Employ caching for container images in subsequent builds using the --cache-from argument in the build configuration file.**

_A is correct because a high-CPU virtual machine type can increase the speed of your build.  
B is not correct because a Container Registry on a VM will not speed up the build.  
C is correct because the same container is used in subsequent steps for testing and to be pushed to the registry.  
D is not correct because an ubuntu container image will be significantly larger than the python:3.7-alpine image.  
E is not correct because storing the application source code on Cloud Storage does not decrease the time to build the application._

**References:**

[https://cloud.google.com/cloud-build/docs/speeding-up-builds](%0d https:/cloud.google.com/cloud-build/docs/speeding-up-builds%0d)

[https://cloud.google.com/build/docs/optimize-builds/increase-vcpu-for-builds](%0d https:/cloud.google.com/build/docs/optimize-builds/increase-vcpu-for-builds%0d)

---

## Question 8

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Which actions should you take to configure object storage while ensuring compliance with regulatory requirements and optimizing storage cost? (choose two)**

- [ ] III. Utilize IAM Conditions to restrict read access to objects based on their creation date, which is included in the object's prefix name.
- [x] I. Configure a retention policy on the bucket specifying a 7-year retention period.
- [ ] V. Develop a Cloud Function to evaluate the age of each object and transfer those older than 3 years to a second bucket configured with the Archive Storage class. Employ Cloud Scheduler to execute the Cloud Function daily.
- [x] II. Implement an object lifecycle policy that automatically transitions objects from Standard Storage to Archive Storage after they have existed for 3 years.
- [ ] IV. Enable Object Versioning to safeguard against accidental deletions for 7 years after object creation.

### Explanation

The actions that should be taken to configure object storage while ensuring compliance with regulatory requirements and optimizing storage cost are:

**I. Configure a retention policy on the bucket specifying a 7-year retention period.**

**II. Implement an object lifecycle policy that automatically transitions objects from Standard Storage to Archive Storage after they have existed for 3 years.**

Explanation:

  * Option I suggests configuring a retention policy on the bucket with a 7-year retention period. This ensures that objects within the bucket cannot be deleted or modified until the retention period expires, thereby helping to maintain compliance with regulatory requirements.

  * Option II proposes implementing an object lifecycle policy to automatically transition objects from Standard Storage to Archive Storage after they have existed for 3 years. This helps optimize storage cost by moving less frequently accessed data to a lower-cost storage class, while still retaining compliance with regulatory requirements by preserving the data.

Option III mentions utilizing IAM Conditions to restrict read access to objects based on their creation date, which may help with access control but does not directly address regulatory compliance or storage cost optimization.

Option IV suggests enabling Object Versioning to safeguard against accidental deletions, which is a useful feature but does not directly relate to regulatory compliance or storage cost optimization.

Option V involves developing a Cloud Function and employing Cloud Scheduler to evaluate and transfer objects older than 3 years to Archive Storage. While this may help with storage cost optimization, it does not directly ensure compliance with regulatory requirements.

Therefore, Options I and II are the most appropriate actions for configuring object storage while ensuring compliance with regulatory requirements and optimizing storage cost.

**Reference:**

<https://cloud.google.com/storage/docs/bucket-lock>

---

## Question 9

*Domain 2: Building and Testing Applications*

**You've recently launched a new service on Cloud Run, which authenticates via a custom service and records transactional data in a Cloud Spanner database. Your aim is to validate the application's capability to handle up to 5,000 read and 1,000 write transactions per second while pinpointing any bottlenecks. Additionally, your testing setup should be able to autoscale. What's the optimal approach?**

- [ ] I. Develop a testing framework to generate requests and deploy it on Cloud Run. Analyze VPC Flow Logs using Cloud Logging.
- [x] II. Set up a Google Kubernetes Engine cluster with Locust or JMeter images to dynamically generate load tests. Analyze outcomes with Cloud Trace.
- [ ] IV. Deploy a Compute Engine instance with a LAMP stack image from the Marketplace. Utilize Apache Bench for load testing against the service. Analyze findings with Cloud Trace.
- [ ] III. Use Cloud Tasks to generate a test load. Schedule 60,000 Cloud Task transactions per minute for 10 minutes using Cloud Scheduler. Review results via Cloud Monitoring.

### Explanation

**II. Set up a Google Kubernetes Engine cluster with Locust or JMeter images to dynamically generate load tests. Analyze outcomes with Cloud Trace.**

**Justification:**

  * **Suitable Load Testing Tools:** Locust and JMeter are industry-standard load testing tools designed specifically to simulate heavy user traffic and stress test systems. They offer flexibility for defining custom request patterns and simulating realistic user behavior.

  * **Scalability with Kubernetes:** GKE provides scalable and self-healing infrastructure for running load testing tools. You can spin up multiple instances of JMeter or Locust pods as needed to achieve the desired load of 5,000 read/1,000 write requests per second.

  * **In-depth Tracing with Cloud Trace:** Cloud Trace integrates seamlessly with Cloud Run and Cloud Spanner. It provides detailed visibility into request latencies, error rates, and spans, allowing you to pinpoint bottlenecks at different layers of your system.

**Why Other Options Are Less Ideal:**

  * **I. Develop a testing framework to generate requests and deploy it on Cloud Run. Analyze VPC Flow Logs using Cloud Logging.** Cloud Run can scale during the tests, but building your own framework would be time-consuming. VPC Flow Logs don't provide the granular telemetry needed to identify bottlenecks.

  * **III. Use Cloud Tasks to generate a test load. Schedule 60,000 Cloud Task transactions per minute for 10 minutes using Cloud Scheduler. Review results via Cloud Monitoring.** While Cloud Tasks can generate load, they are not specialized load testing tools and lack the flexibility to customize request patterns. Cloud Monitoring on its own may not uncover performance bottlenecks.

  * **IV. Deploy a Compute Engine instance with a LAMP stack image from the Marketplace. Utilize Apache Bench for load testing against the service. Analyze findings with Cloud Trace.** Deploying and managing a Compute Engine instance for load testing adds overhead. Apache Bench is not as advanced as Locust or JMeter in terms of customizability.

References:

<https://cloud.google.com/architecture/distributed-load-testing-using-gke>

---

## Question 10

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You've been assigned to oversee the transfer of your company's on-premises application to Google Cloud. The application, serving as an ecommerce platform, will undergo a phased migration to microservices on Google Cloud. As the majority of your company's revenue comes from online sales, it's crucial to minimize risks during the transition. Your task is to prioritize features and select the initial functionality for migration. What's the optimal approach?**

- [ ] IV. Migrate the Shopping cart, integrating it with the frontend, cart database, inventory system, and payment processing platform.
- [ ] III. Move Order fulfillment, establishing connections with the order database, inventory system, and third-party shipping partner.
- [ ] II. Shift Payment processing, integrating it with the frontend, order database, and third-party payment provider.
- [x] I. Transfer the Product catalog, ensuring seamless integration with the frontend and product database.

### Explanation

**I. Transfer the Product catalog, ensuring seamless integration with the frontend and product database.**

Here's my reasoning:

  * **Prioritizing the User Experience:** The product catalog lies at the heart of the customer experience on an ecommerce website. Users need to easily browse and search for products to initiate the purchase process. A disruption-free transfer of the catalog minimizes visible changes to customers, maintaining a positive user experience.

  * **Isolation:** It's likely that the product catalog has relatively independent dependencies, compared to the more interconnected payment and fulfillment systems. This allows for a cleaner, less disruptive migration phase.

  * **Risk Minimization:** Starting with the product catalog allows the team to test the migration process, infrastructure, and integration within Google Cloud with a less critical component. It lowers the risk of major service outages during the initial stages.

Let's analyze why the other options aren't optimal in this initial phase:

  * **II. Shift Payment processing...:** Payment processing is a highly sensitive and mission-critical function. Introducing complexity via migration in the early stages increases the risk of outages or security issues that could lead to lost revenue and customer trust.

  * **III. Move Order fulfillment...:** This option introduces dependencies on external shipping partners and internal inventory systems, adding potential points of failure. It is better postponed until the core product catalog feature is successfully migrated.

  * **IV. Migrate the Shopping cart...:** The shopping cart, while frontend-facing, has tightly coupled dependencies on inventory, payment, and possibly order data. Migrating it too early creates a chain of complex changes that can increase risk.

**References:**  
<https://cloud.google.com/architecture/migrating-a-monolithic-app-to-microservices-gke#choosing_an_initial_migration_effort>

---

## Question 11

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Which Google Cloud service is the optimal choice for deploying your container while ensuring seamless migration from an on-premises Knative environment, maintaining your application's deployment strategy, and utilizing a fully managed service?**

- [ ] II. Google Compute Engine
- [ ] IV. Google App Engine Flexible Environment
- [ ] III. Google Kubernetes Engine
- [x] I. Google Cloud Run

### Explanation

**I. Google Cloud Run**

Here's why it's the best fit:

  * **Knative Compatibility:** Cloud Run is built on Knative, ensuring a smooth migration from your on-premises environment and preserving your existing deployment strategies.

  * **Fully Managed:** Cloud Run eliminates the need to manage Kubernetes clusters and underlying infrastructure, aligning with your goal of a fully managed solution.

  * **Focus on Containers:** Cloud Run's primary focus is running containerized applications, making it a natural fit for your container-based workflow.

**Why the other options aren't as ideal:**

  * **II. Google Compute Engine:** Compute Engine gives you full control but requires managing the underlying virtual machines, deviating from your goal of a fully managed service.

  * **III. Google Kubernetes Engine:** While GKE provides a powerful environment, it entails managing Kubernetes clusters, which may introduce more overhead than you're willing to take on.

  * **IV. Google App Engine Flexible Environment:** App Engine Flexible supports containers but is oriented towards custom runtimes. It might not offer the same Knative compatibility as Cloud Run.

References:

<https://cloud.google.com/blog/products/serverless/knative-based-cloud-run-services-are-ga>

---

## Question 12

*Domain 3: Configuring and Deploying Applications*

**Your application deployed in Google Kubernetes Engine (GKE) is responsible for reading and processing Pub/Sub messages. The message publication rate to the Pub/Sub topic varies significantly throughout the day and week, occasionally leading to large batches of messages being published simultaneously. To ensure timely message processing, what GKE feature should you employ to automatically adjust your workload?**

- [ ] I. Vertical Pod Autoscaler in Auto mode.
- [x] III. Horizontal Pod Autoscaler based on an external metric.
- [ ] II. Vertical Pod Autoscaler in Recommendation mode.
- [ ] IV. Horizontal Pod Autoscaler based on resource utilization.

### Explanation

**III. Horizontal Pod Autoscaler based on an external metric.**

Here's why this choice is optimal:

  * **Scaling Based on Demand:** A Horizontal Pod Autoscaler (HPA) combined with an external metric like the Pub/Sub backlog will directly scale your pods in proportion to the number of unprocessed messages. This ensures timely processing even during bursts of activity.

  * **Specific to Pub/Sub:** The HPA can leverage metrics from Cloud Monitoring specific to Pub/Sub, such as `pubsub.googleapis.com/subscription/num_undelivered_messages`.

  * **Efficiency:** Horizontal scaling allows you to add/remove processing capacity as needed, optimizing resource usage and cost.

**Why Other Options Are Less Ideal:**

  * **I. Vertical Pod Autoscaler in Auto mode.**

    * Vertical scaling changes the resources allocated to individual pods (CPU/memory). This may not be the most efficient way to handle bursts if your bottleneck is the number of pods rather than per-pod resources.

  * **II. Vertical Pod Autoscaler in Recommendation mode.**

    * Recommendations might be useful for long-term adjustments, but don't address the need for rapid scaling in response to workload spikes.

  * **IV. Horizontal Pod Autoscaler based on resource utilization.**

    * While useful for many scenarios, resource utilization (CPU/memory) might not directly correlate to message backlog. If Pods are processing messages quickly, they might show low CPU usage even with a backlog due to network latency/other factors.

References:

<https://cloud.google.com/kubernetes-engine/docs/tutorials/autoscaling-metrics#pubsub>

---

## Question 13

*Domain 4: Integrating Applications with Google Cloud Services*

**Your code, operating on Cloud Functions within project A, aims to write an object to a Cloud Storage bucket owned by project B. Unfortunately, the write operation fails with a "403 Forbidden" error. How can you address this issue effectively?**

- [x] III. Allocate the roles/storage.objectCreator role to the service-PROJECTA@gcf-admin-robot.iam.gserviceaccount.com service account for the Cloud Storage bucket.
- [ ] IV. Ensure the Cloud Storage API is enabled within project B.
- [ ] II. Provide your user account with the roles/iam.serviceAccountUser role for the service-PROJECTA@gcf-admin-robot.iam.gserviceaccount.com service account.
- [ ] I. Grant your user account the roles/storage.objectCreator role for the Cloud Storage bucket.

### Explanation

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

---

## Question 14

*Domain 3: Configuring and Deploying Applications*

**You've set up automatic scaling for your Compute Engine instance group based on overall CPU usage. However, you've noticed a significant uptick in response latency as the cluster scales up. To ensure a smoother user experience, you're considering adjustments to the instance group autoscaler configuration. What are the two recommended changes?**

- [x] II. Shorten the cooldown period for newly added instances in the group.
- [x] IV. Decrease the target CPU usage threshold for the instance group autoscaler.
- [ ] III. Increase the target CPU usage threshold for the instance group autoscaler.
- [ ] V. Remove the health check for individual VMs in the instance group.
- [ ] I. Apply the "AUTOSCALE" label to the instance group template.

### Explanation

**II. Shorten the cooldown period for newly added instances in the group.**

  * **Faster Readiness:** A shorter cooldown period lets new instances handle traffic sooner after being created, reducing the time where existing instances are overloaded.

  * **Cooldown Considerations:** Choose a cooldown period that allows for your application's initialization time. Too short, and new instances will receive traffic before they're ready.

**IV. Decrease the target CPU usage threshold for the instance group autoscaler.**

  * **Proactive Scaling:** Lowering the threshold triggers scaling earlier. This helps avoid the period where existing instances hit high CPU usage (and therefore higher latency) before new ones are added.

  * **Balance with Cost:** Scaling out earlier might increase costs. Tune the threshold to find the sweet spot between responsiveness and efficient resource usage.

**Why Other Options Are Less Ideal**

  * **I. Apply the "AUTOSCALE" label ...** Autoscaling works without an explicit label, this likely won't help your latency issue.

  * **III. Increase the target CPU usage threshold ...** This would worsen the problem. It would delay scaling until instances are even more heavily loaded, leading to worse latency.

  * **V. Remove the health check ...** Health checks are critical! They prevent unhealthy instances from receiving traffic, which would be disastrous for user experience.

---

## Question 15

*Domain 4: Integrating Applications with Google Cloud Services*

**To enable clients to download a file from your website for a limited period while adhering to Google's recommended best practices, how should you architect the application?**

- [x] II. Generate and allocate a Cloud Storage-signed URL for the file, then provide the URL to the client for downloading.
- [ ] III. Create a temporary Cloud Storage bucket with a specified time expiration, granting download permissions to the bucket, copying the file, and providing it to the client.
- [ ] IV. Generate HTTP cookies with a specified time expiration. If the time is valid, retrieve the file from the Cloud Storage bucket and make it accessible for the client to download.
- [ ] I. Configure the application to deliver the file to the client as an email attachment.

### Explanation

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

---

## Question 16

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**To transition a monolithic application into a microservices model efficiently while minimizing business impact, which strategy should you pursue?**

- [ ] III. Refactor the monolithic application by integrating appropriate microservices in a single concerted effort and deploy it.
- [ ] IV. Develop a new application with the necessary microservices independently of the monolith and switch it upon completion.
- [ ] I. Deploy the application on Compute Engine and activate autoscaling.
- [x] II. Gradually replace the application's functionalities with suitable microservices over several phases.

### Explanation

**II. Gradually replace the application's functionalities with suitable microservices over several phases.**

This incremental approach offers several advantages for a monolith-to-microservices transition:

  * **Reduced Risk:** Iteratively replacing components minimizes the chances of widespread disruption and makes errors easier to isolate.

  * **Controlled Pace:** The gradual transition allows your team to learn and adapt to the microservices architecture without overwhelming pressure.

  * **Agility:** You can prioritize the modules that provide the most immediate value or are easiest to refactor as microservices first.

  * **Coexistence:** During the transition, the monolith and new microservices can coexist, often using techniques like the Strangler Fig pattern to manage interactions.

**Why Other Options Have Drawbacks:**

  * **I. Deploy the application on Compute Engine and activate autoscaling.** This focuses on scaling but doesn't address the inherent architectural challenges of a monolithic application.

  * **III. Refactor the monolithic application ... in a single ... effort and deploy it.** Such a "big bang" refactor is high-risk. It can lead to prolonged downtime and increased likelihood of errors and complexities.

  * **IV. Develop a new application ... independently ... and switch it upon completion.** While sometimes necessary for extremely outdated monoliths, it requires maintaining two codebases in parallel for a while and introduces a risky cutover event.

**References:**

<https://cloud.google.com/architecture/microservices-architecture-refactoring-monoliths>

---

## Question 17

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**For a mobile application aiming to store hierarchical data structures in a database, allowing offline syncing and scalability, while ensuring security, which combination of database and IAM role is most suitable?**

- [x] III. Utilize Firestore in Native mode for its offline syncing capabilities, and assign the roles/datastore.user role to the service account for secure data handling.
- [ ] II. Employ Bigtable as the database solution, and assign the roles/bigtable.viewer role to the service account for enriched data processing.
- [ ] I. Opt for Cloud SQL as the database solution, and assign the roles/cloudsql.editor role to the service account for enriched data management.
- [ ] IV. Select Firestore in Datastore mode, and assign the roles/datastore.viewer role to the service account to facilitate secure and scalable data operations.

### Explanation

**III. Utilize Firestore in Native mode for its offline syncing capabilities, and assign the roles/datastore.user role to the service account for secure data handling.**

Here's why this choice stands out:

  * **Hierarchical Data:** Firestore's document-oriented structure excels at handling hierarchical data, a common requirement for mobile applications.

  * **Offline Syncing:** Firestore's Native mode offers robust offline support, ensuring your app functions even with intermittent connectivity.

  * **Scalability:** Firestore scales effortlessly, accommodating the unpredictable usage patterns of mobile apps.

  * **Security:** The `roles/datastore.user` role provides the necessary permissions for data manipulation while adhering to the principle of least privilege.

**Why other options are less suitable:**

  * **I. Cloud SQL:** Cloud SQL is a relational database, making it less natural for hierarchical data and less straightforward for offline use. The `roles/cloudsql.editor` role grants excessive permissions.

  * **II. Bigtable:** Bigtable is a powerful columnar database but is overkill for many mobile apps. It might bring unnecessary complexity. The `roles/bigtable.viewer` role focuses on read operations, not data modification.

  * **IV. Firestore (Datastore Mode):** While suitable, Native mode offers enhanced offline capabilities compared to Datastore mode. The `roles/datastore.viewer` role is read-only.

Ref:

<https://cloud.google.com/architecture/building-scalable-apps-with-cloud-firestore>

---

## Question 18

*Domain 4: Integrating Applications with Google Cloud Services*

**You recently migrated a monolithic application to Google Cloud, breaking it down into microservices. One of these microservices is deployed using Cloud Functions. As you modernize the application, you introduce a backward-incompatible change to the service's API. You now need to support both existing callers using the original API and new callers utilizing the updated API. What's the best approach?**

- [ ] II. Keep the original Cloud Function unchanged and deploy a second Cloud Function containing only the modified API. Calls are automatically routed to the appropriate function.
- [ ] IV. Update the Cloud Function's code to support the new API and redeploy it. Requests for both API versions are handled based on a version identifier included in the call.
- [x] III. Retain the original Cloud Function unchanged and deploy a second Cloud Function with the new API. Utilize Cloud Endpoints to provide an API gateway exposing a versioned API.
- [ ] I. Maintain the original Cloud Function unchanged and deploy a second Cloud Function with the new API. Employ a load balancer to distribute calls between the versions.

### Explanation

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

---

## Question 19

*Domain 3: Configuring and Deploying Applications*

**When configuring a Deployment on Google Kubernetes Engine (GKE), including a check to ensure containers can connect to the database, and initiating a graceful shutdown script if connection fails, what configuration should you employ?**

- [ ] IV. Configure the Deployment with an initContainer to check service availability. Set up a Prestop lifecycle handler to execute the shutdown script if the Pod is failing.
- [ ] I. Establish two jobs: one to assess container-database connectivity, and another to execute the shutdown script if the Pod is encountering connectivity issues.
- [ ] III. Set up the Deployment with a PostStart lifecycle handler to verify service availability. Configure a PreStop lifecycle handler to execute the shutdown script if the container fails.
- [x] II. Construct the Deployment with a livenessProbe for the container, which will fail if database connectivity is not established. Configure a Prestop lifecycle handler to execute the shutdown script if the container fails.

### Explanation

The most suitable answer in this case is

**II. Construct the Deployment with a livenessProbe for the container, which will fail if database connectivity is not established. Configure a Prestop lifecycle handler to execute the shutdown script if the container fails.**

Here's why:

  * **LivenessProbe:** A livenessProbe is specifically designed to monitor the health of a container. If it cannot connect to the database, Kubernetes will recognize the container as unhealthy and automatically restart it, potentially re-establishing the connection.

  * **PreStop Lifecycle Handler:** This hook is triggered before the container is terminated. It's the perfect place to execute your graceful shutdown script, ensuring any in-process tasks are completed cleanly.

Here's why the other options aren't as ideal:

  * **I. Separate Jobs:** This approach adds complexity and might introduce delays. Jobs might not run with the frequency needed to detect connectivity issues promptly.

  * **III. PostStart Handler:** PostStart is executed once after container startup. It wouldn't provide continuous monitoring, and a PreStop hook doesn't automatically trigger if a liveness probe fails.

  * **IV. InitContainer:** An initContainer runs to completion before the main container starts. It might not accurately reflect ongoing connectivity issues after startup and delays the main application container.

References:

<https://cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on->

---

## Question 20

*Domain 2: Building and Testing Applications*

**You want to assess the security vulnerabilities of an application running on App Engine. Which service should you use for this purpose?**

- [ ] I. Cloud Armor
- [ ] IV. Stackdriver Error Reporting
- [ ] II. Stackdriver Debugger
- [x] III. Cloud Security Scanner

### Explanation

**III. Cloud Security Scanner**

Here's why it's the right choice:

  * **Vulnerability Scanning:** Cloud Security Scanner is designed specifically to scan web applications for common vulnerabilities like cross-site scripting (XSS), SQL injection, and outdated libraries.

  * **App Engine Integration:** It seamlessly integrates with App Engine, making it easy to scan your deployed application.

  * **Actionable Reports:** Cloud Security Scanner provides detailed reports on discovered vulnerabilities, along with recommendations for remediation.

**Why Other Options Are Less Ideal:**

  * **I. Cloud Armor** Cloud Armor is a web application firewall (WAF) primarily focused on mitigating DDoS attacks and enforcing IP-based allow/deny lists. While it enhances security, it doesn't directly scan for application-level vulnerabilities.

  * **II. Stackdriver Debugger** Debugger helps inspect an application's state in production for troubleshooting errors, but doesn't have a security focus.

  * **IV. Stackdriver Error Reporting** Error Reporting aids in error analysis, but may indirectly reveal consequences of an exploit rather than identifying the vulnerability itself.

**References:**

[https://cloud.google.com/appengine/docs/standard/python/application-security:](https://cloud.google.com/appengine/docs/standard/python/application-security:  https://cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview)

[https://cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview](https://cloud.google.com/appengine/docs/standard/python/application-security:  https://cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview)

---

## Question 21

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**In the development of a single-page web application with a user interface that interacts with a third-party API using XMLHttpRequest, prioritizing rendering performance is crucial. While the API data displayed on the UI is less critical than other data, delays in API calls should not impact the rendering of other UI elements. Efficient handling of API errors or timeouts is necessary. What's the optimal approach?**

- [ ] III. Implement error handling to capture timeout or error exceptions from the API call and retry with exponential backoff until a successful response is received.
- [ ] IV. Implement error handling to capture timeout or error exceptions from the API call and display the error response in the UI widget.
- [ ] I. Disable the asynchronous option for API requests and conceal the UI widget displaying API results upon encountering a timeout or error.
- [x] II. Enable the asynchronous option for API requests and conceal the UI widget displaying API results upon encountering a timeout or error.

### Explanation

**II. Enable the asynchronous option for API requests and conceal the UI widget displaying API results upon encountering a timeout or error.**

Here's why this approach offers the best trade-off between performance and user experience:

  * **Asynchronous for Performance:** Asynchronous API calls prevent blocking the main UI thread, ensuring the rest of your single-page application remains responsive and can render independently.

  * **User Experience:** Concealing the UI widget specifically for the API data provides a smooth user experience. It indicates that the data is being fetched while not disrupting other page elements.

  * **Error Handling:** While not the primary focus, basic error handling with concealment of the widget maintains a usable application state.

**Why Other Options Are Less Ideal**

  * **I. Disable the asynchronous option...** Synchronous API calls will block the main thread, degrading overall user experience and potentially causing the entire page to become unresponsive.

  * **III. Implement error handling to capture ...and retry...** Retry logic can be valuable, but blindly retrying too often can put unnecessary load on the third-party API and still frustrate users if the issue persists.

  * **IV. ...display the error response in the UI widget.** While informative for debugging, directly displaying raw error messages to users is generally not the best user experience. It's better to provide a more user-friendly indicator that something went wrong.

---

## Question 22

*Domain 4: Integrating Applications with Google Cloud Services*

**While conducting load testing on your server application, you observe that an inactive Cloud Storage bucket is now handling 2000 write requests per second and 7500 read requests per second within the initial 30 seconds. Consequently, your application begins experiencing intermittent 5xx and 429 HTTP responses from the Cloud Storage JSON API due to increased demand. To mitigate the occurrence of failed responses from the Cloud Storage API, what action should you take?**

- [ ] II. Opt for the XML API instead of the JSON API for interacting with Cloud Storage.
- [ ] III. Transmit the HTTP response codes back to clients initiating uploads from your application.
- [ ] I. Distribute the uploads across multiple individual storage buckets.
- [x] IV. Restrict the upload rate from your application clients to ensure a gradual increase in the dormant bucket's peak request rate.

### Explanation

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

---

## Question 23

*Domain 3: Configuring and Deploying Applications*

**While developing a JPEG image-resizing API on Google Kubernetes Engine (GKE), the service's callers will reside within the same GKE cluster. You aim to facilitate clients in obtaining the service's IP address. What's the recommended approach?**

- [ ] IV. Configure a GKE Endpoint. Clients should obtain the endpoint name from Cloud DNS.
- [ ] III. Configure a GKE Endpoint. Clients should retrieve the endpoint name from the appropriate environment variable within the client container.
- [ ] I. Establish a GKE Service. Clients should use the A record's name in Cloud DNS to locate the service's cluster IP address.
- [x] II. Set up a GKE Service. Clients should utilize the service name within the URL to access the service.

### Explanation

**II. Set up a GKE Service. Clients should utilize the service name within the URL to access the service.**

**Explanation:**

Using a GKE Service with its service name is the most efficient and reliable way to enable service discovery within a Kubernetes cluster:

  * **Internal DNS:** Kubernetes automatically assigns a DNS name to each Service, providing a simple abstraction for clients. The service name becomes the hostname (e.g., `my-image-resizer.default.svc.cluster.local`)

  * **Load Balancing:** Kubernetes Services handle load balancing across the pods that actually run your API.

  * **Simplicity for Clients:** Clients don't need to maintain specific IP addresses, which can change as pods are rescheduled or scaled.

**Why Other Options Are Less Ideal:**

  * **I. Establish a GKE Service ... Cloud DNS to locate ... cluster IP address** While technically possible, manually managing Cloud DNS and cluster IPs adds complexity and potential points of failure.

  * **III & IV. Configure a GKE Endpoint ... Clients should retrieve the endpoint name ...** GKE Endpoints are primarily for exposing services outside the cluster. Since you're working within the cluster, they add unnecessary layers.

**References:**

[https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/  https://cloud.google.com/kubernetes-engine/docs/concepts/service-discovery)

[https://cloud.google.com/kubernetes-engine/docs/concepts/service-discovery](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/  https://cloud.google.com/kubernetes-engine/docs/concepts/service-discovery)

---

## Question 24

*Domain 4: Integrating Applications with Google Cloud Services*

**Your service annotates images fetched from Cloud Storage. During peak periods, requests to Cloud Storage result in HTTP 429 "Too Many Requests" errors. How should you address this issue?**

- [ ] IV. Switch the storage class of the Cloud Storage bucket to Multi-regional.
- [ ] II. Request a quota increase through the GCP Console.
- [x] III. Retry the request employing a truncated exponential backoff strategy.
- [ ] I. Apply a cache-control header to the objects.

### Explanation

**III. Retry the request employing a truncated exponential backoff strategy.**

Here's why this is the most effective immediate solution and why the others have limitations:

  * **Addresses the Root Issue:** HTTP 429 errors signal that you're exceeding your Cloud Storage request rate. Retrying with exponential backoff allows your service to gracefully handle temporary throttling, giving the quota time to reset.

  * **Quick Implementation:** Implementing this retry mechanism likely involves minor code changes in the component making requests to Cloud Storage.

  * **Scalability:** Exponential backoff helps your service automatically adjust its behavior to handle temporary load spikes.

**Why Other Options Might Help, But Have Limitations:**

  * **I. Apply a cache-control header...** Caching can reduce future requests for the same images, but it doesn't directly address the 429 errors when the cache is empty.

  * **II. Request a quota increase...** This can be a valid solution, but it might take time for approval and involves additional costs.

  * **IV. Switch ... to Multi-regional.** Multi-regional storage can improve availability and redundancy but might not directly alleviate the current quota limitations.

---

## Question 25

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You have authored a Cloud Function that interacts with other Google Cloud services. To ensure security following the principle of least privilege, what is the recommended approach?**

- [ ] III. Create a fresh service account with Editor permissions for accessing the resources. Give the deployer authorization to act as the new service account.
- [x] IV. Generate a new service account with a custom IAM role tailored for accessing the resources. Provide the deployer authorization to act as the new service account.
- [ ] II. Set up a new service account with a custom IAM role crafted for accessing the resources. Grant the deployer authorization to obtain the access token.
- [ ] I. Establish a new service account with Editor permissions for accessing the resources. Provide the deployer authorization to acquire the access token.

### Explanation

**IV. Generate a new service account with a custom IAM role tailored for accessing the resources. Provide the deployer authorization to act as the new service account.**

Here's why this stands out as the best choice:

  * **Principle of Least Privilege:** A custom IAM role grants only the absolutely necessary permissions required by the Cloud Function, reducing the risk of unintended consequences or privilege escalation.

  * **Separation of Concerns:** Granting the deployer the ability to 'act as' the service account maintains a separation between deployment permissions and the Cloud Function's runtime permissions. This improves auditability and makes the flow of permissions clearer.

  * **Security Best Practice:** This is the approach explicitly recommended by Google for adhering to the principle of least privilege in Cloud Functions.

**Why Other Options are Less Ideal:**

  * **I & III. Editor Permissions:** The Editor role is a basic role that encompasses a wide range of permissions. This significantly violates the principle of least privilege, making your system more vulnerable.

  * **II. Custom Role but Deployer Gets Access Token:** While a custom role is better, granting the deployer the ability to obtain the service account's access token still increases the attack surface unnecessarily.

**References:**

<https://cloud.google.com/functions/docs/securing/function-identity#individual>

<https://cloud.google.com/functions/docs/securing/function-identity#per-function_identity>

<https://cloud.google.com/functions/docs/securing/function-identity>

---

## Question 26

*Domain 3: Configuring and Deploying Applications*

**The latest iteration of your containerized application has undergone rigorous testing and stands poised for deployment to production on Google Kubernetes Engine. Due to limitations, thorough load testing couldn't be conducted in pre-production environments. Ensuring a seamless deployment free from performance glitches is paramount, with automation being a prerequisite. What actions should you take?**

- [ ] IV. Execute the deployment using kubectl and configure the spec.updateStrategy.type to RollingUpdate. Utilize Cloud Monitoring to flag any performance issues and initiate a rollback using the kubectl command if necessary.
- [ ] I. Employ Cloud Load Balancing to gradually increase traffic between versions, while relying on Cloud Monitoring to detect any performance anomalies.
- [x] II. Implement a continuous delivery pipeline featuring canary deployments, utilizing Cloud Monitoring to pinpoint performance issues and incrementally scaling up traffic based on observed metrics.
- [ ] III. Opt for a continuous delivery pipeline with blue/green deployments, leveraging Cloud Monitoring to identify performance bottlenecks and proceeding with full deployment once metrics confirm readiness.

### Explanation

**II. Implement a continuous delivery pipeline featuring canary deployments, utilizing Cloud Monitoring to pinpoint performance issues and incrementally scaling up traffic based on observed metrics.**

**Explanation:**

  * **Risk Mitigation:** Canary deployments are ideal for this scenario, letting you test the new version with a small subset of real production traffic. This limits potential impact if issues arise.

  * **Gradual Rollout:** With incremental traffic increases, you have greater control while gathering live performance data.

  * **Monitoring-Driven:** Cloud Monitoring plays a key role in observing key metrics (latency, error rates, etc.). This data will inform your decision on whether to continue the rollout or roll back.

  * **Automation:** A continuous delivery pipeline automates the entire process, ensuring consistency and speed.

**Why Other Options Aren't as Suitable**

  * **I. Cloud Load Balancing with Monitoring:** While this can help distribute traffic, it lacks the fine-grained control and automated rollback mechanisms offered by a proper canary deployment strategy.

  * **III. Blue/Green Deployments:** Blue/green is well-suited for rapid rollbacks, but it requires double the resources and can be overkill if the changes aren't drastic.

  * **IV. Manual Rollout with Kubectl:** This option lacks the safeguards and automation of a dedicated continuous delivery pipeline. It's error-prone and less scalable.

**Reference:**

<https://cloud.google.com/deploy/docs/deployment-strategies/canary#types_of_canary>

---

## Question 27

*Domain 3: Configuring and Deploying Applications*

**Given the urgent need to implement autoscaling for your stateless and distributed service operating in a Google Kubernetes Engine (GKE) cluster without significant alterations, which approach should you pursue?**

- [x] III. Opting for a Horizontal Pod Autoscaler would enable scaling the number of Pods based on CPU load, offering a straightforward solution that aligns with the stateless and distributed nature of the service, with minimal changes required.
- [ ] II. Deploying a Vertical Pod Autoscaler to scale based on a custom metric could entail substantial changes and additional configurations, potentially complicating the deployment within the constrained two-week timeframe.
- [ ] I. Deploying a Vertical Pod Autoscaler would dynamically adjust the resource requests and limits for individual Pods based on their actual usage, but it doesn't directly cater to autoscaling according to workload demands.
- [ ] IV. Implementing a Horizontal Pod Autoscaler to scale based on a custom metric might necessitate more intricate configurations and adjustments, potentially impeding the deployment within the two-week timeframe.

### Explanation

Given the urgent need to implement autoscaling for your stateless and distributed service operating in a Google Kubernetes Engine (GKE) cluster without significant alterations, the most appropriate approach to pursue is:

**III. Opting for a Horizontal Pod Autoscaler would enable scaling the number of Pods based on CPU load, offering a straightforward solution that aligns with the stateless and distributed nature of the service, with minimal changes required.**

Explanation:

  * Option III suggests deploying a Horizontal Pod Autoscaler, which is designed specifically for scaling the number of Pods based on CPU load. This aligns well with the stateless and distributed nature of the service, as it can automatically adjust the number of Pods to handle varying workload demands without significant changes to the deployment.

  * Option I discusses deploying a Vertical Pod Autoscaler, which adjusts resource requests and limits for individual Pods based on their usage but doesn't directly address autoscaling according to workload demands. This approach might not be suitable for rapidly changing workloads.

  * Option II mentions deploying a Vertical Pod Autoscaler to scale based on a custom metric. While this could be possible, it may entail substantial changes and additional configurations, potentially complicating the deployment within the constrained timeframe.

  * Option IV discusses implementing a Horizontal Pod Autoscaler to scale based on a custom metric, which might necessitate more intricate configurations and adjustments, potentially impeding the deployment within the two-week timeframe.

Therefore, Option III provides the most straightforward and suitable solution for implementing autoscaling for the stateless and distributed service in a GKE cluster within the urgent timeframe.

**References:**

[https://cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling](https://cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling  https://cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler  https://cloud.google.com/kubernetes-engine/docs/tutorials/custom-metrics-autoscaling)

[https://cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler](https://cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling  https://cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler  https://cloud.google.com/kubernetes-engine/docs/tutorials/custom-metrics-autoscaling)

[https://cloud.google.com/kubernetes-engine/docs/tutorials/custom-metrics-autoscaling](https://cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling  https://cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler  https://cloud.google.com/kubernetes-engine/docs/tutorials/custom-metrics-autoscaling)

---

## Question 28

*Domain 2: Building and Testing Applications*

**You've recently launched a Go application on Google Kubernetes Engine (GKE). The operations team has observed high CPU usage even during periods of low production traffic. They've requested you to optimize the application's CPU resource consumption. To identify which Go functions are consuming the most CPU, what action should you take?**

- [ ] III. Access your GKE nodes via SSH. Execute the top command in the shell to extract the CPU utilization of your application.
- [ ] II. Develop a customized dashboard in Cloud Monitoring to assess the CPU performance metrics of your application.
- [x] IV. Adjust your Go application to gather profiling data. Evaluate the CPU metrics of your application using flame graphs in Profiler.
- [ ] I. Implement a Fluent Bit daemonset on the GKE cluster for logging data in Cloud Logging. Analyze the logs to gain insights into your application code's performance.

### Explanation

The most suitable option is 

**IV. Adjust your Go application to gather profiling data. Evaluate the CPU metrics of your application using flame graphs in Profiler.**

**Here's why:**

  * **Profiling provides function-level granularity:** Profiling tools in Go allow pinpointing the exact functions within your application that consume the most CPU resources. This level of detail is crucial for focused optimization efforts.

**Here's why the other options aren't as suitable:**

  * **I. Logs** Logs might indicate performance issues, but they won't directly reveal which functions are consuming the most CPU time. Analyzing logs for this purpose can be cumbersome and indirect.

  * **II. Cloud Monitoring dashboards** Dashboards provide a high-level overview of CPU usage but don't offer the function-level detail needed to pinpoint the root cause of high CPU usage.

  * **III. SSH and top** The `top` command provides real-time process-level CPU usage but lacks the fine-grained analysis that profiling provides for pinpointing the most CPU-intensive functions within your Go application's code.

Ref:

<https://cloud.google.com/profiler/docs>

---

## Question 29

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You are developing a marquee stateless web application to run on Google Cloud. The incoming user traffic rate is expected to be unpredictable, with some days experiencing no traffic and others encountering large spikes. You need the application to automatically scale up and down while minimizing associated costs. What should you do?**

- [x] I. Develop the application in Python with Firestore as the database. Deploy it to Cloud Run.
- [ ] IV. Develop the application in Python with Firestore as the database. Deploy it to a Compute Engine managed instance group with autoscaling.
- [ ] III. Develop the application in Python with CloudSQL as the database. Deploy it to the App Engine standard environment.
- [ ] II. Develop the application in C# with Firestore as the database. Deploy it to the App Engine flexible environment.

### Explanation

**I. Develop the application in Python with Firestore as the database. Deploy it to Cloud Run.**

Let's break down why this is the ideal choice:

  * **Serverless Cost-Efficiency:** Cloud Run is a serverless platform that scales down to zero instances when there's no traffic, ensuring you only pay for resources when the app is active.

  * **Rapid Scaling:** Cloud Run can scale up very quickly in response to sudden traffic spikes, handling your unpredictable traffic patterns.

  * **Stateless Design Alignment:** Your description of a stateless application is a perfect fit for the serverless model of Cloud Run.

  * **Firestore Integration:** Firestore, as a NoSQL database, complements serverless paradigms with its scalability and ease of development.

**Why Other Options are Less Ideal:**

  * **II. App Engine Flexible Environment:** While suitable for web applications, the flexible environment has a minimum number of instances, incurring costs even during periods of inactivity.

  * **III. App Engine Standard Environment:** The standard environment doesn't scale down to zero, and Cloud SQL, as a managed SQL database, is not as ideal a fit for a serverless application as Firestore.

  * **IV. Compute Engine Managed Instance Groups:** While Compute Engine offers autoscaling, it involves overhead in managing VMs and is less cost-effective for unpredictable workloads than a serverless solution like Cloud Run.

---

## Question 30

*Domain 4: Integrating Applications with Google Cloud Services*

**Your team is responsible for developing services on Google Cloud. You're tasked with constructing a data processing service using Cloud Functions. However, the data being processed is sensitive, necessitating robust security measures. You must ensure that invocations originate only from authorized services, adhering to Google's recommended security practices for functions. What's the optimal approach to achieve this?**

- [x] III. Create a service account with the Cloud Functions Invoker role, and utilize that service account for invoking the function.
- [ ] II. Create a service account with the Cloud Functions Viewer role, and utilize that service account for invoking the function.
- [ ] I. Enable Identity-Aware Proxy in your project and secure function access using its permissions.
- [ ] IV. Generate an OAuth 2.0 client ID for your calling service within the same project as the function you intend to secure, and utilize those credentials for invoking the function.

### Explanation

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

---

## Question 31

*Domain 4: Integrating Applications with Google Cloud Services*

**Your operations team requires a script for listing Cloud Bigtable, Memorystore, and Cloud SQL databases within a project. The script should accommodate user-defined filter expressions to narrow down the presented results. How should you retrieve the data?**

- [ ] II. Employ the HBase API, Redis API, and MySQL connection to fetch database lists. Independently filter the results, then merge them for display.
- [x] IV. Execute `**gcloud bigtable instances list**`, `**gcloud redis instances list**`, and `**gcloud sql databases list**` commands. Apply the `**--filter**` flag with each command, then showcase the results.
- [ ] I. Utilize the HBase API, Redis API, and MySQL connection to fetch database lists. Merge the results and apply the filter for displaying.
- [ ] III. Execute `**gcloud bigtable instances list**`, `**gcloud redis instances list**`, and `**gcloud sql databases list**` commands. Implement a filter within the application, then showcase the results.

### Explanation

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

---

## Question 32

*Domain 3: Configuring and Deploying Applications*

**You manage a microservices application on Google Kubernetes Engine (GKE) using Istio. You secure the communication channels between your microservices by implementing an Istio AuthorizationPolicy, a Kubernetes NetworkPolicy, and mTLS on your GKE cluster. You discover that HTTP requests between two Pods to specific URLs fail, while other requests to other URLs succeed. What is the likely cause of the connection issue?**

- [x] III. The Authorization Policy within your cluster might be blocking HTTP requests for specific paths within your application.
- [ ] II. It's possible that the Pod initiating the HTTP requests is trying to connect to the target Pod via an incorrect TCP port.
- [ ] IV. The cluster might have mTLS configured in permissive mode, but the Pod's sidecar proxy could be transmitting unencrypted traffic in plain text, causing the failure.
- [ ] I. The Kubernetes NetworkPolicy resource is likely blocking HTTP traffic between the Pods for specific URLs.

### Explanation

**III. The Authorization Policy within your cluster might be blocking HTTP requests for specific paths within your application.**

**Explanation:**

  1. **Istio AuthorizationPolicy: Istio AuthorizationPolicy allows you to define fine-grained access control policies for services within your mesh. If certain HTTP requests between Pods are failing for specific URLs, it's possible that an AuthorizationPolicy is blocking access to those URLs. This could be due to misconfiguration or intentional access restrictions.**

Options I, II, and IV are less likely to be the cause of the connection issue:

I. While Kubernetes NetworkPolicy could potentially block HTTP traffic between Pods for specific URLs, it's less likely to be the cause of the issue if other HTTP requests to different URLs are succeeding. NetworkPolicy usually works at the network level and is not concerned with specific URLs.

II. If the Pod initiating the HTTP requests is trying to connect to the target Pod via an incorrect TCP port, it would likely result in a connection error or timeout rather than only affecting specific URLs.

IV. If mTLS is configured in permissive mode, it allows both encrypted and unencrypted traffic. However, this scenario is less likely to cause the failure of specific HTTP requests to certain URLs unless there's a specific rule or configuration related to those URLs causing the issue.

**References:**

[https://istio.io/latest/docs/tasks/security/authorization/authz-http/](https://istio.io/latest/docs/tasks/security/authorization/authz-http/  https://istio.io/latest/docs/ops/common-problems/network-issues/#sending-https-to-an-http-port  https://cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-security#authorization_policy_denial_logging)

[https://istio.io/latest/docs/ops/common-problems/network-issues/#sending-https-to-an-http-port](https://istio.io/latest/docs/tasks/security/authorization/authz-http/  https://istio.io/latest/docs/ops/common-problems/network-issues/#sending-https-to-an-http-port  https://cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-security#authorization_policy_denial_logging)

[https://cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-security#authorization_policy_denial_logging ](https://istio.io/latest/docs/tasks/security/authorization/authz-http/  https://istio.io/latest/docs/ops/common-problems/network-issues/#sending-https-to-an-http-port  https://cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-security#authorization_policy_denial_logging)

---

## Question 33

*Domain 2: Building and Testing Applications*

**Your application exhibits significantly slower performance after deployment to a Compute Engine instance, despite performing well during local testing. What is the recommended course of action to diagnose the issue?**

- [ ] II. Utilize Cloud Debugger snapshots to examine a specific moment in the application's execution.
- [x] III. Employ Cloud Profiler to identify the functions within the application consuming the most time.
- [ ] IV. Integrate logging commands within the application code and leverage Cloud Logging to pinpoint the source of latency issues.
- [ ] I. Submit a ticket to Cloud Support, highlighting the contrast in performance between local testing and deployment.

### Explanation

**III. Employ Cloud Profiler to identify the functions within the application consuming the most time.**

Why Profiling is the First Line of Defense:

  * **Pinpointing Bottlenecks:** Cloud Profiler excels at identifying performance-intensive areas within your code. This quickly focuses your investigation on the root cause, rather than just symptoms.

  * **Low Overhead:** It often works with minimal code changes. Profiling production environments gives the most realistic performance picture.

  * **Targeted Troubleshooting:** Knowing which functions are slow helps you determine _why_ they're slow (e.g., network calls, suboptimal algorithms, resource constraints on the VM).

When Other Options Become Relevant:

  * **II. Utilize Cloud Debugger snapshots ...** Debugger is great if you suspect the issue is related to incorrect application state or logic at specific points, but less likely to be the first step for _general_ slowness.

  * **IV. Integrate logging ... Cloud Logging ...** Logging is always useful, but if the core issue is a slow function, logs might show you the consequence of that (long requests), not the cause within the code itself.

  * **I. Submit a ticket to Cloud Support ...** Support can be helpful if the issue seems related to the underlying infrastructure (VM, network, etc.), but it's a good idea to gather performance data from your application first.

---

## Question 34

*Domain 3: Configuring and Deploying Applications*

**Your website resides on Compute Engine. The marketing team wishes to assess conversion rates across three different website designs. What method should you adopt?**

- [ ] IV. Deploy the website on Cloud Functions, dividing it into three distinct functions.
- [x] I. Host the website on App Engine and implement traffic splitting.
- [ ] II. Deploy the website on App Engine, dividing it into three separate services.
- [ ] III. Utilize Cloud Functions to host the website, employing traffic splitting.

### Explanation

**I. Host the website on App Engine and implement traffic splitting.**

**Explanation:**

App Engine is the most suitable choice for this scenario for several reasons:

  * **Traffic Splitting:** App Engine has built-in support for traffic splitting, allowing you to distribute traffic among different versions of your website (each with a different design) based on percentages you define.

  * **Scalability:** App Engine handles scaling automatically, ensuring your website can manage traffic surges during the experiment.

  * **Ease of Use:** App Engine provides a managed environment simplifying deployment and configuration.

**Why Other Options Are Less Suited:**

  * **II. Deploy the website on App Engine, dividing it into three separate services.** While technically possible, this adds unnecessary complexity to your setup and could potentially introduce inconsistencies across the separate services.

  * **III. Utilize Cloud Functions to host the website, employing traffic splitting.** Cloud Functions are better suited for individual, task-based functions rather than hosting entire websites. They lack the built-in traffic routing of App Engine.

  * **IV. Deploy the website on Cloud Functions, dividing it into three distinct functions.** Similar to option III, this approach fractures your website logic and introduces potential overhead in communication between the functions.

**References:**  
<https://cloud.google.com/appengine/docs/standard/python/splitting-traffic>

---

## Question 35

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Identify the reason for the non-linear scalability of Spanner performance during a load test for an ecommerce application that stores customer, order, and inventory data as relational tables within Cloud Spanner.**

- [ ] IV. Opting for the LIKE keyword over the STARTS_WITH keyword in parameterized SQL queries.
- [ ] II. Utilizing the STRING data type for arbitrary-precision values.
- [ ] I. Implementing 64-bit numeric types for 32-bit numbers.
- [x] III. Employing Version 1 UUIDs as primary keys, leading to monotonically increasing values.

### Explanation

**III. Employing Version 1 UUIDs as primary keys, leading to monotonically increasing values.**

Here's why:

  * **Spanner Distribution:** Spanner splits data into tablets and distributes them across servers for scalability. Monotonically increasing primary keys can lead to hotspotting, where inserts concentrate on a narrow range of tablets, affecting the load distribution and scalability.

Let's analyze the other options:

  * **I. Implementing 64-bit numeric types for 32-bit numbers.** While potentially less space-efficient, this alone is unlikely to cause significant scalability issues.

  * **II. Utilizing the STRING data type for arbitrary-precision values.** This can impact storage and query efficiency, but its effect on scalability is less direct compared to hotspotting.

  * **IV. Opting for the LIKE keyword over the STARTS_WITH keyword in parameterized SQL queries.** This would primarily affect query performance and less so Spanner's underlying scalability.

**References:**

[https://cloud.google.com/spanner/docs/schema-and-data-model#choosing_a_primary_key](https://cloud.google.com/spanner/docs/schema-and-data-model#choosing_a_primary_key  https://cloud.google.com/spanner/docs/schema-design#primary-key-prevent-hotspots)

[https://cloud.google.com/spanner/docs/schema-design#primary-key-prevent-hotspots](https://cloud.google.com/spanner/docs/schema-and-data-model#choosing_a_primary_key  https://cloud.google.com/spanner/docs/schema-design#primary-key-prevent-hotspots)

---

## Question 36

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Your team manages an application that aggregates news articles from various sources. The monitoring dashboard, which provides publicly accessible real-time reports, operates as a web application on a Compute Engine instance. External stakeholders and analysts require secure access to these reports without the need for authentication. How should you configure this secure channel?**

- [x] IV. Employ an HTTP(S) load balancer in front of the monitoring dashboard and configure it with a Google-managed SSL certificate for encrypting traffic.
- [ ] II. Utilize Cloud Scheduler to trigger Cloud Build hourly, creating an export from the reports, and store them in a public Cloud Storage bucket.
- [ ] III. Implement an HTTP(S) load balancer in front of the monitoring dashboard and configure Identity-Aware Proxy to secure the communication channel.
- [ ] I. Assign a public IP address to the instance and employ the service account key of the instance to encrypt traffic.

### Explanation

**IV. Employ an HTTP(S) load balancer in front of the monitoring dashboard and configure it with a Google-managed SSL certificate for encrypting traffic.**

Here's why this stands out:

  * **Publicly Accessible and Secure:** An HTTP(S) load balancer provides a public-facing endpoint while ensuring that all traffic to the monitoring dashboard is encrypted in transit with SSL/TLS.

  * **Managed Certificates:** Google-managed SSL certificates simplify setup and maintenance. They rotate automatically, ensuring security without manual intervention.

  * **Ease of Use:** This approach doesn't require complex setup or authentication mechanisms (like Identity-Aware Proxy), making it easy for external stakeholders to access the reports.

  * **Scalability:** If the demand for the reports grows, the load balancer can scale to handle the increased traffic.

**Why Other Options Are Less Ideal**

  * **I. Assign a public IP address to the instance and employ the service account key of the instance to encrypt traffic.**

    * This is insecure! Exposing a Compute Engine directly to the internet can create vulnerabilities. Also, managing encryption with service account keys adds unnecessary complexity.

  * **II. Utilize Cloud Scheduler to trigger Cloud Build hourly, creating an export from the reports, and store them in a public Cloud Storage bucket.**

    * This creates static reports, not a real-time monitoring dashboard as required by the scenario.

  * **III. Implement an HTTP(S) load balancer in front of the monitoring dashboard and configure Identity-Aware Proxy to secure the communication channel.**

    * Identity-Aware Proxy requires authentication, which you want to avoid for this publicly accessible dashboard.

References:

<https://cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs>

---

## Question 37

*Domain 3: Configuring and Deploying Applications*

**Your application is live in production, but certain issues only manifest once the new version starts receiving traffic from users. To mitigate both the impact and the number of users affected, which deployment strategy should you employ?**

- [ ] III. Rolling deployment
- [ ] IV. Recreate deployment
- [ ] I. Blue/green deployment
- [x] II. Canary deployment

### Explanation

**II. Canary deployment**

Here's why:

  * **Traffic Control:** Canary deployments allow you to route a small percentage of real user traffic to the new version, while the majority still gets routed to the stable version.

  * **Minimized Impact:** Any issues arising in the new version affect only a limited subset of users, reducing the overall impact on your application.

  * **Live Testing:** You can carefully monitor the new version under real-world conditions, detecting errors or performance issues before they affect your entire userbase.

  * **Gradual Rollout:** If the new version performs well, you can gradually increase the percentage of traffic routed to it, eventually replacing the old version.

**Why Other Options Are Less Ideal:**

  * **Blue/green deployment:** While offering a safe rollback option, blue/green involves switching entirely between versions. This lacks the gradual exposure offered by canary deployments when issues are subtle.

  * **Rolling deployment:** This sequentially updates instances, which can still affect a significant portion of users if an issue arises.

  * **Recreate deployment:** This has downtime involved and lacks the controlled testing that a canary deployment allows.

Ref:

[https://cloud.google.com/architecture/application-deployment-and-testing-strategies#canary_test_pattern](https://cloud.google.com/architecture/application-deployment-and-testing-strategies#canary_test_pattern  https://cloud.google.com/architecture/implementing-deployment-and-testing-strategies-on-gke#perform_a_bluegreen_deployment)

[https://cloud.google.com/architecture/implementing-deployment-and-testing-strategies-on-gke#perform_a_bluegreen_deployment](https://cloud.google.com/architecture/application-deployment-and-testing-strategies#canary_test_pattern  https://cloud.google.com/architecture/implementing-deployment-and-testing-strategies-on-gke#perform_a_bluegreen_deployment)

---

## Question 38

*Domain 4: Integrating Applications with Google Cloud Services*

**You have an HTTP Cloud Function that's triggered by POST requests. Each request contains a flat, unnested JSON structure with both numerical and textual data. Post-execution, the aggregated data must be promptly accessible for comprehensive analytics by multiple users concurrently. How should you store the submitted data persistently?**

- [ ] IV. Save each POST request's JSON data as an individual file within Cloud Storage, with the file name containing the request identifier.
- [ ] III. Process the JSON data from the POST request and store it in a regional Cloud SQL cluster.
- [x] II. Process the JSON data from the POST request and stream it into BigQuery.
- [ ] I. Directly persist each POST request's JSON data into Datastore.

### Explanation

**II. Process the JSON data from the POST request and stream it into BigQuery.** Here's why:

  * **Analytics Focus:** BigQuery is explicitly designed for large-scale data analysis and querying. It excels at handling structured data (even from flat JSON) and enables complex analysis with SQL-like queries.

  * **Real-Time Streaming:** BigQuery's streaming ingestion allows data to be made available for analytics almost immediately after it's received by your Cloud Function, minimizing latency.

  * **Scalability & Concurrent Access:** BigQuery handles massive datasets, and its serverless nature means it scales seamlessly to support many concurrent analysis requests.

Let's analyze the other options:

  * **I. Directly persist each POST request's JSON data into Datastore:** Datastore is a NoSQL database better suited for storing and retrieving individual data entities with relationships. While it can store JSON, it's less optimal for large-scale, ad-hoc analytics involving complex aggregations.

  * **III. Process the JSON data ... store it in a regional Cloud SQL cluster:** Cloud SQL (MySQL, PostgreSQL) are relational databases. While they can handle JSON, their strength lies in storing highly structured data with well-defined relationships, not in the type of flexible analytics needed here.

  * **IV. Save each POST request's JSON data as an individual file...** Cloud Storage is object storage. This approach creates overhead with individual files and makes analysis complex, requiring you to merge data across files before querying.

---

## Question 39

*Domain 3: Configuring and Deploying Applications*

**Your company's product team has introduced a new requirement, prompted by customer demand, to implement autoscaling for your stateless and distributed service operating within a Google Kubernetes Engine (GKE) cluster. Given the tight timeline of two weeks before this feature needs to be live, what would be the most suitable approach?**

- [ ] IV. Implement a Horizontal Pod Autoscaler, with scaling determined by a custom metric.
- [ ] II. Implement a Vertical Pod Autoscaler, with scaling determined by a custom metric.
- [x] III. Implement a Horizontal Pod Autoscaler, with scaling determined by the CPU load.
- [ ] I. Implement a Vertical Pod Autoscaler, with scaling determined by the CPU load.

### Explanation

**III. Implement a Horizontal Pod Autoscaler, with scaling determined by CPU load.**

**Explanation:**

Here's a breakdown of why this is the best choice, and why the other options are less ideal:

  * **Horizontal vs. Vertical Scaling:** Horizontal scaling (adding/removing replicas of your pods) is inherently better suited for distributed, stateless services than vertical scaling (changing resource allocation of existing pods). This is because horizontal scaling allows you to distribute load and handle more requests in parallel, a key goal of autoscaling.

  * **CPU Load vs. Custom Metrics:** While custom metrics can be valuable, using CPU load as the scaling metric has a significant advantage in this scenario - **speed of implementation**. You can set up a CPU-based Horizontal Pod Autoscaler (HPA) within minutes. Custom metrics usually require defining the metric, ensuring monitoring is in place, and potentially additional code changes.

**Why Other Options Aren't as Suitable**

  * **I. Vertical Pod Autoscaler (CPU Load):** While vertical scaling can handle increased load, it has limits. There comes a point where a single pod can't handle any more load, and horizontal scaling becomes necessary.

  * **II. Vertical Pod Autoscaler (Custom Metric):** VPA with custom metrics could be a good long-term solution, but the two-week deadline makes implementation difficult.

  * **IV. Horizontal Pod Autoscaler (Custom Metric):** This combines the potential complexity of custom metrics with horizontal scaling. While powerful, it's likely too complex for the timeframe.

Reference:

<https://cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautosc>aler

---

## Question 40

*Domain 2: Building and Testing Applications*

**Your company's development teams wish to employ Cloud Build in their projects to build and push Docker images to Container Registry. However, the operations team mandates that all Docker images must be published to a centralized and securely managed Docker registry they oversee. What's the best approach to address this requirement?**

- [x] II. Create a dedicated project for the operations team, equipped with Container Registry. Grant appropriate permissions to the Cloud Build service account in each developer team's project to enable access to the operations team's registry.
- [ ] III. Set up a separate project for the operations team, integrating Container Registry. Generate a Service Account for each development team and allocate necessary permissions to access the operations team's registry. Store the service account key file in the source code repository for authentication against the registry.
- [ ] I. Establish Container Registry within each development team's project. Configure Cloud Build builds to push Docker images to the respective project's registry. Provide the operations team access to each team's registry.
- [ ] IV. Deploy an open-source Docker Registry on a Compute Engine virtual machine instance within a distinct project for the operations team. Assign each development team a unique username and password, storing these credentials in the source code repository for authentication against the operations team's Docker registry.

### Explanation

**II. Create a dedicated project for the operations team, equipped with Container Registry. Grant appropriate permissions to the Cloud Build service account in each developer team's project to enable access to the operations team's registry.**

Here's why this approach excels:

  * **Centralization:** A single registry under the operations team's control provides a unified location for managing and governing Docker images.

  * **Security:** IAM permissions ensure fine-grained access control to the centralized registry, aligning with operational security requirements.

  * **Service Accounts:** Using the Cloud Build service account for authentication is streamlined and avoids the security risks of storing credentials in source code repositories.

  * **Maintainability:** Simplifies the setup and reduces complexity for development teams.

**Why Other Options Are Less Ideal:**

  * **I. Establish Container Registry within each development team's project ...** This creates management overhead for the operations team, who would have to maintain access to numerous registries.

  * **III. ... Generate a Service Account for each development team ...** Storing the key file in the repository is a significant security risk and creates more management complexity.

  * **IV. Deploy an open-source Docker Registry on a Compute Engine virtual machine instance ...** This increases operational overhead compared to using a managed service like Container Registry and introduces additional security considerations in self-managing a registry.

---

## Question 41

*Domain 3: Configuring and Deploying Applications*

**To ensure the security of a secret in your application deployed on a Google Kubernetes Engine (GKE) cluster, preventing its exposure via calls to the Kubernetes API server, what is the recommended approach?**

- [x] IV. Place the secret in Secret Manager, then establish a Google service account authorized to access the secret from Secret Manager. Generate a Kubernetes service account for the container, and employ Workload Identity to authenticate as the Google service account, ensuring protected access to the secret without vulnerability to Kubernetes API calls.
- [ ] II. Deploy GKE Application-layer Secrets Encryption on the cluster using a Cloud Key Management Service (KMS) key, guaranteeing that secrets are encrypted at the application layer, thereby averting exposure through API calls to the Kubernetes server.
- [ ] III. Safeguard the secret in Cloud KMS, then configure a Google service account with authorization to access the secret from Cloud KMS. Export the service account key in JSON format, and attach the JSON file to the container as a ConfigMap volume, enabling secure retrieval of the secret from Cloud KMS.
- [ ] I. Create a Kubernetes Secret and transmit the secret as an environment variable to the container, which could potentially risk exposing it through logs or other channels, thus jeopardizing its security.

### Explanation

The recommended approach to ensure the security of a secret in your application deployed on a Google Kubernetes Engine (GKE) cluster, preventing its exposure via calls to the Kubernetes API server, is:

**IV. Place the secret in Secret Manager, then establish a Google service account authorized to access the secret from Secret Manager. Generate a Kubernetes service account for the container, and employ Workload Identity to authenticate as the Google service account, ensuring protected access to the secret without vulnerability to Kubernetes API calls.**

Explanation:

  * Option IV suggests using Google Cloud's Secret Manager to store the secret, which is designed specifically for securely storing and managing secrets. By establishing a Google service account with appropriate permissions to access the secret from Secret Manager, and then using Workload Identity to authenticate as the Google service account, the application can securely retrieve the secret without directly exposing it to the Kubernetes API server.

  * Option I suggests transmitting the secret as an environment variable to the container, which can risk exposure through logs or other channels, making it less secure.

  * Option II mentions deploying GKE Application-layer Secrets Encryption, which can help encrypt secrets at the application layer, but it doesn't specifically address preventing exposure via calls to the Kubernetes API server.

  * Option III involves safeguarding the secret in Cloud KMS and configuring a service account to access it, but exporting the service account key as a JSON file and attaching it to the container as a ConfigMap volume might introduce additional security risks compared to using Secret Manager and Workload Identity.

Therefore, Option IV provides the most robust and secure approach for protecting secrets in a GKE environment.

**References:**

[https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity  https://cloud.google.com/kms/docs  https://kubernetes.io/docs/concepts/configuration/secret/  https://cloud.google.com/secret-manager/docs/overview)

[https://cloud.google.com/kms/docs](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity  https://cloud.google.com/kms/docs  https://kubernetes.io/docs/concepts/configuration/secret/  https://cloud.google.com/secret-manager/docs/overview)

[https://kubernetes.io/docs/concepts/configuration/secret/](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity  https://cloud.google.com/kms/docs  https://kubernetes.io/docs/concepts/configuration/secret/  https://cloud.google.com/secret-manager/docs/overview)

[https://cloud.google.com/secret-manager/docs/overview](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity  https://cloud.google.com/kms/docs  https://kubernetes.io/docs/concepts/configuration/secret/  https://cloud.google.com/secret-manager/docs/overview)

---

## Question 42

*Domain 3: Configuring and Deploying Applications*

**You've constructed multiple Cloud Functions in Java, accompanied by integration and service tests. Utilizing Cloud Build, you deploy these functions and initiate tests. However, your Cloud Build job flags deployment failures right after validating the code. What steps should you take to address this issue?**

- [ ] I. Review the maximum number of Cloud Function instances.
- [x] IV. Confirm that the Cloud Build service account holds the Cloud Functions Developer role.
- [ ] III. Attempt the tests again, employing the truncated exponential backoff polling strategy.
- [ ] II. Ensure that your Cloud Build trigger is configured with accurate build parameters.

### Explanation

**Correct Option:**

**IV. Confirm that the Cloud Build service account holds the Cloud Functions Developer role.**

**Justification:**

  * **Importance of Service Account Permissions:** Cloud Functions deployment involves resource creation and modification, permissions for which are held by service accounts. The Cloud Functions Developer role is specifically designed to provide the essential set of permissions for Cloud Functions management and deployment. If the Cloud Build service account lacks this role, it won't have adequate authorization, thus impeding the deployment process even if the code itself is valid.

**Why Other Options Are Unsuitable:**

  * **I. Review the maximum number of Cloud Function instances:** While important for scalability and cost management, this wouldn't prevent a deployment failure right after code validation.

  * **II. Ensure that your Cloud Build trigger is configured with accurate build parameters:** Incorrect build parameters might lead to issues in the build process, but the question implies the failure occurs during deployment specifically, pointing towards a permissions problem.

  * **III. Attempt the tests again, employing the truncated exponential backoff polling strategy.:** This approach addresses transient errors but wouldn't resolve a fundamental lack of permissions in the service account.

**References:**

[https://cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account#granting_a_role_using_the_iam_page https://cloud.google.com/build/docs/troubleshooting#build_trigger_fails_due_to_missing_cloudbuildbuildscreate_permission](https://cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account#granting_a_role_using_the_iam_page   https://cloud.google.com/build/docs/troubleshooting#build_trigger_fails_due_to_missing_cloudbuildbuildscreate_permission  https://cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account)

[https://cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account](https://cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account#granting_a_role_using_the_iam_page   https://cloud.google.com/build/docs/troubleshooting#build_trigger_fails_due_to_missing_cloudbuildbuildscreate_permission  https://cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account)

---

## Question 43

*Domain 3: Configuring and Deploying Applications*

**How should you implement a solution on Google Kubernetes Engine to configure each microservice with a specific number of replicas and ensure uniform addressing within the cluster?**

- [ ] D. Deploying microservices as Pods without leveraging Deployments can hinder scalability and management. Expose the Pods within the cluster using an Ingress, and depend on the Ingress IP address for addressing, potentially leading to inconsistent access as the number of replicas scales.
- [ ] C. Directly deploying each microservice as a Pod limits scalability and management capabilities. Expose the Pods within the cluster through a Service, and utilize the Service DNS name for addressing, ensuring uniform access from other microservices within the cluster.
- [x] A. Deploy each microservice as a Deployment, which facilitates easy scaling and replica management. Expose the Deployment within the cluster via a Service, and utilize the Service DNS name for addressing the microservices from other microservices, ensuring consistent access regardless of the number of replicas.
- [ ] B. Use Deployments for each microservice to manage replicas efficiently. Expose the Deployments within the cluster using an Ingress, and use the Ingress IP address to address the microservices from other microservices within the cluster, maintaining a consistent addressing mechanism despite replica scaling.

### Explanation

The correct option is:

**A. Deploy each microservice as a Deployment, which facilitates easy scaling and replica management. Expose the Deployment within the cluster via a Service, and utilize the Service DNS name for addressing the microservices from other microservices, ensuring consistent access regardless of the number of replicas.**

Explanation:

  * Option A suggests using Deployments for each microservice, which allows easy scaling and management of replicas. Services should be used to expose the Deployments within the cluster. This ensures that the microservices can be addressed consistently using the Service DNS name regardless of the number of replicas. This approach provides uniform addressing within the cluster.

  * Option B suggests using Ingress to expose the Deployments within the cluster, but Ingress is typically used for routing external traffic to services within the cluster, not for internal communication between microservices.

  * Option C recommends directly deploying each microservice as a Pod, which limits scalability and management capabilities compared to using Deployments. While it suggests exposing the Pods within the cluster through a Service, it doesn't mention utilizing Service DNS for addressing, which could lead to inconsistent access.

  * Option D also suggests deploying microservices as Pods without leveraging Deployments, which hinders scalability and management. Additionally, using Ingress for addressing internal services is not a recommended practice and can lead to inconsistent access, especially as the number of replicas scales.

Therefore, Option A is the most suitable approach for configuring each microservice with a specific number of replicas and ensuring uniform addressing within the cluster.

References:

<https://cloud.google.com/kubernetes-engine/docs/concepts/service>

---

## Question 44

*Domain 4: Integrating Applications with Google Cloud Services*

**You're developing a microservice-based application intended for deployment on a Google Kubernetes Engine cluster. This application requires both reading from and writing to a Spanner database. Your objective is to ensure adherence to security best practices while minimizing code adjustments. How should you configure the application to access Spanner credentials?**

- [ ] IV. Safeguard the application credentials using Cloud Key Management Service and retrieve them as needed when establishing a database connection.
- [ ] III. Configure suitable routing rules and utilize a VPC-native cluster to establish a direct connection to the database.
- [ ] II. Protect the application credentials as Kubernetes Secrets and expose them as environment variables.
- [x] I. Establish the required service accounts and employ Workload Identity to execute the pods.

### Explanation

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

---

## Question 45

*Domain 2: Building and Testing Applications*

**As the sole developer available over the weekend, your manager tasks you with making an emergency update to a website for your startup's web development team. Your development environment relies on Google Cloud services like Cloud Storage and Cloud Build, with version control managed through Git. Without your work laptop, you cannot store source code locally on a non-corporate computer. How should you configure your developer environment?**

- [ ] IV. Store the necessary source code in a Cloud Storage bucket. Mount the bucket as a drive on a public computer and use a code editor to make the required updates. Enable versioning for the bucket and link it to the team's Git repository.
- [ ] I. Utilize a text editor and Git command line to submit source code updates as pull requests from a public computer.
- [ ] II. Employ a text editor and Git command line to submit source code updates as pull requests from a virtual machine running on a public computer.
- [x] III. Utilize Cloud Shell and its built-in code editor for development tasks, sending source code updates as pull requests.

### Explanation

**III. Utilize Cloud Shell and its built-in code editor for development tasks, sending source code updates as pull requests.**

Here's why this is the best choice:

  * **Accessibility:** Cloud Shell is readily available from any modern web browser, eliminating the need to install software locally.

  * **Cloud Integration:** Cloud Shell provides integrated access to your GCP project's resources, including Cloud Storage, Cloud Build, and your Git repository.

  * **Security:** Your code stays within the secure Google Cloud environment. You don't risk storing sensitive source code on a public computer.

  * **Familiar Tools:** Cloud Shell's code editor and command-line tools provide a familiar development experience.

**Why other options have issues:**

  * **I. Public Computer (Basic Text Editor + Git):**

    * **Security Risk:** Storing or cloning the project on a public computer compromises the security of your source code.

    * **Limited Tools:** Basic text editors may lack the features you need for effective development.

  * **II. Public Computer (VM + Text Editor + Git):**

    * **Complexity:** Requires setting up a VM, which adds overhead and time pressure to your task.

    * **Security Risk:** Still introduces the security concerns of storing code on a public machine.

  * **IV. Cloud Storage Mount with Versioning:**

    * **Not ideal for Git:** While versioning helps, managing a Git project this way is cumbersome and prone to errors.

    * **Local Editing:** Still requires a capable code editor on the public computer.

**Reference:**

<https://cloud.google.com/shell/docs>

---

## Question 46

*Domain 3: Configuring and Deploying Applications*

**After deploying your application on Google Kubernetes Engine, you now seek the capability to swiftly revert to the prior version if complications arise with the new release. Which deployment model is most suitable for your scenario?**

- [x] III. Opt for a blue/green deployment strategy and test the new application after the deployment process is finalized.
- [ ] II. Implement A/B testing and periodically test the application after integrating the new features.
- [ ] I. Execute a rolling deployment and conduct testing of the new application post-deployment completion.
- [ ] IV. Employ a canary deployment approach and periodically test the new application after deploying the updated version.

### Explanation

**III. Opt for a blue/green deployment strategy and test the new application after the deployment process is finalized.**

**Justification:**

  * **Swift Rollback:** Blue/green deployments offer a core advantage – the ability to quickly switch back to the previous version (blue) if the new version (green) exhibits issues. This aligns directly with your need for rapid reversions.

  * **Complete Pre-Release Testing:** Before switching traffic to the new version, the blue/green strategy allows for comprehensive testing of the new application in a production-like environment. This minimizes the risk of surprises.

  * **Clear Separation:** This model maintains two separate environments (blue and green), reducing the risk of interference between old and new versions during testing.

**Why Other Options are Less Ideal:**

  * **I. Execute a rolling deployment and conduct testing of the new application post-deployment completion.** While rolling updates are effective for gradual rollout, if issues are found after the deployment is complete, rollback can be more complex and disruptive.

  * **II. Implement A/B testing and periodically test the application after integrating the new features.** A/B testing focuses primarily on comparing versions for user experience or conversion purposes. It doesn't inherently provide the quick, full rollback mechanism of blue/green.

  * **IV. Employ a canary deployment approach and periodically test the new application after deploying the updated version.** Canary deployments help with gradual rollout and testing but introduce an additional layer of complexity if you need a swift, complete rollback.

**Reference:**

<https://cloud.google.com/architecture/application-deployment-and-testing-strategies#choosing_the_right_strategy>

---

## Question 47

*Domain 4: Integrating Applications with Google Cloud Services*

**As you develop a Compute Engine-hosted application in project A, you need to establish secure authentication to a Cloud Pub/Sub topic in project B. What should be your approach?**

- [x] II. Equip the instances with a service account from project A, and authorize this service account as a publisher directly on the Cloud Pub/Sub topic.
- [ ] IV. Utilize Application Default Credentials with the private key of a service account from project A, and designate this service account as a publisher directly on the Cloud Pub/Sub topic in project B.
- [ ] I. Set up the instances with a service account from project B, then grant this service account publisher permissions on the Cloud Pub/Sub topic in project A.
- [ ] III. Configure Application Default Credentials to utilize the private key of a service account from project B, and assign this service account publisher rights in project A's Cloud Pub/Sub.

### Explanation

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

---

## Question 48

*Domain 4: Integrating Applications with Google Cloud Services*

**You aim to move files from an on-premises virtual machine to Google Cloud Storage for utilization within a Cloud DataProc Hadoop cluster in a GCP environment. Which command is the appropriate choice for this task?**

- [x] I. `**gsutil cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/**`
- [ ] IV. `**gcloud dataproc cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/**`
- [ ] II. `**gcloud cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/**`
- [ ] III. `**hadoop fs cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/**`

### Explanation

**I. gsutil cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/**

**Explanation:**

  * `gsutil` is the command-line tool specifically designed to interact with Google Cloud Storage. It's the most efficient and reliable way to transfer files between your local machine and Google Cloud Storage buckets.

**Why Other Options Are Not Suitable:**

  * **II. gcloud cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/** While the `gcloud` tool has a `cp` command, it's intended for more general-purpose copying operations within the Google Cloud environment. For interacting specifically with Cloud Storage, `gsutil` is the preferred tool.

  * **III. hadoop fs cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/** The `hadoop fs` command with a `gs://` destination can work, but it requires the Google Cloud Storage connector for Hadoop. This adds a layer of setup and might be less efficient than using `gsutil` directly.

  * **IV. gcloud dataproc cp [LOCAL_OBJECT] gs://[DESTINATION_BUCKET_NAME]/** The `gcloud dataproc` tool doesn't have a `cp` command. It's designed for managing Cloud Dataproc clusters, not general data transfer tasks.

Ref:

<https://cloud.google.com/storage/docs/uploading-objects>

---

## Question 49

*Domain 2: Building and Testing Applications*

**To efficiently scan container images for Common Vulnerabilities and Exposures (CVEs) without impeding software development agility using managed services, which approach should you take?**

- [x] A. Activate the Container Analysis API to conduct vulnerability scans on images stored in Artifact Registry, enabling seamless integration of vulnerability scanning into the container image management workflow.
- [ ] D. Utilize Cloud Monitoring to evaluate the outcomes of Cloud Build and identify if a vulnerable version has been utilized, which may provide insights into potential vulnerabilities but does not offer direct vulnerability scanning of container images.
- [ ] C. Restrict the usage of non-commercially supported base images within your development environment, which is a proactive measure but does not address the need for automated vulnerability scanning.
- [ ] B. Establish a Cloud Run service triggered by code check-ins to scan the code for CVEs, which may offer continuous monitoring but might not directly address vulnerabilities within container images.

### Explanation

The most efficient approach to scan container images for Common Vulnerabilities and Exposures (CVEs) without impeding software development agility using managed services is:

**A. Activate the Container Analysis API to conduct vulnerability scans on images stored in Artifact Registry, enabling seamless integration of vulnerability scanning into the container image management workflow.**

Explanation:

  * Option A suggests activating the Container Analysis API to conduct vulnerability scans on images stored in Artifact Registry. This approach directly addresses the need for automated vulnerability scanning of container images within the container image management workflow. It seamlessly integrates vulnerability scanning without impeding software development agility.

  * Option B involves establishing a Cloud Run service triggered by code check-ins to scan the code for CVEs. While continuous monitoring is valuable, this approach does not directly address vulnerabilities within container images, which are a crucial aspect of container security.

  * Option C proposes restricting the usage of non-commercially supported base images within the development environment as a proactive measure. While this is important for security, it does not automate vulnerability scanning of container images, which is necessary for efficient and timely detection of vulnerabilities.

  * Option D suggests utilizing Cloud Monitoring to evaluate the outcomes of Cloud Build and identify if a vulnerable version has been utilized. While this provides insights into potential vulnerabilities, it does not offer direct vulnerability scanning of container images as requested.

Therefore, Option A provides the most efficient approach by seamlessly integrating vulnerability scanning into the container image management workflow using managed services.

**References:**

[https://cloud.google.com/container-registry/docs/get-image-vulnerabilities#viewing_vulnerabilities_and_other_occurrences](https://cloud.google.com/container-registry/docs/get-image-vulnerabilities#viewing_vulnerabilities_and_other_occurrences  https://cloud.google.com/container-registry/docs/container-analysis)

[https://cloud.google.com/container-registry/docs/container-analysis](https://cloud.google.com/container-registry/docs/get-image-vulnerabilities#viewing_vulnerabilities_and_other_occurrences  https://cloud.google.com/container-registry/docs/container-analysis)

---

## Question 50

*Domain 4: Integrating Applications with Google Cloud Services*

**Your application collects user input and publishes it to the user's contacts. This input is stored in a Cloud Spanner table. Given that your application prioritizes latency over consistency, how should you handle reads from Cloud Spanner?**

- [x] II. Conduct stale reads using single-read methods.
- [ ] IV. Carry out stale reads using read-write transactions.
- [ ] III. Execute strong reads using single-read methods.
- [ ] I. Perform Read-Only transactions.

### Explanation

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

---

## Question 51

*Domain 4: Integrating Applications with Google Cloud Services*

**How can you enable your application, developed within Google Kubernetes Engine (GKE), to access Google Cloud services across various projects?**

- [ ] IV. Utilize GKE role-based access control (RBAC) with a designated Google service account.
- [ ] I. Configure a Google service account for the GKE nodes.
- [ ] III. Securely store the Google service account credentials within a Kubernetes Secret.
- [x] II. Implement Workload Identity with a designated Google service account for running the Pod.

### Explanation

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

---

## Question 52

*Domain 3: Configuring and Deploying Applications*

**In your role as a developer collaborating with the CI/CD team, you're tasked with troubleshooting a new feature recently introduced by your team. Utilizing HashiCorp Packer, the CI/CD team created a new Compute Engine image from your development branch. Despite a successful build, the image fails to boot up. What's the appropriate step to investigate the issue with the CI/CD team?**

- [ ] I. Initiate a new feature branch and request the build team to recompile the image.
- [ ] III. Install Packer on your local environment, build the Compute Engine image locally, and then test it within your personal Google Cloud project.
- [x] IV. Analyze the Compute Engine OS logs via the serial port and verify access to the serial port by examining the Cloud Logging logs.
- [ ] II. Halt the deployed virtual machine, export the disk, and subsequently mount the disk locally to access the boot logs.

### Explanation

**IV. Analyze the Compute Engine OS logs via the serial port and verify access to the serial port by examining the Cloud Logging logs.**

Here's why this is the best approach:

  * **Direct Problem Diagnosis:** The serial port provides access to boot logs generated by the operating system installed on the image. These logs frequently reveal the root cause of boot failures.

  * **Cloud Logging Integration:** Cloud Logging captures serial port output, making it easy to access and analyze the logs even if the VM doesn't fully boot.

  * **Troubleshooting Focus:** This approach focuses on identifying the source of the issue, allowing for a targeted fix.

**Why Other Options Are Less Ideal:**

  * **I. New Feature Branch:** This might be necessary later but is premature without identifying the root cause of the issue.

  * **II. Mounting the Disk:** While potentially useful, this is more complex than accessing serial port logs and might not reveal the issue if it's related to early boot processes.

  * **III. Replicating Locally:** This could be helpful but may not fully reproduce the CI/CD team's environment and can be time-consuming.

**References:**  
[https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console](https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console  https://cloud.google.com/compute/docs/troubleshooting/vm-startup#identify_the_reason_why_the_boot_disk_isnt_booting)

[https://cloud.google.com/compute/docs/troubleshooting/vm-startup#identify_the_reason_why_the_boot_disk_isnt_booting](https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console  https://cloud.google.com/compute/docs/troubleshooting/vm-startup#identify_the_reason_why_the_boot_disk_isnt_booting)

---

## Question 53

*Domain 3: Configuring and Deploying Applications*

**You're managing an analytics application that executes numerous queries on BigQuery via the BigQuery API at regular intervals. How can you determine the execution time of these queries?**

- [x] IV. Utilize Stackdriver Monitoring to monitor query execution times.
- [ ] I. Utilize Stackdriver Monitoring to visualize slot usage.
- [ ] III. Utilize Stackdriver Trace to monitor query execution time.
- [ ] II. Employ Stackdriver Trace to track API execution time.

### Explanation

**IV. Utilize Stackdriver Monitoring to monitor query execution times.**

Here's why:

  * **Query-Centric Metrics:** Stackdriver Monitoring (now called Cloud Monitoring) provides metrics specifically tailored to BigQuery, including query execution time. Using it allows you to track and visualize this information as time-series data.

  * **Alerts and Analysis:** You can set alerts based on query execution time thresholds and analyze trends over time to identify performance bottlenecks.

  * **BigQuery Integration:** These metrics are collected directly from BigQuery by Stackdriver Monitoring.

**Why Other Options Are Not Ideal**

  * **I. Utilize Stackdriver Monitoring to visualize slot usage.** Slot usage shows your BigQuery query resource utilization, which can _indirectly_ relate to performance, but isn't a direct measure of execution time.

  * **II & III. Utilize Stackdriver Trace...** Stackdriver Trace is primarily used for distributed tracing and performance profiling within applications. While you might instrument your application code to include parts that interact with BigQuery, it's unnecessary overhead for simply measuring query execution time.

**Reference** :

<https://cloud.google.com/bigquery/docs/monitoring>

---

## Question 54

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**In developing an application to handle sensitive unstructured data objects stored in a Cloud Storage bucket, you must ensure compliance with regulatory mandates dictating that all data objects remain accessible for a minimum of 7 years from their inception. However, objects older than 3 years are rarely accessed. Your objective is to configure object storage while optimizing storage costs. What actions should you take? (Select two.)**

- [ ] II. Utilize IAM Conditions to grant access to objects based on a 7-year period following object creation.
- [x] IV. Establish an object lifecycle policy on the bucket to transition objects from Standard Storage to Archive Storage after 3 years.
- [ ] III. Enable Object Versioning to safeguard objects against accidental deletion for 7 years after their creation.
- [x] I. Implement a retention policy on the bucket with a duration of 7 years.
- [ ] V. Develop a Cloud Function to assess the age of each object in the bucket and relocate objects older than 3 years to a second bucket employing the Archive Storage class. Employ Cloud Scheduler to trigger the Cloud Function on a daily basis.

### Explanation

The two best actions to take in this scenario are:

  * **I. Implement a retention policy on the bucket with a duration of 7 years.**

  * **IV. Establish an object lifecycle policy on the bucket to transition objects from Standard Storage to Archive Storage after 3 years.**

Here's the breakdown:

**Why these options are essential:**

  * **I. Regulatory Compliance:** A 7-year retention policy directly addresses the mandatory requirement to keep data accessible for a minimum of 7 years, ensuring your application remains compliant.

  * **IV. Cost Optimization:** Object lifecycle management transitions infrequently used objects (older than 3 years) to the more cost-effective Archive Storage class, reducing your storage bill without sacrificing data access.

**Why other options aren't as suitable:**

  * **II. Utilize IAM Conditions to grant access to objects based on a 7-year period following object creation.**

    * IAM Conditions control access but don't guarantee the data will be retained or prevent accidental deletion.

  * **III. Enable Object Versioning to safeguard objects against accidental deletion for 7 years after their creation.**

    * Object Versioning offers a powerful safeguard, but it might increase storage costs due to the retention of previous versions. Also, it doesn't directly address the need for cost optimization through tiered storage.

  * **V. Custom Cloud Function & Scheduler**

    * While technically feasible, this introduces complexity and development overhead compared to native Object Lifecycle Management's built-in functionality.

Ref:

<https://cloud.google.com/storage/docs/bucket-lock>

---

## Question 55

*Domain 4: Integrating Applications with Google Cloud Services*

**Which tool should you employ to construct an architecture that authenticates, enforces quotas, and tracks metrics for API callers?**

**

**

**Diagram showing a Google Cloud architecture. An arrow from a “computer” to “Cloud Load Balancing”. An arrow from “Cloud Load Balancing” to an empty box. An arrow from the empty box to “PHP application”.**

- [ ] C. Consider Identity-Aware Proxy (IAP) for securing your APIs by verifying user identities and controlling access based on their permissions, while also offering features for monitoring and reporting API usage metrics.
- [ ] D. Leverage GKE Ingress for HTTP(S) Load Balancing to configure routing rules and manage traffic efficiently to your PHP application, while incorporating additional layers of security and metrics reporting as per your requirements.
- [x] B. Choose Cloud Endpoints to streamline the process of building, deploying, and managing APIs with robust security features, including authentication mechanisms, quota enforcement capabilities, and comprehensive metric tracking for API usage.
- [ ] A. Opt for Cloud Run to establish a scalable and fully managed environment for deploying containerized applications, ensuring efficient execution and seamless integration with authentication, quota enforcement, and metric reporting functionalities.

### Explanation

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

---

## Question 56

*Domain 3: Configuring and Deploying Applications*

**Your application deployed on Compute Engine is encountering persistent failures with a limited number of requests. Upon investigation, you've identified the problem to a particular Compute Engine instance. However, SSH access to the instance is unresponsive. What should be your next course of action?**

- [ ] IV. Capture a disk snapshot and link it to a new instance.
- [ ] I. Restart the machine.
- [x] II. Activate and inspect the serial port output.
- [ ] III. Terminate the instance and create a replacement.

### Explanation

The best course of action in this scenario would be to:

**II. Activate and inspect the serial port output.**

Here's why:

  * **Unresponsive SSH:** This indicates a potential issue at the operating system level or deeper. Inspecting the serial port output can provide valuable insights into the underlying problem, such as kernel panics, boot failures, or other critical errors that might not be visible through other means.

  * **Limited Impact:** The problem is isolated to a single instance, so actions like restarting the machine or terminating it might disrupt the service unnecessarily.

  * **Diagnosis First:** Before taking any drastic action, it's crucial to understand the root cause of the failure. The serial port output can help diagnose the problem accurately, allowing you to take targeted corrective measures.

**Other options and why they might not be the best first step:**

  * **I. Restart the machine:** This might temporarily resolve the issue if it's a minor glitch, but it won't help diagnose the underlying problem, and the issue could recur.

  * **III. Terminate the instance and create a replacement:** This is a more drastic step that should be considered only after exhausting other troubleshooting options. It might lead to data loss if not handled carefully.

  * **IV. Capture a disk snapshot and link it to a new instance:** This is a good practice for preserving data, but it doesn't address the root cause of the failure. The new instance might encounter the same problem if the underlying issue is not resolved.

**In summary, activating and inspecting the serial port output is the most logical first step to diagnose the problem on the unresponsive Compute Engine instance.**

---

## Question 57

*Domain 4: Integrating Applications with Google Cloud Services*

**To ensure proper authentication of services accessing various Google Cloud APIs within a Google Kubernetes Engine (GKE) cluster, adhering to Google's recommended best practices, which approaches should you implement? (Choose two)**

- [x] V. Utilize gcloud to bind Google service accounts and Kubernetes service accounts using roles/iam.workloadIdentityUser, which is a feasible approach but not as endorsed as enabling Workload Identity directly on the cluster.
- [ ] IV. Storing Google service account keys in Secret Manager (as mentioned) could be a method, but it's not a recommended best practice by Google for authenticating services within a GKE cluster.
- [ ] I. Employ the service account linked to the GKE node, enabling services to authenticate with Google Cloud APIs using the node's identity.
- [ ] III. Accessing Google service account keys from Secret Manager (as mentioned) could be a method, but it's not a recommended best practice by Google for authenticating services within a GKE cluster.
- [x] II. Enable Workload Identity on the cluster through the gcloud command-line tool, establishing a secure mechanism for workloads operating in the cluster to access Google Cloud services with fine-grained IAM permissions.

### Explanation

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

---

## Question 58

*Domain 2: Building and Testing Applications*

**In order to assess whether the web application running on Google Kubernetes Engine is susceptible to cross-site scripting (XSS) attacks or if it utilizes libraries with known vulnerabilities, which service should you employ?**

- [ ] I. Google Cloud Armor
- [ ] IV. Error Reporting
- [ ] II. Debugger
- [x] III. Web Security Scanner

### Explanation

**The most suitable option in this case is:**

  * **III. Web Security Scanner**

**Explanation:**

  * **Designed for Vulnerability Detection:** Web Security Scanner is specifically designed to find web application vulnerabilities, including XSS and those caused by outdated libraries with known flaws.

  * **Active Assessment:** It thoroughly examines your application, simulating attacks and analyzing the results to uncover potential attack vectors.

  * **Comprehensive Reports:** It provides detailed reports outlining vulnerabilities, making it easier to focus your remediation efforts.

**Why Other Options Are Less Ideal:**

  * **I. Google Cloud Armor:** Google Cloud Armor is a Web Application Firewall (WAF). While important for defense, it mainly protects against already-known attack patterns. It doesn't actively scan for new vulnerabilities like a dedicated security scanner.

  * **II. Debugger:** A debugger is a development tool used to troubleshoot code problems. It's not designed for proactive vulnerability detection.

  * **IV. Error Reporting:** Error logs can sometimes reveal issues caused by XSS attempts, but this is more of an indirect and reactive approach. Monitoring errors is helpful, but doesn't replace a proactive vulnerability scanner.

Ref:

<https://cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview>

---

## Question 59

*Domain 2: Building and Testing Applications*

**You have developed a new application and aim to deploy it on Cloud Run without utilizing a Dockerfile. Your organization mandates that all container images are stored in a centrally managed container repository. Which approach should you take to construct your container using Google Cloud services? (Select two.)**

- [ ] I. Upload your source code to Artifact Registry.
- [x] III. Utilize the pack build command through pack CLI.
- [x] IV. Incorporate the --source flag within the gcloud run deploy CLI command.
- [ ] V. Add the --platform=kubernetes flag within the gcloud run deploy CLI command.
- [ ] II. Initiate a Cloud Build job for image pushing.

### Explanation

The two correct answers are:

  * **III. Utilize the pack build command through the pack CLI.**

  * **IV. Incorporate the --source flag within the gcloud run deploy CLI command.**

Here's why these choices work together, and why the others aren't suitable:

**III. Using the pack build command:**

  * **Buildpacks:** This command leverages Cloud Native Buildpacks, which automatically examine your source code and detect the appropriate language/framework. Buildpacks then handle the construction of the container image for you, eliminating the need for a Dockerfile.

  * **Pushing to Repository:** The `pack build` command can directly push the built container image to a supported registry, like Artifact Registry, satisfying your organization's central repository requirement.

**IV. Using the gcloud run deploy --source flag:**

  * **Direct Source Deployment:** This flag allows you to deploy your application code directly to Cloud Run. Cloud Build will be triggered under the hood, utilizing Buildpacks to create a container image from your source code.

  * **Automated Repository Storage:** Cloud Build automatically stores the resulting image in a compatible container repository (such as Artifact Registry).

**Why other options aren't correct:**

  * **I. Upload your source code to Artifact Registry.** While Artifact Registry is the right place to store images, simply uploading source code does not create a container image.

  * **II. Initiate a Cloud Build job for image pushing.** You'd need a container image to begin with for Cloud Build to push; this option doesn't address image creation.

  * **V. Add the --platform=kubernetes flag within the gcloud run deploy CLI command.** This flag is used to manage Cloud Run deployments for Kubernetes environments and isn't relevant to building a container image without a Dockerfile.

References:

<https://cloud.google.com/blog/products/containers-kubernetes/google-cloud-now-supports-buildpacks>

---

## Question 60

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**What is the optimal approach to develop and deploy a web application on Google Cloud, considering unpredictable traffic patterns and cost minimization?**

- [ ] B. Develop the application using Firestore as the database and deploy it to a Google Kubernetes Engine (GKE) Standard cluster, providing flexibility and scalability but potentially leading to higher operational costs compared to serverless options.
- [ ] C. Develop the application using Cloud SQL as the database and deploy it to a Google Kubernetes Engine Autopilot cluster, which automatically manages and scales the underlying infrastructure, optimizing costs while ensuring scalability.
- [ ] D. Develop the application using Firestore as the database and deploy it to a Compute Engine managed instance group with autoscaling, which offers scalability but may involve more operational overhead and potentially higher costs compared to serverless options like Cloud Run.
- [x] A. Develop the application using Firestore as the database and deploy it to Cloud Run, which offers serverless scaling to handle varying traffic loads efficiently while minimizing costs.

### Explanation

The optimal approach to develop and deploy a web application on Google Cloud, considering unpredictable traffic patterns and cost minimization, is:

**A. Develop the application using Firestore as the database and deploy it to Cloud Run, which offers serverless scaling to handle varying traffic loads efficiently while minimizing costs.**

Explanation:

  * Option A suggests developing the application using Firestore as the database, which is a scalable and managed NoSQL database service provided by Google Cloud. Deploying the application to Cloud Run leverages serverless computing, which automatically scales the application up or down based on traffic demand, ensuring optimal resource utilization and minimizing costs during periods of low traffic.

  * Cloud Run offers a pay-per-use pricing model, where you only pay for the resources consumed during the execution of your application, making it cost-effective for applications with unpredictable traffic patterns.

  * Option B involves deploying the application to a Google Kubernetes Engine (GKE) Standard cluster. While GKE provides flexibility and scalability, managing a Kubernetes cluster may lead to higher operational costs and complexity compared to serverless options like Cloud Run.

  * Option C suggests deploying the application to a Google Kubernetes Engine Autopilot cluster, which automatically manages and scales the underlying infrastructure. While Autopilot optimizes costs and ensures scalability, it may not offer the same level of simplicity and cost-effectiveness as Cloud Run for applications with unpredictable traffic.

  * Option D involves deploying the application to a Compute Engine managed instance group with autoscaling. While this offers scalability, it may involve more operational overhead and potentially higher costs compared to serverless options like Cloud Run.

Therefore, Option A, deploying the application to Cloud Run with Firestore as the database, is the most optimal approach for handling unpredictable traffic patterns while minimizing costs.

**References:**

[https://cloud.google.com/serverless-options](https://cloud.google.com/serverless-options  https://cloud.google.com/appengine/docs/the-appengine-environments  https://cloud.google.com/run)

[https://cloud.google.com/appengine/docs/the-appengine-environments](https://cloud.google.com/serverless-options  https://cloud.google.com/appengine/docs/the-appengine-environments  https://cloud.google.com/run)

[https://cloud.google.com/run](https://cloud.google.com/serverless-options  https://cloud.google.com/appengine/docs/the-appengine-environments  https://cloud.google.com/run)

---
