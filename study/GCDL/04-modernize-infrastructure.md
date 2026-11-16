# Domain 4 — Modernize Infrastructure and Applications with Google Cloud

59 questions. Answers are collapsed — try each question before expanding it.

## Questions

### Exam 1 · Q5

**BlueCart, a grocery delivery startup, is moving its existing order-processing application from its data center to Google Cloud. The team wants the application to run in the cloud with no changes to the application code and no redesign of the current architecture. Which migration approach matches this plan?**

- A. Rehosted
- B. Reimagined
- C. Replatformed
- D. Refactored

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Rehosted

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

</details>

---

### Exam 1 · Q9

**MealBridge, a grocery pickup app, needs live product availability from several partner stores. The app must also send each customer’s confirmed order details back to the correct store immediately so staff can prepare the order. What should MealBridge use?**

- A. Site reliability engineering (SRE)
- B. An application programming interface (API)
- C. A customized machine learning model
- D. A multi-regional database

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. An application programming interface (API)

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

</details>

---

### Exam 1 · Q15

**TaskFlow, a project management software company, is building several new containerized applications for different departments. The platform team wants a managed Google Cloud service that can help deploy, scale, and orchestrate those containers efficiently. Why should TaskFlow use Google Kubernetes Engine?**

- A. It enables rapid application deployment and testing.
- B. It optimizes virtual machine performance.
- C. It connects legacy systems to an application.
- D. It provides pre-written source code for application development.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. It enables rapid application deployment and testing.

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

</details>

---

### Exam 1 · Q16

**MediBridge, a healthcare appointment platform, wants to run small pieces of backend code whenever users submit forms, upload documents, or trigger events from other cloud services. The team does not want to manage servers, and it cannot predict how much compute capacity will be needed as usage changes throughout the day. Which Google Cloud solution should MediBridge use?**

- A. Compute Engine
- B. Google Kubernetes Engine
- C. Cloud Run functions
- D. Bare Metal Solution for SAP

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Cloud Run functions

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

</details>

---

### Exam 1 · Q18

**MapleBank still runs an older core banking system and does not have the budget to replace or modernize its infrastructure right now. However, MapleBank wants its business partner’s modern analytics platform to securely access selected data from the legacy system. What should MapleBank use to make its data accessible?**

- A. Compute Engine
- B. GKE Enterprise
- C. An application programming interface
- D. Google Kubernetes Engine

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. An application programming interface

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

</details>

---

### Exam 1 · Q21

**ShopTrail, a retail analytics company, relies on older inventory and billing systems that are becoming difficult to adapt whenever new digital services are launched. The company wants a way to make existing system capabilities easier to reuse across mobile apps, partner portals, and cloud services without replacing everything at once. Why should ShopTrail use application programming interfaces APIs?**

- A. To reveal every backend record so external partners can directly change it
- B. To fully rebuild all legacy applications from the ground up
- C. To gain long-term operational flexibility
- D. To move IT spending to a pay-as-you-go model so infrastructure can scale

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. To gain long-term operational flexibility

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

</details>

---

### Exam 1 · Q23

**FitLoop, a fitness subscription app, is finding it difficult to keep up with users who expect frequent feature improvements and quick fixes. The company plans to modernize its older applications by moving them to Google Cloud. Why would this help FitLoop better meet user expectations?**

- A. Customer data can be used to provide personalized content
- B. Toil automation helps perform automatic updates
- C. Updates can be released more quickly to fix bugs
- D. DevOps requires market trends to be measured and tracked

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Updates can be released more quickly to fix bugs

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

</details>

---

### Exam 1 · Q24

**OrbitCart, a retail marketplace, wants one platform that helps its engineering teams create new container-based services, modernize older applications, and operate workloads consistently across Google Cloud and another public cloud provider. Which Google Cloud solution should OrbitCart use?**

- A. Apigee Hybrid
- B. GKE Enterprise
- C. Cloud Run
- D. Compute Engine

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. GKE Enterprise

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

</details>

---

### Exam 1 · Q42

**HarborLedger, a financial services company, wants to move a legacy database platform to Google Cloud. The platform depends on strict third-party licensing terms, low-level server access, and an architecture that cannot be easily redesigned for virtual machines or serverless services. What Google Cloud solution should HarborLedger use?**

- A. Compute Engine
- B. Bare Metal Solution
- C. Cloud Run
- D. Cloud Run functions

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Bare Metal Solution

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

</details>

---

### Exam 1 · Q47

**FitTrackly, a fitness coaching website, has a small development team that built a web application packaged as one container image. The team wants to deploy it with minimal infrastructure management, automatic scaling, and a serverless hosting experience. Which Google Cloud service should FitTrackly use?**

- A. Compute Engine
- B. App Engine
- C. Google Kubernetes Engine
- D. Cloud Run

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Cloud Run

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

</details>

---

### Exam 2 · Q2

**MetroTrail, a public transport route-planning app, wants its engineering teams to make existing backend services easier to expose, manage, secure, and reuse as APIs in upcoming web and mobile projects. Which Google product or solution should MetroTrail use?**

- A. Application migration
- B. Apigee
- C. The App Engine flexible environment
- D. AppSheet

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Apigee

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

</details>

---

### Exam 2 · Q9

**BrightCart is adding a small order-notification feature to its shopping app. The development team wants to write the function code and let Google Cloud manage server provisioning, scaling, patching, and runtime infrastructure. Which infrastructure solution should BrightCart use?**

- A. Virtual machines
- B. Bare Metal Solution
- C. Serverless computing
- D. Artifact Registry

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Serverless computing

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

</details>

---

### Exam 2 · Q16

