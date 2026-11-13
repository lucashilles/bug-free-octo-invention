# Professional Cloud Developer — Practice Exam 3

60 questions.

## Question 1

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You are porting an existing Apache/MySQL/PHP application stack from a single machine to Google Kubernetes Engine. You need to determine how to containerize the application. Your approach should follow Google-recommended best practices for availability. Which containerization strategy should you adopt?**

- [ ] III. Deploy each component in an individual container and coordinate their startup using a script.
- [x] I. Containerize each component in a separate container and integrate readiness and liveness probes.
- [ ] II. Package the entire application in a single container and utilize a process management tool to handle each component.
- [ ] IV. Consolidate the entire application into a single container, use a bash script as the entrypoint, and initiate each component as a background process.

### Explanation

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

---

## Question 2

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Your production application, written in Python, is deployed on Cloud Run. It necessitates reading and writing data stored in a Cloud Storage bucket within the same project. Adhering to the principle of least privilege, how should you grant access to your application?**

- [ ] III. Establish a user-managed service account with the Project Editor Identity and Access Management (IAM) role, granting extensive permissions across the project.
- [ ] IV. Utilize the default service account linked to the Cloud Run revision in production, potentially providing broader access than necessary.
- [ ] II. Establish a user-managed service account with the Storage Admin Identity and Access Management (IAM) role to provide broad access to Cloud Storage functionality.
- [x] I. Establish a user-managed service account with a custom Identity and Access Management (IAM) role tailored to the specific permissions required.

### Explanation

**I. Establish a user-managed service account with a custom Identity and Access Management (IAM) role tailored to the specific permissions required.**

Here's why:

  * **Principle of Least Privilege:** Granting only the minimum necessary permissions is fundamental to good security practices. If your application only needs to read and write to a specific bucket, you should create a custom IAM role that includes only those actions (e.g., `storage.objects.get`, `storage.objects.create`, etc.).

  * **Reduced Attack Surface:** Limiting the permissions of your service account minimizes the potential impact if those credentials are compromised.

**Why the other options are not ideal:**

  * **II. Storage Admin:** This role grants far too many permissions for your scenario. It allows full administrative control over all Cloud Storage resources within the project.

  * **III. Project Editor:** The Project Editor role is also extremely broad. It allows changes to resources across the entire project, far beyond what's required for your use case.

  * **IV. Default Service Account:** While convenient, the default service account often has broader permissions than strictly necessary, violating the principle of least privilege.

---

## Question 3

*Domain 3: Configuring and Deploying Applications*

**Before deploying your new application code to production, you aim to conduct testing across various user profiles. Despite the inherent risks, you intend to assess the new version with production users, controlling access based on their operating systems. If issues arise, you seek a swift rollback process. What's the recommended approach?**

- [ ] III. Opt for App Engine deployment, employing traffic splitting to direct specific user segments to the new version based on IP addresses.
- [ ] IV. Consider Compute Engine deployment, leveraging Traffic Director to guide specific user segments to the new version based on predefined weights.
- [x] II. Choose Google Kubernetes Engine with Anthos Service Mesh deployment, employing traffic splitting to route certain user segments to the new version based on the user-agent header.
- [ ] I. Opt for Cloud Run deployment, utilizing traffic splitting to direct specific user segments to the new version based on the revision tag.

### Explanation

**Correct Answer:**

  * **II. Choose Google Kubernetes Engine with Anthos Service Mesh deployment, employing traffic splitting to route certain user segments to the new version based on the user-agent header.**

**Justification:**

  * **Accurate User Targeting:** The user-agent header within HTTP requests reliably conveys the operating system of the user's device. Anthos Service Mesh (and other service meshes) can finely control traffic routing using these headers.

  * **Rollbacks and Granular Control:** Service meshes excel at swift rollbacks and granular adjustments to traffic distribution percentages. These attributes are well-suited for mitigating potential risks.

  * **Kubernetes as a Foundation:** GKE provides the ideal platform for managing service mesh deployments like Anthos.

**Why Other Options Are Less Optimal:**

  * **I. Opt for Cloud Run deployment, utilizing traffic splitting to direct specific user segments to the new version based on the revision tag.**

    * **Limitation:** While Cloud Run's traffic splitting is robust, it usually targets revisions rather than user-agent headers. This makes OS-based segmentation difficult.

  * **III. Opt for App Engine deployment, employing traffic splitting to direct specific user segments to the new version based on IP addresses.**

    * **Imprecise Targeting:** Relying on IP addresses for identifying operating systems is unreliable, as users on different OSes can share IP ranges.

  * **IV. Consider Compute Engine deployment, leveraging Traffic Director to guide specific user segments to the new version based on predefined weights**

    * **Added Complexity:** Though Traffic Director offers fine-grained control, it increases setup and management complexity compared to the Anthos Service Mesh solution built for this use case.

**References:**

<https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent>

---

## Question 4

*Domain 3: Configuring and Deploying Applications*

**As you develop an HTTP API on a Compute Engine virtual machine instance, it's crucial for multiple clients within the same Virtual Private Cloud (VPC) to access it. How can clients retrieve the service's IP address?**

- [ ] I. Reserve a static external IP address and assign it to an HTTP(S) load balancing service's forwarding rule. Clients should use this IP address for connection.
- [ ] IV. Ensure clients leverage Compute Engine internal DNS by accessing the instance name through the URL https://[API_NAME]/[API_VERSION]/.
- [x] III. Ensure clients leverage Compute Engine internal DNS by accessing the instance name through the URL https://[INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal/.
- [ ] II. Reserve a static external IP address and assign it to an HTTP(S) load balancing service's forwarding rule. Then, set up an A record in Cloud DNS. Clients should use the A record's name to connect.

### Explanation

**III. Ensure clients leverage Compute Engine internal DNS by accessing the instance name through the URL https://[INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal/.**

Here's why this is the most efficient and reliable approach for clients within the same VPC:

  * **Internal communication:** Compute Engine's internal DNS allows for direct communication between instances within a VPC, bypassing the need for external IP addresses.

  * **Simplicity:** This approach doesn't involve reserving external IP addresses, setting up load balancers, or managing extra DNS records.

  * **Cost-effectiveness:** Utilizing internal DNS typically incurs no additional charges, making it efficient and cost-effective.

  * **Dynamic Updates:** Even if the instance's internal IP address changes, the internal DNS record will automatically update, minimizing client-side changes.

**Why Other Options Are Less Ideal**

  * **I & II. Reserve a static external IP address ...** While functional, these options are overly complex for internal VPC communication. They introduce unnecessary components and potential additional costs.

  * **IV. ... using the URL https://[API_NAME]/[API_VERSION]/.** This URL structure doesn't directly provide the IP address. Without internal DNS, client-side configuration would be required to map `[API_NAME]` to the correct address.

Ref:

