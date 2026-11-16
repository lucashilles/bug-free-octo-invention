# Domain 2 Study Guide — Exploring Data Transformation with Google Cloud

> Condensed from the 64-question bank in [`02-data-transformation.md`](02-data-transformation.md). Citations look like (Exam N · QM). The reasoning draws on the exam-prep author's per-option explanations, checked against current Google Cloud docs where they disagree. Many scenarios repeat across exams (Autoclass, serverless Spark, AlloyDB, data lake vs warehouse, data quality dimensions), so look for paired citations. Items marked "see ⚠️" have a shaky key or wording, discussed at the end.

---

## 1. Why data matters: the data value chain and cloud data benefits

### Key facts
- **The data value chain (also called the data supply chain)** is the full journey of data: **collection/ingestion → processing → storage → analysis/use** (reporting, analytics, AI). When a question asks for "the end-to-end journey from creation to business decisions" or "how data is collected, transformed and used", the answer is **data supply chain** (Exam 1 · Q35), (Exam 3 · Q33).
- **Processing** is the step that turns raw data into a **clean, structured, usable format**: cleaning, transforming, aggregating, filtering and validating. Collection gathers it, storage keeps it, analysis finds trends in it (Exam 1 · Q1).
- **Collection** is best when it is **automatic and real time**. Wearable **IoT devices** that upload readings continuously beat manual entry, nightly uploads or clinic visits (Exam 2 · Q21).
- **Digitizing a process** creates a record of every event. Moving from cash to a cloud-connected payment system lets a company **view data history and see each transaction**, which is how it finds mismatches (Exam 1 · Q3, see ⚠️).
- **Breaking down silos** is the main benefit of a unified cloud data platform. Data that sits in one place can be combined and used for innovation. It does not make data automatically cheaper, threat-proof or impossible to lose (Exam 5 · Q9).
- **Transactional data in the cloud** supports **accurate business transactions at scale**, including sudden spikes such as holiday bookings, without anyone touching physical servers (Exam 6 · Q39).

### Value chain steps

| Step | What happens | Exam phrasing |
|---|---|---|
| Collection / ingestion | Data is captured from apps, devices, partners | "IoT devices upload in real time" (Exam 2 · Q21) |
| Processing | Raw data is cleaned, standardized, structured | "converting raw information into a cleaner, structured format" (Exam 1 · Q1) |
| Storage | Data is kept in a database, lake or warehouse | see lessons 5–7 |
| Analysis / use | Reports, dashboards, ML models, AI | "managers discover business trends" |

### Decision rules
- "End-to-end lifecycle of data, creation to decisions" → **data supply chain** (Exam 1 · Q35), (Exam 3 · Q33).
- "Making raw data clean and structured" → **processing** (Exam 1 · Q1).
- "Collect automatically, no manual entry" → **IoT, real-time upload** (Exam 2 · Q21).
- "Benefit of a unified data solution" → **data is no longer in silos, so it can drive innovation** (Exam 5 · Q9).

### Traps
- Absolute promises ("always cheaper", "cannot be lost", "protected from all threats") are always wrong (Exam 5 · Q9).
- Distractors from other domains (error budget, perimeter security, resource hierarchy, IaaS, multicloud networking) show up as filler. They don't describe data flow (Exam 1 · Q3), (Exam 1 · Q35), (Exam 3 · Q33).
- Options that mention on-premises hardware or physical server access are never the cloud benefit (Exam 6 · Q39).
- Unifying data does not remove the customer's security work. Security is shared responsibility: you still configure access, governance and backups (Exam 5 · Q9).

---

## 2. AI-ready data, governance and openness

### Key facts
- **AI-ready data** is data that is **unified, clean, trusted, governed and discoverable**, so it can feed AI and ML reliably. Fragmented, inconsistent, duplicated, poorly governed data is the opposite (Exam 1 · Q34), (Exam 3 · Q38).
- Building that state is described as an **AI-ready data foundation** or **AI-ready data platform**. It is the foundational step before generative AI or AI agents (Exam 3 · Q38), (Exam 5 · Q49).
- **AI-ready data cloud** is how the exam names the Google Cloud differentiator for combining first-party, partner and external data in one place so data scientists can train models (Exam 5 · Q48).
- **Data governance** is a program of policies, roles and controls for data quality, access, lifecycle and compliance. It is the answer when a company wants **more value, controlled costs and regulatory compliance** together (Exam 5 · Q8).
  - What it covers: ownership, classification, access control, retention rules, quality standards, lineage, auditing and privacy. Value comes from trusted, findable data. Cost control comes from finding unused or badly stored data. Compliance comes from retention, access and audit rules (Exam 5 · Q8).
