# Domain 1 — Digital Transformation with Google Cloud

28 questions. Answers are collapsed — try each question before expanding it.

## Questions

### Exam 1 · Q8

**GlobeFleet Logistics, a transportation company with offices in several countries, wants to move from its aging data centers to public cloud services. What is one benefit GlobeFleet Logistics can gain from using the public cloud?**

- A. It can schedule physical server repairs after office hours.
- B. It can receive guaranteed 100% availability for every cloud service in every region.
- C. It no longer needs security controls when moving data to the cloud.
- D. It can access data and computing resources without being limited to one physical location.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. It can access data and computing resources without being limited to one physical location.

**Correct answer: D. It can access data and computing resources without being limited to one physical location.**

Public cloud resources are reachable over the internet from anywhere, and they run in Google's global network of regions. A company with offices in several countries can serve all of them without owning a data center near each office. The clue is "offices in several countries" moving off "aging data centers".

**Why the others are wrong:**
- **A. Schedule physical server repairs after office hours**: in the public cloud the provider handles physical hardware; the customer does not repair servers.
- **B. Guaranteed 100% availability**: no cloud provider guarantees 100% availability; SLAs set targets such as 99.9% or 99.99%.
- **C. No longer needs security controls**: under the shared responsibility model the customer still secures its data, access and configuration.

**Remember:** Public cloud = global reach, on-demand resources, no hardware to maintain. Never 100% uptime and never zero customer security work.

</details>

---

### Exam 1 · Q29

**SunriseMart, a regional grocery chain, wants to move from running most applications in its own data center to using cloud services. The company wants to understand how this move can help its teams create more business value over time. How does switching from on-premises infrastructure to the cloud help SunriseMart gain value over time?**

- A. They can expand their internal application hosting infrastructure
- B. They can focus their efforts on solution development
- C. They can increase development of data recovery systems
- D. They can relax their on-premises data security protocols

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. They can focus their efforts on solution development

**Correct answer: B. They can focus their efforts on solution development**

In the cloud, the provider runs the hardware, data centers and much of the platform. SunriseMart's teams spend less time on infrastructure and more time building solutions that create business value. The clue is "create more business value over time".

**Why the others are wrong:**
- **A. Expand internal hosting infrastructure**: moving to the cloud reduces the need for internal infrastructure.
- **C. Increase development of data recovery systems**: the cloud offers managed backup and recovery, so teams build less of this themselves.
- **D. Relax data security protocols**: security remains a shared responsibility; the company still protects its data and access.

**Remember:** Cloud = less undifferentiated infrastructure work, more focus on what makes the business unique.

</details>

---

### Exam 2 · Q1

**TalentHive HR wants to use an online payroll and employee benefits application provided by a cloud vendor. The company does not want to manage servers, install platform software, or develop the application code itself. Which cloud service model does this represent?**

- A. Infrastructure as a service
- B. Platform as a service
- C. Software as a service
- D. Functions as a service

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Software as a service

**Correct answer: C. Software as a service**

TalentHive uses a finished application from a vendor. It does not manage servers, platform software, or code. In SaaS the provider runs everything, and the customer just uses the app and manages its own data and users. The clue is "does not want to … develop the application code itself".

**Why the others are wrong:**
- **A. Infrastructure as a service**: IaaS gives you virtual machines and networks, and you still manage the OS, platform, and app.
- **B. Platform as a service**: PaaS removes server management, but you still write and deploy your own application code.
- **D. Functions as a service**: FaaS runs code you write in response to events; TalentHive wants a ready-made app, not code.

**Remember:** Ready-made app you just log in to = SaaS; your code on managed platform = PaaS; your VMs = IaaS.

</details>

---

### Exam 2 · Q3

**RidePulse, a bike-sharing mobile app, is gaining users faster than expected. Its main application still runs on older company-owned infrastructure, and the operations team is finding it difficult and expensive to scale capacity for traffic spikes. What might be limiting RidePulse’s ability to keep up with application growth?**

- A. The time it takes their serverless compute function to scale
- B. The overreliance on platform as a service
- C. The inaccessibility of their data due to perimeter security
- D. The cost of provisioning hardware for peak usage

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. The cost of provisioning hardware for peak usage

