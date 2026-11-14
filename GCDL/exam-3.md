# Cloud Digital Leader — Practice Exam 3

50 questions.

## Question 1

*Domain 6: Scaling with Google Cloud Operations*

**MediCart, a healthcare shopping website, runs a production application on Google Cloud. Its developers want to understand what Cloud Debugger helped teams do when investigating application behavior. What was the main purpose of Cloud Debugger?**

- [ ] A. Apply code changes instantly in production without affecting the service level objective (SLO).
- [x] B. Inspect running application source code and state in real time without causing user downtime.
- [ ] C. Manage source code repositories and speed up application development.
- [ ] D. Analyze live source code only after the application is taken offline for user downtime.

### Explanation

**Correct answer: B. Inspect running application source code and state in real time without causing user downtime.**

Cloud Debugger let developers take snapshots of a live application's variables and call stack, and add log points, while the app kept serving users. The stem asks about investigating behavior in production, which points to inspecting state without stopping the app.

**Why the others are wrong:**
- **A. Apply code changes instantly in production**: A debugger observes code; it never deployed or changed code.
- **C. Manage source code repositories**: That describes a source repository tool, not a debugger.
- **D. Analyze code only after taking the app offline**: The whole point was to avoid downtime, so this is the opposite.

**Remember:** Debugger = look inside a running app without stopping it.

**⚠️ Note:** Cloud Debugger was deprecated in 2022 and shut down in 2023; its open-source successor is Snapshot Debugger. The answer correctly describes what it did, so pick the keyed answer on this exam.

---

## Question 2

*Domain 1: Digital Transformation with Google Cloud*

**NorthPeak Logistics is moving toward Google Cloud and wants its internal IT team to develop strong cloud skills as part of a long-term business transformation. Leadership wants employees to learn from trusted Google Cloud training content while also sharing knowledge across teams. What should NorthPeak Logistics do?**

- [ ] A. Focus on training existing employees instead of hiring new employees who already have cloud experience.
- [ ] B. Give elevated access to third-party consultants and contractors so they can cover internal IT knowledge gaps.
- [ ] C. Encourage self-directed, separate learning using official training materials.
- [x] D. Build a culture of continuous peer-to-peer learning using official training materials.

### Explanation

**Correct answer: D. Build a culture of continuous peer-to-peer learning using official training materials.**

The stem has two clues: learn from trusted Google Cloud content, and share knowledge across teams. Peer-to-peer learning built on official training covers both. Transformation is about people and culture, not only technology, so a lasting learning culture is the goal.

**Why the others are wrong:**
- **A. Train existing staff instead of hiring**: Training staff is good, but this option says nothing about official content or sharing knowledge.
- **B. Give elevated access to consultants**: It outsources knowledge instead of building internal skills and weakens least privilege.
- **C. Self-directed, separate learning**: It uses official materials but misses the knowledge-sharing part.

**Remember:** Upskilling for transformation = official training + a culture of sharing.

---

## Question 3

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**BrightDesk Assist is building a new support automation platform for its banking clients. Instead of only predicting which customers may complain, the company wants an AI system that can understand a customer’s goal, decide the next steps, call different internal tools, update records, and complete the support workflow with little or no human involvement. Which concept best describes this type of AI capability?**

- [ ] A. Descriptive analytics
- [ ] B. Generative AI
- [x] C. Agentic AI
- [ ] D. Business Intelligence

### Explanation

**Correct answer: C. Agentic AI**

Agentic AI systems pursue a goal on their own. They reason, plan next steps, call tools and APIs, and take actions to complete a workflow with little human help. The clues are "decide the next steps", "call different internal tools" and "complete the workflow".

**Why the others are wrong:**
- **A. Descriptive analytics**: It explains what happened in past data; it takes no actions.
- **B. Generative AI**: It creates content, but on its own it does not plan and act across tools.
- **D. Business Intelligence**: BI is reporting and dashboards for human decision makers.

**Remember:** Goal + plan + use tools + take action = agentic AI.

---

## Question 4

*Domain 2: Exploring Data Transformation with Google Cloud*

**StreamHive, a media learning app, has accumulated a large archive of unstructured files such as recorded lessons, podcasts, images, and raw video clips. The company wants a Google Cloud storage solution that can hold large volumes of these files reliably and cost-effectively. Which storage solution should StreamHive use?**

- [ ] A. Spanner
- [x] B. Cloud Storage
- [ ] C. Bigtable
- [ ] D. Cloud SQL

### Explanation

**Correct answer: B. Cloud Storage**

Cloud Storage is Google Cloud's object storage. It holds any amount of unstructured files such as video, audio and images, with high durability and storage classes that lower cost for rarely used data. The clues are "unstructured files", "large volumes" and "cost-effectively".

**Why the others are wrong:**
- **A. Spanner**: A globally distributed relational database for transactions, not a file store.
- **C. Bigtable**: A NoSQL wide-column database for high-throughput key-value data, not media files.
- **D. Cloud SQL**: A managed relational database for structured, transactional data.

**Remember:** Files, images, video, backups, archives = Cloud Storage.

---

## Question 5

*Domain 2: Exploring Data Transformation with Google Cloud*

**MediRide, a health transportation booking app, forms a partnership with CareInn, a senior living network. CareInn securely shares its resident appointment and stay-preference data directly with MediRide so MediRide can offer better ride packages to shared customers. From MediRide’s perspective, what type of data is this?**

- [ ] A. First-party data
- [x] B. Second-party data
- [ ] C. Third-party data
- [ ] D. Public domain data

### Explanation

**Correct answer: B. Second-party data**

Second-party data is another organization's first-party data that it shares directly with you as a partner. CareInn collected the data from its own residents and shares it straight with MediRide, so for MediRide it is second-party.

**Why the others are wrong:**
- **A. First-party data**: MediRide did not collect it from its own customers.
- **C. Third-party data**: Third-party data is bought from a provider that aggregates data, not shared directly by a partner.
- **D. Public domain data**: This data is private and shared securely, not openly available.

**Remember:** Own customers = first-party. Partner shares directly = second-party. Bought = third-party.

---

## Question 6

*Domain 2: Exploring Data Transformation with Google Cloud*

**BrightCast, a sports highlights streaming website, stores large collections of match commentary audio clips and game replay video files. These files do not follow a fixed table structure or predefined schema, and they are stored along with HTML pages and JSON metadata documents. How should the audio and video files be classified?**

- [ ] A. Structured data
- [ ] B. Semi-structured data
- [x] C. Unstructured data
- [ ] D. Relational data

### Explanation

**Correct answer: C. Unstructured data**

Audio and video files have no fixed schema or rows and columns. That makes them unstructured data. The stem even says they "do not follow a fixed table structure or predefined schema".

**Why the others are wrong:**
- **A. Structured data**: Structured data fits a fixed schema, like tables in a database.
- **B. Semi-structured data**: This fits the JSON metadata and HTML, which have tags or keys, but not the audio and video files.
- **D. Relational data**: Relational data is structured data in related tables.

**Remember:** Audio, video, images, free text = unstructured. JSON, HTML, XML = semi-structured.

---

