# Cloud Digital Leader — Practice Exam 5

50 questions.

## Question 1

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**PhotoNest, an online image storage app, has thousands of uploaded pictures that need to be automatically categorized by objects, places, and general labels. The team wants to use a Google Cloud service with pre-trained machine learning instead of building and training its own model. Which Google Cloud product or service should PhotoNest use?**

- [x] A. Vision API
- [ ] B. BigQuery ML
- [ ] C. AutoML Vision
- [ ] D. Looker

### Explanation

**Correct answer: A. Vision API**

Vision API is a pre-trained model that labels images out of the box. It detects objects, places, landmarks and general labels with a simple API call. The clue is "pre-trained machine learning instead of building and training its own model", which rules out anything that needs your own training data.

**Why the others are wrong:**
- **B. BigQuery ML**: it trains models with SQL on tabular data in BigQuery, not ready-made image labeling.
- **C. AutoML Vision**: it trains a custom model on your own labeled images, which the team wants to avoid.
- **D. Looker**: it is a BI and dashboard tool, not an image analysis service.

**Remember:** Common labels, no training = pre-trained API (Vision API). Your own custom categories = AutoML.

**References:**
- [docs.cloud.google.com/vision/docs](https://docs.cloud.google.com/vision/docs)
- [docs.cloud.google.com/vision/docs/detect-labels-image-api](https://docs.cloud.google.com/vision/docs/detect-labels-image-api)
- [docs.cloud.google.com/bigquery/docs/bqml-introduction](https://docs.cloud.google.com/bigquery/docs/bqml-introduction)

---

## Question 2

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**AgriPulse Insights stores valuable crop-yield, soil-quality, and weather-pattern data in a relational database. The company wants to create a new income source by allowing partner companies to use this data inside their own mobile and web applications. Which cloud-first approach should AgriPulse Insights choose?**

- [ ] A. Add partner users directly to the relational database.
- [ ] B. Sell paid downloads of old exported data files.
- [x] C. Provide access to the data through a paid API.
- [ ] D. Move the data into a non-relational database.

### Explanation

**Correct answer: C. Provide access to the data through a paid API.**

An API lets partners pull current data straight into their own apps in a controlled, secure way. Charging for API access turns the data into a new revenue stream. The clues are "new income source" and "inside their own mobile and web applications".

**Why the others are wrong:**
- **A. Add partner users directly to the database**: this is a security risk and tightly couples partners to your internal systems.
- **B. Sell paid downloads of old exported files**: the data is stale and can't be used live inside apps.
- **D. Move to a non-relational database**: changing the database type does not give partners access or create revenue.

**Remember:** Monetize data for partners' apps = a paid, managed API.

**References:**
- [cloud.google.com/apigee](https://cloud.google.com/apigee)
- [docs.cloud.google.com/apigee/docs/api-platform/monetization/overview](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/overview)
- [docs.cloud.google.com/api-gateway/docs/about-api-gateway](https://docs.cloud.google.com/api-gateway/docs/about-api-gateway)

---

## Question 3

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**FitPerks, a fitness membership app, gives reward points to its customers. The company recently partnered with nearby gyms, sports shops, and health cafes so members can earn and redeem points across all partner locations. Why should FitPerks use application programming interfaces?**

- [ ] A. To copy all partner information into its own system for disaster recovery
- [ ] B. To create charts showing reward program performance
- [ ] C. To generate personalized offers for members
- [x] D. To connect partner systems so loyalty point details stay current

### Explanation

**Correct answer: D. To connect partner systems so loyalty point details stay current**

APIs let separate systems talk to each other in real time. FitPerks needs gyms, shops and cafes to read and update the same points balance, so every partner sees the current number when a member earns or redeems. The clue is "earn and redeem points across all partner locations".

**Why the others are wrong:**
- **A. Copy partner data for disaster recovery**: that is backup, not integration, and you don't copy partners' systems.
- **B. Create performance charts**: that is a reporting/BI task, not why you integrate partners.
- **C. Generate personalized offers**: that is a machine learning use case, not the core reason for APIs here.

**Remember:** Several businesses sharing live data = connect them with APIs.

**References:**
- [docs.cloud.google.com/apis/docs/overview](https://docs.cloud.google.com/apis/docs/overview)
- [cloud.google.com/learn/what-is-api-management](https://cloud.google.com/learn/what-is-api-management)
- [docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)

---

## Question 4

*Domain 5: Trust and Security with Google Cloud*

**GreenNest Finance, a small digital banking company, experiences a serious customer data leak only eight months after installing a newer security platform. The leadership team wants to reduce the chance of similar incidents over time and improve its overall security approach. What should GreenNest Finance do to support long-term security?**

- [ ] A. Increase data retention periods to at least eight years.
- [ ] B. Spend more money to buy the most expensive security platform available.
- [x] C. Hire cybersecurity experts to improve and expand the data security plan.
- [ ] D. Wait until a newer and more advanced security platform becomes available.

### Explanation

**Correct answer: C. Hire cybersecurity experts to improve and expand the data security plan.**

A leak soon after buying a new platform shows that tools alone don't create security. Long-term protection needs skilled people who keep improving policies, processes and controls as threats change. The clue is "over time" and "improve its overall security approach".

**Why the others are wrong:**
- **A. Increase data retention**: keeping data longer increases what can leak, it doesn't protect it.
- **B. Buy the most expensive platform**: price doesn't fix gaps in process and expertise, which just failed.
- **D. Wait for a newer platform**: waiting leaves the company exposed and again relies only on tools.

**Remember:** Security is ongoing expertise and process, not a one-time product purchase.

**References:**
- [docs.cloud.google.com/architecture/framework/security](https://docs.cloud.google.com/architecture/framework/security)
- [docs.cloud.google.com/architecture/blueprints/security-foundations](https://docs.cloud.google.com/architecture/blueprints/security-foundations)
- [nist.gov/cyberframework](https://nist.gov/cyberframework)

**⚠️ Note:** "Hire cybersecurity experts" is vague. The real lesson is that security needs ongoing expertise and process. It is still clearly the best of the four options, so pick it.

---

## Question 5

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**MedSnap Care, a healthcare mobile app, lets users upload photos of visible symptoms so the app can identify possible condition categories and route the case to the right care team. Which technology is most closely related to this capability?**

- [ ] A. Cloud Logging
- [ ] B. Cloud Profiler
- [ ] C. App Engine
- [x] D. Machine learning

### Explanation

**Correct answer: D. Machine learning**

Recognizing condition categories in symptom photos is image classification. A machine learning model learns from many labeled example images and then classifies new ones, which lets the app route each case to the right team. On Google Cloud this could be the Vision API, AutoML or a custom model, but the technology behind all of them is ML.

**Why the others are wrong:**
- **A. Cloud Logging**: Stores and searches log entries. It doesn't analyze images.
- **B. Cloud Profiler**: Measures CPU and memory use in application code.
- **C. App Engine**: Hosts web applications. It can run the app, but it doesn't classify images.

**Remember:** Recognize, classify or predict from images, text or data → machine learning.

**References:**
- [cloud.google.com/learn/what-is-machine-learning](https://cloud.google.com/learn/what-is-machine-learning)
- [docs.cloud.google.com/logging/docs/overview](https://docs.cloud.google.com/logging/docs/overview)
- [docs.cloud.google.com/appengine/docs](https://docs.cloud.google.com/appengine/docs)

---

## Question 6

*Domain 5: Trust and Security with Google Cloud*

**ClearGate Apps, a multinational SaaS company, is redesigning how employees and partners access its internal systems. The company no longer wants to assume that traffic from an office location or corporate network is automatically trusted. Instead, every identity, endpoint, and application request must be verified, authenticated, and authorized before access is granted, whether the request comes from headquarters, a branch office, or a remote location. Which security model is being described?**

- [x] A. Zero trust architecture
- [ ] B. Virtual Private Network (VPN)
- [ ] C. Shared Responsibility Model
- [ ] D. Capital Expenditure (CapEx) model

### Explanation

**Correct answer: A. Zero trust architecture**

Zero trust means no request is trusted because of where it comes from. Every user, device and request is verified, authenticated and authorized each time, whether it is from the office or from home. The clue is "no longer wants to assume that traffic from... corporate network is automatically trusted". Google's version of this is BeyondCorp.

**Why the others are wrong:**
- **B. VPN**: a VPN extends the trusted network, which is the perimeter model zero trust replaces.
- **C. Shared Responsibility Model**: it splits security duties between provider and customer, not an access model.
- **D. CapEx model**: it is a spending model, not a security model.

**Remember:** "Never trust, always verify", regardless of location = zero trust.

**References:**
- [cloud.google.com/beyondcorp](https://cloud.google.com/beyondcorp)
- [cloud.google.com/docs/security/zero-trust](https://cloud.google.com/docs/security/zero-trust)
- [nist.gov/publications/zero-trust-architecture](https://nist.gov/publications/zero-trust-architecture)

---

## Question 7

*Domain 5: Trust and Security with Google Cloud*

**MetroLedger, a digital banking platform, recently suffered a security incident that temporarily disrupted a few customer-facing services. The leadership team now wants the company to improve its ability to reduce the chance of future attacks, continue running essential services during an incident, limit business impact, and restore normal operations quickly after disruption. Which concept best describes this capability?**

- [ ] A. Data masking
- [x] B. Cyber resilience
- [ ] C. Infrastructure as a Service
- [ ] D. Vendor lock-in

### Explanation

**Correct answer: B. Cyber resilience**

Cyber resilience is the ability to prevent attacks where possible, keep essential services running during an incident, limit the damage and recover quickly. The stem lists exactly these parts: reduce the chance, continue running, limit impact, restore operations.

**Why the others are wrong:**
- **A. Data masking**: it hides sensitive values in data, a single control, not overall resilience.
- **C. Infrastructure as a Service**: it is a cloud service model, not a security capability.
- **D. Vendor lock-in**: it is a risk of depending on one provider, unrelated to recovering from attacks.

**Remember:** Prevent, withstand, recover = cyber resilience.

**References:**
- [cloud.google.com/security/resources/cyber-resilience](https://cloud.google.com/security/resources/cyber-resilience)
- [csrc.nist.gov/glossary/term/cyber_resiliency](https://csrc.nist.gov/glossary/term/cyber_resiliency)
- [nist.gov/cyberframework](https://nist.gov/cyberframework)

---

## Question 8

*Domain 2: Exploring Data Transformation with Google Cloud*

**FinSight Ledger, a financial analytics company, has moved several large customer transaction and reporting databases to Google Cloud. The company wants to get more business value from its data, manage data-related costs more effectively, and improve compliance with financial regulations. What should FinSight Ledger do?**

- [ ] A. Delete data that has been stored for more than 18 months.
- [ ] B. Move relational data into modern NoSQL databases.
- [ ] C. Generate quarterly reports about data access and usage.
- [x] D. Establish an effective data governance program.

### Explanation

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

---

## Question 9

*Domain 2: Exploring Data Transformation with Google Cloud*

**ParkNest, a mobile parking app, stores driver profiles, payment records, parking sensor events, and customer support logs in separate systems. The company wants to move to a unified cloud data solution on Google Cloud. What is the main benefit of this approach?**

- [ ] A. Data will always be cheaper to store.
- [ ] B. Data can be automatically protected from all external threats.
- [ ] C. Data will always be backed up and cannot be lost or deleted.
- [x] D. Data can support innovation because it is no longer isolated in silos.

### Explanation

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

---

## Question 10

*Domain 5: Trust and Security with Google Cloud*

**AsterBay Retail, an international ecommerce company, wants its Security Operations team to improve how it detects and investigates advanced attackers. The team needs a Google Cloud security solution that brings together Mandiant frontline incident response knowledge, VirusTotal crowdsourced malware intelligence, Google’s broad visibility, and AI-assisted analysis so analysts can better understand threats and act before attacks cause damage. Which Google Cloud security offering best fits this requirement?**

- [x] A. Google Threat Intelligence
- [ ] B. Google Kubernetes Engine (GKE)
- [ ] C. Cloud Load Balancing
- [ ] D. Identity and Access Management (IAM)

### Explanation

**Correct answer: A. Google Threat Intelligence**

Google Threat Intelligence combines Mandiant's frontline incident response knowledge, VirusTotal's crowdsourced malware data and Google's own visibility, with Gemini-powered analysis. It helps security teams understand who is attacking and act early. The stem names these exact sources, so the match is direct.

**Why the others are wrong:**
- **B. GKE**: it runs containers, it is not a threat intelligence service.
- **C. Cloud Load Balancing**: it distributes traffic across backends.
- **D. IAM**: it controls who can access which resources, not threat research.

**Remember:** Mandiant + VirusTotal + Google visibility = Google Threat Intelligence.

**References:**
- [cloud.google.com/security/products/threat-intelligence](https://cloud.google.com/security/products/threat-intelligence)
- [gtidocs.virustotal.com/docs/use-cases](https://gtidocs.virustotal.com/docs/use-cases)
- [docs.cloud.google.com/chronicle/docs/detection](https://docs.cloud.google.com/chronicle/docs/detection)

---

## Question 11

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**PixelPeak Media, a digital content company, is comparing cloud providers for its next innovation program. The team wants access to ready-to-use AI agents, advanced Google first-party models, and a unified AI development platform for building and managing AI solutions. Under which category of Google Cloud’s top differentiators do these capabilities belong?**

- [ ] A. Global network infrastructure
- [x] B. World-leading AI
- [ ] C. CapEx reduction
- [ ] D. Open standards

### Explanation

**Correct answer: B. World-leading AI**

Ready-to-use AI agents, Google's first-party models (such as Gemini) and a unified AI development platform all describe Google Cloud's AI leadership. These are AI capabilities, so they fall under the AI differentiator.

**Why the others are wrong:**
- **A. Global network infrastructure**: it is about Google's private fiber network and global reach, not AI models.
- **C. CapEx reduction**: it is a financial benefit of cloud in general, not a Google differentiator category.
- **D. Open standards**: it is about avoiding lock-in and interoperability, not AI products.

**Remember:** Agents, Gemini models, AI platform = the AI differentiator.

**References:**
- [cloud.google.com/gemini-enterprise](https://cloud.google.com/gemini-enterprise)
- [cloud.google.com/products/gemini-enterprise-agent-platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview)

---

## Question 12

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**FitSprint, a fitness tracking web app, has packaged its stateless frontend service into a container. The team wants to deploy it on Google Cloud so it can scale down to zero when there is no traffic and quickly scale up during busy periods, without requiring the team to create or manage Kubernetes clusters or servers. Which service should FitSprint use?**

- [ ] A. Compute Engine
- [x] B. Cloud Run
- [ ] C. Bare Metal Solution
- [ ] D. AlloyDB Omni

### Explanation

**Correct answer: B. Cloud Run**

Cloud Run runs stateless containers without any servers or clusters to manage. It scales automatically with traffic, including down to zero when idle, so you pay nothing while there are no requests. The clues are "container", "scale down to zero" and "without... Kubernetes clusters or servers".

**Why the others are wrong:**
- **A. Compute Engine**: these are VMs you manage yourself, and they don't scale to zero.
- **C. Bare Metal Solution**: dedicated physical servers for special workloads such as Oracle.
- **D. AlloyDB Omni**: a downloadable PostgreSQL-compatible database, not a container hosting service.

**Remember:** Container + serverless + scale to zero = Cloud Run.

**References:**
- [docs.cloud.google.com/run/docs/overview/what-is-cloud-run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)
- [docs.cloud.google.com/run/docs/about-instance-autoscaling](https://docs.cloud.google.com/run/docs/about-instance-autoscaling)
- [docs.cloud.google.com/compute/docs/instances](https://docs.cloud.google.com/compute/docs/instances)

---

## Question 13

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**GreenCart Finance, a small payment processing company, must leave its private server room because the facility contract ends soon. The IT team wants to move its existing virtual machines to Compute Engine with the same operating system images, application settings, and configurations, making only the minimum changes needed to run in Google Cloud. Which migration strategy is this?**

- [x] A. Rehost (Lift and shift)
- [ ] B. Refactor
- [ ] C. Reimagine
- [ ] D. Replatform

### Explanation

**Correct answer: A. Rehost (Lift and shift)**

Rehosting moves existing VMs to the cloud as they are, with the same OS, settings and configuration. It is the fastest path, which fits a hard deadline like an expiring facility contract. The clue is "minimum changes needed".

**Why the others are wrong:**
- **B. Refactor**: it changes the application code to use cloud features, which takes more time.
- **C. Reimagine**: it rethinks or rebuilds the application from scratch, the most effort.
- **D. Replatform**: it makes some optimizations, such as moving to a managed service, so more than minimal changes.

**Remember:** Same VMs, no changes, quick exit = lift and shift.

**References:**
- [docs.cloud.google.com/architecture/migration-to-gcp-getting-started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started)
- [docs.cloud.google.com/migration-center/docs/migration-planning-overview](https://docs.cloud.google.com/migration-center/docs/migration-planning-overview)
- [cloud.google.com/blog/products/application-development/application-rationalization-what-why-and-how](https://cloud.google.com/blog/products/application-development/application-rationalization-what-why-and-how)

---

## Question 14

*Domain 2: Exploring Data Transformation with Google Cloud*

**ShopSprint has migrated customer orders, payment records, and stock-level details to a cloud-based relational database. What capability does a relational database provide?**

- [ ] A. It keeps massive volumes of raw data in the same format in which it was collected
- [x] B. It stores transactional data that applications can access electronically
- [ ] C. It performs fast analysis of very large and multi-dimensional datasets
- [ ] D. It processes unstructured data and makes it available across several geographic locations

### Explanation

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

---

## Question 15

*Domain 6: Scaling with Google Cloud Operations*

**NimbusRide runs several customer-facing applications on Google Cloud. The operations team wants to collect application metrics and resource metadata, then view that information in dashboards to understand service performance. Which Google Cloud tool should they use?**

- [x] A. Cloud Monitoring
- [ ] B. Cloud Trace
- [ ] C. Cloud Logging
- [ ] D. Cloud Debugger

### Explanation

**Correct answer: A. Cloud Monitoring**

Cloud Monitoring collects metrics, events and metadata from applications and Google Cloud resources. It shows them in dashboards and can send alerts. The clue is "metrics" and "dashboards" to understand performance.

**Why the others are wrong:**
- **B. Cloud Trace**: it follows single requests across services to find latency, not general metrics dashboards.
- **C. Cloud Logging**: it collects and stores log entries, not metrics.
- **D. Cloud Debugger**: it inspected running code state to find bugs (and has been retired).

**Remember:** Metrics + dashboards + alerts = Cloud Monitoring. Logs = Cloud Logging. Latency of a request = Cloud Trace.

**References:**
- [docs.cloud.google.com/monitoring/docs](https://docs.cloud.google.com/monitoring/docs)
- [docs.cloud.google.com/monitoring/dashboards](https://docs.cloud.google.com/monitoring/dashboards)
- [docs.cloud.google.com/trace/docs](https://docs.cloud.google.com/trace/docs)

---

## Question 16

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**TrailCart, a small grocery delivery app, wants its developers and analysts to quickly explore reusable machine learning resources on Google Cloud without building everything from scratch. How does Google Cloud AI Hub help Google Cloud customers get started with machine learning?**

- [ ] A. It serves artificial intelligence models for real-time predictions
- [ ] B. It automatically writes complete machine learning model code for users
- [ ] C. It automatically collects, cleans, and prepares users’ machine learning datasets
- [x] D. It provides a repository of ready-to-use artificial intelligence and machine learning resources

### Explanation

**Correct answer: D. It provides a repository of ready-to-use artificial intelligence and machine learning resources**

AI Hub was a catalog of reusable AI and ML assets, such as models, notebooks and pipelines. Teams could find something close to what they needed and start from it. The clue is "explore reusable machine learning resources... without building everything from scratch".

**Why the others are wrong:**
- **A. Serves models for real-time predictions**: that is model serving on the AI platform, not a catalog.
- **B. Writes complete model code**: no catalog writes your whole model for you.
- **C. Collects, cleans and prepares datasets**: data preparation is a separate step and tool set.

**Remember:** Hub = repository of reusable resources.

**References:**
- [cloud.google.com/blog/products/ai-machine-learning/introducing-ai-hub-and-kubeflow-pipelines-making-ai-simpler-faster-and-more-useful-for-businesses](https://cloud.google.com/blog/products/ai-machine-learning/introducing-ai-hub-and-kubeflow-pipelines-making-ai-simpler-faster-and-more-useful-for-businesses)
- [cloud.google.com/model-garden](https://cloud.google.com/model-garden)
- [cloud.google.com/products/ai](https://cloud.google.com/products/ai)

**⚠️ Note:** AI Hub is an older product. Its role is now mostly filled by Model Garden in the AI platform. The definition is still correct, so pick the key.

---

## Question 17

*Domain 5: Trust and Security with Google Cloud*

**CarePulse Clinics, a healthcare services company, finds that an attacker has locked access to its appointment records and patient history database by encrypting the files. The attacker sends a message demanding payment in cryptocurrency before providing the decryption key needed to restore the data. What type of cybersecurity threat does this describe?**

- [ ] A. Phishing
- [x] B. Ransomware
- [ ] C. Cryptomining
- [ ] D. Hardware failure

### Explanation

**Correct answer: B. Ransomware**

Ransomware encrypts a victim's data and demands payment, often in cryptocurrency, for the decryption key. The clues are "encrypting the files" and "demanding payment" to restore access.

**Why the others are wrong:**
- **A. Phishing**: it tricks people into giving away credentials or clicking malicious links. It may deliver ransomware, but it isn't the lockout itself.
- **C. Cryptomining**: attackers secretly use your computing power to mine cryptocurrency; they don't lock your data.
- **D. Hardware failure**: it is an accident, not an attack with a ransom demand.

**Remember:** Data locked + payment demanded = ransomware. Mention of crypto doesn't mean cryptomining.

**References:**
- [cisa.gov/stopransomware/ransomware-101](https://cisa.gov/stopransomware/ransomware-101)
- [nist.gov/itl/smallbusinesscyber/guidance-topic/ransomware](https://nist.gov/itl/smallbusinesscyber/guidance-topic/ransomware)
- [docs.cloud.google.com/architecture/security/mitigating-ransomware-attacks](https://docs.cloud.google.com/architecture/security/mitigating-ransomware-attacks)

---

## Question 18

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**BrightCart Market, an online retail company, is moving its inventory, payments, and customer engagement applications to the cloud. The leadership team is worried about becoming dependent on a single provider and wants future flexibility to run applications across public cloud, private cloud, and on-premises environments when needed. Which principle should best guide the company’s cloud modernization strategy?**

- [ ] A. Adopting proprietary, vendor-specific databases
- [ ] B. Keeping all mission-critical workloads in a single private cloud
- [x] C. Committing to openness and interoperability
- [ ] D. Relying exclusively on Software as a Service (SaaS) products

### Explanation

**Correct answer: C. Committing to openness and interoperability**

Open standards, open source and interoperable tools let workloads move between public cloud, private cloud and on-premises. That avoids depending on one provider. The clues are "dependent on a single provider" and "flexibility to run applications across" environments.

**Why the others are wrong:**
- **A. Proprietary, vendor-specific databases**: these increase lock-in, the opposite of the goal.
- **B. Everything in a single private cloud**: this removes flexibility instead of adding it.
- **D. Only SaaS products**: SaaS can tie you to each vendor and doesn't give control over where apps run.

**Remember:** Fear of lock-in + hybrid/multicloud flexibility = openness and interoperability.

**References:**
- [cloud.google.com/learn/what-is-multicloud](https://cloud.google.com/learn/what-is-multicloud)
- [docs.cloud.google.com/architecture/hybrid-multicloud-patterns/drivers](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/drivers)
- [cloud.google.com/blog/topics/inside-google-cloud/empowering-customers-and-the-ecosystem-with-an-open-cloud](https://cloud.google.com/blog/topics/inside-google-cloud/empowering-customers-and-the-ecosystem-with-an-open-cloud)

---

## Question 19

*Domain 5: Trust and Security with Google Cloud*

**BrightCart, a retail mobile app company, stores customer purchase analytics in Google Cloud. The operations manager wants to understand who should decide which employees can access different company datasets and reports. Who is responsible for defining data access policies?**

- [ ] A. Cloud Identity
- [ ] B. Google Cloud Customer Care team
- [x] C. BrightCart’s IT team
- [ ] D. BrightCart’s app users

### Explanation

**Correct answer: C. BrightCart’s IT team**

Under the shared responsibility model, the customer owns its data and decides who can access it. Google secures the underlying infrastructure, but the customer's IT team defines access policies and grants roles through IAM. The clue is "who should decide which employees can access".

**Why the others are wrong:**
- **A. Cloud Identity**: it is a tool for managing users and groups, not the party who sets policy.
- **B. Google Cloud Customer Care**: support helps with issues but doesn't decide your access rules.
- **D. App users**: end customers don't control internal employee access.

**Remember:** Google secures the cloud; the customer secures data and access in the cloud.

**References:**
- [docs.cloud.google.com/iam/docs/overview](https://docs.cloud.google.com/iam/docs/overview)
- [docs.cloud.google.com/identity/docs/overview](https://docs.cloud.google.com/identity/docs/overview)
- [docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)

---

## Question 20

*Domain 6: Scaling with Google Cloud Operations*

**CityPulse Hosting provides a public cloud service used by several small businesses. Its service performance has dropped below the internal service level objective (SLO), but it is still above the contractual service level agreement (SLA). What is the likely result of this service performance change?**

- [ ] A. CityPulse Hosting is encouraged to release new feature updates more quickly
- [x] B. CityPulse Hosting is encouraged to focus more on service reliability
- [ ] C. Customers experience unexpected or extended service outages
- [ ] D. Customers experience lower service latency

### Explanation

**Correct answer: B. CityPulse Hosting is encouraged to focus more on service reliability**

The SLO is the internal reliability target. Falling below it usually means the error budget (100% − SLO) is used up. The SRE response is to slow down risky changes and spend effort on reliability until performance is back on target. Being above the SLA means no contract penalty yet.

**Why the others are wrong:**
- **A. Release features faster**: that is what you do when error budget remains, not when the SLO is missed.
- **C. Unexpected or extended outages**: performance is still above the SLA, so customers aren't necessarily seeing major outages.
- **D. Lower latency**: performance dropped, so latency would not improve.

**Remember:** SLO missed = focus on reliability. Budget left = innovate.

**References:**
- [sre.google/sre-book/service-level-objectives](https://sre.google/sre-book/service-level-objectives)
- [cloud.google.com/blog/products/devops-sre/sre-fundamentals-sli-vs-slo-vs-sla](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-sli-vs-slo-vs-sla)
- [cloud.google.com/architecture/framework/reliability](https://cloud.google.com/architecture/framework/reliability)

---

## Question 21

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**BrightWave Media wants to analyze campaign clicks, app installs, website visits, and social media engagement data together so it can predict future customer acquisition. How should the company use cloud technology to gain new insights from this data?**

- [ ] A. Import the datasets into a custom data warehouse, and then archive older data
- [ ] B. Import and selectively archive the datasets in a custom data lake
- [ ] C. Keep the datasets separate and make predictions using machine learning
- [x] D. Combine the datasets and make predictions using machine learning

### Explanation

**Correct answer: D. Combine the datasets and make predictions using machine learning**

Predictions get better when the model can see how clicks, installs, visits and social engagement relate to each other. Combining the data in one place, then training ML on it, reveals these patterns. The clues are "analyze... together" and "predict".

**Why the others are wrong:**
- **A. Custom warehouse, then archive**: archiving older data removes history the model needs, and there is no prediction step.
- **B. Selectively archive in a data lake**: storing and archiving is not analysis or prediction.
- **C. Keep the datasets separate**: silos hide the cross-channel patterns the company is looking for.

**Remember:** New insights = combine the data, then apply ML.

**References:**
- [cloud.google.com/bigquery/docs/bigqueryml-intro](https://cloud.google.com/bigquery/docs/bigqueryml-intro)
- [cloud.google.com/learn/what-is-a-data-warehouse](https://cloud.google.com/learn/what-is-a-data-warehouse)
- [cloud.google.com/learn/what-is-a-data-lake](https://cloud.google.com/learn/what-is-a-data-lake)

---

## Question 22

*Domain 2: Exploring Data Transformation with Google Cloud*

**FitPulse, a new wellness mobile app, collects a massive volume of user data such as workout duration, step patterns, heart-rate activity, and estimated calories burned. The company wants to keep this data for future exploration and analytics, even before deciding exactly how it will be processed. Which data management solution should FitPulse use?**

- [x] A. Data lake
- [ ] B. Data warehouse
- [ ] C. Data field
- [ ] D. Database

### Explanation

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

---

## Question 23

*Domain 5: Trust and Security with Google Cloud*

**PixelNest Media stores application files and customer activity records in Google Cloud and also sends data between services for processing. The security team wants to know when Google Cloud automatically encrypts customer data by default. When is data automatically encrypted in Google Cloud?**

- [ ] A. When it is in transit only.
- [x] B. When it is at rest and in transit.
- [ ] C. Data is not automatically encrypted by default.
- [ ] D. When it is at rest only.

### Explanation

**Correct answer: B. When it is at rest and in transit.**

Google Cloud encrypts all customer data at rest by default, with no action needed. Data moving between Google's facilities and services is also encrypted in transit. The stem mentions both stored files and data "sent between services", which points to both states.

**Why the others are wrong:**
- **A. In transit only**: stored data is also encrypted by default.
- **C. Not encrypted by default**: default encryption is a core Google Cloud security feature.
- **D. At rest only**: data in transit is encrypted as well.

**Remember:** Google Cloud default = encrypted at rest and in transit.

**References:**
- [cloud.google.com/security/encryption](https://cloud.google.com/security/encryption)
- [cloud.google.com/docs/security/encryption/default-encryption](https://cloud.google.com/docs/security/encryption/default-encryption)
- [cloud.google.com/docs/security/encryption-in-transit](https://cloud.google.com/docs/security/encryption-in-transit)

---

## Question 24

*Domain 5: Trust and Security with Google Cloud*

**TrailBee Travel uses Google Cloud to host its booking platform. Before a user can open the internal support dashboard, the platform must confirm that the person signing in is really the claimed user. Which aspect of cloud identity management does this action describe?**

- [ ] A. Authorization
- [x] B. Authentication
- [ ] C. Auditing
- [ ] D. Encrypting

### Explanation

**Correct answer: B. Authentication**

Authentication confirms that users are who they claim to be, for example with a password plus 2-step verification. The clue is "confirm that the person signing in is really the claimed user".

**Why the others are wrong:**
- **A. Authorization**: it decides what an authenticated user is allowed to do, which comes after identity is confirmed.
- **C. Auditing**: it records who did what, for later review.
- **D. Encrypting**: it protects data from being read, it doesn't verify identity.

**Remember:** Authentication = who are you? Authorization = what can you do?

**References:**
- [cloud.google.com/docs/authentication](https://cloud.google.com/docs/authentication)
- [cloud.google.com/iam/docs/overview](https://cloud.google.com/iam/docs/overview)
- [cloud.google.com/identity/docs/overview](https://cloud.google.com/identity/docs/overview)

---

## Question 25

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**NimbusPay Systems runs containerized payment applications in Kubernetes clusters across Google Cloud, another public cloud, and an on-premises environment. The platform team wants one consistent and centralized way to manage these Kubernetes environments. Which Google Cloud service should NimbusPay Systems choose?**

- [ ] A. Cloud Run functions
- [x] B. GKE Enterprise
- [ ] C. Cloud Run
- [ ] D. Compute Engine

### Explanation

**Correct answer: B. GKE Enterprise**

GKE Enterprise (formerly Anthos) gives one consistent way to manage Kubernetes clusters across Google Cloud, other public clouds and on-premises. It centralizes policy, configuration and operations for all of them. The clues are "Kubernetes clusters across... another public cloud, and an on-premises environment" and "centralized".

**Why the others are wrong:**
- **A. Cloud Run functions**: it runs single event-driven functions, not multi-environment cluster management.
- **C. Cloud Run**: it runs serverless containers on Google Cloud, not fleets of clusters across environments.
- **D. Compute Engine**: these are VMs, not a Kubernetes management layer.

**Remember:** Kubernetes everywhere (hybrid/multicloud), managed from one place = GKE Enterprise.

**References:**
- [cloud.google.com/kubernetes-engine/docs/fleets-overview](https://cloud.google.com/kubernetes-engine/docs/fleets-overview)
- [cloud.google.com/kubernetes-engine/multi-cloud/docs](https://cloud.google.com/kubernetes-engine/multi-cloud/docs)
- [cloud.google.com/kubernetes-engine/enterprise/clusters/docs](https://cloud.google.com/kubernetes-engine/enterprise/clusters/docs)

---

## Question 26

*Domain 6: Scaling with Google Cloud Operations*

**CodeNest Retail, an ecommerce company, runs a production application on Google Cloud. The development team wants to inspect how the application code behaves while it is running and analyze the application’s state to find difficult programming bugs. Which Google Cloud tool should CodeNest Retail use?**

- [x] A. Debugger
- [ ] B. Profiler
- [ ] C. Cloud Monitoring
- [ ] D. Trace

### Explanation

**Correct answer: A. Debugger**

Cloud Debugger let developers inspect the state of running code, such as variable values at a line, without stopping the application. That helps find hard bugs in production. The clue is "inspect how the application code behaves while it is running and analyze the application's state".

**Why the others are wrong:**
- **B. Profiler**: it shows which code uses the most CPU and memory, for performance, not bug state.
- **C. Cloud Monitoring**: it tracks metrics and dashboards, not code state.
- **D. Trace**: it measures request latency across services.

**Remember:** Inspect running code state = Debugger. Resource use by code = Profiler. Latency = Trace.

**References:**
- [support.google.com/cloud/answer/6323288](https://support.google.com/cloud/answer/6323288)
- [docs.cloud.google.com/profiler/docs/about-profiler](https://docs.cloud.google.com/profiler/docs/about-profiler)
- [docs.cloud.google.com/trace/docs/overview](https://docs.cloud.google.com/trace/docs/overview)

**⚠️ Note:** Cloud Debugger was shut down in 2023; its open-source successor is Snapshot Debugger. The key describes what it did correctly and the other tools don't fit, so pick it on this exam.

---

## Question 27

*Domain 6: Scaling with Google Cloud Operations*

**FitTrack Labs runs several wellness applications on Google Cloud. The operations team wants to collect, view, and store all logs created by these applications and Google Cloud resources in one centralized service. Which Google Cloud service should FitTrack Labs use?**

- [ ] A. Cloud Profiler
- [ ] B. Cloud Monitoring
- [ ] C. Cloud Trace
- [x] D. Cloud Logging

### Explanation

**Correct answer: D. Cloud Logging**

Cloud Logging collects, stores, searches and analyzes logs from applications and Google Cloud resources in one central place. The clue is "collect, view, and store all logs".

**Why the others are wrong:**
- **A. Cloud Profiler**: it analyzes CPU and memory use by code.
- **B. Cloud Monitoring**: it handles metrics, dashboards and alerts, not log storage.
- **C. Cloud Trace**: it measures request latency across services.

**Remember:** Logs = Cloud Logging. Metrics = Cloud Monitoring.

**References:**
- [cloud.google.com/logging/docs](https://cloud.google.com/logging/docs)
- [cloud.google.com/monitoring/docs](https://cloud.google.com/monitoring/docs)
- [cloud.google.com/trace/docs](https://cloud.google.com/trace/docs)

---

## Question 28

*Domain 1: Digital Transformation with Google Cloud*

**ShopNest has already migrated a few small applications to Google Cloud to reduce short-term costs. The leadership team now wants cloud adoption to become a company-wide transformation that supports innovation and faster delivery. How should the organization adapt its leadership approach?**

- [x] A. Increase visible top-down sponsorship and foster a culture of blamelessness
- [ ] B. Move cloud funding from an operational expenditure model to capital expenditure
- [ ] C. Make cloud adoption primarily driven by individual contributors
- [ ] D. Invest in on-premises infrastructure to redefine relationships between IT and employees

### Explanation

**Correct answer: A. Increase visible top-down sponsorship and foster a culture of blamelessness**

Moving from a few cost-saving migrations to a real transformation needs strong executive support and a culture where people can experiment. A blameless culture lets teams learn from failures instead of hiding them, which drives innovation and faster delivery. The clue is "company-wide transformation".

**Why the others are wrong:**
- **B. Move funding from OpEx to CapEx**: cloud moves spending the other way, toward OpEx.
- **C. Driven mainly by individual contributors**: this is early, tactical adoption in Google's Cloud Adoption Framework; bottom-up effort alone can't change a whole company.
- **D. Invest in on-premises infrastructure**: this goes against cloud adoption.

**Remember:** Transformation = executive sponsorship + blameless, learning culture.

**References:**
- [cloud.google.com/adoption-framework](https://cloud.google.com/adoption-framework)
- [services.google.com/fh/files/misc/google_cloud_adoption_framework_whitepaper.pdf](https://services.google.com/fh/files/misc/google_cloud_adoption_framework_whitepaper.pdf)
- [sre.google/sre-book/postmortem-culture/](https://sre.google/sre-book/postmortem-culture/)

---

## Question 29

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**ShopTrail, an online fashion marketplace, wants to use customer browsing history, previous purchases, and product ratings to improve the shopping experience. Which scenario is a good use case for machine learning?**

- [ ] A. Grouping data when there are no useful past examples or patterns to learn from
- [ ] B. Completing tasks that mainly depend on human judgment, life experience, and intuition
- [x] C. Creating personalized product recommendations for customers
- [ ] D. Making final decisions about complex ethical dilemmas

### Explanation

**Correct answer: C. Creating personalized product recommendations for customers**

ML learns patterns from lots of past data, such as browsing, purchases and ratings, and uses them to predict what each customer will like. Recommendations are a classic ML use case. The clue is the rich historical customer data.

**Why the others are wrong:**
- **A. No useful past examples or patterns**: ML needs data with patterns to learn from.
- **B. Tasks based on human judgment and intuition**: these depend on experience ML doesn't have.
- **D. Final decisions on ethical dilemmas**: these need human accountability, not a model.

**Remember:** Lots of data + patterns + prediction at scale = good ML fit.

**References:**
- [cloud.google.com/learn/what-is-machine-learning](https://cloud.google.com/learn/what-is-machine-learning)
- [cloud.google.com/use-cases/recommendations](https://cloud.google.com/use-cases/recommendations)
- [docs.cloud.google.com/bigquery/docs/recommendation-overview](https://docs.cloud.google.com/bigquery/docs/recommendation-overview)

---

## Question 30

*Domain 5: Trust and Security with Google Cloud*

**ClearPath Analytics stores customer reports and transaction files in Google Cloud. The security team asks why stored data in Google Cloud is protected without every application team manually enabling encryption for each service. What is the main reason?**

- [ ] A. Data is encrypted by Security Command Center
- [ ] B. Data is encrypted by Sensitive Data Protection
- [x] C. Data is encrypted by default
- [ ] D. Data is encrypted when an appropriate tag is applied

### Explanation

**Correct answer: C. Data is encrypted by default**

Google Cloud automatically encrypts all customer data at rest, with no setup by application teams. That is why stored data is protected without anyone turning encryption on per service. The clue is "without every application team manually enabling encryption".

**Why the others are wrong:**
- **A. Security Command Center**: it finds misconfigurations and threats, it doesn't encrypt data.
- **B. Sensitive Data Protection**: it discovers, classifies and masks sensitive data, it isn't the default encryption layer.
- **D. When a tag is applied**: encryption doesn't depend on tags; it is always on.

**Remember:** Google Cloud encryption at rest = automatic, on by default.

**References:**
- [docs.cloud.google.com/docs/security/encryption/default-encryption](https://docs.cloud.google.com/docs/security/encryption/default-encryption)
- [docs.cloud.google.com/security-command-center/docs/security-command-center-overview](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)
- [docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)

---

## Question 31

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**MediScan Analytics is building image-recognition models to help hospitals detect patterns in medical scan images. The team wants to reduce the time required to train these machine learning models on Google Cloud. Which domain-specific hardware is designed for this purpose?**

- [ ] A. Bare Metal Solution
- [ ] B. Spot VMs
- [x] C. Cloud TPUs
- [ ] D. Containers

### Explanation

**Correct answer: C. Cloud TPUs**

Tensor Processing Units are chips Google designed specifically to speed up machine learning training and inference. The clues are "reduce the time required to train" and "domain-specific hardware".

**Why the others are wrong:**
- **A. Bare Metal Solution**: dedicated physical servers for special workloads, not ML-specific chips.
- **B. Spot VMs**: lower-cost VMs that can be stopped at any time. They are a pricing option, not special hardware.
- **D. Containers**: a way to package software, not hardware.

**Remember:** Hardware built for ML = TPU.

**References:**
- [docs.cloud.google.com/tpu/docs/intro-to-tpu](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)
- [cloud.google.com/tpu](https://cloud.google.com/tpu)
- [docs.cloud.google.com/compute/docs/instances/spot](https://docs.cloud.google.com/compute/docs/instances/spot)

---

## Question 32

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**HelpNest, a customer service web platform, wants to introduce a system that can read support tickets, decide the next best action, trigger approved workflows such as refunds or account updates, and close routine issues without a human agent. Which technology best describes this capability?**

- [ ] A. Infrastructure as a Service (IaaS)
- [ ] B. Legacy on-premises computing
- [x] C. Agentic AI
- [ ] D. Open source software

### Explanation

**Correct answer: C. Agentic AI**

Agentic AI systems don't just answer questions. They understand a goal, decide on next steps and take actions through tools and workflows. Here the system reads tickets, picks the next action, triggers refunds or updates, and closes issues on its own. The clue is "decide the next best action" and "trigger approved workflows".

**Why the others are wrong:**
- **A. IaaS**: it is a cloud service model for renting compute, storage and networking.
- **B. Legacy on-premises computing**: it describes where systems run, not an AI capability.
- **D. Open source software**: it describes how software is licensed, not what it does.

**Remember:** AI that plans and takes actions = agentic AI.

**References:**
- [cloud.google.com/discover/what-is-agentic-ai](https://cloud.google.com/discover/what-is-agentic-ai)
- [cloud.google.com/discover/what-are-ai-agents](https://cloud.google.com/discover/what-are-ai-agents)
- [cloud.google.com/learn/what-is-iaas](https://cloud.google.com/learn/what-is-iaas)

---

## Question 33

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**UrbanTrail Logistics, a delivery management company, has begun building cloud-native applications to replace older warehouse and routing systems. What additional step should UrbanTrail Logistics take as part of adopting the cloud?**

- [ ] A. Give third-party partners privileged access to the cloud network.
- [x] B. Move selected legacy infrastructure workloads to the cloud.
- [ ] C. Continue performing maintenance on old on-premises hardware.
- [ ] D. Increase capital spending on existing on-premises projects.

### Explanation

**Correct answer: B. Move selected legacy infrastructure workloads to the cloud.**

Cloud adoption usually has two tracks: build new cloud-native apps and migrate existing workloads. Moving suitable legacy workloads lets the company retire old hardware and get cloud benefits for those systems too. The clue is "additional step" beyond building new apps.

**Why the others are wrong:**
- **A. Give partners privileged access**: this weakens security and isn't an adoption step.
- **C. Keep maintaining old hardware**: this keeps the cost and burden that cloud adoption aims to cut.
- **D. Increase on-premises capital spending**: this moves away from the cloud and its OpEx model.

**Remember:** Cloud adoption = build new cloud-native apps and migrate existing workloads.

**References:**
- [cloud.google.com/learn/cloud-migration](https://cloud.google.com/learn/cloud-migration)
- [docs.cloud.google.com/architecture/migration-to-gcp-getting-started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started)
- [cloud.google.com/adoption-framework](https://cloud.google.com/adoption-framework)

---

## Question 34

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**ModelForge Health, a medical research analytics company, wants to train very large machine learning models for drug discovery. The team needs Google Cloud infrastructure that is purpose-built for AI workloads and combines high-performance hardware, open software, ML frameworks, and flexible ways to consume compute capacity. Which Google Cloud differentiator should the company use?**

- [ ] A. Domain Name Service (DNS)
- [x] B. AI Hypercomputer
- [ ] C. Software as a Service (SaaS)
- [ ] D. Edge locations

### Explanation

**Correct answer: B. AI Hypercomputer**

AI Hypercomputer is Google Cloud's integrated supercomputing architecture for AI. It combines performance-optimized hardware (TPUs and GPUs), open software and ML frameworks, and flexible consumption models. The stem describes exactly these parts for training very large models.

**Why the others are wrong:**
- **A. DNS**: it translates domain names into IP addresses.
- **C. SaaS**: it delivers finished applications, not AI training infrastructure.
- **D. Edge locations**: they cache and deliver content close to users, not train large models.

**Remember:** Hardware + open software + flexible consumption for AI = AI Hypercomputer.

**References:**
- [docs.cloud.google.com/ai-hypercomputer/docs/overview](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)
- [cloud.google.com/ai-infrastructure](https://cloud.google.com/ai-infrastructure)
- [docs.cloud.google.com/ai-hypercomputer/docs/consumption-models](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models)

---

## Question 35

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**GreenCart Labs is building several customer-facing applications for order tracking, product search, and user notifications. Its developers want to use their preferred programming languages and tools, but the company also wants to reduce the amount of time spent managing servers and infrastructure. Which Google Cloud solution should GreenCart Labs use?**

- [x] A. Cloud Run
- [ ] B. Managed Service for Apache Spark
- [ ] C. Pub/Sub
- [ ] D. Bare Metal Solution

### Explanation

**Correct answer: A. Cloud Run**

Cloud Run runs containers in a fully managed, serverless environment. Because anything that can go in a container works, developers can use any language, library or tool they prefer. Google handles servers and scaling. The clues are "preferred programming languages and tools" and "reduce... managing servers".

**Why the others are wrong:**
- **B. Managed Service for Apache Spark**: (Dataproc) it runs Spark and Hadoop data processing jobs, not customer-facing apps.
- **C. Pub/Sub**: it is a messaging service between systems, not an app hosting platform.
- **D. Bare Metal Solution**: dedicated physical servers that you manage, the opposite of the goal.

**Remember:** Any language + no servers to manage = Cloud Run.

**References:**
- [cloud.google.com/run/docs/overview/what-is-cloud-run](https://cloud.google.com/run/docs/overview/what-is-cloud-run)
- [cloud.google.com/products/managed-service-for-apache-spark](https://cloud.google.com/products/managed-service-for-apache-spark)
- [cloud.google.com/pubsub/docs/overview](https://cloud.google.com/pubsub/docs/overview)

---

## Question 36

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**BrightCart, an online retail platform, already uses cloud infrastructure to scale its website during seasonal traffic spikes. The leadership team now wants a technology that can independently plan, reason, and carry out multi-step business tasks such as researching customer segments, preparing sales outreach, and coordinating follow-up actions with minimal human direction. What is this concept called?**

- [x] A. Agentic AI
- [ ] B. Virtual Machines
- [ ] C. Hybrid cloud
- [ ] D. Domain Name Service (DNS)

### Explanation

**Correct answer: A. Agentic AI**

Agentic AI can plan, reason and complete multi-step tasks toward a goal with little human direction. Researching segments, drafting outreach and coordinating follow-ups is a chain of actions an AI agent can carry out. The clue is "independently plan, reason, and carry out multi-step business tasks".

**Why the others are wrong:**
- **B. Virtual Machines**: they are compute resources, not decision-making systems.
- **C. Hybrid cloud**: it combines on-premises and public cloud, an infrastructure model.
- **D. DNS**: it resolves domain names to IP addresses.

**Remember:** Plan + reason + act on multi-step tasks = agentic AI.

**References:**
- [cloud.google.com/discover/what-is-agentic-ai](https://cloud.google.com/discover/what-is-agentic-ai)
- [cloud.google.com/discover/what-are-ai-agents](https://cloud.google.com/discover/what-are-ai-agents)
- [cloud.google.com/products/gemini-enterprise-agent-platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)

---

## Question 37

*Domain 2: Exploring Data Transformation with Google Cloud*

**BlueWave Analytics, a multinational reporting platform, uses Google Cloud along with other cloud providers to manage data across different environments. The company wants its data platforms to work together smoothly, exchange data easily, and avoid vendor lock-in or restrictive technology boundaries. Which Google Cloud differentiator best supports this requirement?**

- [ ] A. AI Hypercomputer
- [x] B. Deep commitment to openness and interoperability
- [ ] C. Shift from OpEx to CapEx
- [ ] D. Bare Metal Solution

### Explanation

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

---

## Question 38

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**GlobeTrek Media, a travel content website, wants hotel chains and tour partners to display its latest destination posts, images, and campaign updates inside their own apps and websites. What should GlobeTrek Media use to share this content smoothly with partner systems?**

- [ ] A. A NoSQL database
- [ ] B. Config Sync
- [ ] C. The App Engine standard environment
- [x] D. An application programming interface

### Explanation

**Correct answer: D. An application programming interface**

An API lets partners' apps and websites request GlobeTrek's latest posts, images and updates automatically. The content stays current without manual copying. The clue is "display... inside their own apps and websites" and "partner systems".

**Why the others are wrong:**
- **A. A NoSQL database**: it stores data, but doesn't by itself give partners a safe way to access it.
- **B. Config Sync**: it keeps Kubernetes cluster configurations consistent, unrelated to sharing content.
- **C. App Engine standard environment**: it hosts web apps, but isn't the mechanism for partner integration.

**Remember:** Share data or content with other companies' systems = API.

**References:**
- [docs.cloud.google.com/api-gateway/docs/glossary](https://docs.cloud.google.com/api-gateway/docs/glossary)
- [docs.cloud.google.com/api-gateway/docs/about-api-gateway](https://docs.cloud.google.com/api-gateway/docs/about-api-gateway)
- [docs.cloud.google.com/appengine/docs/standard/overview](https://docs.cloud.google.com/appengine/docs/standard/overview)

---

## Question 39

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**StreamForge, a video creation app, is launching a generative AI feature that will train and serve large models at scale. Its engineering team needs an integrated Google Cloud architecture that combines purpose-built accelerators such as GPUs and TPUs with open software, ML frameworks, and flexible consumption options. Which Google Cloud offering best fits this requirement?**

- [x] A. AI Hypercomputer
- [ ] B. Cloud Storage Coldline
- [ ] C. Virtual Private Cloud (VPC)
- [ ] D. Google Workspace

### Explanation

**Correct answer: A. AI Hypercomputer**

AI Hypercomputer brings together GPUs and TPUs, open software, ML frameworks and flexible consumption options in one architecture for training and serving large AI models. The stem lists these exact components.

**Why the others are wrong:**
- **B. Cloud Storage Coldline**: a low-cost storage class for rarely accessed data.
- **C. VPC**: it provides private networking for cloud resources, not AI compute.
- **D. Google Workspace**: productivity apps such as Gmail and Docs.

**Remember:** GPUs/TPUs + open software + flexible consumption = AI Hypercomputer.

**References:**
- [docs.cloud.google.com/ai-hypercomputer/docs/overview](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)
- [cloud.google.com/ai-infrastructure](https://cloud.google.com/ai-infrastructure)
- [docs.cloud.google.com/compute/docs/gpus](https://docs.cloud.google.com/compute/docs/gpus)

---

## Question 40

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**PixelTrail, a mobile photo-sharing startup, has developers who build new features on their laptops, but the same code sometimes breaks after release because the production environment has different runtime libraries and package versions. Which technology should PixelTrail use to bundle the application code with its required dependencies so the application behaves consistently across development, testing, and production?**

- [x] A. Containerization
- [ ] B. Serverless computing
- [ ] C. Spot VMs
- [ ] D. Load balancing

### Explanation

**Correct answer: A. Containerization**

A container packages the application code with its libraries and dependencies. The same container runs the same way on a laptop, in testing and in production. The clue is "bundle the application code with its required dependencies" so it "behaves consistently".

**Why the others are wrong:**
- **B. Serverless computing**: it removes server management, but doesn't by itself solve dependency mismatch.
- **C. Spot VMs**: a cheaper VM pricing option, unrelated to packaging.
- **D. Load balancing**: it spreads traffic across instances, not about consistent environments.

**Remember:** "Works on my machine" problems = containers.

**References:**
- [cloud.google.com/learn/what-are-containers](https://cloud.google.com/learn/what-are-containers)
- [cloud.google.com/discover/what-is-containerization](https://cloud.google.com/discover/what-is-containerization)
- [docs.cloud.google.com/load-balancing/docs/load-balancing-overview](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)

---

## Question 41

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**BrightCart, an online grocery app, has hired a small group of data scientists and software engineers. The team is building its own advanced machine learning model by writing custom training code in Gemini Enterprise Agent Platform notebooks. Which service should BrightCart use to train this model?**

- [x] A. Custom training
- [ ] B. AutoML
- [ ] C. Compute Engine
- [ ] D. Prebuilt APIs

### Explanation

**Correct answer: A. Custom training**

Custom training lets data scientists write their own training code and run it on the AI platform (formerly Vertex AI). It gives full control over the model. The clues are "data scientists and software engineers", "advanced" model and "writing custom training code".

**Why the others are wrong:**
- **B. AutoML**: it trains models with little or no code, for teams without deep ML skills.
- **C. Compute Engine**: you could run code on VMs, but it isn't the managed ML training service and adds work.
- **D. Prebuilt APIs**: these are pre-trained models; you don't train them yourself.

**Remember:** ML experts + own code = custom training. No code = AutoML. No training = prebuilt APIs.

**References:**
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/training-guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/training-guide)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning)

---

## Question 42

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**EventEase, a local event venue platform, lets customers reserve halls, meeting rooms, and party spaces online. EventEase has recently partnered with FreshFork Catering so customers can request meals while making a venue reservation. How can EventEase use application programming interfaces (APIs) to create new business value?**

- [ ] A. Use an API to redesign the reservation website for a specific customer segment
- [ ] B. Use an API to discover possible future partnership opportunities
- [ ] C. Use an API to move all customer records into a machine learning model to estimate meal demand
- [x] D. Use an API to connect the venue reservation system with FreshFork Catering’s order request form

### Explanation

**Correct answer: D. Use an API to connect the venue reservation system with FreshFork Catering’s order request form**

APIs let two companies' systems work together. Connecting the reservation system to the caterer's ordering lets customers book a venue and order meals in one flow. That creates new value for both partners. The clue is the new partnership and "request meals while making a venue reservation".

**Why the others are wrong:**
- **A. Redesign the website for a segment**: that is a design task, not what APIs do.
- **B. Discover future partnerships**: APIs connect systems, they don't find business partners.
- **C. Move all records into an ML model**: that is forecasting, not the partner integration described.

**Remember:** New partner + combined customer experience = connect systems with APIs.

**References:**
- [cloud.google.com/apis/docs/overview](https://cloud.google.com/apis/docs/overview)
- [cloud.google.com/api-gateway/docs/about-api-gateway](https://cloud.google.com/api-gateway/docs/about-api-gateway)
- [cloud.google.com/solutions/new-channels-using-apis](https://cloud.google.com/solutions/new-channels-using-apis)

---

## Question 43

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**QuickCart, an online grocery delivery platform, is moving its new microservices into containers. The engineering team expects to run and coordinate several thousand containers and wants a managed Google Cloud service that can automate container deployment, scaling, and operations. Which service should QuickCart choose?**

- [ ] A. Cloud Run functions
- [x] B. Google Kubernetes Engine (GKE)
- [ ] C. Apigee
- [ ] D. BigQuery Omni

### Explanation

**Correct answer: B. Google Kubernetes Engine (GKE)**

GKE is Google's managed Kubernetes service. Kubernetes orchestrates containers: it deploys, scales, heals and manages many containers across a cluster. The clues are "several thousand containers" and "automate container deployment, scaling, and operations".

**Why the others are wrong:**
- **A. Cloud Run functions**: it runs small event-driven functions, not large container orchestration.
- **C. Apigee**: it manages APIs, not containers.
- **D. BigQuery Omni**: it runs BigQuery analytics on data in other clouds.

**Remember:** Orchestrate many containers = Kubernetes = GKE.

**References:**
- [docs.cloud.google.com/kubernetes-engine/docs](https://docs.cloud.google.com/kubernetes-engine/docs)
- [docs.cloud.google.com/functions/docs](https://docs.cloud.google.com/functions/docs)
- [docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)

---

## Question 44

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**NimbusLedger, a small fintech website, is modernizing its development process. Its engineering team wants to adopt software whose source code is available for public review, so developers can study it, change it, improve it, and contribute updates back to the community. Which term best describes this type of technology?**

- [ ] A. Proprietary software
- [x] B. Open source
- [ ] C. Platform as a Service (PaaS)
- [ ] D. Closed standard

### Explanation

**Correct answer: B. Open source**

Open source software has public source code that anyone can view, modify and improve, and contribute changes back to the community. The stem describes this exactly.

**Why the others are wrong:**
- **A. Proprietary software**: the vendor owns and controls the code, which you usually can't see or change.
- **C. PaaS**: it is a cloud service model for running apps, not a licensing model.
- **D. Closed standard**: a specification controlled by one party, the opposite of open.

**Remember:** Public code, anyone can change and contribute = open source.

**References:**
- [opensource.org/osd](https://opensource.org/osd)
- [opensource.google/](https://opensource.google/)
- [cloud.google.com/learn/what-is-paas](https://cloud.google.com/learn/what-is-paas)

---

## Question 45

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**TrailBite, a food delivery website, is losing customers because its legacy data center applications cannot respond quickly to new menu, payment, and delivery feature requests. The company decides to modernize these applications by moving toward cloud-based application architecture. What may have led TrailBite to make this business decision?**

- [ ] A. Its data center applications already scale automatically whenever demand changes.
- [ ] B. It wants to move from a pay-as-you-go model to a capital expenditure model.
- [ ] C. Its application code changes by itself without any developer making updates.
- [x] D. Its data center applications take several weeks to update and release.

### Explanation

**Correct answer: D. Its data center applications take several weeks to update and release.**

Slow release cycles stop a company from responding to customer needs, which is exactly why TrailBite is losing customers. Cloud-based architecture, such as microservices, containers and CI/CD, speeds up changes. The clue is "cannot respond quickly to new... feature requests".

**Why the others are wrong:**
- **A. Already scale automatically**: if they did, that would be a reason not to change.
- **B. Move from pay-as-you-go to CapEx**: cloud moves the other way, toward OpEx.
- **C. Code changes by itself**: this doesn't happen and isn't a business problem.

**Remember:** Slow releases + losing customers = modernize applications.

**References:**
- [cloud.google.com/solutions/application-modernization](https://cloud.google.com/solutions/application-modernization)
- [cloud.google.com/learn/cloud-migration](https://cloud.google.com/learn/cloud-migration)
- [cloud.google.com/learn/what-is-cloud-native](https://cloud.google.com/learn/what-is-cloud-native)

---

## Question 46

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**BrightCart, a small retail mobile app, wants to add image labeling and text sentiment detection using Google Cloud AI services. The team wants these capabilities without building machine learning models from scratch or hiring a dedicated machine learning team. How do ready-to-use Google Cloud AI and machine learning APIs make AI and ML easier for customers to adopt?**

- [x] A. They don't require data science expertise.
- [ ] B. They don't require data input and validation.
- [ ] C. They require fewer security permissions.
- [ ] D. They all require custom training models.

### Explanation

**Correct answer: A. They don't require data science expertise.**

Pre-trained APIs, such as the Vision API and Natural Language API, use models Google has already built and trained. A developer sends an image or text to the API and gets labels or sentiment back. Nobody has to collect training data, design a model or tune it, so no data scientists or ML engineers are needed. The clue is "without building machine learning models from scratch or hiring a dedicated machine learning team".

**Why the others are wrong:**
- **B. Don't require data input and validation**: You still send the images and text to analyze, and you should validate them.
- **C. Fewer security permissions**: Access is still controlled with IAM. That isn't the adoption benefit.
- **D. All require custom training**: The opposite. They are pre-trained.

**Remember:** Pre-trained API = no model building, no data science team. A developer just calls it.

**References:**
- [cloud.google.com/ai/apis](https://cloud.google.com/ai/apis)
- [cloud.google.com/vision/docs](https://cloud.google.com/vision/docs)
- [cloud.google.com/natural-language](https://cloud.google.com/natural-language)

---

## Question 47

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**PayBridge, a digital banking company, has created a controlled API that lets approved personal finance apps retrieve customer transaction information. PayBridge wants to track API traffic, apply access control and security rules, and create pricing plans so external developers can be charged for using the API. Which Google Cloud solution should PayBridge use?**

- [x] A. Apigee API Management
- [ ] B. Google Kubernetes Engine
- [ ] C. Spot VMs
- [ ] D. Cloud Run functions

### Explanation

**Correct answer: A. Apigee API Management**

Apigee is Google Cloud's platform for managing APIs. It tracks traffic and analytics, enforces security and access control, and supports monetization with pricing plans for developers. The stem lists all three: track traffic, access rules, charge developers.

**Why the others are wrong:**
- **B. GKE**: it runs containers, but doesn't manage or monetize APIs.
- **C. Spot VMs**: a low-cost compute pricing option.
- **D. Cloud Run functions**: it runs event-driven code, not API management.

**Remember:** Secure, monitor and monetize APIs = Apigee.

**References:**
- [docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)
- [docs.cloud.google.com/apigee/docs/api-platform/monetization/overview](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/overview)
- [docs.cloud.google.com/apigee/docs/api-platform/develop/policy-attachment-and-enforcement](https://docs.cloud.google.com/apigee/docs/api-platform/develop/policy-attachment-and-enforcement)

---

## Question 48

*Domain 2: Exploring Data Transformation with Google Cloud*

**TrendNest, a retail analytics mobile app, wants to bring together its own customer activity data, partner campaign data, and external market data into one unified cloud environment. The goal is to prepare that combined data so data scientists can efficiently build and train new machine learning models. Which Google Cloud differentiator addresses this requirement?**

- [x] A. AI-ready data cloud
- [ ] B. Global edge network
- [ ] C. Infrastructure as a Service (IaaS)
- [ ] D. Two-step verification (2SV)

### Explanation

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

---

## Question 49

*Domain 2: Exploring Data Transformation with Google Cloud*

**NovaStyle Apparel, a fashion e-commerce company, wants to use advanced generative AI to improve product recommendations, summarize customer feedback, and automate merchandising insights. However, its sales, inventory, customer, and marketing data is fragmented across many systems and stored in different formats. What foundational step should the company take to successfully support this AI transformation?**

- [x] A. Build an AI-ready data platform
- [ ] B. Deploy a multi-cloud network architecture
- [ ] C. Shift operational expenditures to capital expenditures
- [ ] D. Restrict all data access to on-premises environments

### Explanation

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

---

## Question 50

*Domain 5: Trust and Security with Google Cloud*

**FinBridgeIQ, a fintech website, uses an internal LLM-based assistant to help employees search payment reports and customer billing summaries. Security teams discover that an attacker could submit cleverly written prompts that cause the assistant to ignore its original instructions, reveal restricted financial records, or bypass built-in response controls. Which modern cybersecurity threat best describes this risk?**

- [ ] A. Cryptomining
- [ ] B. Distributed Denial-of-Service (DDoS)
- [x] C. LLM attack (prompt injection)
- [ ] D. Ransomware

### Explanation

**Correct answer: C. LLM attack (prompt injection)**

Prompt injection is when an attacker writes inputs that trick a large language model into ignoring its instructions, revealing restricted data or bypassing its safety controls. The stem describes exactly that: "cleverly written prompts" that make the assistant "ignore its original instructions".

**Why the others are wrong:**
- **A. Cryptomining**: attackers secretly use your compute to mine cryptocurrency.
- **B. DDoS**: it floods a service with traffic to make it unavailable.
- **D. Ransomware**: it encrypts data and demands payment.

**Remember:** Malicious prompts that hijack an AI model = prompt injection.

**References:**
- [genai.owasp.org/llmrisk/llm01-prompt-injection/](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- [owasp.org/www-community/attacks/PromptInjection](https://owasp.org/www-community/attacks/PromptInjection)
- [cloud.google.com/security/products/model-armor](https://cloud.google.com/security/products/model-armor)

---
