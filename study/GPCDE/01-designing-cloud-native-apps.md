# Domain 1 — Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications

63 questions. Answers are collapsed — try each question before expanding it.

## Questions

### Exam 1 · Q2

**Which storage solution would best fulfill the requirements of transferring log data to a Cloud Storage bucket daily, allowing authenticated users to review logs from the prior two weeks for critical events and enabling annual reviews by an external auditor while minimizing costs? Choose two options from the following:**

- IV. Establish a lifecycle management policy to transition the storage class to Coldline for objects older than 14 days.
- III. Generate a JSON Web Token (JWT) for users necessitating access to the Coldline storage buckets.
- V. Implement a lifecycle management policy to transition the storage class to Nearline for objects older than 14 days.
- I. Implement the Bucket Lock feature to enforce a retention policy on the data.
- II. Utilize a scheduled job to transition the storage class to Coldline for objects older than 14 days.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Establish a lifecycle management policy to transition the storage class to Coldline for objects older than 14 days. **|** I. Implement the Bucket Lock feature to enforce a retention policy on the data.

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

</details>

---

### Exam 1 · Q5

**How should you securely manage session and shopping cart data for your ecommerce platform while adhering to Google's recommended standards?**

- I. Utilize advanced techniques such as storing session and cart data in local memory and enabling cookie-based session affinity within a global external HTTP(S) load balancer, ensuring optimal performance and security.
- IV. Implement a comprehensive approach by utilizing Memorystore for Redis to securely store session data and Firestore for the shopping cart information, ensuring data integrity and scalability for your ecommerce platform.
- III. Opt for BigQuery as the storage solution for both session and shopping cart information, leveraging its scalability and analytical capabilities for robust data management.
- II. Employ Cloud Storage to store the shopping cart details, associating each cart with a unique session identifier, thus facilitating efficient retrieval and management of user data.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Implement a comprehensive approach by utilizing Memorystore for Redis to securely store session data and Firestore for the shopping cart information, ensuring data integrity and scalability for your ecommerce platform.

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

</details>

---

### Exam 1 · Q8

**Which actions should you take to configure object storage while ensuring compliance with regulatory requirements and optimizing storage cost? (choose two)**

- III. Utilize IAM Conditions to restrict read access to objects based on their creation date, which is included in the object's prefix name.
- I. Configure a retention policy on the bucket specifying a 7-year retention period.
- V. Develop a Cloud Function to evaluate the age of each object and transfer those older than 3 years to a second bucket configured with the Archive Storage class. Employ Cloud Scheduler to execute the Cloud Function daily.
- II. Implement an object lifecycle policy that automatically transitions objects from Standard Storage to Archive Storage after they have existed for 3 years.
- IV. Enable Object Versioning to safeguard against accidental deletions for 7 years after object creation.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Configure a retention policy on the bucket specifying a 7-year retention period. **|** II. Implement an object lifecycle policy that automatically transitions objects from Standard Storage to Archive Storage after they have existed for 3 years.

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

</details>

---

### Exam 1 · Q10

**You've been assigned to oversee the transfer of your company's on-premises application to Google Cloud. The application, serving as an ecommerce platform, will undergo a phased migration to microservices on Google Cloud. As the majority of your company's revenue comes from online sales, it's crucial to minimize risks during the transition. Your task is to prioritize features and select the initial functionality for migration. What's the optimal approach?**

- IV. Migrate the Shopping cart, integrating it with the frontend, cart database, inventory system, and payment processing platform.
- III. Move Order fulfillment, establishing connections with the order database, inventory system, and third-party shipping partner.
- II. Shift Payment processing, integrating it with the frontend, order database, and third-party payment provider.
- I. Transfer the Product catalog, ensuring seamless integration with the frontend and product database.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Transfer the Product catalog, ensuring seamless integration with the frontend and product database.

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

</details>

---

### Exam 1 · Q11

**Which Google Cloud service is the optimal choice for deploying your container while ensuring seamless migration from an on-premises Knative environment, maintaining your application's deployment strategy, and utilizing a fully managed service?**

- II. Google Compute Engine
- IV. Google App Engine Flexible Environment
- III. Google Kubernetes Engine
- I. Google Cloud Run

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Google Cloud Run

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

</details>

---

### Exam 1 · Q16

**To transition a monolithic application into a microservices model efficiently while minimizing business impact, which strategy should you pursue?**

- III. Refactor the monolithic application by integrating appropriate microservices in a single concerted effort and deploy it.
- IV. Develop a new application with the necessary microservices independently of the monolith and switch it upon completion.
- I. Deploy the application on Compute Engine and activate autoscaling.
- II. Gradually replace the application's functionalities with suitable microservices over several phases.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Gradually replace the application's functionalities with suitable microservices over several phases.

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

</details>

---

### Exam 1 · Q17

**For a mobile application aiming to store hierarchical data structures in a database, allowing offline syncing and scalability, while ensuring security, which combination of database and IAM role is most suitable?**

- III. Utilize Firestore in Native mode for its offline syncing capabilities, and assign the roles/datastore.user role to the service account for secure data handling.
- II. Employ Bigtable as the database solution, and assign the roles/bigtable.viewer role to the service account for enriched data processing.
- I. Opt for Cloud SQL as the database solution, and assign the roles/cloudsql.editor role to the service account for enriched data management.
- IV. Select Firestore in Datastore mode, and assign the roles/datastore.viewer role to the service account to facilitate secure and scalable data operations.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Utilize Firestore in Native mode for its offline syncing capabilities, and assign the roles/datastore.user role to the service account for secure data handling.

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

</details>

---

### Exam 1 · Q21

**In the development of a single-page web application with a user interface that interacts with a third-party API using XMLHttpRequest, prioritizing rendering performance is crucial. While the API data displayed on the UI is less critical than other data, delays in API calls should not impact the rendering of other UI elements. Efficient handling of API errors or timeouts is necessary. What's the optimal approach?**

- III. Implement error handling to capture timeout or error exceptions from the API call and retry with exponential backoff until a successful response is received.
- IV. Implement error handling to capture timeout or error exceptions from the API call and display the error response in the UI widget.
- I. Disable the asynchronous option for API requests and conceal the UI widget displaying API results upon encountering a timeout or error.
- II. Enable the asynchronous option for API requests and conceal the UI widget displaying API results upon encountering a timeout or error.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Enable the asynchronous option for API requests and conceal the UI widget displaying API results upon encountering a timeout or error.

**II. Enable the asynchronous option for API requests and conceal the UI widget displaying API results upon encountering a timeout or error.**

Here's why this approach offers the best trade-off between performance and user experience:

  * **Asynchronous for Performance:** Asynchronous API calls prevent blocking the main UI thread, ensuring the rest of your single-page application remains responsive and can render independently.

  * **User Experience:** Concealing the UI widget specifically for the API data provides a smooth user experience. It indicates that the data is being fetched while not disrupting other page elements.

  * **Error Handling:** While not the primary focus, basic error handling with concealment of the widget maintains a usable application state.

**Why Other Options Are Less Ideal**

  * **I. Disable the asynchronous option...** Synchronous API calls will block the main thread, degrading overall user experience and potentially causing the entire page to become unresponsive.

  * **III. Implement error handling to capture ...and retry...** Retry logic can be valuable, but blindly retrying too often can put unnecessary load on the third-party API and still frustrate users if the issue persists.

  * **IV. ...display the error response in the UI widget.** While informative for debugging, directly displaying raw error messages to users is generally not the best user experience. It's better to provide a more user-friendly indicator that something went wrong.

</details>

---

### Exam 1 · Q25

**You have authored a Cloud Function that interacts with other Google Cloud services. To ensure security following the principle of least privilege, what is the recommended approach?**

- III. Create a fresh service account with Editor permissions for accessing the resources. Give the deployer authorization to act as the new service account.
- IV. Generate a new service account with a custom IAM role tailored for accessing the resources. Provide the deployer authorization to act as the new service account.
- II. Set up a new service account with a custom IAM role crafted for accessing the resources. Grant the deployer authorization to obtain the access token.
- I. Establish a new service account with Editor permissions for accessing the resources. Provide the deployer authorization to acquire the access token.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Generate a new service account with a custom IAM role tailored for accessing the resources. Provide the deployer authorization to act as the new service account.

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

</details>

---

### Exam 1 · Q29

**You are developing a marquee stateless web application to run on Google Cloud. The incoming user traffic rate is expected to be unpredictable, with some days experiencing no traffic and others encountering large spikes. You need the application to automatically scale up and down while minimizing associated costs. What should you do?**