**Correct answer: D. The cost of provisioning hardware for peak usage**

With on-premises infrastructure, a company must buy and install enough hardware for its highest traffic peak. That is slow and expensive, and the extra capacity sits idle the rest of the time. The clue is "older company-owned infrastructure" that is "difficult and expensive to scale". Cloud solves this with on-demand, elastic capacity.

**Why the others are wrong:**
- **A. Serverless scaling time**: RidePulse is not using serverless; its app runs on its own hardware.
- **B. Overreliance on platform as a service**: PaaS is a cloud model, and RidePulse still runs on company-owned infrastructure.
- **C. Data inaccessible due to perimeter security**: Security design does not explain why capacity is hard and expensive to scale.

**Remember:** On-premises = buy for the peak in advance; cloud = scale on demand and pay for what you use.

</details>

---

### Exam 2 · Q4

**FreshBite Logistics has moved its inventory tracking system from its private data center to Google Cloud. The finance team wants to understand how this migration changes the way infrastructure spending is managed. How has cost management primarily been affected?**

- A. Costs will primarily shift from CapEx to OpEx.
- B. Costs will primarily shift from OpEx to CapEx.
- C. Cost management will stay the same, but the total cost of ownership (TCO) will be lower.
- D. Cost management will stay the same, but the total cost of ownership (TCO) will be higher.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Costs will primarily shift from CapEx to OpEx.

**Correct answer: A. Costs will primarily shift from CapEx to OpEx.**

In a private data center, the company buys servers and buildings up front, which is capital expenditure (CapEx). In the cloud, it pays for resources as it uses them, which is operating expenditure (OpEx). The question asks how the way spending is managed changes, and the main change is this shift to pay-as-you-go.

**Why the others are wrong:**
- **B. OpEx to CapEx**: This is the reverse; moving to the cloud reduces up-front capital purchases.
- **C. Same management, lower TCO**: TCO may drop, but cost management does change: from buying assets to paying for usage.
- **D. Same management, higher TCO**: Cost management changes, and the cloud is not assumed to raise TCO.

**Remember:** Moving to the cloud = CapEx (buy up front) becomes OpEx (pay as you go).

</details>

---

### Exam 2 · Q7

**CityPetCare, a veterinary appointment website, decides to launch a mobile app so pet owners can check appointment details, vaccination reminders, and service updates while they are away from their computers. What business reason most likely led CityPetCare to create the mobile app?**

- A. Customers expect service information to be simple to access from any device.
- B. Customers expect cloud-based information to be available only through mobile devices.
- C. Developers can make customer data more secure only by using a mobile app.
- D. Developers can test different versions of the service only through a mobile app.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Customers expect service information to be simple to access from any device.

**Correct answer: A. Customers expect service information to be simple to access from any device.**

Modern customers expect to reach services anytime, anywhere, on whatever device they have. A mobile app lets pet owners see appointments and reminders while away from their computers. The clue is "while they are away from their computers".

**Why the others are wrong:**
- **B. Only through mobile devices**: Customers want access from any device, not only mobile; the website still exists.
- **C. Only a mobile app makes data secure**: Security does not depend on using a mobile app.
- **D. Testing only through a mobile app**: Developers can test versions on many platforms, and testing is not the business reason here.

**Remember:** Customer expectations drive transformation: access anywhere, on any device.

</details>

---

### Exam 2 · Q22

**FitLoop, a fitness coaching startup, uses a cloud-based SaaS application to publish workout plans and nutrition tips for its subscribers. The SaaS provider manages the application platform and the infrastructure behind it. What is FitLoop exclusively responsible for?**

- A. Keeping the complete SaaS platform operational
- B. Maintaining customer-facing content
- C. Monitoring data center servers
- D. Monitoring underlying computer networks

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Maintaining customer-facing content

**Correct answer: B. Maintaining customer-facing content**

In SaaS, the provider runs the application, platform, servers, and networks. The customer is still responsible for its own data and content, such as the workout plans and tips FitLoop publishes. This is the shared responsibility model.

