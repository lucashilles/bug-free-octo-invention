# Professional Cloud Developer — Practice Exam 4

59 questions.

## Question 1

*Domain 4: Integrating Applications with Google Cloud Services*

**You’re developing an integration for an ecommerce website to manage all steps in order fulfillment. You’ve created several Cloud Functions for each step in the order process and need to orchestrate their execution so that each function’s output guides the workflow. To minimize latency, what should you do?**

- [ ] C. Use Cloud Composer to call the functions and apply an Apache Airflow HTTP operator to manage execution logic.
- [x] B. Use Workflows to call the functions and apply conditional jumps to manage execution logic.
- [ ] A. Use Workflows to call the functions and implement callbacks to manage execution logic.
- [ ] D. Use Cloud Composer to call the functions and apply an Apache Airflow operator to manage execution logic.

### Explanation

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

---

## Question 2

*Domain 4: Integrating Applications with Google Cloud Services*

**You manage a popular mobile game deployed on Google Cloud using Firebase, Firestore, and Cloud Functions. Recently, the game experienced a spike in usage, resulting in HTTP 429 RESOURCE_EXHAUSTED errors when accessing the Firestore API. With an upcoming marketing campaign, another usage surge is expected. To prevent this issue from recurring, what should you do?**

- [x] D. Optimize database queries to reduce read/write operations and update the code to retry Firestore API calls using exponential backoff.
- [ ] A. Request a quota increase and update the code to retry Firestore API calls using fixed backoff.
- [ ] B. Request a quota increase and update the code to retry Firestore API calls using exponential backoff.
- [ ] C. Optimize database queries to reduce read/write operations and update the code to retry Firestore API calls using fixed backoff.

### Explanation

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

---

## Question 3

*Domain 2: Building and Testing Applications*

**You've developed an application intended for Cloud Run, where log records are currently being stored as text in local files. To optimize maintenance and ensure logs are directed to Cloud Logging, what approach is recommended?**

- [ ] I. Integrate the Cloud Logging library into your codebase and utilize it for logging purposes.
- [x] II. Direct logs to Standard Output (stdout) and Standard Error (stderr) streams using your programming language's logger.
- [ ] IV. Set up a cron job to transfer the log files to Cloud Storage once per day for archival purposes.
- [ ] III. Make the log files accessible via a public URL like www.mycompany.com/logs, manually download them, and then upload to Cloud Storage.

### Explanation

Correct answer

**II. Use your programming language logger to write logs to Standard output (stdout) and Standard error (stderr) streams.**

Justifications:

I. This is incorrect. While it's technically possible to use the library, that would result in a lot of code to maintain.  
II. This is correct. Cloud Run has direct integration to Cloud Logging via stdout and stderr.  
III. This is incorrect. This task would have to be performed manually. Also this approach isn’t the most secure.  
IV. This is incorrect. While data can be copied to Cloud Storage buckets, this doesn't help us with our goal of storing log data within Cloud Logging.

**References:**