- I. Develop the application in Python with Firestore as the database. Deploy it to Cloud Run.
- IV. Develop the application in Python with Firestore as the database. Deploy it to a Compute Engine managed instance group with autoscaling.
- III. Develop the application in Python with CloudSQL as the database. Deploy it to the App Engine standard environment.
- II. Develop the application in C# with Firestore as the database. Deploy it to the App Engine flexible environment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Develop the application in Python with Firestore as the database. Deploy it to Cloud Run.

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

</details>

---

### Exam 1 · Q35

**Identify the reason for the non-linear scalability of Spanner performance during a load test for an ecommerce application that stores customer, order, and inventory data as relational tables within Cloud Spanner.**

- IV. Opting for the LIKE keyword over the STARTS_WITH keyword in parameterized SQL queries.
- II. Utilizing the STRING data type for arbitrary-precision values.
- I. Implementing 64-bit numeric types for 32-bit numbers.
- III. Employing Version 1 UUIDs as primary keys, leading to monotonically increasing values.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Employing Version 1 UUIDs as primary keys, leading to monotonically increasing values.

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

</details>

---

### Exam 1 · Q36

**Your team manages an application that aggregates news articles from various sources. The monitoring dashboard, which provides publicly accessible real-time reports, operates as a web application on a Compute Engine instance. External stakeholders and analysts require secure access to these reports without the need for authentication. How should you configure this secure channel?**

- IV. Employ an HTTP(S) load balancer in front of the monitoring dashboard and configure it with a Google-managed SSL certificate for encrypting traffic.
- II. Utilize Cloud Scheduler to trigger Cloud Build hourly, creating an export from the reports, and store them in a public Cloud Storage bucket.
- III. Implement an HTTP(S) load balancer in front of the monitoring dashboard and configure Identity-Aware Proxy to secure the communication channel.
- I. Assign a public IP address to the instance and employ the service account key of the instance to encrypt traffic.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Employ an HTTP(S) load balancer in front of the monitoring dashboard and configure it with a Google-managed SSL certificate for encrypting traffic.

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

</details>

---

### Exam 1 · Q54

**In developing an application to handle sensitive unstructured data objects stored in a Cloud Storage bucket, you must ensure compliance with regulatory mandates dictating that all data objects remain accessible for a minimum of 7 years from their inception. However, objects older than 3 years are rarely accessed. Your objective is to configure object storage while optimizing storage costs. What actions should you take? (Select two.)**

- II. Utilize IAM Conditions to grant access to objects based on a 7-year period following object creation.
- IV. Establish an object lifecycle policy on the bucket to transition objects from Standard Storage to Archive Storage after 3 years.
- III. Enable Object Versioning to safeguard objects against accidental deletion for 7 years after their creation.
- I. Implement a retention policy on the bucket with a duration of 7 years.
- V. Develop a Cloud Function to assess the age of each object in the bucket and relocate objects older than 3 years to a second bucket employing the Archive Storage class. Employ Cloud Scheduler to trigger the Cloud Function on a daily basis.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Establish an object lifecycle policy on the bucket to transition objects from Standard Storage to Archive Storage after 3 years. **|** I. Implement a retention policy on the bucket with a duration of 7 years.

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

</details>

---

### Exam 1 · Q60

**What is the optimal approach to develop and deploy a web application on Google Cloud, considering unpredictable traffic patterns and cost minimization?**

- B. Develop the application using Firestore as the database and deploy it to a Google Kubernetes Engine (GKE) Standard cluster, providing flexibility and scalability but potentially leading to higher operational costs compared to serverless options.
- C. Develop the application using Cloud SQL as the database and deploy it to a Google Kubernetes Engine Autopilot cluster, which automatically manages and scales the underlying infrastructure, optimizing costs while ensuring scalability.
- D. Develop the application using Firestore as the database and deploy it to a Compute Engine managed instance group with autoscaling, which offers scalability but may involve more operational overhead and potentially higher costs compared to serverless options like Cloud Run.
- A. Develop the application using Firestore as the database and deploy it to Cloud Run, which offers serverless scaling to handle varying traffic loads efficiently while minimizing costs.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Develop the application using Firestore as the database and deploy it to Cloud Run, which offers serverless scaling to handle varying traffic loads efficiently while minimizing costs.

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

</details>

---

### Exam 2 · Q12

**You're tasked with constructing an API for Android and iOS apps, with the following prerequisites:**

**HTTPS support is essential**

**Bandwidth usage should be minimized**

**Seamless integration with mobile apps is a priority**

**Which API architecture is the most appropriate choice for meeting these criteria?**

- III. gRPC-based APIs
- I. RESTful APIs
- IV. SOAP-based APIs
- II. MQTT for APIs

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. gRPC-based APIs

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

</details>

---

### Exam 2 · Q14

**In your Google Cloud-hosted application, you're utilizing a MySQL relational database schema with substantial read and write activity. This necessitates backups and ongoing capacity planning. While your team can handle minor administrative tasks, full database management is challenging. How should you deploy the database?**

- III. Configure Bigtable to host the database and import the data.
- I. Implement Cloud SQL for hosting the database, importing the schema accordingly.
- IV. Set up Cloud Spanner to host the database, importing the schema.
- V. Utilize Firestore for hosting the database, importing the data.
- II. Deploy MySQL from the Google Cloud Marketplace using a client and import the schema.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Implement Cloud SQL for hosting the database, importing the schema accordingly.

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

</details>

---

### Exam 2 · Q19

**Your company operates a data warehouse in BigQuery, storing 2 PBs of user data. With the expansion of your user base to include EU users, compliance requirements mandate:**

  * **User account information must be deletable upon user request.**

  * **EU user data must reside within a designated EU region.**

**Which two actions should you take to meet these requirements? (Choose two.)**

- IV. Utilize a Cloud Dataflow pipeline to re-upload data, filtering out user records based on region.
- I. Implement BigQuery federated queries to access data stored in Cloud Storage.
- III. Create a Cloud Storage bucket in the EU region to exclusively store data for EU users.
- V. Execute Data Manipulation Language (DML) statements within BigQuery to update or delete user records as per their requests.
- II. Establish a dataset in the EU region dedicated to storing information for EU users exclusively.

<details><summary>Answer &amp; explanation</summary>

**Correct:** V. Execute Data Manipulation Language (DML) statements within BigQuery to update or delete user records as per their requests. **|** II. Establish a dataset in the EU region dedicated to storing information for EU users exclusively.

* **II. Establish a dataset in the EU region dedicated to storing information for EU users exclusively.** This allows you to comply with data residency requirements by storing EU user data within the specified region.

  * **V. Execute Data Manipulation Language (DML) statements within BigQuery to update or delete user records as per their requests.** DML statements are necessary to fulfill user requests for data modification or deletion, ensuring compliance with privacy regulations.

**Why Other Options Are Not Ideal**

  * **I. Implement BigQuery federated queries to access data stored in Cloud Storage.** While federated queries can be useful, they don't directly address user deletion or data residency requirements.

  * **III. Create a Cloud Storage bucket in the EU region to exclusively store data for EU users.** Using a regional Cloud Storage bucket helps with data residency, but it doesn't intrinsically offer mechanisms for user data deletion. You would still need additional processes in place.

  * **IV. Utilize a Cloud Dataflow pipeline to re-upload data, filtering out user records based on region.** This could achieve compliance, but is likely more complex than necessary. Modifying or deleting data in BigQuery directly is likely to be more efficient.

</details>

---

### Exam 2 · Q22

**As your development team refactors an existing monolithic application into a set of composable microservices, which design aspects should you prioritize for the new application? (Select two.)**

- V. Introduce a versioning scheme to accommodate future changes that might be incompatible with the current interface.
- II. Establish an API contract agreement between the microservice implementation and microservice caller.
- I. Craft the microservice code in the same programming language utilized by the microservice caller.
- IV. Ensure adequate instances of the microservice are running to meet performance requirements.
- III. Implement asynchronous communications between all microservice implementations and microservice callers.

<details><summary>Answer &amp; explanation</summary>

**Correct:** V. Introduce a versioning scheme to accommodate future changes that might be incompatible with the current interface. **|** II. Establish an API contract agreement between the microservice implementation and microservice caller.

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

</details>

---

### Exam 2 · Q23

**For deploying a new API with three distinct URL paths - /students, /teachers, and /classes - each invoking a different function in your code, what action should you take?**

- IV. Deploy three distinct Cloud Functions, each as a separate backend service, exposed via an HTTPS load balancer, and configure them to handle requests for /students, /teachers, and /classes, respectively.
- II. Establish three separate Cloud Functions, each directly exposed, to handle requests for /students, /teachers, and /classes.
- I. Deploy a single Cloud Function serving as a backend service, exposed via an HTTPS load balancer, and configure it to handle requests for all three URL paths.
- III. Create a single Cloud Function directly exposed to handle all incoming requests regardless of the URL path.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Deploy three distinct Cloud Functions, each as a separate backend service, exposed via an HTTPS load balancer, and configure them to handle requests for /students, /teachers, and /classes, respectively.