**Why the others are wrong:**
- **A. Keeping the SaaS platform operational**: Running the platform is the SaaS provider's job.
- **C. Monitoring data center servers**: The provider manages the physical servers.
- **D. Monitoring computer networks**: Underlying networks are also managed by the provider.

**Remember:** In SaaS, the customer always owns its data, content, and user access.

</details>

---

### Exam 2 · Q39

**GreenTrail, a regional travel booking company, is adopting cloud services, analytics, and automation to redesign internal workflows, improve collaboration, create better traveler experiences, and respond faster to changing customer demand. What is this approach called?**

- A. Digital transformation
- B. Data center migration
- C. Operations optimization
- D. User personalization

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Digital transformation

**Correct answer: A. Digital transformation**

Digital transformation means using modern digital technologies, like cloud, analytics, and automation, to change how a business works and delivers value to customers. GreenTrail is changing workflows, collaboration, and customer experience, not just one system. The breadth of change is the clue.

**Why the others are wrong:**
- **B. Data center migration**: Migration moves infrastructure; it does not by itself redesign workflows and customer experience.
- **C. Operations optimization**: This is only one part of what GreenTrail is doing.
- **D. User personalization**: Personalization is one possible outcome, not the overall approach.

**Remember:** Using technology to rethink processes, culture, and customer experience → digital transformation.

</details>

---

### Exam 3 · Q2

**NorthPeak Logistics is moving toward Google Cloud and wants its internal IT team to develop strong cloud skills as part of a long-term business transformation. Leadership wants employees to learn from trusted Google Cloud training content while also sharing knowledge across teams. What should NorthPeak Logistics do?**

- A. Focus on training existing employees instead of hiring new employees who already have cloud experience.
- B. Give elevated access to third-party consultants and contractors so they can cover internal IT knowledge gaps.
- C. Encourage self-directed, separate learning using official training materials.
- D. Build a culture of continuous peer-to-peer learning using official training materials.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Build a culture of continuous peer-to-peer learning using official training materials.

**Correct answer: D. Build a culture of continuous peer-to-peer learning using official training materials.**

The stem has two clues: learn from trusted Google Cloud content, and share knowledge across teams. Peer-to-peer learning built on official training covers both. Transformation is about people and culture, not only technology, so a lasting learning culture is the goal.

**Why the others are wrong:**
- **A. Train existing staff instead of hiring**: Training staff is good, but this option says nothing about official content or sharing knowledge.
- **B. Give elevated access to consultants**: It outsources knowledge instead of building internal skills and weakens least privilege.
- **C. Self-directed, separate learning**: It uses official materials but misses the knowledge-sharing part.

**Remember:** Upskilling for transformation = official training + a culture of sharing.

</details>

---

### Exam 3 · Q22

**Northstar Clinics runs some sensitive patient-management systems in its own private data center, but it also wants to use Google Cloud services for analytics, application scaling, and newer digital services. The company wants an architecture that lets it use both environments together. What kind of architecture does a hybrid cloud offer Northstar Clinics?**

- A. A combination of different virtualized servers
- B. A combination of serverless computing and public cloud services
- C. A combination of private cloud infrastructure and public cloud services
- D. A combination of multiple public cloud provider services

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. A combination of private cloud infrastructure and public cloud services

**Correct answer: C. A combination of private cloud infrastructure and public cloud services**

Hybrid cloud combines on-premises or private cloud infrastructure with public cloud services, working together. Northstar keeps sensitive systems in its own data center and uses Google Cloud for analytics and new services, which is hybrid.

**Why the others are wrong:**
- **A. Different virtualized servers**: Virtualization alone doesn't make an architecture hybrid.
- **B. Serverless plus public cloud**: Serverless runs in the public cloud, so this is just public cloud.
- **D. Multiple public cloud providers**: That is multicloud, not hybrid.

**Remember:** Hybrid = on-prem/private + public. Multicloud = more than one public cloud.

</details>

---

### Exam 3 · Q29

**BrightBasket, an online grocery marketplace, uses traditional technology to host its ecommerce website. During holiday sales, the company often buys too much capacity or does not have enough capacity for sudden traffic spikes. BrightBasket has decided to move its website to cloud technology. What aspect of cloud technology will benefit BrightBasket’s ecommerce business?**