- **Openness and interoperability** is a Google Cloud differentiator: open standards, open source and multicloud tools (BigQuery Omni, Looker, AlloyDB Omni) so data platforms work together and you avoid **vendor lock-in** (Exam 5 · Q37).

### Decision rules
- Data is fragmented, inconsistent or ungoverned, and the goal is AI → **AI-ready data / data foundation / data platform** (Exam 1 · Q34), (Exam 3 · Q38), (Exam 5 · Q49).
- "Combine own, partner and market data to train models" → **AI-ready data cloud** (Exam 5 · Q48).
- Value + cost + compliance in one sentence → **data governance program** (Exam 5 · Q8).
- "Work across clouds, avoid lock-in" → **openness and interoperability** (Exam 5 · Q37).

### Traps
- One-off actions (delete old data, quarterly access reports, move everything to NoSQL) are narrower than a governance program. A blanket "delete after 18 months" rule can even break financial retention laws, and reports only show what already happened (Exam 5 · Q8).
- "Shift OpEx to CapEx" is backwards. Cloud moves spend **from CapEx to OpEx**, so that option is always wrong (Exam 5 · Q37), (Exam 5 · Q49).
- Coldline, ephemeral or on-premises data are not quality states (Exam 1 · Q34). Restricting data to on-premises works against AI readiness (Exam 5 · Q49).
- Other differentiators are filler in data questions: **AI Hypercomputer** (GPU/TPU infrastructure for AI), **Bare Metal Solution** (dedicated physical servers), the **global edge network** (fast delivery to users) and **2-Step Verification** (sign-in security) (Exam 5 · Q37), (Exam 5 · Q48).
- **Knowledge Catalog** (formerly Dataplex Universal Catalog, renamed in April 2026) is Google Cloud's data catalog for governance: discovery, metadata, lineage, data quality checks and business glossaries across lakes and warehouses. It describes data; it doesn't store files (Exam 2 · Q12).

---

## 3. Types of data: structure and source

### Key facts
- **Structured data** fits fixed fields, rows and columns. It is easy to search, filter and analyze in tables. Examples: blood pressure history, stock levels, orders, revenue, GPS coordinates, star ratings (Exam 6 · Q40), (Exam 4 · Q30).
- **Semi-structured data** has no fixed relational schema but carries **tags, keys, nested fields or hierarchy** that give it organization. Examples: **JSON, XML**, HTML (Exam 1 · Q19).
- **Unstructured data** has no predefined model. Examples: **free-text feedback, call transcripts, audio, video, images, scans, handwritten notes** (Exam 1 · Q22), (Exam 3 · Q6), (Exam 6 · Q8).
- Only structured raw data goes into a **relational database without extra processing**. Images, videos and call recordings do not (Exam 4 · Q30).
- **Metadata about a media file is structured; the content is not.** The usual design keeps the file in Cloud Storage and its metadata (product ID, duration, file path) in a database (Exam 3 · Q6), (Exam 4 · Q30).
- Unstructured data still has value. Natural language processing, sentiment analysis, OCR and image analysis turn text, handwriting and images into usable insight. A transcribed call can become structured fields (Exam 1 · Q22), (Exam 6 · Q40), (Exam 4 · Q30).
- **First-party data**: collected **directly** by the company from its own customers (website clicks, orders, loyalty forms) (Exam 1 · Q38).
- **Second-party data**: another company's first-party data, **shared directly** with you by a partner (Exam 3 · Q5).
- **Third-party data**: bought from an **outside aggregator** that has no direct relationship with your customers (Exam 1 · Q39).

### Structure

| Type | Shape | Examples in the bank | Source |
|---|---|---|---|
| Structured | Rows and columns, fixed schema | Blood pressure history, stock levels | (Exam 6 · Q40), (Exam 4 · Q30) |
| Semi-structured | Tags, keys, nesting | JSON and XML logs and config | (Exam 1 · Q19) |
| Unstructured | No schema | Written feedback, call transcripts, audio, video | (Exam 1 · Q22), (Exam 3 · Q6), (Exam 6 · Q8) |

### Source

| Type | Who collected it | Example | Source |
|---|---|---|---|
| First-party | You, from your customers | Clicks, orders, loyalty sign-ups | (Exam 1 · Q38) |
| Second-party | A partner, shared directly | Senior-living network shares resident data | (Exam 3 · Q5) |
| Third-party | An aggregator with no link to your customers | Purchased audience segments | (Exam 1 · Q39) |

### Decision rules
- Free text, speech, images or video → **unstructured**, even if the text is a "transcript" (Exam 6 · Q8).
- JSON / XML / "tags and attributes" → **semi-structured** (Exam 1 · Q19).
- A number or field you could put in a table column → **structured** (Exam 6 · Q40).
- "Directly from our own customers" → first-party. "Partner shares its data with us" → second-party. "Bought from a provider" → third-party (Exam 1 · Q38), (Exam 3 · Q5), (Exam 1 · Q39).