**BrightCart is preparing to release a container-based shopping assistant service. The team is unsure whether the service will receive 500 users or 50,000 users during launch week. They also want to avoid paying for compute capacity when no users are actively using the service. Which benefit of serverless computing best addresses this requirement?**

- A. Disaster recovery
- B. Reduced development costs
- C. Scalability
- D. Built-in security

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Scalability

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

</details>

---

### Exam 2 · Q18

**PhotoDrop, a media-sharing startup, wants to run small pieces of application logic whenever users upload image files to Cloud Storage. The developers want these pieces of code to be event-driven and serverless, and they do not want to manage virtual machines or runtime infrastructure. Which Google Cloud product should they use?**

- A. Compute Engine
- B. Cloud Run functions
- C. Bare Metal Solution
- D. Spot VMs

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Cloud Run functions

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

</details>

---

### Exam 2 · Q20

**MarketNest, an online marketplace, runs containerized applications in Kubernetes clusters on Google Cloud, inside its private data center, and in another public cloud provider. The platform team wants one centralized way to manage these clusters, apply consistent security controls, and operate applications across all environments. Which Google Cloud service should they use?**

- A. Compute Engine
- B. Cloud Run
- C. GKE Enterprise
- D. BigQuery Omni

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. GKE Enterprise

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

</details>

---

### Exam 2 · Q24

**EduCore Apps manages several internal learning platforms for schools. Its IT team spends most of each week installing operating system patches, upgrading application components, and setting up database servers. The leadership team wants developers to move faster by having Google Cloud take over more of these infrastructure administration tasks. Which cloud computing approach does this describe?**

- A. On-premises hosting
- B. Adopting managed services
- C. Bare metal provisioning
- D. Edge computing

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Adopting managed services

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

</details>

---

### Exam 2 · Q26

**RideLoop Mobility is replacing a large legacy ride-booking platform that is difficult to update and scale. The engineering team plans to divide the application into smaller independent services, where each service owns a specific business function and can be built, deployed, and scaled separately. Which modern architecture pattern are they adopting?**

- A. Monolithic architecture
- B. Microservices
- C. Spot VM architecture
- D. Hardware virtualization

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Microservices

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

</details>

---

### Exam 2 · Q31

**RideNest is moving several internal applications to Google Cloud and wants to use managed services wherever possible. The IT team wants to reduce the amount of routine infrastructure maintenance they perform themselves. Which task is typically handled automatically by a managed services platform?**

- A. Managing user access
- B. Patching and upgrades
- C. Data archiving
- D. Cost optimization

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Patching and upgrades

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

</details>

---

### Exam 2 · Q32

**StreamPilot, a video streaming app, is preparing to test a redesigned home page and a few recommendation features. The product team wants some users to access the new app version while other users continue using the existing version, so they can compare feedback before a full release. Why should StreamPilot use App Engine?**

- A. Because their app is containerized and enabled by microservices
- B. Because the updated app will only include new features
- C. To run different versions of the app for different users
- D. To run different versions of the app for the same user

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. To run different versions of the app for different users

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

</details>

---

### Exam 2 · Q34

**BrightCart Retail is moving its inventory application to Google Cloud. Instead of copying the existing virtual machines exactly as they are, the team chooses to replace the self-managed database layer with a managed Cloud SQL instance so database patching, backups, and maintenance require less manual work. The main application logic will remain mostly unchanged. Which migration path does this represent?**

- A. Rehost (Lift and shift)
- B. Replatform (Move and improve)
- C. Retain
- D. Retire

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Replatform (Move and improve)

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

</details>

---

### Exam 2 · Q37

**PulseCart, an online grocery company, is moving its legacy shopping application to Google Cloud. The team plans to redesign the application into smaller, independently deployable services instead of keeping it as one large application. Which benefit would this refactoring approach provide?**

- A. The redesigned application can become more efficient and scalable.
- B. No code changes will be required.
- C. This migration approach provides the quickest path to Google Cloud.
- D. The application will automatically become PCI-DSS compliant.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. The redesigned application can become more efficient and scalable.

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

</details>

---

### Exam 2 · Q42

**BrightBite, a food delivery mobile app, wants its customer app to request menu details, send order information, and receive delivery updates from backend systems. The development team wants to use a standard way for different software components to exchange requests and responses. What is the purpose of an application programming interface (API)?**

- A. To provide a defined set of rules and methods that allow software applications to communicate with each other
- B. To provide cloud extensions for integrated development environments
- C. To link private networks across different cloud vendors
- D. To control and schedule multiple containerized applications

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. To provide a defined set of rules and methods that allow software applications to communicate with each other

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

</details>

---

### Exam 2 · Q43

**MediaNest, a video streaming startup, is building containerized applications with Kubernetes. The engineering team wants to reduce the time spent configuring nodes, scaling cluster infrastructure, and handling cluster operations so they can focus more on application development. Which Google Cloud service should MediaNest choose?**

- A. GKE Autopilot
- B. Compute Engine
- C. Cloud Run
- D. GKE Standard

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. GKE Autopilot

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

</details>

---

### Exam 2 · Q45

**DataCrate Analytics runs a nightly data transformation job that processes millions of log records. The job can safely restart from checkpoints if compute resources are interrupted, and it does not need to finish immediately. The company wants to minimize compute costs and accepts that Google Cloud might stop the instances when capacity is needed elsewhere. Which compute option should the company choose?**

- A. Spot VMs
- B. Managed services
- C. Premium tier virtual machines
- D. Cloud Run functions

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Spot VMs

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

</details>

---

### Exam 2 · Q47

**HarborStyle Retail runs a large on-premises VMware estate for its inventory, billing, and store operations systems. The company wants to move these workloads to Google Cloud, but it wants administrators to continue using familiar VMware tools and existing operating procedures with minimal change. Which Google Cloud service should HarborStyle Retail use?**