- A. Agile infrastructure means that they only pay for what they need, when they need it.
- B. Operational expenditure means that their total cost of ownership is more predictable.
- C. Unlimited storage means that their website will never experience downtime.
- D. Shared responsibility means that the cloud provider gives increased visibility during traffic spikes.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Agile infrastructure means that they only pay for what they need, when they need it.

**Correct answer: A. Agile infrastructure means that they only pay for what they need, when they need it.**

The problem is buying too much capacity or too little for traffic spikes. Cloud resources scale up and down with demand, and you pay only for what you use. That removes the need to guess capacity in advance.

**Why the others are wrong:**
- **B. OpEx makes TCO more predictable**: Pay-per-use costs can vary more, and OpEx doesn't solve the capacity problem.
- **C. Unlimited storage means no downtime**: Storage has nothing to do with downtime, and no system has zero downtime.
- **D. Shared responsibility gives visibility during spikes**: Shared responsibility splits security duties; it isn't about visibility or traffic.

**Remember:** Over- or under-provisioning problem = elastic scaling + pay for what you use.

**⚠️ Note:** "Agile infrastructure" is loose wording. The real ideas are elasticity and consumption-based pricing. It is still the best of the options, so pick it on this exam.

</details>

---

### Exam 3 · Q32

**QuickServeNow runs a food delivery mobile app from its own data center. The company is moving the app to Google Cloud so it can reduce hardware management and scale more easily. After the migration, which change will QuickServeNow need to adapt to?**

- A. Paying compensation for Google Cloud service outages
- B. Managing Google Cloud’s underlying network infrastructure
- C. Adjusting to a consumption-based pay-as-you-go spending model
- D. Optimizing the physical storage systems that run Google Cloud

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Adjusting to a consumption-based pay-as-you-go spending model

**Correct answer: C. Adjusting to a consumption-based pay-as-you-go spending model**

On premises, QuickServeNow bought hardware up front. On Google Cloud it pays for what it uses each month, so costs now go up and down with usage. Finance and engineering teams have to adapt: track spending continuously, set budgets and alerts, and design for cost as well as performance.

**Why the others are wrong:**
- **A. Paying compensation for outages**: The provider gives service credits under its SLA. The customer never pays for the provider's outages.
- **B. Managing Google's network**: Google runs its own network infrastructure.
- **D. Optimizing Google's physical storage**: The physical hardware is Google's responsibility.

**Remember:** Moving to cloud = CapEx up front becomes OpEx pay-as-you-go, and the business must learn to manage variable spending.

</details>

---

### Exam 4 · Q16

**CareNest, a healthcare support app, has received customer feedback that patients need help outside regular business hours. The company decides to extend its phone support availability into evenings and weekends. Why is CareNest making this change?**

- A. Users expect professional expertise
- B. Users require personalization
- C. Users expect always-on services
- D. Users require regional access

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Users expect always-on services

**Correct answer: C. Users expect always-on services**

Modern customers expect help and services to be available whenever they need them, not only in office hours. Extending support into evenings and weekends responds directly to that. The clue is "outside regular business hours".

**Why the others are wrong:**
- **A. Professional expertise**: The feedback is about when support is available, not the skill of the staff.
- **B. Personalization**: Personalization means tailoring to each user, which the change doesn't address.
- **D. Regional access**: The issue is time of day, not geographic location.

**Remember:** "Evenings and weekends", "24/7" → always-on expectations.

</details>

---

### Exam 4 · Q21

**PageVerse, a digital library startup, wants to scan and publish thousands of archived newspapers, letters, and photographs so researchers can access them online. Why is a public cloud a better choice than hosting everything in the company’s own data center?**

- A. It requires the company to manage more in-house hardware
- B. It provides a dedicated physical encryption key by default
- C. It is cost-effective when storing and serving data at large scale
- D. It focuses mainly on increasing capital expenditure

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. It is cost-effective when storing and serving data at large scale

**Correct answer: C. It is cost-effective when storing and serving data at large scale**

Public cloud gives near-unlimited storage and global delivery on a pay-as-you-go basis. PageVerse can store and serve large volumes of scans without buying and running its own hardware. Costs grow with use instead of requiring big upfront purchases.