## Question 7

*Domain 5: Trust and Security with Google Cloud*

**PixelHive Media is building a shared analytics environment on Google Cloud. Its marketing, finance, and engineering teams all need access to the same project, but each team needs different permissions based on the work they perform. What is the fastest and most efficient way to manage access?**

- [x] A. Map IAM roles to job functions for each department.
- [ ] B. Assign IAM basic roles to each employee.
- [ ] C. Apply least-privilege roles separately for each employee.
- [ ] D. Create one shared service account for all departments.

### Explanation

**Correct answer: A. Map IAM roles to job functions for each department.**

Each team needs different permissions, so define roles by what each job requires and grant them per department. This is far easier to manage than handling every person one by one. In practice you put each team in a group and grant the roles to the group.

**Why the others are wrong:**
- **B. Assign basic roles to each employee**: Basic roles (Owner, Editor, Viewer) are too broad and per-person grants don't scale.
- **C. Least-privilege roles separately for each employee**: Least privilege is right, but per-employee management is slow and error-prone.
- **D. One shared service account for all departments**: It removes accountability and gives everyone the same access.

**Remember:** Grant roles by job function to groups, not to individuals.

**⚠️ Note:** Google's stated best practice is to grant roles to groups. Read "map roles to job functions for each department" as the group-based answer. It is the best option here.

---

## Question 8

*Domain 5: Trust and Security with Google Cloud*

**BrightPath Finance is preparing for a Google Cloud compliance review. The audit team is evaluating the company’s network design, identity and access controls, monitoring coverage, and whether security policies are consistently applied across projects and resources. What term best describes this complete view of the company’s cybersecurity readiness?**

- [ ] A. Threat response
- [x] B. Security posture
- [ ] C. Cryptomining
- [ ] D. Digital transformation

### Explanation

**Correct answer: B. Security posture**

Security posture is the overall state of an organization's security: its network design, access controls, monitoring and how consistently policies are applied. The stem asks for a "complete view of cybersecurity readiness", which is the definition of posture.

**Why the others are wrong:**
- **A. Threat response**: That is how you react to an incident, only one part of the picture.
- **C. Cryptomining**: That is an attack type where stolen compute mines cryptocurrency.
- **D. Digital transformation**: That is using technology to change how a business works, not a security term.

**Remember:** Overall security readiness across the environment = security posture.

---

## Question 9

*Domain 2: Exploring Data Transformation with Google Cloud*

**CareBridge Advisors, a healthcare consulting company, needs its employee portal to share and access different volumes of confidential staff documents across offices in several countries. Why would using Cloud Storage be beneficial for CareBridge Advisors?**

- [x] A. It stores geographically distributed copies of data to reduce the risk of loss.
- [ ] B. It provides a paid add-on that turns on data encryption.
- [ ] C. It randomly places data in different storage locations to protect against attacks.
- [ ] D. It has a small minimum storage quantity requirement.

### Explanation

**Correct answer: A. It stores geographically distributed copies of data to reduce the risk of loss.**

Cloud Storage stores data redundantly, and multi-region or dual-region buckets keep copies in separate geographic locations. This protects against loss and suits a company with offices in several countries.

**Why the others are wrong:**
- **B. Paid add-on for encryption**: Google Cloud encrypts all data at rest by default at no extra cost.
- **C. Randomly places data to protect against attacks**: Data placement is based on the location you choose, not random.
- **D. Small minimum storage quantity**: Cloud Storage has no minimum storage quantity; this is not a real feature to rely on.

**Remember:** Cloud Storage = durable, redundant, optionally multi-region object storage.

**⚠️ Note:** Geographically separate copies are only true for multi-region and dual-region buckets. A regional bucket keeps redundant copies across zones in one region. The key is still the best option, so pick it on this exam.

---

## Question 10

*Domain 5: Trust and Security with Google Cloud*

**TrailCart Market runs an online shopping platform on Google Cloud. During a holiday sale, a malicious botnet starts sending a huge volume of fake HTTP requests to the application, trying to exhaust resources and prevent real shoppers from accessing the site. Which Google Cloud service should TrailCart Market use to help protect the application from Distributed Denial-of-Service attacks?**

- [ ] A. Security Command Center
- [x] B. Google Cloud Armor
- [ ] C. Identity-Aware Proxy (IAP)
- [ ] D. Cloud Key Management Service (KMS)

### Explanation

**Correct answer: B. Google Cloud Armor**

Google Cloud Armor protects applications behind Google's load balancers from DDoS attacks and web attacks. It can filter and rate-limit malicious traffic before it reaches the app. The clues are "botnet", "huge volume of fake HTTP requests" and "DDoS".

**Why the others are wrong:**
- **A. Security Command Center**: It gives visibility into security risks and findings; it doesn't block attack traffic.
- **C. Identity-Aware Proxy (IAP)**: It controls who can reach an app based on identity, not volumetric attacks on a public site.
- **D. Cloud KMS**: It manages encryption keys.

**Remember:** DDoS or web attack protection = Cloud Armor.

---

## Question 11

*Domain 6: Scaling with Google Cloud Operations*

**FreshTrail Delivery is running applications and infrastructure on Google Cloud. The operations team wants to understand the health and performance of its services by gathering measurements such as CPU usage, latency, request count, and application-specific values. What does monitoring mean in this cloud operations context?**

- [ ] A. Watching cloud spending in real time to make sure budgets are not exceeded.
- [x] B. Collecting predefined and custom metrics from applications and infrastructure.
- [ ] C. Recording user actions to guarantee compliance with privacy regulations.
- [ ] D. Tracking user locations to document regional access and usage.

### Explanation

**Correct answer: B. Collecting predefined and custom metrics from applications and infrastructure.**

In cloud operations, monitoring means collecting metrics, both built-in ones like CPU and latency and custom application values, to see service health and performance. Cloud Monitoring does this and supports dashboards and alerts.

**Why the others are wrong:**
- **A. Watching cloud spending**: That is cost management or budgets, not operational monitoring.
- **C. Recording user actions for compliance**: That is closer to audit logging.
- **D. Tracking user locations**: That is not what operational monitoring means.

**Remember:** Monitoring = metrics. Logging = events. Tracing = request paths.

---

## Question 12

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**FitFleet, a fitness tracking mobile app, runs its backend microservices on Google Kubernetes Engine. Developers frequently test fixes for application issues and want a platform that helps them deploy, validate, and adjust changes quickly. What makes Google Kubernetes Engine an effective solution for these developers?**

- [x] A. It shortens the time required to test and refine different fixes.
- [ ] B. It automatically provides intelligent recommendations to redesign application code.
- [ ] C. It eliminates the requirement to package applications into containers.
- [ ] D. It keeps application source code copied across multiple servers for cross-team collaboration.

### Explanation

**Correct answer: A. It shortens the time required to test and refine different fixes.**

GKE runs containers and supports fast, repeatable deployments, rolling updates and easy rollbacks. That lets developers deploy a fix, check it, and adjust quickly. The clue is "deploy, validate, and adjust changes quickly".

