# Cloud Digital Leader — Practice Exam 1

50 questions.

## Question 1

*Domain 2: Exploring Data Transformation with Google Cloud*

**CafePulse, a restaurant analytics website, receives daily sales records, customer feedback, and delivery logs from multiple branches. The team is converting this raw information into a cleaner, structured format so managers can later use it to discover business trends. Which step of the data value chain does this action represent?**

- [ ] A. Data analysis
- [ ] B. Data collection
- [ ] C. Data storage
- [x] D. Data processing

### Explanation

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

---

## Question 2

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**BrightCart, a retail mobile app, wants to add features such as product image recognition, customer-support chat, and demand forecasting. The team includes both experienced data scientists and developers who have very limited machine learning experience. How does Google Cloud help BrightCart use artificial intelligence and machine learning effectively?**

- [ ] A. By providing scalable on-premises tensor processing units
- [x] B. By providing APIs and tools for users with different levels of expertise
- [ ] C. By providing affordable and scalable quantum computing for application development
- [ ] D. By providing machine learning models that always require custom training

### Explanation

**Correct answer: B. By providing APIs and tools for users with different levels of expertise**

Google Cloud offers AI at several skill levels: pre-trained APIs (Vision, Natural Language and others) for developers with little ML knowledge, low-code options like AutoML, and full custom training on Gemini Enterprise Agent Platform (formerly Vertex AI) for data scientists. The clue is the mixed team: experienced data scientists and developers with limited ML experience.

**Why the others are wrong:**
- **A. On-premises tensor processing units**: TPUs are offered as cloud resources, and hardware alone does not help non-experts use ML.
- **C. Quantum computing**: quantum computing is not how Google Cloud delivers AI/ML features to app teams.
- **D. Models that always require custom training**: the opposite is true; pre-trained models and APIs work without any custom training.

**Remember:** Mixed skill levels = a range of AI tools, from pre-trained APIs to custom training.