**IV. Deploy three distinct Cloud Functions, each as a separate backend service, exposed via an HTTPS load balancer, and configure them to handle requests for /students, /teachers, and /classes, respectively.**

Explanation:

Option IV is the most suitable approach for deploying a new API with three distinct URL paths (/students, /teachers, and /classes), each invoking a different function in your code. Here's why:

  * **Three distinct Cloud Functions** : Since each URL path (/students, /teachers, and /classes) invokes a different function in your code, deploying three separate Cloud Functions allows you to encapsulate the logic for each endpoint separately. This ensures better maintainability and scalability.

  * **Separate backend services** : By configuring each Cloud Function as a separate backend service, you can route requests to the appropriate function based on the URL path. This allows for clear separation of concerns and efficient handling of incoming requests.

  * **Exposed via an HTTPS load balancer** : Exposing the Cloud Functions via an HTTPS load balancer ensures that incoming requests are distributed evenly and efficiently across the backend services. It also provides HTTPS encryption and scalability features.

Options I, II, and III suggest deploying a single Cloud Function or fewer Cloud Functions to handle all incoming requests, which would not align with the requirement of having distinct functions for each URL path.

Therefore, option IV is the recommended action for deploying a new API with three distinct URL paths on Google Cloud Platform.

</details>

---

### Exam 2 · Q25

**You manage an application hosted on a Compute Engine instance and multiple backend services deployed in standalone Docker containers across Compute Engine instances managed by instance groups in different regions. To achieve loose coupling, you aim to call different service implementations based on the value of an HTTP header in the request. Which Google Cloud feature should you utilize to invoke the backend services?**

- II. Service Directory
- IV. Internal HTTP(S) Load Balancing
- I. Traffic Director
- III. Anthos Service Mesh

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Traffic Director

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

</details>

---

### Exam 2 · Q29

**As part of your role in an ecommerce company planning global expansion, you are tasked with selecting a SQL database and designing a schema capable of scaling with organizational growth. To store all customer transactions, you need to create a table ensuring uniqueness for both CustomerId and TransactionId. Which approach should you take?**

- II. Establish a Cloud SQL table with TransactionId and CustomerId set as primary keys, utilizing random strings (UUID) for TransactionId.
- III. Implement a Cloud Spanner table with TransactionId and CustomerId configured as primary keys, employing random strings (UUID) for TransactionId.
- I. Establish a Cloud SQL table with TransactionId and CustomerId set as primary keys, employing incremental numbers for TransactionId.
- IV. Implement a Cloud Spanner table with TransactionId and CustomerId configured as primary keys, utilizing incremental numbers for TransactionId.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Implement a Cloud Spanner table with TransactionId and CustomerId configured as primary keys, employing random strings (UUID) for TransactionId.

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

</details>

---

### Exam 2 · Q30

**You're structuring a schema for a Cloud Spanner customer database, aiming to incorporate a phone number array field in the customer table for efficient customer search by phone number. How should you design this schema?**

- I. Design a "Customers" table featuring an Array field to accommodate multiple phone numbers per customer.
- II. Create a "Customers" table along with a separate "Phones" table. Include a "CustomerId" field in the "Phones" table to associate phone numbers with customers.
- III. Set up a "Customers" table with an Array field to store phone numbers for each customer. Implement a secondary index on the Array field for efficient querying.
- IV. Establish a "Customers" parent table and a nested "Phones" child table. Interleave the "Phones" table into the "Customers" table and create an index on the phone number field in the "Phones" table for optimized search operations.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Establish a "Customers" parent table and a nested "Phones" child table. Interleave the "Phones" table into the "Customers" table and create an index on the phone number field in the "Phones" table for optimized search operations.

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

</details>

---

### Exam 2 · Q31

**You've recently developed a web application to daily transfer log data to a Cloud Storage bucket. Authenticated users will regularly review logs from the prior two weeks for critical events, while logs will be annually reviewed by an external auditor thereafter. Data retention is required for a minimum of 7 years. To propose a cost-effective storage solution meeting these needs,**

**what should you do? (Choose two.)**

- III. Generate a JSON Web Token (JWT) for users requiring access to the Coldline storage buckets.
- I. Apply the Bucket Lock feature to enforce a retention policy on the data.
- V. Configure a lifecycle management policy to transition objects older than 14 days to the Nearline storage class.
- IV. Establish a lifecycle management policy to transition objects older than 14 days to the Coldline storage class.
- II. Schedule a job to transition objects older than 14 days to the Coldline storage class.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Establish a lifecycle management policy to transition objects older than 14 days to the Coldline storage class. **|** II. Schedule a job to transition objects older than 14 days to the Coldline storage class.

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

</details>

---

### Exam 2 · Q33

**In your application, users can read and post comments on news articles, and you're configuring Firestore to manage this. How should you structure the schema to handle an unspecified number of comments and articles?**

- III. Store each comment as a document and include its key in an array property associated with the article.
- IV. Store each comment as a document and include its key in an array property within the user profile.
- II. Place each comment within an array property linked to the article.
- I. Save each comment under a subcollection related to the article.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Save each comment under a subcollection related to the article.

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

</details>

---

### Exam 2 · Q34

**You're tasked with constructing an API for Android and iOS apps, with the following prerequisites:**

**HTTPS support is essential**

**Bandwidth usage should be minimized**

**Seamless integration with mobile apps is a priority**

**Which API architecture is the most appropriate choice for meeting these criteria?**

- II. MQTT for APIs
- IV. SOAP-based APIs
- I. RESTful APIs
- III. gRPC-based APIs

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. gRPC-based APIs

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

</details>

---

### Exam 2 · Q36

**To expand its user base globally for a popular application, your company seeks to ensure 99.999% availability of the database while minimizing read latency for users worldwide. Which two actions should the company prioritize? (Select two.)**

- V. Create at least two Cloud Spanner instances in separate regions, each with a minimum of one node.
- III. Establish a cluster comprising a minimum of 3 Spanner nodes.
- VI. Develop a Cloud Dataflow pipeline for data replication across diverse databases.
- I. Deploy a multi-regional Cloud Spanner instance configured with "nam-asia-eur1".
- IV. Set up a cluster with at least 1 Spanner node.
- II. Implement a multi-regional Cloud Spanner instance with the "nam3" configuration.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Establish a cluster comprising a minimum of 3 Spanner nodes. **|** I. Deploy a multi-regional Cloud Spanner instance configured with "nam-asia-eur1".

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

</details>

---

### Exam 2 · Q38

**You are deploying your application on a Compute Engine instance, which needs to communicate with Cloud SQL. To ensure minimal access for the role assigned to the service account associated with the instance, following Google's best practices, what action should you take?**

- III. Assign the Cloud SQL Client role.
- II. Designate the Project Owner role.
- IV. Grant the Cloud SQL Editor role.
- I. Allocate the Project Editor role.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Assign the Cloud SQL Client role.

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

</details>

---

### Exam 2 · Q40

**Your existing application manages user state data in a single MySQL database. This data is intensely user-specific and intricately tied to user activity duration. However, maintaining and evolving the schema for diverse user requirements in the MySQL database is proving challenging. Which storage option is the optimal choice in this situation?**

- I. Cloud SQL
- IV. Cloud Datastore/Firestore
- III. Cloud Spanner
- II. Cloud Storage

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Cloud Datastore/Firestore

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

</details>

---

### Exam 2 · Q41

**In the process of auditing all deployed applications in Google Kubernetes Engine, your security team found that some applications transmit data within the cluster in plain text. How can you swiftly encrypt all application traffic, minimizing alterations to applications and ensuring Google support?**

- III. Establish Trusted Network ranges within the application, allowing traffic exclusively from these networks.
- IV. Employ an automated procedure to procure SSL Certificates for applications from Let's Encrypt and integrate them into the applications.
- II. Deploy Istio, activate proxy injection in the application namespace, and then implement mutual TLS (mTLS).
- I. Implement Network Policies to restrict traffic between applications.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Deploy Istio, activate proxy injection in the application namespace, and then implement mutual TLS (mTLS).

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

</details>

---

### Exam 2 · Q52

**Your application is managed by a managed instance group. You aim to distribute a large read-only dataset among all instances in the group. Your goal is to ensure swift instance startup and access to the dataset via the filesystem with minimal latency. Additionally, you seek to minimize the overall solution cost. What's the optimal approach?**