### Traps
- In an "unstructured" question, numeric options like revenue trends, stock counts, GPS coordinates or star ratings are all structured (Exam 1 · Q22), (Exam 6 · Q8).
- Audio and video stored **next to** HTML and JSON are still unstructured. The JSON is the semi-structured part (Exam 3 · Q6).
- "Relational data" and "open standard data" or "public domain data" are not categories the exam uses for these questions (Exam 1 · Q19), (Exam 1 · Q38), (Exam 3 · Q5).
- Purchase orders stored as JSON are still predictable records (structured or semi-structured), never the "unstructured" answer (Exam 6 · Q8).
- Structure and source are separate axes. "Unstructured data" is never the answer to a first/second/third-party question (Exam 1 · Q39).

---

## 4. Data quality dimensions

### Key facts
- Poor data quality leads to weak ML models and bad reports. The exam describes a symptom and asks which **dimension** is broken.
- **Completeness**: required fields or attributes are **missing** (no date of birth, no age group or location) (Exam 3 · Q16), (Exam 3 · Q46).
- **Accuracy**: the stored value **matches the real-world truth** (order total equals the invoice) (Exam 6 · Q16).
- **Validity**: the value **follows the expected format, rule, range or list of allowed values** (an email must contain "@"; an age of 250 or a negative price is invalid) (Exam 6 · Q28), (Exam 3 · Q46), (Exam 4 · Q42).
- **Uniqueness**: each real thing is recorded **once**. Duplicates such as one scooter under two asset codes break it (Exam 6 · Q29).
- **Timeliness** (also called **freshness**): data is **current enough** and available when needed. A fashion model trained on three-year-old data fails (Exam 4 · Q42).
- **Consistency**: the same fact agrees across systems (one system says a jacket is in stock, another says discontinued). It appears only as a distractor in the bank (Exam 4 · Q42).
- For ML, quality gaps hurt the model directly: missing fields weaken or bias it, duplicates make it over-count, wrong values teach it false patterns (Exam 3 · Q46), (Exam 6 · Q29), (Exam 6 · Q16).

### Symptom → dimension

| Symptom | Dimension | Source |
|---|---|---|
| Missing attributes or empty required fields | Completeness | (Exam 3 · Q16), (Exam 3 · Q46) |
| Value differs from the source of truth | Accuracy | (Exam 6 · Q16) |
| Value breaks a format rule | Validity | (Exam 6 · Q28) |
| Same entity stored more than once | Uniqueness | (Exam 6 · Q29) |
| Data is old for a fast-changing domain | Timeliness | (Exam 4 · Q42) |
| Two systems disagree on the same fact | Consistency | (Exam 4 · Q42) |

### Decision rules
- Ask "what is wrong with the value?" Missing → completeness. Wrong → accuracy. Wrong shape → validity. Doubled → uniqueness. Stale → timeliness.

### Traps
- Validity vs accuracy: an email without "@" is **invalid** regardless of whether it belongs to the person. A well-formed total that doesn't match the invoice is **inaccurate** (Exam 6 · Q28), (Exam 6 · Q16).
- "Explainability" is a responsible-AI idea, not a data quality dimension (Exam 6 · Q29).
- Duplicates can each look valid. Two well-formed asset codes for one scooter is a **uniqueness** problem, not validity (Exam 6 · Q29).
- Old data can be accurate, valid and unique and still fail **timeliness** (Exam 4 · Q42).

---

## 5. Databases, data lakes and data warehouses

### Key facts
- **Relational database**: predictable structure, **related tables**, cross-references (joins), strict schema. It stores **transactional data** that applications read and write (Exam 4 · Q46), (Exam 5 · Q14).
- **Non-relational (NoSQL) database**: defined by a **flexible data model**. Good when the structure will change, such as new device metrics (Exam 6 · Q7).
- **Data lake**: holds **large volumes of raw data in its original format** (structured, semi-structured, unstructured) **before you decide how to process it** (Exam 2 · Q33), (Exam 5 · Q22).
- **Data warehouse**: holds **processed** structured and semi-structured data for **analysis**: flexible queries, ad-hoc analysis, custom reports, dashboards (Exam 6 · Q46), (Exam 6 · Q20).
- A modern cloud warehouse like **BigQuery** can analyze structured and unstructured data at scale (Exam 2 · Q27).
- **OLTP vs OLAP.** Operational databases do **OLTP** (online transaction processing): many small reads and writes of single records. Warehouses do **OLAP** (online analytical processing): big scans and aggregations over historical data (Exam 1 · Q4), (Exam 3 · Q15), (Exam 3 · Q41).
- Lake and warehouse work together. Raw data lands in the lake (on Google Cloud, usually Cloud Storage). Once cleaned and modeled, it moves into the warehouse for reporting (Exam 2 · Q33), (Exam 5 · Q22).
- NoSQL comes in several models: **document** (Firestore), **key-value**, **wide-column** (Bigtable) and **graph**. They avoid multi-table joins and keep related data together for fast access (Exam 6 · Q7).