**References:**
- [cloud.google.com/products/ai](https://cloud.google.com/products/ai)
- [docs.cloud.google.com/docs/ai-ml](https://docs.cloud.google.com/docs/ai-ml)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/beginner/beginners-guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/beginner/beginners-guide)

---

## Question 3

*Domain 2: Exploring Data Transformation with Google Cloud*

**SnackWave, a company that operates snack kiosks in office buildings, notices that the money collected from its machines often does not match the products dispensed. The company plans to replace cash-only purchases with a cloud-connected mobile payment system that records each purchase digitally. How could SnackWave benefit from this upgrade?**

- [ ] A. They could relax data access permissions.
- [ ] B. They could reduce their error budget overspend.
- [ ] C. They could improve their perimeter security.
- [x] D. They could view data history to see transactions.

### Explanation

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

---

## Question 4

*Domain 2: Exploring Data Transformation with Google Cloud*

**PayPilot Finance is building a payments application that must record customer transactions with low latency while also allowing analysts to run fast reporting queries on the same PostgreSQL-compatible operational database. The team wants a Google Cloud database that includes a columnar engine to speed up analytical queries without moving the data to a separate analytics system. Which database is designed for this requirement?**

- [ ] A. Cloud SQL
- [x] B. AlloyDB for PostgreSQL
- [ ] C. Cloud Spanner
- [ ] D. Firestore

### Explanation

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

---

## Question 5

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**BlueCart, a grocery delivery startup, is moving its existing order-processing application from its data center to Google Cloud. The team wants the application to run in the cloud with no changes to the application code and no redesign of the current architecture. Which migration approach matches this plan?**

- [x] A. Rehosted
- [ ] B. Reimagined
- [ ] C. Replatformed
- [ ] D. Refactored

### Explanation

**Correct answer: A. Rehosted**

Rehosting ("lift and shift") moves an application to the cloud as it is, with no code changes and no redesign. It is the fastest migration path. The clue is "no changes to the application code and no redesign of the current architecture".

**Why the others are wrong:**
- **B. Reimagined**: reimagining means designing a new cloud-native application from scratch.
- **C. Replatformed**: replatforming ("move and improve") makes small changes, such as swapping in a managed database.
- **D. Refactored**: refactoring changes the code, often splitting a monolith into microservices.

**Remember:** No code changes, no redesign = rehost (lift and shift).

**References:**
- [cloud.google.com/learn/cloud-migration](https://cloud.google.com/learn/cloud-migration)
- [docs.cloud.google.com/architecture/migration-to-gcp-getting-started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started)
- [docs.cloud.google.com/migration-center/docs/migration-planning-overview](https://docs.cloud.google.com/migration-center/docs/migration-planning-overview)

---

## Question 6

*Domain 2: Exploring Data Transformation with Google Cloud*

**StreamNest, a video learning website, stores training clips and images that must be delivered to users in several countries. The company needs a Cloud Storage option that supports broad geographic access and a high level of availability. What Cloud Storage feature would StreamNest benefit from?**

- [x] A. Multi-region bucket location
- [ ] B. Global metadata
- [ ] C. Data encryption
- [ ] D. Object versioning

### Explanation

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

---

## Question 7

*Domain 6: Scaling with Google Cloud Operations*

**PayWave Market, an online payments platform, depends on a public cloud provider for its customer-facing checkout service. The provider promised an SLA of 99.95% availability but did not meet that commitment during a busy shopping week. What is a possible impact on PayWave Market?**

- [ ] A. PayWave Market could use up its internal error budget.
- [ ] B. PayWave Market might need to renegotiate the SLA so uptime matters less.
- [x] C. Unplanned downtime could cause customers to leave the platform.
- [ ] D. All information stored in PayWave Market’s database could be automatically deleted.

### Explanation

**Correct answer: C. Unplanned downtime could cause customers to leave the platform.**

When a provider misses its SLA, the customer-facing checkout service goes down. Customers who cannot pay may go to a competitor and not come back. The question asks for the business impact, and lost customers (churn) and lost revenue are the most direct one, especially during a busy shopping week.

**Why the others are wrong:**
- **A. Use up its internal error budget**: provider downtime can count against PayWave's own SLO, but this is an internal reliability metric, not the main business impact asked for.
- **B. Renegotiate the SLA so uptime matters less**: uptime still matters to customers; a weaker SLA does not fix anything.
- **D. All database information automatically deleted**: an availability failure does not delete stored data.

**Remember:** Missed SLA → downtime → unhappy customers and lost revenue. The provider usually owes service credits.

**References:**
- [cloud.google.com/architecture/framework/reliability/set-targets](https://cloud.google.com/architecture/framework/reliability/set-targets)
- [cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos)
- [cloud.google.com/terms/sla](https://cloud.google.com/terms/sla)

**⚠️ Note:** Option A is not absurd, since provider downtime does count against your own SLO and error budget. C is keyed because it is the clearest business impact. Pick C on this exam.

---

## Question 8

*Domain 1: Digital Transformation with Google Cloud*

**GlobeFleet Logistics, a transportation company with offices in several countries, wants to move from its aging data centers to public cloud services. What is one benefit GlobeFleet Logistics can gain from using the public cloud?**

- [ ] A. It can schedule physical server repairs after office hours.
- [ ] B. It can receive guaranteed 100% availability for every cloud service in every region.
- [ ] C. It no longer needs security controls when moving data to the cloud.
- [x] D. It can access data and computing resources without being limited to one physical location.

### Explanation

**Correct answer: D. It can access data and computing resources without being limited to one physical location.**

Public cloud resources are reachable over the internet from anywhere, and they run in Google's global network of regions. A company with offices in several countries can serve all of them without owning a data center near each office. The clue is "offices in several countries" moving off "aging data centers".

**Why the others are wrong:**
- **A. Schedule physical server repairs after office hours**: in the public cloud the provider handles physical hardware; the customer does not repair servers.
- **B. Guaranteed 100% availability**: no cloud provider guarantees 100% availability; SLAs set targets such as 99.9% or 99.99%.
- **C. No longer needs security controls**: under the shared responsibility model the customer still secures its data, access and configuration.

**Remember:** Public cloud = global reach, on-demand resources, no hardware to maintain. Never 100% uptime and never zero customer security work.

**References:**
- [cloud.google.com/learn/what-is-public-cloud](https://cloud.google.com/learn/what-is-public-cloud)
- [cloud.google.com/learn/advantages-of-cloud-computing](https://cloud.google.com/learn/advantages-of-cloud-computing)
- [cloud.google.com/discover/types-of-cloud-computing](https://cloud.google.com/discover/types-of-cloud-computing)

---

## Question 9

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**MealBridge, a grocery pickup app, needs live product availability from several partner stores. The app must also send each customer’s confirmed order details back to the correct store immediately so staff can prepare the order. What should MealBridge use?**

- [ ] A. Site reliability engineering (SRE)
- [x] B. An application programming interface (API)
- [ ] C. A customized machine learning model
- [ ] D. A multi-regional database

### Explanation

**Correct answer: B. An application programming interface (API)**

An API lets two software systems exchange data in a standard, controlled way. MealBridge can call each partner store's API to read live product availability and send confirmed orders back right away. The clue is two-way, real-time data exchange between separate systems.

**Why the others are wrong:**
- **A. Site reliability engineering (SRE)**: SRE is a practice for running reliable services, not a way to connect systems.
- **C. A customized machine learning model**: nothing here needs prediction; the app just needs to send and receive data.
- **D. A multi-regional database**: a database stores data but does not connect the app to the partner stores' own systems.

**Remember:** Systems need to talk to each other = API.

**References:**
- [cloud.google.com/apis/docs/overview](https://cloud.google.com/apis/docs/overview)
- [cloud.google.com/apis/docs/client-libraries-explained](https://cloud.google.com/apis/docs/client-libraries-explained)
- [cloud.google.com/apis/design](https://cloud.google.com/apis/design)

---

## Question 10

*Domain 5: Trust and Security with Google Cloud*

**FinWell, a digital banking company, stores customer transaction records in cloud regions selected for regulatory reasons. The compliance team wants to understand how the legal idea of data sovereignty affects those records. What does data sovereignty mean for the stored data?**

- [x] A. Data is governed by the laws and regulations of the country where it is stored.
- [ ] B. A country automatically has the right to access all data created inside its borders.
- [ ] C. A customer has the right to fully control their own personal information.
- [ ] D. Data must be encrypted whenever it is stored or transmitted.

### Explanation

**Correct answer: A. Data is governed by the laws and regulations of the country where it is stored.**

Data sovereignty means data is subject to the laws of the country (or region) where it physically resides. That is why FinWell picks regions "for regulatory reasons". Where the data sits decides which rules apply to it.

**Why the others are wrong:**
- **B. A country automatically has the right to access all data**: sovereignty means local laws apply, not that a government can access everything automatically.
- **C. A customer has the right to fully control their own personal information**: this describes data privacy and individual rights, not sovereignty.
- **D. Data must be encrypted**: encryption is a security control; it is not the definition of sovereignty.

**Remember:** Sovereignty = whose laws apply. Residency = where the data is stored.

**References:**
- [cloud.google.com/sovereign-cloud](https://cloud.google.com/sovereign-cloud)
- [docs.cloud.google.com/assured-workloads/docs/data-residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency)
- [docs.cloud.google.com/architecture/framework/security/meet-regulatory-compliance-and-privacy-needs](https://docs.cloud.google.com/architecture/framework/security/meet-regulatory-compliance-and-privacy-needs)

---

## Question 11

*Domain 6: Scaling with Google Cloud Operations*

**RideMango is a food-delivery mobile app running several workloads on Google Cloud. The finance team does not want to wait until the monthly invoice arrives to discover that spending has gone beyond their planned cloud budget. They want to receive a notification when costs cross a defined limit, such as ₹75,000 for the month. What should RideMango do?**

- [ ] A. Stop Compute Engine virtual machines outside peak ordering hours.
- [x] B. Configure a budget threshold rule and alert.
- [ ] C. Change project resource quota policies.
- [ ] D. Review past billing reports to estimate future overspending.

### Explanation

**Correct answer: B. Configure a budget threshold rule and alert.**

Cloud Billing budgets let you set a planned amount and threshold rules (for example, 50%, 90% and 100% of the budget). When spending crosses a threshold, alerts go out to the chosen people. The clue is that finance wants a notification when costs cross a limit, not after the invoice arrives.

**Why the others are wrong:**
- **A. Stop VMs outside peak hours**: this may lower costs, but it does not notify anyone when spending crosses the limit.
- **C. Change resource quota policies**: quotas cap how many resources can be used; they are not a spending alert.
- **D. Review past billing reports**: looking backward is exactly what finance wants to avoid; it is not proactive.

**Remember:** "Notify me when spend crosses X" = budget + threshold alert. Budgets alert; they do not stop spending by themselves.

**References:**
- [cloud.google.com/billing/docs/how-to/budgets](https://cloud.google.com/billing/docs/how-to/budgets)
- [cloud.google.com/billing/docs/how-to/budget-api-overview](https://cloud.google.com/billing/docs/how-to/budget-api-overview)
- [cloud.google.com/docs/quotas/overview](https://cloud.google.com/docs/quotas/overview)

---

## Question 12

*Domain 5: Trust and Security with Google Cloud*

**SkillGrid Analytics, an online learning platform, has hired a new reporting analyst. The administrator wants the analyst to be able to view existing BigQuery datasets for dashboard work, but the analyst must not be allowed to delete datasets or create new datasets. Which Google Cloud service should the administrator use to define and assign the correct access roles?**

- [ ] A. Cloud Storage
- [x] B. Identity and Access Management (IAM)
- [ ] C. Virtual Private Cloud (VPC)
- [ ] D. Cloud Trace

### Explanation

**Correct answer: B. Identity and Access Management (IAM)**

IAM controls who can do what on which resource. The administrator grants the analyst a role that allows viewing BigQuery data but not creating or deleting datasets. This follows the principle of least privilege. The clue is "define and assign the correct access roles".

**Why the others are wrong:**
- **A. Cloud Storage**: Cloud Storage is object storage, not an access control service.
- **C. Virtual Private Cloud (VPC)**: VPC controls network connectivity, not per-user permissions on datasets.
- **D. Cloud Trace**: Cloud Trace measures request latency in applications.

**Remember:** Who can do what on which resource = IAM. Give only the access needed (least privilege).

**References:**
- [docs.cloud.google.com/iam/docs/overview](https://docs.cloud.google.com/iam/docs/overview)
- [docs.cloud.google.com/iam/docs/roles-overview](https://docs.cloud.google.com/iam/docs/roles-overview)
- [docs.cloud.google.com/bigquery/docs/access-control](https://docs.cloud.google.com/bigquery/docs/access-control)

---

## Question 13

*Domain 2: Exploring Data Transformation with Google Cloud*

**ShopNexa is an online shopping mobile app that stores customer orders, inventory, and payment records in an existing PostgreSQL database. As the number of transactions increases, the database is becoming slower during peak sale events. The engineering team wants to move to a fully managed Google Cloud database service that is compatible with PostgreSQL, provides better performance, scales well, and supports high availability with minimal changes to the current application code. Which service should they choose?**

- [ ] A. Spanner
- [x] B. AlloyDB for PostgreSQL
- [ ] C. Bigtable
- [ ] D. Firestore

### Explanation

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

---

## Question 14

*Domain 6: Scaling with Google Cloud Operations*

**TrailNest, a travel booking website, wants to understand what out-of-the-box observability means for its cloud operations team. The team needs a ready-to-use way to gain visibility into the health, performance, and behavior of the services running in its cloud environment. What does out-of-the-box observability mean in the context of cloud operations?**

- [ ] A. Monitoring software release schedules
- [x] B. Monitoring IT infrastructure and applications
- [ ] C. Monitoring traveler ratings and survey responses
- [ ] D. Monitoring monthly cloud billing charges

### Explanation

**Correct answer: B. Monitoring IT infrastructure and applications**

Out-of-the-box observability means you get visibility into the health and performance of your infrastructure and applications right away, with built-in metrics, logs and dashboards. On Google Cloud this comes from Google Cloud Observability (Cloud Monitoring, Cloud Logging and related tools). The clue is "health, performance, and behavior of the services".

**Why the others are wrong:**
- **A. Monitoring software release schedules**: release planning is a project management task, not observability.
- **C. Monitoring traveler ratings**: customer feedback is business data, not service health.
- **D. Monitoring monthly cloud billing**: cost tracking is billing management, not observability.

**Remember:** Observability = visibility into how your systems and apps are running.

**References:**
- [cloud.google.com/products/operations](https://cloud.google.com/products/operations)
- [cloud.google.com/monitoring/docs](https://cloud.google.com/monitoring/docs)
- [cloud.google.com/logging/docs](https://cloud.google.com/logging/docs)

---

## Question 15

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**TaskFlow, a project management software company, is building several new containerized applications for different departments. The platform team wants a managed Google Cloud service that can help deploy, scale, and orchestrate those containers efficiently. Why should TaskFlow use Google Kubernetes Engine?**

- [x] A. It enables rapid application deployment and testing.
- [ ] B. It optimizes virtual machine performance.
- [ ] C. It connects legacy systems to an application.
- [ ] D. It provides pre-written source code for application development.

### Explanation

**Correct answer: A. It enables rapid application deployment and testing.**

GKE is Google's managed Kubernetes service. It deploys, scales and orchestrates containers, so teams can release and test new versions quickly and consistently. The clue is "deploy, scale, and orchestrate those containers efficiently" for several new containerized apps.

**Why the others are wrong:**
- **B. Optimizes VM performance**: GKE manages containers, not the tuning of individual virtual machines.
- **C. Connects legacy systems to an application**: connecting systems is the job of APIs (for example with Apigee), not GKE.
- **D. Provides pre-written source code**: GKE runs your code; it does not write it for you.

**Remember:** Containers that need orchestration and scaling = GKE.

**References:**
- [cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview](https://cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)
- [cloud.google.com/kubernetes-engine/docs/deploy-app-cluster](https://cloud.google.com/kubernetes-engine/docs/deploy-app-cluster)
- [cloud.google.com/kubernetes-engine/docs/get-started/deploy-workloads](https://cloud.google.com/kubernetes-engine/docs/get-started/deploy-workloads)

**⚠️ Note:** "Rapid deployment and testing" is a generic benefit of containers and CI/CD, not something only GKE provides. It is keyed because the other options are clearly false. Pick A on this exam.

---

## Question 16

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**MediBridge, a healthcare appointment platform, wants to run small pieces of backend code whenever users submit forms, upload documents, or trigger events from other cloud services. The team does not want to manage servers, and it cannot predict how much compute capacity will be needed as usage changes throughout the day. Which Google Cloud solution should MediBridge use?**

- [ ] A. Compute Engine
- [ ] B. Google Kubernetes Engine
- [x] C. Cloud Run functions
- [ ] D. Bare Metal Solution for SAP

### Explanation

**Correct answer: C. Cloud Run functions**

Cloud Run functions (formerly Cloud Functions) runs small pieces of code in response to events, such as a form submission, a file upload or a message from another service. It is serverless and scales automatically, including down to zero. The clues are "small pieces of backend code", "trigger events", "does not want to manage servers" and unpredictable demand.

**Why the others are wrong:**
- **A. Compute Engine**: VMs must be sized and managed, which the team wants to avoid.
- **B. Google Kubernetes Engine**: GKE runs containers but still involves cluster management; it is more than needed for small event-driven code.
- **D. Bare Metal Solution for SAP**: this is dedicated physical hardware for special workloads, the opposite of serverless.

**Remember:** Small code + triggered by events + no servers = Cloud Run functions.

**References:**
- [cloud.google.com/functions](https://cloud.google.com/functions)
- [cloud.google.com/run/docs](https://cloud.google.com/run/docs)
- [cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview](https://cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)

---

## Question 17

*Domain 5: Trust and Security with Google Cloud*

**NovaInbox, a secure email collaboration platform, receives a file attachment that looks suspicious after being reported by an employee. The security research team wants to compare the file and related URLs against a large global threat intelligence dataset that aggregates results from many antivirus engines, URL scanners, and security community submissions. Which Google Cloud-affiliated tool should the team use?**

- [ ] A. Cloud Translation API
- [ ] B. Cloud SQL
- [x] C. VirusTotal
- [ ] D. BigQuery Omni

### Explanation

**Correct answer: C. VirusTotal**

VirusTotal, part of Google, checks files and URLs against many antivirus engines, URL scanners and community submissions. It holds a large shared threat intelligence dataset. The clue is the exact description: "aggregates results from many antivirus engines, URL scanners, and security community submissions".

**Why the others are wrong:**
- **A. Cloud Translation API**: it translates text between languages and has no security function.
- **B. Cloud SQL**: it is a managed relational database, not a threat intelligence tool.
- **D. BigQuery Omni**: it runs BigQuery analytics on data in other clouds; it is not a malware scanner.

**Remember:** Check a suspicious file or URL against many scanners = VirusTotal. Frontline incident-response intelligence = Mandiant.

**References:**
- [cloud.google.com/security/resources/google-threat-intelligence-virustotal](https://cloud.google.com/security/resources/google-threat-intelligence-virustotal)
- [docs.virustotal.com/docs/api-overview](https://docs.virustotal.com/docs/api-overview)
- [docs.virustotal.com/docs/contributors](https://docs.virustotal.com/docs/contributors)

---

## Question 18

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**MapleBank still runs an older core banking system and does not have the budget to replace or modernize its infrastructure right now. However, MapleBank wants its business partner’s modern analytics platform to securely access selected data from the legacy system. What should MapleBank use to make its data accessible?**

- [ ] A. Compute Engine
- [ ] B. GKE Enterprise
- [x] C. An application programming interface
- [ ] D. Google Kubernetes Engine

### Explanation

**Correct answer: C. An application programming interface**

An API exposes selected data and functions from a legacy system in a secure, controlled way, without replacing the system. MapleBank can let the partner's analytics platform request only the approved data. The clues are "no budget to replace or modernize" and "securely access selected data".

**Why the others are wrong:**
- **A. Compute Engine**: running VMs does not by itself make the legacy system's data accessible to a partner.
- **B. GKE Enterprise**: it is a platform for running and modernizing container workloads, which the bank has no budget for.
- **D. Google Kubernetes Engine**: GKE runs containers; it does not expose legacy data to partners.

**Remember:** Unlock legacy data without replacing the system = API.

**References:**
- [cloud.google.com/learn/what-is-api-management](https://cloud.google.com/learn/what-is-api-management)
- [cloud.google.com/apigee/docs/api-platform/get-started/what-apigee](https://cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)
- [cloud.google.com/compute/docs/instances/use-cases](https://cloud.google.com/compute/docs/instances/use-cases)

---

## Question 19

*Domain 2: Exploring Data Transformation with Google Cloud*

**StreamNest Media runs a video streaming website that creates application logs and service configuration files in JSON and XML formats. These files do not follow a fixed relational table structure, but they include nested fields, tags, attributes, and hierarchical elements that help organize the meaning of the data. How should this type of data be classified?**

- [ ] A. Structured data
- [x] B. Semi-structured data
- [ ] C. Unstructured data
- [ ] D. Relational data

### Explanation

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

---

## Question 20

*Domain 2: Exploring Data Transformation with Google Cloud*

**BrightCart, an online grocery marketplace, wants a business intelligence solution that lets employees from sales, operations, and marketing explore trusted business data, build reports, and discover insights without depending on engineering teams for every analysis request. Which Google Cloud product or service should BrightCart use?**

- [ ] A. Spanner
- [ ] B. BigQuery
- [x] C. Looker
- [ ] D. Dataflow

### Explanation

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

---

## Question 21

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**ShopTrail, a retail analytics company, relies on older inventory and billing systems that are becoming difficult to adapt whenever new digital services are launched. The company wants a way to make existing system capabilities easier to reuse across mobile apps, partner portals, and cloud services without replacing everything at once. Why should ShopTrail use application programming interfaces APIs?**

- [ ] A. To reveal every backend record so external partners can directly change it
- [ ] B. To fully rebuild all legacy applications from the ground up
- [x] C. To gain long-term operational flexibility
- [ ] D. To move IT spending to a pay-as-you-go model so infrastructure can scale

### Explanation

**Correct answer: C. To gain long-term operational flexibility**

APIs wrap existing system capabilities behind a stable interface. New mobile apps, partner portals and cloud services can reuse them without touching the legacy systems directly. Teams can then modernize the back end step by step. The clues are "easier to reuse" and "without replacing everything at once".

**Why the others are wrong:**
- **A. Reveal every backend record so partners can directly change it**: APIs expose only selected data and actions, with security controls.
- **B. Fully rebuild all legacy applications**: APIs avoid a full rebuild; that is the point.
- **D. Move IT spending to pay-as-you-go**: that describes cloud consumption pricing, not the purpose of APIs.

**Remember:** APIs = reuse what you have, connect new services, modernize gradually.

**References:**
- [cloud.google.com/apigee](https://cloud.google.com/apigee)
- [cloud.google.com/solutions/unlocking-legacy-applications](https://cloud.google.com/solutions/unlocking-legacy-applications)
- [docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)

---

## Question 22

*Domain 2: Exploring Data Transformation with Google Cloud*

**ShopNest, an ecommerce website, wants to improve customer experience by analyzing different kinds of information collected from its platform. Which type of information is an example of unstructured data that ShopNest can use for business decisions?**

- [x] A. Written feedback submitted by customers after delivery
- [ ] B. GPS coordinates of partner store locations
- [ ] C. Monthly product revenue trends
- [ ] D. Stock quantity records in fulfillment centers

### Explanation

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

---

## Question 23

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**FitLoop, a fitness subscription app, is finding it difficult to keep up with users who expect frequent feature improvements and quick fixes. The company plans to modernize its older applications by moving them to Google Cloud. Why would this help FitLoop better meet user expectations?**

- [ ] A. Customer data can be used to provide personalized content
- [ ] B. Toil automation helps perform automatic updates
- [x] C. Updates can be released more quickly to fix bugs
- [ ] D. DevOps requires market trends to be measured and tracked

### Explanation

**Correct answer: C. Updates can be released more quickly to fix bugs**

Modernizing applications on Google Cloud (managed services, containers, CI/CD) shortens the path from code change to production. FitLoop can ship features and fixes more often and more safely. The clue is users expecting "frequent feature improvements and quick fixes".

**Why the others are wrong:**
- **A. Personalized content**: personalization is a possible benefit of data, but it does not answer the need for faster fixes.
- **B. Toil automation helps perform automatic updates**: reducing toil is an SRE idea; it does not mean apps update themselves.
- **D. DevOps requires market trends to be measured**: DevOps is about faster, more reliable software delivery, not tracking market trends.

**Remember:** Modernize → release faster → meet user expectations sooner.

**References:**
- [cloud.google.com/solutions/application-modernization](https://cloud.google.com/solutions/application-modernization)
- [cloud.google.com/devops](https://cloud.google.com/devops)
- [cloud.google.com/architecture/devops](https://cloud.google.com/architecture/devops)

---

## Question 24

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**OrbitCart, a retail marketplace, wants one platform that helps its engineering teams create new container-based services, modernize older applications, and operate workloads consistently across Google Cloud and another public cloud provider. Which Google Cloud solution should OrbitCart use?**

- [ ] A. Apigee Hybrid
- [x] B. GKE Enterprise
- [ ] C. Cloud Run
- [ ] D. Compute Engine

### Explanation

**Correct answer: B. GKE Enterprise**

GKE Enterprise (formerly Anthos) is Google's platform to build, modernize and manage container workloads consistently across Google Cloud, on-premises and other public clouds. The clues are "one platform", "modernize older applications" and "operate workloads consistently across Google Cloud and another public cloud provider".

**Why the others are wrong:**
- **A. Apigee Hybrid**: Apigee manages APIs; it does not run and manage container workloads across clouds.
- **C. Cloud Run**: Cloud Run is a serverless container service on Google Cloud, not a multicloud management platform.
- **D. Compute Engine**: Compute Engine provides VMs on Google Cloud only.

**Remember:** Containers managed consistently across hybrid and multicloud = GKE Enterprise.

**References:**
- [cloud.google.com/kubernetes-engine/enterprise/docs/deployment-options](https://cloud.google.com/kubernetes-engine/enterprise/docs/deployment-options)
- [cloud.google.com/kubernetes-engine/enterprise/clusters/docs](https://cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
- [cloud.google.com/run/docs/overview/what-is-cloud-run](https://cloud.google.com/run/docs/overview/what-is-cloud-run)

---

## Question 25

*Domain 5: Trust and Security with Google Cloud*

**BrightCart, an online grocery delivery app, runs several batch-processing workloads on Compute Engine. The finance team notices that the monthly Compute Engine bill has increased unexpectedly. After reviewing the project, the security team finds that a compromised account created unauthorized VM workloads that are consuming CPU resources to perform hashing calculations and earn cryptocurrency for the attacker. What type of attack is this?**

- [x] A. Cryptomining
- [ ] B. Phishing
- [ ] C. LLM attack
- [ ] D. Distributed Denial-of-Service (DDoS)

### Explanation

**Correct answer: A. Cryptomining**

Cryptomining (cryptojacking) is when attackers use someone else's computing resources to mine cryptocurrency. The victim pays the bill. The clues are unauthorized VMs, high CPU use for "hashing calculations" and a surprise rise in the compute bill.

**Why the others are wrong:**
- **B. Phishing**: phishing tricks people into giving away credentials; it may be how the account was compromised, but it is not what the VMs are doing.
- **C. LLM attack**: this targets AI models, such as with prompt injection; no AI model is involved here.
- **D. DDoS**: a DDoS floods a service with traffic to make it unavailable; it does not use the victim's VMs to earn money.

**Remember:** Surprise compute bill + unknown VMs + high CPU = cryptomining.

**References:**
- [cloud.google.com/security-command-center/cryptomining-protection-program](https://cloud.google.com/security-command-center/cryptomining-protection-program)
- [docs.cloud.google.com/security-command-center/docs/cryptomining-detection-best-practices](https://docs.cloud.google.com/security-command-center/docs/cryptomining-detection-best-practices)
- [docs.cloud.google.com/armor/docs/cloud-armor-overview](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)

---

## Question 26

*Domain 5: Trust and Security with Google Cloud*

**MealTrail, a food delivery app, stores order history and customer contact details in a Cloud Storage bucket. During an internal review, the team discovers that a junior administrator accidentally allowed public internet access to the bucket. External users could view the files without exploiting any software flaw or using advanced attack methods. What is the root cause of this security incident?**

- [x] A. Misconfiguration
- [ ] B. Advanced Persistent Threat (APT)
- [ ] C. Zero-day vulnerability
- [ ] D. Ransomware

### Explanation

**Correct answer: A. Misconfiguration**

The bucket was exposed because an administrator set its access incorrectly. No software flaw or advanced attack was involved. Misconfiguration is one of the most common causes of cloud data exposure. The clue is "accidentally allowed public internet access" and "without exploiting any software flaw".

**Why the others are wrong:**
- **B. Advanced Persistent Threat (APT)**: an APT is a skilled attacker staying hidden in a network for a long time, which is not what happened.
- **C. Zero-day vulnerability**: a zero-day is an unknown software flaw; the stem says no flaw was exploited.
- **D. Ransomware**: ransomware encrypts data and demands payment; here files were simply readable.

**Remember:** Human error in settings (like a public bucket) = misconfiguration.

**References:**
- [docs.cloud.google.com/storage/docs/public-access-prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention)
- [docs.cloud.google.com/storage/docs/access-control](https://docs.cloud.google.com/storage/docs/access-control)
- [docs.cloud.google.com/security-command-center/docs/security-command-center-overview](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)

---

## Question 27

*Domain 5: Trust and Security with Google Cloud*

**HealthBridge, a telemedicine provider, stores patient appointment details and consultation records in Google Cloud. The security team is reviewing the core security principles that help protect data. They want to understand how availability strengthens the organization’s overall data security posture. What does availability mean in this context?**

- [ ] A. By limiting data access only to approved users
- [ ] B. By making sure data follows required regulatory and industry standards
- [ ] C. By verifying that data remains correct, complete, and dependable
- [x] D. By making sure data remains dependable and accessible when needed

### Explanation

**Correct answer: D. By making sure data remains dependable and accessible when needed**

Availability is the "A" in the CIA triad (confidentiality, integrity, availability). It means authorized users can reach data and systems when they need them. For a telemedicine provider, doctors must be able to open patient records during consultations.

**Why the others are wrong:**
- **A. Limiting access to approved users**: this is confidentiality.
- **B. Following regulatory and industry standards**: this is compliance.
- **C. Data remains correct, complete, and dependable**: this is integrity.

**Remember:** Confidentiality = only the right people. Integrity = correct and unaltered. Availability = there when needed.

**References:**
- [cloud.google.com/learn/what-is-cloud-data-security](https://cloud.google.com/learn/what-is-cloud-data-security)
- [docs.cloud.google.com/architecture/framework/security](https://docs.cloud.google.com/architecture/framework/security)
- [docs.cloud.google.com/architecture/framework/reliability](https://docs.cloud.google.com/architecture/framework/reliability)

---

## Question 28

*Domain 2: Exploring Data Transformation with Google Cloud*

**PhotoNest Gallery stores millions of customer-uploaded images and backup files in Cloud Storage. The engineering team wants to reduce storage costs, but they do not want to create manual rules such as “move objects after 45 days” or “change storage class after a specific number of versions.” Instead, they want Cloud Storage to automatically move objects between storage classes based on how frequently each object is actually accessed. Which feature should they use?**

- [ ] A. Object Lifecycle Management
- [x] B. Cloud Storage Autoclass
- [ ] C. Storage Transfer Service
- [ ] D. Cloud CDN

### Explanation

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

---

## Question 29

*Domain 1: Digital Transformation with Google Cloud*

**SunriseMart, a regional grocery chain, wants to move from running most applications in its own data center to using cloud services. The company wants to understand how this move can help its teams create more business value over time. How does switching from on-premises infrastructure to the cloud help SunriseMart gain value over time?**

- [ ] A. They can expand their internal application hosting infrastructure
- [x] B. They can focus their efforts on solution development
- [ ] C. They can increase development of data recovery systems
- [ ] D. They can relax their on-premises data security protocols

### Explanation

**Correct answer: B. They can focus their efforts on solution development**

In the cloud, the provider runs the hardware, data centers and much of the platform. SunriseMart's teams spend less time on infrastructure and more time building solutions that create business value. The clue is "create more business value over time".

**Why the others are wrong:**
- **A. Expand internal hosting infrastructure**: moving to the cloud reduces the need for internal infrastructure.
- **C. Increase development of data recovery systems**: the cloud offers managed backup and recovery, so teams build less of this themselves.
- **D. Relax data security protocols**: security remains a shared responsibility; the company still protects its data and access.

**Remember:** Cloud = less undifferentiated infrastructure work, more focus on what makes the business unique.

**References:**
- [cloud.google.com/learn/what-is-cloud-computing](https://cloud.google.com/learn/what-is-cloud-computing)
- [cloud.google.com/architecture/framework](https://cloud.google.com/architecture/framework)
- [cloud.google.com/security/shared-responsibility-data-model](https://cloud.google.com/security/shared-responsibility-data-model)

---

## Question 30

*Domain 5: Trust and Security with Google Cloud*

**BrightCart, a retail mobile app company, runs more than 240 Google Cloud projects for payment services, product search, inventory APIs, and analytics workloads. Its security team wants one centralized place to review the organization’s overall security posture, find risky configurations, and detect vulnerabilities across the Google Cloud environment. Which Google Cloud product should BrightCart use?**

- [x] A. Security Command Center
- [ ] B. Managed Service for Apache Spark
- [ ] C. Cloud Load Balancing
- [ ] D. Dataflow

### Explanation

**Correct answer: A. Security Command Center**

Security Command Center is Google Cloud's central security and risk management service. It shows the security posture across the whole organization and finds misconfigurations, vulnerabilities and threats. The clues are "240 projects", "one centralized place", "risky configurations" and "vulnerabilities".

**Why the others are wrong:**
- **B. Managed Service for Apache Spark**: it runs Spark and Hadoop data processing jobs, not security reviews.
- **C. Cloud Load Balancing**: it spreads traffic across back ends; it does not assess security posture.
- **D. Dataflow**: Dataflow runs data pipelines, not security scanning.

**Remember:** Central view of security posture, misconfigurations and vulnerabilities across Google Cloud = Security Command Center.

**References:**
- [docs.cloud.google.com/security-command-center/docs](https://docs.cloud.google.com/security-command-center/docs)
- [docs.cloud.google.com/security-command-center/docs/security-command-center-overview](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)
- [docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings)

---

## Question 31

*Domain 5: Trust and Security with Google Cloud*

**FinEdge Pay, a digital wallet company, trains employees to recognize common cybersecurity threats. One employee receives a message that looks like it came from the internal support team. The message says the employee’s account access will be disabled in 12 hours unless they click a link and sign in on a look-alike company portal. The portal is fake and is built to capture the employee’s username and password. What type of cybersecurity threat is this?**

- [ ] A. DDoS attack
- [x] B. Phishing
- [ ] C. Cryptomining
- [ ] D. LLM attack

### Explanation

**Correct answer: B. Phishing**

Phishing is a social engineering attack. A fake message pretends to come from a trusted source and tricks people into giving up credentials or clicking malicious links. The clues are the urgent threat (access disabled in 12 hours), a look-alike portal and a fake sign-in page built to capture usernames and passwords.

**Why the others are wrong:**
- **A. DDoS attack**: a DDoS floods a service with traffic; it does not trick employees into sharing passwords.
- **C. Cryptomining**: cryptomining uses stolen computing power to mine cryptocurrency.
- **D. LLM attack**: this targets AI models, such as with prompt injection; no AI model is involved.

**Remember:** Fake message + urgency + fake login page = phishing.

**References:**
- [support.google.com/mail/answer/8253](https://support.google.com/mail/answer/8253)
- [cisa.gov/secure-our-world/recognize-and-report-phishing](https://cisa.gov/secure-our-world/recognize-and-report-phishing)
- [cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks](https://cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)

---

## Question 32

*Domain 2: Exploring Data Transformation with Google Cloud*

**PhotoTrail is a travel-photo sharing website that stores millions of uploaded images and videos in Cloud Storage. Some files are downloaded frequently for a few days, while others may not be accessed again for months, and the team cannot reliably predict these access patterns. The company wants Cloud Storage to automatically reduce storage costs by placing infrequently accessed objects into colder storage classes without the team manually creating rules or analyzing object usage. Which Cloud Storage feature should they enable?**

- [ ] A. Object Versioning
- [x] B. Autoclass
- [ ] C. Lifecycle management rules
- [ ] D. Requester Pays

### Explanation

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

---

## Question 33

*Domain 5: Trust and Security with Google Cloud*

**FitGuide, a fitness coaching mobile app, is launching several public-facing generative AI chat features for workout planning and nutrition guidance. The security team wants a Google Cloud capability that can inspect AI prompts and responses, reduce prompt injection and jailbreak risks, and block harmful or inappropriate model output before it reaches users. Which Google Cloud capability should the team use?**

- [ ] A. Cloud Storage Autoclass
- [x] B. Model Armor
- [ ] C. Virtual Machine snapshots
- [ ] D. Cloud Run functions

### Explanation

**Correct answer: B. Model Armor**

Model Armor is a Google Cloud service that screens prompts and responses for generative AI apps. It helps detect prompt injection and jailbreak attempts and filters harmful or inappropriate content before it reaches users. The clue is "inspect AI prompts and responses" and "block harmful or inappropriate model output".

**Why the others are wrong:**
- **A. Cloud Storage Autoclass**: it optimizes storage costs; it has nothing to do with AI safety.
- **C. Virtual Machine snapshots**: snapshots back up VM disks; they do not inspect AI traffic.
- **D. Cloud Run functions**: it runs event-driven code, not AI prompt and response screening.

**Remember:** Protect gen AI prompts and responses (prompt injection, jailbreaks, harmful output) = Model Armor.

**References:**
- [docs.cloud.google.com/model-armor/overview](https://docs.cloud.google.com/model-armor/overview)
- [docs.cloud.google.com/model-armor/sanitize-prompts-responses](https://docs.cloud.google.com/model-armor/sanitize-prompts-responses)
- [docs.cloud.google.com/functions/docs](https://docs.cloud.google.com/functions/docs)

---

## Question 34

*Domain 2: Exploring Data Transformation with Google Cloud*

**TrailWise Trips is building a generative AI assistant to help customers plan vacations from past bookings, support chats, destination reviews, and loyalty data. The leadership team wants to launch quickly, but the analytics team says the company’s data is spread across different systems, has inconsistent quality, and is not governed well enough for reliable AI use. The company wants the data to be unified, cleaned, trusted, and governed before using it for AI workloads. What concept best describes this target state of the data?**

- [x] A. AI-ready data
- [ ] B. Coldline storage data
- [ ] C. Ephemeral data
- [ ] D. On-premises data

### Explanation

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

---

## Question 35

*Domain 2: Exploring Data Transformation with Google Cloud*

**FinSightHub is a financial analytics platform that collects transaction events, customer activity logs, and operational records from many systems. The company wants to describe the complete journey of this data, starting from creation and ingestion, continuing through processing and storage, and ending when the data is used for reporting, analytics, and AI-driven business decisions. What term best describes this end-to-end data lifecycle process?**

- [ ] A. Data center modernization
- [x] B. Data supply chain
- [ ] C. Open source integration
- [ ] D. Infrastructure as a Service (IaaS)

### Explanation

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

---

## Question 36

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**Trackly, a logistics analytics company, wants to create custom machine learning models to predict delivery delays. The team needs a managed Google Cloud platform that helps them prepare data, train models, deploy them, and monitor model performance after deployment. Which service should they use?**

- [ ] A. Document AI
- [ ] B. Natural Language API
- [ ] C. Google Kubernetes Engine
- [x] D. Gemini Enterprise Agent Platform

### Explanation

**Correct answer: D. Gemini Enterprise Agent Platform**

Gemini Enterprise Agent Platform (formerly Vertex AI) is Google Cloud's unified, managed ML platform. It covers the full ML lifecycle: preparing data, training custom models, deploying them and monitoring them in production. The clues are "custom machine learning models" and the list of lifecycle steps.

**Why the others are wrong:**
- **A. Document AI**: it extracts data from documents; it does not train general custom prediction models.
- **B. Natural Language API**: it is a pre-trained API for text analysis, not a platform for building custom models.
- **C. Google Kubernetes Engine**: GKE can run ML workloads, but it is a container platform, not a managed ML lifecycle service.

**Remember:** Build, train, deploy and monitor custom ML models = Gemini Enterprise Agent Platform.

**References:**
- [docs.cloud.google.com/gemini-enterprise-agent-platform/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview)

---

## Question 37

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**PulseHelp, a customer support platform, wants to use machine learning to gain insights from data that does not fit neatly into rows and columns. The company wants to analyze spoken customer conversations and identify whether callers are happy, neutral, or frustrated. Which scenario best shows machine learning unlocking business value from unstructured data?**

- [ ] A. Analyzing spreadsheet records of equipment failures to predict upcoming repair schedules.
- [ ] B. Suggesting related items based on a customer’s earlier purchases.
- [ ] C. Reviewing payment activity to detect possible fraud and financial risk.
- [x] D. Identifying customer sentiment from support center audio recordings.

### Explanation

**Correct answer: D. Identifying customer sentiment from support center audio recordings.**

Audio recordings are unstructured data. They do not fit into rows and columns. ML (speech-to-text plus sentiment analysis) can turn them into insight about how customers feel. The clue is "data that does not fit neatly into rows and columns" and "spoken customer conversations".

**Why the others are wrong:**
- **A. Spreadsheet records of equipment failures**: spreadsheets are structured data.
- **B. Suggesting items from earlier purchases**: purchase history is structured transaction data.
- **C. Reviewing payment activity for fraud**: payment records are structured data.

**Remember:** Audio, images, video and free text = unstructured. ML is what unlocks value from them.

**References:**
- [cloud.google.com/speech-to-text](https://cloud.google.com/speech-to-text)
- [docs.cloud.google.com/natural-language/docs](https://docs.cloud.google.com/natural-language/docs)
- [docs.cloud.google.com/natural-language/docs/basics](https://docs.cloud.google.com/natural-language/docs/basics)

---

## Question 38

*Domain 2: Exploring Data Transformation with Google Cloud*

**TrendBasket is a fashion retail app that gathers customer information from its own website clicks, completed orders, abandoned carts, and loyalty membership forms. The marketing team wants to use this directly collected customer data to build personalized product recommendations and shopping offers. What type of data is this considered?**

- [ ] A. Second-party data
- [ ] B. Third-party data
- [x] C. First-party data
- [ ] D. Open standard data

### Explanation

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

---

## Question 39

*Domain 2: Exploring Data Transformation with Google Cloud*

**FreshCart Rewards is planning a new advertising campaign for its grocery delivery app. The marketing team buys anonymized and aggregated audience segments from an outside data provider. This provider collected the data from multiple sources and does not directly interact with FreshCart Rewards customers. Which data classification best describes this audience data?**

- [ ] A. First-party data
- [ ] B. Second-party data
- [x] C. Third-party data
- [ ] D. Unstructured data

### Explanation

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

---

## Question 40

*Domain 5: Trust and Security with Google Cloud*

**MedNova Health, a digital healthcare portal, receives a very large number of security alerts from applications, endpoints, network devices, and cloud services every day. Its security operations team wants a cloud-native platform that can bring security data into one place, use AI and threat intelligence to improve detection, support investigations, and help analysts respond to incidents faster. Which Google Cloud solution should MedNova Health use?**

- [x] A. Google Security Operations
- [ ] B. Apigee API Management
- [ ] C. Compute Engine
- [ ] D. Cloud Spanner

### Explanation

**Correct answer: A. Google Security Operations**

Google Security Operations (formerly Chronicle) is a cloud-native security operations platform (SIEM and SOAR). It collects security data in one place, uses AI and threat intelligence to detect threats, and helps analysts investigate and respond faster. The clues are "a very large number of security alerts", "bring security data into one place" and "respond to incidents faster".

**Why the others are wrong:**
- **B. Apigee API Management**: it manages and secures APIs; it is not a security operations platform.
- **C. Compute Engine**: it provides virtual machines.
- **D. Cloud Spanner**: it is a globally distributed relational database.

**Remember:** Centralize security data, detect, investigate and respond = Google Security Operations.

**References:**
- [cloud.google.com/security/products/security-operations](https://cloud.google.com/security/products/security-operations)
- [docs.cloud.google.com/chronicle/docs/secops/secops-overview](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)
- [docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-overview](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-overview)

---

## Question 41

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**PhotoTrail, a travel-sharing mobile app, wants to train a machine learning model that can classify uploaded photos into categories such as beaches, mountains, city landmarks, and forests. Which Google Cloud product or service should PhotoTrail use?**

- [ ] A. Video Intelligence API
- [x] B. AutoML Vision
- [ ] C. BigQuery ML
- [ ] D. Looker

### Explanation

**Correct answer: B. AutoML Vision**

AutoML Vision lets a team train a custom image classification model using its own labeled photos, without writing ML code. The categories here (beaches, mountains, landmarks, forests) are specific to PhotoTrail. That calls for a custom model, not a generic pre-trained one. The clue is "train a machine learning model" to "classify uploaded photos into categories".

**Why the others are wrong:**
- **A. Video Intelligence API**: it analyzes video, not still photos.
- **C. BigQuery ML**: it builds models with SQL on structured data in BigQuery. It is not the direct way to train an image classifier from photos.
- **D. Looker**: Looker is a BI and reporting tool, not an ML training service.

**Remember:** Custom image categories + labeled photos + little ML expertise = AutoML (Vision).

**References:**
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/classification/train-model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/classification/train-model)
- [docs.cloud.google.com/video-intelligence/docs](https://docs.cloud.google.com/video-intelligence/docs)
- [docs.cloud.google.com/bigquery/docs/bqml-introduction](https://docs.cloud.google.com/bigquery/docs/bqml-introduction)

**⚠️ Note:** "AutoML Vision" is the old standalone product name. AutoML now lives inside Gemini Enterprise Agent Platform. The concept (custom image categories with labeled data and no code = AutoML) is still right, so pick B.

---

## Question 42

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**HarborLedger, a financial services company, wants to move a legacy database platform to Google Cloud. The platform depends on strict third-party licensing terms, low-level server access, and an architecture that cannot be easily redesigned for virtual machines or serverless services. What Google Cloud solution should HarborLedger use?**

- [ ] A. Compute Engine
- [x] B. Bare Metal Solution
- [ ] C. Cloud Run
- [ ] D. Cloud Run functions

### Explanation

**Correct answer: B. Bare Metal Solution**

Bare Metal Solution provides dedicated physical servers in Google Cloud locations, close to Google Cloud services. It suits specialized workloads, such as some legacy databases, that need low-level hardware access or have licensing terms that do not allow virtualization. The clues are "strict third-party licensing terms", "low-level server access" and "cannot be easily redesigned for virtual machines or serverless".

**Why the others are wrong:**
- **A. Compute Engine**: Compute Engine provides virtual machines, which the workload cannot easily use.
- **C. Cloud Run**: Cloud Run is serverless containers, which would need a redesign.
- **D. Cloud Run functions**: event-driven serverless functions are far from a legacy database platform.

**Remember:** Licensing or hardware needs that rule out VMs = Bare Metal Solution.

**References:**
- [cloud.google.com/bare-metal/docs/bms-overview](https://cloud.google.com/bare-metal/docs/bms-overview)
- [cloud.google.com/compute/docs/overview](https://cloud.google.com/compute/docs/overview)
- [cloud.google.com/run/docs/overview/what-is-cloud-run](https://cloud.google.com/run/docs/overview/what-is-cloud-run)

---

## Question 43

*Domain 6: Scaling with Google Cloud Operations*

**RideNest, a scooter rental mobile app, wants one fully managed place where its operations team can view the health of its Google Cloud infrastructure, create dashboards, configure alerts, and run uptime checks for customer-facing services. Which Google Cloud service should RideNest use?**

- [ ] A. Cloud Trace
- [x] B. Cloud Monitoring
- [ ] C. Cloud Logging
- [ ] D. Cloud Profiler

### Explanation

**Correct answer: B. Cloud Monitoring**

Cloud Monitoring collects metrics on the health and performance of infrastructure and services. It provides dashboards, alerting policies and uptime checks in one managed place. The clues are "dashboards, configure alerts, and run uptime checks".

**Why the others are wrong:**
- **A. Cloud Trace**: it tracks request latency across services; it is not the main dashboard and alerting tool.
- **C. Cloud Logging**: it collects and searches logs; metrics, dashboards and uptime checks belong to Cloud Monitoring.
- **D. Cloud Profiler**: it analyzes CPU and memory use in code to find inefficient functions.

**Remember:** Metrics, dashboards, alerts and uptime checks = Cloud Monitoring. Logs = Cloud Logging. Latency of requests = Cloud Trace.

**References:**
- [docs.cloud.google.com/monitoring/docs/monitoring-overview](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)
- [docs.cloud.google.com/monitoring/uptime-checks](https://docs.cloud.google.com/monitoring/uptime-checks)
- [docs.cloud.google.com/trace/docs/overview](https://docs.cloud.google.com/trace/docs/overview)

---

## Question 44

*Domain 2: Exploring Data Transformation with Google Cloud*

**StreamWagon is a media analytics company that processes clickstream and viewing-history data with Apache Spark. Its data engineers are spending too much time provisioning clusters, adjusting cluster sizes, and handling Spark infrastructure operations. The team wants a fully managed, serverless Spark environment on Google Cloud so they can submit Spark jobs and focus mainly on application code. Which service best meets this requirement?**

- [ ] A. Managed Service for Apache Spark managed clusters
- [x] B. Managed Service for Apache Spark serverless
- [ ] C. BigQuery
- [ ] D. Cloud Data Fusion

### Explanation

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

---

## Question 45

*Domain 6: Scaling with Google Cloud Operations*

**MetroPay, a mobile wallet company, notices that one of its payment-status services often makes users wait a long time before showing the final result. According to Google’s Four Golden Signals, which signal should the operations team monitor to measure this part of the service’s performance?**

- [ ] A. Saturation
- [ ] B. Errors
- [x] C. Latency
- [ ] D. Traffic

### Explanation

**Correct answer: C. Latency**

Latency is the time it takes to serve a request. Users waiting a long time for the payment status to appear is a latency problem. The Four Golden Signals from Google's SRE practice are latency, traffic, errors and saturation.

**Why the others are wrong:**
- **A. Saturation**: saturation measures how full the system is (CPU, memory, capacity).
- **B. Errors**: errors measure the rate of failed requests, not slow ones.
- **D. Traffic**: traffic measures demand, such as requests per second.

**Remember:** Slow = latency. Busy = traffic. Failing = errors. Full = saturation.

**References:**
- [sre.google/sre-book/monitoring-distributed-systems](https://sre.google/sre-book/monitoring-distributed-systems)
- [docs.cloud.google.com/application-design-center/docs/monitor-applications](https://docs.cloud.google.com/application-design-center/docs/monitor-applications)
- [docs.cloud.google.com/endpoints/docs/openapi/monitoring-your-api](https://docs.cloud.google.com/endpoints/docs/openapi/monitoring-your-api)

---

## Question 46

*Domain 5: Trust and Security with Google Cloud*

**BluePeak Insurance is reviewing Google Cloud’s advanced security capabilities after a series of industry-wide cyber incidents. The CISO wants to highlight the organization within Google Cloud that is known for intelligence gathered from hands-on incident response work during major cyberattacks across the world. Which organization provides this type of frontline threat intelligence?**

- [ ] A. VirusTotal
- [x] B. Mandiant
- [ ] C. Google Distributed Cloud
- [ ] D. Looker

### Explanation

**Correct answer: B. Mandiant**

Mandiant, part of Google Cloud, is known for frontline threat intelligence. It gathers this from hands-on incident response to major cyberattacks around the world. The clue is "intelligence gathered from hands-on incident response work".

**Why the others are wrong:**
- **A. VirusTotal**: VirusTotal provides crowdsourced scanning of files and URLs, not frontline incident-response intelligence.
- **C. Google Distributed Cloud**: it extends Google Cloud infrastructure to edge and on-premises locations; it is not a threat intelligence group.
- **D. Looker**: Looker is a business intelligence tool.

**Remember:** Frontline incident-response experts and intelligence = Mandiant. Crowdsourced file and URL scanning = VirusTotal.

**References:**
- [cloud.google.com/security/mandiant](https://cloud.google.com/security/mandiant)
- [cloud.google.com/security/consulting/mandiant-incident-response-services](https://cloud.google.com/security/consulting/mandiant-incident-response-services)
- [cloud.google.com/security/consulting/threat-intelligence-services](https://cloud.google.com/security/consulting/threat-intelligence-services)

---

## Question 47

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**FitTrackly, a fitness coaching website, has a small development team that built a web application packaged as one container image. The team wants to deploy it with minimal infrastructure management, automatic scaling, and a serverless hosting experience. Which Google Cloud service should FitTrackly use?**

- [ ] A. Compute Engine
- [ ] B. App Engine
- [ ] C. Google Kubernetes Engine
- [x] D. Cloud Run

### Explanation

**Correct answer: D. Cloud Run**

Cloud Run is a serverless platform that runs container images. It scales automatically, including to zero, and the team does not manage servers or clusters. The clues are "packaged as one container image", "minimal infrastructure management" and "serverless".

**Why the others are wrong:**
- **A. Compute Engine**: VMs require managing the OS and scaling setup.
- **B. App Engine**: App Engine is serverless, but it is code-centric; for an existing container image Cloud Run is the direct fit.
- **C. Google Kubernetes Engine**: GKE runs containers but involves cluster management, more than a small team needs.

**Remember:** Container image + serverless + autoscaling = Cloud Run.

**References:**
- [docs.cloud.google.com/run/docs](https://docs.cloud.google.com/run/docs)
- [docs.cloud.google.com/run/docs/overview/what-is-cloud-run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)
- [docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)

---

## Question 48

*Domain 2: Exploring Data Transformation with Google Cloud*

**RiverPay, a digital payments company, collects transaction records from customers in several regions. The analytics team wants a serverless data warehouse that can store large datasets, run fast SQL-based analysis, and support intelligent analytics without managing servers. Which Google Cloud product or service should RiverPay use?**

- [ ] A. Cloud Spanner
- [ ] B. Compute Engine
- [x] C. BigQuery
- [ ] D. Dataflow

### Explanation

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

---

## Question 49

*Domain 5: Trust and Security with Google Cloud*

**RiverBox Media, a video streaming company, is migrating several internal applications from its private data center to Google Cloud by using Compute Engine virtual machines. The security team is reviewing the Shared Responsibility Model to understand which security duties will move from RiverBox Media to Google Cloud when using Infrastructure as a Service. Which responsibility is inherently handled by Google Cloud?**

- [x] A. Physical security of the data center facilities
- [ ] B. Managing application-level user access
- [ ] C. Encrypting sensitive data within the application
- [ ] D. Applying operating system patches to virtual machines

### Explanation

**Correct answer: A. Physical security of the data center facilities**

Under the shared responsibility model, Google always secures the physical infrastructure: buildings, hardware and the underlying network. With IaaS (Compute Engine), the customer still manages the guest OS, applications, data and user access. The clue is "inherently handled by Google Cloud" with IaaS.

**Why the others are wrong:**
- **B. Managing application-level user access**: the customer controls who can use its applications.
- **C. Encrypting sensitive data within the application**: Google encrypts data at rest by default, but application-level encryption is the customer's job.
- **D. Applying OS patches to VMs**: with IaaS the customer manages the guest operating system, including patches.

**Remember:** IaaS: Google secures the physical layer; you secure the OS, apps, data and access.

**References:**
- [docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate)
- [docs.cloud.google.com/docs/security/overview/whitepaper](https://docs.cloud.google.com/docs/security/overview/whitepaper)
- [docs.cloud.google.com/architecture/regional-deployment-compute-engine](https://docs.cloud.google.com/architecture/regional-deployment-compute-engine)

---

## Question 50

*Domain 6: Scaling with Google Cloud Operations*

**BrightRide, a ride-sharing mobile app, has set an availability service level objective (SLO) of 99.999% for its customer booking service. Based on this “five nines” availability target, approximately how much downtime can riders experience in one year?**

- [x] A. 5 minutes
- [ ] B. 500 minutes
- [ ] C. 5 hours
- [ ] D. 5 days

### Explanation

**Correct answer: A. 5 minutes**

99.999% availability allows 0.001% downtime. A year has about 525,600 minutes, and 0.001% of that is about 5.26 minutes. So "five nines" means roughly 5 minutes of downtime per year.

**Why the others are wrong:**
- **B. 500 minutes**: about 500 minutes (roughly 8.3 hours) per year is closer to 99.9% availability.
- **C. 5 hours**: this is far more than five nines allows; it is between 99.9% and 99.99%.
- **D. 5 days**: this would be about 98.6% availability.

**Remember:** 99.9% ≈ 8.8 hours/year, 99.99% ≈ 53 minutes/year, 99.999% ≈ 5 minutes/year.

**References:**
- [sre.google/sre-book/availability-table](https://sre.google/sre-book/availability-table)
- [sre.google/sre-book/service-level-objectives](https://sre.google/sre-book/service-level-objectives)
- [cloud.google.com/monitoring/slo-monitoring](https://cloud.google.com/monitoring/slo-monitoring)

---
