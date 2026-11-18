# Professional Cloud Architect — Practice Exam 1

60 questions.

## Question 1

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**Your organization is planning a significant update to its API to enhance the developer experience. They need to ensure that the previous version of the API remains accessible and deployable while enabling new customers and testers to explore the updated API. Additionally, they want to retain the existing SSL and DNS records to serve both API versions. What is the best approach to achieve this?**

- [ ] A. Set up a new load balancer specifically for the updated API.
- [ ] B. Modify existing clients to direct traffic to a different endpoint for the new API.
- [ ] C. Configure the existing API to route traffic to the new API based on the request path.
- [x] D. Implement separate backend pools behind the load balancer for different API paths.

### Explanation

**Correct Answer:**

**D. Implement separate backend pools behind the load balancer for different API paths.**

**Explanation:**

The best approach is to use **separate backend pools** behind a single load balancer that directs traffic based on API paths. This solution ensures that:

- Both the old and new API versions remain **accessible** and **deployable** without disrupting existing customers.
- Existing **SSL certificates** and **DNS records** remain unchanged, as traffic is still routed through the same entry point.
- A seamless transition is provided for **new customers and testers** without modifying existing client applications.
- Traffic can be routed based on specific **path rules** using **Google Cloud HTTP(S) Load Balancer**, allowing selective access to API versions.

Google Cloud HTTP(S) Load Balancer allows defining **backend services with different URL path-based routing**. This lets you configure the load balancer to route requests based on API versions (e.g., `/v1/*` to the old API and `/v2/*` to the new API).

**Supporting Documentation:**

- Google Cloud HTTP(S) Load Balancer - Path-based routing:
  **https://cloud.google.com/load-balancing/docs/https/traffic-management#path_rule_examples**

**Why Other Options Are Incorrect:**

**A. Set up a new load balancer specifically for the updated API.**

❌ **Incorrect** – Setting up a new load balancer means:

- You **need a new DNS record and SSL certificate**, which the requirement explicitly says should be retained.
- It introduces **unnecessary complexity** when the existing load balancer can handle both API versions using **backend pools and URL-based routing**.

✅ **Reference:**

- Google Cloud Load Balancing Best Practices:
  **https://cloud.google.com/load-balancing/docs/best-practices**

**B. Modify existing clients to direct traffic to a different endpoint for the new API.**

❌ **Incorrect** – This approach requires **client-side changes**, which:

- **Breaks backward compatibility** for existing customers.
- Does not allow seamless testing of the new API for new customers while keeping the old API operational.
- The requirement explicitly states that **previous API versions must remain accessible without modification**.

✅ **Reference:**

- API versioning strategies in Google Cloud:
  **https://cloud.google.com/endpoints/docs/openapi/versioning-an-api**

**C. Configure the existing API to route traffic to the new API based on the request path.**

❌ **Incorrect** – This approach suggests modifying the **existing API**, but:

- It **adds complexity and dependencies** within the API code rather than handling it at the infrastructure level.
- API applications should not be responsible for **traffic routing**, as this is best handled by the **load balancer**.
- The requirement is to have **both API versions independently deployable**, which this solution does not fully support.

✅ **Reference:**

- Traffic management with Load Balancers:
  **https://cloud.google.com/load-balancing/docs/https/traffic-management**

**Conclusion:**

The best solution is **Option D**: **Implement separate backend pools behind the load balancer for different API paths**. This approach:

- Retains existing **SSL and DNS settings**.
- Ensures both **API versions remain accessible** without modifying client configurations.
- Allows controlled traffic routing to the **new API version** for new customers and testers.
- Uses Google Cloud **HTTP(S) Load Balancer with URL-based routing**, a recommended best practice.

📌 **Final Reference:**
**https://cloud.google.com/load-balancing/docs/https/traffic-management#path_rule_examples**

---

## Question 2

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**Your organization is planning to migrate a multi-petabyte dataset to the cloud while ensuring that the data remains accessible 24/7. The business analysts are familiar with using a SQL interface for analysis. How should the data be stored to optimize ease of analysis?**

- [x] A. Load the data into Google BigQuery.
- [ ] B. Insert the data into Google Cloud SQL.
- [ ] C. Store the data as flat files in Google Cloud Storage.
- [ ] D. Stream the data into Google Cloud Datastore.

### Explanation

**Correct Answer:**

**A. Load the data into Google BigQuery.**

**Explanation:**

Google **BigQuery** is the best choice for storing a **multi-petabyte dataset** while ensuring **24/7 accessibility** and providing a **SQL-based interface** for business analysts.

BigQuery is a **serverless, highly scalable, and fully managed enterprise data warehouse** optimized for running complex SQL queries over large datasets efficiently. It supports:

- **Petabyte-scale data storage and processing** with high performance.
- **Standard SQL interface**, which business analysts are already familiar with.
- **24/7 availability** with no infrastructure management required.
- **Seamless integration** with Google Cloud Storage (GCS), Dataflow, and Dataproc for data ingestion and ETL pipelines.

✅ **Supporting Documentation:**

- **BigQuery Overview:**
  **https://cloud.google.com/bigquery/docs/introduction**
- **BigQuery SQL Interface:**
  **https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax**

**Why Other Options Are Incorrect:**

**B. Insert the data into Google Cloud SQL.**

❌ **Incorrect** – Google Cloud SQL is **not suitable for multi-petabyte-scale datasets** because:

- It is designed for **OLTP (Online Transaction Processing)** rather than **OLAP (Online Analytical Processing)**.
- It has **storage limits** (up to **64 TB for MySQL and PostgreSQL**), which is far smaller than **multi-petabyte** storage needs.
- Querying large datasets in Cloud SQL is significantly **slower and costlier** compared to BigQuery.

✅ **Reference:**

- Cloud SQL **storage limits:**
  **https://cloud.google.com/sql/docs/features**

**C. Store the data as flat files in Google Cloud Storage.**

❌ **Incorrect** – While Google Cloud Storage (GCS) can handle **multi-petabyte** storage, it is **not optimized for SQL-based analysis** because:

- GCS stores data as **flat files**, requiring **additional processing (ETL) and tools** (e.g., Dataproc, Dataflow, or BigQuery external tables) to analyze the data.
- Direct querying of files in GCS is **slower** and **less efficient** than using BigQuery.
- BigQuery supports **native table storage**, which is much more efficient for SQL-based analysis.

✅ **Reference:**

- Cloud Storage vs. BigQuery for analytics:
  **https://cloud.google.com/architecture/data-lake-bigquery**

**D. Stream the data into Google Cloud Datastore.**

❌ **Incorrect** – Google Cloud Datastore (now **Firestore**) is a **NoSQL document database**, which is not optimized for:

- **SQL-based analysis**, as it uses a document-based **NoSQL** model instead of relational data.
- **Multi-petabyte datasets**, as it is designed for structured application data rather than large-scale analytics.
- **OLAP workloads**, since Datastore is more suited for **OLTP transactional applications** rather than analytical queries.

✅ **Reference:**

- Firestore vs. BigQuery:
  **https://cloud.google.com/firestore/docs/bigquery**

**Conclusion:**

The best choice is **A. Load the data into Google BigQuery**, as it:

- **Supports SQL queries** that business analysts are familiar with.
- **Handles petabyte-scale data** efficiently.
- **Provides 24/7 availability** without the need for infrastructure management.
- **Optimizes cost and performance** for analytical workloads.

📌 **Final Reference:**
**https://cloud.google.com/bigquery/docs/introduction**

---

## Question 3

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**The operations manager requests a list of best practices to consider when migrating a J2EE application to the cloud. Which three recommendations should you provide? (Choose three.)**

- [x] A. Adapt the application code to run on Google App Engine.
- [ ] B. Integrate Cloud Dataflow into the application to collect real-time metrics.
- [ ] C. Enable application monitoring using a tool like Stackdriver Debugger.
- [x] D. Use an automation framework to ensure reliable provisioning of cloud infrastructure.
- [x] E. Implement a continuous integration tool with automated testing in a staging environment.
- [ ] F. Transition from MySQL to a managed NoSQL database such as Google Cloud Datastore or Bigtable.

### Explanation

**Correct Answers:**

**A. Adapt the application code to run on Google App Engine.**
**D. Use an automation framework to ensure reliable provisioning of cloud infrastructure.**
**E. Implement a continuous integration tool with automated testing in a staging environment.**

**Explanation for Correct Choices:**

**A. Adapt the application code to run on Google App Engine.** ✅

- Google App Engine (GAE) is a fully managed **Platform-as-a-Service (PaaS)** that supports **J2EE applications** and allows them to run without managing infrastructure.
- Migrating a J2EE application to **App Engine Standard or Flexible** can provide auto-scaling, built-in load balancing, and simplified deployment.
- If the application requires **stateful sessions or specific configurations**, App Engine Flexible Environment may be preferable.

✅ **Reference:**

- **https://cloud.google.com/appengine/docs/java**

**D. Use an automation framework to ensure reliable provisioning of cloud infrastructure.** ✅

- **Infrastructure-as-Code (IaC)** tools like **Terraform, Deployment Manager, or Ansible** help automate cloud resource provisioning.
- Automation reduces **manual errors**, ensures **consistency**, and supports **scalability** when deploying infrastructure.
- Google recommends using automation to define infrastructure as code (IaC) when migrating applications to the cloud.

✅ **Reference:**

- **https://cloud.google.com/docs/automation**

**E. Implement a continuous integration tool with automated testing in a staging environment.** ✅

- A **Continuous Integration/Continuous Deployment (CI/CD)** pipeline ensures smooth application **testing, validation, and deployment** in the cloud.
- Automated testing in a **staging environment** ensures that issues are detected before production deployment.
- Google Cloud offers **Cloud Build, Cloud Deploy, and third-party CI/CD integrations** for automated testing and deployment.

✅ **Reference:**

- **https://cloud.google.com/architecture/devops/devops-tech-continuous-integration**

**Why Other Options Are Incorrect:**

**B. Integrate Cloud Dataflow into the application to collect real-time metrics.** ❌

- **Cloud Dataflow** is a **streaming and batch data processing service** mainly used for **ETL and analytics workflows**, not for collecting application metrics.
- Instead, **Cloud Monitoring (formerly Stackdriver Monitoring) and Cloud Logging** are the correct tools for **application monitoring**.

✅ **Reference:**

- **https://cloud.google.com/dataflow/docs/concepts/overview**

**C. Enable application monitoring using a tool like Stackdriver Debugger.** ❌

- While **monitoring is essential**, **Stackdriver Debugger (now Cloud Debugger)** is mainly used for **real-time debugging**, not for **application performance monitoring**.
- Instead, **Cloud Monitoring (formerly Stackdriver Monitoring) and Cloud Logging** should be used for **application observability**.
- Debugging is important but not a key **migration best practice**.

✅ **Reference:**

- **https://cloud.google.com/debugger/docs**

**F. Transition from MySQL to a managed NoSQL database such as Google Cloud Datastore or Bigtable.** ❌

- Migrating from **MySQL (relational)** to **Cloud Datastore or Bigtable (NoSQL)** is not always a best practice unless the application requires NoSQL scalability.
- If the J2EE application **relies on relational databases**, a better alternative is **Cloud SQL (managed MySQL/PostgreSQL) or Cloud Spanner** instead of NoSQL databases.

✅ **Reference:**

- **https://cloud.google.com/databases**

**Conclusion:**

The **best practices for migrating a J2EE application to Google Cloud** are:

1. **Adapt the application to run on Google App Engine** for seamless deployment and scaling (**Option A**).
2. **Use an automation framework** for reliable cloud infrastructure provisioning (**Option D**).
3. **Implement a CI/CD pipeline** to automate testing and deployment in a staging environment (**Option E**).

📌 **Final Reference:**

- **https://cloud.google.com/migrate**
- **https://cloud.google.com/solutions/migrating-to-app-engine**

**⚠️ Note:** Stackdriver Debugger (later Cloud Debugger) was shut down in 2023, so option C can't be right today. App Engine stands for 'move to a managed platform'; newer versions may offer Cloud Run or GKE instead.

---

## Question 4

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**A development team is concerned that their existing logging tool will not be sufficient for their new cloud-based product. They need a more effective solution to capture errors and analyze historical log data. You want to assist them in finding the right tool. What should you do?**

- [ ] A. Recommend that they download and install the Google Stackdriver Logging agent.
- [ ] B. Provide them with a list of online resources covering best practices for logging.
- [x] C. Work with them to define their requirements and evaluate suitable logging tools.
- [ ] D. Assist them in upgrading their current tool to leverage any new features.

### Explanation

**Correct Answer:**

**C. Work with them to define their requirements and evaluate suitable logging tools.**

**Explanation:**

Before recommending a specific logging tool, it is **critical to first define the team’s requirements** and evaluate the available options based on their needs. This approach ensures that:

- The solution aligns with **business and technical needs** (e.g., real-time monitoring, log retention, security, and scalability).
- The **most suitable** Google Cloud logging tool is selected (e.g., Cloud Logging, BigQuery for log analysis, or third-party tools like Splunk).
- The logging solution integrates well with **existing cloud-based products and workflows**.

This approach follows **Google Cloud’s best practices** for cloud logging, which include:

- **Understanding logging needs** (e.g., performance, storage, security).
- **Evaluating Google Cloud’s built-in tools** (Cloud Logging, Cloud Monitoring, BigQuery, etc.).
- **Considering third-party integrations** if needed.

✅ **Supporting Documentation:**

- **Best practices for Cloud Logging:**
  **https://cloud.google.com/logging/docs/best-practices**
- **Choosing a logging solution:**
  **https://cloud.google.com/logging/docs/**

**Why Other Options Are Incorrect:**

**A. Recommend that they download and install the Google Stackdriver Logging agent.** ❌

- **Google Stackdriver Logging** is now part of **Cloud Operations Suite (Cloud Logging)**, but installing the agent is **not the first step**.
- The team might need a **different tool** depending on their requirements, such as **BigQuery for historical log analysis** or **third-party logging solutions**.
- Jumping straight to implementation without understanding the requirements **may result in selecting an inadequate tool**.

✅ **Reference:**

- **https://cloud.google.com/logging/docs/agent**

**B. Provide them with a list of online resources covering best practices for logging.** ❌

- While best practices are useful, **providing a list of resources does not directly solve the issue**.
- The team needs **guidance on selecting and implementing** a logging solution, not just general information.
- They require an **interactive evaluation process** rather than self-research alone.

✅ **Reference:**

- **https://cloud.google.com/logging/docs/best-practices**

**D. Assist them in upgrading their current tool to leverage any new features.** ❌

- The team has already **expressed concerns** that their existing logging tool **may not be sufficient**.
- Simply upgrading an inadequate tool **does not guarantee that it will meet their cloud-based needs**.
- The **best approach is first to assess their requirements** before making any decisions.

✅ **Reference:**

- **https://cloud.google.com/logging/docs/export/configure_export**

**Conclusion:**

The best approach is **C. Work with them to define their requirements and evaluate suitable logging tools**, ensuring that:

- The selected logging solution meets **performance, scalability, and analytical needs**.
- **Google Cloud Logging, BigQuery, or third-party tools** are considered based on their use case.
- The team adopts a **logging strategy aligned with best practices** in Google Cloud.

📌 **Final Reference:**
**https://cloud.google.com/logging/docs/**

---

## Question 5

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

**Your company wants to further reduce the number of unplanned rollbacks of erroneous production deployments in its web hosting platform. Improvements to the QA and testing processes have already achieved an 80% reduction. Which two additional approaches can help minimize rollbacks? (Choose two.)**

- [x] A. Implement a blue-green deployment strategy.
- [ ] B. Replace the QA environment with canary releases.
- [x] C. Break down the monolithic platform into microservices.
- [ ] D. Minimize the platform’s reliance on relational database systems.
- [ ] E. Migrate from relational database systems to a NoSQL database.

### Explanation

**Correct Answers:**

**A. Implement a blue-green deployment strategy.**
**C. Break down the monolithic platform into microservices.**

**Explanation for Correct Choices:**

**A. Implement a blue-green deployment strategy.** ✅

- **Blue-green deployments** allow for **zero-downtime releases** by maintaining two separate environments:
  - **Blue**: The current production environment.
  - **Green**: The new environment with the updated version.
- Traffic can be **switched between versions** only after validation, reducing **erroneous rollbacks** in production.
- If an issue is detected, **rolling back to the previous (stable) version is instantaneous**.
- This approach is a **Google Cloud-recommended deployment strategy** for reliability.

✅ **Reference:**

- **https://cloud.google.com/architecture/application-deployment-and-testing-strategies**

**C. Break down the monolithic platform into microservices.** ✅

- Migrating from a **monolithic** to a **microservices architecture**:
  - **Reduces the blast radius** of failures by isolating components.
  - Enables **incremental deployments**, where only a small portion of the system is updated instead of the entire platform.
  - Allows for **easier rollbacks** and **smaller, independent teams** to deploy safely.
- Microservices **improve agility** and **reduce the risk of widespread failures**, leading to fewer unplanned rollbacks.

✅ **Reference:**

- **https://cloud.google.com/microservices**

**Why Other Options Are Incorrect:**

**B. Replace the QA environment with canary releases.** ❌

- **Canary releases** are useful for **gradual rollouts**, but **removing the QA environment entirely is not a best practice**.
- A QA environment is crucial for **pre-deployment validation**; eliminating it **increases production risks** rather than reducing rollbacks.

✅ **Reference:**

- **https://cloud.google.com/architecture/application-deployment-and-testing-strategies**

**D. Minimize the platform’s reliance on relational database systems.** ❌

- The **database system itself is not the root cause** of unplanned rollbacks.
- **Reducing reliance on relational databases** may improve **scalability**, but it does not directly prevent **deployment rollbacks**.
- The **deployment process and application architecture** are the primary areas for reducing rollbacks.

✅ **Reference:**

- **https://cloud.google.com/sql/docs**

**E. Migrate from relational database systems to a NoSQL database.** ❌

- Migrating to NoSQL is **not a direct solution** to reducing erroneous rollbacks.
- NoSQL databases are **useful for scalability and flexibility**, but changing the database type does not inherently reduce **failed deployments**.
- A migration could introduce **more risk** and **require significant re-architecting**, potentially increasing **failures** during the transition.

✅ **Reference:**

- **https://cloud.google.com/databases/docs/choosing-database**

**Conclusion:**

The best strategies to **further minimize unplanned rollbacks** are:

1. **Implementing a blue-green deployment strategy** for **safe, reversible** rollouts (**Option A**).
2. **Breaking down the monolithic platform into microservices** for **isolated, incremental deployments** (**Option C**).

📌 **Final Reference:**

- **https://cloud.google.com/architecture/application-deployment-and-testing-strategies**
- **https://cloud.google.com/microservices**

---

## Question 6

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

**To reduce costs, the Director of Engineering has mandated that all developers migrate their development infrastructure from on-premises virtual machines (VMs) to Google Cloud Platform. These resources experience multiple start/stop cycles throughout the day and require persistent state. You have been tasked with designing a solution for running a development environment in Google Cloud while ensuring cost visibility for the finance team. Which two actions should you take? (Choose two.)**

- [x] A. Use the `--no-auto-delete` flag on all persistent disks and stop the VM.
- [ ] B. Use the `--auto-delete` flag on all persistent disks and terminate the VM.
- [ ] C. Apply a VM CPU utilization label and include it in the BigQuery billing export.
- [x] D. Leverage Google BigQuery billing export and labels to track costs by groups.
- [ ] E. Store all state in local SSD, snapshot the persistent disks, and terminate the VM.
- [ ] F. Store all state in Google Cloud Storage, snapshot the persistent disks, and terminate the VM.

### Explanation

**Correct options: A and D**