- II. Transfer the data to a Cloud Storage bucket and copy it to the boot disk of each instance using a startup script.
- I. Move the data to a Cloud Storage bucket and mount the bucket on the filesystem using Cloud Storage FUSE.
- III. Migrate the data to a Compute Engine persistent disk and attach the disk in read-only mode to multiple Compute Engine virtual machine instances.
- IV. Shift the data to a Compute Engine persistent disk, create a snapshot, produce multiple disks from the snapshot, and attach each disk to its respective instance.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Migrate the data to a Compute Engine persistent disk and attach the disk in read-only mode to multiple Compute Engine virtual machine instances.

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

</details>

---

### Exam 2 · Q55

**You are developing an internal application to facilitate organizing community events within your company. The application is deployed on a single Compute Engine instance. Your company utilizes Google Workspace (formerly G Suite), and you need to ensure that company employees can authenticate to the application from anywhere. What should you do?**

- IV. Assign a public IP address to your instance and enable internet traffic. Generate a random hash and create a subdomain containing this hash, pointing it to your instance. Share this DNS address with your company's employees.
- II. Set up an HTTP(S) load balancer in front of the instance and configure Identity-Aware Proxy (IAP). Customize the IAP settings to grant access to the website from your company's domain.
- III. Establish a VPN tunnel between your company network and your instance's VPC location on Google Cloud. Configure necessary firewall rules and routing information for both on-premises and Google Cloud networks.
- I. Provide a public IP address to your instance and restrict access using firewall rules, allowing only your company's proxy as the source IP address.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Set up an HTTP(S) load balancer in front of the instance and configure Identity-Aware Proxy (IAP). Customize the IAP settings to grant access to the website from your company's domain.

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

</details>

---

### Exam 2 · Q60

**Following a recent Google Kubernetes Engine (GKE) API outage caused by a zone failure, you aim to implement a highly available GKE architecture to reduce service interruptions for users during future zone failures. What action should you take?**

- III. Implement Multi-Zone clusters
- I. Implement Zonal clusters
- II. Implement Regional clusters
- IV. Implement GKE on-premises clusters

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Implement Regional clusters

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

</details>

---

### Exam 3 · Q1

**You are porting an existing Apache/MySQL/PHP application stack from a single machine to Google Kubernetes Engine. You need to determine how to containerize the application. Your approach should follow Google-recommended best practices for availability. Which containerization strategy should you adopt?**

- III. Deploy each component in an individual container and coordinate their startup using a script.
- I. Containerize each component in a separate container and integrate readiness and liveness probes.
- II. Package the entire application in a single container and utilize a process management tool to handle each component.
- IV. Consolidate the entire application into a single container, use a bash script as the entrypoint, and initiate each component as a background process.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Containerize each component in a separate container and integrate readiness and liveness probes.

**I. Containerize each component in a separate container and integrate readiness and liveness probes.**

Here's why this approach excels:

  * **Isolation:** Separating Apache, MySQL, and PHP into individual containers provides fault isolation. If one component crashes, it doesn't necessarily bring down the entire application.

  * **Scalability:** Individual components can be scaled independently based on their resource needs.

  * **Updates:** Changes to a component (like a PHP update) can be rolled out without redeploying the whole application.

  * **Health Checks:** Readiness and liveness probes let Kubernetes monitor the health of each container, restarting or replacing them if they fail, ensuring higher availability.

**Why Other Options Are Less Ideal:**

  * **II. Package the entire application in a single container ...** This approach violates containerization best practices. It reduces modularity, flexibility, and makes health management difficult.

  * **III. Deploy each component in an individual container and coordinate their startup using a script.** While better than a single container, managing a complex startup script within the container could introduce fragility. Kubernetes' built-in mechanisms are preferred.

  * **IV. Consolidate the entire application into a single container ... background process.** This has similar drawbacks to option II, limiting benefits of containerizing in the first place.

**Reference:**

<https://cloud.google.com/architecture/best-practices-for-building-containers#package_a_single_app_per_container>

</details>

---

### Exam 3 · Q2

**Your production application, written in Python, is deployed on Cloud Run. It necessitates reading and writing data stored in a Cloud Storage bucket within the same project. Adhering to the principle of least privilege, how should you grant access to your application?**

- III. Establish a user-managed service account with the Project Editor Identity and Access Management (IAM) role, granting extensive permissions across the project.
- IV. Utilize the default service account linked to the Cloud Run revision in production, potentially providing broader access than necessary.
- II. Establish a user-managed service account with the Storage Admin Identity and Access Management (IAM) role to provide broad access to Cloud Storage functionality.
- I. Establish a user-managed service account with a custom Identity and Access Management (IAM) role tailored to the specific permissions required.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Establish a user-managed service account with a custom Identity and Access Management (IAM) role tailored to the specific permissions required.

**I. Establish a user-managed service account with a custom Identity and Access Management (IAM) role tailored to the specific permissions required.**

Here's why:

  * **Principle of Least Privilege:** Granting only the minimum necessary permissions is fundamental to good security practices. If your application only needs to read and write to a specific bucket, you should create a custom IAM role that includes only those actions (e.g., `storage.objects.get`, `storage.objects.create`, etc.).

  * **Reduced Attack Surface:** Limiting the permissions of your service account minimizes the potential impact if those credentials are compromised.

**Why the other options are not ideal:**

  * **II. Storage Admin:** This role grants far too many permissions for your scenario. It allows full administrative control over all Cloud Storage resources within the project.

  * **III. Project Editor:** The Project Editor role is also extremely broad. It allows changes to resources across the entire project, far beyond what's required for your use case.

  * **IV. Default Service Account:** While convenient, the default service account often has broader permissions than strictly necessary, violating the principle of least privilege.

</details>

---

### Exam 3 · Q10

**To streamline developer access to individual Google Cloud projects for each development team in your company while adhering to Google's recommended best practices and optimizing efficiency, what action should you take?**

- II. Add the users directly to their respective projects, assign them the necessary roles, and provide them with the relevant Project Number.
- III. Establish groups, include the users in their corresponding groups, assign the appropriate roles to these groups, and then furnish the users with the relevant Project ID.
- I. Add the users directly to their respective projects, assign them the necessary roles, and provide them with the relevant Project ID.
- IV. Establish groups, include the users in their corresponding groups, assign the appropriate roles to these groups, and then furnish the users with the relevant Project Number.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Establish groups, include the users in their corresponding groups, assign the appropriate roles to these groups, and then furnish the users with the relevant Project ID.

**III. Establish groups, include the users in their corresponding groups, assign the appropriate roles to these groups, and then furnish the users with the relevant Project ID.**

Here's why this approach aligns with Google's best practices and is the most efficient:

  * **Centralized Management:** Using groups simplifies permission management. Adding and removing users from a group automatically updates their permissions across multiple projects.

  * **Role-Based Access Control (RBAC):** Assigning roles to groups adheres to the principle of least privilege, granting users only the necessary permissions to perform their tasks within specific projects.

  * **Scalability:** The group-based approach scales well as your organization and the number of projects grow.

  * **Clarity:** Providing users with the Project ID ensures they easily identify the project they need to access.

**Why other options are less optimal:**

  * **I & II. Individual Permissions:** Adding users and assigning roles at the individual project level becomes cumbersome to manage as the number of users and projects increases. It also makes tracking and auditing permissions difficult.

  * **II. Project Number:** While helpful, the Project Number alone doesn't provide context about the user's permissions within that project.

</details>

---

### Exam 3 · Q15

**Your company requires a database solution for storing customer purchase history, with the following demands:**

**I. Immediate customer access to their purchases post-submission.**

**II. Sorting purchases by multiple fields.**

**III. Simultaneous storage of diverse record formats.**

**Which of the following storage options best fits these requirements?**

- I. Firestore in Native mode
- IV. Firestore in Datastore mode utilizing a global query
- III. Cloud SQL employing a SQL SELECT statement
- II. Cloud Storage utilizing object reads

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Firestore in Native mode

The best storage option that fits the requirements is 

**I. Firestore in Native mode**. Here's why:

  * **I. Immediate customer access to their purchases post-submission:** Firestore provides real-time updates, allowing customers to see their purchase history immediately after a purchase is made.

  * **II. Sorting purchases by multiple fields:** Firestore supports compound queries, allowing you to sort purchases based on multiple fields (e.g., date, price, product category).

  * **III. Simultaneous storage of diverse record formats:** Firestore's flexible document structure allows you to store various data types within a single document, accommodating different record formats.

Let's look at why the other options are less suitable:

  * **II. Cloud Storage utilizing object reads:** Cloud Storage is suitable for storing large objects but lacks the real-time capabilities and querying flexibility needed for this use case.

  * **III. Cloud SQL employing a SQL SELECT statement:** Cloud SQL is a relational database that provides structured data storage and querying but might not be the most efficient for handling real-time updates and diverse data formats.

  * **IV. Firestore in Datastore mode utilizing a global query:** While Firestore in Datastore mode supports global queries, it is generally less performant than Native mode for common use cases like this one.