**Why the others are wrong:**
- **A. More in-house hardware**: Public cloud reduces the hardware a company must manage.
- **B. Dedicated physical encryption key**: Data is encrypted by default, but not with a dedicated physical key per customer.
- **D. Increasing capital expenditure**: Cloud shifts spending away from CapEx toward OpEx.

**Remember:** Large-scale storage and delivery without buying hardware → public cloud.

</details>

---

### Exam 4 · Q27

**BrightCart, an online grocery company, is moving its internal order processing and inventory applications from its own data center to the cloud. How could this move affect the company’s operations and personnel costs?**

- A. Reduced on-premises infrastructure management costs
- B. Increased on-premises hardware maintenance costs
- C. Reduced cloud software licensing costs
- D. Increased cloud hardware management costs

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Reduced on-premises infrastructure management costs

**Correct answer: A. Reduced on-premises infrastructure management costs**

When applications move to the cloud, Google runs the physical hardware, power, cooling and much of the maintenance. The company spends less time and money managing its own servers. Staff can then shift from upkeep to work that adds business value.

**Why the others are wrong:**
- **B. Increased on-premises maintenance**: Moving out of the data center reduces on-premises maintenance.
- **C. Reduced cloud software licensing**: Licensing costs are not the main effect, and they don't necessarily go down.
- **D. Increased cloud hardware management**: The customer doesn't manage cloud hardware; Google does.

**Remember:** Moving to cloud → less infrastructure management for your own team.

</details>

---

### Exam 4 · Q29

**FreshCart Lane, a regional grocery delivery website, is replacing its owned data center equipment with Google Cloud services. The finance team wants to understand how this move usually changes the way the company pays for IT. How does the company’s IT spending generally shift when FreshCart Lane adopts cloud technology?**

- A. Away from cost management toward capital expenditure
- B. Away from operational expenditure toward cost management
- C. Away from capital expenditure toward operational expenditure
- D. Away from operational expenditure toward capital expenditure

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Away from capital expenditure toward operational expenditure

**Correct answer: C. Away from capital expenditure toward operational expenditure**

On premises, a company buys servers and data center equipment up front. That is capital expenditure (CapEx). In the cloud it rents capacity and pays monthly for what it uses, which is operational expenditure (OpEx). So moving to Google Cloud shifts IT spending from CapEx toward OpEx.

**Why the others are wrong:**
- **A. Cost management → CapEx**: Cost management isn't a spending model, and cloud moves away from CapEx, not toward it.
- **B. OpEx → cost management**: Cloud increases OpEx. It doesn't move away from it.
- **D. OpEx → CapEx**: This is exactly backwards.

**Remember:** Cloud migration = CapEx → OpEx.

</details>

---

### Exam 4 · Q31

**GreenNest Retail maintains its inventory and analytics applications on servers in its own office data center. Its development team is unhappy because provisioning environments is slow, scaling is difficult, and experimentation is limited by fixed hardware capacity. How would moving to Google Cloud help the developers?**

- A. They can expect 100% service availability.
- B. They can avoid the limitations of serverless computing.
- C. They can have new tools to innovate and optimize resource usage.
- D. They can optimize maintenance for their on-premises infrastructure.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. They can have new tools to innovate and optimize resource usage.

**Correct answer: C. They can have new tools to innovate and optimize resource usage.**

The cloud lets developers create environments in minutes, scale on demand and use managed services and new tools. They pay only for what they use, so experiments are cheap and resources aren't wasted. This removes the slow provisioning and fixed capacity limits in the stem.

**Why the others are wrong:**
- **A. 100% availability**: No cloud provider guarantees 100% availability.
- **B. Avoid serverless limitations**: Serverless is one of the cloud tools developers gain, not something they escape.
- **D. Optimize on-premises maintenance**: The move is away from on-premises, so this doesn't help developers.

**Remember:** Slow provisioning and fixed capacity → cloud gives on-demand tools and elastic resources.

</details>

---

### Exam 4 · Q32