### Comparison

| Store | Data state | Main use | Source |
|---|---|---|---|
| Relational database | Structured, schema first | Day-to-day transactions | (Exam 4 · Q46), (Exam 5 · Q14) |
| Non-relational database | Flexible schema | Changing app data at scale | (Exam 6 · Q7) |
| Data lake | Raw, any format | Keep everything now, decide later | (Exam 2 · Q33), (Exam 5 · Q22) |
| Data warehouse | Cleaned, modeled | Analytics, reporting, BI | (Exam 6 · Q46), (Exam 6 · Q20) |

### Decision rules
- "Keep in original format" or "before deciding how to process it" → **data lake** (Exam 2 · Q33), (Exam 5 · Q22).
- "Analysts query for reports, dashboards, ad-hoc analysis" → **data warehouse** (Exam 6 · Q46), (Exam 6 · Q20).
- "Related tables, cross-references, predictable structure" → **relational database** (Exam 4 · Q46).
- "Structure will change over time" → **non-relational, flexible model** (Exam 6 · Q7).

### Traps
- **"Data field"** is a made-up distractor. It is never a storage solution (Exam 2 · Q33), (Exam 5 · Q22), (Exam 6 · Q46).
- Strict schemas and multi-table joins describe **relational** databases, not NoSQL (Exam 6 · Q7).
- "Fast analysis of huge multi-dimensional data" describes a **warehouse**. "Raw data in the original format" describes a **lake**. Neither is what a relational database provides (Exam 5 · Q14).
- In an analytics question, "structured tables for transactional queries" is the database answer dressed up as the warehouse one (Exam 6 · Q20).
- A "time-series database" is too narrow for general business reporting (Exam 6 · Q20). "Copy everything into one object store" describes a lake, not a warehouse (Exam 6 · Q20).

---

## 6. Google Cloud databases: Cloud SQL, AlloyDB, Spanner, Firestore

### Key facts
- **Cloud SQL**: fully managed **MySQL, PostgreSQL and SQL Server**. The **cost-effective** relational choice for a **single region**, small and medium apps, no server management (Exam 3 · Q15), (Exam 4 · Q23).
  - Like any operational database, it **integrates with BI and analytics platforms** to produce insights. It doesn't build dashboards or run ML on its own (Exam 2 · Q30).
- Cloud SQL's managed operations: Google handles **backups, patching, replication and high availability** (Exam 4 · Q23), (Exam 2 · Q14).
- **AlloyDB for PostgreSQL**: fully managed, **PostgreSQL-compatible**, higher performance and availability than standard PostgreSQL. It includes a **columnar engine** that speeds up analytical queries (scans, joins, aggregates) on the same operational data. Running transactions and analytics on one database is called **HTAP** (hybrid transactional and analytical processing) (Exam 1 · Q4).
  - Pick it to **move an existing PostgreSQL app** that is slowing down, with **minimal code changes** (Exam 1 · Q13).
  - Pick it for high performance while **staying aligned with open-source PostgreSQL** to reduce lock-in (Exam 3 · Q39, see ⚠️).
- **AlloyDB Omni**: the downloadable, **self-managed** edition of AlloyDB that runs **anywhere**: your **own data center**, the edge or other clouds (Exam 2 · Q40), (Exam 2 · Q14).
- **Spanner** (Cloud Spanner): relational, strongly consistent (**ACID** transactions), **horizontally scalable** and able to **replicate across regions** in real time. It comes in regional, dual-region and multi-region configurations. Pick it for **global, multi-region transactional** apps (Exam 2 · Q25).
  - Spanner is now multi-model: besides relational tables it supports key-value, graph and search. It is still an operational database, not a file store (Exam 3 · Q4).
  - Spanner has a **PostgreSQL interface**, but that is not full PostgreSQL compatibility. Moving an existing PostgreSQL app to it usually needs schema, query or behavior changes (Exam 1 · Q13), (Exam 3 · Q39).
  - It is more powerful and **more expensive** than a single-region app needs (Exam 3 · Q15).
