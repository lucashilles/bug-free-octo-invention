# Domain 2 — Exploring Data Transformation with Google Cloud

64 questions. Answers are collapsed — try each question before expanding it.

## Questions

### Exam 1 · Q1

**CafePulse, a restaurant analytics website, receives daily sales records, customer feedback, and delivery logs from multiple branches. The team is converting this raw information into a cleaner, structured format so managers can later use it to discover business trends. Which step of the data value chain does this action represent?**

- A. Data analysis
- B. Data collection
- C. Data storage
- D. Data processing

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Data processing

**Correct answer: D. Data processing**

Data processing turns raw data into a clean, consistent, structured form that is ready for analysis. The clue is "converting this raw information into a cleaner, structured format so managers can **later** use it". The data has already been collected, and the analysis comes afterwards.

**Why the others are wrong:**
- **A. Data analysis**: analysis is the later step where managers look for trends in the prepared data.
- **B. Data collection**: collection is gathering the sales records, feedback and logs, which has already happened.
- **C. Data storage**: storage is keeping the data somewhere; it does not clean or restructure it.

**Remember:** Collect → process (clean, transform) → store → analyze. "Cleaner, structured format" = processing.

**References:**
- [docs.cloud.google.com/dataflow/docs/overview](https://docs.cloud.google.com/dataflow/docs/overview)
- [cloud.google.com/learn/what-is-data-analytics](https://cloud.google.com/learn/what-is-data-analytics)
- [cloud.google.com/learn/certification/data-engineer](https://cloud.google.com/learn/certification/data-engineer)

**⚠️ Note:** The bank calls this sequence both the "data value chain" and the "data supply chain" (see Q35). Treat them as the same idea.

</details>

---

### Exam 1 · Q3

**SnackWave, a company that operates snack kiosks in office buildings, notices that the money collected from its machines often does not match the products dispensed. The company plans to replace cash-only purchases with a cloud-connected mobile payment system that records each purchase digitally. How could SnackWave benefit from this upgrade?**

- A. They could relax data access permissions.
- B. They could reduce their error budget overspend.
- C. They could improve their perimeter security.
- D. They could view data history to see transactions.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. They could view data history to see transactions.

**Correct answer: D. They could view data history to see transactions.**

Recording each purchase digitally creates a reliable history of every transaction. SnackWave can then compare sales records with products dispensed and find where the mismatch happens. The clue is the problem itself: cash collected does not match what was sold, and the fix is a system that "records each purchase digitally".

**Why the others are wrong:**
- **A. Relax data access permissions**: digitizing payments is no reason to loosen access; payment data needs tight control.
- **B. Reduce error budget overspend**: error budgets are an SRE reliability concept and have nothing to do with cash mismatches.
- **C. Improve perimeter security**: the problem is missing records, not network security, and perimeter security is not what digital payments provide.

**Remember:** Digitizing a process creates data you can track, audit and reconcile.

**References:**
- [cloud.google.com/solutions/financial-services/payments](https://cloud.google.com/solutions/financial-services/payments)
- [cloud.google.com/bigquery/docs/introduction](https://cloud.google.com/bigquery/docs/introduction)
- [cloud.google.com/iam/docs/overview](https://cloud.google.com/iam/docs/overview)

**⚠️ Note:** "View data history" is vague wording. The real benefit is a digital record of every purchase that can be reconciled against inventory. The other options are clearly wrong, so pick the keyed answer.

</details>

---

### Exam 1 · Q4

**PayPilot Finance is building a payments application that must record customer transactions with low latency while also allowing analysts to run fast reporting queries on the same PostgreSQL-compatible operational database. The team wants a Google Cloud database that includes a columnar engine to speed up analytical queries without moving the data to a separate analytics system. Which database is designed for this requirement?**

- A. Cloud SQL
- B. AlloyDB for PostgreSQL
- C. Cloud Spanner
- D. Firestore

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. AlloyDB for PostgreSQL

**Correct answer: B. AlloyDB for PostgreSQL**

AlloyDB is a fully managed, PostgreSQL-compatible database built for demanding transactional workloads. It also includes a built-in columnar engine that speeds up analytical queries on the same operational data. The clues are "PostgreSQL-compatible", "low latency transactions" and "columnar engine ... without moving the data" (mixed transactional and analytical work).

**Why the others are wrong:**
- **A. Cloud SQL**: Cloud SQL supports PostgreSQL but is a standard managed relational database without AlloyDB's columnar engine for fast analytics.
- **C. Cloud Spanner**: Spanner is for global scale and strong consistency across regions, not the PostgreSQL-plus-columnar-analytics use case described here.
- **D. Firestore**: Firestore is a NoSQL document database, not PostgreSQL-compatible.

**Remember:** PostgreSQL + high performance + fast analytics on live data = AlloyDB.

**References:**
- [cloud.google.com/alloydb/docs/overview](https://cloud.google.com/alloydb/docs/overview)
- [cloud.google.com/alloydb/docs/columnar-engine/about](https://cloud.google.com/alloydb/docs/columnar-engine/about)
- [cloud.google.com/sql/docs/postgres/overview](https://cloud.google.com/sql/docs/postgres/overview)

</details>

---

### Exam 1 · Q6

**StreamNest, a video learning website, stores training clips and images that must be delivered to users in several countries. The company needs a Cloud Storage option that supports broad geographic access and a high level of availability. What Cloud Storage feature would StreamNest benefit from?**

- A. Multi-region bucket location
- B. Global metadata
- C. Data encryption
- D. Object versioning

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Multi-region bucket location

**Correct answer: A. Multi-region bucket location**

A multi-region bucket stores data redundantly across a large geographic area (for example, several regions in one continent). This gives broad access for users in many countries and higher availability than a single region. The clue is "users in several countries" plus "a high level of availability".

**Why the others are wrong:**
- **B. Global metadata**: this is not a Cloud Storage location option and does not control where object data lives.
- **C. Data encryption**: encryption protects data (and is on by default), but it does not improve geographic reach or availability.
- **D. Object versioning**: versioning keeps old copies of objects to recover from deletes or overwrites; it is not about location or availability.

**Remember:** Users across many countries + high availability = multi-region bucket.

**References:**
- [cloud.google.com/storage/docs/locations](https://cloud.google.com/storage/docs/locations)
- [cloud.google.com/storage/docs/availability-durability](https://cloud.google.com/storage/docs/availability-durability)
- [cloud.google.com/storage/docs/storage-classes](https://cloud.google.com/storage/docs/storage-classes)

</details>

---

### Exam 1 · Q13

**ShopNexa is an online shopping mobile app that stores customer orders, inventory, and payment records in an existing PostgreSQL database. As the number of transactions increases, the database is becoming slower during peak sale events. The engineering team wants to move to a fully managed Google Cloud database service that is compatible with PostgreSQL, provides better performance, scales well, and supports high availability with minimal changes to the current application code. Which service should they choose?**

- A. Spanner
- B. AlloyDB for PostgreSQL
- C. Bigtable
- D. Firestore

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. AlloyDB for PostgreSQL

**Correct answer: B. AlloyDB for PostgreSQL**

AlloyDB is a fully managed, PostgreSQL-compatible database designed for higher performance, scalability and high availability. Because it speaks PostgreSQL, the existing application needs minimal code changes. The clues are "existing PostgreSQL database", "better performance" and "minimal changes".

**Why the others are wrong:**
- **A. Spanner**: Spanner offers a PostgreSQL interface, but it is built for global scale and usually needs more adaptation than AlloyDB.
- **C. Bigtable**: Bigtable is a NoSQL wide-column database, not PostgreSQL-compatible.
- **D. Firestore**: Firestore is a NoSQL document database; moving to it would mean rewriting the data layer.

**Remember:** Existing PostgreSQL that needs more performance with minimal changes = AlloyDB.

**References:**
- [cloud.google.com/products/alloydb](https://cloud.google.com/products/alloydb)
- [docs.cloud.google.com/alloydb/docs/overview](https://docs.cloud.google.com/alloydb/docs/overview)
- [docs.cloud.google.com/spanner/docs/postgresql-interface](https://docs.cloud.google.com/spanner/docs/postgresql-interface)

</details>

---

### Exam 1 · Q19

**StreamNest Media runs a video streaming website that creates application logs and service configuration files in JSON and XML formats. These files do not follow a fixed relational table structure, but they include nested fields, tags, attributes, and hierarchical elements that help organize the meaning of the data. How should this type of data be classified?**

- A. Structured data
- B. Semi-structured data
- C. Unstructured data
- D. Relational data

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Semi-structured data

**Correct answer: B. Semi-structured data**

Semi-structured data has no fixed table schema but carries its own organizing markers, such as tags, keys, attributes and nesting. JSON and XML are the classic examples. The clue is "do not follow a fixed relational table structure, but they include nested fields, tags, attributes".

**Why the others are wrong:**
- **A. Structured data**: structured data fits a fixed schema of rows and columns, which these files do not.
- **C. Unstructured data**: unstructured data (images, audio, free text) has no organizing markers; JSON and XML do.
- **D. Relational data**: relational data lives in tables with defined relationships, a type of structured data.

**Remember:** Rows and columns = structured. JSON/XML with tags = semi-structured. Images, audio, free text = unstructured.

**References:**
- [cloud.google.com/bigquery/docs/semi-structured-data](https://cloud.google.com/bigquery/docs/semi-structured-data)
- [cloud.google.com/bigquery/docs/json-data](https://cloud.google.com/bigquery/docs/json-data)
- [cloud.google.com/bigquery/docs/xml-functions](https://cloud.google.com/bigquery/docs/xml-functions)

</details>

---

### Exam 1 · Q20

**BrightCart, an online grocery marketplace, wants a business intelligence solution that lets employees from sales, operations, and marketing explore trusted business data, build reports, and discover insights without depending on engineering teams for every analysis request. Which Google Cloud product or service should BrightCart use?**

- A. Spanner
- B. BigQuery
- C. Looker
- D. Dataflow

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Looker

**Correct answer: C. Looker**

Looker is Google Cloud's business intelligence platform. It gives business users governed, trusted data so they can explore, build reports and dashboards, and find insights on their own (self-service). The clue is employees from sales, operations and marketing working "without depending on engineering teams".

**Why the others are wrong:**
- **A. Spanner**: Spanner is a transactional database, not a BI tool.
- **B. BigQuery**: BigQuery is the data warehouse that stores and queries data; Looker is the BI layer that business users work in.
- **D. Dataflow**: Dataflow processes data in pipelines; it does not give business users reports.

**Remember:** Self-service reports and dashboards for business users = Looker. Warehouse = BigQuery.

**References:**
- [cloud.google.com/looker](https://cloud.google.com/looker)
- [cloud.google.com/bigquery/docs/introduction](https://cloud.google.com/bigquery/docs/introduction)
- [cloud.google.com/dataflow/docs/overview](https://cloud.google.com/dataflow/docs/overview)

</details>

---

### Exam 1 · Q22

**ShopNest, an ecommerce website, wants to improve customer experience by analyzing different kinds of information collected from its platform. Which type of information is an example of unstructured data that ShopNest can use for business decisions?**

- A. Written feedback submitted by customers after delivery
- B. GPS coordinates of partner store locations
- C. Monthly product revenue trends
- D. Stock quantity records in fulfillment centers

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Written feedback submitted by customers after delivery

**Correct answer: A. Written feedback submitted by customers after delivery**

Free-form written feedback has no fixed format or schema, so it is unstructured data. Machine learning (for example, sentiment analysis) can turn it into useful insight about customer experience. The clue is "written feedback", which is open text.

**Why the others are wrong:**
- **B. GPS coordinates**: coordinates are fixed numeric fields (latitude, longitude), so they are structured.
- **C. Monthly product revenue trends**: revenue figures fit neatly into rows and columns.
- **D. Stock quantity records**: inventory counts are classic structured table data.

**Remember:** Free text, images, audio, video = unstructured. Numbers in fixed fields = structured.

**References:**
- [cloud.google.com/learn/what-is-big-data](https://cloud.google.com/learn/what-is-big-data)
- [cloud.google.com/storage](https://cloud.google.com/storage)
- [cloud.google.com/bigquery](https://cloud.google.com/bigquery)

</details>

---

### Exam 1 · Q28

**PhotoNest Gallery stores millions of customer-uploaded images and backup files in Cloud Storage. The engineering team wants to reduce storage costs, but they do not want to create manual rules such as “move objects after 45 days” or “change storage class after a specific number of versions.” Instead, they want Cloud Storage to automatically move objects between storage classes based on how frequently each object is actually accessed. Which feature should they use?**

- A. Object Lifecycle Management
- B. Cloud Storage Autoclass
- C. Storage Transfer Service
- D. Cloud CDN

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Cloud Storage Autoclass

**Correct answer: B. Cloud Storage Autoclass**

Autoclass automatically moves each object to the most cost-effective storage class based on how often that object is actually accessed. No manual rules are needed. The clue is "do not want to create manual rules" and "based on how frequently each object is actually accessed".

**Why the others are wrong:**
- **A. Object Lifecycle Management**: lifecycle management uses rules you write, such as age or number of versions, which the team wants to avoid.
- **C. Storage Transfer Service**: it moves data into or between storage locations; it does not change storage classes based on access.
- **D. Cloud CDN**: Cloud CDN caches content near users for faster delivery; it does not lower storage costs.

**Remember:** Access-based, automatic class changes = Autoclass. Rules you write (age, versions) = lifecycle management.

**References:**
- [cloud.google.com/storage/docs/autoclass](https://cloud.google.com/storage/docs/autoclass)
- [cloud.google.com/storage/docs/lifecycle](https://cloud.google.com/storage/docs/lifecycle)
- [cloud.google.com/storage-transfer/docs/overview](https://cloud.google.com/storage-transfer/docs/overview)

</details>

---

### Exam 1 · Q32

**PhotoTrail is a travel-photo sharing website that stores millions of uploaded images and videos in Cloud Storage. Some files are downloaded frequently for a few days, while others may not be accessed again for months, and the team cannot reliably predict these access patterns. The company wants Cloud Storage to automatically reduce storage costs by placing infrequently accessed objects into colder storage classes without the team manually creating rules or analyzing object usage. Which Cloud Storage feature should they enable?**

- A. Object Versioning
- B. Autoclass
- C. Lifecycle management rules
- D. Requester Pays

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Autoclass

**Correct answer: B. Autoclass**

Autoclass watches each object's access pattern and automatically moves it to colder or warmer storage classes. It fits when access is unpredictable and the team does not want to write rules. The clue is "cannot reliably predict these access patterns" and "without the team manually creating rules".

**Why the others are wrong:**
- **A. Object Versioning**: it keeps old versions of objects for recovery; it does not lower storage costs.
- **C. Lifecycle management rules**: these need rules defined in advance (such as "after 30 days"), which the team wants to avoid.
- **D. Requester Pays**: it makes the person downloading the data pay for access; it does not change storage classes.

**Remember:** Unpredictable access + no manual rules = Autoclass.

**References:**
- [cloud.google.com/storage/docs/autoclass](https://cloud.google.com/storage/docs/autoclass)
- [cloud.google.com/storage/docs/lifecycle](https://cloud.google.com/storage/docs/lifecycle)
- [cloud.google.com/storage/docs/requester-pays](https://cloud.google.com/storage/docs/requester-pays)

</details>

---

### Exam 1 · Q34

**TrailWise Trips is building a generative AI assistant to help customers plan vacations from past bookings, support chats, destination reviews, and loyalty data. The leadership team wants to launch quickly, but the analytics team says the company’s data is spread across different systems, has inconsistent quality, and is not governed well enough for reliable AI use. The company wants the data to be unified, cleaned, trusted, and governed before using it for AI workloads. What concept best describes this target state of the data?**

- A. AI-ready data
- B. Coldline storage data
- C. Ephemeral data
- D. On-premises data

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. AI-ready data

**Correct answer: A. AI-ready data**

AI-ready data is data that is unified, clean, trusted and well governed, so AI models can use it reliably. Poor data quality leads to poor AI results. The clue is the target state: data that is "unified, cleaned, trusted, and governed before using it for AI workloads".

**Why the others are wrong:**
- **B. Coldline storage data**: Coldline is a Cloud Storage class for rarely accessed data; it says nothing about quality or governance.
- **C. Ephemeral data**: ephemeral data is short-lived or temporary, the opposite of a trusted foundation.
- **D. On-premises data**: this describes where data lives, not whether it is ready for AI.

**Remember:** Good AI needs good data: unified, high quality, governed = AI-ready data.

**References:**
- [cloud.google.com/learn/what-is-data-governance](https://cloud.google.com/learn/what-is-data-governance)
- [cloud.google.com/learn/what-is-a-data-cloud](https://cloud.google.com/learn/what-is-a-data-cloud)
- [cloud.google.com/storage/docs/storage-classes](https://cloud.google.com/storage/docs/storage-classes)

</details>

---

### Exam 1 · Q35

**FinSightHub is a financial analytics platform that collects transaction events, customer activity logs, and operational records from many systems. The company wants to describe the complete journey of this data, starting from creation and ingestion, continuing through processing and storage, and ending when the data is used for reporting, analytics, and AI-driven business decisions. What term best describes this end-to-end data lifecycle process?**

- A. Data center modernization
- B. Data supply chain
- C. Open source integration
- D. Infrastructure as a Service (IaaS)

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Data supply chain

**Correct answer: B. Data supply chain**

The data supply chain (also called the data value chain) describes data's full journey: creation and ingestion, processing, storage, and finally use in reporting, analytics and AI. The clue is "complete journey ... starting from creation and ingestion ... ending when the data is used".

**Why the others are wrong:**
- **A. Data center modernization**: this is about updating infrastructure, not the lifecycle of data.
- **C. Open source integration**: this is about combining open source tools, not the journey of data.
- **D. Infrastructure as a Service (IaaS)**: IaaS is a cloud service model for renting compute, storage and networking.

**Remember:** Data's end-to-end journey from creation to decisions = data supply chain (data value chain).

**References:**
- [cloud.google.com/docs/data](https://cloud.google.com/docs/data)
- [cloud.google.com/blog/topics/developers-practitioners/what-data-pipeline-architecture-should-i-use](https://cloud.google.com/blog/topics/developers-practitioners/what-data-pipeline-architecture-should-i-use)
- [cloud.google.com/learn/what-is-iaas](https://cloud.google.com/learn/what-is-iaas)

**⚠️ Note:** The bank uses "data supply chain" here and "data value chain" in Q1 for the same idea. Treat them as synonyms.

</details>

---

### Exam 1 · Q38

**TrendBasket is a fashion retail app that gathers customer information from its own website clicks, completed orders, abandoned carts, and loyalty membership forms. The marketing team wants to use this directly collected customer data to build personalized product recommendations and shopping offers. What type of data is this considered?**

- A. Second-party data
- B. Third-party data
- C. First-party data
- D. Open standard data

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. First-party data

**Correct answer: C. First-party data**

First-party data is collected directly by a company from its own customers through its own channels, such as website clicks, orders and loyalty sign-ups. It is usually the most reliable and relevant data for personalization. The clue is "directly collected customer data" from TrendBasket's own website and forms.

**Why the others are wrong:**
- **A. Second-party data**: this is another company's first-party data shared with you through a partnership.
- **B. Third-party data**: this is bought from outside providers who did not collect it from your customers.
- **D. Open standard data**: this is not a data source category; open standards are about formats and interoperability.

**Remember:** Your own channels = first-party. A partner's data = second-party. Bought from aggregators = third-party.

**References:**
- [support.google.com/adspolicy/answer/6242605](https://support.google.com/adspolicy/answer/6242605)
- [cloud.google.com/solutions/customer-data-platform](https://cloud.google.com/solutions/customer-data-platform)
- [cloud.google.com/solutions/marketing-analytics](https://cloud.google.com/solutions/marketing-analytics)

</details>

---

### Exam 1 · Q39

**FreshCart Rewards is planning a new advertising campaign for its grocery delivery app. The marketing team buys anonymized and aggregated audience segments from an outside data provider. This provider collected the data from multiple sources and does not directly interact with FreshCart Rewards customers. Which data classification best describes this audience data?**

- A. First-party data
- B. Second-party data
- C. Third-party data
- D. Unstructured data

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Third-party data

**Correct answer: C. Third-party data**

Third-party data is collected by an outside provider from many sources and sold to other companies. The provider has no direct relationship with the buyer's customers. The clues are "buys ... from an outside data provider", "multiple sources" and "does not directly interact with FreshCart Rewards customers".

**Why the others are wrong:**
- **A. First-party data**: first-party data comes from FreshCart's own customers through its own channels.
- **B. Second-party data**: second-party data is a partner's own first-party data shared directly, not aggregated from many sources.
- **D. Unstructured data**: this describes format, not source; audience segments are typically structured.

**Remember:** Bought from an aggregator with no direct customer relationship = third-party data.

**References:**
- [cloud.google.com/learn/what-is-big-data](https://cloud.google.com/learn/what-is-big-data)
- [support.google.com/google-ads/answer/7542935](https://support.google.com/google-ads/answer/7542935)
- [support.google.com/analytics/answer/11593727](https://support.google.com/analytics/answer/11593727)

</details>

---

### Exam 1 · Q44

**StreamWagon is a media analytics company that processes clickstream and viewing-history data with Apache Spark. Its data engineers are spending too much time provisioning clusters, adjusting cluster sizes, and handling Spark infrastructure operations. The team wants a fully managed, serverless Spark environment on Google Cloud so they can submit Spark jobs and focus mainly on application code. Which service best meets this requirement?**

- A. Managed Service for Apache Spark managed clusters
- B. Managed Service for Apache Spark serverless
- C. BigQuery
- D. Cloud Data Fusion

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Managed Service for Apache Spark serverless

**Correct answer: B. Managed Service for Apache Spark serverless**

The serverless option of Managed Service for Apache Spark (formerly Dataproc) lets teams submit Spark jobs without creating, sizing or managing clusters. Google handles the infrastructure and scaling. The clues are "too much time provisioning clusters", "fully managed, serverless Spark" and "focus mainly on application code".

**Why the others are wrong:**
- **A. Managed clusters**: this still requires creating and sizing clusters, the work the team wants to drop.
- **C. BigQuery**: BigQuery is a SQL data warehouse, not a place to run existing Spark jobs as-is.
- **D. Cloud Data Fusion**: it is a visual, no-code tool for building data pipelines, not a serverless Spark runtime.

**Remember:** Spark without managing clusters = Managed Service for Apache Spark serverless.

**References:**
- [cloud.google.com/products/managed-service-for-apache-spark](https://cloud.google.com/products/managed-service-for-apache-spark)
- [docs.cloud.google.com/managed-spark/docs](https://docs.cloud.google.com/managed-spark/docs)
- [docs.cloud.google.com/data-fusion/docs/concepts/overview](https://docs.cloud.google.com/data-fusion/docs/concepts/overview)

</details>

---

### Exam 1 · Q48

**RiverPay, a digital payments company, collects transaction records from customers in several regions. The analytics team wants a serverless data warehouse that can store large datasets, run fast SQL-based analysis, and support intelligent analytics without managing servers. Which Google Cloud product or service should RiverPay use?**

- A. Cloud Spanner
- B. Compute Engine
- C. BigQuery
- D. Dataflow

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. BigQuery

**Correct answer: C. BigQuery**

BigQuery is Google Cloud's serverless, fully managed data warehouse. It stores very large datasets, runs fast SQL analytics and has built-in ML and AI features. The clues are "serverless data warehouse", "fast SQL-based analysis" and "without managing servers".

**Why the others are wrong:**
- **A. Cloud Spanner**: Spanner is a transactional (OLTP) database, not an analytics warehouse.
- **B. Compute Engine**: it provides VMs that the team would need to manage.
- **D. Dataflow**: Dataflow processes streaming and batch data; it is not a warehouse for storing and querying.

**Remember:** Serverless data warehouse + SQL analytics = BigQuery.

**References:**
- [cloud.google.com/bigquery/docs/introduction](https://cloud.google.com/bigquery/docs/introduction)
- [cloud.google.com/spanner/docs/overview](https://cloud.google.com/spanner/docs/overview)
- [cloud.google.com/dataflow/docs/overview](https://cloud.google.com/dataflow/docs/overview)

</details>

---

### Exam 2 · Q5

**HealthVista Insights is building a company-wide analytics portal for teams that use data platforms across Google Cloud, AWS, and Azure. The organization wants an enterprise business intelligence solution that can model, explore, visualize, and query data across these different cloud environments without being tied to only one provider. Which Google Cloud product should they choose?**

- A. Looker
- B. Compute Engine
- C. Cloud Spanner
- D. Spot VMs

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Looker

**Correct answer: A. Looker**

Looker is Google Cloud's enterprise business intelligence platform. It lets teams model, explore, visualize, and query data, and it connects to databases on many clouds, not just Google Cloud. The clues are "enterprise business intelligence" and "across Google Cloud, AWS, and Azure".

**Why the others are wrong:**
- **B. Compute Engine**: Compute Engine provides virtual machines, not a BI tool.
- **C. Cloud Spanner**: Spanner is a globally distributed operational database, not a BI and visualization platform.
- **D. Spot VMs**: Spot VMs are low-cost, interruptible virtual machines and have nothing to do with BI.

**Remember:** Enterprise BI, dashboards, multicloud data modeling → Looker.

**References:**
- [docs.cloud.google.com/looker/docs](https://docs.cloud.google.com/looker/docs)
- [docs.cloud.google.com/bigquery/docs/looker](https://docs.cloud.google.com/bigquery/docs/looker)
- [cloud.google.com/compute/docs/instances/spot](https://cloud.google.com/compute/docs/instances/spot)

</details>

---

### Exam 2 · Q8

**FreshCart, an online grocery delivery website, wants managers and analysts to explore sales trends, build dashboards, understand customer behavior, and make better business decisions from company data. How would FreshCart benefit from using Looker?**

- A. Optimal identity and access management
- B. Leading serverless warehousing technology
- C. Robust data roll-back accuracy
- D. Advanced business intelligence and analytics

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Advanced business intelligence and analytics

**Correct answer: D. Advanced business intelligence and analytics**

Looker is a business intelligence (BI) platform. It helps managers and analysts explore data, build dashboards, and make data-driven decisions. The clues are "explore sales trends, build dashboards" and "make better business decisions".

**Why the others are wrong:**
- **A. Optimal identity and access management**: Access management is the job of IAM, not Looker.
- **B. Leading serverless warehousing technology**: The serverless data warehouse is BigQuery; Looker sits on top of it for BI.
- **C. Robust data roll-back accuracy**: Rolling back data is a database feature, not what Looker provides.

**Remember:** Dashboards and BI for business users → Looker; storing and querying at scale → BigQuery.

**References:**
- [cloud.google.com/looker](https://cloud.google.com/looker)
- [docs.cloud.google.com/looker/docs](https://docs.cloud.google.com/looker/docs)
- [cloud.google.com/looker-bi](https://cloud.google.com/looker-bi)

</details>

---

### Exam 2 · Q12

**BrightShelf, an online bookstore, keeps a large collection of product images, sales reports, and historical order exports. The team frequently reads only the latest files, while older files are accessed rarely. BrightShelf wants to lower storage costs by keeping less-used data in Nearline storage, Coldline storage, and Archive storage. Which Google Cloud product should BrightShelf use?**

- A. Filestore
- B. Cloud Storage
- C. Knowledge Catalog
- D. Spanner

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Cloud Storage

**Correct answer: B. Cloud Storage**

Cloud Storage is Google Cloud's object storage for files like images, reports, and exports. It offers storage classes (Standard, Nearline, Coldline, Archive) so rarely used data costs less. The clue is the direct mention of Nearline, Coldline, and Archive, which are Cloud Storage classes.

**Why the others are wrong:**
- **A. Filestore**: Filestore is managed file (NFS) storage for apps that need a shared file system, without these storage classes.
- **C. Knowledge Catalog**: This is a catalog for finding and governing data, not a place to store files.
- **D. Spanner**: Spanner is a relational database for transactions, not low-cost file storage.

**Remember:** Nearline, Coldline, Archive → Cloud Storage classes for less frequently accessed data.

**References:**
- [docs.cloud.google.com/storage/docs/storage-classes](https://docs.cloud.google.com/storage/docs/storage-classes)
- [docs.cloud.google.com/storage/docs/lifecycle](https://docs.cloud.google.com/storage/docs/lifecycle)
- [docs.cloud.google.com/filestore/docs/overview](https://docs.cloud.google.com/filestore/docs/overview)

</details>

---

### Exam 2 · Q14

**TravelNest Analytics stores booking history in BigQuery on Google Cloud, while its partner clickstream files remain in object storage in another large public cloud. The analytics team wants to run SQL-based analysis across both locations without first copying all partner data into Google Cloud. Which multicloud product should they choose?**

- A. AlloyDB Omni
- B. Cloud SQL
- C. BigQuery Omni
- D. Cloud Run functions

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. BigQuery Omni

**Correct answer: C. BigQuery Omni**

BigQuery Omni lets you run BigQuery SQL on data stored in other public clouds, such as AWS or Azure, without moving it into Google Cloud first. The clues are "object storage in another large public cloud" and "without first copying".

**Why the others are wrong:**
- **A. AlloyDB Omni**: AlloyDB Omni is a PostgreSQL-compatible database you run anywhere; it is not for analyzing files in another cloud.
- **B. Cloud SQL**: Cloud SQL is a managed relational database on Google Cloud, not a multicloud analytics tool.
- **D. Cloud Run functions**: Cloud Run functions run event-driven code, not SQL analytics across clouds.

**Remember:** Query data in AWS/Azure with BigQuery, without moving it → BigQuery Omni.

**References:**
- [docs.cloud.google.com/bigquery/docs/omni-introduction](https://docs.cloud.google.com/bigquery/docs/omni-introduction)
- [docs.cloud.google.com/alloydb/omni/docs](https://docs.cloud.google.com/alloydb/omni/docs)
- [docs.cloud.google.com/sql/docs/introduction](https://docs.cloud.google.com/sql/docs/introduction)

</details>

---

### Exam 2 · Q21

**CarePulse, a preventive healthcare mobile app, wants to monitor patient wellness more efficiently. The company needs a way to automatically collect health measurements such as heart rate, activity level, sleep patterns, and other patient signals without requiring patients or staff to manually enter the data. What should CarePulse encourage patients to do?**

- A. Use at-home health screening devices and then upload their health data every evening
- B. Wear Internet of Things (IoT) devices that upload their health data in real time
- C. Self-assess their health data and then document and upload it in real time
- D. Visit a clinic assistant who will use Internet of Things (IoT) devices to collect and upload their health data

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Wear Internet of Things (IoT) devices that upload their health data in real time

**Correct answer: B. Wear Internet of Things (IoT) devices that upload their health data in real time**

Wearable IoT devices collect signals like heart rate, activity, and sleep automatically and send them continuously. Nobody has to type anything in. The clues are "automatically collect" and "without requiring patients or staff to manually enter the data".

**Why the others are wrong:**
- **A. Home devices, upload every evening**: Uploading once a day is a manual step and is not continuous.
- **C. Self-assess and upload**: Self-reporting is manual and less accurate.
- **D. Visit a clinic assistant**: This needs staff and in-person visits, which is the opposite of automatic.

**Remember:** Automatic, continuous data collection from the physical world → IoT devices.

**References:**
- [docs.cloud.google.com/architecture/connected-devices](https://docs.cloud.google.com/architecture/connected-devices)
- [docs.cloud.google.com/healthcare-api/docs/concepts/fhir](https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir)
- [cloud.google.com/solutions/healthcare-life-sciences](https://cloud.google.com/solutions/healthcare-life-sciences)

</details>

---

### Exam 2 · Q23

**FreshCart Analytics wants to create a managed data pipeline that processes and transforms sales and inventory data before loading it into a data warehouse for reconciliation. The pipeline must scale automatically as data volume grows and should require minimal operational management. Which Google Cloud product or service should FreshCart Analytics choose?**

- A. Cloud Bigtable
- B. Cloud Storage
- C. Pub/Sub
- D. Dataflow

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Dataflow

**Correct answer: D. Dataflow**

Dataflow is Google Cloud's fully managed service for data processing pipelines. It transforms data in batch or streaming mode, scales automatically, and loads results into a warehouse like BigQuery. The clues are "managed data pipeline", "processes and transforms", and "scale automatically".

**Why the others are wrong:**
- **A. Cloud Bigtable**: Bigtable is a NoSQL database for large, fast reads and writes, not a transformation pipeline.
- **B. Cloud Storage**: Cloud Storage stores files; it does not process or transform data.
- **C. Pub/Sub**: Pub/Sub moves messages between systems, but it does not transform them.

**Remember:** Transform data in a managed, autoscaling pipeline (ETL, batch or streaming) → Dataflow.

**References:**
- [cloud.google.com/dataflow/docs](https://cloud.google.com/dataflow/docs)
- [cloud.google.com/dataflow/docs/concepts/overview](https://cloud.google.com/dataflow/docs/concepts/overview)
- [cloud.google.com/pubsub/docs/overview](https://cloud.google.com/pubsub/docs/overview)

</details>

---

### Exam 2 · Q25

**GlobePay, a digital payments company, runs its application for customers in North America, Europe, and Asia. The company needs a highly available operational database that can keep transactional data consistent and available across multiple geographic regions. How would GlobePay benefit from managing its data with Cloud Spanner?**

- A. Cloud Spanner is optimized for cold storage
- B. Cloud Spanner replicates data across regions in real time
- C. Cloud Spanner is optimized to ingest unstructured data
- D. Cloud Spanner visualizes and analyzes data in real time

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Cloud Spanner replicates data across regions in real time

**Correct answer: B. Cloud Spanner replicates data across regions in real time**

Spanner is a globally distributed relational database. It replicates data across regions synchronously and keeps transactions strongly consistent, with very high availability. The clues are "consistent and available across multiple geographic regions" and "transactional data".

**Why the others are wrong:**
- **A. Optimized for cold storage**: Cold storage is a Cloud Storage use case (Coldline, Archive), not Spanner.
- **C. Optimized for unstructured data**: Spanner is relational and stores structured data.
- **D. Visualizes and analyzes data**: Visualization is the job of BI tools like Looker; analytics is BigQuery.

**Remember:** Global, strongly consistent, highly available transactions → Spanner.

**References:**
- [cloud.google.com/spanner](https://cloud.google.com/spanner)
- [docs.cloud.google.com/spanner/docs/instance-configurations](https://docs.cloud.google.com/spanner/docs/instance-configurations)
- [docs.cloud.google.com/spanner/docs/replication](https://docs.cloud.google.com/spanner/docs/replication)

</details>

---

### Exam 2 · Q27

**HelpHive is a customer service platform that has added an AI support assistant to handle chats and voice calls. The assistant produces large volumes of text transcripts, call metadata, and speech-related files. Why should HelpHive use a cloud data warehouse such as BigQuery to understand this data?**

- A. To automatically display both text and speech data in live dashboards without extra tools
- B. To store and analyze large volumes of structured and unstructured data at scale
- C. To encrypt network traffic between cloud resources and on-premises data centers
- D. To convert organized database records into unstructured text and audio files

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. To store and analyze large volumes of structured and unstructured data at scale

**Correct answer: B. To store and analyze large volumes of structured and unstructured data at scale**

BigQuery is a serverless data warehouse built for analyzing very large datasets with SQL. Besides tables of call metadata, it can work with text such as transcripts, and with files kept in Cloud Storage through features like object tables and built-in AI functions. That lets HelpHive find patterns across everything the assistant produces without managing servers.

**Why the others are wrong:**
- **A. Automatic live dashboards**: BigQuery stores and queries data. Dashboards come from a BI tool such as Looker.
- **C. Encrypt network traffic**: Encrypting links between sites is a networking and security task, not analytics.
- **D. Convert records into text and audio**: This is the opposite of analysis and not what a warehouse does.

**Remember:** Analyze huge volumes of mixed data with SQL, serverless → BigQuery.

**References:**
- [cloud.google.com/bigquery/docs/introduction](https://cloud.google.com/bigquery/docs/introduction)
- [cloud.google.com/bigquery/docs/object-tables](https://cloud.google.com/bigquery/docs/object-tables)
- [cloud.google.com/bigquery/docs/write-api-streaming](https://cloud.google.com/bigquery/docs/write-api-streaming)

</details>

---

### Exam 2 · Q30

**LumaCart is an online grocery marketplace that stores customer profiles, orders, and inventory records in Cloud SQL. The leadership team wants to use this operational data to understand sales trends and customer behavior. How does Cloud SQL help LumaCart create business insights?**

- A. Integrates with business intelligence and analytics platforms
- B. Builds prediction outputs directly by running machine learning models
- C. Automatically creates live dashboards and intelligent charts
- D. Converts unstructured business files into relational tables

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Integrates with business intelligence and analytics platforms

**Correct answer: A. Integrates with business intelligence and analytics platforms**

Cloud SQL is a managed relational database for operational data. It does not create insights on its own, but it connects to analytics and BI tools such as BigQuery and Looker. Those tools turn the data into trends and reports.

**Why the others are wrong:**
- **B. Runs ML models directly**: Cloud SQL is a transactional database, not an ML platform.
- **C. Creates live dashboards automatically**: Dashboards come from BI tools like Looker, not from Cloud SQL.
- **D. Converts unstructured files to tables**: Cloud SQL stores structured data; it does not convert unstructured files.

**Remember:** Operational database (Cloud SQL) + BI/analytics tools = business insights.

**References:**
- [cloud.google.com/sql/docs/introduction](https://cloud.google.com/sql/docs/introduction)
- [cloud.google.com/looker](https://cloud.google.com/looker)
- [cloud.google.com/bigquery/docs/introduction](https://cloud.google.com/bigquery/docs/introduction)

</details>

---

### Exam 2 · Q33

**RideNest, a bike-sharing mobile app, collects trip records from its app, JSON logs from scooters, support chat transcripts, and maintenance images. The analytics team wants to keep all of this structured, semi-structured, and unstructured data together in its original format before deciding how to process it later. Which cloud data management solution should RideNest use?**

- A. Data field
- B. Data lake
- C. Database
- D. Data warehouse

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Data lake

**Correct answer: B. Data lake**

A data lake stores large amounts of raw data of any type (structured, semi-structured, unstructured) in its original format. The data can be processed later when needed. On Google Cloud, Cloud Storage is commonly used for this. The clues are "all of this … data together" and "in its original format".

**Why the others are wrong:**
- **A. Data field**: A data field is a single attribute in a record, not a storage solution.
- **C. Database**: A database stores organized data for applications, usually with a defined schema.
- **D. Data warehouse**: A warehouse holds cleaned, structured data ready for analysis, not raw files in any format.

**Remember:** Raw data, any format, decide later → data lake; cleaned data for analysis → data warehouse.

**References:**
- [cloud.google.com/learn/what-is-a-data-lake](https://cloud.google.com/learn/what-is-a-data-lake)
- [cloud.google.com/discover/data-lake-vs-data-warehouse](https://cloud.google.com/discover/data-lake-vs-data-warehouse)
- [cloud.google.com/storage/docs/introduction](https://cloud.google.com/storage/docs/introduction)

</details>

---

### Exam 2 · Q40

**FinSecure Ledger is modernizing the database layer for its core payment-processing platform. The application needs a highly scalable PostgreSQL-compatible database, but compliance rules require the database to run inside FinSecure Ledger’s private on-premises data center while still using Google’s database technology. Which product should the team use?**

- A. AlloyDB Omni
- B. Cloud Storage
- C. BigQuery
- D. Cloud Run

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. AlloyDB Omni

**Correct answer: A. AlloyDB Omni**

AlloyDB Omni is a downloadable version of AlloyDB, Google's PostgreSQL-compatible database. It can run anywhere, including a company's own data center. FinSecure gets Google's database technology while meeting the rule to stay on-premises. The clues are "PostgreSQL-compatible" and "inside … private on-premises data center".

**Why the others are wrong:**
- **B. Cloud Storage**: Cloud Storage is object storage in Google Cloud, not a PostgreSQL database.
- **C. BigQuery**: BigQuery is an analytics warehouse, not a transactional PostgreSQL database for payments.
- **D. Cloud Run**: Cloud Run runs containers serverlessly; it is not a database.

**Remember:** PostgreSQL-compatible, Google tech, run on-premises or in other clouds → AlloyDB Omni.

**References:**
- [cloud.google.com/alloydb/omni](https://cloud.google.com/alloydb/omni)
- [docs.cloud.google.com/storage/docs/introduction](https://docs.cloud.google.com/storage/docs/introduction)
- [docs.cloud.google.com/bigquery/docs/introduction](https://docs.cloud.google.com/bigquery/docs/introduction)

</details>

---

### Exam 3 · Q4

**StreamHive, a media learning app, has accumulated a large archive of unstructured files such as recorded lessons, podcasts, images, and raw video clips. The company wants a Google Cloud storage solution that can hold large volumes of these files reliably and cost-effectively. Which storage solution should StreamHive use?**

- A. Spanner
- B. Cloud Storage
- C. Bigtable
- D. Cloud SQL

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Cloud Storage

**Correct answer: B. Cloud Storage**

Cloud Storage is Google Cloud's object storage. It holds any amount of unstructured files such as video, audio and images, with high durability and storage classes that lower cost for rarely used data. The clues are "unstructured files", "large volumes" and "cost-effectively".

**Why the others are wrong:**
- **A. Spanner**: A globally distributed relational database for transactions, not a file store.
- **C. Bigtable**: A NoSQL wide-column database for high-throughput key-value data, not media files.
- **D. Cloud SQL**: A managed relational database for structured, transactional data.

**Remember:** Files, images, video, backups, archives = Cloud Storage.

**References:**
- [docs.cloud.google.com/storage/docs/introduction](https://docs.cloud.google.com/storage/docs/introduction)
- [docs.cloud.google.com/storage/docs/storage-classes](https://docs.cloud.google.com/storage/docs/storage-classes)
- [docs.cloud.google.com/bigtable/docs/overview](https://docs.cloud.google.com/bigtable/docs/overview)

</details>

---

### Exam 3 · Q5

**MediRide, a health transportation booking app, forms a partnership with CareInn, a senior living network. CareInn securely shares its resident appointment and stay-preference data directly with MediRide so MediRide can offer better ride packages to shared customers. From MediRide’s perspective, what type of data is this?**

- A. First-party data
- B. Second-party data
- C. Third-party data
- D. Public domain data

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Second-party data

**Correct answer: B. Second-party data**

Second-party data is another organization's first-party data that it shares directly with you as a partner. CareInn collected the data from its own residents and shares it straight with MediRide, so for MediRide it is second-party.

**Why the others are wrong:**
- **A. First-party data**: MediRide did not collect it from its own customers.
- **C. Third-party data**: Third-party data is bought from a provider that aggregates data, not shared directly by a partner.
- **D. Public domain data**: This data is private and shared securely, not openly available.

**Remember:** Own customers = first-party. Partner shares directly = second-party. Bought = third-party.

**References:**
- [support.google.com/adspolicy/answer/6242605](https://support.google.com/adspolicy/answer/6242605)
- [business.google.com/us/privacy/strategy](https://business.google.com/us/privacy/strategy)
- [business.adobe.com/blog/basics/dmp-cdp-crm-whats-the-difference-and-what-do-you-need](https://business.adobe.com/blog/basics/dmp-cdp-crm-whats-the-difference-and-what-do-you-need)

</details>

---

### Exam 3 · Q6

**BrightCast, a sports highlights streaming website, stores large collections of match commentary audio clips and game replay video files. These files do not follow a fixed table structure or predefined schema, and they are stored along with HTML pages and JSON metadata documents. How should the audio and video files be classified?**

- A. Structured data
- B. Semi-structured data
- C. Unstructured data
- D. Relational data

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Unstructured data

**Correct answer: C. Unstructured data**

Audio and video files have no fixed schema or rows and columns. That makes them unstructured data. The stem even says they "do not follow a fixed table structure or predefined schema".

**Why the others are wrong:**
- **A. Structured data**: Structured data fits a fixed schema, like tables in a database.
- **B. Semi-structured data**: This fits the JSON metadata and HTML, which have tags or keys, but not the audio and video files.
- **D. Relational data**: Relational data is structured data in related tables.

**Remember:** Audio, video, images, free text = unstructured. JSON, HTML, XML = semi-structured.

**References:**
- [cloud.google.com/storage](https://cloud.google.com/storage)
- [docs.cloud.google.com/bigquery/docs/object-table-introduction](https://docs.cloud.google.com/bigquery/docs/object-table-introduction)
- [docs.cloud.google.com/architecture/ml-on-gcp-best-practices](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices)

</details>

---

### Exam 3 · Q9

**CareBridge Advisors, a healthcare consulting company, needs its employee portal to share and access different volumes of confidential staff documents across offices in several countries. Why would using Cloud Storage be beneficial for CareBridge Advisors?**

- A. It stores geographically distributed copies of data to reduce the risk of loss.
- B. It provides a paid add-on that turns on data encryption.
- C. It randomly places data in different storage locations to protect against attacks.
- D. It has a small minimum storage quantity requirement.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. It stores geographically distributed copies of data to reduce the risk of loss.

**Correct answer: A. It stores geographically distributed copies of data to reduce the risk of loss.**

Cloud Storage stores data redundantly, and multi-region or dual-region buckets keep copies in separate geographic locations. This protects against loss and suits a company with offices in several countries.

**Why the others are wrong:**
- **B. Paid add-on for encryption**: Google Cloud encrypts all data at rest by default at no extra cost.
- **C. Randomly places data to protect against attacks**: Data placement is based on the location you choose, not random.
- **D. Small minimum storage quantity**: Cloud Storage has no minimum storage quantity; this is not a real feature to rely on.

**Remember:** Cloud Storage = durable, redundant, optionally multi-region object storage.

**References:**
- [cloud.google.com/storage/docs/locations](https://cloud.google.com/storage/docs/locations)
- [cloud.google.com/storage/docs/availability-durability](https://cloud.google.com/storage/docs/availability-durability)
- [cloud.google.com/storage/docs/encryption/default-keys](https://cloud.google.com/storage/docs/encryption/default-keys)

**⚠️ Note:** Geographically separate copies are only true for multi-region and dual-region buckets. A regional bucket keeps redundant copies across zones in one region. The key is still the best option, so pick it on this exam.

</details>

---

### Exam 3 · Q15

**Trendora, a regional fashion marketplace, is building a new ecommerce application on Google Cloud. The application needs a cost-effective transactional database for customer orders, carts, and payments, and it will serve users only from one region. Which service should Trendora use?**

- A. BigQuery
- B. Bigtable
- C. Spanner
- D. Cloud SQL

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Cloud SQL

**Correct answer: D. Cloud SQL**

Cloud SQL is a managed relational database for transactional (OLTP) workloads like orders and payments. It is cost-effective when the app serves one region. The clues are "transactional", "cost-effective" and "only from one region".

**Why the others are wrong:**
- **A. BigQuery**: A data warehouse for analytics, not an app's transactional database.
- **B. Bigtable**: A NoSQL database for huge, high-throughput key-value data, not relational transactions.
- **C. Spanner**: Relational and transactional, but built for global scale; more than a single-region store needs.

**Remember:** Relational + regional + cost-effective = Cloud SQL. Relational + global scale = Spanner.

**References:**
- [docs.cloud.google.com/sql/docs](https://docs.cloud.google.com/sql/docs)
- [docs.cloud.google.com/bigquery/docs](https://docs.cloud.google.com/bigquery/docs)
- [docs.cloud.google.com/bigtable/docs](https://docs.cloud.google.com/bigtable/docs)

</details>

---

### Exam 3 · Q16

**StyleNest, an online apparel store, is training a machine learning model to suggest relevant products to shoppers. The training dataset includes customers’ past purchases and browsing behavior, but it is missing profile attributes such as age group, gender, and location. The recommendation results are weak because an important part of the dataset was not included. Which data quality dimension is causing the poor model performance?**

- A. Validity
- B. Accuracy
- C. Timeliness
- D. Completeness

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Completeness

**Correct answer: D. Completeness**

Completeness asks whether all the required data is present. Profile attributes like age group, gender and location are missing, so the dataset is incomplete. The clue is "an important part of the dataset was not included".

**Why the others are wrong:**
- **A. Validity**: Validity is whether values follow the expected format or rules.
- **B. Accuracy**: Accuracy is whether values are correct, not whether they exist.
- **C. Timeliness**: Timeliness is whether data is current and available when needed.

**Remember:** Missing data = completeness. Wrong values = accuracy. Wrong format = validity.

**References:**
- [cloud.google.com/learn/what-is-data-governance](https://cloud.google.com/learn/what-is-data-governance)
- [docs.cloud.google.com/dataplex/docs/use-auto-data-quality](https://docs.cloud.google.com/dataplex/docs/use-auto-data-quality)
- [ibm.com/think/topics/data-quality-dimensions](https://ibm.com/think/topics/data-quality-dimensions)

</details>

---

### Exam 3 · Q26

**TrailPulse is a fitness tracking app that receives live activity events from thousands of users, such as step counts, heart-rate readings, and GPS updates. The analytics team wants to analyze these incoming events as they arrive so the app can show near real-time insights. What is a defining function of streaming analytics?**

- A. Processing data records continuously
- B. Processing data records in batches
- C. Processing a single historical data reload
- D. Accessing data with high latency

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Processing data records continuously

**Correct answer: A. Processing data records continuously**

Streaming analytics processes events continuously as they arrive, so insights are available in near real time. The clue is "analyze these incoming events as they arrive".

**Why the others are wrong:**
- **B. Processing in batches**: Batch processing collects data and handles it later in groups.
- **C. A single historical data reload**: That is a one-time batch load, not streaming.
- **D. Accessing data with high latency**: Streaming aims for low latency.

**Remember:** Streaming = continuous, as it arrives. Batch = scheduled groups.

**References:**
- [cloud.google.com/learn/what-is-streaming-analytics](https://cloud.google.com/learn/what-is-streaming-analytics)
- [cloud.google.com/solutions/stream-analytics](https://cloud.google.com/solutions/stream-analytics)
- [docs.cloud.google.com/dataflow/docs/concepts/streaming-pipelines](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-pipelines)

</details>

---

### Exam 3 · Q33

**FitCart, a grocery delivery mobile app, is documenting how customer order data is first collected from app events, then cleaned and standardized in analytics pipelines, and finally used by a recommendation model to suggest products. What is this end-to-end view of how data is collected, transformed, and used called?**

- A. Cloud resource hierarchy
- B. Compute modernization
- C. The data supply chain
- D. Multi-cloud networking

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. The data supply chain

**Correct answer: C. The data supply chain**

The data supply chain (also called the data value chain) is the end-to-end journey of data: collected, processed and transformed, stored, then used for analytics or AI. The stem walks through exactly that path from app events to a recommendation model.

**Why the others are wrong:**
- **A. Cloud resource hierarchy**: That organizes Google Cloud resources into organization, folders and projects.
- **B. Compute modernization**: That is about updating how applications run, not data flow.
- **D. Multi-cloud networking**: That connects networks across cloud providers.

**Remember:** Collect, transform, use: the end-to-end data journey = data supply chain.

**References:**
- [cloud.google.com/discover/what-is-data-architecture](https://cloud.google.com/discover/what-is-data-architecture)
- [docs.cloud.google.com/docs/data](https://docs.cloud.google.com/docs/data)
- [cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)

</details>

---

### Exam 3 · Q34

**StreamHive, a music analytics startup, wants to execute Apache Spark batch jobs on Google Cloud for playlist trend analysis. The engineering team does not want to create, operate, scale, or tune Spark clusters, and prefers a fully serverless option where they only submit the workload. Which service should they choose?**

- A. Managed Service for Apache Spark on clusters
- B. Managed Service for Apache Spark serverless deployment
- C. Cloud SQL
- D. Compute Engine

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Managed Service for Apache Spark serverless deployment

**Correct answer: B. Managed Service for Apache Spark serverless deployment**

The serverless option of Managed Service for Apache Spark (formerly Dataproc) runs Spark batch jobs without any clusters to create or manage. You submit the workload and Google handles the infrastructure and scaling. The clues are "does not want to create, operate, scale, or tune Spark clusters" and "fully serverless".

**Why the others are wrong:**
- **A. Managed Service for Apache Spark on clusters**: It still requires creating and sizing clusters.
- **C. Cloud SQL**: A relational database; it doesn't run Spark jobs.
- **D. Compute Engine**: You'd have to build and run your own Spark cluster on VMs, which is the most work.

**Remember:** Spark with no clusters to manage = the serverless option.

**References:**
- [docs.cloud.google.com/managed-spark/docs/serverless-overview](https://docs.cloud.google.com/managed-spark/docs/serverless-overview)
- [cloud.google.com/products/managed-service-for-apache-spark](https://cloud.google.com/products/managed-service-for-apache-spark)
- [docs.cloud.google.com/sql/docs/introduction](https://docs.cloud.google.com/sql/docs/introduction)

</details>

---

### Exam 3 · Q38

**TrustLedger Bank, a digital lending platform, is preparing to launch AI agents that can help employees analyze customer risk and automate routine financial workflows. Before deployment, the bank is unifying fragmented datasets, applying strong governance controls, improving data quality, and making trusted data easier for teams to discover and use. What is TrustLedger Bank creating?**

- A. A legacy data center
- B. An AI-ready data foundation
- C. A hardware-defined network
- D. A perimeter security model

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. An AI-ready data foundation

**Correct answer: B. An AI-ready data foundation**

An AI-ready data foundation is data that is unified, clean, governed and easy to discover, so AI and agents can use it reliably. The bank is unifying datasets, applying governance and improving quality before launching AI agents, which is exactly that.

**Why the others are wrong:**
- **A. A legacy data center**: The bank is modernizing, not building old on-premises infrastructure.
- **C. A hardware-defined network**: The work is about data, not networking.
- **D. A perimeter security model**: That is an older security approach, unrelated to preparing data for AI.

**Remember:** Unified, clean, governed data before AI = AI-ready data foundation.

**References:**
- [cloud.google.com/learn/what-is-data-governance](https://cloud.google.com/learn/what-is-data-governance)
- [cloud.google.com/transform/how-to-build-strong-data-foundations-gen-ai](https://cloud.google.com/transform/how-to-build-strong-data-foundations-gen-ai)
- [docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components)

</details>

---

### Exam 3 · Q39

**FinoraCart is modernizing a legacy enterprise transaction database for its retail payment platform on Google Cloud. The team needs very high performance and availability, but they also want to stay aligned with an open-source database engine so they can reduce the risk of restrictive vendor lock-in. Which Google Cloud service should they choose?**

- A. Bigtable
- B. Spanner
- C. AlloyDB for PostgreSQL
- D. Firestore in Datastore mode

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. AlloyDB for PostgreSQL

**Correct answer: C. AlloyDB for PostgreSQL**

AlloyDB for PostgreSQL is a fully managed, PostgreSQL-compatible database built for high performance and availability on enterprise transactional workloads. Because it is compatible with open-source PostgreSQL, apps and skills can move more easily, which reduces lock-in. The clues are "very high performance and availability" and "open-source database engine".

**Why the others are wrong:**
- **A. Bigtable**: A NoSQL wide-column database; it isn't relational or based on an open-source SQL engine.
- **B. Spanner**: High performance and availability, but its own Google-built engine; less closely tied to open-source PostgreSQL.
- **D. Firestore in Datastore mode**: A NoSQL document database, not for enterprise relational transactions.

**Remember:** Enterprise performance + PostgreSQL compatibility = AlloyDB.

**References:**
- [docs.cloud.google.com/alloydb/docs](https://docs.cloud.google.com/alloydb/docs)
- [docs.cloud.google.com/spanner/docs](https://docs.cloud.google.com/spanner/docs)
- [docs.cloud.google.com/bigtable/docs](https://docs.cloud.google.com/bigtable/docs)

**⚠️ Note:** AlloyDB itself is not open source. It is compatible with open-source PostgreSQL, which is what "aligned with an open-source engine" means. Spanner also offers a PostgreSQL interface, but AlloyDB is the closer fit, so pick it on this exam.

</details>

---

### Exam 3 · Q41

**PetNest Analytics, a mobile app company, has accumulated several petabytes of historical user activity and transaction data. The analytics team needs a fast, scalable, fully managed solution to run advanced queries and analysis across this large dataset. Which Google Cloud product or service should PetNest Analytics use?**

- A. BigQuery
- B. Cloud SQL
- C. Firestore
- D. Cloud Storage

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. BigQuery

**Correct answer: A. BigQuery**

BigQuery is Google Cloud's serverless, fully managed data warehouse. It runs fast SQL analytics over terabytes to petabytes of data. The clues are "petabytes", "advanced queries and analysis" and "fully managed".

**Why the others are wrong:**
- **B. Cloud SQL**: A transactional database, not built for petabyte-scale analytics.
- **C. Firestore**: A NoSQL document database for apps, not large-scale analysis.
- **D. Cloud Storage**: It stores files cheaply but isn't a query and analysis engine by itself.

**Remember:** Large-scale analytics with SQL = BigQuery.

**References:**
- [cloud.google.com/bigquery/docs/introduction](https://cloud.google.com/bigquery/docs/introduction)
- [cloud.google.com/sql/docs/introduction](https://cloud.google.com/sql/docs/introduction)
- [cloud.google.com/storage/docs/introduction](https://cloud.google.com/storage/docs/introduction)

</details>

---

### Exam 3 · Q46

**MediBridge Health is preparing clinical records for a machine learning model that will help predict patient follow-up needs. During data profiling, the team notices that many records do not contain required attributes such as date of birth, heart rate, and diagnosis code. Which data quality dimension is affected by this issue?**

- A. Timeliness
- B. Completeness
- C. Uniqueness
- D. Validity

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Completeness

**Correct answer: B. Completeness**

Completeness measures whether all required data is present. Records missing date of birth, heart rate and diagnosis code are incomplete. The clue is "do not contain required attributes".

**Why the others are wrong:**
- **A. Timeliness**: That is about whether data is current, not missing.
- **C. Uniqueness**: That is about duplicate records.
- **D. Validity**: That is about values following the expected format or rules.

**Remember:** Missing required fields = completeness.

**References:**
- [cloud.google.com/learn/what-is-data-governance](https://cloud.google.com/learn/what-is-data-governance)
- [docs.cloud.google.com/dataplex/docs/auto-data-quality-overview](https://docs.cloud.google.com/dataplex/docs/auto-data-quality-overview)
- [docs.cloud.google.com/dataplex/docs/use-auto-data-quality](https://docs.cloud.google.com/dataplex/docs/use-auto-data-quality)

</details>

---

### Exam 4 · Q13

**HealthBridge Analytics stores database export files in Cloud Storage for disaster recovery. The files are rarely needed and are expected to be read only once every 12 months during recovery testing. Which Cloud Storage class should HealthBridge Analytics choose to minimize storage cost?**

- A. Coldline class
- B. Standard class
- C. Nearline class
- D. Archive class

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Archive class

**Correct answer: D. Archive class**

Archive is the cheapest Cloud Storage class for data accessed less than once a year. Disaster-recovery exports read only during a yearly test fit it exactly. Archive has the lowest storage price, with higher retrieval costs and a longer minimum storage period, which is fine for rarely read data.

**Why the others are wrong:**
- **A. Coldline class**: Coldline suits data read about once a quarter; it costs more to store than Archive.
- **B. Standard class**: Standard is for frequently accessed data and has the highest storage price.
- **C. Nearline class**: Nearline suits data read about once a month, too frequent a pattern for this case.

**Remember:** Monthly → Nearline. Quarterly → Coldline. Yearly or less → Archive.

**References:**
- [docs.cloud.google.com/storage/docs/storage-classes](https://docs.cloud.google.com/storage/docs/storage-classes)
- [cloud.google.com/storage/pricing](https://cloud.google.com/storage/pricing)
- [docs.cloud.google.com/architecture/dr-scenarios-planning-guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide)

</details>

---

### Exam 4 · Q23

**MealTrail, a small food delivery app, needs a budget-friendly database to store customer profiles, restaurant menus, orders, and payment records. The app requires SQL queries and a relational structure, but the team does not want to manage database servers manually. Which Google Cloud service should MealTrail use?**

- A. Cloud Storage
- B. BigQuery
- C. Cloud SQL
- D. Dataflow

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Cloud SQL

**Correct answer: C. Cloud SQL**

Cloud SQL is Google Cloud's fully managed relational database for MySQL, PostgreSQL and SQL Server. It supports SQL and tables, and Google handles patching, backups and server maintenance. For a small app it is a cost-effective choice.

**Why the others are wrong:**
- **A. Cloud Storage**: Cloud Storage holds objects (files), not relational tables with SQL queries.
- **B. BigQuery**: BigQuery is a data warehouse for analytics, not an operational database for an app's orders and payments.
- **D. Dataflow**: Dataflow processes data in pipelines; it doesn't store it as a database.

**Remember:** Small or medium relational app database, managed → Cloud SQL.

**References:**
- [docs.cloud.google.com/sql/docs/introduction](https://docs.cloud.google.com/sql/docs/introduction)
- [docs.cloud.google.com/bigquery/docs/introduction](https://docs.cloud.google.com/bigquery/docs/introduction)
- [docs.cloud.google.com/dataflow/docs/overview](https://docs.cloud.google.com/dataflow/docs/overview)

</details>

---

### Exam 4 · Q30

**ShopSphere, an online shopping platform, is evaluating which data should be stored directly in a relational database. Which type of raw data is best suited to be stored in a relational database without additional processing?**

- A. Product catalog stock levels
- B. Product banner images
- C. Product demonstration videos
- D. Buyer support call recordings

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Product catalog stock levels

**Correct answer: A. Product catalog stock levels**

Relational databases hold structured data that fits neatly into rows and columns. Stock levels are numbers tied to product IDs, so they can be stored directly in a table. The other options are unstructured media files.

**Why the others are wrong:**
- **B. Banner images**: Images are unstructured data; they belong in object storage such as Cloud Storage.
- **C. Demonstration videos**: Videos are unstructured and are stored as objects, not table rows.
- **D. Call recordings**: Audio is unstructured and would need processing (such as transcription) before it fits a table.

**Remember:** Rows and columns → relational database. Images, video, audio → Cloud Storage.

**References:**
- [cloud.google.com/sql/docs](https://cloud.google.com/sql/docs)
- [cloud.google.com/storage/docs/introduction](https://cloud.google.com/storage/docs/introduction)
- [cloud.google.com/architecture/storage-advisor](https://cloud.google.com/architecture/storage-advisor)

</details>

---

### Exam 4 · Q39

**FreshCartGo, a grocery delivery mobile app, wants to build a data pipeline that reads customer order events, transforms them, and writes the results to BigQuery. The team wants to avoid managing servers or manually resizing processing clusters when order volume increases during weekends. What is the main benefit of using a serverless data processing pipeline service such as Dataflow?**

- A. It gives the team complete control over the underlying compute resources.
- B. It removes the need to analyze the processed data.
- C. It manages and scales the pipeline infrastructure automatically.
- D. It guarantees that the processed data contains no errors.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. It manages and scales the pipeline infrastructure automatically.

**Correct answer: C. It manages and scales the pipeline infrastructure automatically.**

Dataflow is a serverless service for batch and streaming pipelines. Google provisions the workers and scales them up and down with the data volume. The team writes pipeline logic and doesn't resize clusters for weekend peaks.

**Why the others are wrong:**
- **A. Complete control of compute**: Serverless gives less control over the underlying machines, not more.
- **B. Removes need to analyze data**: Dataflow prepares data; analysis still happens, for example in BigQuery.
- **D. Guarantees no errors**: No service guarantees error-free data; data quality still needs checks.

**Remember:** Serverless pipeline (Dataflow) = no servers to manage, automatic scaling.

**References:**
- [cloud.google.com/products/dataflow](https://cloud.google.com/products/dataflow)
- [cloud.google.com/dataflow/docs/overview](https://cloud.google.com/dataflow/docs/overview)
- [cloud.google.com/dataflow/docs/horizontal-autoscaling](https://cloud.google.com/dataflow/docs/horizontal-autoscaling)

</details>

---

### Exam 4 · Q42

**TrendCart, an online clothing marketplace, builds a machine learning model to recommend fast-changing seasonal styles to shoppers. The model gives weak predictions because it was trained only on customer behavior and product catalog data from three years ago, even though fashion preferences change frequently. Which data quality dimension is most affected?**

- A. Uniqueness
- B. Validity
- C. Timeliness
- D. Consistency

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Timeliness

**Correct answer: C. Timeliness**

Timeliness means data is current enough for its purpose. Fashion trends change quickly, so three-year-old behavior data no longer reflects what shoppers want. The clues are "three years ago" and "change frequently".

**Why the others are wrong:**
- **A. Uniqueness**: Uniqueness is about duplicate records, which isn't the issue.
- **B. Validity**: Validity is about values following the right format or rules.
- **D. Consistency**: Consistency is about data agreeing across systems or records.

**Remember:** Stale data → timeliness. Duplicates → uniqueness. Wrong format → validity.

**References:**
- [cloud.google.com/learn/what-is-data-governance](https://cloud.google.com/learn/what-is-data-governance)
- [docs.cloud.google.com/dataplex/docs/auto-data-quality-overview](https://docs.cloud.google.com/dataplex/docs/auto-data-quality-overview)
- [ibm.com/think/topics/data-quality-dimensions](https://ibm.com/think/topics/data-quality-dimensions)

</details>

---

### Exam 4 · Q45

**LoopLily, a social journaling mobile app, needs a database to store user profiles, post metadata, comments, and app settings. The development team wants a flexible and scalable NoSQL database that works well for web and mobile applications. Which Google Cloud product or service should the team use?**

- A. Spanner
- B. Cloud Storage
- C. BigQuery
- D. Firestore

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Firestore

**Correct answer: D. Firestore**

Firestore is a serverless NoSQL document database built for web and mobile apps. It stores flexible documents such as profiles, posts and settings, and scales automatically. It also offers real-time sync and offline support for mobile clients.

**Why the others are wrong:**
- **A. Spanner**: Spanner is a globally distributed relational database, not a flexible NoSQL store for a simple app.
- **B. Cloud Storage**: Cloud Storage stores files, not app records you query.
- **C. BigQuery**: BigQuery is an analytics data warehouse, not an app database.

**Remember:** NoSQL for web and mobile apps → Firestore.

**References:**
- [cloud.google.com/firestore/native/docs/overview](https://cloud.google.com/firestore/native/docs/overview)
- [cloud.google.com/spanner/docs](https://cloud.google.com/spanner/docs)
- [cloud.google.com/storage/docs/introduction](https://cloud.google.com/storage/docs/introduction)

</details>

---

### Exam 4 · Q46

**FreshMart Loop is building a backend system for its grocery delivery website. The system must store daily order details, customer profiles, payment records, and purchase history. The information has a predictable structure, uses related tables, and needs to support cross-references between records. Which type of service should FreshMart Loop use?**

- A. Non-relational database
- B. Data warehouse
- C. Relational database
- D. Data lake

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Relational database

**Correct answer: C. Relational database**

Relational databases store structured data in related tables and use keys to link records. Orders, customers and payments with predictable structure and cross-references fit this model. It also supports reliable transactions for payment records.

**Why the others are wrong:**
- **A. Non-relational database**: NoSQL suits flexible or changing structures, not fixed related tables.
- **B. Data warehouse**: A warehouse is for large-scale analytics, not the day-to-day backend.
- **D. Data lake**: A data lake stores raw data in any format, not structured transactional records.

**Remember:** Predictable structure + related tables + transactions → relational database.

**References:**
- [docs.cloud.google.com/sql/docs/introduction](https://docs.cloud.google.com/sql/docs/introduction)
- [docs.cloud.google.com/bigquery/docs/introduction](https://docs.cloud.google.com/bigquery/docs/introduction)
- [cloud.google.com/learn/what-is-a-data-lake](https://cloud.google.com/learn/what-is-a-data-lake)

</details>

---

### Exam 5 · Q8

**FinSight Ledger, a financial analytics company, has moved several large customer transaction and reporting databases to Google Cloud. The company wants to get more business value from its data, manage data-related costs more effectively, and improve compliance with financial regulations. What should FinSight Ledger do?**

- A. Delete data that has been stored for more than 18 months.
- B. Move relational data into modern NoSQL databases.
- C. Generate quarterly reports about data access and usage.
- D. Establish an effective data governance program.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Establish an effective data governance program.

**Correct answer: D. Establish an effective data governance program.**

Data governance sets the rules for how data is owned, classified, accessed, kept and deleted. That one program covers all three goals: more value (trusted, findable data), cost control (lifecycle and retention rules) and compliance (access policies and auditing). The clue is the mix of value, cost and regulations.

**Why the others are wrong:**
- **A. Delete data older than 18 months**: a blanket rule may break financial retention laws and destroy useful data.
- **B. Move to NoSQL**: changing the database type doesn't address value, cost or compliance.
- **C. Quarterly access reports**: reporting is one small piece of governance, not the whole answer.

**Remember:** Value + cost + compliance for data = data governance.

**References:**
- [cloud.google.com/learn/what-is-data-governance](https://cloud.google.com/learn/what-is-data-governance)
- [docs.cloud.google.com/bigquery/docs/data-governance](https://docs.cloud.google.com/bigquery/docs/data-governance)
- [cloud.google.com/compliance](https://cloud.google.com/compliance)

</details>

---

### Exam 5 · Q9

**ParkNest, a mobile parking app, stores driver profiles, payment records, parking sensor events, and customer support logs in separate systems. The company wants to move to a unified cloud data solution on Google Cloud. What is the main benefit of this approach?**

- A. Data will always be cheaper to store.
- B. Data can be automatically protected from all external threats.
- C. Data will always be backed up and cannot be lost or deleted.
- D. Data can support innovation because it is no longer isolated in silos.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Data can support innovation because it is no longer isolated in silos.

**Correct answer: D. Data can support innovation because it is no longer isolated in silos.**

When data sits in separate systems, teams can't combine it to find insights. A unified data platform brings profiles, payments, sensor events and support logs together, so the company can analyze across them and build new features. The clue is "separate systems" moving to a "unified" solution.

**Why the others are wrong:**
- **A. Always cheaper**: cost depends on usage and design; "always" is an overclaim.
- **B. Protected from all threats**: no platform guarantees protection from every threat.
- **C. Cannot be lost or deleted**: backups help, but data can still be deleted or lost through mistakes.

**Remember:** Breaking down data silos = new insights and innovation. Watch for "always" and "all" as red flags.

**References:**
- [cloud.google.com/data-cloud](https://cloud.google.com/data-cloud)
- [cloud.google.com/solutions/data-analytics-and-ai](https://cloud.google.com/solutions/data-analytics-and-ai)
- [cloud.google.com/bigquery](https://cloud.google.com/bigquery)

</details>

---

### Exam 5 · Q14

**ShopSprint has migrated customer orders, payment records, and stock-level details to a cloud-based relational database. What capability does a relational database provide?**

- A. It keeps massive volumes of raw data in the same format in which it was collected
- B. It stores transactional data that applications can access electronically
- C. It performs fast analysis of very large and multi-dimensional datasets
- D. It processes unstructured data and makes it available across several geographic locations

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. It stores transactional data that applications can access electronically

**Correct answer: B. It stores transactional data that applications can access electronically**

A relational database stores structured data in tables with defined relationships. It is built for transactions such as orders, payments and stock updates, which applications read and write constantly. The clue is the list of operational records: orders, payments, stock levels.

**Why the others are wrong:**
- **A. Keeps raw data in its original format**: that describes a data lake.
- **C. Fast analysis of huge datasets**: that describes a data warehouse such as BigQuery.
- **D. Processes unstructured data across locations**: relational databases are for structured data; this fits object storage better.

**Remember:** Database = transactions. Data warehouse = analysis. Data lake = raw data.

**References:**
- [cloud.google.com/products/databases](https://cloud.google.com/products/databases)
- [cloud.google.com/sql/docs/introduction](https://cloud.google.com/sql/docs/introduction)
- [cloud.google.com/learn/what-are-transactional-databases](https://cloud.google.com/learn/what-are-transactional-databases)

</details>

---

### Exam 5 · Q22

**FitPulse, a new wellness mobile app, collects a massive volume of user data such as workout duration, step patterns, heart-rate activity, and estimated calories burned. The company wants to keep this data for future exploration and analytics, even before deciding exactly how it will be processed. Which data management solution should FitPulse use?**

- A. Data lake
- B. Data warehouse
- C. Data field
- D. Database

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Data lake

**Correct answer: A. Data lake**

A data lake stores large volumes of raw data in its original format, structured or not, at low cost. You decide later how to process and analyze it. The clue is "keep this data... even before deciding exactly how it will be processed".

**Why the others are wrong:**
- **B. Data warehouse**: it stores cleaned, structured data in a defined schema for analysis, so you must decide the structure first.
- **C. Data field**: a single attribute in a record, not a storage solution.
- **D. Database**: built for day-to-day transactions, not for storing huge raw datasets for later exploration.

**Remember:** Raw now, decide later = data lake. Structured, ready for analysis = data warehouse.

**References:**
- [cloud.google.com/discover/what-is-a-data-lake](https://cloud.google.com/discover/what-is-a-data-lake)
- [cloud.google.com/learn/what-is-a-data-warehouse](https://cloud.google.com/learn/what-is-a-data-warehouse)
- [cloud.google.com/bigquery/docs/introduction](https://cloud.google.com/bigquery/docs/introduction)

</details>

---

### Exam 5 · Q37

**BlueWave Analytics, a multinational reporting platform, uses Google Cloud along with other cloud providers to manage data across different environments. The company wants its data platforms to work together smoothly, exchange data easily, and avoid vendor lock-in or restrictive technology boundaries. Which Google Cloud differentiator best supports this requirement?**

- A. AI Hypercomputer
- B. Deep commitment to openness and interoperability
- C. Shift from OpEx to CapEx
- D. Bare Metal Solution

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Deep commitment to openness and interoperability

**Correct answer: B. Deep commitment to openness and interoperability**

Google Cloud supports open source, open standards and multicloud tools so data platforms can work across providers and data can move easily. That reduces vendor lock-in. The clues are "other cloud providers", "exchange data easily" and "avoid vendor lock-in".

**Why the others are wrong:**
- **A. AI Hypercomputer**: it is AI training and serving infrastructure, not about cross-cloud data exchange.
- **C. Shift from OpEx to CapEx**: cloud moves spending toward OpEx, and this isn't about interoperability.
- **D. Bare Metal Solution**: dedicated servers for special workloads, unrelated to openness.

**Remember:** Avoid lock-in, work across clouds = openness and interoperability.

**References:**
- [cloud.google.com/data-cloud](https://cloud.google.com/data-cloud)
- [cloud.google.com/security/compliance/swipo-codes](https://cloud.google.com/security/compliance/swipo-codes)
- [docs.cloud.google.com/bare-metal/docs/bms-overview](https://docs.cloud.google.com/bare-metal/docs/bms-overview)

</details>

---

### Exam 5 · Q48

**TrendNest, a retail analytics mobile app, wants to bring together its own customer activity data, partner campaign data, and external market data into one unified cloud environment. The goal is to prepare that combined data so data scientists can efficiently build and train new machine learning models. Which Google Cloud differentiator addresses this requirement?**

- A. AI-ready data cloud
- B. Global edge network
- C. Infrastructure as a Service (IaaS)
- D. Two-step verification (2SV)

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. AI-ready data cloud

**Correct answer: A. AI-ready data cloud**

Google Cloud's data platform brings internal, partner and external data together in one place and prepares it for AI. Data scientists can then build and train models on unified, well-managed data. The clues are "bring together... into one unified cloud environment" and "train new machine learning models".

**Why the others are wrong:**
- **B. Global edge network**: it delivers content fast to users, not data preparation for ML.
- **C. IaaS**: it is a service model for raw compute and storage, not a data differentiator.
- **D. 2SV**: it is a sign-in security feature.

**Remember:** Unified data prepared for ML = AI-ready data cloud.

**References:**
- [cloud.google.com/bigquery](https://cloud.google.com/bigquery)
- [cloud.google.com/learn/what-is-iaas](https://cloud.google.com/learn/what-is-iaas)
- [cloud.google.com/identity-platform/docs/web/mfa](https://cloud.google.com/identity-platform/docs/web/mfa)

</details>

---

### Exam 5 · Q49

**NovaStyle Apparel, a fashion e-commerce company, wants to use advanced generative AI to improve product recommendations, summarize customer feedback, and automate merchandising insights. However, its sales, inventory, customer, and marketing data is fragmented across many systems and stored in different formats. What foundational step should the company take to successfully support this AI transformation?**

- A. Build an AI-ready data platform
- B. Deploy a multi-cloud network architecture
- C. Shift operational expenditures to capital expenditures
- D. Restrict all data access to on-premises environments

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Build an AI-ready data platform

**Correct answer: A. Build an AI-ready data platform**

Generative AI is only as good as the data it can use. When data is spread across systems in different formats, the first step is to unify, clean and govern it on a platform AI can draw from. The clue is "fragmented across many systems" and "foundational step".

**Why the others are wrong:**
- **B. Multi-cloud network architecture**: networking doesn't fix fragmented, inconsistent data.
- **C. Shift OpEx to CapEx**: a spending change, unrelated, and the opposite of the cloud trend.
- **D. Restrict data to on-premises**: this blocks the cloud AI services the company wants to use.

**Remember:** Good AI starts with unified, AI-ready data.

**References:**
- [cloud.google.com/data-cloud](https://cloud.google.com/data-cloud)
- [cloud.google.com/bigquery](https://cloud.google.com/bigquery)
- [docs.cloud.google.com/bigquery/docs/introduction](https://docs.cloud.google.com/bigquery/docs/introduction)

</details>

---

### Exam 6 · Q4

**FreshBasket Analytics, a grocery delivery website, currently processes sales transactions once every quarter to identify buying patterns and create business reports. The leadership team wants more accurate insights and wants managers to react to customer demand as it happens. What should FreshBasket Analytics do?**

- A. Change from a relational database to a NoSQL database.
- B. Filter the data so reports are generated faster.
- C. Switch from batch processing to stream processing.
- D. Process batch reports every two weeks instead of every quarter.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Switch from batch processing to stream processing.

**Correct answer: C. Switch from batch processing to stream processing.**

Batch processing analyzes data in large chunks on a schedule, here once a quarter, so insights are always out of date. Stream processing analyzes data continuously as it arrives, so managers can react to demand in near real time. The clue is "react to customer demand as it happens."

**Why the others are wrong:**
- **A. Change to NoSQL**: The database type does not decide how fast data is analyzed. The processing model does.
- **B. Filter the data**: Less data may make reports faster, but they are still quarterly and possibly less accurate.
- **D. Batch every two weeks**: This is an improvement, but it is still batch and still not "as it happens."

**Remember:** React as it happens → streaming. Periodic reports → batch.

**References:**
- [cloud.google.com/dataflow/docs/overview](https://cloud.google.com/dataflow/docs/overview)
- [cloud.google.com/dataflow/docs/concepts/streaming-pipelines](https://cloud.google.com/dataflow/docs/concepts/streaming-pipelines)
- [cloud.google.com/pubsub/docs/overview](https://cloud.google.com/pubsub/docs/overview)

</details>

---

### Exam 6 · Q7

**FitTrail, a fitness tracking mobile app, needs to store user workout logs, device readings, and profile preferences. The development team expects the structure of this data to change over time as new wearable devices and health metrics are added. What is a defining feature of a non-relational database?**

- A. Reporting across many separate data sources
- B. A schema that must be strictly enforced before data is stored
- C. A flexible data model
- D. Queries that join data from several tables

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. A flexible data model

**Correct answer: C. A flexible data model**

Non-relational (NoSQL) databases do not require a fixed schema. Records can have different fields, and new fields can be added without redesigning tables. That fits FitTrail, whose data structure "will change over time as new wearable devices and health metrics are added." Firestore and Bigtable are Google Cloud examples.

**Why the others are wrong:**
- **A. Reporting across many data sources**: That describes a data warehouse such as BigQuery, not a NoSQL feature.
- **B. Strictly enforced schema**: That is a trait of relational databases, the opposite of NoSQL.
- **D. Joins across several tables**: Joins between related tables are a classic relational database strength.

**Remember:** Changing structure → NoSQL, flexible model. Related tables and transactions → relational.

**References:**
- [cloud.google.com/discover/what-is-nosql](https://cloud.google.com/discover/what-is-nosql)
- [cloud.google.com/firestore](https://cloud.google.com/firestore)
- [docs.cloud.google.com/bigtable/docs](https://docs.cloud.google.com/bigtable/docs)

</details>

---

### Exam 6 · Q8

**ShopKart, an online marketplace, is organizing different types of business information before moving it into Google Cloud for analytics and storage. The team wants to identify which type of information is unstructured data. Which option is an example of unstructured data?**

- A. Monthly warehouse stock records
- B. Product star ratings
- C. Customer purchase orders
- D. Customer support call transcripts

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Customer support call transcripts

**Correct answer: D. Customer support call transcripts**

Unstructured data has no predefined format or fixed fields. Free text, audio, images, and video are typical examples. Call transcripts are free-form conversation text, so they are unstructured, even though they can be analyzed later with tools like the Natural Language API.

**Why the others are wrong:**
- **A. Monthly warehouse stock records**: These fit neatly into rows and columns (item, quantity, date), so they are structured.
- **B. Product star ratings**: A rating is a single numeric value in a fixed field, so it is structured.
- **C. Customer purchase orders**: Orders have defined fields like customer, item, price, and date, so they are structured.

**Remember:** Text, audio, video, transcripts → unstructured. Table fields → structured. JSON/XML → semi-structured.

**References:**
- [cloud.google.com/discover/what-is-unstructured-data](https://cloud.google.com/discover/what-is-unstructured-data)
- [cloud.google.com/discover/what-is-structured-data](https://cloud.google.com/discover/what-is-structured-data)
- [cloud.google.com/natural-language/docs](https://cloud.google.com/natural-language/docs)

</details>

---

### Exam 6 · Q16

**MealPilot Analytics is preparing a training dataset for a food delivery recommendation model. The team wants to make sure that each customer’s stored order total correctly matches the amount shown on the original payment invoice. Which data quality dimension does this represent?**

- A. Completeness
- B. Accuracy
- C. Timeliness
- D. Uniqueness

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Accuracy

**Correct answer: B. Accuracy**

Accuracy measures whether data correctly reflects the real-world value or its trusted source. Checking that the stored order total matches the original payment invoice is a direct accuracy check. The clue is "correctly matches the amount shown on the original."

**Why the others are wrong:**
- **A. Completeness**: This is about missing values, not whether existing values are correct.
- **C. Timeliness**: This is about whether data is up to date and available when needed.
- **D. Uniqueness**: This is about duplicate records.

**Remember:** Missing → completeness. Matches source → accuracy. Right format → validity. Duplicates → uniqueness. Stale → timeliness.

**References:**
- [cloud.google.com/learn/what-is-data-governance](https://cloud.google.com/learn/what-is-data-governance)
- [docs.cloud.google.com/dataplex/docs/auto-data-quality-overview](https://docs.cloud.google.com/dataplex/docs/auto-data-quality-overview)
- [ibm.com/think/topics/data-quality-dimensions](https://ibm.com/think/topics/data-quality-dimensions)

</details>

---

### Exam 6 · Q20

**FreshCart Metrics, an online grocery delivery company, wants to analyze sales, inventory, customer behavior, and delivery performance data in a data warehouse. Business analysts need to run flexible queries, create custom reports, and perform ad-hoc analysis across structured and semi-structured datasets. How should FreshCart Metrics proceed?**

- A. Import data into a semi-structured time-series database.
- B. Choose a system to store structured and semi-structured data that supports ad-hoc analysis and custom reporting.
- C. Copy unstructured data into a single large object store.
- D. Ensure data is stored in structured tables and rows to support transactional queries and relationships.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Choose a system to store structured and semi-structured data that supports ad-hoc analysis and custom reporting.

**Correct answer: B. Choose a system to store structured and semi-structured data that supports ad-hoc analysis and custom reporting.**

A data warehouse, such as BigQuery, is built for analytics. It stores structured and semi-structured data and lets analysts run flexible, ad-hoc queries and build reports. The stem's clues are "data warehouse," "flexible queries," "custom reports," and "structured and semi-structured datasets." Option B restates those needs.

**Why the others are wrong:**
- **A. Semi-structured time-series database**: This is specialized for time-stamped data, not broad business analysis.
- **C. Unstructured data in an object store**: Raw object storage does not by itself support easy ad-hoc SQL reporting.
- **D. Structured tables for transactional queries**: That describes a transactional (OLTP) relational database, not an analytics warehouse, and it ignores semi-structured data.

**Remember:** Analyst reporting and ad-hoc queries → data warehouse. Day-to-day transactions → relational database.

**References:**
- [cloud.google.com/learn/what-is-a-data-warehouse](https://cloud.google.com/learn/what-is-a-data-warehouse)
- [docs.cloud.google.com/bigquery/docs/introduction](https://docs.cloud.google.com/bigquery/docs/introduction)
- [docs.cloud.google.com/bigquery/docs/query-overview](https://docs.cloud.google.com/bigquery/docs/query-overview)

</details>

---

### Exam 6 · Q28

**ShopSphere, an online retail platform, is auditing its customer profile table before loading it into an analytics system. The team finds that many customer email values look like “ravi.example.com” or “support-shop.com” because they do not contain the “@” character and fail the expected email pattern. Which data quality dimension is most directly affected?**

- A. Timeliness
- B. Completeness
- C. Validity
- D. Uniqueness

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Validity

**Correct answer: C. Validity**

Validity checks whether data follows the expected format, type, or rules. An email address without an "@" character fails the email format rule, so it is invalid. The clue is "fail the expected email pattern."

**Why the others are wrong:**
- **A. Timeliness**: This is about whether data is current. The values are wrong in format, not out of date.
- **B. Completeness**: The email fields are filled in, so nothing is missing.
- **D. Uniqueness**: This is about duplicate records, which the stem does not mention.

**Remember:** Wrong format or broken rule → validity. Doesn't match the real value → accuracy.

**References:**
- [docs.cloud.google.com/dataplex/docs/auto-data-quality-overview](https://docs.cloud.google.com/dataplex/docs/auto-data-quality-overview)
- [docs.cloud.google.com/dataplex/docs/use-auto-data-quality](https://docs.cloud.google.com/dataplex/docs/use-auto-data-quality)
- [cloud.google.com/learn/what-is-data-governance](https://cloud.google.com/learn/what-is-data-governance)

</details>

---

### Exam 6 · Q29

**FreshCartGo uses scooters to deliver groceries across several city zones. Its operations team finds that the same scooter is saved more than once in the fleet database with slightly different asset codes, so the maintenance prediction model counts the scooter’s travel distance multiple times. Which data quality dimension should be corrected?**

- A. Timeliness
- B. Validity
- C. Uniqueness
- D. Explainability

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Uniqueness

**Correct answer: C. Uniqueness**

Uniqueness means each real-world thing is recorded only once. The same scooter saved several times with slightly different asset codes is a duplicate, which makes the model count its travel distance more than once. The clue is "saved more than once."

**Why the others are wrong:**
- **A. Timeliness**: This is about data being current, not duplicated.
- **B. Validity**: The asset codes may each be in a valid format. The problem is that they refer to the same scooter.
- **D. Explainability**: This is about understanding how an ML model reaches its outputs. It is not a data quality dimension.

**Remember:** Duplicates → uniqueness.

**References:**
- [cloud.google.com/learn/what-is-data-governance](https://cloud.google.com/learn/what-is-data-governance)
- [docs.cloud.google.com/dataplex/docs/auto-data-quality-overview](https://docs.cloud.google.com/dataplex/docs/auto-data-quality-overview)
- [ibm.com/think/topics/data-quality-dimensions](https://ibm.com/think/topics/data-quality-dimensions)

</details>

---

### Exam 6 · Q39

**SwiftStay, a regional travel booking app, stores room availability and customer reservation records for thousands of hotels. During holiday seasons, the app must handle sudden spikes in bookings while keeping reservation transactions accurate. How does storing this reservation data in the cloud benefit the company?**

- A. It provides on-premises hardware access to transaction data
- B. It performs real-time data transformation at scale inside an on-premises database
- C. It supports accurate business transactions at scale
- D. It provides physical server access during peak booking demand

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. It supports accurate business transactions at scale

**Correct answer: C. It supports accurate business transactions at scale**

Cloud databases built for transactions, such as Cloud SQL and Spanner, keep each reservation consistent and correct while scaling to handle many more users. This lets SwiftStay absorb holiday spikes without double-bookings or lost records. The clues are "sudden spikes in bookings" and "keeping reservation transactions accurate."

**Why the others are wrong:**
- **A. On-premises hardware access**: Moving data to the cloud removes the need to manage on-premises hardware.
- **B. Real-time transformation inside an on-premises database**: This contradicts the move to the cloud and is about transformation, not transactions.
- **D. Physical server access during peaks**: Cloud customers do not get physical server access. The provider manages the hardware.

**Remember:** Transactional data in the cloud → accurate transactions at scale.

**References:**
- [cloud.google.com/learn/advantages-of-cloud-computing](https://cloud.google.com/learn/advantages-of-cloud-computing)
- [cloud.google.com/discover/what-is-cloud-scalability](https://cloud.google.com/discover/what-is-cloud-scalability)
- [docs.cloud.google.com/architecture/scalable-and-resilient-apps](https://docs.cloud.google.com/architecture/scalable-and-resilient-apps)

</details>

---

### Exam 6 · Q40

**BrightCare Hospital stores many kinds of patient information in its clinical system. Some of the information is stored in fixed fields that can be easily searched, filtered, and analyzed in tables. Which item is an example of structured data that BrightCare Hospital stores in its system?**

- A. CT scan images
- B. Operation room video recordings
- C. Patient blood pressure history
- D. Doctor’s handwritten notes

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Patient blood pressure history

**Correct answer: C. Patient blood pressure history**

Structured data fits into fixed fields, like rows and columns, so it is easy to search, filter, and analyze. Blood pressure readings are numbers with dates and patient IDs, which fit neatly into a table. The clue is "stored in fixed fields that can be easily searched, filtered, and analyzed in tables."

**Why the others are wrong:**
- **A. CT scan images**: Images have no fixed fields, so they are unstructured.
- **B. Operating room video recordings**: Video is unstructured data.
- **D. Doctor's handwritten notes**: Free-form handwriting is unstructured until it is processed and extracted.

**Remember:** Table fields and numeric readings → structured. Images, video, free text → unstructured.

**References:**
- [cloud.google.com/learn/what-is-a-relational-database](https://cloud.google.com/learn/what-is-a-relational-database)
- [cloud.google.com/discover/data-lake-vs-data-warehouse](https://cloud.google.com/discover/data-lake-vs-data-warehouse)
- [cloud.google.com/learn/what-is-data-cloud](https://cloud.google.com/learn/what-is-data-cloud)

</details>

---

### Exam 6 · Q46

**BrightCart, an online grocery app, collects customer orders, delivery logs, product reviews, and support messages from several systems. The company wants to process this cloud-based data and make it easy for analysts to query it for reporting, dashboards, and business insights. Which cloud data storage system should BrightCart use?**

- A. Relational database
- B. Private data center
- C. Data field
- D. Data warehouse

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Data warehouse

**Correct answer: D. Data warehouse**

A data warehouse, such as BigQuery, gathers data from many systems into one place, organized for analysis. Analysts can query it for reports, dashboards, and business insights. The clues are "from several systems" and "easy for analysts to query it for reporting, dashboards, and business insights."

**Why the others are wrong:**
- **A. Relational database**: It is designed for day-to-day transactions in one application, not large-scale analytics across many sources.
- **B. Private data center**: This is a location for infrastructure, not a data storage system, and the data is already cloud-based.
- **C. Data field**: A field is a single column or attribute in a record, not a storage system.

**Remember:** Raw data in its original format → data lake. Analyst reporting and dashboards → data warehouse.

**References:**
- [cloud.google.com/learn/what-is-a-data-warehouse](https://cloud.google.com/learn/what-is-a-data-warehouse)
- [docs.cloud.google.com/bigquery/docs/introduction](https://docs.cloud.google.com/bigquery/docs/introduction)
- [docs.cloud.google.com/bigquery/docs/loading-data](https://docs.cloud.google.com/bigquery/docs/loading-data)

</details>

---