**Why the others are wrong:**
- **B. Recommendations to redesign code**: GKE runs workloads; it does not review or redesign code.
- **C. Eliminates packaging into containers**: GKE runs containers, so packaging into containers is required.
- **D. Copies source code across servers**: GKE runs container images, not shared copies of source code for collaboration.

**Remember:** GKE = fast, consistent container deployments and rollbacks.

**⚠️ Note:** The keyed answer is vague. Faster testing is a general benefit of containers and CI/CD, not something only GKE provides. It is keyed because the other options are clearly false.

---

## Question 13

*Domain 6: Scaling with Google Cloud Operations*

**FitTrackGo, a fitness tracking mobile app, runs several customer-facing services on Google Cloud. The operations team wants to measure the main SRE golden signals for the platform. They specifically need to identify how much of the available infrastructure capacity is being used and whether resources such as CPU, memory, or I/O are becoming constrained. Which metric should they focus on?**

- [ ] A. Latency
- [ ] B. Traffic
- [x] C. Saturation
- [ ] D. Errors

### Explanation

**Correct answer: C. Saturation**

Saturation measures how full the system is: how much CPU, memory or I/O capacity is used and whether it is becoming a constraint. The clues are "how much of the available capacity is being used" and "constrained".

**Why the others are wrong:**
- **A. Latency**: Latency is how long a request takes.
- **B. Traffic**: Traffic is how much demand hits the system, such as requests per second.
- **D. Errors**: Errors is the rate of failed requests.

**Remember:** Four golden signals: latency (time), traffic (demand), errors (failures), saturation (how full).

---

## Question 14

*Domain 6: Scaling with Google Cloud Operations*

**QuickFare, a ride-booking website, runs its checkout, driver-matching, pricing, and notification features as separate microservices on Google Cloud. The engineering team is investigating slow requests and wants to see how a single customer request moves through each service and how much time is spent at every step. Which Google Cloud tool should they use?**

- [x] A. Cloud Trace
- [ ] B. Cloud Profiler
- [ ] C. Cloud Logging
- [ ] D. Google Kubernetes Engine (GKE)

### Explanation

**Correct answer: A. Cloud Trace**

Cloud Trace is distributed tracing. It follows a single request as it moves through each microservice and shows how much time each step takes. The clues are "how a single request moves through each service" and "time spent at every step".

**Why the others are wrong:**
- **B. Cloud Profiler**: It shows which code functions use the most CPU or memory, not the request path across services.
- **C. Cloud Logging**: It stores log events but doesn't map a request's timing across services.
- **D. GKE**: It runs containers; it is not an observability tool.

**Remember:** Slow request across microservices = Cloud Trace.

---

## Question 15

*Domain 2: Exploring Data Transformation with Google Cloud*

**Trendora, a regional fashion marketplace, is building a new ecommerce application on Google Cloud. The application needs a cost-effective transactional database for customer orders, carts, and payments, and it will serve users only from one region. Which service should Trendora use?**

- [ ] A. BigQuery
- [ ] B. Bigtable
- [ ] C. Spanner
- [x] D. Cloud SQL

### Explanation

**Correct answer: D. Cloud SQL**

Cloud SQL is a managed relational database for transactional (OLTP) workloads like orders and payments. It is cost-effective when the app serves one region. The clues are "transactional", "cost-effective" and "only from one region".

**Why the others are wrong:**
- **A. BigQuery**: A data warehouse for analytics, not an app's transactional database.
- **B. Bigtable**: A NoSQL database for huge, high-throughput key-value data, not relational transactions.
- **C. Spanner**: Relational and transactional, but built for global scale; more than a single-region store needs.

**Remember:** Relational + regional + cost-effective = Cloud SQL. Relational + global scale = Spanner.

---

## Question 16

*Domain 2: Exploring Data Transformation with Google Cloud*

**StyleNest, an online apparel store, is training a machine learning model to suggest relevant products to shoppers. The training dataset includes customers’ past purchases and browsing behavior, but it is missing profile attributes such as age group, gender, and location. The recommendation results are weak because an important part of the dataset was not included. Which data quality dimension is causing the poor model performance?**

- [ ] A. Validity
- [ ] B. Accuracy
- [ ] C. Timeliness
- [x] D. Completeness

### Explanation

**Correct answer: D. Completeness**

Completeness asks whether all the required data is present. Profile attributes like age group, gender and location are missing, so the dataset is incomplete. The clue is "an important part of the dataset was not included".

**Why the others are wrong:**
- **A. Validity**: Validity is whether values follow the expected format or rules.
- **B. Accuracy**: Accuracy is whether values are correct, not whether they exist.
- **C. Timeliness**: Timeliness is whether data is current and available when needed.

**Remember:** Missing data = completeness. Wrong values = accuracy. Wrong format = validity.

---

## Question 17

*Domain 6: Scaling with Google Cloud Operations*

**PulseCart, a mobile shopping app, wants to improve how it releases application updates. The engineering team wants to reduce user disruption when bugs appear after a release. What DevOps practice should PulseCart use while developing its application?**

- [ ] A. Pause production until all bugs have been eliminated
- [ ] B. Prioritize fixing large bugs during production because they are easier to review
- [x] C. Implement small changes incrementally to reduce recovery time when bugs appear
- [ ] D. Implement large changes together to make rolling back easier when bugs appear

### Explanation

**Correct answer: C. Implement small changes incrementally to reduce recovery time when bugs appear**

A core DevOps and SRE practice is to ship small, frequent changes. Small changes are easier to test, easier to find the cause of a bug in, and faster to roll back. That reduces disruption to users.

**Why the others are wrong:**
- **A. Pause production until all bugs are gone**: Bug-free software is not realistic; this stops delivery.
- **B. Prioritize fixing large bugs in production**: Large changes and bugs are harder to review, not easier.
- **D. Large changes together make rollback easier**: Large batches make rollback harder and riskier.

**Remember:** Small, incremental releases = faster recovery, less risk.

---

## Question 18

*Domain 6: Scaling with Google Cloud Operations*

**CityParkPass, a parking reservation mobile app, has recently launched on Google Cloud. The operations team is reviewing the service’s reliability signals and is specifically tracking how much time passes between a user sending a request and the application returning a response. Which performance metric are they measuring?**

- [ ] A. Traffic
- [ ] B. Saturation
- [x] C. Latency
- [ ] D. Error rate

### Explanation

**Correct answer: C. Latency**

Latency is the time between a request and its response. The stem describes exactly that: "how much time passes between a user sending a request and the application returning a response".

**Why the others are wrong:**
- **A. Traffic**: Traffic measures demand, such as requests per second.
- **B. Saturation**: Saturation measures how full the system's resources are.
- **D. Error rate**: Error rate measures how many requests fail.

**Remember:** Wait time = latency.

---

## Question 19

*Domain 5: Trust and Security with Google Cloud*

**LogiNest Retail uses Google Security Operations to strengthen its Cloud SecOps program. The security team depends on analyzed information about attacker goals, common targets, malware campaigns, tactics, techniques, and procedures so they can detect risks earlier and defend the environment proactively. What is this type of cybersecurity information called?**

- [x] A. Threat intelligence
- [ ] B. Threat response
- [ ] C. Compliance auditing
- [ ] D. Identity management