- **Firestore**: serverless **NoSQL document database** for **web and mobile apps** (profiles, posts, comments, settings). It adds **real-time sync, offline support** and Firebase integration. *Firestore in Datastore mode* is the same database for server-side apps (Exam 4 · Q45), (Exam 3 · Q39).
- **Bigtable** *(only a distractor in the bank)*: wide-column NoSQL for very large, low-latency, high-throughput workloads such as IoT time series, financial data and personalization. Not relational, no joins, not for media files (Exam 1 · Q13), (Exam 3 · Q4), (Exam 2 · Q23).
- Operational databases feed insight; they don't create it. Dashboards come from **Looker** or **Data Studio**, predictions from **BigQuery ML** or **Gemini Enterprise Agent Platform** (formerly Vertex AI) (Exam 2 · Q30).

### Picking a database

| Need | Pick | Source |
|---|---|---|
| Relational, one region, budget-friendly | Cloud SQL | (Exam 3 · Q15), (Exam 4 · Q23) |
| PostgreSQL-compatible, faster, analytics on live data | AlloyDB for PostgreSQL | (Exam 1 · Q4), (Exam 1 · Q13), (Exam 3 · Q39) |
| AlloyDB on-premises or in another cloud | AlloyDB Omni | (Exam 2 · Q40) |
| Global, multi-region, consistent transactions | Spanner | (Exam 2 · Q25) |
| Flexible NoSQL for web and mobile | Firestore | (Exam 4 · Q45) |
| Huge-scale wide-column NoSQL | Bigtable | *(not in the question bank)* |

### Decision rules
- "Only one region" + "cost-effective" + transactions → **Cloud SQL**, not Spanner (Exam 3 · Q15).
- "PostgreSQL" + "performance" or "columnar engine" → **AlloyDB**. Add "on-premises data center" → **AlloyDB Omni** (Exam 1 · Q4), (Exam 2 · Q40).
- "Several continents, consistent, highly available" → **Spanner** (Exam 2 · Q25).
- "NoSQL" + "mobile/web app" → **Firestore** (Exam 4 · Q45).

### Traps
- Spanner is not cold storage, not for unstructured ingestion and not a visualization tool (Exam 2 · Q25).
- BigQuery is for analytics, not an app's transactional database (Exam 3 · Q15), (Exam 4 · Q23).
- Bigtable and Firestore are NoSQL, so they are wrong when the question says PostgreSQL (Exam 1 · Q13), (Exam 3 · Q39).
- Cloud SQL doesn't "convert unstructured files into tables" or "build predictions directly" (Exam 2 · Q30). Parsing files into tables is the job of a processing or ETL service.
- Storing large images or videos inside a relational database is possible but costly and slow. Files go in Cloud Storage (Exam 3 · Q4), (Exam 4 · Q30).

---

## 7. Cloud Storage: classes, locations and Autoclass

### Key facts
- **Cloud Storage** is object storage for **unstructured files** at any scale: images, videos, audio, backups, exports (Exam 3 · Q4).
- **Storage classes** trade storage price for access cost. Standard (frequent) → **Nearline** (about once a month) → **Coldline** (about once a quarter) → **Archive** (less than once a year). Use them to cut the cost of rarely read files (Exam 2 · Q12).
- **Archive** is cheapest for data read **about once a year**, such as disaster-recovery exports (Exam 4 · Q13).
- Colder classes trade a lower storage price for **higher retrieval costs** and a **minimum storage duration**: Nearline 30 days, Coldline 90 days, Archive 365 days (Exam 4 · Q13).
- **Autoclass** moves each object between classes **automatically, based on its actual access**. Unused objects go colder; an object that is read again goes back to Standard. No rules to write, no access patterns to predict (Exam 1 · Q28), (Exam 1 · Q32).
- **Object Lifecycle Management** applies rules **you write** on conditions such as age, creation date, storage class or number of newer versions. Actions are change class or delete. Use it when you know the pattern (Exam 1 · Q28), (Exam 1 · Q32).
- A bucket's **location type** is your choice: **region**, **dual-region** or **multi-region**. Data placement follows that choice, never chance (Exam 3 · Q9).
- **Multi-region** (and dual-region) buckets keep **geo-redundant copies**, giving broad geographic access and higher availability (Exam 1 · Q6), (Exam 3 · Q9, see ⚠️).
- Encryption at rest is **on by default and free**. It is never a paid add-on. For more control you can use **customer-managed encryption keys (CMEK)** in Cloud KMS (Exam 3 · Q9), (Exam 1 · Q6).

### Storage classes

| Class | Typical access | Bank example | Source |
|---|---|---|---|
| Standard | Frequent, hot data | Latest files | (Exam 2 · Q12) |
| Nearline | About once a month | Less-used files | (Exam 2 · Q12) |
| Coldline | About once a quarter | Older files | (Exam 2 · Q12) |
| Archive | Less than once a year | DR exports read yearly | (Exam 4 · Q13) |