**In summary:** Firestore in Native mode provides the real-time updates, flexible querying, and diverse data format support needed to meet the requirements of storing and accessing customer purchase history effectively.

**Reference:**  
<https://cloud.google.com/datastore/docs/firestore-or-datastore>

</details>

---

### Exam 3 · Q17

**In designing a microservices architecture for a cloud and on-premises deployment, prioritizing scalability and managed services, what approach should you take?**

- IV. Establish a GKE cluster in the cloud and deploy open-source Kubernetes on-premises, utilizing an external load balancer service to distribute traffic between the two environments.
- II. Deploy a GKE cluster in each environment leveraging Anthos, while utilizing Cloud Run for Anthos to deploy the application to each cluster.
- I. Implement a multi-cluster deployment using open source Istio on multiple Google Kubernetes Engine (GKE) clusters managed by Anthos.
- III. Set up a GKE cluster in each environment through Anthos, employing Cloud Build to create a Deployment for the application in each cluster.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Deploy a GKE cluster in each environment leveraging Anthos, while utilizing Cloud Run for Anthos to deploy the application to each cluster.

**II. Deploy a GKE cluster in each environment leveraging Anthos, while utilizing Cloud Run for Anthos to deploy the application to each cluster.**

Here's why this approach shines:

  * **Consistency:** Anthos provides unified management for GKE clusters, offering a consistent deployment and operational experience across your hybrid cloud setup.

  * **Scalability & Serverless:** Cloud Run for Anthos seamlessly scales your microservices. Its serverless nature removes the burden of managing underlying infrastructure.

  * **Fully Managed:** Both GKE and Cloud Run are fully-managed Google Cloud services, minimizing operational overhead and letting you focus on application development.

  * **Microservices-Friendly:** Cloud Run's container-based model naturally aligns with microservice architectures.

**Why Other Options Have Shortcomings:**

  * **I. Istio Complexity:** While Istio offers advanced service mesh features, it adds operational complexity. For a focus on scalability and managed services, this might not be the optimal trade-off.

  * **III. Lack of Serverless:** Employing Cloud Build and GKE deployments leaves you managing infrastructure capacity, where Cloud Run's serverless aspect would be advantageous.

  * **IV. Heterogeneity & Load Balancing:** This approach introduces management inconsistencies between GKE and on-premises Kubernetes, plus the added overhead of managing a separate load balancing solution.

Ref:

<https://cloud.google.com/anthos/run/docs/deploy-application>

</details>

---

### Exam 3 · Q20

**In your company's BigQuery environment, the "Master" dataset stores employee travel and expense data, categorized by department. To ensure employees only access relevant departmental information, you seek to implement a streamlined security framework. What's the optimal approach?**

- I. Establish distinct datasets for each department, creating views with appropriate WHERE clauses in the "Master" dataset to filter records. Authorize these views to access records from the "Master" dataset, granting employees access to their respective departmental datasets.
- III. Create a "Master" dataset and develop individual views for each department within it. Grant employees access to the relevant departmental views.
- II. Set up separate datasets for each department and implement data pipelines to copy relevant data from the "Master" dataset to department-specific datasets. Grant employees access to these department-specific datasets.
- IV. Create a "Master" dataset and segregate data into separate tables for each department. Grant employees access to their department's specific table.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Create a "Master" dataset and develop individual views for each department within it. Grant employees access to the relevant departmental views.

**III. Create a "Master" dataset and develop individual views for each department within it. Grant employees access to the relevant departmental views.**

Let's break down why this approach offers the best balance of security, efficiency, and maintainability:

  * **Centralized Data:** Maintaining a single "Master" dataset ensures data consistency and simplifies updates.

  * **Fine-grained Access Control:** Views provide a secure mechanism to filter data based on department without duplication. Each view acts as a virtual table, exposing only the necessary subset of data.

  * **Efficiency:** Views don't replicate data, saving storage costs and avoiding the overhead of data synchronization.

  * **Maintainability:** Changes to the underlying data in the "Master" dataset will automatically propagate to the relevant departmental views without the need to update multiple separate datasets.

**Why Other Options Are Less Ideal:**

  * **I. Establish distinct datasets for each department ...** This approach introduces data duplication and increases storage costs. It also creates overhead in keeping these datasets synchronized with the "Master" dataset.

  * **II. Set up separate datasets for each department and implement data pipelines ...** Similar to option I, this approach leads to data redundancy and the added complexity of managing data pipelines.

  * **IV. Create a "Master" dataset and segregate data into separate tables for each department ...** While this avoids data duplication, it makes queries more complex since you'll likely need to use `UNION ALL` across multiple tables.

**Reference:**

<https://cloud.google.com/bigquery/docs/dataset-access-controls>

</details>

---

### Exam 3 · Q22

**How should you grant IAM permission to a serverless web application on Cloud Run for accessing images stored in a private Cloud Storage bucket, while adhering to Google's recommended security practices?**

- IV. Enable public access prevention for the specified bucket. Configure and update the Cloud Run service to utilize a user-managed service account. Assign the Storage Object Viewer IAM role to the service account.
- III. Implement signed URLs for the specified bucket. Configure and update the Cloud Run service to utilize a user-managed service account. Assign the Storage Object Viewer IAM role to the service account.
- I. Implement signed URLs for the specified bucket. Assign the Storage Object Viewer IAM role to the Compute Engine default service account.
- II. Enable public access prevention for the specified bucket. Assign the Storage Object Viewer IAM role to the Compute Engine default service account.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Enable public access prevention for the specified bucket. Configure and update the Cloud Run service to utilize a user-managed service account. Assign the Storage Object Viewer IAM role to the service account.

**Correct Option:**

  * **IV. Enable public access prevention for the specified bucket. Configure and update the Cloud Run service to utilize a user-managed service account. Assign the Storage Object Viewer IAM role to the service account.**

**Justification:**

  * **Principle of Least Privilege:** User-managed service accounts allow fine-grained access control targeted specifically towards your Cloud Run service. It avoids overly permissive access associated with the Compute Engine default service account.

  * **Security Best Practice:** Public access prevention ensures your bucket remains private, aligning with security recommendations. Signed URLs are unsuitable for frequent access, as they require constant regeneration.

  * **Isolation:** This method creates a dedicated identity for your Cloud Run service, aiding in auditing and minimizing potential impact should other services with wider permissions be compromised.

**Why Other Options Are Less Ideal:**

  * **I. Implement signed URLs for the specified bucket...**

    * **Management Overhead:** Signed URLs are great for temporary, granular access. However, frequent regeneration and management is cumbersome for a serverless web application expecting regular image access.

    * **Potential Security Concerns:** Signed URL structure leaks some information about bucket and object names.

  * **II. Enable public access prevention for the bucket...**

    * **Overly Broad Permissions:** The Compute Engine default service account often encompasses multiple services, granting more permissions than needed, violating the principle of least privilege.

  * **III. Implement signed URLs for the specified bucket...**

    * Has the same issues as option I with the overhead of signed URL management.

</details>

---

### Exam 3 · Q33

**In crafting a new API, your objective is to minimize storage costs and optimize image serving speed. Which architectural strategy is most appropriate?**

- II. Implement Compute Engine with Persistent Disk as the backend.
- IV. Deploy Cloud Content Delivery Network (CDN) with Cloud Storage as the backend.
- III. Employ Transfer Appliance with Cloud Filestore as the backend.
- I. Utilize App Engine with Cloud Storage as the backend.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Deploy Cloud Content Delivery Network (CDN) with Cloud Storage as the backend.

**IV. Deploy Cloud Content Delivery Network (CDN) with Cloud Storage as the backend.**

Explanation:

  * **Cost-Effectiveness:** Cloud Storage offers an economical solution for storing image files.

  * **Performance:** Cloud CDN leverages Google's global edge cache network, delivering images to users from locations closest to them, thereby significantly enhancing serving speed.

  * **Scalability:** Both Cloud Storage and Cloud CDN automatically scale to handle traffic surges, avoiding performance bottlenecks.

Why Other Options Are Less Ideal:

  * **I. Utilize App Engine with Cloud Storage as the backend.** App Engine is designed for serving application code. While it can technically serve images, using Cloud CDN is more optimized for image delivery.

  * **II. Implement Compute Engine with Persistent Disk as the backend.** This setup introduces management overhead. Compute Engines require provisioning and scaling, while Cloud Storage and CDN offer serverless scalability.

  * **III. Employ Transfer Appliance with Cloud Filestore as the backend.** These are generally used for large-scale data migrations or high-performance file workloads. The complexity and cost don't align well with a straightforward image-serving API.