### Explanation

**Correct answer: A. Threat intelligence**

Threat intelligence is analyzed information about attackers: their goals, targets, malware campaigns and tactics, techniques and procedures (TTPs). Security teams use it to detect and stop threats earlier. Google Security Operations includes threat intelligence from Google and Mandiant.

**Why the others are wrong:**
- **B. Threat response**: That is acting on an incident, not the information used to anticipate it.
- **C. Compliance auditing**: That checks controls against regulations or standards.
- **D. Identity management**: That controls user identities and access.

**Remember:** Knowledge about attackers and their methods = threat intelligence.

---

## Question 20

*Domain 5: Trust and Security with Google Cloud*

**MedNest Health has strong internal security controls for its Google Cloud environment, but it recently experienced a data exposure incident. The investigation found that attackers entered through a small appointment-booking plugin from an outside vendor that was connected to MedNest Health’s software delivery process. Which modern cybersecurity threat vector does this situation demonstrate?**

- [x] A. Unsecured third-party systems
- [ ] B. Physical damage
- [ ] C. LLM attacks
- [ ] D. Zero trust architecture

### Explanation

**Correct answer: A. Unsecured third-party systems**

The attackers came in through an outside vendor's plugin connected to the software delivery process. That is a supply chain risk from an unsecured third-party system. Your security is only as strong as the vendors and components you connect to.

**Why the others are wrong:**
- **B. Physical damage**: Nothing physical happened; this was a software entry point.
- **C. LLM attacks**: No AI model or prompt was involved.
- **D. Zero trust architecture**: Zero trust is a security model, not a threat vector.

**Remember:** Breach through a vendor's plugin or library = third-party / supply chain risk.

---

## Question 21

*Domain 6: Scaling with Google Cloud Operations*

**QuickCartPay is a payment-processing website that runs business-critical services on Google Cloud in production. The operations team needs the fastest support response for urgent incidents and also wants guidance from a dedicated Technical Account Manager. Which Google Cloud Customer Care service level should QuickCartPay choose?**

- [ ] A. Enhanced
- [ ] B. Basic
- [x] C. Premium
- [ ] D. Standard

### Explanation

**Correct answer: C. Premium**

Premium Support is the Customer Care tier for business-critical workloads. It has the fastest response for critical issues and includes a dedicated Technical Account Manager (TAM). The clues are "fastest support response" and "dedicated Technical Account Manager".

**Why the others are wrong:**
- **A. Enhanced**: Faster than Standard, but it has no dedicated TAM and isn't the fastest.
- **B. Basic**: Basic covers billing support and documentation, not technical incident response.
- **D. Standard**: Meant for smaller workloads with slower response times and no TAM.

**Remember:** Fastest response + TAM = Premium.

---

## Question 22

*Domain 1: Digital Transformation with Google Cloud*

**Northstar Clinics runs some sensitive patient-management systems in its own private data center, but it also wants to use Google Cloud services for analytics, application scaling, and newer digital services. The company wants an architecture that lets it use both environments together. What kind of architecture does a hybrid cloud offer Northstar Clinics?**

- [ ] A. A combination of different virtualized servers
- [ ] B. A combination of serverless computing and public cloud services
- [x] C. A combination of private cloud infrastructure and public cloud services
- [ ] D. A combination of multiple public cloud provider services

### Explanation

**Correct answer: C. A combination of private cloud infrastructure and public cloud services**

Hybrid cloud combines on-premises or private cloud infrastructure with public cloud services, working together. Northstar keeps sensitive systems in its own data center and uses Google Cloud for analytics and new services, which is hybrid.

**Why the others are wrong:**
- **A. Different virtualized servers**: Virtualization alone doesn't make an architecture hybrid.
- **B. Serverless plus public cloud**: Serverless runs in the public cloud, so this is just public cloud.
- **D. Multiple public cloud providers**: That is multicloud, not hybrid.

**Remember:** Hybrid = on-prem/private + public. Multicloud = more than one public cloud.

---

## Question 23

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**ClearNest Realty runs an internal portal where field agents upload apartment photos after site visits. The compliance team currently reviews every image manually because some photos may accidentally include sensitive documents, such as national ID cards or payment cards. ClearNest wants its developers to add automated image analysis to the portal as quickly as possible, without building and training a custom model. Which solution should ClearNest use?**

- [x] A. Pre-trained APIs
- [ ] B. AutoML
- [ ] C. Custom training
- [ ] D. BigQuery ML

### Explanation

**Correct answer: A. Pre-trained APIs**

Pre-trained APIs such as the Cloud Vision API are ready-to-use models that developers call directly. They can detect text and objects in images with no training. The clues are "as quickly as possible" and "without building and training a custom model".

**Why the others are wrong:**
- **B. AutoML**: AutoML still needs labeled data and training a custom model.
- **C. Custom training**: This takes the most time and ML expertise.
- **D. BigQuery ML**: It trains models with SQL on data in BigQuery, not a ready-made image analysis service.

**Remember:** Common task + fastest + no training = pre-trained API.

---

## Question 24

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**StorySpark is a content creation app that wants to explain a basic AI concept to its new product team. The team needs to understand what type of AI can produce new outputs such as text, images, audio, code, or summaries based on user prompts. What is generative AI?**

- [ ] A. A machine learning model used only for language translation
- [x] B. A specific field of AI that can be used to create content
- [ ] C. A general term that includes every type of machine learning algorithm
- [ ] D. An AI model used only for labeling images

### Explanation

**Correct answer: B. A specific field of AI that can be used to create content**

Generative AI is a subset of AI that creates new content, such as text, images, audio, code and summaries, from prompts. The stem's clue is "produce new outputs".

**Why the others are wrong:**
- **A. Only for language translation**: Translation is one possible use, not the definition.
- **C. Includes every type of ML algorithm**: Generative AI is a subset of ML, not the umbrella term.
- **D. Only for labeling images**: Labeling images is classification, a different task.

**Remember:** Generative AI = creates new content.

---

## Question 25

*Domain 6: Scaling with Google Cloud Operations*

**MetroNest Apps runs several workloads on Google Cloud for its product, finance, and customer support teams. Recently, leadership noticed that some teams are spending more than expected, but the teams do not clearly see how their usage affects the monthly bill. What should MetroNest Apps do to help control cloud costs?**

- [ ] A. Improve the physical server purchasing process to reduce costs.
- [x] B. Share cost views with each department to create more accountability.
- [ ] C. Change the cost model from operational expenditure to capital expenditure.
- [ ] D. Apply one common tag to every cloud resource.

### Explanation

**Correct answer: B. Share cost views with each department to create more accountability.**

Teams can't control costs they can't see. Giving each department visibility into its own spending creates accountability and drives better decisions. This is a core FinOps idea: shared responsibility for cloud costs.

**Why the others are wrong:**
- **A. Improve physical server purchasing**: Buying physical servers isn't part of cloud cost control.
- **C. Change from OpEx to CapEx**: Cloud is OpEx by nature; switching models doesn't fix visibility.
- **D. One common tag on every resource**: One tag for everything can't separate costs by team. Labels must differ per team to help.