### Decision rules
- "Can't predict access" + "don't want rules" → **Autoclass** (Exam 1 · Q28), (Exam 1 · Q32).
- "Move after X days" → **Lifecycle rules** (Exam 1 · Q28).
- "Read once a year, minimize cost" → **Archive** (Exam 4 · Q13).
- "Users in many countries" + "high availability" → **multi-region bucket** (Exam 1 · Q6).
- Large volumes of media files → **Cloud Storage**, not a database (Exam 3 · Q4).

### Traps
- Storage Transfer Service moves data in; Cloud CDN caches content near users. Neither changes storage class (Exam 1 · Q28).
- Object Versioning keeps old copies for recovery and can **increase** storage use. Requester Pays makes the downloader pay access costs. Neither saves on cold data (Exam 1 · Q32), (Exam 1 · Q6).
- Object metadata (content type, cache settings, custom labels) describes objects. It doesn't decide where data lives or how available it is (Exam 1 · Q6).
- Filestore is file (NFS) storage, and Knowledge Catalog is a catalog, not where you store objects (Exam 2 · Q12).
- "Randomly places data" and "small minimum storage quantity" are invented benefits (Exam 3 · Q9).

---

## 8. BigQuery and Looker: analytics and business intelligence

### Key facts
- **BigQuery** is Google Cloud's **serverless data warehouse**: stores large datasets, runs fast SQL at **petabyte** scale, no servers to manage, with built-in ML and AI features (Exam 1 · Q48), (Exam 3 · Q41).
  - It **separates storage and compute** and scales automatically (Exam 3 · Q41).
  - **BigQuery ML** lets analysts build and run ML models with SQL inside BigQuery (Exam 1 · Q48), (Exam 2 · Q30).
  - A common pattern keeps raw files in Cloud Storage and analyzes them with BigQuery. Cloud Storage alone is not a query engine (Exam 3 · Q41).
- BigQuery can analyze **structured and unstructured** data at scale, such as AI assistant transcripts and call metadata (Exam 2 · Q27).
- **BigQuery Omni** runs BigQuery SQL on data that **stays in AWS or Azure** storage (Amazon S3, Azure Blob Storage), through **BigLake** tables, so you don't copy it into Google Cloud first. That avoids the cost and delay of moving data (Exam 2 · Q14).
- **Looker** is Google Cloud's enterprise **business intelligence** platform. It gives business users **self-service** access to trusted, modeled data to explore, build dashboards and reports. It also supports **embedded analytics** (dashboards inside your own apps) (Exam 1 · Q20), (Exam 2 · Q8).
- Looker's **governed semantic model** (LookML) defines each metric once, so every team sees the same numbers (Exam 1 · Q20), (Exam 2 · Q5).
- Looker is **multicloud**: it connects to many databases and warehouses (BigQuery, Snowflake, Redshift, MySQL, Oracle and more) on Google Cloud, AWS and Azure (Exam 2 · Q5).
- **Data Studio**: the free, lighter dashboarding tool, with a paid **Data Studio Pro** edition. It was called Looker Studio from 2022 until Google restored the Data Studio name in April 2026. Looker adds the governed semantic model for the whole enterprise (Exam 2 · Q30).

### Who does what

| Product | Role | Source |
|---|---|---|
| BigQuery | Store and query data with SQL at scale | (Exam 1 · Q48), (Exam 3 · Q41) |
| BigQuery Omni | Query data in other clouds in place | (Exam 2 · Q14) |
| Looker | BI: explore, model, visualize, share insights | (Exam 1 · Q20), (Exam 2 · Q5), (Exam 2 · Q8) |

### Decision rules
- "Serverless data warehouse", "petabytes", "SQL analysis" → **BigQuery** (Exam 1 · Q48), (Exam 3 · Q41).
- "Analyze data in another cloud without copying it" → **BigQuery Omni** (Exam 2 · Q14).
- "Business users explore data and build reports without engineers" → **Looker** (Exam 1 · Q20).
- "What's Looker's benefit?" → **advanced business intelligence and analytics** (Exam 2 · Q8).

### Traps
- BigQuery stores and queries. Looker visualizes and governs the business view. If the question is about **people exploring and reporting**, pick Looker over BigQuery (Exam 1 · Q20).
- "Leading serverless warehousing technology" describes BigQuery, not Looker (Exam 2 · Q8).
- AlloyDB Omni runs a database elsewhere. It doesn't query data across clouds (Exam 2 · Q14).
- Cloud SQL, Firestore and Cloud Storage don't do petabyte-scale analytics (Exam 3 · Q41).
- BigQuery doesn't encrypt network links or convert records into audio (Exam 2 · Q27).
- Looker has its own permissions, but access management for Google Cloud resources is **IAM**, and rollback or recovery belongs to databases and storage. Neither is Looker's benefit (Exam 2 · Q8).
- Compute Engine and Spot VMs are infrastructure. You could install BI software on them, but they are not a BI product (Exam 2 · Q5), (Exam 1 · Q48).