- A. Compute Engine
- B. Google Cloud VMware Engine
- C. VMware vSphere
- D. Bare Metal Solution

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Google Cloud VMware Engine

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

</details>

---

### Exam 2 · Q50

**HomeFixNow, a home repair booking website, wants to build web applications that can automatically scale as customer traffic increases or decreases. The development team also wants Google Cloud to handle the underlying application infrastructure so they can focus on writing code. Which Google Cloud product should HomeFixNow use?**

- A. Anthos
- B. Apigee
- C. AutoML
- D. App Engine

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. App Engine

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

</details>

---

### Exam 3 · Q12

**FitFleet, a fitness tracking mobile app, runs its backend microservices on Google Kubernetes Engine. Developers frequently test fixes for application issues and want a platform that helps them deploy, validate, and adjust changes quickly. What makes Google Kubernetes Engine an effective solution for these developers?**

- A. It shortens the time required to test and refine different fixes.
- B. It automatically provides intelligent recommendations to redesign application code.
- C. It eliminates the requirement to package applications into containers.
- D. It keeps application source code copied across multiple servers for cross-team collaboration.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. It shortens the time required to test and refine different fixes.

**Correct answer: A. It shortens the time required to test and refine different fixes.**

GKE runs containers and supports fast, repeatable deployments, rolling updates and easy rollbacks. That lets developers deploy a fix, check it, and adjust quickly. The clue is "deploy, validate, and adjust changes quickly".

**Why the others are wrong:**
- **B. Recommendations to redesign code**: GKE runs workloads; it does not review or redesign code.
- **C. Eliminates packaging into containers**: GKE runs containers, so packaging into containers is required.
- **D. Copies source code across servers**: GKE runs container images, not shared copies of source code for collaboration.

**Remember:** GKE = fast, consistent container deployments and rollbacks.