[https://cloud.google.com/compute/docs/internal-dns#access_by_internal_DNS](https://cloud.google.com/compute/docs/internal-dns#access_by_internal_DNS  https://cloud.google.com/compute/docs/internal-dns)

[https://cloud.google.com/compute/docs/internal-dns](https://cloud.google.com/compute/docs/internal-dns#access_by_internal_DNS  https://cloud.google.com/compute/docs/internal-dns)

---

## Question 5

*Domain 3: Configuring and Deploying Applications*

**You've deployed a Java application on Cloud Run, requiring access to a Cloud SQL-hosted database. To comply with regulations, the connection must use the Cloud SQL instance's internal IP address. How should you configure connectivity, following Google's best practices?**

- [ ] III. Adapt your application to use the Cloud SQL Java connector for connectivity.
- [ ] I. Set up your Cloud Run service with a Cloud SQL connection.
- [x] II. Configure your Cloud Run service to utilize a Serverless VPC Access connector.
- [ ] IV. Adjust your application to connect to a Cloud SQL Auth proxy instance.

### Explanation

**Correct Option: II. Configure your Cloud Run service to utilize a Serverless VPC Access connector.**

**Explanation:**

  * **Serverless VPC Access:** This is the recommended way to connect Cloud Run to Cloud SQL using private IP addresses. It establishes a secure tunnel within your VPC network.

  * **Security:** Private IP connectivity enhances security by preventing database exposure to the public internet.

  * **No code changes:** This method generally doesn't require any changes to your Java application code.

**Why other options are less ideal:**

  * **I. Cloud SQL connection:** While Cloud Run can connect to Cloud SQL, this usually uses public IP by default, not complying with the internal IP requirement.

  * **III. Cloud SQL Java connector:** The connector is necessary, but on its own, it won't solve the private IP access issue.

  * **IV. Cloud SQL Auth proxy:** The proxy is useful but adds an extra component. Serverless VPC Access is a more streamlined solution for private IP connections from Cloud Run.

**References:**

[https://cloud.google.com/storage/docs/encryption/using-customer-supplied-keys#rest-csek-download-object](https://cloud.google.com/storage/docs/encryption/using-customer-supplied-keys#rest-csek-download-object  https://cloud.google.com/storage/docs/encryption/customer-supplied-keys#response we)

[https://cloud.google.com/storage/docs/encryption/customer-supplied-keys#response we](https://cloud.google.com/storage/docs/encryption/using-customer-supplied-keys#rest-csek-download-object  https://cloud.google.com/storage/docs/encryption/customer-supplied-keys#response we)

---

## Question 6

*Domain 3: Configuring and Deploying Applications*

**As you support a business-critical application deployed on Cloud Run in production, the application reports HTTP 500 errors, impacting its usability. You aim to receive alerts when the error rate exceeds 15% of the requests within a specific time frame. What should be your approach?**

- [ ] I. Develop a Cloud Function utilizing the Cloud Monitoring API. Schedule this function with Cloud Scheduler to trigger daily, notifying you if errors surpass the defined threshold.
- [ ] IV. Implement a Cloud Function consuming the Cloud Monitoring API and schedule it with Cloud Composer to trigger daily, alerting you if errors surpass the set threshold.
- [ ] II. Access the Cloud Run page in the Google Cloud console, select the service from the services list, and utilize the Metrics tab to visualize error rates for the revision. Perform this check daily.
- [x] III. Establish an alerting policy within Cloud Monitoring to notify you if errors exceed the specified threshold.

### Explanation

**Correct Answer:**

  * **III. Establish an alerting policy within Cloud Monitoring to notify you if errors exceed the specified threshold.**

**Justification:**

  * **Purpose-Built:** Cloud Monitoring's alerting functionality is designed specifically for this type of scenario. You can define thresholds, conditions, and notification channels directly within the service.

  * **Real-Time:** Alerting policies continuously monitor your metrics and trigger notifications as soon as the error rate exceeds your defined threshold.

  * **Efficiency:** This eliminates the need to develop custom Cloud Functions, schedule jobs, or manually check metrics.

**Why Other Options Are Less Ideal:**

  * **I. Develop a Cloud Function utilizing the Cloud Monitoring API.**

    * **Unnecessary Complexity:** While feasible, developing a custom Cloud Function introduces more overhead compared to Cloud Monitoring's native alerting features.

    * **Delayed Alerts:** Utilizing Cloud Scheduler for daily checks means you won't receive timely notifications when issues arise.

  * **II. Access the Cloud Run page in the Google Cloud console ...**

    * **Manual Intervention:** This approach relies on manual checks, which isn't proactive or suitable for a production application where timely error detection is critical.

  * **IV. Implement a Cloud Function ...schedule it with Cloud Composer...**

    * **Overkill:** Cloud Composer is designed for complex workflows and data pipelines. Its use for simple error monitoring is over-engineered and adds unnecessary complexity.

**References:**

[https://cloud.google.com/run/docs/monitoring#custom-metrics https://cloud.google.com/run/docs/monitoring#add_alerts](https://cloud.google.com/run/docs/monitoring#custom-metrics   https://cloud.google.com/run/docs/monitoring#add_alerts  https://cloud.google.com/monitoring/alerts)

[https://cloud.google.com/monitoring/alerts](https://cloud.google.com/run/docs/monitoring#custom-metrics   https://cloud.google.com/run/docs/monitoring#add_alerts  https://cloud.google.com/monitoring/alerts)

---

## Question 7

*Domain 4: Integrating Applications with Google Cloud Services*

**In developing a Java Web Server, requiring interaction with Google Cloud services through the Google Cloud API on behalf of users, what workflow should be implemented for user authentication to the Google Cloud API?**

- [ ] II. Upon user arrival, request Google username and password. Forward these credentials in an HTTPS request to the Google Cloud authorization server to obtain an access token. Validate user credentials at the Google server, which returns an access token to the application for subsequent Google Cloud API calls.
- [ ] III. Redirect users to a Google Cloud consent screen on arrival, presenting requested permissions. Prompt users to sign in via SSO to their Google Account. After sign-in and consent, the application receives an authorization code from a Google server, stored in the browser's cookies. Authenticate to the Google Cloud API using this authorization code.
- [x] IV. Upon user arrival, redirect to a Google Cloud consent screen displaying requested permissions. Prompt users to sign in via SSO to their Google Account. Following sign-in and consent, the application receives an authorization code from a Google server. The application exchanges this code for an access token with another request to the Google server, subsequently used for Google Cloud API calls.
- [ ] I. Prompt users for their Google username and password upon arrival at the application. Store an SHA password hash in the application's database along with the username. Authenticate to the Google Cloud API using HTTPS requests, including the username and password hash in the Authorization request header.

### Explanation

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

---

## Question 8

*Domain 2: Building and Testing Applications*

**While leveraging Cloud Build for Docker image creation, you're tasked with integrating unit and integration tests into the build process. In the event of a failure, you aim for clear identification of the failing stage in the build history. What's the optimal strategy to achieve this?**

- [x] IV. Construct a Cloud Build build configuration file featuring distinct cloud builder steps for compiling and executing unit and integration tests.
- [ ] III. Develop a Cloud Build build configuration file to trigger a separate cloud build pipeline dedicated to unit and integration tests.
- [ ] I. Embed RUN commands within the Dockerfile to execute unit and integration tests.
- [ ] II. Craft a Cloud Build build configuration file with a unified build step for compiling unit and integration tests.

### Explanation

**IV. Construct a Cloud Build build configuration file featuring distinct cloud builder steps for compiling and executing unit and integration tests.**

Let's break down why it's the best choice:

  * **Granular Test Stages:** Separate build steps provide a clear demarcation between the unit and integration test stages, making it easier to pinpoint the specific source of a failure.

  * **Targeted Actions:** Each step can have its own dependencies, configuration, and commands tailored to the type of test being executed.

  * **Readable Build History:** The Cloud Build history will clearly display the success or failure status of each individual test stage.

  * **Flexibility:** You can easily add more test stages or modify the order without affecting the overall build.

**Why Other Options Are Less Ideal:**

  * **I. Embed RUN commands within the Dockerfile** Cluttering the Dockerfile compromises readability and can create maintenance challenges. Unit and integration tests should ideally be decoupled from the core image build process.

  * **II. Craft a Cloud Build build configuration file ... unified build step** This approach lumps the tests together, hindering your ability to pinpoint the root cause of a failure.

  * **III. Develop a Cloud Build build configuration file to trigger a separate cloud build pipeline ...** This adds unnecessary complexity and potential build time overhead due to managing separate pipelines.

Ref:

<https://cloud.google.com/build/docs/build-config-file-schema:>

---

## Question 9

*Domain 4: Integrating Applications with Google Cloud Services*

**You've recently developed an application and now need to access the Cloud Storage API from a Compute Engine instance without a public IP address. What's the best approach?**

- [x] IV. Enable Private Google Access
- [ ] III. Implement Shared VPC networks
- [ ] II. Utilize VPC Network Peering
- [ ] I. Opt for Carrier Peering

### Explanation

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

---

## Question 10

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**To streamline developer access to individual Google Cloud projects for each development team in your company while adhering to Google's recommended best practices and optimizing efficiency, what action should you take?**

- [ ] II. Add the users directly to their respective projects, assign them the necessary roles, and provide them with the relevant Project Number.
- [x] III. Establish groups, include the users in their corresponding groups, assign the appropriate roles to these groups, and then furnish the users with the relevant Project ID.
- [ ] I. Add the users directly to their respective projects, assign them the necessary roles, and provide them with the relevant Project ID.
- [ ] IV. Establish groups, include the users in their corresponding groups, assign the appropriate roles to these groups, and then furnish the users with the relevant Project Number.

### Explanation

**III. Establish groups, include the users in their corresponding groups, assign the appropriate roles to these groups, and then furnish the users with the relevant Project ID.**

Here's why this approach aligns with Google's best practices and is the most efficient:

  * **Centralized Management:** Using groups simplifies permission management. Adding and removing users from a group automatically updates their permissions across multiple projects.

  * **Role-Based Access Control (RBAC):** Assigning roles to groups adheres to the principle of least privilege, granting users only the necessary permissions to perform their tasks within specific projects.

  * **Scalability:** The group-based approach scales well as your organization and the number of projects grow.

  * **Clarity:** Providing users with the Project ID ensures they easily identify the project they need to access.

**Why other options are less optimal:**

  * **I & II. Individual Permissions:** Adding users and assigning roles at the individual project level becomes cumbersome to manage as the number of users and projects increases. It also makes tracking and auditing permissions difficult.

  * **II. Project Number:** While helpful, the Project Number alone doesn't provide context about the user's permissions within that project.

---

## Question 11

*Domain 2: Building and Testing Applications*

**In the context of developing an online gaming platform on Google Kubernetes Engine (GKE), where users are experiencing extended loading times for specific URL requests, what is the recommended approach to identify performance bottlenecks and pinpoint HTTP requests with significant latency?**

- [x] III. Integrate your microservices with the OpenTelemetry tracing package. Update application code to dispatch traces to Trace for thorough inspection and analysis. Generate an analysis report within Trace to evaluate user requests comprehensively.
- [ ] II. Enhance your microservices to log HTTP request methods and URL paths to STDOUT. Utilize the logs router to forward container logs to Cloud Logging. Implement filters within Cloud Logging to assess the latency of user requests across various methods and URL paths.
- [ ] IV. Deploy tcpdump on your GKE nodes and initiate it to capture network traffic over an extended duration for data collection. Subsequently, analyze the captured data files employing Wireshark to uncover the root cause of high latency.
- [ ] I. Configure GKE workload metrics through kubectl, directing all Pods to transmit metrics to Cloud Monitoring. Utilize Cloud Monitoring to craft a custom dashboard showcasing application metrics, facilitating the identification of performance bottlenecks within the GKE cluster.

### Explanation

**Correct Option: III. Integrate your microservices with the OpenTelemetry tracing package. Update application code to dispatch traces to Trace for thorough inspection and analysis. Generate an analysis report within Trace to evaluate user requests comprehensively.**

**Explanation:**

  * **Distributed Tracing:** OpenTelemetry is specifically designed for distributed tracing in microservices environments. It provides fine-grained visibility into request paths, timings, and potential bottlenecks across services.

  * **Cloud Trace Integration:** Trace is natively integrated with Google Cloud, offering a powerful visualization and analysis platform tailored for tracing data.

  * **Targeted Analysis:** Traces allow you to pinpoint slow parts of your system specifically related to user-facing HTTP requests, giving you the most relevant data.

**Why other options are less ideal:**

  * **I. GKE Workload Metrics:** While useful for general cluster health, these metrics are less granular for pinpointing latency at the individual HTTP request level.

  * **II. Log Analysis:** While logs can help, analyzing raw HTTP logs for latency is less efficient and provides less granular insights than distributed traces.

  * **IV. tcpdump:** Network packet analysis can be helpful but is very low-level. It is less efficient for quickly understanding bottlenecks within a complex microservices application.#

**Reference:**

<https://cloud.google.com/trace/docs/setup#when-to-instrument>

---

## Question 12

*Domain 3: Configuring and Deploying Applications*

**You are deploying a single website on App Engine, which must be accessible via the URL http://www.altostrat.com/. What steps should you take to achieve this?**

- [x] I. Verify domain ownership through Webmaster Central. Set up a DNS CNAME record directing to the App Engine canonical name ghs.googlehosted.com.
- [ ] III. Configure a mapping in dispatch.yaml to link the domain www.altostrat.com to your App Engine service. Set up a DNS CNAME record pointing to the App Engine canonical name ghs.googlehosted.com.
- [ ] II. Verify domain ownership via Webmaster Central. Configure an A record pointing to the singular global App Engine IP address.
- [ ] IV. Set up a mapping in dispatch.yaml to direct the domain www.altostrat.com to your App Engine service. Establish an A record pointing to the singular global App Engine IP address.

### Explanation

**I. Verify domain ownership through Webmaster Central. Set up a DNS CNAME record directing to the App Engine canonical name ghs.googlehosted.com.**

Explanation:

  * **Domain Verification:** Webmaster Central allows you to prove ownership of your domain, a prerequisite for configuring custom domains with App Engine.

  * **CNAME Record:** CNAME records create an alias. In this case, `www.altostrat.com` becomes an alias for your App Engine's `ghs.googlehosted.com` address.

  * **App Engine Configuration:** You also need to configure your App Engine project to recognize and serve `www.altostrat.com` (this is done within the Google Cloud Console, not `dispatch.yaml`).

**Why Other Options Are Incorrect:**

  * **II. ... Configure an A record pointing to the singular global App Engine IP address.** App Engine IP addresses can change, making A records unreliable for the long term. CNAMEs are more flexible.

  * **III & IV. Set up a mapping in dispatch.yaml ...** `dispatch.yaml` is primarily for routing requests _within_ your App Engine app, not for setting up the initial custom domain mapping. This step is done in the Cloud Console.

**Reference:**

<https://support.google.com/domains/answer/6009957?hl=en app.mydomain.com CNAME 1H ghs.googlehosted.com.>

---

## Question 13

*Domain 4: Integrating Applications with Google Cloud Services*

**In an ANSI-SQL compliant database, you have two tables with matching columns that require swift combination into a single table, eliminating duplicate rows from the result. What's the optimal approach?**

- [x] III. Leverage the UNION operator in SQL for table merging.
- [ ] I. Utilize the JOIN operator in SQL for table merging.
- [ ] II. Employ nested WITH statements for table combination.
- [ ] IV. Deploy the UNION ALL operator in SQL for table merging.

### Explanation

**III. Leverage the UNION operator in SQL for table merging.**

**Explanation:**

The `UNION` operator in SQL specifically addresses the goal of combining data from multiple tables while removing duplicates:

  * **Combination:** The `UNION` operator appends the results of one query below the results of another.

  * **Duplicate Removal:** `UNION` automatically eliminates any duplicate rows from the combined result set.

**Why Other Options Are Less Ideal:**

  * **I. Utilize the JOIN operator in SQL for table merging.** While `JOIN` is excellent for combining tables based on related columns, it doesn't inherently remove duplicates. You'd need additional clauses (`DISTINCT`) to achieve the same behavior as `UNION`.

  * **II. Employ nested WITH statements for table combination.** `WITH` statements (Common Table Expressions) are useful for simplifying complex queries but don't directly offer the functionality of `UNION` in this case.

  * **IV. Deploy the UNION ALL operator in SQL for table merging.** `UNION ALL` appends results like `UNION` but _retains_ duplicate rows. This does not satisfy the requirement of duplicate elimination.

---

## Question 14

*Domain 3: Configuring and Deploying Applications*

**Your team develops stateless services running on Google Kubernetes Engine (GKE). You need to deploy a new service accessible only by other services within the GKE cluster. This service must scale rapidly to meet fluctuating loads. What's the best approach?**

- [ ] I. Utilize a Vertical Pod Autoscaler to adjust container sizes and expose them through a ClusterIP Service.
- [x] III. Deploy a Horizontal Pod Autoscaler to scale the containers and expose them through a ClusterIP Service.
- [ ] IV. Deploy a Horizontal Pod Autoscaler to scale the containers and expose them through a NodePort Service.
- [ ] II. Implement a Vertical Pod Autoscaler to adjust container sizes and expose them through a NodePort Service.

### Explanation

**III. Deploy a Horizontal Pod Autoscaler to scale the containers and expose them through a ClusterIP Service.**

Let's break down why this is the ideal choice:

  * **Internal Access:** ClusterIP Services are designed for communication within the Kubernetes cluster, meeting your requirement of internal-only access.

  * **Scaling:** The Horizontal Pod Autoscaler (HPA) automatically adjusts the number of replicas of your pods based on metrics like CPU or memory usage, ensuring your service can handle varying loads.

  * **Statelessness:** HPAs are well-suited for stateless services, allowing you to scale replicas up and down without affecting data consistency or state.

**Why Other Options Are Less Ideal:**

  * **I & II. Vertical Pod Autoscaling:** VPAs adjust resource requests/limits for _individual pods_ , not their count. This is less suitable for rapidly scaling to meet fluctuating demand.

  * **II & IV. NodePort:** NodePort Services expose your service to external traffic, whereas your requirement is internal-only access.

References:  
<https://cloud.google.com/kubernetes-engine/docs/concepts/service>

---

## Question 15

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Your company requires a database solution for storing customer purchase history, with the following demands:**

**I. Immediate customer access to their purchases post-submission.**

**II. Sorting purchases by multiple fields.**

**III. Simultaneous storage of diverse record formats.**

**Which of the following storage options best fits these requirements?**

- [x] I. Firestore in Native mode
- [ ] IV. Firestore in Datastore mode utilizing a global query
- [ ] III. Cloud SQL employing a SQL SELECT statement
- [ ] II. Cloud Storage utilizing object reads

### Explanation

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

---

## Question 16

*Domain 2: Building and Testing Applications*

**In a distributed microservices architecture, you aim to assess the performance and system resource utilization of a Java-based microservice. What steps should you take?**

- [ ] IV. Utilize OpenCensus to instrument the service for measuring service latency, and subsequently, generate custom metrics in Cloud Monitoring.
- [x] I. Employ Cloud Profiler to instrument the service, enabling measurement of CPU utilization and method-level execution times.
- [ ] II. Utilize Debugger to instrument the service for error investigation purposes.
- [ ] III. Employ Cloud Trace to instrument the service, facilitating the measurement of request latency.

### Explanation

The correct answer for assessing the **performance** and **system resource utilization** of a Java-based microservice in a distributed architecture is

**Option I: Employ Cloud Profiler to instrument the service, enabling measurement of CPU utilization and method-level execution times**.

Why Option I is correct:

  * **Cloud Profiler** is specifically designed to assess **CPU utilization** , memory allocation, and method-level execution times. It continuously samples the application to identify performance bottlenecks and inefficient code paths, making it highly suitable for monitoring system resource utilization in your Java microservice.

Why other options are incorrect:

  * **Option II: Utilize Debugger for error investigation** :

    * Cloud Debugger is used to track down issues in the code without stopping the service. However, it focuses on debugging and inspecting code rather than performance assessment or system resource utilization. It doesn't provide insights into CPU or memory usage.

  * **Option III: Employ Cloud Trace to measure request latency** :

    * Cloud Trace is useful for tracking request latency across services, but it does not give detailed insights into resource utilization (e.g., CPU or memory). Its primary focus is on tracing the flow of requests and measuring how long it takes for services to respond, not on performance profiling.

  * **Option IV: Utilize OpenCensus to measure service latency and generate custom metrics** :

    * OpenCensus (now part of OpenTelemetry) is used for **distributed tracing** and **latency** monitoring, not directly for CPU or method-level performance analysis. While useful for tracking the flow of requests and generating metrics, it doesn’t provide deep insights into resource utilization like Cloud Profiler does.

In conclusion, **Cloud Profiler (Option I)** is the correct choice for your performance assessment and resource utilization needs.

**Reference:**

<https://cloud.google.com/profiler/docs>

---

## Question 17

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**In designing a microservices architecture for a cloud and on-premises deployment, prioritizing scalability and managed services, what approach should you take?**

- [ ] IV. Establish a GKE cluster in the cloud and deploy open-source Kubernetes on-premises, utilizing an external load balancer service to distribute traffic between the two environments.
- [x] II. Deploy a GKE cluster in each environment leveraging Anthos, while utilizing Cloud Run for Anthos to deploy the application to each cluster.
- [ ] I. Implement a multi-cluster deployment using open source Istio on multiple Google Kubernetes Engine (GKE) clusters managed by Anthos.
- [ ] III. Set up a GKE cluster in each environment through Anthos, employing Cloud Build to create a Deployment for the application in each cluster.

### Explanation

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

---

## Question 18

*Domain 2: Building and Testing Applications*

**You're assessing developer tools to facilitate Google Kubernetes Engine adoption and integration within your development ecosystem, which encompasses VS Code and IntelliJ. What's the recommended approach?**

- [ ] IV. Utilize Cloud Shell for managing infrastructure and applications via the command line.
- [ ] III. Implement a Cloud Notebook instance for data ingestion, processing, and model deployment.
- [ ] II. Utilize the Cloud Shell integrated Code Editor for editing code and configuration files.
- [x] I. Employ Cloud Code for application development.

### Explanation

**I. Employ Cloud Code for application development.** Here's why this is the best choice, followed by explanations of why the other options aren't as suitable:

  * **Cloud Code: The Ideal Fit** Cloud Code is purpose-built to enhance the developer experience within Google Kubernetes Engine (GKE) environments. It offers extensions for popular IDEs like VS Code and IntelliJ, providing:

    * Kubernetes-aware coding assistance (e.g., code completion, snippets)

    * Easy debugging for applications running within the cluster

    * Deployment workflows from within the IDE

    * Integrated management of cluster resources

  * **Other Options: Their Limitations**

    * **II. Cloud Shell Integrated Code Editor:** The Cloud Shell code editor is better suited for quick edits and configuration file changes but lacks the depth and Kubernetes-specific features of Cloud Code for full-fledged application development.

    * **III. Cloud Notebook Instance:** Cloud Notebooks are designed primarily for data analysis and machine learning tasks. While they can be used in conjunction with GKE, they are not the primary tool for building and deploying applications onto Kubernetes.

    * **IV. Cloud Shell:** Cloud Shell is powerful for command-line interaction with GKE (using kubectl, etc.). However, it doesn't provide the rich IDE experience, extensions, and code assistance of Cloud Code.

**Reference:**

<https://cloud.google.com/code/docs>

---

## Question 19

*Domain 3: Configuring and Deploying Applications*

**You're preparing to transition a MySQL database to Google Cloud's managed Cloud SQL service. Your Compute Engine VM instances must connect to this Cloud SQL instance without requiring IP whitelisting. Which approach should you take?**

- [ ] III. Define a role within Cloud SQL granting external instance access to the database, then assign this role to the Compute Engine instances.
- [ ] IV. Deploy a CloudSQL instance in one project, create Compute Engine instances in another project, and establish a VPN connection between them for internal CloudSQL access.
- [ ] II. Include Compute Engine instances in a whitelisted project for Cloud SQL access.
- [x] I. Activate private IP for the Cloud SQL instance.

### Explanation

**I. Activate private IP for the Cloud SQL instance.**

**Explanation:**

  * **Efficiency and Security:** Private IP provides direct, internal connectivity between your Compute Engine instances and the Cloud SQL instance. This avoids the need for IP whitelisting, simplifies management, and enhances security.

**Why Other Options Are Less Ideal:**

  * **II. Include Compute Engine instances in a whitelisted project for Cloud SQL access.** While feasible, it relies on managing IP addresses and potential updates if your Compute Engine configuration changes. It's less streamlined than the private IP approach.

  * **III. Define a role within Cloud SQL granting external instance access to the database, then assign this role to the Compute Engine instances.** This works but exposes your Cloud SQL instance to the public internet via its public IP, increasing security risks.

  * **IV. Deploy a CloudSQL instance in one project, create Compute Engine instances in another project, and establish a VPN connection between them for internal CloudSQL access.** Establishing a VPN adds complexity, overhead, and potential performance bottlenecks compared to direct private IP connectivity.

**Reference:**

[https://shorturl.at/ryMUW](https://shorturl.at/ryMUW  https://cloud.google.com/sql/docs/mysql/roles-and-permissions#proxy-roles-permissions)

[https://cloud.google.com/sql/docs/mysql/roles-and-permissions#proxy-roles-permissions](https://shorturl.at/ryMUW  https://cloud.google.com/sql/docs/mysql/roles-and-permissions#proxy-roles-permissions)

---

## Question 20

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**In your company's BigQuery environment, the "Master" dataset stores employee travel and expense data, categorized by department. To ensure employees only access relevant departmental information, you seek to implement a streamlined security framework. What's the optimal approach?**

- [ ] I. Establish distinct datasets for each department, creating views with appropriate WHERE clauses in the "Master" dataset to filter records. Authorize these views to access records from the "Master" dataset, granting employees access to their respective departmental datasets.
- [x] III. Create a "Master" dataset and develop individual views for each department within it. Grant employees access to the relevant departmental views.
- [ ] II. Set up separate datasets for each department and implement data pipelines to copy relevant data from the "Master" dataset to department-specific datasets. Grant employees access to these department-specific datasets.
- [ ] IV. Create a "Master" dataset and segregate data into separate tables for each department. Grant employees access to their department's specific table.

### Explanation

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

---

## Question 21

*Domain 4: Integrating Applications with Google Cloud Services*

**In developing a new public-facing application, you're tasked with retrieving specific properties in the metadata of users' objects within their Cloud Storage buckets while adhering to privacy and data residency regulations, ensuring only metadata is retrieved, not object data. The goal is to optimize retrieval performance. How should you approach metadata retrieval?**

- [ ] I. Employ the patch method for metadata retrieval.
- [x] IV. Use the fields request parameter to retrieve only the desired metadata properties, enhancing retrieval performance.
- [ ] II. Utilize the compose method for efficient metadata extraction.
- [ ] III. Employ the copy method to retrieve metadata while preserving privacy and data residency requirements.

### Explanation

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

---

## Question 22

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**How should you grant IAM permission to a serverless web application on Cloud Run for accessing images stored in a private Cloud Storage bucket, while adhering to Google's recommended security practices?**

- [x] IV. Enable public access prevention for the specified bucket. Configure and update the Cloud Run service to utilize a user-managed service account. Assign the Storage Object Viewer IAM role to the service account.
- [ ] III. Implement signed URLs for the specified bucket. Configure and update the Cloud Run service to utilize a user-managed service account. Assign the Storage Object Viewer IAM role to the service account.
- [ ] I. Implement signed URLs for the specified bucket. Assign the Storage Object Viewer IAM role to the Compute Engine default service account.
- [ ] II. Enable public access prevention for the specified bucket. Assign the Storage Object Viewer IAM role to the Compute Engine default service account.

### Explanation

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

---

## Question 23

*Domain 3: Configuring and Deploying Applications*

**You seek to alert on-call engineers promptly about a service degradation in production, minimizing development time. Which option is the most efficient?**

- [x] IV. Employ Stackdriver Monitoring to monitor resources and generate alerts.
- [ ] II. Implement Cloud Pub/Sub to monitor resources and generate alerts.
- [ ] III. Utilize Stackdriver Error Reporting to capture errors and generate alerts.
- [ ] I. Utilize Cloud Function to monitor resources and generate alerts.

### Explanation

**IV. Employ Stackdriver Monitoring to monitor resources and generate alerts.**

Here's why:

  * **Purpose-Built:** Stackdriver Monitoring (now called Cloud Monitoring) is specifically designed for monitoring resources, metrics, and setting up alerting policies based on various conditions.

  * **Wide Range of Metrics:** It offers comprehensive coverage of infrastructure and application-level metrics, allowing you to pinpoint relevant indicators of service degradation (e.g., error rates, latency, resource utilization).

  * **Alerting Integration:** Stackdriver Monitoring seamlessly integrates with alerting mechanisms, allowing you to define thresholds and quickly notify on-call engineers.

  * **Minimizes Development Effort:** Using Stackdriver Monitoring requires minimal development time compared to building a custom solution.

**Why Other Options are Less Ideal:**

  * **I. Utilize Cloud Function to monitor resources...** While Cloud Functions can be used for this purpose, it involves more development overhead in fetching metrics, defining logic, and handling alerts.

  * **II. Implement Cloud Pub/Sub to monitor resources...** Cloud Pub/Sub is a messaging service. It would need to be integrated with other monitoring and alerting components, adding complexity.

  * **III. Utilize Stackdriver Error Reporting...** Error Reporting is primarily focused on error analysis rather than general resource monitoring and alerting.

**References:**

[https://cloud.google.com/solutions/serverless-web-performance-monitoring-using-cloud-functions](https://cloud.google.com/solutions/serverless-web-performance-monitoring-using-cloud-functions  https://cloud.google.com/error-reporting/docs/notifications  https://cloud.google.com/blog/products/gcp/drilling-down-into-stackdriver-service-monitoring)

[https://cloud.google.com/error-reporting/docs/notifications](https://cloud.google.com/solutions/serverless-web-performance-monitoring-using-cloud-functions  https://cloud.google.com/error-reporting/docs/notifications  https://cloud.google.com/blog/products/gcp/drilling-down-into-stackdriver-service-monitoring)

[https://cloud.google.com/blog/products/gcp/drilling-down-into-stackdriver-service-monitoring](https://cloud.google.com/solutions/serverless-web-performance-monitoring-using-cloud-functions  https://cloud.google.com/error-reporting/docs/notifications  https://cloud.google.com/blog/products/gcp/drilling-down-into-stackdriver-service-monitoring)

---

## Question 24

*Domain 3: Configuring and Deploying Applications*

**You've recently joined a new team managing a Cloud Spanner database instance in production. The manager tasks you with optimizing the Spanner instance to cut costs while maintaining top-notch reliability and availability. What's the recommended strategy?**

- [ ] I. Review error logs using Cloud Logging, gradually reducing Spanner processing units until reaching the minimum required capacity.
- [ ] II. Utilize Cloud Trace to monitor incoming requests' requests per second to Spanner, gradually decreasing Spanner processing units until identifying the minimum necessary capacity.
- [ ] IV. Utilize Snapshot Debugger to identify application errors, gradually decreasing Spanner processing units until finding the minimum required capacity.
- [x] III. Monitor CPU utilization with Cloud Monitoring, gradually reducing Spanner processing units until reaching the minimum required capacity.

### Explanation

**The recommended strategy for optimizing a Cloud Spanner database instance to cut costs while maintaining reliability and availability would be:**

**III. Monitor CPU utilization with Cloud Monitoring, gradually reducing Spanner processing units until reaching the minimum required capacity.**

**Explanation:**

  * **Cloud Monitoring provides comprehensive metrics for monitoring various aspects of Cloud Spanner, including CPU utilization.**

  * **By monitoring CPU utilization, you can determine the actual resource usage of the Spanner instance and make informed decisions about scaling down processing units.**

  * **Gradually reducing processing units based on CPU utilization allows for fine-tuning the capacity while ensuring that the database can handle the workload without compromising performance or availability.**

  * **This approach provides a data-driven method for optimizing costs while maintaining reliability and availability, as it directly correlates resource usage with the actual workload requirements.**

Options I, II, and IV are less suitable for optimizing Cloud Spanner in terms of cost reduction while maintaining reliability and availability:

  * Option I focuses on error logs, which may not directly reflect the resource usage and workload demands of the Spanner instance.

  * Option II suggests monitoring incoming requests per second, which may not accurately represent the resource utilization or workload patterns of the database.

  * Option IV involves using Snapshot Debugger to identify application errors, which is not directly related to optimizing the resource allocation of the Spanner instance.

---

## Question 25

*Domain 3: Configuring and Deploying Applications*

**Your application is deployed as a container within a Google Kubernetes Engine (GKE) cluster. You need to securely integrate a secret into your application. What should be your approach?**

- [ ] III. Safely store the credential in Cloud KMS. Create a Google service account (GSA) to access the credential from Cloud KMS. Export the GSA as a .json file and mount it into the container as a volume, enabling access to the credential from Cloud KMS.
- [ ] I. Create a Kubernetes Secret and inject it as an environment variable into the container.
- [x] IV. Securely store the credential in Secret Manager. Create a Google service account (GSA) to access the credential from Secret Manager. Establish a Kubernetes service account (KSA) to run the container. Utilize Workload Identity to configure your KSA to act as a GSA.
- [ ] II. Implement Application-layer Secret Encryption on the cluster using a Cloud Key Management Service (KMS) key.

### Explanation

**Correct Answer:**

  * **IV. Securely store the credential in Secret Manager. Create a Google service account (GSA) to access the credential from Secret Manager. Establish a Kubernetes service account (KSA) to run the container. Utilize Workload Identity to configure your KSA to act as a GSA.**

**Justification:**

  * **Secret Manager:** Secret Manager is designed specifically to store and manage sensitive data like credentials, offering stronger security than Kubernetes Secrets alone.

  * **Workload Identity:** This method avoids direct handling of service account keys, significantly reducing the risk of key exposure. Kubernetes pods authenticate to Cloud services like Secret Manager using their identity bound to the Kubernetes service account (KSA).

  * **Best Practice:** Google strongly advocates this approach due to its enhanced security posture.

**Why Other Options Are Less Ideal:**

  * **I. Create a Kubernetes Secret and inject it as an environment variable...**

    * **Security Concerns:** While convenient, Kubernetes Secrets are generally base64 encoded, not fully encrypted. They are more vulnerable if the cluster security is compromised.

  * **II. Implement Application-layer Secret Encryption...**

    * **Overhead:** This involves additional complexity, as you'd need to manage encryption/decryption within your application, potentially adding performance impact.

  * **III. Safely store the credential in Cloud KMS...**

    * **Key Handling:** Exporting service account keys as JSON files introduces potential exposure risks. Workload Identity offers a more secure authentication flow.

**References:**

[https://kubernetes.io/docs/concepts/configuration/secret/](https://kubernetes.io/docs/concepts/configuration/secret/  https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity   https://cloud.google.com/secret-manager/docs/overview)

[https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity https://cloud.google.com/secret-manager/docs/overview](https://kubernetes.io/docs/concepts/configuration/secret/  https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity   https://cloud.google.com/secret-manager/docs/overview)

---

## Question 26

*Domain 3: Configuring and Deploying Applications*

**You aim to create**`**fully baked**`**or**`**golden**`**Compute Engine images for your application. Your objective is to configure your application to connect to the correct database depending on the environment (test, staging, production). What's the best approach?**

- [ ] III. During Compute Engine instance creation, set up a metadata item with a key named `**DATABASE**` and specify a value for the appropriate database connection string. In your application, read the `**DATABASE**` environment variable and use its value to connect to the suitable database.
- [ ] II. During Compute Engine instance creation, assign a tag with the database name to be connected. In your application, retrieve the tags for the current instance via the Compute Engine API, and utilize the tag to construct the appropriate database connection string.
- [ ] I. Embed the relevant database connection string in the image and generate a distinct image for each environment.
- [x] IV. During Compute Engine instance creation, configure a metadata item with a key named `**DATABASE**` and specify a value for the appropriate database connection string. In your application, query the metadata server for the `**DATABASE**` value and use it to connect to the suitable database.

### Explanation

**IV. During Compute Engine instance creation, configure a metadata item with a key named DATABASE and specify a value for the appropriate database connection string. In your application, query the metadata server for the DATABASE value and use it to connect to the suitable database.**

Here's why this approach excels:

  * **Flexibility:** Metadata provides a dynamic way to pass environment-specific configuration to your application during instance creation. This avoids building separate images for each environment.

  * **Maintainability:** A single image can be used across all environments, simplifying image management and updates.

  * **Security:** Sensitive database connection strings are not embedded directly within the image, improving security posture.

  * **Standard Practice:** Utilizing metadata is a common and recommended way to configure Compute Engine instances.

**Why Other Options Are Less Ideal:**

  * **I. Embedding Connection Strings:** Hardcoding database connection strings into images creates multiple images, hindering maintainability and security.

  * **II. Using Instance Tags:** While tags can be useful for classification, they are less optimal for storing sensitive information like database connection strings.

  * **III. Environment Variables:** Compute Engine doesn't have a built-in mechanism to set environment variables during instance creation like metadata does.

**References:**

[https://cloud.google.com/compute/docs/metadata/querying-metadata](https://cloud.google.com/compute/docs/metadata/querying-metadata  https://cloud.google.com/compute/docs/metadata/overview)

[https://cloud.google.com/compute/docs/metadata/overview](https://cloud.google.com/compute/docs/metadata/querying-metadata  https://cloud.google.com/compute/docs/metadata/overview)

---

## Question 27

*Domain 4: Integrating Applications with Google Cloud Services*

**In Google Kubernetes Engine (GKE), you aim to update your application for authorized requests to Google Cloud managed services, ensuring a one-time setup while adhering to security best practices for auto-rotating security keys stored in an encrypted manner. Given that you've already configured a service account with the necessary access to Google Cloud services, what should be your next step?**

- [ ] III. Embed the exported Google Cloud service account directly into the application's source code.
- [ ] IV. Upload the exported Google Cloud service account to HashiCorp Vault to generate a dynamic service account for your application.
- [x] I. Implement Workload Identity to associate the Google Cloud service account with your GKE Pod.
- [ ] II. Export the Google Cloud service account and provide it to the Pod as a Kubernetes Secret.

### Explanation

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

---

## Question 28

*Domain 4: Integrating Applications with Google Cloud Services*

**While developing a new application deployed on Cloud Run and leveraging Cloud Functions, managing ENV variables for interservice communication has become challenging with each feature deployment. Seeking a scalable solution, how should you implement dynamic discovery?**

- [ ] III. Adopt a well-documented naming convention to rename Cloud Functions and Cloud Run services endpoints.
- [x] II. Establish a Service Directory namespace, utilizing API calls to register services during deployment and query them at runtime.
- [ ] I. Configure your microservices to utilize the Cloud Run Admin and Cloud Functions APIs for querying deployed services within the Google Cloud project.
- [ ] IV. Deploy HashiCorp Consul on a single Compute Engine instance, registering services with Consul during deployment and querying them at runtime.

### Explanation

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

---

## Question 29

*Domain 4: Integrating Applications with Google Cloud Services*

**You're managing an application employing an HTTP Cloud Function to process user activity from both desktop browser and mobile application clients. This function serves as the endpoint for all metric submissions using HTTP POST. However, due to legacy constraints, the function must be linked to a domain separate from the one requested by users on web or mobile sessions. The Cloud Function's domain is https://fn.example.com, while desktop and mobile clients use https://www.example.com. To restrict metric submissions solely to browser and mobile sessions, which response header should you include?**

- [ ] I. Add Access-Control-Allow-Origin: *
- [x] IV. Add Access-Control-Allow-Origin: https://www.example.com
- [ ] II. Add Access-Control-Allow-Origin: https://*.example.com
- [ ] III. Add Access-Control-Allow-Origin: https://fn.example.com

### Explanation

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

---

## Question 30

*Domain 3: Configuring and Deploying Applications*

**While running a containerized application on Google Kubernetes Engine with container images stored in Container Registry and employing CI/CD practices, how can you prevent the deployment of containers containing known critical vulnerabilities?**

- [ ] III. Enable the Container Scanning API for vulnerability scanning, review vulnerability reporting in Container Registry within the Cloud Console, and provide an attestation of the container's freedom from critical vulnerabilities, enforced by Binary Authorization policy before deployment.
- [ ] I. Utilize Web Security Scanner to automatically crawl the application, review scan results in application logs, and provide an attestation of the container's freedom from critical vulnerabilities, enforced by Binary Authorization policy before deployment.
- [x] IV. Enable the Container Scanning API for vulnerability scanning, programmatically review vulnerability reporting through the Container Scanning API, and provide an attestation of the container's freedom from critical vulnerabilities, enforced by Binary Authorization policy before deployment.
- [ ] II. Utilize Web Security Scanner to automatically crawl the application, review scan results in the Cloud Console's scan details page, and provide an attestation of the container's freedom from critical vulnerabilities, enforced by Binary Authorization policy before deployment.

### Explanation

**IV. Enable the Container Scanning API for vulnerability scanning, programmatically review vulnerability reporting through the Container Scanning API, and provide an attestation of the container's freedom from critical vulnerabilities, enforced by Binary Authorization policy before deployment.**

Here's why this stands out:

  * **Automation & Integration:** Programmatic interaction with the Container Scanning API enables you to integrate vulnerability checks directly into your CI/CD pipeline for a seamless workflow.

  * **Customizable Severity Assessment:** Programmatically parsing the vulnerability scan results gives you fine-grained control to define what constitutes a "critical" vulnerability based on your organization's risk tolerance.

  * **Enforcement:** Binary Authorization provides a robust mechanism to enforce policies based on the scan results, preventing vulnerable images from being deployed into your GKE clusters.

  * **Scalability:** This solution scales well, enabling you to automate vulnerability checks across a large number of container images.

**Why Other Options Are Less Ideal:**

  * **I & II. Web Security Scanner:** While useful for web application security, Web Security Scanner doesn't focus on container image vulnerability scanning.

  * **III. Manual Review in Console:** Relying on manual review in the Cloud Console slows down your CI/CD pipelines and is less scalable for larger deployments.

---

## Question 31

*Domain 4: Integrating Applications with Google Cloud Services*

**As you develop a microservice-based application to operate on Google Kubernetes Engine (GKE), certain services require access to various Google Cloud APIs. How should you configure authentication for these services within the cluster, adhering to Google's recommended best practices? (Select two.)**

- [x] II. Activate Workload Identity within the cluster via the gcloud command-line tool.
- [x] V. Bind the Kubernetes service account and the Google service account using roles/iam.workloadIdentity with gcloud.
- [ ] I. Utilize the service account associated with the GKE node.
- [ ] IV. Centralize the storage of Google service account keys within a secret management service.
- [ ] III. Retrieve the Google service account keys from a secret management service.

### Explanation

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

---

## Question 32

*Domain 4: Integrating Applications with Google Cloud Services*

**You manage an application utilizing the Cloud Storage API. Upon reviewing the logs, you notice several HTTP 503 Service Unavailable errors from the API. Your application logs these errors but does not take any immediate action. To enhance success rates, you want to implement Google-recommended retry logic. Which approach should you take?**

- [x] III. Retry each failed operation at increasing time intervals, up to a maximum number of tries.
- [ ] II. Retry each failed operation at consistent time intervals, up to a maximum number of attempts.
- [ ] I. Retry failed operations in batches after a defined number of failures have been logged.
- [ ] IV. Retry each failed operation at decreasing time intervals, up to a maximum number of tries.

### Explanation

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

---

## Question 33

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**In crafting a new API, your objective is to minimize storage costs and optimize image serving speed. Which architectural strategy is most appropriate?**

- [ ] II. Implement Compute Engine with Persistent Disk as the backend.
- [x] IV. Deploy Cloud Content Delivery Network (CDN) with Cloud Storage as the backend.
- [ ] III. Employ Transfer Appliance with Cloud Filestore as the backend.
- [ ] I. Utilize App Engine with Cloud Storage as the backend.

### Explanation

**IV. Deploy Cloud Content Delivery Network (CDN) with Cloud Storage as the backend.**

Explanation:

  * **Cost-Effectiveness:** Cloud Storage offers an economical solution for storing image files.

  * **Performance:** Cloud CDN leverages Google's global edge cache network, delivering images to users from locations closest to them, thereby significantly enhancing serving speed.

  * **Scalability:** Both Cloud Storage and Cloud CDN automatically scale to handle traffic surges, avoiding performance bottlenecks.

Why Other Options Are Less Ideal:

  * **I. Utilize App Engine with Cloud Storage as the backend.** App Engine is designed for serving application code. While it can technically serve images, using Cloud CDN is more optimized for image delivery.

  * **II. Implement Compute Engine with Persistent Disk as the backend.** This setup introduces management overhead. Compute Engines require provisioning and scaling, while Cloud Storage and CDN offer serverless scalability.

  * **III. Employ Transfer Appliance with Cloud Filestore as the backend.** These are generally used for large-scale data migrations or high-performance file workloads. The complexity and cost don't align well with a straightforward image-serving API.

---

## Question 34

*Domain 3: Configuring and Deploying Applications*

**You're planning to publish a straightforward HTML application online, which serves as an FAQ resource for your application. This static site comprises images, HTML, CSS, and JavaScript. Your aim is to make it accessible on the internet with minimal effort. What's the recommended action?**

- [ ] II. Deploy your application to an App Engine environment.
- [ ] III. Set up a Compute Engine instance with Apache web server installed. Configure Apache to host the application.
- [ ] IV. Containerize your application first. Then, deploy this container to Google Kubernetes Engine (GKE) and assign an external IP address to the GKE pod hosting the application.
- [x] I. Upload your application to Cloud Storage.

### Explanation

**I. Upload your application to Cloud Storage.**

**Explanation:**

For a simple, static website, Cloud Storage is the easiest way to make it publicly accessible:

  * **Simplicity:** Directly upload your files (HTML, CSS, JavaScript, Images) to a Cloud Storage bucket and configure the bucket for website hosting.

  * **Cost-effective:** Cloud Storage is a cost-effective option for simple website hosting.

  * **No Server Management:** You don't have to manage virtual machines or webserver software.

  * **Global Distribution:** Cloud Storage leverages Google's global infrastructure for low-latency content delivery.

**Why Other Options Are Less Ideal:**

  * **II. Deploy your application to an App Engine environment.** App Engine is overkill for a static site, adding unnecessary complexity and potential overhead.

  * **III. Set up a Compute Engine instance ...** This involves managing a virtual machine, installing, and configuring a web server – much more work than necessary for a static site.

  * **IV. Containerize your application ...** Containerizing and using Kubernetes adds complexity (and cost) without offering significant benefits for a purely static site.

**Reference:**  
<https://examlab.co/google/google-cloud-professional-cloud-developer>

---

## Question 35

*Domain 3: Configuring and Deploying Applications*

**Upon migrating certain applications to Google Cloud, you observe that your on-premises legacy monitoring platform, used for both on-premises and cloud applications, is responding sluggishly to urgent issues in the cloud deployments. What's the recommended course of action?**

- [ ] III. Revert some traffic to your previous platform and conduct A/B testing between the two platforms simultaneously.
- [ ] II. Install the Cloud Monitoring agent on your Compute Engine instances.
- [x] IV. Utilize Cloud Logging and Cloud Monitoring for log capture, monitoring, and alerting, directing alerts to your existing platform.
- [ ] I. Transition to Cloud Monitoring as a replacement for your current monitoring platform.

### Explanation

**IV. Utilize Cloud Logging and Cloud Monitoring for log capture, monitoring, and alerting, directing alerts to your existing platform.**

**Justification:**

  * **Integration Focus:** This approach focuses on integrating the strengths of Google Cloud's native monitoring tools with your existing platform. This minimizes disruption and leverages both tools effectively.

  * **Cloud-Native Advantages:** Cloud Logging and Cloud Monitoring are optimized for Google Cloud environments. They provide in-depth visibility into your cloud resources and offer features tailored to GCP.

  * **Minimize Disruption:** Integrating alerts with your existing platform avoids a complete overhaul of your monitoring setup and associated processes. This ensures a smoother transition and lessens the risk of overlooking issues.

  * **Flexibility:** This approach offers flexibility as you gradually evaluate the capabilities of Cloud Monitoring. If needed, you can further expand your use of Cloud Monitoring over time.

**Why Other Options are Less Suitable:**

  * **I. Transition to Cloud Monitoring as a replacement for your current monitoring platform.** A complete replacement introduces a significant change which could be disruptive to existing workflows. Integration may be a better starting point.

  * **II. Install the Cloud Monitoring agent on your Compute Engine instances.** This improves resource monitoring on Compute Engine, but it may not fully address the broader cloud application monitoring requirements and the integration needs with your existing system.

  * **III. Revert some traffic to your previous platform and conduct A/B testing between the two platforms simultaneously.** While helpful for evaluation, splitting traffic and A/B testing setups can be complex, and might not be the most efficient approach to improve monitoring responsiveness for urgent issues.

---

## Question 36

*Domain 3: Configuring and Deploying Applications*

**Your application is deployed using a custom machine image, with multiple unique deployments organized into separate managed instance groups, each with its own template. Each deployment requires distinct configuration values. How can you provide these unique values to each deployment while using the same custom machine image across all deployments, leveraging Compute Engine's built-in functionalities?**

- [ ] II. Store the unique configuration values in a Cloud Bigtable table, accessible by each deployment.
- [ ] III. Include the unique configuration values in the instance template's startup script.
- [ ] I. Store the unique configuration values in a persistent disk accessible to each deployment.
- [x] IV. Embed the unique configuration values in the instance template's instance metadata.

### Explanation

**IV. Embed the unique configuration values in the instance template's instance metadata.**

Here's why this stands out as the most suitable solution:

  * **Built-in Mechanism:** Instance metadata is designed specifically for providing configuration data to Compute Engine instances.

  * **Flexibility:** Metadata can be defined at the instance template level, allowing customization for each deployment.

  * **Security:** Metadata is accessible only from within the VM instance, enhancing security compared to external storage solutions.

  * **Ease of Management:** You can manage metadata through the Cloud Console, gcloud commands, or API calls, making updates straightforward.

**Why Other Options Have Drawbacks:**

  * **I. Store the unique configuration values in a persistent disk ...** This introduces dependencies on additional infrastructure (the disk) and potential complications around disk mounting and access permissions.

  * **II. Store the unique configuration values in a Cloud Bigtable table ...** Using Bigtable adds complexity. It's more suitable for large-scale, structured data rather than simple deployment-specific configuration values.

  * **III. Include the unique configuration values in the instance template's startup script.** Hardcoding values in the startup script makes it inflexible. Updates would require modifying the script and potentially rebuilding the machine image.

**References:**

[https://cloud.google.com/compute/docs/instances/startup-scripts](https://cloud.google.com/compute/docs/instances/startup-scripts  https://cloud.google.com/compute/docs/storing-retrieving-metadata#custom)

[https://cloud.google.com/compute/docs/storing-retrieving-metadata#custom](https://cloud.google.com/compute/docs/instances/startup-scripts  https://cloud.google.com/compute/docs/storing-retrieving-metadata#custom)

---

## Question 37

*Domain 2: Building and Testing Applications*

**As a developer managing three Google Kubernetes Engine clusters on Google Cloud, you need to enable your team to switch between clusters seamlessly while adhering to Google-recommended best practices. What is the best approach to configure access to multiple clusters?**

- [ ] IV. Advise the developers to open three terminals on their workstation and utilize `**kubectl config**` to set up access to each cluster.
- [ ] I. Request the developers to utilize Cloud Shell and execute `**gcloud container clusters get-credential**` to switch to another cluster.
- [x] II. Define the clusters, users, and contexts in a configuration file, and distribute the file to developers, instructing them to employ `**kubectl config**` to incorporate cluster, user, and context details.
- [ ] III. Instruct the developers to install the gcloud CLI on their workstations and execute `**gcloud container clusters get-credentials**` to switch to another cluster.

### Explanation

**Correct Option:**

  * **II. Define the clusters, users, and contexts in a configuration file, and distribute the file to developers, instructing them to employ kubectl config to incorporate cluster, user, and context details.**

**Justification:**

  * **Centralized Management:** Maintaining a single configuration file (often named `kubeconfig`) streamlines cluster access for your entire team and keeps configurations consistent.

  * **kubectl Standard:** This approach leverages the standard `kubectl` tool designed for managing Kubernetes resources across clusters.

  * **Best Practice:** Aligns with Google's recommendations and Kubernetes documentation for configuring access to multiple clusters.

**Why Other Options Are Less Ideal:**

  * **I. Request the developers to utilize Cloud Shell...**

    * **Impractical:** Cloud Shell sessions are transient, requiring repeated configuration and are less suitable for ongoing development work.

    * **Local Tooling:** Developers often need to interact with clusters from their local development environments.

  * **III. Instruct the developers to install the gcloud CLI...**

    * **Additional Overhead:** While the `gcloud` CLI is useful, it introduces an extra tool dependency. `kubectl` is the primary interface for Kubernetes interaction.

  * **IV. Advise the developers to open three terminals...**

    * **Inefficient:** Manually switching context in separate terminals is cumbersome and less manageable than a centralized configuration file.

**Reference:**  
<https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/>

---

## Question 38

*Domain 2: Building and Testing Applications*

**In the development process of a Cloud Function triggered by Cloud Storage events, your team seeks to streamline testing and development while adhering to Google-recommended best practices. Which method should you employ?**

- [x] III. Set up the Functions Framework library and configure the Cloud Function on a local environment. Duplicate the function and modify the new version. Use curl to test the updated version locally.
- [ ] II. Duplicate the Cloud Function and refactor the code to trigger on HTTP requests. Test the updated version by invoking the HTTP endpoint and assess functionality using mock requests.
- [ ] IV. Duplicate the Cloud Function in the Google Cloud console and edit the source code of the new function using the in-line editor. Adapt your web application to call the new function and test the updated version in production.
- [ ] I. Develop a new Cloud Function triggered by Cloud Audit Logs detecting the cloudfunctions.functions.sourceCodeSet operation in the original Cloud Function. Evaluate functionality using mock requests.

### Explanation

**Correct Answer:**

  * **III. Set up the Functions Framework library and configure the Cloud Function on a local environment. Duplicate the function and modify the new version. Use curl to test the updated version locally.**

**Justification:**

  * **Local Development:** The Functions Framework allows you to emulate Cloud Function behavior directly on your local machine, accelerating development and testing cycles.

  * **Isolation:** Testing changes locally before deploying them to the cloud environment minimizes the risk of introducing errors in production.

  * **Ease of Testing:** Using `curl` or other HTTP tools lets you easily send mock requests and verify your function's behavior.

**Why Other Options Are Less Ideal:**

  * **I. Develop a new Cloud Function triggered by Cloud Audit Logs...**

    * **Complexity:** While feasible, setting up another Cloud Function just for testing introduces unnecessary complexity and overhead.

  * **II. Duplicate the Cloud Function and refactor the code to trigger on HTTP requests...**

    * **Limited Testing:** This approach can be useful for basic HTTP testing, but it doesn't fully simulate the Cloud Storage event trigger behavior.

  * **IV. Duplicate the Cloud Function in the Google Cloud console ...**

    * **Production Risk:** Testing directly in a production environment is risky and strongly discouraged. It could lead to unexpected behavior for users.

**References:**

[https://cloud.google.com/functions/docs/running/function-frameworks](https://cloud.google.com/functions/docs/running/function-frameworks  https://cloud.google.com/functions/docs/running/calling#cloudevent_functions  https://cloud.google.com/functions/docs/running/overview#choosing_an_abstraction_layer  https://cloud.google.com/functions/docs/writing/write-event-driven-functions   https://cloud.google.com/functions/docs/calling/storage)

[https://cloud.google.com/functions/docs/running/calling#cloudevent_functions](https://cloud.google.com/functions/docs/running/function-frameworks  https://cloud.google.com/functions/docs/running/calling#cloudevent_functions  https://cloud.google.com/functions/docs/running/overview#choosing_an_abstraction_layer  https://cloud.google.com/functions/docs/writing/write-event-driven-functions   https://cloud.google.com/functions/docs/calling/storage)

[https://cloud.google.com/functions/docs/running/overview#choosing_an_abstraction_layer](https://cloud.google.com/functions/docs/running/function-frameworks  https://cloud.google.com/functions/docs/running/calling#cloudevent_functions  https://cloud.google.com/functions/docs/running/overview#choosing_an_abstraction_layer  https://cloud.google.com/functions/docs/writing/write-event-driven-functions   https://cloud.google.com/functions/docs/calling/storage)

[https://cloud.google.com/functions/docs/writing/write-event-driven-functions ](https://cloud.google.com/functions/docs/running/function-frameworks  https://cloud.google.com/functions/docs/running/calling#cloudevent_functions  https://cloud.google.com/functions/docs/running/overview#choosing_an_abstraction_layer  https://cloud.google.com/functions/docs/writing/write-event-driven-functions   https://cloud.google.com/functions/docs/calling/storage)

[https://cloud.google.com/functions/docs/calling/storage](https://cloud.google.com/functions/docs/running/function-frameworks  https://cloud.google.com/functions/docs/running/calling#cloudevent_functions  https://cloud.google.com/functions/docs/running/overview#choosing_an_abstraction_layer  https://cloud.google.com/functions/docs/writing/write-event-driven-functions   https://cloud.google.com/functions/docs/calling/storage)

---

## Question 39

*Domain 3: Configuring and Deploying Applications*

**In ensuring private traffic on Google Cloud for an application utilizing PostgreSQL and Cloud Run, which approach, aligning with Google's best practices and leveraging managed services, should be pursued?**

- [ ] III. Utilize Cloud SQL and Cloud Run in separate projects. Configure a private IP address for Cloud SQL, enable private services access, and establish a Serverless VPC Access connector. Set up a VPN connection between the projects and configure Cloud Run to use the connector for connecting to Cloud SQL.
- [ ] II. Deploy PostgreSQL on a Compute Engine virtual machine (VM) and enable Cloud Run in the same project. Allocate a private IP address to the VM, enable private services access, and create a Serverless VPC Access connector. Configure Cloud Run to utilize this connector for connecting to the VM hosting PostgreSQL.
- [x] I. Enable Cloud SQL and Cloud Run within the same project. Configure a private IP address for Cloud SQL and activate private services access. Set up a Serverless VPC Access connector, then configure Cloud Run to utilize it for connecting to Cloud SQL.
- [ ] IV. Deploy PostgreSQL on a Compute Engine VM and enable Cloud Run in different projects. Assign a private IP address to the VM, enable private services access, and create a Serverless VPC Access connector. Set up a VPN connection between the projects and configure Cloud Run to utilize the connector for accessing the VM hosting PostgreSQL.

### Explanation

**I. Enable Cloud SQL and Cloud Run within the same project. Configure a private IP address for Cloud SQL and activate private services access. Set up a Serverless VPC Access connector, then configure Cloud Run to utilize it for connecting to Cloud SQL.**

Here's why this is the most streamlined, secure, and Google-recommended approach:

  * **Simplified Networking:** Keeping Cloud SQL and Cloud Run in the same project and using a Serverless VPC Access connector eliminates complex VPN configuration.

  * **Managed Services:** This leverages fully managed Google Cloud services, minimizing operational overhead.

  * **Secure by Default:** Private services access and private IPs enhance security by isolating traffic within Google's internal network.

  * **Google Best Practice:** This is the approach explicitly recommended by Google for this scenario.

**Why Other Options are Less Ideal:**

  * **II. Self-managed PostgreSQL:** Deploying PostgreSQL on a Compute Engine VM adds the burden of managing the database instance and its security.

  * **III & IV. Cross-project VPN:** Setting up VPN tunnels introduces complexity, potential performance overhead, and the need to manage additional networking infrastructure.

**References:**  
[https://cloud.google.com/sql/docs/postgres/connect-run#configure https://cloud.google.com/sql/docs/postgres/connect-run#private-ip](https://cloud.google.com/sql/docs/postgres/connect-run#configure   https://cloud.google.com/sql/docs/postgres/connect-run#private-ip)

---

## Question 40

*Domain 3: Configuring and Deploying Applications*

**You are designing an application to receive messages from a single Pub/Sub topic and insert corresponding rows into a database. The application runs on Linux and utilizes preemptible virtual machines to reduce costs. To ensure a graceful shutdown, what should you do?**

- [ ] III. Implement a shutdown script that writes a file in a specified location, which the application polls every five minutes. Upon reading the file, the application disconnects from the database.
- [x] I. Develop a shutdown script utilizing inter-process signals to notify the application process to disconnect from the database.
- [ ] II. Create a shutdown script that broadcasts a message to all logged-in users, informing them of the Compute Engine instance shutdown, and advises them to save their work and log out.
- [ ] IV. Write a shutdown script that publishes a message to the Pub/Sub topic indicating a shutdown is in progress. After the application reads the message, it disconnects from the database.

### Explanation

**I. Develop a shutdown script utilizing inter-process signals to notify the application process to disconnect from the database.**

Here's why this is the most suitable approach:

  * **Reliability:** Signals are a standard and reliable mechanism for inter-process communication in Linux, ensuring the message is likely to be received by the application.

  * **Efficiency:** Signals are efficient, ensuring a prompt response to the shutdown event.

  * **Preemptible VM Specific:** Shutdown scripts are the recommended way to handle graceful termination of preemptible VMs.

  * **Focus:** This solution specifically addresses graceful shutdown of the application and database connection, without unnecessary steps.

**Why other options are not as good:**

  * **II. User Notification:** While user notification _might_ be helpful in a different context, it's not relevant to graceful shutdown of the automated process.

  * **III. File Polling:** Polling adds overhead, introduces delays (especially with a 5-minute interval), and is generally less reliable than signals.

  * **IV. Pub/Sub Overkill:** While sending a shutdown message to Pub/Sub could be used as an additional notification, it overcomplicates graceful shutdown for a single subscriber application.

**Reference:**

<https://cloud.google.com/compute/docs/instances/preemptible#preemption>

---

## Question 41

*Domain 4: Integrating Applications with Google Cloud Services*

**Your analytics system executes queries against a BigQuery dataset. The SQL query is run in batch mode, where the contents of a SQL file are passed to the BigQuery CLI. Subsequently, the output of the BigQuery CLI is redirected to another process. However, a permission error occurs when executing the queries.**

**You aim to resolve this issue. What action should you take?**

- [ ] IV. Create a new dataset in BigQuery, copy the source table to the new dataset, and then query the new dataset and table from the CLI.
- [x] I. Grant the service account the BigQuery Data Viewer and BigQuery Job User roles.
- [ ] II. Grant the service account the BigQuery Data Editor and BigQuery Data Viewer roles.
- [ ] III. Create a view in BigQuery based on the SQL query, then query the view using the CLI.

### Explanation

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

---

## Question 42

*Domain 3: Configuring and Deploying Applications*

**As you deploy your application to a Compute Engine virtual machine instance, it logs its files to disk. You want to view these logs in Stackdriver Logging without modifying the application code. What's the recommended approach?**

- [x] I. Install the Stackdriver Logging Agent and set it up to transmit the application logs.
- [ ] IV. Modify the application to log to /var/log so that its logs are automatically sent to Stackdriver Logging.
- [ ] III. Specify the log file folder path in the instance's metadata to configure it for sending the application logs.
- [ ] II. Utilize a Stackdriver Logging Library to directly log from the application to Stackdriver Logging.

### Explanation

**I. Install the Stackdriver Logging Agent and set it up to transmit the application logs.**

**Explanation:**

The Stackdriver Logging Agent (now called the Cloud Logging Agent) is the most flexible and least invasive way to achieve this:

  * **No Code Changes:** You don't have to modify your existing logging mechanisms, preserving your application logic.

  * **Customization:** The agent can monitor custom log files and even parse them to extract structured data, making it adaptable to your application's log format.

  * **Centralization:** The agent reliably sends logs to Stackdriver Logging, giving you a unified view in the Google Cloud Console.

**Why Other Options Are Less Ideal:**

  * **II. Utilize a Stackdriver Logging Library...** This requires changes to your code, adding the library and potentially modifying your logging statements.

  * **III. Specify the log file folder path...** This method relies on specific agent configurations and log formats, making it less flexible than actively configuring the agent.

  * **IV. Modify the application to log to /var/log...** This assumes your application can easily be reconfigured to write to `/var/log`. It also assumes standard log paths, which might not always be true.

**Reference:**

<https://cloud.google.com/logging/docs/agent/logging/installation>

---

## Question 43

*Domain 4: Integrating Applications with Google Cloud Services*

**You're tasked with transferring an internal file upload API, which enforces a 500-MB file size limit, to App Engine. What's the optimal approach?**

- [ ] III. Implement signed URLs for file uploads.
- [ ] II. Use CPanel for file uploads.
- [ ] I. Utilize FTP for uploading files.
- [x] IV. Modify the API to function as a multipart file upload API.

### Explanation

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

---

## Question 44

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Your team is developing a backend application to handle the business logic for an interactive voice response (IVR) system supporting a payroll application. The IVR system exhibits the following technical attributes:**

**Each customer phone call is associated with a unique IVR session.**

**A separate persistent gRPC connection is established to the backend for each session.**

**Interruption of connections prompts the IVR system to establish new connections, causing slight latency for the call.**

**Analysis of current call data reveals:**

**Call duration spans from 1 to 30 minutes.**

**Calls are predominantly made during business hours.**

**Significant call surges occur around specific dates (e.g., paydays) or during major payroll changes.**

**To minimize cost, effort, and operational overhead, where should you deploy the backend appliction?**

- [ ] III. Cloud Functions
- [x] IV. Cloud Run
- [ ] I. Compute Engine
- [ ] II. Google Kubernetes Engine cluster in Standard mode

### Explanation

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

---

## Question 45

*Domain 4: Integrating Applications with Google Cloud Services*

**In the development of your web application, which access configuration should you implement for controlling access to private images and videos stored in a Cloud Storage bucket, considering that your users are anonymous and don't have Google Accounts?**

- [ ] III. Set up Identity-Aware Proxy (IAP) for user authentication within the web application. Grant users access to the bucket post-authentication via IAP.
- [x] IV. Generate a signed URL providing read access to the bucket. Users can access the URL following authentication through your web application.
- [ ] I. Cache each web application user's IP address and establish a named IP table using Google Cloud Armor. Then, create a Google Cloud Armor security policy permitting user access to the backend bucket.
- [ ] II. Assign the Storage Object Viewer IAM role to allUsers. Users can access the bucket upon authentication through your web application.

### Explanation

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

---

## Question 46

*Domain 3: Configuring and Deploying Applications*

**During the development of an application with multiple microservices on Google Kubernetes Engine (GKE), one microservice requires connectivity to a third-party on-premises database. It's crucial to securely store database credentials and ensure regular rotation, following security best practices. What's the recommended approach?**

- [x] IV. Securely store credentials as a Kubernetes Secret, employing the Cloud Key Management Service plugin for encryption and decryption.
- [ ] III. Store credentials in an encrypted volume mount, linking a Persistent Volume Claim to the client Pod.
- [ ] I. Save credentials in a sidecar container proxy, using it for database connections.
- [ ] II. Set up a service mesh to control traffic between microservice Pods and the database.

### Explanation

**The recommended approach for securely storing and managing database credentials for a microservice running on Google Kubernetes Engine (GKE) would be option IV:**

**IV. Securely store credentials as a Kubernetes Secret, employing the Cloud Key Management Service plugin for encryption and decryption.**

**Explanation:**

  1. **Kubernetes Secrets** : Kubernetes provides a built-in resource called Secrets, designed specifically for storing sensitive information such as passwords, OAuth tokens, and SSH keys. Kubernetes Secrets are a natural fit for storing database credentials securely within the cluster.

  2. **Cloud Key Management Service (KMS)** : Google Cloud Platform offers a Key Management Service (KMS) that allows you to manage cryptographic keys for your cloud services. By using KMS, you can encrypt the Secrets stored in Kubernetes, adding an extra layer of security to the sensitive data.

  3. **Plugin Integration** : Kubernetes allows for plugins to integrate with external key management services like Google Cloud KMS. By using the Cloud KMS plugin, you can ensure that the Secrets stored in Kubernetes are encrypted using keys managed by Cloud KMS, adding another layer of security.

Options I, II, and III are not the best fit for securely managing database credentials in this scenario:

I. Saving credentials in a sidecar container proxy might introduce unnecessary complexity and potential security vulnerabilities. Additionally, sidecar containers are typically used for tasks such as logging, monitoring, or additional functionality, rather than securely storing sensitive data.

II. Setting up a service mesh could help control traffic between microservices within the cluster, but it's not directly related to securely storing database credentials.

III. Storing credentials in an encrypted volume mount is better than plain text storage, but it lacks the fine-grained control and integration with key management services provided by Kubernetes Secrets with Cloud KMS integration. Additionally, managing encryption keys and rotation might be more complex compared to using Kubernetes Secrets with a KMS plugin.

**Reference:**

<https://cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets#reencrypt-secrets>

---

## Question 47

*Domain 4: Integrating Applications with Google Cloud Services*

**Your company is developing an application that uploads reports to a Cloud Storage bucket. Upon uploading a report, you aim to trigger the publication of a message to a Cloud Pub/Sub topic. You want a solution that requires minimal implementation effort. What should you do?**

- [ ] IV. Deploy an application on a Google Kubernetes Engine cluster to handle the uploaded files and publish messages to the Cloud Pub/Sub topic upon receipt.
- [x] I. Configure the Cloud Storage bucket to activate Cloud Pub/Sub notifications when objects are modified.
- [ ] II. Develop an App Engine application to receive the uploaded files and then publish messages to the Cloud Pub/Sub topic.
- [ ] III. Create a Cloud Function triggered by changes in the Cloud Storage bucket, responsible for publishing messages to the Cloud Pub/Sub topic.

### Explanation

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

---

## Question 48

*Domain 2: Building and Testing Applications*

**Your company stores its source code in a Cloud Source Repositories repository. The company aims to build and test the code with each source code commit to the repository, seeking a managed solution with minimal operational overhead. Which method should they use?**

- [ ] IV. Implement a source code commit trigger to send a message to a Cloud Pub/Sub topic, subsequently activating an App Engine service to build the source code.
- [ ] II. Deploy Jenkins via the Google Cloud Platform Marketplace, set up to monitor source code commits.
- [x] I. Utilize Cloud Build with a trigger configured for each source code commit.
- [ ] III. Employ a Compute Engine virtual machine instance with an open-source continuous integration tool, configured to monitor source code commits.

### Explanation

**I. Utilize Cloud Build with a trigger configured for each source code commit.**

Here's why this is the best choice:

  * **Managed Service:** Cloud Build is a serverless CI/CD solution from Google Cloud, minimizing operational burden compared to self-managing CI tools.

  * **Integration:** Cloud Build has direct integration with Cloud Source Repositories, simplifying setup.

  * **Flexibility:** Cloud Build can be customized for various build and test scenarios.

**Why Other Options Are Less Ideal:**

  * **II. Deploy Jenkins via the Google Cloud Platform Marketplace ...** Jenkins is a versatile CI tool, but deploying it through the Marketplace still involves managing a VM, updates, etc., increasing operational overhead.

  * **III. Employ a Compute Engine virtual machine instance ...** This approach has the most operational overhead, requiring provisioning, OS maintenance, and CI tool configuration.

  * **IV. Implement a source code commit trigger to send a message ...** While feasible, this introduces more moving parts (Pub/Sub, App Engine), adding complexity compared to the direct Cloud Build integration.

---

## Question 49

*Domain 3: Configuring and Deploying Applications*

**You're preparing to deploy a new application revision to Google Kubernetes Engine (GKE) in a production environment. Considering potential container issues, you aim to minimize risks while following Google's recommended practices. Which approach should you take?**

- [ ] III. Convert the Deployment to a StatefulSet and conduct a rolling update with a PodDisruptionBudget set at 80%.
- [ ] IV. Convert the Deployment to a StatefulSet and execute a rolling update with a HorizontalPodAutoscaler scale-down policy value of 0.
- [ ] II. Execute a rolling update with a HorizontalPodAutoscaler scale-down policy value of 0.
- [x] I. Conduct a rolling update with a PodDisruptionBudget set at 80%.

### Explanation

**Correct Answer:**

  * **I. Conduct a rolling update with a PodDisruptionBudget set to 80%.**

**Justification:**

  * **Minimizing Downtime:** Rolling updates replace pods gradually, ensuring service availability during the update process.

  * **Safety Net:** A PodDisruptionBudget (PDB) limits the number of pods that can be unavailable simultaneously. Setting it to 80% guarantees that at least 80% of your pods remain active, mitigating the risk of full service disruption.

  * **Google-Recommended:** This strategy aligns with Google's best practices for production deployments on GKE.

**Why Other Options Are Less Suitable:**

  * **II. Execute a rolling update with a HorizontalPodAutoscaler scale-down policy value of 0.**

    * **HPA's Purpose:** A HorizontalPodAutoscaler (HPA) is meant to adjust the number of replicas based on load, not primarily for deployment strategies. Disabling scaling down during the upgrade might help but doesn't provide the same level of control as a PDB.

  * **III. Convert the Deployment to a StatefulSet and conduct a rolling update with a PodDisruptionBudget set at 80%.**

  * **IV. Convert the Deployment to a StatefulSet and execute a rolling update with a HorizontalPodAutoscaler scale-down policy value of 0.**

    * **Unnecessary for Stateless Apps:** StatefulSets are designed for stateful applications that require stable identifiers and persistent storage. If your application is stateless, converting to a StatefulSet adds unnecessary complexity.

**References:**

[https://kubernetes.io/docs/tasks/run-application/configure-pdb/#identify-an-application-to-protect](https://kubernetes.io/docs/tasks/run-application/configure-pdb/#identify-an-application-to-protect  https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/   https://cloud.google.com/blog/products/containers-kubernetes/ensuring-reliability-and-uptime-for-your-gke-cluster  https://blog.knoldus.com/how-to-avoid-outages-in-your-kubernetes-cluster-using-pdb/)

[https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/ https://cloud.google.com/blog/products/containers-kubernetes/ensuring-reliability-and-uptime-for-your-gke-cluster](https://kubernetes.io/docs/tasks/run-application/configure-pdb/#identify-an-application-to-protect  https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/   https://cloud.google.com/blog/products/containers-kubernetes/ensuring-reliability-and-uptime-for-your-gke-cluster  https://blog.knoldus.com/how-to-avoid-outages-in-your-kubernetes-cluster-using-pdb/)

[https://blog.knoldus.com/how-to-avoid-outages-in-your-kubernetes-cluster-using-pdb/](https://kubernetes.io/docs/tasks/run-application/configure-pdb/#identify-an-application-to-protect  https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/   https://cloud.google.com/blog/products/containers-kubernetes/ensuring-reliability-and-uptime-for-your-gke-cluster  https://blog.knoldus.com/how-to-avoid-outages-in-your-kubernetes-cluster-using-pdb/)

---

## Question 50

*Domain 2: Building and Testing Applications*

**You are setting up a continuous integration pipeline with Cloud Build to automate the deployment of new container images to Google Kubernetes Engine (GKE). The pipeline includes building the application from its source code, running unit and integration tests separately, and pushing the container to Container Registry. The application operates on a Python web server.**

**The Dockerfile provided is as follows:**

- [x] I. Select a virtual machine (VM) size with higher CPU for Cloud Build runs.
- [ ] V. Store application source code on Cloud Storage, and configure the pipeline to use gsutil to download the source code.
- [ ] II. Deploy a Container Registry on a Compute Engine VM in a VPC, and utilize it to store the final images.
- [ ] IV. Change the base image in the Dockerfile to ubuntu:latest, and install Python 3.7 using a package manager utility.
- [x] III. Cache the Docker image for subsequent builds using the --cache-from argument in your build config file.

### Explanation

I. **Select a virtual machine (VM) size with higher CPU for Cloud Build runs:**

  * **Cloud Build allows you to specify machine type and size for your builds.**

  * **Choosing a VM size with higher CPU can speed up build times, especially for CPU-intensive tasks like building Docker images.**

  * **This option can improve build performance and reduce overall pipeline execution time.**

II. **Deploy a Container Registry on a Compute Engine VM in a VPC, and utilize it to store the final images:**

  * Google Container Registry (GCR) is a managed Docker container registry that integrates well with Google Cloud Platform services like Cloud Build and GKE.

  * GCR provides secure, reliable, and scalable storage for Docker images without the need to manage infrastructure.

  * Deploying a separate Container Registry on Compute Engine adds unnecessary complexity and maintenance overhead compared to using GCR directly.

III. **Cache the Docker image for subsequent builds using the --cache-from argument in your build config file:**

  * **Cloud Build supports caching Docker images to improve build performance.**

  * **By caching Docker images, subsequent builds can reuse layers from previous builds, reducing build times.**

  * **This option helps optimize build times and improve pipeline efficiency.**

IV. **Change the base image in the Dockerfile to ubuntu:latest, and install Python 3.7 using a package manager utility:**

  * Changing the base image to Ubuntu and installing Python 3.7 using a package manager utility like apt can introduce compatibility issues.

  * The Docker image might not match the runtime environment of Google Kubernetes Engine, which typically uses container-optimized OS images.

  * It's generally recommended to use base images specifically designed for container environments to ensure compatibility and security.

V. **Store application source code on Cloud Storage, and configure the pipeline to use gsutil to download the source code:**

  * Storing application source code on Cloud Storage and using gsutil to download it adds unnecessary complexity to the pipeline.

  * Cloud Build provides native integration with source code repositories like Cloud Source Repositories or GitHub.

  * Leveraging native integrations simplifies pipeline configuration and management.

Considering the requirements and best practices, the most suitable options would be:

  * **I. Select a virtual machine (VM) size with higher CPU for Cloud Build runs.**

  * **III. Cache the Docker image for subsequent builds using the --cache-from argument in your build config file.**

These options optimize build performance and efficiency without introducing unnecessary complexity or potential compatibility issues.

References:  
[https://cloud.google.com/build/docs/optimize-builds/increase-vcpu-for-builds https://cloud.google.com/build/docs/optimize-builds/building-leaner-containers#building_leaner_containers](https://cloud.google.com/build/docs/optimize-builds/increase-vcpu-for-builds   https://cloud.google.com/build/docs/optimize-builds/building-leaner-containers#building_leaner_containers  https://cloud.google.com/build/docs/optimize-builds/speeding-up-builds#using_a_cached_docker_image)

[https://cloud.google.com/build/docs/optimize-builds/speeding-up-builds#using_a_cached_docker_image](https://cloud.google.com/build/docs/optimize-builds/increase-vcpu-for-builds   https://cloud.google.com/build/docs/optimize-builds/building-leaner-containers#building_leaner_containers  https://cloud.google.com/build/docs/optimize-builds/speeding-up-builds#using_a_cached_docker_image)

---

## Question 51

*Domain 2: Building and Testing Applications*

**To migrate an independent Java application operating on an on-premises Linux virtual machine (VM) to Google Cloud cost-effectively without employing the lift-and-shift method, the plan is to modernize the application by converting it to a container. How should this task be accomplished?**

- [ ] I. Employ Migrate for Anthos to transition the VM to your Google Kubernetes Engine (GKE) cluster as a container.
- [x] IV. Utilize Jib to construct a Docker image from your source code, subsequently uploading it to Artifact Registry. Then, deploy the application within a GKE cluster and perform testing.
- [ ] III. Use Migrate for Compute Engine to transfer the VM to a Compute Engine instance, and leverage Cloud Build for container conversion.
- [ ] II. Export the VM as a raw disk and import it as an image. Then, instantiate a Compute Engine instance from the imported image.

### Explanation

**The most appropriate approach for modernizing the Java application by converting it into a container on Google Cloud would be option IV:**

**IV. Utilize Jib to construct a Docker image from your source code, subsequently uploading it to Artifact Registry. Then, deploy the application within a GKE cluster and perform testing.**

**Explanation:**

  1. Jib: Jib is a tool provided by Google for building Docker and OCI images for Java applications without needing to write a Dockerfile or manage Docker daemon. Jib integrates seamlessly with Maven or Gradle, making it easy to build container images directly from your Java source code.

  2. **Artifact Registry** : Artifact Registry is a managed service provided by Google Cloud for storing and managing container images. Once the Docker image is built using Jib, you can upload it to Artifact Registry for secure storage and distribution.

  3. **Deploy to GKE** : Google Kubernetes Engine (GKE) is a managed Kubernetes service provided by Google Cloud. Once the Docker image is stored in Artifact Registry, you can deploy it to GKE for container orchestration. GKE offers scalability, reliability, and ease of management for running containerized applications.

Options I, II, and III are not the best fit for modernizing the application as described:

I. Migrate for Anthos is a tool for modernizing and migrating workloads to containers and Kubernetes, but it's typically used for more complex applications that may require additional refactoring or integration with Kubernetes features. For a simple Java application, using Jib and deploying to GKE directly would be more straightforward and cost-effective.

II. Exporting the VM as a raw disk and importing it as an image to instantiate a Compute Engine instance doesn't involve containerization. While it can migrate the application to Google Cloud, it doesn't achieve the modernization goal of running the application in a containerized environment.

III. Migrate for Compute Engine is a tool for migrating VMs to Compute Engine instances, but it doesn't inherently involve containerization. Leveraging Cloud Build for container conversion might add unnecessary complexity compared to using Jib directly for building Docker images.

**Reference:**

<https://cloud.google.com/blog/products/application-development/introducing-jib-build-java-docker-images-better>

---

## Question 52

*Domain 3: Configuring and Deploying Applications*

**You aim to monitor the memory usage of your application deployed on Compute Engine. What's the appropriate action?**

- [ ] I. Implement the Stackdriver Client Library.
- [ ] III. Utilize the Stackdriver Metrics Explorer.
- [x] II. Deploy the Stackdriver Monitoring Agent.
- [ ] IV. Access the Google Cloud Platform Console.

### Explanation

**II. Deploy the Stackdriver Monitoring Agent.**

Here's why this is the best option:

  * **Comprehensive Metrics:** The Stackdriver Monitoring Agent automatically collects a wide range of system-level metrics, including memory usage, and sends them to Stackdriver Monitoring.

  * **Minimal Configuration:** Agent installation and basic configuration are relatively straightforward.

  * **Visualization & Alerting:** Stackdriver Monitoring provides tools for visualizing memory usage data over time and creating alerts based on thresholds you define.

**Why Other Options Are Less Ideal:**

  * **I. Implement the Stackdriver Client Library.** While this library _can_ be used for custom metrics, it's overkill for basic memory usage. The agent handles this automatically.

  * **III. Utilize the Stackdriver Metrics Explorer.** Metrics Explorer is for viewing and querying data collected by Stackdriver Monitoring – this relies on the agent collecting those metrics first.

  * **IV. Access the Google Cloud Platform Console.** The GCP console offers a high-level overview of resources, but lacks the granular historical views and alerting capabilities you'd need for detailed memory monitoring.

References:

[https://cloud.google.com/monitoring/api/metrics_agent#agent-memory](https://cloud.google.com/monitoring/api/metrics_agent#agent-memory  https://cloud.google.com/monitoring/agent)

[https://cloud.google.com/monitoring/agent](https://cloud.google.com/monitoring/api/metrics_agent#agent-memory  https://cloud.google.com/monitoring/agent)

---

## Question 53

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**You are developing a web application accessible over both HTTP and HTTPS, hosted on Compute Engine instances. Periodically, you'll require SSH access from your remote laptop to conduct maintenance on these instances. How should you configure the instances while ensuring compliance with Google-recommended best practices?**

- [ ] IV. Establish a backend with Compute Engine web server instances utilizing private IP addresses behind an HTTP(S) load balancer. Additionally, set up a bastion host with a public IP address and open firewall ports. Access the web instances via the bastion host.
- [ ] I. Deploy a backend with Compute Engine web server instances utilizing private IP addresses behind a TCP proxy load balancer.
- [x] III. Implement the Cloud Identity-Aware Proxy API for SSH access. Then, configure the Compute Engine servers with private IP addresses behind an HTTP(s) load balancer for web traffic.
- [ ] II. Configure firewall rules to permit all incoming traffic to connect to the Compute Engine web servers, assigning each server a unique external IP address.

### Explanation

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

---

## Question 54

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**In designing an application comprising multiple microservices, each with its RESTful API deployed as separate Kubernetes Services, ensuring minimal impact on API consumers during changes is paramount. Additionally, it's crucial to prevent disruptions to third-party systems upon new API releases. How should you configure the application's connection, adhering to Google's recommended best practices?**

- [ ] IV. Consolidate multiple versions within the same service and specify the API version in the POST request.
- [ ] II. Utilize a Service Discovery system to connect to the backend specified in the request.
- [ ] III. Implement multiple clusters and route requests to distinct versioned backends via DNS entries.
- [x] I. Employ an Ingress that directs requests to the appropriate backend based on the API's URL.

### Explanation

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

---

## Question 55

*Domain 3: Configuring and Deploying Applications*

**You've deployed a new application to Google Kubernetes Engine and are facing performance degradation. Logs are directed to Cloud Logging, and Prometheus metrics are captured using a sidecar model. How do you effectively correlate metrics and log data to troubleshoot and set up real-time alerts, all while minimizing costs?**

- [ ] II. Export both Cloud Logging logs and Prometheus metrics to Cloud Bigtable. Conduct a query to combine the data for analysis within Google Data Studio.
- [x] IV. Export Prometheus metrics and utilize Cloud Monitoring to visualize them as external metrics. Configure Cloud Monitoring to establish log-based metrics from the logs and correlate them with the Prometheus data.
- [ ] III. Export Cloud Logging logs and stream Prometheus metrics to BigQuery. Set up periodic queries to merge the data and trigger notifications using Cloud Tasks.
- [ ] I. Derive custom metrics from Cloud Logging logs, then leverage Prometheus to import them via the Cloud Monitoring REST API.

### Explanation

**IV. Export Prometheus metrics and utilize Cloud Monitoring to visualize them as external metrics. Configure Cloud Monitoring to establish log-based metrics from the logs and correlate them with the Prometheus data.**

Here's why this stands out as the best choice:

  * **Unified Insights:** Cloud Monitoring provides a centralized platform for both Prometheus metrics and log-based metrics, enabling easier correlation and visualization.

  * **Real-time Alerting:** Cloud Monitoring's built-in alerting mechanisms allow you to create alerts directly based on both metrics and log-based metrics.

  * **Cost Optimization:** Cloud Monitoring is generally a more cost-effective solution compared to exporting all data to BigQuery or Bigtable.

  * **Minimized Complexity:** This approach avoids the overhead of setting up streaming pipelines and additional data transformations.

**Why Other Options Are Less Ideal:**

  * **I. Deriving Custom Metrics:** While possible, it adds complexity and potential latency to your troubleshooting workflow.

  * **II. Cloud Bigtable & Data Studio:** Bigtable is geared towards large-scale data management. Data Studio adds cost and complexity when Cloud Monitoring can cover visualization and alerting needs.

  * **III. BigQuery & Cloud Tasks:** While queries in BigQuery are powerful, setting up this pipeline increases operational overhead and might introduce latency for real-time troubleshooting.

**References:**

<https://cloud.google.com/stackdriver/docs/solutions/gke/prometheus#viewing_metrics>

---

## Question 56

*Domain 4: Integrating Applications with Google Cloud Services*

**While developing an application requiring user-specific subdirectories in Cloud Storage to store files, what action should be taken to ensure the creation of an empty subdirectory when a new user is added?**

- [ ] II. Establish an object with the subdirectory name and promptly delete it to create an empty subdirectory structure.
- [ ] IV. Produce an object with the subdirectory name, ensuring it has a zero-byte size, and set the Content-Type metadata to CLOUDSTORAGE_FOLDER.
- [x] I. Generate an object with the subdirectory name, appending a trailing slash ('/') to denote an empty directory.
- [ ] III. Create an object with the subdirectory name, ensuring it has a zero-byte size and WRITER access control list permission.

### Explanation

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

---

## Question 57

*Domain 4: Integrating Applications with Google Cloud Services*

**As the lead developer overseeing a new retail system operating on Cloud Run and Firestore in Datastore mode, you've successfully implemented the functionality to display a list of available products on the web UI. However, you've encountered HTTP 500 errors during peak usage times, indicating Cloud Run instances exceeding memory limits, coinciding with spikes in Datastore entity reads. To optimize system performance and prevent crashes, what action should you take?**

- [ ] II. Refine the query retrieving the product list by applying limits.
- [ ] I. Adjust the query retrieving the product list by employing integer offsets.
- [x] IV. Refine the query retrieving the product list by implementing cursors.
- [ ] III. Adjust the Cloud Run configuration to raise memory limits.

### Explanation

**Correct Option:** **IV. Refine the query retrieving the product list by implementing cursors.**

**Explanation:**

  * **Cursors for Pagination:** Cursors are essential for efficiently managing large result sets in Firestore. They allow you to break down the retrieval of the product list into smaller, more manageable chunks, preventing memory overload in Cloud Run instances.

**Why other options are less ideal:**

  * **I. Integer Offsets:** While offsets can be used for pagination, they become less efficient as the dataset grows. Firestore needs to skip over the specified number of results each time, leading to increased latency and read costs.

  * **II. Limits:** Simply limiting the results per query helps, but if you have many products, users may need multiple requests to see everything. This leads to a less seamless user experience.

  * **III. Increasing Memory Limits:** This is a temporary fix that masks the underlying problem. It doesn't address inefficient data retrieval and will likely lead to higher costs.

**Reference:**

<https://cloud.google.com/datastore/docs/concepts/queries#cursors_limits_and_offsets>

---

## Question 58

*Domain 3: Configuring and Deploying Applications*

**As you develop a new web application using Cloud Run and commit code to Cloud Source Repositories, you aim to deploy new code efficiently. You've already crafted a Cloud Build YAML file that builds a container and executes the command: gcloud run deploy. What's the next step?**

- [ ] IV. Schedule a Cron job to run the command gcloud builds submit every 24 hours.
- [ ] I. Establish a Pub/Sub topic to receive notifications when code is pushed to the repository. Set up a Pub/Sub trigger to execute the build file upon receiving an event on the topic.
- [x] II. Configure a build trigger to activate the build file when code is pushed to the development branch of the repository.
- [ ] III. Implement a webhook build trigger to execute the build file upon receiving HTTP POST calls at the webhook URL.

### Explanation

**Correct Answer:**

  * **II. Configure a build trigger to activate the build file when code is pushed to the development branch of the repository.**

**Justification:**

  * **Direct Integration:** Cloud Build triggers offer the most seamless integration with Cloud Source Repositories. They directly monitor your repo for changes.

  * **Branch Specificity:** You can configure the trigger to activate only on pushes to the designated branch (development in this case), ensuring builds happen when you expect them.

  * **Efficiency:** This automated process eliminates the need for manual intervention or external systems for triggering builds.

**Why Other Options Are Less Ideal:**

  * **I. Establish a Pub/Sub topic ...**

    * **Added Complexity:** While Pub/Sub could be used to trigger Cloud Build, it introduces an additional layer to manage compared to a direct build trigger.

  * **III. Implement a webhook build trigger...**

    * **External Dependency:** Webhooks require an external system to send the HTTP POST request, adding a dependency outside of Cloud Build.

  * **IV. Schedule a Cron job...**

    * **Inflexible:** Cron jobs are good for scheduled tasks but less responsive to dynamic events like code pushes. Also, daily builds could be too infrequent for active development.

**References:**  
[https://cloud.google.com/build/docs/automating-builds/create-manage-triggers](https://cloud.google.com/build/docs/automating-builds/create-manage-triggers  https://cloud.google.com/build/docs/triggers  https://cloud.google.com/build/docs/automating-builds/create-manage-triggers#connect_repo)

[https://cloud.google.com/build/docs/triggers](https://cloud.google.com/build/docs/automating-builds/create-manage-triggers  https://cloud.google.com/build/docs/triggers  https://cloud.google.com/build/docs/automating-builds/create-manage-triggers#connect_repo)

[https://cloud.google.com/build/docs/automating-builds/create-manage-triggers#connect_repo](https://cloud.google.com/build/docs/automating-builds/create-manage-triggers  https://cloud.google.com/build/docs/triggers  https://cloud.google.com/build/docs/automating-builds/create-manage-triggers#connect_repo)

---

## Question 59

*Domain 1: Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications*

**Your team is developing an ecommerce platform where users log in, add items to their shopping cart, and are automatically logged out after 30 minutes of inactivity. Upon logging back in, their shopping cart should be preserved. How should you store users' session and shopping cart information while adhering to Google-recommended best practices?**

- [ ] I. Save session data in Pub/Sub and shopping cart information in Cloud SQL.
- [x] IV. Utilize Memorystore for Redis or Memorystore for Memcached for session data and Firestore for shopping cart information.
- [ ] III. Maintain both session and shopping cart information in a MySQL database deployed across multiple Compute Engine instances.
- [ ] II. Store shopping cart details in Cloud Storage files, with filenames as the SESSION ID.

### Explanation

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

---

## Question 60

*Domain 2: Building and Testing Applications*

**You manage an application hosted on a production Google Kubernetes Engine (GKE) cluster, deploying updates through Cloud Deploy. As you anticipate frequent code modifications, you need tools to test these changes locally. These tools should:**

  * **Automate testing of local changes.**

  * **Ensure local deployment mirrors production deployment.**

**Which tools should you select to test container building and execution on your local machine with minimal resource usage?**

- [ ] I. Docker Compose and dockerd
- [x] III. Minikube and Skaffold
- [ ] II. Terraform and kubeadm
- [ ] IV. kaniko and Tekton

### Explanation

**Correct Option:** **III. Minikube and Skaffold**

**Explanation:**

  * **Minikube:** This provides a lightweight, single-node Kubernetes cluster on your local machine, replicating a production-like environment for testing.

  * **Skaffold:** Skaffold handles local container builds, pushes them to a registry, and deploys them to the Minikube cluster. It also automates rebuilds/redeploys whenever you make local code changes. This combination is optimized for developer experience and resource efficiency during local testing.

**Why other options are less suitable:**

  * **I. Docker Compose and dockerd:** Docker Compose helps with container orchestration but doesn't fully emulate a Kubernetes environment, making it less ideal for ensuring your local deployment mirrors production. `dockerd` focuses on image management rather than the full deployment process.

  * **II. Terraform and kubeadm:** This combination focuses on infrastructure provisioning (GKE cluster creation) rather than streamlined local development and testing workflows.

  * **IV. kaniko and Tekton:** Kaniko is useful for building container images within a Kubernetes cluster, and Tekton provides a CI/CD framework. While powerful, they are heavier solutions than necessary for optimized local development and testing.

---