---

## 9. Processing data: batch vs streaming, Dataflow and serverless Spark

### Key facts
- **Batch processing** handles data in scheduled chunks (nightly, quarterly). **Streaming** processes records **continuously as they arrive**, giving near real-time insight (Exam 3 · Q26).
- To react to demand **as it happens**, switch **from batch to stream processing**. Running batches more often only shortens the delay (Exam 6 · Q4).
- **Dataflow** is a fully managed, **serverless** service for batch and streaming pipelines (built on Apache Beam). It reads, transforms and loads data, for example into BigQuery (Exam 2 · Q23).
- The main benefit of a serverless pipeline service is that it **manages and scales the infrastructure automatically** (Exam 4 · Q39).
- Batch still has its place: daily reports, monthly billing, historical summaries and **backfills** (reloading a past period) are batch jobs (Exam 3 · Q26).
- **Managed Service for Apache Spark** (formerly Dataproc) runs Spark and Hadoop. Its **serverless** option lets you **submit Spark jobs (batch workloads or interactive sessions) without creating, sizing or tuning clusters**. The **clusters** option is for teams that want control over cluster configuration (Exam 1 · Q44), (Exam 3 · Q34).
- **Pub/Sub**: the managed messaging service that ingests event streams and decouples systems. It moves messages but doesn't transform them (Exam 2 · Q23), (Exam 6 · Q4).
- The standard streaming pipeline is **Pub/Sub (ingest) → Dataflow (process) → BigQuery (analyze)** (Exam 3 · Q26), (Exam 6 · Q4).
- **Cloud Data Fusion**: a fully managed, **visual** (graphical, low-code) tool for building ETL and ELT pipelines between many sources and destinations (Exam 1 · Q44).
- **ETL** transforms data before loading it into the warehouse. **ELT** loads raw data first and transforms it inside the warehouse (Exam 1 · Q44), (Exam 2 · Q23).

### Processing options

| Need | Pick | Source |
|---|---|---|
| Continuous, real-time insight | Stream processing | (Exam 3 · Q26), (Exam 6 · Q4) |
| Managed, auto-scaling ETL into a warehouse | Dataflow | (Exam 2 · Q23), (Exam 4 · Q39) |
| Existing Spark code, no cluster work | Managed Service for Apache Spark serverless | (Exam 1 · Q44), (Exam 3 · Q34) |
| Spark with control over clusters | Managed Service for Apache Spark clusters | (Exam 1 · Q44) |
| Ingest event streams | Pub/Sub | (Exam 2 · Q23), (Exam 6 · Q4) |
| Visual, low-code ETL/ELT | Cloud Data Fusion | (Exam 1 · Q44) |

### Decision rules
- "As it happens" or "as events arrive" → **streaming** (Exam 3 · Q26), (Exam 6 · Q4).
- "Transform before loading into a warehouse" + "scale automatically" → **Dataflow** (Exam 2 · Q23).
- "Spark" + "don't want to manage clusters" → **Managed Service for Apache Spark serverless** (Exam 1 · Q44), (Exam 3 · Q34).

### Traps
- Serverless does **not** mean full control of compute, no need for analysis, or error-free data (Exam 4 · Q39).
- Pub/Sub moves messages. Bigtable and Cloud Storage store data. None of them is the transform pipeline (Exam 2 · Q23).
- The **clusters** option of the Spark service still needs cluster management. Cloud Data Fusion is a visual integration tool, not serverless Spark. Installing Spark on Compute Engine VMs is the most work of all (Exam 1 · Q44), (Exam 3 · Q34).
- BigQuery is serverless too, but it runs SQL, not existing Spark code (Exam 1 · Q44).
- Switching to NoSQL or filtering data doesn't make insights real time (Exam 6 · Q4).
- Moving data into Google Cloud uses **Storage Transfer Service** (online copies from Amazon S3, Azure Blob Storage, on-premises storage or other buckets) (Exam 1 · Q28). Transfer Appliance and Database Migration Service *(not in the question bank)* cover offline bulk transfer and database moves.

---

## ⚠️ Questionable answers