**Remember:** Visibility per team = accountability = cost control.

---

## Question 26

*Domain 2: Exploring Data Transformation with Google Cloud*

**TrailPulse is a fitness tracking app that receives live activity events from thousands of users, such as step counts, heart-rate readings, and GPS updates. The analytics team wants to analyze these incoming events as they arrive so the app can show near real-time insights. What is a defining function of streaming analytics?**

- [x] A. Processing data records continuously
- [ ] B. Processing data records in batches
- [ ] C. Processing a single historical data reload
- [ ] D. Accessing data with high latency

### Explanation

**Correct answer: A. Processing data records continuously**

Streaming analytics processes events continuously as they arrive, so insights are available in near real time. The clue is "analyze these incoming events as they arrive".

**Why the others are wrong:**
- **B. Processing in batches**: Batch processing collects data and handles it later in groups.
- **C. A single historical data reload**: That is a one-time batch load, not streaming.
- **D. Accessing data with high latency**: Streaming aims for low latency.

**Remember:** Streaming = continuous, as it arrives. Batch = scheduled groups.

---

## Question 27

*Domain 5: Trust and Security with Google Cloud*

**ParcelPilot, a delivery tracking website, is hosting its application on Google Cloud. The security team wants to define which incoming and outgoing network traffic should be allowed or denied before users and systems can reach the application. Which security measure should ParcelPilot use?**

- [ ] A. 2-Step Verification
- [ ] B. Privileged access
- [ ] C. Encryption keys
- [x] D. Firewall rules

### Explanation

**Correct answer: D. Firewall rules**

Firewall rules define which incoming and outgoing network traffic is allowed or denied for your resources. The clue is "incoming and outgoing network traffic should be allowed or denied".

**Why the others are wrong:**
- **A. 2-Step Verification**: It confirms a user's identity at sign-in; it doesn't filter network traffic.
- **B. Privileged access**: That is about elevated permissions for users.
- **C. Encryption keys**: They protect data confidentiality, not traffic flow.

**Remember:** Allow or deny network traffic = firewall rules.

---

## Question 28

*Domain 5: Trust and Security with Google Cloud*

**StreamWave, a video streaming platform, plans to expand its service to viewers in multiple countries. The company wants to use cloud capabilities to help meet global compliance and data protection expectations for customer information. What should StreamWave do?**

- [x] A. Automatically encrypt personally identifiable information.
- [ ] B. Obtain a business license before launching in each new market.
- [ ] C. Allow users to turn off two-factor authentication.
- [ ] D. Follow only the data policies of the country where the company headquarters is registered.

### Explanation

**Correct answer: A. Automatically encrypt personally identifiable information.**

Protecting personal data is a key part of data protection rules in many countries. Encrypting PII protects it if it is accessed without permission. It is the only option that uses cloud capabilities to protect customer data.

**Why the others are wrong:**
- **B. Obtain a business license**: A legal step, but it doesn't protect customer data.
- **C. Let users turn off two-factor authentication**: This weakens security.
- **D. Follow only headquarters' data policies**: Companies must respect the laws of every country where they serve users.

**Remember:** Global data protection starts with protecting PII; ignoring local laws or weakening auth is always wrong.

**⚠️ Note:** Encryption alone doesn't meet global compliance. Data residency, consent and local rules matter too, and Google Cloud already encrypts all data at rest by default. Pick the keyed answer because the other options are clearly worse.

---

## Question 29

*Domain 1: Digital Transformation with Google Cloud*

**BrightBasket, an online grocery marketplace, uses traditional technology to host its ecommerce website. During holiday sales, the company often buys too much capacity or does not have enough capacity for sudden traffic spikes. BrightBasket has decided to move its website to cloud technology. What aspect of cloud technology will benefit BrightBasket’s ecommerce business?**

- [x] A. Agile infrastructure means that they only pay for what they need, when they need it.
- [ ] B. Operational expenditure means that their total cost of ownership is more predictable.
- [ ] C. Unlimited storage means that their website will never experience downtime.
- [ ] D. Shared responsibility means that the cloud provider gives increased visibility during traffic spikes.

### Explanation

**Correct answer: A. Agile infrastructure means that they only pay for what they need, when they need it.**

The problem is buying too much capacity or too little for traffic spikes. Cloud resources scale up and down with demand, and you pay only for what you use. That removes the need to guess capacity in advance.

**Why the others are wrong:**
- **B. OpEx makes TCO more predictable**: Pay-per-use costs can vary more, and OpEx doesn't solve the capacity problem.
- **C. Unlimited storage means no downtime**: Storage has nothing to do with downtime, and no system has zero downtime.
- **D. Shared responsibility gives visibility during spikes**: Shared responsibility splits security duties; it isn't about visibility or traffic.

**Remember:** Over- or under-provisioning problem = elastic scaling + pay for what you use.

**⚠️ Note:** "Agile infrastructure" is loose wording. The real ideas are elasticity and consumption-based pricing. It is still the best of the options, so pick it on this exam.

---

## Question 30

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**CedarPeak Insurance currently runs a claims-processing system in its own data center. The company wants to build a new cloud-native application on Google Cloud that will eventually replace the existing on-premises system. Which application modernization approach should CedarPeak Insurance use?**

- [ ] A. Move the application to Google Cloud, and then change it.
- [ ] B. Change the application first, and then move it to Google Cloud.
- [ ] C. Invent in greenfield.
- [x] D. Invent in brownfield.

### Explanation

**Correct answer: D. Invent in brownfield.**

In Google's framing, "invent in brownfield" means building a new cloud-native application that will replace an existing legacy system. The clue is a new app on Google Cloud that "will eventually replace the existing on-premises system".

**Why the others are wrong:**
- **A. Move, then change**: This migrates the existing app first (lift and shift, then modernize); the stem builds a new app instead.
- **B. Change, then move**: This modernizes the existing app before migrating it; again, not building new.
- **C. Invent in greenfield**: Greenfield means no existing system at all; here one exists and will be replaced.

**Remember:** New app, nothing existing = greenfield. New app that replaces a legacy one = brownfield.

---

## Question 31

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**BlueTrail Logistics runs several warehouse applications in its private data center, but the company also wants to build and run newer applications on Google Cloud. It needs a hybrid-cloud management solution that can help teams manage applications consistently across on-premises and cloud environments. What solution should BlueTrail Logistics use?**

- [x] A. GKE Enterprise
- [ ] B. Cloud Run functions
- [ ] C. App Engine
- [ ] D. Compute Engine

### Explanation

**Correct answer: A. GKE Enterprise**

GKE Enterprise (formerly Anthos) is Google Cloud's platform for managing applications and Kubernetes clusters consistently across on-premises, Google Cloud and other clouds. The clue is "hybrid-cloud management" across "on-premises and cloud environments".

**Why the others are wrong:**
- **B. Cloud Run functions**: Serverless functions that run in Google Cloud, not a hybrid management platform.
- **C. App Engine**: A serverless app platform that runs only in Google Cloud.
- **D. Compute Engine**: Virtual machines in Google Cloud; it doesn't manage on-premises environments.