</details>

---

### Exam 3 · Q44

**Your team is developing a backend application to handle the business logic for an interactive voice response (IVR) system supporting a payroll application. The IVR system exhibits the following technical attributes:**

**Each customer phone call is associated with a unique IVR session.**

**A separate persistent gRPC connection is established to the backend for each session.**

**Interruption of connections prompts the IVR system to establish new connections, causing slight latency for the call.**

**Analysis of current call data reveals:**

**Call duration spans from 1 to 30 minutes.**

**Calls are predominantly made during business hours.**

**Significant call surges occur around specific dates (e.g., paydays) or during major payroll changes.**

**To minimize cost, effort, and operational overhead, where should you deploy the backend appliction?**

- III. Cloud Functions
- IV. Cloud Run
- I. Compute Engine
- II. Google Kubernetes Engine cluster in Standard mode

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Cloud Run

**Given the technical attributes of the IVR system and the analysis of current call data, deploying the backend application on Cloud Run would be the most suitable option. Here's why:**

**IV. Cloud Run:**

  * Cloud Run is a fully managed serverless platform that allows you to run containerized applications without worrying about managing the underlying infrastructure.

  * Since each customer phone call is associated with a unique IVR session and a separate persistent gRPC connection is established for each session, Cloud Run's scalability and ability to handle concurrent requests make it an ideal choice.

  * Cloud Run automatically scales up or down based on incoming request traffic, allowing it to handle surges in call volume around specific dates or during major payroll changes without manual intervention.

  * Cloud Run is cost-effective because you only pay for the resources consumed during request processing, making it suitable for a system where calls may vary in duration and occur predominantly during business hours. It automatically scales to zero when there's no traffic, minimizing costs during periods of inactivity.

  * Cloud Run's ease of deployment and management reduces operational overhead, as it abstracts away infrastructure management tasks, allowing the team to focus on developing the business logic for the IVR system.

**Hence, deploying the backend application on Cloud Run would minimize cost, effort, and operational overhead while effectively handling the technical requirements and call patterns of the IVR system.**

**References:**

<https://cloud.google.com/run/docs/tutorials/secure-services#:~:text=The%20backend%20service%20is%20private,Google%20Cloud%20except%20where%20necessary.>

</details>

---

### Exam 3 · Q53

**You are developing a web application accessible over both HTTP and HTTPS, hosted on Compute Engine instances. Periodically, you'll require SSH access from your remote laptop to conduct maintenance on these instances. How should you configure the instances while ensuring compliance with Google-recommended best practices?**

- IV. Establish a backend with Compute Engine web server instances utilizing private IP addresses behind an HTTP(S) load balancer. Additionally, set up a bastion host with a public IP address and open firewall ports. Access the web instances via the bastion host.
- I. Deploy a backend with Compute Engine web server instances utilizing private IP addresses behind a TCP proxy load balancer.
- III. Implement the Cloud Identity-Aware Proxy API for SSH access. Then, configure the Compute Engine servers with private IP addresses behind an HTTP(s) load balancer for web traffic.
- II. Configure firewall rules to permit all incoming traffic to connect to the Compute Engine web servers, assigning each server a unique external IP address.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Implement the Cloud Identity-Aware Proxy API for SSH access. Then, configure the Compute Engine servers with private IP addresses behind an HTTP(s) load balancer for web traffic.

**III. Implement the Cloud Identity-Aware Proxy API for SSH access. Then, configure the Compute Engine servers with private IP addresses behind an HTTP(S) load balancer for web traffic.**

Let's break down why this is the most secure and streamlined option:

  * **Security:**

    * IAP provides strong authentication and access control for SSH, integrated with Google accounts, enabling fine-grained authorization and auditing.

    * Private IP addresses for Compute Engine instances minimize the attack surface by preventing direct access from the internet.

  * **Manageability:**

    * A single HTTP(S) load balancer handles both web traffic and SSH access (tunneled through IAP), simplifying your networking setup.

    * You avoid the overhead of managing bastion hosts or additional firewall rules.

  * **Google Best Practices:** This approach aligns with Google's strong recommendations around network security and access management.

**Why Other Options Are Less Ideal:**

  * **I. TCP Proxy Load Balancer:** This solution would work but is less secure than using IAP for managing SSH access specifically.

  * **II. Firewall Rules with Public IPs:** Exposing Compute Engine instances directly to the internet with wide firewall rules significantly increases the risk profile.

  * **IV. Bastion Host:** A bastion host adds an additional point of management and potential vulnerability and is less streamlined than the IAP-based approach.

**References:**