**TravelNest, an online hotel booking platform, runs its main web application from a Google Cloud region in Western Europe. Users in Singapore and Japan say pages take longer to load, even though their internet speed tests show high download and upload speeds. What is the most likely cause?**

- A. Too few application servers
- B. Insufficient network bandwidth
- C. Network latency
- D. Incorrectly configured application servers

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Network latency

**Correct answer: C. Network latency**

Latency is the delay for data to travel between the user and the server. Users in Asia reaching a region in Western Europe face long physical distance, so each request takes longer. Their high speed-test results show bandwidth is fine; distance is the problem.

**Why the others are wrong:**
- **A. Too few servers**: Users near Europe would also suffer if capacity were short; the issue here is location.
- **B. Insufficient bandwidth**: Speed tests show high bandwidth, which rules this out.
- **D. Misconfigured servers**: A configuration problem would affect all users, not just distant ones.

**Remember:** Fast connection but slow pages for distant users → latency (distance).

</details>

---

### Exam 4 · Q33

**FitTrackly, a fitness coaching website, is moving from its on-premises systems to Google Cloud. The leadership team wants to understand what this move means beyond simply changing where applications run. What does adopting cloud computing mainly represent for the company’s transformation?**

- A. A change that benefits only very large organizations
- B. A chance to redesign current business processes and services
- C. A change that matters only to the IT team
- D. A way to keep the same business model while only reducing costs

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. A chance to redesign current business processes and services

**Correct answer: B. A chance to redesign current business processes and services**

Digital transformation is more than moving servers. The cloud gives companies the chance to rethink how they work, serve customers and create new products. Leadership is asking about "beyond simply changing where applications run", which is this idea.

**Why the others are wrong:**
- **A. Only large organizations**: Cloud benefits organizations of every size, including small startups.
- **C. Only the IT team**: Transformation affects the whole business, not just IT.
- **D. Same model, only lower costs**: Cost savings alone miss the main point of transformation.

**Remember:** Cloud transformation = rethinking the business, not just relocating IT.

</details>

---

### Exam 4 · Q37

**PuzzleRift Games is modernizing its multiplayer arcade platform so the game backend can run on Google Cloud instead of company-owned servers in its office data center. What should PuzzleRift Games generally expect when moving from traditional on-premises technology to cloud technology?**

- A. No change to existing responsibilities
- B. A shift toward OpEx
- C. A shift toward using structured data
- D. Increased hardware maintenance

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. A shift toward OpEx

**Correct answer: B. A shift toward OpEx**

On-premises technology needs upfront capital spending on servers and facilities. In the cloud, the company pays for resources as it uses them, which is operational expenditure. This is the main financial change when moving to the cloud.

**Why the others are wrong:**
- **A. No change to responsibilities**: Responsibilities change: Google takes over the physical infrastructure.
- **C. Shift toward structured data**: Moving to the cloud doesn't change the type of data a business has.
- **D. Increased hardware maintenance**: Hardware maintenance goes down because Google handles it.

**Remember:** On-premises → cloud = CapEx → OpEx.

</details>

---

### Exam 4 · Q41

**StreamNest Media hosts its video preview application in one Google Cloud region in Germany. Many users in the United States are experiencing high latency when opening the application. The company wants to improve the user experience for those U.S. customers. What should StreamNest Media do?**

- A. Create a separate billing account for users in the United States.
- B. Deploy the application across more zones in the same German region.
- C. Deploy the application across more regions in Europe.
- D. Deploy a replica of the application in a region in the United States.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Deploy a replica of the application in a region in the United States.

**Correct answer: D. Deploy a replica of the application in a region in the United States.**

Latency comes from physical distance between users and the servers. Running a copy of the app in a U.S. region puts it close to U.S. users, which cuts the delay. Google Cloud's global regions make this possible.

**Why the others are wrong:**
- **A. Separate billing account**: Billing has no effect on network performance.
- **B. More zones in Germany**: Zones help availability, but the app is still far from U.S. users.
- **C. More regions in Europe**: Europe is still far from the United States.

**Remember:** Distant users with high latency → deploy closer to them, in their region.

</details>

---

### Exam 4 · Q44