**Remember:** Consistent management across on-prem and clouds = GKE Enterprise.

---

## Question 32

*Domain 1: Digital Transformation with Google Cloud*

**QuickServeNow runs a food delivery mobile app from its own data center. The company is moving the app to Google Cloud so it can reduce hardware management and scale more easily. After the migration, which change will QuickServeNow need to adapt to?**

- [ ] A. Paying compensation for Google Cloud service outages
- [ ] B. Managing Google Cloud’s underlying network infrastructure
- [x] C. Adjusting to a consumption-based pay-as-you-go spending model
- [ ] D. Optimizing the physical storage systems that run Google Cloud

### Explanation

**Correct answer: C. Adjusting to a consumption-based pay-as-you-go spending model**

On premises, QuickServeNow bought hardware up front. On Google Cloud it pays for what it uses each month, so costs now go up and down with usage. Finance and engineering teams have to adapt: track spending continuously, set budgets and alerts, and design for cost as well as performance.

**Why the others are wrong:**
- **A. Paying compensation for outages**: The provider gives service credits under its SLA. The customer never pays for the provider's outages.
- **B. Managing Google's network**: Google runs its own network infrastructure.
- **D. Optimizing Google's physical storage**: The physical hardware is Google's responsibility.

**Remember:** Moving to cloud = CapEx up front becomes OpEx pay-as-you-go, and the business must learn to manage variable spending.

---

## Question 33

*Domain 2: Exploring Data Transformation with Google Cloud*

**FitCart, a grocery delivery mobile app, is documenting how customer order data is first collected from app events, then cleaned and standardized in analytics pipelines, and finally used by a recommendation model to suggest products. What is this end-to-end view of how data is collected, transformed, and used called?**

- [ ] A. Cloud resource hierarchy
- [ ] B. Compute modernization
- [x] C. The data supply chain
- [ ] D. Multi-cloud networking

### Explanation

**Correct answer: C. The data supply chain**

The data supply chain (also called the data value chain) is the end-to-end journey of data: collected, processed and transformed, stored, then used for analytics or AI. The stem walks through exactly that path from app events to a recommendation model.

**Why the others are wrong:**
- **A. Cloud resource hierarchy**: That organizes Google Cloud resources into organization, folders and projects.
- **B. Compute modernization**: That is about updating how applications run, not data flow.
- **D. Multi-cloud networking**: That connects networks across cloud providers.

**Remember:** Collect, transform, use: the end-to-end data journey = data supply chain.

---

## Question 34

*Domain 2: Exploring Data Transformation with Google Cloud*

**StreamHive, a music analytics startup, wants to execute Apache Spark batch jobs on Google Cloud for playlist trend analysis. The engineering team does not want to create, operate, scale, or tune Spark clusters, and prefers a fully serverless option where they only submit the workload. Which service should they choose?**

- [ ] A. Managed Service for Apache Spark on clusters
- [x] B. Managed Service for Apache Spark serverless deployment
- [ ] C. Cloud SQL
- [ ] D. Compute Engine

### Explanation

**Correct answer: B. Managed Service for Apache Spark serverless deployment**

The serverless option of Managed Service for Apache Spark (formerly Dataproc) runs Spark batch jobs without any clusters to create or manage. You submit the workload and Google handles the infrastructure and scaling. The clues are "does not want to create, operate, scale, or tune Spark clusters" and "fully serverless".

**Why the others are wrong:**
- **A. Managed Service for Apache Spark on clusters**: It still requires creating and sizing clusters.
- **C. Cloud SQL**: A relational database; it doesn't run Spark jobs.
- **D. Compute Engine**: You'd have to build and run your own Spark cluster on VMs, which is the most work.

**Remember:** Spark with no clusters to manage = the serverless option.

---

## Question 35

*Domain 6: Scaling with Google Cloud Operations*

**MetroCart, a grocery delivery mobile app, wants to reduce the amount of manual operational work its engineering team performs every week. The team wants to follow a site reliability engineering practice that improves operational efficiency. Which SRE best practice should MetroCart adopt?**

- [ ] A. Rely less on operational data when deciding what to improve.
- [ ] B. Give developers sole responsibility for production systems.
- [ ] C. Reduce the effort spent understanding the impact of outages.
- [x] D. Prioritize automating repetitive toil.

### Explanation

**Correct answer: D. Prioritize automating repetitive toil.**

In SRE, toil is manual, repetitive operational work that adds no lasting value. SRE teams aim to automate it so engineers can spend time on improvements. The clue is "reduce the amount of manual operational work".

**Why the others are wrong:**
- **A. Rely less on operational data**: SRE is data-driven; decisions rely on metrics and SLOs.
- **B. Give developers sole responsibility**: SRE is about shared ownership between developers and operations.
- **C. Reduce effort understanding outages**: SRE uses blameless postmortems to learn from outages, not ignore them.

**Remember:** Manual, repetitive work = toil. SRE answer = automate it.

---

## Question 36

*Domain 6: Scaling with Google Cloud Operations*

**CraftlyPay, a creator marketplace, earns most of its revenue from commissions on monthly sales. Because sales volume changes a lot from month to month, the company is having trouble predicting and controlling its Google Cloud costs. How can CraftlyPay optimize the use of its cloud resources?**

- [x] A. By applying intelligent recommendations
- [ ] B. By decentralizing financial decision making
- [ ] C. By sharing project ownership across all teams
- [ ] D. By increasing their capital expenditure

### Explanation

**Correct answer: A. By applying intelligent recommendations**

Google Cloud's intelligent recommendations (Active Assist and Recommender) analyze usage and suggest actions, such as resizing oversized VMs or removing idle resources. That helps match resources to changing demand and control costs.

**Why the others are wrong:**
- **B. Decentralizing financial decisions**: This tends to make costs less controlled, not more.
- **C. Sharing project ownership across all teams**: Broad ownership blurs accountability and doesn't optimize resources.
- **D. Increasing capital expenditure**: Buying up front is the opposite of matching cloud use to variable demand.

**Remember:** Variable demand + optimize resources = intelligent recommendations.

---

## Question 37

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**FleetNest, a logistics tracking company, runs a custom in-house routing application that needs detailed control over the virtual machines, operating system configuration, networking, and machine types. The team also wants the infrastructure to support autoscaling and automatic rolling updates. Which Google Cloud product or solution should FleetNest use?**

- [ ] A. Cloud Build
- [ ] B. Cloud Run
- [x] C. Compute Engine
- [ ] D. App Engine

### Explanation

**Correct answer: C. Compute Engine**

Compute Engine gives full control over virtual machines, including the operating system, machine types and networking. With managed instance groups it also supports autoscaling and automatic rolling updates. The clue is "detailed control over the virtual machines".

**Why the others are wrong:**
- **A. Cloud Build**: A CI/CD service that builds and tests code; it doesn't host the application.
- **B. Cloud Run**: Serverless containers; you don't control the VMs or OS.
- **D. App Engine**: A serverless app platform that hides the underlying VMs.

**Remember:** Need control of VMs and OS = Compute Engine.

---

## Question 38

