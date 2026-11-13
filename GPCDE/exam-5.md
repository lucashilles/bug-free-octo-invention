# Professional Cloud Developer — Practice Exam 5

60 questions.

## Question 1

*Domain 4: Integrating Applications with Google Cloud Services*

**Your application stores customer content in a Cloud Storage bucket, encrypting each object with the respective customer's encryption key. However, an HTTP 4xx error occurs while attempting to read an object from Cloud Storage. What could be a potential reason for this error?**

- [ ] IV. The read operation utilized the base64-encoded SHA256 hash of the customer's encryption key for accessing the object.
- [ ] III. The encryption algorithm specified by the customer was not accurately applied during the read operation.
- [x] II. The read operation lacked the inclusion of the base64-encoded SHA256 hash of the encryption key.
- [ ] I. The read operation was performed using the customer's encryption key encoded in base64.

### Explanation

**Most Likely Cause:**

  * **II. The read operation lacked the inclusion of the base64-encoded SHA256 hash of the encryption key.** When using Customer-Supplied Encryption Keys (CSEK) with Cloud Storage, you must provide the SHA256 hash of the encryption key along with the base64-encoded key itself to read the object. This hash serves as an integrity check.

**Other Potential (But Less Likely) Causes:**

  * **III. The encryption algorithm specified by the customer was not accurately applied during the read operation.** If the wrong algorithm is used during the decryption attempt, this could lead to errors. It's essential to verify that the correct algorithm is being used.

**Why the other options are unlikely:**

  * **I. The read operation was performed using the customer's encryption key encoded in base64.** Base64 encoding is a standard way to represent binary data in text format, and it's necessary for using CSEK with Cloud Storage. This is unlikely to be the sole cause of the error.

  * **IV. The read operation utilized the base64-encoded SHA256 hash of the customer's encryption key for accessing the object.** While utilizing the SHA256 hash is crucial, you also need the base64-encoded key itself to decrypt the content.