**BrightCart, an ecommerce website, is comparing Google Cloud’s infrastructure approach with traditional off-the-shelf server hardware. The infrastructure team learns that Google uses purpose-built servers in its data centers. What is one main benefit of these purpose-built servers compared with standard servers?**

- A. They are optimized for specific tasks, making them more efficient.
- B. They are backward compatible with legacy disk drives.
- C. They are cheaper to build than standard servers.
- D. They run software that cannot be deployed on standard servers.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. They are optimized for specific tasks, making them more efficient.

**Correct answer: A. They are optimized for specific tasks, making them more efficient.**

Google designs its own servers and data centers for its workloads, leaving out parts it doesn't need. This makes them more efficient in performance and energy use, and it reduces the attack surface. The clue is "purpose-built".

**Why the others are wrong:**
- **B. Backward compatible with legacy disks**: Compatibility with old hardware isn't the goal of custom servers.
- **C. Cheaper to build**: The main benefit stated is efficiency, not a lower build cost per server.
- **D. Software that can't run elsewhere**: Google Cloud runs standard software such as Linux and containers.

**Remember:** Purpose-built = optimized for the task = more efficient.

</details>

---

### Exam 4 · Q49

**BrightTrail Foods runs an order-tracking website from its own data center and is planning to migrate the application to Google Cloud. The leadership team wants to compare the long-term financial impact of continuing on-premises operations with the expected cost and business value of using cloud services. Why should the team review total cost of ownership before migration?**

- A. To evaluate error budget
- B. To understand service level availability
- C. To evaluate return on investment
- D. To calculate required compute power

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. To evaluate return on investment

**Correct answer: C. To evaluate return on investment**

Total cost of ownership (TCO) counts all costs over time, including hardware, staff, facilities and licenses. Comparing on-premises TCO with cloud costs and expected business value shows the return on investment of migrating. The clue is "long-term financial impact" and "business value".

**Why the others are wrong:**
- **A. Evaluate error budget**: Error budget is an SRE reliability concept, not a financial comparison.
- **B. Service level availability**: Availability is a reliability measure, not a cost analysis.
- **D. Required compute power**: Sizing compute is a technical planning task, not the purpose of TCO.

**Remember:** TCO comparison → informs ROI and the business case for migration.

</details>

---

### Exam 5 · Q28

**ShopNest has already migrated a few small applications to Google Cloud to reduce short-term costs. The leadership team now wants cloud adoption to become a company-wide transformation that supports innovation and faster delivery. How should the organization adapt its leadership approach?**

- A. Increase visible top-down sponsorship and foster a culture of blamelessness
- B. Move cloud funding from an operational expenditure model to capital expenditure
- C. Make cloud adoption primarily driven by individual contributors
- D. Invest in on-premises infrastructure to redefine relationships between IT and employees

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Increase visible top-down sponsorship and foster a culture of blamelessness

**Correct answer: A. Increase visible top-down sponsorship and foster a culture of blamelessness**

Moving from a few cost-saving migrations to a real transformation needs strong executive support and a culture where people can experiment. A blameless culture lets teams learn from failures instead of hiding them, which drives innovation and faster delivery. The clue is "company-wide transformation".

**Why the others are wrong:**
- **B. Move funding from OpEx to CapEx**: cloud moves spending the other way, toward OpEx.
- **C. Driven mainly by individual contributors**: bottom-up effort alone can't change a whole company.
- **D. Invest in on-premises infrastructure**: this goes against cloud adoption.

**Remember:** Transformation = executive sponsorship + blameless, learning culture.

</details>

---

### Exam 6 · Q11

**PhotoNest, a photo editing web app, wants to rent virtual machines, storage, and networking from a cloud provider so its engineers can build and configure customized servers. The company prefers paying only for the resources it uses instead of buying physical hardware upfront. Which cloud service model should PhotoNest use?**

- A. Hybrid cloud
- B. Software as a service
- C. Infrastructure as a service
- D. Platform as a service

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Infrastructure as a service

**Correct answer: C. Infrastructure as a service**

IaaS provides the basic building blocks: virtual machines, storage, and networking, rented on a pay-as-you-go basis. The customer still configures and manages the operating systems and software on top. The clues are "rent virtual machines, storage, and networking" and "build and configure customized servers." Compute Engine is the typical Google Cloud example.