**References:**
- [docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)
- [docs.cloud.google.com/kubernetes-engine/docs](https://docs.cloud.google.com/kubernetes-engine/docs)
- [docs.cloud.google.com/kubernetes-engine/docs/concepts/best-practices-continuous-integration-delivery-kubernetes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/best-practices-continuous-integration-delivery-kubernetes)

**⚠️ Note:** The keyed answer is vague. Faster testing is a general benefit of containers and CI/CD, not something only GKE provides. It is keyed because the other options are clearly false.

</details>

---

### Exam 3 · Q30

**CedarPeak Insurance currently runs a claims-processing system in its own data center. The company wants to build a new cloud-native application on Google Cloud that will eventually replace the existing on-premises system. Which application modernization approach should CedarPeak Insurance use?**

- A. Move the application to Google Cloud, and then change it.
- B. Change the application first, and then move it to Google Cloud.
- C. Invent in greenfield.
- D. Invent in brownfield.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Invent in brownfield.

**Correct answer: D. Invent in brownfield.**

In Google's framing, "invent in brownfield" means building a new cloud-native application that will replace an existing legacy system. The clue is a new app on Google Cloud that "will eventually replace the existing on-premises system".

**Why the others are wrong:**
- **A. Move, then change**: This migrates the existing app first (lift and shift, then modernize); the stem builds a new app instead.
- **B. Change, then move**: This modernizes the existing app before migrating it; again, not building new.
- **C. Invent in greenfield**: Greenfield means no existing system at all; here one exists and will be replaced.

**Remember:** New app, nothing existing = greenfield. New app that replaces a legacy one = brownfield.

**References:**
- [cloud.google.com/solutions/application-modernization](https://cloud.google.com/solutions/application-modernization)
- [docs.cloud.google.com/architecture/migration-to-gcp-getting-started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started)
- [cloud.google.com/solutions/infrastructure-modernization](https://cloud.google.com/solutions/infrastructure-modernization)

</details>

---

### Exam 3 · Q31

**BlueTrail Logistics runs several warehouse applications in its private data center, but the company also wants to build and run newer applications on Google Cloud. It needs a hybrid-cloud management solution that can help teams manage applications consistently across on-premises and cloud environments. What solution should BlueTrail Logistics use?**

- A. GKE Enterprise
- B. Cloud Run functions
- C. App Engine
- D. Compute Engine

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. GKE Enterprise

**Correct answer: A. GKE Enterprise**

GKE Enterprise (formerly Anthos) is Google Cloud's platform for managing applications and Kubernetes clusters consistently across on-premises, Google Cloud and other clouds. The clue is "hybrid-cloud management" across "on-premises and cloud environments".

**Why the others are wrong:**
- **B. Cloud Run functions**: Serverless functions that run in Google Cloud, not a hybrid management platform.
- **C. App Engine**: A serverless app platform that runs only in Google Cloud.
- **D. Compute Engine**: Virtual machines in Google Cloud; it doesn't manage on-premises environments.

**Remember:** Consistent management across on-prem and clouds = GKE Enterprise.

**References:**
- [cloud.google.com/kubernetes-engine/enterprise](https://cloud.google.com/kubernetes-engine/enterprise)
- [docs.cloud.google.com/kubernetes-engine/enterprise/docs/deployment-options](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/deployment-options)
- [docs.cloud.google.com/functions/docs/concepts/overview](https://docs.cloud.google.com/functions/docs/concepts/overview)

</details>

---

### Exam 3 · Q37

**FleetNest, a logistics tracking company, runs a custom in-house routing application that needs detailed control over the virtual machines, operating system configuration, networking, and machine types. The team also wants the infrastructure to support autoscaling and automatic rolling updates. Which Google Cloud product or solution should FleetNest use?**

- A. Cloud Build
- B. Cloud Run
- C. Compute Engine
- D. App Engine

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Compute Engine

**Correct answer: C. Compute Engine**

Compute Engine gives full control over virtual machines, including the operating system, machine types and networking. With managed instance groups it also supports autoscaling and automatic rolling updates. The clue is "detailed control over the virtual machines".

**Why the others are wrong:**
- **A. Cloud Build**: A CI/CD service that builds and tests code; it doesn't host the application.
- **B. Cloud Run**: Serverless containers; you don't control the VMs or OS.
- **D. App Engine**: A serverless app platform that hides the underlying VMs.

**Remember:** Need control of VMs and OS = Compute Engine.

**References:**
- [docs.cloud.google.com/compute/docs/instance-groups](https://docs.cloud.google.com/compute/docs/instance-groups)
- [docs.cloud.google.com/compute/docs/autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler)
- [docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups)

</details>

---

### Exam 3 · Q44

**BrightCart, a small retail startup, plans to launch its first cloud-based shopping platform and design all supporting infrastructure directly on Google Cloud. The team does not have an existing application to migrate or modify. Which application modernization approach should BrightCart use?**

- A. Move the application to Google Cloud first, and then modernize it.
- B. Modernize the application first, and then move it to Google Cloud.
- C. Invent in greenfield.
- D. Invent in brownfield.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Invent in greenfield.

**Correct answer: C. Invent in greenfield.**

Greenfield means starting fresh with no existing application. BrightCart is building its first platform directly on Google Cloud. The clue is "does not have an existing application to migrate or modify".

**Why the others are wrong:**
- **A. Move first, then modernize**: There is nothing to move.
- **B. Modernize first, then move**: There is nothing to modernize.
- **D. Invent in brownfield**: Brownfield means building a new app to replace an existing system.

**Remember:** Nothing existing = greenfield.

**References:**
- [cloud.google.com/solutions/application-modernization](https://cloud.google.com/solutions/application-modernization)
- [docs.cloud.google.com/architecture/migration-to-gcp-getting-started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started)
- [cloud.google.com/solutions/camp](https://cloud.google.com/solutions/camp)

</details>

---

### Exam 4 · Q5

**TrailPilot Maps, a travel planning website, wants to run its Kubernetes applications across three different public cloud providers so it can use more deployment locations around the world. The engineering team uses GKE Enterprise to manage and deploy these Kubernetes workloads across the different cloud environments. What type of deployment is this?**

- A. On-premises
- B. Multi-cloud
- C. Hybrid-cloud
- D. Private cloud

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Multi-cloud

**Correct answer: B. Multi-cloud**

Multi-cloud means using more than one public cloud provider. Here TrailPilot runs Kubernetes workloads on three different public clouds, and GKE Enterprise (formerly Anthos) gives one way to manage them all. No on-premises data center is mentioned, so it isn't hybrid.

**Why the others are wrong:**
- **A. On-premises**: Everything here runs on public clouds, not in the company's own data center.
- **C. Hybrid-cloud**: Hybrid means combining on-premises (or private) infrastructure with public cloud, which the stem doesn't describe.
- **D. Private cloud**: A private cloud is dedicated infrastructure for one organization, not several public providers.

**Remember:** Several public clouds → multi-cloud. On-premises + public cloud → hybrid.

**References:**
- [cloud.google.com/learn/what-is-multicloud](https://cloud.google.com/learn/what-is-multicloud)
- [cloud.google.com/kubernetes-engine/multi-cloud/docs](https://cloud.google.com/kubernetes-engine/multi-cloud/docs)
- [cloud.google.com/kubernetes-engine/enterprise/clusters/docs](https://cloud.google.com/kubernetes-engine/enterprise/clusters/docs)

</details>

---

### Exam 4 · Q8

**TrailNest, a campsite booking company, wants to update its older reservation platform so travelers can search available campsites and book stays from a mobile app. What is the main benefit of using an application programming interface (API) for this modernization?**

- A. They do not have to build the customer-facing mobile app
- B. They can immediately retire their legacy reservation platform
- C. They can automatically convert their systems into cloud-native applications
- D. They do not have to rewrite the legacy reservation platform

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. They do not have to rewrite the legacy reservation platform

**Correct answer: D. They do not have to rewrite the legacy reservation platform**

An API exposes the existing system's data and functions to new apps in a standard way. The mobile app can call the API to search and book campsites while the old reservation platform keeps running behind it. This lets companies modernize the customer experience without a risky full rewrite.

**Why the others are wrong:**
- **A. Don't have to build the mobile app**: The company still has to build the app; the API only connects it to the backend.
- **B. Immediately retire the legacy platform**: The API relies on the legacy platform still running, so it isn't retired.
- **C. Automatically convert to cloud-native**: An API doesn't turn an old system into a cloud-native one by itself.

**Remember:** API on top of a legacy system = new experiences without rewriting the old system.

**References:**
- [cloud.google.com/solutions/unlocking-legacy-applications](https://cloud.google.com/solutions/unlocking-legacy-applications)
- [cloud.google.com/apigee](https://cloud.google.com/apigee)
- [docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)

</details>

---

### Exam 4 · Q11

**StyleHub, a clothing retailer, keeps its store inventory data in an older warehouse management system. Customers often see jackets, shoes, and accessories listed as available on StyleHub’s website, but when they visit a nearby store, some items are already sold out. How could StyleHub benefit from using an application programming interface (API)?**

- A. To generate personalized product suggestions for shoppers
- B. To improve the stability of the on-premises legacy system itself
- C. By manually connecting each inventory source to the website one at a time
- D. By programmatically connecting the inventory system to their website

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. By programmatically connecting the inventory system to their website

**Correct answer: D. By programmatically connecting the inventory system to their website**

The problem is that the website shows stale stock because it isn't connected to the real inventory. An API lets the website ask the warehouse system for current stock automatically, in code. Customers then see accurate availability without replacing the old system.

**Why the others are wrong:**
- **A. Personalized product suggestions**: That is a recommendations use case, not a fix for wrong stock levels.
- **B. Improve stability of the legacy system**: An API exposes the system to others; it doesn't make the old system itself more stable.
- **C. Manually connecting each source**: APIs are about automated, programmatic connections, not manual work.

**Remember:** APIs connect systems programmatically so data stays in sync.

**References:**
- [cloud.google.com/apigee](https://cloud.google.com/apigee)
- [docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)
- [cloud.google.com/solutions/unlocking-legacy-applications](https://cloud.google.com/solutions/unlocking-legacy-applications)

</details>

---

### Exam 4 · Q15

**SkyPeak Labs wants to consolidate several test environments so Linux and Windows workloads can run separately on the same physical server. Which technology makes it possible to run multiple computer operating systems on one physical hardware machine?**

- A. Hypervisor
- B. Containers
- C. Serverless computing
- D. Open source

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Hypervisor

**Correct answer: A. Hypervisor**

A hypervisor is the software layer that creates and runs virtual machines. It splits one physical server into several VMs, and each VM can run its own operating system, such as Linux and Windows side by side. This is the basis of virtualization and of Compute Engine.

**Why the others are wrong:**
- **B. Containers**: Containers share the host's operating system kernel, so they don't run different full operating systems.
- **C. Serverless computing**: Serverless hides the servers entirely; it isn't the technology that runs multiple OSes on one machine.
- **D. Open source**: Open source is a licensing model, not a virtualization technology.

**Remember:** Multiple operating systems on one physical machine → hypervisor (VMs).

**References:**
- [cloud.google.com/learn/what-is-a-virtual-machine](https://cloud.google.com/learn/what-is-a-virtual-machine)
- [cloud.google.com/discover/containers-vs-vms](https://cloud.google.com/discover/containers-vs-vms)
- [docs.cloud.google.com/compute/docs/overview](https://docs.cloud.google.com/compute/docs/overview)

</details>

---

### Exam 4 · Q34

**BrightCart Analytics runs nightly sales-report calculations on a Compute Engine virtual machine. The job saves progress regularly, can be restarted without data loss, and does not need to finish immediately. The company wants the cheapest suitable compute option for this workload. Which option should BrightCart Analytics choose?**

- A. A Spot VM on Compute Engine
- B. A custom VM in a pay-as-you-go model on Compute Engine
- C. A standard VM in a pay-as-you-go model on Compute Engine
- D. A Cloud Run function with a small memory limit

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. A Spot VM on Compute Engine

**Correct answer: A. A Spot VM on Compute Engine**

Spot VMs run on Google's spare capacity at a large discount. Google can stop them when it needs the capacity back. That is acceptable here because the job saves progress, can restart without data loss and doesn't need to finish right away. These are the classic signs of a Spot VM workload.

**Why the others are wrong:**
- **B. Custom VM, pay-as-you-go**: Custom sizing can save a little, but it is still full price compared with Spot.
- **C. Standard VM, pay-as-you-go**: Works, but it is the most expensive of the VM choices for an interruptible job.
- **D. Cloud Run function with small memory**: Functions are for short, event-driven code, not long nightly batch calculations.

**Remember:** Interruptible + restartable + cheapest → Spot VMs (the successor to Preemptible VMs).

**References:**
- [docs.cloud.google.com/compute/docs/instances/spot](https://docs.cloud.google.com/compute/docs/instances/spot)
- [cloud.google.com/spot-vms/pricing](https://cloud.google.com/spot-vms/pricing)
- [docs.cloud.google.com/functions/docs](https://docs.cloud.google.com/functions/docs)

</details>

---

### Exam 4 · Q36

**FitGlow, a wellness mobile app company, wants to build an application that can adjust workout plans, meal suggestions, and notifications based on each user’s changing preferences across different seasons. Why should FitGlow build a cloud-native application instead of only modernizing its existing on-premises application?**

- A. Developers can depend on the cloud provider to write all source code
- B. Developers can release new features in an agile way
- C. IT managers can move the existing application architecture without making updates
- D. IT managers can speed up capital expenditure planning

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Developers can release new features in an agile way

**Correct answer: B. Developers can release new features in an agile way**

Cloud-native apps are built from microservices, containers and managed services. Teams can update one part at a time and ship changes often and safely. That fits an app that must keep adapting to users' changing preferences.

**Why the others are wrong:**
- **A. Provider writes the source code**: The company's developers still write their own code.
- **C. Move architecture without updates**: That describes lift-and-shift, not building cloud-native.
- **D. Speed up CapEx planning**: Cloud-native apps use pay-as-you-go OpEx, not more capital planning.

**Remember:** Cloud-native → frequent, agile releases.

**References:**
- [cloud.google.com/learn/what-is-cloud-native](https://cloud.google.com/learn/what-is-cloud-native)
- [cloud.google.com/resources/rearchitecting-to-cloud-native](https://cloud.google.com/resources/rearchitecting-to-cloud-native)
- [cloud.google.com/solutions/application-modernization](https://cloud.google.com/solutions/application-modernization)

</details>

---

### Exam 4 · Q38

**MetroFleet Logistics runs its vehicle booking platform on an on-premises SQL Server database. The database team is spending too much time handling capacity planning, patching, and routine administration. The company wants to move quickly to a Google Cloud managed service while keeping the SQL Server database approach. What should MetroFleet Logistics do?**

- A. Redesign the applications to use a cloud-first database such as Firestore.
- B. Use Database Migration Service to migrate the database to Cloud SQL.
- C. Export historical SQL Server tables to Cloud Storage.
- D. Move all SQL Server data into BigQuery.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use Database Migration Service to migrate the database to Cloud SQL.

**Correct answer: B. Use Database Migration Service to migrate the database to Cloud SQL.**

Cloud SQL supports SQL Server as a managed service, so Google handles patching, backups and capacity. Database Migration Service helps move the database with little downtime. The clue is "move quickly" while "keeping the SQL Server database approach".

**Why the others are wrong:**
- **A. Redesign for Firestore**: Rewriting for a NoSQL database is slow and drops the SQL Server approach.
- **C. Export tables to Cloud Storage**: Files in Cloud Storage aren't a running database.
- **D. Move data into BigQuery**: BigQuery is for analytics, not the operational database for a booking platform.

**Remember:** Keep the same relational engine, stop managing it → Cloud SQL (via Database Migration Service).

**References:**
- [docs.cloud.google.com/sql/docs/sqlserver](https://docs.cloud.google.com/sql/docs/sqlserver)
- [docs.cloud.google.com/database-migration/docs/sqlserver/guide](https://docs.cloud.google.com/database-migration/docs/sqlserver/guide)
- [cloud.google.com/sql](https://cloud.google.com/sql)

</details>

---

### Exam 5 · Q2

**AgriPulse Insights stores valuable crop-yield, soil-quality, and weather-pattern data in a relational database. The company wants to create a new income source by allowing partner companies to use this data inside their own mobile and web applications. Which cloud-first approach should AgriPulse Insights choose?**

- A. Add partner users directly to the relational database.
- B. Sell paid downloads of old exported data files.
- C. Provide access to the data through a paid API.
- D. Move the data into a non-relational database.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Provide access to the data through a paid API.

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

</details>

---

### Exam 5 · Q3

**FitPerks, a fitness membership app, gives reward points to its customers. The company recently partnered with nearby gyms, sports shops, and health cafes so members can earn and redeem points across all partner locations. Why should FitPerks use application programming interfaces?**

- A. To copy all partner information into its own system for disaster recovery
- B. To create charts showing reward program performance
- C. To generate personalized offers for members
- D. To connect partner systems so loyalty point details stay current

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. To connect partner systems so loyalty point details stay current

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

</details>

---

### Exam 5 · Q12

**FitSprint, a fitness tracking web app, has packaged its stateless frontend service into a container. The team wants to deploy it on Google Cloud so it can scale down to zero when there is no traffic and quickly scale up during busy periods, without requiring the team to create or manage Kubernetes clusters or servers. Which service should FitSprint use?**

- A. Compute Engine
- B. Cloud Run
- C. Bare Metal Solution
- D. AlloyDB Omni

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Cloud Run

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

</details>

---

### Exam 5 · Q13

**GreenCart Finance, a small payment processing company, must leave its private server room because the facility contract ends soon. The IT team wants to move its existing virtual machines to Compute Engine with the same operating system images, application settings, and configurations, making only the minimum changes needed to run in Google Cloud. Which migration strategy is this?**

- A. Rehost (Lift and shift)
- B. Refactor
- C. Reimagine
- D. Replatform

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Rehost (Lift and shift)

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

</details>

---

### Exam 5 · Q18

**BrightCart Market, an online retail company, is moving its inventory, payments, and customer engagement applications to the cloud. The leadership team is worried about becoming dependent on a single provider and wants future flexibility to run applications across public cloud, private cloud, and on-premises environments when needed. Which principle should best guide the company’s cloud modernization strategy?**

- A. Adopting proprietary, vendor-specific databases
- B. Keeping all mission-critical workloads in a single private cloud
- C. Committing to openness and interoperability
- D. Relying exclusively on Software as a Service (SaaS) products

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Committing to openness and interoperability

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

</details>

---

### Exam 5 · Q25

**NimbusPay Systems runs containerized payment applications in Kubernetes clusters across Google Cloud, another public cloud, and an on-premises environment. The platform team wants one consistent and centralized way to manage these Kubernetes environments. Which Google Cloud service should NimbusPay Systems choose?**

- A. Cloud Run functions
- B. GKE Enterprise
- C. Cloud Run
- D. Compute Engine

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. GKE Enterprise

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

</details>

---

### Exam 5 · Q33

**UrbanTrail Logistics, a delivery management company, has begun building cloud-native applications to replace older warehouse and routing systems. What additional step should UrbanTrail Logistics take as part of adopting the cloud?**

- A. Give third-party partners privileged access to the cloud network.
- B. Move selected legacy infrastructure workloads to the cloud.
- C. Continue performing maintenance on old on-premises hardware.
- D. Increase capital spending on existing on-premises projects.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Move selected legacy infrastructure workloads to the cloud.

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

</details>

---

### Exam 5 · Q35

**GreenCart Labs is building several customer-facing applications for order tracking, product search, and user notifications. Its developers want to use their preferred programming languages and tools, but the company also wants to reduce the amount of time spent managing servers and infrastructure. Which Google Cloud solution should GreenCart Labs use?**

- A. Cloud Run
- B. Managed Service for Apache Spark
- C. Pub/Sub
- D. Bare Metal Solution

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Cloud Run

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

</details>

---

### Exam 5 · Q38

**GlobeTrek Media, a travel content website, wants hotel chains and tour partners to display its latest destination posts, images, and campaign updates inside their own apps and websites. What should GlobeTrek Media use to share this content smoothly with partner systems?**

- A. A NoSQL database
- B. Config Sync
- C. The App Engine standard environment
- D. An application programming interface

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. An application programming interface

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

</details>

---

### Exam 5 · Q40

**PixelTrail, a mobile photo-sharing startup, has developers who build new features on their laptops, but the same code sometimes breaks after release because the production environment has different runtime libraries and package versions. Which technology should PixelTrail use to bundle the application code with its required dependencies so the application behaves consistently across development, testing, and production?**

- A. Containerization
- B. Serverless computing
- C. Spot VMs
- D. Load balancing

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Containerization

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

</details>

---

### Exam 5 · Q42

**EventEase, a local event venue platform, lets customers reserve halls, meeting rooms, and party spaces online. EventEase has recently partnered with FreshFork Catering so customers can request meals while making a venue reservation. How can EventEase use application programming interfaces (APIs) to create new business value?**

- A. Use an API to redesign the reservation website for a specific customer segment
- B. Use an API to discover possible future partnership opportunities
- C. Use an API to move all customer records into a machine learning model to estimate meal demand
- D. Use an API to connect the venue reservation system with FreshFork Catering’s order request form

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Use an API to connect the venue reservation system with FreshFork Catering’s order request form

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

</details>

---

### Exam 5 · Q43

**QuickCart, an online grocery delivery platform, is moving its new microservices into containers. The engineering team expects to run and coordinate several thousand containers and wants a managed Google Cloud service that can automate container deployment, scaling, and operations. Which service should QuickCart choose?**

- A. Cloud Run functions
- B. Google Kubernetes Engine (GKE)
- C. Apigee
- D. BigQuery Omni

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Google Kubernetes Engine (GKE)

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

</details>

---

### Exam 5 · Q44

**NimbusLedger, a small fintech website, is modernizing its development process. Its engineering team wants to adopt software whose source code is available for public review, so developers can study it, change it, improve it, and contribute updates back to the community. Which term best describes this type of technology?**

- A. Proprietary software
- B. Open source
- C. Platform as a Service (PaaS)
- D. Closed standard

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Open source

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

</details>

---

### Exam 5 · Q45

**TrailBite, a food delivery website, is losing customers because its legacy data center applications cannot respond quickly to new menu, payment, and delivery feature requests. The company decides to modernize these applications by moving toward cloud-based application architecture. What may have led TrailBite to make this business decision?**

- A. Its data center applications already scale automatically whenever demand changes.
- B. It wants to move from a pay-as-you-go model to a capital expenditure model.
- C. Its application code changes by itself without any developer making updates.
- D. Its data center applications take several weeks to update and release.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Its data center applications take several weeks to update and release.

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

</details>

---

### Exam 5 · Q47

**PayBridge, a digital banking company, has created a controlled API that lets approved personal finance apps retrieve customer transaction information. PayBridge wants to track API traffic, apply access control and security rules, and create pricing plans so external developers can be charged for using the API. Which Google Cloud solution should PayBridge use?**

- A. Apigee API Management
- B. Google Kubernetes Engine
- C. Spot VMs
- D. Cloud Run functions

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Apigee API Management

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

</details>

---

### Exam 6 · Q6

**MedLedger, a healthcare records company, wants to move several older applications from its private data center to Google Cloud. Each application was designed to run with its own dedicated operating system and cannot share the same OS environment with other applications. Which infrastructure solution should the company choose?**

- A. Virtual machines
- B. Open source software
- C. Serverless computing
- D. Containers

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Virtual machines

**Correct answer: A. Virtual machines**

Each virtual machine runs its own full guest operating system on top of a hypervisor. That gives every legacy application a dedicated OS, isolated from the others, which is exactly what the stem requires: apps that "cannot share the same OS environment." On Google Cloud, this means Compute Engine.

**Why the others are wrong:**
- **B. Open source software**: This is a licensing model for software, not an infrastructure choice.
- **C. Serverless computing**: You don't control the OS at all, and older apps often need changes to run serverless.
- **D. Containers**: Containers share the host's operating system kernel, which conflicts with the dedicated-OS requirement.

**Remember:** Dedicated OS per app → virtual machines. Shared OS kernel, lightweight → containers.

**References:**
- [docs.cloud.google.com/compute/docs/overview](https://docs.cloud.google.com/compute/docs/overview)
- [docs.cloud.google.com/compute/docs/instances](https://docs.cloud.google.com/compute/docs/instances)
- [cloud.google.com/discover/containers-vs-vms](https://cloud.google.com/discover/containers-vs-vms)

</details>

---

### Exam 6 · Q12

**ShopPulse, an ecommerce website, wants to analyze page load times, visitor behavior, clickstream events, and checkout performance by using BigQuery. However, the company does not want to move all of its data to Google Cloud and wants to keep part of its data in its own data center. Which environment should ShopPulse use?**

- A. Private cloud
- B. On-premises
- C. Multi-cloud
- D. Hybrid cloud

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Hybrid cloud

**Correct answer: D. Hybrid cloud**

A hybrid cloud combines on-premises infrastructure with public cloud services. ShopPulse wants to use BigQuery (a public cloud service) while keeping part of its data in its own data center. That mix of on-premises and cloud is the definition of hybrid.

**Why the others are wrong:**
- **A. Private cloud**: A private cloud is dedicated to one organization and would not, by itself, give access to BigQuery.
- **B. On-premises**: Staying fully on-premises means not using BigQuery in Google Cloud at all.
- **C. Multi-cloud**: Multi-cloud means using more than one public cloud provider. The stem mentions only Google Cloud and a private data center.

**Remember:** On-premises + one public cloud → hybrid. Several public clouds → multicloud.

**References:**
- [cloud.google.com/learn/what-is-hybrid-cloud](https://cloud.google.com/learn/what-is-hybrid-cloud)
- [cloud.google.com/hybrid-cloud](https://cloud.google.com/hybrid-cloud)
- [cloud.google.com/bigquery/docs/introduction](https://cloud.google.com/bigquery/docs/introduction)

</details>

---

### Exam 6 · Q21

**TrailCart, a growing grocery delivery website, wants to move its customer ordering platform to the cloud. The technical leadership team is worried that choosing one cloud provider could make future migration difficult if the business later wants to move workloads elsewhere. Which approach would best reduce this concern?**

- A. Open standards
- B. Database services
- C. Service level agreements
- D. Scalable infrastructure

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Open standards

**Correct answer: A. Open standards**

Vendor lock-in happens when an application depends on one provider's proprietary technology, making it hard to move. Open standards and open source tools, such as Kubernetes and containers, work across providers, so workloads stay portable. The clue is the worry that one provider "could make future migration difficult."

**Why the others are wrong:**
- **B. Database services**: Managed databases are useful, but proprietary ones can increase lock-in rather than reduce it.
- **C. Service level agreements**: SLAs define reliability commitments, not portability between providers.
- **D. Scalable infrastructure**: Scalability helps handle growth but does not make it easier to leave a provider.

**Remember:** Avoid lock-in → openness: open standards, open source, portable workloads.

**References:**
- [cloud.google.com/learn/what-is-multicloud](https://cloud.google.com/learn/what-is-multicloud)
- [docs.cloud.google.com/architecture/hybrid-multicloud-patterns/drivers](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/drivers)
- [cloud.google.com/architecture/framework](https://cloud.google.com/architecture/framework)

</details>

---

### Exam 6 · Q31

**ShopSwift runs a flash-sale app that needs to execute lightweight backend code whenever a product price drops below a chosen threshold. The team wants a serverless compute option that can automatically respond to events without managing servers or clusters. Which Google Cloud compute solution should ShopSwift use?**

- A. Google Kubernetes Engine
- B. Cloud Run functions
- C. Bare Metal Solution
- D. Compute Engine

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Cloud Run functions

**Correct answer: B. Cloud Run functions**

Cloud Run functions (formerly Cloud Functions) runs small pieces of code in response to events, such as a price change or a new file. It is serverless: there are no servers or clusters to manage, and you pay only when the code runs. The clues are "lightweight backend code," "automatically respond to events," and "without managing servers or clusters."

**Why the others are wrong:**
- **A. Google Kubernetes Engine**: GKE runs containers on clusters, which the stem explicitly wants to avoid managing.
- **C. Bare Metal Solution**: Dedicated physical servers for specialized workloads like Oracle databases. Not serverless.
- **D. Compute Engine**: Virtual machines that you must manage yourself.

**Remember:** Small code triggered by events, no servers → Cloud Run functions.

**References:**
- [cloud.google.com/functions](https://cloud.google.com/functions)
- [docs.cloud.google.com/run/docs/write-functions](https://docs.cloud.google.com/run/docs/write-functions)
- [docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)

</details>

---

### Exam 6 · Q44

**SecureVision Labs, a fraud detection company, wants to use advanced machine learning capabilities from Google Cloud to improve risk analysis. However, regulatory rules require customer transaction data to remain in the company’s own on-premises data center. Which approach should SecureVision Labs use?**

- A. A hybrid-cloud approach
- B. A multi-cloud approach
- C. A public-cloud approach
- D. A private-cloud approach

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. A hybrid-cloud approach

**Correct answer: A. A hybrid-cloud approach**

A hybrid cloud connects on-premises infrastructure with a public cloud. SecureVision can keep regulated transaction data in its own data center while still using Google Cloud's ML capabilities. The clues are "data to remain in the company's own on-premises data center" plus "advanced machine learning capabilities from Google Cloud."

**Why the others are wrong:**
- **B. Multi-cloud**: This means using several public cloud providers. The stem involves one cloud plus on-premises.
- **C. Public-cloud**: Moving fully to the public cloud would break the rule to keep data on-premises.
- **D. Private-cloud**: A private cloud alone would not give access to Google Cloud's ML services.

**Remember:** Data stays on-premises + Google Cloud services → hybrid.

**References:**
- [cloud.google.com/learn/what-is-hybrid-cloud](https://cloud.google.com/learn/what-is-hybrid-cloud)
- [docs.cloud.google.com/architecture/deployment-archetypes/hybrid](https://docs.cloud.google.com/architecture/deployment-archetypes/hybrid)
- [cloud.google.com/distributed-cloud](https://cloud.google.com/distributed-cloud)

</details>

---

### Exam 6 · Q48

**BrightPulse Rewards, a mobile loyalty app, receives several petabytes of customer activity records, partner campaign logs, and purchase events from systems running on Google Cloud and on two other public cloud providers. The leadership team wants to bring these data sources together across providers so analysts can generate insights for long-term planning and business decisions. What type of environment should BrightPulse Rewards use?**

- A. Multi cloud environment
- B. Virtual machine environment
- C. Hybrid cloud environment
- D. Container environment

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Multi cloud environment

**Correct answer: A. Multi cloud environment**

BrightPulse runs on Google Cloud, but some of its data lives with two other public cloud providers. Using services from more than one public cloud provider is a multicloud environment. Google supports this with tools that work across clouds, such as BigQuery Omni for analyzing data where it sits and Looker for BI across sources.

**Why the others are wrong:**
- **B. Virtual machine environment**: VMs are a compute choice. They say nothing about combining data across providers.
- **C. Hybrid cloud environment**: Hybrid means on-premises or private infrastructure plus public cloud. Here every source is a public cloud.
- **D. Container environment**: Containers package applications. They don't define where data from different providers lives.

**Remember:** Several public clouds → multicloud. On-premises + public cloud → hybrid.

**References:**
- [cloud.google.com/architecture/framework/system-design/compute](https://cloud.google.com/architecture/framework/system-design/compute)
- [cloud.google.com/discover/what-is-multicloud](https://cloud.google.com/discover/what-is-multicloud)
- [cloud.google.com/bigquery/docs/introduction](https://cloud.google.com/bigquery/docs/introduction)

</details>

---