**References:**  
[https://cloud.google.com/storage/docs/encryption/customer-supplied-keys#response https://cloud.google.com/storage/docs/encryption/using-customer-supplied-keys#rest-csek-download-object](https://cloud.google.com/storage/docs/encryption/customer-supplied-keys#response   https://cloud.google.com/storage/docs/encryption/using-customer-supplied-keys#rest-csek-download-object)

---

## Question 2

*Domain 2: Building and Testing Applications*

**For a web application that sends messages to Pub/Sub, you need to configure local testing to quickly assess Pub/Sub integration for each new build. How should you set up local testing?**

- [x] II. Use gcloud to install the Pub/Sub emulator and initiate it with a valid Google Project ID. For local development, configure the application to use the local emulator through ${gcloud beta emulators pubsub env-init}.
- [ ] III. Access the Google Cloud console, navigate to the API Library, and enable the Pub/Sub API. During local development, configure the application to call pubsub.googleapis.com.
- [ ] IV. Deploy the Pub/Sub emulator using gcloud and start it with a valid Google Project ID. When developing locally, configure the application to utilize the local emulator by exporting the PUBSUB_EMULATOR_HOST variable.
- [ ] I. Integrate Cloud Code into the integrated development environment (IDE). Activate Pub/Sub via Cloud APIs with a valid Google Project ID. During local development, configure the application to invoke pubsub.googleapis.com.

### Explanation

**The correct approach to set up local testing for a web application that sends messages to Pub/Sub is:**

**II. Use gcloud to install the Pub/Sub emulator and initiate it with a valid Google Project ID. For local development, configure the application to use the local emulator through**`**${gcloud beta emulators pubsub env-init}**`**.**

**Explanation:**

  * The Pub/Sub emulator allows you to emulate the behavior of Pub/Sub locally, which is useful for testing without incurring costs or affecting production systems.

  * Using `**gcloud**` to install the Pub/Sub emulator and initiating it with a valid Google Project ID sets up the local environment for Pub/Sub emulation.

  * Configuring the application to use the local emulator through `**${gcloud beta emulators pubsub env-init}**` ensures that the application sends messages to the local emulator instead of the actual Pub/Sub service during local development.

Option I is incorrect because it suggests integrating Cloud Code into the IDE and activating Pub/Sub via Cloud APIs with a valid Google Project ID, which may not be suitable for local testing.

Option III is incorrect because it involves enabling the Pub/Sub API in the Google Cloud console, which is not related to setting up local testing with the Pub/Sub emulator.

Option IV is incorrect because it suggests deploying the Pub/Sub emulator using `**gcloud**`, which is unnecessary since the emulator can be started locally without deploying it. Additionally, the method of configuring the application to utilize the local emulator by exporting the `**PUBSUB_EMULATOR_HOST**` variable is not mentioned in this option.

**References:**  
[https://cloud.google.com/pubsub/docs/emulator#env](https://cloud.google.com/pubsub/docs/emulator#env  https://cloud.google.com/pubsub/docs/emulator#automatically_setting_the_variables)

[https://cloud.google.com/pubsub/docs/emulator#automatically_setting_the_variables](https://cloud.google.com/pubsub/docs/emulator#env  https://cloud.google.com/pubsub/docs/emulator#automatically_setting_the_variables)

---

## Question 3

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You're designing an architecture for a system that needs to handle streaming data from thousands of devices. The workflow involves ingesting data into a pipeline, storing it, and analyzing it using SQL statements. Which combination of Google Cloud services should you use for steps 1, 2, 3, and 4?**

**

**

- [ ] A. 1. App Engine
    2\. Pub/Sub
    3\. BigQuery
    4\. Firestore
- [ ] B. 1. Dataflow
    2\. Pub/Sub
    3\. Firestore
    4\. BigQuery
- [x] D. 1. Pub/Sub
    2\. Dataflow
    3\. Firestore
    4\. BigQuery
- [ ] C. 1. Pub/Sub
    2\. Dataflow
    3\. BigQuery
    4\. Firestore

### Explanation

**The correct combination of Google Cloud services for handling streaming data from thousands of devices and performing SQL analysis on it would be:**

**D.**

  1. **Pub/Sub: Used for ingesting and processing real-time streaming data from thousands of devices. Pub/Sub can handle large volumes of data and distribute it to downstream services efficiently.**

  2. **Dataflow: Provides a fully managed, serverless stream processing service for transforming and enriching data in real time. Dataflow can process data from Pub/Sub and perform complex transformations before storing it or analyzing it further.**

  3. **Firestore: A flexible, scalable database for storing and querying semi-structured data. Firestore is suitable for storing metadata, configurations, or other relevant information related to the streaming data.**

  4. **BigQuery: A fully managed, serverless data warehouse for performing fast SQL queries on large datasets. BigQuery can be used to analyze the streaming data stored in Firestore or directly ingest data from Dataflow for analysis.**

Justification:

  * Pub/Sub is ideal for ingesting streaming data from devices due to its scalability and real-time capabilities.

  * Dataflow is suitable for processing and transforming streaming data before storing it or performing further analysis.

  * Firestore provides a flexible and scalable database for storing semi-structured data, which can complement the structured data stored in BigQuery.

  * BigQuery is a powerful tool for performing SQL analysis on large datasets, making it suitable for analyzing streaming data.

Option A is incorrect because App Engine is a platform for building and deploying web applications and does not provide stream processing capabilities like Dataflow or Pub/Sub.

Option B is incorrect because Firestore is not typically used for storing streaming data, as it is designed more for document-oriented databases rather than real-time streaming data.

Option C is incorrect because Dataflow is better suited for stream processing before analysis, rather than BigQuery, which is optimized for performing SQL queries on stored data. Additionally, Firestore is not typically used for storing streaming data.

---

## Question 4

*Domain 4: Integrating Applications with Google Cloud Services*

**Your colleague has shared the code snippet below, which aims to add a credit to an account balance in Cloud Datastore.**

**public Entity creditAccount (long accountId, long creditAmount) {**

**Entity account = Entity.builder(account)**

**.set("creditAmount", creditAmount)**

**.build();**

**datastore.put(account);**

**return account;**

**}**

**What suggestion should you offer for improving this code?**

- [ ] C. Utilize a strongly consistent transactional database.
- [ ] D. Refrain from returning the account entity from the function.
- [x] B. Perform the entity retrieval and update within a transaction.
- [ ] A. Retrieve the entity with an ancestor query.

### Explanation

**Correct Answer:**

  * **B. Perform the entity retrieval and update within a transaction.**

**Justification:**

  * **Data Consistency:** Transactions ensure that either all operations within a transaction succeed, or none do. This is crucial when updating something like an account balance to prevent potential corruption due to concurrent updates (Cloud Datastore Transactions Documentation: <https://cloud.google.com/datastore/docs/concepts/transactions>).

  * **How to Implement:** Wrap your entity retrieval, balance calculation, and the `datastore.put` call within a Datastore transaction to ensure the credit update happens atomically.

**Incorrect Answers:**

  * **A. Retrieve the entity with an ancestor query**

    * **Reasoning:** Ancestor queries are helpful for maintaining hierarchical relationships but don't directly resolve the consistency issue during concurrent updates.

  * **C. Utilize a strongly consistent transactional database**

    * **Reasoning:** While Cloud Datastore does support strong consistency, transactions are still the primary mechanism for ensuring updates happen atomically.

  * **D. Refrain from returning the account entity from the function.**

    * **Reasoning:** This is a minor point about function design, but unrelated to the core consistency issue.

---

## Question 5

*Domain 3: Configuring and Deploying Applications*

**Your team is utilizing Cloud Build to facilitate the promotion of a Node.js application deployed on App Engine from the staging environment to production. The application relies on several directories of photos stored in a Cloud Storage bucket named `webphotos-staging` in the staging environment. Post-promotion, these photos need to be accessible in a Cloud Storage bucket named `webphotos-prod` in the production environment. You aim to automate this process where feasible. What action should you take?**

- [ ] A. Perform a manual copy of the photos to `webphotos-prod`.
- [x] C. Insert a build step in the `cloudbuild.yaml` file before the promotion step with the arguments:
    name: gcr.io/cloud-builders/gsutil
    args: ['cp', '-r', 'gs://webphotos-staging', 'gs://webphotos-prod']
    waitFor: ['-']
- [ ] B. Introduce a startup script in the application's `app.yaml` file to transfer the photos from `webphotos-staging` to `webphotos-prod`.
- [ ] D. Include a build step in the `cloudbuild.yaml` file before the promotion step with the arguments:
    name: 'gcr.io/cloud-builders/gsutil'
    args: ['cp', '-a', 'gs://webphotos-staging', 'gs://webphotos-prod']
    waitFor: ['-']

### Explanation

**Correct Answer:**

  * **C. Insert a build step in the**`**cloudbuild.yaml**`**file before the promotion step with the arguments:...**

1.  name: gcr.io/cloud-builders/gsutil
      2. args: ['cp', '-r', 'gs://webphotos-staging', 'gs://webphotos-prod']
      3. waitFor: ['-']

**Justification:**

  * **Automation within the Build Pipeline:** Integrating the photo transfer into your Cloud Build pipeline ensures it happens automatically during the promotion process. This aligns with the goal of automating where feasible.

  * **The 'gsutil' Cloud Builder:** The `gcr.io/cloud-builders/gsutil` image provides tools for efficient Cloud Storage operations.

  * **Recursive Copy (**`**-r**`**):** Ensures all photos and subdirectories within `webphotos-staging` are copied.

  * `**waitFor: ['-']**`**:** Prevents subsequent build steps from running until the copy operation successfully completes.

**Incorrect Answers:**

  * **A. Perform a manual copy of the photos to**`**webphotos-prod**`**.**

    * **Reasoning:** This breaks the desired automation and introduces the potential for errors or missed steps in the promotion process.

  * **B. Introduce a startup script in the application's**`**app.yaml**`**file...**

    * **Reasoning:** While possible, this mixes concerns. Deployment and data transfer are better separated; keeping the transfer in Cloud Build makes the process more independent and reusable.

  * **D. Include a build step... `args: ['cp', '-a', 'gs://webphotos-staging', 'gs://webphotos-prod']...**

    * **Reasoning:** The `-a` flag (archive mode) is usually for preserving file attributes. While it would work, the simpler `-r` (recursive) flag is more direct for this use case.

---

## Question 6

*Domain 2: Building and Testing Applications*

**You are developing a web application using Cloud Run and Cloud Storage. A production issue has been reported, requiring an immediate fix. You need to execute a script in a Git repository to implement a workaround. Your corporate laptop is unavailable, but you have access to your personal computer and can use your corporate credentials to access necessary Google Cloud resources. To resolve the issue quickly and efficiently, while minimizing costs, what should you do?**

- [ ] B. Install VS Code and the Cloud Code extension on your personal computer. Check Cloud Run logs in Cloud Code to confirm the error, then execute the workaround script. Verify that the issue is resolved.
- [ ] D. Install the gcloud CLI on your personal computer. Authenticate and configure API access, clone the Git repository, and execute the workaround script. Verify that the issue is resolved.
- [ ] A. Use your personal computer to create and launch a Cloud Workstations instance. Authenticate and configure API access in the workstation, clone the Git repository, and execute the workaround script. Verify that the issue is resolved.
- [x] C. Access the Google Cloud Console and open Cloud Shell on your personal computer. Clone the Git repository and execute the workaround script in Cloud Shell. Verify that the issue is resolved.

### Explanation

The correct answer is 

**C. Access the Google Cloud Console and open Cloud Shell on your personal computer. Clone the Git repository and execute the workaround script in Cloud Shell. Verify that the issue is resolved.**

Explanation:

**Cloud Shell** provides a secure, managed environment within the Google Cloud Console that includes preconfigured tools (like `gcloud` and `git`) and does not require any local setup on your personal computer. Using Cloud Shell allows you to quickly access Google Cloud resources, clone the repository, and execute the workaround script without needing to install additional software or configure API access on your personal machine. This option also minimizes costs since Cloud Shell is free for interactive sessions and does not incur additional VM costs.

Justifications for Incorrect Options:

  * **Option A: Launch a Cloud Workstations instance**  
Setting up a Cloud Workstations instance is more complex and costly than using Cloud Shell, as it involves launching a VM and configuring access. Cloud Workstations is ideal for long-term development environments but is unnecessary for quick fixes.

  * **Option B: Install VS Code and Cloud Code extension**  
While Cloud Code is helpful for development, it requires installation and setup on your personal computer. Additionally, Cloud Code is optimized for development workflows, not for quickly executing scripts in production environments.

  * **Option D: Install the**`**gcloud**`**CLI on your personal computer**  
Installing and configuring the `gcloud` CLI on your personal computer is time-consuming compared to simply using Cloud Shell, which comes with `gcloud` pre-installed and fully configured for access to Google Cloud resources.

**Relevant Documentation:**

For more information on Cloud Shell, refer to:

  * [Google Cloud Shell Documentation](https://cloud.google.com/shell/docs)

---

## Question 7

*Domain 2: Building and Testing Applications*

**You are developing an application using App Engine and Cloud SQL for PostgreSQL. Before deploying new versions to a shared development environment, you want to test your application code locally. To ensure secure and authenticated access to Cloud SQL, all traffic must remain encrypted and authenticated to Cloud IAM and PostgreSQL. What should you do before starting your local development server?**

- [ ] D. Configure your local server to connect to the private IP of the Cloud SQL instance. Encrypt database entries before submitting them, and store the decryption key as an environment variable in App Engine.
- [ ] A. Install PostgreSQL on your local workstation, run a local PostgreSQL database, and configure the application to connect to localhost.
- [ ] C. Deploy a Compute Engine instance, install HAProxy on it, and set up Cloud SQL Auth Proxy on the instance. Use the instance’s service account to authenticate to Cloud SQL and configure the application to connect to the Compute Engine instance's IP address.
- [x] B. Download and install the Cloud SQL Auth Proxy on your local development environment. Configure the proxy to connect to Cloud SQL and run it locally. Set the application to connect to localhost.

### Explanation

The correct answer is

**B. Download and install the Cloud SQL Auth Proxy on your local development environment. Configure the proxy to connect to Cloud SQL and run it locally. Set the application to connect to localhost.**

Explanation:

The **Cloud SQL Auth Proxy** is the recommended approach for securely connecting to Cloud SQL from local development environments. It handles both **IAM-based authentication** and **encrypted connections** , ensuring secure access to your Cloud SQL instance. By running the Cloud SQL Auth Proxy locally, you can direct your application to connect to `localhost`, where the proxy securely forwards the connection to Cloud SQL. This setup allows you to test your application in an environment that closely matches the production setup in terms of security.

Justifications for Incorrect Options:

  * **Option A: Run a local PostgreSQL database on your workstation**  
Running a local PostgreSQL instance does not allow you to test the Cloud SQL environment. It also bypasses Cloud IAM and does not reflect the real security configurations required by Cloud SQL.

  * **Option C: Deploy a Compute Engine instance with HAProxy and Cloud SQL Auth Proxy**  
Setting up a Compute Engine instance and HAProxy introduces unnecessary complexity for local testing. The Cloud SQL Auth Proxy can be used directly on your local machine, which is simpler and meets all the security requirements.

  * **Option D: Connect directly to the private IP of the Cloud SQL instance**  
Directly connecting to a private IP requires VPN or VPC peering and does not ensure IAM-based authentication. Additionally, encrypting entries before submission is not equivalent to encrypting the connection itself, which the Cloud SQL Auth Proxy provides.

**Relevant Documentation:**

For more information on secure connections to Cloud SQL, refer to:

  * [Using the Cloud SQL Auth Proxy](https://cloud.google.com/sql/docs/mysql/sql-proxy)

---

## Question 8

*Domain 3: Configuring and Deploying Applications*

**You're attempting to utilize kubectl from Cloud Shell to connect to your Google Kubernetes Engine (GKE) cluster. After deploying the GKE cluster with a public endpoint, you execute the following command from Cloud Shell:**

**```**

**gcloud container clusters get-credentials <cluster-name> \**

**\--zone <zone> \--project <project-name>**

**```**

**However, you observe that the kubectl commands are timing out without providing any error message. What is the most probable cause of this issue?**

- [ ] A. Your user account lacks the necessary privileges to interact with the cluster using kubectl.
- [ ] D. A VPC firewall is obstructing access to the cluster's endpoint.
- [ ] C. Cloud Shell is not part of the same VPC as the GKE cluster.
- [x] B. The Cloud Shell's external IP address is not included in the authorized networks of the cluster.

### Explanation

**Correct Answer:**

  * **B. The Cloud Shell's external IP address is not included in the authorized networks of the cluster.**

**Justification:**

  * **Authorized Networks for Public Clusters:** Even though your GKE cluster has a public endpoint, by default, access is restricted to a set of authorized IP addresses. Cloud Shell has a dynamic, ephemeral IP address that changes, making it likely it's not included in the allowed list. (GCP Documentation: [invalid URL removed])

  * **Timeout Behavior:** The lack of an explicit error message and a timeout is consistent with traffic simply being blocked without rejection at the network level.

**Incorrect Answers:**

  * **A. Your user account lacks the necessary privileges...**

    * **Reasoning:** If this were the case, the `gcloud container clusters get-credentials` command itself would have likely failed with a permission-related error.

  * **C. Cloud Shell is not part of the same VPC as the GKE cluster.**

    * **Reasoning:** While VPC network boundaries _can_ affect connectivity, a public endpoint with proper authorization should be accessible even if Cloud Shell is in a different VPC.

  * **D. A VPC firewall is obstructing access to the cluster's endpoint**

    * **Reasoning:** While possible, VPC firewalls would usually result in a more explicit connection failure rather than a silent timeout.

---

## Question 9

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You are building a web application to be deployed on Cloud Run in production. This application is composed of multiple microservices: some need to be publicly accessible, while others should only be accessible after authenticating with Google identities. Your goal is to allow unrestricted access to public services but restrict access to certain services for authenticated users only. You want to implement the most secure solution while keeping management simple and minimizing overhead. How should you set up access?**

- [ ] C. Set up **Cloud Endpoints** with **Firebase Authentication** for all microservices. Configure **Firebase rules** to manage access control lists (ACLs) for each service, allowing public access where needed.
- [ ] A. Enable **Identity-Aware Proxy (IAP)** for all microservices, and create a new microservice that verifies the authentication requirements for each service and controls access accordingly.
- [x] B. Enable **Identity-Aware Proxy (IAP)** for all microservices. Use **access control lists (ACLs)** to restrict access to specific services and grant **allAuthenticatedUsers** access to public services.
- [ ] D. Set up separate **Cloud Run services** for public and restricted microservices. Enable **IAP** only for restricted services, and set the Cloud Run **ingress settings** to **‘Internal and Cloud Load Balancing’** for these services.

### Explanation

The correct answer is

**B. Enable Identity-Aware Proxy (IAP) for all microservices. Manage access control lists (ACLs) for the restricted services, and configure allAuthenticatedUsers access to the public services.**

Explanation:

**Identity-Aware Proxy (IAP)** is the recommended way to secure access to applications running on Google Cloud by controlling access based on Google identity. Enabling IAP for all microservices allows you to easily manage access control for each service using **Access Control Lists (ACLs)** :

  1. **Restricted Services** : Use ACLs to grant access only to specific, authenticated Google identities for services that require authentication.

  2. **Public Services** : Configure `allAuthenticatedUsers` to allow access to users who have authenticated with any Google account, or alternatively, you can configure these services with `allUsers` if truly unrestricted access is required.

This approach provides **secure, identity-based access** for the restricted services and easy configuration for public services, while avoiding additional infrastructure or complex access control implementations.

Justifications for Incorrect Options:

  * **Option A: Develop a new microservice to manage access**  
Creating a custom access management microservice introduces unnecessary complexity and management overhead, especially when IAP natively supports Google identity-based access control.

  * **Option C: Use Cloud Endpoints with Firebase Authentication**  
Cloud Endpoints and Firebase Authentication can control access, but they add complexity and require more setup than IAP. IAP provides a simpler, built-in approach for managing identity-based access for Google Cloud services.

  * **Option D: Configure separate Cloud Run services with IAP and ‘Internal and Cloud Load Balancing’ ingress**  
Using `Internal and Cloud Load Balancing` ingress restricts access to only internal Google Cloud traffic, which doesn’t meet the requirement for public access. IAP provides a more flexible solution, allowing both public and restricted access within the same framework.

**Relevant Documentation:**

For more details, refer to:

  * [Identity-Aware Proxy (IAP) Overview](https://cloud.google.com/iap/docs/concepts-overview)

---

## Question 10

*Domain 3: Configuring and Deploying Applications*

**You oversee an application governed by a managed instance group. In the event of deploying a new version of the application, your objective is to minimize costs and maintain a consistent number of instances. It's imperative that each new instance created during deployment is deemed healthy before the deployment proceeds.**

**Which approach should you employ to achieve this?**

- [ ] III. Implement a rolling-action with a limit on the maximum number of healthy instances set to 1, and the maximum number of unhealthy instances set to 0.
- [ ] I. Execute a rolling-action with a maximum surge set to 1 and maximum unavailable instances set to 0.
- [x] II. Conduct a rolling-action with a maximum surge set to 0 and a maximum number of instances deemed unavailable set to 1.
- [ ] IV. Engage in a rolling-action with a restriction on the maximum number of healthy instances set to 0, and the maximum number of unhealthy instances set to 1.

### Explanation

**The correct option for this scenario is:**

**II. Conduct a rolling-action with a maximum surge set to 0 and a maximum number of instances deemed unavailable set to 1.**

**Justification:** In this scenario, the objective is to minimize costs and maintain a consistent number of instances while ensuring that each new instance created during deployment is considered healthy before the deployment proceeds. Using a rolling update strategy with a maximum surge set to 0 ensures that no additional instances are created beyond the current capacity, thereby helping to minimize costs. Setting the maximum number of instances deemed unavailable to 1 ensures that only one instance can be considered unhealthy at any given time during the deployment process, maintaining consistency and reducing the risk of service disruption.

**Why the other options are not suitable:**

I. Executing a rolling-action with a maximum surge set to 1 and maximum unavailable instances set to 0: This option allows for one additional instance (surge) to be created during the deployment process, which may not align with the objective of minimizing costs and maintaining a consistent number of instances. Additionally, setting the maximum unavailable instances to 0 does not provide flexibility in handling instances that may temporarily become unhealthy during the deployment.

III. Implementing a rolling-action with a limit on the maximum number of healthy instances set to 1, and the maximum number of unhealthy instances set to 0: This option restricts the number of healthy instances to 1, which may not be desirable as it limits the deployment process and may lead to service disruption if the existing healthy instance experiences issues during deployment. It's also not optimal for maintaining consistency in the number of instances.

IV. Engaging in a rolling-action with a restriction on the maximum number of healthy instances set to 0, and the maximum number of unhealthy instances set to 1: Similarly to option III, this approach imposes unnecessary constraints on the deployment process and may increase the risk of service disruption by disallowing any healthy instances during deployment.

**Documentation Link:** You can find more information about managing instance groups and rolling updates in the official documentation here: [Rolling out updates](https://cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups)

---

## Question 11

*Domain 3: Configuring and Deploying Applications*

**You are creating a public-facing web application on Cloud Run, making it accessible through its public IP address. To test its ability to handle high traffic, you conduct a load test. While the app works fine under light traffic, you observe slower responses and error messages when the load is high. What is the best way to investigate and resolve this performance issue?**

- [x] D. Verify if your Cloud Run service has reached the set maximum instances. If so, increase the maximum instance count to allow for more scaling during high demand.
- [ ] A. Review the network traffic to your Cloud Run service using Cloud Monitoring to confirm if there's a spike in demand. If needed, use traffic splitting on the Cloud Run service to redirect some requests to a previous revision.
- [ ] B. Check the minimum instances setting for your Cloud Run service. If required, increase the minimum number of instances to align with the maximum virtual users in your load test.
- [ ] C. Investigate if Cloud Armor is detecting and blocking potential DDoS attacks before traffic reaches your Cloud Run service. Disable any Cloud Armor policies if they are restricting legitimate traffic.

### Explanation

The correct answer is 

**D. Verify if your Cloud Run service has reached the set maximum instances. If so, increase the maximum instance count to allow for more scaling during high demand.**

Explanation:

In **Cloud Run** , the maximum instances setting controls the upper limit for concurrent instances that can be started in response to incoming traffic. If your application is experiencing slower responses and errors under high load, it is likely that the maximum instance limit has been reached, preventing Cloud Run from scaling further to handle the increased demand. By increasing the **maximum instance count** , you allow Cloud Run to start more instances, which can handle additional traffic and improve performance during peak loads.

Justifications for Incorrect Options:

  * **Option A: Use Cloud Monitoring and traffic splitting**  
While Cloud Monitoring can help monitor traffic spikes, **traffic splitting** is not relevant for handling high demand. Splitting traffic to a previous revision would not improve scalability or performance under load.

  * **Option B: Check the minimum instances setting**  
The **minimum instances setting** determines the baseline number of instances to keep warm, which helps reduce cold start latency but does not impact the ability to scale up. Increasing this setting would result in unnecessary costs without improving the maximum scaling capacity.

  * **Option C: Investigate Cloud Armor for DDoS blocking**  
Cloud Armor provides protection against DDoS attacks, but it is unlikely that it is blocking legitimate traffic without specific configurations. Disabling Cloud Armor would not address performance issues caused by scaling limits in Cloud Run.

---

## Question 12

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You're tasked with migrating your corporate intranet web application to Google Cloud while ensuring accessibility for company employees, even while traveling. The migration should prioritize security and minimize application changes. What's the best approach to achieve this?**

- [ ] I. Implement authentication credential checks for each HTTP(S) request to the application to ensure authorized access.
- [ ] III. Set up a Compute Engine instance requiring users to log in with their corporate accounts. Direct the web application's DNS to this proxy Compute Engine instance. After authentication, the Compute Engine facilitates requests between users and the web application.
- [ ] IV. Set up a Compute Engine instance requiring users to log in with their corporate accounts. Point the web application's DNS to this proxy Compute Engine instance. Upon authentication, the Compute Engine issues an HTTP redirect to a public IP address hosting the web application, ensuring accessibility.
- [x] II. Configure Identity-Aware Proxy to grant employees access to the application via its public IP address while maintaining security measures.

### Explanation

**Best Choice:**

  * **II. Configure Identity-Aware Proxy (IAP) to grant employees access to the application via its public IP address while maintaining security measures.**

**Explanation:**

  * **Seamless User Experience:** IAP integrates with your existing corporate identities (likely G Suite or other SSO provider), minimizing the need for separate logins on the application itself.

  * **Strong Security:** IAP offers robust authentication and authorization at the load balancer level, protecting your intranet even with a public IP address.

  * **Minimal Changes:** Assuming the application isn't tightly coupled to internal IP addresses, IAP requires the least disruptive modifications to your application.

**Why Other Options Are Less Ideal:**

  * **I. Implement authentication credential checks for each HTTP(S) request to the application to ensure authorized access.**

    * **Reinventing the Wheel:** Implementing your own authentication and authorization logic alongside a corporate system is extra work and adds potential security risks.

  * **III. Set up a Compute Engine instance ...**

    * **Increased Complexity:** Introducing a Compute Engine instance as a proxy adds another component to manage and can become a performance/availability bottleneck.

  * **IV. Set up a Compute Engine instance ...**

    * **Same Issues as III + Security Risk:** In addition to drawbacks of III, redirecting users away from the secure IAP domain weakens the security model.

**Reference:**

<https://cloud.google.com/blog/topics/developers-practitioners/control-access-your-web-sites-identity-aware-proxy>

---

## Question 13

*Domain 3: Configuring and Deploying Applications*

**Your team oversees a Google Kubernetes Engine (GKE) cluster hosting an application. Another team intends to integrate with this application. Before commencing the integration, you must ensure that the other team cannot modify your application but can deploy their integration on GKE. What is the appropriate action to take?**

- [ ] I. Grant the Viewer IAM role on the cluster project to the other team using Identity and Access Management (IAM).
- [ ] II. Create a new GKE cluster and grant the Editor role on the cluster project to the other team using Identity and Access Management (IAM).
- [x] IV. Create a new namespace within the existing cluster and grant the Admin role on the new namespace to the other team using Kubernetes role-based access control (RBAC).
- [ ] III. Establish a new namespace within the existing cluster and grant the Editor role on the cluster project to the other team using Identity and Access Management (IAM).

### Explanation

**IV. Create a new namespace within the existing cluster and grant the Admin role on the new namespace to the other team using Kubernetes role-based access control (RBAC).**

Here's why this is the best approach:

  * **Resource Isolation:** Namespaces provide logical separation within a GKE cluster, ensuring the other team's work doesn't interfere with your application's resources.

  * **Principle of Least Privilege:** Granting the Admin role within the namespace gives the other team the necessary permissions to deploy and manage their integration, but limits their access to only that namespace.

  * **Separation of Concerns:** This approach maintains clear ownership boundaries between your application and the other team's integration.

**Why other options are less suitable:**

  * **I. Grant the Viewer IAM role on the cluster project to the other team using Identity and Access Management (IAM).** The Viewer role is too restrictive, preventing the other team from deploying their integration components.

  * **II. Create a new GKE cluster and grant the Editor role on the cluster project to the other team using Identity and Access Management (IAM).** A separate cluster adds unnecessary management overhead and may increase costs.

  * **III. Establish a new namespace within the existing cluster and grant the Editor role on the cluster project to the other team using Identity and Access Management (IAM).** Cluster-wide Editor permissions are too broad and could allow the other team to interfere with resources outside their designated namespace.

**References:**  
[https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control  https://cloud.google.com/kubernetes-engine/docs/concepts/access-control#rbac   https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control)

[https://cloud.google.com/kubernetes-engine/docs/concepts/access-control#rbac https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control  https://cloud.google.com/kubernetes-engine/docs/concepts/access-control#rbac   https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control)

---

## Question 14

*Domain 4: Integrating Applications with Google Cloud Services*

**Within your company's BigQuery data mart, which serves analytics insights to numerous employees, a specific user wishes to execute jobs without disrupting critical workloads. Time efficiency is not a priority for this user. Your objective is to accommodate this request while minimizing expenses for the company and the administrative effort required. What action should you take?**

- [ ] IV. Permit the user to execute jobs during periods when critical workloads are not active.
- [ ] III. Grant the user the job.user role within the existing project.
- [ ] II. Establish a separate project specifically for the user to execute jobs.
- [x] I. Advise the user to execute the jobs as batch processes.

### Explanation

**Correct Option: I. Advise the user to execute the jobs as batch processes.**

**Justification:**

  * **Cost-Effectiveness:** In BigQuery, batch queries are significantly more cost-effective compared to on-demand queries. They are the best option if time efficiency is not a concern.

  * **Workload Prioritization:** Batch jobs run when there is available BigQuery capacity, ensuring they won't disrupt critical workloads.

  * **Minimal Administrative Overhead:** Batch jobs require minimal setup and ongoing management.

**Why Other Options Are Less Suitable:**

  * **II. Establish a separate project:** Creates unnecessary overhead of managing another project and could even increase costs since project-level resources have associated expenses.

  * **III. Grant the user the job.user role:** Only gives the user the ability to execute jobs, but doesn't address workload prioritization and cost optimization.

  * **IV. Permit the user at non-active periods:** This is difficult to manage reliably, as critical workload schedules might change. It also requires ongoing monitoring effort.

**Relevant Documentation:**

  * **BigQuery Batch Queries:** <https://cloud.google.com/bigquery/docs/running-queries#batch>

  * **BigQuery Pricing Overview:** <https://cloud.google.com/bigquery/pricing>

---

## Question 15

*Domain 4: Integrating Applications with Google Cloud Services*

**Your team uses Cloud Storage for a video and image application recently migrated to Google Cloud. Following a surge in popularity, users are experiencing instability, and you notice a 10x increase in HTTP 429 errors from Cloud Storage APIs. You need a solution to resolve the current errors and ensure stability if the load increases again. What should you do?**

- [ ] C. Migrate all image and video data to Firestore and replace Cloud Storage APIs in the application code with Firestore access.
- [ ] B. Compress video and image files to reduce size, minimize storage costs, and reduce bandwidth usage. Implement a custom throttling mechanism in the application to limit concurrent API calls.
- [x] D. Implement a retry strategy with exponential backoff for requests that encounter HTTP 429 errors.
- [ ] A. Optimize the application code to reduce unnecessary Cloud Storage API calls and prevent HTTP 429 errors.

### Explanation

The correct answer is 

**D. Implement a retry strategy with exponential backoff for requests that encounter HTTP 429 errors.**

Explanation:

**HTTP 429 errors** indicate that the application has exceeded the rate limits for Cloud Storage API requests. The recommended approach for handling these errors is to implement a **retry strategy with exponential backoff**. This strategy adjusts the wait time between retries, gradually increasing it after each failed attempt, which helps avoid overwhelming the API and allows requests to succeed as the rate limit resets. This approach addresses the immediate issue and provides resilience if the load increases further.

Justifications for Incorrect Options:

  * **Option A: Optimize the application code to reduce unnecessary Cloud Storage API calls**  
While optimizing the code to reduce unnecessary calls can help, it may not fully resolve HTTP 429 errors if traffic continues to grow. Exponential backoff is more effective in managing rate limits dynamically.

  * **Option B: Compress video and image files and implement custom throttling**  
Compressing files may reduce bandwidth usage and storage costs, but it won’t address the HTTP 429 error rate directly. Custom throttling adds complexity and is less efficient than exponential backoff, which adapts based on API response.

  * **Option C: Migrate all data to Firestore**  
Firestore is not optimized for storing large files like videos and images, and migration would add unnecessary complexity. Cloud Storage is designed for these file types and should be retained with a retry strategy.

**Relevant Documentation:**

For more information on handling HTTP 429 errors and implementing exponential backoff, refer to:

  * [Cloud Storage Best Practices](https://cloud.google.com/storage/docs/best-practices)

---

## Question 16

*Domain 4: Integrating Applications with Google Cloud Services*

**You are building an image processing application that will perform tasks like resizing, cropping, and adding watermarks to images. You also need to monitor the workflow and ensure the system scales efficiently for high image volumes. Your goal is to automate both the image processing tasks and workflow monitoring with minimal setup effort. What approach should you take?**

- [ ] D. Configure Cloud Build to trigger Cloud Functions for each image processing task and manage monitoring with Cloud Logging.
- [x] C. Set up Workflows to orchestrate the image processing tasks, and use Cloud Logging to keep track of workflow performance.
- [ ] B. Deploy the image processing functions on Cloud Run, make them accessible via an API using Apigee, and set up Cloud Logging to monitor the workflow.
- [ ] A. Use Cloud Composer to manage the workflows for image processing, and utilize Dataproc for monitoring and analytics of the workflow.

### Explanation

The correct answer is 

**C. Set up Workflows to orchestrate the image processing tasks, and use Cloud Logging to keep track of workflow performance.**

Explanation:

**Google Cloud Workflows** is a fully managed service designed for orchestrating complex, multi-step workflows, making it ideal for coordinating sequential image processing tasks like resizing, cropping, and watermarking. Workflows provide the necessary automation with minimal setup, allowing you to focus on task logic rather than managing infrastructure. **Cloud Logging** can be integrated with Workflows to monitor performance and track workflow executions, giving visibility into the system’s status and scalability.

Justifications for Incorrect Options:

  * **Option A: Use Cloud Composer and Dataproc**  
**Cloud Composer** (based on Apache Airflow) is primarily used for complex ETL workflows rather than straightforward task automation, which would add unnecessary overhead for this use case. **Dataproc** is intended for big data processing with Spark and Hadoop, which is not required for basic image processing tasks.

  * **Option B: Deploy on Cloud Run and use Apigee**  
Deploying individual image processing functions on **Cloud Run** is possible, but using **Apigee** for API management adds complexity and is unnecessary for internal workflow automation. Cloud Run and Apigee are better suited for external-facing APIs rather than orchestrating internal tasks.

  * **Option D: Use Cloud Build to trigger Cloud Functions**  
**Cloud Build** is designed for CI/CD tasks rather than ongoing automation for a multi-step image processing workflow. It lacks native support for orchestrating workflows and managing interdependencies between tasks, which Workflows handles more efficiently.

**Relevant Documentation:**

For more information, refer to:

  * [Google Cloud Workflows Overview](https://cloud.google.com/workflows/docs/overview)

---

## Question 17

*Domain 4: Integrating Applications with Google Cloud Services*

**You're tasked with constructing a public API that manages authentication, enforces usage quotas, and tracks metrics for API consumers. Which tool is the most suitable for implementing this architecture?**

**

**

- [ ] A. App Engine
- [ ] C. Identity-Aware Proxy
- [x] B. Cloud Endpoints
- [ ] D. GKE Ingress for HTTP(S) Load Balancing

### Explanation

**B. Cloud Endpoints**

Here's why Cloud Endpoints is a good fit for your requirements:

  * **Authentication Management:** Cloud Endpoints integrates with Cloud Identity and Access Management (IAM) to handle user authentication and authorization for your API.

  * **Usage Quotas:** Cloud Endpoints allows you to define and enforce quotas on API calls based on various metrics like request rate, project, or API method.

  * **Metrics Tracking:** Cloud Endpoints provides built-in monitoring and logging capabilities that you can use to track API usage metrics and analyze API performance.

Let's analyze the other options and why they are not ideal:

  * **A. App Engine:** While App Engine can host your API backend, it doesn't offer built-in features for authentication, quota management, and API metrics tracking at the granularity you need.

  * **C. Identity-Aware Proxy (IAP):** IAP focuses primarily on securing access to your backend applications at the network layer. It doesn't provide functionalities for API quota and metric tracking.

  * **D. GKE Ingress for HTTP(S) Load Balancing:** GKE Ingress can be used to route traffic to your API backend, but it doesn't offer functionalities for authentication, quota management, and metric tracking out of the box.

**Reference:**

<https://cloud.google.com/kubernetes-engine/docs/concepts/ingress>

---

## Question 18

*Domain 3: Configuring and Deploying Applications*

**As part of your workflow utilizing Cloud Build, you're tasked with promoting a Docker image across Development, Test, and Production environments. It's imperative to ensure consistency by deploying the same Docker image to each environment.**

**How should you designate the Docker image within your build?**

- [x] III. Utilize the digest of the Docker image for precise identification.
- [ ] II. Employ a unique Docker image name for differentiation.
- [ ] IV. Utilize a semantic version Docker image tag for version control.
- [ ] I. Employ the latest Docker image tag for identification.

### Explanation

**Correct Choice:**

  * **III. Utilize the digest of the Docker image for precise identification.**

**Explanation:**

  * **Immutability:** A Docker image digest is a unique, content-based hash (e.g., sha256:abcd1234...). This guarantees that if you reference a specific digest, you are always referring to the exact, unchanging image contents. This is crucial for ensuring the same image gets deployed across environments.

**Why Other Options Can Be Problematic:**

  * **I. Employ the latest Docker image tag for identification.**

    * **Ambiguity:** The "latest" tag is mutable, meaning it could be reassigned to a different image over time. This introduces uncertainty and undermines reliable promotion across environments.

  * **II. Employ a unique Docker image name for differentiation.**

    * **Insufficent Specificity:** While unique names can help, they don't ensure content hasn't changed. Developers could rebuild an image with the same name but with different contents.

  * **IV. Utilize a semantic version Docker image tag for version control.**

    * **Potential for Human Error:** Semantic versioning (e.g., 1.0.2) is useful for tracking changes. However, a developer could accidentally increment a minor version without intending major changes, leading to unexpected inconsistencies.

**Reference:**  
<https://cloud.google.com/architecture/using-container-images>

---

## Question 19

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You are developing a highly available and globally accessible application to deliver static content to users. What configuration should you implement for the storage and serving components to minimize management overhead, reduce latency, and maximize reliability for users?**

- [x] IV. 1. Utilize a Standard storage class, multi-regional Cloud Storage bucket and store the static content within it.
    2\. Reserve an external IP address and set up an external HTTP(S) load balancer.
    Enable Cloud CDN and direct traffic to the backend bucket.
    3\. Set up an external HTTP(S) load balancer.
    Enable Cloud CDN and route traffic to the unmanaged instance group.
- [ ] II. 1. Create an unmanaged instance group and replicate the static content across the VMs.
    2\. Set up an external HTTP(S) load balancer.
    Enable Cloud CDN and route traffic to the unmanaged instance group.
- [ ] I. 1. Establish a managed instance group and replicate the static content across the virtual machines (VMs).
    2\. Create an external HTTP(S) load balancer.
    Enable Cloud CDN and direct traffic to the managed instance group.
- [ ] III. 1. Deploy a Standard storage class, regional Cloud Storage bucket and store the static content in the bucket.
    2\. Reserve an external IP address and configure an external HTTP(S) load balancer.
    Enable Cloud CDN and direct traffic to the backend bucket.

### Explanation

The most suitable configuration for this scenario is **IV** :

  * **1\. Utilize a Standard storage class, multi-regional Cloud Storage bucket and store the static content within it.** Multi-regional Cloud Storage provides the highest level of availability and geographic redundancy for your content. This ensures reliability even if a single region experiences issues.

  * **2\. Reserve an external IP address and set up an external HTTP(S) load balancer. Enable Cloud CDN and direct traffic to the backend bucket.** The load balancer distributes traffic for global reach, and Cloud CDN optimizes for low-latency content delivery.

**Here's why this combination is the best:**

  * **Maximizes reliability:** Multi-regional storage and load balancing mitigate the risk of regional outages impacting content availability.

  * **Minimizes latency:** Cloud CDN caches the content at edge locations worldwide, placing it closer to users for faster delivery.

  * **Reduces management overhead:** Using fully managed services like multi-regional Cloud Storage and Cloud CDN eliminates the need to manage infrastructure like VMs.

**Why other options are less ideal:**

  * **I & II**: Using instance groups (managed or unmanaged) introduces the overhead of managing VM infrastructure, patching, and scaling. This is less efficient for static content.

  * **III:** A regional Cloud Storage bucket offers less redundancy than a multi-regional one, increasing the risk of downtime if a regional issue occurs.

---

## Question 20

*Domain 3: Configuring and Deploying Applications*

**You're preparing to deploy your application in a Google Kubernetes Engine (GKE) cluster. The application offers an HTTP-based health check accessible at /healthz. You aim to utilize this health check endpoint for determining whether traffic should be directed to the pod by the load balancer. Which code snippet should you include in your Pod configuration?**

- [ ] D.
      
            1. healthCheck:
        2.   httpGet:
        3.     path: /healthz
        4.     port: 80
- [ ] A.
      
            1. livenessProbe:
        2.   httpGet:
        3.     path: /healthz
        4.     port: 80
- [ ] C.
      
            1. loadbalancerHealthCheck:
        2.   httpGet:
        3.     path: /healthz
        4.     port: 80
- [x] B.
      
            1. readinessProbe:
        2.   httpGet:
        3.     path: /healthz
        4.     port: 80

### Explanation

**Correct Answer**

  * **B. readinessProbe: httpGet: path: /healthz port: 80**

**Justification:**

  * **Readiness Probes:** In Kubernetes, readiness probes tell the system when a container is ready to start receiving traffic from a service. A pod only becomes part of a service's endpoints when its readiness probe succeeds. (Kubernetes Documentation: <https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/>)

  * **HTTP Health Checks:** The `httpGet` probe type is used to perform HTTP GET requests on a configured path and port. A successful response indicates the container is healthy. (Kubernetes Documentation: <https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/>)

**Incorrect Answers**

  * **A. livenessProbe: httpGet: path: /healthz port: 80**

    * **Reasoning:** Liveness probes determine if a container is still running and should be restarted if not. While important, liveness probes don't directly handle traffic routing.

  * **C. loadbalancerHealthCheck: httpGet: path: /healthz port: 80**

    * **Reasoning:** There's no concept of a `loadBalancerHealthCheck` in Kubernetes pod specifications. Health checks are defined using readiness and liveness probes.

  * **D. healthCheck: httpGet: path: /healthz port: 80**

    * **Reasoning:** The `healthCheck` field is too generic; Kubernetes needs a specific probe type (`readinessProbe` or `livenessProbe`) to function correctly.

---

## Question 21

*Domain 4: Integrating Applications with Google Cloud Services*

**To handle messages from a Pub/Sub topic and store them in Google Cloud cost-effectively and efficiently, ensuring each message is processed only once, what should you do?**

- [ ] I. Utilize a Dataproc job to process the messages and save the output to storage.
- [x] II. Process messages with a Dataflow streaming pipeline using Apache Beam's PubSubIO package and save the output to storage.
- [ ] III. Deploy a Cloud Function to process messages and store results in a BigQuery location, where data deduplication can be performed.
- [ ] IV. Fetch messages with a Dataflow streaming pipeline, store them in Cloud Bigtable, and utilize another Dataflow streaming pipeline to remove duplicates.

### Explanation

**The most suitable option for handling messages from a Pub/Sub topic efficiently, ensuring each message is processed only once, and storing them in Google Cloud cost-effectively is:**

**II. Process messages with a Dataflow streaming pipeline using Apache Beam's PubSubIO package and save the output to storage.**

**Explanation:**

  * **Dataflow is a fully managed, serverless stream and batch processing service provided by Google Cloud Platform.**

  * **Apache Beam is an open-source unified programming model for defining both batch and streaming data-parallel processing pipelines.**

  * **PubSubIO is a component of Apache Beam that allows for seamless integration with Pub/Sub for message ingestion.**

  * **Using Dataflow with Apache Beam's PubSubIO package ensures efficient processing of messages from the Pub/Sub topic in a streaming fashion.**

  * **Dataflow automatically handles aspects like scaling, fault tolerance, and data deduplication, ensuring that each message is processed only once without the need for manual intervention.**

  * **Dataflow also integrates seamlessly with various storage options provided by Google Cloud Platform, allowing you to save the output to storage in a cost-effective manner.**

The other options can be explained as follows:

I. Utilize a Dataproc job to process the messages and save the output to storage.

  * Dataproc is a managed Spark and Hadoop service provided by Google Cloud Platform. While it can be used for processing messages, it might not be the most efficient or cost-effective solution for real-time stream processing, especially when dealing with Pub/Sub messages.

III. Deploy a Cloud Function to process messages and store results in a BigQuery location, where data deduplication can be performed.

  * While Cloud Functions can be used for processing Pub/Sub messages, they are more suitable for event-driven, lightweight tasks rather than processing large volumes of streaming data. Additionally, BigQuery might not be the most efficient storage option for stream processing, especially when considering data deduplication requirements.

IV. Fetch messages with a Dataflow streaming pipeline, store them in Cloud Bigtable, and utilize another Dataflow streaming pipeline to remove duplicates.

  * While this option involves Dataflow for stream processing and Cloud Bigtable for storage, it introduces unnecessary complexity by using two separate Dataflow pipelines for processing and deduplication. Additionally, Dataflow itself provides built-in mechanisms for handling data deduplication without the need for additional pipelines.

**References:**  
[https://cloud.google.com/pubsub/docs/stream-messages-dataflow https://cloud.google.com/community/tutorials/pubsub-spring-dedup-messages https://cloud.google.com/blog/products/data-analytics/handling-duplicate-data-in-streaming-pipeline-using-pubsub-dataflow](https://cloud.google.com/pubsub/docs/stream-messages-dataflow   https://cloud.google.com/community/tutorials/pubsub-spring-dedup-messages   https://cloud.google.com/blog/products/data-analytics/handling-duplicate-data-in-streaming-pipeline-using-pubsub-dataflow)

---

## Question 22

*Domain 4: Integrating Applications with Google Cloud Services*

**What is the probable reason behind the failure of requests from the application to access objects in the Cloud Storage bucket, resulting in a 403 Permission Denied error code?**

- [ ] IV. A temporary outage is occurring in the Interconnect link from the on-premises data center to Google Cloud.
- [ ] III. The service account key has been rotated but not refreshed on the application server.
- [ ] I. Changes have been made to the folder structure inside the bucket and object paths.
- [x] II. Alterations have occurred in the permissions of the service account’s predefined role.

### Explanation

**The probable reason behind the failure of requests from the application to access objects in the Cloud Storage bucket, resulting in a 403 Permission Denied error code is:**

**II. Alterations have occurred in the permissions of the service account’s predefined role.**

**Explanation:**

  * **The 403 Permission Denied error typically indicates that the request lacks the necessary permissions to access the resource.**

  * **If alterations have occurred in the permissions of the service account's predefined role, it could result in the service account not having sufficient permissions to access the Cloud Storage bucket.**

  * **Permissions can be modified inadvertently by users or administrators, leading to access issues for service accounts.**

  * **Reviewing and ensuring that the service account has the appropriate permissions assigned to its predefined role can resolve the 403 Permission Denied error.**

The other options can be explained as follows:

I. Changes have been made to the folder structure inside the bucket and object paths.

  * Changes to the folder structure or object paths within the Cloud Storage bucket would not typically result in a 403 Permission Denied error. Instead, it might lead to 404 Not Found errors if the requested object path does not exist.

III. The service account key has been rotated but not refreshed on the application server.

  * Rotating the service account key without refreshing it on the application server could lead to authentication failures, but it would not directly result in a 403 Permission Denied error. Instead, it might lead to authentication errors such as 401 Unauthorized.

IV. A temporary outage is occurring in the Interconnect link from the on-premises data center to Google Cloud.

  * An outage in the Interconnect link would affect connectivity between the on-premises data center and Google Cloud services, potentially resulting in connection timeouts or errors related to network connectivity. However, it would not specifically cause a 403 Permission Denied error related to Cloud Storage access permissions.

**References:**  
[https://cloud.google.com/storage/docs/troubleshooting#access-permission https://cloud.google.com/appengine/docs/legacy/standard/python/googlecloudstorageclient/errors https://cloud.google.com/storage/docs/xml-api/reference-status#403%E2%80%94forbidden](https://cloud.google.com/storage/docs/troubleshooting#access-permission   https://cloud.google.com/appengine/docs/legacy/standard/python/googlecloudstorageclient/errors   https://cloud.google.com/storage/docs/xml-api/reference-status#403%E2%80%94forbidden)

---

## Question 23

*Domain 2: Building and Testing Applications*

**In your CI/CD pipeline utilizing Cloud Build, you need to ensure that a flat file generated in one builder is accessible to subsequent builders within the same pipeline. What is the recommended method to store the file for shared access?**

- [ ] III. Use gsutil to output the file contents to a Cloud Storage object, allowing seamless access by subsequent build steps in the pipeline.
- [x] II. Output the file contents to a file within the /workspace directory and read from the same file in subsequent build steps to facilitate shared access.
- [ ] IV. Incorporate a build argument that executes an HTTP POST via curl to a separate web server to persist the file's value in one builder, then employ an HTTP GET via curl from the subsequent build step to retrieve the value for shared access.
- [ ] I. Utilize Compute Engine instance metadata to store and retrieve the file contents, ensuring accessibility across all builders in the pipeline.

### Explanation

**Best Choice:**

  * **II. Output the file contents to a file within the /workspace directory and read from the same file in subsequent build steps to facilitate shared access.**

**Explanation:**

  * **Simplicity:** Cloud Build's `workspace` is a shared directory persisting data across build steps within a pipeline. It's the most straightforward way to pass data between builders.

  * **Efficiency:** Accessing files locally is the fastest approach, avoiding network calls to external services.

**Why Other Options Are Less Ideal:**

  * **I. Utilize Compute Engine instance metadata ...**

    * **Intended Purpose:** Instance metadata is designed for storing small pieces of configuration data, not arbitrary files.

  * **III. Use gsutil to output the file contents to a Cloud Storage object ...**

    * **Unnecessary Overhead:** Accessing Cloud Storage introduces network latency and adds operational overhead compared to the local workspace.

  * **IV. Incorporate a build argument that executes an HTTP POST via curl ...**

    * **Complex and Indirect:** Maintaining a separate web server solely for passing intermediate data during a build process is overly complex.

**References:**  
[https://cloud.google.com/build/docs/build-config-file-schema](https://cloud.google.com/build/docs/build-config-file-schema  https://cloud.google.com/build/docs/configuring-builds/pass-data-between-steps#passing_data_using_workspaces)

[https://cloud.google.com/build/docs/configuring-builds/pass-data-between-steps#passing_data_using_workspaces](https://cloud.google.com/build/docs/build-config-file-schema  https://cloud.google.com/build/docs/configuring-builds/pass-data-between-steps#passing_data_using_workspaces)

---

## Question 24

*Domain 2: Building and Testing Applications*

**Your team is tasked with standardizing log data for services running on Google Kubernetes Engine. How can you achieve this using Google-recommended practices efficiently? (Select two options.)**

- [ ] IV. Enforce the usage of the Logging API within the application code to generate structured logs for Cloud Logging.
- [x] I. Implement logging exports on application logs to BigQuery for streamlined log analytics.
- [ ] V. Enforce the usage of the Pub/Sub API to transmit structured data to Pub/Sub, then establish a Dataflow streaming pipeline to standardize logs and transfer them to BigQuery for analytics.
- [x] III. Configure log output to standard output (stdout) as single-line JSON to be fed into Cloud Logging as structured logs.
- [ ] II. Implement logging exports on application logs to Cloud Storage for enhanced log analytics.

### Explanation

**Based on Google-recommended practices for standardizing log data for services running on Google Kubernetes Engine, the two most efficient options would be:**

**I. Implement logging exports on application logs to BigQuery for streamlined log analytics.**

**III. Configure log output to standard output (stdout) as single-line JSON to be fed into Cloud Logging as structured logs.**

**Justification:**

I. Implement logging exports on application logs to BigQuery for streamlined log analytics: Exporting application logs directly to BigQuery allows for centralized storage and streamlined log analytics. BigQuery is a powerful tool for analyzing large datasets, and by exporting logs to BigQuery, you can perform advanced queries and analyses on your log data efficiently. This aligns with Google-recommended practices for log management and analysis.

III. Configure log output to standard output (stdout) as single-line JSON to be fed into Cloud Logging as structured logs: Configuring log output to standard output (stdout) as single-line JSON allows for easy ingestion of logs into Cloud Logging as structured logs. Cloud Logging can parse and analyze structured logs effectively, providing insights and monitoring capabilities for your applications running on Google Kubernetes Engine. This approach ensures consistency and compatibility with Cloud Logging's structured logging features.

**Why the other options are not as efficient:**

II. Implement logging exports on application logs to Cloud Storage for enhanced log analytics: While exporting logs to Cloud Storage can be useful for archival and storage purposes, it may not be as efficient as exporting logs directly to BigQuery for streamlined log analytics. Cloud Storage is better suited for long-term storage rather than real-time log analysis, which is more effectively handled by BigQuery.

IV. Enforce the usage of the Logging API within the application code to generate structured logs for Cloud Logging: While using the Logging API within the application code can generate structured logs for Cloud Logging, it may introduce complexity and maintenance overhead. Configuring log output to standard output (stdout) as single-line JSON is a more straightforward approach and aligns better with Google-recommended practices for log standardization on Google Kubernetes Engine.

V. Enforce the usage of the Pub/Sub API to transmit structured data to Pub/Sub, then establish a Dataflow streaming pipeline to standardize logs and transfer them to BigQuery for analytics: While this option provides a method for standardizing logs and transferring them to BigQuery for analytics, it involves additional components and complexity compared to directly exporting logs to BigQuery. It may not be as efficient in terms of implementation and management, especially when simpler solutions are available for achieving the same outcome.

**Documentation Links:**

  * [Exporting logs to BigQuery](https://cloud.google.com/logging/docs/export/bigquery)

  * [Structured logging with Cloud Logging](https://cloud.google.com/logging/docs/structured-logging)

---

## Question 25

*Domain 3: Configuring and Deploying Applications*

**You are employed by a company managing an ecommerce platform. Your task involves testing a new product recommendation algorithm through A/B testing to assess its impact on sales in a randomized manner. What is the recommended approach for testing this feature?**

- [ ] IV. Utilize HTTP header-based routing.
- [x] I. Distribute traffic between versions using weights.
- [ ] III. Mirror traffic to the new version of your application.
- [ ] II. Activate the new recommendation feature flag on a single instance.

### Explanation

**The recommended approach for testing a new product recommendation algorithm through A/B testing to assess its impact on sales in a randomized manner is:**

**I. Distribute traffic between versions using weights.**

**Explanation:**

  * **A/B testing involves splitting traffic between different versions of the application to compare their performance.**

  * **By distributing traffic between versions using weights, you can control the proportion of users exposed to each version. For example, you might allocate 50% of the traffic to the current version and 50% to the version with the new recommendation algorithm.**

  * **This approach allows for a randomized and controlled comparison between the two versions, enabling you to measure the impact of the new recommendation algorithm on sales in a statistically valid manner.**

The other options can be explained as follows:

II. Activating the new recommendation feature flag on a single instance (Option II) would not provide a randomized comparison between different versions. It also does not allow for statistical analysis of the impact on sales across a diverse user base.

III. Mirroring traffic to the new version of your application (Option III) involves sending a copy of traffic to the new version without impacting the primary traffic flow. While this approach can be useful for testing in a non-disruptive manner, it does not inherently provide a randomized comparison between different versions.

IV. Utilizing HTTP header-based routing (Option IV) can be a part of the implementation for directing traffic to different versions of the application, but it alone does not ensure randomized distribution or controlled comparison between versions. It's more about routing traffic based on specific conditions rather than conducting A/B testing.

**References:**  
[https://cloud.google.com/traffic-director/docs/advanced-traffic-management#weight-based_traffic_splitting_for_safer_deployments](https://cloud.google.com/traffic-director/docs/advanced-traffic-management#weight-based_traffic_splitting_for_safer_deployments  https://cloud.google.com/load-balancing/docs/https/traffic-management-global)

[https://cloud.google.com/load-balancing/docs/](https://cloud.google.com/traffic-director/docs/advanced-traffic-management#weight-based_traffic_splitting_for_safer_deployments  https://cloud.google.com/load-balancing/docs/https/traffic-management-global)

[https/traffic-management-global](https://cloud.google.com/traffic-director/docs/advanced-traffic-management#weight-based_traffic_splitting_for_safer_deployments  https://cloud.google.com/load-balancing/docs/https/traffic-management-global)

---

## Question 26

*Domain 4: Integrating Applications with Google Cloud Services*

**In order to enhance the application's resilience to errors, what adjustments should be implemented considering that occasional uploads fail, resulting in an HTTP 504 Gateway Timeout error when using the Cloud Client Library to upload an image to Cloud Storage?**

- [x] I. Implement an exponential backoff process around the client library call.
- [ ] II. Implement a one-second wait time backoff process around the client library call.
- [ ] III. Incorporate a retry button within the application and prompt users to click it in case of errors.
- [ ] IV. Establish a queue for the object and notify users that the application will attempt the upload again in 10 minutes.

### Explanation

**The adjustments that should be implemented to enhance the application's resilience to errors, specifically occasional uploads failures resulting in an HTTP 504 Gateway Timeout error when using the Cloud Client Library to upload an image to Cloud Storage, are:**

**I. Implement an exponential backoff process around the client library call.**

**Explanation:**

  * **Exponential backoff is a technique used to handle retries in distributed computing systems by exponentially increasing the waiting time between retries.**

  * **Implementing exponential backoff around the client library call allows the application to gracefully handle transient failures, such as HTTP 504 errors, by backing off and retrying the upload after waiting for a progressively increasing amount of time.**

  * **This approach helps prevent overwhelming the service with retries and reduces the likelihood of continued errors due to transient issues.**

**The other options can be explained as follows:**

II. Implement a one-second wait time backoff process around the client library call.

  * Implementing a fixed one-second wait time backoff process might not be sufficient to handle transient failures effectively, especially if the underlying issue causing the HTTP 504 error persists. It could lead to unnecessary retries and increased load on the service.

III. Incorporate a retry button within the application and prompt users to click it in case of errors.

  * While incorporating a retry button can be helpful for user interaction and providing control over retries, it might not be the most effective approach for automated retries, especially for background tasks like uploads. Relying solely on user intervention might not be practical for handling occasional upload failures.

IV. Establish a queue for the object and notify users that the application will attempt the upload again in 10 minutes.

  * While establishing a queue and notifying users about upload retries can be useful for managing failed uploads, it might not address the immediate need for handling transient errors like HTTP 504 Gateway Timeout. Additionally, a fixed 10-minute delay might not be optimal for handling transient failures, as it could lead to prolonged delays in processing uploads.

**References:**  
[https://cloud.google.com/storage/docs/retry-strategy#exponential-backoff](https://cloud.google.com/storage/docs/retry-strategy#exponential-backoff  https://cloud.google.com/storage/docs/json_api/v1/status-codes#504_Gateway_Timeout)

[https://cloud.google.com/storage/docs/json_api/v1/status-codes#504_Gateway_Timeout ](https://cloud.google.com/storage/docs/retry-strategy#exponential-backoff  https://cloud.google.com/storage/docs/json_api/v1/status-codes#504_Gateway_Timeout)

---

## Question 27

*Domain 3: Configuring and Deploying Applications*

**While creating a Google Kubernetes Engine (GKE) cluster using the command `gcloud container clusters create large-cluster --num-nodes 200`, you encounter an error:**

**insufficient regional quota to satisfy request: resource "CPUS": request requires '200.0' and is short '176.0'. project has a quota of '24.0' with '24.0' available**

**To resolve this issue, what should you do?**

- [ ] D. Modify services in the cluster to function with fewer cores, and rewrite new clusters accordingly.
- [ ] C. Raise a support case to request additional GKE quota.
- [x] B. Increase the Compute Engine quota in the GCP Console.
- [ ] A. Increase the GKE quota in the GCP Console.

### Explanation

**Correct Answer:**

  * **B. Increase the Compute Engine quota in the GCP Console.**

**Justification:**

  * **Quota Limits:** Google Kubernetes Engine (GKE) clusters fundamentally consist of Compute Engine virtual machines (nodes). The "CPUs" quota directly corresponds to the number of virtual CPUs available to your project in the region you're attempting to create the cluster (GCP Documentation: <https://cloud.google.com/compute/quotas>).

**Incorrect Answers:**

  * **A. Increase the GKE quota in the GCP Console.**

    * **Reasoning:** While some regions have specific GKE quotas, the error message indicates a CPU limitation. Often, increasing the underlying Compute Engine quota automatically adjusts the connected GKE quota (if one exists).

  * **C. Raise a support case to request additional GKE quota.**

    * **Reasoning:** While support could eventually help, it's usually faster to directly increase the Compute Engine CPU quota yourself (if your project permissions allow it).

  * **D. Modify services in the cluster to function with fewer cores...**

    * **Reasoning:** Resource optimization is good practice, but it doesn't address the core problem - the project-level limitation on the number of CPUs you can use in the region.

---

## Question 28

*Domain 3: Configuring and Deploying Applications*

**Your application is deployed across multiple Google Kubernetes Engine clusters, each managed by a Deployment. Within each cluster, the Deployment has spawned multiple replicas of your Pod. Your aim is to inspect the logs transmitted to stdout for all replicas within your Deployment across all clusters. Which command should you employ?**

- [ ] III. Run `**kubectl exec -it [PARAM] journalctl**`.
- [ ] I. Execute `**kubectl logs [PARAM]**`.
- [ ] IV. Access logs via `**gcloud compute ssh [PARAM] --command="sudo journalctl"**`.
- [x] II. Utilize `**gcloud logging read [PARAM]**`.

### Explanation

**Best Approach (assuming centralized logging):**

  * **II. Utilize gcloud logging read [PARAM]**

    * **Explanation:** Centralized logging offers the ability to aggregate logs from all your clusters and pods, and `gcloud logging read` lets you access and filter these logs effectively.

    * **Documentation:** <https://cloud.google.com/logging/docs/reference/tools/gcloud-logging>

**If centralized logging is NOT set up:**

In the absence of a centralized logging solution, the task becomes more cumbersome. You _could_ technically achieve the goal with a combination of the following, but it's less than ideal:

  * **I. Execute kubectl logs [PARAM].**

    * **Explanation:** You'd need to iterate through each cluster, retrieve a list of Pods within your Deployment, and then run `kubectl logs` against each Pod individually.

    * **Documentation:** <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_logs/>

**Why the other options are NEVER suitable**

  * **III. Run kubectl exec -it [PARAM] journalctl.**

    * **Incorrect:** `journalctl` provides system-level logs, not necessarily the application logs sent to stdout.

  * **IV. Access logs via gcloud compute ssh [PARAM] --command="sudo journalctl".**

    * **Incorrect and Inefficient:** Same limitations as option III, and it introduces the unnecessary overhead of SSH-ing into each node of your clusters.

---

## Question 29

*Domain 3: Configuring and Deploying Applications*

**Your production application runs on Compute Engine virtual machine instances managed by a managed instance group, with traffic directed through an HTTP(s) load balancer. Despite this setup, users are currently unable to access the application. Your goal is to establish a monitoring mechanism to alert you when the application becomes inaccessible.**

**Which method should you select?**

- [ ] I. Functional tests
- [ ] III. Cloud Load Balancing - health probes
- [ ] IV. Managed instance group - health evaluations
- [x] II. Stackdriver availability checks

### Explanation

The correct option for this scenario is:

**II. Stackdriver availability checks**

**Justification:** Stackdriver availability checks allow you to monitor the availability of your application from various locations globally. By configuring Stackdriver availability checks, you can receive alerts when your application becomes inaccessible, ensuring you're promptly notified of any issues affecting user access. This method directly addresses the goal of establishing a monitoring mechanism to detect when the application becomes inaccessible.

**Why the other options are not suitable:**

I. Functional tests: Functional tests typically involve testing specific functionalities or workflows within your application. While functional tests are valuable for ensuring the correctness of your application's behavior, they may not directly address the need to monitor the overall accessibility of your application from an external perspective.

III. Cloud Load Balancing - health probes: Cloud Load Balancing health probes monitor the health of backend instances within a load balancer's target pool. While health probes are essential for load balancer management and ensuring traffic is directed only to healthy instances, they may not directly alert you when the application as a whole becomes inaccessible from an external perspective.

IV. Managed instance group - health evaluations: Managed instance group health evaluations assess the health of individual instances within the group. While it's crucial to monitor the health of your instances, especially in a managed instance group scenario, this method may not provide direct alerts about the overall accessibility of your application from an external perspective.

---

## Question 30

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Your team is developing an application for a financial institution. The application's frontend operates on Compute Engine, while the data is stored in Cloud SQL and a Cloud Storage bucket. This application will gather data containing Personally Identifiable Information (PII), which will be stored in both the Cloud SQL database and the Cloud Storage bucket. How can you ensure the security of the PII data?**

- [ ] I. 1. Establish specific firewall rules to permit only the frontend to communicate with the Cloud SQL database.
    2\. Utilize IAM to grant access solely to the frontend service account for the Cloud Storage bucket.
- [ ] IV. 1. Configure a private IP address for Cloud SQL.
    2\. Utilize VPC Service Controls (VPC-SC) to create a service perimeter.
    Assign the Cloud SQL database and the Cloud Storage bucket to different service perimeters.
- [ ] II. 1. Implement tailored firewall rules to authorize only the frontend to interact with the Cloud SQL database.
    2\. Enable private access to allow the frontend to securely access the Cloud Storage bucket.
- [x] III. 1. Set up a private IP address for Cloud SQL.
    2\. Utilize VPC Service Controls (VPC-SC) to establish a service perimeter.
    Include both the Cloud SQL database and the Cloud Storage bucket within the same service perimeter.

### Explanation

**The most suitable option is III:**

  * **1\. Set up a private IP address for Cloud SQL.** This prevents direct access to the database from the public internet, enhancing security.

  * **2\. Utilize VPC Service Controls (VPC-SC) to establish a service perimeter. Include both the Cloud SQL database and the Cloud Storage bucket within the same service perimeter.** VPC-SC provides granular control over access between Google Cloud services. Placing both the database and the bucket within a perimeter defends against data exfiltration even if other parts of your project are compromised.

**Why other options are less suitable:**

  * **I.** While firewall rules and IAM are essential security measures, they are not as robust as using private IP addresses and VPC-SC for this sensitive data scenario.

  * **II.** Private Google Access for Cloud Storage is a useful feature, but it's less comprehensive than VPC-SC, which provides more granular, context-aware perimeter protection.

  * **IV.** Separating Cloud SQL and Cloud Storage into different service perimeters introduces additional complexity and could weaken your overall security posture in this scenario.

**Reference:**

<https://cloud.google.com/vpc-service-controls/docs/service-perimeters>

---

## Question 31

*Domain 3: Configuring and Deploying Applications*

**In maintaining a .NET legacy application, your aim is to ensure consistent results during the CI/CD pipeline while minimizing deployment costs and mitigating external factors and dependencies between hosting environments, as containers are not yet sanctioned in your organization. What should be your approach?**

- [ ] III. Deploy the application utilizing MS Web Deploy, ensuring utilization of the latest, patched MS Windows Server base image in Compute Engine.
- [ ] I. Rewrite the application utilizing .NET Core and deploy it to Cloud Run, employing revisions for environment separation.
- [ ] IV. Utilize Cloud Build to package the application and deploy it to a Google Kubernetes Engine cluster, utilizing namespaces for environment separation.
- [x] II. Utilize Cloud Build to deploy the application as a new Compute Engine image for each build, utilizing the same image across all environments.

### Explanation

**Best Choice:**

  * **II. Utilize Cloud Build to deploy the application as a new Compute Engine image for each build, utilizing the same image across all environments.**

**Explanation:**

  * **Consistency:** Creating a golden image with the application pre-installed and baking it into each environment ensures maximal consistency and minimizes external dependencies.

  * **CI/CD Integration:** Cloud Build simplifies image creation and management with automation.

  * **Cost Considerations:** While not as cost-efficient as containers, Compute Engine instances allow better control over costs compared to always-on Kubernetes nodes.

**Why Other Options Are Unsuitableable:**

  * **I. Rewrite the application utilizing .NET Core and deploy it to Cloud Run...**

    * **Major Rewrite:** Rewriting a legacy .NET application for .NET Core could be a significant undertaking that violates your current constraints.

  * **III. Deploy the application utilizing MS Web Deploy...**

    * **Image Management:** Web Deploy is good for quick updates, but doesn't address the image consistency issue for full deployments across environments.

  * **IV. Utilize Cloud Build to package the application and deploy it to a Google Kubernetes Engine cluster...**

    * **Container Requirement:** You explicitly stated that containers are not currently an option in your organization.

**References:**  
[https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud#take_advantage_of_compute_engine](https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud#take_advantage_of_compute_engine  https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud#phase_1_rehost_in_the_cloud  https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud)

[https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud#phase_1_rehost_in_the_cloud](https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud#take_advantage_of_compute_engine  https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud#phase_1_rehost_in_the_cloud  https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud)

[https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud](https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud#take_advantage_of_compute_engine  https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud#phase_1_rehost_in_the_cloud  https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud)

---

## Question 32

*Domain 3: Configuring and Deploying Applications*

**You're developing a new application with specific design requirements:**

**Ensure versioning and auditability of the application infrastructure changes.**

**Optimize the use of Google-managed services for both the application and deployment infrastructure.**

**Utilize a serverless compute platform for the application.**

**Which architecture design should you choose?**

- [x] I.
    I. Maintain the application and infrastructure source code in a Git repository.
    II. Utilize Cloud Build to deploy the application infrastructure using Terraform.
    III. Deploy the application to Cloud Functions within a pipeline step.
- [ ] IV.
    I. Deploy the application infrastructure using gcloud commands.
    II. Define a continuous integration pipeline for application source code changes using Cloud Build.
    III. Implement a pipeline step to fetch the application source code from a Git repository, containerize it.
    IV. Deploy the new container on Cloud Run within the pipeline.
- [ ] II.
    I. Deploy Jenkins from the Google Cloud Marketplace and establish a continuous integration pipeline.
    II. Configure a pipeline step in Jenkins to fetch the application source code from a Git repository.
    III. Deploy the application source code to App Engine within the pipeline.
- [ ] III.
    I. Set up a continuous integration pipeline on Cloud Build and deploy the application infrastructure using Deployment Manager templates.
    II. Implement a pipeline step to create a container with the latest application source code.
    III. Deploy the container to a Compute Engine instance within the pipeline.

### Explanation

**Best Choice:**

  * **I. Maintain the application and infrastructure source code in a Git repository. Utilize Cloud Build to deploy the application infrastructure using Terraform. Deploy the application to Cloud Functions within a pipeline step.**

**Explanation:**

  * **Versioning & Auditability:** Git provides inherent versioning and change tracking for both application code and Infrastructure as Code (IaC) defined in Terraform.

  * **Google-Managed Services:** Cloud Build and Cloud Functions are fully-managed, easing operational burden. Terraform has excellent integration with GCP.

  * **Serverless Alignment:** Cloud Functions is the ideal serverless compute choice for the application tier.

**Why Other Options Are Less Ideal:**

  * **II. Deploy Jenkins ... Deploy the application to App Engine ...**

    * **Operational Overhead:** Jenkins introduces self-management of a VM compared to Cloud Build. App Engine is also less serverless than Cloud Functions.

  * **III. Set up a continuous integration pipeline on Cloud Build ... Deploy the container to a Compute Engine instance ...**

    * **Serverless Mismatch:** While valid for some use cases, deploying a container to a Compute Engine instance misses out on the benefits of serverless compute.

  * **IV. Deploy the application infrastructure using gcloud commands ... Deploy the new container on Cloud Run ...**

    * **Manual Infrastructure:** `gcloud` commands lack the versioning and automation features of IaC tools like Terraform.

**Reference:**

<https://cloud.google.com/docs/ci-cd/products#featured-products-for-cicd>

---

## Question 33

*Domain 3: Configuring and Deploying Applications*

**You’re setting up a container build pipeline for an application hosted on GKE. The requirements are:**

  * **Only images created by your build pipeline should be deployed on the GKE cluster.**

  * **All code and build artifacts must stay within your environment and be protected from data exfiltration.**

**How should you design the pipeline?**

- [ ] D. Use Cloud Build with the default worker pool to create the build pipeline.
    Configure the pipeline to build container images and store them in Artifact Registry.
    Configure the GKE cluster to accept only container images signed by Binary Authorization.
- [ ] A. Use Cloud Build with the default worker pool to create the build pipeline.
    Deploy container images to a private container registry in your VPC.
    Create a VPC firewall policy that denies all egress and ingress traffic to public networks.
- [x] B. Use Cloud Build with a private worker pool to create the build pipeline.
    Use VPC Service Controls to include all CI/CD components and services within a security perimeter.
    Configure the GKE cluster to accept only container images signed by Binary Authorization.
- [ ] C. Use Cloud Build with a private worker pool to create the build pipeline.
    Configure the pipeline to build container images and store them in Artifact Registry.
    Set up Artifact Registry to use customer-managed encryption keys (CMEK) to encrypt container images.

### Explanation

The correct answer is **B**.

Explanation:

To meet the requirements of ensuring that only images created by the build pipeline are deployed on the GKE cluster and to protect code and artifacts from data exfiltration, you should:

  1. **Use Cloud Build with a private worker pool** : This ensures that the build process remains within your private network, isolating it from the public internet and providing additional security for code and build artifacts.

  2. **Use VPC Service Controls** : By configuring a security perimeter around your CI/CD components and services, including Cloud Build, GKE, and Artifact Registry, VPC Service Controls help prevent data exfiltration and enforce strict boundary protection for sensitive data.

  3. **Configure Binary Authorization on GKE** : Binary Authorization allows you to enforce policies that only permit images with the required attestations (e.g., signed images from your build pipeline) to be deployed to the GKE cluster, ensuring that only verified images are used.

Justifications for Incorrect Options:

  * **Option A** : Using the default worker pool in Cloud Build does not provide isolation from the public internet. VPC firewall policies alone do not offer the same level of data exfiltration protection as VPC Service Controls.

  * **Option C** : Although using a private worker pool and customer-managed encryption keys (CMEK) provides some security, it does not fully address the need to prevent data exfiltration without VPC Service Controls. CMEK encrypts stored data but does not provide the comprehensive perimeter protection that VPC Service Controls offer.

  * **Option D** : Using the default worker pool exposes the build pipeline to the public internet, and while Binary Authorization helps secure deployments, it does not address data exfiltration concerns without a private worker pool and VPC Service Controls.

**Relevant Documentation:**

For more information, refer to:

  * [VPC Service Controls](https://cloud.google.com/vpc-service-controls/docs/overview)

  * [Binary Authorization Overview](https://cloud.google.com/binary-authorization/docs/overview)

---

## Question 34

*Domain 4: Integrating Applications with Google Cloud Services*

**You're developing a web application that operates within a Compute Engine instance and is designed to save files to any user's Google Drive. To enable the application to authenticate with the Google Drive API, what course of action should you take?**

- [ ] IV. Employ the App Engine service account with delegated domain-wide authority.
- [ ] III. Employ the App Engine service account along with the https://www.googleapis.com/auth/drive.file scope to generate a signed JSON Web Token (JWT).
- [ ] II. Implement an OAuth Client ID with delegated domain-wide authority.
- [x] I. Utilize an OAuth Client ID configured with the https://www.googleapis.com/auth/drive.file scope to acquire an access token for each user.

### Explanation

**Correct Option:** **I. Utilize an OAuth Client ID configured with the**<https://www.googleapis.com/auth/drive.file> scope to acquire an access token for each user.

**Justification:**

  * **User-Specific Authorization:** OAuth 2.0 is the standard for handling authorization when an application needs to access a user's data on another service (in this case, Google Drive). It gives users granular control over what data your application can access.

  * **Appropriate Scope:** The `https://www.googleapis.com/auth/drive.file` scope grants the necessary permissions to work with files within a user's Drive without providing excessive access.

**Why Other Options Are Less Suitable:**

  * **II. Implement an OAuth Client ID with delegated domain-wide authority:** This provides app-level access to all Drive data within a G Suite domain. Not suitable for user-specific file access, and grants too much power to the application.

  * **III. Employ the App Engine service account with signed JWT:** Service accounts are for server-to-server communication. This option can be used if your app needs its own Drive access, but not for accessing a user's Drive.

  * **IV. Employ the App Engine service account with delegated domain-wide authority:** Again, this would grant the app access to all Drive data within the domain, violating the principle of user-specific permissions.

**Relevant Documentation:**

  * **Google OAuth 2.0 Authorization:** <https://developers.google.com/identity/protocols/oauth2>

  * **Google Drive API - OAuth 2.0 Scopes:** <https://developers.google.com/drive/api/v3/about-auth>

---

## Question 35

*Domain 4: Integrating Applications with Google Cloud Services*

**You are managing multiple APIs for an ecommerce company, and the operations team needs to review traffic patterns in the orders-prod and users-prod environments, which are the only environments within the store-prod environment group. You want to follow Google-recommended practices. What should you do?**

- [x] B. Assign the Apigee Analytics Viewer IAM role to the operations team for both environments, then use Apigee API Analytics to review traffic patterns.
- [ ] C. Assign the Apigee API Reader IAM role to each operations team member for both environments, then use Cloud Monitoring to review traffic patterns.
- [ ] D. Assign the Apigee API Reader IAM role to each operations team member for both environments, then use Apigee API Analytics to review traffic patterns.
- [ ] A. Assign the Apigee Analytics Viewer IAM role to the operations team for both environments, then use Cloud Monitoring to review traffic patterns.

### Explanation

The correct answer is 

**B. Assign the Apigee Analytics Viewer IAM role to the operations team for both environments, then use Apigee API Analytics to review traffic patterns.**

Explanation:

The **Apigee Analytics Viewer IAM role** provides access to Apigee Analytics, which is specifically designed for monitoring and analyzing API traffic patterns. By assigning this role to the operations team, they gain the permissions needed to access detailed analytics on traffic, latency, and errors for the APIs within the `orders-prod` and `users-prod` environments in the Apigee **store-prod** environment group.

Using **Apigee API Analytics** is the recommended approach for reviewing traffic patterns, as it offers API-specific insights that are more relevant and detailed than those available in Cloud Monitoring. Apigee API Analytics provides built-in features like tracking traffic trends, identifying popular API methods, and viewing latency metrics, which are essential for managing and optimizing API performance.

Justifications for Incorrect Options:

  * **Option A: Assign Apigee Analytics Viewer role and use Cloud Monitoring**  
Cloud Monitoring provides general infrastructure metrics, but it lacks the detailed API-specific analytics found in Apigee API Analytics. Apigee Analytics Viewer with Apigee API Analytics is a more focused solution for reviewing API traffic.

  * **Option C: Assign Apigee API Reader role and use Cloud Monitoring**  
The Apigee API Reader role grants read-only access to API proxies and configurations but does not provide access to analytics data. Additionally, Cloud Monitoring is not optimized for API-specific traffic analysis.

  * **Option D: Assign Apigee API Reader role and use Apigee API Analytics**  
The Apigee API Reader role does not include permissions for viewing analytics data. The **Apigee Analytics Viewer** role is necessary to access Apigee’s analytics features.

**Relevant Documentation:**

For more details, refer to:

  * [Apigee Analytics Overview](https://cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview)

  * [Apigee IAM Roles and Permissions](https://cloud.google.com/apigee/docs/apihub/iam-roles)

---

## Question 36

*Domain 3: Configuring and Deploying Applications*

**You are pushing container images to Artifact Registry and deploying a containerized microservices application on GKE. After deployment, you notice unexpected behavior in the services. Upon inspecting the Pods with kubectl get pods, you see that one Pod is in a CrashLoopBackoff state. How should you troubleshoot this Pod?**

- [x] C. Use kubectl logs POD_NAME, where POD_NAME is the problematic Pod’s name, to review logs from previous runs and identify the cause of failed start attempts.
- [ ] A. Connect to the Pod with kubectl exec -it POD_NAME -- /bin/bash, where POD_NAME is the problematic Pod’s name. Check logs in the /var/log/messages folder to identify the issue.
- [ ] B. Run gcloud projects get-iam-policy PROJECT_ID, where PROJECT_ID is the project’s ID for the Artifact Registry. Check IAM bindings of the node pool’s service account to ensure it has roles/artifactregistry.reader permissions.
- [ ] D. In the Google Cloud Console, go to Cloud Logging for the cluster’s VPC project. Filter for denied egress traffic to the Private Google Access CIDR range and verify if egress from the GKE cluster to this range is blocked.

### Explanation

**The correct answer is**

**C. Use kubectl logs POD_NAME, where POD_NAME is the problematic Pod’s name, to review logs from previous runs and identify the cause of failed start attempts.**

Explanation:

When a Pod is in a **CrashLoopBackoff** state, it means the container inside the Pod repeatedly fails to start, causing Kubernetes to restart it. The first step in troubleshooting is to inspect the **Pod’s logs** to understand why the container is crashing. Using `kubectl logs POD_NAME` allows you to view logs for the most recent attempt and any previous failures (`kubectl logs POD_NAME --previous`). These logs often provide direct clues as to why the container is failing to start, such as missing environment variables, incorrect configurations, or application errors.

Justifications for Incorrect Options:

  * **Option A: Connect to the Pod with kubectl exec**  
Since the Pod is in a CrashLoopBackoff state, the container is likely not running long enough to establish a shell connection. Additionally, Kubernetes Pods don’t typically log to `/var/log/messages`, as application logs are usually written to stdout and stderr, which `kubectl logs` retrieves.

  * **Option B: Check IAM permissions for Artifact Registry access**  
While incorrect IAM permissions could prevent access to Artifact Registry, this would cause an `ImagePullBackOff` error, not a CrashLoopBackoff. If the container was deployed successfully, the issue is likely related to the application or its configuration within the container.

  * **Option D: Check Cloud Logging for denied egress traffic to the Private Google Access CIDR range**  
This option is relevant if there are network issues affecting access to external resources; however, a CrashLoopBackoff is typically caused by container-specific errors rather than network configurations. Network issues would more likely prevent the application from functioning properly after starting, rather than causing repeated crashes at startup.

---

## Question 37

*Domain 2: Building and Testing Applications*

**You're preparing to migrate your Compute Engine application to Google Kubernetes Engine (GKE). As part of this process, you need to build a container image and push it to Artifact Registry using Cloud Build. Which steps should you take? (Select two.)**

- [x] A. Execute `gcloud builds submit` in the directory containing the application source code.
- [ ] B. Run `gcloud run deploy app-name --image gcr.io/$PROJECT_ID/app-name` in the directory housing the application source code.
- [ ] E. Within the application source directory, generate a file named `cloudbuild.yaml` with the following content:
    steps:
    \- name: 'gcr.io/cloud-builders/cloud'
    args: ['app', 'deploy']
    timeout: '1600s'
- [ ] C. Use `gcloud container images add-tag gcr.io/$PROJECT_ID/app-name gcr.io/$PROJECT_ID/app-name:latest` in the application source directory.
- [x] D. Create a file named `cloudbuild.yaml` in the application source directory, and include the following content:
    steps:
    \- name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/app-name', '.']
    \- name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/app-name']

### Explanation

**Correct Answers:**

  * **A. Execute**`**gcloud builds submit**`**in the directory containing the application source code.**

    * **Justification:** This command triggers Cloud Build to execute a build process, typically defined in a `cloudbuild.yaml` file. It will handle containerizing your application and pushing the image to Artifact Registry.

  * **D. Create a file named**`**cloudbuild.yaml**`**in the application source directory, and include the following content:**

YAML
        
                    1. steps:
            2. - name: 'gcr.io/cloud-builders/docker'
            3.   args: ['build', '-t', 'gcr.io/$PROJECT_ID/app-name', '.']
            4. - name: 'gcr.io/cloud-builders/docker'
            5.   args: ['push', 'gcr.io/$PROJECT_ID/app-name']

* **Justification:** This `cloudbuild.yaml` file provides Cloud Build with the instructions to:

      1. Build the Docker image from your application code and tag it appropriately for Artifact Registry.

      2. Push the built image to Artifact Registry.

**Incorrect Answers:**

  * **B. Run**`**gcloud run deploy app-name --image gcr.io/$PROJECT_ID/app-name**`**...**

    * **Reasoning:** This is a command for deploying an application to Cloud Run (a separate service), not for building and pushing images to Artifact Registry.

  * **C. Use**`**gcloud container images add-tag gcr.io/$PROJECT_ID/app-name gcr.io/$PROJECT_ID/app-name:latest**`**...**

    * **Reasoning:** This command deals with re-tagging existing container images, not the primary build-and-push process.

  * **E. Within the application source directory, generate a file named**`**cloudbuild.yaml**`**...**

    * **Reasoning:** The `cloudbuild.yaml` content provided here is related to deploying to Cloud App Engine, not for containerization and Artifact Registry.

---

## Question 38

*Domain 3: Configuring and Deploying Applications*

**You’re using Cloud Build to build and test container images before deploying them to Cloud Run. The images are stored in Artifact Registry, and you need to ensure that only images that have passed testing are deployed, with minimal operational overhead. What should you do?**

- [ ] **A.** Deploy a new revision to a **Cloud Run** service and assign it a tag that provides access at a specific URL without serving traffic. Test this revision, and once confirmed, migrate traffic to the new revision.
- [ ] **D.** Configure **build provenance** on your **Cloud Build** pipeline, confirm all tests have passed, and deploy the image to a **Cloud Run** service.
- [ ] **C.** Set up a **GKE cluster** , verify that all tests have passed, and deploy the image to the **GKE cluster**.
- [x] **B.** Enable **Binary Authorization** on your **Cloud Run** service. Create an attestation for images that pass all tests, and configure **Binary Authorization** to allow only images with valid attestations to be deployed.

### Explanation

**The correct answer is**

**B. Enable Binary Authorization on your Cloud Run service. Create an attestation for images that pass all tests, and configure Binary Authorization to allow only images with valid attestations to be deployed.**

Explanation:

**Binary Authorization** provides a security layer that ensures only container images meeting specific criteria, such as passing all tests, are deployed to production environments like **Cloud Run**. By configuring Binary Authorization with attestations, you can require that only images that pass testing (and have corresponding attestations) are allowed to be deployed. This approach automates enforcement of deployment policies with minimal operational overhead, as Binary Authorization will automatically block any unapproved images.

Justifications for Incorrect Options:

  * **Option A: Deploy a new revision and assign it a tag**  
This option requires manual steps to test and shift traffic to the new revision. Although it provides a mechanism for testing, it does not enforce strict control over which images can be deployed, nor does it prevent untested images from being deployed.

  * **Option C: Set up a GKE cluster and deploy the image**  
Deploying to GKE introduces additional complexity, as Cloud Run is the intended deployment environment in this scenario. This option does not address the requirement for controlled deployment based on testing results, nor does it leverage Binary Authorization.

  * **Option D: Configure build provenance on your Cloud Build pipeline**  
Build provenance tracks the source and build process of an artifact but does not enforce deployment rules based on test results. Provenance alone does not restrict deployments to tested images, nor does it automatically prevent untested images from being deployed.

**Relevant Documentation:**

For more on Binary Authorization and using attestations to control deployments, refer to:

  * [Binary Authorization Overview](https://cloud.google.com/binary-authorization/docs/overview)

  * [Binary Authorization with Cloud Run](https://cloud.google.com/binary-authorization/docs/run/enabling-binauthz-cloud-run)

---

## Question 39

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**As a developer at an ecommerce company, you manage a website that stores customer order data in a Cloud SQL for PostgreSQL database. Data scientists on the marketing team access this data to generate reports, which negatively impacts website performance. You need to provide access to up-to-date customer order datasets without affecting website performance. What should you do?**

- [x] C. Create a BigQuery dataset for the data science team and configure Datastream to replicate relevant Cloud SQL tables in BigQuery.
- [ ] B. Set up a Bigtable table for the data science team, and configure the application to write to both Cloud SQL and Bigtable simultaneously.
- [ ] D. Create a clone of the PostgreSQL database instance for the data science team, and schedule a job to update the clone every 15 minutes.
- [ ] A. Use Cloud Scheduler to run an hourly Cloud Function that exports data from Cloud SQL into CSV format and stores it in a Cloud Storage bucket.

### Explanation

The correct answer is 

**C. Create a BigQuery dataset for the data science team and configure Datastream to replicate relevant Cloud SQL tables in BigQuery.**

Explanation:

This approach provides the **data scientists with access to up-to-date customer order data** in **BigQuery** , a platform designed for large-scale data analysis, without impacting the performance of the primary Cloud SQL database used by the website. **Datastream** can replicate data from Cloud SQL to BigQuery in near-real time, ensuring the data is current and readily available for analysis. BigQuery’s scalability and analytics capabilities make it an ideal choice for data science and reporting workloads.

Justifications for Incorrect Options:

  * **Option A: Use Cloud Scheduler with Cloud Function to export data to Cloud Storage**  
While this method would provide access to up-to-date data in Cloud Storage, the exported data would not be in a format that is optimal for querying and analysis. This setup also introduces delays depending on the frequency of exports and lacks the powerful querying capabilities of BigQuery.

  * **Option B: Set up a Bigtable table and configure the application to write to both Cloud SQL and Bigtable**  
Writing to two databases simultaneously increases the application’s complexity and operational burden. Additionally, Bigtable is designed for high-throughput analytical data, not transactional data, and would not be ideal for ad hoc data science queries.

  * **Option D: Create a clone of the PostgreSQL database and schedule updates**  
Regularly updating a cloned database adds overhead and may not reflect real-time data, especially if updates are only every 15 minutes. This approach is less efficient and scalable compared to using BigQuery with Datastream.

**Relevant Documentation:**

For more on real-time data replication from Cloud SQL to BigQuery, refer to:

  * [Datastream for BigQuery Integration](https://cloud.google.com/datastream-for-bigquery?hl=en)

---

## Question 40

*Domain 4: Integrating Applications with Google Cloud Services*

**You have two Google Cloud projects, Project A and Project B. Your objective is to create a Cloud Function in Project A that stores its output in a Cloud Storage bucket located in Project B while ensuring the principle of least privilege. What actions should you take?**

- [ ] III. 1. Identify the default App Engine service account (PROJECT_ID@appspot.gserviceaccount.com) within Project A.
    2\. Deploy the Cloud Function in Project A with the default App Engine service account.
    Allocate the roles/storage.objectCreator role to the default App Engine service account for the storage bucket in Project B.
- [ ] I. 1. Generate a Google service account within Project B.
    2\. Deploy the Cloud Function in Project A using this service account.
    Grant the roles/storage.objectCreator role to this service account for the storage bucket in Project B.
- [x] II. 1. Create a Google service account within Project A.
    2\. Deploy the Cloud Function in Project A with this service account.
    Assign the roles/storage.objectCreator role to this service account for the storage bucket in Project B.
- [ ] IV. 1. Identify the default App Engine service account (PROJECT_ID@appspot.gserviceaccount.com) within Project B.
    2\. Deploy the Cloud Function in Project A with the default App Engine service account.
    Delegate the roles/storage.objectCreator role to the default App Engine service account for the storage bucket in Project B.

### Explanation

**II. 1. Create a Google service account within Project A. 2. Deploy the Cloud Function in Project A with this service account. Assign the roles/storage.objectCreator role to this service account for the storage bucket in Project B.****

Here's why this is the most secure and adheres to best practices:

  * **Project Isolation:** Creating the service account in Project A keeps permissions contained within the project where the function originates.

  * **Least Privilege:** The `roles/storage.objectCreator` role grants the function only the permission to create objects in the bucket, preventing unnecessary access to other resources in Project B.

  * **Specific Service Account:** Using a dedicated service account for the Cloud Function limits the impact if the key is compromised.

**Why other options are less ideal:**

  * **I.** While similar to the recommended approach, creating the service account in Project B gives that project an unnecessary level of control over the Cloud Function.

  * **III & IV.** Using the default App Engine service account has broader permissions than necessary, violating the principle of least privilege.

**Reference:**  
<https://articles.wesionary.team/multi-project-account-service-account-in-gcp-ba8f8821347e>

---

## Question 41

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Your organization is preparing to transfer its on-premises Hadoop ecosystem to the cloud due to mounting concerns regarding the escalating expenses and upkeep associated with storing data in HDFS. Minimizing alterations to existing data analytics processes and infrastructure is a priority.**

**What is the recommended approach for executing the migration?**

- [x] IV. Deploy a Cloud Dataproc cluster on Google Cloud Platform (GCP), migrate your Hadoop code artifacts to this cluster, and transfer your data to Cloud Storage. Utilize the Cloud Dataproc connector to execute jobs on this data.
- [ ] III. Establish a Cloud Dataproc cluster on Google Cloud Platform (GCP), then transfer your Hadoop environment to this new cluster. Transition your HDFS data to larger HDD disks to mitigate storage expenditures.
- [ ] I. Shift your Hadoop data to BigQuery and adapt your data analytics workflows to access data directly from BigQuery, eliminating reliance on the on-premises Hadoop environment.
- [ ] II. Create Compute Engine instances equipped with HDD (Hard Disk Drive) technology instead of SSD (Solid State Drive) to curtail costs, followed by a comprehensive migration of your current environment onto these instances.

### Explanation

**Best Choice:**

  * **IV. Deploy a Cloud Dataproc cluster on Google Cloud Platform (GCP), migrate your Hadoop code artifacts to this cluster, and transfer your data to Cloud Storage. Utilize the Cloud Dataproc connector to execute jobs on this data.**

**Reasons:**

  * **Minimal Disruption:** Cloud Dataproc provides a managed Hadoop environment on GCP, offering the smoothest migration path for your existing Hadoop setup. This minimizes the need for significant code changes to your data analytics jobs.

  * **Optimized and Scalable Storage:** Separating storage from compute by using Cloud Storage gives you greater flexibility. It allows you to store data cost-effectively with independent scaling of storage and compute resources.

  * **Seamless Integration:** Cloud Dataproc's built-in connector to Cloud Storage enables your existing Hadoop jobs to work with Cloud Storage as if it were an extension of HDFS.

**Why Other Options Are Less Ideal**

  * **I. Shift your Hadoop data to BigQuery and adapt your data analytics workflows to access data directly from BigQuery, eliminating reliance on the on-premises Hadoop environment.**

    * **Tool Mismatch:** BigQuery is a powerful data warehouse but it's optimized for structured data analysis using SQL-like queries. If your analytics workflows are heavily dependent on general-purpose Hadoop tools and processing, significant rewrites might be necessary.

  * **II. Create Compute Engine instances equipped with HDD (Hard Disk Drive) technology instead of SSD (Solid State Drive) to curtail costs, followed by a comprehensive migration of your current environment onto these instances.**

    * **Limited Benefits:** This approach reduces costs but essentially replicates your on-premises setup in the cloud. It doesn't fully leverage cloud-native storage solutions for the scalability and cost benefits you're aiming for.

  * **III. Establish a Cloud Dataproc cluster on Google Cloud Platform (GCP), then transfer your Hadoop environment to this new cluster. Transition your HDFS data to larger HDD disks to mitigate storage expenditures.**

    * **Storage Coupling:** While Cloud Dataproc provides benefits, keeping data within its HDFS system still couples storage with compute. This is less flexible than using Cloud Storage for independent scaling.

**References:**

<https://cloud.google.com/architecture/hadoop/hadoop-gcp-migration-overview>

---

## Question 42

*Domain 3: Configuring and Deploying Applications*

**You are migrating a containerized application to Cloud Run and plan to use Cloud Build to build and push your container image to Artifact Registry. For deployment, you’ll use Cloud Deploy to move the image to production. To ensure that only secure images are deployed, what should you do?**

- [ ] **C.** Store the encrypted image in **Secret Manager** and deploy it to production.
- [ ] **B.** Enable **Artifact Analysis** to scan the image for vulnerabilities, and use **Cloud Key Management Service** (KMS) to encrypt the image before deployment to production.
- [ ] **A.** Use **Cloud Armor** in front of **Cloud Run** to protect the container image from threats.
- [x] **D.** Use **Binary Authorization** to enforce a policy allowing only images signed with a trusted key to be deployed to production.

### Explanation

The correct answer is 

**D. Use Binary Authorization to enforce a policy allowing only images signed with a trusted key to be deployed to production.**

Explanation:

**Binary Authorization** is a security feature that allows you to define and enforce policies to ensure that only trusted and verified container images are deployed to production. By configuring Binary Authorization to require a signed attestation, you can enforce that only images that have passed security checks (such as vulnerability scans) and are signed with a trusted key are deployed. This approach is directly aligned with best practices for securing container deployments on Google Cloud.

Justifications for Incorrect Options:

  * **Option A: Use Cloud Armor in front of Cloud Run to protect the container image from threats**  
Cloud Armor provides network-level protection by filtering incoming requests based on rules but does not control or verify container images. It does not enforce security on the images themselves.

  * **Option B: Enable Artifact Analysis and use Cloud Key Management Service (KMS) to encrypt the image**  
While Artifact Analysis is useful for vulnerability scanning, encrypting the image with KMS is unnecessary for deployment. The critical step is using Binary Authorization to enforce deployment policies based on the security of the image.

  * **Option C: Store the encrypted image in Secret Manager and deploy it to production**  
Secret Manager is designed to store sensitive configuration data, not container images. Artifact Registry is the appropriate place for storing container images, with Binary Authorization used to enforce deployment security.

**Relevant Documentation:**

For more information on Binary Authorization and Artifact Analysis, refer to:

  * [Binary Authorization Overview](https://cloud.google.com/binary-authorization/docs/overview)

---

## Question 43

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You are building a scalable web application for internal users in an organization that uses Google Workspace. You need to set up user authentication for the application and deploy it on Google Cloud. You aim to leverage cloud-native features and minimize infrastructure management. What should you do? (Choose two.)**

- [ ] C. Set up a Cloud SQL database with a table containing users and password hashes. Add an authentication screen to restrict access to internal users only.
- [x] D. Configure Identity-Aware Proxy (IAP) and assign the roles/iap.httpsResourceAccessor IAM role to users needing access.
- [x] B. Containerize the application and deploy it as a Cloud Run service.
- [ ] E. Configure Identity-Aware Proxy (IAP) and assign the roles/iap.tunnelResourceAccessor IAM role to users needing access.
- [ ] A. Create a Compute Engine VM, set up a web server, and deploy the application in a VPC.

### Explanation

The correct answers are

**B. Containerize the application and deploy it as a Cloud Run service** and 

**D. Configure Identity-Aware Proxy (IAP) and assign the roles/iap.httpsResourceAccessor IAM role to users needing access.**

Explanation:

  1. **Containerize the application and deploy it as a Cloud Run service (Option B):**

     * **Cloud Run** is a fully managed serverless platform that automatically scales applications based on demand, making it ideal for minimizing infrastructure management.

     * Deploying on Cloud Run enables cloud-native features, such as autoscaling and integration with Google Cloud services, while reducing the operational burden on infrastructure management.

  2. **Configure Identity-Aware Proxy (IAP) and assign the**`**roles/iap.httpsResourceAccessor**`**IAM role (Option D):**

     * **Identity-Aware Proxy (IAP)** provides a secure way to control access to your application by integrating with Google Workspace. IAP authenticates users via their Google Workspace credentials, restricting access to only internal users within the organization.

     * The `roles/iap.httpsResourceAccessor` role allows users to access HTTPS resources protected by IAP, making it the appropriate role for securing a web application deployed on Cloud Run.

Justifications for Incorrect Options:

  * **Option A: Create a Compute Engine VM and deploy the application in a VPC**

    * Deploying on Compute Engine would require significant infrastructure management, including managing VM instances, web server configurations, and scaling. This approach does not align with the goal of minimizing infrastructure management.

  * **Option C: Set up a Cloud SQL database with a table containing users and password hashes**

    * Using a custom authentication mechanism with Cloud SQL and password hashes would require building and maintaining user authentication infrastructure. It is less secure and more complex than using Google Workspace and IAP for user authentication.

  * **Option E: Configure IAP and assign the**`**roles/iap.tunnelResourceAccessor**`**IAM role**

    * The `roles/iap.tunnelResourceAccessor` role is used for TCP forwarding and is not relevant for protecting HTTPS web applications. The correct role for HTTPS access is `roles/iap.httpsResourceAccessor`.

**Relevant Documentation:**

For further details, refer to:

  * [Deploying to Cloud Run](https://cloud.google.com/run/docs/deploying)

  * [Identity-Aware Proxy Overview](https://cloud.google.com/iap/docs/concepts-overview)

---

## Question 44

*Domain 3: Configuring and Deploying Applications*

**Which approach should you take to efficiently configure an application deployed on Compute Engine instances across multiple projects, each representing a different environment in your software development process (development, QA, staging, and production)?**

- [ ] III. Deploy your chosen deployment tool on an instance within each project. Utilize a deployment job to fetch the relevant configuration file from your version control system and apply it during application deployment on each instance.
- [x] II. Configure a metadata key within each project named "environment" and set its value to reflect the environment served by the instance. Use a deployment tool to access instance metadata and configure the application based on the "environment" value.
- [ ] IV. Configure an instance custom-metadata key named "environment" with the appropriate environment value during each instance launch. Use your deployment tool to access instance metadata and configure the application based on the "environment" value.
- [ ] I. Utilize a startup script with the gcloud command when creating instances, which determines the project name indicating the environment, to configure the application accordingly.

### Explanation

**The most efficient approach to configure an application deployed on Compute Engine instances across multiple projects, each representing a different environment, would be:**

**II. Configure a metadata key within each project named "environment" and set its value to reflect the environment served by the instance. Use a deployment tool to access instance metadata and configure the application based on the "environment" value.**

**Justification:**

Option II allows for centralizing the configuration management by utilizing project metadata. By setting a metadata key named "environment" within each project and assigning values corresponding to the environment (e.g., development, QA, staging, production), you can easily identify and manage the environment of each instance.

Using a deployment tool to access instance metadata simplifies the configuration process. The deployment tool can retrieve the "environment" metadata value and configure the application accordingly during deployment. This approach promotes consistency and reduces the complexity of managing configurations across multiple environments.

**Why the other options are not as efficient:**

I. Utilizing a startup script with the gcloud command when creating instances may introduce complexity and potential inconsistencies, especially when dealing with multiple projects and environments. Managing configuration directly within the startup script could lead to maintenance challenges and difficulties in ensuring uniformity across environments.

III. Deploying a deployment tool on an instance within each project and fetching configuration files from a version control system adds unnecessary overhead. It requires additional resources and introduces dependencies on the instance running the deployment tool. This approach may also complicate the configuration management process, especially in large-scale deployments.

IV. Configuring instance custom-metadata keys named "environment" during instance launch introduces manual steps and potential errors. It requires ensuring that the correct metadata keys and values are set for each instance, which could lead to inconsistencies or misconfigurations across environments. Additionally, relying solely on instance metadata for configuration may not be as robust or scalable as leveraging a dedicated deployment tool.

**References:**

[https://cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom-project-wide-metadata](https://cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom-project-wide-metadata  https://cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom)

[https://cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom](https://cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom-project-wide-metadata  https://cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom)

---

## Question 45

*Domain 3: Configuring and Deploying Applications*

**You aim to restrict your App Engine standard configuration to a maximum of 5 instances while using the following setup:**

**Which code snippet should be integrated into your configuration to achieve this?**

- [ ] I. Utilize manual scaling with a set number of instances and a minimum pending latency of 30ms.
- [ ] III. Opt for basic scaling with a designated number of instances set at 5 and a minimum pending latency of 30ms.
- [ ] II. Employ manual scaling with a maximum instance limit of 5 and an idle timeout of 10 minutes.
- [x] IV. Choose basic scaling with a cap on the maximum instances set to 5 and an idle timeout of 10 minutes.

### Explanation

**Correct Choice:**

  * **IV. Choose basic scaling with a cap on the maximum instances set to 5 and an idle timeout of 10 minutes.**

**Explanation:**

  * **Basic Scaling:** App Engine standard environment offers two scaling types: basic and automatic. Basic scaling allows you to directly control the maximum number of instances.

  * **Maximum Instances:** The `max_instances` setting within your configuration file enables you to explicitly limit the number of instances to 5.

  * **Idle Timeout:** The `idle_timeout` setting is relevant for basic scaling, ensuring that instances that remain inactive for 10 minutes are shutdown, thus conserving resources.

**Incorrect Options:**

  * **I. Utilize manual scaling with a set number of instances and a minimum pending latency of 30ms.**

    * **Manual Scaling Limitation:** Manual scaling is used to set a fixed number of instances, not a maximum. It doesn't allow you to cap the instances dynamically based on traffic.

  * **II. Employ manual scaling with a maximum instance limit of 5 and an idle timeout of 10 minutes.**

    * **No Such Setting:** Manual scaling in App Engine doesn't have a `max_instances` setting.

  * **III. Opt for basic scaling with a designated number of instances set at 5 and a minimum pending latency of 30ms.**

    * **Basic Scaling Limitation:** With basic scaling, you control the maximum, not a fixed number of instances. Your app could still run fewer instances.

**References:**  
[https://cloud.google.com/appengine/docs/legacy/standard/python/how-instances-are-managed#scaling_types](https://cloud.google.com/appengine/docs/legacy/standard/python/how-instances-are-managed#scaling_types  https://cloud.google.com/appengine/docs/standard/reference/app-yaml?tab=python#manual_scaling)

[https://cloud.google.com/appengine/docs/standard/reference/app-yaml?tab=python#manual_scaling](https://cloud.google.com/appengine/docs/legacy/standard/python/how-instances-are-managed#scaling_types  https://cloud.google.com/appengine/docs/standard/reference/app-yaml?tab=python#manual_scaling)

---

## Question 46

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Which compute platform would be most suitable for optimizing costs while efficiently handling unpredictable traffic patterns in a single-player mobile game backend?**

- [x] I. Cloud Run
- [ ] IV. Google Kubernetes Engine using cluster autoscaling
- [ ] II. Compute Engine with managed instance groups
- [ ] III. Compute Engine with unmanaged instance groups

### Explanation

**Best Choice:**

  * **I. Cloud Run**

**Explanation:**

  * **True Serverless:** Cloud Run enables scaling down to zero instances when there's no traffic, perfect for unpredictable workloads. This directly minimizes costs during idle periods.

  * **Autoscaling:** Cloud Run rapidly scales up to handle sudden traffic bursts, ensuring your game backend remains responsive even with unexpected activity.

  * **Focus on Application:** Cloud Run abstracts away infrastructure management, letting you focus on your game's logic.

**Why Other Options Are Less Ideal:**

  * **II. Compute Engine with managed instance groups**

    * **Cost of Idling Instances:** Managed instance groups help with scaling, but there's still a baseline cost associated with running VMs even when they're not handling traffic.

  * **III. Compute Engine with unmanaged instance groups**

    * **Operational Overhead:** Unmanaged instance groups offer more control but introduce the significant burden of manual scaling and infrastructure management.

  * **IV. Google Kubernetes Engine using cluster autoscaling**

    * **Overhead and Complexity:** While GKE is powerful, it introduces a degree of Kubernetes cluster management that might be unnecessary for a single-player game's backend, especially if your team is not already well-versed in Kubernetes.

---

## Question 47

*Domain 3: Configuring and Deploying Applications*

**You are setting up monitoring for your application deployed on a Compute Engine virtual machine instance equipped with the Stackdriver Monitoring Agent. The application functions as a Unix process on the instance. Your objective is to receive alerts if the Unix process remains inactive for at least 5 minutes. Given the limitation that you cannot modify the application to produce metrics or logs, what alert condition should you establish?**

- [x] II. Process status evaluation
- [ ] IV. Metric level benchmark
- [ ] III. Metric nonexistence detection
- [ ] I. System availability assessment

### Explanation

**Correct Option: II. Process status evaluation**

**Justification:**

  * **Process Status Evaluation Focus:** Process status checks directly monitor whether a particular process is running or not, aligning precisely with the goal of detecting inactivity.

  * **Monitoring Agent Capability:** The Stackdriver Monitoring Agent can track system-level metrics, including the existence and state of Unix processes. This makes process status evaluation a readily achievable monitoring method with the existing setup.

**Reasons Why Other Options Are Incorrect:**

  * **I. System Availability Assessment:** While useful for overall system health, this is too broad. A system could be available, but the specific application process might be inactive.

  * **III. Metric Nonexistence Detection:** This is relevant when a process _should_ produce metrics. This approach would fail to signal if the process is expected to be inactive for periods and thus naturally produce no metrics.

  * **IV. Metric Level Benchmark:** This involves comparing metrics to thresholds, which is not suitable when the goal is to detect the very absence of activity and the implied lack of any metrics.

**References:**  
[https://cloud.google.com/monitoring/alerts/policies-in-json#json-process-health](https://cloud.google.com/monitoring/alerts/policies-in-json#json-process-health  https://cloud.google.com/monitoring/alerts/types-of-conditions#metric-threshold)

[https://cloud.google.com/monitoring/alerts/types-of-conditions#metric-threshold](https://cloud.google.com/monitoring/alerts/policies-in-json#json-process-health  https://cloud.google.com/monitoring/alerts/types-of-conditions#metric-threshold)

---

## Question 48

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**In designing a schema for a table transitioning from MySQL to Cloud Bigtable, consider the following MySQL table:**

**Account_Activity**

**(**

**Account_id int,**

**Event_timestamp datetime,**

**Transaction_type string,**

**Amount numeric (18,4)**

**)**

**primary key (Account_id, Event_timestamp)**

**What should be the appropriate row key for Cloud Bigtable?**

- [ ] D. Use Event_timestamp as the key.
- [ ] C. Use Event_timestamp_Account_id as the key.
- [x] B. Use Account_id_Event_timestamp as the key.
- [ ] A. Use Account_id as the key.

### Explanation

Here's a breakdown of why option **B (Use Account_id_Event_timestamp as the key)** is the most suitable row key design for transitioning your MySQL table to Cloud Bigtable, along with explanations about why the other options aren't as ideal.

**Correct Answer:**

  * **B. Use Account_id_Event_timestamp as the key.**

**Justification:**

  * **Bigtable Row Key Importance:** In Bigtable, rows are sorted lexicographically by row key; therefore, row key design heavily impacts how your data is stored and how efficiently it can be queried (Bigtable Documentation: <https://cloud.google.com/bigtable/docs/schema-design>).

  * **Uniqueness and Distribution:** Composing the row key as `Account_id_Event_timestamp` achieves the following:

    * **Uniqueness:** Ensures each row is unique, reflecting the original MySQL primary key constraint.

    * **Distribution:** Helps distribute data across Bigtable nodes for better scalability. Using just `Account_id` could lead to hot spotting (too much data on one node) if some accounts have far more activity than others.

**Incorrect Answers:**

  * **A. Use Account_id as the key.**

    * **Reasoning:** While simple, this risks hot spotting; all rows for a single account would be stored together. If some accounts have vastly more activity than others, this could overload a part of the cluster, impacting performance.

  * **C. Use Event_timestamp_Account_id as the key.**

    * **Reasoning:** This primarily sorts by time. If you need to query based on accounts frequently, it would require less efficient table scans.

  * **D. Use Event_timestamp as the key.**

    * **Reasoning:** This fails to ensure uniqueness by itself, as multiple transactions could occur at the same timestamp for different accounts.

---

## Question 49

*Domain 3: Configuring and Deploying Applications*

**You have a container deployed on Google Kubernetes Engine. Occasionally, the container experiences delays in launching, leading to failures in the liveness probe. What is the recommended action to address this issue?**

- [x] I. Implement a startup probe.
- [ ] III. Raise the CPU limit for the container.
- [ ] II. Extend the initial delay for the liveness probe.
- [ ] IV. Introduce a readiness probe.

### Explanation

**The recommended action to address the issue of occasional delays in container launching, leading to failures in the liveness probe, is:**

**I. Implement a startup probe.**

**Explanation:**

  * **A startup probe is specifically designed to determine if a container has started successfully before the liveness probe is activated.**

  * **By implementing a startup probe, you can delay the execution of the liveness probe until the container has had sufficient time to start up and initialize properly.**

  * **This helps prevent false-positive liveness probe failures caused by temporary delays during container startup, allowing the container to become ready and available for handling traffic only after it has fully initialized and is able to respond to requests properly.**

The other options can be explained as follows:

II. Extending the initial delay for the liveness probe may provide some temporary relief by giving the container more time to start up before the probe starts checking its health. However, this approach does not address the root cause of the issue and may result in longer detection times for actual liveness failures.

III. Raising the CPU limit for the container might improve its performance but is unlikely to directly resolve delays in container startup. CPU limits are more relevant for managing resource allocation and preventing resource contention, rather than addressing startup delays.

IV. Introducing a readiness probe is also a good practice, but it specifically checks if the container is ready to handle traffic. While it helps ensure that only healthy containers receive traffic, it does not directly address delays in container startup, which is the primary concern in this scenario.

**Reference:**

<https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-startup-probes>

---

## Question 50

*Domain 4: Integrating Applications with Google Cloud Services*

**Your colleague has requested your input on the following code snippet, which aims to efficiently add a substantial number of small rows to a BigQuery table.**

**BigQuery service = BigQueryOptions.newBuilder().build().getService();**

**for (Map <String, String> row : rows) {**

**public void writeToBigQuery(Collection <Map<String, String>> rows) {**

**InsertAllRequest insertRequest = InsertAllRequest.newBuilder(**

**"datasetId", "tableId",**

**InsertAllRequest.RowToInsert.of(row)).build();**

**service.insertAll(insertRequest);**

**}**

**}**

**What improvement should you suggest to your colleague?**

- [ ] B. Execute the inserts concurrently by employing multiple threads.
- [x] A. Batch multiple rows with each request.
- [ ] C. Direct each row to a Cloud Storage object, then ingest into BigQuery.
- [ ] D. Parallelize the process by directing each row to a Cloud Storage object, then ingest into BigQuery.

### Explanation

The most suitable improvement to suggest to your colleague is:

**A. Batch multiple rows with each request.**

Justification:

  * Batching multiple rows with each request reduces the overhead of making individual API calls to BigQuery for each row, resulting in improved performance and efficiency.

  * BigQuery supports batch inserts through the `**InsertAllRequest**` object, allowing multiple rows to be inserted in a single API call.

  * This approach minimizes network latency and API overhead compared to making separate API calls for each row, which is crucial when adding a substantial number of small rows to a BigQuery table.

Why other options are not as suitable:

B. Executing inserts concurrently by employing multiple threads might introduce complexity and potential issues related to thread safety and resource contention. While it could potentially improve throughput, it might not be as straightforward to implement and could lead to diminishing returns or even performance degradation due to contention for shared resources.

C. Directing each row to a Cloud Storage object and then ingesting into BigQuery adds unnecessary complexity to the process. This approach involves additional steps of writing data to Cloud Storage, managing Cloud Storage objects, and then ingesting the data into BigQuery, which may not be required for the given scenario.

D. Parallelizing the process by directing each row to a Cloud Storage object and then ingesting into BigQuery suffers from similar drawbacks as option C. Additionally, it introduces additional complexity without clear benefits compared to simply batching multiple rows with each request.

---

## Question 51

*Domain 2: Building and Testing Applications*

**Your ecommerce application, which forwards requests to third-party API services for credit card processing, shipping, and inventory management, is experiencing intermittent performance issues reported by customers. However, the application lacks metrics for diagnosis. What action should you take to identify the cause of these performance inconsistencies?**

**

**

- [ ] D. Activate Managed Service for Prometheus on your Google Kubernetes Engine cluster to collect application metrics.
- [ ] C. Adjust your application to include and propagate the X-Cloud-Trace-Context header when communicating with downstream services.
- [ ] B. Deploy the Ops Agent within your container and configure it to collect application metrics.
- [x] A. Implement the OpenTelemetry library in your application code to enable instrumentation.

### Explanation

**A. Implement the OpenTelemetry library in your application code to enable instrumentation.**

Justification:

  * OpenTelemetry is a powerful observability framework that allows you to instrument your code to collect telemetry data such as traces, metrics, and logs.

  * By instrumenting your application code with OpenTelemetry, you can gather detailed information about the execution of requests, including latency measurements, service dependencies, and error rates.

  * OpenTelemetry supports various programming languages and frameworks, making it suitable for a wide range of applications, including containerized microservices running in Kubernetes clusters.

  * Once implemented, OpenTelemetry can provide insights into the performance of your application and help pinpoint the root cause of intermittent performance issues.

  * It is important to collect metrics and traces directly from your application code to gain visibility into internal operations and interactions with third-party API services.

Options B, C, and D are less suitable for this scenario due to the following reasons:

B. Deploying the Ops Agent within your container and configuring it to collect application metrics may provide some insights into the performance of your application, but it may not capture all relevant data needed for diagnosis, especially if the performance issues originate from interactions with third-party API services.

C. Adjusting your application to include and propagate the X-Cloud-Trace-Context header when communicating with downstream services is a best practice for tracing requests in distributed systems. While this can help trace requests, it does not provide detailed performance metrics and may not be sufficient for diagnosing intermittent performance issues.

D. Activating Managed Service for Prometheus on your Google Kubernetes Engine cluster can collect application metrics, but it primarily focuses on infrastructure-level metrics rather than application-level metrics. While it can provide insights into resource utilization and cluster health, it may not capture the specific telemetry data needed to diagnose performance issues within your application code.

---

## Question 52

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You're designing a chat room application with Firestore as the database. Application will host multiple rooms and retain the message history for each room. How should you structure the data in Firestore?**

- [x] C. Create a collection for the rooms. Each room's document will contain a subcollection for messages, with each message stored as a document.
- [ ] D. Create a collection for the rooms. Each room will have a document, and a separate collection for messages will be created, with one document per message. Each room's document will contain references to the messages.
- [ ] B. Create a collection for the rooms. Each room will have a collection containing a document for each message.
- [ ] A. Create a collection for the rooms. Each room will have a document listing the contents of its messages.

### Explanation

**Correct Answer:**

  * **C. Create a collection for the rooms. Each room's document will contain a subcollection for messages, with each message stored as a document.**

**Justification:**

  * **Hierarchical Structure:** Subcollections naturally model the one-to-many relationship between rooms and messages. This structure aligns with how chat data is organized.

  * **Scalability:** Firestore reads are efficient within a collection or subcollection. Storing messages within their respective room subcollections allows for efficient retrieval of a room's message history.

  * **Data Consistency:** Subcollections support atomic operations, making it easier to reliably add a message while updating the corresponding room.

**Incorrect Answers:**

  * **A. ...Each room will have a document listing the contents of its messages.**

    * **Reasoning:** Storing all messages in a single document limits scalability. Large message volumes could make reads inefficient and exceed Firestore's document size limits.

  * **B. ...Each room will have a collection containing a document for each message.**

    * **Reasoning:** While workable, using a top-level collection for each message isn't as efficient or scalable as the nested subcollection approach.

  * **D. ...Each room's document will contain references to the messages.**

    * **Reasoning:** This introduces extra read overhead. Every message fetch would require reading the room document and then separate reads for each message, impacting responsiveness, especially in busy rooms.

---

## Question 53

*Domain 4: Integrating Applications with Google Cloud Services*

**Your team is developing a Google Cloud application where user identities are managed by Cloud Identity. Each user of the application will have their own Pub/Sub topic for publishing messages and a corresponding Pub/Sub subscription for retrieving messages. You need to ensure that only authorized users can publish and subscribe to their respective Pub/Sub topic and subscription. What should you do?**

**

**

- [ ] B. Assign the pubsub.publisher and pubsub.subscriber roles to the user identity at the project level.
- [ ] D. Configure the application to operate as a service account with the pubsub.publisher and pubsub.subscriber roles.
- [x] A. Associate the user identity with the pubsub.publisher and pubsub.subscriber roles at the resource level.
- [ ] C. Create a custom role for the user identity containing the pubsub.topics.create and pubsub.subscriptions.create permissions.

### Explanation

**Correct Answer:**

  * **A. Associate the user identity with the pubsub.publisher and pubsub.subscriber roles at the resource level.**

**Justification:**

  * **Principle of Least Privilege:** Granting permissions at the resource (topic/subscription) level adheres to security best practices, minimizing the scope of access for each user identity.

  * **Cloud Identity Integration:** Pub/Sub supports IAM, allowing you to directly associate Cloud Identity users with the necessary roles on specific Pub/Sub resources. (Documentation: <https://cloud.google.com/pubsub/docs/access-control>)

**Incorrect Answers:**

  * **B. Assign the pubsub.publisher and pubsub.subscriber roles to the user identity at the project level.**

    * **Reasoning:** This is overly broad, granting these permissions to the user across _all_ Pub/Sub topics and subscriptions in the project, violating the principle of least privilege.

  * **C. Create a custom role for the user identity containing the pubsub.topics.create and pubsub.subscriptions.create permissions.**

    * **Reasoning:** While custom roles are valuable, this focuses on creation rights, not the core need for publish/subscribe permissions on user-specific resources.

  * **D. Configure the application to operate as a service account...**

    * **Reasoning:** Using a single service account for all users removes the granular identity management made possible with Cloud Identity and IAM integration.

---

## Question 54

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**To enhance user experience during traffic spikes on your Cloud Run-hosted website,**

**what action should you take?**

- [ ] IV. Ensure that timeout exceptions and errors prompt the Cloud Run instance to exit swiftly, facilitating the initiation of a replacement instance.
- [ ] III. Execute as much work as feasible in the background after the response has been delivered to the user.
- [ ] I. Retrieve application configuration and static data from the database on application startup.
- [x] II. Embed application configuration and static data into the application image during build time.

### Explanation

**The action that should be taken to enhance user experience during traffic spikes on a Cloud Run-hosted website is:**

**II. Embed application configuration and static data into the application image during build time.**

**Explanation:**

  * Embedding application configuration and static data into the application image during build time ensures that the application starts up quickly without needing to retrieve data from external sources like a database on each startup.

  * By including configuration and static data within the application image, the application instances on Cloud Run can scale up rapidly to handle increased traffic without being bottlenecked by database or external resource dependencies during startup.

  * This approach optimizes the startup time of new instances, allowing the service to efficiently handle traffic spikes and provide a better user experience.

The other options can be explained as follows:

I. Retrieve application configuration and static data from the database on application startup.

  * Retrieving application configuration and static data from the database on application startup can introduce delays, especially during traffic spikes when database resources might be overwhelmed. This approach can lead to slower response times and degrade user experience during peak loads.

III. Execute as much work as feasible in the background after the response has been delivered to the user.

  * While executing background tasks after the response has been delivered can help offload some processing from the request handling phase, it might not directly address the issue of enhancing user experience during traffic spikes. Additionally, this approach might not be suitable for all types of tasks and could introduce complexity into the application architecture.

IV. Ensure that timeout exceptions and errors prompt the Cloud Run instance to exit swiftly, facilitating the initiation of a replacement instance.

  * Swiftly exiting instances in response to timeout exceptions and errors can help with resource management but may not directly enhance user experience during traffic spikes. Additionally, rapidly replacing instances might not address the underlying issue of slow startup times caused by external dependencies like database retrieval.

**Reference:**  
<https://cloud.google.com/blog/topics/developers-practitioners/3-ways-optimize-cloud-run-response-times>

---

## Question 55

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**As you develop a corporate tool on Compute Engine for the finance department, requiring user authentication and verification that they belong to the finance department, which approach should you adopt considering that all company employees utilize G Suite?**

- [ ] III. Configure Cloud Armor Security Policies to restrict access exclusively to corporate IP address ranges. Validate the provided JSON Web Token within the application.
- [ ] IV. Set up Cloud Armor Security Policies to limit access solely to corporate IP address ranges. Issue client-side certificates to all finance team members and verify these certificates within the application.
- [x] I. Implement Cloud Identity-Aware Proxy on the HTTP(s) load balancer and limit access to a Google Group containing finance department users. Validate the provided JSON Web Token within the application.
- [ ] II. Implement Cloud Identity-Aware Proxy on the HTTP(s) load balancer and restrict access to a Google Group containing finance department users. Distribute client-side certificates to all members of the finance team and authenticate these certificates within the application.

### Explanation

**Correct Choice:**

  * **I. Implement Cloud Identity-Aware Proxy (IAP) on the HTTP(s) load balancer and limit access to a Google Group containing finance department users. Validate the provided JSON Web Token (JWT) within the application.**

**Explanation:**

  * **IAP Integration:** IAP leverages your existing G Suite user identities and groups, providing seamless, secure authentication and authorization directly at the load balancer level.

  * **Group Authorization:** Restricting access to the finance Google Group is a straightforward way to ensure only authorized users can access the tool.

  * **JWT Validation:** JWTs from IAP carry G Suite user information. Validating these tokens in your application lets you verify user identity and potentially extract any needed info from the JWT.

**Why Other Options Are Unsuitable:**

  * **II. ...Distribute client-side certificates to all members of the finance team and authenticate these certificates within the application.**

    * **Unnecessary Complexity:** Managing client-side certificates introduces significant overhead compared to IAP's G Suite integration, especially for internal tools.

  * **III. Configure Cloud Armor Security Policies to restrict access exclusively to corporate IP address ranges...**

    * **Insufficient Security:** IP-based restrictions are easily spoofed and don't guarantee user identity. This approach is inherently less secure than user-based authentication.

  * **IV. ...Issue client-side certificates to all finance team members and verify these certificates within the application.**

    * **Combines Inadequacies:** Same issues with unnecessary certificate management (as option II) and insufficient security of IP filtering alone (as option III).

**References:**  
[https://cloud.google.com/endpoints/docs/openapi/authenticating-users-google-id](https://cloud.google.com/endpoints/docs/openapi/authenticating-users-google-id  https://cloud.google.com/iap/docs/signed-headers-howto#securing_iap_headers)

[https://cloud.google.com/iap/docs/signed-headers-howto#securing_iap_headers](https://cloud.google.com/endpoints/docs/openapi/authenticating-users-google-id  https://cloud.google.com/iap/docs/signed-headers-howto#securing_iap_headers)

---

## Question 56

*Domain 2: Building and Testing Applications*

**You're deploying a Python application to Cloud Run via Cloud Source Repositories and Cloud Build. Below is the Cloud Build pipeline:**

**```**

**steps:**

**\- name: python**

**entrypoint: ["install", "-r", "requirements.txt", "user"]**

**pip**

**args:**

**\- name: 'gcr.io/cloud-builders/docker'**

**args: ['build', '-t', 'us-central1-docker.pkg.dev/$(PROJECT_ID)/${_REPO_NAME)/myimage:$(SHORT_SHA)',**

**\- name: 'gcr.io/cloud-builders/docker'**

**args: ['push', 'us-central1-docker.pkg.dev/$(PROJECT_ID)/$(_REPO_NAME)/myimage:$(SHORT_SHA)']**

**\- name: google/cloud-sdk**

**args: ['gcloud', 'run', 'deploy', 'helloworld-$(SHORT_SHA)',**

**'--image=us-central1-docker.pkg.dev/$(PROJECT_ID)/$(_REPO_NAME)/myimage:$(SHORT_SHA)',**

**'--region=us-central1', 'platform', 'managed',**

**'--allow-unauthenticated']**

**```**

**You aim to optimize deployment times and eliminate unnecessary steps. What should you do?**

- [x] D. Introduce the --cache-from argument to the Docker build step in your build configuration file.
- [ ] C. Store image artifacts in a Cloud Storage bucket located in the same region as the Cloud Run instance.
- [ ] A. Eliminate the step responsible for pushing the container to Artifact Registry.
- [ ] B. Set up a new Docker registry within a VPC and utilize Cloud Build worker pools within the VPC to execute the build pipeline.

### Explanation

**Correct Answer:**

  * **D. Introduce the --cache-from argument to the Docker build step in your build configuration file.**

**Justification:**

  * **Build Caching:** The `--cache-from` argument in Docker builds allows reusing image layers from previous builds if they haven't changed. This significantly speeds up builds, especially when dependencies (like in `requirements.txt`) are relatively stable.

  * **Direct Impact:** This change addresses the core question of optimizing deployment times.

**Example Modification:**

1.  steps:
      2.   ... 
      3.   - name: 'gcr.io/cloud-builders/docker'
      4.     args: 
      5.       ['build', 
      6.        '--cache-from=us-central1-docker.pkg.dev/$(PROJECT_ID)/${_REPO_NAME)/myimage:latest', # Example - adapt as needed
      7.        '-t', 'us-central1-docker.pkg.dev/$(PROJECT_ID)/${_REPO_NAME)/myimage:$(SHORT_SHA)', 
      8.        '.'] 
      9.   ...

**Incorrect Answers:**

  * **A. Eliminate the step responsible for pushing the container to Artifact Registry.**

    * **Reasoning:** This breaks the deployment. Cloud Run needs the image in a registry it can access.

  * **B. Set up a new Docker registry within a VPC ...**

    * **Reasoning:** While potentially useful for other reasons (security, locality), this adds complexity and management overhead without directly addressing the core goal of faster builds.

  * **C. Store image artifacts in a Cloud Storage bucket ...**

    * **Reasoning:** Cloud Storage isn't a container registry. While a complex workaround _might_ be possible, it deviates significantly from standard container deployment practice.

---

## Question 57

*Domain 3: Configuring and Deploying Applications*

**Your application is deployed within a Google Kubernetes Engine (GKE) cluster. Whenever a new version of your application is released, your CI/CD tool updates the `spec.template.spec.containers[0].image` value to point to the Docker image of the new application version. Upon applying the change, you aim to deploy a minimum of 1 replica of the new version while ensuring that the previous replicas are retained until the new replica is deemed healthy.**

**Which modification should you apply to the GKE Deployment object shown below?**

**apiVersion: apps/v1**

**kind: Deployment**

**metadata:**

**name: ecommerce-frontend-deployment**

**spec:**

**replicas: 3**

**selector:**

**matchLabels:**

**app: ecommerce-frontend**

**template:**

**metadata:**

**labels:**

**app: ecommerce-frontend**

**spec:**

**containers:**

**\- name: ecommerce-frontend-webapp**

**image: ecommerce-frontend-webapp:1.7.9**

**ports:**

**\- containerPort: 80**

- [ ] A. Configure the Deployment strategy as RollingUpdate with `maxSurge` set to 0 and `maxUnavailable` set to 1.
- [ ] C. Configure the Deployment strategy as Recreate with `maxSurge` set to 0 and `maxUnavailable` set to 1.
- [ ] D. Configure the Deployment strategy as Recreate with `maxSurge` set to 1 and `maxUnavailable` set to 0.
- [x] B. Configure the Deployment strategy as RollingUpdate with `maxSurge` set to 1 and `maxUnavailable` set to 0.

### Explanation

**Correct Answer:**

  * **B. Configure the Deployment strategy as RollingUpdate with**`**maxSurge**`**set to 1 and**`**maxUnavailable**`**set to 0.**

**Justification:**

  * **RollingUpdate:** This strategy gracefully replaces existing pods with new ones, ensuring service availability throughout the update. (Kubernetes Documentation: <https://kubernetes.io/docs/concepts/workloads/controllers/deployment/>)

  * **maxSurge: 1** This allows the creation of one additional pod beyond the desired replica count (`replicas: 3`). This ensures the new replica starts and becomes healthy before proceeding.

  * **maxUnavailable: 0** Ensures at least 3 pods (the original `replicas` count) remain available, maintaining service uptime.

**Incorrect Answers**

  * **A. ...maxSurge**`**set to 0 and**`**maxUnavailable` set to 1.**

    * **Reasoning:** This setup would prevent a new pod from being created until an old one is terminated, hindering the requirement for a temporary overlap of a new and old versions.

  * **C. Configure the Deployment strategy as Recreate...**

    * **Reasoning:** The Recreate strategy terminates all existing pods before starting new ones. This would introduce downtime which conflicts with the goal of maintaining service availability.

  * **D. Configure the Deployment strategy as Recreate...**

    * **Reasoning:** Same as C – the Recreate strategy would lead to service unavailability.

---

## Question 58

*Domain 3: Configuring and Deploying Applications*

**As the lead developer responsible for a financial risk calculation API hosted on Cloud Run with a gRPC interface, you continuously work on enhancing the risk analysis features. You want to make these optimizations available first to a select group of customers who signed up to test the improvements before releasing them more broadly. Your CI/CD pipeline has created a new version of the API as a container image, which is now stored in the Artifact Registry.**

**Which rollout strategy should you use to manage this controlled release?**

- [ ] A. Use Cloud Run’s traffic splitting to direct a specific percentage of traffic from registered test users to the updated service.
- [x] C. Control access to the new service using a feature flag for customers registered to test the updates.
- [ ] B. Implement a blue/green deployment to transition traffic to the new version of the service.
- [ ] D. Migrate traffic to the updated service and activate session affinity for Cloud Run.

### Explanation

The correct answer is 

**C. Control access to the new service using a feature flag for customers registered to test the updates.**

Explanation:

Using a **feature flag** is the most effective strategy for selectively enabling new optimizations for a specific group of customers who have opted to test them. Feature flags allow you to control access to the updated features based on specific user criteria, such as registration for testing. This approach enables you to:

  * **Precisely target** only the selected group of customers without affecting others.

  * **Gradually roll out and monitor** the new features for feedback before a full release.

Feature flags offer flexibility and reduce the risk of potential issues affecting all users by isolating changes to only a controlled group.

Justifications for Incorrect Options:

  * **Option A: Traffic splitting based on a percentage**  
Traffic splitting in Cloud Run distributes traffic based on percentage rather than user-specific criteria, making it unsuitable for selectively targeting specific registered customers.

  * **Option B: Blue/green deployment**  
Blue/green deployments are designed for swapping all traffic between two service versions and do not allow selective feature access for a specific user group. This approach is better suited for general rollouts or quick rollbacks, not for limited testing.

  * **Option D: Session affinity for Cloud Run**  
Session affinity ensures that a user’s requests are directed to the same instance, but it does not allow you to control which users see the new features. Session affinity is not relevant for user-specific feature testing.

---

## Question 59

*Domain 3: Configuring and Deploying Applications*

**In the process of replatforming legacy applications onto Google Kubernetes Engine, your organization aims to decompose a monolithic application into microservices without rewriting the application code. There are multiple instances with read and write access to a configuration file stored on a shared file system. How can you minimize the effort required to manage this transition?**

- [ ] IV. Implement a new ConfigMap and volumeMount to store the contents of the configuration file.
- [ ] I. Utilize a new Cloud Storage bucket and mount it within the container using FUSE.
- [ ] II. Establish a new persistent disk and mount the volume as a shared PersistentVolume.
- [x] III. Deploy a new Filestore instance and mount the volume as an NFS PersistentVolume.

### Explanation

**III. Deploy a new Filestore instance and mount the volume as an NFS PersistentVolume.**

Here's why:

  * **Supports Shared Access:** Filestore provides a network file system (NFS) solution that natively supports multiple instances reading and writing to the same shared storage. This aligns well with the legacy application's requirements.

  * **Manageability:** Filestore is a fully managed service, significantly reducing the administrative overhead compared to manually managing a persistent disk or self-hosting an NFS solution.

**Why other options are less suitable:**

  * **I. Utilize a new Cloud Storage bucket and mount it within the container using FUSE.** Cloud Storage is object storage, not a file system. While FUSE could be used, it adds complexity and might introduce performance or consistency issues.

  * **II. Establish a new persistent disk and mount the volume as a shared PersistentVolume.** Most persistent disk types in Kubernetes don't support simultaneous mounting from multiple pods, making this unsuitable for the shared file system requirement.

  * **IV. Implement a new ConfigMap and volumeMount to store the contents of the configuration file.** ConfigMaps are designed for storing configuration data, not large shared files, and they might have size limitations.

**References:**

[https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes https://cloud.google.com/filestore/docs/accessing-fileshares](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes   https://cloud.google.com/filestore/docs/accessing-fileshares  https://cloud.google.com/storage/docs/gcs-fuse)

[https://cloud.google.com/storage/docs/gcs-fuse](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes   https://cloud.google.com/filestore/docs/accessing-fileshares  https://cloud.google.com/storage/docs/gcs-fuse)

---

## Question 60

*Domain 4: Integrating Applications with Google Cloud Services*

**Your organization relies on Cloud Logging to manage large volumes of log data. You are tasked with designing a real-time log analysis architecture to push logs to a third-party application for processing. What is the recommended approach?**

- [ ] IV. Develop a Cloud Function to extract Cloud Logging log entries and transmit them to the third-party application.
- [x] I. Set up a Cloud Logging log export to Pub/Sub.
- [ ] II. Configure a Cloud Logging log export to BigQuery.
- [ ] III. Implement a Cloud Logging log export to Cloud Storage.

### Explanation

**I. Set up a Cloud Logging log export to Pub/Sub.**

  * **Pros:**

    * **Real-time streaming:** Pub/Sub is designed for ingesting and delivering events in real-time.

    * **Scalability:** Pub/Sub can handle large volumes of log data without bottlenecks.

    * **Integration:** Many third-party applications have built-in connectors to Pub/Sub for easy consumption.

  * **Cons:**

    * **Might require some setup on the third-party side** to subscribe to the Pub/Sub topic and process the messages.

**Why other options aren't as suitable:**

  * **II. Configure a Cloud Logging log export to BigQuery.** BigQuery is primarily for batch analytics, not ideal for immediate, real-time processing.

  * **III. Implement a Cloud Logging log export to Cloud Storage.** Cloud Storage is an object store. While logs can be exported there, you'd still need an additional mechanism to pull and process them in real-time.

  * **IV. Develop a Cloud Function to extract Cloud Logging log entries and transmit them to the third-party application.** This option adds development overhead and potential points of failure compared to the more streamlined Pub/Sub approach.

**Reference:**  
[https://cloud.google.com/logging/docs/export/configure_export_v2#overview https://cloud.google.com/logging/docs/export/pubsub](https://cloud.google.com/logging/docs/export/configure_export_v2#overview   https://cloud.google.com/logging/docs/export/pubsub)

---