- **A. Use the `--no-auto-delete` flag on all persistent disks and stop the VM.**
  *Why:* Dev VMs need state to persist across frequent start/stop cycles. Setting **no auto-delete** on Persistent Disks ensures disks aren’t deleted when the instance stops/terminates; stopping the VM saves compute cost while retaining the disk state for the next start.
  Ref: Stop/Start instances & disk persistence: [https://cloud.google.com/compute/docs/instances/stop-start-instance](https://cloud.google.com/compute/docs/instances/stop-start-instance)
- **D. Leverage BigQuery billing export and labels to track costs by groups.**
  *Why:* Finance needs visibility. Enable **Cloud Billing export to BigQuery** and apply **resource labels** (e.g., `env=dev`, `team=payments`) so you can attribute and report costs by team/project/group with SQL.
  Ref: Track costs with labels + BigQuery export: [https://cloud.google.com/billing/docs/how-to/export-data-bigquery](https://cloud.google.com/billing/docs/how-to/export-data-bigquery)

Why not the others

- **B** auto-deletes disks → loses dev state.
- **C** “CPU utilization label” isn’t a thing; labels are arbitrary key/values, not dynamic metrics.
- **E/F** rely on local SSD (ephemeral) or extra snapshot flows/GCS—more ops overhead and not necessary for simple persistent dev environments.

---

## Question 7

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**Your company wants to monitor whether a meeting room is occupied during a scheduled meeting. There are 1,000 meeting rooms distributed across five offices on three continents. Each room is equipped with a motion sensor that sends status updates every second. The sensor data consists of a sensor ID and multiple discrete data points. Analysts will need to combine this data with information about account owners and office locations. Which type of database should you use?**

- [ ] A. Flat file
- [x] B. NoSQL
- [ ] C. Relational
- [ ] D. Blobstore

### Explanation

**Correct Answer:**

**B. NoSQL**

**Explanation:**

A **NoSQL database** is the best choice for storing motion sensor data in this scenario due to the following reasons:

- **High write throughput:** Motion sensors send **status updates every second** from **1,000 meeting rooms**, requiring a database that can handle **high-velocity writes** efficiently.
- **Scalability:** NoSQL databases, such as **Google Cloud Bigtable or Firestore**, can handle large-scale, **distributed data** across multiple regions efficiently.
- **Flexible schema:** Sensor data consists of **sensor IDs and multiple discrete data points**, which may vary over time. NoSQL databases allow **schema flexibility**, unlike relational databases that require strict schema definitions.
- **Global distribution:** Since the sensors are located across **five offices on three continents**, a **distributed NoSQL database** can ensure **low-latency access**.
- **Integration with analytics:** NoSQL databases such as **Bigtable** can integrate with **BigQuery** for analytics, allowing analysts to **combine sensor data with account and location information**.

✅ **Recommended NoSQL solutions on Google Cloud:**

- **Google Cloud Bigtable:** Best for high-ingest, time-series sensor data.
- **Firestore (Cloud Datastore):** Good for semi-structured sensor data with low-latency queries.

✅ **Supporting Documentation:**

- **Google Cloud Bigtable for IoT and Sensor Data:**
  **https://cloud.google.com/bigtable/docs**
- **Choosing between Firestore, Bigtable, and BigQuery:**
  **https://cloud.google.com/databases/docs/choosing-database**

**Why Other Options Are Incorrect:**

**A. Flat file** ❌

- **Not scalable** for **high-frequency** sensor data ingestion.
- Difficult to **query efficiently** and **combine** with account/office location data.
- **Poor real-time processing** capabilities.

✅ **Reference:**

- **https://cloud.google.com/storage/docs/**

**C. Relational** ❌

- **Not suitable for time-series sensor data** due to **scalability constraints**.
- **Rigid schema** structure makes it **less efficient for handling variable sensor data**.
- **High-frequency writes** could overwhelm relational databases, leading to **performance issues**.
- **Better suited for structured data** (e.g., account owners and office locations), but sensor data should be stored in a NoSQL database instead.

✅ **Reference:**

- **https://cloud.google.com/sql/docs/**

**D. Blobstore** ❌

- **Google Cloud Storage (Blobstore)** is ideal for storing **binary large objects (images, videos, backups, documents)**, **not structured or semi-structured sensor data**.
- **Inefficient for real-time analytics** since querying sensor data in blob storage requires additional processing steps.

✅ **Reference:**

- **https://cloud.google.com/storage/docs/what-is-cloud-storage**

**Conclusion:**

The best database choice is **B. NoSQL**, specifically a **Google Cloud Bigtable** or **Firestore** solution, because it supports:

- **High-frequency sensor data ingestion.**
- **Scalability across multiple regions.**
- **Real-time queries and integration with analytics tools.**

📌 **Final Reference:**
**https://cloud.google.com/bigtable/docs**
**https://cloud.google.com/databases/docs/choosing-database**

---

## Question 8

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**You have set up an autoscaling instance group to handle web traffic for an upcoming launch. After configuring the instance group as a backend service for an HTTP(S) load balancer, you notice that virtual machine (VM) instances are terminating and relaunching every minute. The instances do not have public IP addresses. You have confirmed that each instance returns the expected web response using the curl command. To ensure the backend is configured correctly, what should you do?**

- [ ] A. Verify that a firewall rule exists to allow source traffic on HTTP/HTTPS to reach the load balancer.
- [ ] B. Assign a public IP to each instance and configure a firewall rule to allow the load balancer to reach the instance’s public IP.
- [x] C. Ensure that a firewall rule is in place to allow load balancer health checks to reach the instances in the instance group.
- [ ] D. Tag each instance with the load balancer’s name and create a firewall rule allowing traffic from the load balancer to the instance tag as the destination.

### Explanation

**Correct Answer:**

**C. Ensure that a firewall rule is in place to allow load balancer health checks to reach the instances in the instance group.**

**Explanation:**

The behavior of VM instances **terminating and relaunching every minute** suggests that the **load balancer’s health checks are failing**, causing the autoscaler to **remove and replace** instances.

- Google Cloud **HTTP(S) Load Balancer** relies on **health checks** to determine whether backend instances are **healthy**.
- If the health check **fails**, the instance is marked as **unhealthy** and is replaced by the autoscaler.
- Since the VMs **do not have public IPs**, the **load balancer’s health checks must reach the private IPs** of the backend instances.
- **A firewall rule must allow ingress traffic from the load balancer's health check IP ranges** to the backend instances on the **configured health check port (e.g., TCP:80 or TCP:443).**

✅ **Fix:** Create a firewall rule to allow **Google Cloud health check probes** to access the backend instances.

✅ **Supporting Documentation:**

- **Firewall Rules for Load Balancer Health Checks:**
  **https://cloud.google.com/load-balancing/docs/health-checks#firewall_rules**
- **Health Check Configuration for Load Balancers:**
  **https://cloud.google.com/load-balancing/docs/health-checks**

**Why Other Options Are Incorrect:**

**A. Verify that a firewall rule exists to allow source traffic on HTTP/HTTPS to reach the load balancer.** ❌

- **Incorrect** because this rule applies to **external users accessing the web service** and **not** to the load balancer's **health checks**.
- The **load balancer itself does not directly use HTTP/HTTPS to determine instance health**; it relies on **dedicated health check probes**.

✅ **Reference:**

- **https://cloud.google.com/load-balancing/docs/https#firewalls**

**B. Assign a public IP to each instance and configure a firewall rule to allow the load balancer to reach the instance’s public IP.** ❌

- **Incorrect** because:
  - The Google Cloud HTTP(S) Load Balancer uses **internal IPs** for backend instance communication.
  - Backend instances **do not require public IPs** for load balancer health checks or data traffic.
  - Google Cloud best practices **recommend using private IPs** for security and cost efficiency.

✅ **Reference:**

- **https://cloud.google.com/load-balancing/docs/https#backend_services**

**D. Tag each instance with the load balancer’s name and create a firewall rule allowing traffic from the load balancer to the instance tag as the destination.** ❌

- **Incorrect** because:
  - **Instance tags do not control load balancer traffic routing.**
  - The **correct firewall rule must specifically allow traffic from Google’s health check IP ranges**, not just from the load balancer.
  - **Health checks are conducted by Google’s infrastructure, not the load balancer itself.**

✅ **Reference:**

- **https://cloud.google.com/load-balancing/docs/health-checks#firewall_rules**

**Conclusion:**

The best way to **prevent instances from terminating and relaunching** is to ensure **Google Cloud health check traffic can reach the backend instances** by:

1. **Creating a firewall rule** to allow health check IP ranges to access the instances on the appropriate health check port.
2. **Confirming that the health check settings** (protocol, port, and path) match the actual instance configuration.

📌 **Final Reference:**
**https://cloud.google.com/load-balancing/docs/health-checks#firewall_rules**

---

## Question 9

*Domain 3: Designing for Security and Compliance*

**You have written a Python script to connect to Google BigQuery from a Google Compute Engine virtual machine. However, the script is displaying errors indicating that it cannot connect to BigQuery. What should you do to resolve this issue?**

- [ ] A. Install the latest BigQuery API client library for Python.
- [ ] B. Run the script on a new virtual machine with the BigQuery access scope enabled.
- [x] C. Create a new service account with BigQuery access and execute the script using that account.
- [ ] D. Install the BigQuery (`bq`) component for `gcloud` using the command `gcloud components install bq`.

### Explanation

**Correct Answer:**

**C. Create a new service account with BigQuery access and execute the script using that account.**

**Explanation:**

If your **Python script cannot connect to BigQuery** from a **Google Compute Engine (GCE) virtual machine**, the most common reason is **insufficient IAM permissions** or **missing authentication credentials**.

✅ **Creating and using a service account with BigQuery access** ensures that the script has the **necessary authentication and authorization** to interact with BigQuery.

**Steps to Fix the Issue:**

1. **Create a Service Account** in Google Cloud IAM:
  - Assign the **BigQuery User** or **BigQuery Data Viewer/Editor** role, depending on required permissions.
2. **Generate a JSON Key File** for the service account and securely store it on the GCE instance.
3. **Set the Authentication Environment Variable** before running the script:
  ```
  texport GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"
  ```
4. **Ensure the Python script uses the service account credentials** via `google.auth`:
  ```
  from google.cloud import bigquery client = bigquery.Client()
  ```
  - If the `GOOGLE_APPLICATION_CREDENTIALS` variable is set correctly, BigQuery will authenticate using the service account.

✅ **Supporting Documentation:**

- **Authenticating to BigQuery:**
  **https://cloud.google.com/bigquery/docs/authentication/service-account-file**
- **Service Account IAM Roles:**
  **https://cloud.google.com/iam/docs/understanding-roles**

**Why Other Options Are Incorrect:**

**A. Install the latest BigQuery API client library for Python.** ❌

- Installing the `google-cloud-bigquery` library is **necessary** but **not sufficient** to fix authentication issues.
- The error suggests a **connection issue**, which is usually related to **authentication**, not missing libraries.

✅ **Reference:**

- **https://cloud.google.com/python/docs/reference/bigquery/latest**

**B. Run the script on a new virtual machine with the BigQuery access scope enabled.** ❌

- While enabling **BigQuery API access scopes** on a VM **can help**, the **default Compute Engine service account** may still lack **sufficient IAM permissions**.
- The best practice is to **use a dedicated service account with explicit BigQuery permissions** rather than relying on access scopes alone.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/access/service-accounts**

**D. Install the BigQuery (bq) component for gcloud using the command `gcloud components install bq`.** ❌

- The `bq` command-line tool is **useful for manually running queries**, but it **does not affect a Python script’s ability to authenticate and connect** to BigQuery.
- The Python script requires authentication using the **Google Cloud SDK or a service account** rather than just the `bq` CLI tool.

✅ **Reference:**

- **https://cloud.google.com/sdk/gcloud/reference/components/install**

**Conclusion:**

The best way to resolve the **authentication issue in a Python script connecting to BigQuery** from a GCE instance is:

1. **Create a new service account** with BigQuery access.
2. **Generate a JSON key file** for authentication.
3. **Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable**.

📌 **Final Reference:**
**https://cloud.google.com/bigquery/docs/authentication/service-account-file**

**⚠️ Note:** Two things can block a VM from calling BigQuery: the attached service account lacks a BigQuery IAM role, or the VM's access scopes don't include BigQuery (the default scopes don't). Option B fixes the scope; the key fixes the identity. Current best practice is a dedicated service account with least-privilege BigQuery roles, attached to the VM with the cloud-platform scope, not a downloaded JSON key. Learn the key, but expect the scope option to be argued.

---

## Question 10

*Domain 3: Designing for Security and Compliance*

**A customer is migrating an existing corporate application from an on-premises data center to Google Cloud Platform. The business owners want to minimize user disruption during the transition. Additionally, the security team has strict requirements for storing passwords. Which authentication strategy should be implemented?**

- [ ] A. Use G Suite Password Sync to replicate passwords into Google.
- [x] B. Federate authentication via SAML 2.0 with the existing Identity Provider.
- [ ] C. Provision users in Google using the Google Cloud Directory Sync tool.
- [ ] D. Require users to set their Google password to match their corporate password.

### Explanation

**Correct Answer:**

**B. Federate authentication via SAML 2.0 with the existing Identity Provider.**

**Explanation:**

Federating authentication via **SAML 2.0** with the existing **Identity Provider (IdP)** is the best strategy because:

- **Minimizes user disruption**: Users can continue **logging in with their corporate credentials** without changing passwords or adopting new authentication methods.
- **Enhances security**: Passwords **remain stored and managed within the corporate IdP**, meeting the security team’s strict requirements for password storage.
- **Supports Single Sign-On (SSO)**: Users can authenticate once and access Google Cloud resources without re-entering credentials.
- **Google Cloud supports SAML 2.0 integration** with enterprise identity providers like **Microsoft Active Directory, Okta, and Ping Identity**.

✅ **Supporting Documentation:**

- **Setting up SAML for Google Cloud authentication:**
  **https://cloud.google.com/identity/docs/setup/saml**
- **Google Identity Platform Federation Options:**
  **https://cloud.google.com/identity/docs/federation**

**Why Other Options Are Incorrect:**

**A. Use G Suite Password Sync to replicate passwords into Google.** ❌

- **Incorrect** because **Google does not store user passwords** from external directories.
- **G Suite Password Sync** is used to synchronize **Active Directory (AD) passwords to Google Workspace**, but it does not provide **federated authentication**.
- The security team has **strict password storage policies**, and storing passwords in Google **may not meet compliance requirements**.

✅ **Reference:**

- **https://support.google.com/a/answer/2611859?hl=en**

**C. Provision users in Google using the Google Cloud Directory Sync tool.** ❌

- **Incorrect** because **Google Cloud Directory Sync (GCDS)** only synchronizes **user accounts and groups** but **does not synchronize passwords**.
- **GCDS does not provide authentication**—it only **mirrors identities** from Active Directory or LDAP to Google Cloud.
- This approach **does not enable SSO**, meaning users would have **separate login credentials** for Google Cloud, disrupting workflows.

✅ **Reference:**

- **https://cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction**

**D. Require users to set their Google password to match their corporate password.** ❌

- **Incorrect** because:
  - **Users would have to manage two separate passwords**, increasing complexity and risk.
  - **No enforcement mechanism** ensures that users maintain password synchronization between corporate systems and Google.
  - **Less secure** than SAML federation, where authentication happens via a centralized IdP.

✅ **Reference:**

- **https://cloud.google.com/identity/docs/federation**

**Conclusion:**

The best authentication strategy is **B. Federate authentication via SAML 2.0 with the existing Identity Provider**, because it:

- **Ensures seamless authentication** without user disruption.
- **Meets security requirements** by keeping passwords within the corporate system.
- **Supports Single Sign-On (SSO)** for a better user experience.

📌 **Final Reference:**
**https://cloud.google.com/identity/docs/setup/saml**

---

## Question 11

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**Your company has successfully migrated to the cloud and now wants to analyze its data streams to optimize operations. Since there is no existing code for this analysis, all options are being considered. The company requires a combination of batch and stream processing, as some jobs run hourly while other data is processed in real time. Which technology should they use?**

- [ ] A. Google Cloud Dataproc
- [x] B. Google Cloud Dataflow
- [ ] C. Google Kubernetes Engine with Bigtable
- [ ] D. Google Compute Engine with Google BigQuery

### Explanation

**Correct Answer:**

**B. Google Cloud Dataflow**

**Explanation:**

Google Cloud **Dataflow** is the best solution because:

- It **supports both batch and stream processing**, which matches the company’s need to process some jobs **hourly (batch)** and others **in real time (streaming)**.
- **Based on Apache Beam**, it allows defining **unified processing pipelines** that work for both real-time and batch data.
- **Fully managed**, meaning it scales automatically without requiring infrastructure management.
- Integrates seamlessly with **BigQuery, Pub/Sub, and Bigtable**, which are commonly used for analytics and operational optimizations.

✅ **Supporting Documentation:**

- **Dataflow for batch and streaming processing:**
  **https://cloud.google.com/dataflow/docs/concepts/streaming-with-dataflow**
- **Choosing between Dataflow, Dataproc, and BigQuery:**
  **https://cloud.google.com/architecture/data-lakes-with-gcp**

**Why Other Options Are Incorrect:**

**A. Google Cloud Dataproc** ❌

- **Not the best choice** because **Dataproc is a managed Hadoop/Spark service** that is more suitable for existing Spark/Hadoop workloads.
- The company **has no existing code**, so starting fresh with **Apache Beam (Dataflow) is more modern and flexible**.
- **Streaming support in Spark is limited** compared to Apache Beam’s unified batch and streaming model.

✅ **Reference:**

- **https://cloud.google.com/dataproc/docs/concepts/overview**

**C. Google Kubernetes Engine with Bigtable** ❌

- **Incorrect choice** because:
  - **GKE (Kubernetes) is an orchestration tool**, not a stream processing engine.
  - **Bigtable is a NoSQL database**, but the question requires **both batch and stream processing**, not just a database.
  - **More complex to implement** since a custom **Apache Kafka, Flink, or Spark Streaming** setup would be required.

✅ **Reference:**

- **https://cloud.google.com/kubernetes-engine/docs**

**D. Google Compute Engine with Google BigQuery** ❌

- **Not suitable** because Compute Engine requires **manual management of infrastructure**.
- **BigQuery is excellent for batch analytics**, but it does **not provide real-time stream processing** (BigQuery supports batch inserts, but streaming inserts are limited).
- **More effort required** to build a separate streaming pipeline compared to Dataflow, which natively supports streaming data.

✅ **Reference:**

- **https://cloud.google.com/bigquery/docs/loading-data-streaming**

**Conclusion:**

The best choice is **B. Google Cloud Dataflow**, because it:

- **Natively supports both batch and streaming data processing**.
- **Simplifies infrastructure management** compared to Kubernetes or Compute Engine.
- **Uses Apache Beam**, providing a unified programming model for real-time and batch jobs.

📌 **Final Reference:**
**https://cloud.google.com/dataflow/docs/concepts/streaming-with-dataflow**

---

## Question 12

*Domain 6: Ensuring Solution and Operations Excellence*

**A customer is receiving reports that their recently updated Google App Engine application is taking approximately 30 seconds to load for some users. This issue was not observed before the update. What approach should they take?**

- [ ] A. Collaborate with their ISP to diagnose the issue.
- [ ] B. Open a support ticket to request network capture and flow data for troubleshooting, then roll back the application.
- [x] C. Initially roll back to a previously stable release, then use Stackdriver Trace and Logging to investigate the issue in a development, test, or staging environment.
- [ ] D. Roll back to a previously stable release, redeploy the update during a lower-traffic period, and then use Stackdriver Trace and Logging to diagnose the issue.

### Explanation

**Correct Answer:**

**C. Initially roll back to a previously stable release, then use Stackdriver Trace and Logging to investigate the issue in a development, test, or staging environment.**

**Explanation:**

Since the **performance issue started after the update**, the best approach is to:

1. **Roll back to a previously stable release** to restore normal functionality for users.
2. **Use Google Cloud’s monitoring tools (Stackdriver Trace and Logging)** to investigate the root cause of the latency issue.
3. **Conduct debugging in a non-production environment** (development, test, or staging) to prevent further impact on users.

✅ **Why this is the best approach?**

- **Minimizes user impact** by quickly restoring a stable version.
- **Provides detailed latency analysis** using **Stackdriver Trace**.
- **Enables log-based debugging** to identify the problematic changes.
- **Prevents unnecessary redeployment** in production until the issue is resolved.

✅ **Supporting Documentation:**

- **Google Cloud Trace for latency analysis:**
  **https://cloud.google.com/trace/docs**
- **Logging for App Engine troubleshooting:**
  **https://cloud.google.com/appengine/docs/standard/python/logs**

**Why Other Options Are Incorrect:**

**A. Collaborate with their ISP to diagnose the issue.** ❌

- **Incorrect** because the **issue started after the update**, making it highly unlikely that an ISP-related issue is the cause.
- The **problem is likely in the application or backend**, not the network.

✅ **Reference:**

- **https://cloud.google.com/network-intelligence-center/docs/**

**B. Open a support ticket to request network capture and flow data for troubleshooting, then roll back the application.** ❌

- **Not the best approach initially** because:
  - The **issue is more likely in the application code or deployment configuration**, not at the network level.
  - **Rolling back is correct**, but **network capture is unnecessary** at this stage.
  - Google Cloud’s **Stackdriver Trace and Logging** are better tools to diagnose App Engine application latency.

✅ **Reference:**

- **https://cloud.google.com/trace/docs/overview**

**D. Roll back to a previously stable release, redeploy the update during a lower-traffic period, and then use Stackdriver Trace and Logging to diagnose the issue.** ❌

- **Partially correct**, but **redeploying the update before debugging is risky**.
- The issue should first be **investigated in a development/test environment** rather than redeploying directly in production.
- **Rolling back and diagnosing in a non-production environment is the best practice.**

✅ **Reference:**

- **https://cloud.google.com/appengine/docs/troubleshooting**

**Conclusion:**

The best approach is **C. Roll back to a stable release, then use Stackdriver Trace and Logging to investigate the issue in a test environment**.

- **Minimizes downtime** and **prevents further user impact**.
- **Uses Google Cloud’s built-in debugging tools** for efficient root cause analysis.
- **Ensures that the next update is stable before re-deploying to production.**

📌 **Final Reference:**
**https://cloud.google.com/trace/docs**

---

## Question 13

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**A production database virtual machine on Google Compute Engine uses an ext4-formatted persistent disk for storing data files. The database is approaching its storage limit. What is the best way to resolve this issue while minimizing downtime?**

- [x] A. Increase the size of the persistent disk in the Cloud Platform Console, then use the `resize2fs` command in Linux.
- [ ] B. Shut down the virtual machine, increase the persistent disk size in the Cloud Platform Console, and then restart the virtual machine.
- [ ] C. Increase the size of the persistent disk in the Cloud Platform Console and verify the newly allocated space using the `fdisk` command in Linux.
- [ ] D. Create a new persistent disk in the Cloud Platform Console, attach it to the virtual machine, format and mount it, and update the database configuration to store files on the new disk.
- [ ] E. Create a snapshot of the persistent disk in the Cloud Platform Console, restore the snapshot to a new, larger disk, unmount the old disk, mount the new disk, and restart the database service.

### Explanation

**Correct Answer:**

**A. Increase the size of the persistent disk in the Cloud Platform Console, then use the `resize2fs` command in Linux.**

**Explanation:**

The **best approach** to **increase storage while minimizing downtime** is:

1. **Resize the persistent disk** using the Google Cloud Console or `gcloud compute disks resize`.
2. **Expand the filesystem online using** `resize2fs` (for ext4 filesystems) without needing to unmount the disk or restart the VM.

✅ **Why this works best?**

- Google Cloud Persistent Disks **can be resized dynamically** without VM downtime.
- The **Linux `resize2fs` command** allows resizing an **ext4 filesystem online** without unmounting.
- **No need to restart the VM or database**, ensuring **minimal disruption** to production services.

✅ **Supporting Documentation:**

- **Resizing Persistent Disks on Compute Engine:**
  **https://cloud.google.com/compute/docs/disks/resize-persistent-disk**
- **Resizing ext4 partitions with `resize2fs`:**
  **https://man7.org/linux/man-pages/man8/resize2fs.8.html**

**Why Other Options Are Incorrect:**

**B. Shut down the virtual machine, increase the persistent disk size in the Cloud Platform Console, and then restart the virtual machine.** ❌

- **Incorrect because shutting down the VM is unnecessary.**
- Persistent Disks **can be resized while the VM is running**, and `resize2fs` can be run **without downtime**.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/disks/resize-persistent-disk**

**C. Increase the size of the persistent disk in the Cloud Platform Console and verify the newly allocated space using the fdisk command in Linux.** ❌

- **Incorrect because `fdisk` is used for partition management, not filesystem resizing.**
- For **ext4 filesystems,** `resize2fs` is the correct tool to extend the filesystem after resizing the disk.

✅ **Reference:**

- **https://linux.die.net/man/8/fdisk**

**D. Create a new persistent disk in the Cloud Platform Console, attach it to the virtual machine, format and mount it, and update the database configuration to store files on the new disk.** ❌

- **Not the most efficient solution** because:
  - It requires **database reconfiguration**, increasing complexity.
  - Existing data remains on the old disk, **potentially requiring data migration**.
  - A **simpler, non-disruptive** approach is to **resize the existing disk**.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/disks/add-persistent-disk**

**E. Create a snapshot of the persistent disk in the Cloud Platform Console, restore the snapshot to a new, larger disk, unmount the old disk, mount the new disk, and restart the database service.** ❌

- **Not the best approach** because:
  - **Unnecessary downtime** due to snapshot restoration and remounting.
  - **More complex than simply resizing the existing disk**.
  - **Snapshots are primarily for backups** rather than live disk expansion.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/disks/create-snapshots**

**Conclusion:**

The best way to expand storage **without downtime** is:

1. **Increase the size of the persistent disk** in Google Cloud Console (`gcloud compute disks resize`).
2. **Use** `resize2fs` to extend the ext4 filesystem **without unmounting the disk or restarting the VM**.

📌 **Final Reference:**
**https://cloud.google.com/compute/docs/disks/resize-persistent-disk**

---

## Question 14

*Domain 3: Designing for Security and Compliance*

**Your application is required to process credit card transactions. To minimize the scope of Payment Card Industry (PCI) compliance while still allowing analysis of transactional data and payment trends, how should you design your architecture?**

- [x] A. Implement a **tokenization service** and store only tokenized data.
- [ ] B. Use **separate projects** exclusively for processing credit card data.
- [ ] C. Configure **separate subnetworks** to isolate components handling credit card data.
- [ ] D. Simplify the **audit discovery process** by labeling all virtual machines (VMs) that handle PCI data.
- [ ] E. **Export logs to Google BigQuery** and use **ACLs and views** to control data access for auditors.

### Explanation

**Correct Answer:**

**A. Implement a tokenization service and store only tokenized data.**

**Explanation:**

To **minimize the scope of PCI compliance** while still allowing **transactional analysis**, the best practice is to **implement tokenization**.

- **Tokenization replaces sensitive credit card data** (PANs) with **non-sensitive tokens**.
- The **actual credit card data is never stored** in databases or logs, significantly reducing **PCI DSS scope**.
- Transactional data and payment trends can be **analyzed using tokenized values** while maintaining security.
- Google Cloud provides **Cloud Data Loss Prevention (DLP)** and **third-party tokenization solutions** that help achieve this.

✅ **Supporting Documentation:**

- **Google Cloud PCI Compliance Guide:**
  **https://cloud.google.com/security/compliance/pci-dss**
- **Tokenization and Encryption for PCI DSS Compliance:**
  **https://cloud.google.com/security/articles/tokenization-and-encryption**

**Why Other Options Are Incorrect:**

**B. Use separate projects exclusively for processing credit card data.** ❌

- **While separate projects improve isolation**, they do **not reduce PCI compliance scope**.
- If credit card data is **stored or processed**, **all components must comply with PCI DSS**, regardless of project separation.
- **Tokenization is a better approach** because it eliminates the need to store credit card numbers at all.

✅ **Reference:**

- **https://cloud.google.com/security/compliance/pci-dss**

**C. Configure separate subnetworks to isolate components handling credit card data.** ❌

- **Network segmentation helps limit PCI scope**, but it does **not eliminate the storage of sensitive data**.
- **PCI DSS still applies** to all **in-scope** network segments, requiring extensive auditing and security controls.
- Tokenization is **more effective in reducing compliance scope** than just network isolation.

✅ **Reference:**

- **https://cloud.google.com/architecture/framework/security/design-secure-networks**

**D. Simplify the audit discovery process by labeling all virtual machines (VMs) that handle PCI data.** ❌

- **Labeling VMs is helpful for tracking, but it does not minimize PCI scope.**
- If a VM processes **actual credit card data**, it **remains in PCI scope** regardless of labels.
- Tokenization **removes the need to store PCI-sensitive data**, reducing compliance burden.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/labeling-resources**

**E. Export logs to Google BigQuery and use ACLs and views to control data access for auditors.** ❌

- **BigQuery ACLs and views help with access control**, but they do **not reduce PCI compliance scope**.
- If **credit card numbers (PANs) are stored in logs or BigQuery**, **PCI DSS still applies**.
- Tokenization prevents **sensitive data from being stored** in logs or analytics tools.

✅ **Reference:**

- **https://cloud.google.com/bigquery/docs/reference/standard-sql/security**

**Conclusion:**

The best approach is **A. Implement a tokenization service and store only tokenized data**, because:

- **PCI-sensitive data is never stored**, minimizing compliance scope.
- **Transaction analysis remains possible** using tokenized values.
- **Security and audit complexity are significantly reduced**.

📌 **Final Reference:**
**https://cloud.google.com/security/articles/tokenization-and-encryption**

---

## Question 15

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**You need to choose a storage system for handling clickstream data from your company's large portfolio of websites. The data is streamed from a custom website analytics package at an average rate of 6,000 clicks per minute, with spikes reaching 8,500 clicks per second. The data must be stored for future analysis by the data science and user experience teams. Which storage infrastructure should you use?**

- [ ] A. Google Cloud SQL
- [x] B. Google Cloud Bigtable
- [ ] C. Google Cloud Storage
- [ ] D. Google Cloud Datastore

### Explanation

**Correct Answer:**

**B. Google Cloud Bigtable**

**Explanation:**

Google Cloud **Bigtable** is the best choice for handling **high-volume, high-throughput** clickstream data because:

- **Designed for real-time analytics and time-series data:** Bigtable is optimized for handling large-scale, **time-series data**, making it ideal for **clickstream analytics**.
- **Scalability:** It **scales seamlessly** to handle **8,500+ clicks per second**, meeting peak traffic demands.
- **Low-latency writes and high throughput:** Bigtable supports **millions of writes per second**, ensuring efficient ingestion of clickstream events.
- **Native integration with analytics tools:** Bigtable integrates with **BigQuery and Dataflow**, enabling efficient data processing and analysis.
- **Optimized for large datasets:** Unlike relational databases, Bigtable can handle **terabytes to petabytes** of structured, semi-structured, or unstructured data efficiently.

✅ **Supporting Documentation:**

- **Cloud Bigtable Overview:**
  **https://cloud.google.com/bigtable/docs/overview**
- **Bigtable for Real-Time Analytics:**
  **https://cloud.google.com/architecture/real-time-analytics-with-bigtable**

**Why Other Options Are Incorrect:**

**A. Google Cloud SQL** ❌

- **Not designed for high-volume, real-time ingestion** (supports up to **64 TB**).
- **Limited scalability**—relational databases struggle with time-series clickstream data.
- **More expensive and slower** compared to Bigtable for streaming analytics workloads.

✅ **Reference:**

- **https://cloud.google.com/sql/docs/introduction**

**C. Google Cloud Storage** ❌

- **Good for long-term storage**, but **not optimized for real-time ingestion**.
- **Cannot efficiently handle structured queries** without additional processing (e.g., using BigQuery).
- **Higher latency for real-time data retrieval** compared to Bigtable.

✅ **Reference:**

- **https://cloud.google.com/storage/docs/**

**D. Google Cloud Datastore** ❌

- **Designed for transactional, NoSQL document storage**, not high-speed time-series ingestion.
- **Limited scalability for write-heavy workloads** compared to Bigtable.
- **Not optimized for real-time analytics**.

✅ **Reference:**

- **https://cloud.google.com/datastore/docs/concepts/overview**

**Conclusion:**

The best choice is **B. Google Cloud Bigtable**, because:

- **Handles high-throughput, real-time data ingestion (8,500 clicks/sec)**.
- **Scales efficiently for time-series and clickstream analytics**.
- **Integrates seamlessly with BigQuery for future analysis**.

📌 **Final Reference:**
**https://cloud.google.com/bigtable/docs/overview**

---

## Question 16

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**You need to implement a solution to automatically delete backup files older than 90 days from your Cloud Storage bucket while optimizing ongoing storage costs. What should you do?**

- [ ] A. Define a **lifecycle management rule** in **XML** and apply it to the bucket using `gsutil`.
- [x] B. Define a **lifecycle management rule** in **JSON** and apply it to the bucket using `gsutil`.
- [ ] C. Schedule a **cron job** that runs a script using `gsutil ls -lr gs://backups/**` to find and delete files older than 90 days.
- [ ] D. Schedule a **cron job** that runs a script using `gsutil ls -l gs://backups/**` to find and delete files older than 90 days.

### Explanation

**Correct Answer:**

**B. Define a lifecycle management rule in JSON and apply it to the bucket using gsutil.**

**Explanation:**

Google Cloud Storage **Lifecycle Management** allows you to **automate the deletion of backup files older than 90 days**, ensuring:

- **Automatic cleanup** without manual intervention.
- **Optimized storage costs** by reducing long-term storage usage.
- **Policy-based enforcement** that does not require additional scripts or cron jobs.

**Steps to Implement:**

1. Create a **JSON lifecycle policy**:
  ```
  {  "rule": [    {      "action": {"type": "Delete"},      "condition": {"age": 90}    }  ]}
  ```
2. Apply the policy to the bucket using **gsutil**:
  ```
  gsutil lifecycle set lifecycle.json gs://your-bucket-name
  ```
3. Verify the policy:
  ```
  gsutil lifecycle get gs://your-bucket-name
  ```

✅ **Supporting Documentation:**

- **Google Cloud Storage Lifecycle Management**
  **https://cloud.google.com/storage/docs/lifecycle**
- **Using gsutil for lifecycle policies**
  **https://cloud.google.com/storage/docs/gsutil/commands/lifecycle**

**Why Other Options Are Incorrect:**

**A. Define a lifecycle management rule in XML and apply it to the bucket using gsutil.** ❌

- `gsutil lifecycle set` (and today `gcloud storage buckets update --lifecycle-file`) takes a **JSON** file. XML lifecycle documents exist only for the Cloud Storage XML API, not for these tools.

✅ **Reference:**

- **https://cloud.google.com/storage/docs/lifecycle#configuration**

**C. Schedule a cron job that runs a script using `gsutil ls -lr gs://backups/**` to find and delete files older than 90 days.** ❌

- **Inefficient and unnecessary** when **Cloud Storage lifecycle policies** can handle this automatically.
- Running a script **adds operational overhead** and **increases potential failure points**.
- **Recursive listing (`-lr`) is redundant**, as `gsutil` does not require recursion for finding objects.

✅ **Reference:**

- **https://cloud.google.com/storage/docs/gsutil/commands/ls**

**D. Schedule a cron job that runs a script using `gsutil ls -l gs://backups/**` to find and delete files older than 90 days.** ❌

- Similar to **Option C**, this **manual script approach** is **unnecessary**.
- **Lifecycle rules** are **more reliable** than cron-based deletion scripts.

✅ **Reference:**

- **https://cloud.google.com/storage/docs/lifecycle**

**Conclusion:**

The best approach is **B. Define a lifecycle management rule in JSON and apply it to the bucket using gsutil**, as it:

- **Automates deletion** of files older than 90 days.
- **Optimizes storage costs** without manual intervention.
- **Follows Google Cloud best practices** for object lifecycle management.

📌 **Final Reference:**
**https://cloud.google.com/storage/docs/lifecycle**

**⚠️ Note:** `gsutil` is now legacy; the current command is `gcloud storage buckets update gs://BUCKET --lifecycle-file=FILE.json`. The answer (a JSON lifecycle rule with `age: 90` and a Delete action) is unchanged.

---

## Question 17

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**Your company is expecting a significant increase in the number and size of Apache Spark and Hadoop jobs running in its on-premises data center. To handle this growing demand, you want to leverage the cloud while minimizing operational overhead and code modifications. Which Google Cloud product should you use?**

- [ ] A. Google Cloud Dataflow
- [x] B. Google Cloud Dataproc
- [ ] C. Google Compute Engine
- [ ] D. Google Kubernetes Engine

### Explanation

**Correct Answer:**

**B. Google Cloud Dataproc**

**Explanation:**

Google Cloud **Dataproc** is the best solution for **migrating Apache Spark and Hadoop jobs** from an on-premises data center to the cloud while **minimizing operational overhead and code modifications**.

✅ **Key Benefits of Dataproc:**

- **Fully managed Hadoop and Spark service** that runs on Google Cloud.
- **Minimal changes to existing code**: Dataproc is **compatible with Apache Spark, Hadoop, Hive, and Pig**, meaning **existing jobs can run with little to no modifications**.
- **Autoscaling and ephemeral clusters**: Reduces operational costs by **spinning up clusters only when needed**.
- **Seamless integration with cloud storage and analytics tools**, such as **Cloud Storage, BigQuery, and Dataflow**.
- **Optimized performance** with **faster cluster startup times** (in seconds to minutes, compared to on-premises clusters taking hours).

✅ **Supporting Documentation:**

- **Migrating from On-Premises Hadoop to Google Cloud Dataproc:**
  **https://cloud.google.com/dataproc/docs/concepts/migrate-on-prem**
- **Dataproc Overview:**
  **https://cloud.google.com/dataproc**

**Why Other Options Are Incorrect:**

**A. Google Cloud Dataflow** ❌

- **Incorrect because Dataflow is for stream and batch data processing** using Apache Beam, not **Spark or Hadoop clusters**.
- Would require **rewriting Spark and Hadoop jobs** in Apache Beam, which increases complexity.

✅ **Reference:**

- **https://cloud.google.com/dataflow/docs/concepts/streaming-with-dataflow**

**C. Google Compute Engine** ❌

- **Not the best choice** because it requires **manually provisioning and managing Hadoop clusters**, leading to **higher operational overhead**.
- Dataproc **automates cluster management**, whereas **Compute Engine would require manual setup and scaling**.

✅ **Reference:**

- **https://cloud.google.com/compute**

**D. Google Kubernetes Engine** ❌

- **Incorrect because Kubernetes is designed for containerized applications, not native Hadoop/Spark jobs.**
- Running Hadoop or Spark on Kubernetes requires **significant re-architecting** and does not offer the same level of **native integration** as Dataproc.

✅ **Reference:**

- **https://cloud.google.com/kubernetes-engine/docs**

**Conclusion:**

The best choice is **B. Google Cloud Dataproc**, as it:

- **Provides a fully managed Spark and Hadoop environment**.
- **Requires minimal code changes** for on-premises migration.
- **Reduces operational overhead** with autoscaling and ephemeral clusters.

📌 **Final Reference:**
**https://cloud.google.com/dataproc/docs/concepts/migrate-on-prem**

---

## Question 18

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**The database administration team needs your assistance in improving the performance of their new MySQL database server running on Google Compute Engine. The database is used for importing and normalizing performance statistics and is hosted on a Debian Linux virtual machine with an n1-standard-8 configuration and 80 GB of SSD persistent disk. What should they modify to enhance performance?**

- [ ] A. Increase the virtual machine’s memory to **64 GB**.
- [ ] B. Create a new virtual machine running **PostgreSQL** instead of MySQL.
- [x] C. Dynamically resize the **SSD persistent disk** to **500 GB**.
- [ ] D. Migrate the performance metrics warehouse to **BigQuery**.
- [x] E. Optimize batch jobs to use **bulk inserts** into the database.

### Explanation

**Correct Answer:**

**C. Dynamically resize the SSD persistent disk to 500 GB.**
**E. Optimize batch jobs to use bulk inserts into the database.**

**Explanation:**

To improve **MySQL performance on Google Compute Engine**, two key optimizations are required:

1. **Resize the SSD persistent disk to 500 GB (`Option C`)**
  - **Google SSD persistent disks offer higher IOPS with increased disk size.**
  - SSD persistent disk IOPS are a 6,000 baseline plus 30 per GB: an **80 GB disk gets about 8,400 IOPS**, a **500 GB disk about 21,000 IOPS** (both capped by the VM's own limit), significantly improving **read/write performance**.
  - **MySQL benefits from higher disk throughput**, especially for **large-scale data imports and query processing**.
  - Google allows **dynamic disk resizing without downtime**, meaning this change can be applied immediately.
  ✅ **Supporting Documentation:**
  - **Google Cloud SSD Persistent Disk Performance**
    **https://cloud.google.com/compute/docs/disks/performance**
  - **Resizing persistent disks in Google Cloud**
    **https://cloud.google.com/compute/docs/disks/resize-persistent-disk**
2. **Optimize batch jobs to use bulk inserts into the database (`Option E`)**
  - **Bulk inserts reduce the number of disk writes** and **minimize transaction overhead**, leading to **faster import and normalization of performance data**.
  - **MySQL performs better when data is inserted in large batches** instead of multiple individual insert statements.
  - Using `INSERT ... VALUES (...), (...)` or `LOAD DATA INFILE` significantly improves insert speeds.
  ✅ **Supporting Documentation:**
  - **Optimizing MySQL Performance for Batch Inserts**
    [**https://dev.mysql.com/doc/refman/8.0/en/insert-optimization.html**](https://dev.mysql.com/doc/refman/8.0/en/insert-optimization.html)
  - **MySQL Bulk Insert Best Practices**
    **https://cloud.google.com/sql/docs/mysql/import-export/importing**

**Why Other Options Are Incorrect:**

**A. Increase the virtual machine’s memory to 64 GB.** ❌

- While **more memory can improve query caching**, this is **not the primary bottleneck** in this case.
- The **current n1-standard-8 VM** already provides **30 GB RAM**, which is sufficient for MySQL **unless monitoring indicates high memory usage**.
- **Storage and query optimization are more impactful** for performance improvements in this scenario.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/machine-types**

**B. Create a new virtual machine running PostgreSQL instead of MySQL.** ❌

- **Migrating to PostgreSQL does not inherently improve performance**—both databases have similar capabilities for large-scale data ingestion.
- Migration requires **significant rework**, which is **not a practical solution for immediate performance improvement**.

✅ **Reference:**

- **https://cloud.google.com/sql/docs/postgres**

**D. Migrate the performance metrics warehouse to BigQuery.** ❌

- **BigQuery is optimized for analytical queries, not for transactional workloads like MySQL.**
- If the database is **used for normalizing transactional data**, BigQuery is **not a direct replacement**—instead, **MySQL tuning is required**.

✅ **Reference:**

- **https://cloud.google.com/bigquery/docs/introduction**

**Conclusion:**

To **improve MySQL performance** on Google Compute Engine:

1. **Increase the SSD persistent disk size to 500 GB (`Option C`)** for better **IOPS and disk performance**.
2. **Optimize batch jobs to use bulk inserts (`Option E`)** to **minimize transaction overhead** and **speed up data imports**.

📌 **Final References:**

- **https://cloud.google.com/compute/docs/disks/performance**
- [**https://dev.mysql.com/doc/refman/8.0/en/insert-optimization.html**](https://dev.mysql.com/doc/refman/8.0/en/insert-optimization.html)

---

## Question 19

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**You need to optimize the performance of a **real-time weather-charting application** that requires high accuracy. The data is generated by **50,000 sensors**, each sending **10 readings per second** in the format of a **timestamp and sensor reading**. Where should this data be stored?**

- [ ] A. Google BigQuery
- [ ] B. Google Cloud SQL
- [x] C. Google Cloud Bigtable
- [ ] D. Google Cloud Storage

### Explanation

**Correct Answer:**

**C. Google Cloud Bigtable**

**Explanation:**

Google **Cloud Bigtable** is the best choice for a **real-time weather-charting application** with **high accuracy** because:

- **Optimized for high-speed, time-series data**: Handles **millions of writes per second**, making it ideal for **50,000 sensors sending 10 readings per second** (i.e., **500,000 writes per second**).
- **Low-latency reads and writes**: Ensures that **real-time data processing** and chart updates happen with minimal delay.
- **Columnar storage for scalability**: Supports **efficient queries** on **timestamp-based data**, which is critical for weather monitoring.
- **Schema-less design**: Allows storing **variable attributes** and new sensor data formats **without schema modifications**.
- **Native integration with Apache Beam and BigQuery** for real-time and batch analytics.

✅ **Supporting Documentation:**

- **Cloud Bigtable for time-series data:**
  **https://cloud.google.com/bigtable/docs/schema-design-time-series**
- **Real-time analytics with Bigtable:**
  **https://cloud.google.com/architecture/real-time-analytics-with-bigtable**

**Why Other Options Are Incorrect:**

**A. Google BigQuery** ❌

- **BigQuery is designed for batch analytics**, not real-time ingestion.
- **Not optimized for low-latency, high-throughput writes** (limited to ~100,000 rows per second).
- **Better suited for historical analysis** rather than continuous real-time updates.

✅ **Reference:**

- **https://cloud.google.com/bigquery/docs/loading-data-streaming**

**B. Google Cloud SQL** ❌

- **Cloud SQL (MySQL/PostgreSQL) cannot handle 500,000 writes per second efficiently.**
- **Not optimized for real-time, high-ingest workloads**; better suited for **transactional OLTP workloads**.
- **Strict relational schema makes handling variable sensor readings difficult**.

✅ **Reference:**

- **https://cloud.google.com/sql/docs/introduction**

**D. Google Cloud Storage** ❌

- **Object storage, not a real-time database.**
- **Designed for storing files (logs, backups, images, videos), not structured sensor data.**
- **No built-in indexing or query capabilities** for fast lookups on time-series data.

✅ **Reference:**

- **https://cloud.google.com/storage/docs/**

**Conclusion:**

The best choice is **C. Google Cloud Bigtable**, as it:

- **Handles high-frequency sensor readings with low latency**.
- **Supports scalable, time-series data ingestion and retrieval**.
- **Optimizes performance for real-time applications** like weather charting.

📌 **Final Reference:**
**https://cloud.google.com/bigtable/docs/schema-design-time-series**

---

## Question 20

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

**Your company's user-feedback portal runs on a standard LAMP stack replicated across two zones in the us-central1 region. It is deployed using autoscaled managed instance groups for all layers except the database. Currently, only a small group of selected customers have access, and the portal meets a 99.99% availability SLA under these conditions.**

**Next quarter, the portal will be opened to all users, including unauthenticated users. To ensure the system maintains its SLA under increased load, you need to develop a resiliency testing strategy. What approach should you take?**

- [ ] A. Capture existing user input and **replay the recorded user load** until autoscaling is triggered on all layers. Simultaneously, terminate all resources in one of the zones.
- [ ] B. Generate **synthetic random user input**, replay the synthetic load until **autoscaling logic** is triggered on at least one layer, and introduce **chaos** by randomly terminating resources in both zones.
- [x] C. Gradually **increase the exposure** of the new system to a larger user group, expanding the group daily until autoscaling is triggered on all layers. At the same time, terminate random resources in both zones.
- [ ] D. Capture existing user input, **replay the recorded load** until resource utilization exceeds **80%**, estimate the expected number of users based on current usage patterns, and provision enough resources to handle **200% of the projected load**.

### Explanation

**Correct Answer:**

**C. Gradually increase the exposure of the new system to a larger user group, expanding the group daily until autoscaling is triggered on all layers. At the same time, terminate random resources in both zones.**

**Explanation:**

To **ensure 99.99% availability under increased load**, a **gradual rollout strategy** combined with **resiliency testing** is the best approach.

✅ **Why This Works:**

1. **Controlled Traffic Increase**: Gradually expanding user access allows for **monitoring and scaling adjustments** before full exposure.
2. **Observing Autoscaling Behavior**: Ensures that **autoscaling works as expected** across all layers before full public access.
3. **Resiliency Testing via Chaos Engineering**:
  - **Randomly terminating resources** tests fault tolerance and ensures that the system **handles failures gracefully**.
  - **Multi-zone replication** ensures availability despite failures in one zone.
4. **Prevents Overprovisioning**: Instead of blindly **provisioning 200% capacity**, this method allows **dynamic scaling based on real-world traffic patterns**.

✅ **Supporting Documentation:**

- **Google Cloud Autoscaling Best Practices:**
  **https://cloud.google.com/compute/docs/autoscaler**
- **Chaos Engineering on Google Cloud:**
  **https://cloud.google.com/blog/products/management-tools/chaos-engineering-and-google-cloud**

**Why Other Options Are Incorrect:**

**A. Capture existing user input and replay the recorded user load until autoscaling is triggered on all layers. Simultaneously, terminate all resources in one of the zones.** ❌

- **Why Incorrect?**
  - **Capturing existing user input is good for load testing**, but the **traffic profile changes when access is expanded to all users**.
  - **Immediately terminating an entire zone** is **too extreme** and **not realistic** for gradual traffic expansion.
  - The **gradual rollout strategy (Option C) is safer and better aligns with real-world production conditions**.

✅ **Reference:**

- **https://cloud.google.com/architecture/scalable-and-resilient-applications**

**B. Generate synthetic random user input, replay the synthetic load until autoscaling logic is triggered on at least one layer, and introduce chaos by randomly terminating resources in both zones.** ❌

- **Why Incorrect?**
  - **Synthetic load** is **less accurate** than gradually **expanding real user traffic**.
  - **Chaos engineering is important**, but it should be introduced **gradually**, not as the **primary focus**.
  - **Real user behavior is critical for autoscaling validation**, making **Option C a better choice**.

✅ **Reference:**

- **https://cloud.google.com/architecture/chaos-engineering-on-google-cloud**

**D. Capture existing user input, replay the recorded load until resource utilization exceeds 80%, estimate the expected number of users based on current usage patterns, and provision enough resources to handle 200% of the projected load.** ❌

- **Why Incorrect?**
  - **Overprovisioning resources is not cost-efficient** and **does not ensure autoscaling is working properly**.
  - **Traffic patterns will change** once unauthenticated users access the portal, making projections **unreliable**.
  - **Google Cloud autoscaler dynamically scales resources**, making **pre-provisioning unnecessary**.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/autoscaler**

**Conclusion:**

The best approach is **C. Gradually increase user exposure while monitoring autoscaling and performing resiliency testing**. This method:

- **Validates real-world autoscaling behavior**.
- **Avoids sudden failures from excessive chaos testing**.
- **Ensures high availability while efficiently scaling resources**.

📌 **Final Reference:**
**https://cloud.google.com/architecture/scalable-and-resilient-applications**

---

## Question 21

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

**Your solution is encountering **performance issues in production** that were not observed in **staging or test environments**. You need to refine your **testing and deployment** procedures to **prevent this issue in the future**. What should you do?**

- [ ] A. Reduce the number of changes deployed to production.
- [ ] B. Deploy smaller, incremental changes to production.
- [ ] C. Increase the load on your **test and staging** environments.
- [x] D. Gradually deploy changes to a **small subset of users** before rolling out to production.

### Explanation

**Correct Answer:**

**D. Gradually deploy changes to a small subset of users before rolling out to production.**

**Explanation:**

To prevent **performance issues in production**, the best approach is to implement a **gradual rollout strategy**, also known as **canary releases** or **progressive delivery**.

✅ **Why This Works:**

- **Minimizes risk:** Deploying changes to a **small subset of users** first allows **early detection of issues** before affecting all users.
- **Real-world traffic testing:** Unlike staging or test environments, production users generate **actual workloads and edge cases** that may not have been captured in testing.
- **Fast rollback mechanism:** If issues are detected, the deployment can be **paused or rolled back** before a full rollout.
- **Automated monitoring & feedback:** Tools like **Stackdriver (Cloud Monitoring, Logging, and Trace)** help track **latency, error rates, and performance metrics** during gradual deployment.

✅ **Best Practices for Gradual Rollout:**

- **Use feature flags** (e.g., LaunchDarkly) to control feature exposure.
- **Deploy changes to a percentage of users** before full release.
- **Monitor performance metrics before continuing rollout.**

✅ **Supporting Documentation:**

- **Google Cloud Canary Deployment Guide:**
  **https://cloud.google.com/architecture/application-deployment-and-testing-strategies**

**Why Other Options Are Incorrect:**

**A. Reduce the number of changes deployed to production.** ❌

- **Incorrect because reducing changes does not address the root cause of performance issues.**
- **Even small changes can introduce issues if not tested properly in a production-like environment.**
- The **real problem is insufficient production-level testing**, not the volume of changes.

✅ **Reference:**

- **https://cloud.google.com/architecture/application-deployment-and-testing-strategies**

**B. Deploy smaller, incremental changes to production.** ❌

- **Smaller changes are beneficial but do not prevent performance issues alone.**
- **Gradual rollout (Option D) is still needed** to test changes in production conditions before full deployment.
- **Incremental changes help debugging but do not guarantee real-world performance testing.**

✅ **Reference:**

- **https://cloud.google.com/architecture/devops/devops-tech-continuous-deployment**

**C. Increase the load on your test and staging environments.** ❌

- **Test and staging environments cannot fully replicate production workloads.**
- Even if you simulate high traffic, **real user behavior and production-specific configurations** may differ.
- **Canary releases (Option D) provide a more reliable way to test in a live environment.**

✅ **Reference:**

- **https://cloud.google.com/architecture/application-deployment-and-testing-strategies**

**Conclusion:**

The best approach is **D. Gradually deploy changes to a small subset of users before rolling out to production**, as it:

- **Identifies performance issues in real-world conditions.**
- **Reduces risk before full rollout.**
- **Allows monitoring and quick rollback if issues arise.**

📌 **Final Reference:**
**https://cloud.google.com/architecture/application-deployment-and-testing-strategies**

---

## Question 22

*Domain 6: Ensuring Solution and Operations Excellence*

**A **small percentage of API requests** in your **microservices-based application** are experiencing **high latency**. Each request may pass through multiple services, and you need to identify which service is causing the delay. What should you do?**

- [ ] A. Configure timeouts in your application to fail slow requests more quickly.
- [ ] B. Send **custom metrics** for each request to **Stackdriver Monitoring**.
- [ ] C. Use **Stackdriver Monitoring** to analyze insights when API latency is high.
- [x] D. **Instrument your application with Stackdriver Trace** to break down request latencies across microservices.

### Explanation

**Correct Answer:**

**D. Instrument your application with Stackdriver Trace to break down request latencies across microservices.**

**Explanation:**

In a **microservices-based application**, where **each request may pass through multiple services**, **latency issues can originate from different components**.

✅ **Google Cloud’s Stackdriver Trace (Cloud Trace) is the best solution because:**

- It **tracks request flows across microservices**, helping **pinpoint the exact service** causing the delay.
- It provides **detailed latency breakdowns** for each API request.
- It helps **identify performance bottlenecks** in dependencies like **databases, caches, or external services**.
- **Automatically integrates with GKE, Compute Engine, App Engine, and Cloud Run.**

**How It Works:**

1. **Instrument your services** with **Stackdriver Trace SDKs** (or use built-in integration for Google Cloud services).
2. Each request generates a **trace ID** that follows the request **across all microservices**.
3. Use **Stackdriver Trace UI** to analyze end-to-end request latency and identify **slow services or operations**.

✅ **Supporting Documentation:**

- **Google Cloud Trace Overview:**
  **https://cloud.google.com/trace/docs/**
- **Distributed Tracing for Microservices:**
  **https://cloud.google.com/blog/topics/developers-practitioners/distributed-tracing-microservices-google-cloud**

**Why Other Options Are Incorrect:**

**A. Configure timeouts in your application to fail slow requests more quickly.** ❌

- **Timeouts help mitigate latency issues** but do **not diagnose the root cause** of high-latency services.
- Without identifying **which service is slow**, adding timeouts can **lead to unnecessary failures and degraded user experience**.

✅ **Reference:**

- **https://cloud.google.com/architecture/microservices-timeouts-retries**

**B. Send custom metrics for each request to Stackdriver Monitoring.** ❌

- **Metrics provide aggregated latency data**, but they **do not show per-request breakdowns across microservices**.
- Stackdriver Monitoring **does not provide trace-level visibility** like Stackdriver Trace.

✅ **Reference:**

- **https://cloud.google.com/monitoring/docs/**

**C. Use Stackdriver Monitoring to analyze insights when API latency is high.** ❌

- **Stackdriver Monitoring detects latency spikes but does not trace requests across microservices.**
- **Stackdriver Trace is required** for **end-to-end request latency analysis**.

✅ **Reference:**

- **https://cloud.google.com/monitoring/docs/overview**

**Conclusion:**

The best approach is **D. Instrument your application with Stackdriver Trace** to analyze **end-to-end request latency** across microservices.

- **Pinpoints slow microservices.**
- **Provides real-time tracing insights.**
- **Helps optimize API performance.**

📌 **Final Reference:**
**https://cloud.google.com/trace/docs/**

---

## Question 23

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

**During a **high-traffic period**, one of your **relational databases** crashes, but the **replica is never promoted to master**. You want to prevent this issue from happening again in the future. What should you do?**

- [ ] A. Switch to a different database.
- [ ] B. Use larger instance sizes for the database.
- [ ] C. Increase the frequency of database snapshots.
- [x] D. Implement **routinely scheduled failovers** for your databases.

### Explanation

**Correct Answer:**

**D. Implement routinely scheduled failovers for your databases.**

**Explanation:**

To ensure **high availability and automatic failover** for relational databases, **routinely scheduled failover testing** is essential. This ensures that **replica promotion** works as expected during high-traffic periods or failures.

✅ **Why This Works:**

- **Regular failover tests validate automatic promotion** of replicas, ensuring the process works during actual failures.
- **Helps identify misconfigurations** in failover mechanisms, such as **missing IAM permissions or misconfigured replication settings**.
- **Prevents downtime during real failures** by ensuring **read replicas can be promoted to primary**.
- **Google Cloud SQL, Cloud Spanner, and other managed relational databases support automated failover testing.**

✅ **Supporting Documentation:**

- **High Availability for Cloud SQL:**
  **https://cloud.google.com/sql/docs/mysql/high-availability**
- **Testing Cloud SQL Failover:**
  **https://cloud.google.com/sql/docs/mysql/failover**

**Why Other Options Are Incorrect:**

**A. Switch to a different database.** ❌

- **Changing the database is not necessary**—Google Cloud SQL, Cloud Spanner, and self-managed databases **already support failover**.
- **The issue is likely a misconfiguration or untested failover process**, not the database itself.
- **Fixing failover procedures is a better solution than migrating databases.**

✅ **Reference:**

- **https://cloud.google.com/sql/docs/mysql/replication**

**B. Use larger instance sizes for the database.** ❌

- **Scaling the database may improve performance but does not guarantee failover works correctly.**
- **Failover is unrelated to instance size**—a misconfigured failover will still fail, even with larger instances.
- **High availability and replication settings are more critical than instance size.**

✅ **Reference:**

- **https://cloud.google.com/sql/docs/mysql/instance-settings**

**C. Increase the frequency of database snapshots.** ❌

- **Snapshots help with backups but do not prevent failover issues.**
- **Snapshots do not provide real-time failover**—they are used for recovery, which can lead to **downtime during restoration**.
- **Failover should be handled via automated replica promotion, not snapshots.**

✅ **Reference:**

- **https://cloud.google.com/sql/docs/mysql/backup-recovery/backups**

**Conclusion:**

The best solution is **D. Implement routinely scheduled failovers**, as it:

- **Ensures automatic failover works as expected**.
- **Prevents downtime during real failures**.
- **Identifies and resolves failover misconfigurations in advance**.

📌 **Final Reference:**
**https://cloud.google.com/sql/docs/mysql/failover**

---

## Question 24

*Domain 3: Designing for Security and Compliance*

**Your organization requires that application metrics be retained for 5 years to support potential legal proceedings in the future. Which approach should you take?**

- [ ] A. Grant the security team access to logs in each project.
- [ ] B. Configure **Stackdriver Monitoring** for all projects and export the data to **BigQuery**.
- [ ] C. Configure **Stackdriver Monitoring** for all projects using the **default retention policies**.
- [x] D. Configure **Stackdriver Monitoring** for all projects and export the data to **Google Cloud Storage**.

### Explanation

**Correct Answer:**

**D. Configure Stackdriver Monitoring for all projects and export the data to Google Cloud Storage.**

**Explanation:**

Google Cloud **operations suite (formerly Stackdriver Monitoring)** retains **metrics data only for a limited period** (e.g., 6 weeks for free-tier users and up to 24 months for premium tiers). Since your organization requires metrics retention for **5 years**, exporting the data is necessary.

✅ **Why Export to Google Cloud Storage?**

- **Cloud Storage is designed for long-term archival storage** and supports **lifecycle policies for cost optimization**.
- **Supports regulatory compliance** and long-term legal retention requirements.
- **More cost-effective for long-term storage** compared to BigQuery, which incurs query costs.
- **Stackdriver Monitoring provides native integration** for exporting metrics to Cloud Storage.

✅ **Supporting Documentation:**

- **Cloud Monitoring Retention Periods:**
  **https://cloud.google.com/monitoring/quotas**
- **Exporting Monitoring Data to Cloud Storage:**
  **https://cloud.google.com/monitoring/docs/export**

**Why Other Options Are Incorrect:**

**A. Grant the security team access to logs in each project.** ❌

- **Incorrect because access control does not extend data retention.**
- **Security team access does not guarantee compliance** with long-term storage policies.
- **Cloud Monitoring metrics expire after their retention period** unless explicitly exported.

✅ **Reference:**

- **https://cloud.google.com/iam/docs/understanding-roles**

**B. Configure Stackdriver Monitoring for all projects and export the data to BigQuery.** ❌

- **BigQuery is a powerful analytics tool, but it incurs storage and query costs.**
- **Not the best option for long-term archival storage**—Google Cloud Storage is more suitable for compliance-driven retention.
- **BigQuery is better suited for querying structured data**, not raw metric storage.

✅ **Reference:**

- **https://cloud.google.com/bigquery/docs/introduction**

**C. Configure Stackdriver Monitoring for all projects using the default retention policies.** ❌

- **Cloud Monitoring's default retention policies do not meet the 5-year requirement.**
- **Free-tier users get only 6 weeks of metric retention**, while premium users get up to 24 months.
- **Without exporting data, it will be permanently lost after the retention period expires.**

✅ **Reference:**

- **https://cloud.google.com/monitoring/quotas**

**Conclusion:**

The best approach is **D. Configure Stackdriver Monitoring for all projects and export the data to Google Cloud Storage**, as it:

- **Ensures compliance with the 5-year retention requirement.**
- **Optimizes cost for long-term archival storage.**
- **Provides an efficient way to store and retrieve historical application metrics.**

📌 **Final Reference:**
**https://cloud.google.com/monitoring/docs/export**

**⚠️ Note:** Stackdriver Monitoring is now Cloud Monitoring, which keeps most metric data for 24 months. Anything longer has to be exported.

---

## Question 25

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**Your company has decided to create a **backup replica** of its **on-premises user authentication PostgreSQL database** on **Google Cloud Platform**. The database is **4 TB in size**, and **large updates occur frequently**. Additionally, **replication must occur over private address space communication**. Which networking approach should you use?**

- [x] A. **Google Cloud Dedicated Interconnect**.
- [ ] B. **Google Cloud VPN** connected to the on-premises network.
- [ ] C. A **NAT and TLS translation gateway** installed on-premises.
- [ ] D. A **Google Compute Engine instance** with a VPN server installed, connected to the on-premises network.

### Explanation

**Correct Answer:**

**A. Google Cloud Dedicated Interconnect.**

**Explanation:**

To **replicate a 4 TB PostgreSQL database with frequent large updates** over **private address space**, the best approach is **Google Cloud Dedicated Interconnect** because:

✅ **Key Benefits of Dedicated Interconnect:**

- **High-bandwidth, low-latency, and private network connectivity** (up to **100 Gbps**) between on-premises and Google Cloud.
- **Ensures private communication** for secure database replication **without exposing traffic to the public internet**.
- **Minimizes replication lag**, ensuring near real-time synchronization of large updates.
- **More reliable and faster** than VPN-based solutions, which are **limited to 3 Gbps per tunnel**.

✅ **Supporting Documentation:**

- **Google Cloud Dedicated Interconnect Overview:**
  **https://cloud.google.com/interconnect/docs/how-to/dedicated/overview**
- **Best Practices for Database Replication over Cloud Interconnect:**
  **https://cloud.google.com/architecture/database-migration-best-practices**

**Why Other Options Are Incorrect:**

**B. Google Cloud VPN connected to the on-premises network.** ❌

- **Not ideal for a 4 TB database with large frequent updates** due to:
  - **Lower bandwidth limits (3 Gbps per VPN tunnel)** compared to Dedicated Interconnect (up to 100 Gbps).
  - **Higher latency** due to routing over the **public internet** instead of a **private, dedicated network**.
- **Best suited for smaller, less latency-sensitive workloads**, not large-scale database replication.

✅ **Reference:**

- **https://cloud.google.com/network-connectivity/docs/vpn**

**C. A NAT and TLS translation gateway installed on-premises.** ❌

- **Unnecessary complexity** for this use case.
- **NAT (Network Address Translation)** is not required because Dedicated Interconnect or VPN provides **private IP connectivity**.
- **TLS encryption is already built into PostgreSQL replication**, making a separate TLS translation gateway redundant.

✅ **Reference:**

- [**https://www.postgresql.org/docs/current/protocol-overview.html**](https://www.postgresql.org/docs/current/protocol-overview.html)

**D. A Google Compute Engine instance with a VPN server installed, connected to the on-premises network.** ❌

- **Inferior to Google Cloud VPN**, which is a **fully managed service** with better reliability and performance.
- **Manually setting up a VPN server** on Compute Engine adds **operational overhead** without performance benefits.
- **Limited bandwidth (~3 Gbps per VPN tunnel), unsuitable for large database replication.**

✅ **Reference:**

- **https://cloud.google.com/vpn/docs/concepts/overview**

**Conclusion:**

The best approach is **A. Google Cloud Dedicated Interconnect**, as it:

- **Provides high-speed, private connectivity (up to 100 Gbps).**
- **Ensures low-latency, reliable replication of a 4 TB PostgreSQL database.**
- **Avoids the limitations of VPN-based solutions.**

📌 **Final Reference:**
**https://cloud.google.com/interconnect/docs/how-to/dedicated/overview**

---

## Question 26

*Domain 3: Designing for Security and Compliance*

**Auditors conduct reviews every **12 months** and request an analysis of all **Google Cloud Identity and Access Management (Cloud IAM) policy changes** made during the previous year. You need a solution to **streamline and expedite** the audit process. What should you do?**

- [ ] A. Set up **custom Stackdriver alerts** and send the notifications to the auditor.
- [x] B. Enable **Logging export to BigQuery** and use **ACLs and views** to restrict data access for the auditor.
- [ ] C. Use **Cloud Functions** to transfer log entries to **Cloud SQL** and apply **ACLs and views** to control auditor access.
- [ ] D. Enable **log export to Google Cloud Storage (GCS)**, store audit logs in a GCS bucket, and delegate access to the bucket.

### Explanation

**Correct Answer:**

**B. Enable Logging export to BigQuery and use ACLs and views to restrict data access for the auditor.**

**Explanation:**

To **streamline and expedite IAM audit reviews**, the best approach is to **export audit logs to BigQuery**, where auditors can efficiently **query historical IAM policy changes**.

✅ **Why BigQuery is the Best Choice:**

- **Scalable and efficient query engine:** Allows **fast analysis** of **IAM policy changes over the past 12 months**.
- **Native integration with Cloud Audit Logs:** Supports **structured queries** for IAM policy modifications.
- **Access control using ACLs and views:** Restricts **auditor access** to only relevant data.
- **No manual log parsing required:** BigQuery enables **SQL-based queries** rather than manually searching raw logs.

✅ **Implementation Steps:**

1. **Enable Cloud Audit Logging** for **IAM policy changes** (`ADMIN_WRITE` logs).
2. **Set up log export to BigQuery** in a dedicated dataset.
3. **Create a restricted view in BigQuery** to allow **auditors to access only IAM policy change logs**.
4. **Grant auditors read-only access** to the dataset.

✅ **Supporting Documentation:**

- **Exporting Logs to BigQuery:**
  **https://cloud.google.com/logging/docs/export/bigquery**
- **Cloud Audit Logs Overview:**
  **https://cloud.google.com/logging/docs/audit**

**Why Other Options Are Incorrect:**

**A. Set up custom Stackdriver alerts and send the notifications to the auditor.** ❌

- **Not a scalable approach**—auditors require **historical IAM policy change logs**, not real-time alerts.
- **Notifications do not provide a full audit trail** for **past IAM changes over 12 months**.
- **BigQuery is a better tool** for analyzing historical policy changes.

✅ **Reference:**

- **https://cloud.google.com/monitoring/docs/alerts**

**C. Use Cloud Functions to transfer log entries to Cloud SQL and apply ACLs and views to control auditor access.** ❌

- **Unnecessary complexity**—Cloud SQL requires **manual ingestion** and **custom schema design**.
- **BigQuery is a managed analytics solution** designed for large-scale log queries, making it a better fit.
- **Cloud SQL is optimized for transactional data, not large-scale log analysis.**

✅ **Reference:**

- **https://cloud.google.com/sql/docs/introduction**

**D. Enable log export to Google Cloud Storage (GCS), store audit logs in a GCS bucket, and delegate access to the bucket.** ❌

- **GCS is suitable for raw log storage but does not support efficient querying.**
- **Auditors would have to manually parse logs**, making the process time-consuming.
- **BigQuery is the better choice for structured queries and rapid analysis.**

✅ **Reference:**

- **https://cloud.google.com/storage/docs/access-control**

**Conclusion:**

The best approach is **B. Enable Logging export to BigQuery and use ACLs and views to restrict data access for the auditor**, because:

- **BigQuery provides fast and scalable querying for IAM audit logs.**
- **IAM access controls allow secure, auditor-specific views.**
- **Fully automates log analysis without manual parsing.**

📌 **Final Reference:**
**https://cloud.google.com/logging/docs/export/bigquery**

---

## Question 27

*Domain 3: Designing for Security and Compliance*

**You are designing a large distributed application consisting of 30 microservices. Each microservice requires access to a database backend and must securely store its credentials. Where should you store these credentials?**

- [ ] A. Embed them in the **source code**.
- [ ] B. Store them in an **environment variable**.
- [x] C. Use a **secret management system**.
- [ ] D. Store them in a **configuration file** with **restricted access via ACLs**.

### Explanation

**Correct Answer:**

**C. Use a secret management system.**

**Explanation:**

To **securely store and manage credentials** for a **large distributed application with 30 microservices**, a **secret management system** is the best choice.

✅ **Why Use a Secret Management System?**

- **Secure storage and access control:** Ensures **credentials are encrypted** and **access is restricted** to authorized services.
- **Automated credential rotation:** Reduces security risks by **automatically updating and rotating secrets**.
- **Prevents hardcoding credentials** in application code, environment variables, or configuration files.
- **Google Cloud Secret Manager** provides a **centralized, auditable, and secure way to store and retrieve secrets** for microservices.

**Implementation Steps:**

1. **Use Google Cloud Secret Manager** to securely store database credentials.
2. **Grant least privilege IAM roles** to microservices that require access.
3. **Retrieve secrets programmatically** using the **Secret Manager API** or **client libraries**.

✅ **Supporting Documentation:**

- **Google Cloud Secret Manager Overview:**
  **https://cloud.google.com/secret-manager/docs**
- **Best Practices for Managing Secrets:**
  **https://cloud.google.com/architecture/secrets-management**

**Why Other Options Are Incorrect:**

**A. Embed them in the source code.** ❌

- **Hardcoding credentials in source code is a major security risk.**
- **Source code is often shared or exposed**, making credentials vulnerable to **leaks and unauthorized access**.
- **Difficult to update credentials**, requiring **code changes and redeployment**.

✅ **Reference:**

- **https://cloud.google.com/security/articles/secret-management**

**B. Store them in an environment variable.** ❌

- **Environment variables are not secure**—they can be accessed by **any process running on the system**.
- **Lack of encryption and auditing**, making it difficult to track **who accessed the credentials**.
- **Risk of accidental exposure** (e.g., logs, debugging tools).

✅ **Reference:**

- **https://cloud.google.com/security/articles/secret-management**

**D. Store them in a configuration file with restricted access via ACLs.** ❌

- **Configuration files can be compromised** if misconfigured or **accidentally exposed**.
- **Hard to enforce access control dynamically** across multiple microservices.
- **Manual credential rotation is cumbersome and prone to errors.**

✅ **Reference:**

- **https://cloud.google.com/security/articles/secret-management**

**Conclusion:**

The best approach is **C. Use a secret management system**, as it:

- **Securely stores credentials with encryption**.
- **Enforces IAM-based access controls**.
- **Enables automatic credential rotation**.
- **Prevents credential leaks and enhances security**.

📌 **Final Reference:**
**https://cloud.google.com/secret-manager/docs**

---

## Question 28

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

**A lead engineer has developed a custom tool for deploying virtual machines in the legacy data center and now wants to migrate it to the cloud. You want to advocate for using Google Cloud Deployment Manager instead. What are two business risks associated with migrating to Cloud Deployment Manager? (Choose two.)**

- [ ] A. Cloud Deployment Manager relies on **Python**.
- [x] B. Cloud Deployment Manager **APIs could be deprecated** in the future.
- [x] C. Cloud Deployment Manager is **unfamiliar to the company's engineers**.
- [ ] D. Cloud Deployment Manager requires a **Google APIs service account** to operate.
- [ ] E. Cloud Deployment Manager **can permanently delete cloud resources**.
- [ ] F. Cloud Deployment Manager **only automates Google Cloud resources**.

### Explanation

**Correct Answers:**

**B. Cloud Deployment Manager APIs could be deprecated in the future.**
**C. Cloud Deployment Manager is unfamiliar to the company's engineers.**

**Explanation:**

When advocating for **Google Cloud Deployment Manager**, it's important to consider **business risks** that could affect adoption and long-term sustainability.

✅ **Why These Are Business Risks?**

1️⃣ **B. Cloud Deployment Manager APIs could be deprecated in the future.**

- **Google occasionally deprecates services** when better alternatives emerge.
- Deployment Manager is **not actively updated** and **Google recommends Terraform** for infrastructure as code (IaC).
- If **Deployment Manager is deprecated**, the company may need to **migrate to Terraform or another tool**, increasing costs and effort.

✅ **Supporting Documentation:**

- **https://cloud.google.com/deployment-manager/docs/moving-to-terraform**

2️⃣ **C. Cloud Deployment Manager is unfamiliar to the company's engineers.**

- **Requires retraining and ramp-up time**, impacting productivity.
- The **lead engineer already has a custom deployment tool**, meaning resistance to change is possible.
- **Terraform is more widely adopted** and supports **multi-cloud deployments**, making it a more future-proof choice.

✅ **Supporting Documentation:**

- **https://cloud.google.com/docs/terraform**

**Why Other Options Are Incorrect?**

**A. Cloud Deployment Manager relies on Python.** ❌

- **Incorrect** because Deployment Manager **uses YAML and Jinja2 templates**, with **optional Python support**.
- **Python is not mandatory**—most configurations can be done in YAML alone.

✅ **Reference:**

- **https://cloud.google.com/deployment-manager/docs/configuration/supported-python-runtime**

**D. Cloud Deployment Manager requires a Google APIs service account to operate.** ❌

- **Not a significant business risk** because **service accounts are a standard practice** for infrastructure automation tools.
- **Other IaC tools like Terraform also require service accounts** for authentication.

✅ **Reference:**

- **https://cloud.google.com/iam/docs/service-accounts**

**E. Cloud Deployment Manager can permanently delete cloud resources.** ❌

- **Not a risk specific to Deployment Manager**—all IaC tools (Terraform, Ansible, etc.) have the ability to **delete resources**.
- **Safe deletion mechanisms (e.g., preview mode) exist** to prevent accidental resource loss.

✅ **Reference:**

- **https://cloud.google.com/deployment-manager/docs/deployments/updating-deployments**

**F. Cloud Deployment Manager only automates Google Cloud resources.** ❌

- **Not necessarily a business risk** if the company is **fully using Google Cloud**.
- **However, if multi-cloud compatibility is required, Terraform is a better choice.**

✅ **Reference:**

- **https://cloud.google.com/docs/terraform**

**Conclusion:**

The two key **business risks** of using **Cloud Deployment Manager** are:

1. **Potential deprecation** (Option B)
2. **Lack of familiarity among engineers** (Option C)

📌 **Final Reference:**

- **https://cloud.google.com/deployment-manager/docs/moving-to-terraform**

**⚠️ Note:** Deployment Manager reached end of support in March 2026, so the deprecation risk in option B has come true. Google now points to Terraform and Infrastructure Manager.

---

## Question 29

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**A development manager is building a new application and has asked you to review the requirements to identify the cloud technologies that can be used to meet them. The application must:**

1. **Be based on open-source technology for cloud portability.**
2. **Dynamically scale compute capacity based on demand.**
3. **Support continuous software delivery.**
4. **Run multiple isolated copies of the same application stack.**
5. **Deploy application bundles using dynamic templates.**
6. **Route network traffic to specific services based on URL.**

**Which combination of technologies will satisfy all these requirements?**

- [x] A. Google Kubernetes Engine, Jenkins, and Helm
- [ ] B. Google Kubernetes Engine and Cloud Load Balancing
- [ ] C. Google Kubernetes Engine and Cloud Deployment Manager
- [ ] D. Google Kubernetes Engine, Jenkins, and Cloud Load Balancing

### Explanation

**Correct Answer:**

**A. Google Kubernetes Engine, Jenkins, and Helm**

**Explanation:**

To satisfy **all application requirements**, a combination of **Google Kubernetes Engine (GKE), Jenkins, and Helm** is the best choice.

✅ **Requirement Breakdown and Matching Technologies:**

1️⃣ **Be based on open-source technology for cloud portability.**

- **Google Kubernetes Engine (GKE)** is based on **open-source Kubernetes**, ensuring **portability across clouds**.
- **Helm** (Kubernetes package manager) simplifies deployment portability.

2️⃣ **Dynamically scale compute capacity based on demand.**

- **GKE has built-in cluster autoscaling** to **dynamically scale compute capacity**.

3️⃣ **Support continuous software delivery.**

- **Jenkins** is a widely used **CI/CD tool** that integrates with Kubernetes for **continuous delivery**.

4️⃣ **Run multiple isolated copies of the same application stack.**

- **GKE supports multi-tenant deployments** by using **Kubernetes namespaces** and **pods isolation**.

5️⃣ **Deploy application bundles using dynamic templates.**

- **Helm** allows deploying applications using **Helm charts (dynamic templates)**.

6️⃣ **Route network traffic to specific services based on URL.**

- **Kubernetes Ingress** (deployed on GKE) supports **routing traffic based on URL paths**.

✅ **Supporting Documentation:**

- **GKE Autoscaling:**
  **https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler**
- **Jenkins on Kubernetes:**
  **https://www.jenkins.io/doc/book/installing/kubernetes/**
- **Helm Charts for Kubernetes:**
  **https://helm.sh/docs/**

**Why Other Options Are Incorrect?**

**B. Google Kubernetes Engine and Cloud Load Balancing.** ❌

- **Missing continuous delivery support** (Jenkins or another CI/CD tool is needed).
- **Does not provide dynamic templating** (Helm is required for this).

✅ **Reference:**

- **https://cloud.google.com/load-balancing/docs/**

**C. Google Kubernetes Engine and Cloud Deployment Manager.** ❌

- **Cloud Deployment Manager is for infrastructure automation**, not application deployment.
- **Lacks CI/CD support** (Jenkins needed).
- **Lacks dynamic templating** (Helm needed).

✅ **Reference:**

- **https://cloud.google.com/deployment-manager/docs/**

**D. Google Kubernetes Engine, Jenkins, and Cloud Load Balancing.** ❌

- **Missing dynamic application templating support** (Helm is needed).
- **Cloud Load Balancing helps with global routing** but does not **simplify deployments** like Helm.

✅ **Reference:**

- **https://cloud.google.com/kubernetes-engine/docs/concepts/ingress**

**Conclusion:**

The best combination to satisfy **all** application requirements is:
✔ **Google Kubernetes Engine** (scalability, isolation, routing).
✔ **Jenkins** (CI/CD for continuous delivery).
✔ **Helm** (dynamic templating and application bundling).

📌 **Final Reference:**
**https://helm.sh/docs/**

---

## Question 30

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**You have deployed several preemptible Linux virtual machine instances on Google Compute Engine. To ensure that your application properly shuts down before the virtual machines are preempted, what should you do?**

- [ ] A. Create a **shutdown script** named `k99.shutdown` in the `/etc/rc.6.d/` directory.
- [ ] B. Register a **shutdown script** as an **xinetd service** in Linux and configure a **Stackdriver endpoint check** to call the service.
- [x] C. Create a **shutdown script** and set it as the value for a **new metadata entry** with the key `shutdown-script` in the **Cloud Console** when creating the instance.
- [ ] D. Register a **shutdown script** as an **xinetd service** in Linux and use the `gcloud compute instances add-metadata` command to specify the service URL as the value for a **new metadata entry** with the key `shutdown-script-url`.

### Explanation

**Correct Answer:**

**C. Create a shutdown script and set it as the value for a new metadata entry with the key `shutdown-script` in the Cloud Console when creating the instance.**

**Explanation:**

Preemptible **Google Compute Engine (GCE) instances** can be **terminated at any time** by Google Cloud. To ensure that an application **properly shuts down** before preemption:

✅ **Best Approach: Use the `shutdown-script` Metadata Key**

- Google Cloud allows configuring **shutdown scripts via instance metadata**.
- These scripts **execute automatically when a VM is preempted**, ensuring **graceful shutdown**.
- The script should be stored as a **custom metadata key** (`shutdown-script`) and **can include commands to flush logs, close database connections, or gracefully terminate services**.

**Example Implementation:**

1. **Create a shutdown script (e.g., `shutdown.sh`)**:
  ```
  #!/bin/bashecho "Shutting down gracefully..." >> /var/log/shutdown.logsystemctl stop my-app.servicesync
  ```
2. **Set the script in the instance metadata (`shutdown-script` key):**
  ```
  gcloud compute instances add-metadata my-instance \    --metadata shutdown-script="$(cat shutdown.sh)"
  ```

✅ **Supporting Documentation:**

- **Shutdown Scripts in Compute Engine:**
  **https://cloud.google.com/compute/docs/shutdownscript**

**Why Other Options Are Incorrect:**

**A. Create a shutdown script named `k99.shutdown` in the `/etc/rc.6.d/` directory.** ❌

- **Incorrect because modern Linux systems use `systemd`, not** `SysVinit`, meaning scripts in `/etc/rc.6.d/` **may not run on all distributions**.
- **Google Cloud metadata-based shutdown scripts are a more reliable approach.**

✅ **Reference:**

- **https://cloud.google.com/compute/docs/instances/startup-scripts/linux**

**B. Register a shutdown script as an `xinetd` service in Linux and configure a Stackdriver endpoint check to call the service.** ❌

- **xinetd is a legacy daemon for managing network services**—it is **not needed for handling shutdown events**.
- **Stackdriver Monitoring (now Cloud Monitoring) is used for metrics/logging, not triggering shutdown scripts.**

✅ **Reference:**

- **https://cloud.google.com/monitoring/docs**

**D. Register a shutdown script as an `xinetd` service in Linux and use `gcloud compute instances add-metadata` to specify the service URL as the value for `shutdown-script-url`.** ❌

- **Similar to Option B, xinetd is unrelated to shutdown script execution.**
- **The correct metadata key is `shutdown-script`, not `shutdown-script-url`.**

✅ **Reference:**

- **https://cloud.google.com/compute/docs/shutdownscript**

**Conclusion:**

The best solution is **C. Use the `shutdown-script` metadata key**, as it:

- **Executes automatically before preemption.**
- **Allows clean shutdown of applications and services.**
- **Does not rely on outdated or complex mechanisms.**

📌 **Final Reference:**
**https://cloud.google.com/compute/docs/shutdownscript**

**⚠️ Note:** Preemptible VMs have been superseded by **Spot VMs**. The answer still holds: put the script in the `shutdown-script` metadata key. It gets about 30 seconds, best effort, before the VM stops.

---

## Question 31

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**Your organization has a 3-tier web application deployed within the same network on Google Cloud Platform. Each tier—web, API, and database—scales independently. The network traffic should flow from the web tier to the API tier, and then to the database tier, ensuring that traffic does not flow directly between the web and database tiers.**

**How should you configure the network to enforce this traffic flow?**

- [ ] A. Assign each tier to a **different subnetwork**.
- [ ] B. Configure **software-based firewalls** on individual virtual machines (VMs).
- [ ] C. Use **tags** for each tier and configure **routes** to enforce the desired traffic flow.
- [x] D. Use **tags** for each tier and configure **firewall rules** to enforce the desired traffic flow.

### Explanation

**Correct Answer:**

**D. Use tags for each tier and configure firewall rules to enforce the desired traffic flow.**

**Explanation:**

To **enforce controlled traffic flow** between the **web, API, and database tiers**, **firewall rules** should be used. In Google Cloud, firewall rules can be applied based on **network tags**, ensuring:

✅ **Why Use Firewall Rules with Tags?**

- **Network tags allow easy grouping of instances** based on function (e.g., `web-tier`, `api-tier`, `db-tier`).
- **Firewall rules restrict traffic between tiers**, ensuring that:
  - **Web tier can only communicate with API tier**.
  - **API tier can communicate with both web and database tiers**.
  - **Database tier only accepts connections from the API tier**.
- **More scalable and manageable** than manual instance-based firewall rules.

**Implementation Steps:**

1. **Assign network tags to instances**:
  - Web instances → `web-tier`
  - API instances → `api-tier`
  - Database instances → `db-tier`
2. **Create firewall rules:**
  - **Allow traffic from `web-tier` →** `api-tier`:
    ```
    gcloud compute firewall-rules create allow-web-to-api \    --direction=INGRESS --action=ALLOW --priority=1000 \    --source-tags=web-tier --target-tags=api-tier \    --rules=tcp:443,tcp:80
    ```
  - **Allow traffic from `api-tier` →** `db-tier`:
    ```
    gcloud compute firewall-rules create allow-api-to-db \    --direction=INGRESS --action=ALLOW --priority=1000 \    --source-tags=api-tier --target-tags=db-tier \    --rules=tcp:5432
    ```
  - **Deny direct traffic from `web-tier` →** `db-tier`:
    ```
    gcloud compute firewall-rules create deny-web-to-db \    --direction=INGRESS --action=DENY --priority=900 \    --source-tags=web-tier --target-tags=db-tier \    --rules=tcp:5432
    ```

✅ **Supporting Documentation:**

- **Firewall Rules in Google Cloud:**
  **https://cloud.google.com/vpc/docs/firewalls**
- **Using Tags in Firewall Rules:**
  **https://cloud.google.com/vpc/docs/firewalls#network-tags**

**Why Other Options Are Incorrect:**

**A. Assign each tier to a different subnetwork.** ❌

- **Subnetworks define IP ranges but do not enforce security policies.**
- **Without firewall rules**, instances in separate subnets can still communicate freely.
- **Subnet segmentation alone does not restrict traffic flow.**

✅ **Reference:**

- **https://cloud.google.com/vpc/docs/subnets**

**B. Configure software-based firewalls on individual virtual machines (VMs).** ❌

- **Managing firewalls on each VM is complex and not scalable** for large deployments.
- **Google Cloud firewall rules apply at the VPC level**, making VM-based firewalls unnecessary.
- **More error-prone and difficult to maintain** than centrally managed firewall rules.

✅ **Reference:**

- **https://cloud.google.com/vpc/docs/firewalls**

**C. Use tags for each tier and configure routes to enforce the desired traffic flow.** ❌

- **Routes control how traffic is forwarded, but they do not enforce security restrictions.**
- **Firewall rules, not routes, define which traffic is allowed or denied.**
- **A route cannot block or enforce directional traffic flows.**

✅ **Reference:**

- **https://cloud.google.com/vpc/docs/routes**

**Conclusion:**

The best solution is **D. Use tags for each tier and configure firewall rules to enforce the desired traffic flow**, because:

- **Firewall rules enforce traffic control between tiers.**
- **Tags provide a scalable and flexible way to manage security policies.**
- **This ensures that the web tier only communicates with the API tier, and the database remains isolated.**

📌 **Final Reference:**
**https://cloud.google.com/vpc/docs/firewalls#network-tags**

---

## Question 32

*Domain 6: Ensuring Solution and Operations Excellence*

**Your development team has installed a new Linux kernel module on the batch servers running on Google Compute Engine (GCE) virtual machines (VMs) to improve the nightly batch process. However, two days after the installation, 50% of the batch servers failed during the nightly batch run. You need to collect detailed failure information to share with the development team.**

**Which three actions should you take? (Choose three.)**

- [x] A. Use **Stackdriver Logging** to search for log entries related to the kernel module.
- [ ] B. Retrieve the **GCE Activity log** using the API or Cloud Console for debugging.
- [x] C. Use **gcloud** or the **Cloud Console** to connect to the **serial console** and inspect the logs.
- [ ] D. Check the **activity log** to determine whether a **live migration event** occurred on the failed servers.
- [x] E. Adjust the **Google Stackdriver** timeline to match the failure time and review batch server **metrics**.
- [ ] F. Export a **debug VM image**, run it on a **local server**, and observe kernel log messages on the native screen.

### Explanation

**Correct Answers:**

✅ **A. Use Stackdriver Logging to search for log entries related to the kernel module.**
✅ **C. Use gcloud or the Cloud Console to connect to the serial console and inspect the logs.**
✅ **E. Adjust the Google Stackdriver timeline to match the failure time and review batch server metrics.**

**Explanation:**

To **debug the batch server failures caused by a new Linux kernel module**, you need to gather **logs, metrics, and console output** to analyze system behavior before the failure.

**Why These Three Options Are Correct?**

1️⃣ **A. Use Stackdriver Logging to search for log entries related to the kernel module.** ✅

- **Stackdriver Logging (Cloud Logging)** records **system logs, kernel messages, and application logs**.
- You can search for **kernel-related errors (e.g., `dmesg`, `syslog`, or `journalctl`)** to find failures related to the module.
- **Look for `kernel panic` or `modprobe` failures** that might indicate why the batch jobs failed.

✅ **Supporting Documentation:**

- **https://cloud.google.com/logging/docs/view/advanced-queries**

2️⃣ **C. Use gcloud or the Cloud Console to connect to the serial console and inspect the logs.** ✅

- The **serial console** captures **kernel panics, boot logs, and system errors**, even when SSH is unavailable.
- If the **VM crashed due to the new kernel module**, serial console logs may provide **panic messages and backtraces**.
- **Command to enable and access serial console logs:**
  ```
  bashCopyEditgcloud compute instances get-serial-port-output INSTANCE_NAME
  ```

✅ **Supporting Documentation:**

- **https://cloud.google.com/compute/docs/troubleshooting/using-serial-console**

3️⃣ **E. Adjust the Google Stackdriver timeline to match the failure time and review batch server metrics.** ✅

- **Stackdriver (Cloud Monitoring) provides CPU, memory, disk, and network metrics.**
- Checking **performance trends before failure** might reveal **spikes in resource usage or unusual activity** caused by the kernel module.
- **Look for increased memory usage (OOM errors), CPU load, or system crashes.**

✅ **Supporting Documentation:**

- **https://cloud.google.com/monitoring/docs/viewing-metrics**

**Why Other Options Are Incorrect?**

**B. Retrieve the GCE Activity log using the API or Cloud Console for debugging.** ❌

- **GCE Activity Logs track user and API actions**, such as **instance creations, deletions, and metadata changes**.
- **They do not capture system-level failures or kernel issues.**
- **Cloud Logging (Option A) provides more relevant kernel failure details.**

✅ **Reference:**

- **https://cloud.google.com/logging/docs/audit**

**D. Check the activity log to determine whether a live migration event occurred on the failed servers.** ❌

- **Live migration does not cause kernel failures**—it is a transparent process for VMs.
- **If live migration had caused failures, all servers would be affected, not just 50%.**
- **More relevant checks include system logs (Option A) and serial console output (Option C).**

✅ **Reference:**

- **https://cloud.google.com/compute/docs/live-migration**

**F. Export a debug VM image, run it on a local server, and observe kernel log messages on the native screen.** ❌

- **Unnecessary and impractical for debugging a production failure.**
- **Serial console logs (Option C) provide the same kernel error details without needing local debugging.**
- **Exporting and running a VM locally introduces operational overhead.**

✅ **Reference:**

- **https://cloud.google.com/compute/docs/images/export-image**

**Conclusion:**

The best troubleshooting steps are:
✔ **A. Check Stackdriver Logging for kernel-related log entries.**
✔ **C. Use serial console logs to inspect kernel panics and failures.**
✔ **E. Review Stackdriver Monitoring metrics before and during failure.**

📌 **Final References:**

- **Cloud Logging: Advanced Queries**
- **Using Serial Console for Debugging**
- **Viewing Stackdriver Monitoring Metrics**

---

## Question 33

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**Your company wants to explore cloud adoption with minimal risk. As a first step, they plan to archive approximately 100 TB of log data in the cloud for testing analytics capabilities while also retaining the data as a long-term disaster recovery backup.**

**Which two actions should you take? (Choose two.)**

- [x] A. Load the logs into **Google BigQuery**.
- [ ] B. Load the logs into **Google Cloud SQL**.
- [ ] C. Import the logs into **Google Stackdriver**.
- [ ] D. Insert the logs into **Google Cloud Bigtable**.
- [x] E. Upload the log files into **Google Cloud Storage**.

### Explanation

**Correct Answers:**

✅ **A. Load the logs into Google BigQuery.**
✅ **E. Upload the log files into Google Cloud Storage.**

**Explanation:**

Your company wants to **archive 100 TB of log data** in Google Cloud for:

1. **Testing analytics capabilities.**
2. **Long-term disaster recovery backup.**

The best approach is to use **Google Cloud Storage (for cost-effective archiving)** and **Google BigQuery (for analytics)**.

**Why These Two Options Are Correct?**

1️⃣ **E. Upload the log files into Google Cloud Storage.** ✅

- **Cloud Storage is the best choice for long-term log storage and disaster recovery.**
- **Low-cost storage options**:
  - **Coldline or Archive storage** is optimized for infrequent access but retains data securely.
- **Durable, highly available, and scalable** storage solution for 100 TB of logs.

✅ **Supporting Documentation:**

- **Cloud Storage Classes:**
  **https://cloud.google.com/storage/docs/storage-classes**

2️⃣ **A. Load the logs into Google BigQuery.** ✅

- **BigQuery is an ideal tool for analytics on large-scale log data.**
- **Supports real-time and batch queries** without requiring pre-indexing.
- **Cost-efficient for on-demand queries** while keeping raw logs in Cloud Storage.

✅ **Supporting Documentation:**

- **BigQuery for Log Analytics:**
  **https://cloud.google.com/bigquery/docs/reference/auditlogs**

**Why Other Options Are Incorrect?**

**B. Load the logs into Google Cloud SQL.** ❌

- **Not suitable for large-scale log storage** (Cloud SQL has a **10 TB limit per instance**).
- **Relational databases are inefficient for log analytics** compared to **BigQuery**.

✅ **Reference:**

- **https://cloud.google.com/sql/docs/introduction**

**C. Import the logs into Google Stackdriver.** ❌

- **Stackdriver (Cloud Logging) is for monitoring, not long-term archiving.**
- **Expensive for storing 100 TB of logs** (designed for real-time log management, not historical analytics).
- **Best for operational monitoring, not disaster recovery.**

✅ **Reference:**

- **https://cloud.google.com/logging/docs/export**

**D. Insert the logs into Google Cloud Bigtable.** ❌

- **Bigtable is optimized for time-series and real-time operational data**, not long-term log storage.
- **More complex to query compared to BigQuery**.
- **Does not provide built-in analytics** for large-scale log analysis.

✅ **Reference:**

- **https://cloud.google.com/bigtable/docs/overview**

**Conclusion:**

To **archive and analyze 100 TB of logs**, the best approach is:
✔ **Store logs in Google Cloud Storage for low-cost, durable backup.**
✔ **Load logs into Google BigQuery for powerful, scalable analytics.**

📌 **Final References:**

- **Cloud Storage Classes**
- **BigQuery for Log Analytics**

---

## Question 34

*Domain 6: Ensuring Solution and Operations Excellence*

**You have built a deployment pipeline that pushes source code changes to your infrastructure in instance groups with self-healing capabilities. A recent change has negatively impacted a key performance indicator (KPI), and the root cause is unknown. Investigating the issue could take up to a week.**

**What should you do?**

- [ ] A. Log in to a server and manually iterate on the fix locally.
- [x] B. **Revert the source code change** and rerun the deployment pipeline.
- [ ] C. Log into the affected servers and manually replace the bad code with the previous version.
- [ ] D. **Change the instance group template to the previous version** and delete all instances.

### Explanation

**Correct Answer:**

✅ **B. Revert the source code change and rerun the deployment pipeline.**

**Explanation:**

Since the **recent deployment negatively impacted a key performance indicator (KPI)** and the root cause is **unknown**, the best approach is to:

1. **Revert the source code to the previous stable version.**
2. **Rerun the deployment pipeline to automatically push the stable version** back to production.

This ensures:

- **Minimal downtime** while the issue is investigated.
- **Automated rollback using the deployment pipeline**, which is safer and prevents manual errors.
- **Consistent deployment practices**, avoiding ad-hoc fixes on individual servers.

✅ **Supporting Documentation:**

- **Best Practices for Deployment Pipelines:**
  **https://cloud.google.com/architecture/devops/devops-tech-continuous-deployment**

**Why Other Options Are Incorrect?**

**A. Log in to a server and manually iterate on the fix locally.** ❌

- **Manually debugging in production is risky**—changes could introduce more issues.
- **Instance groups have self-healing capabilities**, meaning manual fixes may be lost when instances are recreated.
- **The deployment pipeline should be used for controlled and tested updates.**

✅ **Reference:**

- **https://cloud.google.com/compute/docs/instance-groups**

**C. Log into the affected servers and manually replace the bad code with the previous version.** ❌

- **Manual changes to individual servers will be overridden** when the instance group recreates instances.
- **Not scalable**, as instance groups automatically replace unhealthy VMs.
- **Deployment pipelines should manage rollbacks, not manual updates on individual machines.**

✅ **Reference:**

- **https://cloud.google.com/deployment-manager/docs**

**D. Change the instance group template to the previous version and delete all instances.** ❌

- **Overly disruptive**—deleting instances **can cause downtime**.
- **Changing the template is useful, but the pipeline should handle rollbacks automatically.**
- **Reverting the source code (Option B) is faster and follows DevOps best practices.**

✅ **Reference:**

- **https://cloud.google.com/compute/docs/instance-templates**

**Conclusion:**

The best approach is **B. Revert the source code change and rerun the deployment pipeline**, because:

- **It restores a stable version quickly** while allowing investigation.
- **It prevents manual intervention in production.**
- **It aligns with best DevOps practices.**

📌 **Final Reference:**
**https://cloud.google.com/architecture/devops/devops-tech-continuous-deployment**

---

## Question 35

*Domain 3: Designing for Security and Compliance*

**Your organization wants to **centrally manage IAM policies** while allowing **each department to control its own policies independently**. Which approach should you take?**

- [ ] A. Use **multiple Organizations**, each containing multiple **Folders**.
- [ ] B. Set up **multiple Organizations**, with **one Organization per department**.
- [x] C. Maintain a **single Organization** and create **Folders for each department**.
- [ ] D. Use a **single Organization** with **multiple projects**, each assigned to a central owner.

### Explanation

**Correct Answer:**

✅ **C. Maintain a single Organization and create Folders for each department.**

**Explanation:**

In **Google Cloud Identity and Access Management (IAM)**, the **best way to centrally manage IAM policies** while **allowing departments to control their own policies independently** is to use:

- **A single Organization** (root node for centralized governance).
- **Folders for each department**, where each department can **define its own IAM policies**.

✅ **Why This Works:**

- **Folders allow delegation of IAM policies** while maintaining centralized control.
- **Inheritance of IAM policies** enables **organization-wide rules** while allowing **department-specific permissions**.
- **Departments can manage their own resources independently** while still being part of the same Organization.

**Implementation Example:**

1. **Create a Folder for each department** under the Organization.
2. **Assign IAM roles at the Folder level** to grant department admins control over their resources.
3. **Projects are placed within department-specific Folders**, inheriting the appropriate IAM policies.

✅ **Supporting Documentation:**

- **Google Cloud Resource Hierarchy Best Practices:**
  **https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy**

**Why Other Options Are Incorrect?**

**A. Use multiple Organizations, each containing multiple Folders.** ❌

- **Organizations are meant to represent a single company**, not separate departments.
- **Difficult to centrally manage IAM policies across multiple Organizations.**
- **Cross-organization IAM policy management is complex** and not recommended.

✅ **Reference:**

- **https://cloud.google.com/resource-manager/docs/creating-managing-organization**

**B. Set up multiple Organizations, with one Organization per department.** ❌

- **Each Organization would require separate IAM management, billing, and security policies.**
- **Departments would be completely isolated**, making it harder to enforce company-wide policies.
- **A single Organization with department-specific Folders is the recommended structure.**

✅ **Reference:**

- **https://cloud.google.com/resource-manager/docs/organization-policy/overview**

**D. Use a single Organization with multiple projects, each assigned to a central owner.** ❌

- **IAM policies at the project level do not allow independent department-level control.**
- **Centralized ownership limits department autonomy**, increasing operational bottlenecks.
- **Folders provide better separation and policy delegation than managing projects directly.**

✅ **Reference:**

- **https://cloud.google.com/resource-manager/docs/creating-managing-folders**

**Conclusion:**

The best approach is **C. Maintain a single Organization and create Folders for each department**, because:

- **It provides centralized IAM governance while allowing departmental autonomy.**
- **IAM policies can be set at different levels (Organization, Folder, Project).**
- **It simplifies resource and policy management across the organization.**

📌 **Final Reference:**
**https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy**

---

## Question 36

*Domain 3: Designing for Security and Compliance*

**In designing a mobile chat application, how can you prevent the spoofing of chat messages to ensure they are attributed to specific users?**

- [ ] A. Tag messages client side with the originating user identifier and the destination user.
- [ ] B. Encrypt the message client side using block-based encryption with a shared key.
- [x] C. Use public key infrastructure (PKI) to encrypt the message client side using the originating user's private key.
- [ ] D. Use a trusted certificate authority to enable SSL connectivity between the client application and the server.

### Explanation

**Correct Answer:**

✅ **C. Use public key infrastructure (PKI) to encrypt the message client-side using the originating user's private key.**

**Explanation:**

To **prevent the spoofing of chat messages** and **ensure messages are correctly attributed to specific users**, a **cryptographic approach that verifies message authenticity** is needed.

✅ **Why PKI and Digital Signatures Work?**

- **Public Key Infrastructure (PKI)** provides a **mechanism for authentication and non-repudiation**.
- **Each user has a key pair (public + private key)**, where:
  - The **private key is used to sign messages** before sending.
  - The **public key is used to verify** the signature upon receipt.
- **Prevents attackers from forging messages**, as they cannot generate a valid signature without the sender's private key.

✅ **Implementation Steps:**

1. **User generates a key pair** (Public/Private Key).
2. **Client signs the message using their private key** before sending.
3. **Server verifies the signature using the sender’s public key**.
4. **If the signature is valid, the message is authenticated** as coming from the correct user.

✅ **Supporting Documentation:**

- **Google Cloud PKI and Digital Signatures:**
  **https://cloud.google.com/security/encryption-in-transit**
- **Digital Signature Mechanism Overview:**
  [**https://en.wikipedia.org/wiki/Digital_signature**](https://en.wikipedia.org/wiki/Digital_signature)

**Why Other Options Are Incorrect?**

**A. Tag messages client-side with the originating user identifier and the destination user.** ❌

- **User identifiers can be easily spoofed** if not cryptographically protected.
- **No security mechanism ensures message authenticity**—an attacker could manipulate the sender ID.

✅ **Reference:**

- **https://owasp.org/www-community/controls/Message_Authentication**

**B. Encrypt the message client-side using block-based encryption with a shared key.** ❌

- **Encryption alone does not verify the sender's identity**—anyone with the key can generate messages.
- **Does not prevent spoofing**, as an attacker who obtains the shared key can send messages as someone else.

✅ **Reference:**

- **https://cryptobook.nakov.com/symmetric-key-ciphers/message-authentication-codes**

**D. Use a trusted certificate authority to enable SSL connectivity between the client application and the server.** ❌

- **SSL/TLS ensures secure transport** but **does not authenticate message contents**.
- **An attacker could still modify message payloads before sending them.**

✅ **Reference:**

- **https://cloud.google.com/security/encryption-in-transit**

**Conclusion:**

The best approach is **C. Use public key infrastructure (PKI) to encrypt the message client-side using the originating user's private key**, because it:

- **Ensures message authenticity** (only the rightful user can sign messages).
- **Prevents spoofing** (attackers cannot forge valid messages).
- **Allows secure verification on the server side using public keys**.

📌 **Final Reference:**
[**https://en.wikipedia.org/wiki/Digital_signature**](https://en.wikipedia.org/wiki/Digital_signature)

---

## Question 37

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**As part of their disaster recovery plan, your company is replicating a production MySQL database from an on-premises private data center to Google Cloud Platform (GCP) over a Google Cloud VPN connection. However, they are encountering latency issues and packet loss, which are disrupting replication.**

**What should they do?**

- [ ] A. Configure the replication to use **UDP**.
- [x] B. Set up a **Google Cloud Dedicated Interconnect**.
- [ ] C. Perform a **daily database restore** using **Google Cloud SQL**.
- [ ] D. Add **additional VPN connections** and configure **load balancing** between them.
- [ ] E. Send the **replicated transactions** to **Google Cloud Pub/Sub**.

### Explanation

**Correct Answer:**

✅ **B. Set up a Google Cloud Dedicated Interconnect.**

**Explanation:**

Since the **MySQL database replication is experiencing latency and packet loss over a Google Cloud VPN**, the best solution is to **upgrade to Google Cloud Dedicated Interconnect**.

✅ **Why Google Cloud Dedicated Interconnect?**

- **Provides a high-bandwidth, low-latency connection** between on-premises and Google Cloud.
- **Supports up to 100 Gbps of private connectivity**, reducing replication lag.
- **Bypasses the public internet**, eliminating packet loss and network congestion.
- **Ensures more reliable and predictable performance** compared to VPN.

**Implementation Steps:**

1. **Set up a Dedicated Interconnect connection** in the Google Cloud Console.
2. **Choose a colocation facility** for establishing a direct connection.
3. **Configure a VLAN attachment** to connect on-premises MySQL to Google Cloud SQL or a Compute Engine instance.
4. **Test and optimize MySQL replication performance** over the new connection.

✅ **Supporting Documentation:**

- **Google Cloud Dedicated Interconnect Overview:**
  **https://cloud.google.com/interconnect/docs/how-to/dedicated/overview**

**Why Other Options Are Incorrect?**

**A. Configure the replication to use UDP.** ❌

- **MySQL replication relies on TCP for reliable data transmission**, not UDP.
- **UDP does not guarantee delivery**, making it unsuitable for database replication.

✅ **Reference:**

- [**https://dev.mysql.com/doc/refman/8.0/en/replication.html**](https://dev.mysql.com/doc/refman/8.0/en/replication.html)

**C. Perform a daily database restore using Google Cloud SQL.** ❌

- **Not a real-time solution**—daily restores introduce **significant data lag**.
- **Replication ensures near-real-time sync**, whereas restores are periodic snapshots.

✅ **Reference:**

- **https://cloud.google.com/sql/docs/mysql/replication**

**D. Add additional VPN connections and configure load balancing between them.** ❌

- **VPN tunnels have a 3 Gbps per tunnel limit** and rely on **public internet traffic**, leading to potential congestion.
- **Adding multiple VPNs does not eliminate latency and packet loss**—Dedicated Interconnect is a better solution.

✅ **Reference:**

- **https://cloud.google.com/network-connectivity/docs/vpn/concepts/topologies**

**E. Send the replicated transactions to Google Cloud Pub/Sub.** ❌

- **Pub/Sub is designed for event streaming, not for MySQL database replication.**
- **MySQL replication requires transaction consistency**, which Pub/Sub **does not guarantee**.

✅ **Reference:**

- **https://cloud.google.com/pubsub/docs/overview**

**Conclusion:**

The best solution is **B. Set up a Google Cloud Dedicated Interconnect**, because:

- **It reduces latency and packet loss** by providing a **direct private connection** to Google Cloud.
- **It supports high-speed replication** (up to 100 Gbps), improving database performance.
- **It eliminates dependency on the public internet**, ensuring reliable replication.

📌 **Final Reference:**
**https://cloud.google.com/interconnect/docs/how-to/dedicated/overview**

---

## Question 38

*Domain 3: Designing for Security and Compliance*

**Your **customer support tool** logs all **email and chat conversations** to **Cloud Bigtable** for **retention and analysis**. To comply with **privacy and security requirements**, what is the recommended approach for **removing personally identifiable information (PII) and payment card information (PCI)** before storing the data?**

- [ ] A. **Hash all data** using **SHA-256**.
- [ ] B. **Encrypt all data** using **elliptic curve cryptography (ECC)**.
- [x] C. **De-identify the data** using the **Cloud Data Loss Prevention (DLP) API**.
- [ ] D. Use **regular expressions** to identify and redact **phone numbers, email addresses, and credit card numbers**.

### Explanation

**Correct Answer:**

✅ **C. De-identify the data using the Cloud Data Loss Prevention (DLP) API.**

**Explanation:**

To comply with **privacy and security requirements** when storing **personally identifiable information (PII) and payment card information (PCI) in Cloud Bigtable**, the best approach is to use **Google Cloud Data Loss Prevention (DLP) API** for **de-identification**.

✅ **Why Cloud DLP API?**

- **Automatically detects and removes PII & PCI** (e.g., names, emails, credit card numbers).
- **Supports tokenization, redaction, and pseudonymization**, ensuring compliance with **GDPR, HIPAA, and PCI DSS**.
- **More reliable than regex-based solutions**, which may miss complex data patterns.
- **Can apply irreversible transformations** to ensure sensitive data is no longer identifiable.

**Implementation Example:**

1. **Use Cloud DLP API to scan incoming data.**
2. **Apply de-identification techniques:**
  - **Redaction**: Remove sensitive data.
  - **Tokenization**: Replace data with a non-reversible token.
  - **Format-preserving encryption (FPE)**: Protect structured data.
3. **Store the de-identified data in Bigtable.**

✅ **Supporting Documentation:**

- **Cloud DLP Overview:**
  **https://cloud.google.com/dlp/docs/deidentify-sensitive-data**
- **DLP Tokenization Guide:**
  **https://cloud.google.com/dlp/docs/pseudonymization**

**Why Other Options Are Incorrect?**

**A. Hash all data using SHA-256.** ❌

- **Hashing is irreversible**, making it **unsuitable for structured data** like emails or credit card numbers that may need retrieval.
- **Does not prevent data exposure** if attackers can use dictionary attacks or brute-force lookup tables.
- **DLP tokenization or redaction is a better approach.**

✅ **Reference:**

- **https://cloud.google.com/security/encryption-in-transit**

**B. Encrypt all data using elliptic curve cryptography (ECC).** ❌

- **Encryption protects data in transit and at rest** but does not remove **PII or PCI** before storage.
- **Decryption keys must be managed**, creating additional security concerns.
- **DLP API offers de-identification, which is more suitable for compliance.**

✅ **Reference:**

- **https://cloud.google.com/security/encryption-at-rest**

**D. Use regular expressions to identify and redact phone numbers, email addresses, and credit card numbers.** ❌

- **Regex-based solutions are error-prone** and can **miss complex patterns** in unstructured text.
- **Cloud DLP API is more reliable** as it uses **machine learning** to detect sensitive data.
- **Regex requires constant updates**, while Cloud DLP **automatically adapts to new data formats.**

✅ **Reference:**

- **https://cloud.google.com/dlp/docs/concepts-infotypes**

**Conclusion:**

The best approach is **C. De-identify the data using the Cloud Data Loss Prevention (DLP) API**, because it:

- **Automatically detects and removes PII/PCI**.
- **Supports compliance with security regulations** (GDPR, HIPAA, PCI DSS).
- **Is more robust and scalable than regex or encryption alone**.

📌 **Final Reference:**
**https://cloud.google.com/dlp/docs/deidentify-sensitive-data**

---

## Question 39

*Domain 5: Managing Implementation*

**You are working in Cloud Shell and need to install a custom utility that will be available in the default execution path and persist across sessions for future use. Where should you store the file?**

- [x] A. `~/bin`
- [ ] B. **Google Cloud Storage**
- [ ] C. `/google/scripts`
- [ ] D. `/usr/local/bin`

### Explanation

**Correct Answer:**

✅ **A. `~/bin`

Explanation:**

In **Cloud Shell**, the best place to store a **custom utility** that should:

1. **Be available in the default execution path (`$PATH`)**
2. **Persist across Cloud Shell sessions**

is `~/bin` **(Home Directory `bin` folder)**.

✅ **Why `~/bin`?**

- **Cloud Shell home directory (`~/`) persists across sessions.**
- **Files stored in `~/bin` are automatically included in `$PATH`.**
- **Users have write permissions in** `~/bin`, unlike system directories (`/usr/local/bin`).

**Implementation:**

1. **Create the `bin` directory (if it does not exist):**
  ```
  mkdir -p ~/bin
  ```
2. **Move your custom utility to `~/bin`:**
  ```
  tmv my_custom_utility ~/bin/chmod +x ~/bin/my_custom_utility
  ```
3. **Ensure `~/bin` is in your `$PATH`:**
  ```
  echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrcsource ~/.bashrc
  ```
4. **Verify the utility is available:**
  ```
  which my_custom_utility
  ```

✅ **Supporting Documentation:**

- **Cloud Shell Environment**
- **Using Cloud Shell Home Directory**

**Why Other Options Are Incorrect?**

**B. Google Cloud Storage** ❌

- **GCS (`gs://`) is for storing objects, not for executing utilities.**
- **Cloud Shell does not execute binaries directly from Cloud Storage.**
- **Not in** `$PATH`, so the custom utility wouldn’t be easily accessible.

✅ **Reference:**

- **https://cloud.google.com/storage/docs/**

**C.** `/google/scripts` ❌

- **This is a system directory managed by Google Cloud.**
- **Not writable by users**, so a custom utility cannot be installed there.
- **Changes here do not persist across sessions.**

✅ **Reference:**

- **https://cloud.google.com/shell/docs**

**D.** `/usr/local/bin` ❌

- **Cloud Shell does not allow writes to `/usr/local/bin/`.**
- **Files placed here do not persist across sessions.**
- **Users do not have the necessary permissions to install utilities here in Cloud Shell.**

✅ **Reference:**

- **https://cloud.google.com/shell/docs/configuring-cloud-shell**

**Conclusion:**

The best place to **store a custom utility** in **Cloud Shell** so it:
✔ **Persists across sessions**
✔ **Is in the default** `$PATH`
✔ **Is writable by the user**

is `~/bin` (**Option A**).

📌 **Final Reference:**
**https://cloud.google.com/shell/docs/configuring-cloud-shell#files-persistent-storage**

---

## Question 40

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**You need to establish a **private connection** between your **Compute Engine instances** and your **on-premises data center** with a minimum bandwidth requirement of **20 Gbps**, following **Google-recommended best practices**. How should you set up the connection?**

- [x] A. Create a **VPC** and connect it to the on-premises data center using **Dedicated Interconnect**.
- [ ] B. Create a **VPC** and connect it to the on-premises data center using a **single Cloud VPN**.
- [ ] C. Set up a **Cloud Content Delivery Network (Cloud CDN)** and connect it to the on-premises data center using **Dedicated Interconnect**.
- [ ] D. Set up a **Cloud Content Delivery Network (Cloud CDN)** and connect it to the on-premises data center using a **single Cloud VPN**.

### Explanation

**Correct Answer:**

✅ **A. Create a VPC and connect it to the on-premises data center using Dedicated Interconnect.**

**Explanation:**

To **establish a private connection between Compute Engine instances and an on-premises data center** with a **minimum bandwidth requirement of 20 Gbps**, the best approach is to use **Google Cloud Dedicated Interconnect**.

✅ **Why Dedicated Interconnect?**

- **Provides high-bandwidth private connectivity** (supports **10 Gbps and 100 Gbps connections**).
- **Bypasses the public internet**, ensuring **low latency and high reliability**.
- **Can be configured to provide an aggregated 20 Gbps link** (e.g., two 10 Gbps connections).
- **Supports hybrid cloud architecture**, ensuring **secure and direct access to on-prem resources**.

**Implementation Steps:**

1. **Provision Dedicated Interconnect** via the Google Cloud Console or `gcloud` CLI.
2. **Choose a colocation facility** where Google Cloud has an interconnect location.
3. **Set up VLAN attachments and BGP peering** to establish the private connection.
4. **Create a VPC in Google Cloud** and configure **routes to on-premises networks**.

✅ **Supporting Documentation:**

- **Dedicated Interconnect Overview:**
  **https://cloud.google.com/interconnect/docs/how-to/dedicated/overview**
- **Choosing Between Cloud VPN and Interconnect:**
  **https://cloud.google.com/hybrid-connectivity/docs/interconnect-overview**

**Why Other Options Are Incorrect?**

**B. Create a VPC and connect it to the on-premises data center using a single Cloud VPN.** ❌

- **Cloud VPN has a maximum bandwidth limit of 3 Gbps per tunnel** (even with multiple tunnels, it’s **not ideal for 20 Gbps**).
- **Cloud VPN relies on the public internet**, which introduces **higher latency and potential packet loss**.
- **Not suitable for large-scale hybrid cloud architectures requiring high bandwidth.**

✅ **Reference:**

- **https://cloud.google.com/network-connectivity/docs/vpn/concepts/topologies**

**C. Set up a Cloud Content Delivery Network (Cloud CDN) and connect it to the on-premises data center using Dedicated Interconnect.** ❌

- **Cloud CDN is for caching web content globally**, not for hybrid cloud networking.
- **CDN does not establish private connectivity**—it serves cached data from edge locations.
- **Dedicated Interconnect does not integrate with Cloud CDN** for hybrid connectivity.

✅ **Reference:**

- **https://cloud.google.com/cdn/docs/overview**

**D. Set up a Cloud Content Delivery Network (Cloud CDN) and connect it to the on-premises data center using a single Cloud VPN.** ❌

- **Cloud CDN is for optimizing web content delivery**, not for private hybrid networking.
- **Cloud VPN is limited to 3 Gbps per tunnel**, which is insufficient for 20 Gbps bandwidth needs.
- **Cloud VPN uses the public internet**, introducing reliability concerns for high-bandwidth workloads.

✅ **Reference:**

- **https://cloud.google.com/network-connectivity/docs/vpn/concepts/topologies**

**Conclusion:**

The best solution is **A. Create a VPC and connect it to the on-premises data center using Dedicated Interconnect**, because:

- **It provides private, high-bandwidth (20 Gbps+) connectivity.**
- **It bypasses the public internet, ensuring low latency.**
- **It follows Google Cloud’s best practices for hybrid connectivity.**

📌 **Final Reference:**
**https://cloud.google.com/interconnect/docs/how-to/dedicated/overview**

---

## Question 41

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

**You are analyzing and defining business processes to support your startup’s trial usage of Google Cloud Platform (GCP). Since consumer demand for your product is uncertain, your manager requires you to minimize GCP service costs while following Google best practices.**

**What should you do?**

- [ ] A. Utilize the **free tier** and **sustained use discounts**, and assign a **staff position** for managing service costs.
- [x] B. Utilize the **free tier** and **sustained use discounts**, and provide **cost management training** to the team.
- [ ] C. Utilize the **free tier** and **committed use discounts**, and assign a **staff position** for managing service costs.
- [ ] D. Utilize the **free tier** and **committed use discounts**, and provide **cost management training** to the team.

### Explanation

**Correct Answer:**

✅ **B. Utilize the free tier and sustained use discounts, and provide cost management training to the team.**

**Explanation:**

Since **consumer demand for your product is uncertain**, you need to **minimize GCP service costs** while following **Google-recommended best practices**.

**Why This is the Best Approach?**

✅ **1. Utilize the Free Tier**

- **Google Cloud Free Tier** provides **limited free usage** of key GCP services, helping **startups test workloads without initial costs**.
- **Free services include:** Compute Engine, Cloud Storage, BigQuery, and Firebase.

✅ **2. Take Advantage of Sustained Use Discounts (SUDs)**

- **Sustained Use Discounts (SUDs)** automatically apply **cost reductions** when VMs run for long periods in a month.
- **Better for unpredictable workloads**—you get discounts based on actual usage **without upfront commitments**.

✅ **3. Provide Cost Management Training**

- **Educating the team on cost optimization strategies** ensures **long-term cost control** without hiring a dedicated cost manager.
- **Tools like Cloud Billing Reports, Budgets, and Cost Insights** help teams **track and reduce spending**.

✅ **Supporting Documentation:**

- **Google Cloud Free Tier:**
  **https://cloud.google.com/free**
- **Sustained Use Discounts:**
  **https://cloud.google.com/compute/docs/sustained-use-discounts**
- **Cost Management Best Practices:**
  **https://cloud.google.com/billing/docs/how-to/manage-billing-account**

**Why Other Options Are Incorrect?**

**A. Utilize the free tier and sustained use discounts, and assign a staff position for managing service costs.** ❌

- **Hiring a dedicated staff member for cost management** increases **operational expenses**, which contradicts the goal of minimizing costs.
- **Providing training (Option B) is a more cost-effective solution.**

**C. Utilize the free tier and committed use discounts, and assign a staff position for managing service costs.** ❌

- **Committed Use Discounts (CUDs) require upfront commitments**, which **is not ideal for uncertain demand**.
- **Locking into long-term commitments** may **increase costs if workloads change**.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts**

**D. Utilize the free tier and committed use discounts, and provide cost management training to the team.** ❌

- **Committed Use Discounts (CUDs) are cost-effective only for predictable workloads**, but the scenario specifies **uncertain consumer demand**.
- **Sustained Use Discounts (SUDs) are better suited for fluctuating demand.**

**Conclusion:**

The best approach is **B. Utilize the free tier and sustained use discounts, and provide cost management training to the team**, because:

- **Sustained Use Discounts (SUDs) offer flexibility for uncertain workloads.**
- **The free tier reduces initial costs.**
- **Training the team ensures long-term cost efficiency without adding extra staffing costs.**

📌 **Final Reference:**
**https://cloud.google.com/compute/docs/sustained-use-discounts**

---

## Question 42

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

**You are building a continuous deployment pipeline for a project stored in a Git repository. You need to ensure that code changes are verified before being deployed to production.**

**What should you do?**

- [ ] A. Use **Spinnaker** to deploy builds to production using the **red/black deployment strategy**, allowing easy rollbacks if needed.
- [ ] B. Use **Spinnaker** to deploy builds directly to production and run tests on the production deployment.
- [ ] C. Use **Jenkins** to build both the **staging branches** and the **master branch**, then deploy changes to **10% of users** before performing a full rollout.
- [x] D. Use **Jenkins** to monitor **repository tags**, deploy **staging tags** to a **staging environment** for testing, and after successful testing, tag the repository for **production deployment**.

### Explanation

**Correct Answer:**

✅ **D. Use Jenkins to monitor repository tags, deploy staging tags to a staging environment for testing, and after successful testing, tag the repository for production deployment.**

**Explanation:**

To ensure that **code changes are verified before being deployed to production**, a **controlled deployment pipeline with a staging environment** is required.

✅ **Why This Works:**

- **Jenkins automates the build and deployment process**, reducing human error.
- **Using repository tags for staged deployments** ensures **only tested and verified code is deployed to production**.
- **Deploying to a staging environment first allows for testing before production rollout.**
- **Production deployments are triggered only when a repository is tagged for release**, ensuring consistency.

**Implementation Steps:**

1. **Monitor Git repository for new tags** using Jenkins.
2. **Deploy staging tags to a staging environment** for integration and functional testing.
3. **Run automated tests and manual verification** in staging.
4. **If staging tests pass, tag the repository with a production tag.**
5. **Jenkins deploys production tags to production.**

✅ **Supporting Documentation:**

- **Jenkins Git Integration for Tag-Based Deployments:**
  **https://www.jenkins.io/doc/book/pipeline/scm**
- **CI/CD Best Practices for Jenkins:**
  **https://cloud.google.com/architecture/continuous-deployment-with-jenkins**

**Why Other Options Are Incorrect?**

**A. Use Spinnaker to deploy builds to production using the red/black deployment strategy, allowing easy rollbacks if needed.** ❌

- **Red/black (blue/green) deployment helps with rollback but does not verify code before deployment.**
- **The requirement is to verify before production, not just to handle rollbacks.**

✅ **Reference:**

- **https://spinnaker.io/docs/concepts/deployment-strategies**

**B. Use Spinnaker to deploy builds directly to production and run tests on the production deployment.** ❌

- **Testing should be done in a staging environment first, not in production.**
- **Running tests directly in production risks deploying unverified code to users.**

✅ **Reference:**

- **https://spinnaker.io/docs/setup/ci/jenkins**

**C. Use Jenkins to build both the staging branches and the master branch, then deploy changes to 10% of users before performing a full rollout.** ❌

- **Deploying changes to 10% of users first (canary deployment) is useful, but does not ensure that code is properly verified before any production deployment.**
- **The question requires full verification before deployment, which staging and tagging provide.**

✅ **Reference:**

- **https://cloud.google.com/architecture/canary-deployments-on-gke**

**Conclusion:**

The best approach is **D. Use Jenkins to monitor repository tags, deploy staging tags to a staging environment for testing, and after successful testing, tag the repository for production deployment**, because:

- **It ensures code is tested before production deployment.**
- **It provides a structured, controlled release process.**
- **It prevents unverified changes from reaching production.**

📌 **Final Reference:**
**https://cloud.google.com/architecture/continuous-deployment-with-jenkins**

---

## Question 43

*Domain 6: Ensuring Solution and Operations Excellence*

**Your Compute Engine managed instance group is experiencing an outage, where all instances restart every 5 seconds. A health check is configured, but autoscaling is disabled. Your colleague, who is a Linux expert, has offered to help diagnose the issue.**

**How can you ensure that your colleague can access the VMs to investigate the problem?**

- [ ] A. Assign your colleague the **IAM role of Project Viewer**.
- [ ] B. Perform a **rolling restart** on the instance group.
- [x] C. **Disable the health check**, then add their SSH key to the **project-wide SSH Keys**.
- [ ] D. **Disable autoscaling**, then add their SSH key to the **project-wide SSH Keys**.

### Explanation

**Correct Answer:**

✅ **C. Disable the health check, then add their SSH key to the project-wide SSH Keys.**

**Explanation:**

Since **all instances in the managed instance group (MIG) are restarting every 5 seconds**, it's likely that the **health check is continuously failing**, causing the instances to be **terminated and recreated**.

**Why This Works:**

1. **Disabling the health check** prevents the **instance group from automatically terminating and recreating instances**.
2. **Adding an SSH key at the project-wide level** ensures **your colleague can log in** to the instances for debugging.
3. **Since autoscaling is already disabled**, we don’t need to take action on it.

**Implementation Steps:**

1. **Disable the health check:**
  ```
  gcloud compute instance-groups managed update INSTANCE_GROUP_NAME \    --no-health-check
  ```
2. **Add your colleague’s SSH key to the project-wide metadata:**
  ```
  gcloud compute project-info add-metadata \    --metadata ssh-keys="username:ssh-rsa AAAAB3Nz..."
  ```
3. **Have your colleague SSH into an instance for investigation:**
  ```
  gcloud compute ssh INSTANCE_NAME --zone=ZONE
  ```
4. **Re-enable the health check once the issue is resolved.**

✅ **Supporting Documentation:**

- **Troubleshooting Managed Instance Groups:**
  **https://cloud.google.com/compute/docs/instance-groups/troubleshooting-instance-groups**
- **Adding SSH Keys to Metadata:**
  **https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys**

**Why Other Options Are Incorrect?**

**A. Assign your colleague the IAM role of Project Viewer.** ❌

- **IAM Project Viewer does not grant SSH access.**
- **It only allows read access to resources but does not permit login to instances.**

✅ **Reference:**

- **https://cloud.google.com/iam/docs/understanding-roles**

**B. Perform a rolling restart on the instance group.** ❌

- **Restarting instances does not resolve the root cause** (likely a failing health check).
- **The issue will persist if the health check continues to fail.**

✅ **Reference:**

- **https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups**

**D. Disable autoscaling, then add their SSH key to the project-wide SSH Keys.** ❌

- **Autoscaling is already disabled**, so disabling it **again does not help.**
- **The issue is the health check causing frequent instance terminations, not autoscaling.**

✅ **Reference:**

- **https://cloud.google.com/compute/docs/autoscaler**

**Conclusion:**

The best solution is **C. Disable the health check, then add their SSH key to the project-wide SSH Keys**, because:

- **It prevents the instance group from continuously restarting instances.**
- **It allows your colleague to log in and diagnose the issue.**
- **Once the issue is resolved, the health check can be re-enabled.**

📌 **Final Reference:**
**https://cloud.google.com/compute/docs/instance-groups/troubleshooting-instance-groups**

---

## Question 44

*Domain 3: Designing for Security and Compliance*

**Your company is migrating its on-premises data center to the cloud and plans to integrate Google Kubernetes Engine (GKE) for workload orchestration. Certain parts of your architecture must also comply with PCI DSS requirements.**

**Which statement is most accurate?**

- [ ] A. **App Engine** is the **only** compute platform on GCP that is **certified** for PCI DSS hosting.
- [ ] B. **GKE cannot be used** under PCI DSS because it is considered **shared hosting**.
- [x] C. **GKE and GCP** provide the necessary **tools and configurations** to build a **PCI DSS-compliant** environment.
- [ ] D. **All Google Cloud services** can be used because **Google Cloud Platform** is **fully PCI-compliant**.

### Explanation

**Correct Answer:**

✅ **C. GKE and GCP provide the necessary tools and configurations to build a PCI DSS-compliant environment.**

**Explanation:**

Google Cloud **does not automatically make workloads PCI DSS compliant**, but it **provides the necessary tools and configurations** to help organizations build a **PCI DSS-compliant environment** on **Google Kubernetes Engine (GKE)**.

✅ **Why GKE Can Be Used for PCI DSS Compliance?**

- **Google Cloud is PCI DSS compliant**, meaning **it provides a compliant infrastructure**.
- **GKE supports network segmentation, encryption, and access controls**, which are essential for PCI DSS compliance.
- **Google Cloud’s PCI DSS Attestation of Compliance (AOC) applies to services including GKE.**
- **Companies must still configure their applications correctly** to meet PCI DSS controls.

**Key PCI DSS Compliance Features in GCP and GKE:**

- **VPC Service Controls**: Restrict access to PCI-sensitive workloads.
- **Cloud Audit Logs**: Monitor user access and API calls for compliance.
- **Shielded VMs**: Protect Kubernetes worker nodes from unauthorized modifications.
- **Private GKE Clusters**: Prevent public exposure of workloads.
- **Encryption (At-Rest and In-Transit)**: Meet PCI DSS encryption requirements.

✅ **Supporting Documentation:**

- **Google Cloud PCI DSS Compliance Overview:**
  **https://cloud.google.com/security/compliance/pci-dss**
- **Best Practices for PCI DSS on GKE:**
  **https://cloud.google.com/blog/products/gcp/building-pci-dss-compliant-solutions-on-gcp**

**Why Other Options Are Incorrect?**

**A. App Engine is the only compute platform on GCP that is certified for PCI DSS hosting.** ❌

- **Incorrect because multiple GCP services, including GKE, Compute Engine, and Cloud SQL, can be used for PCI DSS-compliant workloads.**
- **Google Cloud provides PCI DSS compliance tools across multiple compute platforms.**

✅ **Reference:**

- **https://cloud.google.com/security/compliance/pci-dss**

**B. GKE cannot be used under PCI DSS because it is considered shared hosting.** ❌

- **Incorrect because PCI DSS compliance can be achieved in a shared responsibility model.**
- **Google Cloud provides isolation mechanisms such as private clusters, namespaces, and workload identity.**
- **Google Cloud maintains PCI DSS compliance for the infrastructure, while customers must implement application-level security.**

✅ **Reference:**

- **https://cloud.google.com/kubernetes-engine/docs/concepts/security-overview**

**D. All Google Cloud services can be used because Google Cloud Platform is fully PCI-compliant.** ❌

- **Incorrect because while Google Cloud is PCI DSS compliant, not all services are inherently PCI-compliant.**
- **Customers must implement additional controls** (e.g., encryption, network segmentation, logging).
- **GCP follows a shared responsibility model**—Google secures the infrastructure, but users must secure their applications.

✅ **Reference:**

- **https://cloud.google.com/security/compliance/pci-dss**

**Conclusion:**

The best answer is **C. GKE and GCP provide the necessary tools and configurations to build a PCI DSS-compliant environment**, because:

- **Google Cloud provides PCI DSS compliance at the infrastructure level.**
- **GKE offers features (encryption, network controls, audit logs) to meet compliance requirements.**
- **Companies must implement best practices to achieve full PCI DSS compliance.**

📌 **Final Reference:**
**https://cloud.google.com/security/compliance/pci-dss**

---

## Question 45

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**Your company has multiple on-premises systems that serve as data sources for reporting. Over time, the data has not been well maintained and has degraded. You need to follow Google-recommended best practices to detect anomalies and clean the data.**

**What should you do?**

- [ ] A. **Upload files to Cloud Storage**, then use **Cloud Datalab** to explore and clean the data.
- [x] B. **Upload files to Cloud Storage**, then use **Cloud Dataprep** to explore and clean the data.
- [ ] C. **Connect Cloud Datalab** to the on-premises systems and use it to explore and clean the data.
- [ ] D. **Connect Cloud Dataprep** to the on-premises systems and use it to explore and clean the data.

### Explanation

**Correct Answer:**

✅ **B. Upload files to Cloud Storage, then use Cloud Dataprep to explore and clean the data.**

**Explanation:**

To **detect anomalies and clean degraded data** from multiple on-premises systems, **Google recommends using Cloud Dataprep**, which is an **intelligent data wrangling service** designed for **exploratory data analysis and cleaning**.

**Why This is the Best Approach?**

1. **Cloud Dataprep is specifically designed for data cleaning and anomaly detection.**
  - Uses **AI/ML-driven data profiling** to detect anomalies and suggest transformations.
  - Supports **deduplication, missing data handling, and outlier detection.**
2. **Google-recommended approach for data cleaning:**
  - **Step 1:** Upload raw data to **Cloud Storage** for scalable processing.
  - **Step 2:** Use **Cloud Dataprep** to **profile, clean, and transform** data before analysis.
3. **Cloud Dataprep is fully managed and no-code.**
  - Does **not require writing SQL or Python scripts** for cleaning data.
  - **Works seamlessly with BigQuery for further analysis.**

✅ **Supporting Documentation:**

- **Cloud Dataprep Overview:**
  **https://cloud.google.com/dataprep**
- **Best Practices for Data Cleaning:**
  **https://cloud.google.com/blog/topics/developers-practitioners/how-clean-and-transform-your-data-cloud-dataprep**

**Why Other Options Are Incorrect?**

**A. Upload files to Cloud Storage, then use Cloud Datalab to explore and clean the data.** ❌

- **Cloud Datalab is a Jupyter-based notebook environment** used for **data science and ML**, not primarily for **data cleaning and anomaly detection**.
- **Cloud Dataprep is a better tool** because it provides **automatic anomaly detection and transformations**.

✅ **Reference:**

- **https://cloud.google.com/datalab**

**C. Connect Cloud Datalab to the on-premises systems and use it to explore and clean the data.** ❌

- **Directly connecting Cloud Datalab to on-premises systems is not a scalable approach.**
- **Cloud Datalab does not provide automated anomaly detection**, requiring **manual scripting for data cleaning**.
- **Better approach:** Upload data to **Cloud Storage** first, then use **Cloud Dataprep**.

✅ **Reference:**

- **https://cloud.google.com/datalab/docs/quickstarts**

**D. Connect Cloud Dataprep to the on-premises systems and use it to explore and clean the data.** ❌

- **Cloud Dataprep does not support direct connections to on-premises systems.**
- **Google-recommended approach:**
  1. **Upload on-prem data to Cloud Storage**.
  2. **Use Cloud Dataprep to clean and process the data**.

✅ **Reference:**

- **https://cloud.google.com/dataprep/docs**

**Conclusion:**

The best approach is **B. Upload files to Cloud Storage, then use Cloud Dataprep to explore and clean the data**, because:

- **Cloud Dataprep is specifically designed for anomaly detection and data cleaning.**
- **Uploading data to Cloud Storage ensures scalability and reliability.**
- **This follows Google Cloud's best practices for handling and preparing data.**

📌 **Final Reference:**
**https://cloud.google.com/dataprep**

**⚠️ Note:** Cloud Datalab is retired (replaced by Vertex AI Workbench notebooks). Dataprep is a partner service run by Trifacta (now Alteryx). The pattern to remember: land the files in Cloud Storage, then clean them with a visual data-prep tool.

---

## Question 46

*Domain 3: Designing for Security and Compliance*

**Google Cloud Platform (GCP) resources are **managed hierarchically** using **organizations, folders, and projects**. When **Cloud Identity and Access Management (IAM) policies** are applied at different levels of the hierarchy, what determines the **effective policy** at a specific node?**

- [ ] A. The effective policy is determined **only** by the policy set at that node.
- [ ] B. The effective policy is the policy set at the node and is **restricted** by the policies of its ancestors.
- [x] C. The effective policy is the **union** of the policy set at the node and policies **inherited from its ancestors**.
- [ ] D. The effective policy is the **intersection** of the policy set at the node and policies inherited from its ancestors.

### Explanation

**Correct Answer:**

✅ **C. The effective policy is the union of the policy set at the node and policies inherited from its ancestors.**

**Explanation:**

Google Cloud Platform (GCP) follows a **hierarchical resource model** for managing **Identity and Access Management (IAM) policies** at different levels:

1. **Organization (Root Level) → Folders → Projects → Resources**
2. **IAM policies inherit downward**, meaning:
  - Policies set at **higher levels (Organization, Folder, or Project)** apply to all **child resources**.
  - **Policies are additive**—permissions granted at a higher level **cannot be restricted by lower levels**.

✅ **Key IAM Inheritance Rules:**

- **If a role is granted at a higher level (e.g., Folder or Organization), it automatically applies to all child nodes unless an IAM deny policy blocks it.**
- **If a node (Project or Folder) has additional role bindings, they are combined with inherited policies to form the effective policy.**
- **Allow policies are additive.** Separate IAM deny policies (available since 2022) can block specific permissions, and they are evaluated before allow policies.

✅ **Example Scenario:**

1. **Organization Level:**
  - `user@example.com` is assigned **Viewer** (`roles/viewer`) at the **organization** level.
2. **Folder Level:**
  - The **folder inherits Viewer permissions** from the Organization.
  - Additionally, `user@example.com` is granted **Editor** (`roles/editor`) at the **folder level**.
3. **Project Level:**
  - The **project inherits both Viewer and Editor** from the folder.
  - If no additional roles are assigned at the project level, the user **has both Viewer and Editor permissions** on the project.

Thus, the **effective IAM policy at any node is the union of inherited and explicitly assigned permissions**.

✅ **Supporting Documentation:**

- **IAM Policy Hierarchy:**
  **https://cloud.google.com/iam/docs/policy-hierarchy**
- **Understanding IAM Policy Inheritance:**
  **https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy**

**Why Other Options Are Incorrect?**

**A. The effective policy is determined only by the policy set at that node.** ❌

- **Incorrect because IAM policies are inherited downward from parent nodes.**
- **Higher-level IAM policies (Organization, Folder) apply to all child resources.**

✅ **Reference:**

- **https://cloud.google.com/iam/docs/policy-hierarchy**

**B. The effective policy is the policy set at the node and is restricted by the policies of its ancestors.** ❌

- **Incorrect because IAM policies are additive and cannot restrict permissions granted by ancestors.**
- **Once a permission is granted at a higher level, it applies to all child nodes unless explicitly removed (which GCP IAM does not support).**

✅ **Reference:**

- **https://cloud.google.com/iam/docs/policies**

**D. The effective policy is the intersection of the policy set at the node and policies inherited from its ancestors.** ❌

- **Incorrect because IAM permissions do not get "intersected."**
- **Permissions are combined (union), not filtered (intersection).**

✅ **Reference:**

- **https://cloud.google.com/iam/docs/understanding-policies**

**Conclusion:**

The best answer is **C. The effective policy is the union of the policy set at the node and policies inherited from its ancestors**, because:

- **IAM policies are inherited downward** from Organization → Folder → Project → Resources.
- **Permissions are additive**—roles assigned at higher levels **apply to all child nodes**.
- **The effective policy is a combination of inherited and explicitly assigned roles.**

📌 **Final Reference:**
**https://cloud.google.com/iam/docs/policy-hierarchy**

**⚠️ Note:** IAM deny policies now exist and override allow policies. The answer is still C: the effective *allow* policy is the union of the node's allow policy and its ancestors'.

---

## Question 47

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**You are migrating an on-premises solution to Google Cloud in multiple phases. During the transition, you will use Cloud VPN to maintain connectivity between your on-premises systems and Google Cloud. You need to ensure that all on-premises systems remain reachable throughout the migration.**

**How should you configure networking in Google Cloud?**

- [ ] A. Use the **same IP range** on Google Cloud as you use on-premises.
- [ ] B. Use the **same IP range** on Google Cloud as on-premises for your **primary range**, and assign a **secondary range** that does **not overlap** with your on-premises range.
- [x] C. Use an **IP range on Google Cloud that does not overlap** with your on-premises range.
- [ ] D. Use an **IP range on Google Cloud that does not overlap** with your on-premises range for the **primary range**, and configure a **secondary range that matches** your on-premises IP range.

### Explanation

**Correct Answer:**

✅ **C. Use an IP range on Google Cloud that does not overlap with your on-premises range.**

**Explanation:**

When using **Cloud VPN** to maintain connectivity between **on-premises systems and Google Cloud**, **IP address overlap must be avoided** to prevent **routing conflicts** and **connectivity issues**.

✅ **Why Use a Non-Overlapping IP Range in Google Cloud?**

- **Cloud VPN requires distinct, non-overlapping IP ranges** for Google Cloud and on-premises networks to enable proper routing.
- **Overlapping IP ranges cause routing conflicts** because Cloud VPN cannot differentiate traffic between on-prem and Google Cloud.
- **Google-recommended hybrid networking best practice** is to assign **a unique CIDR block** to Google Cloud that does not exist in the on-prem network.

**Implementation Steps:**

1. **Determine your on-premises IP range** (e.g., `192.168.1.0/24`).
2. **Choose a distinct IP range for Google Cloud** (e.g., `10.10.0.0/16`) that does **not** overlap with on-prem.
3. **Configure Cloud VPN** to establish secure connectivity between Google Cloud and the on-prem network.
4. **Set up custom routes in VPC** to enable traffic between the two networks.

✅ **Supporting Documentation:**

- **Google Cloud VPN Overview:**
  **https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview**
- **Avoiding Overlapping IP Ranges in Hybrid Cloud:**
  **https://cloud.google.com/network-connectivity/docs/vpn/how-to/topologies**

**Why Other Options Are Incorrect?**

**A. Use the same IP range on Google Cloud as you use on-premises.** ❌

- **This causes IP conflicts and routing failures** because the same subnet would exist in both networks.
- **Cloud VPN would not be able to distinguish between on-prem and Google Cloud traffic.**

✅ **Reference:**

- **https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview**

**B. Use the same IP range on Google Cloud as on-premises for your primary range, and assign a secondary range that does not overlap with your on-premises range.** ❌

- **The primary range must not overlap with on-prem** to avoid routing conflicts.
- **Even if a secondary range is non-overlapping, the primary range would still create connectivity issues.**

✅ **Reference:**

- **https://cloud.google.com/vpc/docs/subnets#ip_ranges**

**D. Use an IP range on Google Cloud that does not overlap with your on-premises range for the primary range, and configure a secondary range that matches your on-premises IP range.** ❌

- **A secondary range that overlaps with on-premises would still create conflicts.**
- **Both primary and secondary ranges in Google Cloud should be unique and non-overlapping with on-prem.**

✅ **Reference:**

- **https://cloud.google.com/vpc/docs/subnets**

**Conclusion:**

The best approach is **C. Use an IP range on Google Cloud that does not overlap with your on-premises range**, because:

- **Avoids routing conflicts and ensures proper connectivity**.
- **Follows Google Cloud’s hybrid networking best practices**.
- **Ensures a seamless migration while keeping on-premises systems reachable.**

📌 **Final Reference:**
**https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview**

---

## Question 48

*Domain 5: Managing Implementation*

**You have discovered an error in your App Engine application caused by missing Cloud Datastore indexes. To resolve this, you have created a YAML configuration file specifying the required indexes.**

**How should you deploy these new indexes to Cloud Datastore?**

- [x] A. Use the command `gcloud datastore create-indexes` and specify your configuration file.
- [ ] B. Upload the **YAML configuration file** to **App Engine’s default Cloud Storage bucket**, allowing App Engine to detect the new indexes.
- [ ] C. In the **Google Cloud Console**, navigate to **Datastore Admin**, delete the current indexes, and upload the new configuration file.
- [ ] D. Send an **HTTP request** to the **built-in Python module** to upload the index configuration file to your application.

### Explanation

**Correct Answer:**

✅ **A. Use the command `gcloud datastore indexes create` and specify your configuration file.**

**Explanation:**

To deploy new indexes to **Cloud Datastore**, you need to use the **Google Cloud CLI (`gcloud`)** to apply the YAML configuration file that defines the indexes.

**Correct Procedure to Deploy Indexes:**

1. **Create or modify an `index.yaml` file** that defines the required indexes.
2. **Deploy the indexes using the following command:**
  ```
  gcloud datastore indexes create index.yaml
  ```
3. **Verify that the indexes are being built** by checking the status in the **Google Cloud Console → Datastore → Indexes**.

✅ **Why This Works:**

- `gcloud datastore indexes create` is the recommended way to deploy index configurations.
- **Indexes must be explicitly created in Cloud Datastore** before queries can use them.
- **Once submitted, indexes are automatically built by Cloud Datastore** and available for querying.

✅ **Supporting Documentation:**

- **Managing Datastore Indexes:**
  **https://cloud.google.com/datastore/docs/tools/indexconfig**
- **Deploying Indexes Using `gcloud` CLI:**
  **https://cloud.google.com/datastore/docs/creating-indexes**

**Why Other Options Are Incorrect?**

**B. Upload the YAML configuration file to App Engine’s default Cloud Storage bucket, allowing App Engine to detect the new indexes.** ❌

- **App Engine does not automatically detect new index configurations from Cloud Storage.**
- **Cloud Datastore requires an explicit deployment using the `gcloud` CLI.**
- **Storing the YAML file in Cloud Storage has no effect on Datastore indexing.**

✅ **Reference:**

- **https://cloud.google.com/datastore/docs/tools/indexconfig**

**C. In the Google Cloud Console, navigate to Datastore Admin, delete the current indexes, and upload the new configuration file.** ❌

- **There is no option to manually upload an `index.yaml` file in the Google Cloud Console.**
- **Deleting indexes can break existing queries**—instead, new indexes should be added incrementally.
- **Indexes are created and modified using the `gcloud` CLI or the Datastore Admin API.**

✅ **Reference:**

- **https://cloud.google.com/datastore/docs/tools/indexconfig**

**D. Send an HTTP request to the built-in Python module to upload the index configuration file to your application.** ❌

- **There is no built-in Python module in App Engine for deploying Datastore indexes.**
- **Index creation must be explicitly managed via** `gcloud datastore indexes create`.
- **Datastore does not support uploading index configurations via HTTP requests.**

✅ **Reference:**

- **https://cloud.google.com/datastore/docs/creating-indexes**

**Conclusion:**

The best approach is **A. Use the command `gcloud datastore indexes create` and specify your configuration file**, because:

- **This is the official method to deploy Cloud Datastore indexes.**
- **It ensures the indexes are properly registered and built.**
- **It follows Google Cloud’s best practices for managing index configurations.**

📌 **Final Reference:**
**https://cloud.google.com/datastore/docs/tools/indexconfig**

**⚠️ Note:** `gcloud datastore create-indexes` is the older, deprecated form of the command; the current one is `gcloud datastore indexes create index.yaml`. Cloud Datastore is now Firestore in Datastore mode.

---

## Question 49

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**You are designing an architecture for an application running on Compute Engine, ensuring it meets the disaster recovery plan requirement of failing over to another region in case of a regional outage.**

**What should you do?**

- [ ] A. Deploy the application on **two Compute Engine instances** in the **same project but different regions**. Use the **first instance** to serve traffic and configure **HTTP Load Balancing** to fail over to the standby instance in case of a disaster.
- [ ] B. Deploy the application on a **single Compute Engine instance** to serve traffic and configure **HTTP Load Balancing** to fail over to an instance running **on-premises** in case of a disaster.
- [x] C. Deploy the application on **two Compute Engine instance groups**, each in the **same project but in different regions**. Use the **first instance group** to serve traffic and configure **HTTP Load Balancing** to fail over to the standby instance group in case of a disaster.
- [ ] D. Deploy the application on **two Compute Engine instance groups**, each in a **separate project and different region**. Use the **first instance group** to serve traffic and configure **HTTP Load Balancing** to fail over to the standby instance group in case of a disaster.

### Explanation

**Correct Answer:**

✅ **C. Deploy the application on two Compute Engine instance groups, each in the same project but in different regions. Use the first instance group to serve traffic and configure HTTP Load Balancing to fail over to the standby instance group in case of a disaster.**

**Explanation:**

To meet the **disaster recovery plan requirement** of **failing over to another region in case of a regional outage**, the best practice is to:

1. **Deploy the application in multiple regions** to ensure high availability.
2. **Use Compute Engine instance groups** instead of single instances for better scalability and fault tolerance.
3. **Leverage HTTP Load Balancing with cross-region failover** to direct traffic to a standby instance group when the primary region becomes unavailable.

✅ **Why This Works:**

- **Regional instance groups** ensure that workloads can be distributed across **multiple zones** within a region.
- **Global HTTP(S) Load Balancing** can automatically detect failures and route traffic to a healthy region.
- **Compute Engine Instance Groups** provide **auto-healing**, load balancing, and **automatic scaling**.
- **Google Cloud's cross-region failover** ensures traffic is rerouted seamlessly if the primary region fails.

**Implementation Steps:**

1. **Deploy the application using two Compute Engine instance groups in different regions.**
2. **Configure HTTP(S) Load Balancing** to route traffic to the primary region and fail over to the standby region if needed.
3. **Enable health checks** to detect when the primary instance group is down.
4. **Set up Cloud DNS** with a global frontend IP to ensure seamless routing.

✅ **Supporting Documentation:**

- **Google Cloud Disaster Recovery Planning:**
  **https://cloud.google.com/architecture/dr-scenarios**
- **Global HTTP Load Balancing for Failover:**
  **https://cloud.google.com/load-balancing/docs/https/global-ext-backend-failover**

**Why Other Options Are Incorrect?**

**A. Deploy the application on two Compute Engine instances in the same project but different regions. Use the first instance to serve traffic and configure HTTP Load Balancing to fail over to the standby instance in case of a disaster.** ❌

- **Incorrect because individual Compute Engine instances do not provide auto-healing or scalability.**
- **Instance Groups provide automatic instance replacement, which a single instance does not.**

✅ **Reference:**

- **https://cloud.google.com/compute/docs/instance-groups**

**B. Deploy the application on a single Compute Engine instance to serve traffic and configure HTTP Load Balancing to fail over to an instance running on-premises in case of a disaster.** ❌

- **Not recommended because it introduces dependencies on an on-premises system, increasing complexity and latency.**
- **Google Cloud best practices recommend failing over to another cloud region, not an on-premises instance.**

✅ **Reference:**

- **https://cloud.google.com/architecture/dr-scenarios**

**D. Deploy the application on two Compute Engine instance groups, each in a separate project and different region. Use the first instance group to serve traffic and configure HTTP Load Balancing to fail over to the standby instance group in case of a disaster.** ❌

- **Using multiple projects adds unnecessary complexity**—IAM, networking, and load balancing become harder to manage.
- **Best practice is to keep both instance groups within the same project for better policy and resource management.**

✅ **Reference:**

- **https://cloud.google.com/load-balancing/docs/https/global-ext-backend-failover**

**Conclusion:**

The best approach is **C. Deploy the application on two Compute Engine instance groups, each in the same project but in different regions. Use the first instance group to serve traffic and configure HTTP Load Balancing to fail over to the standby instance group in case of a disaster.**

✔ **Ensures regional failover with minimal downtime**
✔ **Uses instance groups for scalability and auto-healing**
✔ **Leverages HTTP Load Balancing for intelligent traffic routing**

📌 **Final Reference:**
**https://cloud.google.com/load-balancing/docs/https/global-ext-backend-failover**

---

## Question 50

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**You are deploying an application on App Engine that needs to integrate with an on-premises database. For security reasons, the on-premises database must not be accessible via the public internet.**

**What should you do?**

- [ ] A. Deploy the application on **App Engine standard environment** and use **App Engine firewall rules** to restrict access to the open on-premises database.
- [ ] B. Deploy the application on **App Engine standard environment** and use **Cloud VPN** to establish a private connection to the on-premises database.
- [ ] C. Deploy the application on **App Engine flexible environment** and use **App Engine firewall rules** to restrict access to the on-premises database.
- [x] D. Deploy the application on **App Engine flexible environment** and use **Cloud VPN** to establish a private connection to the on-premises database.

### Explanation

**Correct Answer:**

✅ **D. Deploy the application on App Engine flexible environment and use Cloud VPN to establish a private connection to the on-premises database.**

**Explanation:**

Since **the on-premises database must not be accessible via the public internet**, you need to:

1. **Use a private connection** between Google Cloud and the on-premises network.
2. **Deploy the application on App Engine flexible environment**, as App Engine standard **does not support direct network access to Cloud VPN**.
3. **Establish a Cloud VPN connection** to securely connect App Engine to the on-premises database over a private network.

**Why This Works?**

✅ **App Engine Flexible Environment**

- **Supports network configuration** that allows direct communication with a private on-premises network via Cloud VPN.
- **Uses Compute Engine VMs**, which have configurable networking capabilities.
- **Allows private IP connectivity** to non-publicly accessible resources.

✅ **Cloud VPN**

- **Enables a secure, private connection** between Google Cloud and on-premises networks.
- **Traffic never traverses the public internet**, ensuring security compliance.

**Implementation Steps:**

1. **Set up Cloud VPN** to establish a private connection to the on-premises database.
2. **Configure firewall rules** to allow App Engine flexible instances to communicate with the on-prem database.
3. **Ensure the App Engine service account has the necessary IAM roles** to access the database.

✅ **Supporting Documentation:**

- **App Engine Flexible Networking:**
  **https://cloud.google.com/appengine/docs/flexible**
- **Using Cloud VPN for Hybrid Connectivity:**
  **https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview**

**Why Other Options Are Incorrect?**

**A. Deploy the application on App Engine standard environment and use App Engine firewall rules to restrict access to the open on-premises database.** ❌

- **App Engine standard does not support direct network access to Cloud VPN or private IPs.**
- **Firewall rules do not provide a private connection** to the on-premises database.
- **This option would still expose the database over the public internet.**

✅ **Reference:**

- **https://cloud.google.com/appengine/docs/standard**

**B. Deploy the application on App Engine standard environment and use Cloud VPN to establish a private connection to the on-premises database.** ❌

- **App Engine standard cannot connect directly to Cloud VPN or private networks.**
- **Standard environment apps are sandboxed and do not allow custom networking configurations.**

✅ **Reference:**

- **https://cloud.google.com/appengine/docs/standard**

**C. Deploy the application on App Engine flexible environment and use App Engine firewall rules to restrict access to the on-premises database.** ❌

- **Firewall rules only restrict access but do not establish a private connection.**
- **A VPN is still required** to ensure the on-premises database is accessible privately.

✅ **Reference:**

- **https://cloud.google.com/appengine/docs/flexible**

**Conclusion:**

The best approach is **D. Deploy the application on App Engine flexible environment and use Cloud VPN to establish a private connection to the on-premises database**, because:

- **App Engine flexible supports private networking.**
- **Cloud VPN ensures secure, private connectivity.**
- **It aligns with Google Cloud best practices for hybrid networking.**

📌 **Final Reference:**
**https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview**

**⚠️ Note:** App Engine standard can now reach a VPC (and on-premises over Cloud VPN) through a **Serverless VPC Access connector** (Exam 3 · Q25). Option B mentions only Cloud VPN, with no connector, so flexible + Cloud VPN is still the best of these options.

---

## Question 51

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**You are working in a highly secured environment where public internet access from Compute Engine VMs is not allowed. There is no VPN connection to access an on-premises file server yet. You need to install specific software on a Compute Engine instance.**

**How should you install the software?**

- [x] A. **Upload the installation files to Cloud Storage**, configure the VM on a **subnet with Private Google Access**, assign **only an internal IP** to the VM, and download the files using **gsutil**.
- [ ] B. **Upload the installation files to Cloud Storage**, configure **firewall rules to block all traffic** except the **IP address range for Cloud Storage**, and download the files using **gsutil**.
- [ ] C. **Upload the installation files to Cloud Source Repositories**, configure the VM on a **subnet with Private Google Access**, assign **only an internal IP** to the VM, and download the files using **gcloud**.
- [ ] D. **Upload the installation files to Cloud Source Repositories**, configure **firewall rules to block all traffic** except the **IP address range for Cloud Source Repositories**, and download the files using **gsutil**.

### Explanation

**Correct Answer:**

✅ **A. Upload the installation files to Cloud Storage, configure the VM on a subnet with Private Google Access, assign only an internal IP to the VM, and download the files using gsutil.**

**Explanation:**

Since the **Compute Engine VM is in a highly secured environment** with **no public internet access**, and there is **no VPN connection to an on-prem file server**, you need a **private and secure way** to download installation files.

**Why This Works?**

1. **Cloud Storage is the best place to store installation files** because it is a **fully managed, secure, and scalable** storage service.
2. **Private Google Access (PGA)** allows VMs with **only internal IPs** to access Google APIs and services (such as Cloud Storage) **without requiring public internet access**.
3. **Using `gsutil` over Private Google Access** ensures **secure and restricted access** to the installation files.

**Implementation Steps:**

1. **Upload the installation files to a Cloud Storage bucket:**
  ```
  bashCopyEditgsutil cp software_package.tar.gz gs://my-secure-bucket/
  ```
2. **Ensure the VM is in a VPC subnet with Private Google Access enabled:**
  - In **Google Cloud Console**, navigate to **VPC network → Subnets → Edit subnet**.
  - Enable **Private Google Access** for the subnet.
3. **Assign only an internal IP to the VM (no public IP).**
4. **Download the files to the VM using `gsutil`:**
  ```
  bashCopyEditgsutil cp gs://my-secure-bucket/software_package.tar.gz .
  ```

✅ **Supporting Documentation:**

- **Private Google Access Overview:**
  **https://cloud.google.com/vpc/docs/configure-private-google-access**
- **Using gsutil with Private Google Access:**
  **https://cloud.google.com/storage/docs/gsutil**

**Why Other Options Are Incorrect?**

**B. Upload the installation files to Cloud Storage, configure firewall rules to block all traffic except the IP address range for Cloud Storage, and download the files using gsutil.** ❌

- **Firewall rules do not control access to Google services like Cloud Storage**—Private Google Access does.
- **Google Cloud services like Cloud Storage do not have fixed IP address ranges** that can be explicitly allowed in firewall rules.
- **PGA is the recommended approach** for accessing Cloud Storage without public internet.

✅ **Reference:**

- **https://cloud.google.com/vpc/docs/configure-private-google-access**

**C. Upload the installation files to Cloud Source Repositories, configure the VM on a subnet with Private Google Access, assign only an internal IP to the VM, and download the files using gcloud.** ❌

- **Cloud Source Repositories is designed for source code, not for large installation files.**
- **Cloud Storage is the recommended service for storing and distributing files.**
- **Downloading binary files using `gcloud source repos` is not the correct approach.**

✅ **Reference:**

- **https://cloud.google.com/source-repositories/docs/**

**D. Upload the installation files to Cloud Source Repositories, configure firewall rules to block all traffic except the IP address range for Cloud Source Repositories, and download the files using gsutil.** ❌

- **Cloud Source Repositories is not meant for binary file distribution.**
- `gsutil` **is used to download from Cloud Storage, not Cloud Source Repositories.**
- **Firewall rules cannot selectively allow Cloud Source Repositories while blocking all other internet access.**

✅ **Reference:**

- **https://cloud.google.com/source-repositories/docs/access-control**

**Conclusion:**

The best approach is **A. Upload the installation files to Cloud Storage, configure the VM on a subnet with Private Google Access, assign only an internal IP to the VM, and download the files using gsutil**, because:

- **Cloud Storage is the recommended service for securely storing installation files.**
- **Private Google Access allows secure access to Cloud Storage without public internet.**
- **The VM remains private and meets the security requirements.**

📌 **Final Reference:**
**https://cloud.google.com/vpc/docs/configure-private-google-access**

**⚠️ Note:** Use `gcloud storage cp` instead of the legacy `gsutil`. Cloud Source Repositories is closed to new customers, which is one more reason the Cloud Storage options win.

---

## Question 52

*Domain 5: Managing Implementation*

**Your company is migrating 75 TB of data to Google Cloud and plans to store it in Cloud Storage. You want to follow Google-recommended best practices for this data transfer.**

**What should you do?**

- [x] A. Transfer the data onto a **Transfer Appliance**, then use a **Transfer Appliance Rehydrator** to decrypt and upload the data to **Cloud Storage**.
- [ ] B. Transfer the data onto a **Transfer Appliance**, then use **Cloud Dataprep** to decrypt and upload the data to **Cloud Storage**.
- [ ] C. Install **gsutil** on each **server containing data** and use **resumable transfers** to upload the data into **Cloud Storage**.
- [ ] D. Install **gsutil** on each **server containing data** and use **streaming transfers** to upload the data into **Cloud Storage**.

### Explanation

**Correct Answer:**

✅ **A. Transfer the data onto a Transfer Appliance, then use a Transfer Appliance Rehydrator to decrypt and upload the data to Cloud Storage.**

**Explanation:**

Since **75 TB of data is being migrated**, using **Google Transfer Appliance** is the best approach for **large-scale, offline data transfers** following **Google-recommended best practices**.

**Why Transfer Appliance?**

✅ **Designed for large data transfers (10 TB - 1 PB+).**

- **Uploading 75 TB over the internet** using `gsutil` would be **slow and unreliable** due to bandwidth constraints.
- **Transfer Appliance enables secure, offline data transfer**—no dependency on network speed.

✅ **How It Works:**

1. **Order a Transfer Appliance** from Google Cloud.
2. **Copy the 75 TB of data to the appliance** at your on-premises location.
3. **Ship the appliance back to Google.**
4. **Google uploads the data to Cloud Storage** using **Transfer Appliance Rehydrator**.

✅ **Supporting Documentation:**

- **Google Transfer Appliance Overview:**
  **https://cloud.google.com/transfer-appliance/docs/**

**Why Other Options Are Incorrect?**

**B. Transfer the data onto a Transfer Appliance, then use Cloud Dataprep to decrypt and upload the data to Cloud Storage.** ❌

- **Cloud Dataprep is a data cleaning and transformation tool, not a transfer tool.**
- **Transfer Appliance Rehydrator** is the correct tool for decrypting and uploading data.

✅ **Reference:**

- **https://cloud.google.com/dataprep/docs**

**C. Install gsutil on each server containing data and use resumable transfers to upload the data into Cloud Storage.** ❌

- **gsutil is good for small-to-medium transfers** but **not recommended for 75 TB due to network limitations**.
- **Even with resumable uploads, transferring this much data over the internet would be slow and error-prone.**

✅ **Reference:**

- **https://cloud.google.com/storage/docs/gsutil**

**D. Install gsutil on each server containing data and use streaming transfers to upload the data into Cloud Storage.** ❌

- **Streaming transfers are not recommended for massive datasets like 75 TB**—they require continuous connectivity.
- **The transfer could fail due to network issues, and there is no checkpoint restart for streamed data.**

✅ **Reference:**

- **https://cloud.google.com/storage/docs/gsutil**

**Conclusion:**

The best approach is **A. Transfer the data onto a Transfer Appliance, then use a Transfer Appliance Rehydrator to decrypt and upload the data to Cloud Storage**, because:
✔ **Transfer Appliance is built for large-scale data migrations.**
✔ **It avoids network limitations and ensures a secure, offline transfer.**
✔ **Google Cloud officially recommends Transfer Appliance for 10 TB+ data transfers.**

📌 **Final Reference:**
**https://cloud.google.com/transfer-appliance/docs/**

**⚠️ Note:** The "Transfer Appliance Rehydrator" belonged to the first-generation appliance. Today you copy data to the appliance and ship it back, and Google uploads it to your Cloud Storage bucket, encrypted with your Cloud KMS key. The rest of the answer (Transfer Appliance for tens of TB+) still holds.

---

## Question 53

*Domain 5: Managing Implementation*

You have an **application deployed on Google Kubernetes Engine (GKE)** using a **Deployment named** `echo-deployment`. This deployment is exposed through a **Service named** `echo-service`. You need to **update the application** while ensuring **minimal downtime**.

What should you do?

- [x] A. Run `kubectl set image deployment/echo-deployment <new-image>` to update the deployment with the new container image.
- [ ] B. Use the **rolling update functionality** of the **Instance Group** that supports the **Kubernetes cluster**.B. Utilize the rolling update functionality of the Instance Group behind the Kubernetes cluster.
- [ ] C. Update the **Deployment YAML file** with the **new container image**, then run **kubectl delete deployment/echo-deployment** followed by **kubectl create -f <yaml-file>**.
- [ ] D. Update the **Service YAML file** with the **new container image**, then run **kubectl delete service/echo-service** followed by **kubectl create -f <yaml-file>**.

### Explanation

**Correct Answer:**

✅ **A. Run `kubectl set image deployment/echo-deployment <new-image>` to update the deployment with the new container image.**

**Explanation:**

To **update the application with minimal downtime**, you should use **Kubernetes rolling updates**, which **gradually replace old pods with new ones** while ensuring availability.

✅ **Why Use `kubectl set image`?**

- **Triggers a rolling update**, ensuring minimal downtime.
- **Pods are updated gradually**, avoiding service interruptions.
- **If an issue occurs, Kubernetes allows rollback to the previous version.**
- **No need to delete and recreate resources**, which could cause unnecessary downtime.

**Command to Perform Rolling Update:**

```
kubectl set image deployment/echo-deployment echo-container=<new-image>
```

- `echo-deployment` → The name of the Kubernetes Deployment.
- `echo-container=<new-image>` → Specifies the container to update with the new image.
- **Kubernetes replaces pods gradually**, ensuring seamless traffic flow.

✅ **Supporting Documentation:**

- **Kubernetes Rolling Updates:**
  **https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/**
- `kubectl set image` **Reference:**
  **https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#set-image**

**Why Other Options Are Incorrect?**

**B. Use the rolling update functionality of the Instance Group that supports the Kubernetes cluster.** ❌

- **Incorrect because Kubernetes manages rolling updates at the Deployment level**, not at the Instance Group level.
- **Instance Groups handle VM lifecycle management, not pod-level deployments.**

✅ **Reference:**

- **https://cloud.google.com/kubernetes-engine/docs/concepts/managed-instance-groups**

**C. Update the Deployment YAML file with the new container image, then run `kubectl delete deployment/echo-deployment` followed by `kubectl create -f <yaml-file>`.** ❌

- **Deleting the Deployment removes all running pods**, causing **downtime**.
- **Best practice is to update the deployment using `kubectl apply` or** `kubectl set image`, which **triggers a rolling update**.

✅ **Reference:**

- **https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#updating-a-deployment**

**D. Update the Service YAML file with the new container image, then run `kubectl delete service/echo-service` followed by `kubectl create -f <yaml-file>`.** ❌

- **Services do not manage container images**—they manage network access to Pods.
- **Updating a Service does not update the Deployment or Pods.**

✅ **Reference:**

- **https://kubernetes.io/docs/concepts/services-networking/service/**

**Conclusion:**

The best approach is **A. Run `kubectl set image deployment/echo-deployment <new-image>` to update the deployment with the new container image**, because:
✔ **It ensures a rolling update with minimal downtime.**
✔ **Kubernetes gradually replaces old pods with new ones.**
✔ **Allows easy rollback if needed.**

📌 **Final Reference:**
**https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/**

---

## Question 54

*Domain 3: Designing for Security and Compliance*

**Your company is using BigQuery as its enterprise data warehouse, with data distributed across multiple Google Cloud projects. All BigQuery queries must be billed to a single project, and no query costs should be incurred on the projects containing the data. Users should be able to query the datasets but not modify them.**

**How should you configure users' access roles?**

- [ ] A. Add all users to a **group**, then grant the group **BigQuery User** on the **billing project** and **BigQuery Data Viewer** on the projects containing the data.
- [ ] B. Add all users to a **group**, then grant the group **BigQuery Data Viewer** on the **billing project** and **BigQuery User** on the projects containing the data.
- [x] C. Add all users to a **group**, then grant the group **BigQuery Job User** on the **billing project** and **BigQuery Data Viewer** on the projects containing the data.
- [ ] D. Add all users to a **group**, then grant the group **BigQuery Data Viewer** on the **billing project** and **BigQuery Job User** on the projects containing the data.

### Explanation

**Correct Answer:**

✅ **C. Add all users to a group, then grant the group BigQuery Job User on the billing project and BigQuery Data Viewer on the projects containing the data.**

**Explanation:**

The requirement is that:

1. **All BigQuery queries must be billed to a single project** (the billing project).
2. **No query costs should be incurred on the projects containing the data**.
3. **Users must be able to query datasets but not modify them**.

**Role Breakdown for Proper Access Control:**

✅ **1. BigQuery Job User (`roles/bigquery.jobUser`) on the billing project:**

- **Required for running queries on behalf of the billing project.**
- **Ensures that all query costs are billed to this project.**
- **Users must have this role on the billing project to execute queries.**

✅ **2. BigQuery Data Viewer (`roles/bigquery.dataViewer`) on the projects containing the data:**

- **Allows users to read/query datasets in these projects.**
- **Prevents users from modifying or deleting data.**
- **Ensures that users can access the data without incurring billing in those projects.**

**Implementation Steps:**

1. **Create a Google Cloud IAM group (e.g., `bigquery-users-group`).**
2. **Assign the group the following roles:**
  - `roles/bigquery.jobUser` on the **billing project**.
  - `roles/bigquery.dataViewer` on the **projects containing the data**.
3. **Add users to the group.**
4. **Users now run queries using the billing project but access data from other projects.**

✅ **Supporting Documentation:**

- **BigQuery Job User Role (`roles/bigquery.jobUser`):**
  **https://cloud.google.com/bigquery/docs/access-control**
- **BigQuery Data Viewer Role (`roles/bigquery.dataViewer`):**
  **https://cloud.google.com/bigquery/docs/reference/roles**

**Why Other Options Are Incorrect?**

**A. Add all users to a group, then grant the group BigQuery User on the billing project and BigQuery Data Viewer on the projects containing the data.** ❌

- `BigQuery User` **(`roles/bigquery.user`) allows users to create datasets and tables** in the billing project, which is **not required**.
- **Users only need `BigQuery Job User` to run queries using the billing project.**

✅ **Reference:**

- **https://cloud.google.com/bigquery/docs/reference/roles**

**B. Add all users to a group, then grant the group BigQuery Data Viewer on the billing project and BigQuery User on the projects containing the data.** ❌

- `BigQuery Data Viewer` **on the billing project does not allow users to run queries—it only allows viewing existing datasets.**
- `BigQuery User` **on the data projects allows users to create datasets/tables, which is unnecessary.**

✅ **Reference:**

- **https://cloud.google.com/bigquery/docs/reference/roles**

**D. Add all users to a group, then grant the group BigQuery Data Viewer on the billing project and BigQuery Job User on the projects containing the data.** ❌

- **Incorrect because `BigQuery Job User` must be granted on the billing project, not on the data projects.**
- **Users would not be able to run queries using the billing project, leading to errors.**

✅ **Reference:**

- **https://cloud.google.com/bigquery/docs/reference/roles**

**Conclusion:**

The best approach is **C. Add all users to a group, then grant the group BigQuery Job User on the billing project and BigQuery Data Viewer on the projects containing the data**, because:
✔ **Ensures all queries are billed to the correct project.**
✔ **Allows users to read/query data but not modify it.**
✔ **Follows Google Cloud's recommended best practices for cross-project BigQuery access.**

📌 **Final Reference:**
**https://cloud.google.com/bigquery/docs/access-control**

---

## Question 55

*Domain 3: Designing for Security and Compliance*

**You have built an application using Cloud ML Engine that can recognize famous paintings from uploaded images. You need to test the application and allow specific users to upload images for the next 24 hours. Some users do not have a Google Account.**

**How should you enable users to upload images?**

- [ ] A. Have users upload images to **Cloud Storage** and **protect the bucket with a password** that expires after **24 hours**.
- [x] B. Have users upload images to **Cloud Storage** using a **signed URL** that expires after **24 hours**.
- [ ] C. Create an **App Engine web application** for users to upload images and configure **App Engine to disable the application after 24 hours**. Authenticate users via **Cloud Identity**.
- [ ] D. Create an **App Engine web application** where users can upload images for the next **24 hours**. Authenticate users via **Cloud Identity**.

### Explanation

**Correct Answer:**

✅ **B. Have users upload images to Cloud Storage using a signed URL that expires after 24 hours.**

**Explanation:**

Since some users **do not have a Google Account**, you need a **temporary, secure, and anonymous method** for them to upload images. The best approach is to use **Cloud Storage signed URLs**, which allow users to **upload files without requiring authentication** while enforcing **time-limited access**.

**Why Signed URLs?**

- **Allows users without a Google Account to upload files.**
- **Supports expiration time (e.g., 24 hours) for controlled access.**
- **Enforces security via cryptographic signing (HMAC-SHA256).**
- **Users do not need IAM roles or Cloud Identity accounts.**

**Implementation Steps:**

1. **Generate a signed URL** for each user using `gsutil` or `gcloud`:
  ```
  bashCopyEditgcloud storage sign-url gs://your-bucket-name --duration=24h
  ```
2. **Share the signed URL** with users.
3. **Users upload images via the signed URL** using `curl` or a simple web form.
4. **After 24 hours, the URL expires**, preventing further uploads.

✅ **Supporting Documentation:**

- **Using Signed URLs in Cloud Storage:**
  **https://cloud.google.com/storage/docs/access-control/signed-urls**

**Why Other Options Are Incorrect?**

**A. Have users upload images to Cloud Storage and protect the bucket with a password that expires after 24 hours.** ❌

- **Cloud Storage does not support password protection**—access is managed via IAM roles or signed URLs.
- **Requires users to have a Google Account, which some do not.**

✅ **Reference:**

- **https://cloud.google.com/storage/docs/access-control**

**C. Create an App Engine web application for users to upload images and configure App Engine to disable the application after 24 hours. Authenticate users via Cloud Identity.** ❌

- **Cloud Identity requires users to have a Google Account**, which **some do not**.
- **Disabling an App Engine app does not automatically revoke access to uploaded files.**

✅ **Reference:**

- **https://cloud.google.com/identity/docs/access-control**

**D. Create an App Engine web application where users can upload images for the next 24 hours. Authenticate users via Cloud Identity.** ❌

- **Requires users to have a Google Account**, which **some do not**.
- **More complex to implement than a signed URL solution.**

✅ **Reference:**

- **https://cloud.google.com/identity/docs**

**Conclusion:**

The best approach is **B. Have users upload images to Cloud Storage using a signed URL that expires after 24 hours**, because:
✔ **Allows access for users without a Google Account.**
✔ **Ensures secure, time-limited file uploads.**
✔ **Simpler and more efficient than setting up an App Engine application.**

📌 **Final Reference:**
**https://cloud.google.com/storage/docs/access-control/signed-urls**

**⚠️ Note:** Cloud ML Engine is now Vertex AI. The answer doesn't depend on it.

---

## Question 56

*Domain 3: Designing for Security and Compliance*

**Your web application must comply with the European Union’s General Data Protection Regulation (GDPR). As the technical architect, you are responsible for ensuring that the application meets GDPR requirements.**

**What should you do?**

- [ ] A. Ensure that your web application **only uses Google Cloud Platform’s native features and services**, as Google already holds various **certifications** and provides **pass-on compliance** when using native features.
- [ ] B. Enable the **relevant GDPR compliance setting** within the **Google Cloud Console** for each service used in your application.
- [ ] C. Include **Cloud Security Scanner** in your **test planning strategy** to identify potential **compliance gaps**.
- [x] D. **Design the security architecture** of your web application in a way that aligns with **GDPR requirements**.

### Explanation

**Correct Answer:**

✅ **D. Design the security architecture of your web application in a way that aligns with GDPR requirements.**

**Explanation:**

As the **technical architect**, your responsibility is to **ensure that the application meets GDPR requirements** by **designing a security architecture that aligns with GDPR principles**. GDPR compliance is **not automatic**—organizations must implement specific **security, data protection, and access control measures**.

**Why Security Architecture is Key?**

- **GDPR mandates data security, privacy by design, and access control.**
- **Your architecture must include encryption, data residency controls, and audit logging.**
- **Google Cloud provides GDPR-compliant infrastructure, but organizations must configure security controls correctly.**

✅ **Key Considerations for a GDPR-Compliant Security Architecture:**

1. **Data Encryption:**
  - Use **Cloud KMS** to encrypt sensitive data.
  - Ensure **encryption at rest and in transit** using **TLS and AES-256**.
2. **Data Residency & Processing:**
  - Store **EU customer data in Google Cloud regions within the EU**.
  - Use **Cloud Storage and BigQuery regional locations** to ensure compliance.
3. **Identity & Access Management (IAM):**
  - Implement **least privilege access** using **Google Cloud IAM roles**.
  - Use **Cloud Identity-Aware Proxy (IAP)** for secure access to applications.
4. **Logging & Auditing:**
  - Enable **Cloud Audit Logs** to track data access and processing.
  - Use **Security Command Center** for monitoring security risks.
5. **Data Subject Rights & Deletion Requests:**
  - Implement **data retention policies**.
  - Enable **Cloud DLP API** to detect and remove Personally Identifiable Information (PII).

✅ **Supporting Documentation:**

- **Google Cloud GDPR Compliance Overview:**
  **https://cloud.google.com/security/compliance/gdpr**
- **Security Best Practices for GDPR:**
  **https://cloud.google.com/blog/topics/inside-google-cloud/google-cloud-gdpr-compliance**

**Why Other Options Are Incorrect?**

**A. Ensure that your web application only uses Google Cloud Platform’s native features and services, as Google already holds various certifications and provides pass-on compliance when using native features.** ❌

- **Google Cloud provides GDPR-compliant infrastructure**, but compliance is a **shared responsibility**.
- **Simply using Google Cloud does not automatically make your application GDPR-compliant**—you must **implement proper security controls**.

✅ **Reference:**

- **https://cloud.google.com/security/compliance/gdpr**

**B. Enable the relevant GDPR compliance setting within the Google Cloud Console for each service used in your application.** ❌

- **There is no single "GDPR compliance setting" in Google Cloud Console**.
- **GDPR compliance is achieved through a combination of security measures**, not a toggle setting.

✅ **Reference:**

- **https://cloud.google.com/security/compliance/gdpr**

**C. Include Cloud Security Scanner in your test planning strategy to identify potential compliance gaps.** ❌

- **Cloud Security Scanner helps identify vulnerabilities in web applications** but **does not cover GDPR compliance requirements** such as **data encryption, data subject rights, and retention policies**.
- **It is useful for security best practices, but not a standalone solution for GDPR compliance**.

✅ **Reference:**

- **https://cloud.google.com/security-command-center/docs/concepts-security-scanner**

**Conclusion:**

The best approach is **D. Design the security architecture of your web application in a way that aligns with GDPR requirements**, because:
✔ **GDPR compliance requires a well-architected security design**.
✔ **You must implement encryption, access controls, logging, and data retention policies**.
✔ **Google Cloud provides GDPR-compliant infrastructure, but you must configure and use it correctly**.

📌 **Final Reference:**
**https://cloud.google.com/security/compliance/gdpr**

---

## Question 57

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**You need to deploy Microsoft SQL Server on Google Cloud Platform (GCP) while ensuring zero downtime in case of a data center outage within a GCP region.**

**What should you do?**

- [ ] A. Configure a **Cloud SQL instance** with **high availability (HA) enabled**.
- [ ] B. Configure a **Cloud Spanner instance** with a **regional instance configuration**.
- [ ] C. Deploy **SQL Server on Compute Engine** using **Always On Availability Groups with Windows Failover Clustering**, placing nodes in **different subnets**.
- [x] D. Deploy **SQL Server Always On Availability Groups with Windows Failover Clustering**, placing nodes in **different zones**.

### Explanation

**Correct choice: D — Deploy SQL Server Always On Availability Groups (AGs) on Compute Engine VMs, using Windows Server Failover Clustering, and place each replica in a different zone of the same region.**

- Google’s reference architecture for SQL Server AGs explicitly distributes the two database nodes and a quorum witness across *three separate zones* inside one region. Running the AG in *synchronous-commit* mode lets a surviving replica accept writes immediately if an entire zone (data-center) fails, so client traffic continues with no perceptible interruption. [Google Cloud](https://cloud.google.com/compute/docs/instances/sql-server/configure-availability-groups-shared/overview)
- The tutorial also shows how to front the replicas with an internal load-balancer or distributed network name so applications always connect to a single listener, hiding the failover. [Google Cloud](https://cloud.google.com/compute/docs/instances/sql-server/configure-availability)

Because the replicas are already alive in different zones and stay fully in-sync, a zone outage only triggers a fast, automatic role change—not a restart—meeting the “zero downtime” goal.

Why the other options don’t satisfy the requirement

**A. Cloud SQL with HA enabled**
Cloud SQL’s regional HA provides automatic failover to a standby in another zone, but Google documents that a failover causes about **60 seconds** of unavailability while connections are reset. That is *reduced* downtime, not zero. [Google Cloud](https://cloud.google.com/sql/docs/mysql/high-availability)

**B. Cloud Spanner regional instance**
Cloud Spanner is a different managed database engine. It cannot host or directly run Microsoft SQL Server workloads, so it doesn’t meet the fundamental requirement to “deploy SQL Server.” [Google Cloud](https://cloud.google.com/spanner)

**C. AG nodes in different subnets only**
Placing replicas in separate subnets does **not** guarantee they reside in distinct physical zones; both subnets could still map to the same data-center. Without explicit cross-zone placement, a single-zone failure can bring all replicas down, defeating the zero-downtime objective. [Google Cloud](https://cloud.google.com/compute/docs/regions-zones)

---

## Question 58

*Domain 5: Managing Implementation*

**The development team has provided you with a Kubernetes Deployment file, but you do not have any infrastructure set up yet. You need to deploy the application from this file.**

**What should you do?**

- [ ] A. Use `gcloud` to create a **Kubernetes cluster**, then use **Deployment Manager** to create the deployment.
- [x] B. Use `gcloud` to create a **Kubernetes cluster**, then use `kubectl` to create the deployment.
- [ ] C. Use `kubectl` to create a **Kubernetes cluster**, then use **Deployment Manager** to create the deployment.
- [ ] D. Use `kubectl` to create a **Kubernetes cluster**, then use `kubectl` to create the deployment.

### Explanation

**Correct Answer:**

✅ **B. Use `gcloud` to create a Kubernetes cluster, then use `kubectl` to create the deployment.**

**Explanation:**

Since you **do not have any infrastructure set up yet**, you first need to **create a Kubernetes cluster** before deploying the application using the provided **Kubernetes Deployment file**.

✅ **Correct Steps to Deploy the Application:**

1. **Create a Google Kubernetes Engine (GKE) cluster** using `gcloud`:
  ```
  gcloud container clusters create my-cluster --zone us-central1-a
  ```
2. **Authenticate `kubectl` with the cluster**:
  ```
  gcloud container clusters get-credentials my-cluster --zone us-central1-a
  ```
3. **Apply the Kubernetes Deployment YAML file** using `kubectl`:
  ```
  kubectl apply -f deployment.yaml
  ```
4. **Verify the deployment**:
  ```
  kubectl get deployments
  ```

✅ **Supporting Documentation:**

- **Creating a GKE Cluster:**
  **https://cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster**
- **Deploying Applications with kubectl:**
  **https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/**

**Why Other Options Are Incorrect?**

**A. Use `gcloud` to create a Kubernetes cluster, then use Deployment Manager to create the deployment.** ❌

- **Deployment Manager is not the recommended tool for deploying Kubernetes resources**—`kubectl` is the standard tool for interacting with Kubernetes.
- **Deployment Manager is primarily used for infrastructure provisioning (e.g., creating clusters, VMs), not Kubernetes workloads.**

✅ **Reference:**

- **https://cloud.google.com/deployment-manager/docs**

**C. Use `kubectl` to create a Kubernetes cluster, then use Deployment Manager to create the deployment.** ❌

- `kubectl` **cannot create Kubernetes clusters**—it is used for managing Kubernetes resources within an existing cluster.
- **You must use `gcloud` to create a GKE cluster.**

✅ **Reference:**

- **https://kubernetes.io/docs/reference/kubectl/**

**D. Use `kubectl` to create a Kubernetes cluster, then use `kubectl` to create the deployment.** ❌

- **Incorrect because `kubectl` cannot create clusters**—you must use `gcloud` to create a GKE cluster first.
- **Once the cluster is created, `kubectl` can then be used to create the deployment.**

✅ **Reference:**

- **https://cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster**

**Conclusion:**

The best approach is **B. Use `gcloud` to create a Kubernetes cluster, then use `kubectl` to create the deployment**, because:
✔ **GKE clusters must be created using `gcloud`.**
✔ `kubectl` **is the standard tool for deploying and managing Kubernetes workloads.**
✔ **This follows Google Cloud and Kubernetes best practices.**

📌 **Final Reference:**
**https://cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster**

**⚠️ Note:** Cloud Deployment Manager reached end of support on March 31, 2026. Google recommends Infrastructure Manager (managed Terraform) instead. It was never the tool for Kubernetes manifests; that is `kubectl`.

---

## Question 59

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

**You need to assess your team’s readiness for a new Google Cloud Platform (GCP) project. As part of the evaluation, you must create a skills gap plan that aligns with the business goal of cost optimization. Your team has already successfully deployed two GCP projects.**

**What should you do?**

- [ ] A. **Allocate budget** for team training and **set a deadline** for the new GCP project.
- [x] B. **Allocate budget** for team training and **develop a roadmap** for team members to obtain **Google Cloud certifications** based on their job roles.
- [ ] C. **Allocate budget** to hire **skilled external consultants** and **set a deadline** for the new GCP project.
- [ ] D. **Allocate budget** to hire **skilled external consultants** and **develop a roadmap** for team members to obtain **Google Cloud certifications** based on their job roles.

### Explanation

**Correct Answer:**

✅ **B. Allocate budget for team training and develop a roadmap for team members to obtain Google Cloud certifications based on their job roles.**

**Explanation:**

Since your **team has already successfully deployed two GCP projects**, they have **some foundational experience** but may still require **upskilling** to align with **cost optimization** and **advanced GCP best practices**.

✅ **Why Training & Certification is the Best Approach?**

1. **Cost Optimization Requires In-House Expertise:**
  - **Google Cloud certifications help team members gain expertise in cost-effective architecture and resource management.**
  - **Training ensures the team can independently manage future projects without relying on external consultants.**
2. **Long-Term Value Over External Consultants:**
  - **Hiring external consultants is expensive** and does not contribute to **team knowledge growth**.
  - **Developing in-house expertise reduces long-term operational costs.**
3. **Job Role-Based Certification Roadmap Ensures Skill Relevance:**
  - Example roadmap:
    - **Cloud Engineers** → **Associate Cloud Engineer (ACE)**
    - **Solution Architects** → **Professional Cloud Architect (PCA)**
    - **Security Teams** → **Professional Cloud Security Engineer**
    - **DevOps Teams** → **Professional Cloud DevOps Engineer**

✅ **Supporting Documentation:**

- **Google Cloud Certification Pathways:**
  **https://cloud.google.com/certification**
- **Google Cloud Cost Management Best Practices:**
  **https://cloud.google.com/billing/docs/cost-management-best-practices**

**Why Other Options Are Incorrect?**

**A. Allocate budget for team training and set a deadline for the new GCP project.** ❌

- **Training is essential, but setting a project deadline without skill assessment may result in inefficient execution.**
- **A structured roadmap for upskilling is missing, which is necessary for long-term success.**

✅ **Reference:**

- **https://cloud.google.com/certification**

**C. Allocate budget to hire skilled external consultants and set a deadline for the new GCP project.** ❌

- **External consultants provide short-term solutions but do not improve team readiness.**
- **Hiring consultants increases costs and creates long-term dependency on external expertise.**

✅ **Reference:**

- **https://cloud.google.com/training**

**D. Allocate budget to hire skilled external consultants and develop a roadmap for team members to obtain Google Cloud certifications based on their job roles.** ❌

- **Hiring external consultants is unnecessary since the team already has GCP experience.**
- **Training the in-house team provides better long-term cost optimization.**

✅ **Reference:**

- **https://cloud.google.com/training**

**Conclusion:**

The best approach is **B. Allocate budget for team training and develop a roadmap for team members to obtain Google Cloud certifications based on their job roles**, because:
✔ **It ensures cost optimization by reducing reliance on external consultants.**
✔ **It helps the team gain expertise in GCP cost management and efficiency.**
✔ **It aligns with business goals and Google Cloud best practices.**

📌 **Final Reference:**
**https://cloud.google.com/certification**

---

## Question 60

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**You are designing an application that will be used only during business hours. For the minimum viable product (MVP) release, you need a fully managed compute service that automatically scales to zero when there is no activity, ensuring no unnecessary costs.**

**Which primary compute resource should you choose?**

- [x] A. Cloud Functions
- [ ] B. Compute Engine
- [ ] C. Google Kubernetes Engine (GKE)
- [ ] D. App Engine flexible environment

### Explanation

**Correct Answer:**

✅ **A. Cloud Functions**

**Explanation:**

The requirement is for a **fully managed compute service that automatically scales to zero when there is no activity** to **minimize costs**.

✅ **Why Cloud Functions?**

- **Fully managed** → No infrastructure management required.
- **Event-driven execution** → Runs only when triggered, reducing costs.
- **Scales to zero when idle** → No charges when not in use.
- **Best for MVP applications** with sporadic workloads.

**Implementation Steps:**

1. **Deploy a Cloud Function** using the `gcloud` CLI:
  ```
  gcloud functions deploy my-function \    --runtime=nodejs20 \    --trigger-http \    --allow-unauthenticated
  ```
2. **Automatically scales to zero** when inactive.
3. **No ongoing costs unless invoked.**

✅ **Supporting Documentation:**

- **Google Cloud Functions Overview:**
  **https://cloud.google.com/functions/docs/**

**Why Other Options Are Incorrect?**

**B. Compute Engine** ❌

- **Compute Engine VMs do not automatically scale to zero**—they continue running unless manually stopped.
- **Not fully managed**—requires instance setup and management.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/**

**C. Google Kubernetes Engine (GKE)** ❌

- **GKE does not automatically scale to zero**—at least one node must always be running.
- **Requires cluster management**, which increases operational overhead.

✅ **Reference:**

- **https://cloud.google.com/kubernetes-engine/docs/concepts/autoscaling**

**D. App Engine Flexible Environment** ❌

- **App Engine flexible environment does not scale to zero**—at least one instance must always be running, incurring costs.
- **Only App Engine Standard supports scaling to zero**, but Cloud Functions is more cost-effective for event-driven workloads.

✅ **Reference:**

- **https://cloud.google.com/appengine/docs/the-appengine-environments**

**Conclusion:**

The best option is **A. Cloud Functions**, because:
✔ **Fully managed, event-driven, and requires no infrastructure management.**
✔ **Automatically scales to zero when idle, ensuring cost efficiency.**
✔ **Best suited for an MVP release with intermittent usage.**

📌 **Final Reference:**
**https://cloud.google.com/functions/docs/**

**⚠️ Note:** Cloud Functions is now **Cloud Run functions**. Cloud Run itself would also scale to zero, so expect either name on newer versions of this question.

---