[https://cloud.google.com/run/docs/logging#container-logs](%0d https:/cloud.google.com/run/docs/logging#container-logs)

[https://cloud.google.com/logging/docs/reference/libraries](%0d https:/cloud.google.com/logging/docs/reference/libraries%0d)

---

## Question 4

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**When migrating an on-premises container from Knative to Google Cloud without changing the application's deployment strategy and preferring a fully managed service, which Google Cloud service is the most suitable option for deploying your container?**

- [ ] IV. App Engine flexible environment
- [x] I. Cloud Run
- [ ] II. Compute Engine
- [ ] III. Google Kubernetes Engine

### Explanation

Here's why **Cloud Run** (option I) is the most suitable choice in this scenario:

  * **Fully Managed:** Cloud Run eliminates the need to manage infrastructure, allowing you to focus on your application.

  * **Knative Compatibility:** Cloud Run is built upon Knative, ensuring a smooth migration experience without changes to your deployment strategy.

  * **Stateless Containers:** Cloud Run is optimized for stateless containerized applications, making it a good fit for many existing Knative use cases.

  * **Scaling:** Cloud Run automatically scales your service up or down based on traffic, including the ability to scale down to zero when not in use (ideal for cost optimization).

**Why the other options are less suitable:**

  * **Compute Engine (II):** Compute Engine provides VMs, so you would still need to manage the underlying infrastructure, including Kubernetes setup and maintenance.

  * **Google Kubernetes Engine (III):** While GKE is a powerful option, it involves managing a Kubernetes cluster. If your goal is a fully managed experience, Cloud Run is a better fit.

  * **App Engine flexible environment (IV):** App Engine flexible environment is designed for more traditional application architectures and can involve more significant changes to your application for migration.

**References:**

[https://cloud.google.com/serverless-options/](https://cloud.google.com/serverless-options/  https://cloud.google.com/appengine/docs/the-appengine-environments  https://cloud.google.com/knative/  https://cloud.google.com/blog/products/containers-kubernetes/when-to-use-google-kubernetes-engine-vs-cloud-run-for-containers)

[https://cloud.google.com/appengine/docs/the-appengine-environments](https://cloud.google.com/serverless-options/  https://cloud.google.com/appengine/docs/the-appengine-environments  https://cloud.google.com/knative/  https://cloud.google.com/blog/products/containers-kubernetes/when-to-use-google-kubernetes-engine-vs-cloud-run-for-containers)

[https://cloud.google.com/knative/](https://cloud.google.com/serverless-options/  https://cloud.google.com/appengine/docs/the-appengine-environments  https://cloud.google.com/knative/  https://cloud.google.com/blog/products/containers-kubernetes/when-to-use-google-kubernetes-engine-vs-cloud-run-for-containers)

[https://cloud.google.com/blog/products/containers-kubernetes/when-to-use-google-kubernetes-engine-vs-cloud-run-for-containers](https://cloud.google.com/serverless-options/  https://cloud.google.com/appengine/docs/the-appengine-environments  https://cloud.google.com/knative/  https://cloud.google.com/blog/products/containers-kubernetes/when-to-use-google-kubernetes-engine-vs-cloud-run-for-containers)

---

## Question 5

*Domain 3: Configuring and Deploying Applications*

**How can you test conversion rates between three different website designs without altering the application code deployed on Compute Engine?**

- [ ] III. Deploy the website on Cloud Functions as three separate functions.
- [x] I. Deploy the website on Cloud Run and utilize traffic splitting to test different designs.
- [ ] II. Deploy the website on Cloud Run as three separate revisions to test different designs.
- [ ] IV. Deploy the website on Cloud Functions and implement custom code to display different designs.

### Explanation

To test conversion rates between three different website designs without altering the application code deployed on Compute Engine, the most appropriate approach is:

**I. Deploy the website on Cloud Run and utilize traffic splitting to test different designs.**

Explanation:

Option I involves deploying the website on Cloud Run and utilizing traffic splitting to direct users to different versions of the website with different designs. Cloud Run allows for easy deployment of containerized applications, and traffic splitting enables directing a portion of the traffic to different revisions of the same service. This approach allows for testing different designs in a real-world scenario without modifying the application code.

Option II suggests deploying the website on Cloud Run as three separate revisions to test different designs. While this approach is feasible, it may require more manual management and monitoring of the different revisions compared to traffic splitting.

Option III proposes deploying the website on Cloud Functions as three separate functions. However, Cloud Functions are designed for event-driven serverless execution, and deploying a website as separate functions may not be the most suitable approach for testing different designs.

Option IV suggests deploying the website on Cloud Functions and implementing custom code to display different designs. While technically possible, this approach would require significant custom development and may introduce complexity and maintenance overhead.

Therefore, option I is the most appropriate approach for testing conversion rates between three different website designs without altering the application code deployed on Compute Engine.

**Documentation:**

  * Traffic splitting in Cloud Run: <https://cloud.google.com/run/docs/rollouts-deployments#traffic_splitting>

---

## Question 6

*Domain 2: Building and Testing Applications*

**What action should you take to ensure that the Cloud Function is deleted even if the test fails during the automated testing process?**

- [ ] I. Change the order of the steps to delete the Cloud Function before performing the test.
- [ ] IV. Have the Cloud Build test step set its outcome in an environment variable called result and return 0. Add a final step after the Cloud Function deletion that checks whether the environment variable contains the expected results.
- [ ] II. Include a waitFor option in the Cloud Build step that deletes the Cloud Function test step as a required preceding step.
- [x] III. Have the Cloud Build step write the Cloud Function results to a file and return 0. Add a step after the Cloud Function deletion that checks whether the file contains the expected results and fails if it doesn't.

### Explanation

The most suitable action to ensure that the Cloud Function is deleted even if the test fails during the automated testing process is:

**III. Have the Cloud Build step write the Cloud Function results to a file and return 0. Add a step after the Cloud Function deletion that checks whether the file contains the expected results and fails if it doesn't.**

Explanation:

Option I suggests changing the order of the steps to delete the Cloud Function before performing the test. While this might ensure that the Cloud Function is deleted regardless of the test outcome, it doesn't address the issue of handling a failed test effectively.

Option II proposes including a waitFor option in the Cloud Build step that deletes the Cloud Function test step as a required preceding step. This approach might ensure that the Cloud Function is deleted only if the test step succeeds, but it doesn't provide a mechanism to handle a failed test and still delete the Cloud Function.

Option IV suggests having the Cloud Build test step set its outcome in an environment variable and adding a final step to check whether the variable contains the expected results. While this approach allows for capturing the test outcome, it doesn't ensure that the Cloud Function is deleted if the test fails.

Option III is the recommended approach because it involves writing the Cloud Function results to a file during the Cloud Build step and then adding a subsequent step to check whether the file contains the expected results. If the test fails, the subsequent step can still execute and verify whether the Cloud Function was deleted as expected, ensuring cleanup regardless of the test outcome.

Therefore, option III is the most suitable action to ensure that the Cloud Function is deleted even if the test fails during the automated testing process.

**Documentation** :

  * Cloud Build: <https://cloud.google.com/build/docs/automating-builds/create-manage-triggers>

---

## Question 7

*Domain 4: Integrating Applications with Google Cloud Services*

**As the overseer of a microservice-driven ecommerce platform on Google Cloud encountering HTTP 500 errors when triggering a Cloud Function responsible for sending confirmation emails, what adjustment should be made to minimize email loss?**

- [ ] I. Extend the Cloud Function's timeout to nine minutes.
- [ ] III. Modify the sender application to store emails in Memorystore and trigger the Cloud Function. Upon invocation, the function retrieves email details from Memorystore and dispatches them to the email service.
- [x] II. Revise the sender application to dispatch outgoing emails as messages to a Pub/Sub topic. Update the Cloud Function configuration to consume the Pub/Sub queue.
- [ ] IV. Configure the sender application to implement Cloud Function execution retries every one second in case of request failures.

### Explanation

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

---

## Question 8

*Domain 2: Building and Testing Applications*

**You are developing an application with a microservices architecture that includes Cloud Run, Bigtable, and Pub/Sub. To create a minimally viable product, you want to complete the testing and debugging process quickly and at minimal cost. What is the best approach?**

- [ ] D. Use Cloud Code for developing, deploying, and testing microservices, and review logs with Cloud Logging.
- [ ] C. Use Cloud Build to set up a pipeline, adding stages for unit testing and manual approval, then deploy the code to your Google Cloud project.
- [x] B. Use emulators to locally test cloud resources, then deploy the code to your Google Cloud project.
- [ ] A. Use Cloud Shell Editor and Cloud Shell for deployment, and test the application using the Google Cloud Console in the project.

### Explanation

The correct answer is

**B. Use emulators to locally test cloud resources, then deploy the code to your Google Cloud project.**

Explanation:

Using **emulators** is the best approach for quick and cost-effective testing of cloud services in a development environment. Google Cloud provides emulators for services like **Bigtable** and **Pub/Sub** that allow you to simulate the behavior of these resources on your local machine without incurring cloud costs. By testing your application locally with emulators, you can debug and validate its functionality before deploying to Google Cloud, saving both time and expenses in the early stages of development.

Justifications for Incorrect Options:

  * **Option A: Use Cloud Shell Editor and Cloud Shell for deployment, and test the application using the Google Cloud Console in the project**  
While Cloud Shell provides a development environment, testing entirely in the cloud could incur higher costs due to resource usage. This option is less suitable for minimizing costs during the MVP phase compared to using local emulators.

  * **Option C: Use Cloud Build to set up a pipeline, adding stages for unit testing and manual approval, then deploy the code to your Google Cloud project**  
While CI/CD pipelines are valuable, setting up a full Cloud Build pipeline for an MVP may be unnecessary overhead. Emulators offer a simpler and more cost-effective solution for early-stage testing.

  * **Option D: Use Cloud Code for developing, deploying, and testing microservices, and review logs with Cloud Logging**  
Cloud Code is helpful for microservices development but involves deploying to Google Cloud for testing, which can incur additional costs. Emulators provide a more cost-efficient local testing option.

**Relevant Documentation:**

For more information on using emulators in Google Cloud, refer to:

  * [Google Cloud Bigtable Emulator](https://cloud.google.com/bigtable/docs/emulator)

  * [Google Cloud Pub/Sub Emulator](https://cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/EMULATOR)

---

## Question 9

*Domain 2: Building and Testing Applications*

**Your company recently deployed a new API to the App Engine Standard environment. However, during testing, the API isn't functioning as anticipated. You aim to continuously monitor the application to diagnose potential issues within the application code without necessitating redeployment. Which tool is most suitable for this purpose?**

- [x] IV. Implement Stackdriver Debug Logpoints to dynamically insert log statements into the running application code for real-time debugging.
- [ ] III. Make use of Stackdriver Debug Snapshots to capture and analyze application state and variables at specific points in time.
- [ ] II. Employ Stackdriver Monitoring to track and monitor the health and performance metrics of the deployed API.
- [ ] I. Utilize Stackdriver Trace to trace and analyze request latency and performance across the application.

### Explanation

**Correct Option:**

  * **IV. Implement Stackdriver Debug Logpoints to dynamically insert log statements into the running application code for real-time debugging.**

**Reasoning:**

  * **Dynamic Logging:** Stackdriver Debug Logpoints provide the most appropriate approach in this scenario because they allow you to add detailed log statements directly into your running code without the need for code changes or redeployment. This enables you to gather real-time insights into the application's behavior and pinpoint the root cause of the unexpected issues.

**Incorrect Options and Why:**

  * **I. Utilize Stackdriver Trace to trace and analyze request latency and performance across the application.**

    * While Stackdriver Trace is valuable, it focuses on tracing requests and uncovering latency bottlenecks within a distributed system. It's less suited for diagnosing issues within the code itself without changes.

  * **II. Employ Stackdriver Monitoring to track and monitor the health and performance metrics of the deployed API.**

    * Stackdriver Monitoring provides insights into the API's overall health and resource usage. It's helpful for general health checks but doesn't offer the granular code-level debugging needed in this case.

  * **III. Make use of Stackdriver Debug Snapshots to capture and analyze application state and variables at specific points in time.**

    * Although Stackdriver Debug Snapshots are useful for debugging, they provide a static view of the application's state at a given moment. Logpoints offer a more dynamic and real-time perspective, which is better suited to finding issues in a continuously running application.

**Supporting Documentation:**

  * **Stackdriver Debugger (Logpoints):** <https://cloud.google.com/blog/products/gcp/add-log-statements-to-your-application-on-the-fly-with-stackdriver-debugger-logpoints/>

  * **Stackdriver Trace:** <https://cloud.google.com/trace>

  * **Stackdriver Monitoring:** <https://cloud.google.com/monitoring>

---

## Question 10

*Domain 3: Configuring and Deploying Applications*

**In your production environment, your application runs on Compute Engine virtual machine instances managed by a managed instance group and accessed through an HTTP(s) load balancer. Users are reporting inability to access the application. How can you set up monitoring to receive alerts when the application becomes unavailable?**

- [ ] IV. Enable managed instance group health checks to monitor the health of your instances.
- [ ] I. Implement smoke tests to detect application unavailability.
- [x] II. Set up Stackdriver uptime checks to monitor the availability of your application.
- [ ] III. Configure Cloud Load Balancing health checks to monitor the health of your instances.

### Explanation

**Option II, "Set up Stackdriver uptime checks to monitor the availability of your application," is the most suitable choice for setting up monitoring to receive alerts when the application becomes unavailable.**

Justification:

  * Stackdriver uptime checks provide a straightforward method to monitor the availability of your application by periodically pinging its endpoints. This directly addresses the need to monitor application unavailability.

  * Stackdriver integrates seamlessly with Google Cloud Platform's monitoring and alerting capabilities, allowing you to configure alerts based on the results of uptime checks.

  * By setting up Stackdriver uptime checks, you can quickly detect when your application becomes unavailable and receive timely alerts to take necessary actions.

  * This option focuses specifically on monitoring application availability, which is crucial for ensuring a good user experience.

While the other options (I, III, and IV) also contribute to monitoring and maintaining the health of your infrastructure and application, they do not directly address the requirement of setting up monitoring to receive alerts when the application becomes unavailable.

For further details, you can refer to the documentation on [Monitoring uptime](https://cloud.google.com/monitoring/uptime-checks).

---

## Question 11

*Domain 4: Integrating Applications with Google Cloud Services*

**You are building an application component to capture and stream user behavior data into BigQuery using the BigQuery Storage Write API. To prevent duplicate data in BigQuery, you need a straightforward solution. What should you do?**

- [ ] A. Use the default type to create a write stream.
- [x] B. Use the committed type to create a write stream.
- [ ] D. Set up a Pub/Sub topic and use Cloud Functions to subscribe and remove duplicates.
- [ ] C. Set up a Kafka cluster and use a unique identifier (UUID) to filter out duplicate messages.

### Explanation

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

---

## Question 12

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**To create a Cloud Function in Project A that stores its output in a Cloud Storage bucket in Project B, while following the principle of least privilege, what is the recommended approach?**

- [x] II. Create a Google service account in Project A. Assign this service account the roles/storage.objectCreator role on the storage bucket in Project B. Deploy the Cloud Function using the service account from Project A.
- [ ] III. Determine the default App Engine service account (PROJECT_ID@appspot.gserviceaccount.com) in Project A. Assign the default App Engine service account the roles/storage.objectCreator role on the storage bucket in Project B. Deploy the Cloud Function using the default App Engine service account in Project A.
- [ ] I. Create a Google service account in Project B. Assign this service account the roles/storage.objectCreator role on the storage bucket in Project B. Deploy the Cloud Function in Project A using the service account from Project B.
- [ ] IV. Determine the default App Engine service account (PROJECT_ID@appspot.gserviceaccount.com) in Project B. Assign the default App Engine service account the roles/storage.objectCreator role on the storage bucket in Project B. Deploy the Cloud Function using the default App Engine service account in Project A.

### Explanation

The recommended approach for creating a Cloud Function in Project A that stores its output in a Cloud Storage bucket in Project B, while following the principle of least privilege, is:

**II. Create a Google service account in Project A. Assign this service account the roles/storage.objectCreator role on the storage bucket in Project B. Deploy the Cloud Function using the service account from Project A.**

Here's why this approach is recommended:

  1. **Service Account Isolation** : It's generally a good practice to use a service account from the same project where the Cloud Function is deployed. This helps in maintaining clear ownership and isolation of permissions.

  2. **Least Privilege** : By creating a specific service account in Project A and assigning it only the necessary role (`roles/storage.objectCreator`) on the storage bucket in Project B, you adhere to the principle of least privilege. This ensures that the service account has only the permissions required to perform its intended function and nothing more.

  3. **Access Control** : Assigning the `roles/storage.objectCreator` role specifically grants the Cloud Function permission to create objects in the Cloud Storage bucket in Project B, without providing unnecessary access to other resources or operations.

Options I, III, and IV are not recommended for the following reasons:

I. Deploying the Cloud Function in Project A using a service account from Project B introduces unnecessary complexity and potential security risks. It's not a recommended practice to use service accounts from different projects unless there's a specific requirement for cross-project access, which doesn't seem to be the case here.

III. and IV. Utilizing the default App Engine service account in either Project A or Project B is not ideal because it's a shared service account that may have broader permissions than necessary. Assigning it the `roles/storage.objectCreator` role on the storage bucket in Project B grants unnecessary permissions to all services running in Project A or Project B, which goes against the principle of least privilege.

Therefore, option II is the recommended approach for creating a Cloud Function in Project A that stores its output in a Cloud Storage bucket in Project B while following the principle of least privilege.

**References:**

[https://cloud.google.com/functions/docs/securing/function-identity#per-function_identity](https://cloud.google.com/functions/docs/securing/function-identity#per-function_identity  https://cloud.google.com/storage/docs/access-control/iam-roles  https://cloud.google.com/iam/docs/using-iam-securely#least_privilege  https://cloud.google.com/iam/docs/understanding-service-accounts#granting_minimum_permissions_to_service_accounts  https://cloud.google.com/functions/docs/securing/function-identity#runtime_service_account)

[https://cloud.google.com/storage/docs/access-control/iam-roles](https://cloud.google.com/functions/docs/securing/function-identity#per-function_identity  https://cloud.google.com/storage/docs/access-control/iam-roles  https://cloud.google.com/iam/docs/using-iam-securely#least_privilege  https://cloud.google.com/iam/docs/understanding-service-accounts#granting_minimum_permissions_to_service_accounts  https://cloud.google.com/functions/docs/securing/function-identity#runtime_service_account)

[https://cloud.google.com/iam/docs/using-iam-securely#least_privilege](https://cloud.google.com/functions/docs/securing/function-identity#per-function_identity  https://cloud.google.com/storage/docs/access-control/iam-roles  https://cloud.google.com/iam/docs/using-iam-securely#least_privilege  https://cloud.google.com/iam/docs/understanding-service-accounts#granting_minimum_permissions_to_service_accounts  https://cloud.google.com/functions/docs/securing/function-identity#runtime_service_account)

[https://cloud.google.com/iam/docs/understanding-service-accounts#granting_minimum_permissions_to_service_accounts](https://cloud.google.com/functions/docs/securing/function-identity#per-function_identity  https://cloud.google.com/storage/docs/access-control/iam-roles  https://cloud.google.com/iam/docs/using-iam-securely#least_privilege  https://cloud.google.com/iam/docs/understanding-service-accounts#granting_minimum_permissions_to_service_accounts  https://cloud.google.com/functions/docs/securing/function-identity#runtime_service_account)

[https://cloud.google.com/functions/docs/securing/function-identity#runtime_service_account](https://cloud.google.com/functions/docs/securing/function-identity#per-function_identity  https://cloud.google.com/storage/docs/access-control/iam-roles  https://cloud.google.com/iam/docs/using-iam-securely#least_privilege  https://cloud.google.com/iam/docs/understanding-service-accounts#granting_minimum_permissions_to_service_accounts  https://cloud.google.com/functions/docs/securing/function-identity#runtime_service_account)

---

## Question 13

*Domain 4: Integrating Applications with Google Cloud Services*

**To facilitate updating the current stock price in an in-memory database for an application monitoring stock prices, how should you configure the Pub/Sub subscription, given each message includes the stock symbol, price, and timestamp?**

- [ ] IV. Establish a push subscription with both ordering and exactly-once delivery disabled.
- [x] III. Configure a pull subscription with ordering enabled, utilizing the stock symbol as the ordering key.
- [ ] I. Set up a push subscription with exactly-once delivery enabled.
- [ ] II. Create a pull subscription with both ordering and exactly-once delivery disabled.

### Explanation

**III. Configure a pull subscription with ordering enabled, utilizing the stock symbol as the ordering key.**

**Explanation:**

  * **Pull Subscriptions:** Provide better control over message consumption, beneficial when updating an in-memory database.

  * **Ordering:** Ensures stock price updates for the same symbol are processed sequentially, maintaining accuracy in your in-memory database.

  * **Stock Symbol as Ordering Key:** Guarantees that updates for a specific stock are applied in the correct order, preventing outdated values from overwriting newer ones.

**Why Other Options Are Less Suitable:**

  * **I. Set up a push subscription with exactly-once delivery enabled.** While push subscriptions can be useful, they relinquish control over message processing order, which might lead to inconsistencies in your in-memory database.

  * **II. Create a pull subscription with both ordering and exactly-once delivery disabled.** No ordering means you could update your in-memory database with older stock prices over newer ones.

  * **IV. Establish a push subscription with both ordering and exactly-once delivery disabled.** Combines the drawbacks of push subscriptions (lack of ordering control) with the potential for duplicate messages.

---

## Question 14

*Domain 4: Integrating Applications with Google Cloud Services*

**As a manager of a system utilizing stateless Compute Engine VMs and Cloud Run instances connected to a VPC with internal ingress settings, you encounter a 403 Permission Denied error when attempting to schedule tasks on Cloud Run. How should you resolve this issue?**

- [ ] II. Set up a cron job on the Compute Engine VMs to trigger Cloud Run based on the schedule.
- [ ] I. Assign the roles/run.developer IAM role to the service account.
- [x] IV. Utilize Cloud Scheduler in conjunction with Pub/Sub to invoke Cloud Run.
- [ ] III. Modify the Cloud Run ingress setting to 'Internal and Cloud Load Balancing.'

### Explanation

**The most likely solution is:**

**IV. Utilize Cloud Scheduler in conjunction with Pub/Sub to invoke Cloud Run.**

**Explanation:**

  * **Cloud Scheduler:** Designed specifically for scheduling tasks on Google Cloud. It has the necessary permissions to work with Cloud Run.

  * **Pub/Sub:** A decoupling mechanism between Cloud Scheduler and Cloud Run, ensuring the security of your internal ingress settings. Cloud Scheduler can publish a message to a Pub/Sub topic, which your Cloud Run service can subscribe to.

**Why Other Options Might Not Be the Best Fit:**

  * **I. Assign the roles/run.developer IAM role to the service account.** Giving the `roles/run.developer` role to an external service account might loosen security too much for an internally facing Cloud Run instance.

  * **II. Set up a cron job on the Compute Engine VMs to trigger Cloud Run based on the schedule.** While possible, it introduces more management overhead and potential points of failure compared to dedicated services like Cloud Scheduler.

  * **III. Modify the Cloud Run ingress setting to 'Internal and Cloud Load Balancing.'** This would expose your Cloud Run instance, breaking your internal ingress requirement.

---

## Question 15

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Your team manages an application that aggregates news articles from various sources, with a real-time monitoring dashboard accessible to external stakeholders and analysts via a Compute Engine instance running a web application. These stakeholders require secure access to reports without authentication. How should you configure this secure channel?**

- [ ] II. Employ Cloud Scheduler to trigger Cloud Build hourly to produce an export from the reports, storing them in a publicly accessible Cloud Storage bucket.
- [x] IV. Introduce an HTTP(S) load balancer in front of the monitoring dashboard and deploy a Google-managed SSL certificate on the load balancer for traffic encryption.
- [ ] III. Implement an HTTP(S) load balancer preceding the monitoring dashboard and configure Identity-Aware Proxy (IAP) to secure the communication channel.
- [ ] I. Utilize the service account key of the instance to encrypt the traffic.

### Explanation

The recommended approach to configure a secure channel for external stakeholders to access reports without authentication for the web application running on a Compute Engine instance is:

**IV. Introduce an HTTP(S) load balancer in front of the monitoring dashboard and deploy a Google-managed SSL certificate on the load balancer for traffic encryption.**

Explanation:

Option I, utilizing the service account key of the instance to encrypt the traffic, is not suitable for securing access to the web application for external stakeholders. Service account keys are typically used for server-to-server communication or accessing Google Cloud resources, not for securing web application traffic.

Option II, employing Cloud Scheduler to trigger Cloud Build hourly to produce an export from the reports and storing them in a publicly accessible Cloud Storage bucket, does not provide real-time access to the reports. It also introduces unnecessary complexity and potential security risks by making the reports publicly accessible without authentication.

Option III, implementing an HTTP(S) load balancer preceding the monitoring dashboard and configuring Identity-Aware Proxy (IAP) to secure the communication channel, is a valid option. However, it adds complexity by requiring users to authenticate with Google credentials via IAP. Since the requirement specifies that external stakeholders require access without authentication, this option may not be suitable.

Option IV is the recommended approach because it provides encryption for the traffic between external stakeholders and the monitoring dashboard without requiring authentication. Deploying a Google-managed SSL certificate on the HTTP(S) load balancer ensures that the communication channel is encrypted, providing a secure channel for stakeholders to access reports without authentication.

Therefore, option IV is the most appropriate configuration for securing the communication channel for external stakeholders to access reports without authentication.

Documentation:

  * Securing user traffic to Compute Engine instances with SSL/TLS: <https://cloud.google.com/load-balancing/docs/ssl-certificates#compute-ssl-proxy>

  * HTTP(S) Load Balancing: <https://cloud.google.com/load-balancing/docs/https>

---

## Question 16

*Domain 4: Integrating Applications with Google Cloud Services*

**You're developing a new application and require it to trigger only upon updates to a specific file in your Cloud Storage bucket. Your trigger specifications may vary, necessitating a process that accommodates different trigger types. Additionally, you aim for a straightforward configuration to enable multiple team members to update triggers in the future. What is the recommended approach?**

- [x] II. Establish an Eventarc trigger to monitor your Cloud Storage bucket for a designated filename, with the target set as Cloud Run.
- [ ] III. Configure a Cloud Function designed to execute your application, triggered by object updates in Cloud Storage.
- [ ] IV. Configure a Firebase function to execute your application, triggered by object updates in Cloud Storage.
- [ ] I. Configure Cloud Storage events to dispatch to Pub/Sub, leveraging Pub/Sub events to initiate a Cloud Build job executing your application.

### Explanation

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

---

## Question 17

*Domain 4: Integrating Applications with Google Cloud Services*

**What approach should your company adopt to enable data analysts to analyze events using SQL on a near real-time basis, while also accommodating rapid growth and leveraging managed services?**

- [x] I. Create a Pub/Sub topic and a subscription. Stream events from the source into the Pub/Sub topic. Utilize Dataflow to ingest these events into BigQuery.
- [ ] IV. Deploy a Kafka instance on a large Compute Engine instance. Stream events from the source into a Kafka pipeline. Leverage Dataflow to ingest these events into Cloud Storage.
- [ ] III. Create a Pub/Sub topic and a subscription. Stream events from the source into the Pub/Sub topic. Utilize Dataflow to ingest these events into Firestore in Datastore mode.
- [ ] II. Create a Pub/Sub topic and a subscription. Stream events from the source into the Pub/Sub topic. Utilize Dataflow to ingest these events into Cloud Storage.

### Explanation

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

---

## Question 18

*Domain 3: Configuring and Deploying Applications*

You manage an application deployed on **GKE clusters** across multiple environments, using **Cloud Build** for user acceptance testing (UAT). **Artifact Analysis** is integrated with **Cloud Build** , and the **Binary Authorization API** is enabled in all Google Cloud projects for your environments. To ensure that only container images passing specific UAT tests are deployed to production, and with an attestor already created, what should you do next?

- [x] D. After the UAT phase, sign the attestation with a key stored in Cloud Key Management Service (KMS) and add a GKE cluster-specific rule in Binary Authorization for the production Google Cloud project policy.
- [ ] A. After the UAT phase, sign the attestation with a key stored as a Kubernetes secret and add a GKE cluster-specific rule in Binary Authorization for the UAT Google Cloud project.
- [ ] C. After the UAT phase, sign the attestation with a key stored in Cloud Key Management Service (KMS) and add a default rule in Binary Authorization for the UAT Google Cloud project.
- [ ] B. After the UAT phase, sign the attestation with a key stored as a Kubernetes secret and add a GKE cluster-specific rule in Binary Authorization for the production Google Cloud project policy.

### Explanation

The correct answer is 

**D. After the UAT phase, sign the attestation with a key stored in Cloud Key Management Service (KMS) and add a GKE cluster-specific rule in Binary Authorization for the production Google Cloud project policy.**

Explanation:

To ensure that only container images passing UAT are deployed to production, you need to follow these steps:

  1. **Sign the attestation** after the UAT phase, indicating that the image has passed the necessary UAT tests. Using **Cloud Key Management Service (KMS)** to store the signing key is a best practice for security and management, as it allows centralized control over cryptographic keys.

  2. **Add a GKE cluster-specific rule in Binary Authorization for the production Google Cloud project**. This rule ensures that only container images with the required attestation can be deployed to production. By applying this rule to the production project, you restrict deployments to images that have passed UAT.

**Justifications for Incorrect Options:**

  * **Option A: Sign with a key stored as a Kubernetes secret and add a rule in Binary Authorization for the UAT Google Cloud project**  
Storing the signing key as a Kubernetes secret is less secure than using Cloud KMS. Additionally, the Binary Authorization rule should be set in the **production** project, as UAT is not the target deployment environment.

  * **Option B: Sign with a key stored as a Kubernetes secret and add a rule in Binary Authorization for the production project**  
Although this option uses the correct environment for Binary Authorization (production), storing the signing key as a Kubernetes secret is not recommended for security. Using Cloud KMS for key management is more secure.

  * **Option C: Sign with a key stored in Cloud KMS and add a default rule in Binary Authorization for the UAT project**  
Adding a Binary Authorization rule in the UAT project does not control deployments to the production environment. You need the rule in the production project to ensure only tested images are deployed there.

**Relevant Documentation:**

For more information on setting up Binary Authorization and best practices with Cloud KMS, refer to:

  * [Binary Authorization Overview](https://cloud.google.com/binary-authorization/docs/overview)

  * [Using Binary Authorization with GKE](https://cloud.google.com/binary-authorization/docs)

---

## Question 19

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**To ensure a more even distribution of demand within the Cloud Bigtable cluster and generate human-readable row keys, what approach should you take?**

- [ ] A. Utilize serially generated integer values for row keys.
- [ ] B. Employ a subset of the MD5 hash of the row contents for row key generation.
- [x] C. Concatenate multiple human-readable attributes for row key generation.
- [ ] D. Adopt UNIX epoch-styled timestamps represented in milliseconds for row key generation.

### Explanation

The best approach for ensuring even distribution and human-readable row keys in Cloud Bigtable is 

**C. Concatenate multiple human-readable attributes for row key generation.**

Let's understand why and examine the limitations of other choices:

**C. Concatenate multiple human-readable attributes for row key generation.**

  * **Pros:**

    * **Hotspot Prevention:** Distributes data across the table by including multiple attributes, avoiding concentrated access on a single node or range.

    * **Readability:** Allows for easier understanding of data and debugging using meaningful components in the row key.

    * **Flexibility:** You can control the granularity and data organization based on your use case.

  * **Cons:**

    * **Length:** Row keys can get lengthy if many attributes are combined.

    * **Ordering:** Carefully consider the order of attributes to optimize query patterns (put most selective attributes first).

**Incorrect Options:**

  * **A. Utilize serially generated integer values for row keys.**

    * Causes hotspots as data is sequentially inserted, overloading specific nodes.

  * **B. Employ a subset of the MD5 hash of the row contents for row key generation.**

    * While hashing helps with distribution, it sacrifices human readability.

  * **D. Adopt Unix epoch-styled timestamps represented in milliseconds for row key generation.**

    * Leads to hotspots if all writes happen within a similar time frame, and also sacrifices readability.

**Example of good rowkey design:**

If you're storing product orders, a row key might look like:
    
          1. <region>_<customerID>_<orderID>

**Relevant Documentation:**

  * **Bigtable Schema Design:** <https://cloud.google.com/bigtable/docs/schema-design>

  * **Key Visualizer (for hotspot analysis):** <https://cloud.google.com/bigtable/docs/keyvis-overview>

---

## Question 20

*Domain 4: Integrating Applications with Google Cloud Services*

**As you're developing a web application to function on a Google Cloud runtime, with the aim of allowing users to save files to their Drive without domain restrictions, how should you configure authentication for the Google Drive API?**

- [ ] I. Employ an OAuth Client ID along with delegated domain-wide authority.
- [ ] II. Utilize a service account empowered with delegated domain-wide authority.
- [ ] IV. Leverage a service account and request the https://www.googleapis.com/auth/drive.file scope to generate a signed JSON Web Token (JWT).
- [x] III. Opt for an OAuth Client ID and request the https://www.googleapis.com/auth/drive.file scope to acquire an access token for each user.

### Explanation

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

---

## Question 21

*Domain 2: Building and Testing Applications*

**To swiftly assess Pub/Sub integration for each new build of a web application that publishes messages to Pub/Sub, how should local testing be configured?**

- [x] II. Use gcloud to install the Pub/Sub emulator, initiating it with a valid Google Project ID. Configure the local application to use the emulator by exporting the PUBSUB_EMULATOR_HOST variable.
- [ ] I. Enable the Pub/Sub API in the Google Cloud console and configure the local application to call pubsub.googleapis.com.
- [ ] IV. Install Cloud Code in the integrated development environment (IDE), enable Pub/Sub in the Cloud APIs against a valid Google Project ID, and configure the local application to call pubsub.googleapis.com.
- [ ] III. Set the Pub/Sub endpoint to the emulator by executing 'gcloud config set api_endpoint_overrides/pubsub https://pubsubemulator.googleapis.com.com/' before starting the application.

### Explanation

**II. Use gcloud to install the Pub/Sub emulator, initiating it with a valid Google Project ID. Configure the local application to use the emulator by exporting the PUBSUB_EMULATOR_HOST variable.**

**Explanation:**

  * **Emulator for Local Testing:** The Pub/Sub emulator provides a local environment that mimics the production Pub/Sub service, allowing you to test your integration without interacting with the actual cloud service.

  * **gcloud for Setup:** gcloud offers a convenient way to manage the installation and initiation of the emulator.

  * **PUBSUB_EMULATOR_HOST:** This environment variable ensures your local application correctly targets the emulator instead of the production service during development.

**Why Other Options Are Less Ideal:**

  * **I. Enable the Pub/Sub API in the Google Cloud console and configure the local application to call pubsub.googleapis.com.** This would connect your local application to the production Pub/Sub service, not ideal for isolated development and testing.

  * **III. Set the Pub/Sub endpoint to the emulator by executing 'gcloud config set api_endpoint_overrides/pubsub**[**https://pubsubemulator.googleapis.com.com/**](https://pubsubemulator.googleapis.com.com/)**' before starting the application.** This endpoint is not valid. The emulator runs locally, and you'd use the `PUBSUB_EMULATOR_HOST` to point to it.

  * **IV. Install Cloud Code in the integrated development environment (IDE), enable Pub/Sub in the Cloud APIs against a valid Google Project ID, and configure the local application to call pubsub.googleapis.com.** Cloud Code might provide some tools, but it unnecessarily adds IDE dependencies and, by default, would still connect to the production service.

**Reference:**

<https://cloud.google.com/pubsub/docs/emulator>

---

## Question 22

*Domain 3: Configuring and Deploying Applications*

**While testing your ecommerce web application, which employs Cloud Run and Memorystore for Redis, you encounter a 502 Bad Gateway error in the browser. Upon investigation, you discover that the application is failing to connect to Memorystore. What is the probable cause of this error?**

- [ ] III. The firewall rule permitting a connection between Cloud Run and Memorystore was inadvertently removed during an infrastructure update by the DevOps team.
- [ ] IV. You configured your application to utilize a Serverless VPC Access connector on a different subnet in a distinct region than your Cloud Run service.
- [ ] I. Your Memorystore for Redis instance was deployed without a public IP address.
- [x] II. You configured your Serverless VPC Access connector in a different region than your Cloud Run service.

### Explanation

Correct answer

**II. You configured your Serverless VPC Access connector in a different region than your Cloud Run service.**

I is not correct because Cloud Run connects to Memorystore via the Serverless VPC Connector. Connections are over private networks. Public addresses are not required.  
II is correct. All of the components must be in the same region.  
III is not correct because for connectivity between Cloud Run and Memorystore all that is required is a Serverless VPN Connector.  
IV is not correct. The Serverless VPC Connector is configured with a non-overlapping subnet that is not associated with the VPC.  
  
**References:**

[https://cloud.google.com/memorystore/docs/redis/redis-overview#connecting](%0d https:/cloud.google.com/memorystore/docs/redis/redis-overview#connecting)

[https://cloud.google.com/memorystore/docs/redis/connect-redis-instance-cloud-run](%0d https:/cloud.google.com/memorystore/docs/redis/connect-redis-instance-cloud-run%0d)

[https://cloud.google.com/vpc/docs/configure-serverless-vpc-access#creating_a_connector](%0d https:/cloud.google.com/vpc/docs/configure-serverless-vpc-access#creating_a_connector)

---

## Question 23

*Domain 3: Configuring and Deploying Applications*

**You're deploying an application to a Compute Engine virtual machine instance equipped with the Stackdriver Monitoring Agent. The application, a Unix process, needs monitoring to alert if it hasn't run for at least 5 minutes. However, you can't modify the application to generate metrics or logs. Which alert condition is most appropriate for this scenario?**

- [ ] II. Configure process health monitoring to detect any issues with the Unix process.
- [x] III. Utilize metric absence detection to alert when the Unix process hasn't been active for the specified duration.
- [ ] I. Set up an uptime check to monitor the availability of the virtual machine instance.
- [ ] IV. Establish a metric threshold to trigger an alert when the Unix process activity falls below the defined threshold.

### Explanation

**Correct Option:**

  * **III. Utilize metric absence detection to alert when the Unix process hasn't been active for the specified duration.**

**Justification:**

Metric absence detection perfectly aligns with the scenario where the application doesn't generate custom metrics or logs. Since most Unix processes utilize system resources, their activity often reflects in system-level metrics like CPU or memory usage. Metric absence allows you to configure an alert that triggers if these metrics haven't been reported for a certain timeframe (5 minutes in this case). This signifies that the process is likely inactive.

  * Supporting Documentation: <https://stackoverflow.com/questions/53095774/stackdriver-monitoring-metric-absent>

**Incorrect Options:**

  * **I. Set up an uptime check to monitor the availability of the virtual machine instance.**

  * Justification: Uptime checks are effective for ensuring the entire VM is operational, but they don't provide insight into the status of individual processes running within the VM. A VM can be online while a specific process within it might be inactive.

  * **II. Configure process health monitoring to detect any issues with the Unix process.**

  * Justification: While this might seem like a suitable solution, Stackdriver Monitoring Agent has limitations when monitoring arbitrary Unix processes. It requires the application to send custom metrics for effective process health monitoring. In this scenario, the application doesn't emit such metrics.

  * Supporting Documentation: <https://cloud.google.com/monitoring/custom-metrics>

  * **IV. Establish a metric threshold to trigger an alert when the Unix process activity falls below the defined threshold.**

  * Justification: This approach could be viable if the Unix process has a metric explicitly indicating its activity level. However, if the only available metrics are system-level ones (CPU, memory), a complete drop to zero is a more reliable indicator of process inactivity compared to a specific low threshold.

Setting a threshold on these system metrics might trigger alerts due to normal process behavior (e.g., the process might sleep occasionally, causing a temporary dip in CPU usage).

---

## Question 24

*Domain 4: Integrating Applications with Google Cloud Services*

**In order to conduct near real-time analysis of audit activity logs captured in Cloud Logging, with multiple processes performing different types of analysis on the logging data, what approach should you adopt?**

- [ ] A. Develop an application to directly read the logs from the Cloud Logging API.
- [x] B. Configure a Cloud Logging sink to Pub/Sub, and retrieve the logs from a Pub/Sub topic.
- [ ] C. Implement a Cloud Function endpoint to directly read from the Cloud Logging API and transfer the logs to Dataproc.
- [ ] D. Establish a Cloud Logging sink to Cloud Storage and retrieve the logs from a Cloud Storage bucket.

### Explanation

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

---

## Question 25

*Domain 3: Configuring and Deploying Applications*

**How can you streamline the management effort required to transition from decomposing a monolithic application into microservices, especially when dealing with multiple instances that require read and write access to a configuration file stored on a shared file system, without necessitating the rewriting of the application code?**

- [ ] II. Opt for a new persistent disk, configuring it as a shared PersistentVolume to fulfill the shared file system requirement.
- [ ] IV. Introduce a new ConfigMap along with volumeMount to efficiently store and access the contents of the configuration file.
- [x] III. Deploy a new Filestore instance and link the volume as an NFS PersistentVolume for seamless access to the configuration file.
- [ ] I. Utilize a Cloud Storage bucket, establishing it as a mounted resource within the container using FUSE.

### Explanation

**The recommended approach is:**

**III. Deploy a new Filestore instance and link the volume as an NFS PersistentVolume for seamless access to the configuration file.**

**Justification:**

  * **Shared File System:** Filestore offers a managed NFS service, creating a shared file system accessible by multiple container instances, perfectly suited for your scenario. (<https://cloud.google.com/filestore/docs/overview>)

  * **Performance and Scalability:** NFS offers better performance and can scale efficiently for multiple concurrent file accesses compared to FUSE-based workarounds on Cloud Storage. (<https://www.linuxtechi.com/configure-nfs-persistent-volume-kubernetes/>)

  * **No Code Changes:** This approach avoids the need to rewrite application code, minimizing the transition effort.

**Considerations:**

  * **Cost:** While convenient, Filestore can be more expensive than object storage solutions. Evaluate your budget and expected usage patterns.

  * **Management Overhead:** Introducing a new service like Filestore adds a small layer of additional management complexity.

**Why Other Options Are Less Ideal:**

  * **I. Utilize a Cloud Storage bucket, establishing it as a mounted resource within the container using FUSE.**

    * **Performance Limitations:** FUSE-based mounts on Cloud Storage can introduce performance overhead and latency, especially with frequent reads and writes compared to native file systems like NFS. (<https://cloud.google.com/storage/docs/gcs-fuse>)

  * **II. Opt for a new persistent disk, configuring it as a shared PersistentVolume to fulfill the shared file system requirement.**

    * **Complexity and Single Point of Failure:** Shared PersistentVolumes often involve complex setups like ReadWriteMany volumes in Kubernetes. Additionally, a single disk failure would impact all instances accessing the configuration file. (<https://www.shebanglabs.io/how-to-set-up-read-write-many-rwx-persistent-volumes-with-nfs-on-kubernetes/>)

  * **IV. Introduce a new ConfigMap along with volumeMount to efficiently store and access the contents of the configuration file.**

    * **Limited Use Case:** ConfigMaps are well-suited for storing configuration data within a Kubernetes cluster, but they are not designed for concurrent modification by multiple containers, which is a key requirement for your shared configuration file. (<https://kubernetes.io/docs/concepts/configuration/configmap/>)

---

## Question 26

*Domain 4: Integrating Applications with Google Cloud Services*

**In the context of an application monitoring numerous stock prices, how should the Pub/Sub subscription be configured to manage a high volume of messages and update the current stock price in a single large in-memory database, considering each message includes the stock symbol, price, and timestamp?**

- [ ] IV. Establish a pull subscription with both ordering and exactly-once delivery disabled.
- [ ] II. Create a push subscription with both ordering and exactly-once delivery disabled.
- [ ] I. Set up a pull subscription with exactly-once delivery enabled.
- [x] III. Configure a push subscription with exactly-once delivery enabled.

### Explanation

**Given the context of an application monitoring numerous stock prices and updating the current stock price in a single large in-memory database, considering each message includes the stock symbol, price, and timestamp, the most suitable configuration for the Pub/Sub subscription would be:**

**III. Configure a push subscription with exactly-once delivery enabled.**

Here's why:

  1. **Push Subscription** : Push subscriptions are generally preferred for high-volume message processing because they can handle a large number of incoming messages more efficiently than pull subscriptions. Push subscriptions allow Google Cloud Pub/Sub to push messages to the subscriber, reducing the need for the subscriber to continuously poll the Pub/Sub topic.

  2. **Exactly-once Delivery Enabled** : Ensuring exactly-once delivery helps prevent duplicate processing of messages, which is crucial for maintaining data consistency, especially in scenarios where updates to the stock prices need to be accurate and not duplicated. This ensures that each message is processed exactly once, avoiding potential issues with data integrity.

Option I is less suitable because pull subscriptions might not be as efficient for managing a high volume of messages, as they require the subscriber to actively pull messages from the Pub/Sub topic.

Option II is not ideal because push subscriptions are generally preferred for high-volume message processing, and disabling exactly-once delivery could lead to potential issues with data consistency.

Option IV might not be the most efficient choice for managing a high volume of messages, and disabling exactly-once delivery could lead to potential issues with data consistency.

**Therefore, option III, configuring a push subscription with exactly-once delivery enabled, is the most appropriate choice for efficiently managing a high volume of messages and ensuring data consistency in updating the current stock prices.**

---

## Question 27

*Domain 4: Integrating Applications with Google Cloud Services*

**As part of an e-commerce company, you are designing a new Orders API to be hosted via Apigee. You created two environments in Apigee, orders-test and orders-prod, and plan to use unique URLs, test.lnk-42.com/api/v1/orders and lnk-42.com/api/v1/orders, for each environment. How can you ensure that each environment is only accessible via its designated URL?**

- [x] D. 1. Attach orders-test to the test environment group and orders-prod to the production environment group.  
  2\. Add each hostname to the relevant environment group.
- [ ] A. 1. Attach orders-test and orders-prod to the orders environment group.  
  2\. Add each hostname to the respective environment.
- [ ] C. 1. Attach orders-test to the test environment group and orders-prod to the production environment group.  
  2\. Add each hostname to the appropriate environment.
- [ ] B. 1. Attach orders-test and orders-prod to the orders environment group.  
  2\. Add each hostname to the orders environment group.

### Explanation

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

---

## Question 28

*Domain 2: Building and Testing Applications*

**To align with your company's IAM tracking procedures and support rapid release cycles with minimal merge conflicts, how should you design a version control system?**

- [ ] III. Create a GitHub repository, mirror it to a Cloud Source Repositories repository, and implement trunk-based development.
- [ ] IV. Create a GitHub repository, mirror it to a Cloud Source Repositories repository, and employ feature-based development.
- [x] I. Establish a Cloud Source Repositories repository and implement trunk-based development.
- [ ] II. Set up a Cloud Source Repositories repository and employ feature-based development.

### Explanation

**Likely Best Solution:**

**I. Establish a Cloud Source Repositories repository and implement trunk-based development.**

  * **IAM Tracking:** Cloud Source Repositories integrates well with Google Cloud's IAM auditing and logging, providing a clear audit trail for changes.

  * **Reduced Merge Conflicts:** Trunk-based development encourages small, frequent commits to the main branch, minimizing the likelihood of large, complex merge conflicts.

**Consideration if GitHub is Mandated:**

**III. Create a GitHub repository, mirror it to a Cloud Source Repositories repository, and implement trunk-based development.**

  * **Workflow Familiarity:** Allows developers to leverage GitHub if it's their preferred tool.

  * **IAM Tracking:** Mirroring to Cloud Source Repositories ensures IAM auditability within Google Cloud.

  * **Potential Complexity:** Maintaining synchronization between repositories introduces a slight overhead.

**Why the Feature Branch Options Are Less Ideal:**

  * **II. Set up a Cloud Source Repositories repository and employ feature-based development.** Feature branches, while common, increase the potential for larger merge conflicts, especially in rapid release environments.

  * **IV. Create a GitHub repository, mirror it to a Cloud Source Repositories repository, and employ feature-based development.** Adds the complexity of mirroring on top of the merge conflict concerns with feature branches.

---

## Question 29

*Domain 3: Configuring and Deploying Applications*

**How can you ensure that your Google Kubernetes Engine (GKE) cluster optimizes performance and minimizes cost by automatically adjusting the number of pods and nodes based on CPU load fluctuations?**

- [ ] IV. Modify the MIG to enable Autoscaling to configure max and min amount of nodes based on CPU load, and configure the Vertical Pod Autoscaler (VPA) to scale workloads based on CPU load.
- [ ] I. Modify the managed instance group (MIG) to enable Autoscaling to configure max and min amount of nodes based on CPU load.
- [x] II. Enable Cluster Autoscaler on the GKE cluster, and configure the Horizontal Pod Autoscaler (HPA) to autoscale the workload based on CPU load.
- [ ] III. Enable Cluster Autoscaler on the GKE cluster, and configure the HPA to autoscale the workloads based on a custom metric.

### Explanation

The best solution is

**II. Enable Cluster Autoscaler on the GKE cluster, and configure the Horizontal Pod Autoscaler (HPA) to autoscale the workload based on CPU load.**

**Explanation:**

  * **Cluster Autoscaler:** This is the essential component for scaling the number of nodes in a GKE cluster based on resource demands (<https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler>).

  * **Horizontal Pod Autoscaler (HPA):** The HPA works in tandem with Cluster Autoscaler. It scales the number of pods in your deployments based on CPU utilization metrics (<https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/>).

**Why other options are less ideal:**

  * **I. Modify the managed instance group (MIG) to enable Autoscaling to configure max and min amount of nodes based on CPU load.** While MIG autoscaling helps, it does not directly manage the scaling of pods within your Kubernetes deployments.

  * **III. Enable Cluster Autoscaler on the GKE cluster, and configure the HPA to autoscale the workloads based on a custom metric.** In most cases, CPU utilization is the ideal metric for horizontal pod scaling to match demand. Custom metrics might be needed in specific scenarios, but they introduce potential additional complexity.

  * **IV. Modify the MIG to enable Autoscaling to configure max and min amount of nodes based on CPU load, and configure the Vertical Pod Autoscaler (VPA) to scale workloads based on CPU load.** The VPA adjusts resource requests and limits for individual pods but doesn't directly increase or decrease the number of pods like the HPA.

---

## Question 30

*Domain 3: Configuring and Deploying Applications*

**In order to deploy new features quickly while minimizing the risk of negatively impacting all users in a Cloud Run application with significant traffic volume, which approach should you choose?**

- [ ] I. Schedule weekly load tests against the production application.
- [x] IV. Implement traffic splitting to have a smaller portion of users test out new features, gradually adjusting traffic splitting until all users receive the new features.
- [ ] II. Utilize the local development environment to perform load testing outside Google Cloud.
- [ ] III. Deploy new features as a new version, conduct smoke tests before allowing all users access, and then enable all users to access the new features.

### Explanation

The best approach for your scenario is

**IV. Implement traffic splitting to have a smaller portion of users test out new features, gradually adjusting traffic splitting until all users receive the new features.**

Here's a breakdown of why this is superior and the limitations of the other choices:

**IV. Traffic Splitting:**

  * **Controlled Rollout:** Allows you to expose new features to a subset of users, minimizing the blast radius of potential issues.

  * **Monitoring and Feedback:** You can monitor real-world performance and gather feedback from the initial rollout before exposing all users.

  * **Gradual Increase:** Traffic splitting allows you to carefully increase the exposure of new features, making it easier to identify and address problems before they become widespread.

**Limitations of Other Approaches:**

  * **I. Schedule weekly load tests against the production application.** Load testing is important but doesn't fully simulate real-world user behavior and edge cases that might arise with new features.

  * **II. Utilize the local development environment to perform load testing outside of Google Cloud.** Local environments rarely match the production environment's scale and complexity, making testing less reliable.

  * **III. Deploy new features as a new version, conduct smoke tests before allowing all users access, and then enable all users to access the new features.** While smoke testing is valuable, it lacks the phased rollout and user feedback that traffic splitting provides.

**Traffic Splitting on Cloud Run**

Cloud Run natively supports traffic splitting, allowing you to precisely control the percentage of traffic directed to different revisions of your service (<https://cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration>).

---

## Question 31

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

You are developing a mobile app for creating and managing **to-do lists** with the following requirements:

  * **Data storage and synchronization** across multiple mobile devices.

  * **Offline access** capability.

  * **Real-time updates** on each user’s device.

You need to select a database solution that minimizes operational effort. Which approach should you choose?

- [ ] D. Implement a SQLite database on each device and use a scheduled job to synchronize each device’s database with a copy stored in Cloud Storage.
- [ ] A. Set up a Cloud SQL for MySQL instance, design a data model for storing to-do information, and create indexes for frequently used queries.
- [ ] B. Set up a Bigtable instance, design the schema to avoid write hotspots, and use Bigtable change streams to capture data changes.
- [x] C. Use Firestore as the database, enable offline persistence to cache data locally, and listen for document changes to update the app in real-time.

### Explanation

The correct answer is 

**C. Use Firestore as the database, enable offline persistence to cache data locally, and listen for document changes to update the app in real-time.**

Explanation:

**Firestore** is ideal for mobile apps with requirements for **data storage, synchronization, offline access, and real-time updates**. Firestore provides built-in features that address these needs with minimal operational effort:

  1. **Offline Persistence** : Firestore supports offline data persistence, enabling users to access and update their data even when disconnected. Data is automatically synchronized with the cloud when the device reconnects.

  2. **Real-Time Updates** : Firestore’s real-time listeners allow the app to receive updates whenever data changes, keeping multiple devices in sync without additional setup.

  3. **Automatic Scaling and Managed Service** : Firestore is fully managed, eliminating the need to handle operational tasks like scaling, backups, and server management.

Justifications for Incorrect Options:

  * **Option A: Set up a Cloud SQL for MySQL instance**  
While Cloud SQL supports relational data, it lacks built-in offline persistence and real-time updates, both of which would require additional development work. Also, managing Cloud SQL would introduce operational overhead.

  * **Option B: Set up a Bigtable instance**  
**Bigtable** is a NoSQL database designed for high-throughput analytics rather than real-time mobile app use cases. It doesn’t support offline access or real-time updates, making it less suited to this requirement.

  * **Option D: Implement a SQLite database on each device with synchronization via Cloud Storage**  
Using SQLite would require custom synchronization logic, and Cloud Storage is not designed for database-like synchronization or real-time updates. This approach would involve significant operational and development overhead to meet the requirements.

**Relevant Documentation:**

For more on Firestore’s offline persistence and real-time capabilities, refer to:

  * [Firestore Offline Persistence](https://firebase.google.com/docs/firestore/manage-data/enable-offline)

  * [Firestore Real-Time Updates](https://firebase.google.com/docs/firestore/query-data/listen)

---

## Question 32

*Domain 4: Integrating Applications with Google Cloud Services*

**In the process of developing an application on Cloud Run that relies on REST API calls to interact with Google Cloud services, and considering the absence of support for Cloud Client Libraries in the selected programming language, the goal is to configure the associated service account to serve as the authorization identity for these calls. What is the recommended approach to achieve this?**

- [ ] I. Embed an API key within the application and transmit its value through the Authorization header.
- [ ] III. Utilize an API key associated with the service account by setting its value as the GOOGLE_APPLICATION_CREDENTIALS environment variable.
- [x] II. Obtain the access token from the metadata server and transmit its value through the Authorization header.
- [ ] IV. During startup, fetch and store the access token using gcloud auth application-default print-access-token, saving it in a file whose path is specified in the GOOGLE_APPLICATION_CREDENTIALS environment variable.

### Explanation

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

---

## Question 33

*Domain 4: Integrating Applications with Google Cloud Services*

**To allow a Compute Engine instance without a public IP address to access the Cloud Storage API, what should you implement?**

- [ ] II. Implement VPC Network Peering.
- [ ] I. Utilize Carrier Peering.
- [ ] III. Deploy Shared VPC networks.
- [x] IV. Enable Private Google Access.

### Explanation

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

---

## Question 34

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You are designing a Node.js-based mobile news feed application that will store data on Google Cloud. The database should provide zonal resiliency by default, low-latency responses, ACID compliance, optional middle-tier functionality, semi-structured data storage, and support for network-partition-tolerant and offline-mode client libraries. Which database should you choose?**

- [ ] D. Set up BigQuery and use the BigQuery REST API in the application.
- [x] A. Set up Firestore and use the Firestore client library in the application.
- [ ] C. Set up Cloud SQL and use the Google Client Library for Cloud SQL in the application.
- [ ] B. Set up Bigtable and use the Bigtable client in the application.

### Explanation

The correct answer is

**A. Set up Firestore and use the Firestore client library in the application**.

Explanation:

**Firestore** is a managed NoSQL document database on Google Cloud that meets the requirements specified for the mobile news feed application:

  * **Zonal resiliency by default** : Firestore offers high availability and resilience, automatically replicating data across multiple zones within a region.

  * **Low-latency responses** : Firestore provides low-latency access suitable for mobile applications with real-time data needs.

  * **ACID compliance** : Firestore transactions are ACID-compliant, ensuring data consistency.

  * **Optional middle-tier functionality** : Firestore can be accessed directly from client-side applications, allowing for direct client-server interactions without needing a middle-tier.

  * **Semi-structured data storage** : Firestore supports semi-structured data storage, allowing for flexible data models that can adapt to evolving data structures.

  * **Network-partition-tolerant and offline-mode client libraries** : Firestore’s client libraries offer offline mode, allowing apps to function when disconnected and synchronizing data when connectivity is restored.

**Justifications for Incorrect Options:**

  * **Option B: Set up Bigtable and use the Bigtable client in the application**  
**Bigtable** is a NoSQL wide-column database suitable for analytics and high-throughput use cases but does not support ACID transactions or offline-mode client libraries, making it unsuitable for this mobile application’s needs.

  * **Option C: Set up Cloud SQL and use the Google Client Library for Cloud SQL in the application**  
**Cloud SQL** is a relational database service that provides ACID compliance and zonal resiliency, but it does not support offline mode for client libraries. It is also not optimized for semi-structured data or mobile application latency needs.

  * **Option D: Set up BigQuery and use the BigQuery REST API in the application**  
**BigQuery** is designed for large-scale data analysis and is not suitable for transactional, low-latency, or semi-structured data storage needs for a mobile application.

**Relevant Documentation:**

For more details, refer to:

  * [Firestore Documentation](https://cloud.google.com/firestore/docs)

  * [Google Cloud Storage Options](https://cloud.google.com/products/storage?hl=en)

---

## Question 35

*Domain 4: Integrating Applications with Google Cloud Services*

**In deploying an application on a Google Kubernetes Engine (GKE) cluster, it needs to connect to a legacy REST service spread across two GKE clusters in different regions. The objective is to establish a resilient connection with minimal steps and enable probe-based health checks on the legacy service via a separate port. How should the connection be configured? (Select two options.)**

- [ ] V. Configure the legacy service's firewall to allow health checks initiated from the Traffic Director control plane.
- [x] III. Configure the legacy service's firewall to allow health checks initiated from the sidecar proxy.
- [ ] II. Implement a proxyless Traffic Director configuration for the application.
- [x] I. Utilize Traffic Director alongside a sidecar proxy to link the application to the service.
- [ ] IV. Configure the legacy service's firewall to allow health checks initiated from the application.

### Explanation

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

---

## Question 36

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**In accordance with the principle of least privilege, which role should you assign to the service account linked to your application's instance, which communicates with Cloud SQL via Cloud SQL Auth Proxy on Google Kubernetes Engine?**

- [ ] II. Assign the Project Owner role.
- [ ] I. Assign the Project Editor role.
- [x] III. Assign the Cloud SQL Client role.
- [ ] IV. Assign the Cloud SQL Editor role.

### Explanation

**The correct answer is**

**III. Assign the Cloud SQL Client role.**

**Justification:**

  * **Principle of Least Privilege:** This principle dictates that you should only grant the minimum necessary permissions for a task. The Cloud SQL Client role specifically grants the ability to connect to Cloud SQL instances.

  * **Security:** Assigning broader roles (Project Editor or Owner) opens up unnecessary permissions to a wide range of resources in the project, increasing potential attack vectors.

**Why other options are not suitable:**

  * **I. Project Editor:** This role grants far-reaching permissions to edit most resources within a project, far exceeding what's required for simply connecting to Cloud SQL.

  * **II. Project Owner:** This role has full administrative control over the entire project, posing a high security risk if the service account is compromised.

  * **IV. Cloud SQL Editor:** This role allows modification of Cloud SQL instances themselves. Unless your application specifically requires database modification capabilities, this role also grants excessive permissions.

**References:**

[https://cloud.google.com/iam/docs/understanding-roles](https://cloud.google.com/iam/docs/understanding-roles  https://cloud.google.com/iam/docs/overview  https://cloud.google.com/sql/docs/mysql/connect-instance-kubernetes#set_up_a_service_account  https://cloud.google.com/sql/docs/postgres/connect-instance-kubernetes#set_up_a_service_account)

[https://cloud.google.com/iam/docs/overview](https://cloud.google.com/iam/docs/understanding-roles  https://cloud.google.com/iam/docs/overview  https://cloud.google.com/sql/docs/mysql/connect-instance-kubernetes#set_up_a_service_account  https://cloud.google.com/sql/docs/postgres/connect-instance-kubernetes#set_up_a_service_account)

[https://cloud.google.com/sql/docs/mysql/connect-instance-kubernetes#set_up_a_service_account](https://cloud.google.com/iam/docs/understanding-roles  https://cloud.google.com/iam/docs/overview  https://cloud.google.com/sql/docs/mysql/connect-instance-kubernetes#set_up_a_service_account  https://cloud.google.com/sql/docs/postgres/connect-instance-kubernetes#set_up_a_service_account)

[https://cloud.google.com/sql/docs/postgres/connect-instance-kubernetes#set_up_a_service_account](https://cloud.google.com/iam/docs/understanding-roles  https://cloud.google.com/iam/docs/overview  https://cloud.google.com/sql/docs/mysql/connect-instance-kubernetes#set_up_a_service_account  https://cloud.google.com/sql/docs/postgres/connect-instance-kubernetes#set_up_a_service_account)

---

## Question 37

*Domain 3: Configuring and Deploying Applications*

**As a cluster administrator overseeing Google Kubernetes Engine (GKE), your organization's clusters are enrolled in a release channel. You require timely updates on pertinent events impacting your GKE clusters, including available upgrades and security bulletins. What is the recommended approach?**

- [ ] IV. Establish an RSS subscription to receive a daily summary of the GKE release notes.
- [ ] II. Schedule a query against the google_cloud_release_notes BigQuery dataset to retrieve relevant information.
- [x] I. Set up cluster notifications to be dispatched to a Pub/Sub topic.
- [ ] III. Query the GKE API to ascertain available versions.

### Explanation

**Correct Option:**

**I. Set up cluster notifications to be dispatched to a Pub/Sub topic.**

**Justification:**

  * **Proactive Updates:** GKE cluster notifications pushed to a Pub/Sub topic provide real-time alerts for important events, including upgrade availability and security notices.

  * **Flexibility:** You can integrate Pub/Sub with various tools (e.g., email, Slack, webhooks) to tailor how you receive the critical notifications.

  * **Minimizes Manual Effort:** Avoids the need for manual queries or polling.

**Why Other Options Are Less Ideal:**

  * **II. Schedule a query against the google_cloud_release_notes BigQuery dataset...**

    * **Reactive:** Regularly querying BigQuery is still a manual approach. While you'll get release information, it's less timely than Pub/Sub notifications.

  * **III. Query the GKE API to ascertain available versions.**

    * **Focused Scope:** Only provides information on available versions, missing out on other important security notices.

  * **IV. Establish an RSS subscription to receive a daily summary...**

    * **Delayed:** Daily summaries may not be timely enough for critical security bulletins or essential upgrades.

**References:**

<https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications>

<https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels#channels>

<https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications>

---

## Question 38

*Domain 2: Building and Testing Applications*

**As a lead developer, you need to recommend a development environment for an organization that recently integrated multiple Google Cloud services within VPC environments secured by VPC Service Controls and Private Service Connect endpoints. Developers use various operating systems, frameworks, and IDEs. Your recommendation should:**

  * **Enforce consistent security controls.**

  * **Access Google Cloud resources and applications within the VPC.**

  * **Allow installation of custom tools and utilities in the development environments.**

**What solution should you recommend?**

- [ ] D. Use the Cloud Code extension with the organization’s IDEs and enable access to VPC services using Identity-Aware Proxy.
- [x] B. Use Cloud Workstations with preconfigured base images, and for custom tools and utilities, use custom images that are rebuilt weekly.
- [ ] C. Use the Cloud Code extension with the organization’s IDEs and configure Cloud VPN for VPC access.
- [ ] A. Use Cloud Workstations and allow developers to create custom images as needed.

### Explanation

**B. Use Cloud Workstations with preconfigured base images, and for custom tools and utilities, use custom images that are rebuilt weekly.**

**Explanation:**

**Why B is the best choice:**

  * **Enforces Consistent Security Controls:**

    * Preconfigured base images ensure that all development environments start with a standardized security baseline.

    * Weekly rebuilds guarantee that the latest security patches and configurations are applied.

  * **Access to Google Cloud Resources and Applications within the VPC:**

    * Cloud Workstations provide a secure and isolated development environment that can access VPC resources and applications.

    * VPC Service Controls and Private Service Connect ensure that only authorized resources can access the VPC.

  * **Allows Installation of Custom Tools and Utilities:**

    * Custom images enable developers to install specific tools and utilities tailored to their needs, while maintaining security standards.

    * Weekly rebuilds of custom images keep them up-to-date and secure.

**Why other options are not as suitable:**

  * **A. Cloud Workstations with Custom Images:** While this option provides flexibility, it can lead to inconsistencies in security configurations if not managed carefully.

  * **C. Cloud Code Extension with Cloud VPN:** This option can be complex to set up and manage, and it may not provide the same level of security and isolation as Cloud Workstations.

  * **D. Cloud Code Extension with Identity-Aware Proxy:** This option can be more complex to configure and manage than Cloud Workstations, and it may not provide the same level of security and isolation.

By choosing Option B, the organization can balance security, flexibility, and developer productivity.

**For more information, refer to the following documentation:**

  * Cloud Workstations: <https://cloud.google.com/workstations/docs>

  * VPC Service Controls: <https://cloud.google.com/vpc-service-controls/docs>

  * Private Service Connect: <https://cloud.google.com/vpc/docs/private-service-connect>

---

## Question 39

*Domain 4: Integrating Applications with Google Cloud Services*

**In your mobile web application where global users vote on popular topics, with a very high volume of votes expected during each 30-minute voting window for each topic, you need to capture and count votes within these intervals while also storing them for future analysis and reporting. How should you approach this?**

- [ ] I. Save the votes to Memorystore, then utilize Cloud Functions to insert the counts into BigQuery, and visualize the results in Google Data Studio.
- [ ] III. Publish the votes to Pub/Sub and use Cloud Functions to insert both the counts and votes into Cloud Storage, thereafter displaying the results in Google Data Studio.
- [ ] IV. Implement Firebase for user authentication, enabling the direct publication of votes to Firestore. Export the votes to a CSV file and import them into Sheets for reporting purposes.
- [x] II. Publish the votes to Pub/Sub, and employ a Dataflow pipeline to insert both the counts and votes into BigQuery, subsequently visualizing the results in Google Data Studio.

### Explanation

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

---

## Question 40

*Domain 3: Configuring and Deploying Applications*

**Your application logs to Stackdriver, and you need to obtain the count of all requests made to endpoints starting with /api/alpha/. How can you achieve this?**

- [ ] IV. Export the logs to Cloud Pub/Sub and count the lines matching the pattern /api/alpha.
- [ ] I. Create a Stackdriver counter metric for the path /api/alpha/.
- [x] II. Create a Stackdriver counter metric for the endpoint /api/alpha/*.
- [ ] III. Export the logs to Cloud Storage and count the lines matching the pattern /api/alpha.

### Explanation

**The most suitable approaches:**

  * **II. Create a Stackdriver counter metric for the endpoint /api/alpha/*.** This is the most direct and efficient way. Steps involved:

    1. Go to Stackdriver Monitoring.

    2. Create a custom counter metric.

    3. Filter this metric with the HTTP request path `/api/alpha/*`

**Why the other options aren't the best fit:**

  * **I. Create a Stackdriver counter metric for the path /api/alpha/.** This is too specific. It won't count requests to sub-endpoints like `/api/alpha/resource1`.

  * **III. Export the logs to Cloud Storage and count the lines matching the pattern /api/alpha.** This method works, but it's less efficient for real-time monitoring:

Set up a logs export to Cloud Storage.

Filter logs for lines containing `/api/alpha/*`.

Use tools (like command-line tools or a script) to count the matching lines.

* **IV. Export the logs to Cloud Pub/Sub and count the lines matching the pattern /api/alpha.** This adds unnecessary complexity. Pub/Sub is good for real-time message distribution, but not optimized for log analysis and counting.

---

## Question 41

*Domain 4: Integrating Applications with Google Cloud Services*

**What action should you take to ensure that consumers of your API endpoint are notified when a write request to Firestore in Datastore mode fails due to encountering an HTTP 5xx server error?**

- [ ] B. Return an HTTP 406 Not Acceptable response.
- [ ] A. Return an HTTP 204 No Content response.
- [x] C. Return an HTTP 500 Internal Server Error response.
- [ ] D. Retry the Datastore API with exponential backoff until Firestore returns an HTTP 2xx response.

### Explanation

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

---

## Question 42

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Which approach should you take to quickly gather data points and suggest improvements to your Tech Lead for optimizing the performance and cost-effectiveness of the web application after migrating it to Google Cloud?**

- [x] III. Migrate the database to Cloud SQL. Then import the data into Firestore in Native mode.
- [ ] II. Migrate the database to BigQuery. Then import the data into Firestore in Native mode.
- [ ] IV. Create a Compute Engine virtual machine instance in Google Cloud, and install PostgreSQL and MongoDB Server software. Migrate the database to the new PostgreSQL, and then migrate the data to MongoDB.
- [ ] I. Migrate the database to Cloud SQL. Then import the data into Cloud Storage.

### Explanation

To quickly gather data points and suggest improvements to your Tech Lead for optimizing the performance and cost-effectiveness of the web application after migrating it to Google Cloud, the most appropriate approach would be:

**III. Migrate the database to Cloud SQL. Then import the data into Firestore in Native mode.**

Explanation:

Option I suggests migrating the database to Cloud SQL and then importing the data into Cloud Storage. While Cloud SQL can be a suitable choice for relational databases, importing data into Cloud Storage might not directly provide insights into optimizing performance and cost-effectiveness. Additionally, Cloud Storage is an object storage solution and may not be the best fit for database storage.

Option II suggests migrating the database to BigQuery and then importing the data into Firestore in Native mode. BigQuery is a data warehouse solution and is typically used for analytical purposes rather than transactional databases. Firestore in Native mode is a NoSQL document database, and while it might be suitable for some use cases, it may not provide the necessary insights for optimizing performance and cost-effectiveness of a web application.

Option IV suggests creating a Compute Engine virtual machine instance, installing PostgreSQL and MongoDB Server software, and migrating the database. This approach introduces unnecessary complexity and may not align with best practices for managing databases on Google Cloud. Managing databases on Compute Engine instances requires manual provisioning, scaling, and maintenance, which can increase operational overhead and costs.

Option III is the most appropriate approach because it involves migrating the database to Cloud SQL, which is a fully managed relational database service on Google Cloud. This simplifies database management and allows you to quickly gather performance and cost-related metrics. Additionally, importing data into Firestore in Native mode can provide insights into optimizing performance and cost-effectiveness, especially if the application can benefit from Firestore's scalability and flexibility.

Therefore, option III is the most suitable approach for quickly gathering data points and suggesting improvements for optimizing the performance and cost-effectiveness of the web application after migrating it to Google Cloud.

**Documentation:**

  * Cloud SQL: <https://cloud.google.com/sql>

  * Firestore: <https://cloud.google.com/firestore>

---

## Question 43

*Domain 4: Integrating Applications with Google Cloud Services*

**Your company relies on a BigQuery data mart to furnish analytics insights to numerous employees. One user requires the ability to run jobs without impeding important workloads, showing no concern for job duration. Your goal is to fulfill this request while minimizing both company expenses and your own effort. What action should you take?**

- [ ] IV. Permit the user to execute jobs during periods when critical workloads are not active, ensuring minimal disruption while utilizing existing resources efficiently.
- [ ] II. Establish a separate project dedicated to the user, providing autonomy for job execution without impacting existing workloads.
- [ ] III. Grant the user the job.user role within the current project, enabling them to submit jobs without unnecessary administrative overhead.
- [x] I. Instruct the user to execute the jobs as batch jobs, allowing for flexible scheduling and resource allocation.

### Explanation

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

---

## Question 44

*Domain 4: Integrating Applications with Google Cloud Services*

**In order to minimize operational overhead while using Cloud Run to write every Pub/Sub message to both a Cloud Storage object and a BigQuery table, which architecture should you implement?**

- [ ] D. Two topics, 2 subscriptions, 2 Cloud Run services: Two independent Pub/Sub topics are used. Each topic has its own subscription, and a Cloud Run service listens to each subscription. This configuration allows for handling completely separate message streams with independent processing.
- [ ] A. One topic, 1 subscription, 2 Cloud Run services: A single Pub/Sub topic publishes messages to one subscription. Two separate Cloud Run services can be configured to listen on that subscription and process the messages.
- [ ] C. One topic, 1 Cloud Run service, 1 push subscription: One Pub/Sub topic with a single subscription. A Cloud Run service receives messages via a push subscription, meaning Pub/Sub actively delivers messages to the service. Data can be written to BigQuery and then Cloud Storage.
- [x] B. One topic, 2 subscriptions, 2 Cloud Run services: Similar to A, but with two subscriptions. Each Cloud Run service listens to a different subscription, allowing for further message filtering or processing specialization.

### Explanation

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

---

## Question 45

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**As a developer at a social media firm transitioning from MySQL to Firestore on Google Cloud to manage user profiles and posts, how should you structure the Firestore collections?**

- [ ] I. Opt for a single root collection for user profiles and another for user posts.
- [ ] IV. Create a root collection for user posts, with subcollections dedicated to each user's profile.
- [x] II. Choose a single root collection for user profiles, and establish subcollections for each user's posts.
- [ ] III. Implement a single root collection for user profiles, storing each user's posts as a nested list within their profile document.

### Explanation

**II. Choose a single root collection for user profiles, and establish subcollections for each user's posts.**

**Explanation:**

  * **Scalability:** Root-level collections scale better than large, nested documents. This accommodates potential growth in the number of users and their posts.

  * **Optimized Queries:** Separating user profiles and posts facilitates efficient queries. You can easily fetch a user's profile without loading all their associated posts.

  * **Data Relationships:** Subcollections establish a clear one-to-many relationship between users and their posts.

**Why Other Options Are Less Ideal:**

  * **I. Opt for a single root collection for user profiles and another for user posts.** While workable, completely separate collections might make it harder to fetch a user's profile and posts together when needed.

  * **III. Implement a single root collection for user profiles, storing each user's posts as a nested list within their profile document.** This risks hitting the 1 MB document size limit in Firestore if users have many posts. It also hinders efficient querying for posts.

  * **IV. Create a root collection for user posts, with subcollections dedicated to each user's profile.** This structure prioritizes posts over users, which might not be optimal for a social media application where the user is the central entity.

---

## Question 46

*Domain 2: Building and Testing Applications*

**To troubleshoot the performance difference between your locally tested application and its deployed version on a Compute Engine instance with minimal adjustments, what approach is recommended?**

- [ ] II. Utilize Cloud Debugger snapshots to examine a specific moment in the application's execution.
- [ ] IV. Integrate logging commands into the application and use Cloud Logging to identify areas of latency.
- [x] III. Leverage Cloud Profiler to identify the functions within the application that consume the most time.
- [ ] I. File a ticket with Cloud Support to report the performance gap between local and deployed environments.

### Explanation

The recommended approach for troubleshooting the performance difference between a locally tested application and its deployed version on a Compute Engine instance with minimal adjustments is:

**III. Leverage Cloud Profiler to identify the functions within the application that consume the most time.**

Explanation:

  1. **Identifying Performance Bottlenecks** : Cloud Profiler is a powerful tool designed specifically for analyzing the performance of applications running on Google Cloud Platform. It provides detailed insights into which functions or methods within your application are consuming the most time, helping you identify performance bottlenecks.

  2. **Minimal Adjustments** : Cloud Profiler requires minimal adjustments to your application code or deployment configuration. Once enabled, it automatically profiles your application's performance without requiring significant modifications.

Options I, II, and IV are not the most suitable for this scenario:

I. Filing a ticket with Cloud Support may not be the most efficient or effective approach for troubleshooting performance differences, especially when there are dedicated tools available for performance analysis like Cloud Profiler. Support tickets are typically reserved for addressing technical issues or inquiries that cannot be resolved through self-service methods.

II. While Cloud Debugger can be useful for examining specific moments in the application's execution, it may not provide comprehensive insights into overall performance differences between the local and deployed environments. Cloud Debugger is more focused on debugging specific issues or errors rather than performance analysis.

IV. Integrating logging commands into the application and using Cloud Logging can help identify areas of latency, but it may not provide the detailed insights into performance bottlenecks that Cloud Profiler offers. Logging can be useful for capturing information about application behavior, but it may not be as effective for pinpointing specific performance issues within the codebase.

Therefore, leveraging Cloud Profiler to identify the functions within the application that consume the most time is the recommended approach for troubleshooting performance differences between a locally tested application and its deployed version on a Compute Engine instance with minimal 

**Reference:**

<https://cloud.google.com/profiler/docs/>

---

## Question 47

*Domain 2: Building and Testing Applications*

**As a developer within a large organization utilizing Git for source code management (SCM), you aim to align your team with Google-recommended best practices to enhance software delivery efficiency. Which SCM process should your team adopt?**

- [ ] III. Each developer creates a branch for their individual work, commits their changes to their branch, and merges their code into the main branch on a daily basis.
- [x] IV. Groups of developers create a feature branch from the main branch for their work, commit their changes to their branch, and merge their code into the main branch following approval from the change advisory board.
- [ ] II. Groups of developers copy the repository, commit their changes to their respective repositories, and merge their code into the main repository before each product release.
- [ ] I. Developers commit their code to the main branch before each product release, conduct testing, and initiate rollbacks if integration issues arise.

### Explanation

**Correct Option:**

  * **IV. Groups of developers create a feature branch from the main branch for their work, commit their changes to their branch, and merge their code into the main branch following approval from the change advisory board.**

**Justification:**

  * **Feature Branch Workflow:** This approach is the core of GitFlow (and similar branching strategies), a widely-adopted model that aligns with Google's best SCM practices. Feature branches promote collaboration while isolating changes, reducing the risk of conflicts and errors in the main branch.

  * **Change Approval:** Having a change advisory board ensures code quality and adherence to standards before integrating features into the main branch.

  * **Collaboration and Isolation:** This process fosters teamwork while keeping unreviewed code safely out of the main branch, aiding quality control.

**Why Other Options Are Not Ideal:**

  * **I. Developers commit their code to the main branch...**

    * **High Risk:** Directly committing to the main branch increases the likelihood of introducing errors and breaking the build.

  * **II. Groups of developers copy the repository...**

    * **Inefficient Merging:** Merging changes from separate repositories adds complexity and increases the risk of conflicts.

    * **Coordination Overhead:** Maintaining multiple repositories for a single project demands extra coordination.

  * **III. Each developer creates a branch...**

    * **Code Review:** Lacks a formal code review process, which could lead to quality issues slipping into the main branch.

---

## Question 48

*Domain 2: Building and Testing Applications*

**You’re preparing to load test a Cloud Run service using JMeter and need to orchestrate the process and tools for effective testing and analysis. You aim to follow Google’s recommended practices. What steps should you take?**

- [x] **D.** Set up a **Compute Engine** instance, install **JMeter** on the instance, create a log sink to **BigQuery** , and use **Looker Studio** for analysis.
- [ ] **A.** Install **JMeter** on your local machine, set up a log sink to **BigQuery** , and use **Looker** to analyze the test results.
- [ ] **C.** Set up a **Compute Engine** instance, install **JMeter** on the instance, create a log sink to a **Cloud Storage** bucket, and use **Looker** for analysis.
- [ ] **B.** Set up a **Compute Engine** instance, install **JMeter** on the instance, create a log sink to a **Cloud Storage** bucket, and use **Looker Studio** for analysis.

### Explanation

The correct answer is 

**D. Set up a Compute Engine instance, install JMeter on the instance, create a log sink to BigQuery, and use Looker Studio for analysis.**

Explanation:

Following Google’s recommended practices for load testing a **Cloud Run** service involves the following key steps:

  1. **Use a dedicated Compute Engine instance for JMeter** : Running JMeter on a Compute Engine instance allows you to scale your load tests independently of your local resources, ensuring consistent and high-performance load testing without impacting your local network or machine.

  2. **Create a log sink to BigQuery** : BigQuery is designed to handle large volumes of log data efficiently, making it ideal for storing and querying log data generated during load testing. Using BigQuery allows for detailed analysis, flexible querying, and seamless integration with other Google Cloud tools.

  3. **Use Looker Studio for analysis** : Looker Studio (formerly known as Data Studio) provides a powerful and user-friendly platform for visualizing BigQuery data. By connecting Looker Studio to BigQuery, you can create interactive reports and dashboards to analyze test results and gain insights into performance trends and bottlenecks.

**Justifications for Incorrect Options:**

  * **Option A: Install JMeter on your local machine, set up a log sink to BigQuery, and use Looker to analyze the test results**  
Running JMeter on a local machine is not recommended for load testing at scale. Using a Compute Engine instance provides more consistent resources and scalability. Additionally, Google recommends using **Looker Studio** rather than Looker for direct integration with BigQuery for reporting.

  * **Option B: Set up a Compute Engine instance, install JMeter, create a log sink to a Cloud Storage bucket, and use Looker Studio for analysis**  
Storing logs in **BigQuery** is preferred over Cloud Storage because BigQuery offers efficient querying and analysis capabilities, which are essential for analyzing large volumes of load test data.

  * **Option C: Set up a Compute Engine instance, install JMeter, create a log sink to Cloud Storage, and use Looker for analysis**  
This approach is incorrect due to both the use of **Cloud Storage** (instead of BigQuery) for logs and **Looker** (instead of Looker Studio) for analysis. BigQuery and Looker Studio are better suited for handling and visualizing large-scale load testing data.

---

## Question 49

*Domain 3: Configuring and Deploying Applications*

**In your Google Cloud project, you're defining system tests for an application hosted in Cloud Run. You need to establish a testing environment that's separate from the production environment. Your goal is to fully automate the creation of this testing environment with minimal effort and execute automated tests. What is the recommended approach?**

- [x] I. Utilize Cloud Build to execute Terraform scripts, thereby creating a new Google Cloud project and deploying a Cloud Run instance of your application within it.
- [ ] III. Utilize Cloud Build to execute gcloud commands, facilitating the creation of a new Google Cloud project and deploying a Cloud Run instance of your application within it.
- [ ] II. Employ Cloud Build to execute a Terraform script, deploying a new Cloud Run revision within the existing Google Cloud project. Implement traffic splitting to direct traffic to your test environment.
- [ ] IV. Employ Cloud Build to execute gcloud commands, deploying a new Cloud Run revision within the existing Google Cloud project. Implement traffic splitting to direct traffic to your test environment.

### Explanation

**Correct Option:**

  * **I. Utilize Cloud Build to execute Terraform scripts, thereby creating a new Google Cloud project and deploying a Cloud Run instance of your application within it.**

**Justification:**

  * **Isolation:** Creating a separate Google Cloud project establishes the strongest level of isolation, guaranteeing that production resources remain unaffected by your system tests.

  * **Automation:** Terraform enables infrastructure-as-code, allowing you to fully define your test environment's resources in a declarative way, ensuring consistency and easy replication.

  * **Cloud Build Integration:** Cloud Build seamlessly integrates with Terraform for executing your scripts, automating environment setup.

  * **Minimizing Production Impact:** Deploying your application in a separate project ensures your system tests won't affect your production environment's stability.

**Why Other Options Are Less Ideal:**

  * **II. Employ Cloud Build to execute a Terraform script, deploying a new Cloud Run revision...**

    * **Lack of Isolation:** Deploying a new revision within your production project still carries the risk of affecting the production environment if tests have unintended side effects.

  * **III. Utilize Cloud Build to execute gcloud commands...**

    * **Less Structured:** `gcloud` commands offer less declarative resource definition than Terraform, potentially making the test environment more difficult to replicate and prone to manual configuration errors.

  * **IV. Employ Cloud Build to execute gcloud commands, deploying a new Cloud Run revision...**

    * **Shares the challenges of options II and III, with less structured configuration and lesser isolation.**

**References:**

<https://cloud.google.com/docs/terraform/best-practices-for-terraform>

<https://cloud.google.com/docs/terraform/resource-management/managing-infrastructure-as-code>

---

## Question 50

*Domain 4: Integrating Applications with Google Cloud Services*

**To effectively manage a significant surge in traffic and ensure efficient scalability during the redesign of the audit event ingestion from the authentication service, currently sharing a Compute Engine virtual machine with the audit service, you plan to separate them into their own pools of Compute Engine VM instances and utilize Pub/Sub for event transmission. How should you configure the Pub/Sub topics and subscriptions?**

- [ ] C. Implement a single Pub/Sub topic and create a push subscription.
- [x] A. Establish a single Pub/Sub topic and set up a single pull subscription.
- [ ] B. Set up a single Pub/Sub topic and create a pull subscription for each instance of the audit service.
- [ ] E. Set up a Pub/Sub topic for each instance of the authentication service and create a push subscription for each topic.
- [ ] D. Create a Pub/Sub topic for each instance of the authentication service and set up a pull subscription for each topic.

### Explanation

**_A_ is correct. This is the most flexible way to scale, allowing the authentication and audit services to be sized independently according to load.**

B is incorrect. This will cause messages to be duplicated, one copy per subscription.  
C is incorrect. This will allow the system to scale, but push subscriptions are less suited to handle large volumes of messages.  
D is incorrect. This will allow the system to scale, however each audit service will listen to all subscriptions.  
E. is incorrect. This will allow the system to scale, however it will require each audit service to listen to all subscriptions. Also push subscriptions are less suited to handle large volumes of messages.

**Reference:**

[https://cloud.google.com/pubsub/docs/subscriber#push-subscription](%0d https:/cloud.google.com/pubsub/docs/subscriber#push-subscription)

---

## Question 51

*Domain 3: Configuring and Deploying Applications*

**What is the recommended method for deploying a microservice developed in C++ with custom software libraries for a Google Cloud-hosted application, ensuring minimal infrastructure management?**

- [ ] I. Utilize Cloud Functions for deploying the microservice.
- [x] II. Employ Cloud Build for container creation and deployment on Cloud Run.
- [ ] III. Utilize Cloud Shell for containerizing the microservice and deploy it on a Container-Optimized OS Compute Engine instance.
- [ ] IV. Leverage Cloud Shell for containerization and deployment on standard Google Kubernetes Engine.

### Explanation

**II. Employ Cloud Build for container creation and deployment on Cloud Run.**

**Explanation:**

  * **Cloud Run** is a fully managed serverless platform perfect for deploying stateless containerized applications. It handles scaling and infrastructure management for you.

  * **Cloud Build** is a service to streamline building and deploying containers. This aligns well for creating the container image of your C++ microservice.

**Why Other Options are Less Suitable:**

  * **I. Utilize Cloud Functions for deploying the microservice.** Cloud Functions are best for short-lived, event-driven tasks rather than continuously running microservices.

  * **III. Utilize Cloud Shell for containerizing the microservice and deploy it on a Container-Optimized OS Compute Engine instance.** While viable, it introduces more manual infrastructure management than Cloud Run, which defeats the purpose of minimizing overhead.

  * **IV. Leverage Cloud Shell for containerization and deployment on standard Google Kubernetes Engine.** Kubernetes is powerful but brings complexity. For a single microservice with minimal management preference, Cloud Run is simpler.

---

## Question 52

*Domain 2: Building and Testing Applications*

**In an application utilizing Cloud Spanner as its primary datastore, how can you prevent performance regressions by running automated performance tests for each commit made via Cloud Build, ensuring concurrent test execution for multiple commits?**

- [ ] IV. Initiate the Cloud Spanner emulator locally, load necessary data, and shut down the emulator after test execution.
- [ ] I. Generate a new project with a random name for every build, load necessary data, and delete the project post-test execution.
- [x] II. Establish a new Cloud Spanner instance for each build, load the requisite data, and delete the Cloud Spanner instance after testing.
- [ ] III. Set up a project with a Cloud Spanner instance containing the required data, and modify the Cloud Build build file to restore data to its initial state automatically post-test.

### Explanation

The **correct answer is:**

✅ **II. Establish a new Cloud Spanner instance for each build, load the requisite data, and delete the Cloud Spanner instance after testing.**

✅ **Explanation for Correct Option:**

**II. Create a new Cloud Spanner instance per build**

  * This approach ensures **isolation** between test runs from different commits.

  * It **avoids shared-state conflicts** , enables **parallel execution** , and provides a **realistic performance environment** , since you’re testing against **actual Cloud Spanner infrastructure**.

  * You can use **Cloud Build** to script instance creation, schema/data loading, testing, and teardown.

  * Although it incurs cost, it’s optimal for **realistic, scalable, and concurrent performance testing**.

**Official Documentation:**

  * Cloud Spanner performance testing guide: https://cloud.google.com/spanner/docs/performance

  * Cloud Build integration: https://cloud.google.com/build/docs/configuring-builds/run-bash-scripts

  * Instance creation via gcloud: https://cloud.google.com/spanner/docs/instances

❌ **Explanation for Incorrect Options:**

**I. Generate a new project per build**

  * **Creating a new GCP project for each build** is **time-consuming** , involves **org-level permissions** , and **slow resource provisioning**.

  * It is **not recommended** for fast, automated CI pipelines.

  * Project creation can also hit **quota limits** and requires IAM & billing setup.

**III. Reuse a single Spanner instance**

  * **Sharing a single Spanner instance** across builds may lead to **race conditions** and **non-deterministic test results**.

  * Resetting data between tests introduces complexity and increases chances of **state leakage or contention** , particularly with concurrent builds.

**IV. Use the Cloud Spanner emulator locally**

  * The **Spanner emulator does not simulate performance characteristics of the real service** (e.g., latency, transactions).

  * Good for functional unit tests, **but not suitable for performance benchmarking** or scalability tests.

**Reference:**  
https://cloud.google.com/spanner/docs/emulator

📌 **Best Practice:**  
Use **Cloud Build** to:

  1. **Create a new Cloud Spanner instance.**

  2. **Load schema and test data.**

  3. **Run performance tests.**

  4. **Delete the instance post-test.**

This ensures **concurrency, test isolation, and reliable performance metrics**.

---

## Question 53

*Domain 2: Building and Testing Applications*

**As you monitor a Go-based web application deployed on Google Kubernetes Engine, you notice an uptick in CPU and memory usage. How can you pinpoint the functions consuming the most CPU and memory resources?**

- [ ] III. Implement OpenTelemetry and Trace export packages within the application and set up the trace provider. Analyze latency data for the application on the Trace overview page to identify functions causing the most latency.
- [x] IV. Incorporate the Cloud Profiler package into the application and initialize the Profiler agent. Examine the generated flame graph in the Google Cloud console to identify functions with significant time consumption.
- [ ] I. Integrate print commands into the application's source code to log function calls, then redeploy the application.
- [ ] II. Develop a Cloud Logging query to collect the application's logs. Utilize a Python script to compute the duration between timestamps of the longest functions, aiding in identifying time-intensive functions.

### Explanation

**To pinpoint the functions consuming the most CPU and memory resources in a Go-based web application deployed on Google Kubernetes Engine, the most effective approach would be:**

**IV. Incorporate the Cloud Profiler package into the application and initialize the Profiler agent. Examine the generated flame graph in the Google Cloud console to identify functions with significant time consumption.**

**Here's why:**

  1. **Cloud Profiler** : Google Cloud Profiler is specifically designed for profiling applications running on Google Cloud Platform, including applications deployed on Google Kubernetes Engine. It collects CPU and memory allocation data with minimal overhead and provides detailed insights into the performance of the application.

  2. **Flame Graphs** : Cloud Profiler generates flame graphs, which are visual representations of stack traces showing where CPU time is being spent. This allows you to easily identify the functions and code paths that are consuming the most CPU and memory resources.

Option I is less suitable because manually adding print commands to the source code and redeploying the application can be time-consuming and may not provide detailed insights into CPU and memory usage.

Option II involves developing custom scripts to analyze application logs, which may not provide accurate or comprehensive data about CPU and memory usage compared to specialized profiling tools like Cloud Profiler.

Option III suggests using OpenTelemetry and Trace export packages, which are primarily focused on distributed tracing for monitoring application latency and performance. While tracing can provide valuable insights into the performance of distributed systems, it may not provide the detailed CPU and memory profiling needed to identify specific functions causing resource consumption.

**Therefore, option IV, incorporating the Cloud Profiler package into the application and examining the generated flame graph, is the most effective approach for pinpointing the functions consuming the most CPU and memory resources in the Go-based web application deployed on Google Kubernetes Engine.**

**References:**

[https://dev.to/billcchung/profiling-go-grpc-service-with-google-cloud-profiler-1k8l and https://www.cncf.io/blog/2020/03/27/continuous-profiling-go-application-running-in-kubernetes/](https://dev.to/billcchung/profiling-go-grpc-service-with-google-cloud-profiler-1k8l and   https://www.cncf.io/blog/2020/03/27/continuous-profiling-go-application-running-in-kubernetes/)

---

## Question 54

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**As you're finalizing the migration of an on-premises data center to Google Cloud, you encounter a web API on a server set for decommissioning. The goal is to modernize this API efficiently while transitioning to Google Cloud, ensuring it's written in Python 3.x, capable of autoscaling during peak traffic, facilitating rapid deployment of new versions due to frequent code changes, all while minimizing costs and operational overhead. Which solution is recommended?**

- [ ] I. Modernize and deploy the code on App Engine flexible environment.
- [x] II. Modernize and deploy the code on Cloud Run.
- [ ] IV. Advise the development team to rewrite the application to operate as a container on Google Kubernetes Engine.
- [ ] III. Deploy the modernized application to an n1-standard-1 Compute Engine instance.

### Explanation

**II. Modernize and deploy the code on Cloud Run.**

  * **Serverless:** Cloud Run is a fully managed serverless platform, eliminating the need to manage infrastructure and simplifying operations.

  * **Scaling:** Cloud Run scales automatically based on traffic, including scaling down to zero when not in use, optimizing costs.

  * **Container Support:** Cloud Run is ideal for containerized applications, which is likely how you'd package your modernized Python API.

  * **Rapid Deployment:** Cloud Run streamlines deployments, supporting frequent code updates.

**Why other options aren't as ideal:**

  * **I. Modernize and deploy the code on App Engine flexible environment.**

    * **Operational Overhead:** App Engine flexible, while supporting Python, still involves some management of virtual machine instances.

    * **Scaling:** App Engine flexible's scaling model might be less dynamic compared to Cloud Run's true "scale-to-zero" feature.

  * **III. Deploy the modernized application to an n1-standard-1 Compute Engine instance.**

    * **Management Burden:** This is the most traditional approach, requiring you to manage the VM, OS, and application updates.

    * **Scaling Limitations:** Manually scaling a single VM is less efficient than Cloud Run's automatic scaling.

  * **IV. Advise the development team to rewrite the application to operate as a container on Google Kubernetes Engine.**

    * **Unnecessary Complexity:** While GKE is powerful, it introduces a significant learning curve and operational complexity. Overkill for a simple modernized API unless you plan on having many services that would benefit from Kubernetes orchestration.

**Documentation:**

  * **Cloud Run:** <https://cloud.google.com/run>

  * **App Engine Flexible:** <https://cloud.google.com/appengine/docs/flexible>

  * **Google Kubernetes Engine (GKE):** <https://cloud.google.com/kubernetes-engine>

---

## Question 55

*Domain 2: Building and Testing Applications*

**How can you ensure that error messages from your Java application appear in the Error Reporting console on Cloud Run?**

- [ ] A. Confirm that the Java application includes the necessary Cloud Monitoring client libraries.
- [ ] D. Implement logging of exceptions using appropriate logging mechanisms rather than System.out.println.
- [x] C. Validate that application errors are being written to the standard error (stderr) stream.
- [ ] B. Ensure that the application logs are correctly directed to the appropriate regional storage bucket.

### Explanation

To ensure that error messages from your Java application appear in the Error Reporting console on Cloud Run, you should:

**C. Validate that application errors are being written to the standard error (stderr) stream.**

Explanation:

Cloud Run automatically captures logs from the standard output (stdout) and standard error (stderr) streams of your containerized application. When an application encounters an error, writing the error message to the stderr stream ensures that Cloud Run captures it and sends it to Cloud Logging. From there, errors can be analyzed and viewed in the Error Reporting console.

Option A, confirming that the Java application includes the necessary Cloud Monitoring client libraries, is not directly related to ensuring error messages appear in the Error Reporting console. While Cloud Monitoring can provide additional monitoring and alerting capabilities, Error Reporting primarily relies on logs captured in Cloud Logging.

Option B, ensuring that the application logs are correctly directed to the appropriate regional storage bucket, is not the recommended approach for Cloud Run. Cloud Run automatically manages logs and directs them to Cloud Logging, where they can be viewed and analyzed, including error messages.

Option D, implementing logging of exceptions using appropriate logging mechanisms rather than System.out.println, is good practice for improving logging clarity and maintainability. However, it does not guarantee that errors will appear in the Error Reporting console unless they are written to stderr.

Therefore, option C is the correct approach to ensure that error messages from your Java application appear in the Error Reporting console on Cloud Run.

**Documentation:**

  * **Error Reporting for Cloud Run** : <https://cloud.google.com/run/docs/error-reporting>

  * <https://cloud.google.com/error-reporting/docs/troubleshooting>

---

## Question 56

*Domain 4: Integrating Applications with Google Cloud Services*

**You're developing a web application on a Compute Engine instance that writes files to users' Google Drive accounts. To enable authentication with the Google Drive API, what should you do?**

- [x] I. Implement an OAuth Client ID with the https://www.googleapis.com/auth/drive.file scope to acquire an access token for each user.
- [ ] II. Configure an OAuth Client ID with delegated domain-wide authority.
- [ ] IV. Employ the App Engine service account with delegated domain-wide authority.
- [ ] III. Utilize the App Engine service account along with the https://www.googleapis.com/auth/drive.file scope to generate a signed JSON Web Token (JWT).

### Explanation

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

---

## Question 57

*Domain 3: Configuring and Deploying Applications*

**For an application deployed on Google Kubernetes Engine (GKE), how should you set up alerts to be notified when the average memory consumption of containers dips below 20% or exceeds 80%?**

- [ ] III. Create a scheduled Cloud Function to execute 'kubectl top' on all cluster workloads and send an email alert if the average memory consumption falls outside the specified bounds.
- [ ] IV. Design a script to gather memory consumption at the OS level and send an email alert if the average memory usage crosses the defined threshold.
- [ ] I. Develop a Cloud Function leveraging the Monitoring API. Schedule it to run hourly and alert you if the average memory consumption strays from the specified range.
- [x] II. Within Cloud Monitoring, establish an alerting policy to notify you of any deviations in average memory consumption from the designated range.

### Explanation

**The most suitable option:**

**II. Within Cloud Monitoring, establish an alerting policy to notify you of any deviations in average memory consumption from the designated range.**

**Explanation:**

  * **Native Integration:** Cloud Monitoring is tightly integrated with GKE, and designed specifically for metric-based alerting.

  * **Efficiency:** You avoid the overhead of custom code and don't need to reinvent the wheel. Cloud Monitoring does the tracking and alerting for you.

  * **Customization:** Alerting policies offer flexibility in notification channels and escalation configurations.

**Why Other Options Are Less Ideal:**

  * **I. Develop a Cloud Function leveraging the Monitoring API. Schedule it to run hourly and alert you if the average memory consumption strays from the specified range.** This is workable, but more complex than necessary. It introduces custom code and scheduling that Cloud Monitoring already handles.

  * **III. Create a scheduled Cloud Function to execute 'kubectl top' on all cluster workloads and send an email alert if the average memory consumption falls outside the specified bounds.** `kubectl top` is useful for spot checks, but not ideal for continuous monitoring. It's also less scalable than Cloud Monitoring's metrics collection.

  * **IV. Design a script to gather memory consumption at the OS level and send an email alert if the average memory usage crosses the defined threshold.** This approach focuses on OS-level metrics rather than container-level metrics, which are more relevant for GKE. It also adds the overhead of script development and management.

Reference:

<https://cloud.google.com/monitoring>

---

## Question 58

*Domain 3: Configuring and Deploying Applications*

You’ve deployed an application to Google Kubernetes Engine (GKE) where the Pods write data to a Compute Engine persistent disk. You’ve already created the PersistentVolume (PV) and PersistentVolumeClaim (PVC) objects and referenced the PVC in your Deployment manifest.

After expanding the persistent disk due to nearing full capacity, you log into one of the running Pods and notice that the increased disk space isn’t reflected inside the container’s file system.  
**What should you do to make the additional space available to the Pods?**

- [x] C. Modify the `spec.resources.requests.storage` field in the PersistentVolumeClaim (PVC) to match the new disk size and apply the change using `kubectl`.
- [ ] D. Use a tool like `fdisk` or `parted` inside the Pod to manually resize the partition to utilize the full disk.
- [ ] B. Restart the application by deleting and reapplying the Deployment using the commands:  
  `kubectl delete deployment DEPLOYMENT_NAME && kubectl apply -f deployment.yaml`.
- [ ] A. Update the `spec.capacity.storage` field in the PersistentVolume (PV) configuration to reflect the new disk size, then apply the changes using `kubectl`.

### Explanation

The correct answer is:  
**C. Modify the spec.resources.requests.storage field in the PersistentVolumeClaim (PVC) to match the new disk size and apply the change using kubectl.**

✅ **Explanation of the Correct Option:**

✅ Option C:

**"Modify the spec.resources.requests.storage field in the PersistentVolumeClaim (PVC) to match the new disk size and apply the change using kubectl."**

When you **resize a Compute Engine persistent disk** , GKE does **not automatically expand the file system inside the Pods**. To propagate the change, you must also update the associated **PersistentVolumeClaim (PVC)** with the new desired size.

  * Kubernetes supports **expanding PVCs** if the underlying StorageClass allows volume expansion (`allowVolumeExpansion: true`).

  * After expanding the PVC, **GKE will automatically resize the file system** when the Pod is restarted or rescheduled.

**Official Documentation:**

  * <https://cloud.google.com/kubernetes-engine/docs/concepts/storage-overview>

  * <https://kubernetes.io/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes>

❌ **Why Other Options Are Incorrect:**

❌ Option A:

**"Update the spec.capacity.storage field in the PersistentVolume (PV) configuration to reflect the new disk size."**

  * You **should never manually edit the PV object** to reflect storage changes.

  * PVs are usually **bound to PVCs** , and their capacity is **automatically managed** by Kubernetes based on the associated PVC.

  * Editing the PV directly can cause inconsistencies and is **not the supported method** for resizing volumes.

**Reference:**  
<https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolume>

❌ Option B:

**"Restart the application by deleting and reapplying the Deployment."**

  * Restarting the Deployment **does not trigger PVC resizing**.

  * If the PVC’s `requests.storage` field hasn't been updated, **the file system inside the Pod remains at the original size**.

❌ Option D:

**"Use a tool like fdisk or parted inside the Pod to manually resize the partition."**

  * This is **not recommended or supported** in GKE.

  * Kubernetes abstracts storage management, and manual partition changes **can lead to data corruption or unsupported states**.

✅ Summary:

To reflect the increased disk size in the Pod’s file system, update the **PVC’s storage request**.

📌 **Correct Action:**  
Edit the PVC and run: kubectl edit pvc YOUR_PVC_NAME

Then update:

spec:

resources:

requests:

storage: 100Gi # Update to new size

Kubernetes will handle the rest, especially if the StorageClass has `allowVolumeExpansion: true`.

---

## Question 59

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**In order to ensure global consistency and high availability for the point trading feature in your multi-player game, which database option should your company select for migrating from the current MySQL backend?**

- [ ] II. Cloud SQL
- [x] III. Google Cloud Spanner
- [ ] IV. Cloud Bigtable
- [ ] I. Google BigQuery

### Explanation

The best choice for your scenario is

**III. Google Cloud Spanner.** Here's why:

**Cloud Spanner's Strengths:**

  * **Global Consistency:** Spanner is specifically designed for globally distributed databases with strong consistency guarantees. This ensures that point balances for players are accurate and synchronized worldwide ([invalid URL removed]).

  * **High Availability:** Spanner maintains exceptional uptime (99.999%) even for multi-region deployments, crucial for minimizing disruptions in a multi-player game ([invalid URL removed]).

  * **Scalability:** Spanner seamlessly scales to handle fluctuations in game traffic and an increasing number of players.

  * **Relational Structure:** Since you're migrating from MySQL, Spanner's familiar relational structure and SQL-like interface ease migration.

**Why Other Options Are Less Ideal:**

  * **I. Google BigQuery:** While excellent for data analytics, it's not suited for highly transactional, consistent, global applications like your game. (<https://cloud.google.com/bigquery>)

  * **II. Cloud SQL:** Provides managed MySQL instances but lacks Spanner's global consistency and extreme uptime guarantees. (<https://cloud.google.com/sql>)

  * **IV. Cloud Bigtable:** Bigtable is a NoSQL wide-column store; its eventual consistency model might introduce discrepancies in point balances, and the different data model from MySQL complicates the migration. (<https://cloud.google.com/bigtable>)

---