**Why the others are wrong:**
- **A. Hybrid cloud**: This is a deployment model (on-premises plus cloud), not a service model.
- **B. Software as a service**: SaaS delivers a finished application, with no servers to configure.
- **D. Platform as a service**: PaaS hides the servers so developers just deploy code, which is the opposite of building custom servers.

**Remember:** Rent VMs, storage, network → IaaS. Deploy code, no servers → PaaS. Ready-made app → SaaS.

</details>

---

### Exam 6 · Q13

**MetroHire, a job-matching web application, wants to deploy its custom application in Google Cloud. The development team needs the application to scale as user traffic changes, but they do not want to manage servers, operating systems, or underlying infrastructure. Which service model should MetroHire use?**

- A. Infrastructure as a service
- B. Platform as a service
- C. Software as a service
- D. Network as a service

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Platform as a service

**Correct answer: B. Platform as a service**

With PaaS, developers deploy their own application code, and the provider manages the servers, operating systems, and scaling. The clues are "deploy its custom application" and "do not want to manage servers, operating systems, or underlying infrastructure." Google Cloud examples include App Engine and Cloud Run.

**Why the others are wrong:**
- **A. Infrastructure as a service**: IaaS still requires the customer to manage VMs and operating systems.
- **C. Software as a service**: SaaS delivers a ready-made application. MetroHire wants to run its own custom app.
- **D. Network as a service**: This is about renting network capabilities, not hosting an application.

**Remember:** Your own code + no server management → PaaS.

</details>

---

### Exam 6 · Q15

**PixelCart Market, an online shopping website, runs its main application from servers in its own data center. During holiday sales, many customers visit the website at the same time, and the application often becomes unavailable. What is the most likely reason for this problem?**

- A. A serverless compute function is unable to scale properly.
- B. The application contains inconsistent customer data.
- C. The company does not have enough servers to handle the traffic.
- D. The application can only be configured in an on-premises environment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. The company does not have enough servers to handle the traffic.

**Correct answer: C. The company does not have enough servers to handle the traffic.**

An on-premises data center has a fixed amount of hardware. When holiday traffic exceeds that capacity, the application slows down or becomes unavailable. Adding servers takes time and money, so the company cannot react to short spikes. The clue is "many customers visit at the same time" with servers "in its own data center."

**Why the others are wrong:**
- **A. A serverless function cannot scale**: The app runs on the company's own servers, not on serverless, and serverless scales automatically.
- **B. Inconsistent customer data**: Data quality problems cause wrong results, not outages during traffic peaks.
- **D. Can only be configured on-premises**: This says nothing about why the app fails under load.

**Remember:** On-premises scaling pain = not enough servers for the peak, and adding more is slow and costly.

</details>

---

### Exam 6 · Q35

**DataBridge Finance, a payment analytics company, runs several customer-facing applications in its own data center. As customer traffic grows, the company needs more compute capacity, but adding new servers requires purchasing hardware, setting it up, configuring it, and maintaining it. Why does DataBridge Finance often struggle to scale this on-premises application infrastructure?**

- A. Scaling compute instances could breach compliance and/or regulation
- B. Increasing compute capacity is time-consuming and costly
- C. Their serverless compute functions struggle to meet the demand
- D. Their multi-cloud architecture is complex and expensive

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Increasing compute capacity is time-consuming and costly

**Correct answer: B. Increasing compute capacity is time-consuming and costly**

On-premises, every new server must be bought, delivered, installed, configured, and maintained. That takes weeks or months and large upfront spending. The stem lists exactly these steps: "purchasing hardware, setting it up, configuring it, and maintaining it." The cloud removes this delay by offering capacity on demand.

**Why the others are wrong:**
- **A. Scaling could breach compliance**: Adding servers is not normally a compliance problem, and the stem says nothing about regulation.
- **C. Serverless functions struggle**: The company runs its own data center servers, not serverless functions.
- **D. Multi-cloud complexity**: The company is fully on-premises, not using multiple clouds.

**Remember:** On-premises scaling = slow and costly to add capacity.

</details>

---
