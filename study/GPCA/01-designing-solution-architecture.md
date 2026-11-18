# Domain 1 — Designing and Planning a Cloud Solution Architecture

84 questions. Answers are collapsed — try each question before expanding it.

## Questions

### Exam 1 · Q2

**Your organization is planning to migrate a multi-petabyte dataset to the cloud while ensuring that the data remains accessible 24/7. The business analysts are familiar with using a SQL interface for analysis. How should the data be stored to optimize ease of analysis?**

- A. Load the data into Google BigQuery.
- B. Insert the data into Google Cloud SQL.
- C. Store the data as flat files in Google Cloud Storage.
- D. Stream the data into Google Cloud Datastore.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Load the data into Google BigQuery.

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

</details>

---

### Exam 1 · Q3

**The operations manager requests a list of best practices to consider when migrating a J2EE application to the cloud. Which three recommendations should you provide? (Choose three.)**

- A. Adapt the application code to run on Google App Engine.
- B. Integrate Cloud Dataflow into the application to collect real-time metrics.
- C. Enable application monitoring using a tool like Stackdriver Debugger.
- D. Use an automation framework to ensure reliable provisioning of cloud infrastructure.
- E. Implement a continuous integration tool with automated testing in a staging environment.
- F. Transition from MySQL to a managed NoSQL database such as Google Cloud Datastore or Bigtable.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Adapt the application code to run on Google App Engine. **|** D. Use an automation framework to ensure reliable provisioning of cloud infrastructure. **|** E. Implement a continuous integration tool with automated testing in a staging environment.

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

</details>

---

### Exam 1 · Q4

**A development team is concerned that their existing logging tool will not be sufficient for their new cloud-based product. They need a more effective solution to capture errors and analyze historical log data. You want to assist them in finding the right tool. What should you do?**

- A. Recommend that they download and install the Google Stackdriver Logging agent.
- B. Provide them with a list of online resources covering best practices for logging.
- C. Work with them to define their requirements and evaluate suitable logging tools.
- D. Assist them in upgrading their current tool to leverage any new features.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Work with them to define their requirements and evaluate suitable logging tools.

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

</details>

---

### Exam 1 · Q7

**Your company wants to monitor whether a meeting room is occupied during a scheduled meeting. There are 1,000 meeting rooms distributed across five offices on three continents. Each room is equipped with a motion sensor that sends status updates every second. The sensor data consists of a sensor ID and multiple discrete data points. Analysts will need to combine this data with information about account owners and office locations. Which type of database should you use?**

- A. Flat file
- B. NoSQL
- C. Relational
- D. Blobstore

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. NoSQL

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

</details>

---

### Exam 1 · Q11

**Your company has successfully migrated to the cloud and now wants to analyze its data streams to optimize operations. Since there is no existing code for this analysis, all options are being considered. The company requires a combination of batch and stream processing, as some jobs run hourly while other data is processed in real time. Which technology should they use?**

- A. Google Cloud Dataproc
- B. Google Cloud Dataflow
- C. Google Kubernetes Engine with Bigtable
- D. Google Compute Engine with Google BigQuery

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Google Cloud Dataflow

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

</details>

---

### Exam 1 · Q15

**You need to choose a storage system for handling clickstream data from your company's large portfolio of websites. The data is streamed from a custom website analytics package at an average rate of 6,000 clicks per minute, with spikes reaching 8,500 clicks per second. The data must be stored for future analysis by the data science and user experience teams. Which storage infrastructure should you use?**

- A. Google Cloud SQL
- B. Google Cloud Bigtable
- C. Google Cloud Storage
- D. Google Cloud Datastore

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Google Cloud Bigtable

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

</details>

---

### Exam 1 · Q17

**Your company is expecting a significant increase in the number and size of Apache Spark and Hadoop jobs running in its on-premises data center. To handle this growing demand, you want to leverage the cloud while minimizing operational overhead and code modifications. Which Google Cloud product should you use?**

- A. Google Cloud Dataflow
- B. Google Cloud Dataproc
- C. Google Compute Engine
- D. Google Kubernetes Engine

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Google Cloud Dataproc

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

</details>

---

### Exam 1 · Q19

**You need to optimize the performance of a **real-time weather-charting application** that requires high accuracy. The data is generated by **50,000 sensors**, each sending **10 readings per second** in the format of a **timestamp and sensor reading**. Where should this data be stored?**

- A. Google BigQuery
- B. Google Cloud SQL
- C. Google Cloud Bigtable
- D. Google Cloud Storage

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Google Cloud Bigtable

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

</details>

---

### Exam 1 · Q29

**A development manager is building a new application and has asked you to review the requirements to identify the cloud technologies that can be used to meet them. The application must:**

1. **Be based on open-source technology for cloud portability.**
2. **Dynamically scale compute capacity based on demand.**
3. **Support continuous software delivery.**
4. **Run multiple isolated copies of the same application stack.**
5. **Deploy application bundles using dynamic templates.**
6. **Route network traffic to specific services based on URL.**

**Which combination of technologies will satisfy all these requirements?**

- A. Google Kubernetes Engine, Jenkins, and Helm
- B. Google Kubernetes Engine and Cloud Load Balancing
- C. Google Kubernetes Engine and Cloud Deployment Manager
- D. Google Kubernetes Engine, Jenkins, and Cloud Load Balancing

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Google Kubernetes Engine, Jenkins, and Helm

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

</details>

---

### Exam 1 · Q33

**Your company wants to explore cloud adoption with minimal risk. As a first step, they plan to archive approximately 100 TB of log data in the cloud for testing analytics capabilities while also retaining the data as a long-term disaster recovery backup.**

**Which two actions should you take? (Choose two.)**

- A. Load the logs into **Google BigQuery**.
- B. Load the logs into **Google Cloud SQL**.
- C. Import the logs into **Google Stackdriver**.
- D. Insert the logs into **Google Cloud Bigtable**.
- E. Upload the log files into **Google Cloud Storage**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Load the logs into **Google BigQuery**. **|** E. Upload the log files into **Google Cloud Storage**.

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

</details>

---

### Exam 1 · Q45

**Your company has multiple on-premises systems that serve as data sources for reporting. Over time, the data has not been well maintained and has degraded. You need to follow Google-recommended best practices to detect anomalies and clean the data.**

**What should you do?**

- A. **Upload files to Cloud Storage**, then use **Cloud Datalab** to explore and clean the data.
- B. **Upload files to Cloud Storage**, then use **Cloud Dataprep** to explore and clean the data.
- C. **Connect Cloud Datalab** to the on-premises systems and use it to explore and clean the data.
- D. **Connect Cloud Dataprep** to the on-premises systems and use it to explore and clean the data.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. **Upload files to Cloud Storage**, then use **Cloud Dataprep** to explore and clean the data.

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

</details>

---

### Exam 1 · Q49

**You are designing an architecture for an application running on Compute Engine, ensuring it meets the disaster recovery plan requirement of failing over to another region in case of a regional outage.**

**What should you do?**

- A. Deploy the application on **two Compute Engine instances** in the **same project but different regions**. Use the **first instance** to serve traffic and configure **HTTP Load Balancing** to fail over to the standby instance in case of a disaster.
- B. Deploy the application on a **single Compute Engine instance** to serve traffic and configure **HTTP Load Balancing** to fail over to an instance running **on-premises** in case of a disaster.
- C. Deploy the application on **two Compute Engine instance groups**, each in the **same project but in different regions**. Use the **first instance group** to serve traffic and configure **HTTP Load Balancing** to fail over to the standby instance group in case of a disaster.
- D. Deploy the application on **two Compute Engine instance groups**, each in a **separate project and different region**. Use the **first instance group** to serve traffic and configure **HTTP Load Balancing** to fail over to the standby instance group in case of a disaster.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Deploy the application on **two Compute Engine instance groups**, each in the **same project but in different regions**. Use the **first instance group** to serve traffic and configure **HTTP Load Balancing** to fail over to the standby instance group in case of a disaster.

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

</details>

---

### Exam 1 · Q57

**You need to deploy Microsoft SQL Server on Google Cloud Platform (GCP) while ensuring zero downtime in case of a data center outage within a GCP region.**

**What should you do?**

- A. Configure a **Cloud SQL instance** with **high availability (HA) enabled**.
- B. Configure a **Cloud Spanner instance** with a **regional instance configuration**.
- C. Deploy **SQL Server on Compute Engine** using **Always On Availability Groups with Windows Failover Clustering**, placing nodes in **different subnets**.
- D. Deploy **SQL Server Always On Availability Groups with Windows Failover Clustering**, placing nodes in **different zones**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Deploy **SQL Server Always On Availability Groups with Windows Failover Clustering**, placing nodes in **different zones**.

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

</details>

---

### Exam 1 · Q60

**You are designing an application that will be used only during business hours. For the minimum viable product (MVP) release, you need a fully managed compute service that automatically scales to zero when there is no activity, ensuring no unnecessary costs.**

**Which primary compute resource should you choose?**

- A. Cloud Functions
- B. Compute Engine
- C. Google Kubernetes Engine (GKE)
- D. App Engine flexible environment

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Cloud Functions

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

</details>

---

### Exam 2 · Q7

**You are using a single Cloud SQL instance to serve your application from a specific zone. You need to introduce high availability to ensure reliability in case of failures.**

**What should you do?**

- A. Create a **read replica** in a **different region**.
- B. Create a **failover replica** in a **different region**.
- C. Create a **read replica** in the **same region but in a different zone**.
- D. Create a **failover replica** in the **same region but in a different zone**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Create a **failover replica** in the **same region but in a different zone**.

**Correct Answer:**

✅ **D. Create a failover replica in the same region but in a different zone.**

**Explanation:**

To ensure **high availability (HA) and reliability in case of failures**, Google Cloud SQL provides **HA configurations** using **failover replicas**.

**Why Use a Failover Replica?**

- **Ensures automatic failover** in case of primary instance failure.
- **Deployed in a different zone within the same region**, providing **zonal redundancy**.
- **Google Cloud SQL automatically promotes the failover replica to primary** when needed.

**Implementation Steps:**

1. **Enable high availability (HA) during Cloud SQL instance creation:**
  ```
  gcloud sql instances create my-instance --region=us-central1 --availability-type=REGIONAL
  ```
2. **Verify that the failover replica is set up in a different zone within the same region:**
  ```
  gcloud sql instances describe my-instance
  ```

✅ **Supporting Documentation:**

- **High Availability in Cloud SQL:**
  **https://cloud.google.com/sql/docs/mysql/high-availability**

**Why Other Options Are Incorrect?**

**A. Create a read replica in a different region.** ❌

- **Read replicas are used for scaling read operations, not high availability.**
- **Read replicas do not provide automatic failover.**
- **If the primary instance fails, a read replica does not automatically become the new primary.**

✅ **Reference:**

- **https://cloud.google.com/sql/docs/mysql/replication**

**B. Create a failover replica in a different region.** ❌

- **Cloud SQL failover replicas must be in the same region** to provide automatic failover.
- **Cross-region failover is not supported for Cloud SQL HA.**
- **For disaster recovery, use cross-region read replicas, but they require manual promotion.**

✅ **Reference:**

- **https://cloud.google.com/sql/docs/mysql/high-availability**

**C. Create a read replica in the same region but in a different zone.** ❌

- **Read replicas do not support automatic failover.**
- **If the primary instance fails, the read replica will not be automatically promoted to primary.**
- **Read replicas are useful for load balancing read traffic but not for HA.**

✅ **Reference:**

- **https://cloud.google.com/sql/docs/mysql/replication**

**Conclusion:**

The best approach is **D. Create a failover replica in the same region but in a different zone**, because:
✔ **Ensures automatic failover in case of primary instance failure.**
✔ **Provides zonal redundancy within the same region.**
✔ **Recommended by Google Cloud for high availability.**

📌 **Final Reference:**
**https://cloud.google.com/sql/docs/mysql/high-availability**

**⚠️ Note:** "Failover replica" is legacy Cloud SQL wording. Today you enable high availability (availability type `REGIONAL`), which creates a standby in another zone of the same region with automatic failover.

</details>

---

### Exam 2 · Q11

**You have been assigned to develop an online analytical processing (OLAP) marketing analytics and reporting tool. The solution requires a relational database capable of handling hundreds of terabytes of data efficiently.**

**Which Google-recommended tool should you use for this application?**

- A. **Cloud Spanner**, because it is **globally distributed**.
- B. **Cloud SQL**, because it is a **fully managed relational database**.
- C. **Cloud Firestore**, because it provides **real-time synchronization across devices**.
- D. **BigQuery**, because it is designed for **large-scale processing of tabular data**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. **BigQuery**, because it is designed for **large-scale processing of tabular data**.

**Correct Answer:**

**D. BigQuery, because it is designed for large-scale processing of tabular data.**

**Explanation:**

The best choice for an OLAP (Online Analytical Processing) tool is BigQuery because:

- It is designed for large-scale analytics with petabyte-scale support.
- It is optimized for analytical queries (OLAP), supporting complex aggregations, joins, and window functions.
- It is serverless and fully managed, requiring no infrastructure maintenance.
- It uses massively parallel processing (MPP), enabling fast queries on large datasets.

**Why BigQuery is Best for OLAP?**

FeatureBigQuerySupports OLAP WorkloadsYesHandles Hundreds of TerabytesYesHighly ScalableYesOptimized for Analytical QueriesYesFully Managed & ServerlessYesSupports Standard SQLYes

**Supporting Documentation:**

- BigQuery Overview:
  https://cloud.google.com/bigquery/docs/introduction
- Best Practices for OLAP in BigQuery:
  https://cloud.google.com/bigquery/docs/querying-data

**Why Other Options Are Incorrect?**

**A. Cloud Spanner, because it is globally distributed.**

- Cloud Spanner is an OLTP (Online Transaction Processing) system, not optimized for analytical queries.
- It is best for transactional workloads requiring strong consistency and high availability.
- It is not optimized for large-scale analytical processing.

**Reference:**

- https://cloud.google.com/spanner/docs

**B. Cloud SQL, because it is a fully managed relational database.**

- Cloud SQL is designed for OLTP, not OLAP.
- It does not scale efficiently for hundreds of terabytes of data.
- Query performance degrades significantly for large analytical workloads.

**Reference:**

- https://cloud.google.com/sql/docs

**C. Cloud Firestore, because it provides real-time synchronization across devices.**

- Cloud Firestore is a NoSQL document database, not designed for relational OLAP workloads.
- It is optimized for real-time mobile and web applications, not large-scale analytical queries.

**Reference:**

- https://cloud.google.com/firestore/docs

**Conclusion:**

The best choice is **D. BigQuery**, because:

- It is designed specifically for OLAP workloads and large-scale analytical processing.
- It supports SQL-based queries and massive parallel processing (MPP).
- It scales efficiently for hundreds of terabytes of data.

