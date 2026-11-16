# Cloud Digital Leader — Practice Exam 2

50 questions.

## Question 1

*Domain 1: Digital Transformation with Google Cloud*

**TalentHive HR wants to use an online payroll and employee benefits application provided by a cloud vendor. The company does not want to manage servers, install platform software, or develop the application code itself. Which cloud service model does this represent?**

- [ ] A. Infrastructure as a service
- [ ] B. Platform as a service
- [x] C. Software as a service
- [ ] D. Functions as a service

### Explanation

**Correct answer: C. Software as a service**

TalentHive uses a finished application from a vendor. It does not manage servers, platform software, or code. In SaaS the provider runs everything, and the customer just uses the app and manages its own data and users. The clue is "does not want to … develop the application code itself".

**Why the others are wrong:**
- **A. Infrastructure as a service**: IaaS gives you virtual machines and networks, and you still manage the OS, platform, and app.
- **B. Platform as a service**: PaaS removes server management, but you still write and deploy your own application code.
- **D. Functions as a service**: FaaS runs code you write in response to events; TalentHive wants a ready-made app, not code.

**Remember:** Ready-made app you just log in to = SaaS; your code on managed platform = PaaS; your VMs = IaaS.

**References:**
- [cloud.google.com/learn/what-is-saas](https://cloud.google.com/learn/what-is-saas)
- [cloud.google.com/learn/what-is-paas](https://cloud.google.com/learn/what-is-paas)
- [cloud.google.com/learn/what-is-iaas](https://cloud.google.com/learn/what-is-iaas)

---

## Question 2

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**MetroTrail, a public transport route-planning app, wants its engineering teams to make existing backend services easier to expose, manage, secure, and reuse as APIs in upcoming web and mobile projects. Which Google product or solution should MetroTrail use?**

- [ ] A. Application migration
- [x] B. Apigee
- [ ] C. The App Engine flexible environment
- [ ] D. AppSheet

### Explanation

**Correct answer: B. Apigee**

Apigee is Google Cloud's API management platform. It lets teams publish existing backend services as APIs and then secure, monitor, manage, and reuse them across web and mobile apps. The clue is "expose, manage, secure, and reuse as APIs".

**Why the others are wrong:**
- **A. Application migration**: Migration moves workloads to the cloud; it does not manage APIs.
- **C. The App Engine flexible environment**: App Engine hosts application code; it is not an API management layer.
- **D. AppSheet**: AppSheet is a no-code app builder for business users, not a tool for managing APIs.

**Remember:** Expose, secure, and manage APIs → Apigee.

**References:**
- [docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)
- [cloud.google.com/apigee](https://cloud.google.com/apigee)
- [docs.cloud.google.com/appengine/docs/flexible/overview](https://docs.cloud.google.com/appengine/docs/flexible/overview)

---

## Question 3

*Domain 1: Digital Transformation with Google Cloud*

**RidePulse, a bike-sharing mobile app, is gaining users faster than expected. Its main application still runs on older company-owned infrastructure, and the operations team is finding it difficult and expensive to scale capacity for traffic spikes. What might be limiting RidePulse’s ability to keep up with application growth?**

- [ ] A. The time it takes their serverless compute function to scale
- [ ] B. The overreliance on platform as a service
- [ ] C. The inaccessibility of their data due to perimeter security
- [x] D. The cost of provisioning hardware for peak usage

### Explanation

**Correct answer: D. The cost of provisioning hardware for peak usage**

With on-premises infrastructure, a company must buy and install enough hardware for its highest traffic peak. That is slow and expensive, and the extra capacity sits idle the rest of the time. The clue is "older company-owned infrastructure" that is "difficult and expensive to scale". Cloud solves this with on-demand, elastic capacity.

**Why the others are wrong:**
- **A. Serverless scaling time**: RidePulse is not using serverless; its app runs on its own hardware.
- **B. Overreliance on platform as a service**: PaaS is a cloud model, and RidePulse still runs on company-owned infrastructure.
- **C. Data inaccessible due to perimeter security**: Security design does not explain why capacity is hard and expensive to scale.

**Remember:** On-premises = buy for the peak in advance; cloud = scale on demand and pay for what you use.

**References:**
- [cloud.google.com/learn/what-is-cloud-computing](https://cloud.google.com/learn/what-is-cloud-computing)
- [docs.cloud.google.com/architecture/migration-to-google-cloud-best-practices](https://docs.cloud.google.com/architecture/migration-to-google-cloud-best-practices)
- [cloud.google.com/solutions/serverless](https://cloud.google.com/solutions/serverless)

---

## Question 4

*Domain 1: Digital Transformation with Google Cloud*

**FreshBite Logistics has moved its inventory tracking system from its private data center to Google Cloud. The finance team wants to understand how this migration changes the way infrastructure spending is managed. How has cost management primarily been affected?**

- [x] A. Costs will primarily shift from CapEx to OpEx.
- [ ] B. Costs will primarily shift from OpEx to CapEx.
- [ ] C. Cost management will stay the same, but the total cost of ownership (TCO) will be lower.
- [ ] D. Cost management will stay the same, but the total cost of ownership (TCO) will be higher.

### Explanation

**Correct answer: A. Costs will primarily shift from CapEx to OpEx.**

In a private data center, the company buys servers and buildings up front, which is capital expenditure (CapEx). In the cloud, it pays for resources as it uses them, which is operating expenditure (OpEx). The question asks how the way spending is managed changes, and the main change is this shift to pay-as-you-go.

**Why the others are wrong:**
- **B. OpEx to CapEx**: This is the reverse; moving to the cloud reduces up-front capital purchases.
- **C. Same management, lower TCO**: TCO may drop, but cost management does change: from buying assets to paying for usage.
- **D. Same management, higher TCO**: Cost management changes, and the cloud is not assumed to raise TCO.

**Remember:** Moving to the cloud = CapEx (buy up front) becomes OpEx (pay as you go).

**References:**
- [cloud.google.com/learn/cloud-migration](https://cloud.google.com/learn/cloud-migration)
- [docs.cloud.google.com/architecture/framework/cost-optimization](https://docs.cloud.google.com/architecture/framework/cost-optimization)
- [docs.cloud.google.com/migration-center/docs/generate-tco-report](https://docs.cloud.google.com/migration-center/docs/generate-tco-report)

---

## Question 5

*Domain 2: Exploring Data Transformation with Google Cloud*

**HealthVista Insights is building a company-wide analytics portal for teams that use data platforms across Google Cloud, AWS, and Azure. The organization wants an enterprise business intelligence solution that can model, explore, visualize, and query data across these different cloud environments without being tied to only one provider. Which Google Cloud product should they choose?**

- [x] A. Looker
- [ ] B. Compute Engine
- [ ] C. Cloud Spanner
- [ ] D. Spot VMs

### Explanation

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

---

## Question 6

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**BrightBee, an online tutoring website, wants to train a custom machine learning model that can sort short customer messages from its support form into categories such as billing, course feedback, technical issue, and tutor request. Which Google Cloud product or service should BrightBee use?**

- [ ] A. Google Distributed Cloud
- [ ] B. Recommendations from Agent Search
- [x] C. AutoML Natural Language
- [ ] D. Pub/Sub

### Explanation

**Correct answer: C. AutoML Natural Language**

BrightBee wants a custom model that sorts short text messages into its own categories. AutoML Natural Language trains a custom text classification model from labeled examples without deep ML expertise. The clues are "custom machine learning model", "short customer messages" (text), and "categories".

**Why the others are wrong:**
- **A. Google Distributed Cloud**: This runs Google Cloud infrastructure in your own locations or at the edge; it is not an ML tool.
- **B. Recommendations from Agent Search**: This recommends products or content to users; it does not classify support messages.
- **D. Pub/Sub**: Pub/Sub is a messaging service for moving events, not for training models.

**Remember:** Custom categories + your own labeled text + little ML expertise → AutoML for text.

**References:**
- [docs.cloud.google.com/natural-language/docs](https://docs.cloud.google.com/natural-language/docs)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training-overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training-overview)
- [docs.cloud.google.com/pubsub/docs/overview](https://docs.cloud.google.com/pubsub/docs/overview)

**⚠️ Note:** "AutoML Natural Language" is an older standalone product name. Today AutoML is part of the AI platform (Gemini Enterprise Agent Platform, formerly Vertex AI), and Google also steers text classification toward tuning Gemini models. The idea is still right, so pick the keyed answer on this exam.

---

## Question 7

*Domain 1: Digital Transformation with Google Cloud*

**CityPetCare, a veterinary appointment website, decides to launch a mobile app so pet owners can check appointment details, vaccination reminders, and service updates while they are away from their computers. What business reason most likely led CityPetCare to create the mobile app?**

- [x] A. Customers expect service information to be simple to access from any device.
- [ ] B. Customers expect cloud-based information to be available only through mobile devices.
- [ ] C. Developers can make customer data more secure only by using a mobile app.
- [ ] D. Developers can test different versions of the service only through a mobile app.

### Explanation

**Correct answer: A. Customers expect service information to be simple to access from any device.**

Modern customers expect to reach services anytime, anywhere, on whatever device they have. A mobile app lets pet owners see appointments and reminders while away from their computers. The clue is "while they are away from their computers".

**Why the others are wrong:**
- **B. Only through mobile devices**: Customers want access from any device, not only mobile; the website still exists.
- **C. Only a mobile app makes data secure**: Security does not depend on using a mobile app.
- **D. Testing only through a mobile app**: Developers can test versions on many platforms, and testing is not the business reason here.

**Remember:** Customer expectations drive transformation: access anywhere, on any device.

**References:**
- [cloud.google.com/learn/what-is-digital-transformation](https://cloud.google.com/learn/what-is-digital-transformation)
- [cloud.google.com/learn/what-is-cloud-computing](https://cloud.google.com/learn/what-is-cloud-computing)
- [docs.cloud.google.com/architecture/framework/security/security-principles](https://docs.cloud.google.com/architecture/framework/security/security-principles)

---

## Question 8

*Domain 2: Exploring Data Transformation with Google Cloud*

**FreshCart, an online grocery delivery website, wants managers and analysts to explore sales trends, build dashboards, understand customer behavior, and make better business decisions from company data. How would FreshCart benefit from using Looker?**

- [ ] A. Optimal identity and access management
- [ ] B. Leading serverless warehousing technology
- [ ] C. Robust data roll-back accuracy
- [x] D. Advanced business intelligence and analytics

### Explanation

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

---

## Question 9

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**BrightCart is adding a small order-notification feature to its shopping app. The development team wants to write the function code and let Google Cloud manage server provisioning, scaling, patching, and runtime infrastructure. Which infrastructure solution should BrightCart use?**

- [ ] A. Virtual machines
- [ ] B. Bare Metal Solution
- [x] C. Serverless computing
- [ ] D. Artifact Registry

### Explanation

**Correct answer: C. Serverless computing**

In serverless computing, developers write the code and Google Cloud handles servers, scaling, patching, and the runtime. A small event-driven feature like an order notification is a classic fit. The clue is "write the function code and let Google Cloud manage" everything else.

**Why the others are wrong:**
- **A. Virtual machines**: With VMs, the team still manages the operating system, patching, and scaling.
- **B. Bare Metal Solution**: Bare Metal gives dedicated physical servers for special workloads, with the most management work.
- **D. Artifact Registry**: Artifact Registry stores container images and packages; it does not run code.

**Remember:** "Just write the code, no servers to manage" → serverless.

**References:**
- [cloud.google.com/serverless](https://cloud.google.com/serverless)
- [cloud.google.com/run/docs](https://cloud.google.com/run/docs)
- [cloud.google.com/artifact-registry/docs](https://cloud.google.com/artifact-registry/docs)

---

## Question 10

*Domain 6: Scaling with Google Cloud Operations*

**PixovaPay, a digital payments website, is adopting Google’s Site Reliability Engineering practices to improve reliability for its transaction service. The operations team wants to know which concept is used as a direct measurement of how the service is actually performing. Which concept should they use?**

- [ ] A. Service-level agreement
- [x] B. Service-level indicator
- [ ] C. Error reporting
- [ ] D. Service-level objective

### Explanation

**Correct answer: B. Service-level indicator**

A service-level indicator (SLI) is a direct, measured value of how the service is performing, such as the percentage of successful requests or request latency. The SLO is the target for that SLI, and the SLA is the contract with customers. The clue is "direct measurement".

**Why the others are wrong:**
- **A. Service-level agreement**: An SLA is a contract with customers that includes consequences if targets are missed; it is not a measurement.
- **C. Error reporting**: Error reporting groups and shows application errors; it is a tool, not the SRE measurement concept.
- **D. Service-level objective**: An SLO is the target value for an SLI, not the measurement itself.

**Remember:** SLI = what you measure; SLO = the goal; SLA = the promise with penalties.

**References:**
- [sre.google/sre-book/service-level-objectives](https://sre.google/sre-book/service-level-objectives)
- [docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
- [cloud.google.com/blog/products/devops-sre/sre-fundamentals-sli-vs-slo-vs-sla](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-sli-vs-slo-vs-sla)

---

## Question 11

*Domain 6: Scaling with Google Cloud Operations*

**QuickKart, an online grocery delivery platform, is moving several application teams to Google Cloud. The finance team notices that different engineering teams can create cloud resources as needed, and monthly costs change based on actual usage. What is the typical cloud spending behavior for most organizations?**

- [x] A. Decentralized and variable
- [ ] B. Centralized and variable
- [ ] C. Decentralized and fixed
- [ ] D. Centralized and fixed

### Explanation

**Correct answer: A. Decentralized and variable**

In the cloud, many teams can create resources themselves, so spending decisions are spread out (decentralized). Bills also change month to month with actual usage (variable). The stem describes both: teams create resources "as needed" and costs "change based on actual usage".

**Why the others are wrong:**
- **B. Centralized and variable**: Spending is not controlled by one central team when many teams create resources.
- **C. Decentralized and fixed**: Usage-based billing means costs are not fixed.
- **D. Centralized and fixed**: This describes traditional on-premises budgeting, not the cloud.

**Remember:** Cloud spending = decentralized and variable; that is why FinOps and cost controls matter.

**References:**
- [cloud.google.com/cost-management](https://cloud.google.com/cost-management)
- [docs.cloud.google.com/docs/costs-usage](https://docs.cloud.google.com/docs/costs-usage)
- [docs.cloud.google.com/architecture/framework/cost-optimization](https://docs.cloud.google.com/architecture/framework/cost-optimization)

---

## Question 12

*Domain 2: Exploring Data Transformation with Google Cloud*

**BrightShelf, an online bookstore, keeps a large collection of product images, sales reports, and historical order exports. The team frequently reads only the latest files, while older files are accessed rarely. BrightShelf wants to lower storage costs by keeping less-used data in Nearline storage, Coldline storage, and Archive storage. Which Google Cloud product should BrightShelf use?**

- [ ] A. Filestore
- [x] B. Cloud Storage
- [ ] C. Knowledge Catalog
- [ ] D. Spanner

### Explanation

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

---

## Question 13

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**CareNest, a healthcare appointment support website, receives thousands of patient questions through chat and phone every week. The support team wants to handle common requests more efficiently while still keeping conversations personalized and helpful for each patient. Which Google Cloud product or service should CareNest use?**

- [ ] A. Recommendations AI
- [ ] B. Cloud Identity
- [x] C. Contact Center AI Platform
- [ ] D. Cloud Text-to-Speech

### Explanation

**Correct answer: C. Contact Center AI Platform**

Contact Center AI Platform is Google's customer-service solution. Virtual agents handle common requests automatically, and AI helps human agents resolve the rest, while keeping conversations personal. The clues are "chat and phone", "common requests more efficiently", and "personalized".

**Why the others are wrong:**
- **A. Recommendations AI**: This suggests products to shoppers; it does not handle support conversations.
- **B. Cloud Identity**: Cloud Identity manages users and sign-in, not customer conversations.
- **D. Cloud Text-to-Speech**: Text-to-Speech only turns text into spoken audio; it is one building block, not a full contact center solution.

**Remember:** High-volume customer chats and calls → Contact Center AI.

**References:**
- [cloud.google.com/solutions/contact-center-ai-platform](https://cloud.google.com/solutions/contact-center-ai-platform)
- [docs.cloud.google.com/contact-center/ccai-platform/docs](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
- [docs.cloud.google.com/text-to-speech/docs](https://docs.cloud.google.com/text-to-speech/docs)

---

## Question 14

*Domain 2: Exploring Data Transformation with Google Cloud*

**TravelNest Analytics stores booking history in BigQuery on Google Cloud, while its partner clickstream files remain in object storage in another large public cloud. The analytics team wants to run SQL-based analysis across both locations without first copying all partner data into Google Cloud. Which multicloud product should they choose?**

- [ ] A. AlloyDB Omni
- [ ] B. Cloud SQL
- [x] C. BigQuery Omni
- [ ] D. Cloud Run functions

### Explanation

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

---

## Question 15

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**UrbanPedal, a bike-sharing company, operates smart docking stations across several cities. They store rider activity, station usage, and repair history in BigQuery. They want to maintain their docking stations more efficiently, reduce unnecessary part replacements, and support their sustainability goals. How can Google Cloud services help UrbanPedal?**

- [ ] A. Secure data access by using Identity and Access Management.
- [ ] B. Provide access to third-party developers by creating an API using Apigee.
- [x] C. Create a model in BigQuery to predict future maintenance schedules.
- [ ] D. Move data from BigQuery to Cloud Storage to reduce storage costs.

### Explanation

**Correct answer: C. Create a model in BigQuery to predict future maintenance schedules.**

UrbanPedal already keeps usage and repair history in BigQuery. With BigQuery ML it can build a predictive maintenance model right where the data lives. Servicing stations only when needed cuts waste and supports sustainability. The clues are "maintain more efficiently" and "reduce unnecessary part replacements".

**Why the others are wrong:**
- **A. Secure data with IAM**: IAM controls access, but it does not make maintenance more efficient.
- **B. Create an API with Apigee**: Sharing data with outside developers does not predict maintenance needs.
- **D. Move data to Cloud Storage**: Moving data may lower storage costs, but it does nothing for maintenance planning.

**Remember:** Historical data + "predict" + data already in BigQuery → build an ML model in BigQuery.

**References:**
- [cloud.google.com/bigquery/docs/bqml-introduction](https://cloud.google.com/bigquery/docs/bqml-introduction)
- [cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create)
- [cloud.google.com/apigee/docs/api-platform/get-started/what-apigee](https://cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)

---

## Question 16

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**BrightCart is preparing to release a container-based shopping assistant service. The team is unsure whether the service will receive 500 users or 50,000 users during launch week. They also want to avoid paying for compute capacity when no users are actively using the service. Which benefit of serverless computing best addresses this requirement?**

- [ ] A. Disaster recovery
- [ ] B. Reduced development costs
- [x] C. Scalability
- [ ] D. Built-in security

### Explanation

**Correct answer: C. Scalability**

Serverless platforms scale automatically with demand, from zero users to many thousands, without the team planning capacity. Because they can scale down to zero, BrightCart does not pay for idle capacity. The clue is the uncertain demand: "500 users or 50,000 users".

**Why the others are wrong:**
- **A. Disaster recovery**: Recovery from outages is not the issue; unpredictable traffic is.
- **B. Reduced development costs**: Serverless can save effort, but the stem is about handling changing user load.
- **D. Built-in security**: Security is a benefit of managed platforms, but it does not address variable demand.

**Remember:** Unknown or spiky traffic on serverless → automatic scaling (up and down to zero).

**References:**
- [cloud.google.com/serverless](https://cloud.google.com/serverless)
- [docs.cloud.google.com/run/docs/overview/what-is-cloud-run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)
- [cloud.google.com/run/pricing](https://cloud.google.com/run/pricing)

**⚠️ Note:** "Avoid paying when no users are active" is really a pay-per-use cost benefit (scale to zero). Scalability is still the best of the four options, so pick the keyed answer.

---

## Question 17

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**FitRoute, a fitness class booking app, wants to create a machine learning model to predict member attendance trends for the next 18 months. The company has four years of attendance records from 220 studios, but each studio exported its data using different column names, date formats, and file structures. FitRoute must prepare the data before training the model. What should they do?**

- [ ] A. Use only the most recent 10 months of data so the model has fewer inconsistencies to process.
- [x] B. Transform the data into a consistent format.
- [ ] C. Group the records by file format and train a separate model for each group.
- [ ] D. Select a machine learning model type that can automatically process all different input formats.

### Explanation

**Correct answer: B. Transform the data into a consistent format.**

Machine learning needs clean, consistent data. When 220 studios use different column names, date formats, and file structures, the first step is to standardize the data into one format. Then the full four years of history can be used to train one good model. The clue is "must prepare the data before training".

**Why the others are wrong:**
- **A. Use only the last 10 months**: Throwing away most of the history weakens an 18-month forecast and does not fix the format problem.
- **C. Separate model per file format**: This splits the data into weaker models and does not solve inconsistent columns or dates.
- **D. Model that handles any format**: No model type automatically fixes messy, inconsistent input; data preparation is still needed.

**Remember:** Good ML starts with clean, consistent data: prepare and standardize first.

**References:**
- [docs.cloud.google.com/bigquery/docs/preprocess-overview](https://docs.cloud.google.com/bigquery/docs/preprocess-overview)
- [docs.cloud.google.com/dataflow/docs/machine-learning/ml-preprocess-data](https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-preprocess-data)
- [docs.cloud.google.com/architecture/ml-on-gcp-best-practices](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices)

---

## Question 18

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**PhotoDrop, a media-sharing startup, wants to run small pieces of application logic whenever users upload image files to Cloud Storage. The developers want these pieces of code to be event-driven and serverless, and they do not want to manage virtual machines or runtime infrastructure. Which Google Cloud product should they use?**

- [ ] A. Compute Engine
- [x] B. Cloud Run functions
- [ ] C. Bare Metal Solution
- [ ] D. Spot VMs

### Explanation

**Correct answer: B. Cloud Run functions**

Cloud Run functions (formerly Cloud Functions) run small pieces of code in response to events, such as a file upload to Cloud Storage. They are serverless, so there are no VMs or runtime to manage. The clues are "small pieces of application logic", "whenever users upload", and "event-driven and serverless".

**Why the others are wrong:**
- **A. Compute Engine**: Compute Engine is virtual machines, which the team would have to manage.
- **C. Bare Metal Solution**: Bare Metal is dedicated physical hardware, the opposite of serverless.
- **D. Spot VMs**: Spot VMs are discounted virtual machines; they are still VMs to manage.

**Remember:** Small code triggered by an event, no servers → Cloud Run functions.

**References:**
- [docs.cloud.google.com/functions/docs](https://docs.cloud.google.com/functions/docs)
- [docs.cloud.google.com/run/docs/tutorials/trigger-functions-storage](https://docs.cloud.google.com/run/docs/tutorials/trigger-functions-storage)
- [docs.cloud.google.com/compute/docs/instances/spot](https://docs.cloud.google.com/compute/docs/instances/spot)

---

## Question 19

*Domain 6: Scaling with Google Cloud Operations*

**ShopEase Media is organizing its Google Cloud environment for separate teams such as marketing, analytics, and payments. The cloud administrator wants to apply access rules once for the analytics team and have those rules automatically apply to every project created under the analytics group. How does the Google Cloud resource hierarchy help with this requirement?**

- [x] A. Policies can be applied at the folder level and are inherited by projects inside the folder.
- [ ] B. Projects in the resource hierarchy are not affected by security policies.
- [ ] C. Policies can only be applied at the organization level and affect all projects.
- [ ] D. Policies can only be applied to individual projects.

### Explanation

**Correct answer: A. Policies can be applied at the folder level and are inherited by projects inside the folder.**

The resource hierarchy is organization, then folders, then projects, then resources. Policies set on a folder are inherited by every project inside it, including new ones. So the admin sets access once on the analytics folder. The clue is "apply access rules once" and "automatically apply to every project".

**Why the others are wrong:**
- **B. Projects not affected by policies**: Projects inherit policies from their parents and can have their own.
- **C. Only at organization level**: Policies can be set at the organization, folder, project, or resource level.
- **D. Only on individual projects**: Setting policies project by project is possible, but it is not the only option and is what the admin wants to avoid.

**Remember:** Group projects in folders; policies flow down the hierarchy.

**References:**
- [docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)
- [docs.cloud.google.com/iam/docs/resource-hierarchy-access-control](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control)
- [docs.cloud.google.com/iam/docs/allow-policies](https://docs.cloud.google.com/iam/docs/allow-policies)

---

## Question 20

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**MarketNest, an online marketplace, runs containerized applications in Kubernetes clusters on Google Cloud, inside its private data center, and in another public cloud provider. The platform team wants one centralized way to manage these clusters, apply consistent security controls, and operate applications across all environments. Which Google Cloud service should they use?**

- [ ] A. Compute Engine
- [ ] B. Cloud Run
- [x] C. GKE Enterprise
- [ ] D. BigQuery Omni

### Explanation

**Correct answer: C. GKE Enterprise**

GKE Enterprise (formerly Anthos) gives one central way to manage Kubernetes clusters on Google Cloud, on-premises, and in other clouds. It applies consistent policies and security across all of them. The clues are "Kubernetes clusters" in three environments and "one centralized way to manage".

**Why the others are wrong:**
- **A. Compute Engine**: Compute Engine provides VMs on Google Cloud only; it does not manage clusters across environments.
- **B. Cloud Run**: Cloud Run runs containers serverlessly; it is not a fleet manager for clusters in many places.
- **D. BigQuery Omni**: BigQuery Omni is multicloud analytics, not container management.

**Remember:** Manage Kubernetes across hybrid and multicloud from one place → GKE Enterprise.

**References:**
- [docs.cloud.google.com/kubernetes-engine/enterprise/docs/deployment-options](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/deployment-options)
- [docs.cloud.google.com/kubernetes-engine/docs/fleets-overview](https://docs.cloud.google.com/kubernetes-engine/docs/fleets-overview)
- [docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)

---

## Question 21

*Domain 2: Exploring Data Transformation with Google Cloud*

**CarePulse, a preventive healthcare mobile app, wants to monitor patient wellness more efficiently. The company needs a way to automatically collect health measurements such as heart rate, activity level, sleep patterns, and other patient signals without requiring patients or staff to manually enter the data. What should CarePulse encourage patients to do?**

- [ ] A. Use at-home health screening devices and then upload their health data every evening
- [x] B. Wear Internet of Things (IoT) devices that upload their health data in real time
- [ ] C. Self-assess their health data and then document and upload it in real time
- [ ] D. Visit a clinic assistant who will use Internet of Things (IoT) devices to collect and upload their health data

### Explanation

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

---

## Question 22

*Domain 1: Digital Transformation with Google Cloud*

**FitLoop, a fitness coaching startup, uses a cloud-based SaaS application to publish workout plans and nutrition tips for its subscribers. The SaaS provider manages the application platform and the infrastructure behind it. What is FitLoop exclusively responsible for?**

- [ ] A. Keeping the complete SaaS platform operational
- [x] B. Maintaining customer-facing content
- [ ] C. Monitoring data center servers
- [ ] D. Monitoring underlying computer networks

### Explanation

**Correct answer: B. Maintaining customer-facing content**

In SaaS, the provider runs the application, platform, servers, and networks. The customer is still responsible for its own data and content, such as the workout plans and tips FitLoop publishes. This is the shared responsibility model.

**Why the others are wrong:**
- **A. Keeping the SaaS platform operational**: Running the platform is the SaaS provider's job.
- **C. Monitoring data center servers**: The provider manages the physical servers.
- **D. Monitoring computer networks**: Underlying networks are also managed by the provider.

**Remember:** In SaaS, the customer always owns its data, content, and user access.

**References:**
- [cloud.google.com/learn/paas-vs-iaas-vs-saas](https://cloud.google.com/learn/paas-vs-iaas-vs-saas)
- [docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate)
- [cloud.google.com/learn/what-is-cloud-security](https://cloud.google.com/learn/what-is-cloud-security)

---

## Question 23

*Domain 2: Exploring Data Transformation with Google Cloud*

**FreshCart Analytics wants to create a managed data pipeline that processes and transforms sales and inventory data before loading it into a data warehouse for reconciliation. The pipeline must scale automatically as data volume grows and should require minimal operational management. Which Google Cloud product or service should FreshCart Analytics choose?**

- [ ] A. Cloud Bigtable
- [ ] B. Cloud Storage
- [ ] C. Pub/Sub
- [x] D. Dataflow

### Explanation

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

---

## Question 24

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**EduCore Apps manages several internal learning platforms for schools. Its IT team spends most of each week installing operating system patches, upgrading application components, and setting up database servers. The leadership team wants developers to move faster by having Google Cloud take over more of these infrastructure administration tasks. Which cloud computing approach does this describe?**

- [ ] A. On-premises hosting
- [x] B. Adopting managed services
- [ ] C. Bare metal provisioning
- [ ] D. Edge computing

### Explanation

**Correct answer: B. Adopting managed services**

With managed services, Google Cloud takes over routine admin work such as OS patching, upgrades, and database setup. Developers can then spend their time on building features. The clue is "having Google Cloud take over more of these infrastructure administration tasks".

**Why the others are wrong:**
- **A. On-premises hosting**: On-premises keeps all of this work with the IT team.
- **C. Bare metal provisioning**: Bare metal servers leave even more management to the customer.
- **D. Edge computing**: Edge computing moves processing closer to users or devices; it does not reduce admin work.

**Remember:** Less patching and maintenance, more time for innovation → managed services.

**References:**
- [docs.cloud.google.com/sql/docs/introduction](https://docs.cloud.google.com/sql/docs/introduction)
- [docs.cloud.google.com/sql/docs](https://docs.cloud.google.com/sql/docs)
- [cloud.google.com/products](https://cloud.google.com/products)

---

## Question 25

*Domain 2: Exploring Data Transformation with Google Cloud*

**GlobePay, a digital payments company, runs its application for customers in North America, Europe, and Asia. The company needs a highly available operational database that can keep transactional data consistent and available across multiple geographic regions. How would GlobePay benefit from managing its data with Cloud Spanner?**

- [ ] A. Cloud Spanner is optimized for cold storage
- [x] B. Cloud Spanner replicates data across regions in real time
- [ ] C. Cloud Spanner is optimized to ingest unstructured data
- [ ] D. Cloud Spanner visualizes and analyzes data in real time

### Explanation

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

---

## Question 26

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**RideLoop Mobility is replacing a large legacy ride-booking platform that is difficult to update and scale. The engineering team plans to divide the application into smaller independent services, where each service owns a specific business function and can be built, deployed, and scaled separately. Which modern architecture pattern are they adopting?**

- [ ] A. Monolithic architecture
- [x] B. Microservices
- [ ] C. Spot VM architecture
- [ ] D. Hardware virtualization

### Explanation

**Correct answer: B. Microservices**

Microservices architecture splits an application into small, independent services. Each one owns a business function and can be built, deployed, and scaled on its own. The stem describes exactly this.

**Why the others are wrong:**
- **A. Monolithic architecture**: A monolith is one large application, which is what RideLoop is moving away from.
- **C. Spot VM architecture**: Spot VMs are a low-cost compute option, not an architecture pattern.
- **D. Hardware virtualization**: Virtualization runs many VMs on one machine; it does not describe how an app is designed.

**Remember:** Small, independent, separately deployable services → microservices.

**References:**
- [cloud.google.com/learn/what-is-microservices-architecture](https://cloud.google.com/learn/what-is-microservices-architecture)
- [cloud.google.com/blog/topics/developers-practitioners/microservices-architecture-google-cloud](https://cloud.google.com/blog/topics/developers-practitioners/microservices-architecture-google-cloud)
- [docs.cloud.google.com/compute/docs/instances/spot](https://docs.cloud.google.com/compute/docs/instances/spot)

---

## Question 27

*Domain 2: Exploring Data Transformation with Google Cloud*

**HelpHive is a customer service platform that has added an AI support assistant to handle chats and voice calls. The assistant produces large volumes of text transcripts, call metadata, and speech-related files. Why should HelpHive use a cloud data warehouse such as BigQuery to understand this data?**

- [ ] A. To automatically display both text and speech data in live dashboards without extra tools
- [x] B. To store and analyze large volumes of structured and unstructured data at scale
- [ ] C. To encrypt network traffic between cloud resources and on-premises data centers
- [ ] D. To convert organized database records into unstructured text and audio files

### Explanation

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

---

## Question 28

*Domain 5: Trust and Security with Google Cloud*

**A payroll assistant at MetroKart receives an email that appears to come from the company’s salary portal. The message says their account will be suspended unless they reply with their bank account number and login password. Which cybersecurity threat is this?**

- [ ] A. Ransomware
- [ ] B. Distributed Denial of Service
- [ ] C. Spamming
- [x] D. Phishing

### Explanation

**Correct answer: D. Phishing**

Phishing is a fake message that pretends to come from a trusted source to trick people into giving away sensitive data like passwords or bank details. The clues are an email that "appears to come from the company’s salary portal" and a request to reply with login and bank details.

**Why the others are wrong:**
- **A. Ransomware**: Ransomware encrypts files and demands payment to unlock them.
- **B. Distributed Denial of Service**: DDoS floods a service with traffic to knock it offline.
- **C. Spamming**: Spam is unwanted bulk email; this message is a targeted attempt to steal credentials.

**Remember:** Fake trusted message asking for passwords or financial data → phishing.

**References:**
- [cisa.gov/secure-our-world/recognize-and-report-phishing](https://cisa.gov/secure-our-world/recognize-and-report-phishing)
- [support.microsoft.com/en-us/security/protect-yourself-from-phishing](https://support.microsoft.com/en-us/security/protect-yourself-from-phishing)
- [docs.cloud.google.com/web-risk/docs/overview](https://docs.cloud.google.com/web-risk/docs/overview)

---

## Question 29

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**RiverBank Plus, a digital banking company, notices that many customers stop using its savings and investment products each year. The company wants to use data and AI to predict which active customers are likely to leave, so the retention team can proactively offer better support, personalized discounts, or improved services. What should RiverBank Plus do?**

- [ ] A. Create a dashboard of customers who closed their accounts in the past, and manually look for visible patterns in the charts.
- [x] B. Create a ML model based on the demographics and activities of previous customers who closed their accounts.
- [ ] C. Create a survey for all customers to identify their current level of satisfaction.
- [ ] D. Create a report based on customer feedback collected during the previous year.

### Explanation

**Correct answer: B. Create a ML model based on the demographics and activities of previous customers who closed their accounts.**

Predicting which current customers will leave (churn) is a classic ML use case. A model learns patterns from past customers who left and then scores active customers by risk. The clues are "predict which active customers are likely to leave" and "proactively".

**Why the others are wrong:**
- **A. Dashboard and manual pattern search**: Dashboards look backward and manual review does not scale or predict individual risk.
- **C. Satisfaction survey**: Surveys show current opinions but do not predict who will leave, and many customers won't answer.
- **D. Report on last year's feedback**: A report describes the past; it does not predict future behavior.

**Remember:** "Predict" + historical examples of the outcome → train an ML model.

**References:**
- [cloud.google.com/learn/what-is-machine-learning](https://cloud.google.com/learn/what-is-machine-learning)
- [docs.cloud.google.com/bigquery/docs/reference-patterns](https://docs.cloud.google.com/bigquery/docs/reference-patterns)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/beginner/bqml](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/beginner/bqml)

---

## Question 30

*Domain 2: Exploring Data Transformation with Google Cloud*

**LumaCart is an online grocery marketplace that stores customer profiles, orders, and inventory records in Cloud SQL. The leadership team wants to use this operational data to understand sales trends and customer behavior. How does Cloud SQL help LumaCart create business insights?**

- [x] A. Integrates with business intelligence and analytics platforms
- [ ] B. Builds prediction outputs directly by running machine learning models
- [ ] C. Automatically creates live dashboards and intelligent charts
- [ ] D. Converts unstructured business files into relational tables

### Explanation

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

---

## Question 31

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**RideNest is moving several internal applications to Google Cloud and wants to use managed services wherever possible. The IT team wants to reduce the amount of routine infrastructure maintenance they perform themselves. Which task is typically handled automatically by a managed services platform?**

- [ ] A. Managing user access
- [x] B. Patching and upgrades
- [ ] C. Data archiving
- [ ] D. Cost optimization

### Explanation

**Correct answer: B. Patching and upgrades**

A managed service handles routine maintenance for you, such as applying security patches and software upgrades. This is the main way managed services cut infrastructure work. The clue is "routine infrastructure maintenance".

**Why the others are wrong:**
- **A. Managing user access**: Who can access what is the customer's responsibility, set with IAM.
- **C. Data archiving**: Deciding what to archive and when is a customer data decision.
- **D. Cost optimization**: Google offers tools and recommendations, but optimizing spending is the customer's job.

**Remember:** Managed service = provider does patching, upgrades, and maintenance; you own access and data.

**References:**
- [cloud.google.com/discover/what-is-managed-database-service](https://cloud.google.com/discover/what-is-managed-database-service)
- [docs.cloud.google.com/compute/vm-manager/docs/patch](https://docs.cloud.google.com/compute/vm-manager/docs/patch)
- [cloud.google.com/security/shared-responsibility-model](https://cloud.google.com/security/shared-responsibility-model)

---

## Question 32

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**StreamPilot, a video streaming app, is preparing to test a redesigned home page and a few recommendation features. The product team wants some users to access the new app version while other users continue using the existing version, so they can compare feedback before a full release. Why should StreamPilot use App Engine?**

- [ ] A. Because their app is containerized and enabled by microservices
- [ ] B. Because the updated app will only include new features
- [x] C. To run different versions of the app for different users
- [ ] D. To run different versions of the app for the same user

### Explanation

**Correct answer: C. To run different versions of the app for different users**

App Engine can run several versions of an app at once and split traffic between them. Some users see the new version while others keep the current one. This supports A/B testing and gradual rollouts. The clue is "some users … while other users".

**Why the others are wrong:**
- **A. Containerized and microservices**: Being containerized is not why App Engine is chosen here; the need is traffic splitting.
- **B. Only new features**: The update content is not the reason; the need is to compare two versions.
- **D. Different versions for the same user**: Traffic splitting sends different users to different versions, not one user to several.

**Remember:** App Engine traffic splitting → A/B tests and gradual rollouts across user groups.

**References:**
- [cloud.google.com/appengine/docs/standard/splitting-traffic](https://cloud.google.com/appengine/docs/standard/splitting-traffic)
- [cloud.google.com/appengine/docs/an-overview-of-app-engine](https://cloud.google.com/appengine/docs/an-overview-of-app-engine)
- [cloud.google.com/appengine/docs/standard/how-requests-are-routed](https://cloud.google.com/appengine/docs/standard/how-requests-are-routed)

---

## Question 33

*Domain 2: Exploring Data Transformation with Google Cloud*

**RideNest, a bike-sharing mobile app, collects trip records from its app, JSON logs from scooters, support chat transcripts, and maintenance images. The analytics team wants to keep all of this structured, semi-structured, and unstructured data together in its original format before deciding how to process it later. Which cloud data management solution should RideNest use?**

- [ ] A. Data field
- [x] B. Data lake
- [ ] C. Database
- [ ] D. Data warehouse

### Explanation

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

---

## Question 34

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**BrightCart Retail is moving its inventory application to Google Cloud. Instead of copying the existing virtual machines exactly as they are, the team chooses to replace the self-managed database layer with a managed Cloud SQL instance so database patching, backups, and maintenance require less manual work. The main application logic will remain mostly unchanged. Which migration path does this represent?**

- [ ] A. Rehost (Lift and shift)
- [x] B. Replatform (Move and improve)
- [ ] C. Retain
- [ ] D. Retire

### Explanation

**Correct answer: B. Replatform (Move and improve)**

Replatforming moves an app to the cloud and makes a few targeted improvements, like switching to a managed database, without rewriting the main code. Here BrightCart keeps its app logic but swaps a self-managed database for Cloud SQL. The clue is "main application logic will remain mostly unchanged" plus the database upgrade.

**Why the others are wrong:**
- **A. Rehost (Lift and shift)**: Rehost copies VMs as they are, with no improvements.
- **C. Retain**: Retain means keeping the app where it is for now.
- **D. Retire**: Retire means shutting the app down.

**Remember:** Copy as is = rehost; small improvements like managed services = replatform; rewrite = refactor.

**References:**
- [docs.cloud.google.com/architecture/migration-to-gcp-getting-started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started)
- [docs.cloud.google.com/migration-center/docs/migration-planning-overview](https://docs.cloud.google.com/migration-center/docs/migration-planning-overview)
- [docs.cloud.google.com/sql/docs/introduction](https://docs.cloud.google.com/sql/docs/introduction)

---

## Question 35

*Domain 5: Trust and Security with Google Cloud*

**FinSurely, a financial planning mobile app, runs workloads on Google Cloud and needs a central way to discover security weaknesses across its cloud resources and applications. The security team wants to identify risks, prioritize findings, and take remediation actions. Which Google Cloud service should FinSurely use?**

- [x] A. Security Command Center
- [ ] B. Google Cloud Armor
- [ ] C. Cloud Storage
- [ ] D. VPC networks

### Explanation

**Correct answer: A. Security Command Center**

Security Command Center is Google Cloud's central security and risk management service. It finds vulnerabilities and misconfigurations across your resources, helps prioritize findings, and supports remediation. The clues are "central way to discover security weaknesses" and "prioritize findings".

**Why the others are wrong:**
- **B. Google Cloud Armor**: Cloud Armor protects web apps from DDoS and web attacks; it does not inventory risks across resources.
- **C. Cloud Storage**: Cloud Storage stores objects; it is not a security tool.
- **D. VPC networks**: VPCs are private networks for your resources, not a risk discovery tool.

**Remember:** One central view of security risks and findings in Google Cloud → Security Command Center.

**References:**
- [docs.cloud.google.com/security-command-center/docs/security-command-center-overview](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)
- [docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings)
- [docs.cloud.google.com/armor/docs/cloud-armor-overview](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)

---

## Question 36

*Domain 6: Scaling with Google Cloud Operations*

**FitCart, an online fitness equipment store, plans to launch a new analytics workload on Google Cloud. The team needs a reliable estimate of the expected monthly cost before they deploy the workload. How should FitCart create this estimate?**

- [x] A. Use the Google Cloud Pricing Calculator.
- [ ] B. Deploy the workload in a test environment to observe costs.
- [ ] C. Use historical costs from an existing similar workload.
- [ ] D. Review pricing pages and manually calculate an estimate.

### Explanation

**Correct answer: A. Use the Google Cloud Pricing Calculator.**

The Google Cloud Pricing Calculator estimates monthly costs for planned services before you deploy them. You enter the products and expected usage and get an estimate. The clues are "estimate … before they deploy".

**Why the others are wrong:**
- **B. Deploy in test environment**: This costs money and time, and test usage may not match production.
- **C. Historical costs of a similar workload**: Another workload may differ in size and services, so the estimate is less reliable.
- **D. Manually calculate from pricing pages**: This is slow and easy to get wrong; the calculator does it for you.

**Remember:** Estimate cost before deploying → Pricing Calculator; track actual cost → billing reports and budgets.

**References:**
- [cloud.google.com/products/calculator](https://cloud.google.com/products/calculator)
- [docs.cloud.google.com/billing/docs/how-to/estimate-costs](https://docs.cloud.google.com/billing/docs/how-to/estimate-costs)
- [cloud.google.com/pricing](https://cloud.google.com/pricing)

---

## Question 37

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**PulseCart, an online grocery company, is moving its legacy shopping application to Google Cloud. The team plans to redesign the application into smaller, independently deployable services instead of keeping it as one large application. Which benefit would this refactoring approach provide?**

- [x] A. The redesigned application can become more efficient and scalable.
- [ ] B. No code changes will be required.
- [ ] C. This migration approach provides the quickest path to Google Cloud.
- [ ] D. The application will automatically become PCI-DSS compliant.

### Explanation

**Correct answer: A. The redesigned application can become more efficient and scalable.**

Refactoring rewrites an application to be cloud native, for example as microservices. It takes the most effort, but the result is more efficient and scales better, because each service can scale on its own. The clue is "redesign the application into smaller, independently deployable services".

**Why the others are wrong:**
- **B. No code changes**: Refactoring means significant code changes.
- **C. Quickest path to Google Cloud**: Rehost (lift and shift) is the quickest; refactoring is the slowest.
- **D. Automatically PCI-DSS compliant**: No architecture makes an app compliant automatically; compliance is a shared responsibility.

**Remember:** Refactor = most work, most cloud benefit (scalability, efficiency).

**References:**
- [docs.cloud.google.com/architecture/migration-to-gcp-getting-started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started)
- [cloud.google.com/learn/what-is-microservices-architecture](https://cloud.google.com/learn/what-is-microservices-architecture)
- [cloud.google.com/security/compliance/pci-dss](https://cloud.google.com/security/compliance/pci-dss)

---

## Question 38

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**BrightLens Analytics is building image recognition models on Google Cloud using TensorFlow. The data science team wants to train these advanced machine learning models more quickly by using hardware specifically designed for machine learning workloads. Which solution should BrightLens Analytics use?**

- [x] A. TPUs
- [ ] B. CPUs
- [ ] C. High-memory VMs
- [ ] D. GPUs

### Explanation

**Correct answer: A. TPUs**

Tensor Processing Units (TPUs) are Google's custom chips designed specifically for machine learning. They speed up training of large models such as image recognition networks, and they work well with TensorFlow. The clue is "hardware specifically designed for machine learning workloads".

**Why the others are wrong:**
- **B. CPUs**: General-purpose processors. They can train models, but slowly compared with accelerators.
- **C. High-memory VMs**: More RAM helps with big datasets in memory, but it doesn't accelerate the math of model training.
- **D. GPUs**: GPUs also accelerate ML training and are a valid choice, but they were designed for graphics first. "Designed specifically for ML" points to TPUs.

**Remember:** Hardware built specifically for ML → TPUs.

**References:**
- [cloud.google.com/tpu](https://cloud.google.com/tpu)
- [docs.cloud.google.com/tpu/docs/intro-to-tpu](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)
- [tensorflow.org/guide/tpu](https://tensorflow.org/guide/tpu)

---

## Question 39

*Domain 1: Digital Transformation with Google Cloud*

**GreenTrail, a regional travel booking company, is adopting cloud services, analytics, and automation to redesign internal workflows, improve collaboration, create better traveler experiences, and respond faster to changing customer demand. What is this approach called?**

- [x] A. Digital transformation
- [ ] B. Data center migration
- [ ] C. Operations optimization
- [ ] D. User personalization

### Explanation

**Correct answer: A. Digital transformation**

Digital transformation means using modern digital technologies, like cloud, analytics, and automation, to change how a business works and delivers value to customers. GreenTrail is changing workflows, collaboration, and customer experience, not just one system. The breadth of change is the clue.

**Why the others are wrong:**
- **B. Data center migration**: Migration moves infrastructure; it does not by itself redesign workflows and customer experience.
- **C. Operations optimization**: This is only one part of what GreenTrail is doing.
- **D. User personalization**: Personalization is one possible outcome, not the overall approach.

**Remember:** Using technology to rethink processes, culture, and customer experience → digital transformation.

**References:**
- [cloud.google.com/learn/what-is-digital-transformation](https://cloud.google.com/learn/what-is-digital-transformation)
- [cloud.google.com/learn/what-is-cloud-migration](https://cloud.google.com/learn/what-is-cloud-migration)
- [cloud.google.com/learn/what-is-operational-efficiency](https://cloud.google.com/learn/what-is-operational-efficiency)

---

## Question 40

*Domain 2: Exploring Data Transformation with Google Cloud*

**FinSecure Ledger is modernizing the database layer for its core payment-processing platform. The application needs a highly scalable PostgreSQL-compatible database, but compliance rules require the database to run inside FinSecure Ledger’s private on-premises data center while still using Google’s database technology. Which product should the team use?**

- [x] A. AlloyDB Omni
- [ ] B. Cloud Storage
- [ ] C. BigQuery
- [ ] D. Cloud Run

### Explanation

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

---

## Question 41

*Domain 5: Trust and Security with Google Cloud*

**SkyTrail Logistics uses Google Cloud to host its shipment tracking portal. The security team is reviewing common cyber threats and is especially worried about attackers tricking employees into revealing passwords or clicking malicious links. Which type of attack best represents this social engineering risk?**

- [ ] A. SQL injection attacks
- [ ] B. Physical damage to hardware
- [x] C. Phishing emails
- [ ] D. Distributed denial-of-service attacks

### Explanation

**Correct answer: C. Phishing emails**

Phishing is a social engineering attack. Attackers send messages that look legitimate to trick people into revealing passwords or clicking malicious links. The clues are "tricking employees" and "social engineering".

**Why the others are wrong:**
- **A. SQL injection attacks**: SQL injection targets application code by sending malicious database queries, not people.
- **B. Physical damage to hardware**: This is a physical threat, not trickery of employees.
- **D. Distributed denial-of-service attacks**: DDoS overwhelms services with traffic; it does not trick people.

**Remember:** Tricking people into giving secrets or clicking links → phishing (social engineering).

**References:**
- [csrc.nist.gov/glossary/term/social_engineering](https://csrc.nist.gov/glossary/term/social_engineering)
- [csrc.nist.gov/glossary/term/phishing](https://csrc.nist.gov/glossary/term/phishing)
- [cloud.google.com/web-risk/docs/advisory](https://cloud.google.com/web-risk/docs/advisory)

---

## Question 42

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**BrightBite, a food delivery mobile app, wants its customer app to request menu details, send order information, and receive delivery updates from backend systems. The development team wants to use a standard way for different software components to exchange requests and responses. What is the purpose of an application programming interface (API)?**

- [x] A. To provide a defined set of rules and methods that allow software applications to communicate with each other
- [ ] B. To provide cloud extensions for integrated development environments
- [ ] C. To link private networks across different cloud vendors
- [ ] D. To control and schedule multiple containerized applications

### Explanation

**Correct answer: A. To provide a defined set of rules and methods that allow software applications to communicate with each other**

An API (application programming interface) is a contract that defines how one piece of software can request data or actions from another. The mobile app uses APIs to get menus, send orders, and receive updates from the backend. The clue is "a standard way for different software components to exchange requests and responses".

**Why the others are wrong:**
- **B. Cloud extensions for IDEs**: IDE plugins help developers write code; they are not what an API is.
- **C. Link private networks across clouds**: Connecting networks is done with networking services like VPN or Interconnect.
- **D. Schedule containerized applications**: Scheduling containers is the job of Kubernetes, such as GKE.

**Remember:** API = agreed rules for apps to talk to each other.

**References:**
- [cloud.google.com/apis/docs/overview](https://cloud.google.com/apis/docs/overview)
- [cloud.google.com/api-gateway/docs](https://cloud.google.com/api-gateway/docs)
- [cloud.google.com/endpoints/docs/openapi/about-cloud-endpoints](https://cloud.google.com/endpoints/docs/openapi/about-cloud-endpoints)

---

## Question 43

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**MediaNest, a video streaming startup, is building containerized applications with Kubernetes. The engineering team wants to reduce the time spent configuring nodes, scaling cluster infrastructure, and handling cluster operations so they can focus more on application development. Which Google Cloud service should MediaNest choose?**

- [x] A. GKE Autopilot
- [ ] B. Compute Engine
- [ ] C. Cloud Run
- [ ] D. GKE Standard

### Explanation

**Correct answer: A. GKE Autopilot**

GKE Autopilot is a mode of Google Kubernetes Engine where Google manages the nodes, scaling, and cluster operations. The team still uses Kubernetes but spends its time on applications. The clues are "Kubernetes" and "reduce the time spent configuring nodes … cluster operations".

**Why the others are wrong:**
- **B. Compute Engine**: Compute Engine gives VMs, so the team would have to build and run Kubernetes itself.
- **C. Cloud Run**: Cloud Run is serverless containers without Kubernetes; the team is building with Kubernetes.
- **D. GKE Standard**: In Standard mode, the customer manages and configures the nodes.

**Remember:** Kubernetes without managing nodes → GKE Autopilot; full node control → GKE Standard.

**References:**
- [docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)
- [docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)
- [docs.cloud.google.com/run/docs/overview/what-is-cloud-run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)

---

## Question 44

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**ShopTrail, a retail analytics website, keeps purchase history and customer behavior data in BigQuery. Its analysts know SQL and want to create machine learning models directly on that data without exporting it or learning Python or Java. Which Google Cloud tool should they use?**

- [ ] A. Cloud Vision API
- [x] B. BigQuery ML
- [ ] C. Agent Studio
- [ ] D. Spanner

### Explanation

**Correct answer: B. BigQuery ML**

BigQuery ML lets analysts create and run ML models using standard SQL, directly on data already stored in BigQuery. No data export and no Python or Java are needed. The clues are "analysts know SQL" and "without exporting it".

**Why the others are wrong:**
- **A. Cloud Vision API**: Vision API is a pre-trained model for images, not for building models on purchase data.
- **C. Agent Studio**: Agent Studio is a no-code tool for building AI agents, not for training models on BigQuery tables.
- **D. Spanner**: Spanner is a transactional database, not an ML tool.

**Remember:** SQL skills + data in BigQuery + ML → BigQuery ML.

**References:**
- [docs.cloud.google.com/bigquery/docs/bqml-introduction](https://docs.cloud.google.com/bigquery/docs/bqml-introduction)
- [docs.cloud.google.com/bigquery/docs/create-machine-learning-model](https://docs.cloud.google.com/bigquery/docs/create-machine-learning-model)
- [docs.cloud.google.com/vision/docs](https://docs.cloud.google.com/vision/docs)

---

## Question 45

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**DataCrate Analytics runs a nightly data transformation job that processes millions of log records. The job can safely restart from checkpoints if compute resources are interrupted, and it does not need to finish immediately. The company wants to minimize compute costs and accepts that Google Cloud might stop the instances when capacity is needed elsewhere. Which compute option should the company choose?**

- [x] A. Spot VMs
- [ ] B. Managed services
- [ ] C. Premium tier virtual machines
- [ ] D. Cloud Run functions

### Explanation

**Correct answer: A. Spot VMs**

Spot VMs are spare Google Cloud capacity at a large discount. Google can stop them when it needs the capacity back. They suit fault-tolerant batch jobs that can restart and do not have tight deadlines. The clues are "restart from checkpoints", "does not need to finish immediately", and "accepts that Google Cloud might stop the instances".

**Why the others are wrong:**
- **B. Managed services**: This is a general approach, not a low-cost interruptible compute option.
- **C. Premium tier virtual machines**: There is no such VM type. In Google Cloud, Premium Tier is a Network Service Tier (traffic on Google's global network), which affects networking, not compute cost.
- **D. Cloud Run functions**: Functions are for short event-driven code, not long nightly batch jobs over millions of records.

**Remember:** Fault-tolerant batch + lowest cost + OK to be interrupted → Spot VMs.

**References:**
- [docs.cloud.google.com/compute/docs/instances/spot](https://docs.cloud.google.com/compute/docs/instances/spot)
- [docs.cloud.google.com/compute/docs/instances/create-use-spot](https://docs.cloud.google.com/compute/docs/instances/create-use-spot)
- [docs.cloud.google.com/compute/docs/instances/provisioning-models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models)

---

## Question 46

*Domain 5: Trust and Security with Google Cloud*

**NovaCart, an online shopping platform, wants to improve its security awareness training for employees. The training team asks which type of cybersecurity threat can secretly steal, alter, or damage information on a device or system without the user noticing. Which cybersecurity threat does this describe?**

- [ ] A. SLA policy violation
- [x] B. Malware attack
- [ ] C. Ransomware attack
- [ ] D. Incomplete data input

### Explanation

**Correct answer: B. Malware attack**

Malware is any malicious software, such as viruses, spyware, or trojans, that can secretly steal, change, or damage data. The broad description "steal, alter, or damage information … without the user noticing" fits malware in general.

**Why the others are wrong:**
- **A. SLA policy violation**: An SLA violation is a missed service promise, not a cyber threat.
- **C. Ransomware attack**: Ransomware is one type of malware; it locks data and demands payment, which users notice right away.
- **D. Incomplete data input**: This is a data quality issue, not an attack.

**Remember:** Malicious software that secretly harms data → malware; locks data for payment → ransomware.

**References:**
- [csrc.nist.gov/glossary/term/malware](https://csrc.nist.gov/glossary/term/malware)
- [csrc.nist.gov/glossary/term/ransomware](https://csrc.nist.gov/glossary/term/ransomware)
- [cisa.gov/topics/cyber-threats-and-advisories/malware-phishing-and-ransomware](https://cisa.gov/topics/cyber-threats-and-advisories/malware-phishing-and-ransomware)

---

## Question 47

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**HarborStyle Retail runs a large on-premises VMware estate for its inventory, billing, and store operations systems. The company wants to move these workloads to Google Cloud, but it wants administrators to continue using familiar VMware tools and existing operating procedures with minimal change. Which Google Cloud service should HarborStyle Retail use?**

- [ ] A. Compute Engine
- [x] B. Google Cloud VMware Engine
- [ ] C. VMware vSphere
- [ ] D. Bare Metal Solution

### Explanation

**Correct answer: B. Google Cloud VMware Engine**

Google Cloud VMware Engine runs a full VMware environment as a managed service on Google Cloud. Admins keep using the VMware tools and procedures they already know. The clues are "large on-premises VMware estate" and "familiar VMware tools … with minimal change".

**Why the others are wrong:**
- **A. Compute Engine**: Moving to Compute Engine means converting VMs and leaving VMware tools behind.
- **C. VMware vSphere**: vSphere is VMware's own software, not a Google Cloud service.
- **D. Bare Metal Solution**: Bare Metal is for specialized workloads like Oracle databases, not for keeping VMware operations.

**Remember:** Move VMware workloads and keep VMware tools → Google Cloud VMware Engine.

**References:**
- [cloud.google.com/vmware-engine](https://cloud.google.com/vmware-engine)
- [docs.cloud.google.com/vmware-engine/docs/overview](https://docs.cloud.google.com/vmware-engine/docs/overview)
- [docs.cloud.google.com/vmware-engine/docs/workloads/howto-migrate-workloads](https://docs.cloud.google.com/vmware-engine/docs/workloads/howto-migrate-workloads)

---

## Question 48

*Domain 6: Scaling with Google Cloud Operations*

**FreshCartGo, a grocery delivery mobile app, runs its backend on a cloud provider and has an SLA that promises a defined level of monthly service availability. During one month, the provider fails to meet the agreed availability target. What should FreshCartGo typically expect from the cloud provider?**

- [ ] A. Automatic increase in subscription fees
- [ ] B. Permanent shutdown of the affected cloud service
- [x] C. Service credit for the service interruption
- [ ] D. Automatic expansion of the application’s error budget

### Explanation

**Correct answer: C. Service credit for the service interruption**

An SLA is a contract that promises a level of service. If the provider misses it, the usual remedy is a service credit, which is a discount on future bills. The clue is "fails to meet the agreed availability target".

**Why the others are wrong:**
- **A. Increase in subscription fees**: A missed SLA leads to compensation, not higher prices.
- **B. Permanent shutdown of the service**: Missing a target does not shut the service down.
- **D. Expansion of the error budget**: The error budget is an internal SRE concept tied to the SLO; it does not grow because of an outage.

**Remember:** Missed SLA → service credits for the customer.

**References:**
- [cloud.google.com/terms/sla](https://cloud.google.com/terms/sla)
- [cloud.google.com/storage/sla](https://cloud.google.com/storage/sla)
- [docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring)

**⚠️ Note:** Under Google Cloud SLAs, customers usually must request credits within a time window; they are not automatic. "Service credit" is still the right answer.

---

## Question 49

*Domain 6: Scaling with Google Cloud Operations*

**TaskNest is a project management app that is adopting a DevOps approach for its software delivery teams. The company wants to use tools and automation to make development, testing, deployment, and operations faster and more reliable. Which operational challenge will this help TaskNest resolve?**

- [x] A. Repetitive manual tasks that slow down workflows
- [ ] B. Continuous supervision of creative design work
- [ ] C. Vendor distribution and product supply-chain delays
- [ ] D. Faulty physical hardware that blocks new ideas

### Explanation

**Correct answer: A. Repetitive manual tasks that slow down workflows**

DevOps uses automation, like CI/CD pipelines and automated testing, to remove slow, error-prone manual steps. This makes building, testing, and releasing software faster and more reliable. The clue is "tools and automation to make … faster and more reliable".

**Why the others are wrong:**
- **B. Supervision of creative design work**: DevOps is about software delivery and operations, not managing design work.
- **C. Supply-chain delays**: Physical product supply chains are outside DevOps.
- **D. Faulty physical hardware**: Hardware failures are an infrastructure issue, not what DevOps automation solves.

**Remember:** DevOps = automate repetitive work to ship faster and more reliably.

**References:**
- [cloud.google.com/devops](https://cloud.google.com/devops)
- [docs.cloud.google.com/architecture/devops](https://docs.cloud.google.com/architecture/devops)
- [docs.cloud.google.com/architecture/framework/operational-excellence/automate-and-manage-change](https://docs.cloud.google.com/architecture/framework/operational-excellence/automate-and-manage-change)

---

## Question 50

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**HomeFixNow, a home repair booking website, wants to build web applications that can automatically scale as customer traffic increases or decreases. The development team also wants Google Cloud to handle the underlying application infrastructure so they can focus on writing code. Which Google Cloud product should HomeFixNow use?**

- [ ] A. Anthos
- [ ] B. Apigee
- [ ] C. AutoML
- [x] D. App Engine

### Explanation

**Correct answer: D. App Engine**

App Engine is a fully managed platform (PaaS) for web applications. Developers deploy code, and Google handles the infrastructure and scales the app up and down with traffic. The clues are "build web applications", "automatically scale", and "focus on writing code".

**Why the others are wrong:**
- **A. Anthos**: Anthos (now GKE Enterprise) manages Kubernetes across hybrid and multicloud environments; it is not a simple app host.
- **B. Apigee**: Apigee manages APIs; it does not host web apps.
- **C. AutoML**: AutoML trains custom ML models, not web applications.

**Remember:** Deploy web app code, Google handles scaling and infrastructure → App Engine (or Cloud Run).

**References:**
- [cloud.google.com/appengine](https://cloud.google.com/appengine)
- [docs.cloud.google.com/appengine/docs](https://docs.cloud.google.com/appengine/docs)
- [docs.cloud.google.com/appengine/docs/standard/how-instances-are-managed](https://docs.cloud.google.com/appengine/docs/standard/how-instances-are-managed)

**⚠️ Note:** App Engine is right among these options, but for new web apps Google now usually steers toward Cloud Run. Pick the keyed answer on this exam.

---