| Item | Issue |
|---|---|
| **(Exam 3 · Q9)** | "Stores geographically distributed copies" is only true for **multi-region and dual-region** buckets. A regional bucket keeps redundant copies across zones in one region. Pick it on the exam, but know the condition. |
| **(Exam 3 · Q39)** | AlloyDB is **PostgreSQL-compatible**, but AlloyDB itself is not open source. The "open-source engine" framing means compatibility with open-source PostgreSQL. Spanner also has a PostgreSQL interface, so the question leans on AlloyDB's closer compatibility. |
| **(Exam 1 · Q3)** | "View data history to see transactions" is vague wording for the real benefit: a digital record of every purchase that can be reconciled. The other options are clearly wrong, so the key stands. |
| **(Exam 1 · Q1)**, **(Exam 1 · Q35)** | The bank uses both "data value chain" and "data supply chain" for the same idea. Treat them as synonyms. |

---

## Last-minute cheat sheet

- End-to-end data journey → **data supply chain**. Raw → clean and structured → **processing** (Exam 1 · Q35), (Exam 3 · Q33), (Exam 1 · Q1).
- Automatic real-time collection → **IoT devices** (Exam 2 · Q21). Digital payments → **transaction history** (Exam 1 · Q3).
- Unified data → **no silos, enables innovation**. Cloud transactional data → **accurate transactions at scale** (Exam 5 · Q9), (Exam 6 · Q39).
- Unified, clean, governed data for AI → **AI-ready data / foundation / platform / data cloud** (Exam 1 · Q34), (Exam 3 · Q38), (Exam 5 · Q49), (Exam 5 · Q48).
- Value + cost + compliance → **data governance program**. Avoid lock-in → **openness and interoperability** (Exam 5 · Q8), (Exam 5 · Q37).
- JSON/XML → **semi-structured**. Text, audio, video, transcripts → **unstructured**. Table fields → **structured** (Exam 1 · Q19), (Exam 1 · Q22), (Exam 3 · Q6), (Exam 6 · Q8), (Exam 6 · Q40), (Exam 4 · Q30).
- Own customers → **first-party**. Partner shares → **second-party**. Bought → **third-party** (Exam 1 · Q38), (Exam 3 · Q5), (Exam 1 · Q39).
- Missing → **completeness**. Matches source → **accuracy**. Format → **validity**. Duplicates → **uniqueness**. Stale → **timeliness** (Exam 3 · Q16), (Exam 3 · Q46), (Exam 6 · Q16), (Exam 6 · Q28), (Exam 6 · Q29), (Exam 4 · Q42).
- Raw, original format → **data lake**. Analyst reporting → **data warehouse** (Exam 2 · Q33), (Exam 5 · Q22), (Exam 6 · Q46), (Exam 6 · Q20).
- Related tables, transactions → **relational**. Changing structure → **NoSQL, flexible model** (Exam 4 · Q46), (Exam 5 · Q14), (Exam 6 · Q7).
- One region, cheap relational → **Cloud SQL** (integrates with BI) (Exam 3 · Q15), (Exam 4 · Q23), (Exam 2 · Q30).
- PostgreSQL + performance + columnar engine → **AlloyDB**. On-prem → **AlloyDB Omni** (Exam 1 · Q4), (Exam 1 · Q13), (Exam 3 · Q39), (Exam 2 · Q40).
- Multi-region consistent transactions → **Spanner**. Mobile/web NoSQL → **Firestore** (Exam 2 · Q25), (Exam 4 · Q45).
- Media files → **Cloud Storage**. Rare access → **Nearline/Coldline/Archive**. Yearly → **Archive** (Exam 3 · Q4), (Exam 2 · Q12), (Exam 4 · Q13).
- Unpredictable access, no rules → **Autoclass**. Global users → **multi-region bucket** (Exam 1 · Q28), (Exam 1 · Q32), (Exam 1 · Q6), (Exam 3 · Q9).
- Serverless warehouse, petabytes, SQL → **BigQuery**. Data in other clouds → **BigQuery Omni** (Exam 1 · Q48), (Exam 3 · Q41), (Exam 2 · Q27), (Exam 2 · Q14).
- Self-service BI, multicloud → **Looker** (Exam 1 · Q20), (Exam 2 · Q5), (Exam 2 · Q8).
- Transactions → **OLTP database**. Large-scale analysis → **OLAP warehouse**. Both on one PostgreSQL database → **AlloyDB (HTAP)** (Exam 3 · Q15), (Exam 3 · Q41), (Exam 1 · Q4).
- Archive minimum storage 365 days; Coldline 90; Nearline 30 (Exam 4 · Q13).
- React as it happens → **streaming** (Exam 3 · Q26), (Exam 6 · Q4).
- Managed auto-scaling pipeline → **Dataflow**. Spark without clusters → **Managed Service for Apache Spark serverless** (Exam 2 · Q23), (Exam 4 · Q39), (Exam 1 · Q44), (Exam 3 · Q34).
- Ingest events → **Pub/Sub**. Visual ETL → **Cloud Data Fusion** (Exam 2 · Q23), (Exam 6 · Q4), (Exam 1 · Q44).