*Domain 2: Exploring Data Transformation with Google Cloud*

**TrustLedger Bank, a digital lending platform, is preparing to launch AI agents that can help employees analyze customer risk and automate routine financial workflows. Before deployment, the bank is unifying fragmented datasets, applying strong governance controls, improving data quality, and making trusted data easier for teams to discover and use. What is TrustLedger Bank creating?**

- [ ] A. A legacy data center
- [x] B. An AI-ready data foundation
- [ ] C. A hardware-defined network
- [ ] D. A perimeter security model

### Explanation

**Correct answer: B. An AI-ready data foundation**

An AI-ready data foundation is data that is unified, clean, governed and easy to discover, so AI and agents can use it reliably. The bank is unifying datasets, applying governance and improving quality before launching AI agents, which is exactly that.

**Why the others are wrong:**
- **A. A legacy data center**: The bank is modernizing, not building old on-premises infrastructure.
- **C. A hardware-defined network**: The work is about data, not networking.
- **D. A perimeter security model**: That is an older security approach, unrelated to preparing data for AI.

**Remember:** Unified, clean, governed data before AI = AI-ready data foundation.

---

## Question 39

*Domain 2: Exploring Data Transformation with Google Cloud*

**FinoraCart is modernizing a legacy enterprise transaction database for its retail payment platform on Google Cloud. The team needs very high performance and availability, but they also want to stay aligned with an open-source database engine so they can reduce the risk of restrictive vendor lock-in. Which Google Cloud service should they choose?**

- [ ] A. Bigtable
- [ ] B. Spanner
- [x] C. AlloyDB for PostgreSQL
- [ ] D. Firestore in Datastore mode

### Explanation

**Correct answer: C. AlloyDB for PostgreSQL**

AlloyDB for PostgreSQL is a fully managed, PostgreSQL-compatible database built for high performance and availability on enterprise transactional workloads. Because it is compatible with open-source PostgreSQL, apps and skills can move more easily, which reduces lock-in. The clues are "very high performance and availability" and "open-source database engine".

**Why the others are wrong:**
- **A. Bigtable**: A NoSQL wide-column database; it isn't relational or based on an open-source SQL engine.
- **B. Spanner**: High performance and availability, but its own Google-built engine; less closely tied to open-source PostgreSQL.
- **D. Firestore in Datastore mode**: A NoSQL document database, not for enterprise relational transactions.

**Remember:** Enterprise performance + PostgreSQL compatibility = AlloyDB.

**⚠️ Note:** AlloyDB itself is not open source. It is compatible with open-source PostgreSQL, which is what "aligned with an open-source engine" means. Spanner also offers a PostgreSQL interface, but AlloyDB is the closer fit, so pick it on this exam.

---

## Question 40

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**GlowTrail Media is adopting AI for its creative and engineering teams. The company wants a system that can produce new campaign emails, generate product banner images, and create sample application code from user prompts. Which branch of artificial intelligence is focused on creating new content like this?**

- [x] A. Generative AI (gen AI)
- [ ] B. Predictive analytics
- [ ] C. Data warehousing
- [ ] D. Relational databases

### Explanation

**Correct answer: A. Generative AI (gen AI)**

Generative AI creates new content such as text, images and code from prompts. Emails, banner images and sample code are all newly generated content.

**Why the others are wrong:**
- **B. Predictive analytics**: It forecasts outcomes from data; it doesn't create content.
- **C. Data warehousing**: It stores and analyzes data; it is not a branch of AI.
- **D. Relational databases**: They store structured data; they are not AI.

**Remember:** Create new content = generative AI.

---

## Question 41

*Domain 2: Exploring Data Transformation with Google Cloud*

**PetNest Analytics, a mobile app company, has accumulated several petabytes of historical user activity and transaction data. The analytics team needs a fast, scalable, fully managed solution to run advanced queries and analysis across this large dataset. Which Google Cloud product or service should PetNest Analytics use?**

- [x] A. BigQuery
- [ ] B. Cloud SQL
- [ ] C. Firestore
- [ ] D. Cloud Storage

### Explanation

**Correct answer: A. BigQuery**

BigQuery is Google Cloud's serverless, fully managed data warehouse. It runs fast SQL analytics over terabytes to petabytes of data. The clues are "petabytes", "advanced queries and analysis" and "fully managed".

**Why the others are wrong:**
- **B. Cloud SQL**: A transactional database, not built for petabyte-scale analytics.
- **C. Firestore**: A NoSQL document database for apps, not large-scale analysis.
- **D. Cloud Storage**: It stores files cheaply but isn't a query and analysis engine by itself.

**Remember:** Large-scale analytics with SQL = BigQuery.

---

## Question 42

*Domain 6: Scaling with Google Cloud Operations*

**BrightCart, an online shopping platform, is organizing its Google Cloud resource hierarchy. The company has one folder named retail-apps that contains multiple projects for checkout, inventory, and analytics workloads. The cloud administrator plans to apply user access policies at the retail-apps folder level. What will happen to those access policies?**

- [ ] A. The policy will be inherited by the projects in the folder but will not affect their resources.
- [x] B. The policy will be inherited by the projects and their resources within the folder.
- [ ] C. The policy will be applied to all folders within the organization.
- [ ] D. The policy applies to the folder only, and will not be inherited by any projects.

### Explanation

**Correct answer: B. The policy will be inherited by the projects and their resources within the folder.**

In the Google Cloud resource hierarchy (organization, folders, projects, resources), policies flow down. A policy set on a folder is inherited by every project in it and by all resources in those projects.

**Why the others are wrong:**
- **A. Inherited by projects but not their resources**: Inheritance continues down to resources.
- **C. Applied to all folders in the organization**: Policies flow down, not up or sideways to other folders.
- **D. Folder only, not inherited**: Inheritance is how the hierarchy works.

**Remember:** Policies flow down the hierarchy: organization, folder, project, resource.

---

## Question 43

*Domain 6: Scaling with Google Cloud Operations*

**SkyTrack Logistics runs containerized workloads on GKE, backend services on virtual machines, and several managed Google Cloud services. The operations team wants a single Google Cloud tool to collect, store, search, and analyze custom log entries from these environments. Which Google Cloud tool should SkyTrack Logistics use?**

- [ ] A. Dialogflow
- [x] B. Cloud Logging
- [ ] C. Cloud SDK
- [ ] D. Data Catalog

### Explanation

**Correct answer: B. Cloud Logging**

Cloud Logging is the managed service to collect, store, search and analyze logs from GKE, VMs and Google Cloud services, including custom log entries. The clues are "collect, store, search, and analyze" and "log entries".

**Why the others are wrong:**
- **A. Dialogflow**: A tool for building conversational agents and chatbots.
- **C. Cloud SDK**: Command-line tools and libraries for working with Google Cloud.
- **D. Data Catalog**: A metadata service for discovering data assets, not logs.

**Remember:** Logs from anywhere in Google Cloud = Cloud Logging.

---

## Question 44

*Domain 4: Modernize Infrastructure and Applications with Google Cloud*