[https://cloud.google.com/compute/docs/connect/ssh-using-iap](https://cloud.google.com/compute/docs/connect/ssh-using-iap  https://medium.com/@larry_nguyen/use-identity-aware-proxy-iap-instead-of-bastion-host-to-connect-to-private-virtual-machines-in-9885bc7c12d  https://cloud.google.com/solutions/connecting-securely#storing_host_keys_by_enabling_guest_attributes)

[https://medium.com/@larry_nguyen/use-identity-aware-proxy-iap-instead-of-bastion-host-to-connect-to-private-virtual-machines-in-9885bc7c12dhttps://cloud.google.com/solutions/connecting-securely#storing_host_keys_by_enabling_guest_attributes](https://cloud.google.com/compute/docs/connect/ssh-using-iap  https://medium.com/@larry_nguyen/use-identity-aware-proxy-iap-instead-of-bastion-host-to-connect-to-private-virtual-machines-in-9885bc7c12d  https://cloud.google.com/solutions/connecting-securely#storing_host_keys_by_enabling_guest_attributes)

</details>

---

### Exam 3 · Q54

**In designing an application comprising multiple microservices, each with its RESTful API deployed as separate Kubernetes Services, ensuring minimal impact on API consumers during changes is paramount. Additionally, it's crucial to prevent disruptions to third-party systems upon new API releases. How should you configure the application's connection, adhering to Google's recommended best practices?**

- IV. Consolidate multiple versions within the same service and specify the API version in the POST request.
- II. Utilize a Service Discovery system to connect to the backend specified in the request.
- III. Implement multiple clusters and route requests to distinct versioned backends via DNS entries.
- I. Employ an Ingress that directs requests to the appropriate backend based on the API's URL.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Employ an Ingress that directs requests to the appropriate backend based on the API's URL.

**Correct Option:**

  * **I. Employ an Ingress that directs requests to the appropriate backend based on the API's URL.**

**Explanation:**

Using an Ingress aligns best with Google's recommendations and provides several advantages:

  * **Centralized Traffic Management:** An Ingress acts as a single entry point for your APIs, routing traffic based on URL paths or other rules. This simplifies management and allows you to control which backend services handle specific API versions.

  * **Versioning:** Ingress rules enable precise URL-based versioning (e.g., /api/v1/, /api/v2/). Users can continue accessing older versions while you introduce new ones.

  * **Flexibility:** Ingress controllers are highly configurable. You can implement load balancing, SSL/TLS termination, and other features at the Ingress level.

  * **Google Cloud Integration:** Ingress works seamlessly with Google Cloud's load balancing and networking services.

**Why Other Options Are Less Ideal:**

  * **II. Utilize a Service Discovery system to connect to the backend specified in the request.** While service discovery is essential in microservices, it's usually not directly exposed to clients to manage versioning.

  * **III. Implement multiple clusters and route requests to distinct versioned backends via DNS entries.** This is overly complex and expensive for API versioning alone. Multiple clusters are better suited for scenarios like isolating environments or scaling specific API versions independently.

  * **IV. Consolidate multiple versions within the same service and specify the API version in the POST request.** This approach violates RESTful principles and complicates API client development and maintainability.

**References:**

[https://cloud.google.com/kubernetes-engine/docs/concepts/ingress#deprecated_annotation https://cloud.google.com/kubernetes-engine/docs/concepts/ingress#features_of_https_load_balancing](https://cloud.google.com/kubernetes-engine/docs/concepts/ingress#deprecated_annotation   https://cloud.google.com/kubernetes-engine/docs/concepts/ingress#features_of_https_load_balancing)

</details>

---

### Exam 3 · Q59

**Your team is developing an ecommerce platform where users log in, add items to their shopping cart, and are automatically logged out after 30 minutes of inactivity. Upon logging back in, their shopping cart should be preserved. How should you store users' session and shopping cart information while adhering to Google-recommended best practices?**

- I. Save session data in Pub/Sub and shopping cart information in Cloud SQL.
- IV. Utilize Memorystore for Redis or Memorystore for Memcached for session data and Firestore for shopping cart information.
- III. Maintain both session and shopping cart information in a MySQL database deployed across multiple Compute Engine instances.
- II. Store shopping cart details in Cloud Storage files, with filenames as the SESSION ID.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Utilize Memorystore for Redis or Memorystore for Memcached for session data and Firestore for shopping cart information.

**IV. Utilize Memorystore for Redis or Memorystore for Memcached for session data and Firestore for shopping cart information.**

Here's why this combination is ideal:

  * **Session Management:** Memorystore (Redis or Memcached) is designed for fast, in-memory session storage. It offers automatic expiration (essential for your 30-minute inactivity logout).

  * **Shopping Cart Persistence:** Firestore's scalability and flexible data model make it suitable for storing shopping cart data that needs persistence beyond session expiry.

  * **Separation of Concerns:** Using separate stores for session data and shopping cart data aligns with the principle of separation of concerns, improving scalability and maintainability.

  * **Google Best Practices:** This approach leverages Google-recommended services specifically suited for these tasks.

**Why Other Options Are Less Ideal:**

  * **I. Pub/Sub & Cloud SQL:** Pub/Sub is primarily for event-driven messaging and Cloud SQL for relational data. They are not optimal for session or shopping cart data.

  * **II. Cloud Storage:** Storing session data in files adds overhead and lacks the in-memory performance of dedicated session stores. It's also not ideal for frequent updates to shopping cart data.

  * **III. MySQL on Compute Engine:** While MySQL can manage both, self-managing a database adds operational complexity compared to managed services like Memorystore and Firestore.

**Reference:**  
<https://cloud.google.com/memorystore/docs/redis/redis-overview>

</details>

---

### Exam 4 · Q4

**When migrating an on-premises container from Knative to Google Cloud without changing the application's deployment strategy and preferring a fully managed service, which Google Cloud service is the most suitable option for deploying your container?**

- IV. App Engine flexible environment
- I. Cloud Run
- II. Compute Engine
- III. Google Kubernetes Engine

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Cloud Run

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

</details>

---

### Exam 4 · Q12

**To create a Cloud Function in Project A that stores its output in a Cloud Storage bucket in Project B, while following the principle of least privilege, what is the recommended approach?**

- II. Create a Google service account in Project A. Assign this service account the roles/storage.objectCreator role on the storage bucket in Project B. Deploy the Cloud Function using the service account from Project A.
- III. Determine the default App Engine service account (PROJECT_ID@appspot.gserviceaccount.com) in Project A. Assign the default App Engine service account the roles/storage.objectCreator role on the storage bucket in Project B. Deploy the Cloud Function using the default App Engine service account in Project A.
- I. Create a Google service account in Project B. Assign this service account the roles/storage.objectCreator role on the storage bucket in Project B. Deploy the Cloud Function in Project A using the service account from Project B.
- IV. Determine the default App Engine service account (PROJECT_ID@appspot.gserviceaccount.com) in Project B. Assign the default App Engine service account the roles/storage.objectCreator role on the storage bucket in Project B. Deploy the Cloud Function using the default App Engine service account in Project A.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Create a Google service account in Project A. Assign this service account the roles/storage.objectCreator role on the storage bucket in Project B. Deploy the Cloud Function using the service account from Project A.

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

</details>

---

### Exam 4 · Q15

**Your team manages an application that aggregates news articles from various sources, with a real-time monitoring dashboard accessible to external stakeholders and analysts via a Compute Engine instance running a web application. These stakeholders require secure access to reports without authentication. How should you configure this secure channel?**

- II. Employ Cloud Scheduler to trigger Cloud Build hourly to produce an export from the reports, storing them in a publicly accessible Cloud Storage bucket.
- IV. Introduce an HTTP(S) load balancer in front of the monitoring dashboard and deploy a Google-managed SSL certificate on the load balancer for traffic encryption.
- III. Implement an HTTP(S) load balancer preceding the monitoring dashboard and configure Identity-Aware Proxy (IAP) to secure the communication channel.
- I. Utilize the service account key of the instance to encrypt the traffic.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Introduce an HTTP(S) load balancer in front of the monitoring dashboard and deploy a Google-managed SSL certificate on the load balancer for traffic encryption.

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

</details>

---

### Exam 4 · Q19

**To ensure a more even distribution of demand within the Cloud Bigtable cluster and generate human-readable row keys, what approach should you take?**

- A. Utilize serially generated integer values for row keys.
- B. Employ a subset of the MD5 hash of the row contents for row key generation.
- C. Concatenate multiple human-readable attributes for row key generation.
- D. Adopt UNIX epoch-styled timestamps represented in milliseconds for row key generation.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Concatenate multiple human-readable attributes for row key generation.

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

</details>

---

### Exam 4 · Q31

You are developing a mobile app for creating and managing **to-do lists** with the following requirements:

  * **Data storage and synchronization** across multiple mobile devices.

  * **Offline access** capability.

  * **Real-time updates** on each user’s device.

You need to select a database solution that minimizes operational effort. Which approach should you choose?

- D. Implement a SQLite database on each device and use a scheduled job to synchronize each device’s database with a copy stored in Cloud Storage.
- A. Set up a Cloud SQL for MySQL instance, design a data model for storing to-do information, and create indexes for frequently used queries.
- B. Set up a Bigtable instance, design the schema to avoid write hotspots, and use Bigtable change streams to capture data changes.
- C. Use Firestore as the database, enable offline persistence to cache data locally, and listen for document changes to update the app in real-time.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Use Firestore as the database, enable offline persistence to cache data locally, and listen for document changes to update the app in real-time.

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

</details>

---

### Exam 4 · Q34

**You are designing a Node.js-based mobile news feed application that will store data on Google Cloud. The database should provide zonal resiliency by default, low-latency responses, ACID compliance, optional middle-tier functionality, semi-structured data storage, and support for network-partition-tolerant and offline-mode client libraries. Which database should you choose?**

- D. Set up BigQuery and use the BigQuery REST API in the application.
- A. Set up Firestore and use the Firestore client library in the application.
- C. Set up Cloud SQL and use the Google Client Library for Cloud SQL in the application.
- B. Set up Bigtable and use the Bigtable client in the application.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Set up Firestore and use the Firestore client library in the application.

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

</details>

---

### Exam 4 · Q36

**In accordance with the principle of least privilege, which role should you assign to the service account linked to your application's instance, which communicates with Cloud SQL via Cloud SQL Auth Proxy on Google Kubernetes Engine?**

- II. Assign the Project Owner role.
- I. Assign the Project Editor role.
- III. Assign the Cloud SQL Client role.
- IV. Assign the Cloud SQL Editor role.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Assign the Cloud SQL Client role.

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

</details>

---

### Exam 4 · Q42

**Which approach should you take to quickly gather data points and suggest improvements to your Tech Lead for optimizing the performance and cost-effectiveness of the web application after migrating it to Google Cloud?**

- III. Migrate the database to Cloud SQL. Then import the data into Firestore in Native mode.
- II. Migrate the database to BigQuery. Then import the data into Firestore in Native mode.
- IV. Create a Compute Engine virtual machine instance in Google Cloud, and install PostgreSQL and MongoDB Server software. Migrate the database to the new PostgreSQL, and then migrate the data to MongoDB.
- I. Migrate the database to Cloud SQL. Then import the data into Cloud Storage.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Migrate the database to Cloud SQL. Then import the data into Firestore in Native mode.

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

</details>

---

### Exam 4 · Q45

**As a developer at a social media firm transitioning from MySQL to Firestore on Google Cloud to manage user profiles and posts, how should you structure the Firestore collections?**

- I. Opt for a single root collection for user profiles and another for user posts.
- IV. Create a root collection for user posts, with subcollections dedicated to each user's profile.
- II. Choose a single root collection for user profiles, and establish subcollections for each user's posts.
- III. Implement a single root collection for user profiles, storing each user's posts as a nested list within their profile document.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Choose a single root collection for user profiles, and establish subcollections for each user's posts.

**II. Choose a single root collection for user profiles, and establish subcollections for each user's posts.**

**Explanation:**

  * **Scalability:** Root-level collections scale better than large, nested documents. This accommodates potential growth in the number of users and their posts.

  * **Optimized Queries:** Separating user profiles and posts facilitates efficient queries. You can easily fetch a user's profile without loading all their associated posts.

  * **Data Relationships:** Subcollections establish a clear one-to-many relationship between users and their posts.

**Why Other Options Are Less Ideal:**

  * **I. Opt for a single root collection for user profiles and another for user posts.** While workable, completely separate collections might make it harder to fetch a user's profile and posts together when needed.

  * **III. Implement a single root collection for user profiles, storing each user's posts as a nested list within their profile document.** This risks hitting the 1 MB document size limit in Firestore if users have many posts. It also hinders efficient querying for posts.

  * **IV. Create a root collection for user posts, with subcollections dedicated to each user's profile.** This structure prioritizes posts over users, which might not be optimal for a social media application where the user is the central entity.

</details>

---

### Exam 4 · Q54

**As you're finalizing the migration of an on-premises data center to Google Cloud, you encounter a web API on a server set for decommissioning. The goal is to modernize this API efficiently while transitioning to Google Cloud, ensuring it's written in Python 3.x, capable of autoscaling during peak traffic, facilitating rapid deployment of new versions due to frequent code changes, all while minimizing costs and operational overhead. Which solution is recommended?**

- I. Modernize and deploy the code on App Engine flexible environment.
- II. Modernize and deploy the code on Cloud Run.
- IV. Advise the development team to rewrite the application to operate as a container on Google Kubernetes Engine.
- III. Deploy the modernized application to an n1-standard-1 Compute Engine instance.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Modernize and deploy the code on Cloud Run.

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

</details>

---

### Exam 4 · Q59

**In order to ensure global consistency and high availability for the point trading feature in your multi-player game, which database option should your company select for migrating from the current MySQL backend?**

- II. Cloud SQL
- III. Google Cloud Spanner
- IV. Cloud Bigtable
- I. Google BigQuery

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Google Cloud Spanner

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

</details>

---

### Exam 6 · Q1

**Your ecommerce application is rapidly gaining new users, resulting in performance issues caused by a high volume of requests to your backend API. This API, which your team maintains, connects to a Cloud SQL database that is currently overwhelmed, leading to high latency and frequent timeouts. You need to find a solution to optimize API performance and enhance the user experience.**

**What approach should you take?**

- A. Use Apigee to expose your API, integrate Memorystore for Redis to cache frequently requested data, and implement exponential backoff in the application to retry failed requests.
- B. Use Apigee to manage your API, apply rate limiting and access control policies in Apigee to regulate API traffic, and utilize Pub/Sub to queue requests and reduce database load.
- C. Expose your API through Cloud Load Balancing, place Cloud CDN in front of the load balancer to cache responses, and incorporate exponential backoff for retrying failed requests.
- D. Use Cloud Load Balancing to expose your API, increase the database instance memory to support more concurrent requests, and build a custom rate-limiting mechanism within your application code to control API traffic.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Use Apigee to expose your API, integrate Memorystore for Redis to cache frequently requested data, and implement exponential backoff in the application to retry failed requests.

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

</details>

---

### Exam 6 · Q4

**Your organization has users and groups set up in an external identity provider (IdP). You want to allow all employees to access the Google Cloud console through this IdP and personalize the sign-in experience by showing each user’s name and photo. What should you do?**

- A. Set up workforce identity federation with the external IdP, and configure attribute mapping to display user information.
- B. Create a service account for each employee using their name and photo, and grant each user permissions to impersonate their respective service accounts.
- C. Set up workload identity federation to obtain tokens from the external IdP, then use these tokens to enable access to the Google Cloud console.
- D. Create a Google group that includes all employees’ organization email addresses. Instruct users to use the same name, email, and password when registering and signing in.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Set up workforce identity federation with the external IdP, and configure attribute mapping to display user information.

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

</details>

---

### Exam 6 · Q5

**You are developing a new API to create requests on an asynchronous message service, which will be consumed by different services. You want to use a gRPC interface to expose the API and minimize infrastructure management overhead. How should you deploy the API?**

- A. Deploy the API to App Engine, create a Pub/Sub topic, and configure the API to publish messages to this topic.
- B. Deploy the API as a Cloud Run service, create a Pub/Sub topic, and configure the API to publish messages to this topic.
- C. Deploy the API to a GKE cluster, set up a Kafka cluster, and configure the API to send messages to this Kafka cluster.
- D. Deploy the API on a Compute Engine instance, set up a Kafka cluster, and configure the API to send messages to this Kafka cluster.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Deploy the API as a Cloud Run service, create a Pub/Sub topic, and configure the API to publish messages to this topic.

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

</details>

---

### Exam 6 · Q6

**You are preparing to deploy an application running on a Windows-based Compute Engine instance that connects to a Cloud SQL database. To establish this connection, you plan to use the Cloud SQL Auth Proxy while adhering to Google’s best practices and the principle of least privilege. You have already set up a custom service account.**

**What is your next step?**

- A. Create a custom role for the service account, granting only the cloudsql.instances.connect permission. Then, update the Cloud SQL Auth Proxy startup command with your instance connection name.
- B. Assign the roles/cloudsql.client role to the custom service account. Modify the Cloud SQL Auth Proxy startup command to include the --unix-socket option.
- C. Grant the custom service account the roles/cloudsql.editor role for broad permissions.
- D. Assign the roles/cloudsql.viewer role to the custom service account and adjust the Cloud SQL Auth Proxy command to specify your instance connection name.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Create a custom role for the service account, granting only the cloudsql.instances.connect permission. Then, update the Cloud SQL Auth Proxy startup command with your instance connection name.

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

</details>

---

### Exam 6 · Q8

**You work for an environmental agency in a large metropolitan area, developing a new platform to monitor air quality. Thousands of sensors will capture air quality data across the city, and you want each device to send and receive data payloads to a RESTful backend every minute using a curl command. The backend is hosted in a single cloud region with Premium Tier networking. Your goal is to connect the devices to the backend in a way that minimizes the average daily latency, specifically focusing on reducing Time to First Byte (TTFB).**

**What setup should you use?**

- A. 1. Host the air quality backend on Compute Engine VMs.  
  2\. Set up a weighted round-robin routing policy on Cloud DNS.  
  3\. Configure the devices to connect using this DNS setup.
- B. 1. Host the air quality backend on Compute Engine VMs.  
  2\. Create a round-robin routing policy on Cloud DNS for these VMs.  
  3\. Configure the devices to connect using this DNS configuration.
- C. 1. Run the air quality backend in a managed instance group.  
  2\. Set up an external passthrough Network Load Balancer linked to the managed instance group.  
  3\. Configure the devices to connect through the Network Load Balancer.
- D. 1. Run the air quality backend in a managed instance group.  
  2\. Set up an external Application Load Balancer and connect it to the managed instance group.  
  3\. Configure the devices to connect through the Application Load Balancer.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. 1. Run the air quality backend in a managed instance group.  

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

</details>

---

### Exam 6 · Q11

**Your team uses Bigtable as the backend database for your application. In the app profile, you observe that the Bigtable connection is set to single-cluster routing, with manual failover configured if the cluster becomes unavailable. You want to improve the application’s Bigtable connectivity to be more efficient and highly available.**

**What should you do?**

- A. Implement a Memcached layer so that queries are directed to the cache first, retrieving data from Bigtable only on a cache miss.
- B. Increase the connection pool size in the Bigtable client to allow more simultaneous connections.
- C. Set up a Dataflow template and use a Beam connector to stream data changes.
- D. Change the app profile to use multi-cluster routing for improved availability.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Change the app profile to use multi-cluster routing for improved availability.

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

</details>

---

### Exam 6 · Q15

**Your team is preparing to use AlloyDB as the database backend for a new application release. The application is hosted in a separate project and network from the AlloyDB instances. You need a secure way to connect the application to the AlloyDB instance while keeping both projects isolated. You also want to minimize additional setup steps and follow Google’s best practices.**

**How should you set up network connectivity for the database?**

- A. Create a Shared VPC and add both the application and AlloyDB projects as service projects to enable connectivity.
- B. Use the AlloyDB Auth Proxy and configure the application project’s firewall to allow traffic on port 5433.
- C. Generate a service account from the AlloyDB project, then use the JSON key file of this service account as the --credentials-file for connecting to AlloyDB.
- D. Request that the database team deploy AlloyDB databases within the same project and network as the application.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Create a Shared VPC and add both the application and AlloyDB projects as service projects to enable connectivity.

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

</details>

---

### Exam 6 · Q16

**You have a containerized service running on-premises, written in the current stable version of Python 3, and accessible only to users in the United States. This service experiences high traffic during the day and no traffic at night. You want to migrate this application to Google Cloud, track error logs using Error Reporting after migration, and keep costs and setup effort low.**

**What should you do?**

- A. Deploy the service on Cloud Run, and configure it to log errors to standard error.
- B. Deploy the service on Cloud Run, and set it up to stream errors to a Cloud Storage bucket.
- C. Deploy the service on a GKE Autopilot cluster, and configure it to log errors to standard error.
- D. Deploy the service on a GKE Autopilot cluster, and set it up to log errors to a Cloud Storage bucket.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Deploy the service on Cloud Run, and configure it to log errors to standard error.

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

</details>

---