**Final Reference:**
[https://cloud.google.com/bigquery/docs/introduction](https://cloud.google.com/bigquery/docs/introduction)

</details>

---

### Exam 2 · Q23

**Your client has engaged you to lead the migration of their application infrastructure to Google Cloud Platform (GCP). One of their current challenges is that their on-premises high-performance SAN requires frequent and costly upgrades to support their varied workloads, which include:**

- **20 TB of log archives (retained for legal compliance).**
- **500 GB of VM boot/data volumes and templates.**
- **500 GB of image thumbnails.**
- **200 GB of customer session state data (to allow customers to resume sessions even after being offline for several days).**

**Which storage allocation strategy would provide the most cost-effective solution?**

- A. Use **Local SSD** for **customer session state data**. Use **lifecycle-managed Cloud Storage** for **log archives, thumbnails, and VM boot/data volumes**.
- B. Use **Memcache backed by Cloud Datastore** for **customer session state data**. Use **lifecycle-managed Cloud Storage** for **log archives, thumbnails, and VM boot/data volumes**.
- C. Use **Memcache backed by Cloud SQL** for **customer session state data**. Use **local SSD-backed instances** for **VM boot/data volumes**. Use **Cloud Storage** for **log archives and thumbnails**.
- D. Use **Memcache backed by Persistent Disk SSD storage** for **customer session state data**. Use **local SSD-backed instances** for **VM boot/data volumes**. Use **Cloud Storage** for **log archives and thumbnails**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use **Memcache backed by Cloud Datastore** for **customer session state data**. Use **lifecycle-managed Cloud Storage** for **log archives, thumbnails, and VM boot/data volumes**.

**Correct Answer:**

**B. Use Memcache backed by Cloud Datastore for customer session state data. Use lifecycle-managed Cloud Storage for log archives, thumbnails, and VM boot/data volumes.**

**Explanation:**

The **best approach optimizes cost, scalability, and performance** while addressing **different workload requirements**:

1. **Customer Session State Data (200 GB)**
  - **Best Choice: Memcache + Cloud Datastore**
  - **Why?**
    - **Session data needs to persist for days**, so an **in-memory cache alone is not enough**.
    - **Memcache speeds up access**, while **Cloud Datastore ensures durability**.
    - **Cloud Datastore is cost-effective and scales seamlessly**.
    - **Persistent storage is required in case Memcache resets**.
2. **Log Archives (20 TB)**
  - **Best Choice: Lifecycle-managed Cloud Storage**
  - **Why?**
    - **Cold storage tiers (Nearline, Coldline, Archive) reduce costs**.
    - **Compliance logs are rarely accessed** → Move older logs to cheaper tiers.
    - **Lifecycle policies automatically transition storage classes**.
3. **VM Boot/Data Volumes (500 GB) & Templates**
  - **Best Choice: Cloud Storage with Lifecycle Management**
  - **Why?**
    - **VM images & snapshots can be stored in Cloud Storage**.
    - **Coldline or Archive tiers reduce costs** for rarely accessed backups.
    - **Compute Engine can boot directly from Cloud Storage-based VM images**.
4. **Image Thumbnails (500 GB)**
  - **Best Choice: Lifecycle-managed Cloud Storage**
  - **Why?**
    - **Cloud Storage is highly available, scalable, and low-cost**.
    - **Use multi-regional storage for fast delivery** if images need frequent access.
    - **Use lifecycle policies to move infrequently accessed thumbnails to Nearline/Coldline.**

**Implementation Details:**

**1. Configure Cloud Datastore for Session Data**

- Use **Memorystore (Memcache) for low-latency caching**:
  ```
  gcloud redis instances create session-cache \    --size=5 \    --region=us-central1 \    --tier=STANDARD
  ```
- Store **persistent session data in Cloud Datastore**:
  ```
  from google.cloud import datastore client = datastore.Client()session = datastore.Entity(client.key("UserSession", "session123"))session["user_id"] = "user_456"session["last_active"] = "2025-03-16"client.put(session)
  ```

**2. Configure Lifecycle Policies for Log Archives and Images**

- Example **lifecycle policy for log retention** (move to Archive after 1 year):
  ```
  {  "rule": [    {      "action": {"type": "SetStorageClass", "storageClass": "ARCHIVE"},      "condition": {"age": 365}    }  ]}
  ```
  ```
  gsutil lifecycle set lifecycle-policy.json gs://log-archives
  ```

**3. Store VM Boot/Data Volumes in Cloud Storage**

- **Upload VM snapshots** to Cloud Storage:
  ```
  gcloud compute images export --destination-uri gs://vm-backups/my-vm-image.tar.gz --image my-vm
  ```

**Why Other Options Are Incorrect?**

**A. Use Local SSD for customer session state data.**

- **Local SSD is ephemeral** → Data is **lost if the VM restarts**.
- **Session data must persist across reboots**, so **Cloud Datastore is a better choice**.

✅ **Reference:**
https://cloud.google.com/compute/docs/disks/local-ssd

**C. Use Memcache backed by Cloud SQL for session state data.**

- **Cloud SQL is not optimized for NoSQL session storage.**
- **Cloud Datastore is a better choice** because:
  - **Supports flexible schemas** (ideal for session data).
  - **Scales automatically** without manual sharding.
  - **Cheaper for infrequent access**.

✅ **Reference:**
https://cloud.google.com/datastore/docs/concepts/overview

**D. Use Persistent Disk SSD for session state data.**

- **Persistent Disk is not ideal for session storage**:
  - More **expensive than Cloud Datastore**.
  - Does **not scale as well as Datastore**.

✅ **Reference:**
https://cloud.google.com/datastore

**Conclusion:**

The best approach is **B. Use Memcache backed by Cloud Datastore for customer session state data. Use lifecycle-managed Cloud Storage for log archives, thumbnails, and VM boot/data volumes.**

✔ **Ensures cost-effective storage** for different workloads.
✔ **Balances performance, scalability, and durability**.
✔ **Uses Google-recommended best practices**.

**Final Reference:**
[https://cloud.google.com/solutions/best-practices-for-compute](https://cloud.google.com/solutions/best-practices-for-compute)

**⚠️ Note:** VMs boot from Persistent Disk, not Cloud Storage; Cloud Storage can hold the VM images and templates. App Engine memcache is a legacy bundled service (Memorystore is the general cache today). B is still the least-wrong option.

</details>

---

### Exam 2 · Q29

**Your customer operates a web service that provides product recommendations to e-commerce websites. They have started experimenting with a machine learning model on Google Cloud Platform (GCP) to enhance recommendation quality.**

**What should they do to improve the model's results over time?**

- A. **Export Cloud Machine Learning Engine performance metrics** from **Stackdriver to BigQuery** for **efficiency analysis**.
- B. **Plan a migration** of the **model training** from **Cloud GPUs to Cloud TPUs**, as TPUs **offer better results**.
- C. **Monitor Compute Engine announcements** for **newer CPU architectures** and deploy the model on them as soon as they become available to enhance performance.
- D. **Store historical recommendations and their outcomes in BigQuery**, using this data as **training input** to refine the model over time.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. **Store historical recommendations and their outcomes in BigQuery**, using this data as **training input** to refine the model over time.

**Correct Answer:**

**D. Store historical recommendations and their outcomes in BigQuery, using this data as training input to refine the model over time.**

**Explanation:**

To **improve a machine learning (ML) model's results over time**, **continuous retraining with fresh, high-quality data** is essential.

- **Historical recommendations and user interactions (clicks, purchases, conversions, etc.) provide valuable feedback.**
- **BigQuery serves as a scalable and cost-effective data warehouse** for storing large datasets and running analytical queries.
- **Retraining the model using actual outcomes refines its accuracy**, making recommendations more relevant over time.

**How This Works?**

1. **Store recommendation results and user interactions** in **BigQuery**.
2. **Analyze the data** to identify patterns (e.g., which recommendations led to purchases).
3. **Use this data as labeled training input** to improve the machine learning model.
4. **Automate retraining** using tools like **Vertex AI Pipelines** or **Cloud Composer**.

**Implementation Steps:**

**1. Store Recommendation Data in BigQuery**

Create a table in **BigQuery** to store **historical recommendation data**:

```
CREATE TABLE ecommerce_recommendations.history (  user_id STRING,  product_id STRING,  recommended_at TIMESTAMP,  clicked BOOLEAN,  purchased BOOLEAN);
```

- `recommended_at`: When the recommendation was made.
- `clicked`: Whether the user clicked the recommendation.
- `purchased`: Whether the user bought the product.

**2. Analyze Model Performance**

Query past recommendations and their outcomes: product_id, COUNT(*) AS total_recommendations, SUM(CASE WHEN clicked THEN 1 ELSE 0 END) AS total_clicks, SUM(CASE WHEN purchased THEN 1 ELSE 0 END) AS total_purchases FROM ecommerce_recommendations.history GROUP BY product_id ORDER BY total_purchases DESC;

- Helps **identify high-performing recommendations** for refining the model.

**3. Retrain the Model with Updated Data**

- Use **BigQuery ML** or export refined data to **Vertex AI** for training.
- Automate training jobs using **Vertex AI Pipelines**.
- Deploy updated models via **CI/CD pipelines**.

**Supporting Documentation:**

- **BigQuery for ML Pipelines**:
  https://cloud.google.com/vertex-ai/docs/pipelines/introduction
- **BigQuery for Machine Learning (BigQuery ML)**:
  https://cloud.google.com/bigquery-ml/docs

**Why Other Options Are Incorrect?**

**A. Export Cloud Machine Learning Engine performance metrics from Stackdriver to BigQuery for efficiency analysis.**

- **Performance metrics (latency, CPU usage, etc.) do not directly improve ML model accuracy.**
- **Model accuracy improves with better training data, not infrastructure monitoring.**

✅ **Reference:**
https://cloud.google.com/monitoring

**B. Plan a migration of the model training from Cloud GPUs to Cloud TPUs, as TPUs offer better results.**

- **TPUs improve training speed, not recommendation accuracy.**
- **A poorly trained model on a TPU is still inaccurate.**
- **Data quality, not hardware, is the key factor in improving results.**

✅ **Reference:**
https://cloud.google.com/tpu/docs

**C. Monitor Compute Engine announcements for newer CPU architectures and deploy the model on them as soon as they become available to enhance performance.**

- **Newer CPUs improve inference speed but do not improve model accuracy.**
- **ML models improve by training on better, more relevant data, not by switching CPU architectures.**

✅ **Reference:**
https://cloud.google.com/compute/docs/machine-types

**Conclusion:**

The best approach is **D. Store historical recommendations and their outcomes in BigQuery, using this data as training input to refine the model over time**, because:

- **It enables continuous learning**, ensuring **recommendations improve over time**.
- **BigQuery efficiently handles large-scale data analysis** for ML model training.
- **It follows Google Cloud’s best practices for machine learning lifecycle management.**

**Final Reference:**
[https://cloud.google.com/bigquery-ml/docs](https://cloud.google.com/bigquery-ml/docs)

</details>

---

### Exam 2 · Q33

**Your company develops rendering software that customers can download from the company website. Since you have customers worldwide, you need to minimize latency for all users while following Google-recommended best practices.**

**How should you store the files?**

- A. Save the files in a **Multi-Regional Cloud Storage bucket**.
- B. Save the files in a **Regional Cloud Storage bucket**, with **one bucket per zone** within the region.
- C. Save the files in **multiple Regional Cloud Storage buckets**, with **one bucket per zone per region**.
- D. Save the files in **multiple Multi-Regional Cloud Storage buckets**, with **one bucket per multi-region**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Save the files in a **Multi-Regional Cloud Storage bucket**.

**Correct Answer:**

**A. Save the files in a Multi-Regional Cloud Storage bucket.**

**Explanation:**

To **minimize latency for customers worldwide** while following **Google-recommended best practices**, the best approach is to **store the files in a Multi-Regional Cloud Storage bucket**.

**Why Use Multi-Regional Cloud Storage?**

- **Geo-redundancy:** Data is automatically replicated **across multiple locations within a multi-region** for **high availability and low latency**.
- **Optimized for frequently accessed content:** Ideal for **public-facing files** like software downloads, as Google Cloud **serves data from the nearest available location**.
- **No need to manage multiple buckets manually**—Google Cloud automatically routes requests to the nearest copy.

**Implementation Steps:**

**1. Create a Multi-Regional Cloud Storage Bucket**

Use the **multi-region closest to your users** (e.g., `us`, `eu`, or `asia`).

```
gcloud storage buckets create my-software-bucket \    --location=US \    --storage-class=MULTI_REGIONAL
```

**2. Upload Software Files**

```
gsutil cp my-rendering-software.zip gs://my-software-bucket/
```

**3. Enable Public Access (Optional, for public downloads)**

```
gsutil iam ch allUsers:objectViewer gs://my-software-bucket
```

**Supporting Documentation:**

- **Google Cloud Multi-Regional Storage**:
  https://cloud.google.com/storage/docs/storage-classes#multi-regional
- **Choosing a Storage Class**:
  https://cloud.google.com/storage/docs/storage-classes

**Why Other Options Are Incorrect?**

**B. Save the files in a Regional Cloud Storage bucket, with one bucket per zone within the region.**

- **Regional buckets are confined to a single region**, which **does not optimize performance for global customers**.
- **Zonal buckets do not exist in Cloud Storage**—Google Cloud Storage works at the **regional and multi-regional level**.

✅ **Reference:**
https://cloud.google.com/storage/docs/storage-classes

**C. Save the files in multiple Regional Cloud Storage buckets, with one bucket per zone per region.**

- **Requires manual setup and maintenance**, increasing operational complexity.
- **Google Cloud Storage Multi-Regional already handles distribution automatically**, making this unnecessary.

✅ **Reference:**
https://cloud.google.com/storage/docs/locations

**D. Save the files in multiple Multi-Regional Cloud Storage buckets, with one bucket per multi-region.**

- **Unnecessary duplication**—a **single Multi-Regional bucket is sufficient** for global distribution.
- **Google automatically directs traffic to the nearest available storage location** within a multi-region.

✅ **Reference:**
https://cloud.google.com/storage/docs/request-endpoints

**Conclusion:**

The best approach is **A. Save the files in a Multi-Regional Cloud Storage bucket**, because:

- **It provides automatic geo-redundancy and low-latency access worldwide.**
- **It minimizes management overhead**—Google Cloud handles traffic routing.
- **It aligns with Google’s best practices for globally distributed content.**

**Final Reference:**
[https://cloud.google.com/storage/docs/storage-classes#multi-regional](https://cloud.google.com/storage/docs/storage-classes#multi-regional)

</details>

---

### Exam 2 · Q35

**You are deploying a PHP App Engine Standard service with Cloud SQL as the backend database. You need to minimize the number of queries sent to Cloud SQL to optimize performance.**

**What should you do?**

- A. **Set the memcache service level to dedicated**. Create a **key from the hash of the query** and **return database values from memcache** before issuing a query to **Cloud SQL**.
- B. **Set the memcache service level to dedicated**. Configure a **cron job** that runs **every minute** to **pre-populate the cache** with keys containing **query results**.
- C. **Set the memcache service level to shared**. Configure a **cron job** that runs **every minute** to **save all expected queries** to a key called **"cached_queries"**.
- D. **Set the memcache service level to shared**. Create a **key called "cached_queries"** and **return database values from that key** before issuing a query to **Cloud SQL**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. **Set the memcache service level to dedicated**. Create a **key from the hash of the query** and **return database values from memcache** before issuing a query to **Cloud SQL**.

**Correct Answer:**

**A. Set the memcache service level to dedicated. Create a key from the hash of the query and return database values from memcache before issuing a query to Cloud SQL.**

**Explanation:**

To **optimize performance and minimize the number of queries sent to Cloud SQL**, the best approach is to:

1. **Use Memcache (Google Cloud Memorystore) to cache query results.**
2. **Generate a unique key based on the query (e.g., using a hash).**
3. **Check the cache first** before making a request to Cloud SQL.
4. **If the result is not in the cache, fetch from Cloud SQL and store the result in Memcache.**

This **reduces database load**, improves response time, and follows **Google-recommended best practices for Cloud SQL optimization**.

**Implementation Steps:**

**1. Enable Memcache with a Dedicated Tier**

- **Dedicated Memcache provides higher performance** and **better eviction policies** compared to shared Memcache.

```
runtime: phpenv: standardentrypoint: serveautomatic_scaling:  min_instances: 1  max_instances: 10beta_settings:  cloud_sql_instances: my-project:us-central1:my-cloudsql-instance  memcache_service: dedicated
```

**2. Implement Query Caching in PHP**

```
$memcache = new Memcached();$memcache->addServer('localhost', 11211); $query = "SELECT * FROM users WHERE id = 123";$cacheKey = md5($query);  // Create a hash of the query // Check if result is in cache$cachedResult = $memcache->get($cacheKey);if ($cachedResult) {    echo "Cache Hit: Returning data from Memcache";    return $cachedResult;} // If not in cache, fetch from Cloud SQL$db = new PDO('mysql:unix_socket=/cloudsql/my-project:us-central1:my-cloudsql-instance;dbname=mydb', 'root', '');$stmt = $db->prepare($query);$stmt->execute();$result = $stmt->fetchAll(PDO::FETCH_ASSOC); // Store result in cache for future requests$memcache->set($cacheKey, $result, 600); // Cache for 10 minutesecho "Cache Miss: Fetched from Cloud SQL";return $result;
```

- **Generates a unique cache key for each query** using `md5($query)`.
- **Checks the cache first** before querying Cloud SQL.
- **Caches results for 10 minutes** to avoid unnecessary database queries.

**Supporting Documentation:**

- **Using Memcache with App Engine**:
  https://cloud.google.com/appengine/docs/standard/php/memcache
- **Best Practices for Cloud SQL Performance**:
  https://cloud.google.com/sql/docs/mysql/performance

**Why Other Options Are Incorrect?**

**B. Set the memcache service level to dedicated. Configure a cron job that runs every minute to pre-populate the cache with keys containing query results.**

- **Inefficient approach** because **not all queries are predictable** or needed every minute.
- **Caches unnecessary data**, leading to **wasted memory**.

✅ **Reference:**
https://cloud.google.com/appengine/docs/standard/php/memcache

**C. Set the memcache service level to shared. Configure a cron job that runs every minute to save all expected queries to a key called "cached_queries".**

- **Shared Memcache is less reliable and has more evictions** than dedicated Memcache.
- **Storing all queries in a single key ("cached_queries") is inefficient**, making retrieval slow.
- **Cron jobs every minute add unnecessary overhead** without guaranteeing relevant data is cached.

✅ **Reference:**
https://cloud.google.com/memorystore/docs/memcached

**D. Set the memcache service level to shared. Create a key called "cached_queries" and return database values from that key before issuing a query to Cloud SQL.**

- **A single cache key for all queries ("cached_queries") is not scalable**.
- **Each query should have its own cache key (hashed query).**
- **Shared Memcache is not ideal for production workloads with high query volume.**

✅ **Reference:**
https://cloud.google.com/sql/docs/mysql/performance

**Conclusion:**

The best approach is **A. Set the memcache service level to dedicated. Create a key from the hash of the query and return database values from memcache before issuing a query to Cloud SQL**, because:

- **It follows best practices for caching database queries.**
- **It reduces Cloud SQL queries and improves response times.**
- **It ensures query results are stored efficiently using a hashed key.**

**Final Reference:**
[https://cloud.google.com/appengine/docs/standard/php/memcache](https://cloud.google.com/appengine/docs/standard/php/memcache)

**⚠️ Note:** App Engine memcache is a legacy bundled service. Outside legacy App Engine runtimes, use the same read-through pattern with Memorystore.

</details>

---

### Exam 2 · Q36

You need to **ensure reliability** for your **application and operations** by implementing **reliable task scheduling** for **compute workloads** on **Google Cloud Platform (GCP)**. You want to follow **Google-recommended best practices**.

What should you do?

- A. Use the **Cron service in App Engine** to **publish messages directly** to a **message-processing utility service** running on **Compute Engine instances**.
- B. Use the **Cron service in App Engine** to **publish messages to a Cloud Pub/Sub topic**. Subscribe to that topic using a **message-processing utility service** running on **Compute Engine instances**.
- C. Use the **Cron service in Google Kubernetes Engine (GKE)** to **publish messages directly** to a **message-processing utility service** running on **Compute Engine instances**.
- D. Use the **Cron service in Google Kubernetes Engine (GKE)** to **publish messages to a Cloud Pub/Sub topic**. Subscribe to that topic using a **message-processing utility service** running on **Compute Engine instances**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use the **Cron service in App Engine** to **publish messages to a Cloud Pub/Sub topic**. Subscribe to that topic using a **message-processing utility service** running on **Compute Engine instances**.

**Correct Answer:**

**B. Use the Cron service in App Engine to publish messages to a Cloud Pub/Sub topic. Subscribe to that topic using a message-processing utility service running on Compute Engine instances.**

**Explanation:**

To ensure **reliable task scheduling for compute workloads** on **Google Cloud Platform (GCP)**, the best practice is to:

1. **Use App Engine's Cron Service** for scheduled task execution.
2. **Publish tasks to a Cloud Pub/Sub topic**, which provides a **reliable, distributed message queue**.
3. **Subscribe to Pub/Sub messages** from a message-processing utility running on **Compute Engine instances**.

This approach ensures:

- **Scalability:** Pub/Sub allows multiple subscribers, distributing the workload efficiently.
- **Reliability:** Pub/Sub guarantees **at least-once delivery**, ensuring no tasks are lost.
- **Decoupling:** App Engine's Cron service triggers tasks **without depending on Compute Engine directly**.

**Implementation Steps**

**1. Define a Cron Job in App Engine**

Create a `cron.yaml` file:

```
cron:- description: "Run scheduled compute workload"  url: /task  schedule: every 5 minutes
```

- This triggers an HTTP request every **5 minutes**.

**2. Publish Messages to Cloud Pub/Sub in App Engine**

Modify the App Engine **handler (`main.py`)** to publish to **Pub/Sub**:

```
from google.cloud import pubsub_v1from flask import Flask app = Flask(__name__) @app.route('/task')def schedule_task():    publisher = pubsub_v1.PublisherClient()    topic_path = publisher.topic_path("my-project", "my-topic")     message = "Run compute job"    publisher.publish(topic_path, message.encode("utf-8"))        return "Task scheduled", 200
```

- This **publishes a message** to a Cloud Pub/Sub topic.

**3. Create a Cloud Pub/Sub Subscriber on Compute Engine**

On Compute Engine, **subscribe and process messages**:

```
from google.cloud import pubsub_v1 def callback(message):    print(f"Received message: {message.data}")    message.ack()  # Acknowledge the message after processing subscriber = pubsub_v1.SubscriberClient()subscription_path = subscriber.subscription_path("my-project", "my-subscription") streaming_pull = subscriber.subscribe(subscription_path, callback=callback)print("Listening for messages...")streaming_pull.result()
```

- **Processes the scheduled task reliably** on Compute Engine.

**Supporting Documentation:**

- **Using App Engine Cron Jobs**:
  https://cloud.google.com/appengine/docs/standard/python3/scheduling-jobs-with-cron-yaml
- **Cloud Pub/Sub for Asynchronous Messaging**:
  https://cloud.google.com/pubsub/docs/overview

**Why Other Options Are Incorrect?**

**A. Use the Cron service in App Engine to publish messages directly to a message-processing utility service running on Compute Engine instances.**

- **Direct HTTP requests from App Engine to Compute Engine introduce tight coupling.**
- **Compute Engine instances may be unavailable at the scheduled time**, leading to **failed tasks**.
- **Cloud Pub/Sub provides a more reliable, decoupled mechanism.**

✅ **Reference:**
https://cloud.google.com/appengine/docs/standard/python/taskqueue/

**C. Use the Cron service in Google Kubernetes Engine (GKE) to publish messages directly to a message-processing utility service running on Compute Engine instances.**

- **Using GKE's CronJobs requires running Kubernetes, which adds operational overhead.**
- **Directly invoking Compute Engine instances is unreliable.**
- **Cloud Pub/Sub provides a better event-driven architecture.**

✅ **Reference:**
https://cloud.google.com/kubernetes-engine/docs/how-to/cron-jobs

**D. Use the Cron service in Google Kubernetes Engine (GKE) to publish messages to a Cloud Pub/Sub topic. Subscribe to that topic using a message-processing utility service running on Compute Engine instances.**

- **Using GKE just for scheduling tasks is unnecessary overhead** when **App Engine's Cron service is simpler and fully managed**.
- **App Engine Cron is more cost-effective and efficient for scheduling periodic tasks.**

✅ **Reference:**
https://cloud.google.com/kubernetes-engine/docs/concepts/jobs

**Conclusion:**

The best approach is **B. Use the Cron service in App Engine to publish messages to a Cloud Pub/Sub topic. Subscribe to that topic using a message-processing utility service running on Compute Engine instances**, because:

- **It ensures reliable, event-driven scheduling.**
- **It decouples scheduling from Compute Engine instances, improving flexibility.**
- **It follows Google Cloud best practices for scalable task scheduling.**

**Final Reference:**
[https://cloud.google.com/pubsub/docs/overview](https://cloud.google.com/pubsub/docs/overview)

**⚠️ Note:** Google's managed cron today is **Cloud Scheduler**, which can publish straight to a Pub/Sub topic. The pattern (scheduler → Pub/Sub → workers) is the same.

</details>

---

### Exam 2 · Q37

**Your company is building a new architecture to support its data-centric business operations. You are responsible for network setup.**

- **Mobile and web-facing applications will be hosted on-premises.**
- **All data analysis will be conducted in Google Cloud Platform (GCP).**
- **You need to process and upload 7 years of archived .csv files totaling 900 TB to Cloud Storage.**
- **Additionally, you will be ingesting 10 TB of new data daily.**
- **Your current internet connection is 100 Mbps.**

**What actions will best meet your company’s needs?**

- A. **Compress and upload** both **archived** and **daily files** using the **gsutil -m** option.
- B. **Lease a Transfer Appliance**, upload **archived files** to it, and send it to **Google** for **Cloud Storage transfer**. Establish a connection using **Dedicated Interconnect** or **Direct Peering** to upload **daily files**.
- C. **Lease a Transfer Appliance**, upload **archived files** to it, and send it to **Google** for **Cloud Storage transfer**. Establish a **Cloud VPN Tunnel** over the **public internet** and **compress and upload daily files** using **gsutil -m**.
- D. **Lease a Transfer Appliance**, upload **archived files** to it, and send it to **Google** for **Cloud Storage transfer**. Establish a **Cloud VPN Tunnel** over the **public internet** and **upload daily files**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. **Lease a Transfer Appliance**, upload **archived files** to it, and send it to **Google** for **Cloud Storage transfer**. Establish a connection using **Dedicated Interconnect** or **Direct Peering** to upload **daily files**.

**Correct Answer:**

**B. Lease a Transfer Appliance, upload archived files to it, and send it to Google for Cloud Storage transfer. Establish a connection using Dedicated Interconnect or Direct Peering to upload daily files.**

**Explanation:**

To efficiently handle **900 TB of archived data transfer** and **10 TB of new daily data ingestion**, Google Cloud recommends:

1. **Using Transfer Appliance for large-scale archival data transfer**
  - **900 TB of data is too large for an internet transfer**, which would take **over 2.5 years** with a **100 Mbps connection**.
  - **Google Transfer Appliance** allows you to **physically ship data** to Google, significantly reducing transfer time.
2. **Using Dedicated Interconnect or Direct Peering for daily data ingestion**
  - **10 TB daily data transfer over 100 Mbps internet is infeasible** (would take **over 9 days per batch**).
  - **Dedicated Interconnect (10 Gbps or more) or Direct Peering** ensures **high-speed, secure, and reliable data transfer**.

**Implementation Steps:**

**1. Transfer 900 TB Archived Data Using Google Transfer Appliance**

- **Order a Transfer Appliance** (up to **1 PB storage capacity**) from Google.
  ```
  gcloud transfer-appliance orders create --region=us-central1
  ```
- **Copy data to the appliance** locally using rsync:
  ```
  rsync -av /local/data /mnt/transfer-appliance/
  ```
- **Ship the appliance to Google for upload to Cloud Storage.**

✅ **Reference:** https://cloud.google.com/transfer-appliance

**2. Establish a High-Speed Connection for Daily 10 TB Transfers**

- **Dedicated Interconnect (10–100 Gbps)**
  ```
  gcloud compute interconnects create my-interconnect \    --customer-name=my-company \    --description="Dedicated Interconnect for 10TB Daily Transfer" \    --requested-link-count=2 \    --interconnect-type=DEDICATED
  ```
  - **Best for consistent, high-volume data transfer**.
  - **Secure, private connection** directly to Google Cloud.

OR

- **Direct Peering (1–10 Gbps)**
  - Connect **your on-premises network directly to Google's network**.
  - Lower latency compared to VPN.

✅ **Reference:** https://cloud.google.com/interconnect/docs/concepts/overview

**Why Other Options Are Incorrect?**

**A. Compress and upload both archived and daily files using the gsutil -m option.**

- **900 TB over a 100 Mbps connection would take ~2.5 years to upload**.
- **10 TB daily over 100 Mbps would take ~9+ days per batch**, making real-time ingestion impossible.
- **Not a practical solution for large-scale data transfers**.

✅ **Reference:**
https://cloud.google.com/storage/docs/gsutil/commands/cp

**C. Lease a Transfer Appliance for archives, then use Cloud VPN + gsutil -m for daily uploads.**

- **Cloud VPN is limited to 3 Gbps per tunnel (max 50 Gbps with multiple tunnels)**, which is **not sufficient for 10 TB daily ingestion**.
- **gsutil -m is inefficient for large daily data ingestion compared to Dedicated Interconnect or Peering**.

✅ **Reference:**
https://cloud.google.com/vpn/docs/concepts/overview

**D. Lease a Transfer Appliance for archives, then use Cloud VPN for daily uploads.**

- **Cloud VPN bandwidth limitations (3 Gbps per tunnel) make it unsuitable for sustained 10 TB daily transfers**.
- **Dedicated Interconnect or Direct Peering is the recommended solution for high-volume, reliable transfers**.

✅ **Reference:**
https://cloud.google.com/vpn/docs/concepts/overview

**Conclusion:**

The best solution is **B. Lease a Transfer Appliance, upload archived files to it, and send it to Google for Cloud Storage transfer. Establish a connection using Dedicated Interconnect or Direct Peering to upload daily files.**

This approach ensures:

- **Efficient bulk data transfer for 900 TB archived files**.
- **Fast and reliable daily ingestion of 10 TB via high-speed network connectivity**.
- **Compliance with Google Cloud best practices for data migration**.

✅ **Final Reference:**
[https://cloud.google.com/architecture/migrating-data-to-google-cloud](https://cloud.google.com/architecture/migrating-data-to-google-cloud)

</details>

---

### Exam 2 · Q38

**You are developing a globally scaled frontend for a legacy streaming backend data API. The API requires events to arrive in strict chronological order with no duplicate data for proper processing.**

**Which Google Cloud products should you deploy to ensure guaranteed-once FIFO (first-in, first-out) delivery of data?**

- A. **Cloud Pub/Sub** alone.
- B. **Cloud Pub/Sub** connected to **Cloud Dataflow**.
- C. **Cloud Pub/Sub** connected to **Stackdriver**.
- D. **Cloud Pub/Sub** connected to **Cloud SQL**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. **Cloud Pub/Sub** connected to **Cloud Dataflow**.

**Correct Answer:**

**B. Cloud Pub/Sub connected to Cloud Dataflow.**

**Explanation:**

To ensure **guaranteed-once FIFO (first-in, first-out) delivery** of streaming events to a **legacy backend API**, you need a **reliable event processing pipeline** that guarantees:

1. **Strict chronological order** of events.
2. **No duplicate messages** (exactly-once delivery).
3. **Scalability for global operations**.

**How Cloud Pub/Sub + Cloud Dataflow Ensures FIFO & Exactly-Once Processing**

**1. Use Cloud Pub/Sub for Event Messaging**

- **Scalable, durable, and globally distributed message broker**.
- **However, it does not natively guarantee strict ordering or exactly-once delivery**.
- **Messages can be duplicated or delivered out of order.**

**2. Use Cloud Dataflow (Apache Beam) for Ordering & Deduplication**

- **Reorders messages based on timestamps before forwarding them**.
- **Ensures exactly-once processing with built-in deduplication**.
- **Applies event-time windowing to maintain strict order**.
- **Automatically scales for large data streams**.

**3. Send Processed Events to the Backend API**

- **The API receives correctly ordered, non-duplicate events**.

**Implementation Example (Apache Beam in Cloud Dataflow)**

This **Python Dataflow pipeline** enforces **FIFO ordering and deduplication** before sending data to the backend API:

```
import apache_beam as beamfrom apache_beam.options.pipeline_options import PipelineOptionsimport json # Define processing functiondef process_event(event):    # Extract timestamp and data    return (event['timestamp'], event['data']) pipeline_options = PipelineOptions(streaming=True) with beam.Pipeline(options=pipeline_options) as p:    (p     | "Read from Pub/Sub" >> beam.io.ReadFromPubSub(topic="projects/my-project/topics/my-topic")     | "Parse JSON" >> beam.Map(lambda x: json.loads(x.decode('utf-8')))     | "Deduplicate" >> beam.Distinct()  # Removes duplicate events     | "Sort Chronologically" >> beam.transforms.combiners.Top.Largest(1000)  # Ensures FIFO order     | "Send to Backend" >> beam.io.WriteToText("gs://my-bucket/sorted-events.txt")  # Replace with API call    )
```

- **Uses `Distinct()` to remove duplicates**.
- **Sorts messages using timestamps to maintain FIFO order**.
- **Ensures reliable event delivery to the backend API**.

✅ **Reference:**
https://cloud.google.com/dataflow/docs/guides

**Why Other Options Are Incorrect?**

**A. Cloud Pub/Sub alone**

- **Cloud Pub/Sub does NOT guarantee FIFO order**.
- **Messages may arrive out of order or be duplicated due to retries**.
- **Cloud Dataflow is needed to enforce ordering and deduplication**.

✅ **Reference:**
https://cloud.google.com/pubsub/docs/ordering

**C. Cloud Pub/Sub connected to Stackdriver**

- **Stackdriver (Cloud Logging) is for monitoring and logging, not for data processing**.
- **It cannot enforce FIFO ordering or deduplicate messages**.

✅ **Reference:**
https://cloud.google.com/logging/docs

**D. Cloud Pub/Sub connected to Cloud SQL**

- **Cloud SQL does not process streaming data efficiently**.
- **It cannot enforce FIFO guarantees at scale**.
- **Cloud Dataflow is required to preprocess and order events before storage.**

✅ **Reference:**
https://cloud.google.com/sql/docs

**Conclusion:**

The best choice is **B. Cloud Pub/Sub connected to Cloud Dataflow**, because:

- **Cloud Dataflow ensures strict ordering and exactly-once delivery**.
- **Cloud Pub/Sub provides scalable, durable messaging**.
- **Meets Google Cloud best practices for real-time, ordered event processing**.

✅ **Final Reference:**
[https://cloud.google.com/dataflow/docs/guides](https://cloud.google.com/dataflow/docs/guides)

**⚠️ Note:** Pub/Sub alone now supports message ordering (ordering keys) and exactly-once delivery (pull subscriptions, within one region). The keyed Pub/Sub + Dataflow remains a safe answer when deduplication and global scale are needed.

</details>

---

### Exam 2 · Q39

**Your company plans to lift and shift its Linux RHEL 6.5+ virtual machines from an on-premises VMware environment to Google Cloud Compute Engine. You want to follow Google-recommended best practices for migration.**

**What should you do?**

- A. **Define a migration plan** based on a **list of applications and their dependencies**. **Migrate each virtual machine** individually to **Compute Engine** using **Migrate for Compute Engine**.
- B. **Assess the virtual machines** running in the **current VMware environment**. **Create images of all disks** and **import them into Compute Engine**. **Create standard virtual machines**, using the **imported boot disks**.
- C. **Perform an assessment** of virtual machines in the **current VMware environment**. **Define a migration plan**, prepare a **Migrate for Compute Engine RunBook**, and **execute the migration**.
- D. **Assess the virtual machines** in the **current VMware environment**. **Install a third-party agent** on all selected virtual machines. **Migrate all virtual machines** to **Compute Engine**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. **Perform an assessment** of virtual machines in the **current VMware environment**. **Define a migration plan**, prepare a **Migrate for Compute Engine RunBook**, and **execute the migration**.

**Correct Answer:**

**C. Perform an assessment of virtual machines in the current VMware environment. Define a migration plan, prepare a Migrate for Compute Engine RunBook, and execute the migration.**

**Explanation:**

To successfully **lift and shift** RHEL **6.5+ virtual machines from an on-premises VMware environment to Google Cloud Compute Engine**, Google Cloud recommends using **Migrate for Compute Engine** (formerly Velostrata).

This approach ensures:

- **Automated, minimal-downtime migration.**
- **Preserving existing VM configurations.**
- **Post-migration testing to validate workloads in Compute Engine.**

**Key Steps for Best-Practice Migration Using Migrate for Compute Engine**

**1. Perform a Pre-Migration Assessment**

- **Use Migrate for Compute Engine’s assessment tools** to analyze the **VMs, dependencies, OS versions, and application requirements**.
- **Identify compatibility issues with Compute Engine** (e.g., deprecated drivers, OS requirements).
- **Determine networking, firewall, and storage configurations**.

**2. Define a Migration Plan**

- **Prioritize workloads based on business requirements** (e.g., critical apps first).
- **Prepare a RunBook** that includes:
  - **VM settings, dependencies, and expected downtime.**
  - **Network configuration in Google Cloud.**
  - **Testing and rollback plans.**

**3. Prepare for Migration**

- **Set up Google Cloud infrastructure**: VPC, subnets, firewall rules, and IAM permissions.
- **Deploy Migrate for Compute Engine Manager** in Google Cloud.
- **Install Migrate for Compute Engine components** in VMware.

**4. Execute the Migration**

- **Migrate workloads in batches** using Migrate for Compute Engine.
- **Validate VM functionality in Compute Engine** before finalizing the cutover.
- **Monitor the migration process via Google Cloud Console.**

**5. Optimize Post-Migration**

- **Upgrade or modernize VMs** to take advantage of cloud-native capabilities.
- **Decommission on-premises VMs after successful migration.**

**Supporting Documentation:**

- **Migrate for Compute Engine Overview**:
  https://cloud.google.com/migrate/compute-engine/docs/
- **VMware to Compute Engine Migration Guide**:
  https://cloud.google.com/migrate/compute-engine/docs/vmware-migration

**Why Other Options Are Incorrect?**

**A. Define a migration plan based on a list of applications and their dependencies. Migrate each virtual machine individually to Compute Engine using Migrate for Compute Engine.**

❌ **Incorrect:**

- **Migrating VMs one by one without a proper RunBook is inefficient.**
- **Does not mention pre-migration assessment**, which is critical for success.

✅ **Reference:**
https://cloud.google.com/migrate/compute-engine/docs/plan-migration

**B. Assess the virtual machines running in the current VMware environment. Create images of all disks and import them into Compute Engine. Create standard virtual machines, using the imported boot disks.**

❌ **Incorrect:**

- **Manual image creation is not efficient for large-scale migrations.**
- **Migrate for Compute Engine provides an automated, structured approach.**

✅ **Reference:**
https://cloud.google.com/migrate/compute-engine/docs/architecture

**D. Assess the virtual machines in the current VMware environment. Install a third-party agent on all selected virtual machines. Migrate all virtual machines to Compute Engine.**

❌ **Incorrect:**

- **Google recommends using Migrate for Compute Engine rather than third-party tools.**
- **Does not account for pre-migration planning and RunBook creation.**

✅ **Reference:**
https://cloud.google.com/migrate/compute-engine/docs/how-to/

**Conclusion:**

The best approach is **C. Perform an assessment of virtual machines in the current VMware environment. Define a migration plan, prepare a Migrate for Compute Engine RunBook, and execute the migration**, because:

- **It follows Google Cloud's best practices for VMware migration**.
- **Ensures minimal downtime and risk** through structured migration.
- **Utilizes Migrate for Compute Engine for automation and efficiency.**

✅ **Final Reference:**
[https://cloud.google.com/migrate/compute-engine/docs/vmware-migration](https://cloud.google.com/migrate/compute-engine/docs/vmware-migration)

**⚠️ Note:** Migrate for Compute Engine is now **Migrate to Virtual Machines**, part of Migration Center.

</details>

---

### Exam 2 · Q40

You need to **deploy an application** on **Google Cloud** that:

- **Receives traffic via TCP**
- **Reads and writes data** to the **filesystem**
- **Does not support horizontal scaling**
- **Requires full control over the filesystem data** (concurrent access causes corruption)
- **Must be available 24/7** but **can tolerate downtime** in case of an incident

How should you **design the architecture** for this application on **Google Cloud**?

- A. Use a **managed instance group** with instances in **multiple zones**, use **Cloud Filestore**, and deploy an **HTTP load balancer** in front of the instances.
- B. Use a **managed instance group** with instances in **multiple zones**, use **Cloud Filestore**, and deploy a **network load balancer** in front of the instances.
- C. Use an **unmanaged instance group** with an **active and standby instance** in different zones, use a **regional persistent disk**, and deploy an **HTTP load balancer** in front of the instances.
- D. Use an **unmanaged instance group** with an **active and standby instance** in different zones, use a **regional persistent disk**, and deploy a **network load balancer** in front of the instances.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Use an **unmanaged instance group** with an **active and standby instance** in different zones, use a **regional persistent disk**, and deploy a **network load balancer** in front of the instances.

**Correct Answer:**

**D. Use an unmanaged instance group with an active and standby instance in different zones, use a regional persistent disk, and deploy a network load balancer in front of the instances.**

**Explanation:**

This application has several key requirements:

1. **Receives traffic via TCP** → Requires a **network load balancer** (not HTTP load balancer).
2. **Reads and writes to the filesystem** → Requires **persistent disk** (not shared storage like Filestore).
3. **Does not support horizontal scaling** → Must use **an active-standby architecture**.
4. **Full control over filesystem data (concurrent access causes corruption)** → **A single active writer setup** is needed.
5. **Must be available 24/7 but can tolerate downtime in case of an incident** → **Regional persistent disk with failover** is required.

**Why This Architecture Works**

**1. Use an Unmanaged Instance Group with Active/Standby Setup**

- Since **horizontal scaling is not supported**, a **managed instance group (MIG) is unnecessary**.
- **Unmanaged instance groups allow manual failover** between the **active and standby** instances.

**2. Use a Regional Persistent Disk for Data Storage**

- **A single active VM should access the disk at a time** (to prevent corruption).
- **Regional Persistent Disks are automatically replicated** across two zones for **high availability**.
- **Failover is manual** but ensures **data consistency** when switching to the standby instance.

**3. Use a Network Load Balancer for TCP Traffic**

- **The application uses TCP**, so a **network load balancer** is required.
- **HTTP load balancers only work for HTTP(S) traffic**, making them unsuitable for this scenario.

**Supporting Documentation:**

- **Regional Persistent Disk Overview:**
  https://cloud.google.com/compute/docs/disks#replication
- **Unmanaged Instance Groups:**
  https://cloud.google.com/compute/docs/instance-groups/unmanaged
- **Network Load Balancer (TCP/UDP Load Balancing):**
  https://cloud.google.com/load-balancing/docs/network

**Why Other Options Are Incorrect?**

**A. Use a managed instance group with instances in multiple zones, use Cloud Filestore, and deploy an HTTP load balancer in front of the instances.**

❌ **Incorrect:**

- **Filestore is a shared filesystem**, which **allows concurrent writes**, making it **unsuitable for applications that require exclusive filesystem access**.
- **HTTP Load Balancer does not support TCP traffic**.

✅ **Reference:**
https://cloud.google.com/filestore/docs/instances

**B. Use a managed instance group with instances in multiple zones, use Cloud Filestore, and deploy a network load balancer in front of the instances.**

❌ **Incorrect:**

- **Cloud Filestore does not guarantee exclusive access** to the filesystem.
- **Managed instance groups are designed for stateless applications that scale horizontally**, which **this application does not support**.

✅ **Reference:**
https://cloud.google.com/compute/docs/instance-groups

**C. Use an unmanaged instance group with an active and standby instance in different zones, use a regional persistent disk, and deploy an HTTP load balancer in front of the instances.**

❌ **Incorrect:**

- **HTTP Load Balancer is not designed for TCP-based applications**.
- **Network Load Balancer is the correct choice for handling TCP traffic.**

✅ **Reference:**
https://cloud.google.com/load-balancing/docs/network

**Conclusion:**

The best solution is **D. Use an unmanaged instance group with an active and standby instance in different zones, use a regional persistent disk, and deploy a network load balancer in front of the instances**, because:

- **It ensures high availability** via **active-standby failover**.
- **It prevents filesystem corruption** using a **regional persistent disk with a single writer**.
- **It supports TCP traffic** using a **network load balancer**.
- **It aligns with Google Cloud best practices for stateful workloads**.

✅ **Final Reference:**
[https://cloud.google.com/compute/docs/instance-groups/unmanaged](https://cloud.google.com/compute/docs/instance-groups/unmanaged)

</details>

---

### Exam 2 · Q45

Your company has decided to **outsource operations functions**. You need a solution that allows **developers to stage new versions** of a **cloud-based application** in the **production environment**, while enabling the **outsourced operations team** to **autonomously promote staged versions to production**.

You also want to **minimize operational overhead**.

Which **Google Cloud product** should you migrate to?

- A. App Engine
- B. GKE On-Prem
- C. Compute Engine
- D. Google Kubernetes Engine (GKE)

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. App Engine

**Correct Answer:**

**A. App Engine**

**Explanation:**

The **key requirements** in this scenario are:

1. **Developers can stage new versions** of an application in the **production environment**.
2. **The outsourced operations team** must have control to **promote staged versions to production**.
3. **Minimize operational overhead** → Requires a **fully managed** solution.

Google **App Engine** is the **best choice** because:

- **Supports versioning & traffic splitting**: Developers can **deploy multiple versions**, and the **operations team can promote a new version** with **zero downtime**.
- **Fully managed (low operational overhead)**: **No infrastructure management** is needed, unlike Compute Engine or GKE.
- **Automatic scaling** and **integrated monitoring** simplify **deployment and operations management**.

**How App Engine Meets the Requirements**

**1. Staging New Versions in Production**

- Developers can **deploy multiple versions** of the application:
  ```
  gcloud app deploy app-v2.yaml --version=v2
  ```
- **The application runs in production**, but traffic is **not yet switched**.

**2. Operations Team Can Promote the Version Autonomously**

- The outsourced team **can shift traffic** to the new version **gradually**:
  ```
  gcloud app services set-traffic my-service --splits v1=50,v2=50
  ```
- **Zero downtime switching** ensures a smooth transition.

**3. Minimal Operational Overhead**

- **No need to manage VMs, clusters, or networking**.
- **Google automatically handles scaling, updates, and security patches**.

✅ **Reference:**
https://cloud.google.com/appengine/docs/standard

**Why Other Options Are Incorrect?**

**B. GKE On-Prem**

❌ **Incorrect:**

- **Requires managing Kubernetes clusters on-prem**, which increases **operational overhead**.
- **Does not minimize infrastructure management**, violating the requirement.

✅ **Reference:**
https://cloud.google.com/anthos/gke/docs/on-prem

**C. Compute Engine**

❌ **Incorrect:**

- **Requires manual instance management**.
- **No built-in versioning or traffic splitting** → Promotions require **manual orchestration**.
- **Higher operational overhead compared to App Engine**.

✅ **Reference:**
https://cloud.google.com/compute

**D. Google Kubernetes Engine (GKE)**

❌ **Incorrect:**

- **Requires managing Kubernetes clusters** → **higher operational complexity**.
- **Needs manual CI/CD setup for versioning and promotions**.
- **More suited for microservices rather than simple versioned deployments**.

✅ **Reference:**
https://cloud.google.com/kubernetes-engine/docs

**Conclusion:**

The best option is **A. App Engine**, because:

- **It allows developers to stage new versions** while the **operations team promotes them autonomously**.
- **Traffic splitting ensures smooth rollouts**.
- **Fully managed with minimal operational overhead**.

✅ **Final Reference:**
[https://cloud.google.com/appengine/docs/standard](https://cloud.google.com/appengine/docs/standard)

</details>

---

### Exam 2 · Q52

**Which solution should you choose to ensure the application is quickly restored in another zone with the latest data whenever a zonal outage occurs on Compute Engine?**

- A. Create a snapshot schedule for the disk containing the application data. Whenever a zonal outage occurs, use the latest snapshot to restore the disk in the same zone.
- B. Configure the Compute Engine instances with an instance template for the application, and use a regional persistent disk for the application data. Whenever a zonal outage occurs, use the instance template to spin up the application in another zone in the same region. Use the regional persistent disk for the application data.
- C. Create a snapshot schedule for the disk containing the application data. Whenever a zonal outage occurs, use the latest snapshot to restore the disk in another zone within the same region.
- D. Configure the Compute Engine instances with an instance template for the application, and use a regional persistent disk for the application data. Whenever a zonal outage occurs, use the instance template to spin up the application in another region. Use the regional persistent disk for the application data.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Configure the Compute Engine instances with an instance template for the application, and use a regional persistent disk for the application data. Whenever a zonal outage occurs, use the instance template to spin up the application in another zone in the same region. Use the regional persistent disk for the application data.

**Correct Answer:**

**B. Configure the Compute Engine instances with an instance template for the application, and use a regional persistent disk for the application data. Whenever a zonal outage occurs, use the instance template to spin up the application in another zone in the same region. Use the regional persistent disk for the application data.**

**Explanation:**

The **best way to ensure high availability in case of a zonal outage** is to use:

- **Regional Persistent Disks (PDs)**: These **synchronously replicate** data across two zones in a **single region** to ensure the latest data is always available in another zone.
- **Instance Templates**: These allow for rapid provisioning of **Compute Engine instances** in another zone **automatically** when a failure occurs.
- **Multi-Zone Deployment**: Ensures the application can be **quickly restored within the same region** without manual intervention.

✅ **Key Advantages of This Approach:**

- **Regional PDs automatically replicate data between two zones**, ensuring minimal data loss.
- **Instance templates simplify failover**, allowing new instances to be created quickly in an alternative zone.
- **This solution follows Google Cloud best practices for high availability and disaster recovery**.

✅ **Reference:**
https://cloud.google.com/compute/docs/disks#repds

**Why Other Options Are Incorrect?**

**A. Create a snapshot schedule for the disk containing the application data. Whenever a zonal outage occurs, use the latest snapshot to restore the disk in the same zone.**

❌ **Incorrect:**

- **Snapshots are NOT real-time and do not offer high availability.** They are **asynchronous backups**, meaning data loss could occur if a failure happens between snapshots.
- **Restoring a disk in the same zone is not possible if the entire zone is down.**
- **Snapshots take time to restore, which delays recovery.**

✅ **Reference:**
https://cloud.google.com/compute/docs/disks/snapshots

**C. Create a snapshot schedule for the disk containing the application data. Whenever a zonal outage occurs, use the latest snapshot to restore the disk in another zone within the same region.**

❌ **Incorrect:**

- **Snapshots are not a real-time failover mechanism.** Data loss is possible between snapshots.
- **Manually restoring a disk from a snapshot takes time**, which results in **longer downtime** compared to a **regional persistent disk** that offers **automatic failover**.

✅ **Reference:**
https://cloud.google.com/compute/docs/disks/snapshots

**D. Configure the Compute Engine instances with an instance template for the application, and use a regional persistent disk for the application data. Whenever a zonal outage occurs, use the instance template to spin up the application in another region. Use the regional persistent disk for the application data.**

❌ **Incorrect:**

- **Regional Persistent Disks are limited to a single region**, so they cannot be used across different regions.
- **A region-wide outage is extremely rare**, and Google Cloud **recommends a multi-zone setup within a region rather than multi-region unless necessary**.
- **For cross-region high availability, Cloud Storage, Cloud SQL, or Spanner would be better suited instead of Regional PDs**.

✅ **Reference:**
https://cloud.google.com/compute/docs/disks#repds

**Conclusion:**

The best approach is **B. Configure the Compute Engine instances with an instance template for the application, and use a regional persistent disk for the application data**, because:

- **It enables automatic failover to another zone within the same region**.
- **It ensures the latest data is available via Regional Persistent Disks**.
- **It follows Google Cloud best practices for disaster recovery and high availability**.

✅ **Final Reference:**
[https://cloud.google.com/compute/docs/disks#repds](https://cloud.google.com/compute/docs/disks#repds)

</details>

---

### Exam 2 · Q53

Your company's **Data Science team** needs to **migrate Hadoop jobs** to **Google Cloud** without modifying the **underlying infrastructure**. You also want to **minimize costs** and **reduce infrastructure management efforts**.

What should you do?

- A. Create a Dataproc cluster using standard worker instances.
- B. Create a Dataproc cluster using preemptible worker instances.
- C. Manually deploy a Hadoop cluster on Compute Engine using standard instances.
- D. Manually deploy a Hadoop cluster on Compute Engine using preemptible instances.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Create a Dataproc cluster using preemptible worker instances.

**Correct Answer:**

**B. Create a Dataproc cluster using preemptible worker instances.**

**Explanation:**

The **best approach** to migrate Hadoop jobs to **Google Cloud** **without modifying the underlying infrastructure** while **minimizing costs** and **reducing infrastructure management** is to use **Google Cloud Dataproc with preemptible worker instances**.

✅ **Google Cloud Dataproc** is a **fully managed Hadoop and Spark service**, which allows the **Data Science team to run existing Hadoop jobs without infrastructure modifications**.
✅ **Preemptible worker instances** **drastically reduce costs** (by up to 80%) while still allowing non-critical workloads to run efficiently.
✅ **Dataproc provides automated scaling, monitoring, and integration with other Google Cloud services**, reducing operational overhead.

**How to Implement This?**

**1. Create a Dataproc Cluster with Preemptible Workers**

Run the following command:

```
gcloud dataproc clusters create my-dataproc-cluster \    --region=us-central1 \    --num-workers=2 \    --num-preemptible-workers=4 \    --worker-machine-type=n1-standard-4 \    --image-version=2.0-debian10
```

- This command **creates a Dataproc cluster** with **2 standard workers and 4 preemptible workers**.
- **Preemptible workers handle temporary workloads at a lower cost.**

✅ **Reference:**
https://cloud.google.com/dataproc/docs/concepts/preemptible-vms

**Why Other Options Are Incorrect?**

**A. Create a Dataproc cluster using standard worker instances.**

❌ **Incorrect:**

- **This option is functional but not cost-effective.**
- **Standard worker instances increase costs significantly**, whereas preemptible workers reduce costs by up to 80%.
- **Preemptible instances should be used when cost optimization is a priority**.

✅ **Reference:**
https://cloud.google.com/dataproc/docs/concepts/compute/dataproc-pricing

**C. Manually deploy a Hadoop cluster on Compute Engine using standard instances.**

❌ **Incorrect:**

- **Manually deploying Hadoop on Compute Engine requires extensive infrastructure management**, including node provisioning, configuration, and scaling.
- **Dataproc automates Hadoop deployment, making it easier to manage and scale**.
- **Higher operational overhead** compared to a managed Dataproc solution.

✅ **Reference:**
https://cloud.google.com/dataproc/docs/concepts/overview

**D. Manually deploy a Hadoop cluster on Compute Engine using preemptible instances.**

❌ **Incorrect:**

- **While preemptible instances lower costs, manually deploying Hadoop increases complexity and management efforts.**
- **Dataproc automates deployment and scales dynamically, making it a better choice than manual deployment.**

✅ **Reference:**
https://cloud.google.com/dataproc/docs/concepts/overview

**Conclusion:**

The best solution is **B. Create a Dataproc cluster using preemptible worker instances**, because:

- **It enables running Hadoop jobs without modifying the infrastructure.**
- **Preemptible instances reduce costs while maintaining performance.**
- **Dataproc automates infrastructure management, reducing operational overhead.**

✅ **Final Reference:**
[https://cloud.google.com/dataproc/docs/concepts/preemptible-vms](https://cloud.google.com/dataproc/docs/concepts/preemptible-vms)

</details>

---

### Exam 2 · Q56

You need to **deploy a stateful workload** on **Google Cloud**.

- The **workload can scale horizontally**.
- Each instance must **read and write to the same POSIX filesystem**.
- Under **high load**, the workload must support **up to 100 MB/s of writes**.

What should you do?

- A. **Use a persistent disk** for each instance.
- B. **Use a regional persistent disk** for each instance.
- C. **Create a Cloud Filestore instance** and **mount it on each instance**.
- D. **Create a Cloud Storage bucket** and **mount it on each instance** using **gcsfuse**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. **Create a Cloud Filestore instance** and **mount it on each instance**.

**Correct Answer:**

**C. Create a Cloud Filestore instance and mount it on each instance.**

**Explanation:**

The **best solution for a stateful workload** that requires **a shared POSIX filesystem with high write throughput** (**100 MB/s**) is **Google Cloud Filestore**.

✅ **Cloud Filestore provides a fully managed NFS (Network File System) solution**, ensuring multiple instances **can read and write to the same filesystem**.
✅ **POSIX-compliant**: Ensures that all instances **can simultaneously read and write** while maintaining filesystem consistency.
✅ **Supports high throughput**: Filestore’s **performance tier can handle up to multiple GB/s of writes**.

**How to Implement This?**

**1. Create a Cloud Filestore Instance**

```
gcloud filestore instances create my-filestore \    --zone=us-central1-a \    --tier=high-scale \    --file-share=name="myshare",capacity=5TB \    --network=name=default
```

- **This creates a Filestore instance** with **high performance** to meet the 100 MB/s write requirement.

**2. Mount Cloud Filestore on Compute Engine Instances**

```
sudo mkdir -p /mnt/filestoresudo mount -o vers=3,hard,timeo=600,retrans=2 nfs-server-ip:/myshare /mnt/filestore
```

- **This mounts the shared Cloud Filestore storage on each instance**, allowing multiple instances to read/write.

✅ **Reference:**
https://cloud.google.com/filestore/docs/creating-instances

**Why Other Options Are Incorrect?**

**A. Use a persistent disk for each instance.**

❌ **Incorrect:**

- **Persistent disks are NOT shared storage**—each instance gets a separate disk.
- **POSIX-compliant filesystem access is not possible across multiple instances.**

✅ **Reference:**
https://cloud.google.com/compute/docs/disks

**B. Use a regional persistent disk for each instance.**

❌ **Incorrect:**

- **Regional Persistent Disks are replicated across zones but are still attached to only one VM at a time.**
- **They do not support concurrent access by multiple instances.**

✅ **Reference:**
https://cloud.google.com/compute/docs/disks/regional-persistent-disk

**D. Create a Cloud Storage bucket and mount it on each instance using gcsfuse.**

❌ **Incorrect:**

- **Cloud Storage is not a POSIX-compliant filesystem.**
- `gcsfuse` **allows access to Cloud Storage, but it does not support concurrent file locking or low-latency operations required for high-throughput writes.**
- **Not designed for workloads requiring shared file storage with 100 MB/s of writes.**

✅ **Reference:**
https://cloud.google.com/storage/docs/gcs-fuse

**Conclusion:**

The best option is **C. Create a Cloud Filestore instance and mount it on each instance**, because:

- **It supports concurrent POSIX-compliant read/write access**.
- **It provides the required high throughput of 100 MB/s or more**.
- **It ensures data consistency across multiple instances**.
- **It follows Google Cloud best practices for shared storage in a stateful workload.**

✅ **Final Reference:**
[https://cloud.google.com/filestore](https://cloud.google.com/filestore)

</details>

---

### Exam 2 · Q62

You are deploying a **single Cloud SQL MySQL second-generation database** that stores **business-critical transaction data**.

To **minimize data loss** in case of a **catastrophic failure**, which **two features** should you implement? (Choose two.)

- A. Sharding
- B. Read replicas
- C. Binary logging
- D. Automated backups
- E. Semisynchronous replication

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Binary logging **|** D. Automated backups

**Correct Answers:**

**C. Binary logging**
**D. Automated backups**

**Explanation:**

For a **business-critical Cloud SQL MySQL** database, **minimizing data loss** in case of a catastrophic failure requires **proper backups and point-in-time recovery mechanisms**.

✅ **Option C: Binary Logging**

- **Enables Point-in-Time Recovery (PITR)** by logging all changes (INSERT, UPDATE, DELETE).
- **Captures transaction history**, allowing recovery up to the last committed transaction before failure.
- **Essential for disaster recovery** when used with automated backups.

✅ **Reference:**
https://cloud.google.com/sql/docs/mysql/enable-binary-logging

✅ **Option D: Automated Backups**

- **Cloud SQL provides daily automated backups**, ensuring data can be restored if a failure occurs.
- **Allows full recovery of the database** in case of corruption or accidental deletion.
- **Can be combined with binary logs for point-in-time recovery**.

✅ **Reference:**
https://cloud.google.com/sql/docs/mysql/backup-recovery/backups

**Why Other Options Are Incorrect?**

**A. Sharding**

❌ **Incorrect:**

- **Sharding distributes data across multiple instances** for **scalability, not disaster recovery**.
- **It does not provide data protection**—data loss can still occur if backups or binary logging are not enabled.

✅ **Reference:**
https://cloud.google.com/sql/docs/mysql/scale-out-using-sharding

**B. Read replicas**

❌ **Incorrect:**

- **Read replicas improve read performance** and provide **high availability** but **are not designed for disaster recovery**.
- **Data loss can propagate to replicas if a failure occurs** (e.g., accidental DELETE operations).
- **Read replicas do not support PITR** (point-in-time recovery).

✅ **Reference:**
https://cloud.google.com/sql/docs/mysql/replication

**E. Semisynchronous Replication**

❌ **Incorrect:**

- **Provides high availability, not data recovery**.
- **Data replication is synchronous, but if both primary and replicas fail, data is still lost**.
- **Replication alone does not prevent data loss if backups are not taken**.

✅ **Reference:**
https://cloud.google.com/sql/docs/mysql/high-availability

**Conclusion:**

To **minimize data loss** in **Google Cloud SQL MySQL**, the best approach is:

1. **Enable Binary Logging (C)** for **Point-in-Time Recovery (PITR)**.
2. **Use Automated Backups (D)** for **full database recovery**.

✅ **Final References:**

- **Binary Logging:** [https://cloud.google.com/sql/docs/mysql/enable-binary-logging](https://cloud.google.com/sql/docs/mysql/enable-binary-logging)
- **Automated Backups:** https://cloud.google.com/sql/docs/mysql/backup-recovery/backups

</details>

---

### Exam 3 · Q2

You are designing the infrastructure for a high-throughput web application on Google Cloud. The application must handle up to **500,000 incoming requests per second**, storing data from each request. Later, this data will be queried in **real time** using **exact-match lookups on a known set of attributes**. The application may experience **periods of inactivity**, and the business has emphasized **cost efficiency** as a priority.

Which combination of web service platform and database would best meet these requirements?

- A. Deploy the service on **Cloud Run** and store the data in **BigQuery**
- B. Deploy the service on **Cloud Run** and store the data in **Cloud Bigtable**
- C. Use a **Compute Engine autoscaling managed instance group** with **BigQuery** for storage
- D. Use a **Compute Engine autoscaling managed instance group** with **Cloud Bigtable** for storage

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Deploy the service on **Cloud Run** and store the data in **Cloud Bigtable**

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

</details>

---

### Exam 3 · Q5

Your company has asked you to design a **highly reliable web application** that includes a **few public APIs** as the backend. While **regular traffic is expected to be low**, there may be **occasional spikes**. You are required to use **Cloud Load Balancing**, and the solution should remain **cost-efficient for end users**.

What is the most appropriate solution?

- A. Store static content (HTML, images) in **Cloud CDN**, host the APIs on **App Engine**, and save user data in **Cloud SQL**.
- B. Store static content (HTML, images) in a **Cloud Storage bucket**, deploy the APIs to a **zonal Google Kubernetes Engine cluster** with nodes spread across multiple zones, and use **Cloud Spanner** for storing user data.
- C. Store static content (HTML, images) in **Cloud CDN**, host the APIs using **Cloud Run**, and store user data in **Cloud SQL**.
- D. Store static content (HTML, images) in a **Cloud Storage bucket**, use **Cloud Functions** for hosting the APIs, and store user data in **Firestore**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Store static content (HTML, images) in a **Cloud Storage bucket**, use **Cloud Functions** for hosting the APIs, and store user data in **Firestore**.

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

</details>

---

### Exam 3 · Q10

Your organization is building a new application that will enable **users around the world** to **upload and share photos** with selected individuals. The application must be able to **handle millions of concurrent users**. The development team wants to **focus solely on writing application code** without being responsible for provisioning or managing the underlying infrastructure.

Which Google Cloud service should you choose to **deploy the application**?

- A. App Engine
- B. Cloud Endpoints
- C. Compute Engine
- D. Google Kubernetes Engine

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. App Engine

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

</details>

---

### Exam 3 · Q16

A **development team** is seeking your guidance. They plan to build and deploy an **HTTP(S) API** using **Go 1.12**. The workload for this API is expected to be **highly unpredictable**, and the system must maintain **reliability during traffic spikes**. They also want to **minimize operational overhead** and infrastructure management.

Which solution should you recommend?

- A. Containerize the application and deploy it on **Google Kubernetes Engine (GKE)**.
- B. Build the application for the **App Engine standard environment**.
- C. Deploy the application to **Compute Engine** using a **Managed Instance Group (MIG)**.
- D. Build the application for the **App Engine flexible environment** using a **custom runtime**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Build the application for the **App Engine standard environment**.

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

</details>

---

### Exam 3 · Q17

Your organization is designing a **data lake architecture on Google Cloud** to support various **data ingestion pipelines** that collect **unstructured data** from multiple sources. After the data is ingested, it will be used in **several processing pipelines** to build a **recommendation engine** for website users.

The **structure of the incoming data may change at any time**, and it is crucial to **store the data exactly as received** so it can be **reprocessed later** if the current pipelines fail to handle the structural changes.

What is the best architectural approach for storing the ingested data to meet this requirement?

- A. Process the data first through the pipeline, then store the **processed data** in **BigQuery** for future reprocessing.
- B. Store the **raw data directly in BigQuery**, and have the processing pipelines read from the BigQuery table.
- C. Process the data through the pipeline first, then store the **processed output** in a **Cloud Storage bucket** for reprocessing.
- D. Store the **raw unprocessed data** in a **Cloud Storage bucket**, and design the processing pipelines to read from that bucket.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Store the **raw unprocessed data** in a **Cloud Storage bucket**, and design the processing pipelines to read from that bucket.

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

</details>

---

### Exam 3 · Q21

TechNova Inc. has an enterprise-grade application deployed on Google Compute Engine that demands both high availability and high performance. The application is set up in an active-passive configuration across two virtual machine instances located in separate zones within the same region. It stores data on a persistent disk. In the event of a zone failure, the data must be instantly accessible by the instance in the other zone. You are tasked with optimizing performance while minimizing both downtime and potential data loss.

**What should you do to meet these requirements?**

- A. Attach a persistent SSD disk to the active instance. Schedule hourly snapshots of the disk. If a zone becomes unavailable, recreate the persistent SSD disk from the latest snapshot and attach it to the standby instance.
- B. Create a Cloud Storage bucket. Mount it on the active instance using gcsfuse. If a zone outage occurs, mount the same Cloud Storage bucket on the passive instance using gcsfuse.
- C. Attach a **regional SSD persistent disk** to the active instance. In case of a zone failure, **force-attach** the regional disk to the passive instance in the other zone.
- D. Attach a **local SSD** to the active instance. Use rsync every hour to copy data to a persistent SSD disk attached to the passive instance. If a zone outage occurs, switch operations to the passive instance.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Attach a **regional SSD persistent disk** to the active instance. In case of a zone failure, **force-attach** the regional disk to the passive instance in the other zone.

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

</details>

---

### Exam 3 · Q28

At **CalcNet Solutions**, your team manages a **stateless web API** that performs scientific computations. This API is currently hosted on a **Google Kubernetes Engine (GKE)** cluster located in the `us-central1` region. The company now wants to **expand access to customers in Asia**, with a key objective of **reducing latency** for users in that region.

**Which action should you take to best meet this requirement?**

- A. Provision a second GKE cluster in `asia-southeast1`, expose both clusters using **Service of type LoadBalancer**, and add the **public IPs** to the **Cloud DNS** zone.
- B. Use a **global HTTP(S) load balancer** with **Cloud CDN** enabled.
- C. Deploy a second GKE cluster in `asia-southeast1`, and use **kubemci** to configure a **global HTTP(S) load balancer**.
- D. Increase the **CPU and memory resources** allocated to the application running in the existing cluster.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Deploy a second GKE cluster in `asia-southeast1`, and use **kubemci** to configure a **global HTTP(S) load balancer**.

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

</details>

---

### Exam 3 · Q32

At **TechVeritas Inc.**, the testing framework is a **custom C++ application** that executes a full suite of tests throughout the day on **Linux virtual machines**. Running the complete test suite takes several hours and currently relies on a small pool of **on-premises servers dedicated to testing**.

The company now wants to **move the testing infrastructure to Google Cloud** in order to **significantly reduce the total test execution time**, while making **minimal changes** to the existing tests.

**Which cloud infrastructure should you recommend?**

- A.Use **Google Compute Engine unmanaged instance groups** with a **Network Load Balancer**.
- B.Use **Google Compute Engine managed instance groups** with **auto-scaling** to dynamically provision test VMs.
- C.Use **Google Cloud Dataproc** to run the tests as **Apache Hadoop** jobs for distributed processing.
- D.Use **Google App Engine** and configure **Cloud Logging (formerly Stackdriver)** for test monitoring.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B.Use **Google Compute Engine managed instance groups** with **auto-scaling** to dynamically provision test VMs.

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

</details>

---

### Exam 3 · Q34

The **application reliability team at Innovare Tech** has recently introduced a debug feature in their backend service that streams **all server event records** to **Google Cloud Storage** for later analysis. Each event record ranges from **50 KB to 15 MB** in size, and the system may produce up to **3,000 events per second** during peak load.

As the cloud architect, you're tasked with designing a process that **minimizes data loss** while handling this volume and variety of data.

**Which process should you implement?**

- A.Append metadata directly to the file body Compress each event file individually Name each file using the format: `serverName-Timestamp` If the current bucket is older than 1 hour, create a new bucket and save files to it; otherwise, continue using the existing bucket
- B.Batch every 10,000 events along with a **manifest file** containing metadata Compress the batch and manifest into a single archive file Name files using the format: `serverName-EventSequence` If the current bucket is older than 1 day, create a new bucket and upload the archive there; otherwise, use the current bucket
- C.Compress each file individually Name each file as `serverName-EventSequence` Save all files into a single bucket After upload, set custom metadata headers for each object
- D.Append metadata to the body of each file Compress files individually Name each file using a **random prefix pattern** Save all files into a single Cloud Storage bucket

<details><summary>Answer &amp; explanation</summary>

**Correct:** D.Append metadata to the body of each file Compress files individually Name each file using a **random prefix pattern** Save all files into a single Cloud Storage bucket

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

</details>

---

### Exam 3 · Q37

**Your company aims to explore cloud services with minimal risk. They intend to archive around 100 TB of their log data to the cloud and experiment with serverless analytics features while maintaining the data for long-term disaster recovery backup. What two steps should they undertake? (Choose two)**

- A. Load logs into BigQuery.
- B. Load logs into Cloud SQL.
- C. Import logs into Cloud Logging.
- D. Insert logs into Cloud Bigtable.
- E. Upload log files into Cloud Storage.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Load logs into BigQuery. **|** E. Upload log files into Cloud Storage.

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

</details>

---

### Exam 3 · Q49

The **marketing team at NexaDigital** plans to launch a promotional email campaign. The **development team** wants to minimize operational overhead while preparing for a potentially high volume of customer interactions—ranging from **100 to 500,000 click-throughs per day**. The campaign will direct users to a lightweight promotional website that collects basic user details and preferences.

Which **two infrastructure solutions** should you recommend to meet their scalability and management goals? *(Choose two.)*

- A. Deploy the website on **Google App Engine**, and use **Cloud Datastore** to store user information.
- B. Use **Google Kubernetes Engine (GKE)** to host the website and store user data on **persistent disks**.
- C. Serve the website with a **Managed Instance Group (MIG)** and use **Cloud Bigtable** for storing user data.
- D. Run the website on a **single Compute Engine VM** backed by **Cloud SQL** for data storage.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Deploy the website on **Google App Engine**, and use **Cloud Datastore** to store user information. **|** C. Serve the website with a **Managed Instance Group (MIG)** and use **Cloud Bigtable** for storing user data.

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

</details>

---

### Exam 3 · Q50

TechNova Solutions recently completed a rapid **lift-and-shift migration** to **Google Compute Engine** to meet immediate compute requirements. You now have **nine months** to plan and implement a more **cloud-native architecture** that emphasizes **auto-scaling** and requires **minimal operational overhead (no-ops)**.

Which **two Google Cloud compute services** would best support this transformation? *(Choose two.)*

- A. Compute Engine running containerized workloads
- B. Google Kubernetes Engine (GKE) using containers
- C. Google App Engine Standard Environment
- D. Compute Engine with custom machine types
- E. Compute Engine with managed instance groups (MIGs)

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Google Kubernetes Engine (GKE) using containers **|** C. Google App Engine Standard Environment

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

</details>

---

### Exam 3 · Q53

**SoundStream Inc.** runs a music streaming application on **Google Compute Engine**. The application lets users play their favorite songs, which are stored in **Cloud Storage** and streamed directly to users. The backend operates with a **fixed number of Compute Engine instances**.

Recently, users have reported intermittent failures when trying to play **popular songs**, often requiring multiple attempts before playback is successful. You need to **enhance the application’s performance and reliability**.

What should you do?

- A.Mount the Cloud Storage bucket using **gcsfuse** on each backend Compute Engine instance Serve music files directly from the backend instance
- B.Set up a **Cloud Filestore NFS volume** and attach it to the backend Compute Engine instances Download frequently played songs to the Filestore volume Serve music files directly from the backend instances
- C.Copy frequently accessed songs into **Cloud SQL** as BLOB data Modify the application to query **Cloud SQL** if Cloud Storage performance degrades
- D.Create a **Managed Instance Group (MIG)** of Compute Engine instances Set up a **global external HTTP(S) load balancer** with two backends: The Managed Instance Group The Cloud Storage bucket **Enable Cloud CDN** on the Cloud Storage backend to cache popular content closer to users

<details><summary>Answer &amp; explanation</summary>

**Correct:** D.Create a **Managed Instance Group (MIG)** of Compute Engine instances Set up a **global external HTTP(S) load balancer** with two backends: The Managed Instance Group The Cloud Storage bucket **Enable Cloud CDN** on the Cloud Storage backend to cache popular content closer to users

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

</details>

---

### Exam 3 · Q59

**EdgeSense Corp.** runs an application on **Google Cloud** that collects data from **thousands of globally distributed IoT devices**. The incoming data is published to **Pub/Sub** and streamed in real time into a **Cloud Bigtable SSD cluster** via a **Dataflow pipeline**.

Recently, the operations team reported that the **Cloud Bigtable cluster is experiencing a hotspot**, causing query performance to degrade.

You need to resolve the issue and ensure it doesn’t recur in the future.

What should you do?

- A. Instruct clients to switch from using **Node.js APIs** to **HBase APIs** for data interaction.
- B. Implement logic to **delete records older than 30 days** from the Bigtable cluster.
- C. **Revisit your RowKey design** and ensure the keys are **evenly distributed** across the alphabet to avoid hotspots.
- D. **Double the number of nodes** in the Cloud Bigtable cluster to distribute the load more evenly.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. **Revisit your RowKey design** and ensure the keys are **evenly distributed** across the alphabet to avoid hotspots.

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

</details>

---

### Exam 4 · Q8

**ZenCore Enterprises** is preparing to migrate their **Windows Server 2022** workloads from their on-premises data center to Google Cloud. They want to **bring their existing Windows Server licenses** into the cloud environment as part of the migration process.

What steps should they take to meet this requirement?

- A. Create an image of the on-premises virtual machines and upload it to Cloud Storage. Import the image as a virtual disk into Compute Engine.
- B. Create standard virtual machine instances in Compute Engine. Choose the same Microsoft Windows version (Windows Server 2022) that is currently used on-premises.
- C.Create an image of the on-premises virtual machine. Import the image as a virtual disk in Compute Engine. Launch a standard Compute Engine instance with the same Windows version selected. Attach a data disk containing content that matches the imported image.
- D. Create an image of the on-premises virtual machine. Import the image into Compute Engine using the flag `--os=windows-2022-byol`. Launch a **sole-tenant VM** in Compute Engine using the imported disk as the boot disk.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Create an image of the on-premises virtual machine. Import the image into Compute Engine using the flag `--os=windows-2022-byol`. Launch a **sole-tenant VM** in Compute Engine using the imported disk as the boot disk.

**Correct Answer: D.**

**Create an image of the on-premises virtual machine. Import the image into Compute Engine using the flag --os=windows-2022-byol. Launch a sole-tenant VM in Compute Engine using the imported disk as the boot disk.**

✅ **Justification for Correct Option (D):**

To **bring your own Windows Server licenses (BYOL)** to Google Cloud, organizations must follow Google’s **License Mobility** and **sole-tenant node** requirements.

**Key requirements for BYOL with Windows Server on Google Cloud:**

1. **Use Sole-Tenant Nodes**:
  - Microsoft licensing requires that BYOL of Windows Server licenses can only be done on **dedicated hardware**.
  - In Google Cloud, this means using **Sole-Tenant VMs**.
2. **Import the Windows Image Properly**:
  - You must **import the on-prem VM image** using `gcloud compute images import` with the correct `--os` flag (e.g., `--os=windows-2022-byol`).
  - This ensures that the system is recognized as Windows Server 2022 with Data Center edition (for license compliance).
3. **Use the imported image as the boot disk** for your sole-tenant VM instance.

**Documentation Reference:**

- Bringing existing Windows licenses

*"You can bring your own Windows Server licenses to Compute Engine by using sole-tenant nodes and importing your existing Windows Server images."*

- Creating sole-tenant VMs

❌ **Why Other Options Are Incorrect:**

**A. Create an image and import it, then use it as a virtual disk.**

- **Incorrect**, because this does **not specify** launching the VM on **sole-tenant nodes**, which is **mandatory for BYOL** under Microsoft licensing for Windows Server.
- Without sole-tenant VMs, this violates licensing terms.

**B. Create standard Compute Engine VM using the same Windows version.**

- **Incorrect**, because selecting a standard GCP Windows image uses **Google's SPLA-licensed images**, **not your own licenses**.
- This defeats the purpose of **BYOL**.

**C. Create image, import virtual disk, launch standard VM and attach data disk.**

- **Incorrect**, again because it uses **standard Compute Engine instances**, not **sole-tenant nodes**, which is **non-compliant** with BYOL rules.
- Also, attaching a data disk doesn’t help for **boot licensing** concerns.

✅ **Final Answer: D.**

Because **BYOL for Windows Server on Google Cloud** requires:

- Using **sole-tenant nodes** (for Microsoft licensing compliance),
- **Importing your own Windows Server image** properly,
- And **booting** your instance using that image.

**⚠️ Note:** `gcloud compute images import` is deprecated; Google now points to image imports in Migrate to Virtual Machines. The BYOL rule is unchanged: import as a BYOL image and run it on sole-tenant nodes.

</details>

---

### Exam 4 · Q14

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

**Company overview -**

Helicopter Racing League (HRL) is a global sports league for competitive helicopter racing. Each year HRL holds the world championship and several regional league competitions where teams compete to earn a spot in the world championship. HRL offers a paid service to stream the races all over the world with live telemetry and predictions throughout each race.

**Solution concept -**

HRL wants to migrate their existing service to a new platform to expand their use of managed AI and ML services to facilitate race predictions. Additionally, as new fans engage with the sport, particularly in emerging regions, they want to move the serving of their content, both real-time and recorded, closer to their users.

**Existing technical environment -**

HRL is a public cloud-first company; the core of their mission-critical applications runs on their current public cloud provider. Video recording and editing is performed at the race tracks, and the content is encoded and transcoded, where needed, in the cloud. Enterprise-grade connectivity and local compute is provided by truck-mounted mobile data centers. Their race prediction services are hosted exclusively on their existing public cloud provider. Their existing technical environment is as follows:

Existing content is stored in an object storage service on their existing public cloud provider.

Video encoding and transcoding is performed on VMs created for each job.

Race predictions are performed using TensorFlow running on VMs in the current public cloud provider.

**Business requirements -**

HRL's owners want to expand their predictive capabilities and reduce latency for their viewers in emerging markets. Their requirements are:

Support ability to expose the predictive models to partners.

Increase predictive capabilities during and before races:

- Race results
- Mechanical failures
- Crowd sentiment

Increase telemetry and create additional insights.

Measure fan engagement with new predictions.

Enhance global availability and quality of the broadcasts.

Increase the number of concurrent viewers.

Minimize operational complexity.

Ensure compliance with regulations.

Create a merchandising revenue stream.

**Technical requirements -**

Maintain or increase prediction throughput and accuracy.

Reduce viewer latency.

Increase transcoding performance.

Create real-time analytics of viewer consumption patterns and engagement.

Create a data mart to enable processing of large volumes of race data.

**Executive statement -**

Our CEO, S. Hawke, wants to bring high-adrenaline racing to fans all around the world. We listen to our fans, and they want enhanced video streams that include predictions of events within the race (e.g., overtaking). Our current platform allows us to predict race outcomes but lacks the facility to support real-time predictions during races and the capacity to process season-long results.

**Question**

In reference to the Helicopter Racing League (HRL) case study, HRL aims to enhance prediction accuracy from their ML prediction models. They request the utilization of Google's AI Platform to facilitate comprehension and interpretation of predictions. What course of action should be taken?

- A. Employ Explainable AI.
- B. Employ Vision AI.
- C. Utilize Google Cloud's Operations Suite.
- D. Utilize Jupyter Notebooks.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Employ Explainable AI.

The best course of action in this scenario is

**A. Employ Explainable AI.** Here's why:

- **Core Requirement Alignment:** The primary need is to understand *why* ML models make specific predictions. Explainable AI techniques are explicitly designed to address this by providing insights into the features that contribute most to a prediction.
- **Improved Model Trust and Debugging:** Explainable AI can help build trust in the ML models, identify potential biases or problems, and provide avenues for further refinement.

**Why Others Are Less Optimal:**

- **B. Vision AI:** Vision AI focuses on analyzing images and videos. While it could be a tangential component if predictions are based on visual data, it doesn't directly address the need to explain model decisions.
- **C. Google Cloud's Operations Suite:** Operations Suite (formerly Stackdriver) focuses on monitoring, logging, and troubleshooting production systems. While helpful for overall system health, it doesn't provide the model-level explainability needed here.
- **D. Jupyter Notebooks:** These are valuable tools for data scientists and ML model development but, by themselves, don't offer the explainability features required.

**How Explainable AI Could Be Used In the HRL Context:**

- **Feature Importance:** Identify the key data points (e.g., race track conditions, weather, pilot history, etc.) that have the most significant influence on race outcome predictions.
- **Local Explanations:** Understand why a model made a specific prediction for a particular race.
- **Counterfactual Explanations:** Explore "what if" scenarios to see how changes in input data might affect the prediction outcome.

**Note:** Explainable AI is an active area of research. Google's AI Platform provides tools and libraries to help with its implementation: [https://cloud.google.com/explainable-ai](https://cloud.google.com/explainable-ai)

Further Details:

[https://cloud.google.com/ai-platform/prediction/docs/ai-explanations/overview](https://cloud.google.com/ai-platform/prediction/docs/ai-explanations/overview)

</details>

---

### Exam 4 · Q15

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

**Company overview -**

Helicopter Racing League (HRL) is a global sports league for competitive helicopter racing. Each year HRL holds the world championship and several regional league competitions where teams compete to earn a spot in the world championship. HRL offers a paid service to stream the races all over the world with live telemetry and predictions throughout each race.

**Solution concept -**

HRL wants to migrate their existing service to a new platform to expand their use of managed AI and ML services to facilitate race predictions. Additionally, as new fans engage with the sport, particularly in emerging regions, they want to move the serving of their content, both real-time and recorded, closer to their users.

**Existing technical environment -**

HRL is a public cloud-first company; the core of their mission-critical applications runs on their current public cloud provider. Video recording and editing is performed at the race tracks, and the content is encoded and transcoded, where needed, in the cloud. Enterprise-grade connectivity and local compute is provided by truck-mounted mobile data centers. Their race prediction services are hosted exclusively on their existing public cloud provider. Their existing technical environment is as follows:

Existing content is stored in an object storage service on their existing public cloud provider.

Video encoding and transcoding is performed on VMs created for each job.

Race predictions are performed using TensorFlow running on VMs in the current public cloud provider.

**Business requirements -**

HRL's owners want to expand their predictive capabilities and reduce latency for their viewers in emerging markets. Their requirements are:

Support ability to expose the predictive models to partners.

Increase predictive capabilities during and before races:

- Race results
- Mechanical failures
- Crowd sentiment

Increase telemetry and create additional insights.

Measure fan engagement with new predictions.

Enhance global availability and quality of the broadcasts.

Increase the number of concurrent viewers.

Minimize operational complexity.

Ensure compliance with regulations.

Create a merchandising revenue stream.

**Technical requirements -**

Maintain or increase prediction throughput and accuracy.

Reduce viewer latency.

Increase transcoding performance.

Create real-time analytics of viewer consumption patterns and engagement.

Create a data mart to enable processing of large volumes of race data.

**Executive statement -**

Our CEO, S. Hawke, wants to bring high-adrenaline racing to fans all around the world. We listen to our fans, and they want enhanced video streams that include predictions of events within the race (e.g., overtaking). Our current platform allows us to predict race outcomes but lacks the facility to support real-time predictions during races and the capacity to process season-long results.

**Question**

In reference to the Helicopter Racing League (HRL) case study, HRL seeks a cost-effective approach for storing their race data, including telemetry. They aim to retain all historical records, train models solely using the previous season's data, and anticipate data growth in terms of volume and collected information. Given HRL's business requirements and the objectives articulated by CEO S. Hawke, what data solution should be proposed?

- A. Implement Firestore for its scalable and flexible document-based database. Utilize collections to aggregate race data by season and event.
- B. Employ Cloud Spanner for its scalability and capability to version schemas seamlessly with zero downtime. Distribute race data using season as a primary key.
- C. Utilize BigQuery for its scalability and ability to incorporate columns into a schema. Partition race data based on season.
- D. Opt for Cloud SQL for its automatic management of storage expansions and compatibility with MySQL. Utilize separate database instances for each season.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Utilize BigQuery for its scalability and ability to incorporate columns into a schema. Partition race data based on season.

Here's the breakdown of why the best choice for this scenario is

**C. Utilize BigQuery for its scalability and ability to incorporate columns into a schema. Partition race data based on season.**

**Reasons for Choosing BigQuery:**

- **Cost-Effective for Historical Storage:** BigQuery's pricing model is based on the amount of data stored and queried. It's ideal for large datasets (historical records) that are infrequently updated but analyzed in bulk (training on previous season's data).
- **Scalability for Growth:** BigQuery is designed to handle massive datasets, scaling seamlessly to accommodate anticipated growth in the volume and complexity of race data.
- **Schema Evolution:** As new types of telemetry data are collected, BigQuery's flexible schema allows for adding new columns without disrupting existing data, supporting future changes.
- **Season-Based Partitioning:** Partitioning race data by season optimizes query performance, making it efficient to train models only on the relevant past season's data.

**Why Other Options Are Less Optimal:**

- **A. Firestore:** While Firestore is scalable and flexible, its pricing model is usually better suited for high read/write frequency use cases. HRL's data is likely write-once, read-infrequently for training purposes.
- **B. Cloud Spanner:** Cloud Spanner is optimized for transactional workloads and strong consistency. The cost model and complexity make it less suitable for the volume of primarily analytical data in the HRL scenario.
- **D. Cloud SQL:** Cloud SQL is a great option for traditional relational database needs, but BigQuery's columnar storage, pricing model, and scaling advantages make it better for this specific data scenario.

**Key Points for HRL:**

- **Query Optimization:** Using partitioning and appropriate querying techniques will be critical for efficiently analyzing large amounts of data in BigQuery.
- **Storage Classes:** Explore BigQuery's long-term storage options to reduce costs for older data not immediately needed for model training.

References:

[https://cloud.google.com/blog/products/gcp/architecting-live-ncaa-predictions-from-archives-to-insights](https://cloud.google.com/blog/products/gcp/architecting-live-ncaa-predictions-from-archives-to-insights)

</details>

---

### Exam 4 · Q26

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

**Introductory Info**

**Company Overview -**

Mountkirk Games makes online, session-based, multiplayer games for the most popular mobile platforms. They build all of their games using some server-side integration. Historically, they have used cloud providers to lease physical servers.

Due to the unexpected popularity of some of their games, they have had problems scaling their global audience, application servers MySQL databases, and analytics tools.

Their current model is to write game statistics to files and send them through an ETL tool that loads them into a centralized MySQL database for reporting.

**Solution Concept -**

Mountkirk Games is building a new game, which they expect to be very popular. They plan to deploy the game's backend on Google Compute Engine so they can capture streaming metrics run intensive analytics, and take advantage of its autoscaling server environment and integrate with a managed NoSQL database.

**Business Requirements -**

- Increase to a global footprint
- Improve uptime, downtime is loss of players
- Increase efficiency of the cloud resources we use
- Reduce latency to all customers

**Technical Requirements -**

Requirements for Game Backend Platform:

- 1. Dynamically scale up or down based on game activity
- 2. Connect to a managed NoSQL database service
- 3. Run customize Linux distro

Requirements for Game Analytics Platform:

- 1. Dynamically scale up or down based on game activity
- 2. Process incoming data on the fly directly from the game servers
- 3. Process data that arrives late because of slow mobile networks
- 4. Allow SQL queries to access at least 10 TB of historical data
- 5. Process files that are regularly uploaded by users' mobile devices
- 6. Use only fully managed services

**CEO Statement -**

Our last successful game did not scale well with our previous cloud provider, resulting in lower user adoption and affecting the game's reputation. Our investors want more key performance indicators (KPIs) to evaluate the speed and stability of the game, as well as other metrics that provide deeper insight into usage patterns so we can adapt the game to target users.

**CTO Statement -**

Our current technology stack cannot provide the scale we need, so we want to replace MySQL and move to an environment that provides autoscaling, low latency load balancing, and frees us up from managing physical servers.

**CFO Statement -**

We are not capturing enough user demographic data, usage metrics, and other KPIs. As a result, we do not engage the right users, we are not confident that our marketing is targeting the right users, and we are not selling enough premium Blast-Ups inside the games, which dramatically impacts our revenue.

**Question**

**Mountkirk Games intends to establish a continuous delivery pipeline for their architecture, which comprises numerous small services requiring quick updates and rollbacks. The company has specific requirements:**

- Services must be redundantly deployed across multiple regions in the US and Europe.
- Only frontend services are publicly accessible on the internet.
- A single frontend IP address should be provided for their service fleet.
- Deployment artifacts must be immutable.

**Which set of products should they use to meet these requirements?**

- A. Google Cloud Storage, Google Cloud Dataflow, Google Compute Engine
- B. Google Cloud Storage, Google App Engine, Google Network Load Balancer
- C. Google Kubernetes Registry, Google Kubernetes Engine, Google HTTP(S) Load Balancer
- D. Google Cloud Functions, Google Cloud Pub/Sub, Google Cloud Deployment Manager

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Google Kubernetes Registry, Google Kubernetes Engine, Google HTTP(S) Load Balancer

The best choice for Mountkirk Games is

**C. Google Kubernetes Registry, Google Kubernetes Engine, Google HTTP(S) Load Balancer**. Here's a breakdown of why this combination aligns with their requirements and why other options are less suitable:

**Why Option C is Ideal**

- **Containerization and Microservices:** Google Kubernetes Engine (GKE) is designed for managing containerized applications, making it perfect for Mountkirk Games' architecture of small services. Google Kubernetes Registry provides secure, private storage for their container images.
- **Multi-Region Redundancy:** GKE supports multi-regional clusters for high availability. This fulfills the requirement for redundant deployment across the US and Europe.
- **Single Frontend IP:** Google HTTP(S) Load Balancer offers a single, global IP address for their frontend services while intelligently distributing traffic across multiple regions.
- **Immutable Artifacts:** Container images are inherently immutable, ensuring consistent deployment artifacts and easy rollbacks if needed.

**Why Other Options Don't Fit As Well**

- **A. Google Cloud Storage, Google Cloud Dataflow, Google Compute Engine**
  - Cloud Storage is purely for object storage.
  - Dataflow is focused on data processing pipelines.
  - While Compute Engine can run containers, the management overhead for small, frequently updated services would be higher than GKE's purpose-built solution.
- **B. Google Cloud Storage, Google App Engine, Google Network Load Balancer**
  - App Engine is better suited to monolithic or less-scalable applications, not as ideal for many small services.
  - Network Load Balancer lacks the advanced traffic management features of HTTP(S) Load Balancer for multi-region distribution.
- **D. Google Cloud Functions, Google Cloud Pub/Sub, Google Cloud Deployment Manager**
  - Cloud Functions is great for event-driven or serverless workloads, but not for consistently running frontend services.
  - Pub/Sub is a messaging service not focused on service deployment.
  - Deployment Manager is for infrastructure automation, but lacks GKE's container-specific deployment and traffic management capabilities.

**⚠️ Note:** "Google Kubernetes Registry" means Container Registry, which has been replaced by **Artifact Registry**.

</details>

---

### Exam 4 · Q29

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

**Introductory Info**

**Company Overview -**

Mountkirk Games makes online, session-based, multiplayer games for the most popular mobile platforms. They build all of their games using some server-side integration. Historically, they have used cloud providers to lease physical servers.

Due to the unexpected popularity of some of their games, they have had problems scaling their global audience, application servers MySQL databases, and analytics tools.

Their current model is to write game statistics to files and send them through an ETL tool that loads them into a centralized MySQL database for reporting.

**Solution Concept -**

Mountkirk Games is building a new game, which they expect to be very popular. They plan to deploy the game's backend on Google Compute Engine so they can capture streaming metrics run intensive analytics, and take advantage of its autoscaling server environment and integrate with a managed NoSQL database.

**Business Requirements -**

- Increase to a global footprint
- Improve uptime, downtime is loss of players
- Increase efficiency of the cloud resources we use
- Reduce latency to all customers

**Technical Requirements -**

Requirements for Game Backend Platform:

- 1. Dynamically scale up or down based on game activity
- 2. Connect to a managed NoSQL database service
- 3. Run customize Linux distro

Requirements for Game Analytics Platform:

- 1. Dynamically scale up or down based on game activity
- 2. Process incoming data on the fly directly from the game servers
- 3. Process data that arrives late because of slow mobile networks
- 4. Allow SQL queries to access at least 10 TB of historical data
- 5. Process files that are regularly uploaded by users' mobile devices
- 6. Use only fully managed services

**CEO Statement -**

Our last successful game did not scale well with our previous cloud provider, resulting in lower user adoption and affecting the game's reputation. Our investors want more key performance indicators (KPIs) to evaluate the speed and stability of the game, as well as other metrics that provide deeper insight into usage patterns so we can adapt the game to target users.

**CTO Statement -**

Our current technology stack cannot provide the scale we need, so we want to replace MySQL and move to an environment that provides autoscaling, low latency load balancing, and frees us up from managing physical servers.

**CFO Statement -**

We are not capturing enough user demographic data, usage metrics, and other KPIs. As a result, we do not engage the right users, we are not confident that our marketing is targeting the right users, and we are not selling enough premium Blast-Ups inside the games, which dramatically impacts our revenue.

**Question**

**Mountkirk Games intends to establish a real-time analytics platform for their latest game, ensuring it meets their technical requirements. Which combination of Google technologies will satisfy all of their requirements?**

- A. Kubernetes Engine, Cloud Pub/Sub, and Cloud SQL
- B. Cloud Dataflow, Cloud Storage, Cloud Pub/Sub, and BigQuery
- C. Cloud SQL, Cloud Storage, Cloud Pub/Sub, and Cloud Dataflow
- D. Cloud Dataproc, Cloud Pub/Sub, Cloud SQL, and Cloud Dataflow
- E. Cloud Pub/Sub, Compute Engine, Cloud Storage, and Cloud Dataproc

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Cloud Dataflow, Cloud Storage, Cloud Pub/Sub, and BigQuery

The best combination of Google technologies for Mountkirk Games' real-time analytics platform is

**B. Cloud Dataflow, Cloud Storage, Cloud Pub/Sub, and BigQuery.**

Here's why this combination closely aligns with their requirements:

- **Real-time Event Ingestion:** Cloud Pub/Sub is a scalable, globally-distributed messaging service ideal for receiving high volumes of game event data in real-time.
- **Stream Processing:** Cloud Dataflow provides a fully-managed service for building, executing, and monitoring complex streaming data pipelines, enabling real-time analysis and transformation of in-flight data.
- **Storage:** Cloud Storage offers durable, highly available storage for raw event data (for replay or historical analysis) and potentially intermediate results from data processing.
- **Analytics:** BigQuery is a serverless, petabyte-scale data warehouse designed for lightning-fast analytics, empowering interactive exploration of real-time data and historical trends.

**Why Other Options Are Less Suitable:**

- **A. Kubernetes Engine, Cloud Pub/Sub, and Cloud SQL:**
  - Kubernetes Engine is primarily for container orchestration. While it could be part of the architecture, it doesn't directly address the need for stream processing or analytics.
  - Cloud SQL is for relational databases, not as well-suited for high-volume, real-time analytics.
- **C. Cloud SQL, Cloud Storage, Cloud Pub/Sub, and Cloud Dataflow:** Same limitations as option A with Cloud SQL.
- **D. Cloud Dataproc, Cloud Pub/Sub, Cloud SQL, and Cloud Dataflow:**
  - Cloud Dataproc is focused on Hadoop and Spark clusters, which might be overkill if the primary need is real-time analytics, rather than large-scale batch processing.
- **E. Cloud Pub/Sub, Compute Engine, Cloud Storage, and Cloud Dataproc:**
  - Using Compute Engine requires more management overhead than using Cloud Dataflow for stream processing.

</details>

---

### Exam 4 · Q30

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

**Introductory Info**

**Company Overview -**

Mountkirk Games makes online, session-based, multiplayer games for mobile platforms. They build all of their games using some server-side integration. Historically, they have used cloud providers to lease physical servers. Due to the unexpected popularity of some of their games, they have had problems scaling their global audience, application servers, MySQL databases, and analytics tools.

Their current model is to write game statistics to files and send them through an ETL tool that loads them into a centralized MySQL database for reporting.

**Solution Concept -**

Mountkirk Games is building a new game, which they expect to be very popular. They plan to deploy the game's backend on Google Compute Engine so they can capture streaming metrics, run intensive analytics, and take advantage of its autoscaling server environment and integrate with a managed NoSQL database.

**Business Requirements -**

- Increase to a global footprint
- Improve uptime downtime is loss of players
- Increase efficiency of the cloud resources we use
- Reduce latency to all customers

**Technical Requirements -**

Requirements for Game Backend Platform

- Dynamically scale up or down based on game activity
- Connect to a transactional database service to manage user profiles and game state
- Store game activity in a timeseries database service for future analysis
- As the system scales, ensure that data is not lost due to processing backlogs
- Run hardened Linux distro

Requirements for Game Analytics Platform

- Dynamically scale up or down based on game activity
- Process incoming data on the fly directly from the game servers
- Process data that arrives late because of slow mobile networks
- Allow queries to access at least 10 TB of historical data
- Process files that are regularly uploaded by users' mobile devices

**Executive Statement -**

Our last successful game did not scale well with our previous cloud provider, resulting in lower user adoption and affecting the game's reputation. Our investors want more key performance indicators (KPIs) to evaluate the speed and stability of the game, as well as other metrics that provide deeper insight into usage patterns so we can adapt the game to target users. Additionally, our current technology stack cannot provide the scale we need, so we want to replace MySQL and move to an environment that provides autoscaling, low latency load balancing, and frees us up from managing physical servers.

**Question**

**In the context of the Mountkirk Games case study, which two steps should be included in their migration plan to transition to a model on Google Cloud Platform that aligns with their technical requirements? (Choose two.)**

- A. Evaluate the impact of migrating their current batch ETL code to Cloud Dataflow.
- B. Develop a schema migration plan to denormalize data for improved performance in BigQuery.
- C. Design an architecture diagram illustrating the transition from a single MySQL database to a MySQL cluster.
- D. Transfer 10 TB of analytics data from a previous game into a Cloud SQL instance and execute test queries against the full dataset to ensure successful completion.
- E. Implement Cloud Armor to safeguard against potential SQL injection attacks in analytics files uploaded to Cloud Storage.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Evaluate the impact of migrating their current batch ETL code to Cloud Dataflow. **|** B. Develop a schema migration plan to denormalize data for improved performance in BigQuery.

Here's the breakdown of why options A and B are the best steps to include in Mountkirk Games' migration plan and why the others aren't as crucial:

**A. Evaluate the impact of migrating their current batch ETL code to Cloud Dataflow.**

- **Focus on Real-Time:** A key requirement is moving to real-time analytics. Cloud Dataflow's strength is stream processing, making it vital to assess the feasibility and impact of adapting existing batch ETL processes to a real-time model.

**B. Develop a schema migration plan to denormalize data for improved performance in BigQuery.**

- **BigQuery Optimization:** BigQuery excels with denormalized data structures. Proactively planning this migration ensures they leverage BigQuery's performance advantages from the start.

**Why Other Options Are Less Critical**

- **C. Design an architecture diagram illustrating the transition from a single MySQL database to a MySQL cluster.** While clustering might be beneficial, it's not directly tied to their core requirement of real-time analytics. Real-time capabilities likely involve new components, not just MySQL optimization.
- **D. Transfer 10 TB of analytics data from a previous game into a Cloud SQL instance and execute test queries against the full dataset to ensure successful completion.** This focuses on legacy data in Cloud SQL, less relevant for the new real-time platform. It could be a later phase of migration, but not a priority for the initial transition.
- **E. Implement Cloud Armor to safeguard against potential SQL injection attacks in analytics files uploaded to Cloud Storage.** Security is vital, but this protects less relevant static files. Immediate focus should be on securing the real-time data ingestion and processing pipeline.

**Important Note:** The best answers depend on the specific technical requirements mentioned in the full Mountkirk Games case study. If the requirements include aspects like data retention, security of historical data, or MySQL cluster integration, then options C, D, and E might become more important.

References:

[https://cloud.google.com/bigquery/docs/loading-data#loading_denormalized_nested_and_repeated_datahttps://cloud.google.com/solutions/bigquery-data-warehouse#managing_data](https://cloud.google.com/bigquery/docs/loading-data#loading_denormalized_nested_and_repeated_data  https://cloud.google.com/solutions/bigquery-data-warehouse#managing_data)

</details>

---

### Exam 4 · Q31

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

**Introductory Info**

**Company Overview -**

Mountkirk Games makes online, session-based, multiplayer games for mobile platforms. They build all of their games using some server-side integration. Historically, they have used cloud providers to lease physical servers. Due to the unexpected popularity of some of their games, they have had problems scaling their global audience, application servers, MySQL databases, and analytics tools.

Their current model is to write game statistics to files and send them through an ETL tool that loads them into a centralized MySQL database for reporting.

**Solution Concept -**

Mountkirk Games is building a new game, which they expect to be very popular. They plan to deploy the game's backend on Google Compute Engine so they can capture streaming metrics, run intensive analytics, and take advantage of its autoscaling server environment and integrate with a managed NoSQL database.

**Business Requirements -**

- Increase to a global footprint
- Improve uptime downtime is loss of players
- Increase efficiency of the cloud resources we use
- Reduce latency to all customers

**Technical Requirements -**

Requirements for Game Backend Platform

- Dynamically scale up or down based on game activity
- Connect to a transactional database service to manage user profiles and game state
- Store game activity in a timeseries database service for future analysis
- As the system scales, ensure that data is not lost due to processing backlogs
- Run hardened Linux distro

Requirements for Game Analytics Platform

- Dynamically scale up or down based on game activity
- Process incoming data on the fly directly from the game servers
- Process data that arrives late because of slow mobile networks
- Allow queries to access at least 10 TB of historical data
- Process files that are regularly uploaded by users' mobile devices

**Executive Statement -**

Our last successful game did not scale well with our previous cloud provider, resulting in lower user adoption and affecting the game's reputation. Our investors want more key performance indicators (KPIs) to evaluate the speed and stability of the game, as well as other metrics that provide deeper insight into usage patterns so we can adapt the game to target users. Additionally, our current technology stack cannot provide the scale we need, so we want to replace MySQL and move to an environment that provides autoscaling, low latency load balancing, and frees us up from managing physical servers.

**Question**

**Considering the business and technical requirements of Mountkirk Games, what approach should you take to analyze and define the technical architecture for the compute workloads?**

- A. Implement network load balancers and utilize preemptible Compute Engine instances.
- B. Implement network load balancers and utilize non-preemptible Compute Engine instances.
- C. Deploy a global load balancer with managed instance groups and autoscaling policies, utilizing preemptible Compute Engine instances.
- D. Deploy a global load balancer with managed instance groups and autoscaling policies, utilizing non-preemptible Compute Engine instances.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Deploy a global load balancer with managed instance groups and autoscaling policies, utilizing non-preemptible Compute Engine instances.

**Option D (Deploy a global load balancer with managed instance groups and autoscaling policies, utilizing non-preemptible Compute Engine instances)**

as the best approach. Here's a deeper explanation of why:

**Why Option D Excels**

- **Global Availability and Low Latency:** Mountkirk Games likely has a global user base. A global load balancer ensures users are routed to the closest available region, minimizing latency and improving their experience.
- **Reliability and Uptime:** Non-preemptible Compute Engine instances guarantee availability, crucial for core game-related workloads where any disruption directly impacts players.
- **Scalability for Peak Demand:** Managed instance groups with autoscaling dynamically adjust the number of instances based on traffic, ensuring the system can handle sudden spikes in player activity.
- **High-Performance Architecture:** This combination of technologies is geared towards delivering a robust, reliable, and performant platform essential for supporting a popular online game.

**Why Other Options Fall Short:**

- **A. Implement network load balancers and utilize preemptible Compute Engine instances.** While cost-effective, preemptible instances are susceptible to interruption. This isn't ideal for core game workloads requiring high availability.
- **B. Implement network load balancers and utilize non-preemptible Compute Engine instances.** This lacks the global reach of a global load balancer, potentially affecting user experience in geographically distant regions.
- **C. Deploy a global load balancer with managed instance groups and autoscaling policies, utilizing preemptible Compute Engine instances.** The risk of preemption for core workloads outweighs the cost savings for this specific case.

**Important Considerations:**

- **Cost vs. Reliability Balance:** While Option D is the most reliable, it's also potentially the most expensive. A hybrid approach using a mix of non-preemptible and preemptible instances could be explored for specific background or less critical workloads.
- **Workload Analysis:** Carefully analyze which aspects of Mountkirk Games' compute workloads are truly disruption-sensitive and require non-preemptible instances.

**Key Takeaway:** Prioritizing reliability and global performance for mission-critical, user-facing game services makes Option D the best choice as a foundation. Strategic use of preemptible instances could still be incorporated for cost optimization where possible.

References:

[https://cloud.google.com/certification/guides/cloud-architect/casestudy-mountkirkgames-rev2](https://cloud.google.com/certification/guides/cloud-architect/casestudy-mountkirkgames-rev2)

</details>

---

### Exam 4 · Q32

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

**Introductory Info**

**Company Overview -**

Mountkirk Games makes online, session-based, multiplayer games for mobile platforms. They build all of their games using some server-side integration. Historically, they have used cloud providers to lease physical servers. Due to the unexpected popularity of some of their games, they have had problems scaling their global audience, application servers, MySQL databases, and analytics tools.

Their current model is to write game statistics to files and send them through an ETL tool that loads them into a centralized MySQL database for reporting.

**Solution Concept -**

Mountkirk Games is building a new game, which they expect to be very popular. They plan to deploy the game's backend on Google Compute Engine so they can capture streaming metrics, run intensive analytics, and take advantage of its autoscaling server environment and integrate with a managed NoSQL database.

**Business Requirements -**

- Increase to a global footprint
- Improve uptime downtime is loss of players
- Increase efficiency of the cloud resources we use
- Reduce latency to all customers

**Technical Requirements -**

Requirements for Game Backend Platform

- Dynamically scale up or down based on game activity
- Connect to a transactional database service to manage user profiles and game state
- Store game activity in a timeseries database service for future analysis
- As the system scales, ensure that data is not lost due to processing backlogs
- Run hardened Linux distro

Requirements for Game Analytics Platform

- Dynamically scale up or down based on game activity
- Process incoming data on the fly directly from the game servers
- Process data that arrives late because of slow mobile networks
- Allow queries to access at least 10 TB of historical data
- Process files that are regularly uploaded by users' mobile devices

**Executive Statement -**

Our last successful game did not scale well with our previous cloud provider, resulting in lower user adoption and affecting the game's reputation. Our investors want more key performance indicators (KPIs) to evaluate the speed and stability of the game, as well as other metrics that provide deeper insight into usage patterns so we can adapt the game to target users. Additionally, our current technology stack cannot provide the scale we need, so we want to replace MySQL and move to an environment that provides autoscaling, low latency load balancing, and frees us up from managing physical servers.

**Question**

**Considering the Mountkirk Games case study, which two steps should they take to design their solution for the future and leverage cloud and technology improvements as they become available? (Choose two.)**

- A. Store as much analytics and game activity data as financially feasible today to utilize for training machine learning models to predict user behavior in the future.
- B. Begin packaging their game backend artifacts in container images and deploying them on Google Kubernetes Engine to enhance scalability based on game activity.
- C. Establish a CI/CD pipeline using Jenkins and Spinnaker to automate canary deployments and enhance development velocity.
- D. Implement a schema versioning tool to minimize downtime when introducing new game features that require storing additional player data in the database.
- E. Implement a weekly rolling maintenance process for the Linux virtual machines to apply critical kernel patches and package updates, mitigating the risk of 0-day vulnerabilities.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Store as much analytics and game activity data as financially feasible today to utilize for training machine learning models to predict user behavior in the future. **|** B. Begin packaging their game backend artifacts in container images and deploying them on Google Kubernetes Engine to enhance scalability based on game activity.

The best two steps Mountkirk Games should take to future-proof their solution are:

- **A. Store as much analytics and game activity data as financially feasible today to utilize for training machine learning models to predict user behavior in the future.** Gathering large amounts of data lays the foundation for future machine learning initiatives, which could drive significant improvements in player engagement and personalization.
- **B. Begin packaging their game backend artifacts in container images and deploying them on Google Kubernetes Engine to enhance scalability based on game activity.** Adopting containers and Kubernetes positions them to embrace modern, scalable architectures. This allows them to respond to dynamic player demand more effectively.

Let's analyze why these options take priority and where others fall slightly short:

**Why the Other Options Are Less Ideal**

- **C. Establish a CI/CD pipeline using Jenkins and Spinnaker to automate canary deployments and enhance development velocity.** While CI/CD is essential, it addresses a different kind of "future-proofing" related to development practices. Options A and B relate more to positioning them to leverage future advancements in data analytics and scalable architecture.
- **D. Implement a schema versioning tool to minimize downtime when introducing new game features that require storing additional player data in the database.** This is good practice but focuses on a narrower aspect of future development flexibility, not as broadly impactful as data collection for ML or scalable architecture foundations.
- **E. Implement a weekly rolling maintenance process for the Linux virtual machines to apply critical kernel patches and package updates, mitigating the risk of 0-day vulnerabilities.** Security is vital, but this is more about ongoing operational maintenance, not directly positioning them to better leverage future cloud technologies or capabilities.

**Important Considerations:**

- **Cost-Benefit of Data Storage:** Balance data collection's value with the storage costs on Google Cloud. Define clear use cases for that data to justify the investment.
- **Learning Curve:** Adopting containers and Kubernetes often has a learning curve. Plan for skill development and potentially external assistance with the transition.

</details>

---

### Exam 4 · Q34

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

**Introductory Info**

**Company Overview -**

Mountkirk Games makes online, session-based, multiplayer games for mobile platforms. They build all of their games using some server-side integration. Historically, they have used cloud providers to lease physical servers. Due to the unexpected popularity of some of their games, they have had problems scaling their global audience, application servers, MySQL databases, and analytics tools.

Their current model is to write game statistics to files and send them through an ETL tool that loads them into a centralized MySQL database for reporting.

**Solution Concept -**

Mountkirk Games is building a new game, which they expect to be very popular. They plan to deploy the game's backend on Google Compute Engine so they can capture streaming metrics, run intensive analytics, and take advantage of its autoscaling server environment and integrate with a managed NoSQL database.

**Business Requirements -**

- Increase to a global footprint
- Improve uptime downtime is loss of players
- Increase efficiency of the cloud resources we use
- Reduce latency to all customers

**Technical Requirements -**

Requirements for Game Backend Platform

- Dynamically scale up or down based on game activity
- Connect to a transactional database service to manage user profiles and game state
- Store game activity in a timeseries database service for future analysis
- As the system scales, ensure that data is not lost due to processing backlogs
- Run hardened Linux distro

Requirements for Game Analytics Platform

- Dynamically scale up or down based on game activity
- Process incoming data on the fly directly from the game servers
- Process data that arrives late because of slow mobile networks
- Allow queries to access at least 10 TB of historical data
- Process files that are regularly uploaded by users' mobile devices

**Executive Statement -**

Our last successful game did not scale well with our previous cloud provider, resulting in lower user adoption and affecting the game's reputation. Our investors want more key performance indicators (KPIs) to evaluate the speed and stability of the game, as well as other metrics that provide deeper insight into usage patterns so we can adapt the game to target users. Additionally, our current technology stack cannot provide the scale we need, so we want to replace MySQL and move to an environment that provides autoscaling, low latency load balancing, and frees us up from managing physical servers.

**Question**

**Considering the business and technical requirements of Mountkirk Games, how should you analyze and define the technical architecture for the database workloads?**

- A. Utilize Cloud SQL for time series data and employ Cloud Bigtable for historical data queries.
- B. Transition to Cloud SQL to replace MySQL and implement Cloud Spanner for historical data queries.
- C. Replace MySQL with Cloud Bigtable and utilize BigQuery for historical data queries.
- D. Implement Cloud Bigtable for time series data, utilize Cloud Spanner for transactional data, and employ BigQuery for historical data queries.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Implement Cloud Bigtable for time series data, utilize Cloud Spanner for transactional data, and employ BigQuery for historical data queries.

The best option here is likely

**D. Implement Cloud Bigtable for time series data, utilize Cloud Spanner for transactional data, and employ BigQuery for historical data queries.** Let's break down why this combination aligns with Mountkirk Games' requirements and potential use cases:

**Why Option D Excels:**

- **Specialized Databases:** This architecture leverages the strengths of each Google Cloud database service to match specific workload types:
  - **Cloud Bigtable:** Ideal for high-volume time-series data typical of game analytics (player actions, metrics, etc.). It offers low latency and high throughput for real-time ingestion and analysis.
  - **Cloud Spanner:** A strongly consistent, distributed relational database well-suited for transactional data that requires ACID properties (like in-game purchases, player profiles, etc.).
  - **BigQuery:** A powerful data warehouse designed for fast analytical queries on massive datasets. It can aggregate and analyze historical data for insights, trends, and reporting.
- **Scalability:** Google Cloud databases are designed to seamlessly scale to meet the demands of a popular game.
- **Future-Proofing:** This architecture aligns with modern, cloud-native architecture patterns and allows Mountkirk Games to leverage the latest database technologies.

**Why Other Options Are Less Ideal:**

- **A. Utilize Cloud SQL for time series data and employ Cloud Bigtable for historical data queries.** Cloud SQL (MySQL-compatible) is less performant for high-volume, fast writes typical of time series data. Cloud Bigtable is a better fit for that workload.
- **B. Transition to Cloud SQL to replace MySQL and implement Cloud Spanner for historical data queries.** While this improves scalability and consistency compared to standalone MySQL, it misses the opportunity to leverage the power of BigQuery for historical analytics workloads.
- **C. Replace MySQL with Cloud Bigtable and utilize BigQuery for historical data queries.** This could work for some scenarios, but Cloud Bigtable is less suited for transactional data that requires strong consistency. Cloud Spanner is a better choice for that use case.

**Important Considerations**

- **Migration Complexity:** Transitioning to multiple databases will require careful planning and execution. Consider a phased approach if possible.
- **Database Compatibility:** If existing MySQL schemas are complex, refactoring them for Cloud Bigtable or Cloud Spanner could be significant.
- **Workload Specifics:** The best architecture depends on the exact nature of their transactional data vs. time series data.

References:

[https://cloud.google.com/architecture/best-practices-cloud-spanner-gaming-database](https://cloud.google.com/architecture/best-practices-cloud-spanner-gaming-database)

</details>

---

### Exam 4 · Q35

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

**Introductory Info**

**Company Overview -**

Mountkirk Games makes online, session-based, multiplayer games for mobile platforms. They build all of their games using some server-side integration. Historically, they have used cloud providers to lease physical servers. Due to the unexpected popularity of some of their games, they have had problems scaling their global audience, application servers, MySQL databases, and analytics tools.

Their current model is to write game statistics to files and send them through an ETL tool that loads them into a centralized MySQL database for reporting.

**Solution Concept -**

Mountkirk Games is building a new game, which they expect to be very popular. They plan to deploy the game's backend on Google Compute Engine so they can capture streaming metrics, run intensive analytics, and take advantage of its autoscaling server environment and integrate with a managed NoSQL database.

**Business Requirements -**

- Increase to a global footprint
- Improve uptime downtime is loss of players
- Increase efficiency of the cloud resources we use
- Reduce latency to all customers

**Technical Requirements -**

Requirements for Game Backend Platform

- Dynamically scale up or down based on game activity
- Connect to a transactional database service to manage user profiles and game state
- Store game activity in a timeseries database service for future analysis
- As the system scales, ensure that data is not lost due to processing backlogs
- Run hardened Linux distro

Requirements for Game Analytics Platform

- Dynamically scale up or down based on game activity
- Process incoming data on the fly directly from the game servers
- Process data that arrives late because of slow mobile networks
- Allow queries to access at least 10 TB of historical data
- Process files that are regularly uploaded by users' mobile devices

**Executive Statement -**

Our last successful game did not scale well with our previous cloud provider, resulting in lower user adoption and affecting the game's reputation. Our investors want more key performance indicators (KPIs) to evaluate the speed and stability of the game, as well as other metrics that provide deeper insight into usage patterns so we can adapt the game to target users. Additionally, our current technology stack cannot provide the scale we need, so we want to replace MySQL and move to an environment that provides autoscaling, low latency load balancing, and frees us up from managing physical servers.

**Question**

**In the context of the Mountkirk Games case study, which managed storage option aligns with Mountkirk's technical requirement for storing game activity in a time series database service?**

- A. Cloud Bigtable
- B. Cloud Spanner
- C. BigQuery
- D. Cloud Datastore

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Cloud Bigtable

The correct answer is **A. Cloud Bigtable**.

Here's why it's the perfect fit for Mountkirk Games' requirement:

**Why Cloud Bigtable is Ideal for Time Series Data**

- **Data Structure:** Cloud Bigtable is designed specifically for storing and managing massive amounts of time-series data. Its columnar structure and row key indexing make it efficient for querying based on time ranges.
- **High Throughput:** Cloud Bigtable excels at handling high-volume data writes with low latency, essential for capturing real-time game activity.
- **Scalability:** It easily scales to handle the potentially vast amounts of game activity data generated by a popular game.
- **Integration with Analytics Tools:** Cloud Bigtable often integrates seamlessly with BigQuery and other analytics tools, enabling Mountkirk Games to perform historical analysis or build visualizations on their game activity data.

**Why Other Options Are Less Suitable**

- **B. Cloud Spanner:** Cloud Spanner is a globally distributed, strongly consistent relational database. While powerful, its primary focus isn't the high-volume, fast write patterns of time-series data.
- **C. BigQuery:** BigQuery is a serverless data warehouse optimized for analytical queries over large datasets. It's great for analysis but isn't the best choice for storing the raw, continuously generated game activity data.
- **D. Cloud Datastore:** Cloud Datastore is a NoSQL document database suited for storing semi-structured data. It's less optimized for the specific structure and access patterns of time-series data compared to Cloud Bigtable.

**References:**

[https://cloud.google.com/bigtable/docs/schema-design-time-series](https://cloud.google.com/bigtable/docs/schema-design-time-series)

</details>

---

### Exam 4 · Q36

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

**Introductory Info**

**Company Overview -**

Mountkirk Games makes online, session-based, multiplayer games for mobile platforms. They build all of their games using some server-side integration. Historically, they have used cloud providers to lease physical servers. Due to the unexpected popularity of some of their games, they have had problems scaling their global audience, application servers, MySQL databases, and analytics tools.

Their current model is to write game statistics to files and send them through an ETL tool that loads them into a centralized MySQL database for reporting.

**Solution Concept -**

Mountkirk Games is building a new game, which they expect to be very popular. They plan to deploy the game's backend on Google Compute Engine so they can capture streaming metrics, run intensive analytics, and take advantage of its autoscaling server environment and integrate with a managed NoSQL database.

**Business Requirements -**

- Increase to a global footprint
- Improve uptime downtime is loss of players
- Increase efficiency of the cloud resources we use
- Reduce latency to all customers

**Technical Requirements -**

Requirements for Game Backend Platform

- Dynamically scale up or down based on game activity
- Connect to a transactional database service to manage user profiles and game state
- Store game activity in a timeseries database service for future analysis
- As the system scales, ensure that data is not lost due to processing backlogs
- Run hardened Linux distro

Requirements for Game Analytics Platform

- Dynamically scale up or down based on game activity
- Process incoming data on the fly directly from the game servers
- Process data that arrives late because of slow mobile networks
- Allow queries to access at least 10 TB of historical data
- Process files that are regularly uploaded by users' mobile devices

**Executive Statement -**

Our last successful game did not scale well with our previous cloud provider, resulting in lower user adoption and affecting the game's reputation. Our investors want more key performance indicators (KPIs) to evaluate the speed and stability of the game, as well as other metrics that provide deeper insight into usage patterns so we can adapt the game to target users. Additionally, our current technology stack cannot provide the scale we need, so we want to replace MySQL and move to an environment that provides autoscaling, low latency load balancing, and frees us up from managing physical servers.

**Question**

**Referring to the Mountkirk Games case study, you are responsible for designing the new Game Backend Platform architecture, which communicates with the game via a REST API. How should you design the backend to adhere to Google-recommended practices?**

- A. Create an instance template for the backend and deploy it on a multi-zone managed instance group for each region. Utilize an L4 load balancer.
- B. Develop an instance template for the backend and deploy it on a single-zone managed instance group for each region. Utilize an L4 load balancer.
- C. Establish an instance template for the backend and deploy it on a multi-zone managed instance group for each region. Utilize an L7 load balancer.
- D. Design an instance template for the backend and deploy it on a single-zone managed instance group for each region. Utilize an L7 load balancer.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Establish an instance template for the backend and deploy it on a multi-zone managed instance group for each region. Utilize an L7 load balancer.

Here's the breakdown of why option **C (Establish an instance template for the backend and deploy it on a multi-zone managed instance group for each region. Utilize an L7 load balancer)**

is the best design adhering to Google-recommended practices:

**Why Option C Excels**

- **Resiliency:** Multi-zone managed instance groups ensure instances are distributed across multiple zones within a region. This protects against localized failures and enhances availability.
- **Scalability:** Managed instance groups enable automatic scaling based on demand, handling traffic spikes without manual intervention.
- **HTTP(S) Traffic:** An L7 (HTTP/HTTPS) load balancer provides intelligent traffic distribution, content-based routing, and features like SSL termination, crucial for a REST API.
- **Google Best Practices:** This architecture aligns with Google's emphasis on reliability, scalability, and using the right load balancing type for the given traffic nature.

**Why Other Options Are Less Optimal**

- **A. Create an instance template for the backend and deploy it on a multi-zone managed instance group for each region. Utilize an L4 load balancer.** An L4 (TCP/UDP) load balancer lacks the content-aware features of an L7 load balancer, which are often useful for REST APIs (path-based routing, header inspection, etc.).
- **B. Develop an instance template for the backend and deploy it on a single-zone managed instance group for each region. Utilize an L4 load balancer.** This is less resilient than a multi-zone setup, as it's vulnerable to a zone-level outage.
- **D. Design an instance template for the backend and deploy it on a single-zone managed instance group for each region. Utilize an L7 load balancer.** Similar to option B, the lack of multi-zone deployment increases the risk of downtime due to zone-level failures.

**Important Considerations:**

- **Global Deployment:** If the game has a global player base, consider a global HTTP(S) load balancer for cross-region distribution and lower latency.
- **API Design:** Ensure the REST API is stateless and well-structured to leverage load balancing effectively.

References:

[https://cloud.google.com/solutions/gaming/cloud-game-infrastructure#dedicated_game_server](https://cloud.google.com/solutions/gaming/cloud-game-infrastructure#dedicated_game_server)

</details>

---

### Exam 4 · Q54

**A public health information website hosted in an on-premises EHR data center is experiencing slow response times, coupled with distributed denial-of-service attacks from specific IP address ranges. EHR management deems the website suitable for migration to Google Cloud due to its low risk. To address latency issues and prevent denial-of-service traffic, what steps should be taken?**

- A. Deploy an external HTTP(S) load balancer, set up VPC firewall rules, and migrate the applications to Compute Engine virtual machines.
- B. Deploy an external HTTP(S) load balancer, configure Google Cloud Armor, and migrate the application to Compute Engine virtual machines.
- C. Containerize the application and migrate it to Google Kubernetes Engine (GKE). Implement a GKE service for pod exposure within the cluster, and establish a GKE network policy.
- D. Containerize the application and migrate it to Google Kubernetes Engine (GKE). Employ an internal load balancer for pod exposure outside the cluster, and enable Identity-Aware Proxy (IAP) for access control.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Deploy an external HTTP(S) load balancer, configure Google Cloud Armor, and migrate the application to Compute Engine virtual machines.

The best choice amongst these options is **B**:

- **External HTTP(S) Load Balancer:** Distributes traffic across multiple VM instances, improving performance and resilience against traffic surges.
- **Google Cloud Armor:** Provides built-in DDoS protection and web application firewall (WAF) capabilities to filter out malicious traffic based on IP ranges and other attack signatures.
- **Compute Engine Virtual Machines:** A flexible and scalable infrastructure-as-a-service (IaaS) option suitable for migrating the existing web application.

**Here's why the other options are less optimal:**

- **A:** While this solution addresses some of the issues, it lacks specific defenses against the mentioned DDoS attacks.
- **C:** While GKE is great for containerized workloads, it might introduce unnecessary complexity for a simple web application migration focused on latency and DDoS protection.
- **D:** GKE's internal load balancer is for traffic within a cluster. IAP focuses on user authentication rather than DDoS mitigation.

**Important Considerations:**

- **Cloud Armor Configuration:** Careful configuration of Cloud Armor's WAF rules is needed to block specific DDoS attack patterns and mitigate the identified IP address ranges.
- **Monitoring:** Implement robust monitoring for both performance metrics and Cloud Armor logs to detect and respond to potential attacks.

[https://cloud.google.com/vpc/docs/firewalls](https://cloud.google.com/vpc/docs/firewalls)

[https://cloud.google.com/load-balancing/docs/tutorials/optimize-app-latency](https://cloud.google.com/load-balancing/docs/tutorials/optimize-app-latency)

[https://cloud.google.com/armor/docs/security-policy-concepts](https://cloud.google.com/armor/docs/security-policy-concepts)

[https://cloud.google.com/kubernetes-engine/docs/concepts/service](https://cloud.google.com/kubernetes-engine/docs/concepts/service)

[https://cloud.google.com/kubernetes-engine/docs/how-to/network-policy](https://cloud.google.com/kubernetes-engine/docs/how-to/network-policy)

[https://cloud.google.com/kubernetes-engine/docs/concepts/ingress-ilb](https://cloud.google.com/kubernetes-engine/docs/concepts/ingress-ilb)

[https://cloud.google.com/iap/docs/concepts-overview#when_to_use_iap](https://cloud.google.com/iap/docs/concepts-overview#when_to_use_iap)

</details>

---

### Exam 4 · Q62

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

For this question, refer to the Helicopter Racing League (HRL) case study.

https://services.google.com/fh/files/blogs/master_case_study_helicopter_racing_league.pdf

**HRL seeks assistance in introducing existing recorded video content to new audiences in emerging regions. How should you proceed, considering HRL's business and technical needs?**

- A. Deliver the video content directly from a multi-region Cloud Storage bucket.
- B. Employ Cloud CDN to cache the video content from HRL's current public cloud provider.
- C. Utilize Apigee Edge to cache the video content from HRL's existing public cloud provider.
- D. Replicate the video content in Google Kubernetes Engine clusters located near the target audience.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Employ Cloud CDN to cache the video content from HRL's current public cloud provider.

**B is correct because Cloud CDN can be used to cache data hosted on other cloud providers and supports large objects such as video.**

**Other options is Not correct:**

A is not correct because a multi-region bucket does not serve all global areas with similar latency.

C is not correct because Apigee Edge is not designed to cache data larger than 512 KB.

D is not correct because replicating the video content introduces unnecessary complexity.

References:

[https://cloud.google.com/storage/docs/locations#considerations](https://cloud.google.com/storage/docs/locations#considerations)

[https://cloud.google.com/cdn/docs/caching#maximum-size](https://cloud.google.com/cdn/docs/caching#maximum-size)

[https://cloud.google.com/cdn/docs/custom-origins-overview#hybrid_and_multi-cloud_architectures](https://cloud.google.com/cdn/docs/custom-origins-overview#hybrid_and_multi-cloud_architectures)

[https://docs.apigee.com/api-platform/antipatterns/caching-large](https://docs.apigee.com/api-platform/antipatterns/caching-large)

[https://cloud.google.com/solutions/building-a-multi-cluster-service-mesh-on-gke-using-replicated-control-plane-architecture](https://cloud.google.com/solutions/building-a-multi-cluster-service-mesh-on-gke-using-replicated-control-plane-architecture)

</details>

---

### Exam 4 · Q65

**Your company aims to monitor the presence of individuals in meeting rooms reserved for scheduled meetings. There are 1000 meeting rooms spread across 5 offices on 3 continents, each equipped with a motion sensor reporting its status every second. How should you design a solution to meet the data ingestion requirements of this sensor network, considering the possibility of inconsistent device connectivity?**

- A. Establish a persistent connection from each device to a Compute Engine instance and transmit messages to a custom application.
- B. Enable devices to check connectivity to Cloud SQL and periodically insert the latest messages into a device-specific table.
- C. Configure devices to verify connectivity to Pub/Sub and regularly publish the latest messages to a shared topic for all devices.
- D. Implement a persistent connection from devices to an App Engine application with Cloud Endpoints, which processes and stores messages in Datastore.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Configure devices to verify connectivity to Pub/Sub and regularly publish the latest messages to a shared topic for all devices.

**C. Configure devices to verify connectivity to Pub/Sub and regularly publish the latest messages to a shared topic for all devices.**

Here's why this approach is superior:

- **Scalability:** Pub/Sub is a managed messaging service designed to handle large volumes of data with high throughput. It can easily accommodate the 1000 rooms and their frequent sensor updates.
- **Decoupled Architecture:** Pub/Sub decouples data producers (sensors) from downstream processing, improving the system's resilience to connectivity issues and uneven data rates from different rooms.
- **Handling Connectivity Issues:** Pub/Sub's buffering and asynchronous nature tolerate inconsistent connectivity. Sensors can publish messages when connectivity is available, ensuring data isn't lost.
- **Global Reach:** Pub/Sub seamlessly operates across multiple continents, simplifying data ingestion from geographically distributed meeting rooms.

**Why Other Options are Less Optimal:**

- **A. Compute Engine Persistence:** Managing persistent connections from 1000 devices to a Compute Engine instance introduces scaling challenges and a higher risk of downtime if the instance fails.
- **B. Cloud SQL:** Cloud SQL is a database, not ideal for real-time message ingestion. Periodic inserts might cause delays in data analysis.
- **D. App Engine and Datastore:** While feasible, this approach requires more custom application logic for message handling and might not scale as gracefully as Pub/Sub.

**Additional Considerations:**

- **Downstream Processing:** Choose a suitable technology (e.g., Dataflow, Cloud Functions) to subscribe to the Pub/Sub topic for real-time or batch processing of the motion sensor data.
- **Data Retention:** Define clear data retention policies within Pub/Sub based on how long you need to store the sensor data.

References:

[https://cloud.google.com/sql/](https://cloud.google.com/sql/)

[https://cloud.google.com/pubsub/](https://cloud.google.com/pubsub/)

</details>

---

### Exam 4 · Q66

Your company runs a large-scale e-commerce application on Google Cloud, serving millions of global customers. The application consists of multiple microservices running on **Google Kubernetes Engine (GKE)** with an **Istio service mesh** for traffic management. The backend is powered by **Cloud Spanner** for transactional consistency, and **BigQuery** for analytics.

Recently, users in different regions have reported **inconsistent and stale data** when querying order details immediately after placing an order. You suspect this is due to eventual consistency issues.

**What is the MOST effective way to ensure strong consistency while maintaining high availability across multiple regions?**

- A) Configure **Cloud CDN** to cache database responses and reduce load on Cloud Spanner.
- B) Use **Cloud Spanner’s strong read** with **leader placement strategy** in the region closest to the majority of users.
- C) Replace **Cloud Spanner with Bigtable**, as Bigtable offers low-latency reads and writes across regions.
- D) Deploy **Memorystore (Redis) for caching**, ensuring all read operations hit the cache before going to Cloud Spanner.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B) Use **Cloud Spanner’s strong read** with **leader placement strategy** in the region closest to the majority of users.

**Answer – Option B: Configure Cloud Spanner clients to issue *strong reads* and set the database’s *default-leader region* to the region that serves most of your traffic.**

Why B solves the problem

• **Strong reads guarantee freshness.** A strong read in Cloud Spanner “is guaranteed to see all data that has been committed up until the start of the read,” eliminating the stale results your users are seeing. [Google Cloud](https://cloud.google.com/spanner/docs/reads?utm_source=chatgpt.com)

• **Leader placement keeps the latency low while preserving external consistency.** By moving the Paxos leader replicas to the primary-traffic region, both writes and strong reads avoid a cross-continent round-trip, yet Spanner continues to synchronously replicate across the other regions for 5-nines availability. [Google Cloud](https://cloud.google.com/blog/topics/developers-practitioners/reduce-latency-with-cloud-spanner-multi-region-leader-placement/?utm_source=chatgpt.com) | [Google Cloud](https://cloud.google.com/spanner/docs/replication?utm_source=chatgpt.com)

Why the other choices are not appropriate

**A – Cloud CDN**
Cloud CDN is designed for caching *static* or publicly cacheable HTTP content. Caching per-order database responses would either violate cacheability rules or require aggressive invalidations, adding the very staleness you are trying to remove. [Google Cloud](https://cloud.google.com/cdn/docs/caching?utm_source=chatgpt.com)

**C – Bigtable**
Cloud Bigtable replication trades strong consistency for very low latency; reads from clusters that did not process the write can be seconds (or longer) behind. Switching would re-introduce eventual consistency rather than fix it. [Google Cloud](https://cloud.google.com/bigtable/docs/replication-overview?utm_source=chatgpt.com)

**D – Memorystore (Redis)**
Memorystore is a single-region cache; any replicas you build yourself are asynchronous and provide no transactional guarantees. Reads served from Redis in one region could easily be stale relative to writes that were just committed in another. [Google Cloud](https://cloud.google.com/memorystore/docs/redis/regions?utm_source=chatgpt.com)

By continuing to use Cloud Spanner but enforcing strong reads and thoughtful leader placement, you keep global high availability while ensuring every customer sees their newly placed order immediately.

</details>

---

### Exam 5 · Q1

**Altostrat Media Case Study**

**Company Overview**

Altostrat is a prominent player in the media industry, with an extensive collection of audio and video content that comprises podcasts, interviews, news broadcasts, and documentaries. Their success in delivering premium content to a diverse audience requires a content management system that can keep pace with the dynamic media landscape.

**Solution Concept**

Altostrat seeks to modernize its content management and user engagement strategies using Google Cloud's generative AI. They want a platform that empowers customers with personalized recommendations, natural language interactions, and seamless self-service support. Simultaneously, they want to drive revenue growth through dynamic pricing, targeted marketing, and personalized product suggestions.

The seamless integration of AI-powered tools into their existing Google Cloud environment will enable Altostrat to efficiently manage their vast media library, enhance user experiences, and unlock new revenue streams. Google Cloud’s generative AI will solidify their leadership in the media industry.

**Existing Technical Environment**

Altostrat's content management and delivery platform leverages GKE for scalability and high availability, essential for handling their vast media library. Their extensive media library, spanning various documents, audio and video formats, is stored in Cloud Storage. To gain valuable insights into user behavior, content consumption patterns, and audience demographics, Altostrat leverages BigQuery as their primary data warehouse. Additionally, they use Cloud Run functions for serverless execution of event-driven tasks such as video transcoding, metadata extraction, and personalized content recommendations.

While Altostrat has made significant strides in cloud adoption, they also maintain some legacy on-premises systems for specific workflows like content ingestion and archival. These systems are slated for modernization and migration to Google Cloud in the near future. User management and authentication are currently handled through a combination of Google Identity and third-party identity providers. For monitoring and observability, Altostrat relies on a mix of native Google Cloud tools like Cloud Monitoring and open-source solutions like Prometheus, with alerts primarily delivered via email notifications.

**Business Requirements**

- Accelerate and enhance the reliability of operational workflows across all environments. [Google Cloud + On-premises]
- Simplify infrastructure management for rapid application deployment.
- Optimize cloud storage costs while maintaining high availability and scalability for media content.
- Enable natural language interaction with the platform with 24/7 user support.
- Automatically generate concise summaries of media content.
- Extract rich metadata from media assets using NLP and computer vision.
- Detect and filter inappropriate content.
- Analyze media content to identify trends and extract insights.
- Inform content strategy and decision-making with data.

**Technical Requirements**

- Modernize CI/CD for containerized deployments with a centralized management platform.
- Secure, high-performance hybrid cloud connectivity for data ingestion.
- Provide scalable, performant kubernetes environments both on-premises and in the cloud.
- Optimize cloud storage costs for growing media volumes.
- Design AI-powered detection of harmful content.
- Ensure that AI systems are auditable and their decisions can be explained
- Leverage LLMs and conversational AI for personalized experiences and content virality.
- Develop advanced chatbots with natural language understanding to provide

personalized assistance.

- Automated summarization for diverse media.

**Executive Statement**

At Altostrat, we are embracing the next frontier of artificial intelligence to revolutionize our content strategy. By harnessing the power of generative AI, we will create an unparalleled user experience by empowering our audience with intelligent tools for content discovery, personalized recommendations, and seamless interaction. Reliability and cost management are our top priorities. This strategic initiative will deepen engagement, foster customer loyalty, and unlock new revenue streams through targeted marketing and tailored content offerings. We see a future where AI-driven innovation is central to our business, leading to greater success for our company and delivering exceptional value to our customers.

---

**Question:**

**Altostrat Media wants to implement AI-driven detection and filtering of inappropriate audio and video content across its large and continuously growing media library stored in Cloud Storage. The solution must scale automatically, integrate with their existing GKE- and Cloud Run–based workflows, and ensure that AI decisions are auditable and explainable for regulatory review.**

**Which architecture should you recommend?**

- A. Use Cloud Functions triggered by Cloud Storage events to invoke Gemini APIs directly and store classification results as object metadata.
- B. Build a Vertex AI pipeline using pre-trained multimodal models for content analysis, store inference results in BigQuery, and expose explanations through Vertex AI Model Monitoring.
- C. Deploy custom TensorFlow models on GKE with GPUs, process content in batch jobs, and log decisions to Cloud Logging.
- D. Use BigQuery ML to analyze extracted metadata and flag inappropriate content using SQL-based classification.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Build a Vertex AI pipeline using pre-trained multimodal models for content analysis, store inference results in BigQuery, and expose explanations through Vertex AI Model Monitoring.

**Correct option: B**

Altostrat needs harmful-content detection on **audio + video** stored in **Cloud Storage**, with **automatic scaling**, clean integration into **GKE/Cloud Run workflows**, and **auditable + explainable** AI decisions for regulators. The case study explicitly calls out “Detect and filter inappropriate content” and “Ensure that AI systems are auditable and their decisions can be explained,” alongside their GKE/Cloud Run foundation. v6.1_pca_altostrat_media_case_s… v6.1_pca_altostrat_media_case_s…

**Why B fits best**

- **Scales and operationalizes content analysis**: Vertex AI Pipelines is designed to orchestrate repeatable ML workflows (batch or event-driven orchestration patterns), which aligns with a continuously growing library and workflow automation needs. [Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction)
- **Auditability**: Persisting inference outputs in **BigQuery** gives a queryable, durable audit trail (what was flagged, when, with what score/labels, and downstream actions).
- **Explainability**: Vertex AI supports **explanations** (feature-/example-based, depending on model type) to help justify decisions during reviews. [Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview)
  - Note: Option B mentions “Model Monitoring” for explanations; in practice, **Explainable AI** is the core feature for explanations, while Model Monitoring is primarily for tracking model/data quality over time. [Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/overview)
    Even with that wording imperfection, B is still the only option that directly addresses the **auditable + explainable** requirement at platform level.

**Why the other options are not best**

**A. Cloud Functions + direct Gemini calls + object metadata**

- Event-driven triggers are workable, but this pattern alone doesn’t meet the **regulatory-grade explainability/audit** requirement (object metadata is not a strong audit system of record, and “why” explanations aren’t inherently managed/governed). Cloud Run/Functions can be triggered from Storage events, but that only covers invocation, not end-to-end governance and explainability. [Google Cloud Documentation](https://docs.cloud.google.com/run/docs/triggering/storage-triggers)

**C. Custom TensorFlow on GKE + batch jobs + Cloud Logging**

- Technically possible, but it shifts you toward **heavy ops** (GPU capacity, model lifecycle, governance, pipeline management) and doesn’t inherently provide standardized **explanations** suitable for review. Logging alone is not the same as explainability or a structured audit dataset.

**D. BigQuery ML on extracted metadata**

- This can help with **metadata-based** flagging, but it does not directly perform robust **multimodal** content understanding (audio/video) by itself. It’s better as an analytics/secondary signal layer, not the primary “AI-driven detection and filtering” engine for the media itself.

**Key documentation (authoritative)**

- Vertex AI Pipelines overview: [Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction)
- Vertex Explainable AI overview: [Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview)

###### Explanation

**Why B fits best**

- **Scales and operationalizes content analysis**: Vertex AI Pipelines is designed to orchestrate repeatable ML workflows (batch or event-driven orchestration patterns), which aligns with a continuously growing library and workflow automation needs. [Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction)
- **Auditability**: Persisting inference outputs in **BigQuery** gives a queryable, durable audit trail (what was flagged, when, with what score/labels, and downstream actions).
- **Explainability**: Vertex AI supports **explanations** (feature-/example-based, depending on model type) to help justify decisions during reviews. [Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview)
  - Note: Option B mentions “Model Monitoring” for explanations; in practice, **Explainable AI** is the core feature for explanations, while Model Monitoring is primarily for tracking model/data quality over time. [Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/overview)
    Even with that wording imperfection, B is still the only option that directly addresses the **auditable + explainable** requirement at platform level.

> [!note]- Why the other options are wrong
> **A. Cloud Functions + direct Gemini calls + object metadata**
>
> - Event-driven triggers are workable, but this pattern alone doesn’t meet the **regulatory-grade explainability/audit** requirement (object metadata is not a strong audit system of record, and “why” explanations aren’t inherently managed/governed). Cloud Run/Functions can be triggered from Storage events, but that only covers invocation, not end-to-end governance and explainability. [Google Cloud Documentation](https://docs.cloud.google.com/run/docs/triggering/storage-triggers)
>
> **C. Custom TensorFlow on GKE + batch jobs + Cloud Logging**
>
> - Technically possible, but it shifts you toward **heavy ops** (GPU capacity, model lifecycle, governance, pipeline management) and doesn’t inherently provide standardized **explanations** suitable for review. Logging alone is not the same as explainability or a structured audit dataset.
>
> **D. BigQuery ML on extracted metadata**
>
> - This can help with **metadata-based** flagging, but it does not directly perform robust **multimodal** content understanding (audio/video) by itself. It’s better as an analytics/secondary signal layer, not the primary “AI-driven detection and filtering” engine for the media itself.

**⚠️ Note:** Explanations come from **Vertex Explainable AI**; Vertex AI Model Monitoring tracks skew and drift, not individual decisions. B is still the only option that covers scale, audit and explainability.

</details>

---

### Exam 5 · Q5

**Altostrat Media Case Study**

**Company Overview**

Altostrat is a prominent player in the media industry, with an extensive collection of audio and video content that comprises podcasts, interviews, news broadcasts, and documentaries. Their success in delivering premium content to a diverse audience requires a content management system that can keep pace with the dynamic media landscape.

**Solution Concept**

Altostrat seeks to modernize its content management and user engagement strategies using Google Cloud's generative AI. They want a platform that empowers customers with personalized recommendations, natural language interactions, and seamless self-service support. Simultaneously, they want to drive revenue growth through dynamic pricing, targeted marketing, and personalized product suggestions.

The seamless integration of AI-powered tools into their existing Google Cloud environment will enable Altostrat to efficiently manage their vast media library, enhance user experiences, and unlock new revenue streams. Google Cloud’s generative AI will solidify their leadership in the media industry.

**Existing Technical Environment**

Altostrat's content management and delivery platform leverages GKE for scalability and high availability, essential for handling their vast media library. Their extensive media library, spanning various documents, audio and video formats, is stored in Cloud Storage. To gain valuable insights into user behavior, content consumption patterns, and audience demographics, Altostrat leverages BigQuery as their primary data warehouse. Additionally, they use Cloud Run functions for serverless execution of event-driven tasks such as video transcoding, metadata extraction, and personalized content recommendations.

While Altostrat has made significant strides in cloud adoption, they also maintain some legacy on-premises systems for specific workflows like content ingestion and archival. These systems are slated for modernization and migration to Google Cloud in the near future. User management and authentication are currently handled through a combination of Google Identity and third-party identity providers. For monitoring and observability, Altostrat relies on a mix of native Google Cloud tools like Cloud Monitoring and open-source solutions like Prometheus, with alerts primarily delivered via email notifications.

**Business Requirements**

- Accelerate and enhance the reliability of operational workflows across all environments. [Google Cloud + On-premises]
- Simplify infrastructure management for rapid application deployment.
- Optimize cloud storage costs while maintaining high availability and scalability for media content.
- Enable natural language interaction with the platform with 24/7 user support.
- Automatically generate concise summaries of media content.
- Extract rich metadata from media assets using NLP and computer vision.
- Detect and filter inappropriate content.
- Analyze media content to identify trends and extract insights.
- Inform content strategy and decision-making with data.

**Technical Requirements**

- Modernize CI/CD for containerized deployments with a centralized management platform.
- Secure, high-performance hybrid cloud connectivity for data ingestion.
- Provide scalable, performant kubernetes environments both on-premises and in the cloud.
- Optimize cloud storage costs for growing media volumes.
- Design AI-powered detection of harmful content.
- Ensure that AI systems are auditable and their decisions can be explained
- Leverage LLMs and conversational AI for personalized experiences and content virality.
- Develop advanced chatbots with natural language understanding to provide

personalized assistance.

- Automated summarization for diverse media.

**Executive Statement**

At Altostrat, we are embracing the next frontier of artificial intelligence to revolutionize our content strategy. By harnessing the power of generative AI, we will create an unparalleled user experience by empowering our audience with intelligent tools for content discovery, personalized recommendations, and seamless interaction. Reliability and cost management are our top priorities. This strategic initiative will deepen engagement, foster customer loyalty, and unlock new revenue streams through targeted marketing and tailored content offerings. We see a future where AI-driven innovation is central to our business, leading to greater success for our company and delivering exceptional value to our customers.

---

**Question:**

**Altostrat wants to enable natural language interaction and 24/7 personalized self-service support for users, leveraging large language models while integrating with existing user data stored in BigQuery. The solution must scale globally and support rapid iteration.**

**Which architecture should you recommend?**

- A. Deploy a custom chatbot on GKE using open-source LLMs fine-tuned with user data.
- B. Use Dialogflow CX integrated with Vertex AI Gemini models and BigQuery for contextual responses.
- C. Build a Cloud Run service that directly calls Gemini APIs and stores conversation state in Cloud SQL.
- D. Use BigQuery ML to generate text responses based on historical query patterns.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use Dialogflow CX integrated with Vertex AI Gemini models and BigQuery for contextual responses.

**Correct option: B**

**Why B is the right architecture**

Altostrat needs **natural language interaction**, **24/7 personalized self-service**, **global scale**, **rapid iteration**, and **tight integration with BigQuery** while leveraging **large language models**.

- **Dialogflow CX** is purpose-built for enterprise conversational AI with visual flows, versioning, testing, and environment management, enabling **fast iteration** without heavy ops.
- **Vertex AI Gemini models** provide state-of-the-art LLM capabilities (NLU, reasoning, multimodal readiness) with managed scaling and enterprise security.
- **BigQuery integration** allows grounding responses with existing user data for **personalized, contextual answers**.
- The combination scales globally, supports governance, and avoids the operational burden of managing custom LLM infrastructure.

**Why the other options are not the best fit**

**A. Custom chatbot on GKE with open-source LLMs**
Requires significant operational overhead (model hosting, scaling, security, fine-tuning pipelines) and slows iteration compared to managed conversational platforms.

**C. Cloud Run calling Gemini APIs + Cloud SQL state**
Viable for simple bots, but lacks Dialogflow CX’s conversation design tools, testing/versioning, and enterprise-grade conversational management needed for complex, scalable support experiences.

**D. BigQuery ML for text generation**
BigQuery ML is not intended for interactive conversational AI or real-time dialogue orchestration with LLMs.

**Authoritative documentation link**
[Dialogflow CX with generative AI and integrations](https://docs.cloud.google.com/dialogflow/cx/docs)

###### Explanation

**Correct option: B**

**Why B is the right architecture**

Altostrat needs **natural language interaction**, **24/7 personalized self-service**, **global scale**, **rapid iteration**, and **tight integration with BigQuery** while leveraging **large language models**.

- **Dialogflow CX** is purpose-built for enterprise conversational AI with visual flows, versioning, testing, and environment management, enabling **fast iteration** without heavy ops.
- **Vertex AI Gemini models** provide state-of-the-art LLM capabilities (NLU, reasoning, multimodal readiness) with managed scaling and enterprise security.
- **BigQuery integration** allows grounding responses with existing user data for **personalized, contextual answers**.
- The combination scales globally, supports governance, and avoids the operational burden of managing custom LLM infrastructure.

> [!note]- Why the other options are wrong
> **A. Custom chatbot on GKE with open-source LLMs**
> Requires significant operational overhead (model hosting, scaling, security, fine-tuning pipelines) and slows iteration compared to managed conversational platforms.
>
> **C. Cloud Run calling Gemini APIs + Cloud SQL state**
> Viable for simple bots, but lacks Dialogflow CX’s conversation design tools, testing/versioning, and enterprise-grade conversational management needed for complex, scalable support experiences.
>
> **D. BigQuery ML for text generation**
> BigQuery ML is not intended for interactive conversational AI or real-time dialogue orchestration with LLMs.

</details>

---

### Exam 5 · Q12

**Cymbal Retail Case Study**

**Company Overview**

Cymbal is an online retailer experiencing significant growth. The retailer specializes in a large assortment of products spanning several retail sub-verticals, which makes managing their extensive product catalog a constant challenge.

**Solution Concept**

Cymbal wants to modernize its operations and enhance the customer experience in three core areas:

- Catalog and Content Enrichment: Cymbal wants to automate and improve the accuracy of their product catalog by utilizing gen AI to generate product attributes, descriptions, and images from supplier-provided information. This solution will streamline their catalog management, reduce manual effort and errors, and ensure information is consistent across all their sales channels.
- Conversational Commerce with Product Discovery: To enhance customer engagement and drive sales conversion, Cymbal wants to implement a Conversational Commerce solution. This solution will involve integrating AI-powered virtual agents into their website and mobile app to provide customers with a personalized and intuitive shopping experience through natural language conversations. These agents will utilize Google Cloud's Discovery AI to process user requests and retrieve the most relevant products based on each customer's needs and preferences, creating a more engaging and satisfying shopping journey.
- Technical Stack Modernization: To streamline operations and reduce costs around manual processes, data transfer, error handling and remediation, Cymbal wants to modernize their technical stack with cloud-based infrastructure, secure and efficient data handling, 3rd party integrations, and proactive monitoring and security.

**Existing Technical Environment**

Cymbal currently relies on the following environment:

- A mix of on-premises and cloud-based systems.
- A variety of databases, including MySQL, Microsoft SQL Server, Redis, and MongoDB, to store and manage its vast product catalog and customer data.
- Kubernetes clusters to run containerized applications.
- Legacy file-based integrations with on-premises systems, including SFTP file transfers, ETL batch processing.
- A custom-built web application which allows customers to browse the product catalog by querying the relational databases for names and categories of products.
- An IVR (Interactive Voice Response) system to handle initial customer calls and route them to the appropriate departments or agents.
- Call center agents who receive transferred calls from the IVR system and manually enter orders into the system when a customer can’t complete a transaction on their own.
- Various open source tools for monitoring such as Grafana, Nagios, and Elastic.

The current technical environment has encountered significant challenges: manual processes are time-consuming and error-prone, data silos limit a unified view of the customer journey, and integrating new technologies is difficult.

**Business Requirements**

Cymbal has outlined these key business requirements for the gen AI solution:

- Automate Product Catalog Enrichment: Reduce manual effort, minimize errors, and ensure accuracy and consistency across the product catalog.
- Improve Product Discoverability: Enhance search relevance and enable customers to find products more efficiently.
- Increase Customer Engagement: Create a more interactive and personalized shopping experience to improve customer satisfaction and potentially reduce product returns.
- Drive Sales Conversion: Provide a more intuitive and helpful shopping experience to improve sales conversion rates and drive revenue growth.
- Reduce costs: Reduce call center staffing costs and data-center hosting costs. Cymbal Retail Case Study 2

**Technical Requirements**

- Attribute Generation: Accurately derive relevant product attributes from various supplier data, including titles, descriptions, and images, ensuring the attributes align with the product category and Cymbal's existing catalog structure.
- Image Generation and Enhancement: Generate different product image variations from a base image (e.g., showcasing various colors). It should also support background changes, product color adjustments, and the addition of text overlays.
- Automate Product Discovery: Process customer requests expressed in natural language and return highly relevant product results.
- Scalability and Performance: The solution must handle Cymbal's extensive product catalog and accommodate their anticipated growth without compromising performance or user experience.
- Human-in-the-Loop (HITL) Review: Provide a user interface (UI) for associates to review and manage gen AI-generated content, allowing them to approve, reject, or modify suggestions before updating the product catalog.
- Data Security and Compliance: Ensure all customer data, including product information and interactions with virtual agents, are handled securely and comply with relevant industry regulations.

**Executive Statement**

By implementing Google Cloud's Generative AI for Digital Commerce solutions, Cymbal can transform its online retail operations to improve efficiency, enhance customer experience, and drive revenue growth. Key benefits for Cymbal include:

- Reduced operational costs through automation of catalog management tasks.
- Increased efficiency and speed in onboarding new products and updating existing ones.
- Improved accuracy and consistency of product information across all sales channels.
- A more engaging and personalized shopping experience that caters to modern customer preferences for conversational commerce.
- Enhanced product discoverability leading to higher conversion rates and increased sales.

This strategic investment in generative AI will position Cymbal to remain competitive and thrive in the rapidly evolving landscape of online retail.

---

**Question:**

**Cymbal Retail wants to automate product catalog enrichment by generating structured product attributes, descriptions, and enhanced images from supplier-provided text and images. The solution must scale to millions of products, allow human review before publishing, and ensure consistency across all sales channels.**

**Which architecture best meets these requirements?**

- A. Use Vertex AI generative models orchestrated with Vertex AI Pipelines, store generated outputs in BigQuery, and provide a custom review UI backed by Cloud Run before committing updates to the catalog databases.
- B. Deploy custom TensorFlow models on GKE, write generated attributes directly into MySQL, and allow associates to modify records using SQL tools.
- C. Use BigQuery ML to generate product descriptions from supplier text and update the catalog tables automatically.
- D. Trigger Cloud Functions from Cloud Storage uploads to generate attributes and images, bypassing manual review to reduce latency.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Use Vertex AI generative models orchestrated with Vertex AI Pipelines, store generated outputs in BigQuery, and provide a custom review UI backed by Cloud Run before committing updates to the catalog databases.

**Correct option: A**

This case requires (1) **catalog/content enrichment using gen AI** (attributes, descriptions, images), (2) **massive scale** (millions of products), (3) **human-in-the-loop review UI** before publishing, and (4) **consistency across sales channels**. The Cymbal Retail case study explicitly lists **Catalog and Content Enrichment** plus a **Human-in-the-Loop (HITL) Review UI** requirement. v6.1_pca_cymbal_retail_case_stu… v6.1_pca_cymbal_retail_case_stu…

**Why A is best**

- **Vertex AI generative models + Vertex AI Pipelines** fits high-volume, repeatable enrichment workflows at scale (orchestration, reliability, governance). [Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction)
- **BigQuery as the generated-output store** supports consistency checks, QA sampling, channel-level publishing rules, and auditability for what was generated and approved.
- A **custom review UI on Cloud Run** directly matches the HITL requirement (approve/reject/modify before updating the catalog). v6.1_pca_cymbal_retail_case_stu… [Google Cloud](https://cloud.google.com/run)

**Why the other options are not best**

- **B**: Running custom models on GKE and editing via SQL tools adds operational burden and is not aligned with a clean HITL publishing workflow; it also doesn’t address omnichannel consistency controls well.
- **C**: BigQuery ML is not the right tool for multimodal generation (attributes + enhanced images) and lacks the required review gate.
- **D**: It explicitly bypasses manual review, which conflicts with the HITL requirement. v6.1_pca_cymbal_retail_case_stu…

**Single authoritative documentation link (for the orchestration backbone):**
[https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction)

###### Explanation

**Correct option: A**

This case requires (1) **catalog/content enrichment using gen AI** (attributes, descriptions, images), (2) **massive scale** (millions of products), (3) **human-in-the-loop review UI** before publishing, and (4) **consistency across sales channels**. The Cymbal Retail case study explicitly lists **Catalog and Content Enrichment** plus a **Human-in-the-Loop (HITL) Review UI** requirement. v6.1_pca_cymbal_retail_case_stu… v6.1_pca_cymbal_retail_case_stu…

**Why A is best**

- **Vertex AI generative models + Vertex AI Pipelines** fits high-volume, repeatable enrichment workflows at scale (orchestration, reliability, governance). [Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction)
- **BigQuery as the generated-output store** supports consistency checks, QA sampling, channel-level publishing rules, and auditability for what was generated and approved.
- A **custom review UI on Cloud Run** directly matches the HITL requirement (approve/reject/modify before updating the catalog). v6.1_pca_cymbal_retail_case_stu… [Google Cloud](https://cloud.google.com/run)

> [!note]- Why the other options are wrong
> - **B**: Running custom models on GKE and editing via SQL tools adds operational burden and is not aligned with a clean HITL publishing workflow; it also doesn’t address omnichannel consistency controls well.
>
> - **C**: BigQuery ML is not the right tool for multimodal generation (attributes + enhanced images) and lacks the required review gate.
>
> - **D**: It explicitly bypasses manual review, which conflicts with the HITL requirement. v6.1_pca_cymbal_retail_case_stu…

</details>

---

### Exam 5 · Q13

**Cymbal Retail Case Study**

**Company Overview**

Cymbal is an online retailer experiencing significant growth. The retailer specializes in a large assortment of products spanning several retail sub-verticals, which makes managing their extensive product catalog a constant challenge.

**Solution Concept**

Cymbal wants to modernize its operations and enhance the customer experience in three core areas:

- Catalog and Content Enrichment: Cymbal wants to automate and improve the accuracy of their product catalog by utilizing gen AI to generate product attributes, descriptions, and images from supplier-provided information. This solution will streamline their catalog management, reduce manual effort and errors, and ensure information is consistent across all their sales channels.
- Conversational Commerce with Product Discovery: To enhance customer engagement and drive sales conversion, Cymbal wants to implement a Conversational Commerce solution. This solution will involve integrating AI-powered virtual agents into their website and mobile app to provide customers with a personalized and intuitive shopping experience through natural language conversations. These agents will utilize Google Cloud's Discovery AI to process user requests and retrieve the most relevant products based on each customer's needs and preferences, creating a more engaging and satisfying shopping journey.
- Technical Stack Modernization: To streamline operations and reduce costs around manual processes, data transfer, error handling and remediation, Cymbal wants to modernize their technical stack with cloud-based infrastructure, secure and efficient data handling, 3rd party integrations, and proactive monitoring and security.

**Existing Technical Environment**

Cymbal currently relies on the following environment:

- A mix of on-premises and cloud-based systems.
- A variety of databases, including MySQL, Microsoft SQL Server, Redis, and MongoDB, to store and manage its vast product catalog and customer data.
- Kubernetes clusters to run containerized applications.
- Legacy file-based integrations with on-premises systems, including SFTP file transfers, ETL batch processing.
- A custom-built web application which allows customers to browse the product catalog by querying the relational databases for names and categories of products.
- An IVR (Interactive Voice Response) system to handle initial customer calls and route them to the appropriate departments or agents.
- Call center agents who receive transferred calls from the IVR system and manually enter orders into the system when a customer can’t complete a transaction on their own.
- Various open source tools for monitoring such as Grafana, Nagios, and Elastic.

The current technical environment has encountered significant challenges: manual processes are time-consuming and error-prone, data silos limit a unified view of the customer journey, and integrating new technologies is difficult.

**Business Requirements**

Cymbal has outlined these key business requirements for the gen AI solution:

- Automate Product Catalog Enrichment: Reduce manual effort, minimize errors, and ensure accuracy and consistency across the product catalog.
- Improve Product Discoverability: Enhance search relevance and enable customers to find products more efficiently.
- Increase Customer Engagement: Create a more interactive and personalized shopping experience to improve customer satisfaction and potentially reduce product returns.
- Drive Sales Conversion: Provide a more intuitive and helpful shopping experience to improve sales conversion rates and drive revenue growth.
- Reduce costs: Reduce call center staffing costs and data-center hosting costs. Cymbal Retail Case Study 2

**Technical Requirements**

- Attribute Generation: Accurately derive relevant product attributes from various supplier data, including titles, descriptions, and images, ensuring the attributes align with the product category and Cymbal's existing catalog structure.
- Image Generation and Enhancement: Generate different product image variations from a base image (e.g., showcasing various colors). It should also support background changes, product color adjustments, and the addition of text overlays.
- Automate Product Discovery: Process customer requests expressed in natural language and return highly relevant product results.
- Scalability and Performance: The solution must handle Cymbal's extensive product catalog and accommodate their anticipated growth without compromising performance or user experience.
- Human-in-the-Loop (HITL) Review: Provide a user interface (UI) for associates to review and manage gen AI-generated content, allowing them to approve, reject, or modify suggestions before updating the product catalog.
- Data Security and Compliance: Ensure all customer data, including product information and interactions with virtual agents, are handled securely and comply with relevant industry regulations.

**Executive Statement**

By implementing Google Cloud's Generative AI for Digital Commerce solutions, Cymbal can transform its online retail operations to improve efficiency, enhance customer experience, and drive revenue growth. Key benefits for Cymbal include:

- Reduced operational costs through automation of catalog management tasks.
- Increased efficiency and speed in onboarding new products and updating existing ones.
- Improved accuracy and consistency of product information across all sales channels.
- A more engaging and personalized shopping experience that caters to modern customer preferences for conversational commerce.
- Enhanced product discoverability leading to higher conversion rates and increased sales.

This strategic investment in generative AI will position Cymbal to remain competitive and thrive in the rapidly evolving landscape of online retail.

---

**Question:**

**Cymbal plans to implement conversational commerce on its website and mobile app, enabling customers to discover products using natural language. The solution must integrate with the existing catalog, scale during peak shopping events, and deliver highly relevant results personalized to user intent.**

**Which solution should you recommend?**

- A. Integrate Dialogflow CX with Discovery AI for Retail and connect it to the product catalog stored in BigQuery.
- B. Deploy an open-source chatbot framework on Kubernetes that queries MongoDB directly using keyword-based search.
- C. Build a Cloud Run service that sends prompts to Gemini APIs and returns unranked product lists from MySQL.
- D. Use BigQuery ML text generation models to respond to customer queries based on historical purchases.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Integrate Dialogflow CX with Discovery AI for Retail and connect it to the product catalog stored in BigQuery.

**Correct option: A**

**Why A is the best solution**

Cymbal needs **conversational commerce**, **natural-language product discovery**, **personalized and highly relevant results**, and **elastic scale during peak events** (sales, festivals).

- **Dialogflow CX** is purpose-built for enterprise conversational experiences, supporting rich NLU, conversation flows, environments, testing, and rapid iteration for web and mobile.
- **Discovery AI for Retail** is designed specifically for **product search, recommendations, and personalization**, using Google-quality relevance, intent understanding, and ranking tuned for retail use cases.
- Integrating Discovery AI with the **existing product catalog in BigQuery** enables real-time, intent-aware product discovery with personalization signals.
- Both services are **fully managed and globally scalable**, making them suitable for traffic spikes during major shopping events.

This architecture directly aligns with Google’s recommended pattern for **conversational commerce + AI-powered retail search**.

**Why the other options are not suitable**

**B. Open-source chatbot + keyword search**

- Keyword-based search does not understand **user intent or personalization**.
- Operating and scaling a custom chatbot on Kubernetes adds significant operational overhead.

**C. Cloud Run + Gemini APIs + unranked MySQL results**

- While Gemini can understand language, returning **unranked product lists** fails the relevance and personalization requirement.
- Lacks retail-specific ranking, merchandising controls, and search tuning.

**D. BigQuery ML text generation**

- BigQuery ML is not designed for **real-time conversational product discovery**.
- It cannot provide interactive, intent-based product search with low latency.

**Authoritative documentation link (single source):**
[https://cloud.google.com/retail/docs/overview](https://cloud.google.com/retail/docs/overview)

###### Explanation

**Correct option: A**

**Why A is the best solution**

Cymbal needs **conversational commerce**, **natural-language product discovery**, **personalized and highly relevant results**, and **elastic scale during peak events** (sales, festivals).

- **Dialogflow CX** is purpose-built for enterprise conversational experiences, supporting rich NLU, conversation flows, environments, testing, and rapid iteration for web and mobile.
- **Discovery AI for Retail** is designed specifically for **product search, recommendations, and personalization**, using Google-quality relevance, intent understanding, and ranking tuned for retail use cases.
- Integrating Discovery AI with the **existing product catalog in BigQuery** enables real-time, intent-aware product discovery with personalization signals.
- Both services are **fully managed and globally scalable**, making them suitable for traffic spikes during major shopping events.

> [!note]- Why the other options are wrong
> **B. Open-source chatbot + keyword search**
>
> - Keyword-based search does not understand **user intent or personalization**.
> - Operating and scaling a custom chatbot on Kubernetes adds significant operational overhead.
>
> **C. Cloud Run + Gemini APIs + unranked MySQL results**
>
> - While Gemini can understand language, returning **unranked product lists** fails the relevance and personalization requirement.
> - Lacks retail-specific ranking, merchandising controls, and search tuning.
>
> **D. BigQuery ML text generation**
>
> - BigQuery ML is not designed for **real-time conversational product discovery**.
> - It cannot provide interactive, intent-based product search with low latency.

**⚠️ Note:** Discovery AI for Retail was renamed Vertex AI Search for retail and then **Vertex AI Search for commerce**.

</details>

---

### Exam 5 · Q14

**Cymbal Retail Case Study**

**Company Overview**

Cymbal is an online retailer experiencing significant growth. The retailer specializes in a large assortment of products spanning several retail sub-verticals, which makes managing their extensive product catalog a constant challenge.

**Solution Concept**

Cymbal wants to modernize its operations and enhance the customer experience in three core areas:

- Catalog and Content Enrichment: Cymbal wants to automate and improve the accuracy of their product catalog by utilizing gen AI to generate product attributes, descriptions, and images from supplier-provided information. This solution will streamline their catalog management, reduce manual effort and errors, and ensure information is consistent across all their sales channels.
- Conversational Commerce with Product Discovery: To enhance customer engagement and drive sales conversion, Cymbal wants to implement a Conversational Commerce solution. This solution will involve integrating AI-powered virtual agents into their website and mobile app to provide customers with a personalized and intuitive shopping experience through natural language conversations. These agents will utilize Google Cloud's Discovery AI to process user requests and retrieve the most relevant products based on each customer's needs and preferences, creating a more engaging and satisfying shopping journey.
- Technical Stack Modernization: To streamline operations and reduce costs around manual processes, data transfer, error handling and remediation, Cymbal wants to modernize their technical stack with cloud-based infrastructure, secure and efficient data handling, 3rd party integrations, and proactive monitoring and security.

**Existing Technical Environment**

Cymbal currently relies on the following environment:

- A mix of on-premises and cloud-based systems.
- A variety of databases, including MySQL, Microsoft SQL Server, Redis, and MongoDB, to store and manage its vast product catalog and customer data.
- Kubernetes clusters to run containerized applications.
- Legacy file-based integrations with on-premises systems, including SFTP file transfers, ETL batch processing.
- A custom-built web application which allows customers to browse the product catalog by querying the relational databases for names and categories of products.
- An IVR (Interactive Voice Response) system to handle initial customer calls and route them to the appropriate departments or agents.
- Call center agents who receive transferred calls from the IVR system and manually enter orders into the system when a customer can’t complete a transaction on their own.
- Various open source tools for monitoring such as Grafana, Nagios, and Elastic.

The current technical environment has encountered significant challenges: manual processes are time-consuming and error-prone, data silos limit a unified view of the customer journey, and integrating new technologies is difficult.

**Business Requirements**

Cymbal has outlined these key business requirements for the gen AI solution:

- Automate Product Catalog Enrichment: Reduce manual effort, minimize errors, and ensure accuracy and consistency across the product catalog.
- Improve Product Discoverability: Enhance search relevance and enable customers to find products more efficiently.
- Increase Customer Engagement: Create a more interactive and personalized shopping experience to improve customer satisfaction and potentially reduce product returns.
- Drive Sales Conversion: Provide a more intuitive and helpful shopping experience to improve sales conversion rates and drive revenue growth.
- Reduce costs: Reduce call center staffing costs and data-center hosting costs. Cymbal Retail Case Study 2

**Technical Requirements**

- Attribute Generation: Accurately derive relevant product attributes from various supplier data, including titles, descriptions, and images, ensuring the attributes align with the product category and Cymbal's existing catalog structure.
- Image Generation and Enhancement: Generate different product image variations from a base image (e.g., showcasing various colors). It should also support background changes, product color adjustments, and the addition of text overlays.
- Automate Product Discovery: Process customer requests expressed in natural language and return highly relevant product results.
- Scalability and Performance: The solution must handle Cymbal's extensive product catalog and accommodate their anticipated growth without compromising performance or user experience.
- Human-in-the-Loop (HITL) Review: Provide a user interface (UI) for associates to review and manage gen AI-generated content, allowing them to approve, reject, or modify suggestions before updating the product catalog.
- Data Security and Compliance: Ensure all customer data, including product information and interactions with virtual agents, are handled securely and comply with relevant industry regulations.

**Executive Statement**

By implementing Google Cloud's Generative AI for Digital Commerce solutions, Cymbal can transform its online retail operations to improve efficiency, enhance customer experience, and drive revenue growth. Key benefits for Cymbal include:

- Reduced operational costs through automation of catalog management tasks.
- Increased efficiency and speed in onboarding new products and updating existing ones.
- Improved accuracy and consistency of product information across all sales channels.
- A more engaging and personalized shopping experience that caters to modern customer preferences for conversational commerce.
- Enhanced product discoverability leading to higher conversion rates and increased sales.

This strategic investment in generative AI will position Cymbal to remain competitive and thrive in the rapidly evolving landscape of online retail.

---

**Question:**

**Cymbal’s current environment includes legacy file-based SFTP integrations, batch ETL jobs, and multiple databases across on-premises and cloud systems. They want to modernize data movement, reduce manual error handling, and improve observability while maintaining secure hybrid connectivity.**

**Which architecture best satisfies these goals?**

- A. Replace SFTP with Storage Transfer Service and continue batch ETL using cron jobs.
- B. Use Cloud VPN for connectivity and migrate all databases to Compute Engine VMs.
- C. Implement Dedicated Interconnect with Cloud Router, use Pub/Sub for event-driven data ingestion, and centralize processing with Dataflow.
- D. Keep SFTP integrations but add Cloud Monitoring alerts for failed transfers.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Implement Dedicated Interconnect with Cloud Router, use Pub/Sub for event-driven data ingestion, and centralize processing with Dataflow.

**Correct option: C**

**Why C best satisfies the goals**

Cymbal wants to **modernize data movement**, **reduce manual error handling**, **improve observability**, and **maintain secure hybrid connectivity** across on-premises and cloud systems.

- **Dedicated Interconnect with Cloud Router** provides private, high-throughput, low-latency hybrid connectivity with dynamic routing (BGP), reducing operational risk and improving reliability for enterprise data flows.
- **Pub/Sub** enables **event-driven ingestion**, replacing brittle, file-based SFTP and cron-driven batches with decoupled, resilient pipelines that naturally reduce manual retries and failures.
- **Dataflow** centralizes processing with managed scaling, built-in fault tolerance, and rich observability (metrics, logs, backpressure), which directly addresses error handling and visibility requirements.

This combination reflects a Google-recommended modernization pattern: **private hybrid connectivity + event-driven ingestion + managed stream/batch processing**.

**Why the other options are not best**

- **A. Storage Transfer Service + cron ETL**
  Improves file transfer but **keeps batch/cron coupling** and does not deliver event-driven processing or end-to-end observability.
- **B. Cloud VPN + move DBs to VMs**
  VPN is suitable for lower throughput and less predictable latency; migrating databases to VMs increases ops burden and does not modernize ingestion.
- **D. Keep SFTP + alerts**
  Monitoring alerts alone do not fix **architectural brittleness** or manual recovery; this is incremental, not modernization.

**Single authoritative documentation link**
[Event-driven data processing with Pub/Sub and Dataflow on Google Cloud](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-with-cloud-pubsub)

###### Explanation

**Correct option: C**

**Why C best satisfies the goals**

Cymbal wants to **modernize data movement**, **reduce manual error handling**, **improve observability**, and **maintain secure hybrid connectivity** across on-premises and cloud systems.

- **Dedicated Interconnect with Cloud Router** provides private, high-throughput, low-latency hybrid connectivity with dynamic routing (BGP), reducing operational risk and improving reliability for enterprise data flows.
- **Pub/Sub** enables **event-driven ingestion**, replacing brittle, file-based SFTP and cron-driven batches with decoupled, resilient pipelines that naturally reduce manual retries and failures.
- **Dataflow** centralizes processing with managed scaling, built-in fault tolerance, and rich observability (metrics, logs, backpressure), which directly addresses error handling and visibility requirements.

> [!note]- Why the other options are wrong
> - **A. Storage Transfer Service + cron ETL**
>   Improves file transfer but **keeps batch/cron coupling** and does not deliver event-driven processing or end-to-end observability.
>
> - **B. Cloud VPN + move DBs to VMs**
>   VPN is suitable for lower throughput and less predictable latency; migrating databases to VMs increases ops burden and does not modernize ingestion.
>
> - **D. Keep SFTP + alerts**
>   Monitoring alerts alone do not fix **architectural brittleness** or manual recovery; this is incremental, not modernization.

</details>

---

### Exam 5 · Q15

**Cymbal Retail Case Study**

**Company Overview**

Cymbal is an online retailer experiencing significant growth. The retailer specializes in a large assortment of products spanning several retail sub-verticals, which makes managing their extensive product catalog a constant challenge.

**Solution Concept**

Cymbal wants to modernize its operations and enhance the customer experience in three core areas:

- Catalog and Content Enrichment: Cymbal wants to automate and improve the accuracy of their product catalog by utilizing gen AI to generate product attributes, descriptions, and images from supplier-provided information. This solution will streamline their catalog management, reduce manual effort and errors, and ensure information is consistent across all their sales channels.
- Conversational Commerce with Product Discovery: To enhance customer engagement and drive sales conversion, Cymbal wants to implement a Conversational Commerce solution. This solution will involve integrating AI-powered virtual agents into their website and mobile app to provide customers with a personalized and intuitive shopping experience through natural language conversations. These agents will utilize Google Cloud's Discovery AI to process user requests and retrieve the most relevant products based on each customer's needs and preferences, creating a more engaging and satisfying shopping journey.
- Technical Stack Modernization: To streamline operations and reduce costs around manual processes, data transfer, error handling and remediation, Cymbal wants to modernize their technical stack with cloud-based infrastructure, secure and efficient data handling, 3rd party integrations, and proactive monitoring and security.

**Existing Technical Environment**

Cymbal currently relies on the following environment:

- A mix of on-premises and cloud-based systems.
- A variety of databases, including MySQL, Microsoft SQL Server, Redis, and MongoDB, to store and manage its vast product catalog and customer data.
- Kubernetes clusters to run containerized applications.
- Legacy file-based integrations with on-premises systems, including SFTP file transfers, ETL batch processing.
- A custom-built web application which allows customers to browse the product catalog by querying the relational databases for names and categories of products.
- An IVR (Interactive Voice Response) system to handle initial customer calls and route them to the appropriate departments or agents.
- Call center agents who receive transferred calls from the IVR system and manually enter orders into the system when a customer can’t complete a transaction on their own.
- Various open source tools for monitoring such as Grafana, Nagios, and Elastic.

The current technical environment has encountered significant challenges: manual processes are time-consuming and error-prone, data silos limit a unified view of the customer journey, and integrating new technologies is difficult.

**Business Requirements**

Cymbal has outlined these key business requirements for the gen AI solution:

- Automate Product Catalog Enrichment: Reduce manual effort, minimize errors, and ensure accuracy and consistency across the product catalog.
- Improve Product Discoverability: Enhance search relevance and enable customers to find products more efficiently.
- Increase Customer Engagement: Create a more interactive and personalized shopping experience to improve customer satisfaction and potentially reduce product returns.
- Drive Sales Conversion: Provide a more intuitive and helpful shopping experience to improve sales conversion rates and drive revenue growth.
- Reduce costs: Reduce call center staffing costs and data-center hosting costs. Cymbal Retail Case Study 2

**Technical Requirements**

- Attribute Generation: Accurately derive relevant product attributes from various supplier data, including titles, descriptions, and images, ensuring the attributes align with the product category and Cymbal's existing catalog structure.
- Image Generation and Enhancement: Generate different product image variations from a base image (e.g., showcasing various colors). It should also support background changes, product color adjustments, and the addition of text overlays.
- Automate Product Discovery: Process customer requests expressed in natural language and return highly relevant product results.
- Scalability and Performance: The solution must handle Cymbal's extensive product catalog and accommodate their anticipated growth without compromising performance or user experience.
- Human-in-the-Loop (HITL) Review: Provide a user interface (UI) for associates to review and manage gen AI-generated content, allowing them to approve, reject, or modify suggestions before updating the product catalog.
- Data Security and Compliance: Ensure all customer data, including product information and interactions with virtual agents, are handled securely and comply with relevant industry regulations.

**Executive Statement**

By implementing Google Cloud's Generative AI for Digital Commerce solutions, Cymbal can transform its online retail operations to improve efficiency, enhance customer experience, and drive revenue growth. Key benefits for Cymbal include:

- Reduced operational costs through automation of catalog management tasks.
- Increased efficiency and speed in onboarding new products and updating existing ones.
- Improved accuracy and consistency of product information across all sales channels.
- A more engaging and personalized shopping experience that caters to modern customer preferences for conversational commerce.
- Enhanced product discoverability leading to higher conversion rates and increased sales.

This strategic investment in generative AI will position Cymbal to remain competitive and thrive in the rapidly evolving landscape of online retail.

---

**Question:**

**Cymbal requires a human-in-the-loop (HITL) workflow so associates can review, approve, or modify AI-generated catalog content before it is published. The solution must support auditability, role-based access control, and rapid iteration.**

**Which approach should you recommend?**

- A. Store generated content in Cloud Storage and allow associates to edit files directly using signed URLs.
- B. Build a review application on Cloud Run secured with IAM and Identity-Aware Proxy, persisting review states and approvals in a managed database.
- C. Allow associates to review content by querying BigQuery tables and updating records manually.
- D. Use Google Sheets as an approval interface connected to the catalog via Apps Script.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Build a review application on Cloud Run secured with IAM and Identity-Aware Proxy, persisting review states and approvals in a managed database.

**Correct option: B**

**Why B is the best approach**

Cymbal needs a **human-in-the-loop (HITL)** workflow with **auditability**, **role-based access control**, and **rapid iteration**.

- **Cloud Run** enables a lightweight, quickly changeable review application that scales automatically with reviewer demand.
- **IAM + Identity-Aware Proxy (IAP)** provide strong **RBAC**, centralized authentication, and fine-grained authorization without building custom auth logic.
- Persisting **review states, approvals, timestamps, and reviewer identity** in a **managed database** (for example, Cloud SQL or Firestore) ensures a durable **audit trail** required for compliance and traceability.
- This pattern cleanly separates **generation**, **review**, and **publish** steps, supporting fast iteration on the UI and workflows without disrupting the AI pipeline.

**Why the other options are not suitable**

- **A. Cloud Storage + signed URLs**
  Lacks structured RBAC, workflow states, and reliable audit history; direct file edits are hard to govern and trace.
- **C. Manual BigQuery updates**
  BigQuery is optimized for analytics, not transactional review workflows or fine-grained approvals; manual edits increase risk and slow iteration.
- **D. Google Sheets + Apps Script**
  Useful for prototypes, but not appropriate for enterprise-grade RBAC, scalability, or auditable approval workflows tied to production catalogs.

**Single authoritative documentation link**
[Identity-Aware Proxy for securing Cloud Run applications](https://docs.cloud.google.com/run/docs/securing/identity-aware-proxy-cloud-run)

###### Explanation

**Correct option: B**

**Why B is the best approach**

Cymbal needs a **human-in-the-loop (HITL)** workflow with **auditability**, **role-based access control**, and **rapid iteration**.

- **Cloud Run** enables a lightweight, quickly changeable review application that scales automatically with reviewer demand.
- **IAM + Identity-Aware Proxy (IAP)** provide strong **RBAC**, centralized authentication, and fine-grained authorization without building custom auth logic.
- Persisting **review states, approvals, timestamps, and reviewer identity** in a **managed database** (for example, Cloud SQL or Firestore) ensures a durable **audit trail** required for compliance and traceability.
- This pattern cleanly separates **generation**, **review**, and **publish** steps, supporting fast iteration on the UI and workflows without disrupting the AI pipeline.

> [!note]- Why the other options are wrong
> - **A. Cloud Storage + signed URLs**
>   Lacks structured RBAC, workflow states, and reliable audit history; direct file edits are hard to govern and trace.
>
> - **C. Manual BigQuery updates**
>   BigQuery is optimized for analytics, not transactional review workflows or fine-grained approvals; manual edits increase risk and slow iteration.
>
> - **D. Google Sheets + Apps Script**
>   Useful for prototypes, but not appropriate for enterprise-grade RBAC, scalability, or auditable approval workflows tied to production catalogs.

</details>

---

### Exam 5 · Q16

**Cymbal Retail Case Study**

**Company Overview**

Cymbal is an online retailer experiencing significant growth. The retailer specializes in a large assortment of products spanning several retail sub-verticals, which makes managing their extensive product catalog a constant challenge.

**Solution Concept**

Cymbal wants to modernize its operations and enhance the customer experience in three core areas:

- Catalog and Content Enrichment: Cymbal wants to automate and improve the accuracy of their product catalog by utilizing gen AI to generate product attributes, descriptions, and images from supplier-provided information. This solution will streamline their catalog management, reduce manual effort and errors, and ensure information is consistent across all their sales channels.
- Conversational Commerce with Product Discovery: To enhance customer engagement and drive sales conversion, Cymbal wants to implement a Conversational Commerce solution. This solution will involve integrating AI-powered virtual agents into their website and mobile app to provide customers with a personalized and intuitive shopping experience through natural language conversations. These agents will utilize Google Cloud's Discovery AI to process user requests and retrieve the most relevant products based on each customer's needs and preferences, creating a more engaging and satisfying shopping journey.
- Technical Stack Modernization: To streamline operations and reduce costs around manual processes, data transfer, error handling and remediation, Cymbal wants to modernize their technical stack with cloud-based infrastructure, secure and efficient data handling, 3rd party integrations, and proactive monitoring and security.

**Existing Technical Environment**

Cymbal currently relies on the following environment:

- A mix of on-premises and cloud-based systems.
- A variety of databases, including MySQL, Microsoft SQL Server, Redis, and MongoDB, to store and manage its vast product catalog and customer data.
- Kubernetes clusters to run containerized applications.
- Legacy file-based integrations with on-premises systems, including SFTP file transfers, ETL batch processing.
- A custom-built web application which allows customers to browse the product catalog by querying the relational databases for names and categories of products.
- An IVR (Interactive Voice Response) system to handle initial customer calls and route them to the appropriate departments or agents.
- Call center agents who receive transferred calls from the IVR system and manually enter orders into the system when a customer can’t complete a transaction on their own.
- Various open source tools for monitoring such as Grafana, Nagios, and Elastic.

The current technical environment has encountered significant challenges: manual processes are time-consuming and error-prone, data silos limit a unified view of the customer journey, and integrating new technologies is difficult.

**Business Requirements**

Cymbal has outlined these key business requirements for the gen AI solution:

- Automate Product Catalog Enrichment: Reduce manual effort, minimize errors, and ensure accuracy and consistency across the product catalog.
- Improve Product Discoverability: Enhance search relevance and enable customers to find products more efficiently.
- Increase Customer Engagement: Create a more interactive and personalized shopping experience to improve customer satisfaction and potentially reduce product returns.
- Drive Sales Conversion: Provide a more intuitive and helpful shopping experience to improve sales conversion rates and drive revenue growth.
- Reduce costs: Reduce call center staffing costs and data-center hosting costs. Cymbal Retail Case Study 2

**Technical Requirements**

- Attribute Generation: Accurately derive relevant product attributes from various supplier data, including titles, descriptions, and images, ensuring the attributes align with the product category and Cymbal's existing catalog structure.
- Image Generation and Enhancement: Generate different product image variations from a base image (e.g., showcasing various colors). It should also support background changes, product color adjustments, and the addition of text overlays.
- Automate Product Discovery: Process customer requests expressed in natural language and return highly relevant product results.
- Scalability and Performance: The solution must handle Cymbal's extensive product catalog and accommodate their anticipated growth without compromising performance or user experience.
- Human-in-the-Loop (HITL) Review: Provide a user interface (UI) for associates to review and manage gen AI-generated content, allowing them to approve, reject, or modify suggestions before updating the product catalog.
- Data Security and Compliance: Ensure all customer data, including product information and interactions with virtual agents, are handled securely and comply with relevant industry regulations.

**Executive Statement**

By implementing Google Cloud's Generative AI for Digital Commerce solutions, Cymbal can transform its online retail operations to improve efficiency, enhance customer experience, and drive revenue growth. Key benefits for Cymbal include:

- Reduced operational costs through automation of catalog management tasks.
- Increased efficiency and speed in onboarding new products and updating existing ones.
- Improved accuracy and consistency of product information across all sales channels.
- A more engaging and personalized shopping experience that caters to modern customer preferences for conversational commerce.
- Enhanced product discoverability leading to higher conversion rates and increased sales.

This strategic investment in generative AI will position Cymbal to remain competitive and thrive in the rapidly evolving landscape of online retail.

---

**Cymbal wants to reduce call center costs by replacing its IVR-based customer support with AI-powered virtual agents capable of handling common shopping and order-related queries. The solution must securely handle customer data and integrate with backend systems.**

**Which architecture best aligns with these requirements?**

- A. Deploy Dialogflow CX integrated with backend services through secure APIs and apply IAM and data access controls for compliance.
- B. Use an open-source voice bot hosted on GKE that stores conversation logs locally for analysis.
- C. Extend the existing IVR system with keyword-based routing and manual escalation.
- D. Build a Cloud Functions–based chatbot that stores conversation history in Redis without encryption.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Deploy Dialogflow CX integrated with backend services through secure APIs and apply IAM and data access controls for compliance.

**Correct option: A**

**Why A best aligns with the requirements**

Cymbal wants to **replace IVR with AI-powered virtual agents**, securely handle **customer data**, and **integrate with backend systems** for shopping and order queries.

- **Dialogflow CX** is designed for enterprise-grade virtual agents (voice and chat) with robust NLU, flow-based conversation design, versioning, testing, and environments.
- Integration with **backend services via secure APIs** (for example, Cloud Run or Apigee–fronted services) enables real-time order status, returns, and account lookups.
- **IAM and data access controls** provide least-privilege access and compliance-aligned security for sensitive customer data.
- This is the standard Google Cloud architecture for modern, secure customer support virtual agents.

**Why the other options are not suitable**

- **B. Open-source voice bot on GKE**
  High operational overhead, weaker built-in security/governance, and local log storage raise compliance risks.
- **C. Enhanced IVR with keywords**
  Does not meet the requirement for AI-powered natural language interactions or cost reduction through automation.
- **D. Cloud Functions + Redis without encryption**
  Storing conversation history without encryption violates basic security and compliance expectations for customer data.

**Single authoritative documentation link**
Dialogflow CX overview and enterprise virtual agent capabilities:
[https://cloud.google.com/dialogflow/cx/docs](https://cloud.google.com/dialogflow/cx/docs)

###### Explanation

**Correct option: A**

**Why A best aligns with the requirements**

Cymbal wants to **replace IVR with AI-powered virtual agents**, securely handle **customer data**, and **integrate with backend systems** for shopping and order queries.

- **Dialogflow CX** is designed for enterprise-grade virtual agents (voice and chat) with robust NLU, flow-based conversation design, versioning, testing, and environments.
- Integration with **backend services via secure APIs** (for example, Cloud Run or Apigee–fronted services) enables real-time order status, returns, and account lookups.
- **IAM and data access controls** provide least-privilege access and compliance-aligned security for sensitive customer data.
- This is the standard Google Cloud architecture for modern, secure customer support virtual agents.

> [!note]- Why the other options are wrong
> - **B. Open-source voice bot on GKE**
>   High operational overhead, weaker built-in security/governance, and local log storage raise compliance risks.
>
> - **C. Enhanced IVR with keywords**
>   Does not meet the requirement for AI-powered natural language interactions or cost reduction through automation.
>
> - **D. Cloud Functions + Redis without encryption**
>   Storing conversation history without encryption violates basic security and compliance expectations for customer data.

</details>

---

### Exam 5 · Q17

**KnightMotives Automotive Case Study**

**Company Overview**

KnightMotives is a car manufacturer specializing in autonomous, self-driving vehicles, including Battery Electric Vehicles (BEVs), hybrids, and traditional internal combustion engine (ICE) vehicles. While KnightMotives has made strides with the in-vehicle experience in their BEV fleet, the hybrid and ICE vehicles have yet to implement these new systems and are viewed poorly by critics and drivers. The lack of modern in-vehicle technology in hybrid and ICE vehicles has resulted in declining sales and customer satisfaction.

KnightMotives wants to modernize the consumer experience across all vehicles within five years. Artificial Intelligence offers a unique opportunity to revolutionize the in-vehicle experience, as well as the shopping, buying, and service/maintenance experience. Investment in this new technology will require a shift in financial priorities on a global scale.

KnightMotives also wants to improve their online ordering system, which is unreliable. Systems for customers to build their vehicle online for acquisition through a dealer are not delivering the data or reliability that dealers need, causing a strain in the relationship between KnightMotives and dealers. Service technicians and sales staff need better tooling to enhance dealer successes, including built-to-order vehicles.

**Solution Concept**

KnightMotives wants to shift from manufacturing cars to creating a complete and compelling "automotive experience." Their strategy prioritizes delivering a consistent experience across all models, developing AI-powered features, generating new revenue from data monetization, adopting a digital focus to differentiate their brand from competitors, and developing better tools for mechanics and salespeople.

**Existing Technical Environment**

KnightMotives's IT is largely on-premises with some applications on major cloud platforms. Their supply chain runs on an outdated mainframe, and Enterprise Resource Planning (ERP) is also outdated, making new promotions and dealer discounts difficult to implement. Dealers have no budget for new equipment. There is fragmentation across vehicles with multiple code bases, and significant technical debt from supporting backwards compatibility. Network connectivity to manufacturing plants and vehicle connectivity in rural areas are challenges.

**Business Requirements**

Key business requirements include fostering a personalized relationship with the driver and delivering a cohesive experience across all models. Creating a better build-to-order model will reduce time on the lot and provide transparency for both dealers and customers. Additionally, KnightMotives seeks to monetize corporate data to finance new technology investments, as their current AI infrastructure is obsolete and corporate data remains siloed. Security is a paramount concern due to past data breaches. Adherence to European Union (EU) data protection regulations, especially for emerging autonomous platforms, is critical.

KnightMotives plans to make significant investments in fully autonomous driving capabilities, with initial implementation targeting regions with favorable regulatory environments. Prioritizing employee upskilling, attracting top-tier talent, and fostering better communication between business and technical teams are also critical objectives.

**Technical Requirements**

- Modernizing the in-vehicle experience includes developing a consistent user experience (UX) that seamlessly integrates AI-powered features across all models, updating in-vehicle hardware and software in legacy models to support new UX features and AI capabilities, and ensuring reliable network connectivity, especially in rural areas, to support real-time AI features and data transmission.
- Network upgrades are necessary to support increased data traffic and improve connectivity between plants and headquarters.
- IT infrastructure modernization requires adopting a hybrid cloud strategy to leverage the benefits of both on-premises and cloud infrastructure, and gradually modernizing or replacing legacy systems to improve efficiency and agility. KnightMotives Automotive Case Study 2
- Autonomous vehicle development and testing requires investing in cutting-edge AI and machine learning technologies, building a robust simulation environment, and ensuring compliance with evolving regulations related to autonomous vehicles.
- Data monetization and insights requires implementing a robust data management platform, strict data security and privacy measures, and a scalable AI/ML infrastructure.
- Increased focus on security and risk management involves implementing a comprehensive security framework to protect against cyber threats and data breaches, developing an incident response plan, and providing security awareness training to employees.
- Providing a delightful experience for dealers and customers requires improving the online build-to-order system; developing modern dealer tools to streamline dealer operations, including sales, service, and inventory management; and implementing a comprehensive Customer Relationship Management (CRM) system to track customer interactions, personalize experiences, and improve customer satisfaction.

**Executive Statement**

KnightMotives is committed to enhancing safety and saving lives by leveraging an extensive body of data—encompassing driving, road conditions, behavioral studies, and crash safety statistics—to create compelling digital experiences for drivers. Our AI consistently outperforms national safety statistics, ensuring the unique and coveted KnightMotives experience is aligned across all our vehicle models.

Michael Knight, KnightMotives CEO

---

**Question:**

**KnightMotives wants to modernize the in-vehicle experience across BEV, hybrid, and ICE vehicles within five years. The solution must provide a consistent AI-powered user experience, support unreliable network connectivity in rural areas, and allow gradual rollout across legacy vehicle platforms.**

**Which architecture best meets these requirements?**

- A. Deploy all in-vehicle AI features as real-time cloud-hosted services accessed through continuous connectivity.
- B. Implement a hybrid architecture using edge-based inference for latency-sensitive features with cloud-based model training and updates delivered over intermittent connectivity.
- C. Centralize all vehicle telemetry and inference in on-premises data centers to meet regulatory constraints.
- D. Use batch-based data uploads from vehicles to cloud storage and process AI features asynchronously.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Implement a hybrid architecture using edge-based inference for latency-sensitive features with cloud-based model training and updates delivered over intermittent connectivity.

**Correct option: B**

**Why B best meets the requirements**

KnightMotives needs a **consistent AI-powered in-vehicle experience** across BEV, hybrid, and ICE vehicles, must **work with unreliable connectivity in rural areas**, and must allow a **gradual rollout across legacy platforms** over five years.

A **hybrid edge + cloud architecture** directly aligns with these constraints:

- **Edge-based inference** inside the vehicle ensures **low latency** and continued functionality when network connectivity is intermittent or unavailable in rural areas, which is explicitly called out as a challenge.
- **Cloud-based model training and centralized updates** allow KnightMotives to continuously improve AI features and roll out enhancements **incrementally** across different vehicle generations and platforms, addressing fragmentation and legacy technical debt.
- This approach supports a **consistent UX across all models** while enabling gradual modernization of hybrid and ICE vehicles without requiring constant connectivity.

**Why the other options are incorrect**

**A. Fully cloud-hosted, real-time services**
Requires continuous connectivity, which conflicts with rural network unreliability and would break core in-vehicle features when offline.

**C. Centralized on-premises inference**
Does not scale globally, fails to address in-vehicle latency requirements, and contradicts the stated need for a **hybrid cloud strategy** and modern AI capabilities.

**D. Batch-based uploads with asynchronous processing**
Cannot support real-time or interactive in-vehicle AI experiences and would not deliver a modern, consistent UX across vehicles.

**Authoritative reference**
[Google Cloud guidance on edge and hybrid AI architectures](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/edge-hybrid-pattern):

###### Explanation

**Correct option: B**

**Why B best meets the requirements**

KnightMotives needs a **consistent AI-powered in-vehicle experience** across BEV, hybrid, and ICE vehicles, must **work with unreliable connectivity in rural areas**, and must allow a **gradual rollout across legacy platforms** over five years.

A **hybrid edge + cloud architecture** directly aligns with these constraints:

- **Edge-based inference** inside the vehicle ensures **low latency** and continued functionality when network connectivity is intermittent or unavailable in rural areas, which is explicitly called out as a challenge.
- **Cloud-based model training and centralized updates** allow KnightMotives to continuously improve AI features and roll out enhancements **incrementally** across different vehicle generations and platforms, addressing fragmentation and legacy technical debt.
- This approach supports a **consistent UX across all models** while enabling gradual modernization of hybrid and ICE vehicles without requiring constant connectivity.

> [!note]- Why the other options are wrong
> **A. Fully cloud-hosted, real-time services**
> Requires continuous connectivity, which conflicts with rural network unreliability and would break core in-vehicle features when offline.
>
> **C. Centralized on-premises inference**
> Does not scale globally, fails to address in-vehicle latency requirements, and contradicts the stated need for a **hybrid cloud strategy** and modern AI capabilities.
>
> **D. Batch-based uploads with asynchronous processing**
> Cannot support real-time or interactive in-vehicle AI experiences and would not deliver a modern, consistent UX across vehicles.

</details>

---

### Exam 5 · Q18

**KnightMotives Automotive Case Study**

**Company Overview**

KnightMotives is a car manufacturer specializing in autonomous, self-driving vehicles, including Battery Electric Vehicles (BEVs), hybrids, and traditional internal combustion engine (ICE) vehicles. While KnightMotives has made strides with the in-vehicle experience in their BEV fleet, the hybrid and ICE vehicles have yet to implement these new systems and are viewed poorly by critics and drivers. The lack of modern in-vehicle technology in hybrid and ICE vehicles has resulted in declining sales and customer satisfaction.

KnightMotives wants to modernize the consumer experience across all vehicles within five years. Artificial Intelligence offers a unique opportunity to revolutionize the in-vehicle experience, as well as the shopping, buying, and service/maintenance experience. Investment in this new technology will require a shift in financial priorities on a global scale.

KnightMotives also wants to improve their online ordering system, which is unreliable. Systems for customers to build their vehicle online for acquisition through a dealer are not delivering the data or reliability that dealers need, causing a strain in the relationship between KnightMotives and dealers. Service technicians and sales staff need better tooling to enhance dealer successes, including built-to-order vehicles.

**Solution Concept**

KnightMotives wants to shift from manufacturing cars to creating a complete and compelling "automotive experience." Their strategy prioritizes delivering a consistent experience across all models, developing AI-powered features, generating new revenue from data monetization, adopting a digital focus to differentiate their brand from competitors, and developing better tools for mechanics and salespeople.

**Existing Technical Environment**

KnightMotives's IT is largely on-premises with some applications on major cloud platforms. Their supply chain runs on an outdated mainframe, and Enterprise Resource Planning (ERP) is also outdated, making new promotions and dealer discounts difficult to implement. Dealers have no budget for new equipment. There is fragmentation across vehicles with multiple code bases, and significant technical debt from supporting backwards compatibility. Network connectivity to manufacturing plants and vehicle connectivity in rural areas are challenges.

**Business Requirements**

Key business requirements include fostering a personalized relationship with the driver and delivering a cohesive experience across all models. Creating a better build-to-order model will reduce time on the lot and provide transparency for both dealers and customers. Additionally, KnightMotives seeks to monetize corporate data to finance new technology investments, as their current AI infrastructure is obsolete and corporate data remains siloed. Security is a paramount concern due to past data breaches. Adherence to European Union (EU) data protection regulations, especially for emerging autonomous platforms, is critical.

KnightMotives plans to make significant investments in fully autonomous driving capabilities, with initial implementation targeting regions with favorable regulatory environments. Prioritizing employee upskilling, attracting top-tier talent, and fostering better communication between business and technical teams are also critical objectives.

**Technical Requirements**

- Modernizing the in-vehicle experience includes developing a consistent user experience (UX) that seamlessly integrates AI-powered features across all models, updating in-vehicle hardware and software in legacy models to support new UX features and AI capabilities, and ensuring reliable network connectivity, especially in rural areas, to support real-time AI features and data transmission.
- Network upgrades are necessary to support increased data traffic and improve connectivity between plants and headquarters.
- IT infrastructure modernization requires adopting a hybrid cloud strategy to leverage the benefits of both on-premises and cloud infrastructure, and gradually modernizing or replacing legacy systems to improve efficiency and agility. KnightMotives Automotive Case Study 2
- Autonomous vehicle development and testing requires investing in cutting-edge AI and machine learning technologies, building a robust simulation environment, and ensuring compliance with evolving regulations related to autonomous vehicles.
- Data monetization and insights requires implementing a robust data management platform, strict data security and privacy measures, and a scalable AI/ML infrastructure.
- Increased focus on security and risk management involves implementing a comprehensive security framework to protect against cyber threats and data breaches, developing an incident response plan, and providing security awareness training to employees.
- Providing a delightful experience for dealers and customers requires improving the online build-to-order system; developing modern dealer tools to streamline dealer operations, including sales, service, and inventory management; and implementing a comprehensive Customer Relationship Management (CRM) system to track customer interactions, personalize experiences, and improve customer satisfaction.

**Executive Statement**

KnightMotives is committed to enhancing safety and saving lives by leveraging an extensive body of data—encompassing driving, road conditions, behavioral studies, and crash safety statistics—to create compelling digital experiences for drivers. Our AI consistently outperforms national safety statistics, ensuring the unique and coveted KnightMotives experience is aligned across all our vehicle models.

Michael Knight, KnightMotives CEO

---

**Question:**

**KnightMotives plans to monetize corporate and vehicle-generated data to fund future autonomous driving investments. The data is currently siloed across legacy ERP systems, manufacturing plants, and vehicle telemetry platforms. Security and EU data protection compliance are critical due to prior breaches.**

**Which data platform architecture should you recommend?**

- A. Consolidate all data into a single on-premises data warehouse to simplify governance.
- B. Build a centralized analytics platform on BigQuery with regional data residency controls, IAM-based access, and customer-managed encryption keys.
- C. Use Cloud Storage exclusively and allow business teams to query data using ad hoc tools.
- D. Replicate all data into multiple clouds to improve availability and reduce compliance risk.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Build a centralized analytics platform on BigQuery with regional data residency controls, IAM-based access, and customer-managed encryption keys.

**Correct option: B. Build a centralized analytics platform on BigQuery with regional data residency controls, IAM-based access, and customer-managed encryption keys.**

**Why B is the best architecture**

KnightMotives wants to **monetize corporate and vehicle-generated data**, eliminate **silos** (ERP, plants, telemetry), and enforce **strong security with EU data protection compliance** after prior breaches.

- **BigQuery as a centralized analytics platform** directly addresses data silos by ingesting and analyzing data from heterogeneous sources at scale, enabling advanced analytics and monetization.
- **Regional data residency controls** support EU regulatory requirements by keeping datasets in specific regions.
- **IAM-based access control** enforces least privilege and auditable access for users and services.
- **Customer-managed encryption keys (CMEK)** provide stronger control over encryption and key lifecycle—an explicit need after prior security incidents.

This design aligns with the case study’s requirements for **hybrid modernization**, **data monetization**, and **strict security/privacy controls**.

**Why the other options are not suitable**

- **A. Single on-premises warehouse**
  Limits scalability and advanced analytics, perpetuates legacy constraints, and conflicts with the stated **hybrid/cloud modernization** direction.
- **C. Cloud Storage only with ad hoc querying**
  Lacks a governed analytics layer, fine-grained access controls, and enterprise-grade compliance capabilities needed for monetization.
- **D. Replicating data into multiple clouds**
  Increases operational complexity and **compliance risk**, making EU data residency harder—not easier—to guarantee.

**Single authoritative documentation link**
[BigQuery security, encryption, and data residency](https://cloud.google.com/blog/products/identity-security/using-bigquery-encrypt-and-decrypt-with-sensitive-data-protection)

###### Explanation

**Correct option: B**

**Why B is the best architecture**

KnightMotives wants to **monetize corporate and vehicle-generated data**, eliminate **silos** (ERP, plants, telemetry), and enforce **strong security with EU data protection compliance** after prior breaches.

- **BigQuery as a centralized analytics platform** directly addresses data silos by ingesting and analyzing data from heterogeneous sources at scale, enabling advanced analytics and monetization.
- **Regional data residency controls** support EU regulatory requirements by keeping datasets in specific regions.
- **IAM-based access control** enforces least privilege and auditable access for users and services.
- **Customer-managed encryption keys (CMEK)** provide stronger control over encryption and key lifecycle—an explicit need after prior security incidents.

This design aligns with the case study’s requirements for **hybrid modernization**, **data monetization**, and **strict security/privacy controls**.

> [!note]- Why the other options are wrong
> **A. Single on-premises warehouse**
> Limits scalability and advanced analytics, perpetuates legacy constraints, and conflicts with the stated **hybrid/cloud modernization** direction.
>
> **C. Cloud Storage only with ad hoc querying**
> Lacks a governed analytics layer, fine-grained access controls, and enterprise-grade compliance capabilities needed for monetization.
>
> **D. Replicating data into multiple clouds**
> Increases operational complexity and **compliance risk**, making EU data residency harder—not easier—to guarantee.

</details>

---

### Exam 5 · Q19

**KnightMotives Automotive Case Study**

**Company Overview**

KnightMotives is a car manufacturer specializing in autonomous, self-driving vehicles, including Battery Electric Vehicles (BEVs), hybrids, and traditional internal combustion engine (ICE) vehicles. While KnightMotives has made strides with the in-vehicle experience in their BEV fleet, the hybrid and ICE vehicles have yet to implement these new systems and are viewed poorly by critics and drivers. The lack of modern in-vehicle technology in hybrid and ICE vehicles has resulted in declining sales and customer satisfaction.

KnightMotives wants to modernize the consumer experience across all vehicles within five years. Artificial Intelligence offers a unique opportunity to revolutionize the in-vehicle experience, as well as the shopping, buying, and service/maintenance experience. Investment in this new technology will require a shift in financial priorities on a global scale.

KnightMotives also wants to improve their online ordering system, which is unreliable. Systems for customers to build their vehicle online for acquisition through a dealer are not delivering the data or reliability that dealers need, causing a strain in the relationship between KnightMotives and dealers. Service technicians and sales staff need better tooling to enhance dealer successes, including built-to-order vehicles.

**Solution Concept**

KnightMotives wants to shift from manufacturing cars to creating a complete and compelling "automotive experience." Their strategy prioritizes delivering a consistent experience across all models, developing AI-powered features, generating new revenue from data monetization, adopting a digital focus to differentiate their brand from competitors, and developing better tools for mechanics and salespeople.

**Existing Technical Environment**

KnightMotives's IT is largely on-premises with some applications on major cloud platforms. Their supply chain runs on an outdated mainframe, and Enterprise Resource Planning (ERP) is also outdated, making new promotions and dealer discounts difficult to implement. Dealers have no budget for new equipment. There is fragmentation across vehicles with multiple code bases, and significant technical debt from supporting backwards compatibility. Network connectivity to manufacturing plants and vehicle connectivity in rural areas are challenges.

**Business Requirements**

Key business requirements include fostering a personalized relationship with the driver and delivering a cohesive experience across all models. Creating a better build-to-order model will reduce time on the lot and provide transparency for both dealers and customers. Additionally, KnightMotives seeks to monetize corporate data to finance new technology investments, as their current AI infrastructure is obsolete and corporate data remains siloed. Security is a paramount concern due to past data breaches. Adherence to European Union (EU) data protection regulations, especially for emerging autonomous platforms, is critical.

KnightMotives plans to make significant investments in fully autonomous driving capabilities, with initial implementation targeting regions with favorable regulatory environments. Prioritizing employee upskilling, attracting top-tier talent, and fostering better communication between business and technical teams are also critical objectives.

**Technical Requirements**

- Modernizing the in-vehicle experience includes developing a consistent user experience (UX) that seamlessly integrates AI-powered features across all models, updating in-vehicle hardware and software in legacy models to support new UX features and AI capabilities, and ensuring reliable network connectivity, especially in rural areas, to support real-time AI features and data transmission.
- Network upgrades are necessary to support increased data traffic and improve connectivity between plants and headquarters.
- IT infrastructure modernization requires adopting a hybrid cloud strategy to leverage the benefits of both on-premises and cloud infrastructure, and gradually modernizing or replacing legacy systems to improve efficiency and agility. KnightMotives Automotive Case Study 2
- Autonomous vehicle development and testing requires investing in cutting-edge AI and machine learning technologies, building a robust simulation environment, and ensuring compliance with evolving regulations related to autonomous vehicles.
- Data monetization and insights requires implementing a robust data management platform, strict data security and privacy measures, and a scalable AI/ML infrastructure.
- Increased focus on security and risk management involves implementing a comprehensive security framework to protect against cyber threats and data breaches, developing an incident response plan, and providing security awareness training to employees.
- Providing a delightful experience for dealers and customers requires improving the online build-to-order system; developing modern dealer tools to streamline dealer operations, including sales, service, and inventory management; and implementing a comprehensive Customer Relationship Management (CRM) system to track customer interactions, personalize experiences, and improve customer satisfaction.

**Executive Statement**

KnightMotives is committed to enhancing safety and saving lives by leveraging an extensive body of data—encompassing driving, road conditions, behavioral studies, and crash safety statistics—to create compelling digital experiences for drivers. Our AI consistently outperforms national safety statistics, ensuring the unique and coveted KnightMotives experience is aligned across all our vehicle models.

Michael Knight, KnightMotives CEO

---

**Question:**

**KnightMotives needs to modernize its unreliable online build-to-order system used by customers and dealers. The solution must improve reliability, provide transparency into order status, and integrate with legacy supply chain and ERP systems during a multi-year transition.**

**Which approach best satisfies these goals?**

- A. Replace the entire ERP and supply chain system in a single migration to cloud-native services.
- B. Build a cloud-native ordering platform with API-based integration to legacy systems, using asynchronous messaging to decouple dependencies.
- C. Continue using the existing system but scale it vertically on larger on-premises servers.
- D. Move the existing application unchanged to virtual machines in the cloud.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Build a cloud-native ordering platform with API-based integration to legacy systems, using asynchronous messaging to decouple dependencies.

**Correct option: B. Build a cloud-native ordering platform with API-based integration to legacy systems, using asynchronous messaging to decouple dependencies.**

**Why B best satisfies the goals**

KnightMotives needs to **improve reliability**, **give customers and dealers transparency into order status**, and **integrate with legacy ERP and supply-chain systems over a multi-year transition**.

- A **cloud-native ordering platform** improves availability, scalability, and user experience compared to the legacy system.
- **API-based integration** allows the new platform to interact with existing ERP and supply-chain systems without forcing a risky “big-bang” replacement.
- **Asynchronous messaging** (for example, event-driven workflows) decouples the ordering system from downstream dependencies, improving reliability and enabling real-time order status updates even when legacy systems are slow or temporarily unavailable.
- This pattern directly supports **incremental modernization**, which aligns with KnightMotives’ long-term transformation roadmap.

**Why the other options are not suitable**

- **A. Single-step ERP replacement**
  High risk, long timelines, and disruption to dealers and customers; contradicts the need for a gradual transition.
- **C. Vertical scaling on-premises**
  Increases cost but does not address architectural fragility, integration challenges, or transparency.
- **D. Lift-and-shift to VMs**
  Improves hosting location but **does not improve reliability or architecture**; legacy coupling and failures remain.

**Authoritative documentation link**
Event-driven and API-based modernization patterns on Google Cloud:
[https://docs.cloud.google.com/solutions/event-driven-architecture-pubsub](https://docs.cloud.google.com/solutions/event-driven-architecture-pubsub)

###### Explanation

**Correct option: B**

**Why B best satisfies the goals**

KnightMotives needs to **improve reliability**, **give customers and dealers transparency into order status**, and **integrate with legacy ERP and supply-chain systems over a multi-year transition**.

- A **cloud-native ordering platform** improves availability, scalability, and user experience compared to the legacy system.
- **API-based integration** allows the new platform to interact with existing ERP and supply-chain systems without forcing a risky “big-bang” replacement.
- **Asynchronous messaging** (for example, event-driven workflows) decouples the ordering system from downstream dependencies, improving reliability and enabling real-time order status updates even when legacy systems are slow or temporarily unavailable.
- This pattern directly supports **incremental modernization**, which aligns with KnightMotives’ long-term transformation roadmap.

> [!note]- Why the other options are wrong
> **A. Single-step ERP replacement**
> High risk, long timelines, and disruption to dealers and customers; contradicts the need for a gradual transition.
>
> **C. Vertical scaling on-premises**
> Increases cost but does not address architectural fragility, integration challenges, or transparency.
>
> **D. Lift-and-shift to VMs**
> Improves hosting location but **does not improve reliability or architecture**; legacy coupling and failures remain.

</details>

---

### Exam 5 · Q20

**KnightMotives Automotive Case Study**

**Company Overview**

KnightMotives is a car manufacturer specializing in autonomous, self-driving vehicles, including Battery Electric Vehicles (BEVs), hybrids, and traditional internal combustion engine (ICE) vehicles. While KnightMotives has made strides with the in-vehicle experience in their BEV fleet, the hybrid and ICE vehicles have yet to implement these new systems and are viewed poorly by critics and drivers. The lack of modern in-vehicle technology in hybrid and ICE vehicles has resulted in declining sales and customer satisfaction.

KnightMotives wants to modernize the consumer experience across all vehicles within five years. Artificial Intelligence offers a unique opportunity to revolutionize the in-vehicle experience, as well as the shopping, buying, and service/maintenance experience. Investment in this new technology will require a shift in financial priorities on a global scale.

KnightMotives also wants to improve their online ordering system, which is unreliable. Systems for customers to build their vehicle online for acquisition through a dealer are not delivering the data or reliability that dealers need, causing a strain in the relationship between KnightMotives and dealers. Service technicians and sales staff need better tooling to enhance dealer successes, including built-to-order vehicles.

**Solution Concept**

KnightMotives wants to shift from manufacturing cars to creating a complete and compelling "automotive experience." Their strategy prioritizes delivering a consistent experience across all models, developing AI-powered features, generating new revenue from data monetization, adopting a digital focus to differentiate their brand from competitors, and developing better tools for mechanics and salespeople.

**Existing Technical Environment**

KnightMotives's IT is largely on-premises with some applications on major cloud platforms. Their supply chain runs on an outdated mainframe, and Enterprise Resource Planning (ERP) is also outdated, making new promotions and dealer discounts difficult to implement. Dealers have no budget for new equipment. There is fragmentation across vehicles with multiple code bases, and significant technical debt from supporting backwards compatibility. Network connectivity to manufacturing plants and vehicle connectivity in rural areas are challenges.

**Business Requirements**

Key business requirements include fostering a personalized relationship with the driver and delivering a cohesive experience across all models. Creating a better build-to-order model will reduce time on the lot and provide transparency for both dealers and customers. Additionally, KnightMotives seeks to monetize corporate data to finance new technology investments, as their current AI infrastructure is obsolete and corporate data remains siloed. Security is a paramount concern due to past data breaches. Adherence to European Union (EU) data protection regulations, especially for emerging autonomous platforms, is critical.

KnightMotives plans to make significant investments in fully autonomous driving capabilities, with initial implementation targeting regions with favorable regulatory environments. Prioritizing employee upskilling, attracting top-tier talent, and fostering better communication between business and technical teams are also critical objectives.

**Technical Requirements**

- Modernizing the in-vehicle experience includes developing a consistent user experience (UX) that seamlessly integrates AI-powered features across all models, updating in-vehicle hardware and software in legacy models to support new UX features and AI capabilities, and ensuring reliable network connectivity, especially in rural areas, to support real-time AI features and data transmission.
- Network upgrades are necessary to support increased data traffic and improve connectivity between plants and headquarters.
- IT infrastructure modernization requires adopting a hybrid cloud strategy to leverage the benefits of both on-premises and cloud infrastructure, and gradually modernizing or replacing legacy systems to improve efficiency and agility. KnightMotives Automotive Case Study 2
- Autonomous vehicle development and testing requires investing in cutting-edge AI and machine learning technologies, building a robust simulation environment, and ensuring compliance with evolving regulations related to autonomous vehicles.
- Data monetization and insights requires implementing a robust data management platform, strict data security and privacy measures, and a scalable AI/ML infrastructure.
- Increased focus on security and risk management involves implementing a comprehensive security framework to protect against cyber threats and data breaches, developing an incident response plan, and providing security awareness training to employees.
- Providing a delightful experience for dealers and customers requires improving the online build-to-order system; developing modern dealer tools to streamline dealer operations, including sales, service, and inventory management; and implementing a comprehensive Customer Relationship Management (CRM) system to track customer interactions, personalize experiences, and improve customer satisfaction.

**Executive Statement**

KnightMotives is committed to enhancing safety and saving lives by leveraging an extensive body of data—encompassing driving, road conditions, behavioral studies, and crash safety statistics—to create compelling digital experiences for drivers. Our AI consistently outperforms national safety statistics, ensuring the unique and coveted KnightMotives experience is aligned across all our vehicle models.

Michael Knight, KnightMotives CEO

---

**Question:**

**KnightMotives is investing heavily in autonomous vehicle development and requires large-scale simulation, model training, and testing. The solution must scale globally, support evolving regulations, and optimize cost while accelerating innovation.**

**Which architecture should you recommend?**

- A. Use Compute Engine VMs with fixed GPU allocations and manual scaling for training workloads.
- B. Leverage Vertex AI with scalable training pipelines, managed datasets, and region-specific deployments for regulatory compliance.
- C. Train models exclusively on in-vehicle hardware to reflect real-world conditions.
- D. Perform all simulations on-premises to avoid regulatory and data sovereignty risks.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Leverage Vertex AI with scalable training pipelines, managed datasets, and region-specific deployments for regulatory compliance.

**Correct option: B. . Leverage Vertex AI with scalable training pipelines, managed datasets, and region-specific deployments for regulatory compliance.**

**Why B is the best architecture**

KnightMotives needs to support **large-scale simulation, model training, and testing** for autonomous vehicles while ensuring **global scalability**, **regulatory compliance**, **cost optimization**, and **fast innovation cycles**.

- **Vertex AI** provides **managed, scalable training pipelines** that can elastically scale GPU/TPU resources up and down, avoiding the cost inefficiencies of fixed infrastructure.
- **Managed datasets and experiment tracking** support rapid iteration, reproducibility, and governance—critical for safety-critical autonomous systems.
- **Region-specific deployments** allow training, testing, and data storage to remain within required geographies, supporting evolving **EU and global data protection regulations**.
- This approach aligns with KnightMotives’ stated direction toward **hybrid/cloud modernization** and avoids long-term operational burden while accelerating AI innovation.

**Why the other options are not suitable**

- **A. Fixed GPU VMs with manual scaling**
  Leads to poor cost efficiency, slower experimentation, and high operational overhead—unsuitable for rapidly evolving autonomous workloads.
- **C. Training exclusively on in-vehicle hardware**
  Vehicles are constrained in compute, power, and scalability; this approach cannot support large-scale simulation or model iteration.
- **D. All simulations on-premises**
  Limits global scalability, slows innovation, and contradicts the requirement to modernize using cloud capabilities while managing cost.

**Single authoritative documentation link**
Vertex AI training and scalable ML pipelines:
[https://cloud.google.com/vertex-ai/docs/training/overview](https://cloud.google.com/vertex-ai/docs/training/overview)

###### Explanation

**Correct option: B. . Leverage Vertex AI with scalable training pipelines, managed datasets, and region-specific deployments for regulatory compliance.**

**Why B is the best architecture**

KnightMotives needs to support **large-scale simulation, model training, and testing** for autonomous vehicles while ensuring **global scalability**, **regulatory compliance**, **cost optimization**, and **fast innovation cycles**.

- **Vertex AI** provides **managed, scalable training pipelines** that can elastically scale GPU/TPU resources up and down, avoiding the cost inefficiencies of fixed infrastructure.
- **Managed datasets and experiment tracking** support rapid iteration, reproducibility, and governance—critical for safety-critical autonomous systems.
- **Region-specific deployments** allow training, testing, and data storage to remain within required geographies, supporting evolving **EU and global data protection regulations**.
- This approach aligns with KnightMotives’ stated direction toward **hybrid/cloud modernization** and avoids long-term operational burden while accelerating AI innovation.

> [!note]- Why the other options are wrong
> **A. Fixed GPU VMs with manual scaling**
> Leads to poor cost efficiency, slower experimentation, and high operational overhead—unsuitable for rapidly evolving autonomous workloads.
>
> **C. Training exclusively on in-vehicle hardware**
> Vehicles are constrained in compute, power, and scalability; this approach cannot support large-scale simulation or model iteration.
>
> **D. All simulations on-premises**
> Limits global scalability, slows innovation, and contradicts the requirement to modernize using cloud capabilities while managing cost.

</details>

---

### Exam 5 · Q23

**KnightMotives Automotive Case Study**

**Company Overview**

KnightMotives is a car manufacturer specializing in autonomous, self-driving vehicles, including Battery Electric Vehicles (BEVs), hybrids, and traditional internal combustion engine (ICE) vehicles. While KnightMotives has made strides with the in-vehicle experience in their BEV fleet, the hybrid and ICE vehicles have yet to implement these new systems and are viewed poorly by critics and drivers. The lack of modern in-vehicle technology in hybrid and ICE vehicles has resulted in declining sales and customer satisfaction.

KnightMotives wants to modernize the consumer experience across all vehicles within five years. Artificial Intelligence offers a unique opportunity to revolutionize the in-vehicle experience, as well as the shopping, buying, and service/maintenance experience. Investment in this new technology will require a shift in financial priorities on a global scale.

KnightMotives also wants to improve their online ordering system, which is unreliable. Systems for customers to build their vehicle online for acquisition through a dealer are not delivering the data or reliability that dealers need, causing a strain in the relationship between KnightMotives and dealers. Service technicians and sales staff need better tooling to enhance dealer successes, including built-to-order vehicles.

**Solution Concept**

KnightMotives wants to shift from manufacturing cars to creating a complete and compelling "automotive experience." Their strategy prioritizes delivering a consistent experience across all models, developing AI-powered features, generating new revenue from data monetization, adopting a digital focus to differentiate their brand from competitors, and developing better tools for mechanics and salespeople.

**Existing Technical Environment**

KnightMotives's IT is largely on-premises with some applications on major cloud platforms. Their supply chain runs on an outdated mainframe, and Enterprise Resource Planning (ERP) is also outdated, making new promotions and dealer discounts difficult to implement. Dealers have no budget for new equipment. There is fragmentation across vehicles with multiple code bases, and significant technical debt from supporting backwards compatibility. Network connectivity to manufacturing plants and vehicle connectivity in rural areas are challenges.

**Business Requirements**

Key business requirements include fostering a personalized relationship with the driver and delivering a cohesive experience across all models. Creating a better build-to-order model will reduce time on the lot and provide transparency for both dealers and customers. Additionally, KnightMotives seeks to monetize corporate data to finance new technology investments, as their current AI infrastructure is obsolete and corporate data remains siloed. Security is a paramount concern due to past data breaches. Adherence to European Union (EU) data protection regulations, especially for emerging autonomous platforms, is critical.

KnightMotives plans to make significant investments in fully autonomous driving capabilities, with initial implementation targeting regions with favorable regulatory environments. Prioritizing employee upskilling, attracting top-tier talent, and fostering better communication between business and technical teams are also critical objectives.

**Technical Requirements**

- Modernizing the in-vehicle experience includes developing a consistent user experience (UX) that seamlessly integrates AI-powered features across all models, updating in-vehicle hardware and software in legacy models to support new UX features and AI capabilities, and ensuring reliable network connectivity, especially in rural areas, to support real-time AI features and data transmission.
- Network upgrades are necessary to support increased data traffic and improve connectivity between plants and headquarters.
- IT infrastructure modernization requires adopting a hybrid cloud strategy to leverage the benefits of both on-premises and cloud infrastructure, and gradually modernizing or replacing legacy systems to improve efficiency and agility. KnightMotives Automotive Case Study 2
- Autonomous vehicle development and testing requires investing in cutting-edge AI and machine learning technologies, building a robust simulation environment, and ensuring compliance with evolving regulations related to autonomous vehicles.
- Data monetization and insights requires implementing a robust data management platform, strict data security and privacy measures, and a scalable AI/ML infrastructure.
- Increased focus on security and risk management involves implementing a comprehensive security framework to protect against cyber threats and data breaches, developing an incident response plan, and providing security awareness training to employees.
- Providing a delightful experience for dealers and customers requires improving the online build-to-order system; developing modern dealer tools to streamline dealer operations, including sales, service, and inventory management; and implementing a comprehensive Customer Relationship Management (CRM) system to track customer interactions, personalize experiences, and improve customer satisfaction.

**Executive Statement**

KnightMotives is committed to enhancing safety and saving lives by leveraging an extensive body of data—encompassing driving, road conditions, behavioral studies, and crash safety statistics—to create compelling digital experiences for drivers. Our AI consistently outperforms national safety statistics, ensuring the unique and coveted KnightMotives experience is aligned across all our vehicle models.

Michael Knight, KnightMotives CEO

---

**For this question, refer to the KnightMotives Automotive case study. As part of building fully autonomous vehicles, KnightMotives wants to analyze all sensor data collected during test drives so they can improve their driving software.**

**• Multiple event types such as parking, overtaking, and navigation must be analyzed, and each event for each vehicle has its own ID.

- Several sensor categories such as cameras, radar, and ultrasonic sensors are involved. During every autonomous event, readings from many sensors are captured and stored in Bigtable.**

**During analysis, you must efficiently retrieve all sensor data for the same event type for a specific vehicle within a given time range. You need a Bigtable schema optimized for read performance. What should you do?**

- A. Use sensor category, event ID, and timestamp (in that order) as the row key. Create a column family for each individual sensor and use a column qualifier for each vehicle.
- B. Use timestamp, vehicle ID, and event ID (in that order) as the row key. Create a column family per sensor category and a column qualifier for each sensor within that category.
- C. Use vehicle ID, event ID, and timestamp (in that order) as the row key. Create a column family per sensor category and a column qualifier for each sensor within that category.
- D. Use vehicle ID and event ID (in that order) as the row key. Create a column family per sensor category and a column qualifier for each sensor within that category, and rely on cell timestamp versions to distinguish different moments in time.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Use vehicle ID, event ID, and timestamp (in that order) as the row key. Create a column family per sensor category and a column qualifier for each sensor within that category.

**Correct answer: C**

**Use vehicle ID, event ID, and timestamp (in that order) as the row key. Create a column family per sensor category and a column qualifier for each sensor within that category.**

**Why option C is correct**

The query pattern is the most important driver of Bigtable schema design. KnightMotives needs to retrieve:

- all sensor data
- for a specific vehicle
- for a specific event type
- within a time range

Bigtable is optimized for **prefix scans on row keys**. To achieve efficient reads, the row key must begin with the most selective fields used in queries.

Option C structures the row key as:

vehicle ID → event ID → timestamp

This enables:

- fast prefix scans for a specific vehicle
- narrowing to a specific event
- efficient range scans by timestamp

Because timestamps are ordered, Bigtable can scan only the relevant rows instead of scanning the entire table.

The column design is also correct:

- column family per sensor category (camera, radar, ultrasonic)
- column qualifier per individual sensor

This matches Bigtable best practice: column families should be small and stable, while qualifiers can be flexible and numerous.

**Official documentation explaining Bigtable schema design principles:**
[https://cloud.google.com/bigtable/docs/schema-design](https://cloud.google.com/bigtable/docs/schema-design)

**Why the other options are not the best choice**

**Option A**

The row key starts with sensor category instead of vehicle ID. This forces scans across many vehicles just to find data for one vehicle. It breaks the primary access pattern and causes inefficient wide scans.

Also, creating a column family per sensor and using vehicles as qualifiers is backwards. Column families should be few and stable, not explode in count.

**Option B**

This puts timestamp first in the row key. That means data is organized primarily by time across all vehicles and events. To fetch data for one vehicle/event, Bigtable must scan across many unrelated rows, which is inefficient.

Time-first row keys are only good when time is the dominant access pattern, which is not the case here.

**Option D**

This removes timestamp from the row key and relies on cell version timestamps. That prevents efficient time-range scans. Bigtable version timestamps are not a substitute for ordered row keys when time filtering is a core query requirement.

You would end up reading too much data and filtering client-side.

**Need-to-know foundational concept**

Bigtable schema design follows one golden rule:

Design the row key around your read pattern.

Key principles:

- Bigtable is a sorted key-value store
- Reads are efficient only when they align with row key ordering
- Prefix scans are fast; scattered reads are expensive
- Put the most selective query dimensions first
- Use timestamps last when time-range queries are needed
- Keep column families small and stable

For analytics systems like autonomous vehicle telemetry, correct row-key design determines whether queries run in milliseconds or minutes.

###### Explanation

**Correct answer: C**

**Use vehicle ID, event ID, and timestamp (in that order) as the row key. Create a column family per sensor category and a column qualifier for each sensor within that category.**

**Why option C is correct**

The query pattern is the most important driver of Bigtable schema design. KnightMotives needs to retrieve:

- all sensor data
- for a specific vehicle
- for a specific event type
- within a time range

Bigtable is optimized for **prefix scans on row keys**. To achieve efficient reads, the row key must begin with the most selective fields used in queries.

Option C structures the row key as:

vehicle ID → event ID → timestamp

This enables:

- fast prefix scans for a specific vehicle
- narrowing to a specific event
- efficient range scans by timestamp

Because timestamps are ordered, Bigtable can scan only the relevant rows instead of scanning the entire table.

The column design is also correct:

- column family per sensor category (camera, radar, ultrasonic)
- column qualifier per individual sensor

This matches Bigtable best practice: column families should be small and stable, while qualifiers can be flexible and numerous.

> [!note]- Why the other options are wrong
> **Option A**
>
> The row key starts with sensor category instead of vehicle ID. This forces scans across many vehicles just to find data for one vehicle. It breaks the primary access pattern and causes inefficient wide scans.
>
> Also, creating a column family per sensor and using vehicles as qualifiers is backwards. Column families should be few and stable, not explode in count.
>
> **Option B**
>
> This puts timestamp first in the row key. That means data is organized primarily by time across all vehicles and events. To fetch data for one vehicle/event, Bigtable must scan across many unrelated rows, which is inefficient.
>
> Time-first row keys are only good when time is the dominant access pattern, which is not the case here.
>
> **Option D**
>
> This removes timestamp from the row key and relies on cell version timestamps. That prevents efficient time-range scans. Bigtable version timestamps are not a substitute for ordered row keys when time filtering is a core query requirement.

</details>

---

### Exam 5 · Q42

**You are preparing to migrate your on-premises compute and SAP workloads to Google Cloud. You want to follow Google-recommended best practices to quickly produce a cost estimate for running these workloads in Google Cloud. What should you do?**

- A. Use **Cloud Asset Inventory** to collect environment details and generate a cost estimate.
- B. Use the **Google Cloud Pricing Calculator** and enter estimated resource requirements to produce a cost estimate.
- C. Work with a **Google Cloud partner** to perform a full assessment and deliver a tailored cost estimate.
- D. Collect details about your current environment and use **Google Cloud Migration Center** to generate a cost estimate.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Collect details about your current environment and use **Google Cloud Migration Center** to generate a cost estimate.

**Correct Answer: D**

**Collect details about your current environment and use Google Cloud Migration Center to generate a cost estimate.**

**Why D is correct**

For migrating **on-prem compute + SAP workloads**, Google-recommended best practice is to use **Google Cloud Migration Center** because it is designed to:

- **Discover and assess** your current on-prem environment (VMs, utilization, sizing)
- **Group workloads** and model migration scenarios
- Produce a **quick, data-driven cost estimate** based on actual observed usage (more accurate than guesswork)

This is the fastest and most reliable way to estimate costs for a migration.

**Why the other options are incorrect / not best fit**

**A. Cloud Asset Inventory**

Cloud Asset Inventory inventories **Google Cloud resources**, not on-prem infrastructure. It won’t help you estimate on-prem migration costs.

**B. Google Cloud Pricing Calculator (manual inputs)**

This can work, but it’s **manual and assumption-based**, and less accurate for SAP + large migrations compared to Migration Center’s assessment-driven approach.

**C. Work with a partner for full assessment**

Partners can help, but this is not the fastest way to “quickly produce a cost estimate.” It’s heavier-weight than required for an initial estimate.

**Need-to-know fundamentals**

- **Pricing Calculator** is good for quick rough estimates when you already know sizing.
- **Migration Center** is best for migration planning because it uses **discovery + assessment** to generate estimates and recommendations.
- For SAP, accuracy matters because sizing, memory, and sustained usage heavily affect cost.

**Official documentation link:**

[Migration Center overview](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)

###### Explanation

**Why D is correct**

For migrating **on-prem compute + SAP workloads**, Google-recommended best practice is to use **Google Cloud Migration Center** because it is designed to:

- **Discover and assess** your current on-prem environment (VMs, utilization, sizing)
- **Group workloads** and model migration scenarios
- Produce a **quick, data-driven cost estimate** based on actual observed usage (more accurate than guesswork)

> [!note]- Why the other options are wrong
> A. Cloud Asset Inventory
>
> Cloud Asset Inventory inventories **Google Cloud resources**, not on-prem infrastructure. It won’t help you estimate on-prem migration costs.
>
> B. Google Cloud Pricing Calculator (manual inputs)
>
> This can work, but it’s **manual and assumption-based**, and less accurate for SAP + large migrations compared to Migration Center’s assessment-driven approach.
>
> C. Work with a partner for full assessment
>
> Partners can help, but this is not the fastest way to “quickly produce a cost estimate.” It’s heavier-weight than required for an initial estimate.

</details>

---

### Exam 5 · Q47

**You are designing the architecture for a global social media website on Google Cloud. The site delivers dynamic API responses, static content such as CSS/JS/images, and user-uploaded videos for streaming. You want to reduce latency worldwide for all content types. What should you do? (Choose two.)**

- A. Use an external **Application Load Balancer** to deliver your application APIs.
- B. Use **Cloud CDN** to deliver the application’s static assets.
- C. Use **Media CDN** to deliver the application’s static assets.
- D. Use **Memorystore** to deliver your web application.
- E. Use a **multi-region Cloud Storage** bucket to host and serve the entire web application.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Use an external **Application Load Balancer** to deliver your application APIs. **|** B. Use **Cloud CDN** to deliver the application’s static assets.

**Correct Answers: A and B**

**A. Use an external Application Load Balancer to deliver your application APIs.**
**B. Use Cloud CDN to deliver the application’s static assets.**

Why **A** is correct

A global social media site needs low-latency delivery for **dynamic API responses**. An **external Application Load Balancer** provides global anycast IPs, intelligent routing, and integrates cleanly with backend services for dynamic traffic.

It’s the right front door for worldwide API delivery.

**Official documentation:**
[https://cloud.google.com/load-balancing/docs/https](https://cloud.google.com/load-balancing/docs/https)

Why **B** is correct

For **static assets** like CSS, JS, and images, **Cloud CDN** caches content at Google’s edge locations, dramatically reducing latency and offloading traffic from your origin.

**Official documentation:**
[https://cloud.google.com/cdn/docs/overview](https://cloud.google.com/cdn/docs/overview)

**Why the other options are incorrect / not best fit**

**C. Media CDN to deliver static assets**

Media CDN is optimized for **large-scale video streaming and media delivery**, not general static web assets like CSS/JS/images.

**D. Memorystore to deliver your web application**

Memorystore is an in-memory cache (Redis/Memcached). It helps accelerate data access but is not a global content delivery solution.

**E. Multi-region Cloud Storage to host and serve the entire web application**

Multi-region Cloud Storage improves availability, but it does not provide edge caching like a CDN, and it doesn’t handle dynamic APIs.

###### Explanation

Why **A** is correct

A global social media site needs low-latency delivery for **dynamic API responses**. An **external Application Load Balancer** provides global anycast IPs, intelligent routing, and integrates cleanly with backend services for dynamic traffic.

It’s the right front door for worldwide API delivery.

Why **B** is correct

For **static assets** like CSS, JS, and images, **Cloud CDN** caches content at Google’s edge locations, dramatically reducing latency and offloading traffic from your origin.

> [!note]- Why the other options are wrong
> C. Media CDN to deliver static assets
>
> Media CDN is optimized for **large-scale video streaming and media delivery**, not general static web assets like CSS/JS/images.
>
> D. Memorystore to deliver your web application
>
> Memorystore is an in-memory cache (Redis/Memcached). It helps accelerate data access but is not a global content delivery solution.
>
> E. Multi-region Cloud Storage to host and serve the entire web application
>
> Multi-region Cloud Storage improves availability, but it does not provide edge caching like a CDN, and it doesn’t handle dynamic APIs.

</details>

---

### Exam 5 · Q48

**Your company uses Salesforce for CRM, ServiceNow for IT service management, and a Cloud SQL database to store customer transaction records. You need a solution that can reliably connect these systems, perform data mapping and transformations, and keep data consistent while supporting near real-time reporting. You want to follow Google-recommended best practices. What should you do?**

- A. Use **Workflows** to integrate the services and apply data transformations.
- B. Use **Application Integration** to integrate the services and apply data transformations.
- C. Use **Pub/Sub** and **BigQuery** to integrate the services and apply data transformations.
- D. Use **Pub/Sub** and **Datastream** to integrate the services and apply data transformations.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use **Application Integration** to integrate the services and apply data transformations.

**Correct Answer: B**

**Use Application Integration to integrate the services and apply data mapping and transformations.**

**Why B is correct**

You need a solution that:

- reliably connects **Salesforce**, **ServiceNow**, and **Cloud SQL**
- supports **data mapping + transformations**
- keeps data consistent
- supports **near real-time reporting**
- follows **Google-recommended integration best practices**

**Application Integration** (part of Google Cloud’s integration platform) is designed for exactly this: connecting SaaS systems and Google Cloud services using **prebuilt connectors**, orchestration, transformation, and error handling in a managed way.

It is a best-practice fit for enterprise integration across CRM/ITSM + databases.

**Official documentation:**
[https://cloud.google.com/application-integration/docs/overview](https://cloud.google.com/application-integration/docs/overview)

**Why the other options are incorrect / not best fit**

**A. Workflows**

Workflows is great for orchestrating Google Cloud services and calling APIs, but it is not the best primary tool for **enterprise SaaS integration with mapping/transformations and connector-based consistency** at scale.

**C. Pub/Sub + BigQuery**

Pub/Sub + BigQuery is excellent for streaming analytics, but it does not directly provide the **connector + transformation + orchestration** capabilities needed to integrate Salesforce and ServiceNow reliably without building more custom glue.

**D. Pub/Sub + Datastream**

Datastream is focused on **CDC replication** (typically from databases like MySQL/PostgreSQL/Oracle) into destinations like BigQuery or Cloud Storage. It is not meant for integrating SaaS systems like Salesforce and ServiceNow with mapping/transformation logic.

Need-to-know fundamentals

- **Application Integration** is for SaaS + cloud service integration with mapping and transformations.
- **Pub/Sub** is messaging/event transport, not full integration orchestration.
- **Datastream** is database CDC replication, not SaaS integration.

###### Explanation

**Why B is correct**

**You need a solution that:**

- reliably connects **Salesforce**, **ServiceNow**, and **Cloud SQL**
- supports **data mapping + transformations**
- keeps data consistent
- supports **near real-time reporting**
- follows **Google-recommended integration best practices**

**Application Integration** (part of Google Cloud’s integration platform) is designed for exactly this: connecting SaaS systems and Google Cloud services using **prebuilt connectors**, orchestration, transformation, and error handling in a managed way.

It is a best-practice fit for enterprise integration across CRM/ITSM + databases.

> [!note]- Why the other options are wrong
> A. Workflows
>
> Workflows is great for orchestrating Google Cloud services and calling APIs, but it is not the best primary tool for **enterprise SaaS integration with mapping/transformations and connector-based consistency** at scale.
>
> C. Pub/Sub + BigQuery
>
> Pub/Sub + BigQuery is excellent for streaming analytics, but it does not directly provide the **connector + transformation + orchestration** capabilities needed to integrate Salesforce and ServiceNow reliably without building more custom glue.
>
> D. Pub/Sub + Datastream
>
> Datastream is focused on **CDC replication** (typically from databases like MySQL/PostgreSQL/Oracle) into destinations like BigQuery or Cloud Storage. It is not meant for integrating SaaS systems like Salesforce and ServiceNow with mapping/transformation logic.

</details>

---

### Exam 5 · Q55

**A large healthcare provider runs its primary electronic health record application on Compute Engine with a Cloud SQL for PostgreSQL database in us-west1. A new regulation requires a formal disaster recovery plan that guarantees recovery in another region with an RTO of 2 hours and an RPO of 15 minutes. You must design a strategy that satisfies these strict business continuity requirements. What should you do?**

- A. Run active managed instance groups in both us-west1 and us-east1 behind a global external HTTP(S) Load Balancer. Use a cross-region Cloud SQL read replica in us-east1 and allow the load balancer to fail over traffic automatically.
- B. Define infrastructure with Terraform. In a disaster, create infrastructure in us-east1, configure a cross-region Cloud SQL replica there, and promote it.
- C. Take daily snapshots of Compute Engine disks and the Cloud SQL database, copy them to Cloud Storage in us-east1, and restore manually during an outage.
- D. Deploy a regional MIG in us-west1 and depend on the regional SLA for availability.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Run active managed instance groups in both us-west1 and us-east1 behind a global external HTTP(S) Load Balancer. Use a cross-region Cloud SQL read replica in us-east1 and allow the load balancer to fail over traffic automatically.

**Correct option: A. Run active managed instance groups in both regions and use a cross-region Cloud SQL read replica.**

**Need-to-know foundational concept**

RTO and RPO drive architecture decisions:

- **RTO (Recovery Time Objective)** = how fast you must be back online
- **RPO (Recovery Point Objective)** = how much data you can afford to lose

An RPO of 15 minutes means replication must be continuous and near real time.
An RTO of 2 hours means the standby environment must already exist — you cannot build it from scratch during a disaster.

This pushes you toward a **warm standby / active-active architecture** with cross-region replication already running. Cloud SQL cross-region read replicas continuously replicate WAL changes and can be promoted quickly during a failure, supporting strict DR objectives.

**Google documents cross-region replicas specifically as a disaster recovery mechanism:**
[https://cloud.google.com/sql/docs/postgres/replication/cross-region-replicas](https://cloud.google.com/sql/docs/postgres/replication/cross-region-replicas)

**Why the correct option fits the scenario**

Option A keeps compute capacity already running in both regions and maintains a continuously replicated Cloud SQL instance. In a disaster:

- Traffic can fail over immediately to the secondary region
- The replica can be promoted quickly
- Data loss stays within the 15-minute RPO window
- Recovery happens well inside a 2-hour RTO

This is exactly what a formal, guaranteed DR architecture requires: pre-provisioned infrastructure + live replication.

**Why the other options are not the best choice**

**B. Terraform + create infra during disaster**
Creating infrastructure after a failure violates the RTO requirement. Provisioning compute, networking, and database promotion under pressure can exceed 2 hours. DR environments must already exist for strict RTO guarantees.

**C. Daily snapshots**
Daily backups produce a 24-hour RPO, which completely fails the 15-minute requirement. Snapshots are for backup and restore, not low-RPO disaster recovery.

**D. Regional SLA only**
A regional deployment protects against zone failure, not region failure. The requirement explicitly demands recovery in another region. This option does not meet regulatory DR requirements.

The only strategy that simultaneously satisfies cross-region recovery, sub-hour RPO, and fast failover is an always-replicating standby architecture with Cloud SQL cross-region replicas and active compute capacity.

###### Explanation

**Correct option: A. Run active managed instance groups in both regions and use a cross-region Cloud SQL read replica.**

**Need-to-know foundational concept**

RTO and RPO drive architecture decisions:

- **RTO (Recovery Time Objective)** = how fast you must be back online
- **RPO (Recovery Point Objective)** = how much data you can afford to lose

An RPO of 15 minutes means replication must be continuous and near real time.
An RTO of 2 hours means the standby environment must already exist — you cannot build it from scratch during a disaster.

> [!note]- Why the other options are wrong
> **B. Terraform + create infra during disaster**
> Creating infrastructure after a failure violates the RTO requirement. Provisioning compute, networking, and database promotion under pressure can exceed 2 hours. DR environments must already exist for strict RTO guarantees.
>
> **C. Daily snapshots**
> Daily backups produce a 24-hour RPO, which completely fails the 15-minute requirement. Snapshots are for backup and restore, not low-RPO disaster recovery.
>
> **D. Regional SLA only**
> A regional deployment protects against zone failure, not region failure. The requirement explicitly demands recovery in another region. This option does not meet regulatory DR requirements.

</details>

---

### Exam 5 · Q58

**A retail company’s most business-critical workload is its online payment processing application. The business requires that the system continue operating through a full zonal outage while keeping costs as low as possible. You need an architecture that tolerates a zone failure. What should you do?**

- A. Run the application in an active-active setup using managed instance groups in two separate regions, fronted by a global external HTTP(S) Load Balancer, and use a multi-regional database such as Spanner.
- B. Deploy the application using a regional managed instance group to provide availability across multiple zones within the primary region.
- C. Configure the regional managed instance group to use only Spot VMs to reduce cost while still providing high availability.
- D. Deploy the application on Compute Engine across multiple regions and rely on daily snapshots for recovery to minimize cost.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Deploy the application using a regional managed instance group to provide availability across multiple zones within the primary region.

**Correct option: B. Deploy the application using a regional managed instance group to provide availability across multiple zones within the primary region.**

**Need-to-know foundational concept**

A “full zonal outage” means one zone is unavailable, but the rest of the region is still healthy. The lowest-cost architecture that can survive a zone failure is **multi-zone within a single region**, not multi-region. A **regional Managed Instance Group (MIG)** is designed for exactly this: it spreads instances across multiple zones in the same region so the workload can continue serving if a zone fails.

**Why the correct option fits the scenario**

Option B gives zonal-failure tolerance at minimal added cost:

- Instances are distributed across multiple zones in one region.
- If one zone goes down, instances in the remaining zone(s) keep serving traffic.
- You avoid the higher operational and data costs of multi-region active-active.

Google explicitly states that a regional MIG deploys instances to multiple zones across the same region and improves availability by protecting against zonal failure.

**Why the other options are not the best choice**

**A. Active-active across two regions + global LB + Spanner**
This is more than what’s required (multi-region resilience), and it is significantly more expensive (duplicate regional stacks + a premium multi-region database like Spanner). It does tolerate a zone outage, but it does not meet “keep costs as low as possible.”

**C. Use only Spot VMs**
Spot VMs can be preempted at any time and are not appropriate for a business-critical payment system where you need predictable availability. Spot can reduce cost, but it increases the risk of disruption unrelated to zonal failure.

**D. Multi-region compute + daily snapshots**
Daily snapshots don’t provide continuity through a zonal outage; they are a backup/recovery mechanism, not high availability. Also, relying on restore processes during failure conflicts with “continue operating” requirements.

**Authoritative reference: Regional MIGs for multi-zone availability in a region**
[https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs?utm_source=chatgpt.com)

###### Explanation

**Correct option: B.**

**Why the correct option fits the scenario**

Option B gives zonal-failure tolerance at minimal added cost:

- Instances are distributed across multiple zones in one region.
- If one zone goes down, instances in the remaining zone(s) keep serving traffic.
- You avoid the higher operational and data costs of multi-region active-active.

Google explicitly states that a regional MIG deploys instances to multiple zones across the same region and improves availability by protecting against zonal failure.

> [!note]- Why the other options are wrong
> **A. Active-active across two regions + global LB + Spanner**
> This is more than what’s required (multi-region resilience), and it is significantly more expensive (duplicate regional stacks + a premium multi-region database like Spanner). It does tolerate a zone outage, but it does not meet “keep costs as low as possible.”
>
> **C. Use only Spot VMs**
> Spot VMs can be preempted at any time and are not appropriate for a business-critical payment system where you need predictable availability. Spot can reduce cost, but it increases the risk of disruption unrelated to zonal failure.
>
> **D. Multi-region compute + daily snapshots**
> Daily snapshots don’t provide continuity through a zonal outage; they are a backup/recovery mechanism, not high availability. Also, relying on restore processes during failure conflicts with “continue operating” requirements.

</details>

---

### Exam 5 · Q59

**Your organization is a global financial services company that processes a large volume of credit card transactions in real time for fraud detection. The analytics team also needs to run complex batch queries on the same transaction dataset for daily reporting. You must design a solution that supports both streaming and batch processing while keeping operational overhead and infrastructure management as low as possible. What should you do?( Choose two)**

- A. Use Dataprep to ingest transaction data.
- B. Use Dataflow to process the real-time transaction stream.
- C. Use a Dataproc cluster to run both the streaming and batch workloads.
- D. Use BigQuery to run the daily batch analytics reports.
- E. Use Firestore to store and analyze the transaction data.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use Dataflow to process the real-time transaction stream. **|** D. Use BigQuery to run the daily batch analytics reports.

**Correct options: B and D**

**Need-to-know foundational concept**

Modern analytics architectures often separate **processing** from **analytics storage**:

- A **stream processing engine** handles real-time ingestion and transformation
- A **serverless analytics warehouse** handles large batch queries

Google’s recommended low-ops architecture for streaming + batch analytics is:

**Dataflow → BigQuery**

Dataflow processes streaming data and writes it into BigQuery, where analysts run complex SQL batch queries. Both services are fully managed and serverless, minimizing infrastructure overhead.

**Dataflow supports unified streaming and batch pipelines:**
[https://cloud.google.com/dataflow/docs/overview](https://cloud.google.com/dataflow/docs/overview)

**BigQuery is a serverless analytics warehouse optimized for large batch queries:**
[https://cloud.google.com/bigquery/docs/introduction](https://cloud.google.com/bigquery/docs/introduction)

**Why the correct options fit the scenario**

**B. Dataflow for real-time processing**
Dataflow is built for high-throughput streaming analytics like fraud detection. It scales automatically and requires no cluster management. It can continuously write processed transactions into BigQuery.

**D. BigQuery for batch analytics**
BigQuery is designed for complex analytical SQL queries on massive datasets. The analytics team can run daily reports without managing infrastructure.

Together, they provide:

- Real-time fraud pipeline
- Batch reporting
- Shared dataset
- Serverless architecture
- Minimal ops overhead

This is a canonical Google Cloud streaming analytics pattern.

**Why the other options are not the best choice**

**A. Dataprep**
Dataprep is for interactive data cleaning and wrangling, not high-volume production ingestion or streaming pipelines.

**C. Dataproc**
Dataproc requires managing Spark/Hadoop clusters. That increases operational burden, violating the requirement to keep infrastructure management low.

**E. Firestore**
Firestore is an operational NoSQL database optimized for application workloads, not analytical batch queries or fraud analytics pipelines.

The only combination that satisfies **streaming + batch + low operational overhead** is **Dataflow + BigQuery**.

###### Explanation

**B. Dataflow for real-time processing**
Dataflow is built for high-throughput streaming analytics like fraud detection. It scales automatically and requires no cluster management. It can continuously write processed transactions into BigQuery.

**D. BigQuery for batch analytics**
BigQuery is designed for complex analytical SQL queries on massive datasets. The analytics team can run daily reports without managing infrastructure.

Together, they provide:

- Real-time fraud pipeline
- Batch reporting
- Shared dataset
- Serverless architecture
- Minimal ops overhead

> [!note]- Why the other options are wrong
> **A. Dataprep**
> Dataprep is for interactive data cleaning and wrangling, not high-volume production ingestion or streaming pipelines.
>
> **C. Dataproc**
> Dataproc requires managing Spark/Hadoop clusters. That increases operational burden, violating the requirement to keep infrastructure management low.
>
> **E. Firestore**
> Firestore is an operational NoSQL database optimized for application workloads, not analytical batch queries or fraud analytics pipelines.

</details>

---

### Exam 5 · Q60

**Your company runs a custom application on a Compute Engine VM that processes real-time sales data and writes it to a zonal Persistent Disk. A new audit requires an automated backup and recovery strategy that protects against zonal failures. All backup data must be retained for at least 90 days and stored in a separate project with restricted access. You need a fully automated solution that satisfies these requirements with minimal operational effort. What should you do?**

- A. Develop a script that creates daily disk backups, copies them to another zone, and labels each snapshot with its planned deletion date.
- B. Use gcloud commands to generate Persistent Disk snapshots, store them in a regional Cloud Storage bucket, and configure a lifecycle rule to delete backups older than 90 days.
- C. Configure an automated snapshot schedule and use a script to transfer snapshots into a multi-regional Cloud Storage bucket.
- D. Use Backup and Disaster Recovery (DR) to define a backup plan that performs daily backups and stores them in a backup vault with a 90-day retention policy.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Use Backup and Disaster Recovery (DR) to define a backup plan that performs daily backups and stores them in a backup vault with a 90-day retention policy.

**Correct option: D. Use Backup and Disaster Recovery (DR) to define a backup plan that performs daily backups and stores them in a backup vault with a 90-day retention policy.**

**Need-to-know foundational concept**

To meet an audit-grade requirement with minimal operations, you want a **policy-driven backup service** that is (1) scheduled and automated, (2) enforces retention automatically, and (3) keeps backups **isolated** from the source workload’s admins (separate project with restricted access). Google Cloud’s **Backup and DR** uses **backup vaults** that store backups with **enforced retention** (backups expire automatically) and are designed to be immutable/indelible for the enforced period—ideal for compliance.
**Authoritative reference:** [https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault)

**Why the chosen option is correct**

- **Automated daily backups**: A backup plan schedules backups without custom scripting.
- **90-day retention**: The vault’s retention policy automatically governs expiry for at least 90 days.
- **Separate project + restricted access**: You can place the **backup vault in a dedicated project** and restrict IAM there, so backup storage access is tightly controlled and isolated from the workload project.
- **Zonal failure protection**: Persistent Disk backups (snapshots) are stored separately from the VM/zone and can be used to restore disks/VMs even if the original zone is unavailable.

**Why the other options are not the best choice**

**A. Script + copy to another zone + labels**
This is operationally heavy and error-prone (custom scheduling, labeling, deletion logic). Also, “another zone” does not satisfy the requirement of storing backups in a **separate project** with restricted access.

**B. Snapshots into a regional Cloud Storage bucket + lifecycle**
Persistent Disk snapshots are not “stored in a Cloud Storage bucket” in the way objects are; lifecycle rules on a bucket don’t govern snapshot retention. This design also doesn’t inherently address cross-project isolation for backups.

**C. Snapshot schedule + script to transfer snapshots into a multi-regional Cloud Storage bucket**
Same core issue: snapshots are not exported into Cloud Storage buckets by default, and you’re again relying on custom scripting for cross-project storage and retention controls—more ops and more risk than a managed vault-based approach.

A vault-based Backup and DR plan is the only option here that cleanly satisfies **automation**, **90-day retention**, and **separate-project isolation with minimal operational effort**.

###### Explanation

**Correct option: D. Use Backup and Disaster Recovery (DR) to define a backup plan that performs daily backups and stores them in a backup vault with a 90-day retention policy.**

**Need-to-know foundational concept**

To meet an audit-grade requirement with minimal operations, you want a **policy-driven backup service** that is (1) scheduled and automated, (2) enforces retention automatically, and (3) keeps backups **isolated** from the source workload’s admins (separate project with restricted access). Google Cloud’s **Backup and DR** uses **backup vaults** that store backups with **enforced retention** (backups expire automatically) and are designed to be immutable/indelible for the enforced period—ideal for compliance.

> [!note]- Why the other options are wrong
> **A. Script + copy to another zone + labels**
> This is operationally heavy and error-prone (custom scheduling, labeling, deletion logic). Also, “another zone” does not satisfy the requirement of storing backups in a **separate project** with restricted access.
>
> **B. Snapshots into a regional Cloud Storage bucket + lifecycle**
> Persistent Disk snapshots are not “stored in a Cloud Storage bucket” in the way objects are; lifecycle rules on a bucket don’t govern snapshot retention. This design also doesn’t inherently address cross-project isolation for backups.
>
> **C. Snapshot schedule + script to transfer snapshots into a multi-regional Cloud Storage bucket**
> Same core issue: snapshots are not exported into Cloud Storage buckets by default, and you’re again relying on custom scripting for cross-project storage and retention controls—more ops and more risk than a managed vault-based approach.

</details>

---

### Exam 5 · Q61

**Your ecommerce web application serves many products that include images and videos. You want to speed up page load times and reduce latency for customer requests. What actions should you take? (Choose two.)**

- A. Deploy the application on Cloud Run and enable request concurrency.
- B. Use Memorystore for Redis.
- C. Add a CDN to the application’s external HTTPS load balancer.
- D. Replace the database backend from Bigtable with Spanner.
- E. Migrate the application to a GKE Autopilot cluster instead of a standard GKE cluster.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use Memorystore for Redis. **|** C. Add a CDN to the application’s external HTTPS load balancer.

**Correct options: B and C**

**Need-to-know foundational concept**

When optimizing end-user latency for media-heavy web apps, two foundational performance patterns matter:

1. **Edge caching** — serve static assets (images/videos) from locations close to users
2. **Application caching** — avoid repeatedly recomputing or fetching expensive data

Cloud CDN reduces geographic latency by caching content at Google’s edge locations. Memorystore provides in-memory caching to reduce backend round trips. Together they attack latency from both the network layer and the application layer.

**Cloud CDN is designed specifically to accelerate delivery of static content globally:**
[https://cloud.google.com/cdn/docs/overview](https://cloud.google.com/cdn/docs/overview)

Memorystore for Redis is used to cache frequently accessed data in memory for low-latency retrieval:
[https://cloud.google.com/memorystore/docs/redis/redis-overview](https://cloud.google.com/memorystore/docs/redis/redis-overview)

**Why the correct options fit the scenario**

**C. Add a CDN to the external HTTPS load balancer**
This is the biggest win for images and videos. CDN caches media at edge POPs worldwide so customers download from a nearby location instead of your origin. That directly reduces page load time.

**B. Use Memorystore for Redis**
Memorystore reduces latency for dynamic content by caching frequently accessed data in RAM. This prevents repeated database reads and improves response time for product metadata, sessions, or catalog lookups.

Together:

- CDN speeds delivery of static media
- Redis speeds backend data access
- Users experience faster page loads globally

**Why the other options are not the best choice**

**A. Cloud Run concurrency**
Concurrency affects resource efficiency, not user-facing latency for media delivery. It doesn’t solve static asset delivery or caching.

**D. Bigtable → Spanner migration**
This is a database architecture change unrelated to image/video delivery latency. It adds complexity without addressing the core problem.

**E. GKE Autopilot migration**
Cluster management mode has no direct impact on page load latency. It affects ops overhead, not edge delivery performance.

The fastest way to improve ecommerce media performance is **edge caching + in-memory caching**, which is exactly what CDN + Memorystore provide.

###### Explanation

**B. Use Memorystore for Redis**
Memorystore reduces latency for dynamic content by caching frequently accessed data in RAM. This prevents repeated database reads and improves response time for product metadata, sessions, or catalog lookups.

Together:

- CDN speeds delivery of static media
- Redis speeds backend data access
- Users experience faster page loads globally

**C. Add a CDN to the external HTTPS load balancer**
This is the biggest win for images and videos. CDN caches media at edge POPs worldwide so customers download from a nearby location instead of your origin. That directly reduces page load time.

> [!note]- Why the other options are wrong
> **A. Cloud Run concurrency**
> Concurrency affects resource efficiency, not user-facing latency for media delivery. It doesn’t solve static asset delivery or caching.
>
> **D. Bigtable → Spanner migration**
> This is a database architecture change unrelated to image/video delivery latency. It adds complexity without addressing the core problem.
>
> **E. GKE Autopilot migration**
> Cluster management mode has no direct impact on page load latency. It affects ops overhead, not edge delivery performance.

</details>

---

### Exam 5 · Q62

**You must build and deploy a containerized web application on Google Cloud. The workload is heavily write-intensive and depends on a relational database. The application must be highly available across multiple regions, and you want to keep operational management as low as possible while following Google best practices. What should you do?**

- A. Deploy the app to GKE clusters in multiple regions and expose it with a regional load balancer. Use Cloud SQL as the database.
- B. Deploy the app to Cloud Run in multiple regions behind a global HTTPS load balancer. Use Spanner as the database.
- C. Deploy the app to a GKE standard cluster behind a global HTTPS load balancer. Use Firestore in multi-region mode as the database.
- D. Deploy the app to a GKE standard cluster with a global ingress endpoint. Use Bigtable as the database.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Deploy the app to Cloud Run in multiple regions behind a global HTTPS load balancer. Use Spanner as the database.

**Correct option: B. Deploy the app to Cloud Run in multiple regions behind a global HTTPS load balancer. Use Spanner as the database.**

**Need-to-know foundational concept**

The architecture must satisfy three constraints at the same time:

- **Write-intensive relational workload**
- **Multi-region high availability**
- **Minimal operational management**

Only **Spanner** is a fully managed, relational database designed for **multi-region writes with strong consistency**. Traditional relational databases (like Cloud SQL) are regional and rely on replicas or failover, not active multi-region writes.

On the compute side, Google’s best practice for low-ops container hosting is **Cloud Run**. It is serverless, auto-scales, and removes cluster management overhead.

**Spanner is designed for global, horizontally scalable relational workloads:**
[https://cloud.google.com/spanner/docs/overview](https://cloud.google.com/spanner/docs/overview)

**Cloud Run is a fully managed container runtime that eliminates cluster management:**
[https://cloud.google.com/run/docs/overview/what-is-cloud-run](https://cloud.google.com/run/docs/overview/what-is-cloud-run)

**Why the correct option fits the scenario**

- Cloud Run = serverless, no cluster ops
- Multi-region deployment supported behind global load balancing
- Spanner = globally distributed relational database
- Supports heavy write workloads with strong consistency
- Active-active multi-region architecture
- Follows Google HA best practices

This is the only option that satisfies **relational + multi-region + low ops** simultaneously.

**Why the other options are not the best choice**

**A. GKE + regional LB + Cloud SQL**
Cloud SQL is regional and not designed for active multi-region relational writes. It does not meet the multi-region HA requirement.

**C. GKE + Firestore**
Firestore is NoSQL, not relational. The requirement explicitly states a relational dependency.

**D. GKE + Bigtable**
Bigtable is a NoSQL wide-column store, not relational, and not suited for relational workloads.

The only architecture aligned with Google’s recommended pattern for **global relational applications** is **Cloud Run + Spanner**.

###### Explanation

**Correct option: B.**

**Need-to-know foundational concept**

The architecture must satisfy three constraints at the same time:

- **Write-intensive relational workload**
- **Multi-region high availability**
- **Minimal operational management**

**Why the correct option fits the scenario**

- Cloud Run = serverless, no cluster ops
- Multi-region deployment supported behind global load balancing
- Spanner = globally distributed relational database
- Supports heavy write workloads with strong consistency
- Active-active multi-region architecture
- Follows Google HA best practices

> [!note]- Why the other options are wrong
> **A. GKE + regional LB + Cloud SQL**
> Cloud SQL is regional and not designed for active multi-region relational writes. It does not meet the multi-region HA requirement.
>
> **C. GKE + Firestore**
> Firestore is NoSQL, not relational. The requirement explicitly states a relational dependency.
>
> **D. GKE + Bigtable**
> Bigtable is a NoSQL wide-column store, not relational, and not suited for relational workloads.

</details>

---

### Exam 5 · Q64

**Your employer is a financial services company that has acquired a fintech startup. The startup’s main system is a monolithic Python application running on a managed instance group of Compute Engine VMs with a single large PostgreSQL database. Deployments are slow, and the tightly coupled architecture makes it hard to integrate new ML-based fraud detection features. You need a long-term modernization approach that improves developer agility and prepares the platform to take advantage of Google Cloud’s advanced data and AI services. What should you do?**

- A. Deploy the fraud detection model to a Vertex AI endpoint, expose it through a REST API, and modify the monolithic application to call the endpoint for real-time analysis.
- B. Containerize the application, run it on Google Kubernetes Engine, and migrate the PostgreSQL database to Cloud SQL for PostgreSQL.
- C. Plan a phased migration to an event-driven microservices architecture, use Pub/Sub for asynchronous communication, and deploy fraud detection models on Vertex AI endpoints.
- D. Migrate PostgreSQL to Cloud SQL, replicate the data to BigQuery with Datastream, and build and deploy fraud models directly using BigQuery ML.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Plan a phased migration to an event-driven microservices architecture, use Pub/Sub for asynchronous communication, and deploy fraud detection models on Vertex AI endpoints.

**Correct option: C. Plan a phased migration to an event-driven microservices architecture, use Pub/Sub for asynchronous communication, and deploy fraud detection models on Vertex AI endpoints.**

**Need-to-know foundational concept**

Modernizing a tightly coupled monolith isn’t just about moving it to containers — it’s about **decoupling architecture** so teams can evolve parts of the system independently. Google’s recommended modernization pattern is:

- Break the monolith into **microservices**
- Use **event-driven communication**
- Integrate ML services through APIs
- Enable independent deployment and scaling

Event-driven systems improve agility because services communicate asynchronously instead of blocking each other. Pub/Sub is Google’s global messaging backbone for this pattern, and Vertex AI provides managed ML serving.

**Event-driven architecture with Pub/Sub is a core Google modernization pattern:**
[https://cloud.google.com/architecture/event-driven-architecture-pubsub](https://cloud.google.com/architecture/event-driven-architecture-pubsub)

**Vertex AI endpoints provide scalable model serving via APIs:**
[https://cloud.google.com/vertex-ai/docs/predictions/get-online-predictions](https://cloud.google.com/vertex-ai/docs/predictions/get-online-predictions)

**Why the correct option fits the scenario**

The question asks for a **long-term modernization strategy** that:

- Improves developer agility
- Supports ML integration
- Reduces coupling
- Prepares for advanced data/AI services

**Option C does all of this:**

- Phased microservices migration = gradual modernization
- Pub/Sub = asynchronous decoupling
- Vertex AI = scalable ML integration
- Enables independent deployments
- Supports future AI pipelines

This is architectural transformation, not just lift-and-shift.

**Why the other options are not the best choice**

**A. Call Vertex AI from the monolith**
This adds ML, but the monolith remains tightly coupled. It doesn’t modernize architecture or improve agility.

**B. Containerize monolith on GKE**
This is infrastructure modernization, not architectural modernization. You still have a monolith with slow deployments.

**D. BigQuery ML + Datastream**
This supports analytics ML, not real-time fraud detection. It also doesn’t address application architecture or agility.

Only option C modernizes the platform while enabling scalable ML integration and future extensibility.

###### Explanation

**Correct option: C. Plan a phased migration to an event-driven microservices architecture, use Pub/Sub for asynchronous communication, and deploy fraud detection models on Vertex AI endpoints.**

**Need-to-know foundational concept**

Modernizing a tightly coupled monolith isn’t just about moving it to containers — it’s about **decoupling architecture** so teams can evolve parts of the system independently. Google’s recommended modernization pattern is:

- Break the monolith into **microservices**
- Use **event-driven communication**
- Integrate ML services through APIs
- Enable independent deployment and scaling

Event-driven systems improve agility because services communicate asynchronously instead of blocking each other. Pub/Sub is Google’s global messaging backbone for this pattern, and Vertex AI provides managed ML serving.

> [!note]- Why the other options are wrong
> **A. Call Vertex AI from the monolith**
> This adds ML, but the monolith remains tightly coupled. It doesn’t modernize architecture or improve agility.
>
> **B. Containerize monolith on GKE**
> This is infrastructure modernization, not architectural modernization. You still have a monolith with slow deployments.
>
> **D. BigQuery ML + Datastream**
> This supports analytics ML, not real-time fraud detection. It also doesn’t address application architecture or agility.

</details>

---

### Exam 5 · Q71

**Your ecommerce platform relies on a regional Cloud SQL for PostgreSQL database to store critical order data. The business requires a disaster recovery plan with an RTO under 10 minutes and an RPO of 2 minutes in the event of a full regional outage. You must design a solution that meets these targets while keeping operational complexity low. What should you do?**

- A. Configure hourly automated backups to a multi-regional Cloud Storage bucket and restore the latest backup in another region during a disaster.
- B. Use Database Migration Service to continuously replicate the database to another region and redirect traffic to that replica if an outage occurs.
- C. Create a cross-region read replica of the Cloud SQL instance and promote it to primary during a regional failure.
- D. Enable high availability on the primary instance and fail over to the standby instance during a regional outage.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Create a cross-region read replica of the Cloud SQL instance and promote it to primary during a regional failure.

**Correct option: C. Create a cross-region read replica of the Cloud SQL instance and promote it to primary during a regional failure.**

**Need-to-know foundational concept**

For Cloud SQL disaster recovery:

- **High availability (HA)** protects against **zonal failure**
- **Cross-region replicas** protect against **regional failure**
- Backups protect against **data loss**, not low-RTO recovery

When the requirement is recovery from a *full regional outage* with tight RTO/RPO, you need **continuous cross-region replication**, not backups.

Cloud SQL cross-region read replicas are designed specifically for disaster recovery and can be promoted quickly to become primary. Replication is near-real-time and supports low RPO targets.

**Authoritative reference:**
[https://cloud.google.com/sql/docs/postgres/replication/cross-region-replicas](https://cloud.google.com/sql/docs/postgres/replication/cross-region-replicas)

**Why the correct option fits the scenario**

- Cross-region replication = protects against regional outage
- Near-real-time WAL replication = supports ~2 minute RPO
- Replica promotion is fast = supports <10 minute RTO
- Fully managed service = low operational complexity

This is the official DR architecture pattern for Cloud SQL.

**Why the other options are not the best choice**

**A. Hourly backups**
Hourly backups cannot meet a 2-minute RPO. Backup restore also exceeds a 10-minute RTO.

**B. Database Migration Service (DMS)**
DMS is for migration, not production disaster recovery. It is not designed as an operational failover mechanism.

**D. High availability instance**
Cloud SQL HA protects only against **zone failure inside the same region**, not a regional outage. The requirement explicitly states regional disaster.

Exam principle:

Regional DR for Cloud SQL = cross-region replica + promotion.

Final answer: C

###### Explanation

**Correct option: C. Create a cross-region read replica of the Cloud SQL instance and promote it to primary during a regional failure.**

**Need-to-know foundational concept**

For Cloud SQL disaster recovery:

- **High availability (HA)** protects against **zonal failure**
- **Cross-region replicas** protect against **regional failure**
- Backups protect against **data loss**, not low-RTO recovery

When the requirement is recovery from a *full regional outage* with tight RTO/RPO, you need **continuous cross-region replication**, not backups.

Cloud SQL cross-region read replicas are designed specifically for disaster recovery and can be promoted quickly to become primary. Replication is near-real-time and supports low RPO targets.

**Why the correct option fits the scenario**

- Cross-region replication = protects against regional outage
- Near-real-time WAL replication = supports ~2 minute RPO
- Replica promotion is fast = supports <10 minute RTO
- Fully managed service = low operational complexity

This is the official DR architecture pattern for Cloud SQL.

> [!note]- Why the other options are wrong
> **A. Hourly backups**
> Hourly backups cannot meet a 2-minute RPO. Backup restore also exceeds a 10-minute RTO.
>
> **B. Database Migration Service (DMS)**
> DMS is for migration, not production disaster recovery. It is not designed as an operational failover mechanism.
>
> **D. High availability instance**
> Cloud SQL HA protects only against **zone failure inside the same region**, not a regional outage. The requirement explicitly states regional disaster.

</details>

---

### Exam 5 · Q75

**A global media company is rolling out a new web application. The backend runs on Compute Engine in us-central1 and serves both static content (images, CSS, JavaScript) and dynamic, user-specific content backed by a Cloud SQL database in the same region. Initial feedback from users in Europe and Asia reports noticeable page load slowness, primarily due to delayed loading of static assets. You need to reduce latency for global users when accessing the static content. What should you do? (Choose two.)**

- A. Use a regional external Network Load Balancer in us-central1 to better distribute worldwide traffic.
- B. Enable Cloud CDN for the backend service that delivers static assets, and attach it to a global external HTTP(S) Load Balancer.
- C. Scale up the Compute Engine instances in us-central1 by selecting larger machine types.
- D. Deploy the application’s frontend service to managed instance groups in Europe and Asia, and use a global external HTTP(S) Load Balancer to send users to the closest region.
- E. Create Cloud SQL read replicas in Europe and Asia, and route read-only database traffic from those regions to the nearest replica.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Enable Cloud CDN for the backend service that delivers static assets, and attach it to a global external HTTP(S) Load Balancer. **|** D. Deploy the application’s frontend service to managed instance groups in Europe and Asia, and use a global external HTTP(S) Load Balancer to send users to the closest region.

**Correct options: B and D**

**Need-to-know foundational concept**

When global users complain about **slow static asset loading**, the highest-impact fixes are:

- **Cache static content at the edge** close to users (CDN)
- **Move the serving origin closer** to users when needed (multi-region backends behind a global HTTP(S) load balancer)

Cloud CDN caches cacheable content at Google’s edge locations to reduce latency for globally distributed users. A global external HTTP(S) Load Balancer can route users to the closest healthy backend across regions.

**Cloud CDN overview (edge caching with global external HTTP(S) Load Balancer):**
[https://cloud.google.com/cdn/docs/overview](https://cloud.google.com/cdn/docs/overview)

**Global external HTTP(S) Load Balancing (global anycast, nearest-backend routing):**
[https://cloud.google.com/load-balancing/docs/https](https://cloud.google.com/load-balancing/docs/https)

**Why the chosen options are correct**

**B. Enable Cloud CDN for the backend service that delivers static assets, and attach it to a global external HTTP(S) Load Balancer.**
This directly targets the stated problem: static assets are slow for Europe/Asia users because they’re fetched from us-central1. Cloud CDN caches those assets at edge POPs closer to users, reducing round-trip time and improving page load speed without changing the app architecture.

**D. Deploy the application’s frontend service to managed instance groups in Europe and Asia, and use a global external HTTP(S) Load Balancer to send users to the closest region.**
This reduces latency by placing the web serving tier closer to users, so even cache misses (or non-cacheable static assets) are served from a nearer region. The global HTTP(S) load balancer routes users to the closest healthy backend, improving responsiveness for worldwide traffic.

**Why the other options are not the best choice**

**A. Regional external Network Load Balancer in us-central1**
A regional NLB does not provide global edge caching and does not route users to the nearest global entry point the way global HTTP(S) load balancing does. It won’t materially improve static asset latency for distant regions.

**C. Scale up Compute Engine instances in us-central1**
Bigger instances can help if you’re CPU-bound, but the issue described is latency to static assets for global users, which is primarily network distance, not compute capacity.

**E. Cloud SQL read replicas in Europe and Asia**
This can help with database read latency for dynamic content, but the problem statement says slowness is **primarily due to delayed static assets**. Read replicas do not address static file delivery.

Final answer: **B and D**

###### Explanation

**B. Enable Cloud CDN for the backend service that delivers static assets, and attach it to a global external HTTP(S) Load Balancer.**
This directly targets the stated problem: static assets are slow for Europe/Asia users because they’re fetched from us-central1. Cloud CDN caches those assets at edge POPs closer to users, reducing round-trip time and improving page load speed without changing the app architecture.

**D. Deploy the application’s frontend service to managed instance groups in Europe and Asia, and use a global external HTTP(S) Load Balancer to send users to the closest region.**
This reduces latency by placing the web serving tier closer to users, so even cache misses (or non-cacheable static assets) are served from a nearer region. The global HTTP(S) load balancer routes users to the closest healthy backend, improving responsiveness for worldwide traffic.

> [!note]- Why the other options are wrong
> **A. Regional external Network Load Balancer in us-central1**
> A regional NLB does not provide global edge caching and does not route users to the nearest global entry point the way global HTTP(S) load balancing does. It won’t materially improve static asset latency for distant regions.
>
> **C. Scale up Compute Engine instances in us-central1**
> Bigger instances can help if you’re CPU-bound, but the issue described is latency to static assets for global users, which is primarily network distance, not compute capacity.
>
> **E. Cloud SQL read replicas in Europe and Asia**
> This can help with database read latency for dynamic content, but the problem statement says slowness is **primarily due to delayed static assets**. Read replicas do not address static file delivery.

</details>

---

### Exam 5 · Q79

**Your organization plans to migrate applications to Kubernetes and adopt managed cloud services for deployment. The engineering team is new to Kubernetes and wants to onboard quickly. You want to minimize operational overhead so the team can focus on delivering features instead of managing infrastructure. What should you do?**

- A. Containerize the application and deploy it to Kubernetes running on Compute Engine.
- B. Use Cloud Build to generate a container image and automatically deploy it to Kubernetes on Compute Engine.
- C. Evaluate the application and its dependencies for containerization, then plan a migration to GKE Standard mode.
- D. Evaluate the application and its dependencies for containerization, then plan a migration to GKE Autopilot mode.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Evaluate the application and its dependencies for containerization, then plan a migration to GKE Autopilot mode.

**Correct option: D. Evaluate the application and its dependencies for containerization, then plan a migration to GKE Autopilot mode.**

**Need-to-know foundational concept**

The key requirement is:

New to Kubernetes + minimize operational overhead

GKE has two operating models:

- **Standard mode** → you manage nodes, scaling, upgrades
- **Autopilot mode** → Google manages the infrastructure

Autopilot is designed for teams that want Kubernetes **without managing Kubernetes infrastructure**. It handles:

- node provisioning
- upgrades
- scaling
- security hardening
- capacity management
- bin-packing optimization

**You focus only on workloads.**

**Official Autopilot overview:**
[https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview](https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

**Why option D is correct**

Option D matches all requirements:

- onboarding-friendly for Kubernetes beginners
- minimal infrastructure management
- managed operations by Google
- best practice for cloud-native teams
- lets engineers focus on application delivery
- still full Kubernetes compatibility

It’s the lowest-ops path to Kubernetes.

**Why the other options are not the best choice**

**A. Kubernetes on Compute Engine**
You’re managing your own cluster manually. Highest operational burden.

**B. Cloud Build + Kubernetes on Compute Engine**
Adds CI/CD but still requires self-managed Kubernetes infrastructure.

**C. GKE Standard mode**
Still requires node management and cluster operations. Not ideal for beginners aiming to minimize overhead.

**Exam principle:**

**New to Kubernetes + low ops → GKE Autopilot.**

**Final answer: D**

###### Explanation

**Correct option: D.**

**Need-to-know foundational concept**

The key requirement is:

New to Kubernetes + minimize operational overhead

GKE has two operating models:

- **Standard mode** → you manage nodes, scaling, upgrades
- **Autopilot mode** → Google manages the infrastructure

Autopilot is designed for teams that want Kubernetes **without managing Kubernetes infrastructure**. It handles:

- node provisioning
- upgrades
- scaling
- security hardening
- capacity management
- bin-packing optimization

**Why option D is correct**

Option D matches all requirements:

- onboarding-friendly for Kubernetes beginners
- minimal infrastructure management
- managed operations by Google
- best practice for cloud-native teams
- lets engineers focus on application delivery
- still full Kubernetes compatibility

> [!note]- Why the other options are wrong
> **A. Kubernetes on Compute Engine**
> You’re managing your own cluster manually. Highest operational burden.
>
> **B. Cloud Build + Kubernetes on Compute Engine**
> Adds CI/CD but still requires self-managed Kubernetes infrastructure.
>
> **C. GKE Standard mode**
> Still requires node management and cluster operations. Not ideal for beginners aiming to minimize overhead.

</details>

---