**BrightCart, a small retail startup, plans to launch its first cloud-based shopping platform and design all supporting infrastructure directly on Google Cloud. The team does not have an existing application to migrate or modify. Which application modernization approach should BrightCart use?**

- [ ] A. Move the application to Google Cloud first, and then modernize it.
- [ ] B. Modernize the application first, and then move it to Google Cloud.
- [x] C. Invent in greenfield.
- [ ] D. Invent in brownfield.

### Explanation

**Correct answer: C. Invent in greenfield.**

Greenfield means starting fresh with no existing application. BrightCart is building its first platform directly on Google Cloud. The clue is "does not have an existing application to migrate or modify".

**Why the others are wrong:**
- **A. Move first, then modernize**: There is nothing to move.
- **B. Modernize first, then move**: There is nothing to modernize.
- **D. Invent in brownfield**: Brownfield means building a new app to replace an existing system.

**Remember:** Nothing existing = greenfield.

---

## Question 45

*Domain 3: Innovating with Google Cloud Artificial Intelligence*

**HelioWorks Analytics wants its operations analysts to create and test internal AI agents that can answer policy questions, summarize business data, and automate simple approval workflows. The analysts do not have advanced coding or machine learning skills, so the company needs a Google Cloud interface where they can visually design, prototype, and publish agents with a no-code or low-code experience. Which option should they use?**

- [x] A. Agent Studio
- [ ] B. Spanner
- [ ] C. Security Command Center
- [ ] D. Cloud Run

### Explanation

**Correct answer: A. Agent Studio**

Agent Studio is the no-code and low-code visual interface for designing, prototyping and publishing AI agents. It suits analysts without coding or ML skills. The clues are "visually design" and "no-code or low-code".

**Why the others are wrong:**
- **B. Spanner**: A globally distributed relational database.
- **C. Security Command Center**: A security and risk management service.
- **D. Cloud Run**: A serverless platform for running containers; it needs developers.

**Remember:** No-code or low-code agent building = Agent Studio.

---

## Question 46

*Domain 2: Exploring Data Transformation with Google Cloud*

**MediBridge Health is preparing clinical records for a machine learning model that will help predict patient follow-up needs. During data profiling, the team notices that many records do not contain required attributes such as date of birth, heart rate, and diagnosis code. Which data quality dimension is affected by this issue?**

- [ ] A. Timeliness
- [x] B. Completeness
- [ ] C. Uniqueness
- [ ] D. Validity

### Explanation

**Correct answer: B. Completeness**

Completeness measures whether all required data is present. Records missing date of birth, heart rate and diagnosis code are incomplete. The clue is "do not contain required attributes".

**Why the others are wrong:**
- **A. Timeliness**: That is about whether data is current, not missing.
- **C. Uniqueness**: That is about duplicate records.
- **D. Validity**: That is about values following the expected format or rules.

**Remember:** Missing required fields = completeness.

---

## Question 47

*Domain 5: Trust and Security with Google Cloud*

**QuickCart Labs is rolling out stricter access controls for employees who sign in to Google Cloud. The security team wants every user to enter their password and then prove their identity again by using a phone prompt, verification code, or hardware security key. Which security practice is being implemented?**

- [ ] A. Distributed Denial-of-Service protection
- [ ] B. Data masking
- [x] C. Two-step verification (2SV) / Multi-factor authentication
- [ ] D. Threat intelligence sharing

### Explanation

**Correct answer: C. Two-step verification (2SV) / Multi-factor authentication**

Two-step verification, a form of multi-factor authentication, requires a password plus a second proof such as a phone prompt, code or security key. This blocks attackers who only have a stolen password.

**Why the others are wrong:**
- **A. DDoS protection**: Protects against floods of traffic, not user sign-in.
- **B. Data masking**: Hides sensitive values in data.
- **D. Threat intelligence sharing**: Shares information about attackers; it doesn't verify identity.

**Remember:** Password + second proof = 2SV / MFA.

---

## Question 48

*Domain 6: Scaling with Google Cloud Operations*

**BrightCart, a grocery delivery mobile app, runs multiple backend services on Google Cloud. The developers want a tool that can automatically collect, group, and show application crashes and exceptions as they happen, so they do not have to inspect large volumes of raw logs manually. Which Google Cloud Observability tool should they use?**

- [ ] A. Cloud Profiler
- [x] B. Error Reporting
- [ ] C. Cloud Trace
- [ ] D. Cloud Monitoring

### Explanation

**Correct answer: B. Error Reporting**

Error Reporting automatically collects application crashes and exceptions, groups similar ones together, and shows them as they happen. The clue is "collect, group, and show application crashes and exceptions".

**Why the others are wrong:**
- **A. Cloud Profiler**: It shows CPU and memory use by code function.
- **C. Cloud Trace**: It shows request latency across services.
- **D. Cloud Monitoring**: It tracks metrics and alerts, but doesn't group exceptions.

**Remember:** Crashes and exceptions grouped for you = Error Reporting.

---

## Question 49

*Domain 6: Scaling with Google Cloud Operations*

**LumaCart, an online marketplace, wants to introduce a camera-based image recognition login feature for its internal support portal. The engineering team wants to release the feature while following SRE principles and reducing risk. What should LumaCart do?**

- [x] A. Roll out the new system to a small group of support employees to test it first.
- [ ] B. Roll out the new system to all support employees immediately to collect the maximum amount of usage data.
- [ ] C. Avoid rolling out the new system because it may have authentication weaknesses.
- [ ] D. Avoid rolling out the new system because it may conflict with privacy requirements.

### Explanation

**Correct answer: A. Roll out the new system to a small group of support employees to test it first.**

SRE favors gradual rollouts, such as a canary release to a small group first. If something goes wrong, only a few users are affected and the change is easy to roll back. The clue is "reducing risk".

**Why the others are wrong:**
- **B. Roll out to everyone immediately**: This maximizes the impact if something breaks.
- **C. Avoid rollout over authentication weaknesses**: SRE manages risk; it doesn't block innovation out of fear.
- **D. Avoid rollout over privacy conflicts**: Same: test and manage the risk rather than refusing to launch.

**Remember:** New feature + reduce risk = roll out to a small group first.

---

## Question 50

*Domain 6: Scaling with Google Cloud Operations*

**MealSprint, a food delivery web app, notices that one backend service is causing unusually high cloud costs. The development team wants to inspect the running production application and continuously collect CPU usage and memory-allocation data so they can find which specific code functions are consuming the most resources. Which Google Cloud tool should they use?**

- [ ] A. Cloud Logging
- [ ] B. Cloud Trace
- [ ] C. Error Reporting
- [x] D. Cloud Profiler

### Explanation

**Correct answer: D. Cloud Profiler**

Cloud Profiler continuously collects CPU and memory-allocation data from running production apps with low overhead. It shows which functions use the most resources. The clues are "CPU usage and memory-allocation" and "which specific code functions".

**Why the others are wrong:**
- **A. Cloud Logging**: It stores log events, not resource use by function.
- **B. Cloud Trace**: It shows request latency across services, not code-level resource use.
- **C. Error Reporting**: It groups crashes and exceptions.

**Remember:** Which code uses the most CPU or memory = Cloud Profiler.

---
